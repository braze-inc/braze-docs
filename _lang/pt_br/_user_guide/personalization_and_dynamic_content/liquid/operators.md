---
nav_title: Operadores
article_title: Operadores de líquidos
page_order: 2
description: "Esta página de referência indica os operadores que o Liquid suporta, bem como exemplos relevantes."

---

# Operadores

> O Liquid oferece suporte a muitos [operadores](https://docs.shopify.com/themes/liquid/basics/operators) que podem ser usados em suas instruções condicionais. Esta página aborda os operadores compatíveis com o Liquid e fornece casos de uso de como você pode usá-los em suas mensagens.

Esta tabela lista os operadores compatíveis. Observe que os parênteses são caracteres inválidos no Liquid e impedem que suas tags funcionem.

|   Sintaxe| Descrição do operador|
|---------|-----------|
| ==  | iguais        |
| !=  | não é igual a|
|  >  | maior que  |
| <   | menos de     |
| >=| maior ou igual a|
| <= | menor ou igual a |
| ou | condição A ou condição B|
| e | condição A e condição B|
| contém | verifica se uma string ou matriz de string contém uma string|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Tutoriais

Vamos examinar alguns tutoriais para saber como usar esses operadores em suas campanhas de marketing:

### Selecionar mensagem com um atributo personalizado inteiro

Vamos enviar notificações push com descontos promocionais personalizados para usuários que fizeram ou não fizeram compras. A notificação por push usará um atributo personalizado inteiro chamado `total_spend` para verificar o total de gastos de um usuário.

1. Escreva uma instrução condicional usando o operador greater than (`>`) para verificar se o total de gastos de um usuário é maior que `0`, indicando que ele fez uma compra. Em seguida, crie uma mensagem para enviar a esses usuários.

{% raw %}
```liquid
{% if {{custom_attribute.${total_spend}}} >0 %}
Surprise! We added a 15% discount code to your account that automatically applies to your next order.
```
{% endraw %}

{: start="2"}
2\. Adicione a tag {% raw %}`{% else %}`{% endraw %} para capturar usuários cujo total de despesas seja igual a `0` ou não exista. Em seguida, crie uma mensagem para enviar a esses usuários.

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

Um compositor de notificação por push com o código Liquid completo do tutorial.]({% image_buster /assets/img/liquid-if-totalspend.png %}){: width="100%"}

{% details Full Liquid code %}
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

Agora, se o atributo personalizado "Total Spend" de um usuário for maior que `0`, ele receberá a mensagem:

```
Surprise! We added a 15% discount code to your account that automatically applies to your next order.
```
Se o atributo personalizado "Total Spend" de um usuário não existir ou for igual a `0`, ele receberá a seguinte mensagem:

```
Need a sign to update your wardrobe? We added a 15% discount code to your account that will automatically apply to your first order.
```

### Selecionar mensagem com um atributo personalizado de string

Vamos enviar notificações por push aos usuários e personalizar a mensagem com base no jogo jogado mais recentemente por cada usuário. Isso usará um atributo personalizado de string chamado `recent_game` para verificar qual foi o último jogo jogado pelo usuário.

1. Escreva uma instrução condicional usando o operador igual (`==`) para verificar se o jogo mais recente de um usuário é *Awkward Dinner Party*. Em seguida, crie uma mensagem para enviar a esses usuários.

{% raw %}
```liquid
{% if {{custom_attribute.${recent_game}}} == 'Awkward Dinner Party' %}
You are formally invited to our next dinner party. Log on next week for another round of delectable dishes and curious conversations.
```
{% endraw %}

{: start="2"}
2\. Use a tag `elsif` com o operador equals (`==`) para verificar se o jogo mais recente do usuário é *Proxy War 3: War of Thirst*. Em seguida, crie uma mensagem para enviar a esses usuários.

{% raw %}
```liquid
{% elsif {{custom_attribute.${recent_game}}} == 'Proxy War 3: War of Thirst' %}
Your fleet awaits your next orders. Log on when you're ready to rejoin the war for hydration.
```
{% endraw %}

{: start="3"}
3\. Use a tag `elsif` com os operadores does not equal (`!=`) e "and" (`&&`) para verificar se o usuário tem um jogo recente (ou seja, se o valor não está em branco) e se o jogo não é *Awkward Dinner Party* ou *Proxy War 3: War of Thirst*. Em seguida, crie uma mensagem para enviar a esses usuários.

{% raw %}
```liquid
{% elsif {{custom_attribute.${recent_game}}} != blank && 'Awkward Dinner Party' or 'Proxy War 3: War of Thirst' %}
Limited Time Deal! Get 15% off our best-selling classics!
```
{% endraw %}

{: start="4"}
4\. Adicione a tag {% raw %}`{% else %}`{% endraw %} para capturar usuários que não tenham um jogo recente. Em seguida, crie uma mensagem para enviar a esses usuários.

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

{% details Full Liquid code %}
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

Um compositor de notificação por push com o código Liquid completo do tutorial.]({% image_buster /assets/img/liquid-if-elsif-games.png %})

Agora, se um usuário jogou *Awkward Dinner Party* pela última vez, ele receberá esta mensagem:

```
You are formally invited to our next dinner party. Log on next week for another round of delectable dishes and curious conversations.
```

Se o jogo mais recente de um usuário for *Proxy War 3: War of Thirst*, eles receberão esta mensagem:

```
Your fleet awaits your next orders. Log on when you're ready to rejoin the war for hydration.
```

Se um usuário tiver jogado recentemente um jogo que não tenha sido *Awkward Dinner Party* ou *Proxy War 3: War of Thirst*, eles receberão essa mensagem:

```
Limited Time Deal! Get 15% off our best-selling classics!
```

Se um usuário não tiver jogado nenhum jogo ou se esse atributo personalizado não existir em seu perfil, ele receberá esta mensagem:

```
Hey! I've got a deal for you. Buy 2 of our newest releases and get 10% off!
```

### Mensagem de cancelamento com base na localização

Você pode abortar uma mensagem com base em praticamente qualquer coisa. Vamos abortar uma mensagem se um usuário não estiver localizado em uma área especificada, pois ele pode não se qualificar para a promoção, o show ou a entrega.

1. Escreva uma instrução condicional usando o operador igual (`==`) para verificar se o fuso horário do usuário é `America/Los_Angeles` e, em seguida, crie uma mensagem para enviar a esses usuários. 

{% raw %}
```liquid
{% if {{${time_zone}}} == 'America/Los_Angeles' %}
Stream now!
```
{% endraw %}

{: start="2"}
2\. Para evitar o envio de mensagens a usuários fora do fuso horário `America/Los_Angeles`, envolva as tags {% raw %}`{% else %}`{% endraw %} e {% raw %}`{% endif %}`{% endraw %} em uma tag {% raw %}`{% abort_message () %}`{% endraw %}.

{% raw %}
```liquid
{% else %}
{% abort_message () %}
{% endif %}
```
{% endraw %}

{% details Full Liquid code %}
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

Um compositor de notificação por push com o código Liquid completo do tutorial.]({% image_buster /assets/img/abort-if.png %})

Você também pode [abortar mensagens]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content/) com base no Connected Content.


