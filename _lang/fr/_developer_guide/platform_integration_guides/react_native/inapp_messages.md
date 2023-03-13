---
nav_title: Messages in-app
article_title: Messages in-app pour React Native
platform: React Native
page_order: 4
page_type: reference
description: "Cet article couvre les messages in-app des applications pour iOS et Android utilisant React Native, y compris l’analytique de la personnalisation et de la journalisation."
channel: messages in-app

---

# Messages in-app

Les messages in-app natifs s’affichent automatiquement sur Android et iOS lors de l’utilisation de React Native. Cet article couvre la personnalisation et la journalisation des analytiques pour vos messages in-app pour les applications utilisant React Native.

## Accès aux données de message in-app

Si vous souhaitez accéder aux données du message in-app dans la couche Javascript, appelez la méthode `Braze.subscribeToInAppMessage()` pour que les SDK publient un événement `inAppMessageReceived` lors du déclenchement du message in-app. Vous pouvez ajouter une fonction de rappel à cette méthode ou configurer un écouteur pour cet événement qui va réaliser une fonction de rappel lors du déclenchement du message in-app.

Cette méthode intègre un paramètre qui indique au SDK de Braze si l’interface utilisateur intégrée de Braze va, ou non, afficher les messages in-app. Si vous préférez utiliser une interface utilisateur personnalisée, vous pouvez transmettre `false` à cette méthode et utiliser les données des messages in-app pour construire votre propre message dans Javascript.

```javascript
importer Braze depuis "@braze/react-native-sdk";

Braze.subscribeToInAppMessage(false, (event) => {
  const inAppMessage = new Braze.BrazeInAppMessage(event.inAppMessage);
});

// Vous pouvez également configurer un écouteur directement pour l’événement
Braze.addListener(Braze.Events.IN_APP_MESSAGE_RECEIVED, (event) => {
  const inAppMessage = new Braze.BrazeInAppMessage(event.inAppMessage);
});
```

## Personnalisation avancée

Si vous souhaitez inclure une logique plus avancée pour savoir si un message in-app va ou non s’afficher à l’aide de l’interface utilisateur intégrée, vous devez implémenter les messages in-app dans la couche native.

{% tabs %}
{% tab Android %}

Implémentez `IInAppMessageManagerListener`, tel que décrit dans notre article Android sur [Ecouteur de gestionnaire personnalisé]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/custom_listeners/#custom-manager-listener). Dans votre implémentation de `beforeInAppMessageDisplayed`, vous pouvez accéder aux données `inAppMessage`, les envoyer à la couche Javascript et décider d’afficher ou non le message natif en fonction de la valeur de retour.

Pour plus d’informations sur ces valeurs, consultez notre [Documentation Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/).

```java
// Messagerie In-App
@Override
public InAppMessageOperation beforeInAppMessageDisplayed(IInAppMessage inAppMessage) {
    WritableMap parameters = new WritableNativeMap();
    parameters.putString("inAppMessage", inAppMessage.forJsonPut().toString());
    getReactNativeHost()
        .getReactInstanceManager()
        .getCurrentReactContext()
        .getJSModule(DeviceEventManagerModule.RCTDeviceEventEmitter.class)
        .emit("inAppMessageReceived", parameters);
    // Remarque  : retournez InAppMessageOperation.DISCARD si vous souhaitez
    // empêcher Braze SDK d’afficher les messages en mode natif.
    return InAppMessageOperation.DISPLAY_NOW;
}
```
{% endtab %}
{% tab iOS %}

Implémentez le délégué `ABKInAppMessageControllerDelegate` comme décrit dans notre article iOS sur le [délégué de message in-app de base]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/setting_delegates/#core-in-app-message-delegate). Dans la méthode de délégation `beforeInAppMessageDisplayed:`, vous pouvez accéder aux données `inAppMessage`, les envoyer à la couche Javascript et décider d’afficher ou non le message natif en fonction de la valeur de retour.

Pour plus d’informations sur ces valeurs, consultez notre [Documentation iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/handing_in_app_display/).

{% subtabs %}
{% subtab OBJECTIVE-C %}
```objc
// Messagerie In-App
- (ABKInAppMessageDisplayChoice) beforeInAppMessageDisplayed:(ABKInAppMessage *)inAppMessage {
  NSData *inAppMessageData = [inAppMessage serializeToData];
  NSString *inAppMessageString = [[NSString alloc] initWithData:inAppMessageData encoding:NSUTF8StringEncoding];
  NSDictionary *arguments = @{
    @"inAppMessage" : inAppMessageString
  };
  // Envoyer à Javascript
  [self.bridge.eventDispatcher
             sendDeviceEventWithName:@"inAppMessageReceived"
             body:arguments];
  // Remarque: retourner ABKDiscardInAppMessage si vous souhaitez
  // empêcher Braze SDK d’afficher les messages en mode natif.
  return ABKDisplayInAppMessageNow;
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Réception de message in-app dans Javascript

Côté Javascript, ces données peuvent être utilisées pour instancier un `BrazeInAppMessage` :
```javascript
Braze.addListener(Braze.Events.IN_APP_MESSAGE_RECEIVED, (event) => {
  const inAppMessage = new Braze.BrazeInAppMessage(event.inAppMessage);
});
```

## Analytique

Pour enregistrer l’analytique à l’aide de votre `BrazeInAppMessage`, passez l’instance dans la fonction d’analytique souhaitée :
- `logInAppMessageClicked`
- `logInAppMessageImpression`
- `logInAppMessageButtonClicked` (avec l’index des boutons)

Par exemple :
```js
// Journaliser un clic
Braze.logInAppMessageClicked(inAppMessage);
// Journaliser une impression
Braze.logInAppMessageImpression(inAppMessage);
// Index de bouton de journalisation `0` cliqué
Braze.logInAppMessageButtonClicked(inAppMessage, 0);
```

## Tester l’affichage d’un exemple de message in-app

Suivez ces étapes pour tester un exemple de message in-app.

1. Définissez un utilisateur actif dans l’application React en appelant la méthode `Braze.changeUserId('your-user-id')`.
2. Dirigez-vous vers **Campaigns** et suivez [ce guide][5] pour créer une nouvelle campagne de messages in-app.
3. Composez votre campagne de messages in-app et rendez-vous sur l’onglet **Test**. Ajoutez les mêmes `user-id` que l’utilisateur de test et cliquez sur **Envoyer le test**. Vous devriez être très prochainement en mesure de lancer un message in-app sur votre périphérique.

![Une campagne de messages in-app Braze montrant que vous pouvez ajouter votre propre ID utilisateur en tant que destinataire de test pour essayer votre message in-app][6]

Un exemple d’implémentation est disponible dans AppboyProject, dans le [SDK React][7]. D’autres exemples d’implémentation Android et iOS sont disponibles dans le SDK [Android][8] et [iOS][9]

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/custom_listeners/#custom-manager-listener
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/custom_listeners/#step-1-implement-an-in-app-message-manager-listener
[5]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/
[6]: {% image_buster /assets/img/react-native/iam-test.png %} "In-App Messaging Test"
[7]: https://github.com/braze-inc/braze-react-native-sdk
[8]: https://github.com/braze-inc/braze-android-sdk
[9]: https://github.com/Appboy/appboy-ios-sdk
