---
nav_title: Carrinho abandonado
article_title: Carrinho Abandonado
page_order: 1
page_type: reference
description: "Este artigo descreve como usar um modelo de Canvas do Braze para interagir com os usuários em tempo real e incentivá-los a completar suas compras."
tool: Canvas
---

# Carrinho abandonado

> Interaja com os usuários em tempo real para incentivá-los a completar suas compras. Use este modelo para criar uma jornada do usuário que se concentra em enviar mensagens personalizadas e oportunas que lembram os usuários de seus carrinhos abandonados, destacando os benefícios dos produtos e oferecendo incentivos, como códigos de desconto.

Neste artigo, vamos guiá-lo por um caso de uso para o modelo **Intenção Abandonada**, que é destinado à fase de consideração do ciclo de vida do usuário. Após este artigo, você terá personalizado uma jornada do usuário que incentiva compras de usuários que não realizaram compras após adicionar itens aos seus carrinhos.

## Pré-requisitos

Para usar este modelo com sucesso, você precisará do seguinte:

- Uma jornada do usuário pós-compra separada, pois fazer uma compra neste Canvas fará com que os usuários saiam do Canvas.
- Uma [Sincronização de Audiência do Braze]({{site.baseurl}}/partners/canvas_audience_sync/) configurada com os parceiros e audiências que você utiliza.

## Personalizando o modelo para suas necessidades

Vamos supor que trabalhamos na Kitchenerie, uma marca de varejo especializada em utensílios de cozinha, e nosso objetivo é reengajar usuários que adicionaram o último produto "Prato de Papel Enorme" aos seus carrinhos, mas não realizaram suas compras.

Antes de criar o Canvas, configuramos a integração [Sincronização de Audiência do Braze com o Facebook]({{site.baseurl}}/partners/canvas_audience_sync/facebook_audience_sync/) para que possamos adicionar dados de usuários do Braze às Audiências do Facebook para enviar anúncios com base em gatilhos comportamentais, segmentação e mais.

Para acessar o modelo de intenção abandonada, ao criar um novo Canvas, selecione **Usar um modelo de Canvas** > **Modelos do Braze**. Em seguida, ao lado de **Intenção Abandonada**, selecione **Aplicar Modelo**. Agora, podemos passar pelo modelo para ajustá-lo às nossas necessidades.

### Passo 1: Configure os detalhes

Vamos ajustar os detalhes do Canvas para refletir nosso objetivo.

1. Selecione **Editar** ao lado do nome do modelo.

\![O título e a descrição atuais do Canvas.]({% image_buster /assets/img/canvas_templates/abandoned_intent_old_name_description.png %}){: style="max-width:60%;"}

{:start="2"}
2\. Atualize o nome do Canvas para especificar que o Canvas é para direcionar usuários com carrinhos abandonados.
3\. Atualize a descrição para especificar que o Canvas é para incentivar os usuários a completarem compras do último lançamento de utensílios de cozinha sazonais.
4\. Adicione a tag **Abandonar Carrinho** para que possamos filtrá-la na página inicial do Canvas.

\![O novo nome, descrição e tag para o Canvas.]({% image_buster /assets/img/canvas_templates/abandoned_intent_new_name_description.png %}){: style="max-width:60%;"}

### Passo 2: Atribua seus eventos de conversão

Em seguida, vamos atribuir nosso evento de conversão. Como nosso foco é no produto "Prato de Papel Enorme", faremos o seguinte para **Evento de Conversão Primário A**:

1. Para o **tipo de evento de conversão**, selecione **Faz Compra**.
2. Selecione **Fazer uma compra específica**. Isso nos permite selecionar um nome de produto específico.
3. Selecione **Prato de Papel Enorme**.

\![Evento de Conversão Primário - A com o tipo de conversão "Faz Compra" com o nome do produto "Prato de Papel Enorme". Há um prazo de conversão de 3 dias.]({% image_buster /assets/img/canvas_templates/abandoned_intent1.png %})

### Passo 3: Defina um cronograma de entrada

Enquanto o cronograma de entrada deste modelo está definido para **API-Triggered**, nosso caso de uso se beneficiará mais ao ter uma entrada baseada em ação para este Canvas, já que queremos focar em usuários que abandonaram seu carrinho (que é uma ação).

1. Selecione **Ação Baseada** como o tipo de cronograma de entrada.
2. Selecione **Carrinho Abandonado** como o gatilho.
3. Para a janela de entrada, selecione a data e hora de início.
4. Selecione a opção para permitir que os usuários entrem em seu fuso horário local. Isso pode manter nossas mensagens relevantes e levar a um maior engajamento se as mensagens forem enviadas em horários ideais.

\![Um Canvas baseado em ação que visa usuários que abandonaram seu carrinho, com a janela de entrada em 15 de outubro de 2024 às 15:20 no fuso horário local dos usuários.]({% image_buster /assets/img/canvas_templates/abandoned_intent2.png %})

### Passo 4: Determine quem entra no Canvas

Em seguida, vamos definir nosso público-alvo como usuários que compraram exclusivamente online conosco nos últimos 90 dias. Isso nos ajuda a restringir nosso público a usuários que sabemos que estão engajados com nossos produtos. 

\!["Segmento de Compradores Online - 90 Dias" como o segmento de usuários a serem alvo para este Canvas.]({% image_buster /assets/img/canvas_templates/abandoned_intent3.png %})

Deixaremos os controles de entrada como estão, para que os usuários não possam reentrar neste Canvas e não há limite para o número de pessoas que podem potencialmente entrar neste Canvas.

Para os critérios de saída, os usuários sairão do Canvas se tiverem comprado o "Prato de Papel Enorme". Dessa forma, eles não receberão mais mensagens sobre um item que já compraram.

\![Critérios de saída que determinam que usuários que fazem uma compra específica do prato de papel enorme sairão do Canvas.]({% image_buster /assets/img/canvas_templates/abandoned_intent4.png %})

### Passo 5: Selecione suas configurações de envio

Manteremos as configurações de assinatura padrão, então enviaremos apenas para usuários que se inscreveram ou optaram por receber mensagens ou notificações, e deixaremos as outras configurações como estão.

### Passo 6: Personalize seu Canvas

Agora, construiremos nosso Canvas personalizando os passos template:

1. Selecione o passo Action Paths, em seguida, selecione o nome do grupo de ações **Fez a compra**.
2. Para **Fazer Compra**, selecione **Fazer Uma Compra Específica** e escolha **Prato de Papel Enorme** para o produto. Semelhante aos critérios de saída, os usuários que comprarem este produto sairão do Canvas.

\!["Grupo de ações 'Fez a compra' que sairá do Canvas se o usuário comprar o prato de papel enorme.]({% image_buster /assets/img/canvas_templates/abandoned_intent5.png %})

{: start="3"}
3\. Para o passo Mensagem, selecione **Editar mensagem** para personalizar o e-mail que será enviado aos nossos usuários, notificando-os sobre os itens em seu carrinho abandonado.
4\. Mantenha o passo Delay como está.
5\. Nos passos de Mensagem subsequentes ao passo Audience Path, personalizaremos o e-mail e a mensagem SMS que nossos usuários receberão. É aqui que queremos incentivar nossos usuários a comprar produtos com mensagens personalizadas.

\![Uma prévia da mensagem SMS que os usuários receberão: "Oi, você deixou o prato de papel enorme para trás no seu carrinho! Complete sua compra agora e melhore seu jogo de anfitrião. Use o código MYPLATE na finalização da compra para 20 por cento de desconto no seu pedido!"]({% image_buster /assets/img/canvas_templates/abandoned_intent6.png %})

{: start="6"}
6\. No próximo passo Action Paths, selecione o grupo de ações **Fez a compra**. Em seguida, selecione **Fazer uma compra específica** e escolha **Prato de Papel Enorme** para o produto. Esta etapa refletirá a primeira etapa dos Caminhos de Ação, saindo dos usuários que compraram nosso produto para que não recebam mais mensagens.
7\. Certifique-se de que nossa etapa de Sincronização de Público esteja configurada para sincronizar com o Facebook. Isso ajudará ainda mais com a retargetização de anúncios.

{% alert tip %}
Você pode usar [Propriedades de entrada do Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/) para personalizar as mensagens em seu Canvas com base no produto ao qual você está se referindo.
{% endalert %}

### Etapa 7: Teste e lance o Canvas

Após testar e revisar nosso Canvas para garantir que funcione como esperado, selecione **Lançar Canvas** para lançar o Canvas. Agora, podemos direcionar os usuários de forma consciente com uma jornada personalizada para incentivá-los a conferir o produto que adicionaram aos seus carrinhos!

{% alert tip %}
Confira nossa [Lista de verificação pré e pós-lançamento]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) para coisas a considerar antes e depois de lançar um Canvas.
{% endalert %}

