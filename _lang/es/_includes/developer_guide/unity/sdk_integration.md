## Acerca del SDK de Unity Braze

Para ver una lista completa de tipos, funciones, variables y demás, consulta el [Archivo de Declaraciones de Unity](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/BrazePlatform.cs). Además, si ya has integrado Unity manualmente para iOS, puedes cambiar [a una integración automatizada](#unity_automated-integration).

## Integración del SDK de Unity

### Requisitos previos

Antes de empezar, comprueba que tu entorno es compatible con la [última versión del SDK de Unity de Braze](https://github.com/braze-inc/braze-unity-sdk/releases).

### Paso 1: Elige tu paquete Braze Unity

{% tabs %}
{% tab Android %}
El [`.unitypackage`](https://docs.unity3d.com/Manual/AssetPackages.html) de Braze incluye enlaces nativos para las plataformas Android e iOS, junto con una interfaz en C#.

Hay varios paquetes de Braze Unity disponibles para su descarga en la [página de versiones de Braze Unity](https://github.com/Appboy/appboy-unity-sdk/releases):
 
- `Appboy.unitypackage`
    - Este paquete incluye los SDK para Android e iOS de Braze y la dependencia [SDWebImage](https://github.com/SDWebImage/SDWebImage) para el SDK de iOS, que es necesaria para el correcto funcionamiento de la mensajería dentro de la aplicación de Braze y las características de las tarjetas de contenido en iOS. El framework SDWebImage se utiliza para descargar y mostrar imágenes, incluidos los GIF. Si pretendes utilizar todas las funciones de Braze, descarga e importa este paquete.
- `Appboy-nodeps.unitypackage`
    - Este paquete es similar a `Appboy.unitypackage`, salvo que no está presente el marco [SDWebImage](https://github.com/SDWebImage/SDWebImage). Este paquete es útil si no quieres que el framework SDWebImage esté presente en tu aplicación iOS.

{% alert note %}
A partir de Unity 2.6.0, el artefacto incluido del SDK de Braze para Android requiere dependencias de [AndroidX](https://developer.android.com/jetpack/androidx). Si antes utilizabas un `jetified unitypackage`, puedes pasar sin problemas al `unitypackage` correspondiente.
{% endalert %}
{% endtab %}

{% tab Swift %}
El [`.unitypackage`](https://docs.unity3d.com/Manual/AssetPackages.html) de Braze incluye enlaces nativos para las plataformas Android e iOS, junto con una interfaz en C#.

El paquete Braze Unity está disponible para su descarga en la [página de versiones de Braze Unity](https://github.com/Appboy/appboy-unity-sdk/releases) con dos opciones de integración:

1. `Appboy.unitypackage` solo
  - Este paquete incluye los SDK de Braze para Android e iOS sin dependencias adicionales. Con este método de integración, no funcionarán correctamente las características de mensajería dentro de la aplicación de Braze ni las tarjetas de contenido en iOS. Si quieres utilizar todas las funciones de Braze sin código personalizado, utiliza la opción siguiente.
  - Para utilizar esta opción de integración, asegúrate de que la casilla junto a `Import SDWebImage dependency` *no está marcada* en la interfaz de usuario de Unity, en "Configuración de Braze".
2. `Appboy.unitypackage` con `SDWebImage`
  - Esta opción de integración incluye los SDK de Braze para Android e iOS y la dependencia de [SDWebImage](https://github.com/SDWebImage/SDWebImage) para el SDK de iOS, que es necesaria para el correcto funcionamiento de la mensajería dentro de la aplicación de Braze y las características de las tarjetas de contenido en iOS. El framework `SDWebImage` se utiliza para descargar y mostrar imágenes, incluidos los GIF. Si pretendes utilizar todas las funciones de Braze, descarga e importa este paquete.
  - Para importar automáticamente `SDWebImage`, asegúrate de *marcar* la casilla junto a `Import SDWebImage dependency` en la interfaz de usuario de Unity, en "Configuración de Braze".

{% alert note %}
Para ver si necesitas la dependencia [SDWebImage](https://github.com/SDWebImage/SDWebImage) para tu proyecto iOS, visita la [documentación de mensajes dentro de la aplicación iOS]({{ site.baseurl }}/developer_guide/platform_integration_guides/swift/in-app_messaging/overview/).
{% endalert %}
{% endtab %}
{% endtabs %}

### Paso 2: Importa el paquete

{% tabs %}
{% tab Android %}
En el editor de Unity, importa el paquete a tu proyecto de Unity yendo a **Assets (Activos) > Import Package (Importar paquete) > Custom Package (Paquete personalizado).** A continuación, haz clic en **Importar**.

También puedes seguir las instrucciones de [importación de paquetes de activos de](https://docs.unity3d.com/Manual/AssetPackages.html) Unity para obtener una guía más detallada sobre la importación de paquetes de Unity personalizados. 

{% alert note %}
Si solo deseas importar el plugin para iOS o Android, anula la selección del subdirectorio `Plugins/Android` o `Plugins/iOS` al importar `.unitypackage` de Braze.
{% endalert %}
{% endtab %}

{% tab Swift %}
En el editor de Unity, importa el paquete a tu proyecto de Unity yendo a **Assets (Activos) > Import Package (Importar paquete) > Custom Package (Paquete personalizado).** A continuación, haz clic en **Importar**.

También puedes seguir las instrucciones de [importación de paquetes de activos de](https://docs.unity3d.com/Manual/AssetPackages.html) Unity para obtener una guía más detallada sobre la importación de paquetes de Unity personalizados. 

{% alert note %}
Si solo deseas importar el plugin para iOS o Android, anula la selección del subdirectorio `Plugins/Android` o `Plugins/iOS` al importar `.unitypackage` de Braze.
{% endalert %}
{% endtab %}
{% endtabs %}

### Paso 3: Configura el SDK

{% tabs %}
{% tab Android %}
#### Paso 3.1: Configura `AndroidManifest.xml`

Cumplir [`AndroidManifest.xml`](https://docs.unity3d.com/Manual/android-manifest.html) funcionar. Si tu aplicación no tiene una dirección `AndroidManifest.xml`, puedes utilizar la siguiente plantilla. De lo contrario, si ya tienes un `AndroidManifest.xml`, asegúrate de que cualquiera de las siguientes secciones que faltan se añaden a tu `AndroidManifest.xml` existente.

1. Ve al directorio `Assets/Plugins/Android/` y abre tu archivo `AndroidManifest.xml`. Esta es la [ubicación predeterminada en el editor de Unity](https://docs.unity3d.com/Manual/android-manifest.html).
2. En tu `AndroidManifest.xml`, añade los permisos y actividades necesarios de la siguiente plantilla.
3. Cuando hayas terminado, tu `AndroidManifest.xml` sólo debe contener una única Actividad con `"android.intent.category.LAUNCHER"` presente.

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

{% alert important %}
Todas las clases de Actividad registradas en tu archivo `AndroidManifest.xml` deben estar totalmente integradas con el SDK para Android de Braze, de lo contrario no se recopilarán tus análisis. Si añades tu propia clase de Actividad, asegúrate de [extender el reproductor Unity de Braze](#unity_extend-unity-player) para evitarlo.
{% endalert %}

#### Paso 3.2: Actualiza `AndroidManifest.xml` con el nombre de tu paquete.

Para encontrar el nombre de tu paquete, haz clic en **Archivo > Configuración de compilación > Configuración del reproductor > pestaña Android.**

![]({% image_buster /assets/img_archive/UnityPackageName.png %})

En tu `AndroidManifest.xml`, todas las instancias de `REPLACE_WITH_YOUR_PACKAGE_NAME` deben sustituirse por tu `Package Name` del paso anterior.

#### Paso 3.3: Añadir dependencias gradle

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

#### Paso 3.4: Automatización de la integración de Unity con Android

Braze proporciona una solución nativa de Unity para automatizar la integración de Unity con Android. 

1. En el editor de Unity, abre los Ajustes de configuración de Braze navegando hasta **Braze > Braze Configuration (Configuración de Braze)**.
2. Marca la casilla **Automatizar la integración de Android en Unity**.
3. En el campo **Clave de API de Braze**, introduce la clave de API de tu aplicación que se encuentra en **Administrar configuración** desde el panel de Braze.

{% alert note %}
Esta integración automática no debe utilizarse con un archivo `braze.xml` creado manualmente, ya que los valores de configuración pueden entrar en conflicto durante la construcción del proyecto. Si necesitas una `braze.xml` manual, desactiva la integración automática.
{% endalert %}
{% endtab %}

{% tab Swift %}
#### Paso 3.1: Configura tu clave de API

Braze proporciona una solución nativa de Unity para automatizar la integración de Unity en iOS. Esta solución modifica el proyecto creado en Xcode utilizando [`PostProcessBuildAttribute`](http://docs.unity3d.com/ScriptReference/Callbacks.PostProcessBuildAttribute.html) de Unity y subclasifica el `UnityAppController` utilizando la macro `IMPL_APP_CONTROLLER_SUBCLASS`.

1. En el editor de Unity, abre los Ajustes de configuración de Braze navegando hasta **Braze > Braze Configuration (Configuración de Braze)**.
2. Marca la casilla **Automatizar la integración de Unity iOS**.
3. En el campo **Clave de API de Braze**, introduce la clave de API de tu aplicación que se encuentra en **Administrar configuración**.

![]({% image_buster /assets/img_archive/unity-ios-appboyconfig.png %})

Si tu aplicación ya está utilizando otra subclase de `UnityAppController`, tendrás que fusionar la implementación de tu subclase con `AppboyAppDelegate.mm`.
{% endtab %}
{% endtabs %}

## Personalizar el paquete Unity

### Paso 1: Clonar el repositorio

En tu terminal, clona el [repositorio de GitHub del SDK de Unity de Braze](https://github.com/braze-inc/braze-unity-sdk) y, a continuación, navega hasta esa carpeta:

{% tabs local %}
{% tab MacOS %}
```bash
git clone git@github.com:braze-inc/braze-unity-sdk.git
cd ~/PATH/TO/DIRECTORY/braze-unity-sdk
```
{% endtab %}

{% tab Windows Powershell %}
```powershell
git clone git@github.com:braze-inc/braze-unity-sdk.git
cd C:\PATH\TO\DIRECTORY\braze-unity-sdk
```
{% endtab %}
{% endtabs %}

### Paso 2: Exportar paquete desde repositorio

En primer lugar, inicia Unity y mantenlo en ejecución en segundo plano. A continuación, en la raíz del repositorio, ejecuta el siguiente comando para exportar el paquete a `braze-unity-sdk/unity-package/`.

{% tabs local %}
{% tab MacOS %}
```bash
/Applications/Unity/Unity.app/Contents/MacOS/Unity -batchmode -nographics -projectPath "$(pwd)" -executeMethod Appboy.Editor.Build.ExportAllPackages -quit
```
{% endtab %}

{% tab Windows Powershell %}
```powershell
"%UNITY_PATH%" -batchmode -nographics -projectPath "%PROJECT_ROOT%" -executeMethod Appboy.Editor.Build.ExportAllPackages -quit	
```
{% endtab %}
{% endtabs %}

{% alert tip %}
Si experimentas algún problema después de ejecutar estos comandos, consulta [Unity: Argumentos de la línea de comandos](https://docs.unity3d.com/2017.2/Documentation/Manual/CommandLineArguments.html).
{% endalert %}

### Paso 3: Importar paquete a Unity

1. En Unity, importa el paquete deseado a tu proyecto Unity navegando a **Activos** > **Importar paquete** > Paquete personalizado.
2. Si hay algún archivo que no quieres importar, desactívalo ahora.
3. Personaliza el paquete Unity exportado ubicado en `Assets/Editor/Build.cs`.

## Cambiar a una integración automatizada (sólo Swift) {#automated-integration}

Para aprovechar la integración automatizada de iOS que ofrece el SDK Braze Unity, sigue estos pasos para pasar de una integración manual a una automatizada.

1. Elimina todo el código relacionado con Braze de la subclase `UnityAppController` de tu proyecto Xcode.
2. Elimina las bibliotecas Braze iOS de tu proyecto Unity o Xcode (como `Appboy_iOS_SDK.framework` y `SDWebImage.framework`).
3. Importa de nuevo el paquete Braze Unity a tu proyecto. Para un recorrido completo, consulta [Paso 2: Importa el paquete](#unity_step-2-import-the-package).
4. Vuelve a configurar tu clave de API. Para un recorrido completo, consulta [Paso 3.1: Configura tu clave de API](#unity_step-31-set-your-api-key).

## Configuraciones opcionales

### Registro detallado

Para habilitar el registro detallado en el editor de Unity, haz lo siguiente:

1. Abre los ajustes de configuración de Braze navegando hasta **Braze** > **Configuración de Braze**.
2. Haz clic en el menú desplegable **Mostrar configuración de Android Braze**.
3. En el campo **Nivel de registro SDK**, introduce el valor "0".

### Compatibilidad con Prime 31

Para utilizar el plugin Unity de Braze con los plugins de Prime31, edita la página `AndroidManifest.xml` de tu proyecto para utilizar las clases de Actividad compatibles con Prime31. Cambia todas las referencias de
`com.braze.unity.BrazeUnityPlayerActivity` a `com.braze.unity.prime31compatible.BrazeUnityPlayerActivity`

### Mensajería de dispositivos de Amazon (ADM)

Braze soporta la integración de [ADM push](https://developer.amazon.com/public/apis/engage/device-messaging) en aplicaciones Unity. Si quieres integrar ADM push, crea un archivo llamado `api_key.txt` que contenga tu clave de API de ADM y colócalo en la carpeta `Plugins/Android/assets/`.  Para más información sobre la integración de ADM con Braze, visita nuestras [instrucciones de integración push de ADM]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=unity).

### Ampliar el reproductor Braze Unity (sólo Android) {#extend-unity-player}

El archivo de ejemplo `AndroidManifest.xml` proporcionado tiene registrada una clase de Actividad, [`BrazeUnityPlayerActivity`](https://github.com/braze-inc/braze-android-sdk/blob/e804cb3a10ae68364b354b52abf1bef8a0d1a9dc/android-sdk-unity/src/main/java/com/braze/unity/BrazeUnityPlayerActivity.kt). Esta clase está integrada con el SDK de Braze y amplía `UnityPlayerActivity` con gestión de sesiones, registro de mensajes dentro de la aplicación, registro de análisis de notificaciones push y mucho más. Consulta [Unity](https://docs.unity3d.com/Manual/AndroidUnityPlayerActivity.html) para obtener más información sobre la ampliación de la clase `UnityPlayerActivity`.

Si estás creando tu propio `UnityPlayerActivity` personalizado en un proyecto de biblioteca o de plugin, tendrás que ampliar nuestro `BrazeUnityPlayerActivity` para integrar tu funcionalidad personalizada con Braze. Antes de empezar a trabajar en la ampliación de `BrazeUnityPlayerActivity`, sigue nuestras instrucciones para integrar Braze en tu proyecto Unity.

1. Añade el SDK para Android de Braze como dependencia a tu proyecto de biblioteca o plugin, tal y como se describe en [las instrucciones de integración de SDK para Android de Braze]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android).
2. Integra nuestro Unity `.aar`, que contiene nuestra funcionalidad específica de Unity, a tu proyecto de biblioteca Android que estás construyendo para Unity. El `appboy-unity.aar` está disponible en nuestro [repositorio público](https://github.com/braze-inc/braze-unity-sdk/tree/master/Assets/Plugins/Android). Una vez que nuestra biblioteca Unity se haya integrado correctamente, modifica tu `UnityPlayerActivity` para ampliar `BrazeUnityPlayerActivity`.
3. Exporta tu proyecto de biblioteca o plugin y colócalo en `/<your-project>/Assets/Plugins/Android` de la forma habitual. No incluyas ningún código fuente de Braze en tu biblioteca o plugin, ya que ya estarán presentes en `/<your-project>/Assets/Plugins/Android`.
4. Edita tu `/<your-project>/Assets/Plugins/Android/AndroidManifest.xml` para especificar tu subclase `BrazeUnityPlayerActivity` como actividad principal.

Ahora deberías poder empaquetar un `.apk` desde el IDE de Unity que esté totalmente integrado con Braze y contenga tu funcionalidad personalizada de `UnityPlayerActivity`.

## Solución de problemas

### Error: "No se ha podido leer el archivo"

Los errores parecidos a los siguientes pueden ignorarse con seguridad. El software de Apple utiliza una extensión PNG propietaria llamada CgBI, que Unity no reconoce. Estos errores no afectarán a tu compilación de iOS ni a la correcta visualización de las imágenes asociadas en el paquete Braze.

```
Could not create texture from Assets/Plugins/iOS/AppboyKit/Appboy.bundle/...png: File could not be read
```
