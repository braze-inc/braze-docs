---
nav_title: Messages In-App
article_title: Messages In-App pour Flutter
platform: Flution
page_order: 4
page_type: reference
description: "Cet article couvre les messages dans l'application pour les applications iOS et Android utilisant Flutter, y compris la personnalisation et la journalisation des analyses."
channel: messages intégrés à l'application
---

# Messages dans l'application

Les messages natifs dans l'application s'affichent automatiquement sur Android et iOS lors de l'utilisation de Flutter. Cet article couvre différentes options de personnalisation pour les messages dans l'application.

## Analyses

Pour enregistrer les analytiques en utilisant votre `BrazeInAppMessage`, passez l'instance dans la fonction analytique désirée:
- `Vous avez cliqué sur le message de l'application.`
- `Impression du message de connexion`
- `logInAppMessageButtonClicked` (avec l'index du bouton)

Par exemple :
```dart
// Log a click
braze.logInAppMessageClicked(inAppMessage);
// Log an impression
braze.logInAppMessageImpression(inAppMessage);
// Log button index `0` being clicked
braze.logInAppMessageButtonClicked(inAppMessage, 0);
```

## Désactivation de l'affichage automatique

Pour désactiver l'affichage automatique des messages dans l'application, faites ces mises à jour dans la couche native.

{% tabs %}
{% tab Android %}

1. Assurez-vous que vous utilisez l'insertion automatique d'intégration, qui est activée par défaut à partir de la version `2.2.0`.
2. Définissez l'opération de message dans l'application par défaut à `DISCARD` en ajoutant la ligne ci-dessous à votre fichier `braze.xml`.

```xml
<string name="com_braze_flutter_automatic_integration_iam_operation">DÉSACTIVER</string>
```

{% endtab %}
{% tab iOS %}

1. Implémentez le délégué `ABKInAppMessageControllerDelegate` comme décrit dans notre section iOS sur [le délégué de message Core In-App]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/#core-in-app-message-delegate).

2. Mettez à jour votre implémentation `beforeInAppMessageDisplay` déléguée pour retourner `ABKInAppMessageDisplayChoice.discardInAppMessage`.

Pour un exemple, voir [AppDelegate.swift](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/ios/Runner/AppDelegate.swift) dans notre exemple d'application.

{% endtab %}
{% endtabs %}

## Rappel de données du message dans l'application

Vous pouvez définir un callback dans Dart pour recevoir les données de message dans l'application Braze dans l'application.

Pour définir le callback, appelez `BrazePlugin.setBrazeInAppMessageCallback()` depuis votre application Flutter avec une fonction qui prend une instance `BrazeInAppMessage`.

L'objet `BrazeInAppMessage` prend en charge un sous-ensemble de champs disponibles dans les objets modèles natifs, y compris `uri`, `message`, `en-tête`, `boutons`, `extras`, et plus.

{% tabs %}
{% tab Android %}

Ce callback fonctionne sans intégration supplémentaire.

{% endtab %}
{% tab iOS %}

1. Implémentez le délégué `ABKInAppMessageControllerDelegate` comme décrit dans notre section iOS sur [le délégué de message Core In-App]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/#core-in-app-message-delegate).

2. Mettez à jour votre implémentation `beforeInAppMessageDisplayed` délégué pour appeler `BrazePlugin.process(inAppMessage`.

Pour un exemple, voir [AppDelegate.swift](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/ios/Runner/AppDelegate.swift) dans notre exemple d'application.

{% endtab %}
{% endtabs %}

### Relecture de la fonction de rappel pour les messages dans l'application

Pour stocker tous les messages déclenchés dans l'application avant que la fonction de rappel soit disponible et les rejouer une fois qu'elle est définie, ajouter l'entrée suivante à la carte `customConfigs` lors de l'intimidation du `BrazePlugin`:
```dart
BrazePlugin braze = new BrazePlugin(customConfigs: {replayCallbacksConfigKey: true});
```

## Teste l'affichage d'un exemple de message dans l'application

Suivez les étapes ci-dessous pour tester un exemple de message dans l'application.

1. Définissez un utilisateur actif dans l'application React en appelant la méthode `braze.changeUser('votre-utilisateur-id')`.
2. Rendez-vous sur la page **Campagnes** de votre tableau de bord et suivez [ce guide][1] pour créer une nouvelle campagne de message dans l'application.
3. Écrivez votre campagne de messagerie de test dans l'application et dirigez-vous vers l'onglet **Test**. Ajoutez le même `identifiant utilisateur` que l'utilisateur de test et cliquez sur **Envoyer le test**.
4. Appuyez sur la notification push et cela devrait afficher le message dans l'application sur votre appareil.

!\[Test de Campagne de Messagerie In-App\]\[2\]
[2]: {% image_buster /assets/img/react-native/iam-test.png %} "In-App Messaging Test"


[1]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/
