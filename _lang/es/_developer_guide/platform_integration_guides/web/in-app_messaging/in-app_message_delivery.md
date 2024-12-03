---
nav_title: Entrega de mensajes dentro de la aplicación
article_title: Entrega de mensajes dentro de la aplicación para Web
platform: Web
channel: in-app messages
page_order: 4
page_type: reference
description: "Este artículo describe la entrega de mensajes dentro de la aplicación a través del SDK de Braze, como la visualización manual de mensajes dentro de la aplicación o el envío de mensajes locales dentro de la aplicación y de intención de salida."

---

# Entrega de mensajes dentro de la aplicación

> Este artículo describe la entrega de mensajes dentro de la aplicación a través del SDK de Braze, como la visualización manual de mensajes dentro de la aplicación o el envío de mensajes locales dentro de la aplicación y de intención de salida.

## Tipos de desencadenantes

Nuestro producto de mensajes dentro de la aplicación te permite desencadenar la visualización de un mensaje dentro de la aplicación como resultado de varios tipos de eventos diferentes: `Any Purchase`, `Specific Purchase`, `Session Start`, `Custom Event`, y `Push Click`. Además, los desencadenantes `Specific Purchase` y `Custom Event` contienen filtros de propiedades sólidos.

{% alert note %}
Los mensajes desencadenados dentro de la aplicación sólo funcionan con eventos personalizados registrados a través del SDK de Braze. Los mensajes dentro de la aplicación no pueden desencadenarse a través de la API o por eventos de la API (como eventos de compra). Si trabajas con una aplicación Web, consulta cómo [registrar eventos personalizados]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_custom_events/#tracking-custom-events).
{% endalert %}

## Semántica de la entrega

Todos los mensajes dentro de la aplicación para los que un usuario es elegible se descargan automáticamente en el dispositivo o explorador del usuario tras un evento de inicio de sesión y se desencadenan de acuerdo con las reglas de entrega del mensaje. Visita nuestra [documentación sobre el ciclo de vida de la sesión]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_sessions/#session-lifecycle) para obtener más información sobre la semántica de inicio de sesión del SDK.

## Intervalo de tiempo mínimo entre desencadenamientos

De forma predeterminada, limitamos la tasa de mensajes dentro de la aplicación a una vez cada 30 segundos para garantizar una experiencia de usuario de calidad. Para anular este valor, puedes pasar la opción de configuración `minimumIntervalBetweenTriggerActionsInSeconds` a tu [`initialize`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize) función:

```javascript
// Sets the minimum time interval between triggered in-app messages to 5 seconds instead of the default 30
braze.initialize('YOUR-API-KEY', { minimumIntervalBetweenTriggerActionsInSeconds: 5 })
```

## Visualización manual de mensajes dentro de la aplicación

Si no quieres que tu sitio muestre inmediatamente nuevos mensajes dentro de la aplicación cuando se desencadenan, puedes desactivar la visualización automática y registrar tus propios suscriptores de visualización. 

Primero, busca y elimina la llamada a `braze.automaticallyShowInAppMessages()` dentro de tu fragmento de código de carga. A continuación, crea tu propia lógica para gestionar de forma personalizada un mensaje dentro de la aplicación desencadenado, en el que muestres o no el mensaje. 

```javascript
braze.subscribeToInAppMessage(function(inAppMessage) {
  // control group messages should always be "shown"
  // this will log an impression and not show a visible message
  
  if (inAppMessage.isControl) { // v4.5.0+, otherwise use  `inAppMessage instanceof braze.ControlMessage`
     return braze.showInAppMessage(inAppMessage);
  }
  
  // Display the in-app message. You could defer display here by pushing this message to code within your own application.
  // If you don't want to use Braze's built-in display capabilities, you could alternatively pass the in-app message to your own display code here.
  
  if ( should_show_the_message_according_to_your_custom_logic ) {
      braze.showInAppMessage(inAppMessage);
  } else {
      // do nothing
  }
});
```

{% alert important %}
Si no eliminas `braze.automaticallyShowInAppMessages()` de tu sitio web al llamar también a `braze.showInAppMessage`, el mensaje puede aparecer dos veces.
{% endalert %}

El parámetro `inAppMessage` será una subclase [`braze.InAppMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessage.html) o un objeto [`braze.ControlMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.controlmessage.html), cada uno de los cuales tiene varios métodos de suscripción a eventos del ciclo de vida. Consulta la documentación completa en [los JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessage.html).

Se puede mostrar solo un mensaje dentro de la aplicación [`Modal`]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in_app_messaging/#modal-in-app-messages) o [`Full`]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in_app_messaging/#full-in-app-messages) en un momento determinado. Si intentas mostrar un segundo mensaje modal o completo mientras ya se está mostrando uno, `braze.showInAppMessage` devolverá false y el segundo mensaje no se mostrará.

## Mensajes locales dentro de la aplicación

También se pueden crear mensajes dentro de la aplicación en tu sitio y mostrarlos localmente en tiempo real. Todas las opciones de personalización disponibles en el panel también están disponibles localmente. Esto es especialmente útil para mostrar mensajes que deseas desencadenar dentro de la aplicación en tiempo real. Sin embargo, el análisis de estos mensajes creados localmente no estará disponible en el panel de Braze.

```javascript
  // Displays a slideup type in-app message.
  var message = new braze.SlideUpMessage("Welcome to Braze! This is an in-app message.");
  message.slideFrom = braze.InAppMessage.SlideFrom.TOP;
  braze.showInAppMessage(message);
```

## Mensajes con intención de salida

Los mensajes dentro de la aplicación con intención de salida aparecen cuando los visitantes están a punto de salir de tu sitio. Proporcionan otra oportunidad de comunicar información importante a los usuarios sin interrumpir su experiencia en tu sitio. 

Para enviar estos mensajes, primero añade a tu sitio web una biblioteca de intención de salida, como esta [biblioteca de código abierto](https://github.com/carlsednaoui/ouibounce). A continuación, utiliza el siguiente fragmento de código para registrar la "intención de salida" como un evento personalizado. Las campañas de mensajería dentro de la aplicación pueden crearse en el panel utilizando "intención de salida" como evento personalizado desencadenante.

```javascript
  var _ouibounce = ouibounce(false, {
    callback: function() { braze.logCustomEvent('exit intent'); }
  });
```


