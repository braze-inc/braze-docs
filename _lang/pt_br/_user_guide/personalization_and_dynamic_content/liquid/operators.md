---
nav_title: Operadores
article_title: Operadores Liquid
page_order: 2
description: "Esta página de referência nota os operadores que o Liquid suporta, bem como exemplos relevantes."

---

# Operadores

> O Liquid oferece suporte a muitos [operadores][25] que podem ser usados em suas instruções condicionais. Esta página cobre os operadores que Liquid suporta e fornece casos de uso de como você pode usá-los em suas mensagens.

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

## Casos de uso

Aqui estão alguns casos de uso de como esses operadores podem ser úteis para suas campanhas de marketing:

### Escolha a mensagem com um atributo personalizado inteiro

{% raw %}
```liquid
{% if {{custom_attribute.${total_spend}}} >0 %}
Thanks for purchasing! Here's another 10% off!
{% else %}
Buy now! Would 5% off convince you?
{% endif %}
```
{% endraw %}

![][13]{: width="100%"}

Neste caso de uso, se o atributo personalizado "Total Spend" de um cliente for maior que `0`, eles receberão a mensagem:

```
Thanks for purchasing! Here's another 10% off!
```
Se o atributo personalizado "Total Spend" de um cliente não existir ou for igual a `0`, ele receberá a seguinte mensagem:

```
Buy now! Would 5% off convince you?
```

### Escolha a mensagem com um atributo personalizado de string

{% raw %}

```liquid
{% if {{custom_attribute.${Game}}} == 'Game1' %}
You played our Game! We're so happy!
{% elsif{{custom_attribute.${Game}}} == 'Game2' %}
You played our other Game! Woop!{% else %}
Hey! Get in here and play this Game!
{% endif %}
```
{% endraw %}

![][14]

Neste caso de uso, se você tiver jogado um determinado jogo, receberá a seguinte mensagem:

```
You played our Game! We're so happy!
```

Se você jogou outro jogo especificado:

```
You played our other Game! Woop!
```

Se não tiver jogado nenhum jogo ou se esse atributo personalizado não existir em seu perfil, você receberá a seguinte mensagem:

```
Hey! Get in here and play this Game!
```

### Mensagem de cancelamento com base no local

Você pode abortar uma mensagem com base em praticamente qualquer coisa. O exemplo a seguir mostra como é possível abortar uma mensagem se um usuário não estiver localizado em uma área especificada, pois ele pode não se qualificar para a promoção, o show ou a entrega.

{% raw %}
```liquid
{% if {{${time_zone.$}}} =='America/Los_Angeles' %}
Stream now!
{% else %}
{% abort_message () %}
{% endif %}
```
{% endraw %}

![][26]

Você também pode [abortar mensagens][1] com base no Connected Content.


[1]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content/
[13]: {% image_buster /assets/img/liquid-if-totalspend.png %}
[14]: {% image_buster /assets/img/liquid-if-elsif-games.png %}
[25]: https://docs.shopify.com/themes/liquid/basics/operators
[26]: {% image_buster /assets/img/abort-if.png %}
