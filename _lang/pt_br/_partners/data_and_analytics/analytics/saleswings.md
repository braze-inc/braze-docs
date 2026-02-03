---
nav_title: SalesWings
article_title: SalesWings
description: "Este artigo de referência descreve a parceria entre a Braze e a SalesWings. O SalesWings é uma solução de operações de vendas e marketing para o Braze que ajuda a qualificar leads e contas e fornece insights e alertas de vendas dentro do CRM, como o Salesforce, bem como relatórios de atribuição B2B. Você pode aproveitar os interesses e o engajamento no Braze para personalização no Canva e segmentação. O SalesWings também oferece uma maneira de gerar leads a partir de um site, semelhante ao Digioh."
alias: /partners/saleswings/
page_type: partner
search_tag: Partner

---

# SalesWings

> [A SalesWings](https://www.saleswingsapp.com/?utm_source=braze&utm_campaign=technicaldocs) é uma solução de operações de marketing e vendas B2B SaaS que ajuda a gerenciar a qualificação de leads e contas por meio de pontuação e classificação holísticas de leads, além de fornecer insights e alertas de vendas e relatórios de atribuição B2B, juntamente com uma forte integração com o Salesforce CRM.  Um complemento de engajamento do site, semelhante ao Digioh, permite que você gere leads no site. Você pode aproveitar os interesses e o engajamento no Braze para personalização no Canva e segmentação.

_Essa integração é mantida pela SalesWings._

## Sobre a integração

O SalesWings permite que as equipes de marketing e os gerentes de operações de marketing qualifiquem leads e contas para suas equipes de vendas, o que é essencial para o alinhamento entre vendas e marketing e para a eficiência operacional. Além disso, o SalesWings, juntamente com o Braze, pode apresentar aos representantes de vendas a jornada completa do cliente de um lead e da conta e os dados de engajamento da campanha de marketing do Braze, permitindo que você aumente as taxas de qualificação de leads por meio de conversas mais educadas. O SalesWings identifica necessidades e interesses juntamente com outros sinais, permitindo a transferência de compradores qualificados para as equipes de vendas dentro do seu CRM de forma automatizada. Você pode usar as necessidades, os interesses e a prontidão de vendas identificados como atribuições do usuário Braze para personalização e segmentação.

## Pré-requisitos
 
| Requisito | Descrição |
| ----------- | ----------- |
| Conta SalesWings | É necessária uma conta [SalesWings](https://www.saleswingsapp.com/?utm_source=braze&utm_campaign=technicaldocs) para aproveitar esta parceria. |
| Chave da API REST do Braze | Uma chave da API REST do Braze com permissões `users.export.ids` (e `users.track` se estiver usando o recurso push de insights do SalesWings). <br><br> Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
| Endpoint REST do Braze | [Sua URL de endpoint REST.]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) Seu endpoint dependerá da URL do Braze para sua instância. |
| Segment.com conta (opcional) | Se você é um usuário do Segment.com, é possível enviar todos os dados de engajamento e perfis de leads e identificar eventos via Segment.com para a criação de perfis de leads. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Casos de uso

{% tabs %}
{% tab Lead and Account Scoring %}

A SalesWings fornece aos clientes da Braze [uma maneira flexível de qualificar leads, contatos e contas com pontuação de leads de última geração](https://www.saleswingsapp.com/braze-lead-scoring-and-sales-insights?utm_source=braze&utm_campaign=technicaldocs) e capacidades de classificação de leads. Todos os seus dados de qualificação de leads são enviados nativamente para o Salesforce CRM e outros sistemas onde você deseja gerenciar e relatar leads, contatos, contas e oportunidades.

![Exemplo de um modelo simples de pontuação de leads sem código de cliques no SalesWings]({% image_buster /assets/img/saleswings/example_lead_scoring_builder_braze_lead_scoring.png %})

_Exemplo de um modelo simples de pontuação de leads, clique e não codifique, no SalesWings_
{% endtab %}
{% tab Sales and Marketing Alignment %}
SalesWings permite que as equipes de marketing rastreiem, qualifiquem e repassem leads qualificados para marketing para suas equipes de vendas. Todos os dados do SalesWings são enviados nativamente para o Salesforce e podem ser aproveitados para ajustar qualquer processo existente ou criar novos processos por meio de listas, relatórios, fluxos e mais.

![Exemplo de como a pontuação de leads do SalesWings prioriza uma lista de leads ou contatos nativamente dentro do Salesforce]({% image_buster /assets/img/saleswings/prioritized_lead_or_contact_list_braze_lead_scoring.png %})

_Exemplo de como a pontuação de leads do SalesWings prioriza uma lista de leads ou contatos nativamente dentro do Salesforce_

![Exemplo de como a pontuação de leads da SalesWings prioriza uma lista de contas nativamente dentro do Salesforce]({% image_buster /assets/img/saleswings/prioritized_account_list_braze_lead_scoring.png %})

_Exemplo de como a pontuação de leads do SalesWings prioriza uma lista de contas nativamente dentro do Salesforce_
{% endtab %}
{% tab Lead and Account Grading %}
A SalesWings permite que os clientes da Braze qualifiquem leads e contas com base em dados de perfil (normalmente dados de CRM). Isso também é conhecido como “classificação de leads”, “pontuação de adequação” ou “pontuação firmográfica”. Os clientes da Braze podem enviar dados de atributos diretamente para o SalesWings, e o SalesWings pode ler quaisquer dados e registros de objetos padrão ou personalizados do Salesforce CRM para uma pontuação de perfil holística.
{% endtab %}
{% tab Sales Insights for Sales Reps %}
A SalesWings permite mostrar aos seus representantes de vendas insights de vendas sobre seus leads, contatos e contas (alternativa ao Marketo Sales Insights). Essencialmente, você pode disponibilizar quaisquer dados da Braze e de engajamento na Web para sua equipe de vendas. Os insights são incorporados nativamente no Salesforce CRM e podem ser enviados para outros CRMs ou sistemas ou via um e-mail da Braze como um “alerta de vendas”.

![Exemplo de visualização de insights de vendas para representantes de vendas no Salesforce (também disponível para outros sistemas de CRM)]({% image_buster /assets/img/saleswings/marketo_sales_insights_alternative_for_braze.png %})

_Exemplo de visualização de insights de vendas para representantes de vendas no Salesforce (também disponível para outros sistemas CRM)_
{% endtab %}
{% tab Sales Alerts %}
A SalesWings oferece alertas nativos por e-mail e Slack, e você pode configurar assinaturas de relatórios no Salesforce que sua equipe de vendas pode acessar para obter relatórios diários, semanais e mensais por e-mail. Além disso, através de uma integração com o Zapier, você pode criar fluxos de trabalho adicionais com base nos dados de qualificação de leads do SalesWings.

![Exemplo de alerta de vendas via canal Slack]({% image_buster /assets/img/saleswings/smart_watch_alerts.png %})

_Exemplo de alerta de vendas via canal do Slack_
{% endtab %}
{% tab Reporting in Salesforce CRM %}
Por meio da integração nativa do SalesWings com o Salesforce, é possível criar relatórios automatizados com leads, contatos, contas e oportunidades com base em dados de engajamento na Web e qualquer engajamento de campanha do Braze com uma integração nativa do Braze Currents. Por exemplo, é possível exibir uma lista de leads quentes para uma equipe de vendas, com todos que clicaram em uma campanha de e-mail específica ou realizaram uma ação específica em seu app ou site.

![Exemplo de painel vinculado ao envio de e-mail do Braze & engajamento de marketing no Salesforce, analisando o impacto das campanhas do Braze nos resultados de vendas]({% image_buster /assets/img/saleswings/saleswings_email_campaign_attribution_dashboard.png %})

_Exemplo de painel vinculado ao envio de e-mail do Braze & engajamento de marketing no Salesforce, analisando o impacto das campanhas do Braze nos resultados de vendas_
{% endtab %}
{% endtabs %}

## Integração

### Etapa 1: Conta e configuração do SalesWings

[Agende uma demonstração](https://www.saleswingsapp.com/schedule-a-demo?utm_source=braze&utm_campaign=technicaldocs) com a amigável equipe da SalesWings para saber mais sobre a SalesWings.

### Etapa 2: instale o rastreamento comportamental no seu site ou app

Há várias maneiras de coletar dados comportamentais no SalesWings para pontuação de leads e contas, identificando a intenção do comprador e insights de vendas:
* [Implante o JavaScript de rastreamento da SalesWings](https://support.saleswingsapp.com/en/collections/3285135-1-implementing-saleswings-tracking-script) nos sites e aplicativos onde você deseja rastrear e identificar leads
* Ingerir eventos Braze juntamente com as propriedades do evento no SalesWings via Braze Currents
* Enviar dados comportamentais de atividade de leads (e dados de perfil de leads) por meio da [integração do SalesWings com o Segment](https://support.saleswingsapp.com/en/articles/9258905-segment-com-integration)
* Envie dados diretamente para a [API](https://support.saleswingsapp.com/en/articles/6930889-using-saleswings-open-api-to-send-events-to-saleswings) do SalesWings a partir de uma solução de terceiros

### Etapa 3: Conectando SalesWings ao Braze

Acesse a [página**SalesWings Integrations (Integrações do SalesWings**](https://helium.saleswings.pro/integrations) ) e expanda a seção **Braze Integration (Integração do Braze** ).

![A seção de Integração da Braze na página de Configurações do SalesWings.]({% image_buster /assets/img/saleswings/saleswings_braze_lead_scoring_integration_settings.png %})

Copie o valor da coluna **Identifier** para a nova chave criada e cole-o no campo **chave de API da Braze** da seção **Integração da Braze do SalesWings**.

Adicione seu endpoint da API do Braze conforme descrito no [artigo Endpoints da API e do SDK]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints) e insira-o no campo **Braze API endpoint**. Copie o valor da coluna **REST Endpoint** (Endpoint REST) e insira-o no campo **Braze API endpoint** (Endpoint da API da Braze) na seção **Braze Integration** (Integração da Braze) da SalesWings.

Em seguida, selecione **Salvar**.

### Etapa 4: Ativar a capacitação do SalesWings insights push para o Braze (opcional)

Se quiser disponibilizar os insights do SalesWings em seus perfis de usuário do Braze para segmentação, personalização ou orquestração da jornada do Canva, visite a [página**SalesWings Integrations**](https://helium.saleswings.pro/integrations) e expanda a seção **Braze Integration**.

Clique em **Start data push (Iniciar envio de dados** ) em **SalesWings-to-Braze insights data push**.

### Etapa 5: Configure uma exportação personalizada do Currents para o SalesWings (opcional)

Se quiser usar [o comportamento do usuário]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events) e os eventos [de engajamento com mensagens]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events) para inteligência comportamental, pontuação de leads e contas, produzir insights de vendas ou gerar relatórios em seu CRM, acesse a [página**SalesWings Integrations**](https://helium.saleswings.pro/integrations) e expanda a seção **Braze Integration**.

Selecione **Generate (Gerar** ) em **Generate an API token (Gerar um token de API) para configurar uma Custom Currents Export (Exportação de Currents Personalizados**).

Em seguida, [crie uma nova corrente]({{site.baseurl}}/user_guide/data/braze_currents/setting_up_currents) e selecione **Custom Currents Export** como o tipo de corrente.

Na seção **Credentials (Credenciais** ) do formulário Current creation (Criação atual), insira o token da API gerado na [página**SalesWings Integrations (Integrações da SalesWings**](https://helium.saleswings.pro/integrations) ) para **Bearer Token (Token portador**) e `https://helium.saleswings.pro/api/braze/currents/events` para **Endpoint (Ponto de extremidade**).

### Etapa 6: Configuração da pontuação de leads e contas do SalesWings para o Braze, integração com CRM e muito mais

Consulte a equipe de serviços da SalesWings para obter suporte completo de integração pelo [website](https://www.saleswingsapp.com/?utm_source=braze&utm_campaign=technicaldocs).

## Usando essa integração 

Para disparar a vinculação de dados comportamentais e outros dados a leads e contas, a SalesWings deve identificar um usuário em seu site ou app, ou por meio de uma integração de terceiros. Isso pode ocorrer das seguintes maneiras:

- **Envios de formulários:** Quando um usuário envia um formulário da web, o SalesWings identificará automaticamente todos os tipos de formulários da web (como login, baixar, entre em contato conosco, etc.) e resolverá a identidade de um usuário quando ele enviar um formulário. 
- **Cliques em URL com ID da Braze ou ID externo:** Um usuário clica em uma ação de marketing da Braze, tipicamente cliques em e-mail, cliques em banner ou similar, levando a uma página que você está rastreando com SalesWings.
- **Eventos Braze Currents (opcional):** Se a exportação de Currents personalizados para o SalesWings estiver configurada, o SalesWings criará um perfil identificado para cada usuário do Braze com um e-mail que tenha eventos enviados para o Current.
- **Rastreamento de e-mail de vendas via plugins do Gmail e Outlook (opcional):** Se você decidir capacitar seu representante de vendas com plugins de rastreamento de e-mail, ele poderá disparar o rastreamento completo do site dos usuários enviando links rastreáveis.
- **Segment.com identificar evento (opcional):** Se você é um usuário do Segment.com, também pode resolver a identidade de um usuário com a integração do Segment.com.

### Identificando usuários a partir de cliques em URLs

Você pode identificar os usuários automaticamente quando eles clicam em um URL rastreável (por exemplo, e-mails em massa, banners com URLs). Para tornar uma URL rastreável, existem duas maneiras de modificar os URLs do seu site em seus e-mails, banners ou SMS, adicionando o parâmetro e o ID ao final de seus links.

1. Anexando `?braze_id=` seguido por {% raw %}`{{${braze_id}}}`{% endraw %} 
  - **Exemplo de link:** {% raw %}`https://www.your-website.com?braze_id={{${braze_id}}}`{% endraw %}<br><br>

2. Anexando `?br_user_id=` seguido por {% raw %}`{{${user_id}}}`{% endraw %}
  - **Exemplo de link:** {% raw %}`https://www.client-website.com?br_user_id={{${user_id}}}`{% endraw %}

A variável `braze_id` é definida como um identificador do usuário gerado pelo Braze e está sempre disponível. A variável `br_user_id` é definida como o identificador do usuário no seu sistema e pode estar ausente em certos cenários (por exemplo, para usuários anônimos criados pelo SDK da Braze). Se ambos `braze_id` e `br_user_id` forem usados em um link, a SalesWings considerará apenas o parâmetro `braze_id`.

### Pushing SalesWings insights to Braze

Se você ativar a capacitação de insights do SalesWings para o Braze, o SalesWings atualizará os perfis de usuário do Braze com os seguintes [atributos personalizados]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes):

| Atributo personalizado | Tipo | Descrição |
| ----------- | ----------- | ----------- |
| `sw_favorite` | booleano | Se o lead foi marcado como favorito no SalesWings ou no Salesforce CRM |
| `sw_last_active_at` | data | O momento da última atividade do lead em seu site |
| `sw_lead_link_open` | string | O link para acessar um perfil de lead no SalesWings (sem uma conta no dashboard do SalesWings) |
| `sw_lead_link_protected` | string | O link para acessar um perfil de lead no SalesWings (com uma conta no dashboard do SalesWings) |
| `sw_lead_owner` | string | O proprietário definido para o lead no SalesWings ou no Salesforce CRM |
| `sw_lead_score` | flutuante | O valor da pontuação principal do lead do SalesWings configurado no SalesWings [Rule Engine](https://helium.saleswings.pro/falcon) |
| `sw_predictive_score` | string | O valor da [pontuação de previsão](https://support.saleswingsapp.com/en/articles/581795-the-predictive-lead-score) da SalesWings que avalia o engajamento do lead com base no número e na recência das atividades rastreadas. Os valores possíveis são `HOT`, `WARM`, `NORMAL`, `COLD` ou `FROZEN` |
| `sw_salesforce_record_id` | string | O ID do registro de lead ou contato no Salesforce CRM |
| `sw_salesforce_record_url` | string | O URL do registro de lead ou contato no Salesforce CRM |
| `sw_session_count` | inteiro | O número de sessões rastreadas em seu site para esse lead |
| `sw_tags` | matriz de string | As necessidades e os interesses que a SalesWings identificou, representados como "tags". Os nomes das tags do SalesWings configuradas no SalesWings [Rule Engine](https://helium.saleswings.pro/falcon) que se aplicam a esse lead |
| Atribuições adicionais de pontuação de leads | flutuante | Um atributo personalizado para cada pontuação de lead adicional configurada no SalesWings [Rule Engine](https://helium.saleswings.pro/falcon). O nome do atributo é derivado do nome da pontuação do SalesWings; por exemplo, uma pontuação chamada `Likeliness to meet` é enviada como atributo personalizado `sw_likeliness_to_meet`. Se você renomear uma pontuação depois que o sistema a criar, o SalesWings continuará sincronizando com o nome inicial do atributo personalizado. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Quando o push é ativado, o SalesWings começa imediatamente a enviar atributos personalizados para o Braze assim que os pontos de dados subjacentes mudam nos perfis de leads do SalesWings e sincroniza progressivamente todos os leads existentes, mesmo que eles não tenham novas atualizações.

A SalesWings atualiza todos os usuários do Braze com um e-mail que corresponde ao endereço de e-mail do perfil de lead da SalesWings. Se não houver usuários correspondentes no Braze, o SalesWings não criará um novo usuário. 

### Usando eventos Braze Currents em seu CRM

Se você conectar um Braze Currents ao SalesWings, o SalesWings criará perfis de leads identificados para cada usuário do Braze com um e-mail e registrará os eventos suportados pelo Braze como atividade de lead. Em seu CRM, todos os dados podem ser automaticamente agregados no nível da conta do lead. A atividade e os dados registrados podem ser combinados ainda mais com os dados comportamentais coletados com o script de rastreamento da SalesWings ou Segment.com, ou enviando outros dados para a API da SalesWings, e depois usados para identificar as necessidades e a prontidão de vendas de seus clientes potenciais para seus processos de gerenciamento de leads e contas.

A tabela a seguir mostra os tipos de eventos do Braze suportados pelo SalesWings e sua representação no histórico de atividades de leads e no mecanismo de regras do SalesWings:

| Categoria do evento | Tipo de evento | Nome do evento em SalesWings |
| ----------- | ----------- | ----------- |
| Eventos do canva | Entradas | `[Nurturing] Added by marketing team onto the journey $canvas_name` |
| Eventos de comportamento do cliente | Eventos personalizados | `[Custom Event tracked] $name` |
| Eventos de comportamento do cliente | Primeira sessão | `[User Action] Today marks the user's first session` |
| Eventos de comportamento do cliente | Instalar atribuição | `[User Action] User installed app from $source` |
| Eventos de comportamento do cliente | Eventos de compra | `[Purchase] Customer purchased $product_id for $price $currency` |
| Eventos de mensagem | Clique no cartão de conteúdo | `[Content Card engagement] Clicked on $campaign_name content card` |
| Eventos de mensagem | Bounce de e-mail | `[Alerting or negative] Email hard-bounced. This person's email appears to be no longer valid` |
| Eventos de mensagem | Clique no e-mail | `[Email campaign engagement] Clicked in email $campaign_name on $url` |
| Eventos de mensagem | Entrega de e-mail | `[Nurturing] Received email $campaign_name` |
| Eventos de mensagem | Abertura de e-mail | `[Email campaign engagement] Opened email $campaign_name` |
| Eventos de mensagem | Cancelamento de inscrição de e-mail | `[Subscription status change] Unsubscribed from $campaign_name` |
| Eventos de mensagem | Clique em mensagem no app | `[In-app campaign engagement] Clicked on message $campaign_name` |
| Eventos de mensagem | Abertura de push | `[Push notification engagement] Clicked on notification $campaign_name` |
| Eventos de mensagem | SMS/MMS de entrada recebidos | `[SMS/mobile campaign engagement] We received a message from this person to our internal number $inbound_phone_number: $message_body` |
| Eventos de mensagem | Clique em link encurtado em SMS/MMS | `[SMS/mobile campaign engagement] Clicked on $short_url` |
| Eventos de mensagem | WhatsApp Inbound Recebido | `[WhatsApp engagement] We received a message from this person to our WhatsApp number $inbound_phone_number: $message_body` |
| Eventos de mensagem | Leitura de WhatsApp | `[WhatsApp engagement] Lead read our message from the $campaign_name campaign` |
| Inscrições | Alteração de estado de inscrição global | `[Subscription status change] Global marketing subscription setting set to $subscription_status` |
| Inscrições | Alteração de estado do grupo de inscrições | `[Subscription status change] $subscription_status to/from $campaign_name` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Em seguida, você pode configurar as condições de **Evento personalizado** > **Nome do evento** e **Evento personalizado** > **Propriedade do evento** para as tags e pontuações do SalesWings em relação aos nomes de eventos do SalesWings da tabela acima. A lista de propriedades de eventos disponíveis para condições é pré-preenchida com algumas das entradas mais usadas, e você sempre pode adicionar novas na seção **Propriedade do evento** da [página de configuração do Mecanismo de Regras](https://helium.saleswings.pro/falcon).

![Exemplo de uma condição de nome de evento.]({% image_buster /assets/img/saleswings/saleswings_braze_lead_scoring_custom_event_condition.png %})

Para configuração e mais solução de problemas, entre em contato com a [equipe de serviços da SalesWings](https://www.saleswingsapp.com/?utm_source=braze&utm_campaign=technicaldocs) para suporte de integração.

