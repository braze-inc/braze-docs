---
nav_title: Anular contenidos conectados
article_title: Anular contenidos conectados
page_order: 2
description: "Este artículo de referencia cubre algunas de las mejores prácticas de cancelación de mensajes para el Contenido conectado."

---

# Anular contenidos conectados {#aborting-connected-content}

> Cuando utilizas la plantilla Liquid, tienes la opción de abortar mensajes con lógica condicional. Esta página cubre las mejores prácticas al hacerlo.

En el siguiente ejemplo, los condicionales `connected.recommendations.size < 5` y `connected.foo.bar == nil` especifican situaciones que harían que el mensaje fuera abortado.

{% raw %}
```
{% connected_content https://example.com/webservice.json :save connected %}
   {% if connected.recommendations.size < 5 or connected.foo.bar == nil %}
     {% abort_message() %}
   {% endif %}
```
{% endraw %}

## Especifica una razón para abortar

También puede especificar un motivo de cancelación, que se guardará en el [registro de actividad de mensajes]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/). Esta razón para abortar debe ser una cadena y no puede contener Liquid.

{% raw %}
`{% abort_message('Could not get enough recommendations') %}`
{% endraw %}

{% alert important %}
Braze no cuenta los mensajes abortados en el recuento de envíos de tu cuenta Braze o en Currents.
{% endalert %}
