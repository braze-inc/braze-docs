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

### Cliques em AMP

{% apitags %}
E-mail
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='AMP Clicks' %}

{% endapi %}

{% api %}

### AMP abre

{% apitags %}
E-mail
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='AMP Opens' %}

{% endapi %}

{% api %}

### Público

{% apitags %}
Todos
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Audience' %}

<span class="calculation-line">Cálculo: (Número de destinatários na variante) / (destinatários únicos)</span>

{% endapi %}

{% api %}

### Saltos

{% apitags %}
E-mail, Web Push, iOS Push
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Bounces' %} Isso pode ocorrer porque não há um token de envio válido, o usuário cancelou a assinatura após o lançamento da campanha ou o endereço de e-mail está incorreto ou desativado.

|Canal|Informações adicionais|
|-------|-----------------------|
|E-mail|Uma rejeição de e-mail para os clientes que usam a SendGrid consiste em rejeições graves, spam (`spam_report_drops`) e e-mails enviados para endereços inválidos (`invalid_emails`).<br><br>Para e-mail, a *%* de *rejeição* ou a *taxa de rejeição* é a porcentagem de mensagens que foram enviadas sem sucesso ou designadas como "devolvidas" ou "não recebidas" dos serviços de envio usados ou não recebidas pelos usuários de e-mail pretendidos.|
|Empurrar|Esses usuários foram automaticamente descadastrados de todas as futuras notificações por push.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Saltos</i>: Contagem</li>
        <li><i>Bounce %</i> ou <i>Bounce Rate %</i>: (Bounces) / (Sends)</li>
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
Mensagem no aplicativo
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Body Clicks' %} Para obter mais detalhes, consulte os registros de alterações do SDK para [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/changelog/objc_changelog#3310) e [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/changelog#1100).

<span class="calculation-line">Cálculo: (Cliques no corpo) / (Impressões)</span>

{% endapi %}

{% api %}

### Botão 1 Cliques

{% apitags %}
Mensagem no aplicativo
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Button 1 Clicks' %} Os relatórios de _cliques no botão 1_ só funcionam quando você especifica o **identificador para relatórios** como "0" na mensagem in-app.

<span class="calculation-line">Cálculo: (Cliques no Botão 1) / (Impressões)</span>

{% endapi %}

{% api %}

### Botão 2 cliques

{% apitags %}
Mensagem no aplicativo
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Button 2 Clicks' %} Os relatórios para _cliques no botão 2_ só funcionam quando você especifica o **identificador para relatórios** como "1" na mensagem in-app.

<span class="calculation-line">Cálculo: (Botão 2 Cliques) / (Impressões)</span>

{% endapi %}

{% api %}

### Análise de campanhas

{% apitags %}
Sinalizadores de recursos
{% endapitags %}

O desempenho da mensagem em vários canais. As métricas mostradas dependem do canal de mensagens selecionado e se o [experimento do sinalizador de recursos]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/experiments/#campaign-analytics) é um teste multivariado.

{% endapi %}

{% api %}

### Opções enviadas

{% apitags %}
Mensagem no aplicativo
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Choices Submitted' %}

{% endapi %}

{% api %}

### Taxa de cliques para abrir

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
        <li><i>Entregas confirmadas</i>: Contagem</li>
        <li><i>Taxa de entrega confirmada</i>: (Entregas confirmadas) / (Envios)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Confiança

{% apitags %}
Cartões de conteúdo, e-mail, mensagem no aplicativo, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confidence' %}

{% endapi %}

{% api %}

### Botão da página de confirmação

{% apitags %}
Mensagem no aplicativo
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confirmation Page Button' %}

{% endapi %}

{% api %}

### Dispensas da página de confirmação

{% apitags %}
Mensagem no aplicativo
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confirmation Page Dismissals' %}

{% endapi %}

{% api %}

### Conversões (B, C, D)

{% apitags %}
Cartões de conteúdo, e-mail, mensagem no aplicativo, Web Push, iOS Push, Android Push, Webhook, SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Conversions (B, C, D)' %} Esse evento definido é determinado por você ao criar a campanha. 

|Canal|Informações adicionais|
|-------|-----------------------|
|E-mail, Push, Webhooks|As conversões são rastreadas após o envio inicial.|
|Cartões de conteúdo|As conversões são contadas quando o usuário visualiza um Content Card pela primeira vez.|
|Mensagens no aplicativo|Uma conversão é contada se o usuário tiver recebido e visualizado a campanha de mensagens in-app e, posteriormente, realizar o evento de conversão específico dentro da janela de conversão definida, independentemente de ter clicado ou não na mensagem.<br><br>As conversões são atribuídas à mensagem recebida mais recentemente. Se a reelegibilidade estiver ativada, a conversão será atribuída à última mensagem in-app recebida, desde que ela ocorra dentro da janela de conversão definida. No entanto, se a mensagem in-app já tiver sido atribuída a uma conversão, a nova conversão não poderá ser registrada para essa mensagem específica. Isso significa que cada entrega de mensagem in-app está associada a apenas uma conversão.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endapi %}

{% api %}

### Total de conversões

{% apitags %}
Mensagem no aplicativo
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Conversions' %}

Quando um usuário visualiza uma campanha de mensagem in-app apenas uma vez, apenas uma conversão é contada, mesmo que ele realize o evento de conversão várias vezes posteriormente. No entanto, se a reelegibilidade estiver ativada e o usuário visualizar a campanha de mensagem in-app várias vezes, *o Total de conversões* poderá aumentar uma vez para cada vez que o usuário registrar uma impressão para uma nova instância da campanha de mensagem in-app. 

Por exemplo, se um usuário aciona uma mensagem in-app duas vezes e converte após cada impressão de mensagem in-app (resultando em duas conversões), *o Total de conversões* aumentará em dois. No entanto, se houver apenas uma impressão de mensagem in-app seguida de dois eventos de conversão, apenas uma conversão será registrada e *o Total de conversões* aumentará em um.

{% endapi %}

{% api %}

### Fechar mensagem

{% apitags %}
Mensagem no aplicativo
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Close Message' %}

{% endapi %}

{% api %}

### Taxa de conversão

{% apitags %}
Cartões de conteúdo, e-mail, mensagem no aplicativo, Web Push, iOS Push, Android Push, Webhook, SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Conversion Rate' %}

|Canal|Informações adicionais|
|-------|-----------------------|
|Mensagens no aplicativo|A métrica do total de <i>impressões únicas</i> diárias é usada para calcular a <i>taxa de conversão</i> de mensagens in-app.<br><br>As impressões de mensagens in-app só podem ser contadas uma vez por dia. Por outro lado, o número de vezes que um usuário conclui uma ação desejada (uma "conversão") pode aumentar em um período de 24 horas. Embora as conversões possam ocorrer mais de uma vez por dia, as impressões não podem. Portanto, se um usuário concluir uma conversão várias vezes em um dia, a <i>taxa de conversão</i> poderá aumentar de acordo, mas as impressões serão contadas apenas uma vez.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><b>Mensagens no aplicativo</b>: (Conversões primárias) / (Impressões exclusivas)</li>
        <li><b>Outros canais</b>: (Conversões primárias) / (Destinatários exclusivos)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Janela de conversão

{% apitags %}
Todos
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
        <li><i>Entregas %</i>: (Envios - Devoluções) / (Envios)</li>
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

Entre em contato com o <a href="/docs/braze_support/">Suporte Braze</a> para obter ajuda para entender os motivos das falhas de entrega.

<span class="calculation-line">Cálculo: (Envia) - (Envia para a operadora)</span>

{% endapi %}

{% api %}

### Falhas na entrega

{% apitags %}
RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Delivery Failures RCS' %}

Entre em contato com o <a href="/docs/braze_support/">Suporte Braze</a> para obter ajuda para entender os motivos das falhas de entrega.

<span class="calculation-line">Cálculo: (Envia) - (Envia para a operadora)</span>

{% endapi %}

{% api %}

### Taxa de falha na entrega

{% apitags %}
SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Failed Delivery Rate' %}

Entre em contato com o <a href="/docs/braze_support/">Suporte Braze</a> para obter ajuda para entender os motivos das falhas de entrega.

<span class="calculation-line">Cálculo: (Falhas na entrega) / (Envios)</span>

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

### Pode ser enviado por e-mail

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

<span class="calculation-line">Cálculo<i>(taxa de falha</i>): (Falhas) / (Envios)</span>

{% endapi %}

{% api %}

### Desempenho do experimento do sinalizador de recursos

{% apitags %}
Sinalizadores de recursos
{% endapitags %}

Métricas de desempenho para a mensagem em um experimento de sinalizador de recursos. As métricas específicas mostradas variam de acordo com o canal de mensagens e se o experimento foi ou não um teste multivariado.

{% endapi %}

{% api %}

### Hard Bounce

{% apitags %}
E-mail
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Hard Bounce' %} 

Quando isso ocorre, o Braze marca o endereço de e-mail como inválido, mas não atualiza o [status da assinatura]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/) do usuário. Se um e-mail receber um hard bounce, interromperemos todas as solicitações futuras para esse endereço de e-mail.

{% endapi %}

{% api %}

### Ajuda

{% apitags %}
SMS/MMS, RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Help' %} Uma resposta do usuário é medida sempre que um usuário envia uma mensagem de entrada dentro de quatro horas após o recebimento da sua mensagem.

{% endapi %}

{% api %}

### Aberturas influenciadas

{% apitags %}
iOS Push, Android Push
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Influenced Opens' %}

<span class="calculation-line">Cálculo: (Aberturas influenciadas) / (Entregas)</span>

{% endapi %}

{% api %}

### Receita vitalícia

{% apitags %}
Cartões de conteúdo, e-mail, mensagem no aplicativo, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Lifetime Revenue' %}

{% endapi %}

{% api %}

### Valor vitalício por usuário

{% apitags %}
Cartões de conteúdo, e-mail, mensagem no aplicativo, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Lifetime Value Per User' %}

{% endapi %}

{% api %}

### Receita média diária

{% apitags %}
Cartões de conteúdo, e-mail, mensagem no aplicativo, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Average Daily Revenue' %}

{% endapi %}

{% api %}

### Compras diárias

{% apitags %}
Cartões de conteúdo, e-mail, mensagem no aplicativo, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Daily Purchases' %}

{% endapi %}

{% api %}

### Receita diária por usuário

{% apitags %}
Cartões de conteúdo, e-mail, mensagem no aplicativo, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Daily Revenue Per User' %}

{% endapi %}

{% api %}

### A máquina abre

{% apitags %}
E-mail
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Machine Opens' %} Essa métrica é rastreada a partir de 11 de novembro de 2021 para o SendGrid e de 2 de dezembro de 2021 para o SparkPost. Para o Amazon SES, as análises serão exibidas como _Opens_. No entanto, haverá suporte à filtragem de bots para cliques.

{% endapi %}

{% api %}

### Abre

{% apitags %}
Web Push, iOS Push, Android Push
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Opens' %}

{% endapi %}

{% api %}

### Opt-Out

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

{% multi_lang_include analytics/metrics.md metric='Other Opens' %} Observe que um usuário também pode abrir um e-mail (como as contagens de abertura em relação a Outras aberturas) antes que uma contagem de aberturas de máquina seja registrada. Se um usuário abrir um e-mail uma vez (ou mais) após um evento de abertura de máquina de uma caixa de entrada que não seja do Apple Mail, a quantidade de vezes que o usuário abrir o e-mail será calculada para Outras aberturas e apenas uma vez para Aberturas exclusivas.

{% endapi %}

{% api %}

### Repetição pendente

{% apitags %}
E-mail
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Pending Retry' %}

{% endapi %}

{% api %}

### Conversões primárias (A) ou Evento de conversão primária

{% apitags %}
Cartões de conteúdo, e-mail, mensagem no aplicativo, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Primary Conversions (A) or Primary Conversion Event' %} 

|Canal|Informações adicionais|
|-------------|----------------------|
|E-mail, Push, Webhooks|Após o envio inicial.|
|Cartões de conteúdo, mensagens no aplicativo|Quando o usuário visualiza o Content Card ou a mensagem pela primeira vez.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Conversões primárias (A) ou Evento de conversão primária</i>: Contagem</li>
        <li><i>Conversões primárias (A) %</i> ou <i>Taxa de eventos de conversão primária</i>: (Conversões primárias) / (Destinatários exclusivos)</li>
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
E-mail, Cartões de conteúdo, Mensagem no aplicativo, Web Push, iOS Push, Android Push, SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Received' %} 

|Canal|Informações adicionais|
|-------|-------|
|Cartões de conteúdo|Recebido quando os usuários visualizam o cartão no aplicativo.|
|Empurrar|Recebido quando as mensagens são enviadas do servidor do Braze para o provedor de push.|
|E-mail|Recebido quando as mensagens são enviadas do servidor do Braze para o provedor de serviços de e-mail.|
|SMS/MMS|"Entregue" depois que o provedor de SMS receber a confirmação da operadora upstream e do dispositivo de destino.|
|Mensagem no aplicativo|Recebido no momento da exibição com base na ação de acionamento definida.|
|WhatsApp|Recebido no momento da exibição com base na ação de acionamento definida.|
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
        <li><i>Rejeições</i>: Contagem</li>
        <li><i>Taxa de rejeição</i>: (Rejeições) / (Envios)</li>
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

### Enviado

{% apitags %}
SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Sent' %}

<span class="calculation-line">Cálculo: Contagem</span>

{% endapi %}

{% api %}

### Envia

{% apitags %}
Cartões de conteúdo, e-mail, mensagem no aplicativo, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, RCS, WhatsApp, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Sends' %} Essa métrica é fornecida pela Braze. Observe que, ao lançar uma campanha agendada, essa métrica incluirá todas as mensagens enviadas, independentemente de já terem sido enviadas devido à limitação de taxa.

{% alert tip %}
Para os cartões de conteúdo, essa métrica é calculada de forma diferente, dependendo do que você selecionou para a [criação do cartão]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/):

- **No lançamento ou na entrada da etapa:** O número de cartões criados e disponíveis para serem vistos. Isso não conta se os usuários visualizaram o cartão.
- **Na primeira impressão:** O número de cartões exibidos aos usuários.
{% endalert %}

<span class="calculation-line">Cálculo: Contagem</span>

{% endapi %}

{% api %}

### Mensagens enviadas

{% apitags %}
Cartões de conteúdo, e-mail, mensagem no aplicativo, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, WhatsApp, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Messages Sent' %}  Essa métrica é fornecida pela Braze. Observe que, ao lançar uma campanha agendada, essa métrica incluirá todas as mensagens enviadas, independentemente de já terem sido enviadas devido à limitação de taxa.

{% alert tip %}
Para os cartões de conteúdo, essa métrica é calculada de forma diferente, dependendo do que você selecionou para a [criação do cartão]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/):

- **No lançamento ou na entrada da etapa:** O número de cartões criados e disponíveis para serem vistos. Isso não conta se os usuários visualizaram o cartão.
- **Na primeira impressão:** O número de cartões exibidos aos usuários.
{% endalert %}

<span class="calculation-line">Cálculo: Contagem</span>

{% endapi %}

{% api %}

### Envia para a operadora

{% apitags %}
SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Sends to Carrier' %} 

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Envia para a operadora</i>: Contagem</li>
        <li><i>Envia para a taxa da operadora</i>: (Envia para a operadora) / (Envia)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Salto suave

{% apitags %}
E-mail
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Soft Bounce' %} Observe que _os Soft Bounces_ são diferentes dos _Deferrals_. Se nenhum e-mail for entregue com êxito durante esse período de nova tentativa, o Braze enviará um evento de soft bounce por tentativa de campanha enviada. Antes de 25 de fevereiro de 2025, essas novas tentativas eram contadas como vários soft bounces para um envio de campanha.

Embora os soft bounces não sejam rastreados na análise da campanha, você pode monitorar os soft bounces no [Message Activity Log]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/). Você também pode excluir esses usuários do seu envio ou analisar a quantidade de soft bounces dos últimos 30 dias com o [filtro de segmento Soft Bounced]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#soft-bounced). No Message Activity Log (Registro de atividade de mensagens), você também pode ver o motivo dos soft bounces e entender possíveis discrepâncias entre os "envios" e as "entregas" de suas campanhas de e-mail.

{% endapi %}

{% api %}

### Spam

{% apitags %}
E-mail
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Spam' %}

{% alert note %}
As reclamações de spam são tratadas diretamente pelos provedores de serviços de e-mail e, em seguida, transmitidas à Braze por meio de um ciclo de feedback. A maioria dos loops de feedback informa apenas uma parte das reclamações reais, portanto, a métrica de _spam_ geralmente representa uma fração do total real. Somente os provedores de serviços de e-mail podem visualizar o volume real de reclamações de spam, o que significa que _o spam_ deve ser visto como uma métrica indicativa, não exaustiva.
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
Mensagem no aplicativo
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Survey Page Dismissals' %}

{% endapi %}

{% api %}

### Envio de pesquisas

{% apitags %}
Mensagem no aplicativo
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
|LINHA|Rastreado após um limite mínimo de 20 mensagens por dia ter sido atingido. Os e-mails AMP incluem cliques registrados nas versões HTML e de texto simples. Esse número pode ser artificialmente inflado por ferramentas anti-spam.|
|Banners|O número total (e a porcentagem) de usuários que clicaram na mensagem entregue, independentemente de o mesmo usuário ter clicado várias vezes.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><b>E-mail:</b> (Total de cliques) / (Entregas)</li>
        <li><b>Cartões de conteúdo:</b> (Total de cliques) / (Total de impressões)</li>
        <li><b>SMS:</b> (Abertura de cliques) / (Entregas)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Total de demissões

{% apitags %}
Cartões de conteúdo
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Dismissals' %} Se um usuário receber dois cartões diferentes da mesma campanha e descartar ambos, essa contagem aumentará em dois. A reelegibilidade permite incrementar o _Total Dismissals_ uma vez a cada vez que um usuário recebe um cartão; cada cartão é uma mensagem diferente.

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Total de demissões:</i> Contagem</li>
        <li><i>Taxa total de demissões:</i> Total de rejeições / Total de impressões</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Total de impressões

{% apitags %}
Mensagem no aplicativo, cartões de conteúdo
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Impressions' %} Esse número é a soma do número de eventos de impressão que o Braze recebe dos SDKs.

|Canal|Informações adicionais|
|-------|-----------------------|
|Cartões de conteúdo|A contagem total de impressões registradas para um determinado Content Card. Isso pode ser incrementado várias vezes para o mesmo usuário.|
|Mensagens no aplicativo|Se houver vários dispositivos e a reelegibilidade estiver desativada, o usuário deverá ver a mensagem no aplicativo apenas uma vez. Mesmo que o usuário use vários dispositivos, ele só o verá no primeiro dispositivo que for direcionado. Isso pressupõe que o perfil tenha dispositivos consolidados e que um usuário tenha um ID de usuário no qual esteja conectado em todos os dispositivos. Se a reelegibilidade estiver ativada, uma impressão será registrada para cada vez que o usuário vir a mensagem in-app.|
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
|LINHA|Rastreado após um limite mínimo de 20 mensagens por dia ter sido atingido.|
|E-mails AMP|O total abre para as versões HTML e de texto simples.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><b><i>Total de aberturas</i> de e-mail:</b> Contagem</li>
        <li><b><i>Taxa de abertura total</i> do e-mail:</b> (Aberturas) / (Entregas)</li>
        <li><b>Web push <i>Total de aberturas</i>:</b> Contagem de <i>aberturas diretas</i> </li>
        <li><b>Web push <i>Total Open Rate</i>:</b> (Total de aberturas) / (Entregas)</li>
        <li><b>iOS, Android e Kindle push <i>Total de aberturas</i>:</b> (Aberturas diretas) + (Aberturas influenciadas)</li>
        <li><b>iOS, Android e Kindle push <i>Total Open Rate</i>:</b> (Total de aberturas) / (Entregas)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Receita total

{% apitags %}
Cartões de conteúdo, e-mail, mensagem no aplicativo, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Revenue' %} Essa métrica está disponível apenas nos relatórios de comparação de campanhas por meio do <a href='https://braze.com/docs/user_guide/data_and_analytics/reporting/report_builder/'>Report Builder</a>

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
|E-mail|Rastreado em um período de sete dias.|
|LINHA|Rastreado após um limite mínimo de 20 mensagens por dia ter sido atingido.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Cliques únicos</i>: Contagem</li>
        <li><b>Cartões de conteúdo</b> <i>% de cliques únicos</i> ou <i>taxa de cliques únicos</i>: (Cliques únicos) / (Impressões únicas)</li>
        <li><b>Email</b> <i>Unique Clicks %</i> ou <i>Unique Clicks Rate</i>: (Cliques únicos) / (Entregas)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Demissões exclusivas

{% apitags %}
Cartões de conteúdo
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Dismissals' %}

<span class="calculation-line">Cálculo: (Demissões únicas) / (Impressões únicas)</span>

{% endapi %}

{% api %}

### Impressões exclusivas

{% apitags %}
Mensagem no aplicativo, cartões de conteúdo
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Impressions' %} 

|Canal|Informações adicionais|
|-------|-----------------------|
|Mensagens no aplicativo|As impressões exclusivas podem ser incrementadas novamente após 24 horas se a reelegibilidade estiver ativada e um usuário executar a ação de acionamento. Se a reelegibilidade estiver ativada, <i>Impressões únicas</i> = <i>Destinatários únicos</i>.|
|Cartões de conteúdo|A contagem não deve ser incrementada na segunda vez que um usuário visualizar um cartão.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

<span class="calculation-line">Cálculo: Contagem</span>

{% endapi %}

{% api %}

### Aberturas exclusivas

{% apitags %}
E-mail, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Opens' %}

|Canal|Informações adicionais|
|-------|-----------------------|
|E-mail|Rastreado em um período de 7 dias.|
|LINHA|Rastreado após um limite mínimo de 20 mensagens por dia ter sido atingido.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Aberturas exclusivas</i>: Contagem</li>
        <li><i>Unique Opens %</i> ou <i>Unique Open Rate</i>: (Aberturas únicas) / (Entregas)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Destinatários exclusivos

{% apitags %}
Todos
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Recipients' %}

Como um visualizador pode ser um destinatário único todos os dias, você deve esperar que esse valor seja maior do que o de <i>Impressões únicas</i>. Para Cartões de Conteúdo, cada Cartão de Conteúdo só pode ser recebido uma vez, portanto, visualizar o mesmo Cartão de Conteúdo uma segunda vez, independentemente do dia, não aumentará essa contagem.<br><br>Esse número é recebido da Braze e se baseia no site `user_id`. Os destinatários exclusivos são contados no nível da campanha ou da etapa do Canvas, e não no nível do <a href='https://braze.com/docs/api/identifier_types/#send-identifier'>identificador de envio</a>.

<span class="calculation-line">Cálculo: Contagem</span>

{% endapi %}

{% api %}

### Cancelamento de assinatura ou cancelamento de assinatura

{% apitags %}
E-mail
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unsubscribers or Unsub' %}

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Cancelamento</i><i>de</i> assinaturas ou <i>Unsub</i>: Contagem</li>
        <li><i>% de cancelamentos de assinaturas</i> ou <i>taxa de cancelamento de assinaturas</i>: (Cancelamentos) / (Entregas)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Cancelamento de inscrição

{% apitags %}
E-mail
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unsubscribes' %}

<span class="calculation-line">Cálculo: (Cancelamentos) / (Entregas)</span>

{% endapi %}

{% api %}

### Variação

{% apitags %}
Cartões de conteúdo, e-mail, mensagem no aplicativo, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Variation' %}

<span class="calculation-line">Cálculo: Contagem</span>

{% endapi %}