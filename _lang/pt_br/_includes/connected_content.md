{% if include.section == "default behavior" %}

Por padrão, o conteúdo conectado definirá um `Content-Type` cabeçalho em uma solicitação HTTP GET que ele faz para `application/json` com `Accept: */*`. Se precisar de outro tipo de conteúdo, especifique-o explicitamente adicionando `:content_type your/content-type` à tag. A Braze definirá então tanto o cabeçalho Content-Type quanto o cabeçalho Accept para o tipo que você especificar.

{% raw %}
```js
{% connected_content http://numbersapi.com/random/trivia :content_type application/json %}
```
{% endraw %}

{% endif %}

{% if include.section == "http post" %}

Por padrão, o conteúdo conectado faz uma solicitação HTTP GET para a URL especificada. Para fazer uma solicitação POST, especifique `:method post`.

Você pode opcionalmente fornecer um corpo POST especificando `:body` seguido por uma consulta string do formato `key1=value1&key2=value2&...` ou uma referência aos valores capturados. O tipo de conteúdo padrão é `application/x-www-form-urlencoded`. Se você especificar `:content_type application/json` e fornecer um corpo codificado em formulário, como `key1=value1&key2=value2`, a Braze codificará automaticamente o corpo em JSON antes de enviar.

O Connected Content também não armazena em cache as chamadas POST por padrão. Você pode atualizar esse comportamento adicionando `:cache_max_age` à chamada POST do Connected Content.

{% tabs %}
{% tab Tipo de conteúdo padrão %}

{% raw %}
```js
{% connected_content https://example.com/api/endpoint :method post :body key1=value1&key2=value2 %}
```
{% endraw %}

{% endtab %}
{% tab Application/JSON Content-Type %}

{% raw %}
```js
{% connected_content https://example.com/api/endpoint :method post :body key1=value1&key2=value2 :content_type application/json %}
```
{% endraw %}

{% endtab %}
{% endtabs %}


{% endif %}