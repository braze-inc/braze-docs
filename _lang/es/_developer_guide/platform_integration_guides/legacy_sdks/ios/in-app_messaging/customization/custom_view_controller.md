---
nav_title: Controlador de vista personalizado
article_title: Mensaje dentro de la aplicación en un controlador de vista personalizado para iOS
platform: iOS
page_order: 7
description: "Este artículo de referencia explica cómo aprovechar un controlador de vista de mensajería dentro de la aplicación personalizado para tu aplicación de iOS."
channel:
  - in-app messages
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Mostrar mensajes dentro de la aplicación en un controlador de vista personalizado

Los mensajes dentro de la aplicación también pueden mostrarse dentro de un controlador de vista personalizado, que pasas a Braze. Braze animará la entrada y salida del mensaje dentro de la aplicación personalizado y gestionará los análisis del mensaje dentro de la aplicación. El controlador de vista debe cumplir los siguientes requisitos

- Debe ser una subclase o una instancia de `ABKInAppMessageViewController`.
- La vista del controlador de vista devuelto debe ser una instancia de `ABKInAppMessageView` o de su subclase.

El siguiente método delegado de interfaz de usuario se llama cada vez que se ofrece un mensaje dentro de la aplicación a `ABKInAppMessageViewController` para permitir que la aplicación pase un controlador de vista personalizado a Braze para la visualización de mensajes dentro de la aplicación:

{% tabs %}
{% tab OBJETIVO-C %}

```objc
- (ABKInAppMessageViewController *)inAppMessageViewControllerWithInAppMessage:(ABKInAppMessage *)inAppMessage;
```

{% endtab %}
{% tab swift %}

```swift
func inAppMessageViewControllerWithInAppMessage(inAppMessage: ABKInAppMessage!) -> ABKInAppMessageViewController!
```

{% endtab %}
{% endtabs %}

Nuestros [controladores de vista de mensajes dentro de la aplicación](https://github.com/Appboy/appboy-ios-sdk/tree/master/AppboyUI/ABKInAppMessage/ViewControllers) son personalizables. Puedes utilizar subclases o categorías para personalizar la visualización o el comportamiento de los mensajes dentro de la aplicación.

## Declaraciones de métodos

Para más información, consulta los siguientes archivos de encabezado:

- [`ABKInAppMessage.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessage.h)

## Muestras de aplicación

Consulta [`ViewController.m`](https://github.com/Appboy/appboy-ios-sdk/blob/master/Samples/InAppMessage/BrazeInAppMessageSample/BrazeInAppMessageSample/ViewController.m) y [`CustomInAppMessageViewController.m`](https://github.com/Appboy/appboy-ios-sdk/blob/master/Samples/InAppMessage/BrazeInAppMessageSample/BrazeInAppMessageSample/) en la aplicación de ejemplo de mensajes dentro de la aplicación.

