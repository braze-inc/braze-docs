---
nav_title: Referencias y ejemplos de aplicaciones
article_title: "Referencias, repositorios y aplicaciones de ejemplo del SDK de Braze"
page_order: 5.5
description: "Esta es una lista de documentación de referencia, repositorios de GitHub y aplicaciones de ejemplo pertenecientes a cada SDK de Braze."
toc_headers: h2
---

# Referencias, repositorios y aplicaciones de ejemplo

> Esta es una lista de documentación de referencia, repositorios de GitHub y aplicaciones de ejemplo pertenecientes a cada SDK de Braze. La documentación de referencia de un SDK detalla sus clases, tipos, funciones y variables disponibles. Mientras que el repositorio de GitHub proporciona información sobre las declaraciones de funciones y atributos, los cambios de código y las versiones de ese SDK. Cada repositorio incluye también aplicaciones de ejemplo totalmente compilables que puedes utilizar para probar las características de Braze o implementarlas junto con tus propias aplicaciones.

## Lista de recursos

{% alert note %}
Actualmente, algunos SDK no tienen documentación de referencia específica, pero estamos trabajando activamente en ello.
{% endalert %}

| Plataforma          | Referencia                                                                                                                                    | Repositorio                                                                 | Ejemplo de aplicación                                                                |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| SDK para Android       | [Documentación de referencia](https://braze-inc.github.io/braze-android-sdk/kdoc/index.html)                                                                           | [Repositorio GitHub](https://github.com/braze-inc/braze-android-sdk)      | [Ejemplo de aplicación](https://github.com/braze-inc/braze-android-sdk/tree/master/samples)      |
| SDK de Swift         | [Documentación de referencia](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze)                                                                | [Repositorio GitHub](https://github.com/braze-inc/braze-swift-sdk)            | [Ejemplo de aplicación](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples)            |
| SDK Web           | [Documentación de referencia](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize)                                                               | [Repositorio GitHub](https://github.com/braze-inc/braze-web-sdk)              | [Ejemplo de aplicación](https://github.com/braze-inc/braze-web-sdk/tree/master/sample-builds)              |
| SDK de Cordova       | [Archivo de declaración](https://github.com/braze-inc/braze-cordova-sdk/blob/master/www/BrazePlugin.js)                                      | [Repositorio GitHub](https://github.com/braze-inc/braze-cordova-sdk)      | [Ejemplo de aplicación](https://github.com/braze-inc/braze-cordova-sdk/tree/master/sample-project)      |
| SDK de Flutter       | [Documentación de referencia](https://pub.dev/documentation/braze_plugin/latest/braze_plugin/)                                                   | [Repositorio GitHub](https://github.com/braze-inc/braze-flutter-sdk)      | [Ejemplo de aplicación](https://github.com/braze-inc/braze-flutter-sdk/tree/master/example)      |
| SDK nativo de React  | [Archivo de declaración](https://github.com/braze-inc/braze-react-native-sdk/blob/master/src/index.d.ts)                   | [Repositorio GitHub](https://github.com/braze-inc/braze-react-native-sdk) | [Ejemplo de aplicación](https://github.com/braze-inc/braze-react-native-sdk/tree/master/BrazeProject) |
| SDK de Roku          | N/A                                                                                                                                                         | [Repositorio GitHub](https://github.com/braze-inc/braze-roku-sdk)            | [Ejemplo de aplicación](https://github.com/braze-inc/braze-roku-sdk/tree/main/torchietv)            |
| SDK de Unity         | [Archivo de declaración](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/BrazePlatform.cs)     | [Repositorio GitHub](https://github.com/braze-inc/braze-unity-sdk)          | [Ejemplo de aplicación](https://github.com/braze-inc/braze-unity-sdk/tree/master/unity-samples)          |
| SDK de Unreal Engine | N/A                                                                                                                                                         | [Repositorio GitHub](https://github.com/braze-inc/braze-unreal-sdk)        | [Ejemplo de aplicación](https://github.com/braze-inc/braze-unreal-sdk/tree/master/BrazeSample)        |
| SDK de .NET MAUI       | N/A                                                                                                                                                         | [Repositorio GitHub](https://github.com/braze-inc/braze-xamarin-sdk)      | [Ejemplo de aplicación](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/samples)      |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Construir una aplicación de ejemplo

{% tabs %}
{% tab android %}
### Construyendo a "Droidboy"

Nuestra aplicación de prueba dentro del [repositorio GitHub del SDK de Android](https://github.com/braze-inc/braze-android-sdk) se llama Droidboy. Sigue estas instrucciones para crear una copia totalmente funcional junto a tu proyecto.

1. Crea un nuevo [espacio de trabajo]({{site.baseurl}}/developer_guide/platform_wide/app_group_configuration/#app-group-configuration) y anota la clave de identificador de la API Braze.<br><br>
2. Copia tu ID de remitente del FCM y la clave de identificador de la API de Braze en los lugares adecuados dentro de `/droidboy/res/values/braze.xml` (entre las etiquetas de las cadenas denominadas `com_braze_push_fcm_sender_id` y `com_braze_api_key`, respectivamente).<br><br>
3. Copia la clave de tu servidor FCM y el ID del servidor en la configuración de tu espacio de trabajo, en **Administrar configuración**.<br><br>
4. Para montar el APK de Droidboy, ejecuta `./gradlew assemble` dentro del directorio del SDK. Utiliza `gradlew.bat` en Windows.<br><br>
5. Para instalar automáticamente el APK de Droidboy en un dispositivo de prueba, ejecuta `./gradlew installDebug` dentro del directorio del SDK:

### Construir "Hola Braze"

La aplicación de prueba Hello Braze muestra un caso de uso mínimo del SDK de Braze y, además, muestra cómo integrar fácilmente el SDK de Braze en un proyecto Gradle.

1. Copia tu clave de identificador de API de la página **Administrar configuración** en tu archivo `braze.xml` de la carpeta `res/values`.
![]({% image_buster /assets/img_archive/hello_appboy.png %})<br><br>
2. Para instalar la aplicación de muestra en un dispositivo o emulador, ejecuta el siguiente comando dentro del directorio del SDK:
```
./gradlew installDebug
```
Si no tienes bien configurada la variable `ANDROID_HOME` o no tienes una carpeta `local.properties` con una carpeta `sdk.dir` válida, este complemento también instalará el SDK base por ti. Consulta el [repositorio de plugins](https://github.com/JakeWharton/sdk-manager-plugin) para obtener más información.

Para obtener más información sobre el sistema de compilación del SDK de Android, consulta el [README del repositorio de GitHub](https://github.com/braze-inc/braze-android-sdk/blob/master/README.md).
{% endtab %}

{% tab swift %}
### Creación de aplicaciones Swift de prueba

Sigue estas instrucciones para crear y ejecutar nuestras aplicaciones de prueba.

1. Crea un nuevo [espacio de trabajo]({{site.baseurl}}/developer_guide/platform_wide/app_group_configuration/#creating-your-app-group-in-my-apps) y anota la clave de API y el punto final del identificador de la aplicación.
2. Según tu método de integración (Swift Package Manager, CocoaPods, Manual), selecciona el archivo `xcodeproj` adecuado para abrirlo.
3. Coloca tu clave de API y tu punto final en el campo correspondiente del archivo `Credentials`.
{% endtab %}
{% endtabs %}

{% alert note %}
Mientras realizas el control de calidad de tu integración de SDK, utiliza [el depurador de SDK]({{site.baseurl}}/developer_guide/sdk_integration/debugging) para solucionar problemas sin activar el registro detallado de tu aplicación.
{% endalert %}
