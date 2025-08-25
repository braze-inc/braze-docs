---
nav_title: Recomendações de IA
article_title: Criação de recomendações de itens de IA
description: "Este artigo de referência aborda como criar uma recomendação de item IA para itens em um catálogo."
page_order: 1
---

# Criação de recomendações de itens de IA

> Saiba como criar um mecanismo de recomendação de IA a partir de itens em seu catálogo.

## Sobre as recomendações de itens de IA

Use as recomendações de itens de IA para calcular os produtos mais populares ou crie recomendações de IA personalizadas para um [catálogo]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/) específico. Depois de criar sua recomendação, você pode usar a personalização para inserir esses produtos em suas mensagens.

{% alert tip %}
[As recomendações personalizadas por IA](#recommendation-types) funcionam melhor com centenas ou milhares de itens e, normalmente, com pelo menos 30.000 usuários com dados de compra ou interação. Esse é apenas um guia aproximado e pode variar. Os outros tipos de recomendação podem trabalhar com menos dados.
{% endalert %}

## Criação de uma recomendação de item de IA

### Pré-requisitos

Antes de começar, você precisará concluir o seguinte:

- Você deve ter pelo menos um [catálogo]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/) para usar qualquer um dos tipos de recomendação descritos abaixo.
- Você deve ter dados de compra ou de evento no Braze (eventos personalizados ou o objeto de compra) que incluam uma referência a IDs de produtos exclusivos armazenados em um catálogo.

### Etapa 1: Criar uma nova recomendação

Você pode criar uma recomendação de item de IA em qualquer lugar do dashboard:

{% tabs local %}
{% tab No menu de navegação %}
1. Acesse **Análise de** dados > **Recomendação de item de IA**.
2. Selecione **Criar previsão** > **Recomendação de item IA**.
{% endtab %}

{% tab De um catálogo %}
Você também pode optar por criar uma recomendação diretamente de um catálogo individual. Selecione seu catálogo na página **Catálogos** e, em seguida, selecione **Criar recomendação**.
{% endtab %}
{% endtabs %}

### Etapa 2: Adicionar detalhes da recomendação

Dê um nome e uma descrição opcional à sua recomendação.

![Etapa "Detalhes da recomendação" com os campos de nome e descrição.]({% image_buster /assets/img/item_recs_1.png %})

### Etapa 3: Defina sua recomendação {#recommendation-type}

Selecione um tipo de recomendação. Cada tipo usa os últimos seis meses de dados de interação do item, como uma compra ou dados de eventos personalizados. Para saber mais sobre informações detalhadas e casos de uso de cada um, consulte [Tipos e casos de uso]({{site.baseurl}}/user_guide/brazeai/recommendations/).

{% alert tip %}
Ao usar **Mais recentes** ou **IA personalizada**, os usuários com dados insuficientes para criar recomendações individualizadas receberão itens **mais populares** como fallback. A proporção de usuários que recebem o fallback **Mais popular** é exibida na página **Análise de dados**.
{% endalert %}

#### Etapa 3.1: Excluir compras ou interações anteriores (opcional)

Para evitar sugerir itens que um usuário já tenha comprado ou com os quais já tenha interagido, selecione **Não recomendar itens com os quais os usuários tenham interagido anteriormente**. Essa opção só está disponível quando o **Tipo** de recomendação está definido como **IA Personalizado**.

![Etapa "Defina sua recomendação" com "IA Personalizada" como o tipo e a opção "Não recomendar itens com os quais os usuários interagiram anteriormente" selecionada.]({% image_buster /assets/img/item_recs_2-3.png %})

Essa configuração impede que as mensagens reutilizem os itens que um usuário já comprou ou com os quais interagiu, desde que a recomendação tenha sido atualizada recentemente. Os itens comprados ou com os quais houve interação entre as atualizações de recomendação ainda podem aparecer. Na versão gratuita das recomendações de itens, as atualizações ocorrem semanalmente. Para a versão profissional das recomendações de itens de IA, as atualizações ocorrem a cada 24 horas.

Por exemplo, ao usar a versão pro das recomendações de itens IA, se um usuário comprar algo e receber um e-mail de marketing em 30 minutos, o item que acabou de comprar poderá não ser excluído do e-mail a tempo. No entanto, as mensagens enviadas após 24 horas não incluirão esse item.

#### Etapa 3.2: Selecione um catálogo

Se ainda não estiver preenchido, selecione o [catálogo]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/) do qual essa recomendação extrairá itens.

#### Etapa 3.3: Adicionar uma seleção (opcional)

Se quiser ter mais controle sobre sua recomendação, escolha uma [seleção]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections/) para aplicar filtros personalizados. As seleções filtram as recomendações por colunas específicas em seu catálogo, como marca, tamanho ou local. As seleções que contêm Liquid não podem ser usadas em sua recomendação.

![Um exemplo da seleção "em estoque" selecionada para a recomendação.]({% image_buster /assets/img/item_recs_2-2.png %})

{% alert tip %}
Caso não encontre sua seleção, lembre-se de que é preciso criá-la primeiro.
{% endalert %}

### Etapa 4: Selecione a interação para conduzir as recomendações

Selecione o evento para o qual você deseja que essa recomendação seja otimizada. Esse evento geralmente é uma compra, mas também pode ser qualquer interação com um item.

Você pode otimizar para:

- Eventos de compra com o [objeto Purchase]({{site.baseurl}}/api/objects_filters/purchase_object/)
- Eventos personalizados que representam uma compra
- Eventos personalizados que representam qualquer outra interação de item (como visualizações de produtos, cliques ou reproduções de mídia)

Se você escolher **Evento personalizado**, selecione seu evento na lista.

![O evento personalizado "Compra concluída" selecionado como a forma como os eventos são rastreados atualmente.]({% image_buster /assets/img/item_recs_3.png %})

### Etapa 5: Selecione o nome da propriedade correspondente {#property-name}

Para criar uma recomendação, você precisa informar ao Braze qual campo do seu evento de interação (objeto de compra ou evento personalizado) tem o identificador exclusivo que corresponde ao campo `id` de um item no catálogo. Não tem certeza? [Visualizar requisitos](#requirements).

Selecione esse campo para o **Nome da propriedade**.

O campo **Property Name (Nome da propriedade** ) será preenchido previamente com uma lista de campos enviados pelo SDK à Braze. Se forem fornecidos dados suficientes, essas propriedades também serão classificadas em ordem de probabilidade de serem a propriedade correta. Selecione a opção que corresponde ao campo `id` do catálogo.

![O nome da propriedade "purchase_item" selecionada que corresponde aos IDs de item no catálogo.]({% image_buster /assets/img/item_recs_4.png %})

#### Requisitos {#requirements}

Há alguns requisitos para selecionar sua propriedade:

- Deve ser mapeado para o campo `id` de seu catálogo selecionado.
- **Se você selecionou Objeto de compra:** Deve ser o `product_id` ou um campo do evento de interação `properties`.
- **Se você selecionou Evento personalizado:** Deve ser um campo de seu evento personalizado `properties`.
- Os campos aninhados devem ser digitados no menu suspenso **Nome da propriedade** em notação de ponto com o formato `event_property.nested_property`. Por exemplo, se estiver selecionando a propriedade aninhada `district_name` dentro da propriedade de evento `location`, você digitará `location.district_name`.
- O campo pode estar dentro de uma matriz de produtos ou terminar com uma matriz de IDs. Em ambos os casos, cada ID de produto será tratada como um evento separado e sequencial com o mesmo registro de data e hora.

#### Exemplos de mapeamentos

Os exemplos de mapeamentos a seguir referem-se a esse catálogo de amostra:

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;font-size: 14px; font-weight: bold; background-color: #f4f4f7; text-transform: lowercase; color: #212123; font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top;word-break:normal}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky">id</th>
    <th class="tg-0pky">título</th>
    <th class="tg-0pky">preço</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">ADI-BL-7</td>
    <td class="tg-0pky">Adidas Preto Tamanho 7</td>
    <td class="tg-0pky">100,00 USD</td>
  </tr>
  <tr>
    <td class="tg-0pky">ADI-RD-8</td>
    <td class="tg-0pky">Adidas Vermelho Tamanho 8</td>
    <td class="tg-0pky">100,00 USD</td>
  </tr>
  <tr>
    <td class="tg-0pky">ADI-WH-9</td>
    <td class="tg-0pky">Adidas Branco Tamanho 9</td>
    <td class="tg-0pky">100,00 USD</td>
  </tr>
  <tr>
    <td class="tg-0pky">ADI-PP-10</td>
    <td class="tg-0pky">Adidas Roxo Tamanho 10</td>
    <td class="tg-0pky">75,00 USD</td>
  </tr>
</tbody>
</table>

{% tabs %}
{% tab Evento personalizado %}

Digamos que você queira usar o evento personalizado `added_to_cart` para poder recomendar produtos semelhantes antes que o cliente faça o check-out. O evento `added_to_cart` tem uma propriedade de evento de `product_sku`.

Então, a propriedade `product_sku` deve incluir pelo menos um dos valores da coluna `id` no catálogo de amostras: "ADI-BL-7", "ADI-RD-8", "ADI-WH-9" ou "ADI-PP-10". Você não precisa de eventos para cada item do catálogo, mas precisa de alguns deles para que o mecanismo de recomendação tenha conteúdo suficiente para trabalhar.

##### Exemplo de objeto de evento personalizado

Esse evento tem o endereço `"product_sku": "ADI-BL-7"`, que corresponde ao primeiro item do catálogo de amostras.

```json
{
  "events": [
    {
      "external_id": "user1",
      "app_id": "your-app-id",
      "name": "added_to_cart",
      "time": "2024-07-16T19:20:30+01:00",
      "properties": {
        "product_sku": "ADI-BL-7"
      }
    }
  ]
}
```

##### Exemplo de objeto de evento personalizado com um vetor de produtos

Se as propriedades do evento contiverem vários produtos em uma matriz, cada ID de produto será tratada como um evento separado e sequencial. Esse evento pode usar a propriedade `products.sku` para corresponder ao primeiro e ao terceiro itens do catálogo de amostra.

```json
{
  "events": [
    {
      "external_id": "user1",
      "app_id": "your-app-id",
      "name": "added_to_cart",
      "time": "2024-07-16T19:20:30+01:00",
      "properties": {
        "transaction_id": "2ff3f9a9-8803-4c3a-91da-14adbf93dc99",
        "products": [
          { "sku": "ADI-BL-7" },
          { "sku": "ADI-WH-9" }
        ]
      }
    }
  ]
}
```

##### Exemplo de objeto de evento personalizado com um objeto aninhado contendo um vetor de objeto de ID de produto

Se as IDs de seus produtos forem valores em um vetor em vez de objetos, você poderá usar a mesma notação e cada ID de produto será tratada como um evento separado e sequencial. Isso pode ser combinado de forma flexível com objetos aninhados no evento a seguir, configurando a propriedade como `purchase.product_skus` para corresponder ao primeiro e ao terceiro itens no catálogo de amostra.

```json
{
  "events": [
    {
      "external_id": "user1",
      "app_id": "your-app-id",
      "name": "added_to_cart",
      "time": "2024-07-16T19:20:30+01:00",
      "properties": {
        "transaction_id": "13791e08-7c22-4f6c-8cc6-832c76af3743",
        "purchase": {
          "product_skus": ["ADI-BL-7", "ADI-WH-9"]
        }
      }
    }
  ]
}
```

{% endtab %}
{% tab Objeto de compra %}

Um objeto de compra é passado pela API quando uma compra é feita.

Em termos de mapeamento, aplica-se uma lógica semelhante aos objetos de compra e aos eventos personalizados, exceto que você pode escolher entre usar o objeto de compra `product_id` ou um campo no objeto `properties`.

Lembre-se de que você não precisa de eventos para cada item do catálogo, mas precisa de alguns deles para que o mecanismo de recomendação tenha conteúdo suficiente para trabalhar.

##### Exemplo de objeto de compra mapeado para o ID do produto

Esse evento tem o endereço `"product_id": "ADI-BL-7`, que mapeia o primeiro item do catálogo.

```json
{
  "purchases": [
    {
      "external_id": "user1",
      "app_id": "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id": "ADI-BL-7",
      "currency": "USD",
      "price": 100.00,
      "time": "2024-07-16T19:20:30+01:00",
      "properties": {
        "color": "black",
        "checkout_duration": 180,
        "size": "7",
        "brand": "Adidas"
      }
    }
  ]
}
```

##### Exemplo de objeto de compra mapeado para um campo de propriedades

Esse evento tem uma propriedade de `"sku": "ADI-RD-8"`, que mapeia o segundo item do catálogo.

```json
{
  "purchases": [
    {
      "external_id": "user1",
      "app_id": "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id": "shoes",
      "currency": "USD",
      "price": 100.00,
      "time": "2024-07-16T19:20:30+01:00",
      "properties": {
        "sku": "ADI-RD-8",
        "color": "red",
        "checkout_duration": 180,
        "size": "8",
        "brand": "Adidas"
      }
    }
  ]
}
```

{% endtab %}
{% endtabs %}

### Etapa 6: Treinar a recomendação

Quando estiver pronto, selecione **Criar recomendação**. Esse processo pode levar de 10 minutos a 36 horas para ser concluído. Você receberá uma atualização por e-mail quando a recomendação for treinada com sucesso ou uma explicação do motivo pelo qual a criação pode ter falhado.

Você pode encontrar a recomendação na página **Previsões**, onde poderá editá-la ou arquivá-la conforme necessário. As recomendações serão treinadas automaticamente uma vez por semana (pago) ou por mês (gratuito).

## Recursos específicos do plano

A tabela a seguir descreve as diferenças entre a versão gratuita e a versão profissional dos tipos de recomendação IA Personalized, Popular e Trending:

| Área                   | Versão gratuita                          | Versão Pro            |
| :---------------------- | ------------------------------------- | :--------------------------------------- |
| <sup>Frequência</sup> de atualização do usuário1   | Semanalmente                                | Diariamente                                    |
| Frequência de retreinamento do modelo  | Mensalmente                               | Semanalmente                                   |
| Modelos de recomendação máxima | 1 modelo por <sup>tipo2</sup> | 100 modelos por <sup>tipo2</sup> |

<sup>1\. Essa é a frequência com que as recomendações de itens específicos do usuário são atualizadas (todos os modelos, exceto os itens Mais populares, que são atualizados quando o modelo é retreinado). Por exemplo, se um usuário comprar um item recomendado com base nas recomendações de itens da IA, seus itens recomendados serão atualizados de acordo com essa frequência</sup><br>
<sup>2\. Os tipos de recomendação disponíveis são IA Personalizada, Mais recente, Mais popular e Tendências.</sup>

## Perguntas frequentes (FAQ) {#faq}

### O que faz com que os itens "Mais populares" sejam misturados às recomendações de outros modelos?

Quando nosso mecanismo de recomendação faz a curadoria de uma lista para você, ele primeiro prioriza as seleções personalizadas com base no modelo específico que você escolheu, como "Mais recente" ou "IA Personalizado". Se esse modelo não puder preencher a lista completa de 30 recomendações por qualquer motivo, alguns dos itens mais populares entre todos os usuários serão adicionados para garantir que cada usuário sempre tenha um conjunto completo de recomendações.

Isso acontece em algumas condições específicas:

- O modelo encontra menos de 30 itens que correspondem aos seus critérios.
- Os itens relevantes não estão mais disponíveis ou em estoque.
- Os itens não atendem aos critérios de seleção atuais, talvez devido a uma alteração no estoque ou nas preferências do usuário.

### As recomendações existentes treinam semanalmente após a atualização para Item Recommendations Pro?

Sim, mas somente após a próxima atualização programada. As recomendações existentes não mudam para treinamento semanal e previsão diária imediatamente após o upgrade para o Item Recommendations Pro. No entanto, eles adotarão o novo cronograma automaticamente em seu próximo ciclo de retreinamento. Por exemplo, se uma recomendação foi treinada pela última vez em 1º de fevereiro e está definida para ser treinada novamente a cada 30 dias, ela adotará a nova programação semanal após a próxima atualização em 2 de março.
