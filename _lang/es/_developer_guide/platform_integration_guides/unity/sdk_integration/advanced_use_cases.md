---
nav_title: Aplicación avanzada
article_title: Implementación avanzada del SDK
platform: 
  - Unity
  - iOS
  - Android
page_order: 2
description: "En este artículo de referencia se cubre la implementación avanzada del SDK para la plataforma Unity."
---

# Aplicación avanzada

> En este artículo de referencia se cubre la implementación avanzada del SDK para la plataforma Unity.

## Personalizar el paquete Unity

Puedes elegir personalizar y exportar el paquete Braze Unity utilizando los scripts proporcionados.

1. Clona el [proyecto GitHub del SDK de Unity de Braze](https://github.com/appboy/appboy-unity-sdk):

	```bash
	git clone git@github.com:braze-inc/braze-unity-sdk.git
	```
2. Desde el directorio `braze-unity-sdk/scripts`, ejecuta `./generate_package.sh` para exportar los paquetes de Unity. Unity debe estar abierto mientras se ejecuta `generate_package.sh`.
3. Los paquetes se exportarán a `braze-unity-sdk/unity-package/`.
4. En el editor de Unity, importa el paquete deseado a tu proyecto Unity navegando a **Activos** > **Importar paquete** > **Paquete personalizado**.
5. (opcional) Desmarca los archivos que no desees importar.

Puedes personalizar el paquete de Unity exportado editando tanto `generate_package.sh` como el script de exportación que se encuentra en `Assets/Editor/Build.cs`.

## Compatibilidad con Prime 31

Para utilizar el plugin Unity de Braze con los plugins de Prime31, edita la página `AndroidManifest.xml` de tu proyecto para utilizar las clases de Actividad compatibles con Prime31. Cambia todas las referencias de
`com.braze.unity.BrazeUnityPlayerActivity` a `com.braze.unity.prime31compatible.BrazeUnityPlayerActivity`

## Amazon ADM push

Braze soporta la integración de [Amazon ADM push](https://developer.amazon.com/public/apis/engage/device-messaging) en aplicaciones Unity. Si quieres integrar ADM push de Amazon, crea un archivo llamado `api_key.txt` que contenga tu clave de API de ADM y colócalo en la carpeta `Plugins/Android/assets/`.  Para obtener más información sobre la integración de Amazon ADM con Braze, visita nuestras [instrucciones de integración push de ADM]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/push_notifications/adm_push_notifications/).

## Opciones avanzadas de implementación del SDK de Android {#android-sdk-advanced}

### Habilitar el registro detallado en el editor de Unity
Para habilitar el registro detallado en el editor de Unity, haz lo siguiente:

1. Abre los ajustes de configuración de Braze navegando hasta **Braze** > **Configuración de Braze**.
2. Haz clic en el menú desplegable **Mostrar configuración de Android Braze**.
3. En el campo **Nivel de registro SDK**, introduce el valor "0".

### Ampliación del reproductor Braze Unity (Android) {#extending-braze-unity-player}

El archivo de ejemplo `AndroidManifest.xml` proporcionado tiene registrada una clase de Actividad, [`BrazeUnityPlayerActivity`](https://github.com/braze-inc/braze-android-sdk/blob/e804cb3a10ae68364b354b52abf1bef8a0d1a9dc/android-sdk-unity/src/main/java/com/braze/unity/BrazeUnityPlayerActivity.kt). Esta clase está integrada con el SDK de Braze y amplía `UnityPlayerActivity` con gestión de sesiones, registro de mensajes dentro de la aplicación, registro de análisis de notificaciones push y mucho más. Consulta [Unity](https://docs.unity3d.com/Manual/AndroidUnityPlayerActivity.html) para obtener más información sobre la ampliación de la clase `UnityPlayerActivity`.

Si estás creando tu propio `UnityPlayerActivity` personalizado en un proyecto de biblioteca o de plugin, tendrás que ampliar nuestro `BrazeUnityPlayerActivity` para integrar tu funcionalidad personalizada con Braze. Antes de empezar a trabajar en la ampliación de `BrazeUnityPlayerActivity`, sigue nuestras instrucciones para integrar Braze en tu proyecto Unity.
1. Añade el SDK para Android de Braze como dependencia a tu proyecto de biblioteca o plugin, tal y como se describe en [las instrucciones de integración de SDK para Android de Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/).
2. Integra nuestro Unity `.aar`, que contiene nuestra funcionalidad específica de Unity, a tu proyecto de biblioteca Android que estás construyendo para Unity. El `appboy-unity.aar` está disponible en nuestro [repositorio público](https://github.com/braze-inc/braze-unity-sdk/tree/master/Assets/Plugins/Android). Una vez que nuestra biblioteca Unity se haya integrado correctamente, modifica tu `UnityPlayerActivity` para ampliar `BrazeUnityPlayerActivity`.
3. Exporta tu proyecto de biblioteca o plugin y colócalo en `/<your-project>/Assets/Plugins/Android` de la forma habitual. No incluyas ningún código fuente de Braze en tu biblioteca o plugin, ya que ya estarán presentes en `/<your-project>/Assets/Plugins/Android`.
4. Edita tu `/<your-project>/Assets/Plugins/Android/AndroidManifest.xml` para especificar tu subclase `BrazeUnityPlayerActivity` como actividad principal.

Ahora deberías poder empaquetar un `.apk` desde el IDE de Unity que esté totalmente integrado con Braze y contenga tu funcionalidad personalizada de `UnityPlayerActivity`.

## Opciones avanzadas de implementación del SDK de iOS {#ios-sdk-advanced}

### Habilitar el registro detallado en el editor de Unity
Para habilitar el registro detallado en el editor de Unity, haz lo siguiente:

1. Abre los ajustes de configuración de Braze navegando hasta **Braze** > **Configuración de Braze**.
2. Haz clic en el menú desplegable **Mostrar configuración de Braze iOS**.
3. En el campo **Nivel de registro SDK**, introduce el valor "0".

### Ampliar el SDK (iOS)

Para ampliar los comportamientos del SDK, bifurca el [proyecto GitHub del SDK de Unity de Braze](https://github.com/appboy/appboy-unity-sdk) y haz los cambios que necesites.

Para publicar tu código modificado como un paquete de Unity, consulta nuestros [Casos de uso avanzado]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/advanced_use_cases/).

### Pasar de la integración manual a la automatización (iOS)

Para aprovechar la integración automatizada de iOS que ofrece el SDK Braze Unity, sigue estos pasos para pasar de una integración manual a una automatizada.

1. Elimina todo el código relacionado con Braze de la subclase `UnityAppController` de tu proyecto Xcode.
2. Elimina las bibliotecas Braze iOS de tu proyecto Unity o Xcode (como `Appboy_iOS_SDK.framework` y `SDWebImage.framework`) e [importa el paquete Braze Unity](#step-1-importing-the-braze-unity-package) a tu proyecto Unity.
3. Sigue las instrucciones de integración para [configurar tu clave de API a través de Unity](#step-2-setting-your-api-key).

