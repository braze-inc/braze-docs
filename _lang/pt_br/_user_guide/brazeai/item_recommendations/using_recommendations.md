---
nav_title: Usando recomendações
article_title: Use Recomendações de Itens em Seu Envio de Mensagens
description: "Este artigo descreve como usar recomendações de itens em sua mensagem."
page_order: 1.2
---

# Use recomendações de itens em seu envio de mensagens

> Depois que sua recomendação estiver treinada, você pode usar Liquid para buscar e exibir itens recomendados em suas mensagens, trabalhando diretamente com o objeto Liquid `product_recommendation`.

{% alert tip %}
Para um guia passo a passo, confira nosso curso do Braze Learning: [Elaborando Experiências Personalizadas com IA](https://learning.braze.com/ai-item-recommendations-use-case/1996254).
{% endalert %}

## Pré-requisitos

Antes que você possa usar recomendações em seu envio de mensagens, você precisará [criar e treinar um motor de recomendações]({{site.baseurl}}/user_guide/brazeai/recommendations/creating_recommendations/). O treinamento pode levar entre 10 minutos e 36 horas—você receberá um e-mail quando estiver concluído ou se ocorrer um erro.

## Usando recomendações em seu envio de mensagens

### Etapa 1: Adicione código Liquid

Depois que sua recomendação terminar o treinamento, você pode personalizar suas mensagens com Liquid para inserir os produtos mais populares naquele catálogo.

{% tabs local %}
{% tab pre-formatted code %}
![Modal "Adicionar Personalização" com recomendação de item como o tipo de personalização.]({% image_buster /assets/img/add_personalization.png %}){: style="max-width:30%;float:right;margin-left:15px;"}

Você pode gerar Liquid na seção **Adicionar personalização** em seu criador de mensagem:

1. Em todos os criadores de mensagens que suportam personalização, selecione <i class="fa-solid fa-circle-plus" style="color: #12aec5;" title="Adicionar personalização"></i> para abrir a janela de personalização.
2. Para **Tipo de personalização**, selecione **Recomendação de item**.
3. Em **Item Recommendation Name (Nome da recomendação do item**), selecione a recomendação que você acabou de criar.
4. Em **Number of Predicted Items (Número de itens previstos**), digite quantos produtos principais você gostaria que fossem inseridos. Por exemplo, você pode exibir os três itens mais comprados.
5. Em **Informações a serem exibidas**, selecione quais campos do catálogo devem ser incluídos para cada item. Os valores desses campos para cada item serão extraídos do catálogo associado a essa recomendação.
6. Selecione o ícone **Copiar** e cole o Liquid onde quer que ele seja necessário em sua mensagem.
{% endtab %}

{% tab custom code %}
Você pode escrever código Liquid personalizado referenciando o objeto `product_recommendation` de um catálogo. Ele contém todos os dados de recomendação de produtos gerados dinamicamente para aquele catálogo, estruturados como um array de objetos, onde cada objeto representa um item recomendado.

|Especificação|Informações|
|-------------|-------|
|**Estrutura**|Cada item é acessado como `items[index]`, onde o índice começa em 0 (para o primeiro item) e incrementa para os itens subsequentes.|
|**Campos do catálogo**|Cada item da matriz contém pares de valores-chave correspondentes a campos (colunas) no catálogo. Por exemplo, os campos comuns do catálogo para recomendações do produto incluem:<br>- `name` ou `title`<br>- `price`<br>- `image_url`|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Use a tag `assign` para buscar os dados `product_recommendation` e atribuí-los a uma variável.

{% raw %}
```liquid
{% assign items = {{product_recommendation.${recommendation_name}}} %}
```
{% endraw %}

Substitua o seguinte:

|Espaço reservado|Descrição|
|-----------|-----------|
|`recommendation_name`|O nome da recomendação de IA que você criou no Braze.|
|`items`|A variável que armazena o array de itens recomendados.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Em seguida, faça referência a itens específicos e seus campos usando indexação de array e notação de ponto:

{% raw %}
```liquid
{% assign items = {{product_recommendation.${recommendation_name}}} %}
{{ items[0].name }} for {{ items[0].price }}
```
{% endraw %}

Para incluir vários itens, faça referência a cada item individualmente pelo seu índice. `.name` e `.price` puxam o campo correspondente do catálogo. 

{% raw %}
```liquid
{% assign items = {{product_recommendation.${recommendation_name}}} %}
{{ items[0].name }} for {{ items[0].price }}
{{ items[1].name }} for {{ items[1].price }}
{{ items[2].name }} for {{ items[2].price }}
```
{% endraw %}

As recomendações de IA retornam vários produtos como um array, onde `items[0]` é o primeiro item, `items[1]` é o segundo, e assim por diante. Se uma recomendação retornar apenas um item, tentar referenciar `items[1]` resultará em um campo vazio.
{% endtab %}
{% endtabs %}

### Etapa 2: Referencie uma imagem (opcional)

Se o catálogo que sua recomendação inclui links de imagem, você pode referenciá-los em sua mensagem. 

{% tabs %}
{% tab Drag-and-drop%}
No editor de arrastar e soltar de e-mail, adicione um bloco de imagem ao seu e-mail, depois selecione o bloco de imagem para abrir **Propriedades da imagem**.

![Painel de propriedades da imagem no editor de arrastar e soltar]({% image_buster /assets/img/image_with_liquid.png %}){: style="max-width:45%"}

Ative **Imagem com Liquid**, depois adicione o seguinte ao campo **URL dinâmico**:

{% raw %}
```liquid
{% assign items = {{product_recommendation.${recommendation_name}}} %}
{{ items[0].image_url_field }}
```
{% endraw %}

Substitua o seguinte:

|Espaço reservado|Descrição|
|-----------|-----------|
|`recommendation_name`|O nome da sua recomendação.|
|`image_url_field`|O nome do campo no seu catálogo que contém URLs de imagens.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Para incluir uma imagem de espaço reservado na sua prévia e e-mails de teste, selecione **Escolher imagem** e escolha uma imagem da sua biblioteca de mídia ou insira a URL de uma imagem do seu site de hospedagem.
{% endtab %}

{% tab HTML %}
Para referências de imagem em HTML, defina o atributo `src` da imagem para o campo de URL da imagem no catálogo. Talvez você queira usar outro campo, como o nome ou a descrição de um produto, como o texto alternativo.

{% raw %}
```html
{% assign items = {{product_recommendation.${recommendation_name}}} %}
<img src="{{ items[0].image_url_field }}" alt="{{ items[0].name }}">
```
{% endraw %}

Substitua o seguinte:

|Espaço reservado|Descrição|
|-----------|-----------|
|`recommendation_name`|O nome da sua recomendação.|
|`image_url_field`|O nome do campo no seu catálogo que contém URLs de imagens.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% endtab %}
{% endtabs %}
