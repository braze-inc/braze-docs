{% multi_lang_include developer_guide/prerequisites/flutter.md %}

## Enregistrement des données des messages

Pour enregistrer les analyses à l'aide de votre `BrazeInAppMessage`, passez l'instance dans la fonction d'analyse souhaitée :

- `logInAppMessageClicked`
- `logInAppMessageImpression`
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

## Accès aux données des messages

Pour accéder aux données des messages in-app dans votre application Flutter, le `BrazePlugin` prend en charge l'envoi de données de messages in-app à l'aide de [Dart Streams](https://dart.dev/tutorials/language/streams).

L'objet `BrazeInAppMessage` prend en charge un sous-ensemble de champs disponibles dans les objets du modèle natif, notamment `uri`, `message`, `header`, `buttons`, `extras`, et d'autres.

### Écouter les données des messages in-app dans la couche Dart

Pour recevoir les données des messages in-app dans la couche Dart, utilisez le code ci-dessous pour créer un `StreamSubscription` et appeler `braze.subscribeToInAppMessages()`. N'oubliez pas d'appeler `cancel()` sur l'abonnement au flux lorsqu'il n'est plus nécessaire.

```dart
// Create stream subscription
StreamSubscription inAppMessageStreamSubscription;

inAppMessageStreamSubscription = braze.subscribeToInAppMessages((BrazeInAppMessage inAppMessage) {
  // Handle in-app messages
}

// Cancel stream subscription
inAppMessageStreamSubscription.cancel();
```

Consultez [main.dart](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/lib/main.dart) dans l'exemple d'application du SDK Flutter de Braze.

### Transmettre les données des messages in-app depuis la couche native

{% tabs %}
{% tab Flutter SDK 18.0.0+ %}

Les données des messages in-app sont automatiquement transmises depuis les couches natives Android et iOS. Aucune configuration supplémentaire n'est requise.

{% endtab %}
{% tab Flutter SDK 17.1.0 and earlier %}

Si vous utilisez le SDK Flutter 17.1.0 ou une version antérieure, la transmission des données des messages in-app depuis la couche native iOS nécessite une configuration manuelle. Votre application contient probablement l'un des éléments suivants. Pour migrer vers le SDK Flutter 18.0.0, supprimez l'appel à `BrazePlugin.processInAppMessage(_:)` — la transmission des données est désormais gérée automatiquement.

{% subtabs %}
{% subtab UI Delegate %}

Supprimez l'appel à `BrazePlugin.processInAppMessage(_:)` de votre [implémentation du délégué `willPresent`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:willpresent:view:)-4pzvv).

{% endsubtab %}

{% subtab Custom presenter %}

Supprimez l'appel à `BrazePlugin.processInAppMessage(message)` de l'implémentation [`present(message:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui/present(message:)-f2ra) de votre présentateur personnalisé :

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

### Rejouer le rappel pour les messages in-app (facultatif)

Pour stocker tous les messages in-app déclenchés avant que le rappel ne soit disponible et les rejouer une fois celui-ci défini, ajoutez l'entrée suivante au mappage `customConfigs` lors de l'initialisation du `BrazePlugin` :
```dart
BrazePlugin braze = new BrazePlugin(customConfigs: {replayCallbacksConfigKey: true});
```
