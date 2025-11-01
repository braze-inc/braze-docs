{% multi_lang_include developer_guide/prerequisites/roku.md %} Además, los mensajes dentro de la aplicación sólo se enviarán a dispositivos Roku que ejecuten la versión mínima compatible del SDK:

{% sdk_min_versions roku:0.1.2 %}

## Tipos de mensajes

{% tabs %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/android.md %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/swift.md %}
{% endtabs %}

## Habilitación de mensajes dentro de la aplicación

### Paso 1: Añade un observador

Para procesar mensajes dentro de la aplicación, puedes añadir un observador en `BrazeTask.BrazeInAppMessage`:

```brightscript
m.BrazeTask.observeField("BrazeInAppMessage", "onInAppMessageReceived")
```

### Paso 2: Acceder a mensajes desencadenados

Después, dentro de tu controlador, tendrás acceso al mensaje dentro de la aplicación más alto que hayan desencadenado tus campañas:

```brightscript
sub onInAppMessageReceived()
  in_app_message = m.BrazeTask.BrazeInAppMessage
  ...
end sub
```

## Campos de mensajería

### Manejo de

A continuación se enumeran los campos que necesitarás para gestionar tus mensajes dentro de la aplicación:

| Campos | Descripción |
| ------ | ----------- |
| `buttons` | Lista de botones (puede ser una lista vacía). |
| `click_action` | `"URI"` o `"NONE"`. Utiliza este campo para indicar si el mensaje dentro de la aplicación debe abrirse a un enlace URI o cerrar el mensaje al hacer clic. Cuando no hay botones, esto debería ocurrir cuando el usuario hace clic en "Aceptar" cuando se muestra el mensaje dentro de la aplicación. |
| `dismiss_type` | `"AUTO_DISMISS"` o `"SWIPE"`. Utiliza este campo para indicar si tu mensaje dentro de la aplicación se descartará automáticamente o si será necesario deslizar el dedo para descartarlo. |
| `display_delay` | Cuánto tiempo (segundos) hay que esperar hasta que aparezca el mensaje dentro de la aplicación. |
| `duration` | Cuánto tiempo (milisegundos) debe mostrarse el mensaje cuando `dismiss_type` está configurado en `"AUTO_DISMISS"`. |
| `extras` | Pares clave-valor. |
| `header` | El texto de la cabecera. |
| `id` | El ID utilizado para registrar las impresiones o los clics. |
| `image_url` | URL de la imagen del mensaje dentro de la aplicación. |
| `message` | Texto del cuerpo del mensaje. |
| `uri` | Se enviará a los usuarios de tu URI en función de tu `click_action`. Este campo debe incluirse cuando `click_action` es `"URI"`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Para los mensajes dentro de la aplicación que contengan botones, el mensaje `click_action` también se incluirá en la carga útil final si la acción de clic se añade antes de añadir el texto del botón.
{% endalert %}

### Estilismo

También hay varios campos de estilo que puedes utilizar desde el panel:

| Campos | Descripción |
| ------ | ----------- |
| `bg_color` | Color de fondo. |
| `close_button_color` | Color del botón de cierre. |
| `frame_color` | El color de la superposición de la pantalla de fondo. |
| `header_text_color` | Color del texto de la cabecera. |
| `message_text_color` | Color del texto del mensaje. |
| `text_align` | "INICIO", "CENTRO" o "FIN". Tu alineación de texto seleccionada. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Alternativamente, podrías implementar el mensaje dentro de la aplicación y darle estilo dentro de tu aplicación Roku utilizando una paleta estándar:

### Botones de acción

| Campos | Descripción |
| ------ | ----------- |
| `click_action` | `"URI"` o `"NONE"`. Utiliza este campo para indicar si el mensaje dentro de la aplicación debe abrirse a un enlace URI o cerrar el mensaje al hacer clic. |
| `id` | El valor ID del propio botón. |
| `text` | El texto que se mostrará en el botón. |
| `uri` | Se enviará a los usuarios de tu URI en función de tu `click_action`. Este campo debe incluirse cuando `click_action` es `"URI"`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
