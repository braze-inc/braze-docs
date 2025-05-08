---
nav_title: Glosario de Email Analytics
article_title: Glosario de Email Analytics
layout: email_report_metrics
page_order: 0
excerpt_separator: ""
page_type: glossary
description: "Este glosario incluye los términos que encontrará en la sección de análisis de su campaña de correo electrónico o Canvas, tras el lanzamiento. Este glosario no incluye las métricas Currents."
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
Recuento
{% endapitags %}

{% multi_lang_include metrics.md metric='Variation' %}

<span class="calculation-line">Cálculo: Recuento</span>

{% endapi %}

{% api %}

### Envío por correo electrónico

{% apitags %}
Recuento
{% endapitags %}

{% multi_lang_include metrics.md metric='Emailable' %}

<span class="calculation-line">Cálculo: Recuento</span>

{% endapi %}

{% api %}

### % de audiencia

{% apitags %}
Porcentaje
{% endapitags %}

{% multi_lang_include metrics.md metric='Audience' %}

<span class="calculation-line">Cálculo: (Número de destinatarios en la variante) / (Destinatarios únicos)</span>

{% endapi %}

{% api %}

### Destinatarios únicos

{% apitags %}
Recuento
{% endapitags %}

{% multi_lang_include metrics.md metric='Destinatarios únicos' %} Este número se recibe de Braze.

<span class="calculation-line">Cálculo: Recuento</span>

{% endapi %}

{% api %}

### Envíos

{% apitags %}
Recuento
{% endapitags %}

{% multi_lang_include metrics.md metric='Envíos' %} Esta métrica la proporciona Braze.

<span class="calculation-line">Cálculo: Recuento</span>

{% endapi %}

{% api %}

### Mensajes enviados

{% apitags %}
Recuento
{% endapitags %}

{% multi_lang_include metrics.md metric='Mensajes enviados' %} Esta métrica la proporciona Braze.

<span class="calculation-line">Cálculo: Recuento</span>

{% endapi %}

{% api %}

### Entregas

{% apitags %}
Recuento
{% endapitags %}

{% multi_lang_include metrics.md metric='Entregas' %} En el caso de los correos electrónicos, *las Entregas* son el número total de mensajes (Envíos) enviados y recibidos correctamente por las partes que pueden enviar correos electrónicos.

<span class="calculation-line">Cálculo: (Envía) - (Rebota) </span>

{% endapi %}

{% api %}

### % de entregas

{% apitags %}
Porcentaje
{% endapitags %}

{% multi_lang_include metrics.md metric='Deliveries %' %}

<span class="calculation-line">Cálculo: (Envíos - Rebotes) / (Envíos) </span>

{% endapi %}

{% api %}

### Rebotes

{% apitags %}
Recuento, Porcentaje
{% endapitags %}

{% multi_lang_include metrics.md metric='Bounces' %} 

Para el correo electrónico, *el % de rebote* o *tasa de rebote* es el porcentaje de mensajes que se enviaron sin éxito o se designaron como "devueltos" o "no recibidos" de los servicios de envío utilizados o no recibidos por los usuarios destinatarios del correo electrónico.

Un rebote de correo electrónico para clientes que utilizan SendGrid consiste en rebotes duros, correo no deseado (`spam_report_drops`) y correos enviados a direcciones no válidas (`invalid_emails`).

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><b><i>Rebota</i>:</b> Recuento</li>
        <li><b><i>% de rebote</i> o <i>tasa de rebote %</i>:</b> (Rebota) / (Envía)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Rebote duro

{% apitags %}
Recuento
{% endapitags %}

{% multi_lang_include metrics.md metric='Hard Bounce' %} 

<span class="calculation-line">Cálculo: Cuenta </span>

{% endapi %}

{% api %}

### Rebote suave

{% apitags %}
Recuento
{% endapitags %}

{% multi_lang_include metrics.md metric='Rebote blando' %} Si un correo electrónico recibe un rebote blando, normalmente lo reintentaremos en un plazo de 72 horas, pero el número de intentos de reintento varía de un receptor a otro. 

Aunque los rebotes blandos no se siguen en los análisis de tu campaña, puedes controlar los rebotes blandos en el [Registro de actividad de mensajes]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) o excluir a estos usuarios de tus envíos con el [filtro de segmento de rebotes blandos]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#soft-bounced). En el Registro de actividad de mensajes, también puedes ver el motivo de los rebotes blandos y comprender las posibles discrepancias entre los "envíos" y las "entregas" de tus campañas de correo electrónico.

<span class="calculation-line">Cálculo: Cuenta </span>

{% endapi %}

{% api %}
  
### Correo no deseado

{% apitags %}
Recuento, Porcentaje
{% endapitags %}

{% multi_lang_include metrics.md metric='Spam' %}

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><b><i>Correo no deseado</i>:</b> Recuento</li>
        <li><b><i>% de correo no deseado</i> o <i>% de tasa de correo no deseado</i>:</b> (Marcado como correo no deseado) / (Envía)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}
  
### Aperturas únicas

{% apitags %}
Recuento, Porcentaje
{% endapitags %}

{% multi_lang_include metrics.md metric='Unique Opens' %} En el caso del correo electrónico, se realiza un seguimiento durante un periodo de 7 días.

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><b><i>Unique Opens</i>:</b> Recuento</li>
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

{% multi_lang_include metrics.md metric='Clics únicos' %} Se realiza un seguimiento durante un periodo de siete días para el correo electrónico y se mide por <a href='/docs/help/help_articles/data/dispatch_id/'>dispatch_id</a>. Esto incluye los clics en los enlaces de cancelación de suscripción proporcionados por Braze.

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><b><i>Clics únicos</i>:</b> Recuento</li>
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

{% multi_lang_include metrics.md metric='Unsubscribers or Unsub' %}

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><b><i>Cancelar suscripción</i> o <i>darse de baja</i>:</b> Recuento</li>
        <li><b><i>Suscriptores %</i> o <i>tasa de cancelación de suscripciones</i>:</b> (Cancelaciones de suscripción) / (Entregas)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Ingresos

{% apitags %}
Recuento
{% endapitags %}

{% multi_lang_include metrics.md metric='Revenue' %}

<span class="calculation-line">Cálculo: Cuenta </span>

{% endapi %}

{% api %}

### Conversiones primarias (A) o evento de conversión primaria

{% apitags %}
Recuento, Porcentaje
{% endapitags %}

{% multi_lang_include metrics.md metric='Conversiones primarias (A) o evento de conversión primaria' %} En el caso del correo electrónico, push y webhooks, empezamos a hacer el seguimiento de las conversiones después del envío inicial.

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><b><i>Conversiones primarias (A)</i> o <i>evento de conversión primaria</i>:</b> Recuento</li>
        <li><b><i>Conversiones primarias (A) %</i> o <i>tasa del evento de conversión primaria</i>:</b> (Conversiones primarias) / (Destinatarios únicos)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Confianza

{% apitags %}
Recuento
{% endapitags %}

{% multi_lang_include metrics.md metric='Confidence' %}

{% endapi %}

{% api %}

### Machine Opens (Aperturas automáticas)
  
{% multi_lang_include metrics.md metric='Machine Opens' %} Esta métrica es objeto de seguimiento a partir del 11 de noviembre de 2021 para SendGrid y del 2 de diciembre de 2021 para SparkPost.

<span class="calculation-line">Cálculo: Cuenta </span>

{% endapi %}

{% api %}

### Otras aperturas

{% apitags %}
Recuento
{% endapitags %}

{% multi_lang_include metrics.md metric='Other Opens' %} Ten en cuenta que un usuario también puede abrir un correo electrónico (como las aperturas que cuentan para <i>Otras aperturas</i>) antes de que se registre un recuento de <i>Aperturas de máquina</i>. Si un usuario abre un correo electrónico una vez (o más) después de un evento de apertura automática desde una bandeja de entrada que no sea de Apple Mail, entonces la cantidad de veces que el usuario abre el correo electrónico se calcula para <i>Otras aperturas</i> y sólo una vez para <i>Aperturas únicas</i>.

<span class="calculation-line">Cálculo: Cuenta </span>

{% endapi %}

{% api %}

### Tasa de clics de apertura

{% apitags %}
Porcentaje
{% endapitags %}

{% multi_lang_include metrics.md metric='Click-to-Open Rate' %}

<span class="calculation-line">Cálculo: (Clics únicos) / (Aperturas únicas) (para correo electrónico)</span>

{% endapi %}