---
nav_title: Lógica de envio de mensagens condicionais
article_title: Lógica condicional de envio de mensagens Liquid
page_order: 6
description: "Este artigo de referência aborda como as tags podem e devem ser usadas em suas campanhas."

---

# Lógica de envio de mensagens condicionais

> [As tags][7] permitem incluir lógica de programação em suas campanhas de mensagens. As tags podem ser usadas para executar instruções condicionais, bem como para casos de uso avançados, como atribuir variáveis ou iterar em um bloco de código. <br><br>Esta página aborda como as tags podem e devem ser usadas, por exemplo, como considerar valores de atributos nulos, nulos e em branco e como fazer referência a atributos personalizados.

## Tags de formatação

{% raw %}
Uma tag deve ser envolvida em `{% %}`.
{% endraw %}

{% alert tip %}
Para facilitar sua vida, o Braze incluiu a formatação de cores que será ativada em verde e roxo se você tiver formatado corretamente a sintaxe do Liquid. A formatação verde pode ajudar a identificar as tags, enquanto a formatação roxa destaca as áreas que contêm personalização.
<br><br>
Se estiver com dificuldades para usar o envio de mensagens condicionais, tente escrever a sintaxe condicional antes de inserir seus atributos personalizados e outros elementos Liquid.
<br><br>
Por exemplo, adicione o seguinte no campo de mensagem primeiro:  
{% raw %}
```liquid
{% if X >0 %}
{% else %}
{% endif %}
```

Certifique-se de que ele esteja destacado em verde e, em seguida, substitua o `X` pelo Liquid ou Connected Content escolhido usando o `+` azul no canto do campo de mensagem e o `0` pelo valor desejado.
<br><br>
Em seguida, adicione suas variações de mensagem conforme necessário entre as condicionais `else`:
```liquid
{% if {{custom_attribute.${total_spend}}} >0 %}
Thanks for purchasing! Here's another 10% off!
{% else %}
Buy now! Would 5% off convince you?
{% endif %}
```
{% endraw %}
{% endalert %}

## Lógica condicional

Você pode incluir muitos tipos de [lógica inteligente nas mensagens][1], como uma instrução condicional. Veja o exemplo a seguir, que usa [conditionais][8] para internacionalizar uma campanha:
{% raw %}

```liquid
{% if ${language} == 'en' %}
This is a message in English from Braze!
{% elsif ${language} == 'es' %}
Este es un mensaje en español de Braze !
{% elsif ${language} == 'zh' %}
这是一条来自Braze的中文消息。
{% else %}
This is a message from Braze! This is going to go to anyone who did not match the other specified languages!
{% endif %}
```

### Exemplo de etapa

Neste exemplo, usamos tags com instruções "if", "elsif" e "else" para fornecer conteúdo internacionalizado.

```liquid
{% if ${language} == 'en' %}
This is a message in English from Braze!
```
Se o idioma do usuário for o inglês, a primeira condição será atendida e o usuário receberá uma mensagem em inglês.

```liquid
{% elsif ${language} == 'es' %}
Este es un mensaje en español de Braze !
{% elsif ${language} == 'zh' %}
这是一条来自Braze的中文消息。
```

Você pode especificar quantas instruções condicionais desejar. As condições subsequentes serão verificadas se as condições anteriores não forem atendidas. Neste exemplo, se o dispositivo de um usuário não estiver definido como inglês, esse código verificará se o dispositivo do usuário está definido como espanhol ou chinês. Se o dispositivo do usuário atender a uma dessas condições, o usuário receberá uma mensagem no idioma relevante.

```liquid
{% else %}
This is a message from Braze! This is going to go to anyone who didn't match the other specified languages!
```

Você tem a opção de incluir uma declaração `{% else %}` em sua lógica condicional. Se nenhuma das condições que você definiu for atendida, a instrução `{% else %}` especificará a mensagem que deve ser enviada. Nesse caso, o padrão é o inglês se o idioma do usuário não for inglês, espanhol ou chinês.

```liquid
{% endif %}
```

A tag `{% endif %}` indica que você terminou sua lógica condicional. Você deve incluir a tag `{% endif %}` em qualquer mensagem com lógica condicional. Se você não incluir uma tag `{% endif %}` em sua lógica condicional, receberá um erro, pois o Braze não conseguirá analisar sua mensagem.

{% endraw %}

## Contabilização de valores de atribuição nulos, nulos e em branco

A lógica condicional é uma maneira útil de levar em conta os valores de atribuição que não estão definidos nos perfis de usuário.

### Valores de atribuição nulos e nulos

Um valor nulo ou nil ocorre quando o valor de um atributo personalizado não foi definido. Por exemplo, um usuário que ainda não definiu seu primeiro nome não terá um primeiro nome registrado no Braze.

Em algumas circunstâncias, talvez você queira enviar uma mensagem completamente diferente para usuários que têm um nome definido e para usuários que não têm um nome definido.

A tag a seguir permite especificar uma mensagem para usuários com a atribuição "first name" nula:

{% raw %}
```liquid
{% if ${first_name} == null %}
  ....
{% endif %}
```
{% endraw %} 

![Uma mensagem de exemplo no dashboard Braze, usando um atributo 'nome' nulo.][36]{: style="max-width:60%;"}

{% raw %}
```liquid
{% if ${first_name} == null %}
We're having a sale! Hurry up and get 10% off all items today only!
{% else %}
Hey {{${first_name} | default: 'there'}}, we're having a sale! Hurry up and get 10% off all items today only!
{% endif %}
```

Note que um valor de atribuição nulo não está estritamente associado a um tipo de valor (por exemplo, uma string "nula" é o mesmo que uma matriz "nula"), portanto, no exemplo acima, o valor de atribuição nulo está fazendo referência a um nome não definido, que seria uma string.

{% endraw %}

### Valores de atribuição em branco

Um valor em branco ocorre quando a atribuição em um perfil de usuário não está definida, é definida com uma string de espaço em branco (` `) ou é definida como `false`. Os valores em branco devem ser verificados antes de outras variáveis para evitar um erro de processamento do Liquid.

A tag a seguir permite especificar uma mensagem para usuários que tenham a atribuição "first name" em branco.

{% raw %}
```liquid
{% if ${first_name} == blank %}
  ....
{% endif %}
```
{% endraw %} 

## Referência a atributos personalizados

Depois de criar atributos personalizados][2], você poderá fazer referência a esses atributos personalizados em seu envio de mensagens Liquid.

Ao usar a lógica condicional, será necessário conhecer o tipo de dados do atributo personalizado para garantir que esteja usando a sintaxe correta. Na página **Atributos personalizados** no dashboard, procure o tipo de dados associado ao seu atributo personalizado e consulte os seguintes exemplos listados para cada tipo de dados.

![Seleção de um tipo de dados para um atributo personalizado. O exemplo fornecido mostra uma atribuição de Favorite_Category com um tipo de dados de string.][20]{: style="max-width:80%;"}

{% alert tip %}
Strings e matrizes exigem apóstrofos retos ao redor delas, enquanto booleanos e inteiros nunca terão apóstrofos.
{% endalert %}

#### Booleano

[Os booleanos][9] são valores binários e podem ser definidos como `true` ou `false`, como `registration_complete: true`. Os valores booleanos não têm apóstrofos ao redor deles.

{% raw %}

```liquid
{% if {{custom_attribute.${registration_complete}}} == true %}
```

{% endraw %}

#### Número

[Números][10] são valores numéricos, que podem ser inteiros ou flutuantes. Por exemplo, um usuário pode ter `shoe_size: 10` ou `levels_completed: 287`. Os valores numéricos não têm apóstrofos ao redor deles.

{% raw %}

```liquid
{% if {{custom_attribute.${shoe_size}}} == 10 %}
```

{% endraw %}

Você também pode usar outros [operadores básicos](https://shopify.dev/docs/themes/liquid/reference/basics/operators), como menor que (<) ou maior que (>) para números inteiros:

{% raw %}

```liquid
{% if {{custom_attribute.${flyer_miles}}} >= 500 %}
```

{% endraw %}

#### String

Uma [string][11] é composta de caracteres alfanuméricos e armazena dados de usuários. Por exemplo, você pode ter `favorite_color: red` ou `phone_number: 3025981329`. Os valores de string devem ter apóstrofos ao redor.

{% raw %}

```liquid
{% if {{custom_attribute.${favorite_color}}} == 'blue' %}
```

{% endraw %}

Para strings, você pode usar tanto "==" quanto "contains" em seu Liquid.

#### Vetor

Uma [matriz][12] é uma lista de informações sobre o seu usuário. Por exemplo, um usuário pode ter `last_viewed_shows: stranger things, planet earth, westworld`. Os valores da matriz devem ter apóstrofos ao redor.

{% raw %}

```liquid
{% if {{custom_attribute.${last_viewed_shows}}} contains 'homeland' %}
```

{% endraw %}

Para matrizes, você deve usar "contains" e não pode usar "==". 

#### Horário

Um registro de data e hora de quando um evento ocorreu. [Time][13] valores devem ter um [math filter][5] sobre eles para serem usados na lógica condicional.

{% raw %}

```liquid
{% assign expire = {{custom_attribute.${subscription_end_date}}} | plus: 0 %} 
```

{% endraw %}


[36]:{% image_buster /assets/img/value_null.png %}
Daqui a [1]: http://docs.shopify.com/themes/liquid-documentation/basics
[2]: {{site.baseurl}}/user_guide/data_e_analytics/custom_data/custom_attributes/#managing-custom-attributes
[5]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/filters/#math-filters
Daqui a [7]: https://docs.shopify.com/themes/liquid-documentation/tags
[8]: http://docs.shopify.com/themes/liquid-documentation/tags/control-flow-tags "Tags de fluxo de controle"
[9]: {{site.baseurl}}/user_guide/data_e_analytics/custom_data/custom_attributes/#booleans
[10]: {{site.baseurl}}/user_guide/data_e_analytics/custom_data/custom_attributes/#numbers
[11]: {{site.baseurl}}/user_guide/data_e_analytics/custom_data/custom_attributes/#strings
[12]: {{site.baseurl}}/user_guide/data_e_analytics/custom_data/custom_attributes/#arrays
[13]: {{site.baseurl}}/user_guide/data_e_analytics/custom_data/custom_attributes/#time
[20]: {% image_buster /assets/img_archive/custom_attribute_data_type.png %}
