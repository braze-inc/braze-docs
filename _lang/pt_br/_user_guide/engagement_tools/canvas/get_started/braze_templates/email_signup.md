---
nav_title: Registro de e-mail com double opt-in
article_title: Registro de e-mail com double opt-in
page_order: 2
page_type: reference
description: "Este artigo descreve como usar um modelo do Braze Canvas para expandir seu alcance com inscrições de e-mail verificadas."
tool: Canvas
---

# Registro de e-mail com double opt-in

> Use o modelo de inscrição de e-mail com opt-in duplo para expandir seu alcance com inscrições de e-mail verificadas. Direcione os novos usuários para capturar o e-mail deles, confirmar a assinatura e receber um código promocional, tudo em uma única jornada perfeita.

Este artigo o guiará por um caso de uso para a **inscrição por e-mail com o** modelo **double opt-in**, que foi projetado para o estágio de consideração do ciclo de vida do usuário. Quando terminar, você terá criado um Canvas que envia e-mails e mensagens no aplicativo para os usuários quando eles iniciam uma sessão ou quando não concluíram a integração.

## Pré-requisitos

Para usar esse modelo com sucesso, você precisará do seguinte:

- Uma [mensagem in-app de várias páginas]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create#multi-page) com uma página para capturar os e-mails dos usuários e outra para comunicar uma mensagem de sucesso.
- Um e-mail de confirmação para que os usuários verifiquem seus endereços de e-mail.
- Um e-mail de boas-vindas com um código promocional exclusivo para os usuários que fizerem double opt-in.

## Adaptar o modelo às suas necessidades

Digamos que estejamos trabalhando para a Steppington, um aplicativo de saúde conhecido por seus recursos, como rastreamento de calorias, aulas de exercícios digitais e maratonas de flashmob. Antes de criar o Canvas, configuramos [mensagens de várias páginas no aplicativo e no navegador]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create#multi-page) que incluem uma série de perguntas envolventes para determinar a experiência e a impressão da primeira viagem do usuário com o aplicativo.

Para acessar o modelo, ao criar um novo Canvas, selecione **Usar um modelo de Canvas** > **Modelos do Braze**. Em seguida, ao lado de **Email sign-up with double opt-in**, selecione **Apply Template (Aplicar modelo**). Agora, podemos examinar o modelo para adequá-lo às nossas necessidades.

### Etapa 1: Configurar os detalhes

Vamos ajustar os detalhes do Canvas para refletir nosso objetivo.

1. Selecione **Editar** ao lado do nome do modelo.

\![O título e a descrição atuais do Canvas.]({% image_buster /assets/img/canvas_templates/email_signup1.png %}){: style="max-width:50%;"}

{:start="2"}
2\. Atualize o nome do Canvas para especificar que o Canvas é para segmentar novos usuários quando eles usam o aplicativo pela primeira vez.
3\. Atualize a descrição para explicar que esse Canvas contém mensagens personalizadas para que os usuários optem por participar duas vezes.
4\. Adicione a tag **Email** para que possamos filtrá-la na página inicial do Canvas.

\![O novo nome, descrição e tag do Canvas.]({% image_buster /assets/img/canvas_templates/email_signup2.png %}){: style="max-width:90%;"}

### Etapa 2: Atribuir eventos de conversão

Em seguida, vamos atribuir nossos eventos de conversão. Os eventos de conversão são um tipo de métrica que pode ser usada para medir o sucesso do Canvas. Para o **tipo de evento de conversão**, selecione **Performs Custom Event (Executa evento personalizado**). Em seguida, selecione **email_opt_in** para o **nome do evento personalizado**.

\!["Assign Conversion Events" (Atribuir eventos de conversão) para o tipo de evento de conversão de opt-in para e-mail.]({% image_buster /assets/img/canvas_templates/email_signup3.png %}){: style="max-width:90%;"}

Manteremos o prazo de conversão do modelo de três dias, pois queremos atingir nossos usuários mais recentes.

### Etapa 3: Adaptar o cronograma de entrada

Vamos manter a programação de entrada como **Action-Based** para que os usuários entrem em nosso Canvas quando iniciarem uma sessão no aplicativo. Dessa forma, podemos começar a construir nosso relacionamento com um engajamento oportuno.

Também manteremos as **Action Based Options** como estão, para que os usuários só entrem no Canvas quando iniciarem uma sessão.

Uma programação de entrada baseada em ações para inserir usuários que iniciam qualquer sessão no Canvas.]({% image_buster /assets/img/canvas_templates/email_signup4.png %}){: style="max-width:90%;"}

Para a **Janela de entrada**, atualizaremos a **Hora de início (obrigatório)** para a data e hora desejadas.

Uma janela de entrada com o horário de início em 16 de janeiro de 2025 às 12:30h. Os usuários digitarão essa mensagem em seu fuso horário local.]({% image_buster /assets/img/canvas_templates/email_signup5.png %}){: style="max-width:90%;"}

### Etapa 4: Selecione o público-alvo

Definiremos nosso público-alvo como usuários do Steppington que não têm um endereço de e-mail em seu perfil de usuário. Faremos isso mantendo o [filtro de segmentação]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters) padrão do modelo `Email Available is false`.

\![Entry Audience com o filtro "E-mail disponível é falso".]({% image_buster /assets/img/canvas_templates/email_signup6.png %}){: style="max-width:90%;"}

### Etapa 5: Selecione suas configurações de envio

Manteremos as configurações de assinatura padrão, para que enviemos apenas aos usuários que se inscreveram ou optaram por receber mensagens ou notificações, e ignoraremos as outras configurações (limite de frequência, horas de silêncio e grupos de sementes).

Opções de envio padrão para enviar apenas aos usuários que estão inscritos ou optaram por participar.]({% image_buster /assets/img/canvas_templates/email_signup7.png %}){: style="max-width:90%;"}

### Etapa 6: Personalize seu Canvas

Agora, criaremos nosso Canvas personalizando os canais e o conteúdo que serão enviados aos usuários. Como estamos nos concentrando na verificação de nossas inscrições por e-mail, não precisamos adicionar ou remover nenhuma das etapas e canais do Canvas do modelo.

1. Selecione a primeira etapa da mensagem chamada **Email Sign-up (Registro de e-mail)**. É aqui que atualizaremos o modelo para usar nossa mensagem in-app (e in-browser) de várias páginas.

- A página 1 capturará os e-mails.
- A página 2 exibirá uma mensagem de confirmação.

Duas páginas de uma mensagem no aplicativo para capturar e-mails de usuários e exibir uma mensagem de sucesso.]({% image_buster /assets/img/canvas_templates/email_signup8.png %}){: style="max-width:90%;"}

{:start="2"}
2\. A partir daqui, manteremos a etapa **Subscribed** Action Path como está. Essa etapa divide nossos usuários em dois grupos em uma janela de um dia:

- Usuários que se inscreveram na Steppington com seu e-mail
- Usuários que não se inscreveram na Steppington com seu e-mail

{:start="3"}
3\. Em seguida, substitua o corpo do e-mail pelo e-mail de confirmação da nossa marca para a etapa **Verify Email** Message ( **Verificar** mensagem **de e-mail** ). Isso enviará um e-mail para nossos usuários inscritos e solicitará que confirmem seu endereço de e-mail e optem por receber nossas mensagens.
4\. Mantenha a etapa **Confirmar** caminho de ação **da assinatura** como está. Essa etapa divide ainda mais nossos usuários entre aqueles que confirmaram seu e-mail e aqueles que não confirmaram, com um prazo de uma semana.
5\. Por fim, atualize a etapa Mensagem de **boas-vindas + desconto** com nosso e-mail de confirmação que inclui um código promocional exclusivo.  

### Etapa 7: Teste e inicie seu Canvas

Depois de testar e revisar nosso Canvas para garantir que ele funcione conforme o esperado, nós o iniciaremos selecionando **Launch Canvas**.

{% alert tip %}
Confira nossa [lista de verificação pré e pós-lançamento]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) para saber o que considerar antes e depois de lançar um Canvas.
{% endalert %}