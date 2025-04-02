---
nav_title: Perguntas frequentes
article_title: Perguntas frequentes
page_order: 12
description: "Este artigo fornece respostas às perguntas frequentes sobre Liquid."

---

# Perguntas frequentes

> Nesta página, você encontrará respostas para algumas perguntas frequentes sobre Liquid.<br><br>A Braze atualmente não é compatível com 100% do Liquid da Shopify, apenas certas partes que tentamos delinear em nossa documentação. Recomendamos fortemente testar todas as mensagens usando Liquid antes de enviá-las para reduzir o risco de erros ou de usar Liquid não suportado.

### Como eu uso trechos de Liquid na Braze?

Em muitos casos, você pode incorporar trechos de Liquid navegando para suas campanhas ou canvas, e inserindo Liquid no modal de personalização em áreas como o corpo da mensagem de e-mail ou em seus segmentos. 

#### Onde posso aprender mais?

Para mais informações sobre o Liquid, confira nossa jornada de aprendizado Braze [Personalização Dinâmica com Liquid](https://learning.braze.com/path/dynamic-personalization-with-liquid)! Você também pode consultar a [biblioteca de casos de uso do Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/liquid_use_cases/) para inspiração e uma variedade de exemplos de personalização usando Liquid.

### Qual é a diferença entre usar Liquid e Conteúdo Conectado para personalização?

Braze Connected Content é um exemplo de um Liquid tag. Também é usado para personalização, mas esses dados vêm de um endpoint externo em vez de dados armazenados na Braze. Confira nossa seção dedicada a [Conteúdo Conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content) para saber mais sobre como expandir a personalização de suas mensagens.

### O que é a modelagem Liquid?

Esta é a maneira mais comum de usar Liquid no Braze. A modelagem Liquid envolve extrair dados do perfil de um usuário para uma mensagem. Esses dados podem variar desde o nome de um usuário até eventos personalizados de uma mensagem acionada por evento.

Consulte [tags de personalização compatíveis]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/) para ver uma lista completa das tags Liquid suportadas.

### Como eu atribuo variáveis com Liquid?

Você pode criar e atribuir variáveis usando a tag `assign`. Isso gera uma variável no criador de mensagem que também pode ser referenciada em toda a sua mensagem.

### Usar Liquid consome pontos de dados?

Não.

### Como posso usar Liquid para enviar uma saudação personalizada?

Para uma saudação personalizada usando o nome do usuário, você pode obter os atributos padrão do perfil do usuário, como {% raw %} `{{${first_name}}}`, `{{${last_name}}}`.

Você também pode usar uma `{% if X %}` {% endraw %}declaração Liquid para fazer renderização condicional com base em qualquer coisa, como o dia da semana ou atributos personalizados. Para saber mais sobre os operadores Liquid suportados que podem ser usados em declarações condicionais, confira [Operadores]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/operators/).

### Como posso personalizar uma mensagem com base na {local} de um cliente?

{% raw %}
Há um atributo padrão para a localização do usuário: `{{${most_recent_location}}}`.

### Qual é a diferença entre {{campaign.${name}}} e {{campaign.${message_name}}}?

Tanto `{{campaign.${name}}}` quanto `{{campaign.${message_name}}}` são tags de personalização Liquid suportadas. Ambas as tags referenciam atributos da campanha. `{{campaign.${name}}}` denota o nome da sua campanha, e `{{campaign.${message_name}}}` é o nome da sua variante de mensagem.
{% endraw %}

### Como eu uso Liquid com objetos aninhados?

Braze possui um recurso embutido que gera código Liquid para segmentos que podem ser usados em uma mensagem. Especificamente, você pode criar um segmento que corresponda a vários critérios em um objeto.

Para saber mais, confira [Segmentação multi-critério]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/#multi-criteria-segmentation).

### Como uso atributos de evento para personalizar uma mensagem que um evento está acionando?

{% raw %}
Você pode acessar as propriedades dos eventos acionados pela API com a tag `api_triggered_property`: `{{api_trigger_properties.${attribute_key}}}`.  
{% endraw %}

### O que é lógica de aborto e como posso usá-la?

A lógica de aborto permite que você pare uma mensagem de ser enviada se as condições forem atendidas. Isso é especialmente útil para evitar que mensagens incompletas sejam enviadas aos seus usuários. Para exemplos de lógica de aborto em suas campanhas de marketing, leia mais em [Abortando mensagens]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/).

### Qual é a lógica do loop for e como posso usá-la?

Os loops for também são conhecidos como [tags de iteração](https://shopify.github.io/liquid/tags/iteration/). Usar a lógica do loop em seus trechos de Liquid permite que você percorra blocos de Liquid até que uma condição seja atendida. 

Na Braze, isso pode ser usado para verificar itens em um atributo personalizado de array, ou uma lista de valores e objetos retornados por uma resposta de [catálogo]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs), [seleção]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections/) ou chamada de [Conteúdo Conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content). Especificamente, você pode usar a lógica de loop for como parte do seu envio de mensagens para verificar se um produto está em estoque ou se um produto tem uma classificação mínima. 

Por exemplo, digamos que você tenha um catálogo chamado "Jogos" que tem uma seleção chamada "jogos_baratos". Para puxar os títulos dos jogos em "jogos_baratos", você poderia usar este trecho Liquid:

{% raw %}
```liquid
{% catalog_selection_items Games cheap_games %}
{% for item in items %}
 Get this game: {{ item.title }}
{% endfor %}
```
{% endraw %}

Uma vez que as condições estabelecidas sejam atendidas, sua mensagem pode prosseguir. Usar essa lógica é uma maneira útil de economizar tempo, em vez de repetir blocos de Liquid para diferentes condições.
