---
nav_title: Integración con Baidu
article_title: Integración de notificaciones push de Baidu para Android
platform: Android
permalink: /baidu_integration/
description: "Este artículo muestra cómo configurar una integración de Baidu en Android."
hidden: true
---
# Integración con Baidu
{% multi_lang_include archive/baidu_deprecation.md %}

Braze puede enviar notificaciones push a dispositivos Android utilizando [Baidu Cloud Push][14]. Ten en cuenta que el uso de Baidu Cloud Push **no** requiere que distribuyas tus aplicaciones a través de Baidu App Store.

## Paso 1: Crear una cuenta Baidu

Para crear una cuenta Baidu, visita el [Portal Baidu][7] y haz clic **en 登录** (Iniciar sesión) para que aparezca un cuadro de diálogo que te permitirá iniciar sesión o crear una cuenta nueva.

![][33]

Para crear una nueva cuenta, en la parte inferior del diálogo de iniciar sesión, haz clic **en 立即注册** (nueva cuenta).

![][38]{: style="max-width:70%;"}

Introduce tu nombre de usuario, número de teléfono y contraseña en la página de creación de cuenta. A continuación, haz clic en el botón "Recibir código de verificación". Ahora recibirás un mensaje SMS de Baidu con un código de verificación. Por último, acepta el acuerdo de licencia y haz clic **en 注册** (crear cuenta) para registrarte. Si estos pasos de configuración fallan, intenta registrarte a través del inicio de sesión en Baidu Cloud como se describe en este [artículo sobre el inicio de sesión](https://www.adchina.io/how-to-open-a-baidu-account-outside-china/).

![Página de registro de Baidu][17]{: style="max-width:80%;"}

## Paso 2: Registrarse como desarrollador de Baidu

A continuación, debes registrarte como desarrollador de Baidu. Primero, visita el [portal para desarrolladores de Baidu][36] y elige **注册** (crear nueva cuenta de desarrollador) para iniciar el registro.

![][37]

En la página de registro, elige tu tipo de cuenta (个人 para personal, 公司 para empresa) y el tipo de desarrollador (el desarrollador está preseleccionado y es correcto en la mayoría de los casos). Introduce tu nombre, una biografía y un número de teléfono con el código del país entre paréntesis (Por ejemplo, (1)xxxxxxxxxx). Haz clic en **发送验证码** (enviar código de verificación) e introduce el código de verificación en la línea siguiente. Los dos campos siguientes, sitio web del desarrollador y logotipo del desarrollador, son opcionales. Acepta el acuerdo de licencia y haz clic **en 提交** (enviar) para enviarlo. Ahora tienes una cuenta de desarrollador de Baidu.

![][13]

## Paso 3: Registra tu solicitud en Baidu

Para registrar tu aplicación en Baidu, visita el [portal de proyectos de Baidu][11] y haz clic **en 创建工程** (crear proyecto).

![][10]

En la página siguiente, introduce el nombre de tu candidatura. Las dos casillas siguientes sirven para activar servicios adicionales de Baidu. En la mayoría de los casos, deben dejarse en blanco.

![][26]

Al configurar tu aplicación, accederás a una consola que muestra información sobre tu aplicación, incluida la clave de API. A continuación, ve a **云推送** (cloud push) en la barra lateral. En la página siguiente, haz clic **en 推送设置** (configurar push).

![][14]

![][29]

En la página siguiente, introduce el nombre del paquete de tu aplicación (por ejemplo, `com.braze.sample`) y especifica si deseas almacenar en caché los mensajes y, en caso afirmativo, durante cuánto tiempo (en horas). Indica a Baidu cuánto tiempo debe seguir intentando enviar mensajes a usuarios desconectados. Haz clic en **保存设置** (guardar configuración) para guardar.

![][39]

## Paso 4: Añade Baidu a tu aplicación

Visita el [portal Baidu push SDK][40] y descarga el último SDK para Android de Baidu Cloud Push.

![][41]

Dentro del SDK, encontrarás el jar del servicio push y las bibliotecas nativas específicas de la plataforma. Intégralos en tu proyecto. Asegúrate de que tu aplicación se dirige a la versión más alta del SDK actualmente soportada por Baidu. Esta documentación es actual para Baidu Cloud push Android SDK versión `4.6.2.38`.

Añade los siguientes permisos necesarios de Baidu a la página `AndroidManifest.xml` de tu aplicación.

```xml
    <uses-permission android:name="android.permission.READ_PHONE_STATE" />
    <uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED" />
    <uses-permission android:name="android.permission.WRITE_SETTINGS" />
    <uses-permission android:name="android.permission.VIBRATE" />
    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
    <uses-permission android:name="android.permission.DISABLE_KEYGUARD" />
    <uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
    <uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
```

La biblioteca de Baidu contiene receptores de difusión que gestionan los mensajes push entrantes. Declara los receptores internos de Baidu en la página `AndroidManifest.xml` de tu aplicación, dentro del elemento `<application>`.

```xml
  <!-- 用于接收系统消息以保证 PushService 正常运行 -->
      <receiver
        android:name="com.baidu.android.pushservice.PushServiceReceiver"
        android:process=":bdservice_v1">
        <intent-filter>
          <action android:name="android.intent.action.BOOT_COMPLETED"/>
          <action android:name="android.net.conn.CONNECTIVITY_CHANGE"/>
          <action android:name="com.baidu.android.pushservice.action.notification.SHOW"/>
          <action android:name="com.baidu.android.pushservice.action.media.CLICK"/>
        </intent-filter>
      </receiver>
      <!-- Push 服务接收客户端发送的各种请求-->
      <!-- 注意:RegistrationReceiver 在 2.1.1 及之前版本有拼写失误,为 RegistratonReceiver ,用 新版本 SDK 时请更改为如下代码-->
      <receiver
        android:name="com.baidu.android.pushservice.RegistrationReceiver"
        android:process=":bdservice_v1">
        <intent-filter>
          <action android:name="com.baidu.android.pushservice.action.METHOD"/>
          <action android:name="com.baidu.android.pushservice.action.BIND_SYNC"/>
        </intent-filter>
        <intent-filter>
          <action android:name="android.intent.action.PACKAGE_REMOVED"/>
          <data android:scheme="package"/>
        </intent-filter>
      </receiver>
      <!-- Push 服务 -->
      <!-- 注意:在 4.0 (包含)之后的版本需加上如下所示的 intent-filter action -->
      <service
        android:name="com.baidu.android.pushservice.PushService"
        android:exported="true"
        android:process=":bdservice_v1">
        <intent-filter >
          <action android:name="com.baidu.android.pushservice.action.PUSH_SERVICE"/>
        </intent-filter>
      </service>
```

También tendrás que crear un receptor de difusión que escuche los mensajes y notificaciones push entrantes. Declara tu receptor en el `AndroidManifest.xml` de tu aplicación dentro del elemento `<application>`. Este receptor tendrá que ampliar `com.baidu.android.pushservice.PushMessageReceiver` e implementar métodos que reciban actualizaciones de eventos del servicio push de Baidu.

```xml
      <receiver android:name=".MyPushMessageReceiver">
        <intent-filter>
          <action android:name="com.baidu.android.pushservice.action.MESSAGE"/>
          <action android:name="com.baidu.android.pushservice.action.RECEIVE"/>
          <action android:name="com.baidu.android.pushservice.action.notification.CLICK"/>
        </intent-filter>
      </receiver>
```

En el método `onCreate()` de tu actividad principal, añade la siguiente línea, que registrará tu aplicación en Baidu y empezará a escuchar los mensajes push entrantes. Asegúrate de sustituir "Your-API-Key" por la clave de API de Baidu de tu proyecto.

```
PushManager.startWork(getApplicationContext(), PushConstants.LOGIN_TYPE_API_KEY, "Your-API-Key");
```

Por último, tendrás que registrar a tus usuarios en Braze. En el método `onBind()` del receptor de difusión de Baidu que has creado en este paso, envía el `channelId` a Braze utilizando `Braze.registerAppboyPushMessages(channelId)`.

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).setRegisteredPushToken(channelId);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).setRegisteredPushToken(channelId)
```

{% endtab %}
{% endtabs %}

## Paso 5: El registro de push se abre

Baidu admite el envío de pares clave-valor adicionales con mensajes push en formato JSON. Se llamará al método `public void onNotificationClicked(Context context, String title, String description, String customContentString)` de tu receptor de difusión cada vez que un usuario haga clic en un mensaje push entrante. El parámetro `customContentString` contiene los extras en formato JSON. Todos los mensajes de Braze contendrán los dos siguientes pares clave-valor:

  ```json
  {
    "source": "Appboy",
    "cid": "your-campaign-Id"
  }
  ```

Siempre que se llame a `onNotificationClicked`, tu receptor de Baidu debe enviar una [Intención][44] a tu aplicación que contenga `customContentString`. Tu aplicación registrará el clic en Braze utilizando la dirección `customContentString`.

El siguiente código de ejemplo pasa `customContentString` a Braze y registra un clic:

{% tabs %}
{% tab JAVA %}

  ```java
  String customContentString = intent.getStringExtra(ChinaPushMessageReceiver.NOTIFICATION_CLICKED_KEY);
  BrazeNotificationUtils.logBaiduNotificationClick(mApplicationContext, customContentString);
  ```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val customContentString = intent.getStringExtra(ChinaPushMessageReceiver.NOTIFICATION_CLICKED_KEY)
BrazeNotificationUtils.logBaiduNotificationClick(context, customContentString)
```

{% endtab %}
{% endtabs %}

## Paso 6: Extras

Aparte de las claves reservadas utilizadas por Braze, el parámetro `customContentString` también contendrá todos los pares clave-valor personalizados definidos por el usuario. Para extraer tus pares clave-valor, envuelve `customContentString` en un JSONObject y recupera tus extras:

{% tabs %}
{% tab JAVA %}

```java
try {
  JSONObject myExtras = new JSONObject(customContentString);
  String myValue = myExtras.optString("my_key", null);
} catch (Exception e) {
  Log.e(TAG, "Caught an exception processing customContentString");
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
try {
  val myExtras = JSONObject(customContentString)
  val myValue = myExtras.optString("my_key", null)
} catch (e: Exception) {
  Log.e(TAG, "Caught an exception processing customContentString", e)
}
```

{% endtab %}
{% endtabs %}

## Paso 7: Configurar las teclas de Baidu

Tienes que introducir tu clave de API de Baidu y tu clave secreta de Baidu en el panel de Braze. Ambas teclas están disponibles en la consola de la aplicación Baidu.

En la página **Administrar configuración**, selecciona tu aplicación Android China e introduce tu clave de API de Baidu y tu clave secreta de Baidu en la sección de notificaciones push.

![][19]{: style="max-width:80%;"}

## Recursos adicionales

- [Portal Baidu][7]
- [Portal del desarrollador de Baidu][36]
- [Portal del proyecto Baidu][11]
- [Portal SDK push de Baidu][40]
- [Documentación sobre la integración con Baidu][43]

[7]: https://www.baidu.com/
[10]: {% image_buster /assets/img_archive/baidu_project.png %}
[11]: http://developer.baidu.com/console#app/project
[13]: {% image_buster /assets/img_archive/baidu_dev_reg.png %}
[14]: {% image_buster /assets/img_archive/baidu_app_console.png %}
[17]: {% image_buster /assets/img_archive/baidu_signup.png %}
[19]: {% image_buster /assets/img_archive/baidu_api_key.png %} "APIKey"
[26]: {% image_buster /assets/img_archive/baidu_app_name.png %}
[29]: {% image_buster /assets/img_archive/baidu_continue.png %}
[33]: {% image_buster /assets/img_archive/baidu_portal.png %}
[34]: {% image_buster /assets/img_archive/baidu_email.png %}
[35]: {% image_buster /assets/img_archive/baidu_text.png %}
[36]: http://developer.baidu.com/
[37]: {% image_buster /assets/img_archive/baidu_dev_portal.png %}
[38]: {% image_buster /assets/img_archive/baidu_login_dialog.png %}
[39]: {% image_buster /assets/img_archive/baidu_configure_cloud.png %}
[40]: http://developer.baidu.com/wiki/index.php?title=docs/cplat/push/sdk/clientsdk
[41]: {% image_buster /assets/img_archive/baidu_sdk.png %}
[43]: http://developer.baidu.com/wiki/index.php?title=docs/frontia/guide-android/overview
[44]: http://developer.android.com/reference/android/content/Intent.html
