---
nav_title: in-app Messages
article_title: Messages in-app pour React Native
platform: React Native
page_order: 4
page_type: reference
description: "Cet article couvre les messages in-app des applications pour iOS et Android utilisant React Native, y compris l’analyse de la personnalisation et de la journalisation."
channel: in-app messages

---

# Intégration de message in-app

> Les messages in-app natifs s’affichent automatiquement sur Android et iOS lors de l’utilisation de React Native. Cet article couvre la personnalisation et la journalisation des analyses pour vos messages in-app pour les applications utilisant React Native.

## Accès aux données de message in-app

Dans la plupart des cas, vous pouvez utiliser la méthode `Braze.addListener` pour enregistrer des récepteurs d'événements afin de gérer les données provenant des messages in-app. 

En outre, vous pouvez accéder aux données des messages in-app dans la couche JavaScript en appelant la méthode `Braze.subscribeToInAppMessage` pour que les SDK publient un événement `inAppMessageReceived` lorsqu'un message in-app est déclenché. Transmettez un rappel à cette méthode pour exécuter votre propre code lorsque le message in-app est déclenché et reçu par l'auditeur.

Pour personnaliser davantage le comportement par défaut, ou si vous n'avez pas accès à la personnalisation du code iOS ou Android natif, nous vous recommandons de désactiver l'interface utilisateur par défaut tout en continuant à recevoir des événements message in-app de Braze. Pour désactiver l'interface utilisateur par défaut, transmettez `false` à la méthode `Braze.subscribeToInAppMessage` et utilisez les données du message in-app pour élaborer votre propre message en JavaScript. Notez que, si vous choisissez de désactiver l’interface utilisateur par défaut, vous devrez [enregistrer manuellement l'analyse](#analytics) de vos messages.

```javascript
import Braze from "@braze/react-native-sdk";

// Option 1: Listen for the event directly via `Braze.addListener`.
//
// You may use this method to accomplish the same thing if you don't
// wish to make any changes to the default Braze UI.
Braze.addListener(Braze.Events.IN_APP_MESSAGE_RECEIVED, (event) => {
  console.log(event.inAppMessage);
});

// Option 2: Call `subscribeToInAppMessage`.
//
// Pass in `false` to disable the automatic display of in-app messages.
Braze.subscribeToInAppMessage(false, (event) => {
  console.log(event.inAppMessage);
  // Use `event.inAppMessage` to construct your own custom message UI.
});
```

## Personnalisation avancée

Pour inclure une logique plus avancée permettant de déterminer s'il faut ou non afficher un message in-app à l'aide de l'interface utilisateur intégrée, mettez en œuvre les messages in-app par le biais de la couche native.

{% alert warning %}
Étant donné qu'il s'agit d'une option de customisation avancée, notez que le fait de remplacer l'implémentation par défaut de Braze annulera également la logique d'émission d'événements de messages in-app vers vos listeners JavaScript. Si vous souhaitez continuer à utiliser `Braze.subscribeToInAppMessage` ou `Braze.addListener` comme décrit dans [Accès aux données des messages in-app](#accessing-in-app-message-data), vous devrez gérer vous-même la publication des événements.
{% endalert %}

{% tabs %}
{% tab Android %}

Implémentez le `IInAppMessageManagerListener` comme décrit dans notre article Android [Auditeur de gestionnaire personnalisé]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/custom_listeners/#custom-manager-listener). Dans votre implémentation de `beforeInAppMessageDisplayed`, vous pouvez accéder aux données `inAppMessage`, les envoyer à la couche Javascript et décider d’afficher ou non le message natif en fonction de la valeur de retour.

Pour en savoir plus sur ces valeurs, consultez notre [documentation Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/).

```java
// In-app messaging
@Override
public InAppMessageOperation beforeInAppMessageDisplayed(IInAppMessage inAppMessage) {
    WritableMap parameters = new WritableNativeMap();
    parameters.putString("inAppMessage", inAppMessage.forJsonPut().toString());
    getReactNativeHost()
        .getReactInstanceManager()
        .getCurrentReactContext()
        .getJSModule(DeviceEventManagerModule.RCTDeviceEventEmitter.class)
        .emit("inAppMessageReceived", parameters);
    // Note: return InAppMessageOperation.DISCARD if you would like
    // to prevent the Braze SDK from displaying the message natively.
    return InAppMessageOperation.DISPLAY_NOW;
}
```
{% endtab %}
{% tab iOS %}
### Remplacer le délégué de l'interface utilisateur par défaut

Par défaut, [`BrazeInAppMessageUI`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui/) est créée et attribuée lorsque vous initialisez l'instance `braze`. `BrazeInAppMessageUI` est une implémentation du protocole [`BrazeInAppMessagePresenter`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter) et dispose d'une propriété `delegate` qui peut être utilisée pour personnaliser la gestion des messages in-app qui ont été reçus.

1. Implémentez le délégué `BrazeInAppMessageUIDelegate` comme décrit dans [notre article iOS ici](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui).

2. Dans la méthode de délégation `inAppMessage(_:displayChoiceForMessage:)`, vous pouvez accéder aux données `inAppMessage`, les envoyer à la couche Javascript et décider d’afficher ou non le message natif en fonction de la valeur de retour.

Pour plus de détails sur ces valeurs, consultez notre [documentation iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/).

{% subtabs %}
{% subtab OBJECTIVE-C %}
```objc
- (enum BRZInAppMessageUIDisplayChoice)inAppMessage:(BrazeInAppMessageUI *)ui
                            displayChoiceForMessage:(BRZInAppMessageRaw *)message {
  // Convert the message to a JavaScript representation.
  NSData *inAppMessageData = [message json];
  NSString *inAppMessageString = [[NSString alloc] initWithData:inAppMessageData encoding:NSUTF8StringEncoding];
  NSDictionary *arguments = @{
    @"inAppMessage" : inAppMessageString
  };

  // Send to JavaScript.
  [self sendEventWithName:@"inAppMessageReceived" body:arguments];

  // Note: Return `BRZInAppMessageUIDisplayChoiceDiscard` if you would like
  // to prevent the Braze SDK from displaying the message natively.
  return BRZInAppMessageUIDisplayChoiceNow;
}
```
{% endsubtab %}
{% endsubtabs %}

Pour utiliser ce délégué, affectez-le à `brazeInAppMessagePresenter.delegate` après avoir initialisé l'instance `braze`. 

{% alert note %}
`BrazeUI` ne peut être importé qu'en Objective-C ou Swift. Si vous utilisez Objective-C++, vous devrez gérer ceci dans un fichier séparé.
{% endalert %}

{% subtabs %}
{% subtab OBJECTIVE-C %}
```objc
@import BrazeUI;

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:apiKey endpoint:endpoint];
  Braze *braze = [BrazeReactBridge initBraze:configuration];
  ((BrazeInAppMessageUI *)braze.inAppMessagePresenter).delegate = [[CustomDelegate alloc] init];
  AppDelegate.braze = braze;
}
```
{% endsubtab %}
{% endsubtabs %}

### Remplacer l'interface utilisateur native par défaut

Si vous souhaitez personnaliser entièrement la présentation de vos messages in-app au niveau de la couche native d'iOS, conformez-vous au protocole [`BrazeInAppMessagePresenter`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter) et attribuez votre présentateur personnalisé en suivant l'exemple ci-dessous :

{% subtabs %}
{% subtab OBJECTIVE-C %}
```objc
BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:apiKey endpoint:endpoint];
Braze *braze = [BrazeReactBridge initBraze:configuration];
braze.inAppMessagePresenter = [[MyCustomPresenter alloc] init];
AppDelegate.braze = braze;
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Analyse et méthodes d’action

Vous pouvez utiliser ces méthodes en passant votre instance `BrazeInAppMessage` pour enregistrer des analyses et effectuer des actions :

| Méthode                                                    | Description                                                                           |
| --------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `logInAppMessageClicked(inAppMessage)`                    | Enregistre un clic pour les données du message in-app fourni.                                    |
| `logInAppMessageImpression(inAppMessage)`                 | Enregistre une impression pour les données de message in-app fournies.                              |
| `logInAppMessageButtonClicked(inAppMessage, buttonId)`    | Enregistre un clic sur un bouton pour les données du message in-app et l'ID du bouton fournis.               |
| `hideCurrentInAppMessage()`                               | Désactive le message in-app en cours d'affichage.                                     |
| `performInAppMessageAction(inAppMessage)`                 | Effectue l'action pour un message in-app.                                            |
| `performInAppMessageButtonAction(inAppMessage, buttonId)` | Effectue l'action pour un bouton message in-app.                                     |

## Tester l’affichage d’un exemple de message in-app

Suivez ces étapes pour tester un exemple de message in-app.

1. Définissez un utilisateur actif dans l’application React en appelant la méthode `Braze.changeUserId('your-user-id')`.
2. Dirigez-vous vers **Campagnes** et suivez [ce guide]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/) pour créer une nouvelle campagne d'envoi de messages in-app.
3. Composez votre campagne d'envoi de messages in-app de test et dirigez-vous vers l'onglet **Test.**  Ajoutez le même `user-id` que l'utilisateur test et cliquez sur **Envoyer le test**. Vous devriez être très prochainement en mesure de lancer un message in-app sur votre appareil.

![Une campagne de communication in-app de Braze montrant que vous pouvez ajouter votre propre ID utilisateur en tant que destinataire test pour tester votre message in-app.]({% image_buster /assets/img/react-native/iam-test.png %} "In-App Messaging Test")

Un exemple de mise en œuvre peut être trouvé dans ReactProject, au sein du [SDK React Native](https://github.com/braze-inc/braze-react-native-sdk). Vous trouverez d'autres exemples de mise en œuvre pour Android et iOS dans le SDK [Android](https://github.com/braze-inc/braze-android-sdk) et [iOS](https://github.com/braze-inc/braze-swift-sdk).

## Modèle de données des messages in-app

Le modèle de message in-app est disponible dans le SDK React Native. Braze propose quatre types de messages in-app qui partagent le même modèle de données : **contextuel** **fenêtre modale**, **complet** et **HTML complet**.

### Propriétés du modèle de message in-app

Le modèle de message in-app constitue la base de tous les messages in-app.

|Propriété          | Description                                                                                                            |
|------------------|------------------------------------------------------------------------------------------------------------------------|
|`inAppMessageJsonString` | La représentation JSON du message.                                                                                |
|`message`         | Le texte du message.                                                                                                      |
|`header`          | L'en-tête du message.                                                                                                    |
|`uri`             | L'URI associé à l'action de clic sur le bouton.                                                                       |
|`imageUrl`        | L'URL de l'image du message.                                                                                                 |
|`zippedAssetsUrl` | Les ressources zippées préparées pour afficher le contenu HTML.                                                                    |
|`useWebView`      | Indique si l'action de clic sur le bouton doit être redirigée à l'aide d'une vue web.                                            |
|`duration`        | La durée d'affichage du message.                                                                                          |
|`clickAction`     | Le type d'action « clic sur bouton ». Les trois types sont les suivants : `NEWS_FEED`, `URI`, et `NONE`.                                     |
|`dismissType`     | Le type de fermeture du message. Les deux types sont : `SWIPE` et `AUTO_DISMISS`.                                                 |
|`messageType`     | Le type de message in-app pris en charge par le SDK. Les quatre types sont les suivants : `SLIDEUP`, `MODAL`, `FULL` et `HTML_FULL`.          |
|`extras`          | Le dictionnaire des suppléments de message. Valeur par défaut : `[:]`.                                                                   |
|`buttons`         | La liste des boutons sur le message in-app.                                                                             |
|`toString()`      | L'envoi de messages sous la forme d'une chaîne de caractères.                                                                                |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Pour une référence complète du modèle d'envoi de messages in-app, consultez la documentation [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/index.html) et [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage).

### Propriétés du modèle du bouton d'envoi de messages in-app

Des boutons peuvent être ajoutés aux messages in-app pour effectuer des actions et enregistrer des analyses. Le modèle de bouton constitue la base de tous les boutons de messages in-app.

|Propriété          | Description                                                                                                                 |
|------------------|-----------------------------------------------------------------------------------------------------------------------------|
|`text`            | Le texte du bouton.                                                                                                     |
|`uri`             | L'URI associé à l'action de clic sur le bouton.                                                                            |
|`useWebView`      | Indique si l'action de clic sur le bouton doit être redirigée à l'aide d'une vue web.                                                 |
|`clickAction`     | Le type d'action de clic traité lorsque l'utilisateur clique sur le bouton. Les trois types sont les suivants : `NEWS_FEED`, `URI`, et `NONE`. |
|`id`              | L'ID du bouton dans le message.                                                                                               |
|`toString()`      | Le bouton sous forme de chaîne de caractères.                                                                                      |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Pour une référence complète du modèle de bouton, consultez la documentation [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-message-button/index.html) et [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/button).

## Support GIF

{% multi_lang_include wrappers/gif_support/in_app_messaging.md %}

