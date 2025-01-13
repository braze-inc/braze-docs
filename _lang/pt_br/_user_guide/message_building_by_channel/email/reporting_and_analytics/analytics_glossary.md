---
nav_title: Glossário de análise de dados de e-mail
article_title: Glossário de análise de dados de e-mail
layout: email_report_metrics
page_order: 0
excerpt_separator: ""
page_type: glossary
description: "Este glossário inclui os termos que serão encontrados na seção de análise de dados da sua campanha de e-mail ou do Canva, após o lançamento. Este glossário não inclui as métricas do Currents."
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

{% multi_lang_include metrics.md metric='Variation' %}

<span class="calculation-line">Cálculo: Contagem</span>

{% endapi %}

{% api %}

### Envio de e-mail

{% apitags %}
Contagem
{% endapitags %}

{% multi_lang_include metrics.md metric='Emailable' %}

<span class="calculation-line">Cálculo: Contagem</span>

{% endapi %}

{% api %}

### % de público

{% apitags %}
Porcentagem
{% endapitags %}

{% multi_lang_include metrics.md metric='Audience' %}

<span class="calculation-line">Cálculo: (Número de destinatários na variante) / (destinatários únicos)</span>

{% endapi %}

{% api %}

### Destinatários únicos

{% apitags %}
Contagem
{% endapitags %}

{% multi_lang_include metrics.md metric='Unique Recipients' %} Esse número é recebido do Braze.

<span class="calculation-line">Cálculo: Contagem</span>

{% endapi %}

{% api %}

### Envios

{% apitags %}
Contagem
{% endapitags %}

{% multi_lang_include metrics.md metric='Sends' %} Essa métrica é fornecida pelo Braze.

<span class="calculation-line">Cálculo: Contagem</span>

{% endapi %}

{% api %}

### Mensagens enviadas

{% apitags %}
Contagem
{% endapitags %}

{% multi_lang_include metrics.md metric='Messages Sent' %} Essa métrica é fornecida pelo Braze.

<span class="calculation-line">Cálculo: Contagem</span>

{% endapi %}

{% api %}

### Entregas

{% apitags %}
Contagem
{% endapitags %}

{% multi_lang_include metrics.md metric='Deliveries' %} Para e-mails, *Deliveries* é o número total de mensagens (Sends) enviadas e recebidas com sucesso por partes que podem enviar e-mails.

<span class="calculation-line">Cálculo: (Sends) - (Bounces) </span>

{% endapi %}

{% api %}

### Entregas %

{% apitags %}
Porcentagem
{% endapitags %}

{% multi_lang_include metrics.md metric='Deliveries %' %}

<span class="calculation-line">Cálculo: (Envios - Bounces) / (Envios) </span>

{% endapi %}

{% api %}

### Bounces

{% apitags %}
Contagem, porcentagem
{% endapitags %}

{% multi_lang_include metrics.md metric='Bounces' %} 

Para e-mail, a % de *bounce* ou a *taxa de bounce* é a porcentagem de mensagens que foram enviadas sem sucesso ou designadas como "devolvidas" ou "não recebidas" dos serviços de envio usados ou não recebidas pelos usuários de e-mail pretendidos.

Um envio de e-mail para clientes que usam o SendGrid consiste em hard bounce, spam (`spam_report_drops`) e e-mails enviados para endereços inválidos (`invalid_emails`).

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><b><i>Bounces</i>:</b> Contagem</li>
        <li><b><i>Bounce %</i> ou <i>Bounce Rate %</i>:</b> (Bounces) / (Sends)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Hard bounce

{% apitags %}
Contagem
{% endapitags %}

{% multi_lang_include metrics.md metric='Hard Bounce' %} 

<span class="calculation-line">Cálculo: Contagem </span>

{% endapi %}

{% api %}

### Soft bounce

{% apitags %}
Contagem
{% endapitags %}

{% multi_lang_include metrics.md metric='Soft Bounce' %} Se um e-mail receber um soft bounce, normalmente tentaremos novamente dentro de 72 horas, mas o número de tentativas de nova tentativa varia de receptor para receptor.

<span class="calculation-line">Cálculo: Contagem </span>

{% endapi %}

{% api %}
  
### Spam

{% apitags %}
Contagem, porcentagem
{% endapitags %}

{% multi_lang_include metrics.md metric='Spam' %}

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
  
### Aberturas únicas projetadas

{% apitags %}
Contagem, porcentagem
{% endapitags %}

{% multi_lang_include metrics.md metric='Unique Opens' %} Para envio de e-mail, esse rastreamento é feito em um período de 7 dias.

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><b><i>Aberturas exclusivas</i>:</b> Contagem</li>
        <li><b><i>Unique Opens % (% de aberturas únicas)</i> ou <i>Unique Open Rate (taxa de abertura única)</i>:</b> (Aberturas únicas) / (Entregas)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Cliques únicos projetados

{% apitags %}
Contagem, porcentagem
{% endapitags %}

{% multi_lang_include metrics.md metric='Unique Clicks' %} Isso é rastreado em um período de sete dias para envio de e-mail e medido por <a href='/docs/help/help_articles/data/dispatch_id/'>dispatch_id</a>. Isso inclui cliques em links de cancelamento de inscrição fornecidos pela Braze.

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
  
### Cancelamento de inscrição

{% apitags %}
Contagem, porcentagem
{% endapitags %}

{% multi_lang_include metrics.md metric='Unsubscribers or Unsub' %}

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><b><i>Cancelamento de inscrição</i> ou <i>Unsub</i>:</b> Contagem</li>
        <li><b><i>% de cancelamentos de inscrição</i> ou <i>taxa de cancelamento de inscrição</i>:</b> (Cancelamentos de inscrição) / (Entregas)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Receita

{% apitags %}
Contagem
{% endapitags %}

{% multi_lang_include metrics.md metric='Revenue' %}

<span class="calculation-line">Cálculo: Contagem </span>

{% endapi %}

{% api %}

### Conversões primárias (A) ou evento de conversão primária

{% apitags %}
Contagem, porcentagem
{% endapitags %}

{% multi_lang_include metrics.md metric='Primary Conversions (A) or Primary Conversion Event' %} Para e-mail, push e webhooks, começamos a rastrear as conversões após o envio inicial.

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><b><i>Conversões primárias (A)</i> ou <i>Evento de conversão primária</i>:</b> Contagem</li>
        <li><b><i>Conversões primárias (A) %</i> ou <i>Taxa de evento de conversão primária</i>:</b> (Conversões primárias) / (Destinatários únicos)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Confiança

{% apitags %}
Contagem
{% endapitags %}

{% multi_lang_include metrics.md metric='Confidence' %}

{% endapi %}

{% api %}

### Aberturas por máquina
  
{% multi_lang_include metrics.md metric='Machine Opens' %} Essa métrica será rastreada a partir de 11 de novembro de 2021 para a SendGrid e de 2 de dezembro de 2021 para a SparkPost.

<span class="calculation-line">Cálculo: Contagem </span>

{% endapi %}

{% api %}

### Outras aberturas

{% apitags %}
Contagem
{% endapitags %}

{% multi_lang_include metrics.md metric='Other Opens' %} Observe que um usuário também pode abrir um e-mail (como as contagens de abertura para <i>Outras aberturas</i>) antes que uma contagem de <i>aberturas de máquina</i> seja registrada. Se um usuário abrir um e-mail uma vez (ou mais) após um evento de abertura de máquina de uma caixa de entrada que não seja do Apple Mail, a quantidade de vezes que o usuário abrir o e-mail será calculada para <i>Outras aberturas</i> e apenas uma vez para <i>Aberturas exclusivas</i>.

<span class="calculation-line">Cálculo: Contagem </span>

{% endapi %}

{% api %}

### Taxa de cliques por abertura

{% apitags %}
Porcentagem
{% endapitags %}

{% multi_lang_include metrics.md metric='Click-to-Open Rate' %}

<span class="calculation-line">Cálculo: (Cliques únicos) / (Aberturas únicas) (para e-mail)</span>

{% endapi %}