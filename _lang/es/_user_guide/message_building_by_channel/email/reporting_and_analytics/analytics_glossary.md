---
nav_title: Glosario de análisis de correo electrónico
article_title: Glosario de análisis de correo electrónico
layout: email_report_metrics
page_order: 0
excerpt_separator: ""
page_type: glossary
description: "Este glosario incluye los términos que encontrarás en la sección de análisis de tu campaña de correo electrónico o Canvas, tras el lanzamiento. Este glosario no incluye las métricas de Currents."
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

### Variación

{% apitags %}
Cuenta
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Variation' %}

<span class="calculation-line">Cálculo: Cuenta</span>

{% endapi %}

{% api %}

### Envío por correo electrónico

{% apitags %}
Cuenta
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Emailable' %}

<span class="calculation-line">Cálculo: Cuenta</span>

{% endapi %}

{% api %}

### Audiencia

{% apitags %}
Porcentaje
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Audience' %}

<span class="calculation-line">Cálculo: (Número de destinatarios en la variante) / (Destinatarios únicos)</span>

{% endapi %}

{% api %}

### Destinatarios únicos

{% apitags %}
Cuenta
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Recipients' %} Este número se recibe de Braze.

<span class="calculation-line">Cálculo: Cuenta</span>

{% endapi %}

{% api %}

### Envía

{% apitags %}
Cuenta
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Sends' %}  Esta métrica la proporciona Braze.

<span class="calculation-line">Cálculo: Cuenta</span>

{% endapi %}

{% api %}

### Mensajes enviados

{% apitags %}
Cuenta
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Messages Sent' %}  Esta métrica la proporciona Braze.

<span class="calculation-line">Cálculo: Cuenta</span>

{% endapi %}

{% api %}

### Entregas

{% apitags %}
Cuenta
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Deliveries' %} En el caso de los correos electrónicos, las *entregas* son el número total de mensajes (envíos) enviados y recibidos correctamente por las partes que pueden enviar correos electrónicos.

<span class="calculation-line">Cálculo: (Envía) - (Rebota) </span>

{% endapi %}

{% api %}

### % de entregas

{% apitags %}
Porcentaje
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Deliveries %' %}

<span class="calculation-line">Cálculo: (Envíos - Rebotes) / (Envíos) </span>

{% endapi %}

{% api %}

### Rebotes

{% apitags %}
Recuento, Porcentaje
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Bounces' %} 

Para el correo electrónico, *el % de rebote* o *tasa de rebote* es el porcentaje de mensajes que se enviaron sin éxito o se designaron como "devueltos" o "no recibidos" de los servicios de envío utilizados o no recibidos por los usuarios destinatarios del correo electrónico.

Un rebote de correo electrónico para clientes que utilizan SendGrid consiste en rebotes duros, correo no deseado (`spam_report_drops`) y correos enviados a direcciones no válidas (`invalid_emails`).

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><b><i>Rebota</i>:</b> Cuenta</li>
        <li><b><i>% de rebote</i> o <i>tasa de rebote %</i>:</b> (Rebota) / (Envía)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Rebote duro

{% apitags %}
Cuenta
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Hard Bounce' %} 

<span class="calculation-line">Cálculo: Cuenta </span>

{% endapi %}

{% api %}

### Rebote blando

{% apitags %}
Cuenta
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Soft Bounce' %} Si un correo electrónico recibe un rebote blando, normalmente lo reintentaremos en un plazo de 72 horas, pero el número de intentos de reintento varía de un receptor a otro. 

Aunque los rebotes blandos no se siguen en los análisis de tu campaña, puedes controlar los rebotes blandos en el [Registro de actividad de mensajes]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) o excluir a estos usuarios de tus envíos con el [filtro de segmento de rebotes blandos]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#soft-bounced). En el Registro de actividad de mensajes, también puedes ver el motivo de los rebotes blandos y comprender las posibles discrepancias entre los "envíos" y las "entregas" de tus campañas de correo electrónico.

<span class="calculation-line">Cálculo: Cuenta </span>

{% endapi %}

{% api %}
  
### Correo no deseado

{% apitags %}
Recuento, Porcentaje
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Spam' %}

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><b><i>Correo no deseado</i>:</b> Cuenta</li>
        <li><b><i>% de correo no deseado</i> o <i>% de tasa de correo no deseado</i>:</b> (Marcado como correo no deseado) / (Envía)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}
  
### Unique Opens

{% apitags %}
Recuento, Porcentaje
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Opens' %} En el caso del correo electrónico, el seguimiento se realiza durante un periodo de 7 días.

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><b><i>Unique Opens</i>:</b> Cuenta</li>
        <li><b><i>Unique Opens %</i> o <i>tarifa abierta única</i>:</b> (Unique Opens) / (Entregas)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Clics únicos

{% apitags %}
Recuento, Porcentaje
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Clicks' %} Esto se sigue durante un periodo de siete días para el correo electrónico y se mide mediante <a href='/docs/help/help_articles/data/dispatch_id/'>dispatch_id</a>. Esto incluye los clics en los enlaces para cancelar suscripción proporcionados por Braze.

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><b><i>Clics únicos</i>:</b> Cuenta</li>
        <li><b><i>Porcentaje de clics únicos</i> o <i>tasa de clics</i>:</b> (Clics únicos) / (Entregas)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}
  
### Cancelar suscripción o darse de baja

{% apitags %}
Recuento, Porcentaje
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unsubscribers or Unsub' %}

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><b><i>Cancelar suscripción</i> o <i>darse de baja</i>:</b> Cuenta</li>
        <li><b><i>Suscriptores %</i> o <i>tasa de cancelación de suscripciones</i>:</b> (Cancelaciones de suscripción) / (Entregas)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Ingresos

{% apitags %}
Cuenta
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Revenue' %}

<span class="calculation-line">Cálculo: Cuenta </span>

{% endapi %}

{% api %}

### Conversiones primarias (A) o evento de conversión primaria

{% apitags %}
Recuento, Porcentaje
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Primary Conversions (A) or Primary Conversion Event' %} Para el correo electrónico, push y webhooks, empezamos a hacer el seguimiento de las conversiones después del envío inicial.

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><b><i>Conversiones primarias (A)</i> o <i>evento de conversión primaria</i>:</b> Cuenta</li>
        <li><b><i>Conversiones primarias (A) %</i> o <i>tasa del evento de conversión primaria</i>:</b> (Conversiones primarias) / (Destinatarios únicos)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Confianza

{% apitags %}
Cuenta
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confidence' %}

{% endapi %}

{% api %}

### La máquina se abre
  
{% multi_lang_include analytics/metrics.md metric='Machine Opens' %} Esta métrica es objeto de seguimiento a partir del 11 de noviembre de 2021 para SendGrid y del 2 de diciembre de 2021 para SparkPost.

<span class="calculation-line">Cálculo: Cuenta </span>

{% endapi %}

{% api %}

### Otros Abre

{% apitags %}
Cuenta
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Other Opens' %} Ten en cuenta que un usuario también puede abrir un correo electrónico (como el recuento de aperturas para <i>Otras aperturas</i>) antes de que se registre un recuento de <i>Aperturas de máquina</i>. Si un usuario abre un correo electrónico una vez (o más) después de un evento de apertura de máquina desde un buzón de entrada que no sea de Apple Mail, entonces la cantidad de veces que el usuario abre el correo electrónico se calcula para <i>Otras aperturas</i> y sólo una vez para <i>Aperturas únicas</i>.

<span class="calculation-line">Cálculo: Cuenta </span>

{% endapi %}

{% api %}

### Tasa de clics abiertos

{% apitags %}
Porcentaje
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Click-to-Open Rate' %}

<span class="calculation-line">Cálculo: (Clics únicos) / (Aperturas únicas) (para correo electrónico)</span>

{% endapi %}