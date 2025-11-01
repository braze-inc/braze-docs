---
nav_title: PREGUNTAS FRECUENTES
article_title: Preguntas frecuentes sobre mensajes dentro de la aplicación
page_order: 19
description: "Este artículo ofrece respuestas a las preguntas más frecuentes sobre los mensajes dentro de la aplicación."
tool: in-app messages

---

# Preguntas más frecuentes

> Este artículo ofrece respuestas a algunas preguntas frecuentes sobre los mensajes dentro de la aplicación.

### ¿Qué es un mensaje en el explorador y en qué se diferencia de un mensaje dentro de la aplicación?

Los mensajes dentro de la aplicación se envían a los navegadores web. Para crear un mensaje dentro del explorador, asegúrate de seleccionar **Explorador** web en el campo **Enviar a** al crear tu campaña de mensajería dentro de la aplicación o Canvas. 

### ¿Se mostrará un mensaje dentro de la aplicación si el dispositivo está desconectado?

Depende. Como los mensajes dentro de la aplicación se entregan al inicio de la sesión, el dispositivo puede descargar la carga útil antes de desconectarse, y el mensaje dentro de la aplicación puede seguir mostrándose mientras se está desconectado. Si no se descarga la carga útil, el mensaje dentro de la aplicación no se mostrará.

### Si un usuario ya tiene una carga útil de mensaje dentro de la aplicación en su dispositivo y se cambia la caducidad del mensaje, ¿se actualizará la caducidad en su dispositivo?

Cuando un usuario inicia una sesión, Braze comprueba si se han realizado cambios en los mensajes dentro de la aplicación para los que es elegible y los actualiza en consecuencia. Así, si la caducidad ha cambiado y registran una sesión, entonces el mensaje dentro de la aplicación se envía al dispositivo con la información actualizada.

### ¿Cómo configuro las horas tranquilas para una campaña de mensajes dentro de la aplicación?

La característica Horas tranquilas no está disponible para su uso con campañas de mensajes dentro de la aplicación. Esta característica se utiliza para evitar que se envíen mensajes a tus usuarios durante determinadas horas. En las campañas de mensajería dentro de la aplicación, tus usuarios sólo recibirán mensajes dentro de la aplicación si están activos en ella. 

Como solución para enviar mensajes dentro de la aplicación durante un tiempo específico, utiliza el siguiente código Liquid de ejemplo. Esto permite abortar el mensaje si el mensaje dentro de la aplicación se muestra después de las 19:59 o antes de las 8 en la zona horaria especificada.

{% raw %}
```liquid
{% assign time = 'now' | time_zone: ${time_zone} %}{% assign hour = time | date: '%H' | plus: 0 %}
{% if hour > 19 or hour < 8 %}
{% abort_message("Outside allowed time window") %}
{% endif %}
MESSAGE HERE
```
{% endraw %}

### ¿Cuándo se calcula la elegibilidad para un mensaje dentro de la aplicación?

La elegibilidad para un mensaje dentro de la aplicación se calcula en el momento de la entrega. Si un mensaje dentro de la aplicación está programado para enviarse a las 7 de la mañana, entonces la elegibilidad se comprueba para este mensaje dentro de la aplicación a las 7 de la mañana.

Una vez que se muestre el mensaje dentro de la aplicación, la elegibilidad dependerá de cuándo se descargue y desencadene el mensaje dentro de la aplicación.

### ¿Qué son las plantillas de mensajes dentro de la aplicación?

Los mensajes dentro de la aplicación se entregarán como plantillas de mensajes dentro de la aplicación cuando se seleccione **Reevaluar elegibilidad de campaña antes de mostrar** o si en el mensaje existe alguna de las siguientes etiquetas de Liquid:

- `canvas_entry_properties`
- `connected_content`
- Variables SMS como {% raw %}`{sms.${*}}`{% endraw %}
- `catalog_items`
- `catalog_selection_items`
- `event_properties`

Esto significa que, durante el inicio de la sesión, el dispositivo recibirá el desencadenante de ese mensaje dentro de la aplicación en lugar del mensaje completo. Cuando el usuario desencadena el mensaje dentro de la aplicación, el dispositivo del usuario realiza una solicitud de red para obtener el mensaje real.

{% alert note %}
El mensaje no se entregará si el dispositivo no tiene acceso a Internet. El mensaje podría no entregarse si la lógica Liquid tarda demasiado en resolverse.
{% endalert %}

### ¿Por qué mi campaña de mensajería dentro de la aplicación archivada sigue entregando impresiones de mensajes dentro de la aplicación?

Esto puede ocurrir para los usuarios que cumplían los criterios del segmento cuando la campaña de mensajería dentro de la aplicación estaba activa.

Para evitarlo, durante la configuración de tu campaña, selecciona **Reevaluar elegibilidad de la campaña antes de mostrarla**. 

### ¿Cómo calcula Braze la caducidad de un mensaje dentro de la aplicación configurado como "después de 1 día(s)"?

Braze calcula un tiempo de caducidad de un día como 24 horas después de que los usuarios sean elegibles para recibir un mensaje.