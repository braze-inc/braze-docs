{% multi_lang_include developer_guide/prerequisites/web.md %}

## Estilos personalizados

Los elementos de la interfaz de usuario de Braze vienen con un aspecto predeterminado que crea una experiencia de mensajería dentro de la aplicación neutral y busca la coherencia con otras plataformas móviles Braze. Los estilos predeterminados de Braze se definen en CSS dentro del SDK de Braze. 

### Configuración de un estilo predeterminado

Al anular los estilos seleccionados en tu aplicación, puedes personalizar nuestros tipos de mensajes dentro de la aplicación estándar con tus propias imágenes de fondo, familias de fuentes, estilos, tamaños, animaciones y mucho más. 

Por ejemplo, lo siguiente es un ejemplo de modificación que hará que las cabeceras de un mensaje dentro de la aplicación aparezcan en cursiva:

```css
  body .ab-in-app-message .ab-message-header {
    font-style: italic;
  }
```

Consulta [los JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessage.html) para más información.

### Personalizar el índice z

De manera predeterminada, los mensajes dentro de la aplicación se muestran utilizando `z-index: 9001`. Esto es configurable mediante la [opción de inicialización](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions) `inAppMessageZIndex ` en el caso de que tu sitio web estilice elementos con valores superiores a ese.

```javascript
braze.initialize("YOUR-API-KEY", {
    baseUrl: "YOUR-API-ENDPOINT",
    inAppMessageZIndex: 12000
});
```

{% alert important %}
Esta característica sólo está disponible para Web Braze SDK v3.3.0 y posteriores.
{% endalert %}

## Personalización de la desestimación de mensajes

De forma predeterminada, cuando se muestra un mensaje dentro de la aplicación, al pulsar el botón de escape o hacer clic en el fondo gris de la página se descartará el mensaje. Configura la [opción de inicialización](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions) `requireExplicitInAppMessageDismissal` en `true` para evitar este comportamiento y requerir un clic explícito en el botón para descartar los mensajes. 

```javascript
import * as braze from "@braze/web-sdk";
braze.initialize("YOUR-API-KEY", {
    baseUrl: "YOUR-API-ENDPOINT",
    requireExplicitInAppMessageDismissal: true
});
```

## Abrir enlaces en una pestaña nueva

Para configurar tus enlaces de mensajes dentro de la aplicación para que se abran en una pestaña nueva, configura la opción `openInAppMessagesInNewTab` en `true` para forzar que todos los enlaces de los clics de mensajes dentro de la aplicación se abran en una pestaña o ventana nueva.

```javascript
braze.initialize('api-key', { openInAppMessagesInNewTab: true} );
```
