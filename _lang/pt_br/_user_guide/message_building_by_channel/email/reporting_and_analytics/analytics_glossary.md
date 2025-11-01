---
nav_title: Glossário de análise de e-mail
article_title: Glossário de análise de e-mail
layout: email_report_metrics
page_order: 0
excerpt_separator: ""
page_type: glossary
description: "Este glossário inclui os termos que você encontrará na seção de análise da sua campanha de e-mail ou do Canvas, após o lançamento. Este glossário não inclui as métricas do Currents."
channel: 
  - email
---

<style>
  .calculation-line {
    color: #76848C;
    font-size: 14px;
  }
</style>

{% api %}

### Variação

{% apitags %}
Contagem
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Variation' %}

<span class="calculation-line">Cálculo: Contagem</span>

{% endapi %}

{% api %}

### Pode ser enviado por e-mail

{% apitags %}
Contagem
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Emailable' %}

<span class="calculation-line">Cálculo: Contagem</span>

{% endapi %}

{% api %}

### Público %

{% apitags %}
Porcentagem
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Audience' %}

<span class="calculation-line">Cálculo: (Número de destinatários na variante) / (destinatários únicos)</span>

{% endapi %}

{% api %}

### Destinatários exclusivos

{% apitags %}
Contagem
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Recipients' %} Esse número é recebido do Braze.

<span class="calculation-line">Cálculo: Contagem</span>

{% endapi %}

{% api %}

### Envia

{% apitags %}
Contagem
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Sends' %}  Essa métrica é fornecida pela Braze.

<span class="calculation-line">Cálculo: Contagem</span>

{% endapi %}

{% api %}

### Mensagens enviadas

{% apitags %}
Contagem
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Messages Sent' %}  Essa métrica é fornecida pela Braze.

<span class="calculation-line">Cálculo: Contagem</span>

{% endapi %}

{% api %}

### Entregas

{% apitags %}
Contagem
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Deliveries' %} Para e-mails, *Entregas* é o número total de mensagens (Envios) enviadas e recebidas com sucesso por partes que podem enviar e-mails.

<span class="calculation-line">Cálculo: (Sends) - (Bounces) </span>

{% endapi %}

{% api %}

### Entregas %

{% apitags %}
Porcentagem
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Deliveries %' %}

<span class="calculation-line">Cálculo: (Envios - Devoluções) / (Envios) </span>

{% endapi %}

{% api %}

### Saltos

{% apitags %}
Contagem, porcentagem
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Bounces' %} 

Para e-mail, a *%* de *rejeição* ou a *taxa de rejeição* é a porcentagem de mensagens que foram enviadas sem sucesso ou designadas como "devolvidas" ou "não recebidas" dos serviços de envio usados ou não recebidas pelos usuários de e-mail pretendidos.

Uma rejeição de e-mail para os clientes que usam a SendGrid consiste em rejeições graves, spam (`spam_report_drops`) e e-mails enviados para endereços inválidos (`invalid_emails`).

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><b><i>Saltos</i>:</b> Contagem</li>
        <li><b><i>Bounce %</i> ou <i>Bounce Rate %</i>:</b> (Bounces) / (Sends)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Hard Bounce

{% apitags %}
Contagem
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Hard Bounce' %} 

<span class="calculation-line">Cálculo: Contagem </span>

{% endapi %}

{% api %}

### Salto suave

{% apitags %}
Contagem
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Soft Bounce' %} Se um e-mail receber um soft bounce, normalmente tentaremos novamente dentro de 72 horas, mas o número de tentativas de nova tentativa varia de acordo com o destinatário. 

Embora os soft bounces não sejam rastreados na análise da sua campanha, você pode monitorar os soft bounces no [Message Activity Log]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) ou excluir esses usuários do seu envio com o [filtro de segmento Soft Bounced]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#soft-bounced). No Message Activity Log (Registro de atividade de mensagens), você também pode ver o motivo dos soft bounces e entender possíveis discrepâncias entre os "envios" e as "entregas" de suas campanhas de e-mail.

<span class="calculation-line">Cálculo: Contagem </span>

{% endapi %}

{% api %}
  
### Spam

{% apitags %}
Contagem, porcentagem
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Spam' %}

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><b><i>Spam</i>:</b> Contagem</li>
        <li><b><i>Spam %</i> ou <i>Spam Rate %</i>:</b> (Marcado como Spam) / (Envia)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}
  
### Aberturas exclusivas

{% apitags %}
Contagem, porcentagem
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Opens' %} Para e-mail, isso é rastreado em um período de 7 dias.

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><b><i>Aberturas exclusivas</i>:</b> Contagem</li>
        <li><b><i>Unique Opens %</i> ou <i>Unique Open Rate</i>:</b> (Aberturas únicas) / (Entregas)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Cliques únicos

{% apitags %}
Contagem, porcentagem
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Clicks' %} Isso é rastreado em um período de sete dias para e-mail e medido por <a href='/docs/help/help_articles/data/dispatch_id/'>dispatch_id</a>. Isso inclui cliques em links de cancelamento de inscrição fornecidos pela Braze.

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><b><i>Cliques únicos</i>:</b> Contagem</li>
        <li><b><i>% de cliques únicos</i> ou <i>taxa de cliques</i>:</b> (Cliques únicos) / (Entregas)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}
  
### Cancelamento de assinatura ou cancelamento de assinatura

{% apitags %}
Contagem, porcentagem
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unsubscribers or Unsub' %}

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><b><i>Unsubscribers</i> ou <i>Unsub</i>:</b> Contagem</li>
        <li><b><i>% de cancelamentos de assinaturas</i> ou <i>taxa de cancelamento de assinaturas</i>:</b> (Cancelamentos) / (Entregas)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Receita

{% apitags %}
Contagem
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Revenue' %}

<span class="calculation-line">Cálculo: Contagem </span>

{% endapi %}

{% api %}

### Conversões primárias (A) ou Evento de conversão primária

{% apitags %}
Contagem, porcentagem
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Primary Conversions (A) or Primary Conversion Event' %} Para e-mail, push e webhooks, começamos a rastrear as conversões após o envio inicial.

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><b><i>Conversões primárias (A)</i> ou <i>Evento de conversão primária</i>:</b> Contagem</li>
        <li><b><i>Conversões primárias (A) %</i> ou <i>Taxa de eventos de conversão primária</i>:</b> (Conversões primárias) / (Destinatários exclusivos)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Confiança

{% apitags %}
Contagem
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confidence' %}

{% endapi %}

{% api %}

### A máquina abre
  
{% multi_lang_include analytics/metrics.md metric='Machine Opens' %} Essa métrica é rastreada a partir de 11 de novembro de 2021 para o SendGrid e de 2 de dezembro de 2021 para o SparkPost.

<span class="calculation-line">Cálculo: Contagem </span>

{% endapi %}

{% api %}

### Outras aberturas

{% apitags %}
Contagem
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Other Opens' %} Observe que um usuário também pode abrir um e-mail (como as contagens de abertura em relação a <i>Outras aberturas</i>) antes que uma contagem de <i>aberturas de máquina</i> seja registrada. Se um usuário abrir um e-mail uma vez (ou mais) após um evento de abertura de máquina de uma caixa de entrada que não seja do Apple Mail, a quantidade de vezes que o usuário abrir o e-mail será calculada para <i>Outras aberturas</i> e apenas uma vez para <i>Aberturas exclusivas</i>.

<span class="calculation-line">Cálculo: Contagem </span>

{% endapi %}

{% api %}

### Taxa de cliques para abrir

{% apitags %}
Porcentagem
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Click-to-Open Rate' %}

<span class="calculation-line">Cálculo: (Cliques únicos) / (Aberturas únicas) (para e-mail)</span>

{% endapi %}