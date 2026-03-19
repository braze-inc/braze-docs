{% multi_lang_include developer_guide/prerequisites/web.md %}

## Desencadenantes de mensajes

## Tipos de desencadenantes

Los mensajes dentro de la aplicación se desencadenan automáticamente cuando el SDK registra uno de los siguientes tipos de eventos personalizados: `Any Purchase`,`Specific Purchase` `Session Start`, `Custom Event`, y `Push Click`. Ten en cuenta que los `Specific Purchase`desencadenantes`Custom Event`  y  también contienen filtros de propiedades robustos.

{% alert note %}
Los mensajes dentro de la aplicación no se pueden desencadenar a través de la API ni mediante eventos de la API, solo mediante eventos personalizados registrados por el SDK. Para obtener más información sobre el registro, consulta [Registro de eventos personalizados]({{site.baseurl}}/developer_guide/analytics/logging_events/).
{% endalert %}

### Semántica de la entrega

Todos los mensajes elegibles dentro de la aplicación se entregan al dispositivo del usuario al inicio de la sesión. Cuando se entregue, el SDK precargará los activos para que estén disponibles en el momento del desencadenamiento, minimizando así la latencia de visualización. Si el evento desencadenante tiene más de un mensaje dentro de la aplicación elegible, solo se entregará el mensaje con la prioridad más alta.

Para obtener más información sobre la semántica de inicio de sesión del SDK, consulta[ Ciclo de vida de la sesión]({{site.baseurl}}/developer_guide/platform_integration_guides/analytics/tracking_sessions/).

### Límites de tarifa

De forma predeterminada, puedes enviar un mensaje dentro de la aplicación una vez cada 30 segundos.

Para anular esto, añade la siguiente propiedad a tu configuración de Braze, antes de que se inicialice la instancia de Braze. Puedes establecerlo en cualquier número entero positivo, que representa el intervalo de tiempo mínimo en segundos. Por ejemplo:

```javascript
// Sets the minimum time interval between triggered in-app messages to 5 seconds instead of the default 30
braze.initialize('YOUR-API-KEY', { minimumIntervalBetweenTriggerActionsInSeconds: 5 })
```

## Pares clave-valor

Cuando creas una campaña en Braze, puedes establecer pares clave-valor como `extras`, que el objeto de mensajería dentro de la aplicación puede utilizar para enviar datos a tu aplicación. Por ejemplo:

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

## Desactivación de los activadores automáticos

Para evitar que los mensajes dentro de la aplicación se desencadenen automáticamente:

Elimina la llamada a`braze.automaticallyShowInAppMessages()`  dentro de tu fragmento de código de carga y, a continuación, crea una lógica personalizada para gestionar la visualización o no de los mensajes dentro de la aplicación.

```javascript
braze.subscribeToInAppMessage(function(inAppMessage) {
  // control group messages should always be "shown"
  // this will log an impression and not show a visible message
  
  if (inAppMessage.isControl) { // v4.5.0+, otherwise use  `inAppMessage instanceof braze.ControlMessage`
     return braze.showInAppMessage(inAppMessage);
  }
  
  // Display the in-app message. You could defer display here by pushing this message to code within your own application.
  // If you don't want to use the Braze built-in display capabilities, you could alternatively pass the in-app message to your own display code here.
  
  if ( should_show_the_message_according_to_your_custom_logic ) {
      braze.showInAppMessage(inAppMessage);
  } else {
      // do nothing
  }
});
```

{% alert important %}
Si no eliminas`braze.automaticallyShowInAppMessages()`  de tu sitio web, llama al`braze.showInAppMessage` , el mensaje puede aparecer varias veces.
{% endalert %}

El parámetro `inAppMessage` será una subclase [`braze.InAppMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessage.html) o un objeto [`braze.ControlMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.controlmessage.html), cada uno de los cuales tiene varios métodos de suscripción a eventos del ciclo de vida. Consulta la documentación completa en [los JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessage.html).

Se puede mostrar solo un mensaje dentro de la aplicación [`Modal`]({{site.baseurl}}/developer_guide/in_app_messages/?tab=modal&sdktab=web) o [`Full`]({{site.baseurl}}/developer_guide/in_app_messages/?tab=full&sdktab=web) en un momento determinado. Si intentas mostrar un segundo mensaje modal o completo mientras ya se está mostrando uno, `braze.showInAppMessage` devolverá false y el segundo mensaje no se mostrará.

## Activación manual de mensajes desencadenados

### Mostrar un mensaje en tiempo real

También se pueden crear mensajes dentro de la aplicación en tu sitio y mostrarlos localmente en tiempo real. Todas las opciones de personalización disponibles en el panel también están disponibles localmente. Esto es especialmente útil para mostrar mensajes que deseas desencadenar dentro de la aplicación en tiempo real. Sin embargo, el análisis de estos mensajes creados localmente no estará disponible en el panel de Braze.

```javascript
  // Displays a slideup type in-app message.
  var message = new braze.SlideUpMessage("Welcome to Braze! This is an in-app message.");
  message.slideFrom = braze.InAppMessage.SlideFrom.TOP;
  braze.showInAppMessage(message);
```

## Desencadenamiento de mensajes de intención de salida

Los mensajes de intención de salida son mensajes no intrusivos que se muestran dentro de la aplicación y se utilizan para comunicar información importante a los visitantes antes de que abandonen tu sitio web.

Para configurar los activadores de estos tipos de mensajes, implementa una biblioteca de intención de salida en tu sitio web (como [la biblioteca de código abierto de ouibounce](https://github.com/carlsednaoui/ouibounce)) y, a continuación, utiliza el siguiente código para registrarlo`'exit intent'`como un evento personalizado en Braze. Ahora, tus futuras campañas de mensajes dentro de la aplicación pueden utilizar este tipo de mensaje como desencadenante de eventos personalizados.

```javascript
  var _ouibounce = ouibounce(false, {
    callback: function() { braze.logCustomEvent('exit intent'); }
  });
```
