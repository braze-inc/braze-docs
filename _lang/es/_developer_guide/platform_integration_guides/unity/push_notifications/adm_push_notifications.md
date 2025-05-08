---
nav_title: Mensajería para dispositivos de Amazon
article_title: Notificaciones push de mensajería de dispositivos de Amazon para Unity
platform: 
  - Unity
  - Android
page_order: 2
description: "En este artículo de referencia se cubre la integración de notificaciones push de Amazon en Android para la plataforma Unity."
channel: push

---

# Mensajería para dispositivos de Amazon

> En este artículo de referencia se cubre la integración de notificaciones push de Amazon en Android para la plataforma Unity.

Una notificación push es una alerta fuera de la aplicación que aparece en la pantalla del usuario cuando se produce una actualización importante. Las notificaciones push son una forma valiosa de proporcionar a tus usuarios contenido relevante y urgente, o de reactivar su interacción con tu aplicación.

ADM (Mensajería de dispositivos de Amazon) no es compatible con dispositivos que no sean de Amazon. Para probar las notificaciones push de Kindle, debes tener un [dispositivo FireOS](https://developer.amazon.com/appsandservices/apis/engage/device-messaging/tech-docs/04-integrating-your-app-with-adm). Consulta la [sección de ayuda]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/fireos/troubleshooting/) para conocer otras buenas prácticas.

Braze envía notificaciones push a los dispositivos de Amazon utilizando [la mensajería de dispositivos de Amazon (ADM)](https://developer.amazon.com/public/apis/engage/device-messaging).

## Paso 1: Habilitar ADM

1. Crea una cuenta en el [Portal del Desarrollador de Amazon Apps & Games](https://developer.amazon.com/public) si aún no lo has hecho.
2. Obtén [credenciales OAuth (ID de cliente y secreto de cliente) y una clave de API de ADM](https://developer.amazon.com/public/apis/engage/device-messaging/tech-docs/02-obtaining-adm-credentials).
3. **Habilita el Registro Automático de ADM Habilitado** en la ventana de Configuración de Unity Braze. 
  - Alternativamente, puedes añadir la siguiente línea a tu archivo `res/values/braze.xml` para habilitar el registro de ADM:

  ```xml
  <bool name="com_braze_push_adm_messaging_registration_enabled">true</bool>
  ```

## Paso 2: Actualizar Unity AndroidManifest.xml

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

## Paso 3: Almacena tu clave de API de ADM

En primer lugar, [obtén una clave de API de ADM para tu aplicación](https://developer.amazon.com/public/apis/engage/device-messaging/tech-docs/02-obtaining-adm-credentials).  A continuación, guarda tu clave de API de ADM en un archivo llamado `api_key.txt` y guárdalo en la carpeta de tu proyecto [`Assets/`](https://docs.unity3d.com/Manual/AndroidAARPlugins.html) de tu proyecto.

Amazon no reconocerá tu clave si `api_key.txt` contiene algún carácter de espacio en blanco, como un salto de línea final.

En tu archivo `mainTemplate.gradle`, añade lo siguiente:

```gradle
task copyAmazon(type: Copy) {
    def unityProjectPath = $/file:///**DIR_UNITYPROJECT**/$.replace("\\", "/")
    from unityProjectPath + '/Assets/api_key.txt'
    into new File(projectDir, 'src/main/assets')
}

preBuild.dependsOn(copyAmazon)
```

## Paso 4: Añadir archivo jar de ADM

El archivo jar ADM necesario puede colocarse en cualquier lugar de tu proyecto de acuerdo con la [documentación JAR de Unity](https://docs.unity3d.com/Manual/AndroidJARPlugins.html).

## Paso 5: Añadir el secreto de cliente y el ID de cliente a tu panel de Braze

Por último, debes añadir el secreto de cliente y el ID de cliente que obtuviste en [el paso 1](#step-1-enable-adm) a la página **Administrar configuración** del panel de Braze.

![]({% image_buster /assets/img_archive/fire_os_dashboard.png %})

