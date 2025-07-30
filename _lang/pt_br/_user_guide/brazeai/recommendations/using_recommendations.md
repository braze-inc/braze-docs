---
nav_title: Uso de recomendações de itens
article_title: Uso de recomendações de itens em seu envio de mensagens
description: "Este artigo descreve como usar recomendações de itens em sua mensagem."
page_order: 20
---

# Uso de recomendações de itens em seu envio de mensagens

> Depois que sua recomendação for treinada, você poderá usar o Liquid para buscar e exibir itens recomendados em suas mensagens. A chave aqui é trabalhar diretamente com o objeto `product_recommendation` Liquid. Este artigo aborda o objeto `product_recommendation` Liquid e inclui um tutorial para ajudá-lo a colocar esse conhecimento em prática.

{% alert tip %}
Este artigo descreve detalhadamente a sintaxe do objeto Liquid. No entanto, você pode [inserir variáveis pré-formatadas]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#inserting-pre-formatted-variables) com padrões por meio do modal **Add Personalization (Adicionar personalização** ), localizado no canto superior direito de qualquer campo de texto modelado.
{% endalert %}

Para saber mais sobre o uso de recomendações de itens de IA no Braze, confira nosso [curso do Braze Learning sobre como criar experiências personalizadas com IA][1]. Este curso abrange casos de uso do setor, instruções passo a passo e um caso de uso adicional para criar uma mensagem no app com recomendações orientadas por IA.

## Anatomia do objeto de recomendação

O objeto `product_recommendation` representa o conjunto de itens recomendados pelo modelo. Ele fornece dados diretamente do catálogo associado, estruturado como um vetor de objetos, em que cada objeto representa um item recomendado.

- **Estrutura:** Cada item é acessado como `items[index]`, em que o índice começa em 0 (para o primeiro item) e aumenta para os itens subsequentes.
- **Campos do catálogo:** Cada item da matriz contém pares de valores-chave correspondentes a campos (colunas) no catálogo. Por exemplo, os campos comuns do catálogo para recomendações do produto incluem:
   - `name` ou `title`
   - `price`
   - `image_url`

## Liquid tags

O objeto `product_recommendation` contém recomendações de produtos geradas dinamicamente. Para acessá-los no Liquid, você deve primeiro atribuir os dados a uma variável antes de usá-los na mensagem.

### Atribuindo dados de recomendação

Sempre comece com a tag assign para buscar os dados do `product_recommendation` e armazená-los em uma variável.

{% raw %}

```liquid
{% assign items = {{product_recommendation.${RECOMMENDATION_NAME}}} %}
```

{% endraw %}

- `RECOMMENDATION_NAME`: Substitua isso pelo nome da recomendação de IA que você criou no Braze.
- `items`: A variável que armazena a matriz de itens recomendados.

### Acesso a itens individuais

Depois que os dados da recomendação forem atribuídos, você poderá fazer referência a itens específicos e seus campos usando a indexação de matriz e a notação de ponto:

{% raw %}

```liquid
{% assign items = {{product_recommendation.${RECOMMENDATION_NAME}}} %}
{{ items[0].name }} for {{ items[0].price }}
```

{% endraw %}

Para incluir vários itens, faça referência a cada item individualmente por seu índice. `.name` e `.price` extraem o campo correspondente do catálogo. 

{% raw %}

```liquid
{% assign items = {{product_recommendation.${RECOMMENDATION_NAME}}} %}
{{ items[0].name }} for {{ items[0].price }}
{{ items[1].name }} for {{ items[1].price }}
{{ items[2].name }} for {{ items[2].price }}
```

{% endraw %}

As recomendações do produto IA retornam vários produtos como uma matriz, em que `items[0]` é o primeiro item, `items[1]` é o segundo e assim por diante. Se uma recomendação retornar apenas um item, a tentativa de fazer referência a `items[1]` resultará em um campo vazio.

## Adição de imagens

Se o catálogo usado por sua recomendação incluir links para imagens, você poderá fazer referência a essas imagens em sua mensagem. 

{% tabs %}

{% tab Arrastar e soltar%}
Em criadores com campos de imagem, adicione o seguinte Liquid ao respectivo campo no criador:

{% raw %}

```liquid
{% assign items = {{product_recommendation.${RECOMMENDATION_NAME}}} %}
{{ items[0].IMAGE_URL_FIELD }}
```

{% endraw %}

Para o editor de arrastar e soltar de e-mail:

1. Adicione um bloco de imagem ao seu e-mail.
2. Selecione o bloco de imagem (não o botão **Pesquisar** ) para abrir o painel **Propriedades da imagem**.
3. Ativar **Imagem com Liquid**. 
4. Cole o snippet Liquid no campo **URL dinâmico**.

{% raw %}

```liquid
{% assign items = {{product_recommendation.${RECOMMENDATION_NAME}}} %}
{{ items[0].IMAGE_URL_FIELD }}
```

{% endraw %}

![Painel de propriedades da imagem no editor de arrastar e soltar]({% image_buster /assets/img/image_with_liquid.png %}){: style="max-width:60%"}

{:start="5"}

5. Para incluir uma imagem de espaço reservado nos e-mails de prévia e teste, pressione **Escolher imagem** para adicionar uma imagem de espaço reservado da biblioteca de mídia ou insira um URL onde a imagem esteja hospedada.

{% endtab %}

{% tab HTML %}

Para referências de imagens HTML, defina a atribuição `src` da imagem para o campo URL da imagem no catálogo. Talvez você queira usar outro campo, como o nome ou a descrição de um produto, como o texto alternativo.

{% raw %}

```html
{% assign items = {{product_recommendation.${RECOMMENDATION_NAME}}} %}
<img src="{{ items[0].IMAGE_URL_FIELD }}" alt="{{ items[0].name }}">
```

{% endraw %}

{% endtab %}

{% endtabs %}

-  Substitua `MY_RECOMMENDATION_NAME` pelo nome de sua recomendação
- Substitua `IMAGE_URL_FIELD` pelo nome do campo em seu catálogo que contém URLs de imagens.


## Tutorial: Criar um e-mail de carrinho abandonado

Neste tutorial, você aprenderá a criar um e-mail dinâmico que recomenda produtos aos usuários com base em suas preferências ou comportamento usando as recomendações de itens do Braze IA. 

Digamos que você seja um profissional de marketing da "Flash & Thread", uma varejista de roupas on-line. Você deseja reengajar os clientes que deixaram itens em seus carrinhos e fazer upsell de produtos adicionais. Seu objetivo é criar um e-mail que exiba os itens abandonados e recomendações personalizadas.

### Etapa 1: Prepare seu catálogo

Sua recomendação extrairá itens de um catálogo. Siga as etapas para Criar um catálogo. Certifique-se de que seu catálogo inclua esses campos:

| Campo | Tipo de dados | Descrição |
| --- | --- | --- |
| id | String | Um identificador exclusivo para cada item em seu catálogo |
| nome | String | O nome do produto, por exemplo, "Suéter de malha listrado". |
| preço | Número | O preço do produto, por exemplo, "49,99". |
| image_url | String | Um URL que aponta para a imagem do produto. Deve ser protegido por HTTPS. Se suas imagens estiverem hospedadas na biblioteca de mídia, passe o mouse sobre um ativo para copiar seu URL. |
| categoria | String | A categoria do produto, como "Suéteres" ou "Acessórios". |
| cor | String | Uma cor descritiva para o produto, como "Navy/Grey". |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


#### Exemplo de catálogo

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;font-size: 14px; font-weight: bold; background-color: #f4f4f7; text-transform: lowercase; color: #212123; font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top;word-break:normal}
</style>

<table class="tg">
  <tr>
    <th>id</th>
    <th>nome</th>
    <th>preço</th>
    <th>image_url</th>
    <th>categoria</th>
    <th>cor</th>
  </tr>
  <tr>
    <td>1001</td>
    <td>Suéter de tricô listrado</td>
    <td>49.99</td>
    <td>https://{{media_library}}/images/67a41294f5eac400685ce908/original.png?1738805908</td>
    <td>Suéteres</td>
    <td>Marinho/Cinza</td>
  </tr>
  <tr>
    <td>1002</td>
    <td>Sapatos personalizados do Yacht Club</td>
    <td>79.99</td>
    <td>https://{{media_library}}/images/67a4136fe5a7660068bbe046/original.png?1738806127</td>
    <td>Calçados</td>
    <td>Marinha</td>
  </tr>
  <tr>
    <td>1003</td>
    <td>Sapatos de volta ao trabalho</td>
    <td>89.99</td>
    <td>https://{{media_library}}/images/67a41370f542c1006798c26e/original.png?1738806128</td>
    <td>Calçados</td>
    <td>Rosa/Dourado</td>
  </tr>
  <tr>
    <td>1004</td>
    <td>Chapéu de ponta a ponta do verão</td>
    <td>29.99</td>
    <td>https://{{media_library}}/images/67a4136fbf6f620068511b67/original.png?1738806127</td>
    <td>Acessórios</td>
    <td>Floral branco</td>
  </tr>
</table>


### Etapa 2: Configure sua recomendação

1. Em seu catálogo, selecione **Criar recomendação**.
2. Siga as etapas de [Criação de uma recomendação de item de IA][3]. 
3. Para o tipo de recomendação, selecione **IA Personalizada**.
4. Use o catálogo que você acabou de criar para treinar a recomendação. Isso pode levar algum tempo - você receberá um e-mail quando o treinamento for concluído.

### Etapa 3: Criar um e-mail

Quando a recomendação tiver concluído o treinamento, você poderá usá-la em seu envio de mensagens.

1. Crie um e-mail com o editor de arrastar e soltar.
2. No corpo da mensagem, adicione um bloco de imagem onde quer que você queira extrair uma recomendação do catálogo. 
3. Selecione o bloco de imagem e ative a opção **Imagem com Liquid** no painel **Propriedades da imagem**. 
4. Cole esse trecho de Liquid no campo URL dinâmico.


{% raw %}

```liquid
{% assign items = {{product_recommendation.${abandoned_cart}}} %}
{{ items[0].image_url }}
```

{% endraw %}

{: start="5"}

5. Abaixo da imagem, adicione um bloco de parágrafo. Aqui é onde você adicionará o nome do produto e quaisquer detalhes de apoio. 
6. Cole o seguinte trecho de Liquid no bloco. Isso extrai o nome, a categoria, a cor e o preço da primeira recomendação do catálogo e os adiciona como linhas separadas. 

{% raw %}

```liquid
{% assign items = {{product_recommendation.${abandoned_cart}}} %}
{{ items[0].name }}
{{ items[0].category }}
{{ items[0].color }}
${{ items[0].price }}
```

{% endraw %}

{: start="7"}

7. Em ambos os snippets, substitua `abandoned_cart` pelo nome de sua recomendação no Braze.
8. Verifique novamente se os nomes dos campos do item (`{{ items[0].field_name }}`) correspondem aos nomes das colunas em seu catálogo.
9. Incremente a matriz em uma unidade cada vez que você repetir o bloco para extrair o próximo item recomendado do catálogo. Por exemplo, a matriz começa com `{{ items[0].name }}`, portanto, o próximo item seria `{{ items[1].name }}`.

### Etapa 4: Prévia de sua mensagem

Para ver a aparência da sua mensagem para um usuário real:

1. Acesse a guia **Preview & Test (Prévia e teste** ) em seu editor.
2. Selecione **Usuário aleatório** na lista suspensa.
3. Selecione **Obter usuário aleatório** para buscar um usuário do seu público e fazer uma prévia de como o e-mail aparecerá com os dados dele.

A prévia renderizará totalmente o Liquid, incluindo recomendações de IA, desde que o usuário selecionado tenha os atributos necessários ou dados de eventos vinculados à recomendação.

Se a recomendação não aparecer na prévia, verifique o seguinte:

- O usuário interagiu com produtos ou eventos relevantes que treinaram o modelo de recomendação
- A recomendação em si foi treinada com sucesso
- O código Liquid faz referência corretamente à recomendação e aos campos corretos



[1]: https://learning.braze.com/ai-item-recommendations-use-case/1996254
[2]: {% image_buster /assets/img/image_with_liquid.png %}
[3]: {{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations#creating-an-ai-item-recommendation