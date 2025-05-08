---
nav_title: Integración
article_title: Guía de integración de mensajes dentro de la aplicación para Roku
platform: Roku
page_order: 2
description: "Esta guía de referencia explica cómo integrar mensajes dentro de la aplicación para Roku y las consideraciones sobre códigos pertinentes"
channel:
  - in-app messages
---

# Integración de mensajes dentro de la aplicación

> Esta guía de implementación cubre las consideraciones sobre códigos de mensajes dentro de la aplicación y los fragmentos de código que los acompañan. Aunque proporcionamos un código de integración de ejemplo, tendrás que añadir lógica para gestionar y mostrar los mensajes desencadenados dentro de la interfaz de usuario que desees. 

Dado que tu código será único para tu aplicación, no es necesario que gestiones todas las situaciones enumeradas si no son relevantes para tu caso de uso. Por ejemplo, si no utilizas la visualización diferida de mensajes dentro de la aplicación, no necesitarás implementar esa lógica ni los casos extremos.

## Requisitos del SDK {#supported-sdk-versions}

Los mensajes dentro de la aplicación sólo se enviarán a dispositivos Roku que ejecuten la versión mínima compatible del SDK:

{% sdk_min_versions roku:0.1.2 %}

## Configuración de mensajes dentro de la aplicación

Para procesar mensajes dentro de la aplicación, puedes añadir un observador en `BrazeTask.BrazeInAppMessage`:

```brightscript
m.BrazeTask.observeField("BrazeInAppMessage", "onInAppMessageReceived")
```

Después, dentro de tu controlador, tendrás acceso al mensaje dentro de la aplicación más alto que hayan desencadenado tus campañas:

```brightscript
sub onInAppMessageReceived()
  in_app_message = m.BrazeTask.BrazeInAppMessage
  ...
end sub
```

## Campos de mensajería dentro de la aplicación

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

### Campos de estilo
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

### Campos de botón

| Campos | Descripción |
| ------ | ----------- |
| `click_action` | `"URI"` o `"NONE"`. Utiliza este campo para indicar si el mensaje dentro de la aplicación debe abrirse a un enlace URI o cerrar el mensaje al hacer clic. |
| `id` | El valor ID del propio botón. |
| `text` | El texto que se mostrará en el botón. |
| `uri` | Se enviará a los usuarios de tu URI en función de tu `click_action`. Este campo debe incluirse cuando `click_action` es `"URI"`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Manejar las interacciones

Tendrás que asegurarte de que se llaman determinadas funciones para gestionar los análisis de tu campaña.

##### Cuando se muestra un mensaje

Cuando se muestra o se ve un mensaje, registra una impresión:
```brightscript
LogInAppMessageImpression(in_app_message.id, brazetask)
```

##### Cuando un usuario hace clic en un mensaje
Una vez que un usuario hace clic en el mensaje, registra un clic y luego procesa `in_app_message.click_action`:
```brightscript
LogInAppMessageClick(in_app_message.id, brazetask)
```

##### Cuando un usuario hace clic en un botón
Si el usuario hace clic en un botón, registra el clic en el botón y luego procesa `inappmessage.buttons[selected].click_action`:

```brightscript
LogInAppMessageButtonClick(inappmessage.id, inappmessage.buttons[selected].id, brazetask)
```

##### Después de procesar un mensaje dentro de la aplicación
Después de procesar un mensaje dentro de la aplicación, debes borrar el campo:
```brightscript
m.BrazeTask.BrazeInAppMessage = invalid
```
