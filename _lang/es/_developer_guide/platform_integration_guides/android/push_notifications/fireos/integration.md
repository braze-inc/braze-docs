---
nav_title: Integración
article_title: Integración push para FireOS
platform: FireOS
page_order: 0
page_type: solution
description: "Este artículo de referencia te explica cómo integrar las notificaciones push de Braze en tu aplicación FireOS."
channel: push
search_rank: 0.9
---

# Integración push de FireOS

> Este artículo de referencia te explica cómo integrar las notificaciones push de Braze en tu aplicación FireOS.

Una notificación push es una alerta fuera de la aplicación que aparece en la pantalla del usuario cuando se produce una actualización importante. Las notificaciones push son una forma valiosa de proporcionar a tus usuarios contenido relevante y sensible al tiempo para reactivar su interacción con tu aplicación.

ADM (Mensajería de dispositivos de Amazon) no es compatible con dispositivos que no sean de Amazon. Para probar las notificaciones push de Kindle, debes tener un [dispositivo FireOS](https://developer.amazon.com/appsandservices/apis/engage/device-messaging/tech-docs/04-integrating-your-app-with-adm). Consulta nuestro [artículo de ayuda]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/fireos/troubleshooting/) para conocer otras buenas prácticas.

Braze envía notificaciones push a los dispositivos de Amazon utilizando [la mensajería de dispositivos de Amazon (ADM)](https://developer.amazon.com/public/apis/engage/device-messaging).

## Paso 1: Habilitar ADM

1. Crea una cuenta en el [Portal del Desarrollador de Amazon Apps & Games](https://developer.amazon.com/public) si aún no lo has hecho.
2. Obtén [credenciales OAuth (ID de cliente y secreto de cliente) y una clave de API de ADM](https://developer.amazon.com/public/apis/engage/device-messaging/tech-docs/02-obtaining-adm-credentials).
3. **Habilita el Registro Automático de ADM Habilitado** en la ventana de Configuración de Unity Braze. 
  - Alternativamente, puedes añadir la siguiente línea a tu archivo `res/values/braze.xml` para habilitar el registro de ADM:

  ```xml
  <bool name="com_braze_push_adm_messaging_registration_enabled">true</bool>
  ```

## Paso 2: Actualiza AndroidManifest.xml

En la página AndroidManifest.xml de tu aplicación, añade el espacio de nombres de Amazon a la etiqueta `<>manifest</>`:

```xml
  xmlns:amazon="http://schemas.amazon.com/apk/res/android"
```

A continuación, declara los permisos necesarios para admitir ADM añadiendo los elementos `<>permission</>` y `<>uses-permission</>` después de `<>manifest</> element`:

  ```xml
  <manifest xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:amazon="http://schemas.amazon.com/apk/res/android"
    package="[YOUR PACKAGE NAME]"
    android:versionCode="1"
    android:versionName="1.0">

  <!-- This permission verifies that no other application can intercept your ADM messages. -->
  <permission
    android:name="[YOUR PACKAGE NAME].permission.RECEIVE_ADM_MESSAGE"
    android:protectionLevel="signature" />
  <uses-permission android:name="[YOUR PACKAGE NAME].permission.RECEIVE_ADM_MESSAGE" />

   <!-- This permission allows your app access to receive push notifications from ADM. -->
  <uses-permission android:name="com.amazon.device.messaging.permission.RECEIVE" />

  <!-- ADM uses WAKE_LOCK to keep the processor from sleeping when a message is received. -->
  <uses-permission android:name="android.permission.WAKE_LOCK" />
    ...
  </manifest>
```

A continuación, declara que tu aplicación utiliza la característica ADM del dispositivo y que tu aplicación está diseñada para seguir funcionando sin ADM presente en el dispositivo (`android:required="false"`) añadiendo un elemento `amazon:enable-feature` al elemento de aplicación del manifiesto. Es seguro configurar `android:required` como `"false"` porque el código ADM de Braze se degrada sin problemas cuando ADM no está presente en el dispositivo:

  ```xml
  ...
  <application
    android:icon="@drawable/ic_launcher"
    android:label="@string/app_name"
    android:theme="@style/AppTheme">

    <amazon:enable-feature android:name="com.amazon.device.messaging" android:required="false"/>
  ...
  ```

Por último, añade filtros de intención para gestionar las intenciones `REGISTRATION` y `RECEIVE` de ADM dentro de tu archivo Braze `AndroidManifest.xml`. Inmediatamente después de `amazon:enable-feature`, añade los siguientes elementos:

```xml
    <receiver
      android:name="com.braze.push.BrazeAmazonDeviceMessagingReceiver"
      android:exported="true"
      android:permission="com.amazon.device.messaging.permission.SEND">
      <intent-filter>
        <action android:name="com.amazon.device.messaging.intent.RECEIVE" />
        <action android:name="com.amazon.device.messaging.intent.REGISTRATION" />

        <category android:name="${applicationId}" />
      </intent-filter>
    </receiver>
```

## Paso 3: Almacena tu clave de API de ADM

En primer lugar, guarda tu clave de API de ADM en un archivo llamado `api_key.txt` y guárdalo en la carpeta [`Assets/Plugins/Android/assets`][54] de tu proyecto. A continuación, [obtén una clave de API de ADM para tu aplicación](https://developer.amazon.com/public/apis/engage/device-messaging/tech-docs/02-obtaining-adm-credentials).

Amazon no reconocerá tu clave si `api_key.txt` contiene algún carácter de espacio en blanco, como un salto de línea final.

## Paso 4: Añadir vínculos profundos

#### Habilitación de la apertura automática de vínculos profundos

Para habilitar Braze para que abra automáticamente tu aplicación y cualquier vínculo profundo cuando se haga clic en una notificación push, configura `com_braze_handle_push_deep_links_automatically` en `true` en tu `braze.xml`:

```
<bool name="com_braze_handle_push_deep_links_automatically">true</bool>
```

Si quieres gestionar de forma personalizada los vínculos profundos, tendrás que crear una devolución de llamada push que escuche las intenciones push recibidas y abiertas de Braze. Para más información, consulta [Gestión personalizada de los recibos push y de las aperturas]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#android-push-listener-callback) en la documentación sobre push de Android.

## Paso 5: Añadir secreto de cliente e ID de cliente al panel de Braze

Por último, debes añadir el secreto de cliente y el ID de cliente que obtuviste en [el paso 1](#step-1-enable-adm) a la página **Administrar configuración** del panel de Braze.

![]({% image_buster /assets/img_archive/fire_os_dashboard.png %})

## Registro push manual

Braze no recomienda utilizar el registro manual, pero si necesitas encargarte tú mismo del registro de ADM, añade lo siguiente en tu archivo [braze.xml](https://developer.amazon.com/public/apis/engage/device-messaging/tech-docs/03-setting-up-adm):

```xml
<!-- This will disable automatic registration for ADM via the Braze SDK-->
<bool name="com_braze_push_adm_messaging_registration_enabled">false</bool>
```
A continuación, utiliza [`Braze.setRegisteredPushToken()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/registered-push-token.html) para pasar el ADM `registration_id` de tu usuario a Braze:

{% tabs local %}
{% tab Java %}

```java
Braze.getInstance(context).setRegisteredPushToken(registration_id);
```

{% endtab %}
{% tab Kotlin %}

```kotlin
Braze.getInstance(context).registeredPushToken = registration_id
```

{% endtab %}
{% endtabs %}

## Extras ADM

Los usuarios pueden enviar pares clave-valor personalizados con un mensaje push de Kindle como `extras` para [vinculación en profundidad]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/deep_linking/), URL de seguimiento, etc. A diferencia de lo que ocurre en Android push, los usuarios de Kindle push no pueden utilizar claves reservadas de Braze como claves al definir los pares clave-valor de `extra`.

Las llaves reservadas incluyen:

- `_ab`
- `a`
- `cid`
- `p`
- `s`
- `t`
- `ttl`
- `uri`

Si se detecta una clave Kindle reservada, Braze devuelve `Status Code 400: Kindle Push Reserved Key Used`.

