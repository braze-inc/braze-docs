---
nav_title: Glossário de métricas de relatório
article_title: Glossário de métricas de relatórios
layout: report_metrics
page_order: 0.5
excerpt_separator: ""
page_type: glossary
description: "Este glossário define os termos que você encontrará em seus relatórios na sua conta da Braze."
tool: Reports
---

<style>
  .calculation-line {
    color: #76848C;
    font-size: 14px;
  }
</style>

{% api %}

### Cliques de AMP

{% apitags %}
E-mail
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='AMP Clicks' %}

{% endapi %}

{% api %}

### Aberturas de AMP

{% apitags %}
E-mail
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='AMP Opens' %}

{% endapi %}

{% api %}

### Público

{% apitags %}
Tudo
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Audience' %}

<span class="calculation-line">Cálculo: (Número de destinatários na variante) / (destinatários únicos)</span>

{% endapi %}

{% api %}

### Bounces

{% apitags %}
E-mail, Push para a web, iOS Push
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Bounces' %} Isso pode ocorrer porque não há um token por push válido, o usuário cancelou a inscrição após o lançamento da campanha ou o endereço de e-mail está incorreto ou desativado.

|Canal|Informações adicionais|
|-------|-----------------------|
|E-mail|Um bounce de e-mail para clientes que usam o SendGrid consiste em hard bounces, spam (`spam_report_drops`) e e-mails enviados para endereços inválidos (`invalid_emails`).<br><br>Para e-mail, a % de *bounce* ou a *taxa de bounce* é a porcentagem de mensagens que foram enviadas sem sucesso ou designadas como "devolvidas" ou "não recebidas" dos serviços de envio usados ou não recebidas pelos usuários de e-mail pretendidos.|
|Push|Esses usuários foram automaticamente cancelados de todas as futuras notificações por push.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Bounces</i>: Contagem</li>
        <li><i>Bounce %</i> ou <i>Bounce Rate %</i>: (Bounces) / (Envios)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Clique no corpo

{% apitags %}
iOS Push, Android Push
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Body Click' %}

<span class="calculation-line">Cálculo: (Cliques no corpo) / (Impressões)</span>

{% endapi %}

{% api %}

### Cliques no corpo

{% apitags %}
Mensagem no app
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Body Clicks' %} Para mais detalhes, consulte os changelogs do SDK para [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/changelog/objc_changelog#3310) e [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/changelog#1100).

<span class="calculation-line">Cálculo: (Cliques no corpo) / (Impressões)</span>

{% endapi %}

{% api %}

### Cliques no botão 1

{% apitags %}
Mensagem no app
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Button 1 Clicks' %} O relatório para _Cliques no Botão 1_ só funciona quando você especifica o **Identificador para Relatório** como "0" na mensagem no app.

<span class="calculation-line">Cálculo: (Cliques no Botão 1) / (Impressões)</span>

{% endapi %}

{% api %}

### Cliques no botão 2

{% apitags %}
Mensagem no app
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Button 2 Clicks' %} O relatório para _Cliques no Botão 2_ só funciona quando você especifica o **Identificador para Relatório** como "1" na mensagem no app.

<span class="calculation-line">Cálculo: (Cliques no Botão 2) / (Impressões)</span>

{% endapi %}

{% api %}

### Análise de dados de campanha

{% apitags %}
Feature Flags
{% endapitags %}

A performance da mensagem em vários canais. As métricas mostradas dependem do canal de envio de mensagens selecionado e se o [experimento de Feature Flag]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/experiments/#campaign-analytics) é um teste multivariante.

{% endapi %}

{% api %}

### Opções enviadas

{% apitags %}
Mensagem no app
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Choices Submitted' %}

{% endapi %}

{% api %}

### Taxa de cliques por abertura

{% apitags %}
E-mail
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Click-to-Open Rate' %}

<span class="calculation-line">Cálculo: (Cliques únicos) / (Aberturas únicas) (para e-mail)</span>

{% endapi %}

{% api %}

### Entregas confirmadas de RCS ou entregas confirmadas de SMS

{% apitags %}
SMS/MMS, RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confirmed Deliveries' %} Como cliente da Braze, as entregas são contabilizadas em sua cota de SMS. 

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Entregas confirmadas:</i> Contagem</li>
        <li><i>Taxa de entrega confirmada:</i> (Entregas confirmadas) / (Envios)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Confiança

{% apitags %}
Cartões de conteúdo, E-mail, Mensagem no app, Push para a web, iOS Push, Android Push, Webhook, SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confidence' %}

{% endapi %}

{% api %}

### Botão da página de confirmação

{% apitags %}
Mensagem no app
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confirmation Page Button' %}

{% endapi %}

{% api %}

### Dispensas da página de confirmação

{% apitags %}
Mensagem no app
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confirmation Page Dismissals' %}

{% endapi %}

{% api %}

### Conversões (B, C, D)

{% apitags %}
Cartões de conteúdo, E-mail, Mensagem no app, Push para a web, iOS Push, Android Push, Webhook, SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Conversions (B, C, D)' %} Este evento definido é determinado por você ao construir a campanha. 

|Canal|Informações adicionais|
|-------|-----------------------|
|E-mail, Push, Webhooks|As conversões são rastreadas após o envio inicial.|
|Cartões de conteúdo|As conversões são contadas quando o usuário visualiza um cartão de conteúdo pela primeira vez.|
|Mensagem no app|Uma conversão é contada se o usuário recebeu e visualizou a campanha de mensagem no app e, subsequentemente, realiza o evento de conversão específico dentro do período de conversão definido, independentemente de ter clicado na mensagem ou não.<br><br>As conversões são atribuídas à mensagem recebida mais recentemente. Se a reelegibilidade estiver ativada, a conversão será atribuída à última mensagem no app recebida, desde que ocorra dentro do período de conversão definido. No entanto, se a mensagem no app já tiver sido atribuída a uma conversão, a nova conversão não poderá ser registrada para essa mensagem específica. Isso significa que cada envio de mensagem no app está associado a apenas uma conversão.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endapi %}

{% api %}

### Conversões totais

{% apitags %}
Mensagem no app
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Conversions' %}

Quando um usuário visualiza uma campanha de mensagem no app apenas uma vez, apenas uma conversão é contada, mesmo que ele realize o evento de conversão várias vezes posteriormente. No entanto, se a reelegibilidade estiver ativada e o usuário vir a campanha de mensagem no app várias vezes, o *total de conversões* poderá aumentar uma vez para cada vez que o usuário registrar uma impressão para uma nova instância da campanha de mensagem no app. 

Por exemplo, se um usuário disparar uma mensagem no app duas vezes e converter após cada impressão de mensagem no app (resultando em duas conversões), o *Total de conversões* aumentará em dois. No entanto, se houver apenas uma impressão de mensagem no app seguida de dois eventos de conversão, apenas uma conversão será registrada e o *Total de conversões* aumentará em um.

{% endapi %}

{% api %}

### Fechar mensagem

{% apitags %}
Mensagem no app
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Close Message' %}

{% endapi %}

{% api %}

### Taxa de conversão

{% apitags %}
Cartões de conteúdo, E-mail, Mensagem no app, Push para a web, iOS Push, Android Push, Webhook, SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Conversion Rate' %}

|Canal|Informações adicionais|
|-------|-----------------------|
|Mensagem no app|A métrica do total de <i>impressões únicas</i> diárias é usada para calcular a <i>taxa de conversão</i> de mensagens no app.<br><br>As impressões de mensagens no app só podem ser contadas uma vez por dia. Por outro lado, o número de vezes que um usuário conclui uma ação desejada (uma "conversão") pode aumentar em um período de 24 horas. Embora as conversões possam ocorrer mais de uma vez por dia, as impressões não podem. Portanto, se um usuário concluir uma conversão várias vezes em um dia, a <i>taxa de conversão</i> poderá aumentar de acordo, mas as impressões serão contadas apenas uma vez.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><b>Mensagens no app</b>: (Conversões primárias) / (Impressões únicas)</li>
        <li><b>Outros canais</b>: (Conversões primárias) / (Destinatários únicos)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Período de conversão

{% apitags %}
Tudo
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Conversion Window' %}

{% endapi %}

{% api %}

### Entregas

{% apitags %}
E-mail, Push para a web, iOS Push, Android Push, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Deliveries' %}

|Canal|Informações adicionais|
|-------|-----------------------|
|E-mail|Refere-se ao número total de mensagens (Envios) enviadas com sucesso e recebidas por destinatários com e-mail válido.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Entregas</i>: Contagem</li>
        <li><i>Entregas %</i>: (Envios - Bounces) / (Envios)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Falhas de entrega de RCS ou falhas de entrega de SMS

{% apitags %}
SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Delivery Failures' %}

Fale com o <a href="/docs/braze_support/">suporte da Braze</a> para obter assistência sobre as razões das falhas de entrega.

<span class="calculation-line">Cálculo: (Envios) - (Envios para a operadora)</span>

{% endapi %}

{% api %}

### Falhas na entrega

{% apitags %}
RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Delivery Failures RCS' %}

Fale com o <a href="/docs/braze_support/">suporte da Braze</a> para obter assistência sobre as razões das falhas de entrega.

<span class="calculation-line">Cálculo: (Envios) - (Envios para a operadora)</span>

{% endapi %}

{% api %}

### Taxa de falhas de entrega

{% apitags %}
SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Failed Delivery Rate' %}

Fale com o <a href="/docs/braze_support/">suporte da Braze</a> para obter assistência sobre as razões das falhas de entrega.

<span class="calculation-line">Cálculo: (Falhas de entrega) / (Envios)</span>

{% endapi %}

{% api %}

### Aberturas diretas

{% apitags %}
iOS Push
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Direct Opens' %}

<span class="calculation-line">Cálculo: (Aberturas diretas) / (Entregas)</span>

{% endapi %}

{% api %}

### Aptos para e-mail

{% apitags %}
E-mail
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Emailable' %}

<span class="calculation-line">Cálculo: Contagem</span>

{% endapi %}

{% api %}

### Erros

{% apitags %}
Webhook
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Errors' %} Os erros estão incluídos na contagem de <i>Envios</i>, mas não estão incluídos na contagem de <i>Destinatários únicos</i>.

{% endapi %}

{% api %}

### Estimativa de aberturas reais

{% apitags %}
E-mail
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Estimated Real Opens' %}

{% endapi %}

{% api %}

### Falhas

{% apitags %}
WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Failures' %} As falhas estão incluídas na contagem de <i>Envios</i>, mas não na contagem de <i>Entregas</i>.</td>

<span class="calculation-line">Cálculo (<i>Taxa de falha</i>): (Falhas) / (Envios)</span>

{% endapi %}

{% api %}

### Performance do experimento de Feature Flag

{% apitags %}
Feature Flags
{% endapitags %}

Métricas de performance da mensagem em um experimento de Feature Flag. As métricas específicas mostradas variam dependendo do canal de envio de mensagens e se o experimento foi um teste multivariante ou não.

{% endapi %}

{% api %}

### Hard bounce

{% apitags %}
E-mail
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Hard Bounce' %} 

Quando isso ocorre, a Braze marca o endereço de e-mail como inválido, mas não atualiza o [status da inscrição]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/) do usuário. Se um e-mail receber um hard bounce, interromperemos todas as solicitações futuras para esse endereço de e-mail.

{% endapi %}

{% api %}

### Ajuda

{% apitags %}
SMS/MMS, RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Help' %} Uma resposta do usuário é medida sempre que um usuário envia uma mensagem de entrada dentro de quatro horas após receber sua mensagem.

{% endapi %}

{% api %}

### Aberturas por influência

{% apitags %}
iOS Push, Android Push
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Influenced Opens' %}

<span class="calculation-line">Cálculo: (Aberturas por influência) / (Entregas)</span>

{% endapi %}

{% api %}

### Receita por tempo de vida

{% apitags %}
Cartões de conteúdo, E-mail, Mensagem no app, Push para a web, iOS Push, Android Push, Webhook, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Lifetime Revenue' %}

{% endapi %}

{% api %}

### Valor do tempo de vida por usuário

{% apitags %}
Cartões de conteúdo, E-mail, Mensagem no app, Push para a web, iOS Push, Android Push, Webhook, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Lifetime Value Per User' %}

{% endapi %}

{% api %}

### Receita média diária

{% apitags %}
Cartões de conteúdo, E-mail, Mensagem no app, Push para a web, iOS Push, Android Push, Webhook, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Average Daily Revenue' %}

{% endapi %}

{% api %}

### Compras diárias

{% apitags %}
Cartões de conteúdo, E-mail, Mensagem no app, Push para a web, iOS Push, Android Push, Webhook, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Daily Purchases' %}

{% endapi %}

{% api %}

### Receita diária por usuário

{% apitags %}
Cartões de conteúdo, E-mail, Mensagem no app, Push para a web, iOS Push, Android Push, Webhook, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Daily Revenue Per User' %}

{% endapi %}

{% api %}

### Aberturas por máquina

{% apitags %}
E-mail
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Machine Opens' %} Essa métrica é rastreada a partir de 11 de novembro de 2021 para SendGrid e 2 de dezembro de 2021 para SparkPost. Para Amazon SES, a análise de dados aparecerá como _Aberturas_. No entanto, a filtragem de bot para cliques será suportada.

{% endapi %}

{% api %}

### Aberturas

{% apitags %}
Push para a web, iOS Push, Android Push
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Opens' %}

{% endapi %}

{% api %}

### Opt-Out

{% apitags %}
SMS/MMS, RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Opt-Out' %} Uma resposta do usuário é medida sempre que um usuário envia uma mensagem de entrada dentro de quatro horas após receber sua mensagem.

{% endapi %}

{% api %}

### Outras aberturas

{% apitags %}
E-mail
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Other Opens' %} Observe que um usuário também pode abrir um e-mail (e essa abertura conta para Outras aberturas) antes que uma contagem de Aberturas por máquina seja registrada. Se um usuário abrir um e-mail uma vez (ou mais) após um evento de abertura por máquina de uma caixa de entrada que não seja do Apple Mail, a quantidade de vezes que o usuário abrir o e-mail será calculada para Outras aberturas e apenas uma vez para Aberturas únicas.

{% endapi %}

{% api %}

### Repetição pendente

{% apitags %}
E-mail
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Pending Retry' %}

{% endapi %}

{% api %}

### Conversões primárias (A) ou evento de conversão primária

{% apitags %}
Cartões de conteúdo, E-mail, Mensagem no app, Push para a web, iOS Push, Android Push, Webhook, SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Primary Conversions (A) or Primary Conversion Event' %} 

|Canal|Informações adicionais|
|-------------|----------------------|
|E-mail, Push, Webhooks|Após o envio inicial.|
|Cartões de conteúdo, Mensagens no app|Quando o usuário visualiza o cartão de conteúdo ou a mensagem pela primeira vez.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Conversões primárias (A) ou Evento de conversão primária</i>: Contagem</li>
        <li><i>Conversões primárias (A) %</i> ou <i>Taxa de evento de conversão primária</i>: (Conversões primárias) / (Destinatários únicos)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Leituras

{% apitags %}
WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Reads' %}

{% endapi %}

{% api %}

### Taxa de leitura

{% apitags %}
WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Read Rate' %}

<span class="calculation-line">Cálculo: (Leituras com confirmação de leitura) / (Envios)</span>

{% endapi %}

{% api %}

### Recebido

{% apitags %}
E-mail, Cartões de conteúdo, Mensagem no app, Push para a web, iOS Push, Android Push, SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Received' %} 

|Canal|Informações adicionais|
|-------|-------|
|Cartões de conteúdo|Recebido quando os usuários visualizam o cartão no app.|
|Push|Recebido quando as mensagens são enviadas do servidor da Braze para o provedor de push.|
|E-mail|Recebido quando as mensagens são enviadas do servidor da Braze para o prestador de serviço de e-mail.|
|SMS/MMS|"Entregue" depois que o provedor de SMS recebe a confirmação da operadora upstream e do dispositivo de destino.|
|Mensagem no app|Recebido no momento da exibição com base na ação-gatilho definida.|
|WhatsApp|Recebido no momento da exibição com base na ação-gatilho definida.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endapi %}

{% api %}

### Rejeições de RCS ou rejeições de SMS

{% apitags %}
SMS/MMS, RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Rejections' %} Como cliente da Braze, as rejeições são contabilizadas em sua cota de SMS.

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Rejeições:</i> Contagem</li>
        <li><i>Taxa de rejeição:</i> (Rejeições) / (Envios)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Receita

{% apitags %}
E-mail
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Revenue' %}

{% endapi %}

{% api %}

### Enviados

{% apitags %}
SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Sent' %}

<span class="calculation-line">Cálculo: Contagem</span>

{% endapi %}

{% api %}

### Envios

{% apitags %}
Cartões de conteúdo, E-mail, Mensagem no app, Push para a web, iOS Push, Android Push, Webhook, SMS/MMS, RCS, WhatsApp, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Sends' %} Esta métrica é fornecida pela Braze. Observe que, ao lançar uma campanha programada, essa métrica incluirá todas as mensagens enviadas, independentemente de já terem sido enviadas devido ao limite de taxa.

{% alert tip %}
Para cartões de conteúdo, essa métrica é calculada de forma diferente, dependendo do que você selecionou para a [criação do cartão]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/):

- **No lançamento ou na entrada da etapa:** O número de cartões criados e disponíveis para serem vistos. Isso não conta se os usuários visualizaram o cartão.
- **Na primeira impressão:** O número de cartões exibidos aos usuários.
{% endalert %}

<span class="calculation-line">Cálculo: Contagem</span>

{% endapi %}

{% api %}

### Mensagens enviadas

{% apitags %}
Cartões de conteúdo, E-mail, Mensagem no app, Push para a web, iOS Push, Android Push, Webhook, SMS/MMS, WhatsApp, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Messages Sent' %} Esta métrica é fornecida pela Braze. Observe que, ao lançar uma campanha programada, essa métrica incluirá todas as mensagens enviadas, independentemente de já terem sido enviadas devido ao limite de taxa.

{% alert tip %}
Para cartões de conteúdo, essa métrica é calculada de forma diferente, dependendo do que você selecionou para a [criação do cartão]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/):

- **No lançamento ou na entrada da etapa:** O número de cartões criados e disponíveis para serem vistos. Isso não conta se os usuários visualizaram o cartão.
- **Na primeira impressão:** O número de cartões exibidos aos usuários.
{% endalert %}

<span class="calculation-line">Cálculo: Contagem</span>

{% endapi %}

{% api %}

### Envios para a operadora

{% apitags %}
SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Sends to Carrier' %} 

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Envios para a operadora:</i> Contagem</li>
        <li><i>Taxa de envios para a operadora:</i> (Envios para a operadora) / (Envios)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Soft bounce

{% apitags %}
E-mail
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Soft Bounce' %} Observe que _soft bounces_ diferem de _deferrals_. Se nenhum e-mail foi entregue com sucesso durante esse período de nova tentativa, a Braze enviará um evento de soft bounce por campanha enviada. Antes de 25 de fevereiro de 2025, essas tentativas eram contadas como múltiplos soft bounces para 1 envio de campanha.

Embora os soft bounces não sejam rastreados na análise de dados da sua campanha, você pode monitorá-los no [Registro de atividade de mensagens]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/). Você também pode excluir esses usuários do seu envio ou verificar a quantidade de soft bounces dos últimos 30 dias com o [filtro de segmento Soft Bounced]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#soft-bounced). No Registro de atividade de mensagens, você também pode ver o motivo dos soft bounces e entender possíveis discrepâncias entre os "envios" e as "entregas" das suas campanhas de e-mail.

{% endapi %}

{% api %}

### Spam

{% apitags %}
E-mail
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Spam' %}

{% alert note %}
As reclamações de spam são tratadas diretamente pelos provedores de serviço de e-mail e, em seguida, retransmitidas para a Braze por meio de um feedback loop. A maioria dos feedback loops relata apenas uma parte das reclamações reais, então a métrica _Spam_ muitas vezes representa uma fração do total real. Apenas os provedores de serviço de e-mail podem ver o verdadeiro volume de reclamações de spam, o que significa que _Spam_ deve ser visto como uma métrica indicativa, não exaustiva.
{% endalert %}

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Spam</i>: Contagem</li>
        <li><i>Spam %</i> ou <i>Spam Rate %</i>: (Marcado como Spam) / (Envios)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Dispensas da página de pesquisa

{% apitags %}
Mensagem no app
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Survey Page Dismissals' %}

{% endapi %}

{% api %}

### Envios de pesquisa

{% apitags %}
Mensagem no app
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Survey Submissions' %}

{% endapi %}

{% api %}

### Total de cliques

{% apitags %}
E-mail, Cartões de conteúdo, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Clicks' %}

|Canal|Informações adicionais|
|-------|-------|
|LINE|Rastreados após um limite mínimo de 20 mensagens por dia ter sido alcançado. E-mails AMP incluem cliques registrados nas versões HTML e texto simples. Esse número pode ser artificialmente inflacionado por ferramentas anti-spam.|
|Banners|O número total (e porcentagem) de usuários que clicaram na mensagem entregue, independentemente de o mesmo usuário clicar várias vezes.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><b>E-mail:</b> (Total de cliques) / (Entregas)</li>
        <li><b>Cartões de conteúdo:</b> (Total de cliques) / (Total de impressões)</li>
        <li><b>SMS:</b> (Cliques de abertura) / (Entregas)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Total de descartes

{% apitags %}
Cartões de conteúdo
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Dismissals' %} Se um usuário receber dois cartões diferentes da mesma campanha e descartar ambos, essa contagem aumentará em dois. A reelegibilidade permite que você incremente o _Total de descartes_ toda vez que um usuário receber um cartão; cada cartão é uma mensagem diferente.

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Total de descartes:</i> Contagem</li>
        <li><i>Taxa total de descartes:</i> Total de descartes / Total de impressões</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Total de impressões

{% apitags %}
Mensagem no app, Cartões de conteúdo
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Impressions' %} Este número é a soma do número de eventos de impressão que a Braze recebe dos SDKs.

|Canal|Informações adicionais|
|-------|-----------------------|
|Cartões de conteúdo|A contagem total de impressões registradas para um determinado cartão de conteúdo. Isso pode ser incrementado várias vezes para o mesmo usuário.|
|Mensagem no app|Se houver vários dispositivos e a reelegibilidade estiver desativada, o usuário deve ver a mensagem no app apenas uma vez. Mesmo que o usuário use vários dispositivos, ele só a verá no primeiro dispositivo direcionado. Isso pressupõe que o perfil tenha dispositivos consolidados e que um usuário tenha um ID de usuário no qual esteja conectado em todos os dispositivos. Se a reelegibilidade estiver ativada, uma impressão é registrada toda vez que esse usuário vê a mensagem no app.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

<span class="calculation-line">Cálculo: Contagem</span>

{% endapi %}

{% api %}

### Total de aberturas

{% apitags %}
E-mail, iOS Push, Android Push, Push para a web, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Opens' %}

|Canal|Informações adicionais|
|-------|-----------------------|
|LINE|Rastreados após um limite mínimo de 20 mensagens por dia ter sido alcançado.|
|E-mails AMP|O total de aberturas para as versões HTML e texto simples.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><b>E-mail <i>Total Opens</i>:</b> Contagem</li>
        <li><b>E-mail <i>Total Open Rate</i>:</b> (Aberturas) / (Entregas)</li>
        <li><b>Push para a web <i>Total Opens</i>:</b> Contagem de <i>aberturas diretas</i></li>
        <li><b>Push para a web <i>Total Open Rate</i>:</b> (Total Opens) / (Entregas)</li>
        <li><b>iOS, Android e Kindle Push <i>Total Opens</i>:</b> (Aberturas diretas) + (Aberturas por influência)</li>
        <li><b>iOS, Android e Kindle Push <i>Total Open Rate</i>:</b> (Total Opens) / (Entregas)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Total de receita

{% apitags %}
Cartões de conteúdo, E-mail, Mensagem no app, Push para a web, iOS Push, Android Push, Webhook, SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Revenue' %} Esta métrica está disponível apenas em relatórios de comparação de campanhas por meio do <a href='https://braze.com/docs/user_guide/data_and_analytics/reporting/report_builder/'>Construtor de Relatórios</a>.

{% endapi %}

{% api %}

### Cliques únicos

{% apitags %}
E-mail, Cartões de conteúdo, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Clicks' %}

Isso inclui cliques em links de cancelamento de inscrição fornecidos pela Braze.

|Canal|Informações adicionais|
|-------|-----------------------|
|E-mail|Rastreado ao longo de um período de sete dias.|
|LINE|Rastreados após um limite mínimo de 20 mensagens por dia ter sido alcançado.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Cliques únicos</i>: Contagem</li>
        <li><b>Cartões de conteúdo</b> <i>% de cliques únicos</i> ou <i>Taxa de cliques únicos</i>: (Cliques únicos) / (Impressões únicas)</li>
        <li><b>E-mail</b> <i>% de cliques únicos</i> ou <i>Taxa de cliques únicos</i>: (Cliques únicos) / (Entregas)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Descartes únicos

{% apitags %}
Cartões de conteúdo
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Dismissals' %}

<span class="calculation-line">Cálculo: (Descartes únicos) / (Impressões únicas)</span>

{% endapi %}

{% api %}

### Impressões únicas

{% apitags %}
Mensagem no app, Cartões de conteúdo
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Impressions' %} 

|Canal|Informações adicionais|
|-------|-----------------------|
|Mensagem no app|As impressões únicas podem ser incrementadas novamente após 24 horas se a reelegibilidade estiver ativada e o usuário realizar a ação-gatilho. Se a reelegibilidade estiver ativada, <i>Impressões únicas</i> = <i>Destinatários únicos</i>.|
|Cartões de conteúdo|A contagem não deve ser incrementada na segunda vez que um usuário visualiza um cartão.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

<span class="calculation-line">Cálculo: Contagem</span>

{% endapi %}

{% api %}

### Aberturas únicas

{% apitags %}
E-mail, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Opens' %}

|Canal|Informações adicionais|
|-------|-----------------------|
|E-mail|Rastreado ao longo de um período de 7 dias.|
|LINE|Rastreados após um limite mínimo de 20 mensagens por dia ter sido alcançado.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Aberturas únicas</i>: Contagem</li>
        <li><i>% de aberturas únicas</i> ou <i>Taxa de abertura única</i>: (Aberturas únicas) / (Entregas)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Destinatários únicos

{% apitags %}
Tudo
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Recipients' %}

Como um visualizador pode ser um destinatário único todos os dias, você deve esperar que esse valor seja maior do que o de <i>Impressões únicas</i>. Para cartões de conteúdo, cada cartão de conteúdo pode ser recebido apenas uma vez, portanto, visualizar o mesmo cartão de conteúdo uma segunda vez, independentemente do dia, não incrementará essa contagem.<br><br>Esse número é recebido da Braze e se baseia no `user_id`. Os destinatários únicos são contados no nível da campanha ou etapa do canva, não no nível do <a href='https://braze.com/docs/api/identifier_types/#send-identifier'>identificador de envio</a>.

<span class="calculation-line">Cálculo: Contagem</span>

{% endapi %}

{% api %}

### Cancelamento de inscrição

{% apitags %}
E-mail
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unsubscribers or Unsub' %}

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Cancelamentos de inscrição</i> ou <i>Unsub</i>: Contagem</li>
        <li><i>% de cancelamentos de inscrição</i> ou <i>Taxa de cancelamento de inscrição</i>: (Cancelamentos de inscrição) / (Entregas)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Cancelamentos de inscrição

{% apitags %}
E-mail
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unsubscribes' %}

<span class="calculation-line">Cálculo: (Cancelamentos de inscrição) / (Entregas)</span>

{% endapi %}

{% api %}

### Variação

{% apitags %}
Cartões de conteúdo, E-mail, Mensagem no app, Push para a web, iOS Push, Android Push, Webhook, SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Variation' %}

<span class="calculation-line">Cálculo: Contagem</span>

{% endapi %}