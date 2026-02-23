{% multi_lang_include developer_guide/prerequisites/unity.md %}

## Configuración de la notificación push

### Paso 1: Configurar la plataforma

{% tabs %}
{% tab Android %}
#### Paso 1.1: Habilitar Firebase

Para empezar, sigue la [documentación de configuración de Firebase Unity](https://firebase.google.com/docs/unity/setup).

{% alert note %}
La integración del SDK Unity de Firebase puede hacer que se anule tu `AndroidManifest.xml`. Si eso ocurre, asegúrate de revertirlo al original.
{% endalert %}

#### Paso 1.2: Configura tus credenciales de Firebase

Tienes que introducir tu clave de servidor Firebase y tu ID de remitente en el panel de Braze. Para ello, accede a [la consola de desarrolladores de Firebase](https://console.firebase.google.com/) y selecciona tu proyecto Firebase. A continuación, selecciona **Mensajería en la nube** en **Configuración** y copia la clave del servidor y el ID del remitente:<br>![]({% image_buster /assets/img_archive/finding_firebase_server_key.png %} "FirebaseServerKey")

En Braze, selecciona tu aplicación Android en la página **Configuración de la aplicación**, en **Administrar configuración**. A continuación, introduce tu clave de servidor de Firebase en el campo **Clave de servidor de mensajería en la nube de Firebase** y el ID de remitente de Firebase en el campo ID de **remitente de mensajería en la nube de Firebase**.

![]({% image_buster /assets/img_archive/fcm_api_insert.png %} "FCMKey")
{% endtab %}

{% tab Swift %}
#### Paso 1.1: Verifica el método de integración

Braze proporciona una solución nativa de Unity para automatizar las integraciones push de iOS. Si prefieres configurar y administrar tu integración manualmente, consulta [Swift: Notificaciones push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift).

De lo contrario, continúa con el siguiente paso.

{% alert note %}
Nuestra solución de notificación push automática aprovecha la característica de Autorización Provisional de iOS 12 y no se puede utilizar con la ventana emergente de notificación push nativa.
{% endalert %}
{% endtab %}

{% tab Amazon Device Messaging %}
#### Paso 1.1: Habilitar ADM

1. Crea una cuenta en el [Portal del Desarrollador de Amazon Apps & Games](https://developer.amazon.com/public) si aún no lo has hecho.
2. Obtén [credenciales OAuth (ID de cliente y secreto de cliente) y una clave de API de ADM](https://developer.amazon.com/public/apis/engage/device-messaging/tech-docs/02-obtaining-adm-credentials).
3. **Habilita el Registro Automático de ADM Habilitado** en la ventana de Configuración de Unity Braze. 
  - Alternativamente, puedes añadir la siguiente línea a tu archivo `res/values/braze.xml` para habilitar el registro de ADM:

  ```xml
  <bool name="com_braze_push_adm_messaging_registration_enabled">true</bool>
  ```
{% endtab %}
{% endtabs %}

### Paso 2: Configurar notificaciones push

{% tabs %}
{% tab Android %}
#### Paso 2.1: Configurar los ajustes push

El SDK de Braze puede gestionar automáticamente el registro push con los servidores de mensajería en la nube de Firebase para que los dispositivos reciban notificaciones push. En Unity, habilita **Automatizar integración Android de Unity** y, a continuación, configura los siguientes ajustes de **notificación push**.

| Configuración                                | Descripción                                                                                                                                              |
|----------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Habilitado el registro automático de mensajería en la nube Firebase | Ordena al SDK de Braze que recupere y envíe automáticamente un token de notificaciones push de FCM para un dispositivo.                                                                |
| ID de remitente de Firebase Cloud Messaging     | El ID de remitente de tu consola Firebase.                                                                                                                |
| Gestiona los vínculos profundos push automáticamente    | Si el SDK debe gestionar la apertura de vínculos profundos o la apertura de la aplicación cuando se hace clic en las notificaciones push.                                                  |
| Pequeño icono de notificación Dibujable       | El dibujable debe mostrarse como el icono pequeño siempre que se reciba una notificación push. La notificación utilizará el icono de la aplicación como icono pequeño si no se proporciona ningún icono. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% endtab %}

{% tab Swift %}
#### Paso 2.1: Sube tu token de APNs

{% multi_lang_include developer_guide/swift/apns_token.md %}

#### Paso 2.2: Habilitar push automático

Abre los ajustes de configuración de Braze en el editor de Unity navegando hasta **Braze > Configuración de Braze**.

Marca **Integrar Push con Braze** para registrar automáticamente usuarios para notificaciones push, pasar tokens de notificaciones push a Braze, hacer un seguimiento de los análisis de aperturas push y aprovechar nuestra gestión predeterminada de notificaciones push.

#### Paso 2.3: Habilitar push en segundo plano (opcional)

Marca **Activar Push en segundo plano** si quieres habilitar `background mode` para las notificaciones push. Esto permite al sistema despertar tu aplicación del estado `suspended` cuando llega una notificación push, habilitando tu aplicación para descargar contenido en respuesta a las notificaciones push. Marcar esta opción es necesario para nuestra funcionalidad de seguimiento de la desinstalación.

![El editor de Unity muestra las opciones de configuración de Braze. En este editor están habilitadas las opciones "Automatizar la integración de Unity con iOS", "Integrar push con Braze" y "Habilitar push en segundo plano".]({% image_buster /assets/img/unity/ios/unity_ios_enable_background.png %})

#### Paso 2.4: Desactivar el registro automático (opcional)

Los usuarios que aún no hayan optado por la adhesión voluntaria a las notificaciones push serán autorizados automáticamente a recibir notificaciones push al abrir tu aplicación. Para desactivar esta característica y registrar manualmente a los usuarios para push, marca **Desactivar registro push automático**.

- Si la opción **Desactivar autorización provisional** no está marcada en iOS 12 o posterior, el usuario estará autorizado provisionalmente (de forma silenciosa) a recibir push silenciosos. Si está marcada, se mostrará al usuario el aviso push nativo.
- Si necesitas configurar exactamente cuándo se muestra el aviso en tiempo de ejecución, desactiva el registro automático desde el editor de configuración de Braze y utiliza en su lugar `AppboyBinding.PromptUserForPushPermissions()`.

![El editor de Unity muestra las opciones de configuración de Braze. En este editor están habilitadas las opciones "Automatizar la integración de Unity en iOS", "Integrar push con Braze" y "Desactivar el registro push automático".]({% image_buster /assets/img/unity/ios/unity_ios_disable_auto_push.png %})
{% endtab %}

{% tab Amazon Device Messaging %}
#### Paso 2.1: Actualiza `AndroidManifest.xml`

Si tu aplicación no tiene una dirección `AndroidManifest.xml`, puedes utilizar la siguiente plantilla. De lo contrario, si ya tienes un `AndroidManifest.xml`, asegúrate de que cualquiera de las siguientes secciones que faltan se añaden a tu `AndroidManifest.xml` existente.

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
          package="REPLACE_WITH_YOUR_PACKAGE_NAME">

  <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
  <uses-permission android:name="android.permission.INTERNET" />
  <permission
    android:name="REPLACE_WITH_YOUR_PACKAGE_NAME.permission.RECEIVE_ADM_MESSAGE"
    android:protectionLevel="signature" />
  <uses-permission android:name="REPLACE_WITH_YOUR_PACKAGE_NAME.permission.RECEIVE_ADM_MESSAGE" />
  <uses-permission android:name="com.amazon.device.messaging.permission.RECEIVE" />

  <application android:icon="@drawable/app_icon" 
               android:label="@string/app_name">

    <!-- Calls the necessary Braze methods to ensure that analytics are collected and that push notifications are properly forwarded to the Unity application. -->
    <activity android:name="com.braze.unity.BrazeUnityPlayerActivity" 
      android:label="@string/app_name" 
      android:configChanges="fontScale|keyboard|keyboardHidden|locale|mnc|mcc|navigation|orientation|screenLayout|screenSize|smallestScreenSize|uiMode|touchscreen" 
      android:screenOrientation="sensor">
      <meta-data android:name="android.app.lib_name" android:value="unity" />
      <meta-data android:name="unityplayer.ForwardNativeEventsToDalvik" android:value="true" />
      <intent-filter>
        <action android:name="android.intent.action.MAIN" />
        <category android:name="android.intent.category.LAUNCHER" />
      </intent-filter>
    </activity>

    <receiver android:name="com.braze.push.BrazeAmazonDeviceMessagingReceiver" android:permission="com.amazon.device.messaging.permission.SEND">
      <intent-filter>
          <action android:name="com.amazon.device.messaging.intent.RECEIVE" />
          <action android:name="com.amazon.device.messaging.intent.REGISTRATION" />
          <category android:name="REPLACE_WITH_YOUR_PACKAGE_NAME" />
      </intent-filter>
    </receiver>
  </application>
</manifest>
```

#### Paso 2.2: Almacena tu clave de API de ADM

En primer lugar, [genera una clave de API ADM para tu aplicación](https://developer.amazon.com/public/apis/engage/device-messaging/tech-docs/02-obtaining-adm-credentials), luego guarda la clave en un archivo llamado `api_key.txt` y añádelo al directorio [`Assets/`](https://docs.unity3d.com/Manual/AndroidAARPlugins.html) de tu proyecto.

{% alert important %}
Amazon no reconocerá tu clave si `api_key.txt` contiene algún carácter de espacio en blanco, como un salto de línea final.
{% endalert %}

A continuación, en tu archivo `mainTemplate.gradle`, añade lo siguiente:

```gradle
task copyAmazon(type: Copy) {
    def unityProjectPath = $/file:///**DIR_UNITYPROJECT**/$.replace("\\", "/")
    from unityProjectPath + '/Assets/api_key.txt'
    into new File(projectDir, 'src/main/assets')
}

preBuild.dependsOn(copyAmazon)
```

#### Paso 2.3: Añadir archivo jar de ADM

El archivo jar ADM necesario puede colocarse en cualquier lugar de tu proyecto de acuerdo con la [documentación JAR de Unity](https://docs.unity3d.com/Manual/AndroidJARPlugins.html).

#### Paso 2.4: Añadir el secreto de cliente y el ID de cliente a tu panel de Braze

Por último, debes añadir el secreto de cliente y el ID de cliente que obtuviste en [el paso 1](#unity_step-1-enable-adm) a la página **Administrar configuración** del panel de Braze.

![]({% image_buster /assets/img_archive/fire_os_dashboard.png %})
{% endtab %}
{% endtabs %}

### Paso 3: Configurar escuchas push

{% tabs %}
{% tab Android %}
#### Paso 3.1: Habilitar la escucha push recibida

El receptor de notificaciones push se activa cuando un usuario recibe una notificación push. Para enviar la carga útil push a Unity, establece el nombre de tu objeto del juego y el método de devolución de llamada del receptor push en **Establecer receptor push**.

#### Paso 3.2: Habilitar la escucha abierta push

El receptor push abierto se activa cuando un usuario inicia la aplicación haciendo clic en una notificación push. Para enviar la carga útil de push a Unity, establece el nombre de tu objeto del juego y el método de devolución de llamada de escucha abierta push en **Establecer escucha abierta push**.

#### Paso 3.3: Habilitar la escucha push eliminada

El receptor de notificaciones push eliminadas se activa cuando un usuario elimina o rechaza una notificación push. Para enviar la carga útil de push a Unity, establece el nombre de tu objeto del juego y el método de devolución de llamada de escucha eliminada push en **Establecer escucha eliminada push**.

#### Ejemplo de receptor push

En el siguiente ejemplo se implementa el objeto del juego `BrazeCallback` utilizando un nombre de método de devolución de llamada de `PushNotificationReceivedCallback`, `PushNotificationOpenedCallback` y `PushNotificationDeletedCallback` respectivamente.

![Este gráfico de ejemplo de implementación muestra las opciones de configuración de Braze mencionadas en las secciones anteriores y un fragmento de código en C#.]({% image_buster /assets/img/unity/android/unity_android_full_push_listener.png %} "Android Full Listener Example")

```csharp
public class MainMenu : MonoBehaviour {
  void PushNotificationReceivedCallback(string message) {
#if UNITY_ANDROID
    Debug.Log("PushNotificationReceivedCallback message: " + message);
    PushNotification pushNotification = new PushNotification(message);
    Debug.Log("Push Notification received: " + pushNotification);   
#elif UNITY_IOS
    ApplePushNotification pushNotification = new ApplePushNotification(message);
    Debug.Log("Push received Notification event: " + pushNotification);   
#endif  
  }

  void PushNotificationOpenedCallback(string message) {
#if UNITY_ANDROID
    Debug.Log("PushNotificationOpenedCallback message: " + message);
    PushNotification pushNotification = new PushNotification(message);
    Debug.Log("Push Notification opened: " + pushNotification);  
#elif UNITY_IOS
    ApplePushNotification pushNotification = new ApplePushNotification(message);
    Debug.Log("Push opened Notification event: " + pushNotification);   
#endif  
  }

  void PushNotificationDeletedCallback(string message) {
#if UNITY_ANDROID
    Debug.Log("PushNotificationDeletedCallback message: " + message);
    PushNotification pushNotification = new PushNotification(message);
    Debug.Log("Push Notification dismissed: " + pushNotification);  
#endif
  }
}
```
{% endtab %}

{% tab Swift %}
#### Paso 3.1: Habilitar la escucha push recibida

El receptor de notificaciones push se activa cuando un usuario recibe una notificación push mientras utiliza activamente la aplicación (por ejemplo, cuando la aplicación está en primer plano). Configura la escucha push recibida en el editor de configuración de Braze. Si necesitas configurar la escucha de tu objeto del juego en tiempo de ejecución, utiliza `AppboyBinding.ConfigureListener()` y especifica `BrazeUnityMessageType.PUSH_RECEIVED`.

![El editor de Unity muestra las opciones de configuración de Braze. En este editor, se amplía la opción "Establecer receptor de recepción push" y se proporcionan el "Nombre del objeto del juego" (AppBoyCallback) y el "Nombre del método de devolución de llamada" (PushNotificationReceivedCallback).]({% image_buster /assets/img/unity/ios/unity_ios_push_received.png %})

#### Paso 3.2: Habilitar la escucha abierta push

El receptor push abierto se activa cuando un usuario inicia la aplicación haciendo clic en una notificación push. Para enviar la carga útil de push a Unity, establece el nombre de tu objeto del juego y el método de devolución de llamada de la escucha push abierta en la opción **Establecer escucha push abierta**:

![El editor de Unity muestra las opciones de configuración de Braze. En este editor, se amplía la opción "Establecer receptor de recepción push" y se proporcionan el "Nombre del objeto del juego" (AppBoyCallback) y el "Nombre del método de devolución de llamada" (PushNotificationOpenedCallback).]({% image_buster /assets/img/unity/ios/unity_ios_push_opened.png %})

Si necesitas configurar la escucha de tu objeto del juego en tiempo de ejecución, utiliza `AppboyBinding.ConfigureListener()` y especifica `BrazeUnityMessageType.PUSH_OPENED`.

#### Ejemplo de receptor push

El siguiente ejemplo implementa el objeto del juego `AppboyCallback` utilizando un nombre de método de devolución de llamada de `PushNotificationReceivedCallback` y `PushNotificationOpenedCallback`, respectivamente.

![Este gráfico de ejemplo de implementación muestra las opciones de configuración de Braze mencionadas en las secciones anteriores y un fragmento de código en C#.]({% image_buster /assets/img/unity/ios/unity_ios_appboy_callback.png %})

```csharp
public class MainMenu : MonoBehaviour {
  void PushNotificationReceivedCallback(string message) {
#if UNITY_ANDROID
    Debug.Log("PushNotificationReceivedCallback message: " + message);
    PushNotification pushNotification = new PushNotification(message);
    Debug.Log("Push Notification received: " + pushNotification);   
#elif UNITY_IOS
    ApplePushNotification pushNotification = new ApplePushNotification(message);
    Debug.Log("Push received Notification event: " + pushNotification);   
#endif  
  }

  void PushNotificationOpenedCallback(string message) {
#if UNITY_ANDROID
    Debug.Log("PushNotificationOpenedCallback message: " + message);
    PushNotification pushNotification = new PushNotification(message);
    Debug.Log("Push Notification opened: " + pushNotification);  
#elif UNITY_IOS
    ApplePushNotification pushNotification = new ApplePushNotification(message);
    Debug.Log("Push opened Notification event: " + pushNotification);   
#endif  
  }
}
```
{% endtab %}

{% tab Amazon Device Messaging %}
Al actualizar tu `AndroidManifest.xml` en el [paso anterior](#unity_step-21-update-androidmanifestxml), las escuchas push se configuraron automáticamente cuando añadiste las siguientes líneas. Por lo tanto, no es necesaria ninguna otra configuración.

```xml
<action android:name="com.amazon.device.messaging.intent.RECEIVE" />
<action android:name="com.amazon.device.messaging.intent.REGISTRATION" />
```

{% alert note %}
Para saber más sobre las escuchas push de ADM, consulta [Amazon: Integra la mensajería de dispositivos de Amazon](https://developer.amazon.com/docs/video-skills-fire-tv-apps/integrate-adm.html).
{% endalert %}
{% endtab %}
{% endtabs %}

## Configuraciones opcionales

{% tabs %}
{% tab Android %}
#### Vinculación en profundidad a los recursos de la aplicación

Aunque Braze puede gestionar vínculos profundos estándar (como URL de sitios web, URI de Android, etc.) de forma predeterminada, la creación de vínculos profundos personalizados requiere una configuración adicional del Manifiesto.

Para obtener información sobre la configuración, visita [Vinculación en profundidad con recursos de la aplicación](https://developer.android.com/training/app-links/deep-linking).

#### Añadir iconos de notificación push Braze

Para añadir iconos push a tu proyecto, crea un plug-in Android Archive (AAR) o una biblioteca Android que contenga los archivos de imagen de los iconos. Para conocer los pasos y la información, consulta la documentación de Unity: [Proyectos de bibliotecas Android y plug-ins de archivos Android](https://docs.unity3d.com/Manual/AndroidAARPlugins.html).
{% endtab %}

{% tab Swift %}
#### Devolución de llamada de token de notificaciones push

Para recibir una copia de los tokens de dispositivo Braze del SO, establece un delegado mediante `AppboyBinding.SetPushTokenReceivedFromSystemDelegate()`.
{% endtab %}

{% tab Amazon Device Messaging %}
De momento no hay configuraciones opcionales para ADM.
{% endtab %}
{% endtabs %}
