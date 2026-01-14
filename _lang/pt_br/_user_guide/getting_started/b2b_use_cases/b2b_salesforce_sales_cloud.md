---
nav_title: Salesforce Sales Cloud
article_title: Gerenciando leads com o Salesforce Sales Cloud
page_order: 3
page_type: reference
description: "Aprenda a usar webhooks do Braze para criar e atualizar leads no Salesforce Sales Cloud através do endpoint sobjects/Lead do Salesforce."
---

# Gerenciando leads com o Salesforce Sales Cloud

> [Salesforce](https://www.salesforce.com/) é uma das principais plataformas de Gestão de Relacionamento com o Cliente (CRM) baseadas em nuvem do mundo, projetada para ajudar as empresas a gerenciar todo o seu processo de vendas, incluindo geração de leads, rastreamento de oportunidades e gerenciamento de contas.<br><br>Esta página demonstra como usar webhooks do Braze para criar e atualizar leads no Salesforce Sales Cloud através de uma integração submetida pela comunidade.

{% alert important %}
Esta é uma integração submetida pela comunidade e não é suportada diretamente pelo Braze. Apenas os modelos de webhook fornecidos oficialmente pelo Braze são suportados pelo Braze.
{% endalert %}

## Como funciona

A integração entre Braze e Salesforce Sales Cloud usa webhooks do Braze para criar e atualizar leads no Salesforce Sales Cloud através do endpoint [sobjects/Lead](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_lead.html) do Salesforce.

Atualmente, o Braze oferece duas integrações com o Salesforce Sales Cloud para os seguintes casos de uso:
1. [Criando um lead no Salesforce Sales Cloud](#creating-lead)
2. [Atualizando um lead no Salesforce Sales Cloud](#updating-lead)

{% alert note %}
Esta integração é puramente para atualizar o Salesforce a partir do Braze como parte de seus esforços de aquisição e nutrição de leads. Para sincronizar dados do Salesforce de volta para o Braze, confira [modelo de dados B2B]({{site.baseurl}}/user_guide/getting_started/b2b_use_cases/b2b_data_models/) ou conecte-se com um de nossos [parceiros de tecnologia]({{site.baseurl}}/partners/home/).
{% endalert %}

## Pré-requisitos

Esta integração requer que você crie um aplicativo conectado no Salesforce Sales Cloud seguindo os passos na documentação do Salesforce: [Configurar um Aplicativo Conectado para o Fluxo de Credenciais do Cliente OAuth 2.0](https://help.salesforce.com/s/articleView?id=sf.connected_app_client_credentials_setup.htm&type=5).

Ao configurar as configurações necessárias de OAuth para o aplicativo conectado, mantenha todas as configurações de oAuth com seus valores e seleções padrão, exceto pelas seguintes:
1. Selecione **Ativar para dispositivo** fluxo. Você pode deixar **URL de Retorno** em branco, pois ele será definido como um espaço reservado.
2. Para **Escopos OAuth** selecionados, adicione **Gerenciar dados do usuário via APIs (api)**.
3. Selecione **Ativar Fluxo de Credenciais do Cliente**.

## Criando um lead no Salesforce Sales Cloud {#creating-lead}

Como sua plataforma de engajamento do cliente, a Braze pode gerar novos leads com base em fluxos de usuários, como preencher um formulário em uma página de destino. Quando isso acontecer, você pode usar um webhook do Braze Salesforce Sales Cloud para criar um lead correspondente no Salesforce.

### Passo 1: Colete seu `client_id` e `client_secret`

1. No Salesforce, vá para **Ferramentas da Plataforma** > **Aplicativos** > **Gerenciador de Aplicativos**.
2. Encontre seu aplicativo Braze recém-criado e selecione **Visualizar**.
3. Em **Chave do Consumidor e Segredo**, selecione **Gerenciar Detalhes do Consumidor**.
4. Na página resultante, anote sua **Chave do Consumidor** e **Segredo do Consumidor**. A **Chave do Consumidor** é seu `client_id`, e o **Segredo do Consumidor** é seu `client_secret`.

### Passo 2: Configure seu modelo de webhook

Use modelos para reutilizar rapidamente este webhook em toda a plataforma Braze. 

1. No Braze, vá para **Modelos**, selecione **Modelos de Webhook**, e depois selecione **\+ Criar Modelo de Webhook**.
2. Forneça um nome para o modelo, como “Salesforce Sales Cloud > Criar Lead”.
3. Na aba **Compor**, insira os seguintes detalhes:

#### Compor webhook 

| Campo | Detalhes |
| --- | --- |
| URL do webhook | {% raw %}`https://[insert_instance_name].my.salesforce.com/services/data/v60.0/sobjects/Lead/`{% endraw %} |
| Método HTTP | `POST` |
| Corpo da Solicitação | Pares de Chave/Valor JSON |
{: .reset-td-br-1 .reset-td-br-2 role=”presentation” }

#### Valores de chave de propriedade do corpo

Selecione **\+ Adicionar Nova Propriedade de Corpo** para cada um dos pares chave/valor que você deseja mapear do Braze para o Salesforce. Você pode mapear qualquer campo que desejar, então a tabela a seguir é apenas um exemplo.

| Chave | Valor |
| --- | --- |
| primeiroNome | {% raw %}`{{${first_name}}}`{% endraw %} |
| sobrenome | {% raw %}`{{${last_name}}}`{% endraw %} |
| email | {% raw %}`{{${email_address}}}`{% endraw %} |
| empresa | {% raw %}`{{custom_attribute.${company}}}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 role=”presentation” }

#### Cabeçalhos da solicitação

Selecione **\+ Adicionar Novo Cabeçalho** para cada um dos seguintes cabeçalhos de solicitação.

| Chave | Valor |
| --- | --- |
| Autorização | {% raw %}`{% connected_content https://[insert_instance_name].my.salesforce.com/services/oauth2/token     :method post     :body client_id=[insert_client_id]&client_secret=[insert_client_secret]&grant_type=client_credentials     :save result %}Bearer {{result.access_token}}`{% endraw %} |
| Tipo de Conteúdo | `application/json` |
{: .reset-td-br-1 .reset-td-br-2 role=”presentation” }

{: start="4" }
4\. Selecione **Salvar Modelo**.

\![Um modelo de webhook preenchido para criar um lead.]({% image_buster /assets/img/b2b/create_lead_webhook.png %}){: style="max-width:70%;"}
 
## Atualizando um lead no Salesforce Sales Cloud {#updating-lead}

Para configurar um webhook do Braze Salesforce Sales Cloud que atualiza leads no Salesforce, você precisa de um identificador comum entre o Salesforce Sales Cloud e o Braze. O exemplo abaixo usa o `lead_id` do Salesforce como o `external_id` do Braze, mas você também pode fazer isso usando um `user_alias`. Para detalhes sobre isso, consulte [B2B Data]({{site.baseurl}}/user_guide/getting_started/b2b_use_cases/b2b_data_models)

Este exemplo demonstra especificamente como atualizar o estágio de um lead para “MQL” (Lead Qualificado para Marketing) após um lead ultrapassar um certo limite de lead. Esta é uma parte central do nosso caso de uso [B2B lead scoring workflow]({{site.baseurl}}/user_guide/getting_started/b2b_use_cases/lead_scoring/).

### Passo 1: Colete seu `client_id` e `client_secret`

1. No Salesforce, vá para **Ferramentas da Plataforma** > **Aplicativos** > **Gerenciador de Aplicativos**.
2. Encontre seu aplicativo Braze recém-criado e selecione **Visualizar**.
3. Em **Chave do Consumidor e Segredo**, selecione **Gerenciar Detalhes do Consumidor**.
4. Na página resultante, anote sua **Chave do Consumidor** e **Segredo do Consumidor**.
    - A **Chave do Consumidor** é seu `client_id`, e o **Segredo do Consumidor** é seu `client_secret`.

### Passo 2: Configure seu modelo de webhook

1. No Braze, vá para **Modelos**, selecione **Modelos de Webhook**, e depois selecione **\+ Criar Modelo de Webhook**.
2. Forneça um nome para o modelo, como “Salesforce Sales Cloud > Atualizar Lead para MQL”.
3. Na aba **Compor**, insira os seguintes detalhes:

#### Compor webhook 

| Campo | Detalhes |
| --- | --- |
|URL do webhook | {% raw %}`https://[insert_instance_name].my.salesforce.com/services/data/v60.0/sobjects/Lead/{{${user_id}}}`{% endraw %} |
| Método HTTP | `PATCH` |
| Corpo da Solicitação | Pares de Chave/Valor JSON |
{: .reset-td-br-1 .reset-td-br-2 role=”presentation” }

#### Valores de chave de propriedade do corpo

Selecione **\+ Adicionar Nova Propriedade de Corpo** para o seguinte par chave/valor. Observe que `Lead_Stage__c` é um nome de exemplo. O campo personalizado que você usa para rastrear MQLs no Salesforce pode ter um nome diferente, então certifique-se de que eles correspondam.

| Chave | Valor |
| --- | --- |
| `Lead_Stage__c` | `MQL` |
{: .reset-td-br-1 .reset-td-br-2 role=”presentation” }

#### Cabeçalhos da solicitação

Selecione **\+ Adicionar Novo Cabeçalho** para cada um dos seguintes cabeçalhos de solicitação.

| Chave | Valor |
| --- | --- |
| Autorização | {% raw %}`{% connected_content https://[insert_instance_name].my.salesforce.com/services/oauth2/token     :method post     :body client_id=[insert_client_id]&client_secret=[insert_client_secret]&grant_type=client_credentials     :save result %}Bearer {{result.access_token}}`{% endraw %} |
| Tipo de Conteúdo | `application/json` |
{: .reset-td-br-1 .reset-td-br-2 role=”presentation” }

{: start="4"}
4\. Selecione **Salvar Modelo**.

\![Um modelo de webhook preenchido para atualizar um lead.]({% image_buster /assets/img/b2b/update_lead_webhook.png %}){: style="max-width:70%;"}

## Usando esses webhooks em um fluxo de trabalho operacional

Você pode adicionar rapidamente seus modelos aos seus fluxos de trabalho operacionais no Braze, como:

1. Parte de uma [nova campanha de usuário](#new-lead) que cria um lead no Salesforce
2. Parte de um [Canvas de pontuação de leads](#lead-scoring) que atualiza usuários que ultrapassaram seu limite de MQL para “MQL”, e que atualiza o Salesforce Sales Cloud com as mesmas informações

### Nova campanha de leads {#new-lead}

Para criar um lead no Salesforce quando um usuário fornece seu endereço de e-mail, você pode criar uma campanha que usa o modelo de webhook “Atualizar Lead” e é acionada quando um usuário adiciona seu endereço de e-mail (por exemplo, preenche um formulário na web).

\![Passo 2 de criar uma campanha que é baseada em ações e tem a ação de gatilho de “Adicionar um Endereço de E-mail”.]({% image_buster /assets/img/b2b/salesforce_create_campaign.png %}){: style="max-width:70%;"}

### Canvas de pontuação de leads para ultrapassar o limite de Lead Qualificado de Marketing (MQL) {#lead-scoring}

Este webhook é coberto no caso de uso [pontuação de leads]({{site.baseurl}}/user_guide/getting_started/b2b_use_cases/lead_scoring/#lead-handoff), mas você também pode verificar os MQLs e atualizar diretamente o Salesforce dentro do Canvas de pontuação de leads (em vez de criar uma campanha de webhook separada): 

Adicione um passo subsequente à atualização do usuário para verificar se um usuário ultrapassou seu limite de MQL definido. Se eles ultrapassaram, atualize o status do usuário para “MQL”, e então atualize o Salesforce com o mesmo status “MQL” usando este modelo de webhook. O Salesforce cuida do resto roteando este lead para as equipes de vendas apropriadas usando suas regras de roteamento de leads definidas.  

#### Adicionando um passo no Canvas para verificar usuários que passaram o limite de MQL 

1. Adicione um passo de **Caminho de Audiência** com dois grupos: “Limite de MQL” e “Todos os Outros”.
2. No grupo “Limite de MQL”, procure por qualquer usuário que atualmente não tenha um status de “MQL” (por exemplo, `lead_stage` igual a “Lead”), mas tenha uma pontuação de lead que está acima do seu limite definido (por exemplo, `lead_score` maior que 50). Se sim, eles avançam para o próximo passo, se não, eles saem.

\![O grupo “Caminho de Audiência” do “Limite de MQL” com filtros para um `lead_stage` igual a “Lead” e um `lead_score` sendo mais que “50”.]({% image_buster /assets/img/b2b/salesforce_check_mql.png %}){: style="max-width:70%;"}

{: start="3" }
3\. Adicione um passo de **Atualização de Usuário** que atualiza o valor do atributo `lead_stage` do usuário para “MQL”.

\![O passo de Atualização de Usuário “Atualizar para MQL” que atualiza o atributo `lead_stage` para ter um valor de “MQL”.]({% image_buster /assets/img/b2b/salesforce_update_mql.png %}){: style="max-width:70%;"}

{: start="4" }
4\. Adicione um passo de webhook que atualiza o Salesforce com o novo estágio de MQL.

\![O passo de webhook “Atualizar Salesforce” com detalhes completos.]({% image_buster /assets/img/b2b/salesforce_webhook.png %}){: style="max-width:70%;"}

Agora seu fluxo do Canvas atualizará os usuários que ultrapassaram seu limite de MQL!

\![Uma etapa de atualização do usuário do Canvas que verifica se um usuário ultrapassa o limite de MQL e, se o usuário passar, atualiza o Salesforce.]({% image_buster /assets/img/b2b/salesforce_canvas.png %}){: style="max-width:50%;"}

## Solução de Problemas

Esses fluxos de trabalho têm capacidade de depuração limitada dentro do Salesforce, por isso recomendamos consultar o [Registro de Atividade de Mensagem]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab#message-activity-log) do Braze para descobrir por que um Webhook falhou e se ocorreram erros.

Por exemplo, um erro causado por uma URL inválida usada para a recuperação do token oAuth seria exibido como `https://[insert_instance_name].my.salesforce.com/services/oauth2/token is not a valid URL`.

\![Um corpo de resposta de erro afirmando que a URL não é uma URL válida.]({% image_buster /assets/img/b2b/error_message_invalid_url.png %})

