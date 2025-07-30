---
nav_title: Liquid
article_title: Liquid
page_order: 0
layout: dev_guide
search_rank: 3
guide_top_header: "Personalização Usando Liquid Tags"
guide_top_text: "Braze pode substituir automaticamente valores de um determinado usuário em suas mensagens. Coloque sua expressão dentro de dois conjuntos de chaves para notificar a Braze que você usará um valor interpolado. Dentro destes colchetes, quaisquer valores de usuário que você queira substituir devem ser cercados por um conjunto adicional de colchetes com um cifrão na frente deles.<br><br>Para mais informações sobre Liquid, confira nossa jornada guiada <b><a href='https://learning.braze.com/path/dynamic-personalization-with-liquid'>Personalização Dinâmica com Liquid</a></b> no Braze Learning!"
description: "Esta landing page cobre todas as coisas sobre Liquid, como tags de personalização suportadas, filtros, definição de valores padrão e mais."

guide_featured_title: "Artigos de seção"
guide_featured_list:
- name: Usando Liquid
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/using_liquid/
  image: /assets/img/braze_icons/beaker-02.svg
- name: Tags de Personalização Suportadas
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/
  image: /assets/img/braze_icons/tag-01.svg
- name: Operadores
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/operators/
  image: /assets/img/braze_icons/code-02.svg
- name: Filtros
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/filters/
  image: /assets/img/braze_icons/flag-02.svg
- name: Filtros Avançados
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/
  image: /assets/img/braze_icons/settings-01.svg
- name: Definindo Valores Padrão
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/setting_default_values/
  image: /assets/img/braze_icons/table.svg
- name: Lógica Condicional de Envio de Mensagens
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/
  image: /assets/img/braze_icons/columns-01.svg
- name: Abortando Mensagens
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/
  image: /assets/img/braze_icons/refresh-ccw-01.svg
- name: Casos de Uso de Liquid
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

> O Liquid é uma linguagem de modelo de código aberto desenvolvida pela Shopify e escrita em Ruby. Na Braze, Liquid é usado para modelar dados do perfil de um usuário em mensagens. 

Por exemplo, você pode recuperar um atributo personalizado de um perfil de usuário que é um tipo de dado inteiro e arredondar esse valor para o número inteiro mais próximo. Para mais informações sobre a sintaxe e uso do Liquid, consulte [**Tags de personalização compatíveis**]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/).

A linguagem de modelo Liquid é compatível com o uso de objetos, tags e filtros.

- [**Objetos**]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) permitem que você insira atributos personalizados em suas mensagens.
- [**Tags**]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/) permitem que você insira dados no envio de mensagens e use a lógica condicional para enviar mensagens se determinadas condições forem atendidas. Por exemplo, você pode usar tags para incluir lógica inteligente, como declarações "if", em suas campanhas.
- [**Filtros**]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/filters/) permitem que você reformate atributos personalizados e conteúdo dinâmico. Por exemplo, você pode usar o [filtro `date` ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/filters/#date-filter) para converter um carimbo de data/hora, como *2016-09-07 08:43:50 UTC*, em uma data, como *7 de setembro de 2016*.

{% alert warning %}
Atualmente, o Braze não suporta 100% do Liquid da Shopify, apenas algumas partes que tentamos delinear em nossa documentação. Recomendamos fortemente testar todas as mensagens usando Liquid antes de enviá-las para reduzir o risco de erros ou de usar Liquid não suportado.
{% endalert %}

### Suporte ao Liquid 5

A Braze é compatível com o Liquid até a versão **Liquid 5 da Shopify**. A implementação do Liquid permite a personalização da sintaxe, tipos de tag e controle de espaços em branco. Para saber mais sobre tags específicas, consulte [tags de sintaxe]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#syntax-tags).

Os seguintes novos filtros de vetor e matemática estão disponíveis para uso no seu Liquid enquanto você constrói seu envio de mensagens.
- `at_least`
- `at_most`
- `compact`
- `concat`
- `sort_natural`
- `where`

Consulte [Filtros]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/filters/) para obter definições.

### Atualizações do Liquid

#### Etiquetas coloridas

Cada elemento Liquid corresponde a uma cor, permitindo que você diferencie seu Liquid de relance no seu editor Liquid.

![]({% image_buster /assets/img/liquid_color_code.png %})

#### Predictive Liquid

Você também pode aproveitar a previsão do Liquid para atributos personalizados, nomes de atributos e muito mais ao criar suas mensagens personalizadas.

![]({% image_buster /assets/img/liquid_auto_complete.gif %}){: style="max-width:70%;"}

## Termos a saber

Estes termos são reinterpretados a partir da [**documentação da Shopify**](https://shopify.github.io/liquid/basics/introduction/) com base no nosso nível de suporte.

{% raw %}

| Prazo | Definição | Exemplo |  
|---|---|---|
| Liquid | Uma linguagem de modelo comumente usada e voltada para o cliente, criada pela Shopify e escrita em Ruby, que é usada para carregar e extrair conteúdo dinâmico. | `{{${first_name}}}` inserirá o nome de um usuário em uma mensagem. |
| Objeto | Uma denotação de uma variável e local do nome da variável pretendida que diz ao Liquid onde mostrar o conteúdo na mensagem. | `{{${city}}}` inserirá a cidade de um usuário em uma mensagem. |
| tag de lógica condicional | Usado para criar lógica e controlar o fluxo do conteúdo da mensagem. No Braze, as tags de lógica condicional são usadas para criar exceções e variações nas mensagens com base em certos critérios predefinidos. | ```{% if ${language} == 'en' %}``` disparará sua mensagem de uma forma designada no caso de um usuário ter designado "Inglês" como seu idioma. |
| Filtros | Usado para alterar, restringir ou reformatar a saída do objeto Liquid. Ele é frequentemente usado para criar operações matemáticas. | ```{{"Big Sale" | upcase}}``` fará com que as palavras "Big Sale" apareçam como "BIG SALE" na mensagem. |
| Operadores | Usado em mensagens para criar dependências ou critérios que podem afetar qual mensagem seu usuário recebe. | Se um usuário atender aos critérios definidos em uma mensagem marcada com `{% custom_attribute.${Total_Revenue} > 0%}`, ele receberá a mensagem. Se não, eles receberão outra mensagem designada (ou não), dependendo do que você definir. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endraw %}

<br>

