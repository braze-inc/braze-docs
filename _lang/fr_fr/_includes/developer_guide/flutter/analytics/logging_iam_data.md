{% multi_lang_include developer_guide/prerequisites/flutter.md %}

## Données d'envoi des messages

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

## Accès aux données des messages

Pour accéder aux données des messages in-app dans votre application Flutter, le site `BrazePlugin` transmet les données des messages in-app à l'aide de [Dart Streams](https://dart.dev/tutorials/language/streams).

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
{% subtabs %}

Vous pouvez transmettre les données des messages in-app de deux manières :

{% subtab UI Delegate %}

1. Implémentez le délégué `BrazeInAppMessageUIDelegate` comme décrit dans notre article iOS sur le [délégué de message in-app de base](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui).

2. Mettez à jour votre [implémentation de délégué `willPresent`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:willpresent:view:)-4pzvv) pour qu’elle appelle `BrazePlugin.process(inAppMessage)`.
{% endsubtab %}

{% subtab custom presenter %}
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
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Étape 3 : Reprise du rappel pour les messages in-app (facultatif).

Pour stocker tous les messages in-app déclenchés avant que le rappel ne soit disponible et les rejouer une fois qu'il est défini, ajoutez l'entrée suivante au mappage `customConfigs` lors de l'initialisation de l'application `BrazePlugin`:
```dart
BrazePlugin braze = new BrazePlugin(customConfigs: {replayCallbacksConfigKey: true});
```
