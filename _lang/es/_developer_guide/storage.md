---
nav_title: Almacenamiento
article_title: Almacenamiento para iOS
page_order: 3.60
page_type: reference
description: "Conoce las diferentes propiedades a nivel de dispositivo que almacena el SDK de Braze."
platform:
  - Android
  - FireOS
  - Swift
  - Web
---

# Almacenamiento

> Conoce las diferentes propiedades a nivel de dispositivo que almacena el SDK de Braze.

## Propiedades del dispositivo

De forma predeterminada, Braze recopilará las siguientes propiedades a nivel de dispositivo para permitir la personalización de mensajes basada en el dispositivo, el idioma y la zona horaria:

{% tabs %}
{% tab Android %}
- `AD_TRACKING_ENABLED`
- `ANDROID_VERSION`
- `CARRIER`
- `IS_BACKGROUND_RESTRICTED`
- `LOCALE`
- `MODEL`
- `NOTIFICIATION_ENABLED`
- `RESOLUTION`
- `TIMEZONE`

{% alert note %}
`AD_TRACKING_ENABLED` y `TIMEZONE` no se recogen si son `null` o están en blanco. `GOOGLE_ADVERTISING_ID` no es recogido automáticamente por el SDK y debe pasarse a través de [`setGoogleAdvertisingId`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/set-google-advertising-id.html).
{% endalert %}
{% endtab %}

{% tab swift %}
- Operador del dispositivo (consulta la nota sobre la [eliminación de`CTCarrier` ](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/deviceproperty/carrier))
- Configuración regional del dispositivo
- Modelo del dispositivo
- Versión del sistema operativo del dispositivo
- Estado de la autorización push
- Opciones de la pantalla push
- Notificaciones push habilitadas
- Resolución del dispositivo
- Zona horaria del dispositivo

{% alert note %}
El SDK de Braze no recoge IDFA automáticamente. Las aplicaciones pueden pasar opcionalmente IDFA a Braze implementando los métodos que se indican directamente a continuación. Las aplicaciones deben obtener la adhesión voluntaria explícita al seguimiento por parte del usuario final a través del marco de Transparencia del Seguimiento de Aplicaciones antes de pasar IDFA a Braze.

1. Para establecer el estado de seguimiento de la publicidad, utiliza [`set(adTrackingEnabled:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(adtrackingenabled:)/).
2. Para configurar el identificador del anunciante (IDFA), utiliza [`set(identifierForAdvertiser:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforadvertiser:)/).
{% endalert %}
{% endtab %}

{% tab Web %}
- `BROWSER`
- `BROWSER_VERSION`
- `LANGUAGE`
- `OS`
- `RESOLUTION`
- `TIME_ZONE`
- `USER_AGENT`
{% endtab %}
{% endtabs %}

Por defecto, todas las propiedades están habilitadas. Sin embargo, puedes habilitarlas o deshabilitarlas manualmente. Ten en cuenta que algunas características del SDK de Braze requieren propiedades específicas (como la entrega según la zona horaria local y la zona horaria), así que asegúrate de probar tu configuración antes de pasarla a producción.

{% tabs %}
{% tab android %}
Por ejemplo, puedes especificar la versión del sistema operativo Android y la configuración regional del dispositivo a incluir en la lista de permitidos. Para más información, consulta [`setDeviceObjectAllowlistEnabled()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-device-object-allowlist-enabled.html) y [`setDeviceObjectAllowlist()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-device-object-allowlist.html) métodos. 

```java
new BrazeConfig.Builder()
    .setDeviceObjectAllowlistEnabled(true)
    .setDeviceObjectAllowlist(EnumSet.of(DeviceKey.ANDROID_VERSION, DeviceKey.LOCALE));
```
{% endtab %}

{% tab swift %}
Por ejemplo, puedes especificar la zona horaria y la colección de configuraciones regionales que se deben permitir. Para más información, consulta la propiedad [`devicePropertyAllowList`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/devicepropertyallowlist) del objeto `configuration`.

{% subtabs %}
{% subtab swift %}

```swift
configuration.devicePropertyAllowList = [.timeZone, .locale]
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
configuration.devicePropertyAllowList = @[
    BRZDeviceProperty.timeZone,
    BRZDeviceProperty.locale
];
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Web %}
Por ejemplo, puedes especificar el idioma del dispositivo que se va a permitir. Para más información, consulta la opción `devicePropertyAllowlist` para [`InitializationOptions`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions).

```javascript
import * as braze from"@braze/web-sdk";
braze.initialize("API-KEY", {
    baseUrl: "BASE-URL",
    devicePropertyAllowlist: [ braze.DeviceProperties.LANGUAGE ] // list of `DeviceProperties` you want to collect
});
```
{% endtab %}
{% endtabs %}

{% alert tip %}
Para saber más sobre las propiedades del dispositivo recopiladas automáticamente, consulta [Recopilación de datos del SDK]({{site.baseurl}}/user_guide/data/user_data_collection/sdk_data_collection/).
{% endalert %}

## Almacenamiento de cookies (sólo Web) {#cookies}

Tras [inicializar el SDK de Web Braze](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize), éste creará y almacenará cookies con una caducidad de 400 días que se renueva automáticamente en las nuevas sesiones.

Se almacenan las siguientes cookies:

|Cookie|Descripción|Tamaño|
|---|----|---|---|
|`ab.storage.userId.[your-api-key]`|Se utiliza para determinar si el usuario conectado actualmente ha cambiado y para asociar eventos con el usuario actual.|En función del tamaño del valor pasado a `changeUser`|
|`ab.storage.sessionId.[your-api-key]`|Cadena generada aleatoriamente que se utiliza para determinar si el usuario está iniciando una sesión nueva o existente para sincronizar mensajes y calcular los análisis de la sesión.|~200 bytes|
|`ab.storage.deviceId.[your-api-key]`|Cadena generada aleatoriamente que se utiliza para identificar a los usuarios anónimos y para diferenciar los dispositivos de los usuarios y habilita la mensajería basada en dispositivos.|~200 bytes|
|`ab.optOut`|Se utiliza para almacenar la preferencia de adhesión voluntaria de un usuario cuando se llama a `disableSDK` |~40 bytes|
|`ab._gd`|Creado temporalmente (y luego eliminado) para determinar el dominio de la cookie de nivel raíz, que permite que el SDK funcione correctamente a través de subdominios.|n/a|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Desactivar cookies {#disable-cookies}

Para desactivar todas las cookies, utiliza la opción [`noCookies`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions) al inicializar el SDK Web. Esto evitará que asocies usuarios anónimos que navegan por subdominios y dará lugar a un nuevo usuario en cada subdominio.

```javascript
import * as braze from"@braze/web-sdk";
braze.initialize("API-KEY", {
    baseUrl: "BASE-URL",
    noCookies: true
});
```

Para detener el seguimiento de Braze en general, o para borrar todos los datos almacenados del navegador, consulta los métodos del SDK [`disableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disableSDK) y [`wipeData`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#wipedata), respectivamente. Estos dos métodos pueden ser útiles si un usuario revoca su consentimiento o si quieres detener toda la funcionalidad de Braze después de que el SDK se haya inicializado.
