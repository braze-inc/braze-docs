---
nav_title: Tutoriais
article_title: "Tutoriais: Escrevendo código Liquid"
page_order: 11
description: "Esta página de referência contém tutoriais para iniciantes que o ajudarão a começar a usar o código Liquid."
page_type: tutorial
---

# Tutoriais: Escrevendo código Liquid

> Novo no Liquid? Esses tutoriais o ajudarão a começar a escrever código Liquid para casos de uso fáceis para iniciantes. Cada tutorial abrange uma combinação diferente de objetivos de aprendizado, como lógica condicional e operadores.

Quando terminar de ler estes tutoriais, você será capaz de:

- Escreva código Liquid para casos de uso comuns
- Combine a lógica condicional do Liquid para personalizar mensagens com base nos dados do usuário
- Use variáveis e filtros para escrever equações que usem os valores dos atributos
- Reconhecer comandos básicos no código Liquid e formar um entendimento geral sobre o que o código está fazendo

| Tutorial | Objetivos de aprendizado |
| --- | --- |
| [Personalize mensagens para segmentos de usuários](#segments) | valores padrão, lógica condicional |
| [Lembretes de carrinhos abandonados](#reminders) | operadores, lógica condicional |
| [Contagem regressiva do evento](#countdown) | variáveis, filtros de data |
| [Mensagem mensal de aniversário](#birthday) | variáveis, filtros de data, operadores |
| [Promover um produto favorito](#favorite-product) | variáveis, filtros de data, equações, operadores |
{: .reset-br-td-1 .reset-br-td-2}

## Mensagens personalizadas para segmentos de usuários {#segments}

Vamos personalizar as mensagens para diferentes segmentos de usuários, como clientes VIP e novos assinantes.

1. Abra a mensagem com saudações personalizadas para enviar quando tiver e não tiver o primeiro nome de um usuário. Para fazer isso, crie uma tag Liquid que inclua o atributo `first_name` e um valor padrão a ser usado se `first_name` estiver em branco. Nesse cenário, vamos usar "traveler" como o valor padrão.

{% raw %}
```liquid
Happy summer, {{${first_name} | default: "traveler"}}!
```
{% endraw %}

{: start="2"}
2\. Agora, vamos fornecer a mensagem a ser enviada se o usuário for um cliente VIP. Para isso, precisaremos usar uma tag de lógica condicional: `if`. Essa tag dirá que, se o atributo personalizado `vip_status` for igual a `VIP`, o seguinte Liquid será executado. Nesse caso, uma mensagem específica será enviada.

{% raw %}
```liquid
{% if {{custom_attribute.${vip_status}}} == 'VIP' %}
Thank you for being a VIP customer! Enjoy your exclusive discount code: VIPSUMMR464.
```
{% endraw %}

{: start="3"}
3\. Vamos enviar uma mensagem personalizada para os usuários que são novos assinantes. Usaremos a tag de lógica condicional `elsif` para especificar que, se o endereço `vip_status` do usuário for `new`, a seguinte mensagem será enviada.

{% raw %}
```liquid
{% elsif {{custom_attribute.${vip_status}}} == 'new' %}
Thank you for subscribing! Enjoy your welcome discount code: NEWTRAVEL257.
```
{% endraw %}

{: start="4"}
4\. E quanto aos usuários que não são VIP ou novos? Podemos enviar uma mensagem a todos os outros usuários com a tag `else`, que especifica que a mensagem a seguir deve ser enviada se as condições anteriores não forem atendidas. Em seguida, podemos fechar a lógica condicional com a tag `endif`, pois não há mais status VIP a considerar.

{% raw %}
```liquid
{% else %}
Thanks for traveling with us! Enjoy your unique discount code: SUMMRTRVLS240.
{% endif %}
```
{% endraw %}

{% details Full Liquid code %}
{% raw %}
```liquid
Happy summer, {{${first_name} | default: "traveler"}}!
{% if {{custom_attribute.${vip_status}}} == 'VIP' %}
Thank you for being a VIP customer! Enjoy your exclusive discount code: VIPSUMMR464.
{% elsif {{custom_attribute.${vip_status}}} == 'new' %}
Thank you for subscribing! Enjoy your welcome discount code: NEWTRAVEL257.
{% else %}
Thanks for traveling with us! Enjoy your unique discount code: SUMMRTRVLS240.
{% endif %}
```
{% endraw %}
{% enddetails %}

## Lembretes de carrinhos abandonados {#reminders}

Vamos enviar mensagens personalizadas para lembrar os usuários dos itens deixados no carrinho. Nós os personalizaremos ainda mais para enviar com base no número de itens no carrinho, de modo que, se eles tiverem mais de três itens ou menos, listaremos todos os itens. Se houver mais de três itens, enviaremos uma mensagem mais concisa.

1. Vamos verificar se o carrinho do usuário está vazio, abrindo uma lógica condicional Liquid com o operador `!=`, que significa "não é igual". Nesse caso, definiremos a condição para que o atributo personalizado `cart_items` não seja igual a um valor em branco.

{% raw %}
```liquid
{% if {{custom_attribute.${cart_items}}} != blank %}
```
{% endraw %}

{: start="2"}
2\. Em seguida, precisaremos restringir nosso foco e verificar se o carrinho tem mais de três itens usando o operador \`>', que significa "maior que".

{% raw %}
```liquid
{% if {{custom_attribute.${cart_items}}} | size > 3 %}
```
{% endraw %}

{: start="3"}
3\. Escreva uma mensagem que cumprimente o usuário pelo primeiro nome ou, se ele não estiver disponível, use "there" como o valor padrão. Inclua o que deve ser declarado se houver mais de três itens no carrinho. Como não queremos sobrecarregar o usuário com uma lista completa, vamos listar os três primeiros `cart_items`.

{% raw %}
```liquid
Hi {{${first_name} | default: 'there'}}, don't forget to complete your purchase! Your items {{custom_attribute.${cart_items[0]}}}, {{custom_attribute.${cart_items[1]}}}, {{custom_attribute.${cart_items[2]}}}, and others are waiting for you.
```
{% endraw %}

{: start="4"}
4\. Use a tag `else` para especificar o que deve acontecer se as condições anteriores não forem atendidas (em outras palavras, se `cart_items` estiver em branco ou tiver menos de três) e, em seguida, forneça a mensagem a ser enviada. Como três itens não ocupam muito espaço, podemos listar todos eles. Usaremos o operador Liquid `join` e `,` para especificar que os itens devem ser listados com uma vírgula separando-os. Feche a lógica com `endif`.

{% raw %}
```liquid
{% else %}
Hi {{${first_name} | default: 'there'}}, don't forget to complete your purchase! Your items: {{{custom_attribute.${cart_items}}} | join: ', '}  are waiting for you. 
{% endif %}
```
{% endraw %}

{: start="5"}
5\. Use `else` e, em seguida, `abort_message` para informar ao código do Liquid para não enviar uma mensagem se o carrinho não atender a nenhuma das condições anteriores. Em outras palavras, se o carrinho estiver vazio. Feche a lógica com `endif`.

{% raw %}
```liquid
{% else %}
{% abort_message('No items in cart') %}
{% endif %}
```
{% endraw %}

{% details Full Liquid code %}
{% raw %}
```liquid
{% if {{custom_attribute.${cart_items}}} != blank %}
{% if {{custom_attribute.${cart_items}}} | size > 3 %}
Hi {{${first_name} | default: 'there'}}, don't forget to complete your purchase! Your items {{custom_attribute.${cart_items[0]}}}, {{custom_attribute.${cart_items[1]}}}, {{custom_attribute.${cart_items[2]}}}, and others are waiting for you.
{% else %}
Hi {{${first_name} | default: 'there'}}, don't forget to complete your purchase! Your items: {{{custom_attribute.${cart_items}}} | join: ', '}  are waiting for you.
{% endif %}
{% else %}
{% abort_message('No items in cart') %}
{% endif %}
```
{% endraw %}
{% enddetails %}

## Contagem regressiva do evento {#countdown}

Vamos enviar aos usuários uma mensagem que informa quantos dias faltam para uma promoção de aniversário. Para isso, usaremos variáveis para podermos criar equações que manipulem os valores dos atributos.

1. Primeiro, vamos atribuir a variável `sale_date` ao atributo personalizado `anniversary_date` e aplicar o filtro `date: "s"`. Isso converte o `anniversary_date` em um formato de carimbo de data/hora expresso em segundos e, em seguida, atribui esse valor a `sale_date`.

{% raw %}
```liquid
{% assign sale_date = {{custom_attribute.${anniversary_date}}} | date: "%s" %}
```
{% endraw %}

{: start="2"}
2\. Também precisamos atribuir uma variável para capturar o registro de data e hora de hoje. Vamos atribuir a variável `today` a `now` (a data e a hora atuais) e, em seguida, aplicar o filtro `date: "%s"`.

{% raw %}
```liquid
{% assign today =  'now' | date: "%s"  %}
```
{% endraw %}

{: start="3"}
3\. Agora vamos calcular quantos segundos faltam entre agora (`today`) e a Promoção de Aniversário (`sale_date`). Para fazer isso, atribua a variável `difference` para igualar o valor de `sale_date` menos `today`.

{% raw %}
```liquid
{% assign difference =  event_date | minus: today %}
```
{% endraw %}

{: start="4"}
4\. Agora precisamos converter `difference` em um valor que possa ser referenciado em uma mensagem, pois não é ideal informar ao usuário quantos segundos faltam para uma venda. Vamos atribuir `difference_days` a `event_date` e dividi-lo por `86400` para obter o número de dias.

{% raw %}
```liquid
{% assign difference_days = difference | divided_by: 86400 %}
```
{% endraw %}

{: start="5"}
5\. Por fim, vamos criar a mensagem a ser enviada.

{% raw %}
```liquid
Get ready! Our Anniversary Sale is in {{ difference_days }} days!
```
{% endraw %}

{% details Full Liquid code %}
{% raw %}
```liquid
{% assign sale_date = {{custom_attribute.${anniversary_date}}} | date: "%s" %}
{% assign today =  'now' | date: "%s"  %}
{% assign difference =  event_date | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}
Get ready! Our Anniversary Sale is in {{ difference_days }} days!
```
{% endraw %}
{% enddetails %}

## Mensagem mensal de aniversário {#birthday}

Vamos enviar uma promoção especial a todos os usuários que fazem aniversário no mês de hoje. Os usuários que não fizerem aniversário neste mês não receberão nenhuma mensagem.

1. Primeiro, vamos puxar o mês de hoje. Atribuiremos a variável `this_month` a `now` (a data e a hora atuais) e, em seguida, usaremos o filtro `date: "%B"` para especificar que a variável deve ser igual ao mês.

{% raw %}
```liquid
{% assign this_month = 'now' | date: "%B" %}
```
{% endraw %}

{: start="2"}
2\. Agora, vamos extrair o mês de nascimento do site do usuário `date_of_birth`. Atribuiremos a variável `birth_month` a `date_of_birth` e, em seguida, usaremos o filtro `date: "%B"`.

{% raw %}
```liquid
{% assign birth_month = {{${date_of_birth}}} | date: "%B" %}
```
{% endraw %}

{: start="3"}
3\. Agora que temos duas variáveis que têm um mês como valor, podemos compará-las com a lógica condicional. Vamos definir a condição para que `date_of_birth` seja igual ao `birth_month` do usuário.

{% raw %}
```liquid
{% if {{this_month}} == {{birth_month}} %}
```
{% endraw %}

{: start="4"}
4\. Vamos criar a mensagem a ser enviada se esse mês também for o mês de nascimento do usuário.

{% raw %}
```liquid
We heard {{this_month}} is a special month! Enjoy a 50% discount on your purchase with code BIRTHDAY50 until the end of {{this_month}}.
```
{% endraw %}

{: start="5"}
5\. Use a tag `else` para especificar o que acontecerá se a condição não for atendida (porque esse mês não é o mês de nascimento do usuário).

{% raw %}
```liquid
{% else %} 
```
{% endraw %}

{: start="6"}
6\. Não queremos enviar uma mensagem se o mês de nascimento do usuário não for este mês, portanto, usaremos `abort_message` para cancelar a mensagem e, em seguida, fecharemos a lógica condicional com `endif`.

{% raw %}
```liquid
{% abort_message("Not their birthday month") %}
{% endif %}
```
{% endraw %}

{% details Full Liquid code %}
{% raw %}
```liquid
{% assign this_month = 'now' | date: "%B" %}
{% assign birth_month = {{${date_of_birth}}} | date: "%B" %}
{% if {{this_month}} == {{birth_month}} %}
We heard {{this_month}} is a special month! Enjoy a 50% discount on your purchase with code BIRTHDAY50 until the end of {{this_month}}.
{% else %} 
{% abort_message("Not their birthday month") %}
{% endif %}
```
{% endraw %}
{% enddetails %}

## Promoção do produto favorito {#favorite-product}

Vamos promover o produto favorito de um usuário se a data da última compra tiver sido há mais de seis meses.

1. Primeiro, usaremos a lógica condicional para verificar se temos o produto favorito do usuário e a data da última compra.

{% raw %}
```liquid
{% if {{custom_attribute.${favorite_product}}} == blank or {{custom_attribute.${last_purchase_date}}} == blank %}
```
{% endraw %}

{: start="2"}
2\. Em seguida, declararemos que, se não tivermos o produto favorito do usuário ou a data da última compra, não enviaremos uma mensagem.

{% raw %}
```liquid
{% abort_message("No favorite product or last purchase date") %}
```
{% endraw %}

{: start="3"}
3\. Usaremos `else` para especificar o que deve acontecer se a condição acima não for atendida (porque _temos_ o produto favorito do usuário e a data da última compra).

{% raw %}
```liquid
{% else %}
```
{% endraw %}

{: start="4"}
4\. Se tivermos a data da compra, precisaremos atribuí-la a uma variável para que possamos compará-la com a data de hoje. Primeiro, vamos criar um valor para a data de hoje atribuindo a variável `today` a `now` (a data e a hora atuais) e usando o filtro `date: "%s"` para converter o valor em um formato de carimbo de data/hora expresso em segundos. Adicionaremos o filtro `plus: 0` para adicionar um "0" ao registro de data e hora. Isso não altera o valor do carimbo de data/hora, mas é útil para usar o carimbo de data/hora em equações futuras.


{% raw %}
```liquid
{% assign today = 'now' | date: "%s" | plus: 0 %}
```
{% endraw %}

{: start="5"}
5\. Agora, vamos capturar a data da última compra em segundos atribuindo a variável `last_purchase_date` ao atributo personalizado `last_purchase_date` e usando o filtro `date: "s"`. Adicionaremos novamente o filtro `plus: 0`.

{% raw %}
```liquid
{% assign last_purchase_date = {{custom_attribute.${last_purchase_date}}} | date: "%s" | plus: 0 %}
```
{% endraw %}

{: start="6"}
6\. Como a data da última compra e a data de hoje estão em segundos, precisaremos calcular quantos segundos existem em seis meses. Vamos criar uma equação (aproximadamente 6 meses * 30,44 dias * 24 horas * 60 minutos * 60 segundos) e atribuí-la à variável `six_months`. Usaremos o endereço `times` para especificar a multiplicação de unidades de tempo.

{% raw %}
```liquid
{% assign six_months = 6 | times: 30.44 | times: 24 | times: 60 | times: 60 %}
```
{% endraw %}

{: start="7"}
7\. Agora que todos os nossos valores de tempo estão em segundos, podemos usar seus valores em equações. Vamos atribuir uma variável chamada `today_minus_last_purchase_date` que pega o valor de hoje e subtrai dele o `last_purchase_date`. Isso nos dá quantos segundos se passaram desde a última compra.

{% raw %}
```liquid
{% assign today_minus_last_purchase_date = {{today | minus: last_purchase_date}} %}
```
{% endraw %}

{: start="8"}
8\. Agora vamos comparar diretamente nossos valores de tempo na lógica condicional. Vamos definir a condição como `today_minus_last_purchase_date` sendo maior ou igual (`>=`) a seis meses. Em outras palavras, a data da última compra foi há pelo menos seis meses.

{% raw %}
```liquid
{% if today_minus_last_purchase_date >= six_months %}
```
{% endraw %}

{: start="9"}
9\. Vamos criar a mensagem a ser enviada se a última compra tiver sido feita há pelo menos seis meses.

{% raw %}
```liquid
We noticed it’s been a while since you last purchased {{custom_attribute.${favorite_product}}}. Have you checked out our latest offerings?
```
{% endraw %}

{: start="10"}
10\. Usaremos a tag `else` para especificar o que deve acontecer se a condição não for atendida (porque a compra não foi feita há pelo menos seis meses).

{% raw %}
```liquid
{% else %}
```
{% endraw %}

{: start="11"}
11\. Incluiremos um `abort_message` para cancelar a mensagem.

{% raw %}
```liquid
{% abort_message("No favorite product or last purchase date") %}
```
{% endraw %}

{: start="12"}
12\. Para finalizar, encerraremos o Liquid com duas tags `endif`. O primeiro `endif` encerra a verificação condicional do produto favorito ou da data da última compra, e o segundo `endif` encerra a verificação condicional da data da última compra, que é de pelo menos seis meses atrás.

{% raw %}
```liquid
{% endif %}
{% endif %}
```
{% endraw %}

{% details Full Liquid code %}
{% raw %}
```liquid
{% if {{custom_attribute.${favorite_product}}} == blank or {{custom_attribute.${last_purchase_date}}} == blank %}
{% abort_message("No favorite product or last purchase date") %}
{% else %}
{% assign today = 'now' | date: "%s" | plus: 0 %}
{% assign last_purchase_date = {{custom_attribute.${last_purchase_date}}} | date: "%s" | plus: 0 %}
{% assign six_months = 6 | times: 30.44 | times: 24 | times: 60 | times: 60 %}
{% assign today_minus_last_purchase_date = {{today | minus: last_purchase_date}} %}
{% if today_minus_last_purchase_date >= six_months %}
We noticed it’s been a while since you last purchased {{custom_attribute.${favorite_product}}}. Have you checked out our latest offerings?
{% else %}
{% abort_message("Last purchase was less than six months ago") %}
{% endif %}
{% endif %}
```
{% endraw %}
{% enddetails %}
