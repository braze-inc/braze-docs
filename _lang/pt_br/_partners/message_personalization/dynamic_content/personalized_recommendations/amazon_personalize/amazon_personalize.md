---
nav_title: Amazon Personalize
article_title: Amazon Personalize
alias: "/partners/amazon_personalize_overview/"
description: "Este artigo de referência descreve uma arquitetura de referência e a integração entre o Braze e o Amazon Personalize. Este artigo de referência o ajudará a entender os casos de uso que o Amazon Personalize oferece, os dados com os quais ele trabalha, como configurar o serviço e como integrá-lo ao Braze."
page_type: partner
search_tag: Partner
---

# Amazon Personalize
<!--
{% multi_lang_include video.html id="xFZ3HMleYYE" align="right" %}
-->
> O Amazon Personalize é como ter seu próprio sistema de recomendação de machine learning da Amazon o dia todo. Com base em mais de 20 anos de experiência em recomendações, o Amazon Personalize o capacita a melhorar o engajamento dos clientes, fornecendo recomendações personalizadas de produtos e conteúdo em tempo real e promoções de marketing direcionadas.

_Essa integração é mantida pela Amazon Personalize._

## Sobre a integração

Usando machine learning e um algoritmo que você ajuda a definir, o Amazon Personalize pode ajudá-lo a treinar um modelo que produz recomendações de alta qualidade para seus sites e aplicativos. Esses modelos permitirão que você crie listas de recomendações com base nos comportamentos anteriores dos usuários, classifique itens por relevância e recomende outros itens com base na similaridade. As listas obtidas da Amazon Personalize API podem ser usadas no Braze Connected Content para executar campanhas de recomendação personalizadas do Braze. Ao integrar-se ao Amazon Personalize, os clientes têm a liberdade de controlar os parâmetros usados para treinar os modelos e definir objetivos comerciais opcionais que otimizam o resultado do algoritmo. 

Este artigo de referência o ajudará a entender os casos de uso que o Amazon Personalize oferece, os dados com os quais ele trabalha, como configurar o serviço e como integrá-lo ao Braze.

## Pré-requisitos

| Requisito| Descrição|
| ---| ---| 
| Conta do Amazon Web Service | É necessário ter uma conta da AWS para aproveitar essa parceria. Depois de ter uma conta da AWS, você pode acessar o Amazon Personalize por meio do console do Amazon Personalize, da AWS Command Line Interface (AWS CLI) ou dos SDKs da AWS. |
| Casos de uso definidos | Antes de criar um modelo, determine seu caso de uso para essa integração. Consulte a lista a seguir para ver os casos de uso comuns. |
| Conjuntos de dados | Os modelos de recomendação do Amazon Personalize requerem três tipos diferentes de conjuntos de dados: interações, usuários e itens. Consulte os detalhes a seguir para ver os requisitos de cada conjunto de dados. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% tabs %}
{% tab Casos de uso %}

**Casos de uso**

Antes de criar um modelo, determine seu caso de uso para essa integração. Alguns casos de uso comuns incluem:
- Recomende itens para os usuários com base em suas interações anteriores, criando uma experiência verdadeiramente personalizada para seus usuários.
- Forneça uma lista de itens ou resultados de pesquisa personalizados para cada usuário, aumentando o engajamento ao mostrar itens por relevância para o usuário.
- Encontre recomendações de itens semelhantes, ajudando os usuários a descobrir coisas novas.

No guia a seguir, vamos nos concentrar na receita de recomendações personalizadas do usuário.

{% endtab %}
{% tab Conjuntos de dados %}

**Conjuntos de dados**

Para começar a usar os modelos de recomendação do Amazon Personalize, você precisa de três tipos de conjuntos de dados:

- Interações
  - Armazena o histórico de interações entre usuários e itens
  - Requer os valores `USER_ID`, `ITEM_ID`, `EVENT_TYPE` e `TIMESTAMP` e, opcionalmente, aceita metadados sobre o evento
- Usuários
  - Armazena metadados sobre os usuários
  - Requer um valor `USER_ID` e pelo menos um campo de metadados (string ou numérico), como gênero, idade e inscrição com fidelidade
- Itens
  - Armazena metadados sobre itens
  - Requer um `ITEM_ID` e pelo menos um campo de metadados (textual, categórico ou numérico) que descreva o item

Para uma receita de recomendações de usuários, é necessário fornecer um conjunto de dados de interações contendo pelo menos 1.000 pontos de dados de interação de pelo menos 25 usuários exclusivos com pelo menos duas interações cada. Esses conjuntos de dados podem ser enviados por upload em massa usando arquivos CSV armazenados no S3 ou de forma incremental por meio da API.

{% endtab %}
{% endtabs %}

## Criação de modelos

### Etapa 1: Em treinamento

Depois que os conjuntos de dados forem importados, você poderá criar uma solução. Uma solução usa uma das [receitas](https://docs.aws.amazon.com/personalize/latest/dg/working-with-predefined-recipes.html) (algoritmos) do Amazon Personalize para treinar um modelo. Em nosso caso, usaremos a receita do site `USER_PERSONALIZATION`. O treinamento da solução cria uma versão da solução (modelo treinado) que você pode avaliar com base nas métricas de performance do modelo.

O Amazon Personalize permite que você ajuste os hiperparâmetros que o modelo usa para treinamento. Por exemplo:
- O parâmetro "User history length percentile" (Percentil de comprimento do histórico do usuário) encontrado no console do Amazon Personalize permite ajustar o percentil do histórico do usuário a ser incluído no treinamento:<br><br>![Configuração mínima e máxima do perfil do usuário]({% image_buster /assets/img/amazon_personalize/min_and_max_user_percentile.png %})
  - `min_user_history_length_percentile`exclui uma porcentagem de usuários com históricos muito curtos, o que pode ser útil para eliminar itens populares e criar recomendações com base em padrões subjacentes mais profundos.
  - `max_user_history_length_percentile`: ajusta a porcentagem de usuários a ser levada em conta no treinamento com durações de histórico muito longas.

O número de dimensões ocultas ajuda a detectar padrões mais complicados para conjuntos de dados complexos, enquanto a técnica de retropropagação ao longo do tempo (BPTT) ajusta as recompensas para um evento inicial após a ocorrência de uma cadeia de eventos que resultou em uma ação de alto valor.

Além disso, o Amazon Personalize oferece ajuste automático de hiperparâmetros, executando várias versões da solução com valores diferentes simultaneamente. Para usar o ajuste, ative **Perform HPO** (Executar HPO) ao criar uma solução.

### Etapa 2: Avaliar e comparar

Quando o treinamento da solução fica pronto, você pode avaliá-la e comparar as diferentes versões. Cada versão da solução exibe métricas computadas. Algumas das métricas disponíveis incluem:

- **Normalizar o ganho cumulativo descontado:** compara a ordem recomendada dos itens com a lista real de itens e atribui a cada item um peso correspondente à sua posição na lista
- **Precisão @k:** a quantidade de itens recomendados corretamente dividida pela quantidade de todos os itens recomendados, em que `k` é o número de itens
- **Classificação recíproca média:** concentra-se na primeira recomendação com classificação mais alta e calcula quantos itens recomendados são vistos antes que a primeira recomendação correspondente apareça
- **Cobertura:** a proporção de itens recomendados exclusivos em relação ao número total de itens exclusivos no conjunto de dados

## Como obter recomendações

Depois de criar uma versão da solução que o satisfaça, é hora de colocar as recomendações em prática. Há duas maneiras de acessar as recomendações:

1. Campanha em tempo real<br>Uma campanha é uma versão de solução implementada com uma taxa de transferência de transação mínima definida. Uma transação é uma única chamada à API para obter uma saída de recomendação e é definida como TPS, ou transações por segundo, com um valor mínimo de um. A campanha dimensionará os recursos em caso de aumento de carga, mas não cairá abaixo de seu valor mínimo. É possível consultar as recomendações no console, na CLI da AWS ou por meio dos SDKs da AWS no seu código.<br><br>
2. Trabalho em lote<br>Um trabalho em lote exporta as recomendações para um bucket S3. O trabalho recebe uma entrada de um arquivo JSON com uma lista de IDs de usuário para os quais você deseja exportar as recomendações. Em seguida, depois de especificar as permissões corretas e o destino de saída, você poderá para executar o trabalho. O tempo de execução depende do tamanho de seus conjuntos de dados e do tamanho da lista de recomendações.

### Filtros

Os filtros permitem que você ajuste o resultado da recomendação excluindo itens com base na ID do item, no tipo de evento ou nos metadados. Também é possível filtrar usuários com base em seus metadados, como idade ou status de inscrição com fidelidade. Os filtros podem ser úteis para evitar a recomendação de itens com os quais o usuário já tenha interagido.

## Integração de resultados com o Braze

Com o modelo criado e a campanha de recomendações, você está pronto para executar uma campanha do Braze para seus usuários usando cartões de conteúdo e Connected Content.
Antes de executar uma campanha no Braze, você deve criar um serviço que possa atender a essas recomendações por meio de uma API. Você pode seguir a [etapa 3 do artigo do workshop]({{site.baseurl}}/partners/amazon_personalize_workshop/#step-3-send-personalized-emails-from-braze) para implantar o serviço usando os serviços da AWS. Você também pode implantar seu próprio serviço de backend independente que fornece as recomendações.

### Caso de uso da campanha do cartão de conteúdo

Vamos executar uma campanha de cartão de conteúdo com o primeiro item recomendado da lista.<br><br>
Nos exemplos a seguir, vamos consultar
Endpoint `GET http://<service-endpoint.com>/recommendations?user_id=user123` com um parâmetro `user_id` que retornará uma lista de itens recomendados:

```json
[
  {
    "id": "abc123",
    "url": "http://productpage.com/product/abc123",
    "name": "First Item",
    "price": 39.99,
    "image": "http://pp.cdn.com/abvh3321pjb1j"
  },
  {
    "id": "xyz987",
    "url": "http://productpage.com/product/xyz987",
    "name": "Great Item",
    "price": 19.99,
    "image": "http://pp.cdn.com/234bjl1gioj1b2b"
  },
  ...
]
```

No dashboard da Braze, crie uma nova [campanha de cartão de conteúdo]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/). No campo de texto da mensagem, crie um bloco do Liquid de conteúdo conectado para consultar a API e salvar a resposta na variável `recommendations`:

{% raw %}

```liquid
{% connected_content https:/<service-endpoint.com>/recommendations?user_id={{${user_id}}} :save recommendations %}
```

Em seguida, é possível fazer referência ao primeiro item da matriz resultante e exibir o conteúdo para o usuário:

```liquid
This seems like a great fit for you:
{% recommendations[0].name %}
{% recommendations[0].price %}
```

{% endraw %}

Incluindo o título, a imagem e o link para o URL, é assim que o cartão de conteúdo completo ficaria:

![Uma imagem de uma campanha com conteúdo conectado adicionada ao corpo da mensagem e ao campo "Adicionar imagem". Essa imagem também mostra a lógica do Connected Content adicionada ao campo "Redirect to Web URL", vinculando os usuários a um URL de recomendação.]({% image_buster /assets/img/amazon_personalize/content-card-campaign.png %})


