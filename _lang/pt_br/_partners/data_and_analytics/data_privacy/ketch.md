---
title: Ketch
nav_title: Ketch
description: "Este artigo de referência aborda a integração entre a Braze e a Ketch. A Ketch fornece operações de privacidade simplificadas e controle de dados completo, dinâmico e inteligente."
alias: /partners/ketch
page_type: partner
search_tag: Ketch
---

# Ketch

> [Ketch](https://www.ketch.com) permite que as empresas sejam administradoras responsáveis por seus dados. A Ketch fornece operações de privacidade simplificadas e controle de dados completo, dinâmico e inteligente. 

_Essa integração é mantida pela Ketch._

## Sobre a integração

A integração Braze e Ketch permite que você controle as preferências de comunicação do cliente na Central de Preferências Ketch e propague automaticamente essas alterações para o Braze. 

{% alert note %}
Procurando orientação sobre como criar grupos de inscrição? Confira nossos artigos para <a href='/docs/user_guide/message_building_by_channel/sms/sms_subscription_group/'>grupos de inscrição por SMS</a> e <a href='/docs/user_guide/message_building_by_channel/email/managing_user_subscriptions/'>grupos de inscrição por e-mail</a>.
{% endalert %}

## Pré-requisitos

| Solicitações | Descrição |
|---|---|
| Conta Ketch | Uma conta [Ketch](https://www.ketch.com) com privilégios de administrador é necessária para ativar esta integração. |
| chave de API Braze | Uma chave da API REST da Braze com as permissões `users.track`, `subscription.status.get`, `subscription.status.set`, `users.delete`, `users.alias.new`, `users.export.ids`, `email.unsubscribe` e `email.blacklist`. <br><br> Ela pode ser criada no dashboard da Braze (**Console de desenvolvedor** > **Chave da API REST** > **Criar nova chave de API**). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração

### Etapa 1: Configure a conexão Braze

1. Na sua [instância do Ketch](https://app.ketch.com), navegue até **Sistemas de Dados** e selecione **Braze**. Em seguida, clique em **Nova Conexão**.
2. Dê à sua conexão da Braze um nome identificável, que será usado para se referir a essa conexão em processos baseados em API. Nota que um código também será criado para essa conexão. Este código deve ser único em todas as conexões.
3. Confirme o mapeamento de identidade de seus usuários. Por padrão, o Ketch mapeará as identidades dos usuários pelo endereço de e-mail do usuário ou pelo `external_id` no Braze.
4. Adicione a chave de API da Braze e forneça o endpoint da API. Note que o [endpoint da API]({{site.baseurl}}/api/basics/#endpoints) é baseado em qual instância da Braze sua organização usa.

### Etapa 2: configure as preferências de inscrição

1. Acessar **Policy Center > Subscriptions** (Central de políticas > Inscrições). Se você não vir a guia de assinaturas em **Central de Políticas**, certifique-se de que você tem acesso à Central de Preferências de marketing e verifique se você tem as permissões de conta corretas para acessar esta parte do produto.
2. Clique **Criar Nova Inscrição** para criar um novo tópico. Cada inscrição terá um nome e um código.
3. Adicione os canais para enviar seus tópicos de inscrição. Cada canal será exibido na Central de Preferências de marketing para seus usuários. Você também pode adicionar os detalhes de como deseja que a Central de Preferências do Ketch orquestre um sinal específico de aceitação ou recusa.
4. Selecione a conexão Braze que você gostaria de usar para orquestrar os sinais de aceitação e recusa.
5. Insira o Braze `subscription_group_id` para o grupo de inscrições ao qual você deseja enviar as preferências do usuário Ketch.

![ID do grupo de inscrições do Braze.]({% image_buster /assets/img/ketch/ketch1.png %})

{% alert note %}
Para coletar e orquestrar sinais de aceitação e recusa de usuários, as identidades devem ser configuradas corretamente. A Ketch recomenda configurar o e-mail como o identificador para orquestrar os sinais de preferência do usuário para esta integração.
{% endalert %}


### Etapa 3: Configurar identidades

Um usuário só pode ver a central de preferências de marketing quando a Ketch pode confirmar a identidade de preferência de marketing desse usuário. Se o Ketch não conseguir capturar a identidade do usuário corretamente, a página de preferências de marketing não será exibida para esse usuário, pois o Ketch não poderá gerenciar suas preferências de usuário.

1. Para configurar a identidade de preferência de marketing, acessar a página **Configurações** no Ketch e clicar em **Espaço de identidade**. Você precisará criar um novo espaço de identidade ou editar um espaço de identidade existente para atribuir esse espaço de identidade como a identidade de preferência de marketing. Verifique se a tag Ketch implantada na propriedade captura corretamente esse espaço de identidade.
2. Acesse **Experience Server** > **Properties** (Servidor de experiência > Propriedades) e edite a propriedade desejada. No nível de dados dessa propriedade, ative o espaço de identidade personalizado. Em seguida, configure como a identidade de preferência de marketing é capturada neste site.
3. Depois de configurar o espaço de identidade, teste para ver se a Central de Preferências aparece abrindo a Central de Preferências no site onde a tag Ketch foi implantada.


