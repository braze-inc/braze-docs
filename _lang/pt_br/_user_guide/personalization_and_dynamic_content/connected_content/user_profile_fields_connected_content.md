---
nav_title: Extração de dados do perfil do usuário
article_title: Extração de dados de perfil de usuário em chamadas de conteúdo conectado
page_order: 3
description: "Este artigo aborda como extrair perfis de usuário para suas chamadas de Connected Content e as práticas recomendadas que envolvem o modelo Liquid."
toc_headers: h2
---

# Extração de dados do perfil do usuário

> Esta página aborda como extrair perfis de usuário para suas chamadas de Connected Content e as práticas recomendadas que envolvem o modelo Liquid. 

## Pré-requisitos

Se uma resposta do Connected Content contiver campos de perfil de usuário (em uma tag de personalização do Liquid), esses valores deverão ser definidos anteriormente na mensagem com o Liquid, antes da chamada do Connected Content, para que o passback do Liquid seja processado corretamente. Da mesma forma, o sinalizador `:rerender` deve ser incluído na solicitação. Observe que o sinalizador `:rerender` tem apenas um nível de profundidade, o que significa que ele não se aplicará a nenhuma tag Connected Content aninhada.

## Modelo líquido nas chamadas do Connected Content

Para a personalização, o Braze extrai os campos do perfil do usuário antes de passar esse campo para o Liquid - portanto, se a resposta do Connected Content tiver campos de perfil do usuário, ele deverá ser definido previamente. 

Por exemplo, se essa fosse a chamada do Connected Content:
{% raw %}
```liquid
Hi ${first_name},
{% connected_content https://examplewebsite.com :rerender %}
```
{% endraw %}

A resposta do Connected Content é {% raw %}`Your language is ${language}`{% endraw %}. O conteúdo exibido neste exemplo é `Hi Jon, your language is`. 

A linguagem em si não será modelada. Isso ocorre porque o Braze precisa saber quais campos devem ser recuperados do usuário antes de fazermos a chamada do Connected Content.

Para renderizar o Liquid passback corretamente, você deve incluir a tag {% raw %}`${language}`{% endraw %} em qualquer lugar da solicitação, conforme mostrado no trecho de código a seguir. O pré-processador do Liquid saberá pegar o atributo "language" do usuário para deixá-lo pronto para modelar a resposta.

{%raw%}
```liquid
"Hi ${first_name}, {% connected_content https://examplewebsite.com?language=${language} :rerender %}
```
{% endraw %}

{% alert important %}
Lembre-se de que a opção de bandeira `:rerender` tem apenas um nível de profundidade. Se a própria resposta de Connected Content tiver mais tags de Connected Content ou quaisquer tags de catálogo, o Braze não renderizará novamente essas tags adicionais.
{% endalert %}

## Práticas recomendadas

### Use `json_escape` com tags Liquid que possam quebrar o formato JSON

Ao usar `:rerender`, adicione o filtro `json_escape` a qualquer tag Liquid que possa quebrar o formato JSON. Se as suas tags Liquid contiverem caracteres que quebram o formato JSON, toda a resposta do Connected Content será interpretada como texto e será modelada na mensagem, e nenhuma das variáveis será salva.

Por exemplo, se a propriedade de evento `message` no exemplo abaixo contiver caracteres que possam quebrar o formato JSON, adicione o filtro `json_escape` como neste exemplo:

{% raw %}
```liquid
[{
"message":"{{event_properties.${message} | json_escape}}"
}]
```
{% endraw %}