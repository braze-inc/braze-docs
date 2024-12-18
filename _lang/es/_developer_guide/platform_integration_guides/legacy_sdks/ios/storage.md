---
nav_title: Almacenamiento
article_title: Almacenamiento para iOS
platform: iOS
page_order: 8.9
page_type: reference
description: "Este artículo de referencia describe las propiedades a nivel de dispositivo capturadas por el SDK de Braze para iOS."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Almacenamiento

En este artículo se describen las diferentes propiedades a nivel de dispositivo que se capturan al utilizar el SDK de Braze para iOS.

## Propiedades del dispositivo

De forma predeterminada, Braze recopilará las siguientes [propiedades a nivel de dispositivo](https://github.com/Appboy/appboy-ios-sdk/blob/16e893f2677af7de905b927505d4101c6fb2091d/AppboyKit/headers/AppboyKitLibrary/Appboy.h#L181) para permitir la personalización de mensajes basada en el dispositivo, el idioma y la zona horaria:

* Resolución del dispositivo
* Operador del dispositivo
* Configuración regional del dispositivo
* Modelo del dispositivo
* Versión del sistema operativo del dispositivo
* IDFV (opcional a partir de la versión 5.7.0 del SDK [ para iOS](https://github.com/braze-inc/braze-swift-sdk))
* Notificaciones push habilitadas
* Zona horaria del dispositivo
* Estado de la autenticación push
* Seguimiento de anuncios habilitado

{% alert note %}
El SDK de Braze no recoge IDFA automáticamente. Las aplicaciones pueden pasar opcionalmente IDFA a Braze implementando nuestro protocolo `ABKIDFADelegate`. Las aplicaciones deben obtener la adhesión voluntaria explícita del usuario final al seguimiento a través del marco de transparencia de seguimiento de aplicaciones antes de pasar IDFA a Braze.
{% endalert %}

Los campos configurables del dispositivo se definen en la enumeración [`ABKDeviceOptions`](https://github.com/Appboy/appboy-ios-sdk/blob/4390e9eac8401bccdb81b053fa54eb87b1f6fcaa/Appboy-tvOS-SDK/AppboyTVOSKit.framework/Headers/Appboy.h#L179). Para desactivar o especificar el campo del dispositivo que te gustaría permitir en la lista, asigna el bitwise `OR` de los campos deseados a [`ABKDeviceAllowlistKey`](https://github.com/Appboy/appboy-ios-sdk/blob/fed071000722673754da288cace15c1ff8aca432/AppboyKit/include/Appboy.h#L148) en el `appboyOptions` de `startWithApiKey:inApplication:withAppboyOptions:`.

Por ejemplo, para especificar la zona horaria y la recopilación de configuraciones regionales que se deben permitir, establece:
```
appboyOptions[ABKDeviceAllowlistKey] = @(ABKDeviceOptionTimezone | ABKDeviceOptionLocale);
```

Por defecto, todos los campos están habilitados. Ten en cuenta que, sin algunas propiedades, no todas las funciones funcionarán correctamente. Por ejemplo, la entrega según la zona horaria local no funcionará sin la zona horaria.

Para saber más sobre las propiedades del dispositivo recopiladas automáticamente, visita nuestra [recopilación de datos del SDK]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/). 
