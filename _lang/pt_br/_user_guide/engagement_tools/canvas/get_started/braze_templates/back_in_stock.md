---
nav_title: Voltar ao estoque
article_title: De volta ao estoque
page_order: 2
page_type: reference
description: "Este artigo descreve como usar um modelo do Braze Canvas para impulsionar as compras, notificando seus usuários quando um item estiver de volta ao estoque com mensagens personalizadas."
tool: Canvas
---

# Voltar ao estoque

> Use o modelo "back-in-stock" para criar mensagens direcionadas aos usuários que visualizaram anteriormente ou expressaram interesse em um item que estava fora de estoque, mas agora está disponível para compra. Isso ajuda os usuários a obter os produtos que desejam, envolvendo-os no momento crítico em que um produto volta a estar disponível.

Este artigo o guiará por um caso de uso do modelo **Back In Stock**, que foi projetado para a etapa de conversão do ciclo de vida do usuário. Quando terminar, você terá criado um Canvas que envia um push (Web ou celular), SMS ou e-mail aos usuários quando um item estiver de volta ao estoque e até dois lembretes.

## Pré-requisitos

Para usar esse modelo com sucesso, você precisará do seguinte:

- Um [catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog) contendo informações sobre seu item
- [As notificações de falta de estoque]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications/#how-back-in-stock-notifications-work) devem ser configuradas para o item sobre o qual você deseja enviar mensagens aos usuários

## Adaptar o modelo às suas necessidades

Digamos que estejamos trabalhando para a PantsLabyrinth, uma varejista de roupas direta ao consumidor, especializada em calças, jeans, culotes e muitos outros tipos de calças. Podemos usar o modelo de volta ao estoque para notificar os clientes em vários canais quando um par de jeans popular, o Classic Straight Leg, estiver de volta ao estoque.

Antes de criar o Canvas, configuramos [um catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog) que contém informações sobre nosso estoque de calças de perna reta e configuramos [notificações de falta de estoque]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications/#setting-up-back-in-stock-notifications) para o jeans Classic Straight Leg. Fizemos com que os usuários se inscrevessem para receber notificações após realizarem o evento personalizado de favoritar o jeans Classic Straight Leg no aplicativo.

Para acessar o modelo em estoque, ao criar um novo Canvas, selecione **Usar um modelo de Canvas** > **Modelos de brasagem**. Em seguida, ao lado de **Back in Stock**, selecione **Apply Template (Aplicar modelo**). Agora, podemos examinar o modelo para adequá-lo às nossas necessidades.

### Etapa 1: Configurar os detalhes

Vamos ajustar os detalhes do Canvas para refletir nosso objetivo.

1. Selecione **Editar** ao lado do nome do modelo.

\![O título e a descrição atuais do Canvas.]({% image_buster /assets/img/canvas_templates/back_in_stock_old_name_description.png %}){: style="max-width:45%;"}

{:start="2"}
2\. Atualize o nome do Canvas para especificar que o Canvas é para direcionar os usuários quando nosso produto Classic Straight Leg estiver novamente em estoque.
3\. Atualize a descrição para explicar que esse Canvas contém mensagens personalizadas.
4\. Adicione a tag **Back in Stock**, que está aninhada sob a tag **Promotional**, para que possamos filtrá-la na página inicial do Canvas. 

\!["Set Up Canvas Details" com um nome de tela "Back in Stock - Classic Straight Leg" e uma breve descrição da tela.]({% image_buster /assets/img/canvas_templates/back_in_stock_1.png %})

### Etapa 2: Atribuir eventos de conversão

Altere o **evento de conversão primário - A** para **Make a specific purchase (Fazer uma compra específica** ) e selecione **Classic Straight Leg (Perna reta clássica** ) para o nome do produto.

\!["Atribuir eventos de conversão" para o tipo de evento de conversão de compra do produto Classic Straight Leg com um prazo de conversão de 7 dias.]({% image_buster /assets/img/canvas_templates/back_in_stock_2.png %})

### Etapa 3: Adaptar o cronograma de entrada

Vamos manter o cronograma de entrada como **Action-Based** para que os usuários entrem em nosso Canvas quando executarem uma ação, que o modelo já definiu como **Perform a Back in Stock Event**.

Faremos dois ajustes nessa etapa:

1. Selecione o catálogo que inclui informações sobre nossos jeans Classic Straight Leg, que chamamos de "Straight Leg Pants". 

Etapa "Entry Schedule" para um Canvas baseado em ações.]({% image_buster /assets/img/canvas_templates/back_in_stock_3.png %})

{: start="2"}
2\. Defina a **Hora de início (obrigatório)** para a data e hora de início desejadas.

Seção "Janela de entrada" com horário de início em 2 de janeiro de 2025 às 12 horas.]({% image_buster /assets/img/canvas_templates/back_in_stock_4.png %})

### Etapa 4: Selecione o público-alvo

Definiremos nosso público-alvo como usuários que, em nossa opinião, têm maior probabilidade de comprar o jeans Classic Straight Leg.

1. Selecione nosso segmento-alvo, "Favorited - Classic Straight Leg Jeans", que consiste em usuários que favoritaram nosso jeans Classic Straight Leg em nosso aplicativo ou site.
2. Selecione um filtro para incluir usuários que compraram "Jeans" mais de "0" vezes.

\!["Target Audience" com o segmento "Favorited - Classic Straight Leg Jeans".]({% image_buster /assets/img/canvas_templates/back_in_stock_5.png %})

{: start="3"}
3\. Ajuste os controles de entrada para permitir que os usuários entrem novamente no Canvas após a duração máxima do Canvas, para evitar a probabilidade de os usuários acionarem a mesma etapa simultaneamente.

\!["Controles de entrada" com uma caixa de seleção para permitir que os usuários entrem novamente nesse Canvas com uma duração máxima do Canvas.]({% image_buster /assets/img/canvas_templates/back_in_stock_6.png %})

{: start="4"}
4\. Ajuste os critérios de saída para remover os usuários que realizaram o evento personalizado de desfavorecimento do jeans Classic Straight Leg.

\!["Critérios de saída" com uma exceção para os usuários que realizam o evento personalizado de "Desfavorecido".]({% image_buster /assets/img/canvas_templates/back_in_stock_7.png %})

### Etapa 5: Selecione suas configurações de envio

Manteremos as configurações de assinatura padrão, para que enviemos apenas aos usuários que se inscreveram ou optaram por receber mensagens ou notificações, e ignoraremos as outras configurações (limite de frequência, horas de silêncio e grupos de sementes).

\!["Send Settings" (Configurações de envio), visando os usuários que estão inscritos ou optaram por participar.]({% image_buster /assets/img/canvas_templates/back_in_stock_8.png %})

### Etapa 6: Personalize seu Canvas

Agora, criaremos nosso Canvas personalizando os canais e o conteúdo que serão enviados aos usuários. Como estamos usando todos os quatro canais de modelo (push para celular e web, SMS e e-mail) e usando o filtro [Intelligent Channel]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_channel/), não precisamos adicionar ou remover nenhum.

{% alert tip %}
Você pode usar [as propriedades de entrada do Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/) para personalizar as mensagens no seu Canvas com base no produto ao qual você está se referindo.
{% endalert %}

Começaremos nossa personalização percorrendo cada etapa da mensagem para atualizar o conteúdo.

1. Substitua `!!YOURCATALOGHERE!!` pelo nome do nosso catálogo (“Straight_Leg_Pants”).
2. Substitua `[0]` pelo número de índice do jeans Classic Straight Leg, que é "9", porque o jeans é o décimo item na matriz `items` do nosso catálogo. (As matrizes são indexadas a zero no Liquid, portanto, o primeiro item é `0` e não `1`.)
3. Repita as etapas 1 e 2 para todas as etapas restantes da Mensagem, inclusive:
    - A mensagem "In-Product Msg & Email" que é enviada após o atraso de um dia
    - As mensagens "Push+Email Alert" que são enviadas aos usuários que não fizeram uma compra
4. Atualize a etapa Caminhos de ação selecionando o grupo de ação **Comprar**. Em seguida, selecione **Fazer uma compra específica** e escolha o jeans Classic Straight Leg como produto.

Etapa do Mobile Push Canvas com uma mensagem notificando os usuários de que um produto está de volta ao estoque.]({% image_buster /assets/img/canvas_templates/back_in_stock_9.png %})

### Etapa 7: Teste e inicie seu Canvas

Depois de testar e revisar nosso Canvas para garantir que ele funcione conforme o esperado, nós o iniciaremos selecionando **Launch Canvas**. Agora, nossos usuários que favoritaram nosso jeans Classic Straight Leg e se inscreveram em nossos canais de mensagens receberão notificações quando ele estiver novamente em estoque!

{% alert tip %}
Confira nossa [lista de verificação pré e pós-lançamento]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) para saber o que considerar antes e depois de lançar um Canvas.
{% endalert %}

