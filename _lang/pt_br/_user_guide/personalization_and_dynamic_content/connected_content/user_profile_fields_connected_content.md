---
nav_title: Puxando Dados do Perfil do Usuário
article_title: Puxando Dados de Perfil do Usuário em Chamadas de Conteúdo Conectado
page_order: 3
description: "Este artigo aborda como puxar perfis de usuários em suas chamadas de Conteúdo Conectado e melhores práticas envolvendo modelagem Liquid."
toc_headers: h2
---

# Puxando dados do perfil do usuário

> Esta página aborda como extrair perfis de usuário para suas chamadas de Connected Content e as práticas recomendadas envolvendo modelos Liquid. 

## Pré-requisitos

Se uma resposta do Connected Content contiver campos de perfil de usuário (dentro de uma tag de personalização do Liquid), esses valores deverão ser definidos anteriormente na mensagem com o Liquid, antes da chamada do Connected Content, para que o passback do Liquid seja renderizado corretamente. Da mesma forma, a bandeira `:rerender` deve ser incluída na solicitação. Observe que a bandeira `:rerender` é apenas um nível profundo, o que significa que não se aplicará a nenhuma tag de Conteúdo Conectado aninhada.

## Modelos Liquid nas chamadas do Connected Content

Para personalização, Braze puxa campos de perfil de usuário antes de passar esse campo para Liquid—então, se a resposta do Conteúdo Conectado tiver campos de perfil de usuário, ele deve ser definido previamente. 

Por exemplo, se esta fosse a chamada para a API Connected Content:
{% raw %}
```liquid
Hi ${first_name},
{% connected_content https://examplewebsite.com :rerender %}
```
{% endraw %}

A resposta do Connected Content é {% raw %}`Your language is ${language}`{% endraw %}. O conteúdo exibido neste exemplo é `Hi Jon, your language is`. 

A linguagem em si não será modelada. Isso ocorre porque a Braze precisa saber quais campos recuperar do usuário antes de fazermos a chamada de Conteúdo Conectado.

Para renderizar o Liquid passback corretamente, você deve incluir a tag {% raw %}`${language}`{% endraw %} em qualquer lugar da solicitação, conforme mostrado no seguinte trecho de código. O pré-processador Liquid saberá pegar o atributo "language" do usuário para tê-lo pronto para a modelagem da resposta.

{%raw%}
```liquid
"Hi ${first_name}, {% connected_content https://examplewebsite.com?language=${language} :rerender %}
```
{% endraw %}

{% alert important %}
Lembre-se de que a opção de bandeira `:rerender` só tem um nível de profundidade. Se a própria resposta de Connected Content tiver mais tags de Connected Content ou quaisquer tags de catálogo, o Braze não renderizará novamente essas tags adicionais.
{% endalert %}

## Melhores práticas

### Use `json_escape` com tags Liquid que possam quebrar o formato JSON

Ao usar `:rerender`, adicione o filtro `json_escape` a qualquer tag Liquid que possa quebrar o formato JSON. Se suas tags Liquid contiverem caracteres que quebram o formato JSON, toda a resposta do Connected Content será interpretada como texto e será modelada na mensagem, e nenhuma das variáveis será salva.

Por exemplo, se a propriedade de evento `message` no exemplo abaixo contiver caracteres que possam quebrar o formato JSON, adicione o filtro `json_escape` como neste exemplo:

{% raw %}
```liquid
[{
"message":"{{event_properties.${message} | json_escape}}"
}]
```
{% endraw %}