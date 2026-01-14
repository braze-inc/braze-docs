{% multi_lang_include developer_guide/prerequisites/web.md %} También tendrás que [configurar las notificaciones push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web).

## Acerca de los avisos push suaves

A menudo es una buena idea que los sitios implementen una notificación push "suave" en la que "prepares" al usuario y expongas tus argumentos para enviarle notificaciones push antes de solicitar el permiso push. Esto es útil porque el navegador regula la frecuencia con la que puedes preguntar directamente al usuario, y si el usuario deniega el permiso no puedes volver a preguntárselo.

Alternativamente, si quieres incluir una gestión personalizada especial, en lugar de llamar directamente a `requestPushPermission()` como se describe en la [integración push web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration/#step-2-browser-registration) estándar, utiliza nuestros [mensajes dentro de la aplicación desencadenados]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages/?tab=web).

{% alert tip %}
Esto puede hacerse sin necesidad de personalizar el SDK utilizando nuestro [nuevo primer push sin código]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/).
{% endalert %}

## Configuración de los avisos soft push

{% multi_lang_include archive/web-v4-rename.md %}

### Paso 1: Crear una campaña push primer

En primer lugar, debes crear una campaña de mensajería dentro de la aplicación "Prime for Push" en el panel de Braze:

1. Crea un mensaje **Modal** dentro de la aplicación con el texto y el estilo que desees. 
2. A continuación, establece el comportamiento al hacer clic en **Cerrar mensaje**. Este comportamiento se personalizará más adelante.
3. Añade un par clave-valor al mensaje donde la clave es `msg-id`, y el valor es `push-primer`.
4. Asigna una acción desencadenante de evento personalizada (como "prime-for-push") al mensaje. Si es necesario, puedes crear el evento personalizado manualmente desde el panel.

### Paso 2: Eliminar llamadas

En tu integración de SDK de Braze, busca y elimina cualquier llamada a `automaticallyShowInAppMessages()` dentro de tu fragmento de código de carga.

### Paso 3: Integración de actualizaciones

Por último, sustituye la llamada eliminada por el siguiente fragmento de código:

```javascript
import * as braze from "@braze/web-sdk";
// Be sure to remove any calls to braze.automaticallyShowInAppMessages()
braze.subscribeToInAppMessage(function(inAppMessage) {
  // check if message is not a control variant
  if (inAppMessage instanceof braze.inAppMessage) {
    // access the key-value pairs, defined as `extras`
    const keyValuePairs = inAppMessage.extras || {};
    // check the value of our key `msg-id` defined in the Braze dashboard
    if (keyValuePairs["msg-id"] === "push-primer") {
      // We don't want to display the soft push prompt to users on browsers
      // that don't support push, or if the user has already granted/blocked permission
      if (
        braze.isPushSupported() === false ||
        braze.isPushPermissionGranted() ||
        braze.isPushBlocked()
      ) {
        // do not call `showInAppMessage`
        return;
      }

      // user is eligible to receive the native prompt
      // register a click handler on one of the two buttons
      if (inAppMessage.buttons[0]) {
        // Prompt the user when the first button is clicked
        inAppMessage.buttons[0].subscribeToClickedEvent(function() {
          braze.requestPushPermission(
            function() {
              // success!
            },
            function() {
              // user declined
            }
          );
        });
      }
    }
  }

  // show the in-app message now
  braze.showInAppMessage(inAppMessage);
});
```

Cuando quieras mostrar el mensaje push suave al usuario, llama a `braze.logCustomEvent` - con el nombre del evento que desencadene este mensaje dentro de la aplicación.
