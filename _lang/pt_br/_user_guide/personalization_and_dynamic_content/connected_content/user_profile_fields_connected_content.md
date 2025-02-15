---
nav_title: Puxando Dados do Perfil do Usuário
article_title: Puxando Dados de Perfil do Usuário em Chamadas de Conteúdo Conectado
page_order: 5
description: "Este artigo aborda como puxar perfis de usuários em suas chamadas de Conteúdo Conectado e melhores práticas envolvendo modelagem Liquid."

---

# Puxando dados do perfil do usuário

> Se uma resposta de Conteúdo Conectado contiver campos de perfil do usuário (dentro de uma tag de personalização Liquid), esses valores devem ser definidos anteriormente na mensagem via Liquid, antes da chamada de Conteúdo Conectado para renderizar corretamente o retorno do Liquid. 

Da mesma forma, a bandeira `:rerender` deve ser incluída na solicitação. Observe que a bandeira `:rerender` é apenas um nível profundo, o que significa que não se aplicará a nenhuma tag de Conteúdo Conectado aninhada.

Para personalização, Braze puxa campos de perfil de usuário antes de passar esse campo para Liquid—então, se a resposta do Conteúdo Conectado tiver campos de perfil de usuário, ele deve ser definido previamente. 

Por exemplo, se esta fosse a chamada para a API Connected Content:
{% raw %}
```liquid
Hi ${first_name},
{% connected_content https://examplewebsite.com :rerender %}
```
{% endraw %}
E a resposta fosse{% raw %}`Your language is ${language}`{% endraw %}, o conteúdo exibido neste cenário seria `Hi Jon, your language is`. A própria linguagem não será modelada. Isso ocorre porque a Braze precisa saber quais campos recuperar do usuário antes de fazermos a chamada de Conteúdo Conectado.

Para renderizar o passback Liquid corretamente, você deve colocar a tag {% raw %}`${language}`{%endraw%} em qualquer lugar da solicitação, conforme mostrado no trecho de código a seguir. O pré-processador Liquid saberá pegar o atributo "language" do usuário para tê-lo pronto para a modelagem da resposta.
{%raw%}
```liquid
"Hi ${first_name}, {% connected_content https://examplewebsite.com?language=${language} :rerender %}
```
{% endraw %}
{% alert important %}
Lembre-se de que a opção de bandeira `:rerender` só tem um nível de profundidade. Se a resposta do Conteúdo Conectado em si tiver mais tags de Conteúdo Conectado, a Braze não renderizará novamente essas tags adicionais.
{% endalert %}
