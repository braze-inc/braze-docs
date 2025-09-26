---
nav_title: Nuvem de vendas do Salesforce
article_title: Gerenciamento de leads com o Salesforce Sales Cloud
page_order: 3
page_type: reference
description: "Saiba como usar os webhooks do Braze para criar e atualizar leads no Salesforce Sales Cloud por meio do endpoint Salesforce sobjects/Lead."
---

# Gerenciamento de leads com o Salesforce Sales Cloud

> A [Salesforce](https://www.salesforce.com/) é uma das principais plataformas de gestão de relacionamento com o cliente (CRM) baseada em nuvem do mundo, projetada para ajudar as empresas a gerenciar todo o processo de vendas, incluindo geração de leads, rastreamento de oportunidades e gerenciamento de contas.<br><br>Esta página demonstra como usar os webhooks do Braze para criar e atualizar leads no Salesforce Sales Cloud por meio de uma integração enviada pela comunidade.

{% alert important %}
Essa é uma integração enviada pela comunidade e não é diretamente suportada pela Braze. Somente os modelos oficiais de webhook fornecidos pelo Braze são compatíveis com o Braze.
{% endalert %}

## Como funciona?

A integração entre o Braze e o Salesforce Sales Cloud usa webhooks do Braze para criar e atualizar leads no Salesforce Sales Cloud por meio do endpoint [sobjects/Lead](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_lead.html) da Salesforce.

Atualmente, o Braze oferece duas integrações com o Salesforce Sales Cloud para os seguintes casos de uso:
1. [Criação de um lead no Salesforce Sales Cloud](#creating-lead)
2. [Atualização de um lead no Salesforce Sales Cloud](#updating-lead)

{% alert note %}
Essa integração serve exclusivamente para atualizar o Salesforce a partir do Braze como parte de seus esforços de aquisição e nutrição de leads. Para sincronizar dados do Salesforce com o Braze, confira o [modelo de dados B2B]({{site.baseurl}}/user_guide/getting_started/b2b_use_cases/b2b_data_models/) ou entre em contato com um de nossos [parceiros de tecnologia]({{site.baseurl}}/partners/home/).
{% endalert %}

## Pré-requisitos

Essa integração exige que você crie um app conectado no Salesforce Sales Cloud seguindo as etapas da documentação do Salesforce: [Configure um aplicativo conectado para o fluxo de credenciais de cliente OAuth 2.0](https://help.salesforce.com/s/articleView?id=sf.connected_app_client_credentials_setup.htm&type=5).

Ao definir as configurações de OAuth necessárias para o app conectado, mantenha todas as configurações de oAuth com seus valores e seleções padrão, exceto as seguintes:
1. Selecione o fluxo **Ativar para o dispositivo**. Você pode deixar o **URL de retorno de chamada** em branco, pois o padrão será um espaço reservado.
2. Para os **escopos OAuth** selecionados, adicione **Gerenciar dados de usuários via APIs (api)**.
3. Selecione **Ativar fluxo de credenciais de cliente**.

## Criação de um lead no Salesforce Sales Cloud {#creating-lead}

Como sua plataforma de engajamento com clientes, o Braze pode gerar novos leads com base nos fluxos de usuários, como o preenchimento de um formulário em uma landing page. Quando isso acontece, você pode usar um webhook do Braze Salesforce Sales Cloud para criar um lead correspondente no Salesforce.

### Etapa 1: Colete seu `client_id` e `client_secret`

1. No Salesforce, acesse **Ferramentas da plataforma** > **Aplicativos** > **Gerenciador de aplicativos**.
2. Encontre seu Braze App recém-criado e selecione **View**.
3. Em **Chave e segredo do consumidor**, selecione **Gerenciar detalhes do consumidor**.
4. Na página resultante, anote sua **Consumer Key** e **Consumer Secret**. A **chave do consumidor** é seu `client_id`, e o **segredo do consumidor** é seu `client_secret`.

### Etapa 2: Configure seu modelo de webhook

Use modelos para reutilizar rapidamente esse webhook em toda a plataforma Braze. 

1. No Braze, acesse **Modelos**, selecione **Modelos de webhook** e, em seguida, selecione **\+ Criar modelo de webhook**.
2. Forneça um nome para o modelo, como "Salesforce Sales Cloud > Criar lead".
3. Na guia **Criador**, insira os seguintes detalhes:

#### Criar webhook 

| Campo | Informações |
| --- | --- |
| URL do webhook | {% raw %}`https://[insert_instance_name].my.salesforce.com/services/data/v60.0/sobjects/Lead/`{% endraw %} |
| Método HTTP | `POST` |
| Corpo da solicitação | Pares de chave-valor JSON |
{: .reset-td-br-1 .reset-td-br-2 role=”presentation” }

#### Valores-chave da propriedade do corpo

Selecione **\+ Adicionar nova propriedade de corpo** para cada um dos pares de chave/valor que você deseja mapear do Braze para o Salesforce. Você pode mapear qualquer campo que desejar, portanto, a tabela a seguir é apenas um exemplo.

| Chave | Valor |
| --- | --- |
| firstName | {% raw %}`{{${first_name}}}`{% endraw %} |
| lastName | {% raw %}`{{${last_name}}}`{% endraw %} |
| email | {% raw %}`{{${email_address}}}`{% endraw %} |
| empresa | {% raw %}`{{custom_attribute.${company}}}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 role=”presentation” }

#### Cabeçalhos da solicitação

Selecione **\+ Add New Header** para cada um dos seguintes cabeçalhos de solicitação.

| Chave | Valor |
| --- | --- |
| Autorização | {% raw %}`{% connected_content https://[insert_instance_name].my.salesforce.com/services/oauth2/token     :method post     :body client_id=[insert_client_id]&client_secret=[insert_client_secret]&grant_type=client_credentials     :save result %}Bearer {{result.access_token}}`{% endraw %} |
| Content-Type | `application/json` |
{: .reset-td-br-1 .reset-td-br-2 role=”presentation” }

{: start="4" }
4\. Selecione **Salvar modelo**.

![Um modelo de webhook preenchido para criar um lead.]({% image_buster /assets/img/b2b/create_lead_webhook.png %}){: style="max-width:70%;"}
 
## Atualização de um lead no Salesforce Sales Cloud {#updating-lead}

Para configurar um webhook do Braze Salesforce Sales Cloud que atualiza os leads no Salesforce, você precisa de um identificador comum entre o Salesforce Sales Cloud e o Braze. O exemplo abaixo usa o Salesforce `lead_id` como o Braze `external_id`, mas você também pode fazer isso usando um `user_alias`. Para obter detalhes sobre isso, consulte [Dados B2B]({{site.baseurl}}/user_guide/getting_started/b2b_use_cases/b2b_data_models)

Este exemplo demonstra especificamente como atualizar o estágio do lead de um lead para "MQL" (Marketing Qualified Lead) depois que um lead ultrapassa um determinado limite de lead. Essa é uma parte essencial do nosso caso de uso do [fluxo de trabalho de pontuação de leads B2B]({{site.baseurl}}/user_guide/getting_started/b2b_use_cases/lead_scoring/).

### Etapa 1: Colete seu `client_id` e `client_secret`

1. No Salesforce, acesse **Ferramentas da plataforma** > **Aplicativos** > **Gerenciador de aplicativos**.
2. Encontre seu Braze App recém-criado e selecione **View**.
3. Em **Chave e segredo do consumidor**, selecione **Gerenciar detalhes do consumidor**.
4. Na página resultante, anote sua **Consumer Key** e **Consumer Secret**.
    - A **chave do consumidor** é seu `client_id`, e o **segredo do consumidor** é seu `client_secret`.

### Etapa 2: Configure seu modelo de webhook

1. No Braze, acesse **Modelos**, selecione **Modelos de webhook** e, em seguida, selecione **\+ Criar modelo de webhook**.
2. Forneça um nome para o modelo, como "Salesforce Sales Cloud > Atualizar lead para MQL".
3. Na guia **Criador**, insira os seguintes detalhes:

#### Criar webhook 

| Campo | Informações |
| --- | --- |
|URL do webhook | {% raw %}`https://[insert_instance_name].my.salesforce.com/services/data/v60.0/sobjects/Lead/{{${user_id}}}`{% endraw %} |
| Método HTTP | `PATCH` |
| Corpo da solicitação | Pares de chave-valor JSON |
{: .reset-td-br-1 .reset-td-br-2 role=”presentation” }

#### Valores-chave da propriedade do corpo

Selecione **\+ Adicionar nova propriedade de corpo** para o seguinte par de chave/valor. Note que `Lead_Stage__c` é um nome de exemplo. O campo personalizado que você usa para rastrear MQLs no Salesforce pode ter um nome diferente, portanto, certifique-se de que eles correspondam.

| Chave | Valor |
| --- | --- |
| `Lead_Stage__c` | `MQL` |
{: .reset-td-br-1 .reset-td-br-2 role=”presentation” }

#### Cabeçalhos da solicitação

Selecione **\+ Add New Header** para cada um dos seguintes cabeçalhos de solicitação.

| Chave | Valor |
| --- | --- |
| Autorização | {% raw %}`{% connected_content https://[insert_instance_name].my.salesforce.com/services/oauth2/token     :method post     :body client_id=[insert_client_id]&client_secret=[insert_client_secret]&grant_type=client_credentials     :save result %}Bearer {{result.access_token}}`{% endraw %} |
| Content-Type | `application/json` |
{: .reset-td-br-1 .reset-td-br-2 role=”presentation” }

{: start="4"}
4\. Selecione **Salvar modelo**.

![Um modelo de webhook preenchido para atualizar um lead.]({% image_buster /assets/img/b2b/update_lead_webhook.png %}){: style="max-width:70%;"}

## Uso desses webhooks em um fluxo de trabalho operacional

Você pode adicionar rapidamente seus modelos a seus fluxos de trabalho operacionais no Braze, como, por exemplo:

1. Parte de uma [nova campanha de usuário](#new-lead) que cria um lead no Salesforce
2. Parte de uma [canva de pontuação de leads](#lead-scoring) que atualiza os usuários que ultrapassaram seu limite de MQL para "MQL" e que atualiza o Salesforce Sales Cloud com as mesmas informações

### Nova campanha de leads {#new-lead}

Para criar um lead no Salesforce quando um usuário fornece seu endereço de e-mail, é possível criar uma campanha que use o modelo de webhook "Atualizar lead" e dispare quando um usuário adicionar seu endereço de e-mail (por exemplo, preencher um formulário da Web).

![Etapa 2 da criação de uma campanha baseada em ação e com a ação-gatilho de "Adicionar um endereço de e-mail".]({% image_buster /assets/img/b2b/salesforce_create_campaign.png %}){: style="max-width:70%;"}

### Canva de pontuação de leads para ultrapassar o limite de Leads Qualificados de Marketing (MQL) {#lead-scoring}

Esse webhook é abordado no caso de uso de [pontuação de leads]({{site.baseurl}}/user_guide/getting_started/b2b_use_cases/lead_scoring/#lead-handoff), mas você também pode verificar se há MQLs e atualizar diretamente o Salesforce no Canvas de pontuação de leads (em vez de criar uma campanha de webhook separada): 

Adicione uma etapa subsequente à sua atualização de usuário para verificar se um usuário ultrapassou o limite de MQL definido. Se eles tiverem cruzado, atualize o status do usuário para "MQL" e, em seguida, atualize o Salesforce com o mesmo status "MQL" usando esse modelo de webhook. O Salesforce cuida do resto, encaminhando esse lead para as equipes de vendas apropriadas usando suas regras de encaminhamento de lead definidas.  

#### Adição da etapa do Canva para verificar os usuários que ultrapassaram o limite de MQL 

1. Adicione uma etapa de **Jornada do público** com dois grupos: "Limite de MQL" e "Todos os demais".
2. No grupo "MQL Threshold" (Limite de MQL), procure todos os usuários que atualmente não tenham um status de "MQL" (por exemplo, `lead_stage` é igual a "Lead"), mas que tenham uma pontuação de lead acima do limite definido (por exemplo, `lead_score` maior que 50). Em caso afirmativo, eles avançam para a próxima etapa; em caso negativo, saem.

![O grupo de jornada do público "MQL Threshold" com filtros para um `lead_stage` igual a "Lead" e um `lead_score` maior que "50".]({% image_buster /assets/img/b2b/salesforce_check_mql.png %}){: style="max-width:70%;"}

{: start="3" }
3\. Adicione uma etapa de **atualização de usuário** que atualize o valor do atributo `lead_stage` do usuário para "MQL".

![A etapa de atualização do usuário "Update to MQL" que atualiza o atributo `lead_stage` para ter um valor de "MQL".]({% image_buster /assets/img/b2b/salesforce_update_mql.png %}){: style="max-width:70%;"}

{: start="4" }
4\. Adicione uma etapa de webhook que atualize o Salesforce com a nova etapa de MQL.

![A etapa do webhook "Update Salesforce" com detalhes concluídos.]({% image_buster /assets/img/b2b/salesforce_webhook.png %}){: style="max-width:70%;"}

Agora seu fluxo do Canvas Flow atualizará os usuários que ultrapassaram seu limite de MQL!

![Uma etapa de atualização do usuário do Canva que verifica se um usuário ultrapassa o limite de MQL e, se o usuário for aprovado, atualiza o Salesforce.]({% image_buster /assets/img/b2b/salesforce_canvas.png %}){: style="max-width:50%;"}

## Solução de problemas

Esses fluxos de trabalho têm capacidade limitada de depuração no Salesforce, portanto, recomendamos consultar o [Registro de atividades de mensagem]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab#message-activity-log) da Braze para descobrir por que um Webhook falhou e se ocorreu algum erro.

Por exemplo, um erro causado por um URL inválido usado para recuperação de token oAuth seria exibido como `https://[insert_instance_name].my.salesforce.com/services/oauth2/token is not a valid URL`.

![Um corpo de resposta de erro informando que o URL não é um URL válido.]({% image_buster /assets/img/b2b/error_message_invalid_url.png %})

