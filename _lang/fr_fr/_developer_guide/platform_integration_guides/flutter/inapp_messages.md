---
nav_title: in-app Messages
article_title: Messages in-app pour Flutter
platform: Flutter
page_order: 4
page_type: reference
description: "Cet article couvre les messages in-app des applications pour iOS et Android utilisant Flutter, y compris l’analyse de la personnalisation et de la journalisation."
channel: in-app messages

---

# Intégration de messages in-app

> Découvrez comment intégrer et personnaliser les messages in-app pour Android et iOS à l'aide de Flutter.

## Activer l'interface utilisateur des messages in-app

Pour intégrer l’envoi de messages in-app de Flutter à iOS, [activez l’envoi de messages in-app à l'aide du SDK Braze Swift]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/in-app_message_delivery/#enabling-in-app-messages). Il n'y a pas d'étapes supplémentaires pour Android.

## Enregistrer les analyses

Pour enregistrer les analyses à l’aide de votre `BrazeInAppMessage`, passez l’instance dans la fonction d’analyses souhaitée :
- `logInAppMessageClicked`
- `logInAppMessageImpression`
- `logInAppMessageButtonClicked` (avec l’index des boutons)

Par exemple :
```dart
// Log a click
braze.logInAppMessageClicked(inAppMessage);
// Log an impression
braze.logInAppMessageImpression(inAppMessage);
// Log button index `0` being clicked
braze.logInAppMessageButtonClicked(inAppMessage, 0);
```

## Désactiver l’affichage automatique

Pour désactiver l’affichage automatique des messages in-app, effectuez ces mises à jour dans la couche native.

{% tabs %}
{% tab Android %}

1. Assurez-vous d’utiliser l’initiateur d’intégration automatique, activé par défaut à partir de la version `2.2.0`.
2. Définissez l’opération par défaut de message in-app `DISCARD` en ajoutant la ligne suivante à votre fichier `braze.xml`.

```xml
<string name="com_braze_flutter_automatic_integration_iam_operation">DISCARD</string>
```

{% endtab %}
{% tab iOS %}

1. Implémentez le délégué `BrazeInAppMessageUIDelegate` comme décrit dans notre [article iOS ici](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui).

2. Mettez à jour votre méthode de délégué `inAppMessage(_:displayChoiceForMessage:)` pour qu’elle retourne `.discard`.

{% endtab %}
{% endtabs %}

## Réception des données de message in-app

Pour recevoir des données de messages in-app dans votre application Flutter, le `BrazePlugin` prend en charge l'envoi de données de messages in-app à l'aide de [Dart Streams](https://dart.dev/tutorials/language/streams).

L’objet `BrazeInAppMessage` prend en charge un sous-ensemble de champs disponibles dans les objets du modèle natif, y compris `uri`, `message`, `header`, `buttons`, `extras` et plus encore.

### Étape 1 : Écouter les données des messages in-app dans la couche Dart

Pour recevoir les données des messages in-app dans la couche Dart, utilisez le code ci-dessous pour créer un `StreamSubscription` et appeler `braze.subscribeToInAppMessages()`. N’oubliez pas de `cancel()` l’abonnement au flux lorsqu’il n’est plus nécessaire.

```dart
// Create stream subscription
StreamSubscription inAppMessageStreamSubscription;

inAppMessageStreamSubscription = braze.subscribeToInAppMessages((BrazeInAppMessage inAppMessage) {
  // Handle in-app messages
}

// Cancel stream subscription
inAppMessageStreamSubscription.cancel();
```

Consultez [main.dart](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/lib/main.dart) dans notre exemple d'application.

### Étape 2 : Transmettre les données des messages in-app à partir de la couche native

Pour recevoir les données dans la couche Dart de l'étape 1, ajoutez le code suivant pour envoyer les données du message in-app à partir des couches natives.

{% tabs %}
{% tab Android %}

Les données des messages in-app sont automatiquement transmises par la couche Android.

{% endtab %}
{% tab iOS %}

### Option 1 - Utilisation de `BrazeInAppMessageUIDelegate`

1. Implémentez le délégué `BrazeInAppMessageUIDelegate` comme décrit dans notre article iOS sur le [délégué de message in-app de base](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui).

2. Mettez à jour votre [implémentation de délégué `willPresent`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:willpresent:view:)-4pzvv) pour qu’elle appelle `BrazePlugin.process(inAppMessage)`.

### Option 2 - Présentateur de message in-app personnalisé

1. Assurez-vous d'avoir activé l'interface utilisateur de l'envoi message in-app et définissez l'adresse `inAppMessagePresenter` sur votre présentateur personnalisé.
```swift
    let inAppMessageUI = CustomInAppMessagePresenter()
    braze.inAppMessagePresenter = inAppMessageUI
```
2. Créez votre classe de présentateur personnalisée et appelez `BrazePlugin.process(inAppMessage)` à l'intérieur de [`present(message:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui/present(message:)-f2ra).
```swift
class CustomInAppMessagePresenter: BrazeInAppMessageUI {
  override func present(message: Braze.InAppMessage) {
    // Pass in-app message data to the Dart layer.
    BrazePlugin.processInAppMessage(message)

    // If you want the default UI to display the in-app message.
    super.present(message: message)
  }
}
```

{% endtab %}
{% endtabs %}

#### Rejouer la fonction de rappel pour les messages in-app

Pour stocker tous les messages in-app déclenchés avant que le rappel ne soit disponible et les rejouer une fois qu'il est défini, ajoutez l'entrée suivante au mappage `customConfigs` lors de l'initialisation de l'application `BrazePlugin`:
```dart
BrazePlugin braze = new BrazePlugin(customConfigs: {replayCallbacksConfigKey: true});
```

## Test d'un exemple de message in-app

Suivez ces étapes pour tester un exemple de message in-app.

1. Définissez un utilisateur actif dans l’application React en appelant la méthode `braze.changeUser('your-user-id')`.
2. Rendez-vous sur la page **Campagnes de** votre tableau de bord et suivez [ce guide]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/) pour créer une nouvelle campagne de messages in-app.
3. Composez votre campagne d'envoi de messages in-app de test et dirigez-vous vers l'onglet **Test.**  Ajoutez le même `user-id` que l'utilisateur test et cliquez sur **Envoyer le test**.
4. Appuyez sur la notification push qui devrait afficher le message in-app sur votre appareil.

## Support GIF

{% multi_lang_include wrappers/gif_support/in_app_messaging.md %}

![Une campagne de communication in-app de Braze montrant que vous pouvez ajouter votre propre ID utilisateur en tant que destinataire test pour tester votre message in-app.]({% image_buster /assets/img/react-native/iam-test.png %} "In-App Messaging Test")

