---
nav_title: Variáveis de conteúdo local conectado
article_title: Variáveis de conteúdo local conectado
page_order: 1
description: "Este artigo de referência aborda como usar e armazenar variáveis locais do Connected Content."
search_rank: 1
---

# Variáveis de conteúdo local conectado

> Esta página fornece uma visão geral das variáveis locais do Connected Content e como usá-las e armazená-las.

O Braze faz uma solicitação GET padrão no momento do envio para o endpoint especificado na tag `connected_content`. Se o ponto de extremidade retornar JSON, ele será automaticamente analisado e armazenado em uma variável chamada `connected`. Se o ponto de extremidade retornar texto, ele será inserido diretamente na mensagem no lugar da tag `connected_content`.

Se você quiser salvar sua resposta em uma variável, é recomendável retornar objetos JSON. E se você quiser que a resposta do Connected Content substitua a tag pelo texto, certifique-se de que a resposta não seja um JSON válido (conforme definido por [json.org](http://www.json.org))

Você também pode especificar `:save your_variable_name` após o URL para salvar os dados como outra coisa. Por exemplo, a seguinte tag `connected_content` armazenará a resposta em uma variável local chamada `localweather` (você pode salvar várias variáveis JSON `connected_content` ):

{% raw %}
```js
{% connected_content https://www.metaweather.com/api/location/2459115/ :save localweather %}
```
{% endraw %}

Metaweather é uma API meteorológica gratuita que usa um "ID Where-on-Earth" para retornar o clima em uma área. Use esse código apenas para fins de teste e aprendizado.

>  A variável armazenada só pode ser acessada dentro do campo que contém a solicitação `connected_content`. Por exemplo, se você quiser usar a variável `localweather` nos campos de mensagem e título, deverá fazer a solicitação `connected_content` em ambos os campos. Se a solicitação for idêntica, o Braze usará os resultados armazenados em cache, em vez de fazer uma segunda solicitação ao servidor de destino. No entanto, as chamadas de Connected Content feitas via HTTP POST não são armazenadas em cache por padrão e farão uma segunda solicitação ao servidor de destino. Se você quiser adicionar o armazenamento em cache às chamadas POST, consulte a opção [`cache_max_age`](#configurable-caching) opção.

## Análise de JSON

A Connected Content interpretará todos os resultados formatados em JSON em uma variável local, quando você especificar `:save`. Por exemplo, um endpoint Connected Content relacionado ao clima retorna o seguinte objeto JSON, que você armazena em uma variável local `localweather` especificando `:save localweather`.
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

Você pode testar se está chovendo ou não fazendo referência a `{{localweather.consolidated_weather[0].weather_state_name}}`, que, se usado nesse objeto, retornaria `Clear`. Se você também quiser personalizar com o nome do local resultante, `{{localweather.title}}` retornará `New York`.
{% endraw %}

A imagem a seguir ilustra o tipo de realce de sintaxe que você deve ver no painel se estiver configurando tudo corretamente. Ele também demonstra como você pode aproveitar o exemplo da solicitação `connected_content`!

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

Se a API respondesse com {%raw%}`{{localweather.consolidated_weather[0].weather_state_name}}`{%endraw%} retornando `Rain`, o usuário receberia esse push.

Notificação push com a mensagem "It's raining! Pegue um guarda-chuva!"]({% image_buster /assets/img_archive/connected_weather_push2.png %} "Connected Content Push Usage Example"){:style="max-width:50%" }

{% multi_lang_include connected_content.md section='default behavior' %}

## HTTP POST

{% multi_lang_include connected_content.md section='http post' %}

### Fornecimento de corpo JSON

Se você quiser fornecer seu próprio corpo JSON, poderá escrevê-lo em linha se não houver espaços. Se o seu corpo tiver espaços, você deverá usar uma instrução de atribuição ou captura. Ou seja, qualquer uma dessas três opções é aceitável:

{% raw %}
##### Inline: espaços não são permitidos

```js
{% connected_content https://example.com/api/endpoint :method post :body {"foo":"bar","baz":"{{1|plus:1}}"} :content_type application/json %}
```

##### Corpo em uma declaração de captura: espaços permitidos

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
##### Corpo em uma instrução de atribuição: espaços permitidos

```js
{% assign postbody = '{"foo":"bar", "baz": "2"}' %}
{% connected_content https://example.com/api/endpoint :method post :body {{postbody}} :content_type application/json %}
```
{% endraw %}

## Códigos de status HTTP

Você pode utilizar o status HTTP de uma chamada de Connected Content salvando-o primeiro como uma variável local e, em seguida, usando a tecla `__http_status_code__`. Por exemplo:

{% raw %}
```js
{% connected_content https://example.com/api/endpoint :save result %}
{% if result.__http_status_code__ != 200 %}
  {% abort_message('Connected Content returned a non-200 status code') %}
{% endif %}
```
{% endraw %}

{% alert important %}
Essa chave só será adicionada automaticamente ao objeto Connected Content se o ponto de extremidade retornar um objeto JSON válido e uma resposta `2XX`. Se o ponto de extremidade retornar uma matriz ou outro tipo, essa chave não poderá ser definida automaticamente na resposta.
{% endalert %}


[16]: [success@braze.com](mailto:success@braze.com)
