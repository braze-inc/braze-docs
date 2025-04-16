# Almacenamiento

> Este artículo describe las diferentes propiedades a nivel de dispositivo que se capturan al utilizar el SDK para Android de Braze.

## Propiedades del dispositivo

De forma predeterminada, Braze recopilará las siguientes [propiedades a nivel de dispositivo](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.enums/-device-key/index.html) para permitir la personalización de mensajes basada en el dispositivo, el idioma y la zona horaria:

* `AD_TRACKING_ENABLED`
* `ANDROID_VERSION`
* `CARRIER`
* `IS_BACKGROUND_RESTRICTED`
* `LOCALE`
* `MODEL`
* `NOTIFICIATION_ENABLED`
* `RESOLUTION`
* `TIMEZONE`

{% alert note %}
`AD_TRACKING_ENABLED` y `TIMEZONE` no se recogen si son `null` o están en blanco. `GOOGLE_ADVERTISING_ID` no es recogido automáticamente por el SDK y debe pasarse a través de [`setGoogleAdvertisingId`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/set-google-advertising-id.html).
{% endalert %}

Puedes desactivar o especificar las propiedades que deseas recopilar configurándolas mediante [`BrazeConfig.Builder.setDeviceObjectAllowlistEnabled()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-device-object-allowlist-enabled.html) y [`BrazeConfig.Builder.setDeviceObjectAllowlist()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-device-object-allowlist.html).

El siguiente ejemplo muestra cómo permitir que el objeto dispositivo solo incluya la versión del sistema operativo Android y la configuración regional del dispositivo:
```
  new BrazeConfig.Builder()
      .setDeviceObjectAllowlistEnabled(true)
      .setDeviceObjectAllowlist(EnumSet.of(DeviceKey.ANDROID_VERSION, DeviceKey.LOCALE));
```
Por defecto, todos los campos están habilitados. Ten en cuenta que, sin algunas propiedades, no todas las funciones funcionarán correctamente. Por ejemplo, la entrega según la zona horaria local no funcionará sin la zona horaria.

Visita nuestro artículo [Recopilación de datos de SDK]({{site.baseurl}}/user_guide/data/user_data_collection/sdk_data_collection/) para obtener más información sobre las propiedades del dispositivo recopiladas automáticamente.


