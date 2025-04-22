---
nav_title: Reintentos de contenido conectado
article_title: Reintentos de contenido conectado
page_order: 5
description: "Este artículo de referencia explica cómo tratar los reintentos de Contenido conectado."

---

# 

> Esta página explica cómo añadir reintentos a tus llamadas de Contenido conectado.

##  

 En este caso, Braze admite la lógica de reintento para reintentar la solicitud utilizando un backoff exponencial.

{% alert note %}
Contenido conectado `:retry` no está disponible para los mensajes in-app.
{% endalert %}

## 




```
{% connected_content https://yourwebsite.com/api/endpoint :retry %}
{% connected_content https://www.braze.com :save my_content :basic_auth auth_name :retry %}
```
{% endraw %}



### Resultados del reintento

#### Cuando un reintento tiene éxito



#### Cuando falla la llamada a la API y se habilitan los reintentos

 Braze moverá cualquier mensaje fallido al final de la cola y añadirá minutos adicionales, si es necesario, al total de minutos que tardaría en enviar su mensaje.

