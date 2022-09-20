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

{% tabs %}
{% tab Android %}

Si vous souhaitez accéder aux données de message in-app dans la couche Javascript, implémentez le `IInAppMessageManagerListener` comme décrit dans notre article Android sur le [Gestionnaire d’auditeur personnalisé]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/custom_listeners/#custom-manager-listener). Dans votre implémentation de `beforeInAppMessageDisplayed`, vous pouvez accéder aux données `inAppMessage`, les envoyer à la couche Javascript et décider d’afficher ou non le message natif en fonction de la valeur de retour.

Pour plus d’informations sur ces valeurs, consultez notre [Documentation Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/).

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

Si vous souhaitez accéder aux données de message in-app dans la couche Javascript, implémentez le délégué `ABKInAppMessageControllerDelegate` comme décrit dans notre article iOS sur le [délégué principal de message in-app]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/setting_delegates/#core-in-app-message-delegate). Dans la méthode de délégation `beforeInAppMessageDisplayed:`, vous pouvez accéder aux données `inAppMessage`, les envoyer à la couche Javascript et décider d’afficher ou non le message natif en fonction de la valeur de retour.

Pour plus d’informations sur ces valeurs, consultez notre [Documentation iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/handing_in_app_display/).

{% subtabs %}
{% subtab OBJECTIVE-C %}
```objc
// In-app messaging
- (ABKInAppMessageDisplayChoice) beforeInAppMessageDisplayed:(ABKInAppMessage *)inAppMessage {
  NSData *inAppMessageData = [inAppMessage serializeToData];
  NSString *inAppMessageString = [[NSString alloc] initWithData:inAppMessageData encoding:NSUTF8StringEncoding];
  NSDictionary *arguments = @{
    @"inAppMessage" : inAppMessageString
  };
  // Send to JavaScript
  [self.bridge.eventDispatcher
             sendDeviceEventWithName:@"inAppMessageReceived"
             body:arguments];
  // Note: return ABKDiscardInAppMessage if you would like
  // to prevent the Braze SDK from displaying the message natively.
  return ABKDisplayInAppMessageNow;
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Réception de message in-app dans Javascript

Côté Javascript, ces données peuvent être utilisées pour instancier un `BrazeInAppMessage` :
```javascript
DeviceEventEmitter.addListener("inAppMessageReceived", (event) => {
    const inAppMessage = new ReactAppboy.BrazeInAppMessage(event.inAppMessage);
});
```

## Analytique

Pour enregistrer l’analytique à l’aide de votre `BrazeInAppMessage`, passez l’instance dans la fonction d’analytique souhaitée :
- `logInAppMessageClicked`
- `logInAppMessageImpression`
- `logInAppMessageButtonClicked` (avec l’index des boutons)

Par exemple :
```js
// Log a click
ReactAppboy.logInAppMessageClicked(inAppMessage);
// Log an impression
ReactAppboy.logInAppMessageImpression(inAppMessage);
// Log button index `0` being clicked
ReactAppboy.logInAppMessageButtonClicked(inAppMessage, 0);
```

## Tester l’affichage d’un exemple de message in-app

Suivez ces étapes pour tester un exemple de message in-app.

1. Définir un utilisateur actif dans l’application React en appelant la méthode `ReactAppboy.changeUserId('your-user-id')`.
2. Dirigez-vous vers **Campaigns** et suivez [ce guide][5] pour créer une nouvelle campagne de messages in-app.
3. Composez votre campagne de messages in-app et rendez-vous sur l’onglet **Test**. Ajouter le même `user-id` comme utilisateur de test et cliquez sur **Send Test** (Envoyer le test). Vous devriez être très prochainement en mesure de lancer un message in-app sur votre périphérique.

![Une campagne de messages in-app Braze montrant que vous pouvez ajouter votre propre ID utilisateur en tant que destinataire de test pour essayer votre message in-app.][6]

Un exemple d’implémentation est disponible dans AppboyProject, dans le [SDK React][7]. D’autres exemples d’implémentation Android et iOS sont disponibles dans le SDK [Android][8] et [iOS][9].

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/custom_listeners/#custom-manager-listener
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/custom_listeners/#step-1-implement-an-in-app-message-manager-listener
[5]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/
[6]: {% image_buster /assets/img/react-native/iam-test.png %} "In-App Messaging Test"
[7]: https://github.com/Appboy/appboy-react-sdk
[8]: https://github.com/Appboy/appboy-android-sdk
[9]: https://github.com/Appboy/appboy-ios-sdk