---
nav_title: PERGUNTAS FREQUENTES
article_title: Perguntas frequentes
page_order: 12
description: "Este artigo fornece respostas a perguntas frequentes sobre o Liquid."

---

# Perguntas frequentes

> Nesta página, você encontrará respostas para algumas perguntas frequentes sobre o Liquid.<br><br>No momento, o Braze não oferece suporte a 100% do Shopify Liquid, apenas a algumas partes que tentamos delinear em nossa documentação. É altamente recomendável testar todas as mensagens usando o Liquid antes de enviá-las para reduzir o risco de erros ou de usar um Liquid sem suporte.

### Como faço para usar os snippets do Liquid no Braze?

Em muitos casos, você pode incorporar snippets do Liquid navegando até suas campanhas ou Canvases e inserindo o Liquid no modal de personalização em áreas como o corpo da mensagem de e-mail ou em seus segmentos. 

#### Onde posso obter mais informações?

Para saber mais sobre o Liquid, confira nosso caminho guiado de aprendizagem [Dynamic Personalization with Liquid](https://learning.braze.com/path/dynamic-personalization-with-liquid) Braze! Você também pode consultar a [biblioteca de casos de uso do Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/liquid_use_cases/) para obter inspiração e uma variedade de exemplos de personalização usando o Liquid.

### Qual é a diferença entre usar o Liquid e o Connected Content para personalização?

O Braze Connected Content é um exemplo de uma tag Liquid. Ele também é usado para personalização, mas esses dados vêm de um endpoint externo em vez de dados armazenados no Braze. Confira nossa seção dedicada ao [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content) para saber mais sobre como expandir a forma de personalizar suas mensagens.

### O que é o Liquid Templating?

Essa é a maneira mais comum de usar o Liquid in Braze. A modelagem líquida envolve a extração de dados do perfil de um usuário para uma mensagem. Esses dados podem variar desde o primeiro nome de um usuário até eventos personalizados de uma mensagem acionada por evento.

Consulte [Tags de personalização compatíveis]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/) para obter uma lista completa das tags Liquid compatíveis.

### Como faço para atribuir variáveis com o Liquid?

Você pode criar e atribuir variáveis usando a tag `assign`. Isso cria uma variável no compositor da mensagem que também pode ser referenciada em sua mensagem.

### O uso do Liquid registra pontos de dados?

Não.

### Como posso usar o Liquid para enviar uma saudação personalizada?

Para uma saudação personalizada usando o primeiro nome de um usuário, é possível obter os atributos padrão do perfil do usuário, como {% raw %} `{{${first_name}}}`, `{{${last_name}}}`.

Você também pode usar uma instrução Liquid `{% if X %}` {% endraw %}para fazer a renderização condicional com base em qualquer coisa, como o dia da semana ou atributos personalizados. Para obter mais informações sobre os operadores Liquid suportados que podem ser usados em instruções condicionais, consulte [Operadores]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/operators/).

### Como posso personalizar uma mensagem com base na localização de um cliente?

{% raw %}
Há um atributo padrão para o local do usuário: `{{${most_recent_location}}}`.

### Qual é a diferença entre {{campaign.${name}}} e {{campaign.${message_name}}}?

Tanto `{{campaign.${name}}}` quanto `{{campaign.${message_name}}}` são compatíveis com as tags de personalização Liquid. Ambas as tags fazem referência aos atributos da campanha. `{{campaign.${name}}}` indica o nome de sua campanha e `{{campaign.${message_name}}}` é o nome de sua variante de mensagem.
{% endraw %}

### Como uso o Liquid com objetos aninhados?

O Braze tem um recurso interno que gera código líquido para segmentos que podem ser usados em uma mensagem. Especificamente, você pode criar um segmento que corresponda a vários critérios em um objeto.

Para obter mais informações, consulte [Segmentação multicritério]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/#multi-criteria-segmentation).

### Como posso usar atributos de evento para personalizar uma mensagem que um evento está acionando?

{% raw %}
Você pode acessar as propriedades dos eventos acionados pela API com a tag `api_triggered_property`: `{{api_trigger_properties.${attribute_key}}}`.  
{% endraw %}

### O que é a lógica de abortar e como posso usá-la?

A lógica de abortar permite que você interrompa o envio de uma mensagem se as condições forem atendidas. Isso é especialmente útil para evitar que mensagens incompletas sejam enviadas aos seus usuários. Para obter exemplos de lógica de abortamento em suas campanhas de marketing, leia mais em [Abortar mensagens]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/).

### O que é a lógica de loop for e como posso usá-la?

Os loops For também são conhecidos como [tags de iteração](https://shopify.github.io/liquid/tags/iteration/). O uso da lógica de loop for em seus snippets do Liquid permite que você percorra blocos do Liquid até que uma condição seja atendida. 

No Braze, isso pode ser usado para verificar itens em um atributo personalizado de matriz ou uma lista de valores e objetos retornados por uma resposta de chamada de [catálogo]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs), [seleção]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/) ou [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content). Especificamente, você pode usar a lógica de loop for como parte de suas mensagens para verificar se um produto está em estoque ou se um produto tem uma classificação mínima. 

Por exemplo, digamos que você tenha um catálogo chamado "Games" (Jogos) com uma seleção chamada "cheap_games".. Para obter os títulos dos jogos em "cheap_games",, você pode usar este snippet do Liquid:

{% raw %}
```liquid
{% catalog_selection_items Games cheap_games %}
{% for item in items %}
 Get this game: {{ item.title }}
{% endfor %}
```
{% endraw %}

Quando as condições definidas forem atendidas, sua mensagem poderá prosseguir. Usar essa lógica é uma maneira útil de economizar tempo, em vez de repetir blocos Liquid para diferentes condições.
