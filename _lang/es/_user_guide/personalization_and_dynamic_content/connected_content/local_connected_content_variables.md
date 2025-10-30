---
nav_title: Variables locales de contenido conectado
article_title: Variables de contenido conectado local
page_order: 1
description: "Este artículo de referencia explica cómo utilizar y almacenar variables locales de Contenido conectado."
search_rank: 1
---

# Variables locales de contenido conectado

> Esta página proporciona un resumen de las variables locales de Contenido conectado y de cómo utilizarlas y almacenarlas.

Braze realiza una solicitud GET estándar en el momento del envío al punto final especificado en la etiqueta `connected_content`. Si el punto final devuelve JSON, se analiza automáticamente y se almacena en una variable llamada `connected`. Si el punto final devuelve texto, se insertará directamente en el mensaje en lugar de la etiqueta `connected_content`.

Si quieres guardar tu respuesta en una variable, se recomienda devolver objetos JSON. Y si quieres que la respuesta de Contenido conectado sustituya la etiqueta por el texto, asegúrate de que la respuesta no sea JSON válido (según la definición de [json.org](http://www.json.org))

También puedes especificar `:save your_variable_name` después de la URL para guardar los datos como otra cosa. Por ejemplo, la siguiente etiqueta `connected_content` almacenará la respuesta en una variable local llamada `localweather` (puedes guardar varias variables JSON `connected_content` ):

{% raw %}
```js
{% connected_content https://www.metaweather.com/api/location/2459115/ :save localweather %}
```
{% endraw %}

Metaweather es una API meteorológica gratuita que utiliza un "ID de dónde está la Tierra" para devolver el tiempo en una zona. Utiliza este código sólo con fines de prueba y aprendizaje.

>  Sólo se puede acceder a la variable almacenada dentro del campo que contiene la petición `connected_content`. Por ejemplo, si quisieras utilizar la variable `localweather` tanto en el campo mensaje como en el campo título, deberías hacer la petición `connected_content` dentro de ambos campos. Si la petición es idéntica, Braze utilizará los resultados almacenados en caché, en lugar de hacer una segunda petición al servidor de destino. Sin embargo, las llamadas a Contenido conectado realizadas mediante HTTP POST no se almacenan en caché de forma predeterminada y realizarán una segunda solicitud al servidor de destino. Si deseas añadir caché a las llamadas POST, consulta la opción [`cache_max_age`](#configurable-caching) opción

## Análisis JSON

El Contenido conectado interpretará cualquier resultado con formato JSON en una variable local, cuando especifiques `:save`. Por ejemplo, un punto final de Contenido conectado relacionado con el tiempo devuelve el siguiente objeto JSON, que almacenas en una variable local `localweather` especificando `:save localweather`.
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

Puedes comprobar si llueve o no haciendo referencia a `{{localweather.consolidated_weather[0].weather_state_name}}`, que si se utilizara en este objeto devolvería `Clear`. Si quieres personalizar también con el nombre de la ubicación resultante, `{{localweather.title}}` devuelve `New York`.
{% endraw %}

La siguiente imagen ilustra el tipo de resaltado de sintaxis que deberías ver en el panel si estás configurando las cosas correctamente. ¡También demuestra cómo podrías aprovechar el ejemplo de solicitud `connected_content`!

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

¡\![Notificación push con el mensaje "¡Está lloviendo! Coge un paraguas".]({% image_buster /assets/img_archive/connected_weather_push2.png %} "Connected Content Push Usage Example"){:style="max-width:50%" }

{% multi_lang_include connected_content.md section='default behavior' %}

## HTTP POST

{% multi_lang_include connected_content.md section='http post' %}

### Proporcionar cuerpo JSON

Si quieres proporcionar tu propio cuerpo JSON, puedes escribirlo en línea si no hay espacios. Si tu cuerpo tiene espacios, debes utilizar una sentencia asignar o capturar. Es decir, cualquiera de los tres es aceptable:

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
##### Cuerpo en una sentencia asignar: espacios permitidos

```js
{% assign postbody = '{"foo":"bar", "baz": "2"}' %}
{% connected_content https://example.com/api/endpoint :method post :body {{postbody}} :content_type application/json %}
```
{% endraw %}

## Códigos de estado HTTP

Puedes utilizar el estado HTTP de una llamada a Contenido conectado guardándolo primero como variable local y utilizando después la tecla `__http_status_code__`. Por ejemplo:

{% raw %}
```js
{% connected_content https://example.com/api/endpoint :save result %}
{% if result.__http_status_code__ != 200 %}
  {% abort_message('Connected Content returned a non-200 status code') %}
{% endif %}
```
{% endraw %}

{% alert important %}
Esta clave sólo se añadirá automáticamente al objeto Contenido conectado si el punto final devuelve un objeto JSON válido y una respuesta `2XX`. Si el punto final devuelve una matriz u otro tipo, esa clave no puede establecerse automáticamente en la respuesta.
{% endalert %}


[16]: [success@braze.com](mailto:success@braze.com)
