---
nav_title: Integração com Pesquisa de Preferências
article_title: Integração com Pesquisa de Preferências
page_order: 5.5
page_type: reference
description: "Este artigo descreve como usar um modelo Canvas do Braze para impulsionar a adoção inicial com um fluxo de integração guiado para apresentar novos usuários à sua marca e coletar preferências para mantê-los engajados a longo prazo."
tool: Canvas
---

# Integração com pesquisa de preferências

> Use a integração com o modelo de pesquisa de preferências para criar um fluxo de integração guiado que tenha como alvo novos usuários. Apresente sua marca a eles, ajude-os a começar e colete suas preferências para mantê-los engajados a longo prazo.

Este artigo irá guiá-lo através de um caso de uso para o modelo **Integração com Pesquisa de Preferências**, que é projetado para a fase de consideração do ciclo de vida do usuário. Quando você terminar, terá criado um canva que envia e-mails e mensagens no app para os usuários quando eles iniciam uma sessão e quando não completaram sua integração.

## Pré-requisitos

Para usar esse modelo com sucesso, você precisará do seguinte:

- Um e-mail de boas-vindas que incentiva os usuários a começarem a integração.
- Um e-mail de acompanhamento que inclui dicas para começar a usar o app para usuários que se cadastraram.
- Um e-mail de acompanhamento para incentivar os usuários a completarem sua integração.
- Uma [pesquisa]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/templates/simple_survey) contendo várias perguntas para determinar as preferências dos usuários.

## Adaptar o modelo às suas necessidades

Vamos dizer que estamos trabalhando para StyleRyde, um app de caronas sob demanda que leva as pessoas aonde elas precisam ir. Antes de criar o canva, [configuramos uma pesquisa simples]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog) que inclui uma série de perguntas envolventes para determinar a experiência e a impressão da primeira viagem de um usuário com o app.

Para acessar o modelo, ao criar um novo canva, selecione **Usar um modelo do canvas** > **Modelos da Braze**. Em seguida, ao lado de **Integração com Pesquisa de Preferências**, selecione **Aplicar modelo**. Agora, podemos examinar o modelo para adequá-lo às nossas necessidades.

### Etapa 1: Configurar os detalhes

Vamos ajustar os detalhes do Canva para refletir nosso objetivo.

1. Selecione **Editar** ao lado do nome do modelo.

![O título e a descrição atuais do Canva.]({% image_buster /assets/img/canvas_templates/preference_survey1.png %}){: style="max-width:50%;"}

{:start="2"}
2\. Atualize o canva para especificar que o canva é para direcionamento de novos usuários quando eles usam o app pela primeira vez.
3\. Atualize a descrição para explicar que esse Canva contém envio de mensagens personalizadas.
4\. Adicione a tag **Integração** para que possamos filtrá-la na página inicial do Canva.

![O novo nome, a descrição e a tag do Canva.]({% image_buster /assets/img/canvas_templates/preference_survey2.png %}){: style="max-width:90%;"}

### Etapa 2: Atribuir eventos de conversão

Atualizar o **Evento de conversão primária – A** para **Executa evento personalizado**. Em seguida, selecione o **Usou o app pela última vez** para o evento personalizado.

![Último uso do app como o nome do evento personalizado selecionado para o evento de conversão.]({% image_buster /assets/img/canvas_templates/preference_survey3.png %}){: style="max-width:90%;"}

### Etapa 3: Adaptar o cronograma de entrada

Vamos manter o cronograma de entrada como **Baseado em ação** para que os usuários entrem em nosso canva quando iniciarem uma sessão no app. Dessa forma, podemos começar a construir nosso relacionamento com engajamento oportuno.

Faremos uma atualização nesta seção ajustando o **Período de entrada** para a data e hora desejadas.

![Seção "Período de entrada" com o horário de início 30 de janeiro de 2025 às 12h.]({% image_buster /assets/img/canvas_templates/preference_survey4.png %}){: style="max-width:90%;"}

### Etapa 4: Selecione o público-alvo

Manteremos o público-alvo como está para direcionar nossos usuários que usaram o app StyleRyde pela primeira vez há menos de um dia.

![O filtro "Usou estes apps pela primeira vez há menos de 1 dia" selecionado para direcionar o público de entrada.]({% image_buster /assets/img/canvas_templates/preference_survey5.png %}){: style="max-width:90%;"}

### Etapa 5: Selecione suas configurações de envio

Manteremos as configurações de inscrição padrão, para que enviemos apenas para usuários que se inscreveram ou optaram por receber mensagens ou notificações com o horário de silêncio ativado, e ignoraremos as outras configurações (limitação de frequência e grupos de semente).

![Seção "Enviar Configurações" com as configurações de inscrição para usuários que estão inscritos ou optaram por participar com o Horário de Silêncio ativado entre 12h e 20h.]({% image_buster /assets/img/canvas_templates/preference_survey6.png %}){: style="max-width:90%;"}

### Etapa 6: Personalize sua tela

Agora, vamos construir nosso canva personalizando o conteúdo que será enviado aos usuários. 

1. Para a primeira etapa da mensagem **Envio de e-mail de boas-vindas**, atualizaremos esta etapa para incluir nosso e-mail de boas-vindas do StyleRyde.
2. Em seguida, manteremos a etapa do Caminho da Ação como está. Esta etapa divide nossos usuários em dois grupos em um intervalo de três dias:

- Usuários que iniciaram uma sessão ou clicaram no e-mail de integração
- Usuários que não iniciaram uma sessão ou clicaram no e-mail de integração

![Um passo da jornada de ação dividido em dois caminhos, com um para usuários que iniciaram uma sessão e outro para todos os outros.]({% image_buster /assets/img/canvas_templates/preference_survey8.png %}){: style="max-width:50%;"}

A partir daqui, vamos direcionar nossos usuários e envio de mensagens com base nos grupos mencionados anteriormente.

#### Direcione seus usuários engajados

Para nossos usuários que iniciaram uma sessão ou interagiram com nosso e-mail de integração a partir da primeira etapa da Mensagem, atualizaremos a etapa da mensagem **Dicas para começar** para incluir as dicas essenciais de viagem e segurança para nossos novos usuários do StyleRyde.

Depois que um usuário concluir sua integração, ele sairá do canva.

Em seguida, atualize a etapa da mensagem **Pesquisa de preferências de conteúdo** para incluir nossa pesquisa de preferências que solicita aos nossos usuários que selecionem quais tópicos estão interessados em receber informações no futuro.

![Uma prévia da pesquisa de preferências que solicita aos usuários que selecionem todos os interesses que se aplicam.]({% image_buster /assets/img/canvas_templates/preference_survey7.png %}){: style="max-width:90%;"}

#### Empurre os usuários que não começaram a integração 

Para nossos outros usuários, atualizaremos a etapa da mensagem **Lembrete de recuperação** com nosso e-mail de acompanhamento para incentivar os usuários a completarem sua integração.

Como nosso última etapa para re-engajamento, vamos renomear a **Etapa 2** como **Lembrete final de recuperação** e atualizar a etapa com nossa mensagem no app para incentivar nossos novos usuários a concluir a integração.

### Etapa 7: Teste e inicie seu Canva

Depois de testar e revisar nosso Canvas para garantir que ele funcione conforme o esperado, nós o iniciaremos selecionando **Lançar canva**.

{% alert tip %}
Confira nossa [lista de verificação pré e pós-lançamento]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) para saber o que considerar antes e depois de lançar um Canva.
{% endalert %}