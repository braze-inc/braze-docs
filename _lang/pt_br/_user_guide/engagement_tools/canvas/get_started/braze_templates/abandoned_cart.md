---
nav_title: Carrinho abandonado
article_title: Carrinho abandonado
page_order: 1
page_type: reference
description: "Este artigo descreve como usar um modelo do Braze Canvas para fazer o engajamento com os usuários em tempo real e incentivá-los a concluir suas compras."
tool: Canvas
---

# Carrinho abandonado

> Engajamento com os usuários em tempo real para incentivá-los a concluir suas compras. Use esse modelo para criar uma jornada do usuário que se concentre no envio de mensagens oportunas e personalizadas que lembrem os usuários de seus carrinhos abandonados, destacando os benefícios do produto e oferecendo incentivos, como códigos de desconto.

Neste artigo, vamos orientá-lo em um caso de uso do modelo **Abandoned Intent**, que se destina ao estágio de consideração do ciclo de vida do usuário. Após este artigo, você terá personalizado uma jornada do usuário que incentiva as compras de usuários que não fizeram compras depois de adicionar itens aos carrinhos.

## Pré-requisitos

Para usar esse modelo com sucesso, você precisará do seguinte:

- Um Canvas separado para a jornada do usuário pós-compra, já que fazer uma compra nesse Canvas fará com que os usuários saiam do Canvas.
- Um [Braze Audience Sync]({{site.baseurl}}/partners/canvas_audience_sync/) configurado com os parceiros e públicos que você usa.

## Adaptar o modelo às suas necessidades

Digamos que trabalhamos na Kitchenerie, uma marca de varejo especializada em utensílios de cozinha, e nossa meta é reengajar os usuários que adicionaram o produto mais recente, "Enormous Paper Plate", aos seus carrinhos, mas não fizeram a compra.

Antes de criar o Canva, configuramos a integração [Braze Audience Sync to Facebook]({{site.baseurl}}/partners/canvas_audience_sync/facebook_audience_sync/) para que possamos adicionar dados de usuários do Braze ao público do Facebook para enviar anúncios com base em disparadores comportamentais, segmentação e muito mais.

Para acessar o modelo de intenção abandonada, ao criar um novo Canvas, selecione **Usar um modelo de Canvas** > **Modelos do Braze**. Em seguida, ao lado de **Abandoned Intent**, selecione **Apply Template (Aplicar modelo)**. Agora, podemos examinar o modelo para adequá-lo às nossas necessidades.

### Etapa 1: Configurar os detalhes

Vamos ajustar os detalhes do Canva para refletir nosso objetivo.

1. Selecione **Editar** ao lado do nome do modelo.

![O título e a descrição atuais do Canva.]({% image_buster /assets/img/canvas_templates/abandoned_intent_old_name_description.png %}){: style="max-width:60%;"}

{:start="2"}
2\. Atualize o nome do Canvas para especificar que o Canvas é para direcionamento de usuários com carrinhos abandonados.
3\. Atualize a descrição para especificar que o Canva serve para incentivar os usuários a concluir as compras do último lançamento sazonal de utensílios de cozinha.
4\. Adicione a tag **Abandono de carrinho** para que possamos filtrá-la na página inicial do Canva.

![O novo nome, a descrição e a tag do Canva.]({% image_buster /assets/img/canvas_templates/abandoned_intent_new_name_description.png %}){: style="max-width:60%;"}

### Etapa 2: Atribua seus eventos de conversão

Em seguida, vamos atribuir nosso evento de conversão. Como nosso foco está em nosso produto "Enormous Paper Plate", faremos o seguinte para o **evento de conversão primária A**:

1. Para o **tipo de evento Conversion (Conversão)**, selecione **Makes Purchase (Compra)**.
2. Selecione **Fazer uma compra específica**. Isso nos permite selecionar um nome de produto específico.
3. Selecione **Enormous Paper Plate**.

![Evento de conversão primária - Um evento com o tipo de conversão "Faz compra" com o nome do produto "Enormous Paper Plate". Há um prazo de conversão de 3 dias.]({% image_buster /assets/img/canvas_templates/abandoned_intent1.png %})

### Etapa 3: Definir uma programação de entrada

Embora a programação de entrada desse modelo esteja definida como **API-Triggered**, nosso caso de uso se beneficiará mais com uma entrada baseada em ação para esse Canva, pois queremos nos concentrar nos usuários que abandonaram o carrinho (que é uma ação).

1. Selecione **Baseado em ação** como o tipo de programação de entrada.
2. Selecione **Abandono de carrinho** como o disparador.
3. Na janela de entrada, selecione a data de início.
4. Selecione a opção para permitir que os usuários insiram seu fuso local. Isso pode manter a relevância do envio de mensagens e levar a um maior engajamento se as mensagens forem enviadas nos melhores horários para envio.

![Um Canvas baseado em ações que visa usuários que abandonaram seu carrinho, com a janela de entrada em 15 de outubro de 2024 às 15:20 no fuso local dos usuários.]({% image_buster /assets/img/canvas_templates/abandoned_intent2.png %})

### Etapa 4: Determinar quem entra no Canva

Em seguida, vamos definir nosso público-alvo como usuários que fizeram compras exclusivamente on-line conosco nos últimos 90 dias. Isso nos ajuda a restringir nosso público a usuários que sabemos que estão engajados com nossos produtos. 

!["Segmento de Compradores Online - 90 Dias" como o segmento de usuários a serem alvo para este Canvas.]({% image_buster /assets/img/canvas_templates/abandoned_intent3.png %})

Deixaremos os controles de entrada como estão, para que os usuários não tenham permissão para entrar novamente nesse Canvas e não haja limite para o número de pessoas que podem potencialmente entrar nesse Canvas.

Para os critérios de saída, os usuários sairão do Canva se tiverem comprado o "Enormous Paper Plate". Dessa forma, eles não receberão mais mensagens sobre um item que já compraram.

![Critérios de saída que determinam usuários que fazem uma compra específica do enorme prato de papel sairão do Canvas.]({% image_buster /assets/img/canvas_templates/abandoned_intent4.png %})

### Etapa 5: Selecione suas configurações de envio

Manteremos as configurações de inscrição padrão, para que enviemos apenas aos usuários que se inscreveram ou aceitaram receber mensagens ou notificações, e deixaremos as outras configurações como estão.

### Etapa 6: Personalize sua tela

Agora, criaremos nosso Canvas personalizando as etapas do modelo:

1. Selecione a etapa Jornadas de ação e, em seguida, selecione o nome do grupo de ação **Compra efetuada**.
2. Em **Make Purchase**, selecione **Make A Specific Purchase** e escolha **Enormous Paper Plate** como produto. Semelhante aos critérios de saída, usuários que comprarem este produto sairão do Canvas.

![Grupo de ação "Fez a compra" que sairá do Canvas se o usuário comprar o enorme prato de papel.]({% image_buster /assets/img/canvas_templates/abandoned_intent5.png %})

{: start="3"}
3\. Para a etapa Message (Mensagem), selecione **Edit message (Editar mensagem)** para personalizar o e-mail que será enviado aos nossos usuários, notificando-os sobre os itens em seu carrinho abandonado.
4\. Mantenha a etapa de postergação como está.
5\. Nas etapas de Mensagem subsequentes à etapa de Jornada do público, personalizaremos o e-mail e a mensagem SMS que nossos usuários receberão. É aqui que queremos incentivar nossos usuários a comprar produtos com envio de mensagens personalizadas.

![Uma prévia da mensagem SMS que os usuários receberão: "Olá, você deixou o enorme prato de papel no carrinho! Conclua sua compra agora e dê uma etapa em seu jogo de hospedagem. Use o código MYPLATE na finalização da compra para 20 por cento de desconto no seu pedido!"]({% image_buster /assets/img/canvas_templates/abandoned_intent6.png %})

{: start="6"}
6\. Na próxima etapa das jornadas de ação, selecione o grupo de ação **Compra efetuada**. Em seguida, selecione **Fazer uma compra específica** e escolha **Enormous Paper Plate** como o produto. Essa etapa espelhará a primeira etapa das jornadas de ação, encerrando os usuários que compraram nosso produto para que eles não recebam mais envios de mensagens.
7\. Certifique-se de que a etapa de sincronização do público do Facebook esteja configurada para sincronizar com o Facebook. Isso ajudará ainda mais no redirecionamento de anúncios.

{% alert tip %}
Você pode usar as [propriedades de entrada do Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/) para personalizar as mensagens no seu Canvas com base no produto ao qual está se referindo.
{% endalert %}

### Etapa 7: Teste e inicie o Canva

Depois de testar e revisar nosso Canvas para garantir que ele funcione conforme o esperado, selecione **Launch Canvas** para iniciar o Canvas. Agora, podemos direcionar os usuários de forma consciente com uma jornada de usuário personalizada para incentivá-los a finalizar a compra do produto que adicionaram aos carrinhos!

{% alert tip %}
Confira nossa [lista de verificação pré e pós-lançamento]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) para saber o que considerar antes e depois de lançar um Canva.
{% endalert %}

