---
nav_title: OneTrust
article_title: OneTrust
description: "Este artigo de referência descreve a parceria entre a Braze e a OneTrust, um provedor de software de privacidade e segurança de dados, permitindo que você use o criador de fluxos de trabalho da OneTrust para criar fluxos de trabalho de segurança para o seu produto."
alias: /partners/onetrust/
page_type: partner
search_tag: Partner

---

# OneTrust

> A [OneTrust](https://www.onetrust.com/) é um provedor de software de privacidade e segurança que fornece a visibilidade necessária para entender melhor seu cenário de confiança, ações para aproveitar insights poderosos e automação para manter sua empresa à frente da concorrência. 

_Essa integração é mantida pela OneTrust._

## Sobre a integração

A integração entre o Braze e a OneTrust permite que você use o construtor de fluxo de trabalho da OneTrust para criar fluxos de trabalho de segurança para o seu produto.
## Pré-requisitos

| Solicitações | Descrição |
|---|---|
| Conta OneTrust | Uma [OneTrust](https://www.onetrust.com/) conta para aproveitar esta parceria. |
| chave de API Braze | Uma chave da API REST da Braze com as permissões necessárias para o endpoint que sua ação da OneTrust usará.<br><br>Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
| Instância do Braze | Sua instância do Braze pode ser obtida com seu gerente de integração do Braze ou pode ser encontrada na [página de visão geral da API]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração

A seguinte integração fornece orientação sobre como criar um fluxo de trabalho de atualização de consentimento do usuário e um fluxo de trabalho de exclusão de usuário. Para mais detalhes sobre os endpoints adicionais suportados pelo Braze, consulte [Outras ações suportadas](#Other-supported-actions).

### Adicione credenciais da Braze ao OneTrust

No menu **Integrations** (Integrações) da OneTrust, navegue até **Credentials** (Credenciais) > botão **Add New** (Adicionar novo) para abrir a tela **Select System** (Selecionar sistema). Agora encontre **Braze** e clique no botão **Next** (Avançar).

Siga as instruções na tela **Insira os Detalhes das Credenciais** e forneça as seguintes informações. Salve suas credenciais quando terminar.
  - Nome da credencial
  - Defina o tipo de conector para **Web App**
  - Nome do host: `<your-braze-instance-url>`
  - **Cabeçalho da solicitação**:
    - **Autorização**: portador
    - **Tipo de Conteúdo**: application/json
  - Token: `<your-braze-api-key>`

### Adicionar Braze como um sistema

#### Etapa 1: Criar um fluxo de trabalho

{% tabs %}
{% tab Atualização de Consentimento do Usuário %}
1. No menu de integrações do OneTrust, navegue para **Galeria** > **Braze** > **Adicionar** para criar um novo fluxo de trabalho.![]({% image_buster /assets/img/onetrust/onetrust.png %})<br><br>
2. Forneça um nome e um e-mail de notificação no modal de fluxo de trabalho. Clique no botão **Create** (Criar). Na criação, você verá o construtor de fluxo de trabalho. Seu fluxo de trabalho Braze será preenchido com chamadas e ações de API que podem ser usadas para processar solicitações de exclusão. <br><br>
3. No construtor de fluxo de trabalho, escolha a ação que você deseja disparar no fluxo de trabalho.<br>![]({% image_buster /assets/img/onetrust/onetrust2.png %})

{% endtab %}
{% tab Exclusão de Usuário %}

1. No menu de integrações do OneTrust, navegue para **Galeria** > **Braze** > **Adicionar** para criar um novo fluxo de trabalho.![]({% image_buster /assets/img/onetrust/onetrust.png %})<br><br>
2. Forneça um nome e um e-mail de notificação no modal de fluxo de trabalho. Clique no botão **Create** (Criar). Na criação, você verá o construtor de fluxo de trabalho. Seu fluxo de trabalho Braze será preenchido com chamadas e ações de API que podem ser usadas para processar solicitações de exclusão. <br><br>
3. No construtor de fluxo de trabalho, escolha a ação que você deseja disparar no fluxo de trabalho.<br>![]({% image_buster /assets/img/onetrust/onetrust8.png %})
{% endtab %}
{% endtabs %}

#### Etapa 2: Selecionar ação
{% tabs %}
{% tab Atualização de Consentimento do Usuário %}

1. Quando terminar, clique em **Done** (Concluído) e escolha **Add Action** (Adicionar ação). Nota que a ação que você escolher dependerá do tipo de preferência que está sendo atualizada e do seu endpoint preferido.
- Para atualizar as preferências globais de inscrição de um usuário, escolha a ação **POST User track - attributes** (POST monitoramento de usuários – atributos).
- Para atualizar as preferências do grupo de inscrições de um usuário, escolha a ação **POST User Track - Attributes** (POST monitoramento de usuário – atributos) ou a ação **POST Set Users Subscription Group Status** (POST definir status de grupo de inscrição de usuário).<br>![]({% image_buster /assets/img/onetrust/onetrust4.png %})<br><br>
2. Escolha a ação desejada, selecione suas credenciais da Braze pré-criadas e clique em **Next** (Avançar).<br>![]({% image_buster /assets/img/onetrust/onetrust5.png %})

{% endtab %}
{% tab Exclusão de Usuário %}

1. Quando terminar, clique em **Done** (Concluído) e escolha **Add Action** (Adicionar ação).
- Para excluir um usuário da Braze, escolha a ação **POST User Delete Action** (POST ação de exclusão de usuário).
<br>![]({% image_buster /assets/img/onetrust/onetrust9.png %})<br><br>
2. Escolha a ação desejada, selecione suas credenciais da Braze pré-criadas e clique em **Next** (Avançar).<br>![]({% image_buster /assets/img/onetrust/onetrust5.png %})

{% endtab %}
{% endtabs %}
#### Etapa 3: atualize o corpo da solicitação
{% tabs %}
{% tab Atualização de Consentimento do Usuário %}

1. Atualize o corpo para incluir quaisquer valores dinâmicos necessários. Confira se o corpo da ação corresponde ao [endpoint `/users/track`](https://www.braze.com/docs/api/endpoints/user_data/post_user_track/) e ao [endpoint `/subscription/status/set`](https://www.braze.com/docs/api/endpoints/subscription_groups/post_update_user_subscription_group_status/).
2. Personalize o fluxo de trabalho com parâmetros adicionais ou lógica condicional para atender às necessidades da sua organização.
3. Quando terminar de editar, clique em **Concluir** e depois em **Ativar** para ativar o fluxo de trabalho.

{% alert note %}
Ao usar os fluxos de trabalho do OneTrust para atualizar as preferências do grupo de inscrições no Braze, o `subscription_group_id` deve corresponder ao ID definido pelo Braze quando o grupo de inscrições foi criado. Você pode acessar o `subscription_group_id` de um grupo de inscrições navegando até a página **Grupo de Inscrições** no dashboard do Braze.
{% endalert %}

![]({% image_buster /assets/img/onetrust/onetrust6.png %})

{% endtab %}
{% tab Exclusão de Usuário %}

1. Atualize o corpo para incluir quaisquer valores dinâmicos necessários. Confira se o corpo da ação corresponde ao [endpoint `/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/).
2. Quando terminar de editar, selecione **Concluir** e depois **Ativar** para ativar o fluxo de trabalho.

![]({% image_buster /assets/img/onetrust/onetrust10.png %})

#### Atualizar o fluxo de trabalho da solicitação do titular dos dados
1. No menu **Privacy Rights Automation** (Automação de direitos de privacidade), selecione **Workflows** (Fluxos de trabalho). 
2. Selecione o fluxo de trabalho que você deseja atualizar com a integração Braze. 
3. Selecione o botão **Edit** (Editar) para ativar a edição.
4. Em seguida, selecione a etapa do fluxo de trabalho para adicionar a integração da Braze e clique em **Add Connection** (Adicionar conexão).
5. Adicione o fluxo de trabalho Braze criado anteriormente como uma subtarefa do sistema.

{% endtab %}
{% endtabs %}

## Outras ações suportadas

Além das ações **POST User track - Attributes** (POST monitoramento de usuário – atributos), **POST Set Users Subscription Group Status** (POST definir status do grupo de inscrições de usuário) e **POST User Delete** (POST exclusão de usuário), a Braze oferece outros endpoints que podem ser usados para criar fluxos de trabalho personalizados e usados como subtarefas dentro de fluxos de trabalho existentes. 

Para ver uma lista completa de ações suportadas:
1. No OneTrust, clique em **Systems** no menu **Integrations**. 
2. Escolha o sistema **Braze**.
3. Navegue até a guia **Actions** (Ações).

![]({% image_buster /assets/img/onetrust/onetrust7.png %})


