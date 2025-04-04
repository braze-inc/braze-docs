---
nav_title: Reintentos de contenido conectado
article_title: Reintentos de contenido conectado
page_order: 3
description: "Este artículo de referencia explica cómo tratar los reintentos de Contenido conectado."

---

# Reintentos de contenido conectado

> Dado que Connected Content depende de la recepción de datos de las API, existe la posibilidad de que una API no esté disponible de forma intermitente mientras Braze realiza la llamada. En este caso, Braze admite la lógica de reintento para reintentar la solicitud utilizando un backoff exponencial. <br><br> Esta página explica cómo añadir reintentos a tus llamadas de Contenido conectado.

## Cómo habilitar los reintentos

Para habilitar los reintentos, añada `:retry` en la llamada al contenido conectado, como se muestra en el siguiente fragmento de código:
{% raw %}
```
{% connected_content https://yourwebsite.com/api/endpoint :retry %}
{% connected_content https://www.braze.com :save my_content :basic_auth auth_name :retry %}
```
{% endraw %}

## Resultados del reintento

### Cuando falla la llamada a la API y se habilitan los reintentos

Si la llamada a la API falla y esta opción está activada, Braze reintentará la llamada respetando el [límite de velocidad][47] establecido para cada reenvío. Braze moverá cualquier mensaje fallido al final de la cola y añadirá minutos adicionales, si es necesario, al total de minutos que tardaría en enviar su mensaje.

### Cuando un reintento tiene éxito

Si un intento de reintento tiene éxito, el mensaje se envía y no se intentan más reintentos para ese mensaje. Si la llamada a Contenido Conectado falla 5 veces, el mensaje se aborta de forma similar a si se activara una [etiqueta de mensaje de abortar][1].

{% alert note %}
Contenido conectado `:retry` no está disponible para los mensajes in-app.
{% endalert %}


[1]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content/
[16]: [success@braze.com](mailto:success@braze.com)
[47]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#delivery-speed-rate-limiting
