---
nav_title: Operadores
article_title: Operadores Liquid
page_order: 2
description: "Esta página de referência nota os operadores que o Liquid suporta, bem como exemplos relevantes."

---

# Operadores

> O Liquid suporta muitos [operadores](https://docs.shopify.com/themes/liquid/basics/operators) que podem ser usados em suas declarações condicionais. Esta página cobre os operadores que Liquid suporta e fornece casos de uso de como você pode usá-los em suas mensagens.

Esta tabela lista os operadores que são suportados. Note que parênteses são caracteres inválidos no Liquid e impedem que suas tags funcionem.

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

{% alert note %}
Operadores podem ser usados em declarações condicionais (`if`, `elsif`, `unless`), mas não em declarações `assign`, loops `for`, declarações `case`/`when` ou colchetes de acesso a arrays. Para uma explicação completa, veja [Onde usar operadores e filtros]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#where-to-use-operators-and-filters).
{% endalert %}

### Agrupando condições sem parênteses

O Liquid não suporta parênteses para agrupar expressões. Para avaliar lógica booleana complexa como `(a and b) or c`, use declarações `if` aninhadas ou variáveis intermediárias.

Por exemplo, para verificar se um valor satisfaz uma condição composta, atribua uma variável intermediária:

{% raw %}
```liquid
{% assign qualifies = false %}
{% if points > 100 %}
{% assign qualifies = true %}
{% elsif points == 100 and member_level == 'gold' %}
{% assign qualifies = true %}
{% endif %}

{% if qualifies %}
You qualify for a reward!
{% endif %}
```
{% endraw %}

## Tutoriais

Vamos passar por alguns tutoriais para aprender como usar esses operadores em suas campanhas de marketing:

### Escolha uma mensagem com um atributo personalizado inteiro

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

Agora, se o atributo personalizado "Total Gasto" de um usuário for maior que `0`, ele receberá a mensagem:

```
Surprise! We added a 15% discount code to your account that automatically applies to your next order.
```
Se o atributo personalizado "Total Gasto" de um usuário não existir ou for igual a `0`, eles receberão a seguinte mensagem:

```
Need a sign to update your wardrobe? We added a 15% discount code to your account that will automatically apply to your first order.
```

### Escolha uma mensagem com um atributo personalizado string

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
3\. Use a tag `elsif` com o operador "não é igual" (`!=`) e "e" (`and`) para verificar se o usuário tem um jogo recente (significando que o valor não está em branco), e que o jogo não é *Jantar Desconfortável* ou *Guerra Proxy 3: War of Thirst*. Em seguida, crie uma mensagem para enviar a esses usuários.

{% raw %}
```liquid
{% elsif {{custom_attribute.${recent_game}}} != blank and {{custom_attribute.${recent_game}}} != 'Awkward Dinner Party' and {{custom_attribute.${recent_game}}} != 'Proxy War 3: War of Thirst' %}
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

{% details Full Liquid code %}
{% raw %}
```liquid
{% if {{custom_attribute.${recent_game}}} == 'Awkward Dinner Party' %}
You are formally invited to our next dinner party. Log on next week for another round of delectable dishes and curious conversations.
{% elsif {{custom_attribute.${recent_game}}} == 'Proxy War 3: War of Thirst' %}
Your fleet awaits your next orders. Log on when you're ready to rejoin the war for hydration.
{% elsif {{custom_attribute.${recent_game}}} != blank and {{custom_attribute.${recent_game}}} != 'Awkward Dinner Party' and {{custom_attribute.${recent_game}}} != 'Proxy War 3: War of Thirst' %}
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

![Um criador de notificações por push com o código Liquid completo do tutorial.]({% image_buster /assets/img/abort-if.png %})

Você também pode [abortar mensagens]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content/) com base no Connected Content.

## Solução de problemas

### A prévia pode coercionar incorretamente os tipos de propriedade 

Ao visualizar uma mensagem no dashboard, a maioria das variáveis (como atributos personalizados) é coercionada para o tipo correto. No entanto, algumas variáveis não têm um tipo definido que a prévia pode consultar:

- `api_trigger_properties`
- `canvas_entry_properties`
- `context`

Para essas propriedades, a prévia tenta inferir o tipo a partir do valor. Isso significa que um valor que você pretende que seja um **string** pode ser interpretado erroneamente como um **número**. Por exemplo, se o valor de uma propriedade for uma string `"3"`, a prévia pode coercioná-la para o inteiro `3`, o que pode causar comportamentos inesperados em operações de string como `contains` ou `split`.

Se você ver resultados inesperados na prévia ao usar esses tipos de propriedade, tenha em mente que a inferência de tipo da prévia pode não corresponder ao que acontece no momento do envio. No momento do envio, os tipos de dados reais do evento que acionou ou da chamada da API são preservados.

Para forçar um tipo específico na prévia, você pode converter explicitamente o valor:

{% raw %}
```liquid
{% comment %} Force a value to be treated as a number {% endcomment %}
{% assign orders = {{canvas_entry_properties.${number_of_orders}}} | plus: 0 %}

{% comment %} Force a value to be treated as a string {% endcomment %}
{% assign code = {{api_trigger_properties.${promo_code}}} | append: "" %}
```
{% endraw %}