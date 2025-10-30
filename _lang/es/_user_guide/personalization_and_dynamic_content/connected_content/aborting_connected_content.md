---
nav_title: Abortar contenido conectado
article_title: Abortar contenido conectado
page_order: 2
description: "Este artículo de referencia cubre algunas de las mejores prácticas de cancelación de mensajes para el Contenido conectado."
---

# Abortar contenido conectado {#aborting-connected-content}

> Cuando utilizas la plantilla Liquid, tienes la opción de abortar mensajes con lógica condicional. Esta página cubre las mejores prácticas al hacerlo.

En el siguiente ejemplo, los condicionales `connected.recommendations.size < 5` y `connected.foo.bar == nil` especifican situaciones que harían que se abortara el mensaje.

{% raw %}
```
{% connected_content https://example.com/webservice.json :save connected %}
   {% if connected.recommendations.size < 5 or connected.foo.bar == nil %}
     {% abort_message() %}
   {% endif %}
```
{% endraw %}

## Especifica una razón para abortar

También puedes especificar un motivo de cancelación, que se guardará en el [Registro de Actividad de Mensajes]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/). Este motivo de cancelación debe ser una cadena y no puede contener Liquid.

{% raw %}
`{% abort_message('Could not get enough recommendations') %}`
{% endraw %}

{% alert important %}
Braze no cuenta los mensajes abortados en el recuento de envíos de tu cuenta Braze o en Currents.
{% endalert %}
