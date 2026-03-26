---
nav_title: Anular mensajes
article_title: Cancelar mensajes líquidos
page_order: 7
description: "Este artículo de referencia trata sobre la cancelación de mensajes Liquid y algunos ejemplos de uso."

---

# Mensajes de abortar

> Opcionalmente, puedes utilizar la etiqueta de`abort_message("optional reason for aborting")` mensaje Liquid dentro de condicionales para evitar enviar un mensaje a un usuario. Este artículo de referencia enumera algunos ejemplos de cómo puede utilizarse esta función en campañas de marketing.

{% alert note %}
Si se cancela un paso de mensaje en un lienzo, el usuario **no** saldrá del lienzo **y** pasará al siguiente paso.
{% endalert %}

## Mensaje de cancelación si "Número de Partidas Asistidas" = 0

Por ejemplo, supongamos que no desea enviar un mensaje a los clientes que no han asistido a un partido:

{% raw %}
```liquid
{% if custom_attribute.${Number_Game_Attended} == 1 %}
Loved the game? Get 10% off your second one with code SAVE10.
{% elsif custom_attribute.${Number_Game Attended} > 1 %}
Love the games? Get 10% off your next one with code SAVE10.
{% else %}
{% abort_message() %}
{% endif %}
```
{% endraw %}

Este mensaje sólo se enviará a los clientes de los que se sepa que han asistido a un partido.

## Mensaje Sólo para clientes de habla inglesa

Puedes enviar mensajes sólo a clientes que hablen inglés creando una sentencia "if" que coincidirá cuando el idioma de un cliente sea el inglés y una sentencia "else" que abortará el mensaje para cualquiera que no hable inglés o no tenga un idioma en su perfil.

{% raw %}
```liquid

{% if ${language} == 'en' %}
Send this message in English!
{% else %}
{% abort_message() %}
{% endif %}
```

Por defecto, Braze registrará un mensaje de error genérico en el registro de actividad de mensajes:

```text
{% abort_message %} called
```

También puede hacer que el mensaje de cancelación registre algo en el registro de actividad de mensajes incluyendo una cadena dentro del paréntesis:

```liquid
{% abort_message('language was nil') %}
```
{% endraw %}

![Registro de error de mensaje en la consola para desarrolladores con un mensaje de cancelación de "el idioma era nulo".]({% image_buster /assets/img_archive/developer_console.png %})

## Consulta de mensajes de cancelación

Puedes utilizar [el Generador de consultas]({{site.baseurl}}/user_guide/analytics/query_builder/) o tu propio almacén de datos, si está conectado a Braze, para consultar mensajes específicos de interrupción que se desencadenan cuando la lógica de Liquid hace que se interrumpa un mensaje.

## Cuando se evalúa la lógica de abortar

El momento en que se evalúa la lógica de abortar depende del canal de mensajería.

### Notificaciones push, correo electrónico, SMS, webhooks y tarjetas de contenido.

La lógica de abortar se evalúa en el momento del envío, cuando Braze procesa el mensaje para su entrega.

### Mensajes dentro de la aplicación

La lógica de abortar se evalúa en el momento en que se activa el mensaje dentro de la aplicación (por ejemplo, cuando el usuario realiza el evento desencadenante o inicia una sesión), no cuando el mensaje se envía inicialmente al dispositivo. Los mensajes dentro de la aplicación se entregan al SDK al inicio de la sesión y se almacenan en caché localmente; el Liquid, incluidas las`abort_message()`llamadas, se ejecuta cuando se cumple la condición de activación.

## Consideraciones

La etiqueta de`abort_message()` mensaje líquido impide que los mensajes se envíen a los usuarios, lo que significa que el mensaje no se mostrará en los perfiles de usuario y no se tendrá en cuenta para las entregas ni para la limitación de frecuencia.
