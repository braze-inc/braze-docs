---
nav_title: Lógica de envio de mensagens condicionais
article_title: Lógica condicional de envio de mensagens Liquid
page_order: 6
description: "Este artigo de referência aborda como as tags podem e devem ser usadas em suas campanhas."

---

# Lógica de envio de mensagens condicionais

>  As tags podem ser usadas para executar instruções condicionais, bem como para casos de uso avançados, como atribuir variáveis ou iterar em um bloco de código. <br><br>Esta página aborda como as tags podem e devem ser usadas, por exemplo, como considerar valores de atributos nulos, nulos e em branco e como fazer referência a atributos personalizados.

## Tags de formatação

{% raw %}
Uma tag deve ser envolvida em `{% %}`.
{% endraw %}

Para facilitar sua vida, o Braze incluiu a formatação de cores que será ativada em verde e roxo se você tiver formatado corretamente a sintaxe do Liquid. A formatação verde pode ajudar a identificar as tags, enquanto a formatação roxa destaca as áreas que contêm personalização.

Se estiver com dificuldades para usar o envio de mensagens condicionais, tente escrever a sintaxe condicional antes de inserir seus atributos personalizados e outros elementos Liquid.

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

## Lógica condicional

 
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

A lógica condicional começa com a tag `if`, que declara a primeira condição a ser verificada. Condições subsequentes usam a tag `elsif` e serão verificadas se as condições anteriores não forem atendidas. Neste exemplo, se o dispositivo de um usuário não estiver configurado para inglês, este código verificará se o dispositivo do usuário está configurado para espanhol, e se isso falhar, verificará se o dispositivo está configurado para. Se o dispositivo do usuário atender a uma dessas condições, o usuário receberá uma mensagem no idioma relevante.

#### `else`

Você tem a opção de incluir uma declaração `{% else %}` em sua lógica condicional. Se nenhuma das condições que você definiu for atendida, a declaração `{% else %}` especifica a mensagem que deve ser enviada. Neste exemplo, definimos o padrão para inglês se o idioma do usuário não for inglês, espanhol ou chinês.

#### `endif`

A tag `{% endif %}` indica que você terminou sua lógica condicional. Você deve incluir a tag `{% endif %}` em qualquer mensagem com lógica condicional. Se você não incluir uma tag `{% endif %}` em sua lógica condicional, receberá um erro, pois o Braze não conseguirá analisar sua mensagem.

### Tutorial: Entregar conteúdo baseado em localização

Quando você terminar este tutorial, poderá usar tags com "if", "elsif" e "else" para entregar conteúdo com base na localização do usuário.

1. Comece com uma tag `if` para estabelecer qual mensagem deve ser enviada quando a cidade do usuário estiver em Nova York. Se a cidade do usuário for Nova York, esta primeira condição é atendida e o usuário receberá uma mensagem especificando sua identidade nova-iorquina.

```liquid
{% if ${city} == "New York" %}
  🎉 Hey there, New Yorker! We're excited to offer you a special deal! 
  Get 20% off your next sandwich at your local Sandwich Emperor. 
  Just show this message at the counter to redeem your offer!
```

{: start="2"}
2\. Em seguida, use a tag `elseif` para estabelecer qual mensagem deve ser enviada se a cidade do usuário estiver em Los Angeles.

```liquid
{% elsif ${city} == "Los Angeles" %}
  🌞 Hello, Los Angeles! Enjoy a sunny day with a delicious sandwich! 
  Present this message at our LA restaurant for a 20% discount on your next order!
```

{: start="3"}
3\. Vamos usar outra tag `elseif` para estabelecer qual mensagem deve ser enviada se a cidade do usuário estiver em Chicago.

```liquid
{% elsif ${city} == "Chicago" %}
  🍕 Chicago, we have a treat for you! 
  Swing by our restaurant and get 20% off your favorite sandwich. 
  Just show this message to our staff!
```

{: start="4"}
4\. Agora, vamos usar a tag `{% else %}` para especificar qual mensagem deve ser enviada se a cidade do usuário não estiver em São Francisco, Nova York ou Chicago.

```liquid
{% else %}
 🥪 Craving a sandwich? Visit us at any of our locations for a delicious meal! 
  Check our website for the nearest restaurant to you!
```

{: start="5"}
5\. Finalmente, usaremos a tag `{% endif %}` para especificar que nossa lógica condicional está concluída.

```liquid
{% endif %}
```

{% endraw %}

{% details Código Liquid completo %}

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



Ao usar a lógica condicional, será necessário conhecer o tipo de dados do atributo personalizado para garantir que esteja usando a sintaxe correta. Na página **Atributos personalizados** no dashboard, procure o tipo de dados associado ao seu atributo personalizado e consulte os seguintes exemplos listados para cada tipo de dados.

![Seleção de um tipo de dados para um atributo personalizado. 

{% alert tip %}
Strings e matrizes exigem apóstrofos retos ao redor delas, enquanto booleanos e inteiros nunca terão apóstrofos.
{% endalert %}

#### Booleano

 Os valores booleanos não têm apóstrofos ao redor deles.

{% raw %}

```liquid
{% if {{custom_attribute.${registration_complete}}} == true %}
```

{% endraw %}

#### Número

 Por exemplo, um usuário pode ter `shoe_size: 10` ou `levels_completed: 287`. Os valores numéricos não têm apóstrofos ao redor deles.

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

 Por exemplo, você pode ter `favorite_color: red` ou `phone_number: 3025981329`. Os valores de string devem ter apóstrofos ao redor.

{% raw %}

```liquid
{% if {{custom_attribute.${favorite_color}}} == 'blue' %}
```

{% endraw %}

Para strings, você pode usar tanto "==" quanto "contains" em seu Liquid.

#### Vetor

 Por exemplo, um usuário pode ter `last_viewed_shows: stranger things, planet earth, westworld`. Os valores da matriz devem ter apóstrofos ao redor.

{% raw %}

```liquid
{% if {{custom_attribute.${last_viewed_shows}}} contains 'homeland' %}
```

{% endraw %}

Para matrizes, você deve usar "contains" e não pode usar "==". 

#### Horário

 

{% raw %}

```liquid
{% assign expire = {{custom_attribute.${subscription_end_date}}} | plus: 0 %} 
```

{% endraw %}


