---
nav_title: Anular mensajes
article_title: Anular mensajes de Liquid
page_order: 7
description: "Este artículo de referencia trata sobre la cancelación de mensajes Liquid y algunos ejemplos de uso."

---

# Anular mensajes

> Opcionalmente, puede abortar mensajes Líquidos dentro de condicionales. Este artículo de referencia enumera algunos ejemplos de cómo puede utilizarse esta función en campañas de marketing.

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

![Registro de error de mensaje en la consola para desarrolladores con un mensaje de cancelación de "el idioma era nulo".][26]

## Consulta de mensajes de cancelación

Puedes utilizar [el Generador de consultas]({{site.baseurl}}/user_guide/analytics/query_builder/) o tu propio almacén de datos, si está conectado a Braze, para consultar mensajes específicos de interrupción que se desencadenan cuando la lógica de Liquid hace que se interrumpa un mensaje.

[15]: {% image_buster /assets/img_archive/liquid_abort.png %}
[26]: {% image_buster /assets/img_archive/developer_console.png %}
[31]:[31]:
[32]:[32]:
[34]:{% image_buster /assets/img_archive/personalized_iflogic_.png %}
[37]:\#accounting-for-null-attribute-values
