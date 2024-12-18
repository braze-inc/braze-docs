---
nav_title: Ejemplos de aplicaciones
article_title: Ejemplos de aplicaciones para Android y FireOS
platform: 
  - Android
  - FireOS
page_order: 10
description: "Este artículo de referencia explica cómo utilizar las aplicaciones de ejemplo de Android."

---

# Ejemplos de aplicaciones

> Cada SDK de Braze incluye una aplicación de ejemplo en el repositorio para tu comodidad. Cada una de estas aplicaciones se puede compilar por completo, para que puedas probar las características de Braze al mismo tiempo que las implementas en tus propias aplicaciones. 

Probar el comportamiento dentro de tu propia aplicación en comparación con el comportamiento esperado y las rutas de código dentro de las aplicaciones de ejemplo es una forma excelente de depurar cualquier problema que puedas encontrarte.

## Construir la aplicación de prueba Droidboy
Nuestra aplicación de prueba dentro del [repositorio SDKBraze](https://github.com/braze-inc/braze-android-sdk "GitHub de Android") se llama Droidboy. Sigue estas instrucciones para crear una copia totalmente funcional junto a tu proyecto.

1. Crea un nuevo [espacio de trabajo]({{site.baseurl}}/developer_guide/platform_wide/app_group_configuration/#app-group-configuration) y anota la clave de identificador de la API Braze.<br><br>
2. Copia tu ID de remitente del FCM y la clave de identificador de la API de Braze en los lugares adecuados dentro de `/droidboy/res/values/braze.xml` (entre las etiquetas de las cadenas denominadas `com_braze_push_fcm_sender_id` y `com_braze_api_key`, respectivamente).<br><br>
3. Copia la clave de tu servidor FCM y el ID del servidor en la configuración de tu espacio de trabajo, en **Administrar configuración**.<br><br>
4. Para montar el APK de Droidboy, ejecuta `./gradlew assemble` dentro del directorio del SDK. Utiliza `gradlew.bat` en Windows.<br><br>
5. Para instalar automáticamente el APK de Droidboy en un dispositivo de prueba, ejecuta `./gradlew installDebug` dentro del directorio del SDK:

## Construir la aplicación de prueba Hello Braze
La aplicación de prueba Hello Braze muestra un caso de uso mínimo del SDK de Braze y, además, muestra cómo integrar fácilmente el SDK de Braze en un proyecto Gradle.

1. Copia tu clave de identificador de API de la página **Administrar configuración** en tu archivo `braze.xml` de la carpeta `res/values`.
![]({% image_buster /assets/img_archive/hello_appboy.png %})<br><br>
2. Para instalar la aplicación de muestra en un dispositivo o emulador, ejecuta el siguiente comando dentro del directorio del SDK:
```
./gradlew installDebug
```
Si no tienes bien configurada la variable `ANDROID_HOME` o no tienes una carpeta `local.properties` con una carpeta `sdk.dir` válida, este complemento también instalará el SDK base por ti. Consulta el [repositorio de plugins](https://github.com/JakeWharton/sdk-manager-plugin) para obtener más información.

Para obtener más información sobre el sistema de compilación del SDK de Android, consulta el [README del repositorio de GitHub](https://github.com/braze-inc/braze-android-sdk/blob/master/README.md).

