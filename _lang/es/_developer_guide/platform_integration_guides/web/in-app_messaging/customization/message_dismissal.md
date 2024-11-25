---
nav_title: Descarte de mensajes
article_title: Envío de mensajes dentro de la aplicación para Web
platform: Web
channel: in-app messages
page_order: 2
page_type: reference
description: "Este artículo trata sobre la eliminación de mensajes dentro de la aplicación para tu aplicación Web."

---

# Descarte de mensajes

> Este artículo explica cómo gestionar la eliminación de mensajes dentro de la aplicación para tu aplicación Web.

De forma predeterminada, cuando se muestra un mensaje dentro de la aplicación, al pulsar el botón de escape o hacer clic en el fondo gris de la página se descartará el mensaje. Configura la [opción de inicialización](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions) `requireExplicitInAppMessageDismissal` en `true` para evitar este comportamiento y requerir un clic explícito en el botón para descartar los mensajes. 

```javascript
import * as braze from "@braze/web-sdk";
braze.initialize("YOUR-API-KEY", {
    baseUrl: "YOUR-API-ENDPOINT",
    requireExplicitInAppMessageDismissal: true
});
```

