---
nav_title: Messages in-app
article_title: Messages in-app pour Flutter
platform: Flutter
page_order: 4
page_type: reference
description: "Cet article couvre les messages in-app des applications pour iOS et Android utilisant Flutter, y compris l’analytique de la personnalisation et de la journalisation."
channel: messages in-app

---

# Messages in-app

Les messages in-app natifs s’affichent automatiquement sur Android et iOS lors de l’utilisation de Flutter. Cet article couvre différentes options de personnalisation pour les messages in-app.

## Analytique

Pour enregistrer l’analytique à l’aide de votre `BrazeInAppMessage`, passez l’instance dans la fonction d’analytique souhaitée :
- `logInAppMessageClicked`
- `logInAppMessageImpression`
- `logInAppMessageButtonClicked` (avec l’index des boutons)

Par exemple :
```dart
// Journaliser un clic
braze.logInAppMessageClicked(inAppMessage);
// Journaliser une impression
braze.logInAppMessageImpression(inAppMessage);
// Index de bouton de journalisation `0` cliqué
braze.logInAppMessageButtonClicked(inAppMessage, 0);
```

## Désactiver l’affichage automatique

Pour désactiver l’affichage automatique des messages in-app, effectuez ces mises à jour dans la couche native.

{% tabs %}
{% tab Android %}

1. Assurez-vous d’utiliser l’initiateur d’intégration automatique, activé par défaut à partir de la version `2.2.0`.
2. Définissez l’opération par défaut de message in-app `DISCARD` en ajoutant la ligne suivante à votre fichier `braze.xml`.

```xml
<string name="com_braze_flutter_automatic_integration_iam_operation">SUPPRIMER</string>
```

{% endtab %}
{% tab iOS %}

1. Implémentez le délégué `BrazeInAppMessageUIDelegate` comme décrit dans notre [article iOS ici](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui).

2. Mettez à jour votre méthode de délégué `inAppMessage(_:displayChoiceForMessage:)` pour qu’elle retourne `.discard`.

Consultez [AppDelegate.swift](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/ios/Runner/AppDelegate.swift) dans notre exemple d’application pour en avoir un exemple.

{% endtab %}
{% endtabs %}

## Réception des données de message in-app

Pour recevoir des données dans le mesage in-app dans votre appli Flutter, le `BrazePlugin` est compatible avec l’envoi de données dans un message in-app à l’aide de [Dart Streams](https://dart.dev/tutorials/language/streams) (recommandé) ou en utilisant une fonction de rappel de données (hérité).

L’objet `BrazeInAppMessage` prend en charge un sous-ensemble de champs disponibles dans les objets du modèle natif, y compris `uri`, `message`, `header`, `buttons`, `extras` et plus encore.

{% alert note %} La méthode de fonction de rappel de données héritées sera bientôt déconseillée. Il est possible d’ajouter des messages in-app aux flux de données et aux fonctions de rappel de données. SI vous avez déjà des fonctions de rappel de données intégrées et souhaitez utiliser des flux de données, supprimez toute logique de fonction de rappel pour garantir que les messages in-app sont traités exactement une seule fois. {% endalert %}

### Méthode 1  : Flux de données de message in-app (recommandée)

Vous pouvez définir une fonction de rappel dans Dart pour recevoir les données du message in-app dans votre application Flutter.

Pour commencer à écouter le flux, utilisez le code ci-dessous pour créer un `StreamSubscription` dans votre appli Flutter et appelez la méthode `subscribeToInAppMessages()` avec une fonction prenant l’instance `BrazeInAppMessage`. N’oubliez pas de `cancel()` l’abonnement au flux lorsqu’il n’est plus nécessaire.

```dart
// Créer un abonnement au flux
StreamSubscription inAppMessageStreamSubscription;

inAppMessageStreamSubscription = _braze.subscribeToInAppMessages((BrazeInAppMessage inAppMessage) {
  // Fonctionnalité de gestion des messages in-app
}

// Annuler un abonnement au flux
inAppMessageStreamSubscription.cancel();
```

Consultez [main.dart](https://github.com/Appboy/flutter-sdk/blob/develop/braze_plugin/example/lib/main.dart) dans votre exemple d’application.

### Méthode 2 : Fonction de rappel des données de message in-app (héritée)

Vous pouvez définir une fonction de rappel dans Dart pour recevoir les données du messages in-app Braze dans l’application Flutter hôte.

Pour définir la fonction de rappel, appelez `BrazePlugin.setBrazeInAppMessageCallback()` depuis votre application Flutter avec une fonction qui prend une instance `BrazeInAppMessage`.

{% tabs %}
{% tab Android %}

Cette fonction de rappel marche sans requérir d’intégration supplémentaire.

{% endtab %}
{% tab iOS %}

1. Implémentez le délégué `BrazeInAppMessageUIDelegate` comme décrit dans notre article iOS sur le [délégué de message in-app de base](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui).

2. Mettez à jour votre implémentation de délégué `willPresent` pour qu’elle appelle `BrazePlugin.process(inAppMessage)`.

Consultez [AppDelegate.swift](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/ios/Runner/AppDelegate.swift) dans notre exemple d’application pour en avoir un exemple.

{% endtab %}
{% endtabs %}

#### Rejouer la fonction de rappel pour les messages in-app

Pour enregistrer des messages in-app déclenchés avant que la fonction de rappel soit disponible et les rejouer une fois qu’elle est définie, ajoutez l’entrée suivante à la map `customConfigs` lors de l’initialisation de `BrazePlugin` :
```dart
BrazePlugin braze = new BrazePlugin(customConfigs: {replayCallbacksConfigKey: true});
```

## Tester l’affichage d’un exemple de message in-app

Suivez ces étapes pour tester un exemple de message in-app.

1. Définissez un utilisateur actif dans l’application React en appelant la méthode `braze.changeUser('your-user-id')`.
2. Dirigez-vous vers la page **Campaigns** de votre tableau de bord et suivez [ce guide][1] pour créer une nouvelle campagne de messages in-app.
3. Composez votre campagne de messages in-app et rendez-vous sur l’onglet **Test**. Ajoutez les mêmes `user-id` que l’utilisateur de test et cliquez sur **Envoyer le test**.
4. Appuyez sur la notification push qui devrait afficher le message in-app sur votre appareil.

![Une campagne de messages in-app Braze montrant que vous pouvez ajouter votre propre ID utilisateur en tant que destinataire de test pour essayer votre message in-app.][2]

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/
[2]: {% image_buster /assets/img/react-native/iam-test.png %} "In-App Messaging Test"
