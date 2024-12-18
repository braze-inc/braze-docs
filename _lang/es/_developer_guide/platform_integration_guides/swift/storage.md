---
nav_title: Almacenamiento
article_title: Almacenamiento para iOS
platform: Swift
page_order: 8.9
page_type: reference
description: "Este artículo de referencia describe las propiedades a nivel de dispositivo capturadas por el SDK Swift iOS de Braze."
---

# Almacenamiento

> Este artículo describe las diferentes propiedades a nivel de dispositivo que se capturan al utilizar el SDK Swift iOS de Braze.

## Propiedades del dispositivo

De forma predeterminada, Braze recopilará las siguientes [propiedades a nivel de dispositivo](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/deviceproperty) para permitir la personalización de mensajes basada en el dispositivo, el idioma y la zona horaria:

* Operador del dispositivo (consulta la nota sobre la [eliminación de`CTCarrier` ](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/deviceproperty/carrier))
* Configuración regional del dispositivo
* Modelo del dispositivo
* Versión del sistema operativo del dispositivo
* Estado de la autorización push
* Opciones de la pantalla push
* Notificaciones push habilitadas
* Resolución del dispositivo
* Zona horaria del dispositivo

{% alert note %}
El SDK de Braze no recoge IDFA automáticamente. Las aplicaciones pueden pasar opcionalmente IDFA a Braze implementando los métodos que se indican directamente a continuación. Las aplicaciones deben obtener la adhesión voluntaria explícita al seguimiento por parte del usuario final a través del marco de Transparencia del Seguimiento de Aplicaciones antes de pasar IDFA a Braze.

1. Para establecer el estado de seguimiento de la publicidad, utiliza [`set(adTrackingEnabled:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(adtrackingenabled:)/).
2. Para configurar el identificador del anunciante (IDFA), utiliza [`set(identifierForAdvertiser:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforadvertiser:)/).
{% endalert %}

Los campos configurables del dispositivo se definen en la enumeración [`Braze.Configuration.DeviceProperty`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/deviceproperty). Para desactivar o especificar el campo del dispositivo que quieres permitir, añade los campos a la propiedad [`devicePropertyAllowList`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/devicepropertyallowlist) del objeto `configuration`.

Por ejemplo, para especificar la zona horaria y la recopilación de configuraciones regionales que se deben permitir, establece:

{% tabs %}
{% tab swift %}

```swift
configuration.devicePropertyAllowList = [.timeZone, .locale]
```

{% endtab %}
{% tab OBJETIVO-C %}

```objc
configuration.devicePropertyAllowList = @[
    BRZDeviceProperty.timeZone,
    BRZDeviceProperty.locale
];
```

{% endtab %}
{% endtabs %}

Por defecto, todos los campos están habilitados. Ten en cuenta que, sin algunas propiedades, no todas las funciones funcionarán correctamente. Por ejemplo, la entrega según la zona horaria local no funcionará sin la zona horaria.

Para saber más sobre las propiedades del dispositivo recopiladas automáticamente, visita nuestra [recopilación de datos del SDK]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/).

