---
nav_title: Configurar com o Klaviyo
article_title: Configurar com o Klaviyo para o BrazeAI Decisioning Studio
page_order: 3
description: "Saiba como configurar um Klaviyo Flow para uso com o BrazeAI Decisioning <sup>StudioTM</sup> Acessar."
toc_headers: h2
---

# Configurar com o Klaviyo para o BrazeAI Decisioning Studio™ Acessar

> Configure um modelo de espaço reservado e um fluxo no Klaviyo para disparar ativações por meio do BrazeAI Decisioning Studio™ Acessar.

{% alert important %}
É necessário criar um novo fluxo no Klaviyo para cada novo experimentador que você configurar. Se você tiver criado anteriormente um fluxo de espaço reservado para importar seus modelos, deverá criar um novo fluxo e não poderá reutilizar o fluxo de espaço reservado anterior.
{% endalert %}

Antes de criar um fluxo no Klaviyo, você deve ter os seguintes detalhes do seu portal BrazeAI Decisioning Studio™ Acessar para referência:

- Nome do fluxo
- Nome do evento de gatilho

## Criação de um modelo de espaço reservado no Klaviyo

O BrazeAI Decisioning Studio™ Acessar importa modelos que estão associados a fluxos existentes em sua conta Klaviyo. Para usar um modelo que não esteja associado a nenhum fluxo, você pode criar um fluxo de espaço reservado contendo os modelos que gostaria de usar. O fluxo pode ser deixado como um rascunho; não precisa ser ao vivo.

### Etapa 1: Configure seu fluxo

{% alert note %}
A finalidade desses fluxos de espaço reservado é importar seu conteúdo desejado para o BrazeAI Decisioning Studio™ Acessar. É necessário criar um fluxo separado em uma etapa posterior, que o BrazeAI Decisioning Studio™ Acessar usa para disparar as ativações quando o experimentador estiver ativo.
{% endalert %}

1. No Klaviyo, selecione **Flows (Fluxos**). 
2. Selecione **Criar fluxo** > **Criar do zero**.
3. Dê ao fluxo de espaço reservado um nome que você reconheça e, em seguida, selecione **Criar fluxo**.

![Um fluxo chamado "OFE Placeholder Flow".]({% image_buster /assets/img/decisioning_studio_go/create_flow.png %})

{: start="4"}
4\. Selecione qualquer disparador e salve o fluxo.
5\. Selecione **Confirmar e salvar**. 

### Etapa 2: Criar o modelo de espaço reservado

Em seguida, crie o modelo de espaço reservado: 

1. Arraste e solte um nó **de e-mail** após o **disparador**.

![Um fluxo com um nó de disparo seguido de um nó de e-mail.]({% image_buster /assets/img/decisioning_studio_go/set_up_email_node.png %})

{: start="2"}
2\. No nó **E-mail**, selecione **Selecionar modelo**.
3\. Em seguida, escolha o modelo a ser usado e selecione **Usar modelo**.
4\. Selecione **Salvar** > **Concluído**.
5\. (Opcional) Para adicionar mais modelos a serem usados no BrazeAI Decisioning Studio™ Acessar, adicione outro nó **de e-mail** e repita as etapas 2 a 4.
6\. Deixe todos os e-mails no modo **Rascunho** e saia do Flow.

No portal do BrazeAI Decisioning Studio™ Acessar, seus modelos devem ser selecionáveis em seu fluxo de espaço reservado.

![Um exemplo de um modelo Klaviyo de espaço reservado no portal do Decisioning Studio Acessar.]({% image_buster /assets/img/decisioning_studio_go/placeholder_flow.png %})

## Criação de um fluxo no Klaviyo

### Etapa 1: Configurar o fluxo

1. No Klaviyo, selecione **Flows** > **Create flow**( **Fluxos** > **Criar fluxo**).
2. Selecione **Construir o seu próprio**.
3. Para **Nome**, digite o nome do fluxo de seu portal BrazeAI Decisioning Studio™ Acessar. Em seguida, selecione **Criar manualmente**.

![A opção "Criar manualmente" foi selecionada para um fluxo de exemplo.]({% image_buster /assets/img/decisioning_studio_go/flow1.png %}){: style="max-width:50%;"}

{: start="4"}
4\. Selecione o disparador.
5\. Faça a correspondência entre o nome da métrica e o nome do evento de gatilho de seu portal BrazeAI Decisioning Studio™ Acessar.

![Um exemplo de nome de métrica que corresponde ao nome do evento de gatilho "OFE_TEST_CASE_API_EVENT_TRIGGER".]({% image_buster /assets/img/decisioning_studio_go/flow2.png %})

{: start="6"}
6\. Selecione **Salvar**.

{% alert note %}
Se o seu experimentador tiver um modelo de base, prossiga para as etapas a seguir. Se o seu experimentador tiver dois ou mais modelos básicos, pule para [Etapa 3: Adicione uma divisão de disparo ao seu fluxo](#step-3-add-a-trigger-split-to-your-flow).
{% endalert %}

### Etapa 2: Adicione um e-mail ao seu fluxo 

1. Arraste e solte um nó **de e-mail** após o nó **Trigger**.
2. Nos **detalhes do e-mail**, selecione **Selecionar modelo**.

![Opção "Select template" (Selecionar modelo) na seção "Email details" (Detalhes do e-mail).]({% image_buster /assets/img/decisioning_studio_go/flow3.png %})

{: start="3"}
3\. Encontre e selecione seu modelo básico. É possível procurar seu modelo pelo nome do modelo na seção **Recursos a serem usados** do portal BrazeAI Decisioning Studio™ Acessar.

![Um exemplo de modelo básico no Klaviyo.]({% image_buster /assets/img/decisioning_studio_go/flow4.png %})

{: start="4"}
4\. Selecione **Usar modelo** > **Salvar**.
5\. Na **linha de assunto**, digite {% raw %}`{{event.SubjectLine}}`{% endraw %}.
6\. Para **Nome do remetente** e **Endereço de e-mail do remetente**, digite os detalhes que deseja usar.

![Um exemplo de linha de assunto, nome do remetente e endereço de e-mail do remetente para "E-mail 1".]({% image_buster /assets/img/decisioning_studio_go/flow5.png %})

{: start="7"}
7\. Selecione **Concluído**.
8\. Desmarque a caixa de seleção **Ignorar perfis enviados recentemente por e-mail** e selecione **Salvar**.
9\. No nó de e-mail, atualize o modo de **Rascunho** para **Ativo**.

![O editor de fluxo do Klaviyo mostra um nó de disparo conectado a um nó de e-mail.]({% image_buster /assets/img/decisioning_studio_go/flow6.png %})

Está tudo pronto! Agora você pode disparar ativações por meio do BrazeAI Decisioning Studio™ Acessar. 

### Etapa 3: Adicione uma divisão de disparo ao seu fluxo 

1. Arraste e solte um nó **de divisão de disparo** após o **nó de disparo**.
2. Selecione o nó de **divisão Trigger** e defina a **Dimensão** como **EmailTemplateID**.

![Diagrama de fluxo do Klaviyo mostrando um nó de disparo alimentando uma divisão de disparo configurada com Dimension EmailTemplateID.]({% image_buster /assets/img/decisioning_studio_go/flow7.png %})

#### Etapa 3.1: Adicione seu modelo de e-mail

1. No portal do BrazeAI Decisioning Studio™ Acessar, encontre a **ID do envio de e-mail** para seu primeiro modelo na seção **Recursos a serem usados**. Digite o **ID do modelo de e-mail** para o campo **Dimensão** e, em seguida, selecione **Salvar**.
2. Arraste e solte um nó de **e-mail** no ramo **Yes** da **divisão Trigger**. 

![Um fluxo do Klaviyo com um nó de divisão de disparo, que tem um ramo Sim que leva a um nó de e-mail e um ramo Não que se conecta a outra divisão de disparo.]({% image_buster /assets/img/decisioning_studio_go/flow8.png %})

{: start="3"}
3\. Nos **detalhes do e-mail**, selecione **Selecionar modelo**.
4\. Encontre e selecione seu modelo básico. É possível procurar seu modelo pelo nome do modelo base na seção **Recursos a serem usados** do portal BrazeAI Decisioning Studio™ Acessar.
5\. Selecione **Usar modelo** > **Salvar**.
6\. Na **linha de assunto**, digite {% raw %}`{{event.SubjectLine}}`{% endraw %}.
7\. Para **Nome do remetente** e **Endereço de e-mail do remetente**, digite os detalhes que deseja usar.

![Um modelo de e-mail selecionado e campos para a linha de assunto, o nome do remetente e o endereço de e-mail do remetente.]({% image_buster /assets/img/decisioning_studio_go/flow5.png %})

{: start="8"}
8\. Selecione **Concluído**.
9\. Desmarque a caixa de seleção **Ignorar perfis enviados recentemente por e-mail** e selecione **Salvar**.
10\. No nó de e-mail, atualize o modo de **Rascunho** para **Ativo**.

#### Etapa 3.2: Adicionar uma nova divisão de disparo

Em seguida, crie uma nova **divisão de disparo** e um novo nó de **e-mail** para cada modelo de base adicional que seu experimentador usará. 

1. Arraste e solte outro nó de **divisão Trigger** no ramo **No do** nó de **divisão Trigger** anterior.
2. Defina a **Dimensão** como **EmailTemplateID** e preencha o valor **da Dimensão** com o **ID** do modelo **de e-mail** do modelo básico que está configurando.
3. Selecione **Salvar**.

![Diagrama de um editor de fluxo do Klaviyo mostrando um nó Trigger que leva a uma divisão Trigger. A divisão do disparador tem um ramo Sim que leva a um nó de e-mail e um ramo Não que se conecta a outra divisão do disparador que leva a nós de e-mail adicionais.]({% image_buster /assets/img/decisioning_studio_go/flow9.png %})

{: start="4"}
4\. Arraste e solte um nó de **e-mail** no ramo **Yes (Sim** ) de sua nova divisão de disparo.
5\. Repita as etapas 1 a 5 da [Etapa 3.1](#step-31-add-your-email-template) para selecionar o modelo correspondente.
5\. Defina a **linha de assunto** como {% raw %}`{{event.SubjectLine}}`{% endraw %} e desmarque a caixa de seleção **Ignorar perfis enviados recentemente por e-mail**.
6\. Repita esse processo até ter um nó de **divisão de disparo** e um nó **de e-mail** para cada modelo de base que seu experimentador estiver usando. Sua última divisão do disparador não deve ter nada na ramificação "Não".

![Um fluxo do Klaviyo com vários nós de divisão de disparo que se ramificam para vários nós de e-mail.]({% image_buster /assets/img/decisioning_studio_go/flow10.png %})

{: start="7"}
7\. Em cada um de seus nós **de e-mail**, atualize o modo de **Rascunho** para **Ativo**.

![A opção de atualizar o status do nó para "Live".]({% image_buster /assets/img/decisioning_studio_go/flow11.png %})

Está tudo pronto! Agora você pode disparar ativações por meio do BrazeAI Decisioning Studio™ Acessar. 