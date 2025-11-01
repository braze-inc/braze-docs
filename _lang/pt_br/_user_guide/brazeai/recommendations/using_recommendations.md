---
nav_title: Usando recomendações
article_title: Uso de recomendações de itens em suas mensagens
description: "Este artigo descreve como usar recomendações de itens em sua mensagem."
page_order: 1.2
---

# Uso de recomendações de itens em suas mensagens

> Depois que sua recomendação for treinada, você poderá usar o Liquid para buscar e exibir itens recomendados em suas mensagens, trabalhando diretamente com o objeto Liquid `product_recommendation`.

{% alert tip %}
Para obter uma explicação passo a passo, confira nosso curso Braze Learning: [Criando experiências personalizadas com IA](https://learning.braze.com/ai-item-recommendations-use-case/1996254).
{% endalert %}

## Pré-requisitos

Antes de poder usar as recomendações em suas mensagens, você precisará [criar e treinar um mecanismo de recomendação]({{site.baseurl}}/user_guide/brazeai/recommendations/creating_recommendations/). O treinamento pode levar de 10 minutos a 36 horas - você receberá um e-mail quando ele for concluído ou se ocorrer um erro.

## Usar recomendações em suas mensagens

### Etapa 1: Adicionar código Liquid

Depois que sua recomendação terminar de ser treinada, você poderá personalizar suas mensagens com o Liquid para inserir os produtos mais populares nesse catálogo.

{% tabs local %}
{% tab pre-formatted code %}
\!["Adicionar personalização" modal com recomendação de item como o tipo de personalização.]({% image_buster /assets/img/add_personalization.png %}){: style="max-width:30%;float:right;margin-left:15px;"}

É possível gerar o Liquid na seção **Adicionar personalização** no compositor de mensagens:

1. Em qualquer compositor de mensagem que ofereça suporte à personalização, selecione <i class="fa-solid fa-circle-plus" style="color: #12aec5;" title="Adicionar personalização"></i> para abrir a janela de personalização.
2. Para **Tipo de personalização**, selecione **Recomendação de item**.
3. Em **Item Recommendation Name (Nome da recomendação do item**), selecione a recomendação que você acabou de criar.
4. Em **Number of Predicted Items (Número de itens previstos**), digite quantos produtos principais você gostaria que fossem inseridos. Por exemplo, você pode exibir os três itens mais comprados.
5. Em **Informações a serem exibidas**, selecione quais campos do catálogo devem ser incluídos para cada item. Os valores desses campos para cada item serão extraídos do catálogo associado a essa recomendação.
6. Selecione o ícone **Copiar** e cole o Liquid onde quer que ele esteja em sua mensagem.
{% endtab %}

{% tab custom code %}
Você pode escrever código Liquid personalizado fazendo referência a um objeto `product_recommendation` do catálogo. Ele contém todos os dados de recomendação de produtos gerados dinamicamente para esse catálogo, estruturados como uma matriz de objetos, em que cada objeto representa um item recomendado.

|Especificação|Detalhes|
|-------------|-------|
|**Estrutura**|Cada item é acessado como `items[index]`, em que o índice começa em 0 (para o primeiro item) e aumenta para os itens subsequentes.|
|**Campos do catálogo**|Cada item da matriz contém pares de valores-chave correspondentes a campos (colunas) no catálogo. Por exemplo, os campos comuns do catálogo para recomendações de produtos incluem:<br>- `name` ou `title`<br>- `price`<br>- `image_url`|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Use a tag `assign` para obter os dados de `product_recommendation` e atribuí-los a uma variável.

{% raw %}
```liquid
{% assign items = {{product_recommendation.${recommendation_name}}} %}
```
{% endraw %}

Substitua o seguinte:

|Espaço reservado|Descrição|
|-----------|-----------|
|`recommendation_name`|O nome da recomendação de IA que você criou no Braze.|
|`items`|A variável que armazena a matriz de itens recomendados.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Em seguida, faça referência a itens específicos e seus campos usando indexação de matriz e notação de ponto:

{% raw %}
```liquid
{% assign items = {{product_recommendation.${recommendation_name}}} %}
{{ items[0].name }} for {{ items[0].price }}
```
{% endraw %}

Para incluir vários itens, faça referência a cada item individualmente por seu índice. `.name` e `.price` extraem o campo correspondente do catálogo. 

{% raw %}
```liquid
{% assign items = {{product_recommendation.${recommendation_name}}} %}
{{ items[0].name }} for {{ items[0].price }}
{{ items[1].name }} for {{ items[1].price }}
{{ items[2].name }} for {{ items[2].price }}
```
{% endraw %}

As recomendações de IA retornam vários produtos como uma matriz, em que `items[0]` é o primeiro item, `items[1]` é o segundo e assim por diante. Se uma recomendação retornar apenas um item, a tentativa de fazer referência a `items[1]` resultará em um campo vazio.
{% endtab %}
{% endtabs %}

### Etapa 2: Faça referência a uma imagem (opcional)

Se o catálogo recomendado incluir links para imagens, você poderá fazer referência a elas em sua mensagem. 

{% tabs %}
{% tab Drag-and-drop%}
No editor de arrastar e soltar do e-mail, adicione um bloco de imagem ao seu e-mail e selecione o bloco de imagem para abrir **as propriedades da imagem**.

\![Painel de propriedades da imagem no editor de arrastar e soltar]({% image_buster /assets/img/image_with_liquid.png %}){: style="max-width:45%"}

Alterne **Image with Liquid** e adicione o seguinte ao campo **Dynamic URL**:

{% raw %}
```liquid
{% assign items = {{product_recommendation.${recommendation_name}}} %}
{{ items[0].image_url_field }}
```
{% endraw %}

Substitua o seguinte:

|Espaço reservado|Descrição|
|-----------|-----------|
|`recommendation_name`|O nome de sua recomendação.|
|`image_url_field`|O nome do campo em seu catálogo que contém URLs de imagens.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Para incluir uma imagem de espaço reservado nos e-mails de visualização e teste, selecione **Escolher imagem** e, em seguida, escolha uma imagem da sua biblioteca de mídia ou insira o URL de uma imagem do seu site de hospedagem.
{% endtab %}

{% tab HTML %}
Para referências de imagens HTML, defina o atributo `src` da imagem para o campo URL da imagem no catálogo. Talvez você queira usar outro campo, como o nome ou a descrição de um produto, como o texto alternativo.

{% raw %}
```html
{% assign items = {{product_recommendation.${recommendation_name}}} %}
<img src="{{ items[0].image_url_field }}" alt="{{ items[0].name }}">
```
{% endraw %}

Substitua o seguinte:

|Espaço reservado|Descrição|
|-----------|-----------|
|`recommendation_name`|O nome de sua recomendação.|
|`image_url_field`|O nome do campo em seu catálogo que contém URLs de imagens.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% endtab %}
{% endtabs %}
