---
nav_title: SalesWings
article_title: SalesWings
description: "Este artigo de referência descreve a parceria entre a Braze e a SalesWings, uma plataforma de análise de dados, que ajuda você a rastrear pontuação e classificação, insights e alertas de vendas, alinhamento de marketing e relatórios de atribuição B2B."
alias: /partners/saleswings/
page_type: partner
search_tag: Partner

---

# SalesWings

> [SalesWings][1] é um complemento de perfil de leads B2B SaaS desenvolvido para equipes de marketing e vendas, que ajuda a gerenciar a qualificação de leads e contas por meio de pontuação e classificação de leads, insights e alertas de vendas, alinhamento de marketing e relatórios de atribuição B2B, juntamente com uma integração estreita com o Salesforce CRM.

SalesWings permite que as equipes de marketing e os gerentes de operações de marketing qualifiquem leads e contas para suas equipes de vendas, essencial para o alinhamento e eficiência de vendas e marketing. Além disso, a SalesWings, juntamente com a Braze, pode revelar a jornada do cliente de um lead e os dados de engajamento da campanha de marketing da Braze para os representantes de vendas, permitindo que você aumente as taxas de qualificação de leads por meio de conversas mais informadas.

## Pré-requisitos
 
| Requisito | Descrição |
| ----------- | ----------- |
| Conta SalesWings | É necessária uma conta [SalesWings][1] para aproveitar esta parceria. |
| chave da API REST Braze | Uma chave da API REST da Braze com permissões `users.export.ids`. <br><br> Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
| Endpoint REST do Braze | [Seu URL do ponto de extremidade REST][2]. Seu endpoint dependerá da URL do Braze para sua instância. |
| Segment.com conta (opcional) | Se você é um usuário do Segment.com, é possível enviar todos os dados de engajamento e perfis de leads e identificar eventos via Segment.com para a criação de perfis de leads. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Casos de uso

{% tabs %}
{% tab Pontuação de Leads %}

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
Através da integração do SalesWings com o Salesforce, você pode criar relatórios automatizados com leads, contatos, contas e oportunidades com base em dados de engajamento da web e engajamento de campanhas do Braze. Por exemplo, você pode exibir uma lista de leads quentes para uma equipe de vendas, com todos que clicaram em uma campanha de e-mail específica ou realizaram uma ação específica no seu app ou site.

![Exemplo de dashboard vinculado ao e-mail e engajamento de marketing da Braze na Salesforce, observando o impacto das campanhas da Braze nos resultados de vendas e desfechos]({% image_buster /assets/img/saleswings/saleswings_email_campaign_attribution_dashboard.png %})

_Exemplo de dashboard vinculado ao e-mail e engajamento de marketing da Braze na Salesforce, observando o impacto das campanhas da Braze nos resultados de vendas e desfechos_
{% endtab %}
{% endtabs %}

## Integração

### Etapa 1: Conta e configuração do SalesWings

[Agende uma demonstração][4] com a amigável equipe da SalesWings para saber mais sobre a SalesWings.

### Etapa 2: instale o rastreamento comportamental no seu site ou app

Atualmente, existem duas maneiras de coletar dados comportamentais no SalesWings para pontuação de leads e insights de vendas:
* [Implante o JavaScript de rastreamento da SalesWings][5] nos sites e aplicativos onde você deseja rastrear e identificar leads
* Envie dados de atividade de lead comportamental (e dados de perfil de lead) via integração da SalesWings com Segment.com

### Etapa 3: Conectando SalesWings ao Braze

Acessar a [**página de Configurações do SalesWings**][6] e expandir a seção **Integração com a Braze**.

![A seção de Integração da Braze na página de Configurações do SalesWings.][7]

Copie o valor da coluna **Identifier** para a nova chave criada e cole-o no campo **chave de API da Braze** da seção **Integração da Braze do SalesWings**.

Adicione seu endpoint da API da Braze conforme descrito no [artigo de endpoints de API e SDK][8] e insira-o no campo de **endpoint da API Braze**. Copie o valor da coluna **REST Endpoint** (Endpoint REST) e insira-o no campo **Braze API endpoint** (Endpoint da API da Braze) na seção **Braze Integration** (Integração da Braze) da SalesWings.

Em seguida, clique em **Salvar alterações** nas configurações do SalesWings.

### Etapa 4: configure a pontuação de leads da SalesWings para Braze, integração com CRM e mais

Consulte a equipe de serviços da SalesWings para obter suporte completo de integração pelo [website][1].

## Usando esta integração 

Para disparar a pontuação de leads e a criação de insights de vendas, o SalesWings deve identificar um usuário em seu site ou app. Isso pode ocorrer das seguintes maneiras:

- **Envios de formulários:** Quando um usuário envia um formulário da web, o SalesWings identificará automaticamente todos os tipos de formulários da web (como login, baixar, entre em contato conosco, etc.) e resolverá a identidade de um usuário quando ele enviar um formulário. 
- **Cliques em URL com ID da Braze ou ID externo:** Um usuário clica em uma ação de marketing da Braze, tipicamente cliques em e-mail, cliques em banner ou similar, levando a uma página que você está rastreando com SalesWings.
- **Rastreamento de e-mail de vendas via plugins do Gmail e Outlook (opcional):** Se você decidir capacitar seu representante de vendas com plugins de rastreamento de e-mail, ele poderá disparar o rastreamento completo do site dos usuários enviando links rastreáveis.
- **Segment.com identificar evento (opcional):** Se você é um usuário do Segment.com, também pode resolver a identidade de um usuário com a integração do Segment.com.

### Identificando usuários a partir de cliques em URLs

Você pode identificar os usuários automaticamente quando eles clicam em um URL rastreável (por exemplo, e-mails em massa, banners com URLs). Para tornar uma URL rastreável, existem duas maneiras de modificar os URLs do seu site em seus e-mails, banners ou SMS, adicionando o parâmetro e o ID ao final de seus links.

1. Anexando `?braze_id=` seguido por {% raw %}`{{${braze_id}}}`{% endraw %} 
  - **Exemplo de link:** {% raw %}`https://www.your-website.com?braze_id={{${braze_id}}}`{% endraw %}<br><br>

2. Anexando `?br_user_id=` seguido por {% raw %}`{{${user_id}}}`{% endraw %}
  - **Exemplo de link:** {% raw %}`https://www.client-website.com?br_user_id={{${user_id}}}`{% endraw %}

A variável `braze_id` é definida como um identificador do usuário gerado pelo Braze e está sempre disponível. A variável `br_user_id` é definida como o identificador do usuário no seu sistema e pode estar ausente em certos cenários (por exemplo, para usuários anônimos criados pelo SDK da Braze). Se ambos `braze_id` e `br_user_id` forem usados em um link, a SalesWings considerará apenas o parâmetro `braze_id`.

Para configuração e mais solução de problemas, entre em contato com a [equipe de serviços da SalesWings][1] para suporte de integração.

[1]: https://www.saleswingsapp.com/?utm_source=braze&utm_campaign=technicaldocs
[2]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[3]: https://www.saleswingsapp.com/braze-lead-scoring-and-sales-insights?utm_source=braze&utm_campaign=technicaldocs
[4]: https://www.saleswingsapp.com/schedule-a-demo?utm_source=braze&utm_campaign=technicaldocs
[5]: https://support.saleswingsapp.com/en/collections/3285135-1-implementing-saleswings-tracking-script
[6]: https://helium.saleswings.pro/settings
[7]: {% image_buster /assets/img/saleswings/saleswings_braze_lead_scoring_integration_settings.png %}
[8]: {{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints
