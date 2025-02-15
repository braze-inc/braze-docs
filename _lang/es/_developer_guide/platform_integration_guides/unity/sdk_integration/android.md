---
nav_title: Android
article_title: Integración de SDK Android para Unity
platform: 
  - Unity
  - Android
page_order: 0
description: "Este artículo de referencia cubre la integración de SDK de Android para la plataforma Unity."
search_rank: .9
---

# Integración de SDK Android

> Este artículo de referencia cubre la integración de SDK de Android para la plataforma Unity. Sigue estas instrucciones para hacer que Braze funcione en tu aplicación Unity.

## Paso 1: Elige tu paquete Braze Unity

El [`.unitypackage`](https://docs.unity3d.com/Manual/AssetPackages.html) de Braze incluye enlaces nativos para las plataformas Android e iOS, junto con una interfaz en C#.

Hay varios paquetes de Braze Unity disponibles para su descarga en la [página de versiones de Braze Unity](https://github.com/Appboy/appboy-unity-sdk/releases):
 
- `Appboy.unitypackage`
    - Este paquete incluye los SDK para Android e iOS de Braze y la dependencia [SDWebImage](https://github.com/SDWebImage/SDWebImage) para el SDK de iOS, que es necesaria para el correcto funcionamiento de la mensajería dentro de la aplicación de Braze y las características de las tarjetas de contenido en iOS. El framework SDWebImage se utiliza para descargar y mostrar imágenes, incluidos los GIF. Si pretendes utilizar todas las funciones de Braze, descarga e importa este paquete.
- `Appboy-nodeps.unitypackage`
    - Este paquete es similar a `Appboy.unitypackage`, salvo que no está presente el marco [SDWebImage](https://github.com/SDWebImage/SDWebImage). Este paquete es útil si no quieres que el framework SDWebImage esté presente en tu aplicación iOS.

**iOS**: Para ver si necesitas la dependencia [SDWebImage](https://github.com/SDWebImage/SDWebImage) para tu proyecto iOS, visita la [documentación de mensajes dentro de la aplicación iOS]({{ site.baseurl }}/developer_guide/platform_integration_guides/android/in-app_messaging/integration/).<br>
**Android**: A partir de Unity 2.6.0, el artefacto incluido del SDK de Braze para Android requiere dependencias de [AndroidX](https://developer.android.com/jetpack/androidx). Si antes utilizabas un `jetified unitypackage`, puedes pasar sin problemas al `unitypackage` correspondiente.

## Paso 2: Importa el paquete

En el editor de Unity, importa el paquete a tu proyecto de Unity yendo a **Assets (Activos) > Import Package (Importar paquete) > Custom Package (Paquete personalizado).** A continuación, haz clic en **Importar**.

También puedes seguir las instrucciones de [importación de paquetes de activos de](https://docs.unity3d.com/Manual/AssetPackages.html) Unity para obtener una guía más detallada sobre la importación de paquetes de Unity personalizados. 

{% alert note %}
Si solo deseas importar el plugin para iOS o Android, anula la selección del subdirectorio `Plugins/Android` o `Plugins/iOS` al importar `.unitypackage` de Braze.
{% endalert %}

## Paso 3: Actualizar tu AndroidManifest.xml

Los proyectos Unity de Android requieren la presencia de un archivo [`AndroidManifest.xml`](https://docs.unity3d.com/Manual/android-manifest.html) para ejecutar la aplicación. Además, Braze requiere varias adiciones a tu [`AndroidManifest.xml`](https://docs.unity3d.com/Manual/android-manifest.html) para funcionar.

### Configurar el AndroidManifest.xml

Si tu aplicación no tiene una dirección `AndroidManifest.xml`, puedes utilizar la siguiente plantilla. De lo contrario, si ya tienes un `AndroidManifest.xml`, asegúrate de que cualquiera de las siguientes secciones que faltan se añaden a tu `AndroidManifest.xml` existente.

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
          package="REPLACE_WITH_YOUR_PACKAGE_NAME">

  <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
  <uses-permission android:name="android.permission.INTERNET" />

  <application android:icon="@drawable/app_icon" 
               android:label="@string/app_name">

    <!-- Calls the necessary Braze methods to ensure that analytics are collected and that push notifications are properly forwarded to the Unity application. -->
    <activity android:name="com.braze.unity.BrazeUnityPlayerActivity" 
      android:theme="@style/UnityThemeSelector"
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

    <!-- A Braze specific FirebaseMessagingService used to handle push notifications. -->
    <service android:name="com.braze.push.BrazeFirebaseMessagingService"
      android:exported="false">
      <intent-filter>
        <action android:name="com.google.firebase.MESSAGING_EVENT" />
      </intent-filter>
    </service>
  </application>
</manifest>
```

> Tu `AndroidManifest.xml` debe existir en `Assets/Plugins/Android/AndroidManifest.xml`. Consulta [la documentación de Unity AndroidManifest](https://docs.unity3d.com/Manual/android-manifest.html) para obtener más información.

> Todas las clases de Actividad registradas en tu archivo `AndroidManifest.xml` deben estar totalmente integradas con el SDK para Android de Braze. Si añades tu propia clase de Actividad, debes seguir nuestras [instrucciones de integración de la Actividad de Unity](#extending-braze-unity-player) para asegurarte de que se recopilan los análisis.

{% alert note %}
Tu `AndroidManifest.xml` final sólo debe contener una única Actividad con `"android.intent.category.LAUNCHER"` presente.
{% endalert %}

### Actualiza AndroidManifest.xml con el nombre de tu paquete.

Para encontrar el nombre de tu paquete, haz clic en **Archivo > Configuración de compilación > Configuración del reproductor > pestaña Android.**
![]({% image_buster /assets/img_archive/UnityPackageName.png %})

En tu `AndroidManifest.xml`, todas las instancias de `REPLACE_WITH_YOUR_PACKAGE_NAME` deben sustituirse por tu `Package Name` del paso anterior.

## Paso 4: Añadir dependencias gradle {#unity-android-gradle-configuration}

Para añadir dependencias gradle a tu proyecto Unity, habilita primero ["Plantilla Gradle principal personalizada"](https://docs.unity3d.com/Manual/class-PlayerSettingsAndroid.html#Publishing) en tu configuración de publicación. Esto creará un archivo gradle de plantilla que utilizará tu proyecto. Un archivo gradle se encarga de establecer las dependencias y otras configuraciones del proyecto en tiempo de compilación. Para más información, consulta el ejemplo de aplicación de Unity de Braze [mainTemplate.gradle](https://github.com/braze-inc/braze-unity-sdk/blob/master/unity-samples/Assets/Plugins/Android/mainTemplate.gradle).

Se necesitan las siguientes dependencias:

```groovy
implementation 'com.google.firebase:firebase-messaging:22.0.0'
implementation "androidx.swiperefreshlayout:swiperefreshlayout:1.1.0"
implementation "androidx.recyclerview:recyclerview:1.2.1"
implementation "org.jetbrains.kotlin:kotlin-stdlib:1.6.0"
implementation "org.jetbrains.kotlinx:kotlinx-coroutines-android:1.6.1"
implementation 'androidx.core:core:1.6.0'
```

También puedes establecer estas dependencias utilizando el [Administrador de dependencias externas](https://github.com/googlesamples/unity-jar-resolver).

## Paso 5: Configura el SDK {#unity-static-configuration}

Braze proporciona una solución nativa de Unity para automatizar la integración de Unity con Android. 

1. En el editor de Unity, abre los Ajustes de configuración de Braze navegando hasta **Braze > Braze Configuration (Configuración de Braze)**.
2. Marca la casilla **Automatizar la integración de Android en Unity**.
3. En el campo **Clave de API de Braze**, introduce la clave de API de tu aplicación que se encuentra en **Administrar configuración** desde el panel de Braze.

{% alert note %}
Esta integración automática no debe utilizarse con un archivo `braze.xml` creado manualmente, ya que los valores de configuración pueden entrar en conflicto durante la construcción del proyecto. Si necesitas una `braze.xml` manual, desactiva la integración automática.
{% endalert %}

## Integración de SDK básica completa

Ahora Braze debería estar recopilando datos de tu aplicación, y tu integración básica debería estar completa. Para más información sobre la integración push, consulta los siguientes artículos: [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/push_notifications/android/) e [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/push_notifications/ios/), [mensajes dentro de la aplicación]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/in-app_messaging/) y [tarjetas de contenido]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/content_cards/).

Para conocer las opciones avanzadas de integración de SDK, consulta [Implementación avanzada]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/sdk_integration/advanced_use_cases/#android-sdk-advanced).

