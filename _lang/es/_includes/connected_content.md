{% if include.section == "default behavior" %}

De manera predeterminada, el contenido conectado establecerá un encabezado `Content-Type` en una solicitud GET HTTP que haga a `application/json` con `Accept: */*`. Si necesita otro tipo de contenido, especifíquelo explícitamente añadiendo `:content_type your/content-type` a la etiqueta. A continuación, Braze establecerá tanto el encabezado Content-Type como Accept en el tipo que especifique.

{% raw %}
```js
{% connected_content http://numbersapi.com/random/trivia :content_type application/json %}
```
{% endraw %}

{% endif %}

{% if include.section == "http post" %}

De manera predeterminada, el Contenido conectado realiza una solicitud HTTP GET a la URL especificada. Para realizar una solicitud POST en su lugar, especifique `:method post`.

Opcionalmente, puede proporcionar un cuerpo POST especificando `:body` seguido de una cadena de consulta con el formato `key1=value1&key2=value2&...` o una referencia a los valores capturados. Content-Type predeterminado a `application/x-www-form-urlencoded`. Si especifica `:content_type application/json` y proporciona un cuerpo con codificación URL de formulario como `key1=value1&key2=value2`, Braze codificará automáticamente el cuerpo en JSON antes de enviarlo.

El Contenido conectado tampoco almacena en caché las llamadas POST de forma predeterminada. Puedes actualizar este comportamiento añadiendo `:cache_max_age` a la llamada POST de Contenido conectado.

{% tabs %}
{% tab Tipo de contenido predeterminado %}

{% raw %}
```js
{% connected_content https://example.com/api/endpoint :method post :body key1=value1&key2=value2 %}
```
{% endraw %}

{% endtab %}
{% tab Application/JSON Tipo de contenido %}

{% raw %}
```js
{% connected_content https://example.com/api/endpoint :method post :body key1=value1&key2=value2 :content_type application/json %}
```
{% endraw %}

{% endtab %}
{% endtabs %}


{% endif %}