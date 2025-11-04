---
nav_title: Feedback pós-compra
article_title: Feedback pós-compra
page_order: 6
page_type: reference
description: "Este artigo descreve como usar um modelo do Braze Canvas para orquestrar experiências personalizadas que lhe permitem responder ao feedback e criar um relacionamento com seus usuários."
tool: Canvas
---

# Feedback pós-compra

> Use o modelo de feedback pós-compra para obter insights importantes sobre como seus clientes interagem com sua marca e garantir que eles continuem a ter experiências positivas. Ao aproveitar a comunicação personalizada e um conjunto estruturado de mensagens, você pode continuar a construir e promover o relacionamento com seus clientes.

Este artigo o guiará por um caso de uso do modelo **Post-Purchase Feedback**, que foi projetado para a etapa de conversão do ciclo de vida do usuário. Quando terminar, você terá criado um Canvas que incentiva os usuários a fornecer feedback sobre o seu aplicativo.

## Pré-requisitos

Para usar esse modelo com sucesso, você precisará do seguinte:

- Um [atributo personalizado]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#managing-custom-attributes) para fazer referência aos resultados da pesquisa de feedback.
- Um [Braze Audience Sync]({{site.baseurl}}/partners/canvas_audience_sync/) configurado com os parceiros e públicos que você usa.

## Adaptar o modelo às suas necessidades

Digamos que estejamos trabalhando para a Decorumsoft, uma desenvolvedora de videogames para celular. Usaremos o modelo de feedback pós-compra para avaliar o feedback do nosso mais recente lançamento de videogame, o Proxy War 3: Guerra da sede. Usando esse feedback, informaremos nossos planos de desenvolvimento para o pacote de expansão, Liquid Mirage.

Antes de criar o Canvas, configuramos a integração do [Braze Audience Sync com o Google]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync/) para que possamos adicionar dados de usuários do Braze ao Google Audiences para enviar anúncios com base em acionadores comportamentais, segmentação e muito mais.

Para acessar o modelo de feedback pós-compra, ao criar um novo Canvas, selecione **Usar um modelo de Canvas** > **Modelos do Braze**. Em seguida, ao lado de **Post-Purchase Feedback**, selecione **Apply Template (Aplicar modelo**). Agora, podemos examinar o modelo para adequá-lo às nossas necessidades.

### Etapa 1: Configurar detalhes do Canvas

Vamos ajustar os detalhes do Canvas para refletir nosso objetivo.

1. Selecione **Editar** ao lado do nome do modelo.

\![O título e a descrição atuais do Canvas.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/select_edit_details.png %}){: style="max-width:50%;"}

{:start="2"}
2\. Atualize o nome do Canvas para especificar que o Canvas é destinado a usuários recentes.
3\. Atualize a descrição para especificar que o Canvas serve para incentivar os usuários a enviar feedback.
4\. Adicione a tag **Feedback** para filtrá-la na página inicial do Canvas.

\![O novo nome e a descrição do Canvas. A nova descrição indica: Um Canvas de feedback pós-compra para avaliar o interesse na próxima expansão do PWD3, Liquid Mirage.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/enter_new_canvas_name.png %}){: style="max-width:50%;"}

### Etapa 2: Atribuir eventos de conversão

Em seguida, vamos atribuir nossos eventos de conversão. Atualize o **Evento de Conversão Primário - A** para **Fazer uma compra específica** e selecione **Proxy War**.

\!["Atribuir eventos de conversão" para o tipo de evento de conversão da compra do produto do jogo Proxy War.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/select_conversion_event.png %}){: style="max-width:90%;"}

Manteremos o prazo de conversão do modelo de três dias, pois queremos atingir nossos usuários mais recentes.

### Etapa 3: Definir uma programação de entrada

1. Mantenha o tipo de programação de entrada como **Baseado em ação**.
2. Defina a **Hora de início** da janela de entrada para a data de lançamento do jogo.

### Etapa 4: Determinar quem entra no Canvas

Nosso público-alvo para feedback são os usuários que adquiriram recentemente o Proxy War 3.

1. Selecione nosso segmento-alvo, "Purchased Proxy War 3", que consiste em usuários que compraram o jogo.
2. Selecione um filtro para incluir usuários que compraram "Proxy War 3" mais de "0" vezes.

\![Um segmento chamado "Purchased Proxy War 3" que segmenta os usuários que compraram o jogo.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/entry_window_segment.png %}){: style="max-width:90%;"}

{: start="3"}
3\. Atualize os controles de entrada para não permitir que os usuários entrem novamente no Canvas após a duração máxima do Canvas.

### Etapa 5: Selecione suas configurações de envio

Manteremos as configurações de assinatura padrão, de modo que enviaremos apenas aos usuários que se inscreveram ou optaram por receber mensagens ou notificações. 

Como queremos ser cuidadosos com nosso envio, selecionaremos **Enable Quiet Hours** para evitar a solicitação de feedback entre 23h e 10h no fuso horário de nossos usuários e enviaremos somente no próximo horário disponível.

\!["Send Settings" (Configurações de envio), visando os usuários que estão inscritos ou optaram por participar. O Quiet Hours está ativado.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/send_settings_with_quiet_hours.png %}){: style="max-width:90%;"}

Para o nosso exemplo, ignoraremos as outras configurações (limite de frequência e grupos de sementes).

### Etapa 6: Personalize seu Canvas

Em seguida, criaremos nosso Canvas personalizando os canais de mensagens e o conteúdo que será enviado aos usuários. Como só estamos buscando feedback usando os canais de e-mail, mensagem no aplicativo e webhook, examinaremos o modelo e removeremos as variantes de SMS das etapas de Mensagem.

Começaremos nossa personalização passando por cada componente de mensagens para atualizar o conteúdo. Nosso atributo personalizado para referência é `Experience Feedback`.

1. No construtor do Canvas, selecione a primeira etapa da Mensagem na jornada do usuário.
2. Selecione a variante **Email**.
3. Preencha as **informações de envio** com um assunto que incentive o feedback do usuário. 
4. Selecione **Editar mensagem** para substituir a mensagem de e-mail do modelo pela nossa mensagem de pesquisa de feedback. Isso inclui a substituição dos links de cada call-to-action para capturar a opção selecionada, que será referenciada na etapa Action Path da jornada do usuário.

{% alert tip %}
Você pode usar [as propriedades de entrada do Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/) para personalizar as mensagens no seu Canvas com base no produto ao qual você está se referindo.
{% endalert %}

#### Configure a pesquisa de feedback

Em seguida, precisaremos preencher os detalhes da variante **In-App Message**. É aqui que precisamos especificar nosso atributo personalizado `Experience Feedback` que indica o sentimento do feedback do usuário. (Também faremos referência a isso na etapa subsequente do Caminho de Ação).

1. Na mesma etapa da primeira mensagem, selecione a variante **In-App Messages**. Manteremos os controles de mensagens como estão. 
2. Para o cabeçalho e o corpo, usaremos uma linguagem que incentive os usuários a serem honestos sobre sua experiência com o Proxy War 3.
3. Como queremos que as respostas da pesquisa sejam registradas com seus perfis, manteremos a pesquisa como **seleção de escolha única** e **atributos de registro no envio**.
4. Para cada uma das três opções de pesquisa, selecione **Experience Feedback** como nosso atributo personalizado. 
5. Manteremos os valores de atributo no perfil do usuário como estão, pois esses valores estão alinhados com nosso atributo personalizado.

\![Uma pesquisa que pergunta ao usuário se ele gostou da compra recente do Proxy War 3 com três opções: "Adorei", "Foi bom" e "Não é para mim".]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/survey_example_iam.png %}){: style="max-width:90%;"}

#### Crie o caminho da ação

Usando nosso atributo personalizado `Experience Feedback` e os valores de atributo da seção anterior, atualizaremos o Action Path do modelo para corresponder ao nosso atributo e aos valores.

O grupo "Bom feedback" para a etapa do Caminho de ação que inclui usuários que responderam "Adorei" em nossa pesquisa.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/action_path_good_example.png %}){: style="max-width:90%;"}

### Configure o redirecionamento de anúncios

Vamos nos certificar de que a sincronização do Google Audience esteja configurada em nossa etapa **de Ad Retargeting**. Isso incluirá a seleção de nossa conta de anúncios, um público existente e a opção de adicionar usuários ao público.

### Configurar casos de suporte de webhook

Em seguida, vamos configurar o webhook para acionar possíveis casos de suporte. Isso pode ser especialmente perspicaz em combinação com a análise do feedback do usuário.

Para a etapa da mensagem denominada **Support Case Creation (Criação de caso de suporte**), atualizaremos o modelo para compor um webhook para usuários insatisfeitos com a compra e que desejam um reembolso.

Um webhook que cria casos de suporte para clientes que têm um sentimento negativo e querem um reembolso pela compra do Proxy War 3.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/webhook_example.png %}){: style="max-width:90%;"}

### Etapa 6: Teste e inicie o Canvas

Depois de testar e revisar nosso Canvas para garantir que ele funcione conforme o esperado, selecione **Launch Canvas** para iniciar o Canvas. Agora, podemos direcionar os usuários de forma consciente com uma jornada de usuário personalizada para incentivá-los a responder à nossa pesquisa de feedback com base na compra recente do Proxy War 3!

{% alert tip %}
Confira nossa [lista de verificação pré e pós-lançamento]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) para saber o que considerar antes e depois de lançar um Canvas.
{% endalert %}
