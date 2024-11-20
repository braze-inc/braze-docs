---
nav_title: Registro de impresiones y clics
article_title: Registro de impresiones y clics
platform: Web
channel: in-app messages
page_order: 3
page_type: reference
description: "Este artículo trata del registro de impresiones y clics de mensajes dentro de la aplicación para tu aplicación Web."

---

# Registro de impresiones y clics

> Este artículo explica cómo registrar impresiones y clics de mensajes dentro de la aplicación para tu aplicación Web.

El registro de [impresiones](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#loginappmessageimpression) y [clics](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#loginappmessagebuttonclick) de mensajes dentro de la aplicación se realiza automáticamente cuando utilizas el método `showInAppMessage` o `automaticallyShowInAppMessage`.

Si no utilizas ninguno de estos métodos y optas por mostrar manualmente el mensaje utilizando tu propio código de interfaz de usuario, utiliza los siguientes métodos para registrar los análisis:

```javascript
// Registers that a user has viewed an in-app message with the Braze server.
braze.logInAppMessageImpression(inAppMessage);
// Registers that a user has clicked on the specified in-app message with the Braze server.
braze.logInAppMessageClick(inAppMessage);
// Registers that a user has clicked a specified in-app message button with the Braze server.
braze.logInAppMessageButtonClick(button, inAppMessage);
// Registers that a user has clicked on a link in an HTML in-app message with the Braze server.
braze.logInAppMessageHtmlClick(inAppMessage, buttonId?, url?)
```


