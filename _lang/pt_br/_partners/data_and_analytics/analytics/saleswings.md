---
nav_title: SalesWings
article_title: SalesWings
description: "Este artigo de referência descreve a parceria entre Braze e SalesWings, uma solução de operações de vendas e marketing para Braze, que ajuda a qualificar leads e contas, fornece insights de vendas e alertas dentro do CRM como Salesforce, além de relatórios de atribuição B2B."
alias: /partners/saleswings/
page_type: partner
search_tag: Partner

---

# SalesWings

> [SalesWings](https://www.saleswingsapp.com/?utm_source=braze&utm_campaign=technicaldocs) é uma solução de operações de vendas e marketing SaaS B2B, que ajuda a gerenciar a qualificação de leads e contas por meio de pontuação e classificação holísticas de leads, fornece insights de vendas e alertas, relatórios de atribuição B2B, juntamente com uma integração estreita com o CRM Salesforce.

_Esta integração é mantida pela SalesWings._

## Sobre a integração

SalesWings permite que equipes de marketing e gerentes de operações de marketing qualifiquem leads e contas para suas equipes de vendas, essencial para o alinhamento de vendas e marketing e eficiência operacional. Além disso, a SalesWings, junto com a Braze, pode apresentar a jornada completa do cliente de um lead e os dados de engajamento da campanha de marketing da Braze para os representantes de vendas, permitindo aumentar as taxas de qualificação de leads por meio de conversas mais informadas. SalesWings identifica necessidades e interesses junto com outros sinais, permitindo transferir compradores qualificados para as equipes de vendas dentro do seu CRM de maneira automatizada.

## Pré-requisitos
 
| Requisito | Descrição |
| ----------- | ----------- |
| Conta SalesWings | É necessária uma conta [SalesWings](https://www.saleswingsapp.com/?utm_source=braze&utm_campaign=technicaldocs) para aproveitar esta parceria. |
| chave da API REST Braze | Uma chave da API REST da Braze com permissões `users.export.ids`. <br><br> Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
| Endpoint REST do Braze | [Sua URL de endpoint REST.]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) Seu endpoint dependerá da URL do Braze para sua instância. |
| Segment.com conta (opcional) | Se você é um usuário do Segment.com, é possível enviar todos os dados de engajamento e perfis de leads e identificar eventos via Segment.com para a criação de perfis de leads. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Casos de uso

{% tabs %}
{% tab Pontuação de Leads e Contas %}

A SalesWings fornece aos clientes da Braze [uma maneira flexível de qualificar leads, contatos e contas com pontuação de leads de última geração](https://www.saleswingsapp.com/braze-lead-scoring-and-sales-insights?utm_source=braze&utm_campaign=technicaldocs) e capacidades de classificação de leads. Todos os seus dados de qualificação de leads são enviados nativamente para o Salesforce CRM e outros sistemas onde você deseja gerenciar e relatar leads, contatos, contas e oportunidades.

![Exemplo de um modelo simples de pontuação de leads sem código no SalesWings]({% image_buster /assets/img/saleswings/example_lead_scoring_builder_braze_lead_scoring.png %})

_Exemplo de um modelo simples de pontuação de leads, clique e não codifique, no SalesWings_
{% endtab %}
{% tab Alinhamento de Vendas e Marketing %}
SalesWings permite que as equipes de marketing rastreiem, qualifiquem e repassem leads qualificados para marketing para suas equipes de vendas. Todos os dados do SalesWings são enviados nativamente para o Salesforce e podem ser aproveitados para ajustar qualquer processo existente ou criar novos processos por meio de listas, relatórios, fluxos e mais.

![Exemplo de como a pontuação de leads do SalesWings prioriza uma lista de leads ou contatos nativamente dentro do Salesforce]({% image_buster /assets/img/saleswings/prioritized_lead_or_contact_list_braze_lead_scoring.png %})

_Exemplo de como a pontuação de leads do SalesWings prioriza uma lista de leads ou contatos nativamente dentro do Salesforce_

![Exemplo de como a pontuação de leads do SalesWings prioriza uma lista de contas nativamente dentro do Salesforce]({% image_buster /assets/img/saleswings/prioritized_account_list_braze_lead_scoring.png %})

_Exemplo de como a pontuação de leads do SalesWings prioriza uma lista de contas nativamente dentro do Salesforce_
{% endtab %}
{% tab Classificação de Leads e Contas %}
A SalesWings permite que os clientes da Braze qualifiquem leads e contas com base em dados de perfil (normalmente dados de CRM). Isso também é conhecido como “classificação de leads”, “pontuação de adequação” ou “pontuação firmográfica”. Os clientes da Braze podem enviar dados de atributos diretamente para o SalesWings, e o SalesWings pode ler quaisquer dados e registros de objetos padrão ou personalizados do Salesforce CRM para uma pontuação de perfil holística.
{% endtab %}
{% tab Insights de Vendas para Representantes de Vendas %}
A SalesWings permite mostrar aos seus representantes de vendas insights de vendas sobre seus leads, contatos e contas (alternativa ao Marketo Sales Insights). Essencialmente, você pode disponibilizar quaisquer dados da Braze e de engajamento na Web para sua equipe de vendas. Os insights são incorporados nativamente no Salesforce CRM e podem ser enviados para outros CRMs ou sistemas ou via um e-mail da Braze como um “alerta de vendas”.

![Exemplo de visualização de insights de vendas para representantes de vendas no Salesforce (também disponível para outros sistemas CRM)]({% image_buster /assets/img/saleswings/marketo_sales_insights_alternative_for_braze.png %})

_Exemplo de visualização de insights de vendas para representantes de vendas no Salesforce (também disponível para outros sistemas CRM)_
{% endtab %}
{% tab Alertas de Vendas %}
A SalesWings oferece alertas nativos por e-mail e Slack, e você pode configurar assinaturas de relatórios no Salesforce que sua equipe de vendas pode acessar para obter relatórios diários, semanais e mensais por e-mail. Além disso, através de uma integração com o Zapier, você pode criar fluxos de trabalho adicionais com base nos dados de qualificação de leads do SalesWings.

![Exemplo de alerta de vendas via canal do Slack]({% image_buster /assets/img/saleswings/smart_watch_alerts.png %})

_Exemplo de alerta de vendas via canal do Slack_
{% endtab %}
{% tab Relatórios no Salesforce CRM %}
Por meio da integração nativa da SalesWings com o Salesforce, você pode construir relatórios automatizados com leads, contatos, contas e oportunidades com base em dados de engajamento na web e qualquer engajamento de campanha da Braze com uma integração nativa de Braze currents. Por exemplo, você pode apresentar uma lista de leads quentes para uma equipe de vendas, com todos que clicaram em uma campanha de e-mail específica ou realizaram uma ação específica em seu aplicativo ou site.

![Exemplo de dashboard vinculado ao e-mail e engajamento de marketing da Braze na Salesforce, observando o impacto das campanhas da Braze nos resultados de vendas e desfechos]({% image_buster /assets/img/saleswings/saleswings_email_campaign_attribution_dashboard.png %})

_Exemplo de dashboard vinculado ao e-mail e engajamento de marketing da Braze na Salesforce, observando o impacto das campanhas da Braze nos resultados de vendas e desfechos_
{% endtab %}
{% endtabs %}

## Integração

### Etapa 1: Conta e configuração do SalesWings

[Agende uma demonstração](https://www.saleswingsapp.com/schedule-a-demo?utm_source=braze&utm_campaign=technicaldocs) com a amigável equipe da SalesWings para saber mais sobre a SalesWings.

### Etapa 2: instale o rastreamento comportamental no seu site ou app

Existem várias maneiras de coletar dados comportamentais na SalesWings para pontuação de leads e contas, identificando a intenção de compra e insights de vendas:
* [Implante o JavaScript de rastreamento da SalesWings](https://support.saleswingsapp.com/en/collections/3285135-1-implementing-saleswings-tracking-script) nos sites e aplicativos onde você deseja rastrear e identificar leads
* Ingerir eventos da Braze junto com propriedades de eventos na SalesWings via Braze Currents
* Enviar dados de atividade de lead comportamental (e dados de perfil de lead) via [integração da SalesWings com Segment](https://support.saleswingsapp.com/en/articles/9258905-segment-com-integration)
* Enviar dados diretamente para a [API](https://support.saleswingsapp.com/en/articles/6930889-using-saleswings-open-api-to-send-events-to-saleswings) da SalesWings a partir de uma solução de terceiros

### Etapa 3: Conectando SalesWings ao Braze

Acessar a [**página de Integrações da SalesWings**](https://helium.saleswings.pro/integrations) e expandir a seção **Integração Braze**.

![A seção de Integração Braze da página de Configurações da SalesWings.]({% image_buster /assets/img/saleswings/saleswings_braze_lead_scoring_integration_settings.png %})

Copie o valor da coluna **Identifier** para a nova chave criada e cole-o no campo **chave de API da Braze** da seção **Integração da Braze do SalesWings**.

Adicione seu endpoint da API Braze conforme descrito no [artigo de endpoints da API e SDK]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints), e insira-o no campo **endpoint da API Braze**. Copie o valor da coluna **REST Endpoint** (Endpoint REST) e insira-o no campo **Braze API endpoint** (Endpoint da API da Braze) na seção **Braze Integration** (Integração da Braze) da SalesWings.

Em seguida, selecione **Salvar**.

### Etapa 4: Configurar uma exportação personalizada de Currents para a SalesWings (opcional)

Se você quiser usar eventos de [comportamento do usuário]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events) e [engajamento com mensagem]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events) para inteligência comportamental, pontuação de leads e contas, produzir insights de vendas ou gerar relatórios em seu CRM, acesse a [**página de Integrações da SalesWings**](https://helium.saleswings.pro/integrations) e expanda a seção **Integração Braze**.

Selecione **Gerar** em **Gerar um token de API para configurar uma Exportação Personalizada de Currents**.

Então, [crie um novo Current]({{site.baseurl}}/user_guide/data/braze_currents/setting_up_currents) e selecione **Exportação Personalizada de Currents** como o tipo de Current.

Na seção **Credenciais** do formulário de criação de Current, insira o token da API que você gerou na página [**Integrações SalesWings** ](https://helium.saleswings.pro/integrations) para **Token Bearer**, e `https://helium.saleswings.pro/api/braze/currents/events` para **Ponto de Extremidade**.

### Etapa 5: Configurando a pontuação de leads e contas do SalesWings para Braze, integração de CRM e mais

Consulte a equipe de serviços da SalesWings para obter suporte completo de integração pelo [website](https://www.saleswingsapp.com/?utm_source=braze&utm_campaign=technicaldocs).

## Usando essa integração 

Para disparar dados comportamentais e outros dados para leads e contas, o SalesWings deve identificar um usuário em seu site ou app, ou através de uma integração de terceiros. Isso pode ocorrer das seguintes maneiras:

- **Envios de formulários:** Quando um usuário envia um formulário da web, o SalesWings identificará automaticamente todos os tipos de formulários da web (como login, baixar, entre em contato conosco, etc.) e resolverá a identidade de um usuário quando ele enviar um formulário. 
- **Cliques em URL com ID da Braze ou ID externo:** Um usuário clica em uma ação de marketing da Braze, tipicamente cliques em e-mail, cliques em banner ou similar, levando a uma página que você está rastreando com SalesWings.
- **Eventos Braze Currents (opcional):** Se a exportação de Currents personalizada para SalesWings estiver configurada, o SalesWings criará um perfil identificado para cada usuário do Braze com um e-mail que tenha eventos enviados para o Current.
- **Rastreamento de e-mail de vendas via plugins do Gmail e Outlook (opcional):** Se você decidir capacitar seu representante de vendas com plugins de rastreamento de e-mail, ele poderá disparar o rastreamento completo do site dos usuários enviando links rastreáveis.
- **Segment.com identificar evento (opcional):** Se você é um usuário do Segment.com, também pode resolver a identidade de um usuário com a integração do Segment.com.

### Identificando usuários a partir de cliques em URLs

Você pode identificar os usuários automaticamente quando eles clicam em um URL rastreável (por exemplo, e-mails em massa, banners com URLs). Para tornar uma URL rastreável, existem duas maneiras de modificar os URLs do seu site em seus e-mails, banners ou SMS, adicionando o parâmetro e o ID ao final de seus links.

1. Anexando `?braze_id=` seguido por {% raw %}`{{${braze_id}}}`{% endraw %} 
  - **Exemplo de link:** {% raw %}`https://www.your-website.com?braze_id={{${braze_id}}}`{% endraw %}<br><br>

2. Anexando `?br_user_id=` seguido por {% raw %}`{{${user_id}}}`{% endraw %}
  - **Exemplo de link:** {% raw %}`https://www.client-website.com?br_user_id={{${user_id}}}`{% endraw %}

A variável `braze_id` é definida como um identificador do usuário gerado pelo Braze e está sempre disponível. A variável `br_user_id` é definida como o identificador do usuário no seu sistema e pode estar ausente em certos cenários (por exemplo, para usuários anônimos criados pelo SDK da Braze). Se ambos `braze_id` e `br_user_id` forem usados em um link, a SalesWings considerará apenas o parâmetro `braze_id`.

### Usando eventos Braze Currents em seu CRM

Se você conectar um Current Braze ao SalesWings, o SalesWings criará perfis de leads identificados para cada usuário do Braze com um e-mail e registrará eventos Braze suportados como atividade de lead. Em seu CRM, todos os dados podem ser automaticamente agregados no nível da conta do lead. A atividade e os dados registrados podem ser combinados ainda mais com os dados comportamentais coletados com o script de rastreamento do SalesWings ou Segment.com, ou enviando outros dados para a API do SalesWings, e depois usados para identificar as necessidades e a prontidão para vendas de seus prospects para seus processos de gerenciamento de leads e contas.

A tabela a seguir mostra os tipos de eventos Braze suportados pelo SalesWings e sua representação no histórico de atividade de leads do SalesWings e no mecanismo de regras:

| Categoria do Evento | Tipo de evento | Nome do Evento no SalesWings |
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
| Eventos de mensagem | SMS/MMS Recebido | `[SMS/mobile campaign engagement] We received a message from this person to our internal number $inbound_phone_number: $message_body` |
| Eventos de mensagem | Clique em link encurtado em SMS/MMS | `[SMS/mobile campaign engagement] Clicked on $short_url` |
| Eventos de mensagem | WhatsApp Recebido | `[WhatsApp engagement] We received a message from this person to our WhatsApp number $inbound_phone_number: $message_body` |
| Eventos de mensagem | Leitura de WhatsApp | `[WhatsApp engagement] Lead read our message from the $campaign_name campaign` |
| Inscrições | Alteração de estado de inscrição global | `[Subscription status change] Global marketing subscription setting set to $subscription_status` |
| Inscrições | Alteração de estado do grupo de inscrições | `[Subscription status change] $subscription_status to/from $campaign_name` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Você pode então configurar **Evento Personalizado** > **Nome do Evento** e **Evento Personalizado** > **Propriedade do Evento** condições para tags e pontuações do SalesWings contra os nomes de eventos do SalesWings da tabela acima. A lista de propriedades de eventos disponíveis para condições é preenchida previamente com algumas das entradas comumente usadas, e você pode sempre adicionar novas na seção **Propriedade do Evento** da [página de configuração do Mecanismo de Regras](https://helium.saleswings.pro/falcon).

![Exemplo de uma condição de Nome de Evento.]({% image_buster /assets/img/saleswings/saleswings_braze_lead_scoring_custom_event_condition.png %})

Para configuração e mais solução de problemas, entre em contato com a [equipe de serviços da SalesWings](https://www.saleswingsapp.com/?utm_source=braze&utm_campaign=technicaldocs) para suporte de integração.

