---
nav_title: Messages In-App
article_title: Messages In-App pour React Native
platform: React Natif
page_order: 4
page_type: Référence
description: "Cet article couvre les messages dans l'application pour les applications iOS et Android utilisant React Native, y compris la personnalisation et la journalisation des analyses."
channel: messages intégrés à l'application
---

# Messages dans l'application

Les messages natifs dans l'application s'affichent automatiquement sur Android et iOS lorsque vous utilisez React Native. Cet article couvre la personnalisation et la journalisation de vos messages dans l'application pour les applications utilisant React Native.

## Accès aux données du message dans l'application

{% tabs %}
{% tab Android %}

Si vous voulez accéder aux données du message dans l'application dans la couche JavaScript, implémentez `IInAppMessageManagerListener` comme décrit dans notre section Android sur [l'écouteur du Gestionnaire personnalisé]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/#custom-manager-listener). Dans votre implémentation `beforeInAppMessageDisplayed` , vous pouvez accéder aux données de `inAppMessage` l'envoyer à la couche JavaScript, et décider d'afficher ou de ne pas afficher le message natif en fonction de la valeur de retour.

Pour plus d'informations sur ces valeurs, consultez notre [documentation Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/).

```java
// Messaging In-app
@Override
public InAppMessageOperation beforeInAppMessageDisplayed(IInAppMessage inAppMessage) {
    Paramètres WritableMap = new WritableNativeMap();
    paramètres. utString("inAppMessage", inAppMessage.forJsonPut().toString());
    getReactNativeHost()
        . etReactInstanceManager()
        .getCurrentReactContext()
        . etJSModule(DeviceEventManagerModule.RCTDeviceEventEmitter.class)
        . mit("inAppMessageReceived", paramètres);
    // Note: return InAppMessageOperation. ISCARD si vous souhaitez
    // pour empêcher le Braze SDK d'afficher le message nativement.
    retourner InAppMessageOperation.DISPLAY_MAINTENANT ;
}
```
{% endtab %}
{% tab iOS %}

Si vous souhaitez accéder aux données du message dans l'application dans la couche JavaScript, implémentez le délégué `ABKInAppMessageControllerDelegate` comme décrit dans notre section iOS sur [le délégué de message Core In-App]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/#core-in-app-message-controller-delegate). Dans la méthode `beforeInAppMessageDisplayed:` délégué, vous pouvez accéder aux données de `inAppMessage` l'envoyer à la couche JavaScript, et décider d'afficher ou de ne pas afficher le message natif en fonction de la valeur de retour.

Pour plus d'informations sur ces valeurs, consultez notre [documentation iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/#custom-handling-in-app-message-display).

{% subtabs %}
{% subtab OBJECTIVE-C %}
```objc
// Messagerie In-app
- (ABKInAppMessageDisplayChoice) beforeInAppMessageDisplayed:(ABKInAppMessage *)inAppMessage {
  NSData *inAppMessageData = [inAppMessage serializeToData];
  NSString *inAppMessageString = [[NSString alloc] initWithData:inAppMessageData encoding:NSUTF8StringEncoding] ;
  NSDictionary *arguments = @{
    @"inAppMessage" : inAppMessageString
  };
  // Envoyer à JavaScript
  [soi. La crête. ventDispatcher
             sendDeviceEventWithName:@"inAppMessageReceived"
             body:arguments];
  // Note: retourne ABKDiscardInAppMessage si vous souhaitez que
  // empêche le Braze SDK d'afficher le message nativement.
  retourner ABKDisplayInAppMessageMaintenant ;
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Réception du message dans l'application en JavaScript

Du côté JavaScript, ces données peuvent être utilisées pour instancier un `BrazeInAppMessage`:
```javascript
DeviceEventEmitter.addListener("inAppMessageReceived", (event) => {
    const inAppMessage = new ReactAppboy.BrazeInAppMessage(event.inAppMessage);
});
```

## Analyses

Pour enregistrer les analytiques en utilisant votre `BrazeInAppMessage`, passez l'instance dans la fonction analytique désirée:
- `Vous avez cliqué sur le message de l'application.`
- `Impression du message de connexion`
- `logInAppMessageButtonClicked` (avec l'index du bouton)

Par exemple :
```js
// Log a click
ReactAppboy.logInAppMessageClicked(inAppMessage);
// Log an impression
ReactAppboy.logInAppMessageImpression(inAppMessage);
// Log button index `0` being clicked
ReactAppboy.logInAppMessageButtonClicked(inAppMessage, 0);

```

## Teste l'affichage d'un exemple de message dans l'application

Suivez les étapes ci-dessous pour tester un exemple de message dans l'application.

1. Définissez un utilisateur actif dans l'application React en appelant la méthode `ReactAppboy.changeUserId('votre-utilisateur-id')`.
2. Rendez-vous sur **Campagnes** et suivez [ce guide][5] pour créer une nouvelle campagne **Messagerie In-App**.
3. Écrivez votre campagne de messagerie de test dans l'application et dirigez-vous vers l'onglet **Test**. Ajoutez le même `identifiant utilisateur` que l'utilisateur de test et cliquez sur **Envoyer le test**. Vous devriez être en mesure de lancer un message dans l'application sur votre appareil sous peu.

!\[Test de Campagne de Messagerie In-App\]\[6\]

Un exemple d'implémentation peut être trouvé dans AppboyProject, dans le [React SDK][7]. Des échantillons supplémentaires d'implémentation Android et iOS peuvent être trouvés dans le SDK [Android][8] et [iOS][9].
[6]: {% image_buster /assets/img/react-native/iam-test.png %} "In-App Messaging Test"

[5]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/
[7]: https://github.com/Appboy/appboy-react-sdk
[8]: https://github.com/Appboy/appboy-android-sdk
[9]: https://github.com/Appboy/appboy-ios-sdk