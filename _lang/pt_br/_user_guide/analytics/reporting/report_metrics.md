---
nav_title: Glossário de métricas de relatório
article_title: Glossário de métricas de relatórios
layout: report_metrics
page_order: 0.5
excerpt_separator: ""
page_type: glossary
description: "Este glossário define os termos que você encontrará em seus relatórios na sua conta Braze."
tool: Reports
---

<style>
  .calculation-line {
    color: #76848C;
    font-size: 14px;
  }
</style>

{% api %}

### Cliques de accelerated mobile pages

{% apitags %}
E-mail
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='AMP Clicks' %}

{% endapi %}

{% api %}

### Aberturas de accelerated mobile pages

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
Envio de e-mail, Web Push, iOS Push
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Bounces' %} Isso pode ocorrer porque não há um token por push válido, o usuário cancelou a inscrição após o lançamento da campanha ou o endereço de e-mail está incorreto ou desativado.

|Canal|Informações adicionais|
|-------|-----------------------|
|E-mail|Um envio de e-mail para clientes que usam o SendGrid consiste em hard bounce, spam (`spam_report_drops`) e e-mails enviados para endereços inválidos (`invalid_emails`).<br><br>Para e-mail, a % de *bounce* ou a *taxa de bounce* é a porcentagem de mensagens que foram enviadas sem sucesso ou designadas como "devolvidas" ou "não recebidas" dos serviços de envio usados ou não recebidas pelos usuários de e-mail pretendidos.|
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

{% multi_lang_include analytics/metrics.md metric='Body Clicks' %} Para obter mais detalhes, consulte os changelogs do SDK para [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/changelog/objc_changelog#3310) e [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/changelog#1100).

<span class="calculation-line">Cálculo: (Cliques no corpo) / (Impressões)</span>

{% endapi %}

{% api %}

### Cliques no botão 1

{% apitags %}
Mensagem no app
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Button 1 Clicks' %} Os relatórios de _cliques no botão 1_ só funcionam quando você especifica o **identificador para relatórios** como "0" na mensagem no app.

<span class="calculation-line">Cálculo: (Cliques no Botão 1) / (Impressões)</span>

{% endapi %}

{% api %}

### Cliques no botão 2

{% apitags %}
Mensagem no app
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Button 2 Clicks' %} Os relatórios para _cliques no botão 2_ só funcionam quando você especifica o **identificador para relatórios** como "1" na mensagem no app.

<span class="calculation-line">Cálculo: (Botão 2 Cliques) / (Impressões)</span>

{% endapi %}

{% api %}

### Análise de dados de campanha

{% apitags %}
Feature Flags
{% endapitags %}

O desempenho da mensagem em vários canais. As métricas mostradas dependem do canal de envio de mensagens selecionado e se o [experimento do Feature Flag]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/experiments/#campaign-analytics) é um teste multivariado.

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

### Entregas confirmadas por RCS ou entregas confirmadas por SMS

{% apitags %}
SMS/MMS, RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confirmed Deliveries' %} Como cliente Braze, as entregas são cobradas em sua cota de SMS. 

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Entregas Confirmadas:</i> Contagem</li>
        <li><i>Taxa de Entrega Confirmada:</i> (Entregas Confirmadas) / (Envios)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Confiança

{% apitags %}
Cartões de conteúdo, e-mail, mensagem no app, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, WhatsApp
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
Cartões de conteúdo, e-mail, mensagem no app, Web Push, iOS Push, Android Push, Webhook, SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Conversions (B, C, D)' %} Esse evento definido é determinado por você ao criar a campanha. 

|Canal|Informações adicionais|
|-------|-----------------------|
|Envio de e-mail, push, webhooks|As conversões são rastreadas após o envio inicial.|
|Cartões de conteúdo|As conversões são contadas quando o usuário visualiza um cartão de conteúdo pela primeira vez.|
|Mensagem no app|Uma conversão é contada se o usuário tiver recebido e visualizado a campanha de mensagens no app e, subsequentemente, performar o evento de conversão específico dentro da janela de conversão definida, independentemente de ter clicado ou não na mensagem.<br><br>As conversões são atribuídas à mensagem recebida mais recentemente. Se a reelegibilidade estiver ativada, a conversão será atribuída à última mensagem no app recebida, desde que ocorra dentro da janela de conversão definida. No entanto, se a mensagem no app já tiver sido atribuída a uma conversão, a nova conversão não poderá ser registrada para essa mensagem específica. Isso significa que cada envio de mensagens no app está associado a apenas uma conversão.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endapi %}

{% api %}

### Conversões totais

{% apitags %}
Mensagem no app
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Conversions' %}

Quando um usuário visualiza uma campanha de mensagens no app apenas uma vez, apenas uma conversão é contada, mesmo que ele realize o evento de conversão várias vezes posteriormente. No entanto, se a reelegibilidade estiver ativada e o usuário vir a campanha de mensagens no app várias vezes, o *total de conversões* poderá aumentar uma vez para cada vez que o usuário registrar uma impressão para uma nova instância da campanha de mensagens no app. 

Por exemplo, se um usuário disparar uma mensagem no app duas vezes e converter após cada impressão de mensagem no app (resultando em duas conversões), o *Total de conversões* aumentará em dois. No entanto, se houver apenas uma impressão de mensagem no app seguida de dois eventos de conversão, apenas uma conversão será registrada e o *total de conversões* aumentará em um.

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
Cartões de conteúdo, e-mail, mensagem no app, Web Push, iOS Push, Android Push, Webhook, SMS/MMS
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
        <li><b>Mensagens no app</b>: (Conversões primárias) / (impressões exclusivas)</li>
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
E-mail, Web Push, iOS Push, Android Push, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Deliveries' %}

|Canal|Informações adicionais|
|-------|-----------------------|
|E-mail|Refere-se ao número total de mensagens (Envios) enviadas e recebidas com êxito por partes que podem enviar e-mails.|
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

### Falhas na entrega de RCS ou falhas na entrega de SMS

{% apitags %}
SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Delivery Failures' %}

Entre em contato com <a href="/docs/braze_support/">o suporte da Braze</a> para obter assistência na compreensão dos motivos das falhas de entrega.

<span class="calculation-line">Cálculo: (Envia) - (Envia para a operadora)</span>

{% endapi %}

{% api %}

### Falhas na entrega

{% apitags %}
RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Delivery Failures RCS' %}

Entre em contato com <a href="/docs/braze_support/">o suporte da Braze</a> para obter assistência na compreensão dos motivos das falhas de entrega.

<span class="calculation-line">Cálculo: (Envia) - (Envia para a operadora)</span>

{% endapi %}

{% api %}

### Taxa de entregas com falhas

{% apitags %}
SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Failed Delivery Rate' %}

Entre em contato com <a href="/docs/braze_support/">o suporte da Braze</a> para obter assistência na compreensão dos motivos das falhas de entrega.

<span class="calculation-line">Cálculo: (Falhas de Entrega) / (Envios)</span>

{% endapi %}

{% api %}

### Aberturas diretas

{% apitags %}
Push para iOS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Direct Opens' %}

<span class="calculation-line">Cálculo: (aberturas diretas) / (entregas)</span>

{% endapi %}

{% api %}

### Envio de e-mail

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

{% multi_lang_include analytics/metrics.md metric='Errors' %} Os erros são incluídos na contagem de <i>Envios</i>, mas não são incluídos na contagem de <i>Destinatários Únicos</i>.

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

{% multi_lang_include analytics/metrics.md metric='Failures' %} As falhas são incluídas na contagem de <i>envios</i>, mas não na contagem de <i>entregas</i>.</td>

<span class="calculation-line">Cálculo<i>(taxa de falha)</i>: (Falhas) / (Envios)</span>

{% endapi %}

{% api %}

### Desempenho do experimento de Feature Flag

{% apitags %}
Feature Flags
{% endapitags %}

Métricas de desempenho da mensagem em um experimento de Feature Flag. As métricas específicas mostradas variarão dependendo do canal de envio de mensagens e se o experimento foi um teste multivariado ou não.

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

{% multi_lang_include analytics/metrics.md metric='Help' %} Uma resposta do usuário é medida sempre que um usuário envia uma mensagem de entrada dentro de quatro horas após o recebimento da sua mensagem.

{% endapi %}

{% api %}

### Aberturas por influência

{% apitags %}
iOS Push, Android Push
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Influenced Opens' %}

<span class="calculation-line">Cálculo: (aberturas por influência) / (entregas)</span>

{% endapi %}

{% api %}

### Receitas por tempo de vida

{% apitags %}
Cartões de conteúdo, e-mail, mensagem no app, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Lifetime Revenue' %}

{% endapi %}

{% api %}

### Valor de tempo de vida por usuário

{% apitags %}
Cartões de conteúdo, e-mail, mensagem no app, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Lifetime Value Per User' %}

{% endapi %}

{% api %}

### Receita média diária

{% apitags %}
Cartões de conteúdo, e-mail, mensagem no app, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Average Daily Revenue' %}

{% endapi %}

{% api %}

### Compras diárias

{% apitags %}
Cartões de conteúdo, e-mail, mensagem no app, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Daily Purchases' %}

{% endapi %}

{% api %}

### Receitas diárias por usuário

{% apitags %}
Cartões de conteúdo, e-mail, mensagem no app, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Daily Revenue Per User' %}

{% endapi %}

{% api %}

### Aberturas por máquina

{% apitags %}
E-mail
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Machine Opens' %} Essa métrica é rastreada a partir de 11 de novembro de 2021 para a SendGrid e de 2 de dezembro de 2021 para a SparkPost. Para o Amazon SES, a análise de dados será exibida como _Opens_. No entanto, haverá suporte para a filtragem de bots para cliques.

{% endapi %}

{% api %}

### Aberturas

{% apitags %}
Web push, iOS push, Android push
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Opens' %}

{% endapi %}

{% api %}

### Cancelamentos de inscrição

{% apitags %}
SMS/MMS, RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Opt-Out' %} Uma resposta do usuário é medida sempre que um usuário envia uma mensagem de entrada dentro de quatro horas após o recebimento da sua mensagem.

{% endapi %}

{% api %}

### Outras aberturas

{% apitags %}
E-mail
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Other Opens' %} Note que um usuário também pode abrir um e-mail (como as contagens de abertura para Outras aberturas) antes que uma contagem de Aberturas de máquina seja registrada. Se um usuário abrir um e-mail uma vez (ou mais) após um evento de abertura de máquina de uma caixa de entrada que não seja do Apple Mail, a quantidade de vezes que o usuário abrir o e-mail será calculada para Outras aberturas e apenas uma vez para Aberturas exclusivas.

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
Cartões de conteúdo, e-mail, mensagem no app, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Primary Conversions (A) or Primary Conversion Event' %} 

|Canal|Comportamento|
|-------------|----------------------|
|Envio de e-mail, push, webhooks|O usuário é contado como um destinatário depois que a mensagem é enviada.|
|Cartões de conteúdo, mensagens no app|O usuário é contado como destinatário depois de visualizar a mensagem pela primeira vez.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Conversões primárias (A) ou Evento de conversão primária</i>: Número de usuários que concluíram o evento de conversão primária dentro da janela de conversão definida </li>
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

<span class="calculation-line">Cálculo: (Leituras com recibos de leitura) / (Envios)</span>

{% endapi %}

{% api %}

### Recebido

{% apitags %}
E-mail, cartões de conteúdo, mensagem no app, web push, iOS push, Android push, SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Received' %} 

|Canal|Informações adicionais|
|-------|-------|
|Cartões de conteúdo|Recebido quando os usuários visualizam o cartão no aplicativo.|
|Push|Recebido quando as mensagens são enviadas do servidor Braze para o provedor push.|
|E-mail|Recebido quando as mensagens são enviadas do servidor do Braze para o provedor de serviço de e-mail.|
|SMS/MMS|"Entregue" depois que o provedor de SMS receber a confirmação da operadora upstream e do dispositivo de destino.|
|Mensagem no app|Recebido no momento da exibição com base na ação-gatilho definida.|
|WhatsApp|Recebido no momento da exibição com base na ação-gatilho definida.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endapi %}

{% api %}

### Rejeições de RCS ou rejeições de SMS

{% apitags %}
SMS/MMS, RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Rejections' %} Como cliente Braze, as rejeições são cobradas em sua cota de SMS.

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Rejeições:</i> Contagem</li>
        <li><i>Taxa de Rejeição:</i> (Rejeições) / (Envios)</li>
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

### Envios

{% apitags %}
SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Sent' %}

<span class="calculation-line">Cálculo: Contagem</span>

{% endapi %}

{% api %}

### Envios

{% apitags %}
Cartões de conteúdo, e-mail, mensagem no app, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, RCS, WhatsApp, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Sends' %} Essa métrica é fornecida pelo Braze. Observe que, ao lançar uma campanha programada, essa métrica incluirá todas as mensagens enviadas, independentemente de já terem sido enviadas devido ao limite de frequência.

{% alert tip %}
Para cartões de conteúdo, essa métrica é calculada de forma diferente, dependendo do que você selecionou para a [criação do cartão]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/):

- **No lançamento ou na etapa de entrada:** O número de cartões criados e disponíveis para serem vistos. Isso não conta se os usuários visualizaram o cartão.
- **Na primeira impressão:** O número de cartões exibidos aos usuários.
{% endalert %}

<span class="calculation-line">Cálculo: Contagem</span>

{% endapi %}

{% api %}

### Mensagens enviadas

{% apitags %}
Cartões de conteúdo, e-mail, mensagem no app, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, WhatsApp, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Messages Sent' %}  Essa métrica é fornecida pelo Braze. Observe que, ao lançar uma campanha programada, essa métrica incluirá todas as mensagens enviadas, independentemente de já terem sido enviadas devido ao limite de frequência.

{% alert tip %}
Para cartões de conteúdo, essa métrica é calculada de forma diferente, dependendo do que você selecionou para a [criação do cartão]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/):

- **No lançamento ou na etapa de entrada:** O número de cartões criados e disponíveis para serem vistos. Isso não conta se os usuários visualizaram o cartão.
- **Na primeira impressão:** O número de cartões exibidos aos usuários.
{% endalert %}

<span class="calculation-line">Cálculo: Contagem</span>

{% endapi %}

{% api %}

### Envios para operadora

{% apitags %}
SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Sends to Carrier' %} 

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Envios para operadora:</i> Contagem</li>
        <li><i>Taxa de envios para operadora:</i> (Envia para a operadora) / (Envia)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Soft bounce

{% apitags %}
E-mail
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Soft Bounce' %} Se um e-mail receber um soft bounce, geralmente tentaremos novamente dentro de 72 horas, mas o número de tentativas de nova tentativa varia de acordo com o destinatário.

Embora os soft bounces não sejam rastreados na análise de dados da campanha, é possível monitorar os soft bounces no [Message Activity Log]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/). Também é possível excluir esses usuários do seu envio ou analisar a quantidade de soft bounces dos últimos 30 dias com o [filtro de segmento Soft Bounced]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#soft-bounced). No registro de atividades de mensagens, você também pode ver o motivo dos soft bounces e entender possíveis discrepâncias entre os "envios" e as "entregas" de suas campanhas de e-mail.

{% endapi %}

{% api %}

### Spam

{% apitags %}
E-mail
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Spam' %}

{% alert note %}
As reclamações de spam são tratadas diretamente pelos prestadores de serviço de e-mail e, em seguida, transmitidas ao Braze por meio de um ciclo de feedback. A maioria dos loops de feedback relata apenas uma parte das reclamações reais, portanto, a métrica de _spam_ geralmente representa uma fração do total real. Somente os prestadores de serviço de e-mail podem visualizar o volume real de reclamações de spam, o que significa que _o spam_ deve ser visto como uma métrica indicativa, não exaustiva.
{% endalert %}

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Spam</i>: Contagem</li>
        <li><i>Spam %</i> ou <i>Spam Rate %</i>: (Marcado como Spam) / (Envia)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Rejeições de páginas de pesquisa

{% apitags %}
Mensagem no app
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Survey Page Dismissals' %}

{% endapi %}

{% api %}

### Envio de pesquisas

{% apitags %}
Mensagem no app
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Survey Submissions' %}

{% endapi %}

{% api %}

### Total de cliques

{% apitags %}
E-mail, cartões de conteúdo, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Clicks' %}

|Canal|Informações adicionais|
|-------|-------|
|LINE|Rastreamento após um limite mínimo de 20 mensagens por dia ter sido atingido. Os e-mails AMP incluem cliques registrados nas versões HTML e texto simples. Esse número pode ser artificialmente inflacionado por ferramentas anti-spam.|
|Banners|O número total (e a porcentagem) de usuários que clicaram na mensagem entregue, independentemente de o mesmo usuário clicar várias vezes.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><b>Envio de e-mail:</b> (Total de cliques) / (Entregas)</li>
        <li><b>Cartões de conteúdo:</b> (Total de cliques) / (Total de impressões)</li>
        <li><b>SMS:</b> (Abertura de cliques) / (Entregas)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Total de descartes

{% apitags %}
Cartões de conteúdo
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Dismissals' %} Se um usuário receber dois cartões diferentes da mesma campanha e descartar ambos, essa contagem aumentará em dois. A re-eligibilidade permite que você incremente o _Total de Descartes_ toda vez que um usuário receber um cartão; cada cartão é uma mensagem diferente.

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Total de Descartes:</i> Contagem</li>
        <li><i>Taxa Total de Descartes:</i> Total de Descartes / Total de Impressões</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Total de impressões

{% apitags %}
Mensagem no app, cartões de conteúdo
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Impressions' %} Esse número é a soma do número de eventos de impressão que o Braze recebe dos SDKs.

|Canal|Informações adicionais|
|-------|-----------------------|
|Cartões de conteúdo|A contagem total de impressões registradas para um determinado cartão de conteúdo. Isso pode ser incrementado várias vezes para o mesmo usuário.|
|Mensagem no app|Se houver vários dispositivos e a reelegibilidade estiver desativada, o usuário deverá ver a mensagem no app apenas uma vez. Mesmo que o usuário use vários dispositivos, ele só o verá no primeiro dispositivo que for direcionado. Isso pressupõe que o perfil tenha dispositivos consolidados e que um usuário tenha um ID de usuário no qual esteja registrado em todos os dispositivos. Se a reelegibilidade estiver ativada, será registrada uma impressão para cada vez que o usuário vir a mensagem no app.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

<span class="calculation-line">Cálculo: Contagem</span>

{% endapi %}

{% api %}

### Total de aberturas

{% apitags %}
E-mail, iOS Push, Android Push, Web Push, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Opens' %}

|Canal|Informações adicionais|
|-------|-----------------------|
|LINE|Rastreamento após um limite mínimo de 20 mensagens por dia ter sido atingido.|
|Envio de e-mails AMP|O total abre para as versões HTML e de texto simples.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><b><i>Total de aberturas</i> de e-mail:</b> Contagem</li>
        <li><b><i>Taxa total de abertura</i> de e-mail:</b> (Aberturas) / (Entregas)</li>
        <li><b>Web push <i>Total de aberturas</i>:</b> Contagem de <i>aberturas diretas</i> </li>
        <li><b><i>Taxa de abertura total do</i> web push:</b> (Total de aberturas) / (Entregas)</li>
        <li><b>iOS, Android e push do Kindle <i>Total de aberturas</i>:</b> (aberturas diretas) + (aberturas por influência)</li>
        <li><b>iOS, Android e Kindle push <i>Taxa total de abertura</i>:</b> (Total de aberturas) / (Entregas)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Total de receitas

{% apitags %}
Cartões de conteúdo, e-mail, mensagem no app, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Revenue' %} Essa métrica só está disponível nos relatórios de comparação de campanhas por meio do <a href='https://braze.com/docs/user_guide/data_and_analytics/reporting/report_builder/'>Report Builder</a>

{% endapi %}

{% api %}

### Cliques únicos projetados

{% apitags %}
Envio de e-mail, cartões de conteúdo, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Clicks' %}

Isso inclui cliques em links de cancelamento de inscrição fornecidos pela Braze.

|Canal|Informações adicionais|
|-------|-----------------------|
|E-mail|Rastreamento em um período de sete dias.|
|LINE|Rastreamento após um limite mínimo de 20 mensagens por dia ter sido atingido.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Cliques únicos</i>: Contagem</li>
        <li><b>Cartões de conteúdo</b> <i>% de cliques únicos</i> ou <i>taxa de cliques únicos</i>: (Cliques únicos) / (Impressões únicas)</li>
        <li><i>% de cliques únicos</i> de <b>e-mail</b> ou <i>taxa de cliques únicos</i>: (Cliques únicos) / (Entregas)</li>
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
Mensagem no app, cartões de conteúdo
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Impressions' %} 

|Canal|Informações adicionais|
|-------|-----------------------|
|Mensagem no app|As impressões exclusivas podem ser incrementadas novamente após 24 horas se a reelegibilidade estiver ativada e um usuário executar a ação-gatilho. Se a reelegibilidade estiver ativada, <i>Impressões únicas</i> = <i>Destinatários únicos</i>.|
|Cartões de conteúdo|A contagem não deve ser incrementada na segunda vez que um usuário visualizar um cartão.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

<span class="calculation-line">Cálculo: Contagem</span>

{% endapi %}

{% api %}

### Aberturas únicas projetadas

{% apitags %}
Envio de e-mail, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Opens' %}

|Canal|Informações adicionais|
|-------|-----------------------|
|E-mail|Rastreamento em um período de 7 dias.|
|LINE|Rastreamento após um limite mínimo de 20 mensagens por dia ter sido atingido.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Aberturas exclusivas</i>: Contagem</li>
        <li><i>Unique Opens % (% de aberturas únicas</i> ) ou <i>Unique Open Rate (taxa de abertura única)</i>: (Aberturas únicas) / (Entregas)</li>
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

Como um espectador pode ser um destinatário único todos os dias, você deve esperar que esse valor seja maior do que o de <i>impressões únicas</i>. Para os cartões de conteúdo, cada cartão só pode ser recebido uma vez, portanto, a visualização do mesmo cartão de conteúdo uma segunda vez, independentemente do dia, não incrementará essa contagem.<br><br>Esse número é recebido da Braze e se baseia no `user_id`. Os destinatários únicos são contados no nível da campanha ou etapa do canva, não no nível do <a href='https://braze.com/docs/api/identifier_types/#send-identifier'>identificador de envio</a>.

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
        <li><i>% de cancelamentos de inscrição %</i> ou <i>taxa de cancelamento de inscrição</i>: (Cancelamentos de inscrição) / (Entregas)</li>
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
Cartões de conteúdo, e-mail, mensagem no app, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Variation' %}

<span class="calculation-line">Cálculo: Contagem</span>

{% endapi %}