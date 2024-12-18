---
nav_title: Usando Liquid
article_title: Visão geral e caso de uso do Liquid
page_order: 0
description: "Este artigo de referência fornece uma visão geral dos casos de uso comuns do Liquid e como incluir as tags do Liquid em seu envio de mensagens."
search_rank: 2
---

# [![Curso do Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/path/dynamic-personalization-with-liquid){: style="float:right;width:120px;border:0;" class="noimgborder"}Usando Liquid

> Este artigo mostrará como usar uma variedade de atribuições do usuário para inserir dinamicamente informações pessoais no envio de mensagens.

O Liquid é uma linguagem de modelo de código aberto desenvolvida pela Shopify e escrita em Ruby. Você pode usá-lo no Braze para extrair dados do perfil do usuário para suas mensagens e personalizar esses dados. Por exemplo, é possível usar Liquid tags para criar mensagens condicionais, como o envio de ofertas diferentes com base na data de aniversário da inscrição de um usuário. Além disso, os filtros podem manipular dados, como formatar a data de registro de um usuário a partir de um carimbo de data/hora em um formato mais legível, como "15 de janeiro de 2022". Para obter mais detalhes sobre a sintaxe do Liquid e seus recursos, consulte [Tags de personalização compatíveis][1].

## Como funciona?

As Liquid tags funcionam como espaços reservados em suas mensagens que podem extrair informações consentidas da conta do usuário e ativar a personalização e as práticas de envio de mensagens relevantes.

No bloco a seguir, é possível ver o uso duplo de uma tag Liquid para chamar o primeiro nome do usuário, bem como uma tag padrão no caso de um usuário não ter seu primeiro nome registrado.

{% raw %}
```liquid
Hi {{ ${first_name} | default: 'Valued User' }}, thanks for using the App!
```
{% endraw %}

Para um usuário chamado Janet Doe, a mensagem apareceria como:

```
Hi Janet, thanks for using the App!
```

Ou...

```
Hi Valued User, thanks for using the App!
```

## Valores suportados para substituição

Os valores a seguir podem ser substituídos em uma mensagem, dependendo de sua disponibilidade:

- [Informações básicas do usuário][1] (por exemplo, `first_name`, `last_name`, `email_address`)
- [Atributos personalizados][2]
    - [Atributos personalizados aninhados][3]
- [Propriedades de eventos personalizados][11]
- [Informações do dispositivo usado mais recentemente][39]
- [Informações do dispositivo de direcionamento][40]

Você também pode extrair conteúdo diretamente de um servidor da Web por meio do Braze [Connected Content][9].

{% alert important %}
Atualmente, o Braze suporta o Liquid até o Liquid 5 da Shopify, inclusive.
{% endalert %}

## Usando Liquid

Usando [as Liquid tags][1], você pode elevar a qualidade de suas mensagens, enriquecendo-as com um toque pessoal. 

### Sintaxe Liquid

O Liquid segue uma estrutura específica, ou sintaxe, que você precisará ter em mente ao criar uma personalização dinâmica. Aqui estão algumas regras básicas que você deve ter em mente:

1. **Use aspas retas no Braze:** Há uma diferença entre aspas curvas ('**')** e aspas retas ('**')**. Use aspas retas ('**')** em seu Liquid na Braze. Você pode ver aspas curvas ao copiar e colar de determinados editores de texto, o que pode causar problemas em seu Liquid. Se estiver inserindo cotações diretamente no dashboard do Braze, não haverá problema!
2. **As chaves vêm em pares:** Abra e feche chaves, **{ }**. Não deixe de usar chaves!
3. **Se as declarações vierem em pares:** Para cada `if`, você precisa de um `endif` para indicar que a declaração `if` terminou.

#### Atributos padrão e atributos personalizados

{% raw %}

Se você incluir o seguinte texto em sua mensagem: `{{${first_name}}}`, o nome do usuário (extraído do perfil do usuário) será substituído quando a mensagem for enviada. É possível usar o mesmo formato com outras atribuições padrão do usuário.

Se quiser usar o valor de um atributo personalizado, você deverá adicionar o namespace "custom_attribute" à variável. Por exemplo, para usar um atributo personalizado chamado "zip code" (CEP), você deve incluir `{{custom_attribute.${zip code}}}` em sua mensagem.

### Inserção de tags

Você pode inserir tags digitando duas chaves abertas `{{` em qualquer mensagem, o que disparará um recurso de preenchimento automático que continuará a ser atualizado à medida que você digitar. Você pode até mesmo selecionar uma variável nas opções que aparecem à medida que você digita.

Se estiver usando uma tag personalizada, poderá copiar e colar a tag em qualquer mensagem que desejar.

{% endraw %}

{% alert note %}

Se usar o Liquid em seus envios de e-mail, certifique-se de usá-lo:

1. Insira-o usando o editor de HTML em vez do editor clássico. O editor clássico pode analisar o Liquid como texto simples. Por exemplo, o Liquid analisaria como {% raw %}`Hi {{ ${first_name} }}, thanks for using our service!`{% endraw %} em vez de modelar o nome do usuário.
2. Coloque o código Liquid somente na tag `<body>`. Colocá-lo fora dessa tag pode causar uma renderização inconsistente na entrega.

{% endalert %}

{% raw %}

### Inserção de variáveis pré-formatadas

Você pode inserir variáveis pré-formatadas com padrões por meio do modal **Add Personalization (Adicionar personalização** ), localizado no canto superior direito de qualquer campo de texto modelado.

![O modal Add Personalization que aparece após a seleção de inserir personalização. O modal tem campos para o tipo de personalização, atribuição, valor padrão opcional e exibe uma prévia da sintaxe do Liquid][44]{: style="max-width:70%;"}

O modal inserirá o Liquid com o valor padrão especificado no ponto em que o cursor estava. O ponto de inserção também é especificado pela caixa de prévia, que tem o texto antes e depois. Se um bloco de texto for destacado, o texto destacado será substituído.

![Um GIF do modal Add Personalization que mostra o usuário inserindo "fellow traveler" como um valor padrão e o modal substituindo o texto destacado "name" no criador pelo snippet do Liquid.][45]

{% endraw %}

### Atribuindo variáveis

{% raw %}
Algumas operações no Liquid exigem que você armazene o valor que deseja manipular como uma variável. Isso geralmente ocorre se sua instrução Liquid incluir várias atribuições, propriedades de eventos ou filtros.

Por exemplo, digamos que você queira adicionar dois inteiros de dados personalizados. 

#### Exemplo de Liquid incorreto

Você não pode usar:

```liquid
{{custom_attribute.${one}}} | plus: {{custom_attribute.${two}}}
```

Esse Liquid não funciona porque não é possível fazer referência a várias atribuições em uma linha; é necessário atribuir uma variável a pelo menos um desses valores antes que as funções matemáticas sejam executadas. A adição de dois atributos personalizados exigiria duas linhas de LINE: uma para atribuir o atributo personalizado a uma variável e outra para realizar a adição.

#### Exemplo correto de Liquid

Você pode usar:

```liquid
{% assign value_one = {{custom_attribute.${one}}} %}
{% assign result = value_one | plus: {{custom_attribute.${two}}} %}
```

#### Tutorial: Uso de variáveis para calcular um saldo

Vamos calcular o saldo atual de um usuário adicionando o saldo do cartão-presente e o saldo das recompensas:

Primeiro, use a tag `assign` para substituir o atributo personalizado de `current_rewards_balance` pelo termo "balance". Isso significa que agora você tem uma variável chamada `balance`, que pode ser manipulada.

```liquid
{% assign balance = {{custom_attribute.${current_rewards_balance}}} %}
```

Em seguida, usaremos o filtro `plus` para combinar o saldo do cartão-presente de cada usuário com seu saldo de recompensas, indicado por `{{balance}}`.

```liquid
{% assign balance = {{custom_attribute.${current_rewards_balance}}} %}
You have ${{custom_attribute.${giftcard_balance} | plus: {{balance}}}} to spend!
```
{% endraw %}

{% alert tip %}
Está atribuindo as mesmas variáveis em todas as mensagens? Em vez de escrever a tag `assign` várias vezes, você pode salvar essa tag como um bloco de conteúdo e colocá-la na parte superior da mensagem.

1. [Criar um bloco de conteúdo]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/#create-a-content-block).
2. Dê um nome ao seu bloco de conteúdo (sem espaços ou caracteres especiais).
3. Selecione **Edit (Editar** ) na parte inferior da página.
4. Digite suas tags `assign`.

Desde que o bloco de conteúdo esteja na parte superior da mensagem, toda vez que a variável for inserida na mensagem como um objeto, ela fará referência ao atributo personalizado escolhido!
{% endalert %}

[1]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/
[2]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/
[3]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/#liquid-templating
[9]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/
[11]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/
[39]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#most-recently-used-device-information
[40]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#targeted-device-information
[44]: {% image_buster /assets/img_archive/insert_liquid_var_arrow.png %}
[45]: {% image_buster /assets/img_archive/insert_var_shot.gif %}
