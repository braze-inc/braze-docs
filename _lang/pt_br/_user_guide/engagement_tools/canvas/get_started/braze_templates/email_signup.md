---
nav_title: Cadastro de e-mail com aceitação dupla
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

Para usar este modelo com sucesso, você precisa do seguinte:

- Uma [mensagem no app de várias páginas]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create#multi-page), com uma página para capturar os e-mails dos seus usuários e outra para comunicar uma mensagem de sucesso. 
- Um e-mail de confirmação para os usuários verificarem seu endereço de e-mail.
- Um e-mail de boas-vindas com um código de promoção exclusivo para usuários que aceitam duas vezes.

## Adaptar o modelo às suas necessidades

Vamos supor que você esteja trabalhando para a Steppington, um aplicativo de saúde conhecido por seus recursos, como rastreamento de calorias, aulas de exercícios digitais e maratonas em flash mob. Antes de criar o Canvas, você [configura mensagens em várias páginas no aplicativo e no navegador]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create#multi-page) que incluem uma série de perguntas envolventes para determinar a experiência e a impressão da primeira viagem de um usuário com o aplicativo.

Para acessar o modelo, ao criar um novo canva, selecione **Usar um modelo do canvas** > **Modelos da Braze**. Em seguida, ao lado de **Cadastro de E-mail com Aceitação Dupla**, selecione **Aplicar modelo**. Agora, podemos examinar o modelo para adequá-lo às nossas necessidades.

### Etapa 1: Configurar os detalhes

Ajuste os detalhes do Canvas para refletir seu objetivo.

1. Selecione **Editar** ao lado do nome do modelo.

![O título e a descrição atuais do Canvas.]({% image_buster /assets/img/canvas_templates/email_signup1.png %}){: style="max-width:50%;"}

{:start="2"}
2\. Atualize o canva para especificar que o canva é para direcionamento de novos usuários quando eles usam o app pela primeira vez.
3\. Atualize a descrição para explicar que este Canvas contém mensagens personalizadas para os usuários optarem por participar.
4\. Adicione a tag **E-mail** para que possamos filtrá-la na página inicial do canva.

![O novo nome, descrição e tag para o Canvas.]({% image_buster /assets/img/canvas_templates/email_signup2.png %}){: style="max-width:90%;"}

### Etapa 2: Atribuir eventos de conversão

Em seguida, atribua nossos eventos de conversão. Eventos de conversão são um tipo de métrica que você pode usar para medir o sucesso do Canvas. Em **Tipo de evento de conversão**, selecione **Realiza evento personalizado**. Então, selecione **email_opt_in** para o **Nome do evento personalizado**.

![Seção "Atribuir Eventos de Conversão" para o tipo de evento de conversão de optar por e-mail.]({% image_buster /assets/img/canvas_templates/email_signup3.png %}){: style="max-width:90%;"}

Mantenha o prazo de conversão do modelo de três dias porque você deseja direcionar seus usuários mais recentes.

### Etapa 3: Adaptar o cronograma de entrada

Mantenha o cronograma de entrada como **Ação Baseada** para que os usuários entrem no seu Canvas quando iniciarem uma sessão no aplicativo. Dessa forma, você pode começar a construir seu relacionamento com um engajamento oportuno.

Além disso, considere manter as **Opções Baseadas em Ação** como estão para que os usuários entrem no Canvas apenas quando iniciarem uma sessão.

![Um cronograma de entrada baseado em ação para inserir usuários que iniciam qualquer sessão no Canvas.]({% image_buster /assets/img/canvas_templates/email_signup4.png %}){: style="max-width:90%;"}

Para a **Janela de Entrada**, atualize o **Hora de Início (Obrigatório)** para a data e hora desejadas.

![Um período de entrada com o horário de início 16 de janeiro de 2025 às 12:30. Os usuários entrarão nesta mensagem em seu fuso horário local.]({% image_buster /assets/img/canvas_templates/email_signup5.png %}){: style="max-width:90%;"}

### Etapa 4: Selecione o público-alvo

Defina seu público-alvo como usuários da Steppington que não têm um endereço de e-mail em seu perfil de usuário, mantendo o [filtro de segmentação]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters) padrão do modelo `Email Available is false`.

![Entrada do público com o filtro "E-mail disponível é falso".]({% image_buster /assets/img/canvas_templates/email_signup6.png %}){: style="max-width:90%;"}

### Etapa 5: Selecione suas configurações de envio

Mantenha as configurações de inscrição padrão, para que você envie apenas para usuários que se inscreveram ou optaram por receber mensagens ou notificações, e pule as outras configurações (limitação de frequência, horário de silêncio e grupos de teste).

![Opções de envio padrão para enviar apenas para usuários que estão inscritos ou optaram por receber.]({% image_buster /assets/img/canvas_templates/email_signup7.png %}){: style="max-width:90%;"}

### Etapa 6: Personalize sua tela

Em seguida, construa o canva personalizando os canais e o conteúdo que você deseja enviar aos usuários. Como você está focando na verificação de inscrições por e-mail, não precisa adicionar ou remover nenhuma das etapas e canais do modelo do canva.

1. Selecione a primeira etapa da mensagem chamada **Inscrição para e-mail**. Aqui é onde você atualiza o modelo para usar nossa mensagem em várias páginas no app (e no navegador).

- A página 1 captura os e-mails.
- A página 2 exibe uma mensagem de confirmação.

![Duas páginas de uma mensagem no app para capturar e-mails de usuários e exibir uma mensagem de sucesso.]({% image_buster /assets/img/canvas_templates/email_signup8.png %}){: style="max-width:90%;"}

{:start="2"}
2\. A partir daqui, mantenha a etapa do caminho de ação **Inscrito** como está. Esta etapa divide nossos usuários em dois grupos em um intervalo de um dia:

- Usuários que se inscreveram no Steppington com seu e-mail
- Usuários que não se inscreveram no Steppington com seu e-mail

{:start="3"}
3\. Em seguida, substitua o corpo do e-mail pelo nosso e-mail de confirmação da marca para a etapa de **Verificar e-mail**. Isso enviará um e-mail para nossos usuários inscritos e os solicitará a confirmar seu endereço de e-mail e optar por nossas mensagens.
4\. Mantenha a etapa do caminho de ação **Confirmar inscrição** como está. Esta etapa divide ainda mais nossos usuários entre aqueles que confirmaram seu e-mail e aqueles que não confirmaram, com uma janela de uma semana.
5\. Por fim, atualize a etapa de **Mensagem de Boas-Vindas + Desconto** com nosso e-mail de confirmação que inclui um código de promoção exclusivo.

{% alert note %}
A etapa da mensagem **Verificar E-mail** é disparada na segunda sessão do usuário. Isso ocorre porque o evento de início da primeira sessão dispararia o canva, mas um início de segunda sessão após o usuário ter alcançado a primeira etapa da mensagem **Inscrição por E-mail** é necessário para que o usuário seja elegível para disparar a segunda mensagem no app.
{% endalert %}

### Etapa 7: Teste e inicie seu Canva

Após testar e revisar seu canva para garantir que funcione como esperado, lance-o selecionando **Lançar Canva**.

{% alert tip %}
Confira nossa [lista de verificação pré e pós-lançamento]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) para saber o que considerar antes e depois de lançar um Canva.
{% endalert %}
