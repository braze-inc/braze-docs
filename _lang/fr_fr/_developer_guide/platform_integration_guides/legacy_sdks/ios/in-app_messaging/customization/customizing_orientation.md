---
nav_title: Personnalisation de l’orientation
article_title: Personnalisation de l’orientation des messages in-app pour iOS
platform: iOS
page_order: 3
description: "Cet article de référence explique comment définir l’orientation des messages in-app pour votre application iOS."
channel:
  - in-app messages

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Personnalisation de l’orientation

## Définir l’orientation pour tous les messages in-app

Pour définir une orientation fixe pour tous les messages in-app, vous pouvez définir la propriété `supportedOrientationMask` sur `ABKInAppMessageUIController`. Ajoutez le code suivant après l’appel de votre application à `startWithApiKey:inApplication:withLaunchOptions:` :

{% tabs %}
{% tab OBJECTIF-C %}

```objc
// Set fixed in-app message orientation to portrait.
// Use UIInterfaceOrientationMaskLandscape to display in-app messages in landscape
id<ABKInAppMessageUIControlling> inAppMessageUIController = [Appboy sharedInstance].inAppMessageController.inAppMessageUIController;
((ABKInAppMessageUIController *)inAppMessageUIController).supportedOrientationMask = UIInterfaceOrientationMaskPortrait;
```

{% endtab %}
{% tab swift %}

```swift
// Set fixed in-app message orientation to portrait
// Use .landscape to display in-app messages in landscape
if let controller = Appboy.sharedInstance()?.inAppMessageController.inAppMessageUIController as? ABKInAppMessageUIController {
  controller.supportedOrientationMask = .portrait
}
```

{% endtab %}
{% endtabs %}

Ensuite, tous les messages in-app seront affichés dans l’orientation prise en charge, quelle que soit l’orientation de l’appareil. Notez que l’orientation de l’appareil doit également être prise en charge par la propriété `orientation` du message in-app à afficher.

## Définition de l’orientation par message in-app

Vous pouvez également définir l’orientation message par message. Pour ce faire, définissez un [délégué de message in-app]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/setting_delegates/). Ensuite, dans votre méthode de délégation `beforeInAppMessageDisplayed:`, définissez la propriété `orientation` sur le `ABKInAppMessage` :

{% tabs %}
{% tab OBJECTIF-C %}

```objc
// Set inAppMessage orientation to portrait
inAppMessage.orientation = ABKInAppMessageOrientationPortrait;

// Set inAppMessage orientation to landscape
inAppMessage.orientation = ABKInAppMessageOrientationLandscape;
```

{% endtab %}
{% tab swift %}

```swift    
  // Set inAppMessage orientation to portrait
  inAppMessage.orientation = ABKInAppMessageOrientation.portrait

  // Set inAppMessage orientation to landscape
  inAppMessage.orientation = ABKInAppMessageOrientation.landscape
```

{% endtab %}
{% endtabs %}

Les messages in-app ne s’affichent pas si l’orientation de l’appareil ne correspond pas à la propriété `orientation` sur le message in-app.

{% alert note %}
Pour les iPads, les messages in-app apparaissent dans le style d’orientation préféré de l’utilisateur, quelle que soit l’orientation réelle de l’écran.
{% endalert %}

## Déclarations de méthode

Pour plus d’informations, voir le fichier d’en-tête suivant :

- [`ABKInAppMessage.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessage.h)

