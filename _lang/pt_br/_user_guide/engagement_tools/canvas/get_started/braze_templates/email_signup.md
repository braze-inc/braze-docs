---
nav_title: Cadastro de E-mail com Aceitação Dupla
article_title: Cadastro de E-mail com Aceitação Dupla
page_order: 2
page_type: reference
description: "Este artigo descreve como usar um modelo Canvas do Braze para expandir seu alcance com inscrições de e-mail verificadas."
tool: Canvas
---

# Cadastro de e-mail com aceitação dupla

> Use o modelo de inscrição por e-mail com aceitação dupla para expandir seu alcance com inscrições de e-mail verificadas. Alcance novos usuários para capturar seu e-mail, confirmar sua inscrição e receber um código de promoção, tudo em uma jornada contínua.

Este artigo irá guiá-lo através de um caso de uso para o modelo **Cadastro de E-mail com Aceitação Dupla**, que é projetado para a fase de consideração do ciclo de vida do usuário. Quando você terminar, terá criado um canva que envia e-mails e mensagens no app para os usuários quando eles iniciam uma sessão ou quando não completaram sua integração.

## Pré-requisitos

Para usar esse modelo com sucesso, você precisará do seguinte:

- Uma [mensagem no app de várias páginas]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create#multi-page), com uma página para capturar os e-mails dos seus usuários e outra para comunicar uma mensagem de sucesso.
- Um e-mail de confirmação para os usuários verificarem seu endereço de e-mail.
- Um e-mail de boas-vindas com um código de promoção exclusivo para usuários que aceitam duas vezes.

## Adaptar o modelo às suas necessidades

Vamos dizer que estamos trabalhando para a Steppington, um app de integridade conhecido por seus recursos, como rastreamento de calorias, aulas de exercícios digitais e maratonas de flash mob. Antes de criar o canva, [configuramos mensagens em várias páginas no app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create#multi-page) e no navegador que incluem uma série de perguntas envolventes para determinar a experiência e a impressão da primeira viagem de um usuário com o app.

Para acessar o modelo, ao criar um novo canva, selecione **Usar um modelo do canvas** > **Modelos da Braze**. Em seguida, ao lado de **Cadastro de E-mail com Aceitação Dupla**, selecione **Aplicar modelo**. Agora, podemos examinar o modelo para adequá-lo às nossas necessidades.

### Etapa 1: Configurar os detalhes

Vamos ajustar os detalhes do Canva para refletir nosso objetivo.

1. Selecione **Editar** ao lado do nome do modelo.

![O título e a descrição atuais do Canva.]({% image_buster /assets/img/canvas_templates/email_signup1.png %}){: style="max-width:50%;"}

{:start="2"}
2\. Atualize o canva para especificar que o canva é para direcionamento de novos usuários quando eles usam o app pela primeira vez.
3\. Atualize a descrição para explicar que este canva contém envio de mensagens personalizadas para os usuários aceitarem duas vezes.
4\. Adicione a tag **E-mail** para que possamos filtrá-la na página inicial do canva.

![O novo nome, a descrição e a tag do Canva.]({% image_buster /assets/img/canvas_templates/email_signup2.png %}){: style="max-width:90%;"}

### Etapa 2: Atribuir eventos de conversão

Em seguida, vamos atribuir nossos eventos de conversão. Os eventos de conversão são um tipo de métrica que pode ser usada para medir o sucesso do Canva. Em **Tipo de evento de conversão**, selecione **Realiza evento personalizado**. Em seguida, selecione **e-mail_opt_in** em **Nome do evento personalizado**.

![Seção "Atribuir eventos de conversão" para o tipo de evento de conversão de aceitação para e-mail.]({% image_buster /assets/img/canvas_templates/email_signup3.png %}){: style="max-width:90%;"}

Manteremos o prazo de conversão do modelo de três dias porque queremos direcionar nossos usuários mais recentes.

### Etapa 3: Adaptar o cronograma de entrada

Vamos manter o cronograma de entrada como **Baseado em ação** para que os usuários entrem em nosso canva quando iniciarem uma sessão no app. Dessa forma, podemos começar a construir nosso relacionamento com engajamento oportuno.

Nós também manteremos as **Opções baseadas em ação** como estão, para que os usuários entrem apenas no canva quando iniciarem uma sessão.

![Um cronograma de entrada baseado em ações para inserir usuários que iniciam qualquer sessão no canva.]({% image_buster /assets/img/canvas_templates/email_signup4.png %}){: style="max-width:90%;"}

Em **Período de entrada**, atualizaremos o **Horário de início (obrigatório)** para a data e hora desejadas.

![Um período de entrada com o horário de início 16 de janeiro de 2025 às 12:30. Os usuários inserirão esta mensagem em seu fuso local.]({% image_buster /assets/img/canvas_templates/email_signup5.png %}){: style="max-width:90%;"}

### Etapa 4: Selecione o público-alvo

Definiremos nosso público-alvo como usuários de Steppington que não têm um e-mail em seu perfil de usuário. Faremos isso mantendo o [filtro de segmentação]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters) padrão do modelo como `Email Available is false`.

![Entrada público com o filtro "Email Available is false".]({% image_buster /assets/img/canvas_templates/email_signup6.png %}){: style="max-width:90%;"}

### Etapa 5: Selecione suas configurações de envio

Manteremos as configurações padrão de inscrição, para que enviemos apenas aos usuários que se inscreveram ou aceitaram receber mensagens ou notificações, e ignoraremos as outras configurações (limite de frequência, horário de silêncio e grupos de teste).

![Opções de envio padrão para enviar apenas para usuários que estão inscritos ou optaram por participar.]({% image_buster /assets/img/canvas_templates/email_signup7.png %}){: style="max-width:90%;"}

### Etapa 6: Personalize sua tela

Agora, criaremos nosso Canva personalizando os canais e o conteúdo que será enviado aos usuários. Porque estamos focando na verificação das nossas inscrições por e-mail, não precisamos adicionar ou remover nenhum dos passos e canais do modelo do canva.

1. Selecione a primeira etapa da mensagem chamada **Inscrição para e-mail**. Este é o local onde atualizaremos o modelo para usar nossa mensagem em aplicativo (e no navegador) de várias páginas.

- A página 1 irá capturar os e-mails.
- A página 2 exibirá uma mensagem de confirmação.

![Duas páginas de uma mensagem no app para capturar e-mails de usuários e exibir uma mensagem de sucesso.]({% image_buster /assets/img/canvas_templates/email_signup8.png %}){: style="max-width:90%;"}

{:start="2"}
2\. A partir daqui, manteremos a etapa do caminho de ação **Inscrito** como está. Esta etapa divide nossos usuários em dois grupos em um intervalo de um dia:

- Usuários que se inscreveram no Steppington com seu e-mail
- Usuários que não se inscreveram no Steppington com seu e-mail

{:start="3"}
3\. Em seguida, substitua o corpo do e-mail pelo nosso e-mail de confirmação da marca para a etapa de **Verificar e-mail**. Isso enviará um e-mail para nossos usuários inscritos e os solicitará a confirmar seu endereço de e-mail e aceitar a nossa envio de mensagens.
4\. Mantenha a etapa do caminho de ação **Confirmar inscrição** como está. Esta etapa divide ainda mais nossos usuários entre aqueles que confirmaram seu e-mail e aqueles que não confirmaram, com um prazo de uma semana.
5\. Por fim, atualize a etapa de **Mensagem de Boas-Vindas + Desconto** com nosso e-mail de confirmação que inclui um código de promoção exclusivo.  

### Etapa 7: Teste e inicie seu Canva

Depois de testar e revisar nosso Canvas para garantir que ele funcione conforme o esperado, nós o iniciaremos selecionando **Lançar canva**.

{% alert tip %}
Confira nossa [lista de verificação pré e pós-lançamento]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) para saber o que considerar antes e depois de lançar um Canva.
{% endalert %}