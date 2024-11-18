---
nav_title: Pares clave-valor
article_title: Pares clave-valor de mensajes dentro de la aplicación para la Web
platform: Web
channel: in-app messages
page_order: 9
page_type: reference
description: "Este artículo explica cómo aprovechar los pares clave-valor de la mensajería dentro de la aplicación para mostrar información de tu aplicación Web."

---

# Pares clave-valor

> Este artículo explica cómo aprovechar los pares clave-valor de la mensajería dentro de la aplicación para mostrar información de tu aplicación Web.

Los objetos de mensaje dentro de la aplicación pueden llevar pares clave-valor como propiedad `extras`. Se especifican en el panel, en **Configuración**, al crear una campaña de mensajes dentro de la aplicación. Se pueden utilizar para enviar datos con un mensaje dentro de la aplicación para que tu sitio los gestione posteriormente. Por ejemplo:

```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToInAppMessage(function(inAppMessage) {
  // control group messages should always be "shown"
  // this will log an impression and not show a visible message
  if (inAppMessage instanceof braze.ControlMessage) {
    return braze.showInAppMessage(inAppMessage);
  }


  if (inAppMessage instanceof braze.InAppMessage) {
    const extras = inAppMessage.extras;
    if (extras) {
      for (const key in extras) {
        console.log("key: " + key + ", value: " + extras[key]);
      }
    }
  }
  braze.showInAppMessage(inAppMessage);
});
```
