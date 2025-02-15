---
nav_title: Abrir enlace en una pestaña nueva
article_title: Abrir enlace de mensaje dentro de la aplicación en una pestaña nueva para Web
platform: Web
channel: in-app messages
page_order: 8
page_type: reference
description: "En este artículo se explica cómo configurar tus enlaces de mensajes dentro de la aplicación para que se abran en una nueva pestaña para tu aplicación web."

---

# Abrir enlace en nueva pestaña

> En este artículo se explica cómo configurar tus enlaces de mensajes dentro de la aplicación para que se abran en una nueva pestaña para tu aplicación web.

Para configurar tus enlaces de mensajes dentro de la aplicación para que se abran en una pestaña nueva, configura la opción `openInAppMessagesInNewTab` en `true` para forzar que todos los enlaces de los clics de mensajes dentro de la aplicación se abran en una pestaña o ventana nueva.

```javascript
braze.initialize('api-key', { openInAppMessagesInNewTab: true} );
```
