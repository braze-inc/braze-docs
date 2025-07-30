---
nav_title: Variáveis de Conteúdo Conectado Local
article_title: Variáveis de Conteúdo Conectado Local
page_order: 1
description: "Este artigo de referência cobre como usar e armazenar variáveis de conteúdos conectados locais."
search_rank: 1
---

# Variáveis de Conteúdo Local Conectado

> Esta página fornece uma visão geral das variáveis locais do Connected Content e como usá-las e armazená-las.

A Braze faz uma solicitação GET padrão no momento do envio para o endpoint especificado na tag `connected_content`. Se o endpoint retornar JSON, ele será automaticamente analisado e armazenado em uma variável chamada `connected`. Se o endpoint retornar texto, ele será inserido diretamente na mensagem no lugar da tag `connected_content`.

Se você deseja salvar sua resposta em uma variável, é recomendável retornar objetos JSON. E se você quiser que a resposta do Connected Content substitua a tag pelo texto, certifique-se de que a resposta não seja um JSON válido (conforme definido por [json.org](http://www.json.org))

Você também pode especificar `:save your_variable_name` após o URL para salvar os dados como outra coisa. Por exemplo, a seguinte tag `connected_content` armazenará a resposta em uma variável local chamada `localweather` (você pode salvar várias variáveis JSON `connected_content`):

{% raw %}
```js
{% connected_content https://www.metaweather.com/api/location/2459115/ :save localweather %}
```
{% endraw %}

Metaweather é uma API de clima gratuita que usa um "Where-on-Earth ID" para retornar o clima em uma região. Use este código apenas para fins de teste e aprendizado.

>  A variável armazenada só pode ser acessada dentro do campo que contém a `connected_content` solicitação. Por exemplo, se você quiser usar a variável `localweather` tanto no campo de mensagem quanto no campo de título, você deve fazer a solicitação `connected_content` dentro de ambos os campos. Se a solicitação for idêntica, a Braze usará os resultados em cache, em vez de fazer uma segunda solicitação ao servidor de destino. No entanto, as chamadas de Conteúdo Conectado feitas via HTTP POST não são armazenadas em cache por padrão e farão uma segunda solicitação ao servidor de destino. Se você deseja adicionar cache às chamadas POST, consulte a opção [`cache_max_age`](#configurable-caching).

## análise JSON

O conteúdo conectado interpretará quaisquer resultados formatados em JSON em uma variável local, quando você especificar `:save`. Por exemplo, um endpoint de conteúdo conectado relacionado ao clima retorna o seguinte objeto JSON, que você armazena em uma variável local `localweather` especificando `:save localweather`.
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

Você pode testar se está chovendo ou não referenciando `{{localweather.consolidated_weather[0].weather_state_name}}`, o que, se usado neste objeto, retornaria `Clear`. Se você também quiser personalizar com o nome do local resultante, `{{localweather.title}}` retorna `New York`.
{% endraw %}

A imagem a seguir ilustra o tipo de realce de sintaxe que você deve ver no dashboard se estiver configurando as coisas corretamente. Também demonstra como você pode aproveitar o exemplo de solicitação `connected_content`!

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

Se a API respondesse com {%raw%}`{{localweather.consolidated_weather[0].weather_state_name}}`{%endraw%} retornando `Rain`, o usuário receberia este push.

![Notificação por push com a mensagem "Está chovendo!" Pegue um guarda-chuva!"]({% image_buster /assets/img_archive/connected_weather_push2.png %} "Connected Content Push Usage Example"){:style="max-width:50%" }

Por padrão, o conteúdo conectado definirá um `Content-Type` cabeçalho em uma solicitação HTTP GET que ele faz para `application/json` com `Accept: */*`. Se precisar de outro tipo de conteúdo, especifique-o explicitamente adicionando `:content_type your/content-type` à tag. A Braze definirá então tanto o cabeçalho Content-Type quanto o cabeçalho Accept para o tipo que você especificar.

{% raw %}
```js
{% connected_content http://numbersapi.com/random/trivia :content_type application/json %}
```
{% endraw %}

## POST HTTP

Por padrão, o conteúdo conectado faz uma solicitação HTTP GET para a URL especificada. Para fazer uma solicitação POST, especifique `:method post`.

Você pode opcionalmente fornecer um corpo POST especificando `:body` seguido por uma consulta string do formato `key1=value1&key2=value2&...` ou uma referência aos valores capturados. O tipo de conteúdo padrão é `application/x-www-form-urlencoded`. Se você especificar `:content_type application/json` e fornecer um corpo codificado em formulário, como `key1=value1&key2=value2`, a Braze codificará automaticamente o corpo em JSON antes de enviar.

O Connected Content também não armazena em cache as chamadas POST por padrão. Você pode atualizar esse comportamento adicionando `:cache_max_age` à chamada POST do Connected Content.

#### Tipo de conteúdo padrão

{% raw %}
```js
{% connected_content https://example.com/api/endpoint :method post :body key1=value1&key2=value2 %}
```
#### Tipo de Conteúdo Application/JSON

```js
{% connected_content https://example.com/api/endpoint :method post :body key1=value1&key2=value2 :content_type application/json %}
```
{% endraw %}

### Fornecimento de corpo JSON

Para fornecer seu próprio corpo JSON, escreva-o em linha se não houver espaços. Se seu corpo tiver espaços, você deve usar uma instrução de atribuir ou capturar. Ou seja, qualquer um desses três é aceitável:

{% raw %}
##### Em linha: espaços não permitidos

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

Você pode utilizar o status HTTP de uma chamada de conteúdo conectado salvando-o primeiro como uma variável local e depois usando a chave `__http_status_code__`. Por exemplo:

{% raw %}
```js
{% connected_content https://example.com/api/endpoint :save result %}
{% if result.__http_status_code__ != 200 %}
  {% abort_message('Connected Content returned a non-200 status code') %}
{% endif %}
```
{% endraw %}

{% alert important %}
Esta chave só será adicionada automaticamente ao objeto de conteúdo conectado se o endpoint retornar um objeto JSON válido e uma `2XX` resposta. Se o endpoint retornar um vetor ou outro tipo, essa chave não poderá ser configurada automaticamente na resposta.
{% endalert %}


[16]: [success@braze.com](mailto:success@braze.com)
