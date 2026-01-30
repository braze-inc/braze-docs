{% multi_lang_include developer_guide/prerequisites/react_native.md %}

## Méthodes d'enregistrement

Vous pouvez utiliser ces méthodes en passant votre instance `BrazeInAppMessage` pour enregistrer des analyses et effectuer des actions :

| Méthode                                                    | Description                                                                           |
| --------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `logInAppMessageClicked(inAppMessage)`                    | Enregistre un clic pour les données du message in-app fourni.                                    |
| `logInAppMessageImpression(inAppMessage)`                 | Enregistre une impression pour les données de message in-app fournies.                              |
| `logInAppMessageButtonClicked(inAppMessage, buttonId)`    | Enregistre un clic sur un bouton pour les données du message in-app et l'ID du bouton fournis.               |
| `hideCurrentInAppMessage()`                               | Désactive le message in-app en cours d'affichage.                                     |
| `performInAppMessageAction(inAppMessage)`                 | Effectue l'action pour un message in-app.                                            |
| `performInAppMessageButtonAction(inAppMessage, buttonId)` | Effectue l'action pour un bouton message in-app.                                     |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Envoi de données de messages

Dans la plupart des cas, vous pouvez utiliser la méthode `Braze.addListener` pour enregistrer des récepteurs d'événements afin de gérer les données provenant des messages in-app. 

En outre, vous pouvez accéder aux données des messages in-app dans la couche JavaScript en appelant la méthode `Braze.subscribeToInAppMessage` pour que les SDK publient un événement `inAppMessageReceived` lorsqu'un message in-app est déclenché. Transmettez un rappel à cette méthode pour exécuter votre propre code lorsque le message in-app est déclenché et reçu par l'auditeur.

Pour personnaliser l'envoi des données des messages, reportez-vous aux exemples de mise en œuvre suivants :

{% tabs local %}
{% tab basic %}
Pour améliorer le comportement par défaut, ou si vous n'avez pas accès à la personnalisation du code iOS ou Android natif, nous vous recommandons de désactiver l'interface utilisateur par défaut tout en continuant à recevoir des événements de messages in-app de Braze. Pour désactiver l'interface utilisateur par défaut, transmettez `false` à la méthode `Braze.subscribeToInAppMessage` et utilisez les données du message in-app pour élaborer votre propre message en JavaScript. Notez que vous devrez procéder manuellement à l'analyse/analytique de vos messages si vous choisissez de désactiver l'interface utilisateur par défaut.

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
{% endtab %}

{% tab advanced %}
Pour inclure une logique plus avancée permettant de déterminer s'il faut ou non afficher un message in-app à l'aide de l'interface utilisateur intégrée, mettez en œuvre les messages in-app par le biais de la couche native.

{% alert warning %}
Étant donné qu'il s'agit d'une option de customisation avancée, notez que le fait de remplacer l'implémentation par défaut de Braze annulera également la logique d'émission d'événements de messages in-app vers vos listeners JavaScript. Si vous souhaitez continuer à utiliser `Braze.subscribeToInAppMessage` ou `Braze.addListener` comme décrit dans [Accès aux données des messages in-app](#accessing-in-app-message-data), vous devrez gérer vous-même la publication des événements.
{% endalert %}

{% subtabs %}
{% subtab Android %}
Implémentez le `IInAppMessageManagerListener` comme décrit dans notre article Android [Auditeur de gestionnaire personnalisé]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=android#android_setting-custom-manager-listeners). Dans votre implémentation de `beforeInAppMessageDisplayed`, vous pouvez accéder aux données `inAppMessage`, les envoyer à la couche Javascript et décider d’afficher ou non le message natif en fonction de la valeur de retour.

Pour en savoir plus sur ces valeurs, consultez notre [documentation Android]({{site.baseurl}}/developer_guide/in_app_messages/).

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
{% endsubtab %}
{% subtab iOS %}
### Remplacer le délégué de l'interface utilisateur par défaut

Par défaut, [`BrazeInAppMessageUI`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui/) est créée et attribuée lorsque vous initialisez l'instance `braze`. `BrazeInAppMessageUI` est une implémentation du protocole [`BrazeInAppMessagePresenter`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter) et dispose d'une propriété `delegate` qui peut être utilisée pour personnaliser la gestion des messages in-app qui ont été reçus.

1. Implémentez le délégué `BrazeInAppMessageUIDelegate` comme décrit dans [notre article iOS ici](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui).

2. Dans la méthode de délégation `inAppMessage(_:displayChoiceForMessage:)`, vous pouvez accéder aux données `inAppMessage`, les envoyer à la couche Javascript et décider d’afficher ou non le message natif en fonction de la valeur de retour.

Pour plus de détails sur ces valeurs, consultez notre [documentation iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/).

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

Pour utiliser ce délégué, affectez-le à `brazeInAppMessagePresenter.delegate` après avoir initialisé l'instance `braze`. 

{% alert note %}
`BrazeUI` ne peut être importé qu'en Objective-C ou Swift. Si vous utilisez Objective-C++, vous devrez gérer ceci dans un fichier séparé.
{% endalert %}

```objc
@import BrazeUI;

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:apiKey endpoint:endpoint];
  Braze *braze = [BrazeReactBridge initBraze:configuration];
  ((BrazeInAppMessageUI *)braze.inAppMessagePresenter).delegate = [[CustomDelegate alloc] init];
  AppDelegate.braze = braze;
}
```

### Remplacer l'interface utilisateur native par défaut

Si vous souhaitez personnaliser entièrement la présentation de vos messages in-app au niveau de la couche native d'iOS, conformez-vous au protocole [`BrazeInAppMessagePresenter`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter) et attribuez votre présentateur personnalisé en suivant l'exemple ci-dessous :

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
