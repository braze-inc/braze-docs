---
nav_title: Lógica de mensagens condicionais
article_title: Lógica condicional de mensagens líquidas
page_order: 6
description: "Este artigo de referência aborda como as tags podem e devem ser usadas em suas campanhas."

---

# Lógica de mensagens condicionais

> [As tags](https://docs.shopify.com/themes/liquid-documentation/tags) permitem que você inclua lógica de programação em suas campanhas de mensagens. As tags podem ser usadas para executar instruções condicionais, bem como para casos de uso avançados, como atribuir variáveis ou iterar em um bloco de código. <br><br>Esta página aborda como as tags podem e devem ser usadas, por exemplo, como considerar valores de atributos nulos, nulos e em branco e como fazer referência a atributos personalizados.

## Tags de formatação

{% raw %}
Uma tag deve ser envolvida em `{% %}`.
{% endraw %}

Para facilitar um pouco sua vida, o Braze incluiu a formatação de cores que será ativada em verde e roxo se você tiver formatado corretamente a sintaxe do Liquid. A formatação verde pode ajudar a identificar tags, enquanto a formatação roxa destaca as áreas que contêm personalização.

Se estiver com dificuldades para usar mensagens condicionais, tente escrever a sintaxe condicional antes de inserir os atributos personalizados e outros elementos Liquid.

Por exemplo, adicione o seguinte no campo de mensagem primeiro:  
{% raw %}
```liquid
{% if X >0 %}
{% else %}
{% endif %}
```

Certifique-se de que ele esteja destacado em verde e, em seguida, substitua o `X` pelo Conteúdo líquido ou conectado escolhido usando o `+` azul no canto do campo de mensagem e o `0` pelo valor desejado.
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

## Lógica condicional

Você pode incluir muitos tipos de [lógica inteligente nas mensagens](http://docs.shopify.com/themes/liquid-documentation/basics), como uma instrução condicional. O exemplo a seguir usa [condicionais](http://docs.shopify.com/themes/liquid-documentation/tags/control-flow-tags) para internacionalizar uma campanha:
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

### Tags condicionais

#### `if` e `elsif`

A lógica condicional começa com a tag `if`, que indica a primeira condição a ser verificada. As condições subsequentes usam a tag `elsif` e serão verificadas se as condições anteriores não forem atendidas. Neste exemplo, se o dispositivo de um usuário não estiver definido como inglês, esse código verificará se o dispositivo do usuário está definido como espanhol e, se isso falhar, verificará se o dispositivo está definido como. Se o dispositivo do usuário atender a uma dessas condições, o usuário receberá uma mensagem no idioma relevante.

#### `else`

Você tem a opção de incluir uma declaração `{% else %}` em sua lógica condicional. Se nenhuma das condições que você definiu for atendida, a instrução `{% else %}` especificará a mensagem que deve ser enviada. Neste exemplo, o padrão é o inglês se o idioma do usuário não for inglês, espanhol ou chinês.

#### `endif`

A tag `{% endif %}` indica que você concluiu sua lógica condicional. Você deve incluir a tag `{% endif %}` em qualquer mensagem com lógica condicional. Se você não incluir uma tag `{% endif %}` em sua lógica condicional, receberá um erro, pois o Braze não conseguirá analisar sua mensagem.

### Tutorial: Fornecer conteúdo baseado em localização

Ao terminar este tutorial, você poderá usar tags com instruções "if", "elsif" e "else" para fornecer conteúdo com base na localização do usuário.

1. Comece com uma tag `if` para estabelecer qual mensagem deve ser enviada quando a cidade do usuário for Nova York. Se a cidade do usuário for Nova York, essa primeira condição será atendida e o usuário receberá uma mensagem especificando sua identidade nova-iorquina.

```liquid
{% if ${city} == "New York" %}
  🎉 Hey there, New Yorker! We're excited to offer you a special deal! 
  Get 20% off your next sandwich at your local Sandwich Emperor. 
  Just show this message at the counter to redeem your offer!
```

{: start="2"}
2\. Em seguida, use a tag `elseif` para estabelecer qual mensagem deve ser enviada se a cidade do usuário for Los Angeles.

```liquid
{% elsif ${city} == "Los Angeles" %}
  🌞 Hello, Los Angeles! Enjoy a sunny day with a delicious sandwich! 
  Present this message at our LA restaurant for a 20% discount on your next order!
```

{: start="3"}
3\. Vamos usar outra tag `elseif` para estabelecer qual mensagem deve ser enviada se a cidade do usuário for Chicago.

```liquid
{% elsif ${city} == "Chicago" %}
  🍕 Chicago, we have a treat for you! 
  Swing by our restaurant and get 20% off your favorite sandwich. 
  Just show this message to our staff!
```

{: start="4"}
4\. Agora, vamos usar a tag `{% else %}` para especificar qual mensagem deve ser enviada se a cidade do usuário não for São Francisco, Nova York ou Chicago.

```liquid
{% else %}
 🥪 Craving a sandwich? Visit us at any of our locations for a delicious meal! 
  Check our website for the nearest restaurant to you!
```

{: start="5"}
5\. Por fim, usaremos a tag `{% endif %}` para especificar que nossa lógica condicional está concluída.

```liquid
{% endif %}
```

{% endraw %}

{% details Full Liquid code %}

{% raw %}
```liquid
{% if ${city} == "New York City" %}
  🎉 Hey there, New Yorker! We're excited to offer you a special deal! 
  Get 20% off your next sandwich at our New York location. 
  Just show this message at the counter to redeem your offer!
{% elsif ${city} == "Los Angeles" %}
  🌞 Hello, Los Angeles! Enjoy a sunny day with a delicious sandwich! 
  Present this message at our LA restaurant for a 20% discount on your next order!
{% elsif ${city} == "Chicago" %}
  🍕 Chicago, we have a treat for you! 
  Swing by our restaurant and get 20% off your favorite sandwich. 
  Just show this message to our staff!
{% else %}
  🥪 Craving a sandwich? Visit us at any of our locations for a delicious meal! 
  Check our website for the nearest restaurant to you!
{% endif %}
```
{% endraw %}

{% enddetails %}

## Contabilização de valores de atributos nulos, nulos e em branco

A lógica condicional é uma maneira útil de levar em conta os valores de atributos que não estão definidos nos perfis de usuário.

### Valores de atributo nulos e nulos

Um valor nulo ou nil ocorre quando o valor de um atributo personalizado não foi definido. Por exemplo, um usuário que ainda não definiu seu primeiro nome não terá um primeiro nome registrado no Braze.

Em algumas circunstâncias, talvez você queira enviar uma mensagem completamente diferente para os usuários que têm um primeiro nome definido e para os usuários que não têm um primeiro nome definido.

A tag a seguir permite especificar uma mensagem para usuários com um atributo "first name" nulo:

{% raw %}
```liquid
{% if ${first_name} == null %}
  ....
{% endif %}
```
{% endraw %} 

\![Um exemplo de mensagem no painel do Braze, usando um atributo "first name" nulo.]({% image_buster /assets/img/value_null.png %}){: style="max-width:60%;"}

{% raw %}
```liquid
{% if ${first_name} == null %}
We're having a sale! Hurry up and get 10% off all items today only!
{% else %}
Hey {{${first_name} | default: 'there'}}, we're having a sale! Hurry up and get 10% off all items today only!
{% endif %}
```

Observe que um valor de atributo nulo não está estritamente associado a um tipo de valor (por exemplo, uma cadeia de caracteres "nula" é o mesmo que uma matriz "nula"), portanto, no exemplo acima, o valor de atributo nulo está fazendo referência a um primeiro nome não definido, que seria uma cadeia de caracteres.

{% endraw %}

### Valores de atributos em branco

Um valor em branco ocorre quando o atributo em um perfil de usuário não está definido, é definido com uma string de espaço em branco (` `) ou é definido como `false`. Os valores em branco devem ser verificados antes de outras variáveis para evitar um erro de processamento do Liquid.

A tag a seguir permite especificar uma mensagem para usuários que têm um atributo "first name" em branco.

{% raw %}
```liquid
{% if ${first_name} == blank %}
  ....
{% endif %}
```
{% endraw %} 

## Referência a atributos personalizados

Depois de [criar atributos]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#managing-custom-attributes) personalizados, você pode fazer referência a esses atributos personalizados em suas mensagens do Liquid.

Ao usar a lógica condicional, você precisará conhecer o tipo de dados do atributo personalizado para garantir que esteja usando a sintaxe correta. Na página **Atributos personalizados** do painel, procure o tipo de dados associado ao seu atributo personalizado e consulte os seguintes exemplos listados para cada tipo de dados.

\![Selecionando um tipo de dados para um atributo personalizado. O exemplo fornecido mostra um atributo de Favorite_Category com um tipo de dados de string.]({% image_buster /assets/img_archive/custom_attribute_data_type.png %}){: style="max-width:80%;"}

{% alert tip %}
As cadeias de caracteres e as matrizes exigem apóstrofos retos ao redor delas, enquanto os booleanos e os inteiros nunca terão apóstrofos.
{% endalert %}

#### Booleano

[Os booleanos]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#booleans) são valores binários e podem ser definidos como `true` ou `false`, como `registration_complete: true`. Os valores booleanos não têm apóstrofos ao redor deles.

{% raw %}

```liquid
{% if {{custom_attribute.${registration_complete}}} == true %}
```

{% endraw %}

#### Número

[Números]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#numbers) são valores numéricos, que podem ser inteiros ou flutuantes. Por exemplo, um usuário pode ter `shoe_size: 10` ou `levels_completed: 287`. Os valores numéricos não têm apóstrofos ao redor deles.

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

#### Cordas

Uma [cadeia]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#strings) de caracteres é composta de caracteres alfanuméricos e armazena uma parte dos dados sobre o usuário. Por exemplo, você pode ter `favorite_color: red` ou `phone_number: 3025981329`. Os valores de cadeia de caracteres devem ter apóstrofos ao redor.

{% raw %}

```liquid
{% if {{custom_attribute.${favorite_color}}} == 'blue' %}
```

{% endraw %}

Para cadeias de caracteres, você pode usar "==" ou "contains" em seu Liquid.

#### Matriz

Uma [matriz]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#arrays) é uma lista de informações sobre seu usuário. Por exemplo, um usuário pode ter `last_viewed_shows: stranger things, planet earth, westworld`. Os valores da matriz devem ter apóstrofos ao redor.

{% raw %}

```liquid
{% if {{custom_attribute.${last_viewed_shows}}} contains 'homeland' %}
```

{% endraw %}

Para matrizes, você deve usar "contains" e não pode usar "==". 

#### Tempo

Um registro de data e hora de quando um evento ocorreu. Os valores [de tempo]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#time) devem ter um [filtro matemático]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/filters/#math-filters) para serem usados na lógica condicional.

{% raw %}

```liquid
{% assign expire = {{custom_attribute.${subscription_end_date}}} | plus: 0 %} 
```

{% endraw %}


