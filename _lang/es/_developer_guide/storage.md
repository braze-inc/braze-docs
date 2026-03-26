---
nav_title: Almacenamiento
article_title: Almacenamiento para iOS
page_order: 3.60
page_type: reference
description: "Obtén información sobre las diferentes propiedades a nivel de dispositivo que almacena el SDK de Braze."
platform:
  - Android
  - FireOS
  - Swift
  - Web
---

# Almacenamiento

> Obtén información sobre las diferentes propiedades a nivel de dispositivo que almacena el SDK de Braze.

## Propiedades del dispositivo

De forma predeterminada, Braze recopilará las siguientes propiedades a nivel de dispositivo para permitir la personalización de mensajes basada en el dispositivo, el idioma y la zona horaria:

{% tabs %}
{% tab web %}
- `BROWSER`
- `BROWSER_VERSION`
- `LANGUAGE`
- `OS`
- `RESOLUTION`
- `TIME_ZONE`
- `USER_AGENT`
{% endtab %}

{% tab android %}
- `AD_TRACKING_ENABLED`
- `ANDROID_VERSION`
- `CARRIER`
- `IS_BACKGROUND_RESTRICTED`
- `LOCALE`
- `MODEL`
- `NOTIFICATION_ENABLED`
- `RESOLUTION`
- `TIMEZONE`

{% alert note %}
`AD_TRACKING_ENABLED` y `TIMEZONE` no se recopilan si son `null` o están en blanco. `GOOGLE_ADVERTISING_ID` no se recopila automáticamente por el SDK y debe pasarse a través de [`setGoogleAdvertisingId`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/set-google-advertising-id.html).
{% endalert %}
{% endtab %}

{% tab swift %}
- Operador del dispositivo (consulta la nota sobre la [eliminación de `CTCarrier`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/deviceproperty/carrier))
- Configuración regional del dispositivo
- Modelo del dispositivo
- Versión del sistema operativo del dispositivo
- Estado de la autorización push
- Opciones de visualización push
- Push habilitado
- Resolución del dispositivo
- Zona horaria del dispositivo

{% alert note %}
El SDK de Braze no recopila IDFA automáticamente. Las aplicaciones pueden pasar opcionalmente IDFA a Braze implementando los métodos que se indican directamente a continuación. Las aplicaciones deben obtener la adhesión voluntaria explícita al seguimiento por parte del usuario final a través del marco de Transparencia del Seguimiento de Aplicaciones antes de pasar IDFA a Braze.

1. Para establecer el estado de seguimiento de la publicidad, utiliza [`set(adTrackingEnabled:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(adtrackingenabled:)/).
2. Para configurar el identificador del anunciante (IDFA), utiliza [`set(identifierForAdvertiser:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforadvertiser:)/).
{% endalert %}
{% endtab %}
{% endtabs %}

De forma predeterminada, todas las propiedades están habilitadas. Sin embargo, puedes elegir habilitarlas o deshabilitarlas manualmente. Ten en cuenta que algunas características del SDK de Braze requieren propiedades específicas (como la entrega según la zona horaria local y la zona horaria), así que asegúrate de probar tu configuración antes de lanzarla a producción.

{% tabs %}
{% tab web %}
Por ejemplo, puedes especificar el idioma del dispositivo para incluirlo en la lista de permitidos. Para obtener más información, consulta la opción `devicePropertyAllowlist` para [`InitializationOptions`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions).

```javascript
import * as braze from"@braze/web-sdk";
braze.initialize("API-KEY", {
    baseUrl: "BASE-URL",
    devicePropertyAllowlist: [ braze.DeviceProperties.LANGUAGE ] // list of `DeviceProperties` you want to collect
});
```
{% endtab %}

{% tab android %}
Por ejemplo, puedes especificar la versión del sistema operativo Android y la configuración regional del dispositivo para incluirlos en la lista de permitidos. Para obtener más información, consulta los métodos [`setDeviceObjectAllowlistEnabled()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-device-object-allowlist-enabled.html) y [`setDeviceObjectAllowlist()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-device-object-allowlist.html). 

```java
new BrazeConfig.Builder()
    .setDeviceObjectAllowlistEnabled(true)
    .setDeviceObjectAllowlist(EnumSet.of(DeviceKey.ANDROID_VERSION, DeviceKey.LOCALE));
```
{% endtab %}

{% tab swift %}
Por ejemplo, puedes especificar la zona horaria y la configuración regional para incluirlas en la lista de permitidos. Para obtener más información, consulta la propiedad [`devicePropertyAllowList`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/devicepropertyallowlist) del objeto `configuration`.

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
{% endtabs %}

{% alert tip %}
Para obtener más información sobre las propiedades de los dispositivos recopiladas automáticamente, consulta [Recopilación de datos del SDK]({{site.baseurl}}/user_guide/data/user_data_collection/sdk_data_collection/).
{% endalert %}

## Almacenamiento de cookies (solo Web) {#cookies}

Después de [inicializar el SDK Web de Braze](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize), este creará y almacenará cookies con una caducidad de 400 días que se renovarán automáticamente en nuevas sesiones.

Se almacenan las siguientes cookies:

|Cookie|Descripción|Tamaño|
|---|----|---|---|
|`ab.storage.userId.[your-api-key]`|Se utiliza para determinar si el usuario conectado actualmente ha cambiado y para asociar eventos con el usuario actual.|En función del tamaño del valor pasado a `changeUser`|
|`ab.storage.sessionId.[your-api-key]`|Cadena generada aleatoriamente que se utiliza para determinar si el usuario está iniciando una sesión nueva o existente, para sincronizar mensajes y calcular los análisis de la sesión.|~200 bytes|
|`ab.storage.deviceId.[your-api-key]`|Cadena generada aleatoriamente que se utiliza para identificar a los usuarios anónimos, diferenciar los dispositivos de los usuarios y habilitar la mensajería basada en dispositivos.|~200 bytes|
|`ab.optOut`|Se utiliza para almacenar la preferencia de exclusión de un usuario cuando se llama a `disableSDK`.|~40 bytes|
|`ab._gd`|Se crea temporalmente (y luego se elimina) para determinar el dominio de cookie de nivel raíz, lo que permite que el SDK funcione correctamente en subdominios.|n/a|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Cambiar la caducidad de las cookies {#cookie-expiry}

De forma predeterminada, las cookies de Braze caducan después de 400 días. Para anular este valor, utiliza la opción `cookieExpiryInDays` al inicializar el SDK Web. Los valores deben ser mayores que 0; si la opción se omite o se establece en 0 o menos, se aplica el valor predeterminado de 400 días. Esta opción requiere el SDK Web 6.6.0 o posterior.

```javascript
import * as braze from "@braze/web-sdk";
braze.initialize("API-KEY", {
  baseUrl: "BASE-URL",
  cookieExpiryInDays: 30 // expires after 30 days
});
```

### Desactivar cookies {#disable-cookies}

Para desactivar todas las cookies, utiliza la opción [`noCookies`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions) al inicializar el SDK Web. Esto evitará que se asocien usuarios anónimos que navegan entre subdominios y dará lugar a un nuevo usuario en cada subdominio.

```javascript
import * as braze from "@braze/web-sdk";
braze.initialize("API-KEY", {
  baseUrl: "BASE-URL",
  noCookies: true
});
```

Para detener el seguimiento de Braze en general, o para borrar todos los datos almacenados del navegador, consulta los métodos del SDK [`disableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disableSDK) y [`wipeData`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#wipedata), respectivamente. Estos dos métodos pueden ser útiles si un usuario revoca su consentimiento o si quieres detener toda la funcionalidad de Braze después de que el SDK se haya inicializado.