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

Les messages in-app natifs s’affichent automatiquement d’origine sur Android et iOS lors de l’utilisation de Flutter. Cet article couvre différentes options de personnalisation pour les messages in-app.

## Analytique

Pour enregistrer l’analytique à l’aide de votre `BrazeInAppMessage`, passez l’instance dans la fonction d’analytique souhaitée :
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

1. Implémentez le délégué `ABKInAppMessageControllerDelegate` comme décrit dans notre article iOS sur le [délégué de message in-app de base]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/setting_delegates/#core-in-app-message-delegate).

2. Mettez à jour votre implémentation de délégué `beforeInAppMessageDisplayed` pour qu’elle retourne `ABKInAppMessageDisplayChoice.discardInAppMessage`.

Consultez [AppDelegate.swift](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/ios/Runner/AppDelegate.swift) dans notre exemple d’application pour en avoir un exemple.

{% endtab %}
{% endtabs %}

## Fonction de rappel des données de message in-app

Vous pouvez définir une fonction de rappel dans Dart pour recevoir les données du messages in-app Braze dans l’application Flutter hôte.

Pour définir la fonction de rappel, appelez `BrazePlugin.setBrazeInAppMessageCallback()` depuis votre application Flutter avec une fonction qui prend une instance `BrazeInAppMessage`.

L’objet `BrazeInAppMessage` prend en charge un sous-ensemble de champs disponibles dans les objets du modèle natif, y compris `uri`, `message`, `header`, `buttons`, `extras` et plus encore.

{% tabs %}
{% tab Android %}

Cette fonction de rappel marche sans requérir d’intégration supplémentaire.

{% endtab %}
{% tab iOS %}

1. Implémentez le délégué `ABKInAppMessageControllerDelegate` comme décrit dans notre article iOS sur le [délégué de message in-app de base]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/setting_delegates/#core-in-app-message-delegate).

2. Mettez à jour votre implémentation de délégué `beforeInAppMessageDisplayed` pour qu’elle appelle `BrazePlugin.process(inAppMessage)`.

Consultez [AppDelegate.swift](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/ios/Runner/AppDelegate.swift) dans notre exemple d’application pour en avoir un exemple.

{% endtab %}
{% endtabs %}

### Rejouer la fonction de rappel pour les messages in-app

Pour enregistrer des messages in-app déclenchés avant que la fonction de rappel soit disponible et les rejouer une fois qu’elle est définie, ajoutez l’entrée suivante à la map `customConfigs` lors de l’initialisation de `BrazePlugin` :
```dart
BrazePlugin braze = new BrazePlugin(customConfigs: {replayCallbacksConfigKey: true});
```

## Tester l’affichage d’un exemple de message in-app

Suivez ces étapes pour tester un exemple de message in-app.

1. Définissez un utilisateur actif dans l’application React en appelant la méthode `braze.changeUser('your-user-id')`.
2. Dirigez-vous vers la page **Campaigns** de votre tableau de bord et suivez [ce guide][1] pour créer une nouvelle campagne de messages in-app.
3. Composez votre campagne de messages in-app et rendez-vous sur l’onglet **Test**. Ajoutez les mêmes `user-id` que l’utilisateur de test et cliquez sur **Send Test (Envoyer le test)**.
4. Appuyez sur la notification push qui devrait afficher le message in-app sur votre appareil.

![Une campagne de messages in-app Braze montrant que vous pouvez ajouter votre propre ID utilisateur en tant que destinataire de test pour essayer votre message in-app.][2]

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/
[2]: {% image_buster /assets/img/react-native/iam-test.png %} "In-App Messaging Test"
