---
nav_title: Líquido
article_title: Líquido
page_order: 0
layout: dev_guide
alias: /liquid/
search_rank: 3
guide_top_header: "Personalização usando Liquid Tags"
guide_top_text: "O Braze pode substituir automaticamente os valores de um determinado usuário em suas mensagens. Coloque sua expressão dentro de dois conjuntos de chaves para notificar o Braze de que você usará um valor interpolado. Dentro desses colchetes, todos os valores de usuário que você deseja substituir devem ser cercados por um conjunto adicional de colchetes com um cifrão na frente deles.<br><br>Para saber mais sobre o Liquid, confira nosso guia <b><a href='https://learning.braze.com/path/dynamic-personalization-with-liquid'>Personalização dinâmica com Liquid</a></b> Braze Learning!"
description: "Essa página de destino abrange todos os aspectos do Liquid, como tags de personalização compatíveis, filtros, definição de valores padrão e muito mais."

guide_featured_title: "Artigos de seção"
guide_featured_list:
- name: Usando líquido
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/using_liquid/
  image: /assets/img/braze_icons/beaker-02.svg
- name: Tags de personalização compatíveis
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/
  image: /assets/img/braze_icons/tag-01.svg
- name: Operadores
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/operators/
  image: /assets/img/braze_icons/code-02.svg
- name: Filtros
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/filters/
  image: /assets/img/braze_icons/flag-02.svg
- name: Filtros avançados
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/
  image: /assets/img/braze_icons/settings-01.svg
- name: Definição de valores padrão
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/setting_default_values/
  image: /assets/img/braze_icons/table.svg
- name: Lógica de mensagens condicionais
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/
  image: /assets/img/braze_icons/columns-01.svg
- name: Interrupção de mensagens
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/
  image: /assets/img/braze_icons/refresh-ccw-01.svg
- name: Casos de uso de líquidos
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/liquid_use_cases/
  image: /assets/img/braze_icons/list.svg
- name: Tutoriais
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/tutorials/
  image: /assets/img/braze_icons/book-open-01.svg
- name: Perguntas frequentes
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/faq/
  image: /assets/img/braze_icons/annotation-question.svg
  
---

## Sobre o Liquid

> Liquid é uma linguagem de modelo de código aberto desenvolvida pela Shopify e escrita em Ruby. Na Braze, o Liquid é usado para modelar dados do perfil de um usuário em mensagens. 

Por exemplo, você pode recuperar um atributo personalizado de um perfil de usuário que seja um tipo de dados inteiro e arredondar esse valor para o número inteiro mais próximo. Para obter mais informações sobre a sintaxe e o uso do Liquid, consulte [**Tags de personalização compatíveis**]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/).

A linguagem de modelagem Liquid suporta o uso de objetos, tags e filtros.

- [**Objetos**]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) permitem que você insira atributos personalizados em suas mensagens.
- [**Tags**]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/) permitem que você insira dados em mensagens e use a lógica condicional para enviar mensagens se determinadas condições forem atendidas. Por exemplo, você pode usar tags para incluir lógica inteligente, como instruções "if", em suas campanhas.
- [**Filtros**]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/filters/) permitem que você reformate atributos personalizados e conteúdo dinâmico. Por exemplo, você pode usar o [filtro`date` ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/filters/#date-filter) para converter um carimbo de data/hora, como *2016-09-07 08:43:50 UTC*, em uma data, como *7 de setembro de 2016*.

{% alert warning %}
Atualmente, o Braze não é compatível com 100% do Liquid da Shopify, apenas com algumas partes que tentamos delinear em nossa documentação. É altamente recomendável testar todas as mensagens usando o Liquid antes de enviá-las para reduzir o risco de erros ou de usar um Liquid sem suporte.
{% endalert %}

### Suporte ao Liquid 5

O Braze é compatível com o Liquid até o **Liquid 5 da Shopify**, inclusive. A implementação do Liquid oferece suporte a tipos de tags de personalização de sintaxe e controle de espaço em branco. Para obter mais informações sobre tags específicas, consulte [tags de sintaxe]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#syntax-tags).

Os novos filtros de matriz e matemáticos a seguir estão disponíveis para uso em seu Liquid à medida que você cria suas mensagens.
- `at_least`
- `at_most`
- `compact`
- `concat`
- `sort_natural`
- `where`

Consulte [Filtros]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/filters/) para obter definições.

### Atualizações líquidas

#### Etiquetas coloridas

Cada elemento Liquid corresponde a uma cor, permitindo que você diferencie seu Liquid rapidamente no editor Liquid.

\![]({% image_buster /assets/img/liquid_color_code.png %})

#### Líquido preditivo

Você também pode aproveitar o Predictive Liquid para atributos personalizados, nomes de atributos e muito mais ao criar suas mensagens personalizadas.

\![]({% image_buster /assets/img/liquid_auto_complete.gif %}){: style="max-width:70%;"}

## Termos a serem conhecidos

Esses termos são reinterpretados da [**documentação da Shopify**](https://shopify.github.io/liquid/basics/introduction/) com base em nosso nível de suporte.

{% raw %}

| Prazo | Definição | Exemplo |  
|---|---|---|
| Líquido | Uma linguagem de modelo comumente usada e voltada para o cliente, criada pela Shopify e escrita em Ruby, que é usada para carregar e extrair conteúdo dinâmico. | `{{${first_name}}}` inserirá o primeiro nome de um usuário em uma mensagem. |
| Objeto | Uma denotação de uma variável e o local do nome da variável pretendida que informa ao Liquid onde exibir o conteúdo na mensagem. | `{{${city}}}` inserirá a cidade de um usuário em uma mensagem. |
| Tag de lógica condicional | Usado para criar lógica e controlar o fluxo do conteúdo da mensagem. No Braze, as tags de lógica condicional são usadas para criar exceções e variações nas mensagens com base em determinados critérios predefinidos. | ```{% if ${language} == 'en' %}``` acionará sua mensagem de uma forma designada caso um usuário tenha designado "inglês" como seu idioma. |
| Filtros | Usado para alterar, restringir ou reformatar a saída do objeto Liquid. Ele é frequentemente usado para criar operações matemáticas. | ```{{"Big Sale" | upcase}}``` fará com que as palavras "Big Sale" apareçam como "BIG SALE" na mensagem. |
| Operadores | Usado em mensagens para criar dependências ou critérios que podem afetar a mensagem que o usuário recebe. | Se um usuário atender aos critérios definidos em uma mensagem marcada com `{% custom_attribute.${Total_Revenue} > 0%}`, ele receberá a mensagem. Caso contrário, eles receberão outra mensagem designada (ou não), dependendo do que você definir. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endraw %}

<br>

