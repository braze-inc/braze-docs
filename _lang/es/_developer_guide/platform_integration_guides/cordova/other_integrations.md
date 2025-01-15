---
nav_title: Otras integraciones
article_title: Otras integraciones
page_order: 6
---

# Otras integraciones

> Estas son las otras integraciones admitidas en el SDK Braze de Cordova.

{% multi_lang_include cordova/prerequisites.md %}

## Mensajería dentro de la aplicación

De manera predeterminada, el SDK Cordova admite mensajes dentro de la aplicación sin cambios. Consulta los ejemplos de integración [en Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/integration/) o [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/overview/) para obtener información sobre cómo personalizar los mensajes dentro de la aplicación. Además, puedes consultar el [ejemplo de aplicación Cordova](https://github.com/braze-inc/braze-cordova-sdk/blob/master/sample-project/www/js/index.js) o el ejemplo de aplicación [Android](https://github.com/braze-inc/braze-android-sdk) o [iOS](https://github.com/braze-inc/braze-swift-sdk) para ver ejemplos de implementación.

### Soporte GIF

{% multi_lang_include wrappers/gif_support/in_app_messaging.md %}

## Canal de noticias

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

Consulta las instrucciones de integración en [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/news_feed/integration/) e [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/legacy_sdks/ios/news_feed/integration/) para obtener información sobre cómo integrar la fuente de noticias en tu aplicación Cordova. Alternativamente, nuestro plugin Cordova proporciona un método, `launchNewsFeed`, que lanzará un canal de noticias modal sin más integración.

El SDK de Braze Cordova tiene varios métodos para obtener el número de tarjetas de canal de noticias leídas o no leídas para diferentes categorías. Echa un vistazo a [la implementación de un proyecto de muestra](https://github.com/braze-inc/braze-cordova-sdk/blob/master/sample-project/www/js/index.js) para ver un ejemplo.
