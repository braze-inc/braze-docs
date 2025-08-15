---
nav_title: Recomendações baseadas em regras
article_title: Criação de recomendações de itens baseadas em regras
description: "Este artigo de referência aborda como criar uma recomendação de item IA para itens em um catálogo."
page_order: 2
---

# Criação de recomendações de itens baseadas em regras

> Saiba como criar um mecanismo de recomendação baseado em regras a partir de itens em seu catálogo.

## Sobre recomendações de itens baseadas em regras

Um mecanismo de recomendação baseado em regras usa dados de usuários e informações de produtos para sugerir itens relevantes aos usuários dentro das mensagens. Ele usa [o Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) e [os catálogos]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/) do Braze ou [o Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) para personalizar dinamicamente o conteúdo com base no comportamento e nas atribuições do usuário.

{% alert important %}
As recomendações baseadas em regras são baseadas em uma lógica fixa que você deve definir manualmente. Isso significa que suas recomendações não se ajustarão ao histórico de compras e aos gostos do usuário, a menos que você atualize a lógica.<br><br>Para criar recomendações personalizadas de IA que se ajustam automaticamente ao histórico de um usuário, confira [as recomendações de itens de IA]({{site.baseurl}}/user_guide/brazeai/recommendations/creating_recommendations/ai/).
{% endalert %}

## Opções do mecanismo de recomendação

Ao decidir qual mecanismo de recomendação se adequa aos seus recursos disponíveis e aos casos de uso, consulte esta tabela de considerações:

<table style="text-align: center;">
  <thead>
    <tr>
      <th>Mecanismo de recomendação</th>
      <th>Nenhum ponto de dados consumido</th>
      <th>Solução sem código</th>
      <th>Sem Liquid avançado</th>
      <th>Atualiza automaticamente o feed de produtos</th>
      <th>Gerado com a interface do usuário do Braze</th>
      <th>Sem hospedagem de dados ou solução de problemas</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Catálogos CSV</strong></td>
      <td>✔</td>
      <td>Sim, se estiver usando Liquid pré-gerado.</td>
      <td>✔</td>
      <td>Sim, se as recomendações <strong>não</strong> forem atualizadas com frequência.</td>
      <td>✔</td>
      <td>✔</td>
    </tr>
    <tr>
      <td><strong>API de catálogos</strong></td>
      <td>✔</td>
      <td></td>
      <td>✔</td>
      <td>Sim, se as recomendações forem atualizadas a cada hora.</td>
      <td>✔</td>
      <td>✔</td>
    </tr>
    <tr>
      <td><strong>Conteúdo conectado</strong></td>
      <td>✔</td>
      <td></td>
      <td></td>
      <td>✔<br>(Recomendações atualizadas em tempo real)</td>
      <td>Sim, se for gerado fora do Braze.</td>
      <td></td>
    </tr>
    <tr>
      <td><strong>Liquid</strong></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>✔</td>
      <td>✔</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 .reset-td-br-7 role="presentation" }

## Criação de um mecanismo de recomendação

Crie seu mecanismo de recomendação usando um catálogo ou o Connected Content:

{% tabs local %}
{% tab usando um catálogo %}
Para criar seu mecanismo de recomendação usando um catálogo:

1. [Crie um catálogo]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/) de produtos.
2. Para cada produto, adicione uma lista de produtos recomendados como uma string separada por um delimitador (como um pipe `|`) em uma coluna chamada "product_recommendations".
3. Passe para o catálogo o ID do produto para o qual você deseja encontrar recomendações.
4. Obtenha o valor `product_recommendations` para esse item de catálogo e divida-o pelo delimitador com um filtro de divisão Liquid.
5. Passe um ou mais desses IDs de volta para o catálogo para coletar os outros detalhes do produto.

### Exemplo

Digamos que você tenha um aplicativo de alimentos saudáveis e queira criar uma campanha de cartão de conteúdo que envie receitas diferentes com base no tempo em que o usuário inscreveu-se em seu app. Primeiro, crie e faça upload de um catálogo por meio de um arquivo CSV que inclua as seguintes informações:

|Campo|Descrição|
|-----|-----------|
| **id** | Um número exclusivo que se correlaciona com o número de dias desde que o usuário inscreveu-se no seu app. Por exemplo, `3` está correlacionado a três dias. |
| **tipo** | A categoria da receita, como `comfort`, `fresh`, e outras. |
| **título** | O título do cartão de conteúdo que será enviado para cada ID, como "Prepare-se para o almoço desta semana" ou "Vamos almoçar tacos". |
| **link** | O link para o artigo da receita. |
| **image_url** | A imagem que corresponde à receita. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Depois que for feito o upload do catálogo para a Braze, verifique a prévia de um número selecionado de itens do catálogo para confirmar se as informações foram importadas com precisão. Os itens podem ser randomizados na prévia, mas isso não afetará o resultado do mecanismo de recomendação.

![Exemplo de catálogo em Braze.]({% image_buster /assets/img/recs/catalog_items.png %})

Crie uma campanha de cartão de conteúdo. No criador, insira a lógica Liquid para determinar quais usuários devem receber a campanha e qual receita e imagem devem ser exibidas. Nesse caso de uso, o Braze extrairá o endereço `start_date` do usuário (ou data de inscrição) e o comparará com a data atual. A diferença de dias determinará qual cartão de conteúdo será enviado.

{% subtabs local %}
{% subtab title %}
{% raw %}
```liquid
{% assign start_date = {{custom_attribute.${start_date}}} | date: "%s" %}
{% assign current_date = "now" | date: "%s" %}
{% assign diff = {{current_date}} | minus: {{start_date}} | divided_by: 86400 %}
{% assign days = {{diff}} | round %}
{% catalog_items Healthy_Recipe_Catalog_SMB {{days}} %}
{{ items[0].title }}
```
{% endraw %}
{% endsubtab %}

{% subtab message %}
{% raw %}
```liquid
{% assign start_date = {{custom_attribute.${start_date}}} | date: "%s" %}
{% assign current_date = "now" | date: "%s" %}
{% assign diff = {{current_date}} | minus: {{start_date}} | divided_by: 86400 %}
{% assign days = {{diff}} | round %}
{% catalog_items Healthy_Recipe_Catalog_SMB {{days}} %}
{% if items[0].title != blank %}
{{ items[0].body }}
{% else %}
{% abort_message('no card for today') %}
{% endif %}
```
{% endraw %}
{% endsubtab %}

{% subtab image %}
{% raw %}
```liquid
{% assign start_date = {{custom_attribute.${start_date}}} | date: "%s" %}
{% assign current_date = "now" | date: "%s" %}
{% assign diff = {{current_date}} | minus: {{start_date}} | divided_by: 86400 %}
{% assign days = {{diff}} | round %}
{% catalog_items Healthy_Recipe_Catalog_SMB {{days}} %}
{{ items[0].image_url }}
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}

Por exemplo:

![Um exemplo de criador de mensagens de uma campanha de cartão de conteúdo.]({% image_buster /assets/img/recs/content_card_preview.png %})

Na seção **Comportamento ao clicar**, insira a lógica Liquid para onde os usuários devem ser redirecionados quando clicarem no Content Card em dispositivos iOS, Android e Web. 

{% raw %}
```liquid
{% assign start_date = {{custom_attribute.${start_date}}} | date: "%s" %}
{% assign current_date = "now" | date: "%s" %}
{% assign diff = {{current_date}} | minus: {{start_date}} | divided_by: 86400 %}
{% assign days = {{diff}} | round %}
{% catalog_items Healthy_Recipe_Catalog_SMB {{days}} %}
{{ items[0].link }}
```
{% endraw %}

Por exemplo:

![Um exemplo de bloco de comportamento ao clicar no criador.]({% image_buster /assets/img/recs/on_click_behavior.png %}){: style="max-width:60%;"}<br><br>

Acesse a guia **Teste** e selecione **Usuário personalizado** em **Pré-visualizar mensagem como usuário**. Insira uma data no campo **Atributo personalizado** para prévia do cartão de conteúdo que seria enviado a um usuário que inscreveu-se nessa data. <br><br>

![Um exemplo de atributo personalizado chamado 'start_date'.]({% image_buster /assets/img/recs/custom_attributes_test.png %})
{% endtab %}

{% tab usando o Connected Content %}
Para criar seu mecanismo de recomendação usando o Connected Content, primeiro crie um novo endpoint usando um dos métodos a seguir:

|Opção|Descrição|
|------|-----------|
|**Converter uma planilha**|Converta uma planilha em um ponto de extremidade da API JSON usando um serviço como o SheetDP e anote o URL da API que isso gera.|
|**Criar um ponto de extremidade personalizado**|Crie, hospede e mantenha um endpoint interno personalizado.|
|**Use um mecanismo de terceiros** |Usar um mecanismo de recomendação de terceiros, como um de nossos [parceiros da Alloys]({{site.baseurl}}/partners/message_personalization/), incluindo [Amazon Personalise]({{site.baseurl}}/partners/amazon_personalize/), [Certona]({{site.baseurl}}/partners/message_personalization/dynamic_content/personalized_recommendations/certona/), [Dynamic Yield]({{site.baseurl}}/partners/dynamic_yield/) e outros.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Em seguida, use o Liquid em sua mensagem que chama o endpoint para fazer a correspondência de um valor de atributo personalizado com o perfil de um usuário e extrair a recomendação correspondente.

{% raw %}
```liquid
{% connected_content YOUR_API_URL :save items %}

{% assign recommended_item_ids_from_user_profile = custom_attribute.${RECOMMENDED_ITEM_IDS} | split: ';' %}

{% for item_id in recommended_item_ids_from_user_profile %}
  {% assign recommended_item = items | where: "ITEM_ID", ITEM_ID | first %}
  recommended_item.item_name
{% endfor %}
```
{% endraw %}

Substitua o seguinte:

| Atributo | Substituição |
| --- | --- |
|`YOUR_API_URL` | Substitua pelo URL real de sua API. |
|`RECOMMENDED_ITEM_IDS` | Substitua pelo nome real de seu atributo personalizado que contém os IDs dos itens recomendados. Espera-se que esse atributo seja uma string de IDs separados por ponto e vírgula. |
|`ITEM_ID` | Substitua pelo nome real da atribuição em sua resposta da API que corresponde à ID do item. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Este é um exemplo básico e talvez você precise modificá-lo ainda mais com base em suas necessidades específicas e na estrutura de dados. Para obter orientações mais detalhadas, consulte a [documentação do Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) ou consulte um desenvolvedor.
{% endalert %}

### Exemplo

Digamos que você queira extrair recomendações de restaurantes do banco de dados do Zomato Restaurants e salvar o resultado como uma variável local chamada `restaurants`. Você pode fazer a seguinte chamada de Connected Content:

{% raw %}
```liquid

{% connected_content https://developers.zomato.com/api/v2.1/search?entity_id={{city_id}}&entity_type=city&count=20&cuisines={{food_type}}&sort=rating:headers{“user-key”:“USER_KEY”} :save restaurants %}

{{city_food.restaurants[0]}}
```
{% endraw %}

Em seguida, digamos que você queira obter recomendações de restaurantes com base na cidade e no tipo de comida de um usuário. Isso pode ser feito inserindo dinamicamente os atributos personalizados da cidade e do tipo de alimento do usuário no início da chamada e atribuindo o valor de `restaurants` à variável `city_food.restaurants`.

A chamada do Connected Content seria semelhante a esta:

{% raw %}
```liquid
{% assign city_id = {{custom_attribute.${city_id} | default: ‘306’}} %}
{% assign food_type = {{custom_attribute.${food_type} | default: ‘471’}} %}

{%- connected_content https://developers.zomato.com/api/v2.1/search?entity_id={{city_id}}&entity_type=city&count=20&cuisines={{food_type}}&sort=rating:headers{“user-key”:“USER_KEY”} :save restaurants %}

{% assign restaurants = city_food.restaurants %}

{{city_food.restaurants[0]}}
```
{% endraw %}

Se quiser personalizar a resposta para recuperar apenas o nome e a classificação do restaurante, você pode adicionar filtros à ponta da chamada, da seguinte forma:

{% raw %}
```liquid
{% assign city_id = {{custom_attribute.${city_id} | default: ‘306’}} %}
{% assign food_type = {{custom_attribute.${food_type} | default: ‘471’}} %}

{%- connected_content https://developers.zomato.com/api/v2.1/search?entity_id={{city_id}}&entity_type=city&count=20&cuisines={{food_type}}&sort=rating:headers{“user-key”:”USER_KEY”} :save restaurants %}
{% assign restaurants = city_food.restaurants %}

{{city_food.restaurants[0].restaurant.name}}
{{city_food.restaurants[0].restaurant.user_rating.rating_text}}
```
{% endraw %}

Por fim, digamos que você queira agrupar as recomendações de restaurantes por classificação. Faça o seguinte:

1. Use `assign` para criar matrizes em branco para categorias de classificação de "excelente", "muito bom" e "bom".
2. Adicione um loop `for` que examine a classificação de cada restaurante da lista. 
- Se uma classificação for "Excelente", acrescente o nome do restaurante à string `excellent_restaurants` e, em seguida, adicione um caractere * no final para separar cada nome de restaurante. 
- Se uma classificação for "Muito bom", acrescente o nome do restaurante à string `very_good_restaurants` e, em seguida, adicione um caractere * no final.
- Se uma classificação for "Boa", acrescente o nome do restaurante à string `good_restaurants` e, em seguida, adicione um caractere * no final.
3. Limite o número de recomendações de restaurantes retornadas a quatro por categoria.

Esta é a aparência da chamada final:

{% raw %}
```liquid
{% assign city_id = {{custom_attribute.${city_id} | default: ‘306’}} %}
{% assign food_type = {{custom_attribute.${food_type} | default: ‘471’}} %}
{%- connected_content https://developers.zomato.com/api/v2.1/search?entity_id={{city_id}}&entity_type=city&count=20&cuisines={{food_type}}&sort=rating:headers{“user-key”:”USER_KEY”} :save restaurants %}
{% assign restaurants = city_food.restaurants %}
{% assign excellent_restaurants = “” %}
{% assign very_good_resturants = “” %}
{% assign good_restaurants = “” %}
{% for list in restaurants %}
{% if {{list.restaurant.user_rating.rating_text}} == `Excellent` %}
{% assign excellent_restaurants = excellent_restaurants | append: list.restaurant.name | append: `*` %}
{% elseif {{list.restaurant.user_rating.rating_text}} == `Very Good` %}
{% assign very_good_restaurants = very_good_restaurants | append: list.restaurant.name | append: `*` %}
{% elseif {{list.restaurant.user_rating.rating_text}} == `Good` %}
{% assign good_restaurants = good_restaurants | append: list.restaurant.name | append: `*` %}
{% endif %}
{% endfor %}
{% assign excellent_array = excellent_restaurants | split: `*` %}
{% assign very_good_array = very_good_restaurants | split: `*` %}
{% assign good_array = good_restaurants | split: `*` %}

Excellent places
{% for list in excellent_array %}

{{list}}
{% assign total_count = total_count | plus:1 %}
{% if total_count >= 4 %}
{% break %}
{% endif %}
{% endfor %}

Very good places
{% for list in very_good_array %}

{{list}}
{% assign total_count = total_count | plus:1 %}
{% if total_count >= 4 %}
{% break %}
{% endif %}
{% endfor %}

Good places
{% for list in good_array %}

{{list}}
{% assign total_count = total_count | plus:1 %}
{% if total_count >= 4 %}
{% break %}
{% endif %}
{% endfor %}
```
{% endraw %}

Veja na captura de tela abaixo um exemplo de como a resposta é exibida no dispositivo de um usuário.

![Renderização de uma lista de restaurantes gerada pelo exemplo de chamada final.]({% image_buster /assets/img/recs/sample_response.png %}){: style="max-width:30%;"}
{% endtab %}
{% endtabs %}
