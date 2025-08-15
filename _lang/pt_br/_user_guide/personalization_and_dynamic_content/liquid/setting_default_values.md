---
nav_title: Definição de valores padrão
article_title: Definição de valores padrão do Liquid
page_order: 5
description: "Este artigo de referência cobre como definir valores de fallback padrão para qualquer atributo de personalização que você usa em suas mensagens."

---

# Definição de valores padrão

{% raw %}

> Os valores de fallback padrão podem ser definidos para qualquer atributo de personalização que você use em suas mensagens. Este artigo aborda como funcionam os valores padrão, como configurá-los e como usá-los em suas mensagens.

## Como eles funcionam

Os valores padrão podem ser adicionados especificando um [Liquid Filter](http://docs.shopify.com/themes/liquid-documentation/filters) (use `|` para distinguir o filtro em linha, como mostrado) com o nome "default".

```
| default: 'Insert Your Desired Default Here'
```

Se um valor padrão não for fornecido e o campo estiver ausente ou não estiver definido no usuário, o campo ficará em branco na mensagem.

O exemplo a seguir mostra a sintaxe correta para adicionar um valor padrão. Nesse caso, as palavras "Valued User" substituirão o atributo `{{ ${first_name} }}` se o campo `first_name` de um usuário estiver vazio ou indisponível.

```liquid
Hi {{ ${first_name} | default: 'Valued User' }}, thanks for using the App!
```

Para um usuário chamado Janet Doe, a mensagem apareceria como:

```
Hi Janet, thanks for using the App!
```

Ou...

```
Hi Valued User, thanks for using the App!
```
{% endraw %}

{% alert important %}
O valor padrão será exibido para valores vazios, mas não para valores em branco. Um valor vazio não contém nada, enquanto um valor em branco contém caracteres de espaço em branco (como espaços) e nenhum outro caractere. Por exemplo, uma string vazia pode se parecer com `""` e uma string em branco pode se parecer com `" "`.
{% endalert %}

## Definição de valores padrão para diferentes tipos de dados

O exemplo acima mostra como definir um padrão para uma string. Você pode definir valores padrão para qualquer tipo de dados Liquid que tenha o valor de `empty`, `nil` (indefinido) ou `false`, o que inclui strings, booleanos, vetores de objetos e números.

### Caso de uso: Booleanos

Digamos que você tenha um atributo personalizado booleano chamado `premium_user` e queira enviar uma mensagem personalizada com base no status premium do usuário. Alguns usuários não têm um status premium configurado, portanto, você precisará configurar um valor padrão para capturar esses usuários.

1. Você atribuirá uma variável chamada `is_premium_user` ao atributo `premium_user` com um valor padrão de `false`. Isso significa que, se `premium_user` for `nil`, o valor de `is_premium_user` terá como padrão `false`. 

{% raw %}
```liquid
{% assign is_premium_user = {{custom_attribute.${premium_user}}} | default: false %}
```

{: start="2"}
2\. Em seguida, use a lógica condicional para especificar a mensagem a ser enviada se `is_premium_user` for `true`. Em outras palavras, o que enviar se `premium_user` for `true`. Você também atribuirá um valor padrão ao nome do usuário, caso não tenhamos o nome do usuário.

```liquid
{% if is_premium_user %}
Hi {{${first_name} | default: 'premium user'}}, thank you for being a premium user!
```

{: start="3"}
3\. Por fim, especifique a mensagem a ser enviada se `is_premium_user` for `false` (o que significa que `premium_user` é `false` ou `nil`). Em seguida, você fechará a lógica condicional.

```liquid
{% else %}
Hi {{${first_name} | default: 'valued user'}}, consider upgrading to premium for more benefits!
{% endif %}
```
{% endraw %}

{% details Código Liquid completo %}
{% raw %}
```liquid
{% assign is_premium_user = {{custom_attribute.${premium_user}}} | default: false %}
{% if is_premium_user %}
Hi {{${first_name} | default: 'premium user'}}, thank you for being a premium user!
{% else %}
Hi {{${first_name} | default: 'valued user'}}, consider upgrading to premium for more benefits!
{% endif %}
```
{% endraw %}
{% enddetails %}

### Caso de uso: Números

Digamos que você tenha um atributo personalizado numérico chamado `reward_points` e queira enviar uma mensagem com os pontos de recompensas do usuário. Alguns usuários não têm pontos de recompensas configurados, portanto, você precisará configurar um valor padrão para levar em conta esses usuários.

1. Comece a mensagem com o primeiro nome do usuário ou com um valor padrão de `Valued User`, caso não tenha o nome dele.

{% raw %}
```liquid
Hi {{${first_name} | default: 'valued user'}},
```
{% endraw %}

{: start="2"}
2\. Termine a mensagem com quantos pontos de recompensa o usuário tem usando o atributo personalizado chamado `reward_points` e usando o valor padrão de `0`. Todos os usuários cujo `reward_points` tenha um valor `nil` terão pontos de recompensas `0` na mensagem.

{% raw %}
```liquid
Hi {{${first_name} | default: 'valued user'}}, you have {{custom_attribute.${reward_points} | default: 0}} reward points.
```
{% endraw %}

### Caso de uso: Objetos

Digamos que você tenha um objeto de atributo personalizado aninhado chamado `location` que contém as propriedades `city` e `state`. Se alguma dessas propriedades não estiver definida, você deve incentivar o usuário a fornecê-la.

1. Dirija-se ao usuário pelo nome e inclua um valor padrão, caso não tenha o nome dele.

{% raw %}
```liquid
Hi {{${first_name} | default: 'valued user'}},
```
{% endraw %}

{: start="2"}
2\. Escreva uma mensagem dizendo que gostaria de confirmar o local do usuário.

{% raw %}
```liquid
We'd like to confirm the location associated with your account. We use this location to send you promotions and offers for stores nearest you. You can update your location in your profile settings.
```
{% endraw %}

{: start="3"}
3\. Insira o local do usuário na mensagem e atribua valores padrão para quando a propriedade de endereço não estiver definida.

{% raw %}
```liquid
Your location:
City: {{custom_attribute.${address.city} | default: 'Unknown'}}
State: {{custom_attribute.${address.state} | default: 'Unknown'}}
```
{% endraw %}

{% details Código Liquid completo %}
{% raw %}
```liquid
Hi {{${first_name} | default: 'valued user'}}

We'd like to confirm the location associated with your account. We use this location to send you promotions and offers for stores nearest you. You can update your location in your profile settings.

Your location:
City: {{custom_attribute.${address.city} | default: 'Unknown'}}
State: {{custom_attribute.${address.state} | default: 'Unknown'}}
```
{% endraw %}
{% enddetails %}

### Caso de uso: Matrizes

Digamos que você tenha um atributo personalizado de matriz chamado `upcoming_trips` que contém viagens com as propriedades `destination` e `departure_date`. Deseja enviar mensagens personalizadas aos usuários com base no fato de eles terem viagens programadas.

1. Escreva uma lógica condicional para especificar que uma mensagem não deve ser enviada se `upcoming_trips` for `empty`.

{% raw %}
```liquid
{% if {{custom_attribute.${upcoming_trips}}} == empty %}
{% abort_message('No upcoming trips scheduled') %}
```
{% endraw %}

{: start="2"}
2\. Especifique a mensagem a ser enviada se o site `upcoming_trips` tiver conteúdo:<br><br>**2a.** Dirija-se ao usuário e inclua um valor padrão, caso não tenha o nome dele. <br>**2b.** Use uma tag `for` para especificar que você extrairá propriedades (ou informações) para cada viagem contida em `upcoming_trips`. <br>**2c.** Liste as propriedades na mensagem e inclua um valor padrão para o caso de o `departure_date` não estar definido. (Digamos que um `destination` seja necessário para que uma viagem seja criada, portanto, você não precisa definir um valor padrão para isso).<br>**2d.** Feche a tag `for` e, em seguida, feche a lógica condicional.

{% raw %}
```liquid
{% else %}
Hello {{${first_name} | default: 'fellow traveler'}},
  Here are your upcoming trips:
  <ul>
  {% for trip in {{custom_attribute.${upcoming_trips}}} %}
    <li>
      Destination: {{trip.destination}}
      Departure Date: {{trip.departure_date | default: 'Date not set'}}
    </li>
  {% endfor %}
  </ul>
{% endif %}
```
{% endraw %}

{% details Código Liquid completo %}
{% raw %}
```liquid
{% if {{custom_attribute.${upcoming_trips}}} == blank %}
{% abort_message('No upcoming trips scheduled') %}
{% else %}
Hello {{${first_name} | default: 'fellow traveler'}},
  Here are your upcoming trips:
  <ul>
  {% for trip in {{custom_attribute.${upcoming_trips}}} %}
    <li>
      Destination: {{trip.destination}}
      Departure Date: {{trip.departure_date | default: 'Date not set'}}
    </li>
  {% endfor %}
  </ul>
{% endif %}
```
{% endraw %}
{% enddetails %}

[31]:https://docs.shopify.com/themes/liquid/tags/variable-tags
[32]:https://docs.shopify.com/themes/liquid/tags/iteration-tags
[37]:#accounting-for-null-attribute-values
