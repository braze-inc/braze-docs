---
nav_title: Integraciones de Smart TV
article_title: Integración de Smart TV para Web
platform: Web
page_order: 20
description: "Este artículo explica cómo utilizar el SDK Web de Braze para la integración con Smart TV (Samsung y LG)."

---

# Integración de Smart TV

> El SDK Web de Braze te permite recopilar análisis y mostrar mensajes enriquecidos dentro de la aplicación y mensajes de tarjeta de contenido a los usuarios de Smart TV, incluidos [los televisores Samsung Tizen](https://developer.samsung.com/smarttv/develop/specifications/tv-model-groups.html) y [LG (webOS)](https://webostv.developer.lge.com/discover). Este artículo explica cómo utilizar el SDK Web de Braze para la integración con Smart TV.

Para una referencia técnica completa, consulta nuestra [Documentación de JavaScript](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html) o nuestras [aplicaciones de ejemplo](https://github.com/Appboy/smart-tv-sample-apps) para ver el SDK Web funcionando en un televisor.

## Instala el SDK de Braze

Para empezar, sigue nuestra guía de [configuración inicial del SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/) para el SDK Web.

Hay dos cambios necesarios para la integración con Smart TV:

1. Cuando descargues o importes el SDK Web, asegúrate de utilizar el paquete "core" (disponible en https://js.appboycdn.com/web-sdk/x.y/braze.core.min.js, donde x.y es la versión deseada). Recomendamos utilizar la versión CDN de nuestro SDK Web, ya que la versión NPM está escrita en módulos ES nativos, mientras que la versión CDN está transpilada a ES5. Si prefieres utilizar la [versión de NPM](https://www.npmjs.com/package/@braze/web-sdk), asegúrate de que utilizas un bundler como webpack que elimine el código no utilizado y que el código se transpile a ES5.
2. Al inicializar el SDK Web, debes establecer las opciones de inicialización `disablePushTokenMaintenance` y `manageServiceWorkerExternally` en `true`.

## Análisis

Todos los mismos métodos del SDK Web para análisis se pueden utilizar en las Smart TV.

Para obtener una guía completa sobre el seguimiento de eventos personalizados, atributos personalizados y mucho más, lee nuestra documentación [de Análisis]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_sessions/).

## Mensajes dentro de la aplicación y tarjetas de contenido

El SDK Web de Braze admite tanto [mensajes dentro de la aplicación]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/integration/) como [tarjetas de contenido]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/integration/) en Smart TV. Ten en cuenta que debes utilizar el [ SDK Web "Core"](https://www.npmjs.com/package/@braze/web-sdk), ya que la representación de mensajes dentro de la aplicación y de tarjetas de contenido no es compatible con nuestra visualización de interfaz de usuario estándar y, en su lugar, debe ser personalizada por tu aplicación para adaptarse a la experiencia de tu TV App.

Visita [Visualización manual de mensajes dentro]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/in-app_message_delivery/#manual-in-app-message-display) de la aplicación para obtener más información sobre cómo tu aplicación Smart TV puede recibir y mostrar mensajes dentro de la aplicación.


