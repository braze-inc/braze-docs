---
nav_title: Preguntas frecuentes
article_title: Preguntas frecuentes sobre los mensajes en la aplicación
page_order: 19
description: "Este artículo ofrece respuestas a las preguntas más frecuentes sobre los Mensajes In-App."
tool: in-app messages

---

# Preguntas más frecuentes

> Este artículo ofrece respuestas a algunas preguntas frecuentes sobre los mensajes in-app.

### ¿Qué es un mensaje in-browser y en qué se diferencia de un mensaje in-app?

Los mensajes dentro del navegador son mensajes dentro de la aplicación que se envían a los navegadores web. Para crear un mensaje en navegador, asegúrate de seleccionar **Navegador web** en el campo **Enviar a** al crear tu campaña de mensajes en aplicación o Canvas. 

### ¿Se mostrará un mensaje en la aplicación si el dispositivo está desconectado?

Depende. Dado que los mensajes in-app se entregan al inicio de la sesión, el dispositivo puede descargar la carga útil antes de desconectarse, y el mensaje in-app puede seguir mostrándose mientras se está desconectado. Si no se descarga la carga útil, el mensaje dentro de la aplicación no se mostrará.

### Si un usuario ya tiene una carga útil de mensaje in-app en su dispositivo y se cambia la caducidad del mensaje, ¿se actualizará la caducidad en su dispositivo?

Cuando un usuario inicia una sesión, Braze comprueba si se han realizado cambios en los mensajes de la aplicación a los que tiene derecho y los actualiza en consecuencia. De este modo, si la caducidad ha cambiado y se registra una sesión, el mensaje de la aplicación se envía al dispositivo con la información actualizada.

### ¿Cómo configuro las horas de silencio para una campaña de mensajes in-app?

La función Horas de silencio no está disponible para campañas de mensajes dentro de la aplicación. Esta función se utiliza para impedir que se envíen mensajes a sus usuarios durante determinadas horas. En el caso de las campañas de mensajes dentro de la aplicación, los usuarios sólo recibirán mensajes dentro de la aplicación si están activos en ella. 

Como solución para enviar mensajes dentro de la aplicación a una hora determinada, utilice el siguiente código Liquid de ejemplo. Esto permite abortar el mensaje si el mensaje in-app se muestra después de las 7:59 pm o antes de las 8 am en la zona horaria especificada.

{% raw %}
```liquid
{% assign time = 'now' | time_zone: ${time_zone} %}{% assign hour = time | date: '%H' | plus: 0 %}
{% if hour > 19 or hour < 8 %}
{% abort_message("Outside allowed time window") %}
{% endif %}
MESSAGE HERE
```
{% endraw %}

### ¿Cuándo se calcula la elegibilidad para un mensaje in-app?

La elegibilidad para un mensaje dentro de la aplicación se calcula en el momento de la entrega. Si un mensaje in-app está programado para enviarse a las 7 am, entonces la elegibilidad se comprueba para este mensaje in-app a las 7 am.

Una vez que se muestre el mensaje dentro de la aplicación, la elegibilidad dependerá de cuándo se descargue y desencadene el mensaje dentro de la aplicación.

### ¿Qué son las plantillas de mensajes in-app?

Los mensajes in-app se entregarán como mensajes in-app con plantilla cuando se seleccione **Reevaluar elegibilidad de campaña antes de mostrar** o si alguna de las siguientes etiquetas Liquid existe en el mensaje:

- `canvas_entry_properties`
- `connected_content`
- Variables SMS como {% raw %}`{sms.${*}}`{% endraw %}
- `catalog_items`
- `catalog_selection_items`
- `event_properties`

Esto significa que durante el inicio de sesión, el dispositivo recibirá el desencadenante de ese mensaje in-app en lugar del mensaje completo. Cuando el usuario activa el mensaje in-app, el dispositivo del usuario hará una petición de red para obtener el mensaje real.

{% alert note %}
El mensaje no se enviará si el dispositivo no tiene acceso a Internet. El mensaje podría no entregarse si la lógica de Liquid tarda demasiado en resolverse.
{% endalert %}

### ¿Por qué mi campaña archivada de mensajes in-app sigue proporcionando impresiones de mensajes in-app?

Esto puede ocurrir para usuarios que cumplían los criterios del segmento cuando la campaña de mensajes in-app estaba activa.

Para evitarlo, durante la configuración de la campaña, seleccione **Reevaluar la elegibilidad de la campaña antes de mostrarla**. 

### ¿Cómo calcula Braze la caducidad de un mensaje in-app configurado como "después de 1 día(s)"?

Braze calcula un tiempo de expiración de un día como 24 horas después de que los usuarios sean elegibles para recibir un mensaje.