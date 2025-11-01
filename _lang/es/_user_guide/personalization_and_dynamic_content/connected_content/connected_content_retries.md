---
nav_title: Reintentos de contenido conectado
article_title: Reintentos de contenido conectado
page_order: 5
description: "Este artículo de referencia explica cómo tratar los reintentos de Contenido conectado."

---

# Utilizar la lógica de reintento para el Contenido conectado

> Esta página explica cómo añadir reintentos a tus llamadas de Contenido conectado.

## Cómo funcionan los reintentos 

Dado que el Contenido conectado depende de la recepción de datos de las API, una API podría no estar disponible de forma intermitente mientras Braze realiza la llamada. En este caso, Braze admite la lógica de reintento para reintentar la solicitud utilizando la retirada exponencial.

{% alert note %}
Contenido conectado `:retry` no está disponible para mensajes dentro de la aplicación.
{% endalert %}

## Utilizar la lógica de reintento

Para utilizar la lógica de reintento, añade la etiqueta `:retry` a la llamada al contenido conectado, como se muestra en el siguiente fragmento de código:

{% raw %}
```
{% connected_content https://yourwebsite.com/api/endpoint :retry %}
{% connected_content https://www.braze.com :save my_content :basic_auth auth_name :retry %}
```
{% endraw %}

Cuando se incluye una etiqueta `:retry` en la llamada de contenido conectado, Braze intentará reintentar la llamada hasta cinco veces.

### Resultados del reintento

#### Cuando un reintento tiene éxito

Si un intento de reintento tiene éxito, el mensaje se envía y no se intentan más reintentos para ese mensaje.

#### Cuando falla la llamada a la API y se habilitan los reintentos

Si la llamada a la API falla y esto está habilitado, Braze reintentará la llamada respetando el [límite de velocidad]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#delivery-speed-rate-limiting) que establezcas para cada reenvío. Braze moverá cualquier mensaje fallido al final de la cola y añadirá minutos adicionales, si es necesario, al total de minutos que tardaría en enviarse tu mensaje.

Si la llamada a Contenido conectado da error más de cinco veces, el mensaje se aborta, de forma similar a como se desencadena una [etiqueta de mensaje de abortar]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content/).