---
nav_title: Orientación personalizada
article_title: Personalizar la orientación de los mensajes dentro de la aplicación para iOS
platform: iOS
page_order: 3
description: "Este artículo de referencia explica cómo configurar la orientación de los mensajes dentro de la aplicación para tu aplicación de iOS."
channel:
  - in-app messages

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Orientación personalizada

## Configurar la orientación de todos los mensajes dentro de la aplicación

Para establecer una orientación fija para todos los mensajes dentro de la aplicación, puedes configurar la propiedad `supportedOrientationMask` en `ABKInAppMessageUIController`. Añade el siguiente código después de la llamada de tu aplicación a `startWithApiKey:inApplication:withLaunchOptions:`:

{% tabs %}
{% tab OBJETIVO-C %}

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

A continuación, todos los mensajes dentro de la aplicación se mostrarán en la orientación admitida, independientemente de la orientación del dispositivo. Ten en cuenta que la orientación del dispositivo también debe ser compatible con la propiedad `orientation` del mensaje dentro de la aplicación para que el mensaje se muestre.

## Configuración de la orientación por mensaje dentro de la aplicación

También puedes configurar la orientación por mensaje. Para ello, establece un [delegado de mensajes dentro de la aplicación]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/setting_delegates/). A continuación, en tu método delegado `beforeInAppMessageDisplayed:`, establece la propiedad `orientation` en `ABKInAppMessage`:

{% tabs %}
{% tab OBJETIVO-C %}

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

Los mensajes dentro de la aplicación no se mostrarán si la orientación del dispositivo no coincide con la propiedad `orientation` del mensaje dentro de la aplicación.

{% alert note %}
En los iPads, los mensajes dentro de la aplicación aparecerán en el estilo de orientación preferido por el usuario, independientemente de la orientación real de la pantalla.
{% endalert %}

## Declaraciones de métodos

Para más información, consulta el siguiente archivo de cabecera:

- [`ABKInAppMessage.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessage.h)

