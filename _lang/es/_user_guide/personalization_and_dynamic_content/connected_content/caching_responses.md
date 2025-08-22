---
nav_title: Almacenamiento en caché de las respuestas
article_title: Almacenamiento en caché de respuestas de contenido conectado
page_order: 2.5
description: "Este artículo explica cómo almacenar en caché las respuestas del Contenido conectado en diferentes campañas o mensajes en el mismo espacio de trabajo para optimizar la velocidad de envío."
---

# Almacenamiento en caché de respuestas de contenido conectado

> Las respuestas del contenido conectado pueden almacenarse en caché en diferentes campañas o mensajes (en el mismo espacio de trabajo) para optimizar la velocidad de envío.

Braze no registra ni almacena permanentemente las respuestas de Contenido conectado. Si eliges explícitamente almacenar una respuesta a una llamada de Contenido conectado como una variable Liquid, Braze sólo la almacena en memoria, es decir, en un almacenamiento temporal que se elimina tras un breve periodo de tiempo, para renderizar la variable Liquid y enviar el mensaje.

Para evitar el almacenamiento en caché, puedes especificar `:no_cache`, lo que puede provocar un aumento del tráfico de red. Para ayudar a solucionar problemas y controlar la salud del sistema, Braze también puede registrar las llamadas a Contenido conectado que fallan (como `404` y `429`). Estos registros se conservan hasta 30 días.

## Configuración predeterminada de la caché

La antigüedad de la caché es de hasta cinco minutos (300 segundos). Puedes actualizarlo añadiendo el parámetro `:cache_max_age` a la llamada al Contenido conectado. Un ejemplo:

{% raw %}
```
{{ {% connected_content [https://example.com/webservice.json] :cache_max_age 900 %}}}
```
{% endraw %}

Las peticiones GET se almacenan en caché. Puedes configurarlo añadiendo el parámetro :no_cache a la llamada al Contenido conectado.

Las peticiones POST no se almacenan en caché. Esto puede forzarse añadiendo el parámetro :cache_max_age a la llamada al Contenido conectado. El tiempo mínimo de caché es de 5 minutos, y el tiempo máximo de caché es de 4 horas.

{% alert note %}
La configuración de la caché no está garantizada. El almacenamiento en caché puede reducir las llamadas a tus puntos finales, por lo que recomendamos utilizar varias llamadas por punto final dentro de la duración del almacenamiento en caché, en lugar de depender excesivamente de éste.
{% endalert %}

### Límite de tamaño de la caché

El cuerpo de respuesta del Contenido conectado puede ser de hasta 1 MB. Si el cuerpo de la respuesta supera 1 MB, no se almacenará en caché.

## Tiempo de caché 

El Contenido conectado guardará en caché el valor que devuelva de los puntos finales GET durante un mínimo de cinco minutos. Si no se especifica un tiempo de caché, el tiempo de caché predeterminado es de cinco minutos.

El tiempo de caché del contenido conectado puede configurarse para que sea mayor con :cache_max_age, como se muestra en el siguiente ejemplo. El tiempo mínimo de caché es de cinco minutos y el máximo de cuatro horas. Los datos del Contenido conectado se almacenan en caché en memoria utilizando un sistema de caché volátil, como Memcached. 

Como resultado, independientemente del tiempo de caché especificado, los datos de Contenido Conectado pueden ser desalojados de la caché en memoria de Braze antes de lo especificado. Esto significa que las duraciones de caché son sugerencias y pueden no representar realmente la duración que se garantiza que los datos serán almacenados en caché por Braze y es posible que vea más solicitudes de Contenido Conectado de las que podría esperar con una duración de caché determinada.

### Caché durante los segundos especificados

Este ejemplo almacenará en caché durante 900 segundos (o 15 minutos).

{% raw %}
```
{% connected_content https://example.com/webservice.json :cache_max_age 900 %}
```
{% endraw %}

### Eliminación de caché

Para evitar que Connected Content almacene en caché el valor que devuelve de una solicitud GET, puede utilizar la configuración `:no_cache`. Sin embargo, las respuestas de los hosts internos de Braze seguirán almacenándose en caché.

{% raw %}
```js
{% connected_content https://example.com/webservice.json :no_cache %}
```
{% endraw %}

{% alert important %}
Asegúrese de que el punto final de contenido conectado proporcionado puede gestionar grandes cantidades de tráfico antes de utilizar esta opción, o es probable que aumente la latencia de envío (mayores retrasos o intervalos de tiempo más amplios entre la solicitud y la respuesta) debido a que Braze realiza solicitudes de contenido conectado para cada mensaje.
{% endalert %}

Con un POST no necesitas almacenar en caché el busto, ya que Braze nunca almacena en caché los resultados de las peticiones POST.

## Lo que hay que saber

- El almacenamiento en caché puede ayudar a reducir las llamadas duplicadas de Contenido conectado. Sin embargo, no está garantizado que siempre resulte en una única llamada de Contenido conectado por usuario.
- El almacenamiento en caché del Contenido conectado se basa en la URL y el espacio de trabajo. Si la llamada al contenido conectado es a la misma URL, puede almacenarse en caché en todas las campañas y lienzos.
- La caché se basa en una URL única, no en un ID de usuario o campaña. Esto significa que la versión en caché de una llamada a Contenido conectado podría utilizarse en varios usuarios y campañas de un espacio de trabajo si la URL es la misma.
