---
nav_title: De volta ao estoque
article_title: De volta ao estoque
page_order: 2
page_type: reference
description: "Este artigo descreve como usar um modelo do Braze Canvas para impulsionar as compras, notificando seus usuários quando um item estiver de volta ao estoque com envio de mensagens personalizadas."
tool: Canvas
---

# De volta ao estoque

> Use o modelo "back-in-stock" para criar mensagens direcionadas aos usuários que visualizaram anteriormente ou expressaram interesse em um item que estava fora de estoque, mas que agora está disponível para compra. Isso ajuda os usuários a obter os produtos que desejam por meio do engajamento no momento crítico em que um produto volta a estar disponível.

Este artigo o guiará por um caso de uso do modelo **Back In Stock**, que foi projetado para a etapa de conversão do ciclo de vida do usuário. Quando terminar, você terá criado um Canva que envia um push (web ou mobile), SMS ou e-mail aos usuários quando um item estiver de volta ao estoque e até dois lembretes.

## Pré-requisitos

Para usar esse modelo com sucesso, você precisará do seguinte:

- Um [catálogo]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog) com informações sobre seu item
- As [notificações de falta de estoque]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog_triggers/back_in_stock_notifications/#how-back-in-stock-notifications-work) devem ser configuradas para o item sobre o qual deseja enviar mensagens aos usuários

## Adaptar o modelo às suas necessidades

Digamos que estejamos trabalhando para a PantsLabyrinth, uma varejista de roupas direto ao consumidor, especializada em slacks, jeans, culotes e muitos outros tipos de calças. Podemos usar o modelo de volta ao estoque para notificar os clientes em vários canais quando um par de jeans popular, o Classic Straight Leg, estiver de volta ao estoque.

Antes de criar o Canva, configuramos um [catálogo]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog) que contém informações sobre nosso estoque de calças de perna reta e configuramos [notificações de falta de estoque]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog_triggers/back_in_stock_notifications/#setting-up-back-in-stock-notifications) para o jeans Classic Straight Leg. Fizemos com que os usuários se inscrevessem para receber notificações depois de realizar o evento personalizado de favoritar o jeans Classic Straight Leg no app.

Para acessar o modelo em estoque, ao criar um novo Canvas, selecione **Usar um modelo de Canvas** > **Modelos de Braze**. Em seguida, ao lado de **Back in Stock**, selecione **Apply Template (Aplicar modelo)**. Agora, podemos examinar o modelo para adequá-lo às nossas necessidades.

### Etapa 1: Configurar os detalhes

Vamos ajustar os detalhes do Canva para refletir nosso objetivo.

1. Selecione **Editar** ao lado do nome do modelo.

![O título e a descrição atuais do Canva.]({% image_buster /assets/img/canvas_templates/back_in_stock_old_name_description.png %}){: style="max-width:45%;"}

{:start="2"}
2\. Atualize o nome do Canvas para especificar que o Canvas é para direcionamento de usuários quando nosso produto Classic Straight Leg estiver de volta ao estoque.
3\. Atualize a descrição para explicar que esse Canva contém envio de mensagens personalizadas.
4\. Adicione a tag **Back in Stock**, que está aninhada sob a tag **Promotional**, para que possamos filtrá-la na página inicial do Canva. 

!["Configurar Detalhes do Canva" etapa com um nome de Canva de "De Volta em Estoque - Perna Reta Clássica" e uma breve descrição do Canva.]({% image_buster /assets/img/canvas_templates/back_in_stock_1.png %})

### Etapa 2: Atribuir eventos de conversão

Altere o **evento de conversão primária - A** para **Make a specific purchase (Fazer uma compra específica)** e selecione **Classic Straight Leg (Perna reta clássica)** como o nome do produto.

!["Atribuir Eventos de Conversão" seção para o tipo de evento de conversão de compra do produto Perna Reta Clássica com um prazo de conversão de 7 dias.]({% image_buster /assets/img/canvas_templates/back_in_stock_2.png %})

### Etapa 3: Adaptar o cronograma de entrada

Vamos manter o cronograma de entrada como **Baseado em ação** para que os usuários entrem em nosso Canva quando executarem uma ação, que o modelo já definiu como **Executar um evento de retorno ao estoque**.

Faremos dois ajustes nesta etapa:

1. Selecione o catálogo que inclui informações sobre nossos jeans Classic Straight Leg, que chamamos de "Straight Leg Pants". 

!["Cronograma de Entrada" etapa para um Canva baseado em ação.]({% image_buster /assets/img/canvas_templates/back_in_stock_3.png %})

{: start="2"}
2\. Defina a **Hora de início (obrigatório)** para a data e hora de início desejadas.

!["Janela de Entrada" seção com um horário de início em 2 de janeiro de 2025 às 12h.]({% image_buster /assets/img/canvas_templates/back_in_stock_4.png %})

### Etapa 4: Selecione o público-alvo

Definiremos nosso público-alvo como os usuários que, em nossa opinião, têm maior probabilidade de comprar o jeans Classic Straight Leg.

1. Selecione nosso segmento-alvo, "Favorited - Classic Straight Leg Jeans", que consiste em usuários que favoritaram nosso jeans Classic Straight Leg em nosso app ou site.
2. Selecione um filtro para incluir usuários que compraram "Jeans" mais de "0" vezes.

!["Público-Alvo" etapa com o segmento de "Favoritado - Jeans Perna Reta Clássica".]({% image_buster /assets/img/canvas_templates/back_in_stock_5.png %})

{: start="3"}
3\. Ajuste os controles de entrada para permitir que os usuários entrem novamente no Canvas após a duração máxima do Canvas, para evitar a probabilidade de os usuários dispararem a mesma etapa simultaneamente.

!["Controles de Entrada" seção com uma caixa de seleção para permitir que os usuários reentrem neste Canva com uma duração máxima do Canva.]({% image_buster /assets/img/canvas_templates/back_in_stock_6.png %})

{: start="4"}
4\. Ajuste os critérios de saída para remover os usuários que realizaram o evento personalizado de desfavorecer o jeans Classic Straight Leg.

!["Critérios de Saída" seção com uma exceção para usuários que realizam o evento personalizado de "Desfavoritado".]({% image_buster /assets/img/canvas_templates/back_in_stock_7.png %})

### Etapa 5: Selecione suas configurações de envio

Manteremos as configurações padrão de inscrição, para que enviemos apenas aos usuários que se inscreveram ou aceitaram receber mensagens ou notificações, e ignoraremos as outras configurações (limite de frequência, horário de silêncio e grupos de teste).

!["Configurações de Envio" etapa direcionando usuários que estão inscritos ou optaram por participar.]({% image_buster /assets/img/canvas_templates/back_in_stock_8.png %})

### Etapa 6: Personalize sua tela

Agora, criaremos nosso Canva personalizando os canais e o conteúdo que será enviado aos usuários. Como estamos usando todos os quatro canais do modelo (push para mobile e web, SMS e e-mail) e usando o filtro [Intelligent Channel]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_channel/), não precisamos adicionar ou remover nenhum.

{% alert tip %}
Você pode usar as [propriedades de entrada do Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/) para personalizar as mensagens no seu Canvas com base no produto ao qual está se referindo.
{% endalert %}

Começaremos nossa personalização percorrendo cada etapa do Message para atualizar o conteúdo.

1. Substitua `!!YOURCATALOGHERE!!` pelo nome do nosso catálogo ("Straight_Leg_Pants").
2. Substitua `[0]` pelo número de índice do jeans Classic Straight Leg, que é "9", porque o jeans é o décimo item na matriz `items` do nosso catálogo. (As matrizes são indexadas a zero no Liquid, portanto, o primeiro item é `0` e não `1`).
3. Repita as etapas 1 e 2 para todas as etapas restantes do Message, inclusive:
    - A mensagem "In-Product Msg & E-mail" que é enviada após a postergação de um dia
    - As mensagens "Push+Email Alert" que são enviadas aos usuários que não fizeram uma compra
4. Atualize a etapa Jornadas de ação selecionando o grupo de ação **Comprar**. Em seguida, selecione **Fazer uma compra específica** e escolha o jeans Classic Straight Leg como produto.

![Etapa do Canva de Push Móvel com uma mensagem notificando os usuários que um produto está de volta em estoque.]({% image_buster /assets/img/canvas_templates/back_in_stock_9.png %})

### Etapa 7: Teste e inicie seu Canva

Depois de testar e revisar nosso Canvas para garantir que ele funcione conforme o esperado, nós o iniciaremos selecionando **Launch Canvas**. Agora, nossos usuários que favoritaram nosso jeans Classic Straight Leg e se inscreveram em nossos canais de envio de mensagens receberão notificações quando ele estiver novamente em estoque!

{% alert tip %}
Confira nossa [lista de verificação pré e pós-lançamento]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) para saber o que considerar antes e depois de lançar um Canva.
{% endalert %}

