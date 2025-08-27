---
nav_title: Operadores
article_title: Operadores Liquid
page_order: 2
description: "Esta página de referência nota os operadores que o Liquid suporta, bem como exemplos relevantes."

---

# Operadores

> O Liquid suporta muitos [operadores](https://docs.shopify.com/themes/liquid/basics/operators) que podem ser usados em suas declarações condicionais. Esta página cobre os operadores que Liquid suporta e fornece casos de uso de como você pode usá-los em suas mensagens.

Esta tabela lista os operadores que são suportados. Nota que parênteses são caracteres inválidos em Liquid e impedem que suas tags funcionem.

|   Sintaxe| Descrição do operador|
|---------|-----------|
| ==  | é igual a        |
| !=  | não é igual a|
|  >  | é maior que  |
| <   | menos de     |
| >=| maior ou igual a|
| <= | menor ou igual a |
| ou | condição A ou condição B|
| e | condição A e condição B|
| contém | verifica se uma string ou matriz de string contém uma string|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Tutoriais

Vamos passar por alguns tutoriais para aprender como usar esses operadores em suas campanhas de marketing:

### Escolha a mensagem com um atributo personalizado inteiro

Vamos enviar notificações por push com descontos promocionais personalizados para usuários que fizeram ou não fizeram compras. A notificação por push usará um atributo personalizado inteiro chamado `total_spend` para verificar o total gasto por um usuário.

1. Escreva uma declaração condicional usando o operador maior que (`>`) para verificar se o total gasto por um usuário é maior que `0`, indicando que ele fez uma compra. Em seguida, crie uma mensagem para enviar a esses usuários.

{% raw %}
```liquid
{% if {{custom_attribute.${total_spend}}} >0 %}
Surprise! We added a 15% discount code to your account that automatically applies to your next order.
```
{% endraw %}

{: start="2"}
2\. Adicione a tag {% raw %}`{% else %}`{% endraw %} para capturar usuários cujo total gasto é igual a `0` ou não existe. Em seguida, crie uma mensagem para enviar a esses usuários.

{% raw %}
```liquid
{% else %}
Need a sign to update your wardrobe? We added a 15% discount code to your account that will automatically apply to your first order.
```
{% endraw %}

{: start="3"}
3\. Feche a lógica condicional com a tag {% raw %}`{% endif %}`{% endraw %}.

{% raw %}
```liquid
{% endif %}
```
{% endraw %}

![Um criador de notificações por push com o código Liquid completo do tutorial.]({% image_buster /assets/img/liquid-if-totalspend.png %}){: width="100%"}

{% details Código Liquid completo %}
{% raw %}
```liquid
{% if {{custom_attribute.${total_spend}}} >0 %}
Surprise! We added a 15% discount code to your account that automatically applies to your next order.
{% else %}
Need a sign to update your wardrobe? We added a 15% discount code to your account that will automatically apply to your first order.
{% endif %}
```
{% endraw %}
{% enddetails %}

Agora, se o atributo personalizado "Total Gasto" de um usuário for maior que `0`, eles receberão a mensagem:

```
Surprise! We added a 15% discount code to your account that automatically applies to your next order.
```
Se o atributo personalizado "Total Gasto" de um usuário não existir ou for igual a `0`, eles receberão a seguinte mensagem:

```
Need a sign to update your wardrobe? We added a 15% discount code to your account that will automatically apply to your first order.
```

### Escolha a mensagem com um atributo personalizado de string

Vamos enviar notificações por push para usuários e personalizar a mensagem com base no jogo mais recentemente jogado por cada usuário. Isso usará um atributo personalizado string chamado `recent_game` para verificar qual jogo um usuário jogou por último.

1. Escreva uma declaração condicional usando o operador igual a (`==`) para verificar se o jogo mais recente de um usuário é *Awkward Dinner Party*. Em seguida, crie uma mensagem para enviar a esses usuários.

{% raw %}
```liquid
{% if {{custom_attribute.${recent_game}}} == 'Awkward Dinner Party' %}
You are formally invited to our next dinner party. Log on next week for another round of delectable dishes and curious conversations.
```
{% endraw %}

{: start="2"}
2\. Use a tag `elsif` com o operador igual a (`==`) para verificar se o jogo mais recente de um usuário é *Proxy War 3: War of Thirst*. Em seguida, crie uma mensagem para enviar a esses usuários.

{% raw %}
```liquid
{% elsif {{custom_attribute.${recent_game}}} == 'Proxy War 3: War of Thirst' %}
Your fleet awaits your next orders. Log on when you're ready to rejoin the war for hydration.
```
{% endraw %}

{: start="3"}
3\. Use a tag `elsif` com os operadores diferente de (`!=`) e "e" (`&&`) para verificar se o usuário tem um jogo recente (significa que o valor não está em branco) e que o jogo não é *Awkward Dinner Party* ou *Proxy War 3: War of Thirst*. Em seguida, crie uma mensagem para enviar a esses usuários.

{% raw %}
```liquid
{% elsif {{custom_attribute.${recent_game}}} != blank && 'Awkward Dinner Party' or 'Proxy War 3: War of Thirst' %}
Limited Time Deal! Get 15% off our best-selling classics!
```
{% endraw %}

{: start="4"}
4\. Adicione a tag {% raw %}`{% else %}`{% endraw %} para capturar usuários que não têm um jogo recente. Em seguida, crie uma mensagem para enviar a esses usuários.

{% raw %}
```liquid
{% else %}
Hey! I've got a deal for you. Buy 2 of our newest releases and get 10% off!
```
{% endraw %}

{: start="5"}
5\. Feche a lógica condicional com a tag {% raw %}`{% endif %}`{% endraw %}.

{% raw %}
```liquid
{% endif %}
```
{% endraw %}

{% details Código Liquid completo %}
{% raw %}
```liquid
{% if {{custom_attribute.${recent_game}}} == 'Awkward Dinner Party' %}
You are formally invited to our next dinner party. Log on next week for another round of delectable dishes and curious conversations.
{% elsif {{custom_attribute.${recent_game}}} == 'Proxy War 3: War of Thirst' %}
Your fleet awaits your next orders. Log on when you're ready to rejoin the war for hydration.
{% elsif {{custom_attribute.${recent_game}}} != blank && 'Awkward Dinner Party' or 'Proxy War 3: War of Thirst' %}
Limited Time Deal! Get 15% off our best-selling classics!
{% else %}
Hey! I've got a deal for you. Buy 2 of our newest releases and get 10% off!
{% endif %}
```
{% endraw %}
{% enddetails %}

![Um criador de notificações por push com o código Liquid completo do tutorial.]({% image_buster /assets/img/liquid-if-elsif-games.png %})

Agora, se um usuário jogou por último *Awkward Dinner Party*, ele receberá esta mensagem:

```
You are formally invited to our next dinner party. Log on next week for another round of delectable dishes and curious conversations.
```

Se o jogo mais recente de um usuário for *Proxy War 3: War of Thirst*, eles receberão esta mensagem:

```
Your fleet awaits your next orders. Log on when you're ready to rejoin the war for hydration.
```

Se um usuário jogou recentemente um jogo que não foi *Awkward Dinner Party* ou *Proxy War 3: War of Thirst*, ele receberá esta mensagem:

```
Limited Time Deal! Get 15% off our best-selling classics!
```

Se um usuário não jogou nenhum jogo ou se esse atributo personalizado não existe em seu perfil, eles receberão esta mensagem:

```
Hey! I've got a deal for you. Buy 2 of our newest releases and get 10% off!
```

### Mensagem de cancelamento com base no local

Você pode abortar uma mensagem com base em praticamente qualquer coisa. Vamos abortar uma mensagem se um usuário não estiver baseado em uma área especificada, pois eles podem não se qualificar para a promoção, show ou entrega.

1. Escreva uma declaração condicional usando o operador de igualdade (`==`) para verificar se o fuso horário do usuário é `America/Los_Angeles`, então crie uma mensagem para enviar a esses usuários. 

{% raw %}
```liquid
{% if {{${time_zone}}} == 'America/Los_Angeles' %}
Stream now!
```
{% endraw %}

{: start="2"}
2\. Para evitar enviar mensagens a usuários fora do fuso horário `America/Los_Angeles`, envolva as tags {% raw %}`{% else %}`{% endraw %} e {% raw %}`{% endif %}`{% endraw %} em torno de uma tag {% raw %}`{% abort_message () %}`{% endraw %}.

{% raw %}
```liquid
{% else %}
{% abort_message () %}
{% endif %}
```
{% endraw %}

{% details Código Liquid completo %}
{% raw %}
```liquid
{% if {{${time_zone}}} =='America/Los_Angeles' %}
Stream now!
{% else %}
{% abort_message () %}
{% endif %}
```
{% endraw %}
{% enddetails %}

![Um criador de notificações por push com o código Liquid completo do tutorial.]({% image_buster /assets/img/abort-if.png %})

Você também pode [abortar mensagens]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content/) com base no Connected Content.


