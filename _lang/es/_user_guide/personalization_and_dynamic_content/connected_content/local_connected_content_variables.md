---
nav_title: Variables locales de Contenido conectado
article_title: Variables locales de Contenido conectado
page_order: 1
description: "Este artículo de referencia explica cómo utilizar y almacenar variables locales de contenido conectado."
search_rank: 1
---

# Variables locales de contenido conectado

> Esta página proporciona un resumen de las variables locales de Contenido conectado y de cómo utilizarlas y almacenarlas.

Braze realiza una solicitud GET estándar en el momento del envío al punto final especificado en la etiqueta `connected_content`. Si el endpoint devuelve JSON, se analiza automáticamente y se almacena en una variable llamada `connected`. Si el endpoint devuelve texto, éste se insertará directamente en el mensaje en lugar de la etiqueta `connected_content`.

Si quieres guardar tu respuesta en una variable, se recomienda devolver objetos JSON. Y si quieres que la respuesta de Contenido conectado sustituya la etiqueta por el texto, asegúrate de que la respuesta no sea JSON válido (como se define en [json.org][46])

También puedes especificar `:save your_variable_name` después de la URL para guardar los datos como otra cosa. Por ejemplo, la siguiente etiqueta `connected_content` almacenará la respuesta en una variable local denominada `localweather` (puede guardar varias variables JSON `connected_content` ):

{% raw %}
```js
{% connected_content https://www.metaweather.com/api/location/2459115/ :save localweather %}
```
{% endraw %}

Metaweather es una API meteorológica gratuita que utiliza un "ID de lugar en la Tierra" para devolver el tiempo en una zona. Utilice este código sólo con fines de prueba y aprendizaje.

>  Sólo se puede acceder a la variable almacenada dentro del campo que contiene la solicitud `connected_content`. Por ejemplo, si desea utilizar la variable `localweather` tanto en el campo de mensaje como en el de título, deberá realizar la petición `connected_content` dentro de ambos campos. Si la solicitud es idéntica, Braze utilizará los resultados almacenados en caché, en lugar de realizar una segunda solicitud al servidor de destino. Sin embargo, las llamadas a Contenidos Conectados realizadas a través de HTTP POST no se almacenan en caché por defecto y realizarán una segunda petición al servidor de destino. Si deseas añadir caché a las llamadas POST, consulta la opción [`cache_max_age`](#configurable-caching).

## Análisis JSON

Connected Content interpretará cualquier resultado con formato JSON en una variable local, cuando especifique `:save`. Por ejemplo, un punto final de Contenido conectado relacionado con el tiempo devuelve el siguiente objeto JSON, que almacenas en una variable local `localweather` especificando `:save localweather`.
{% raw %}

```js
{
  "consolidated_weather": [
    {
      "id": 5.8143475362693e+15,
      "weather_state_name": "Clear",
      "weather_state_abbr": "c",
      "wind_direction_compass": "WSW",
      "created": "2017-06-12T14:14:46.268110Z",
      "applicable_date": "2017-06-12",
      "min_temp": 22.511666666667,
      "max_temp": 31.963333333333,
      "the_temp": 27.803333333333,
      "wind_speed": 6.8884690250312,
      "wind_direction": 251.62921994166,
      "air_pressure": 1021.335,
      "humidity": 50,
      "visibility": 14.945530601288,
      "predictability": 68
    },
    .
    .
    .
    "title": "New York",
    "location_type": "City",
    "woeid": 2459115,
    "latt_long": "40.71455,-74.007118",
    "timezone": "US\/Eastern"
  }
```

Puede comprobar si está lloviendo o no haciendo referencia a `{{localweather.consolidated_weather[0].weather_state_name}}`, que si se utiliza en este objeto devolvería `Clear`. Si desea personalizar también con el nombre de la ubicación resultante, `{{localweather.title}}` devuelve `New York`.
{% endraw %}

La siguiente imagen ilustra el tipo de resaltado de sintaxis que debería ver en el panel de control si está configurando las cosas correctamente. También muestra cómo se puede aprovechar el ejemplo de la solicitud `connected_content`.

{% raw %}
```liquid
{% connected_content https://www.metaweather.com/api/location/search/?query={{custom_attribute.${customCity}}} :save locationjson %}
{% connected_content https://www.metaweather.com/api/location/{{locationjson[0].woeid}}/ :save localweather %}

{% if {{localweather.consolidated_weather[0].weather_state_name}} == 'Rain' %}
It's raining! Grab an umbrella!
{% elsif {{localweather.consolidated_weather[0].weather_state_name}} == 'Clouds' %}
No sunscreen needed :)
{% else %}
Enjoy the weather!
{% endif %}
```
{% endraw %}

Si la API respondiera con {%raw%}`{{localweather.consolidated_weather[0].weather_state_name}}`{%endraw%} devolviendo `Rain`, el usuario recibiría entonces este push.

![Notificación push con el mensaje "¡Está lloviendo! Toma un paraguas".][17]{:style="max-width:50%" }

De manera predeterminada, el contenido conectado establecerá un encabezado `Content-Type` en una solicitud GET HTTP que haga a `application/json` con `Accept: */*`. Si necesita otro tipo de contenido, especifíquelo explícitamente añadiendo `:content_type your/content-type` a la etiqueta. A continuación, Braze establecerá tanto el encabezado Content-Type como Accept en el tipo que especifique.

{% raw %}
```js
{% connected_content http://numbersapi.com/random/trivia :content_type application/json %}
```
{% endraw %}

## HTTP POST

De manera predeterminada, el Contenido conectado realiza una solicitud HTTP GET a la URL especificada. Para realizar una solicitud POST en su lugar, especifique `:method post`.

Opcionalmente, puede proporcionar un cuerpo POST especificando `:body` seguido de una cadena de consulta con el formato `key1=value1&key2=value2&...` o una referencia a los valores capturados. Content-Type predeterminado a `application/x-www-form-urlencoded`. Si especifica `:content_type application/json` y proporciona un cuerpo con codificación URL de formulario como `key1=value1&key2=value2`, Braze codificará automáticamente el cuerpo en JSON antes de enviarlo.

#### Tipo de contenido por defecto
{% raw %}
```js
{% connected_content https://example.com/api/endpoint :method post :body key1=value1&key2=value2 %}
```
#### Content-Type para aplicación/JSON
```js
{% connected_content https://example.com/api/endpoint :method post :body key1=value1&key2=value2 :content_type application/json %}
```
{% endraw %}

### Proporcionar cuerpo JSON
Si quieres proporcionar tu propio cuerpo JSON, puedes escribirlo en línea si no hay espacios. Si tu cuerpo tiene espacios, debes usar una sentencia assign o capture. Es decir, cualquiera de estos tres es aceptable:

{% raw %}
##### Inline: espacios no permitidos
```js
{% connected_content https://example.com/api/endpoint :method post :body {"foo":"bar","baz":"{{1|plus:1}}"} :content_type application/json %}
```

##### Cuerpo en una declaración de captura: espacios permitidos
```js
{% capture postbody %}
{"foo": "bar", "baz": "{{ 1 | plus: 1 }}"}
{% endcapture %}
{% connected_content https://example.com/api/endpoint :method post :body {{postbody}} :content_type application/json %}
```
{% endraw %}

{% raw %}
```js
{% capture postbody %}
{
"ids":[ca_57832,ca_75869],"include":{"attributes":{"withKey":["daily_deals"]}}
}
{% endcapture %}

{% connected_content
    https://example.com/api/endpoint
    :method post
    :headers {
      "Content-Type": "application/json"
  }
  :body {{postbody}}
  :save result
%}
```
{% endraw %}
{% raw %}
##### Cuerpo en una sentencia assign: espacios permitidos
```js
{% assign postbody = '{"foo":"bar", "baz": "2"}' %}
{% connected_content https://example.com/api/endpoint :method post :body {{postbody}} :content_type application/json %}
```
{% endraw %}

## Códigos de estado HTTP

Puede utilizar el estado HTTP de una llamada a Contenido Conectado guardándolo primero como una variable local y utilizando después la tecla `__http_status_code__`. Por ejemplo:

{% raw %}
```js
{% connected_content https://example.com/api/endpoint :save result %}
{% if result.__http_status_code__ != 200 %}
  {% abort_message('Connected Content returned a non-200 status code') %}
{% endif %}
```
{% endraw %}

{% alert important %}
Esta clave sólo se añadirá automáticamente al objeto Contenido conectado si el endpoint devuelve un objeto JSON válido y una respuesta `2XX`. Si el endpoint devuelve un array u otro tipo, esa clave no puede establecerse automáticamente en la respuesta.
{% endalert %}

## Almacenamiento en caché configurable {#configurable-caching}

Las respuestas de Connected Content pueden almacenarse en caché en diferentes campañas o mensajes (dentro del mismo espacio de trabajo) para optimizar la velocidad de envío.

Braze no registra ni almacena permanentemente las respuestas de Contenido conectado. Si eliges explícitamente almacenar una respuesta a una llamada de Contenido conectado como una variable Liquid, Braze sólo la almacena en memoria, es decir, en un almacenamiento temporal que se elimina tras un breve periodo de tiempo, para renderizar la variable Liquid y enviar el mensaje. Para evitar por completo el almacenamiento en caché, puedes especificar `:no_cache`, lo que puede provocar un aumento del tráfico de red. Para ayudar a solucionar problemas y supervisar el estado del sistema, Braze también puede registrar las llamadas de contenido conectado que fallan (como 404 y 429); estos registros se conservan durante un máximo de 30 días.

### Límite de tamaño de la caché

El cuerpo de la respuesta Contenido conectado no debe superar 1 MB, o no se almacenará en caché.

### Tiempo de caché

Connected Content guardará en caché el valor que devuelva de los puntos finales GET durante un mínimo de 5 minutos. Si no se especifica un tiempo de caché, el tiempo de caché predeterminado es de 5 minutos. 

El tiempo de caché de Connected Content puede configurarse para que sea más largo con `:cache_max_age`, como se muestra en el siguiente ejemplo. El tiempo mínimo de caché es de 5 minutos y el tiempo máximo de caché es de 4 horas. Los datos del Contenido conectado se almacenan en caché en memoria utilizando un sistema de caché volátil, como Memcached. Como resultado, independientemente del tiempo de caché especificado, los datos de contenido conectado pueden ser desalojados de la caché en memoria de Braze antes de lo especificado. Esto significa que las duraciones de caché son sugerencias y pueden no representar realmente la duración que se garantiza que los datos serán almacenados en caché por Braze y es posible que vea más solicitudes de Contenido Conectado de las que podría esperar con una duración de caché determinada.

Por defecto, el Contenido conectado no almacena en caché las llamadas POST. Puede cambiar este comportamiento añadiendo `:cache_max_age` a la llamada POST de contenido conectado.

#### Caché durante los segundos especificados

Este ejemplo almacenará en caché durante 900 segundos (o 15 minutos).
{% raw %}
```
{% connected_content https://example.com/webservice.json :cache_max_age 900 %}
```
{% endraw %}

#### Eliminación de caché

Para evitar que Connected Content almacene en caché el valor que devuelve de una solicitud GET, puede utilizar la configuración `:no_cache`. Sin embargo, las respuestas de los hosts internos de Braze seguirán almacenándose en caché.

{% raw %}
```js
{% connected_content https://example.com/webservice.json :no_cache %}
```
{% endraw %}

{% alert important %}
Asegúrese de que el punto final de contenido conectado proporcionado puede gestionar grandes cantidades de tráfico antes de utilizar esta opción, o es probable que aumente la latencia de envío (mayores retrasos o intervalos de tiempo más amplios entre la solicitud y la respuesta) debido a que Braze realiza solicitudes de contenido conectado para cada mensaje.
{% endalert %}

Con un `POST` no necesitas usar la técnica de eliminación de caché, ya que Braze nunca almacena en caché los resultados de las solicitudes a `POST`.

[16]: [success@braze.com](mailto:success@braze.com)
[17]: {% image_buster /assets/img_archive/connected_weather_push2.png %} "Ejemplo de uso de push de contenido conectado"
[46]: http://www.json.org
