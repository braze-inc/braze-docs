---
nav_title: Integração com pesquisa de preferências
article_title: Onboarding com pesquisa de preferências
page_order: 5.5
page_type: reference
description: "Este artigo descreve como usar um modelo do Braze Canvas para promover a adoção antecipada com um fluxo de integração guiado para apresentar sua marca aos novos usuários e coletar preferências para mantê-los envolvidos a longo prazo."
tool: Canvas
---

# Integração com pesquisa de preferências

> Use o modelo de pesquisa de integração com preferências para criar um fluxo de trabalho de integração guiado voltado para novos usuários. Apresente sua marca a eles, ajude-os a começar e colete suas preferências para mantê-los engajados a longo prazo.

Este artigo o guiará por um caso de uso do modelo **de pesquisa de integração com preferências**, que foi criado para o estágio de consideração do ciclo de vida do usuário. Ao terminar, você terá criado um Canvas que envia e-mails e mensagens no aplicativo para os usuários quando eles iniciam uma sessão e quando não concluem a integração.

## Pré-requisitos

Para usar esse modelo com sucesso, você precisará do seguinte:

- Um e-mail de boas-vindas que solicita aos usuários que iniciem a integração.
- Um e-mail de acompanhamento que inclui dicas para começar a usar o aplicativo para os usuários que o integraram.
- Um e-mail de acompanhamento para solicitar aos usuários que concluam a integração.
- Uma [pesquisa]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/templates/simple_survey) com várias perguntas para determinar as preferências do usuário.

## Adaptar o modelo às suas necessidades

Digamos que estejamos trabalhando para a StyleRyde, um aplicativo de compartilhamento de carona sob demanda que leva as pessoas aonde elas precisam ir. Antes de criar o Canvas, configuramos [uma pesquisa simples]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog) que inclui uma série de perguntas envolventes para determinar a experiência e a impressão da primeira viagem de um usuário com o aplicativo.

Para acessar o modelo, ao criar um novo Canvas, selecione **Usar um modelo de Canvas** > **Modelos do Braze**. Em seguida, ao lado de **Onboarding with preferences survey**, selecione **Apply Template (Aplicar modelo**). Agora, podemos examinar o modelo para adequá-lo às nossas necessidades.

### Etapa 1: Configurar os detalhes

Vamos ajustar os detalhes do Canvas para refletir nosso objetivo.

1. Selecione **Editar** ao lado do nome do modelo.

\![O título e a descrição atuais do Canvas.]({% image_buster /assets/img/canvas_templates/preference_survey1.png %}){: style="max-width:50%;"}

{:start="2"}
2\. Atualize o nome do Canvas para especificar que o Canvas é para segmentar novos usuários quando eles usam o aplicativo pela primeira vez.
3\. Atualize a descrição para explicar que esse Canvas contém mensagens personalizadas.
4\. Adicione a tag **Onboarding** para que possamos filtrá-la na página inicial do Canvas.

\![O novo nome, descrição e tag do Canvas.]({% image_buster /assets/img/canvas_templates/preference_survey2.png %}){: style="max-width:90%;"}

### Etapa 2: Atribuir eventos de conversão

Atualize o **evento de conversão primário - A** para **Performs Custom Event**. Em seguida, selecione **Last Used App (Último aplicativo usado** ) para o evento personalizado.

\![Last Used App como o nome do evento personalizado selecionado para o evento de conversão.]({% image_buster /assets/img/canvas_templates/preference_survey3.png %}){: style="max-width:90%;"}

### Etapa 3: Adaptar o cronograma de entrada

Vamos manter a programação de entrada como **Action-Based** para que os usuários entrem em nosso Canvas quando iniciarem uma sessão no aplicativo. Dessa forma, podemos começar a construir nosso relacionamento com um engajamento oportuno.

Faremos uma atualização nessa seção, ajustando a **Entry Window** para a data e hora desejadas.

Seção "Janela de inscrição" com o horário de início em 30 de janeiro de 2025 às 12 horas.]({% image_buster /assets/img/canvas_templates/preference_survey4.png %}){: style="max-width:90%;"}

### Etapa 4: Selecione o público-alvo

Manteremos o público-alvo como está, para atingir nossos usuários que usaram o aplicativo StyleRyde pela primeira vez há menos de um dia.

O filtro "First used these apps less than 1 days ago" (Primeiro uso desses aplicativos há menos de 1 dia) foi selecionado para atingir o público-alvo de entrada.]({% image_buster /assets/img/canvas_templates/preference_survey5.png %}){: style="max-width:90%;"}

### Etapa 5: Selecione suas configurações de envio

Manteremos as configurações de assinatura padrão, de modo que enviaremos apenas aos usuários que se inscreveram ou optaram por receber mensagens ou notificações com o Quiet Hours ativado e ignoraremos as outras configurações (limite de frequência e grupos de sementes).

Seção "Send Settings" (Configurações de envio) com as configurações de assinatura para usuários que estão inscritos ou optaram por participar com o Quiet Hours ativado entre 12 e 20 horas.]({% image_buster /assets/img/canvas_templates/preference_survey6.png %}){: style="max-width:90%;"}

### Etapa 6: Personalize seu Canvas

Agora, criaremos nosso Canvas personalizando o conteúdo que será enviado aos usuários. 

1. Para a primeira etapa da mensagem **Welcome Email**, atualizaremos essa etapa para incluir nosso e-mail de boas-vindas do StyleRyde.
2. Em seguida, manteremos a etapa Action Path como está. Essa etapa divide nossos usuários em dois grupos em um período de três dias:

- Usuários que iniciaram uma sessão ou clicaram no e-mail de integração
- Usuários que não iniciaram uma sessão ou clicaram no e-mail de integração

Uma etapa do Action Path dividida em dois caminhos, um para os usuários que iniciaram uma sessão e outro para todos os outros.]({% image_buster /assets/img/canvas_templates/preference_survey8.png %}){: style="max-width:50%;"}

A partir daí, direcionaremos nossos usuários e mensagens com base nos grupos mencionados acima.

#### Segmente seus usuários engajados

Para nossos usuários que iniciaram uma sessão ou se envolveram com nosso e-mail de integração a partir da primeira etapa da Mensagem, atualizaremos a etapa da Mensagem de **dicas de introdução** para incluir as dicas essenciais de viagem e segurança para nossos novos usuários do StyleRyde.

Depois que um usuário concluir a integração, ele sairá do Canvas.

Em seguida, atualize a etapa **Content Preferences Survey** Message para incluir nossa pesquisa de preferências que solicita que nossos usuários selecionem os tópicos sobre os quais têm interesse em receber informações no futuro.

Uma visualização da pesquisa de preferências que solicita que os usuários selecionem todos os interesses que se aplicam.]({% image_buster /assets/img/canvas_templates/preference_survey7.png %}){: style="max-width:90%;"}

#### Incentivar os usuários que não iniciaram a integração 

Para nossos outros usuários, atualizaremos a etapa **Winback Nudge** Message com nosso e-mail de acompanhamento para solicitar que os usuários concluam a integração.

Como nossa última etapa para reengajamento, renomearemos a **Etapa 2** para **Final Winback Nudge** e atualizaremos a etapa com nossa mensagem no aplicativo para solicitar que nossos novos usuários concluam a integração.

### Etapa 7: Teste e inicie seu Canvas

Depois de testar e revisar nosso Canvas para garantir que ele funcione conforme o esperado, nós o iniciaremos selecionando **Launch Canvas**.

{% alert tip %}
Confira nossa [lista de verificação pré e pós-lançamento]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) para saber o que considerar antes e depois de lançar um Canvas.
{% endalert %}