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

Si quieres guardar tu respuesta en una variable, se recomienda devolver objetos JSON. Y si quieres que la respuesta de Contenido conectado sustituya la etiqueta por el texto, asegúrate de que la respuesta no sea JSON válido (según la definición de [json.org](http://www.json.org))

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

![Notificación push con el mensaje "¡Está lloviendo! Coge un paraguas!"]({% image_buster /assets/img_archive/connected_weather_push2.png %} "Ejemplo de uso de push de contenido conectado"){:style="max-width:50%" }

De manera predeterminada, el contenido conectado establecerá un encabezado `Content-Type` en una solicitud GET HTTP que haga a `application/json` con `Accept: */*`. Si necesita otro tipo de contenido, especifíquelo explícitamente añadiendo `:content_type your/content-type` a la etiqueta. A continuación, Braze establecerá tanto el encabezado Content-Type como Accept en el tipo que especifique.

{% raw %}
```js
{% connected_content http://numbersapi.com/random/trivia :content_type application/json %}
```
{% endraw %}

## HTTP POST

De manera predeterminada, el Contenido conectado realiza una solicitud HTTP GET a la URL especificada. Para realizar una solicitud POST en su lugar, especifique `:method post`.

Opcionalmente, puede proporcionar un cuerpo POST especificando `:body` seguido de una cadena de consulta con el formato `key1=value1&key2=value2&...` o una referencia a los valores capturados. Content-Type predeterminado a `application/x-www-form-urlencoded`. Si especifica `:content_type application/json` y proporciona un cuerpo con codificación URL de formulario como `key1=value1&key2=value2`, Braze codificará automáticamente el cuerpo en JSON antes de enviarlo.

El Contenido conectado tampoco almacena en caché las llamadas POST de forma predeterminada. Puedes actualizar este comportamiento añadiendo `:cache_max_age` a la llamada POST de Contenido conectado.

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


[16]: [success@braze.com](mailto:success@braze.com)
