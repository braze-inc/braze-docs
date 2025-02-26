---
nav_title: Estilo personalizado
article_title: Mensaje dentro de la aplicación con estilo personalizado para Web
platform: Web
channel: in-app messages
page_order: 1
page_type: reference
description: "Este artículo trata del estilo personalizado de la mensajería dentro de la aplicación para tu aplicación Web."

---

# Estilo personalizado

> Los elementos de la interfaz de usuario de Braze vienen con un aspecto predeterminado que crea una experiencia de mensajería dentro de la aplicación neutral y busca la coherencia con otras plataformas móviles Braze. Los estilos predeterminados de Braze se definen en CSS dentro del SDK de Braze. 

Al anular los estilos seleccionados en tu aplicación, puedes personalizar nuestros tipos de mensajes dentro de la aplicación estándar con tus propias imágenes de fondo, familias de fuentes, estilos, tamaños, animaciones y mucho más. 

Por ejemplo, lo siguiente es un ejemplo de modificación que hará que las cabeceras de un mensaje dentro de la aplicación aparezcan en cursiva:

```css
  body .ab-in-app-message .ab-message-header {
    font-style: italic;
  }
```

Consulta [los JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessage.html) para más información.

## Índice z predeterminado de mensajes dentro de la aplicación

De manera predeterminada, los mensajes dentro de la aplicación se muestran utilizando `z-index: 9001`. Esto es configurable mediante la [opción de inicialización](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions) `inAppMessageZIndex ` en el caso de que tu sitio web estilice elementos con valores superiores a ese.

```javascript
braze.initialize("YOUR-API-KEY", {
    baseUrl: "YOUR-API-ENDPOINT",
    inAppMessageZIndex: 12000
});
```

{% alert important %}
Esta opción se introdujo en el SDK Web versión 3.3.0. Los SDK antiguos deben actualizarse para utilizar esta opción.
{% endalert %}

