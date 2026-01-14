---
nav_title: Glosario de métricas de los informes
article_title: Glosario de métricas de los informes
layout: report_metrics
page_order: 0.5
excerpt_separator: ""
page_type: glossary
description: "Este glosario define los términos que encontrarás en los informes de tu cuenta Braze."
tool: Reports
---

<style>
  .calculation-line {
    color: #76848C;
    font-size: 14px;
  }
</style>

{% api %}

### Clics AMP

{% apitags %}
Correo electrónico
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='AMP Clicks' %}

{% endapi %}

{% api %}

### Abre la AMP

{% apitags %}
Correo electrónico
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='AMP Opens' %}

{% endapi %}

{% api %}

### Audiencia

{% apitags %}
Todos
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Audience' %}

<span class="calculation-line">Cálculo: (Número de destinatarios en la variante) / (Destinatarios únicos)</span>

{% endapi %}

{% api %}

### Rebotes

{% apitags %}
Correo electrónico, Web Push, iOS Push
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Bounces' %} Esto puede ocurrir porque no hay un token de notificaciones push válido, el usuario se dio de baja después de lanzar la campaña o la dirección de correo electrónico es inexacta o está desactivada.

|Canal|Información adicional|
|-------|-----------------------|
|Correo electrónico|Un rebote de correo electrónico para clientes que utilizan SendGrid consiste en rebotes duros, correo no deseado (`spam_report_drops`) y correos enviados a direcciones no válidas (`invalid_emails`).<br><br>Para el correo electrónico, *el % de rebote* o *tasa de rebote* es el porcentaje de mensajes que se enviaron sin éxito o se designaron como "devueltos" o "no recibidos" de los servicios de envío utilizados o no recibidos por los usuarios destinatarios del correo electrónico.|
|Push|Estos usuarios se han dado de baja automáticamente de todas las notificaciones push futuras.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Rebota</i>: Cuenta</li>
        <li><i>% de rebote</i> o <i>tasa de rebote %</i>: (Rebota) / (Envía)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Cuerpo Clic

{% apitags %}
Push iOS, Push Android
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Body Click' %}

<span class="calculation-line">Cálculo: (Clics en el cuerpo) / (Impresiones)</span>

{% endapi %}

{% api %}

### Clics en el cuerpo

{% apitags %}
Mensaje dentro de la aplicación
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Body Clicks' %} Para más detalles, consulta los registros de cambios del SDK para [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/changelog/objc_changelog#3310) y [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/changelog#1100).

<span class="calculation-line">Cálculo: (Clics en el cuerpo) / (Impresiones)</span>

{% endapi %}

{% api %}

### Botón 1 Clics

{% apitags %}
Mensaje dentro de la aplicación
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Button 1 Clicks' %} La generación de informes para los _clics del botón 1_ sólo funciona cuando especificas el **identificador para la generación de** informes como "0" en el mensaje dentro de la aplicación.

<span class="calculation-line">Cálculo: (Clics en el botón 1) / (Impresiones)</span>

{% endapi %}

{% api %}

### Botón 2 Clics

{% apitags %}
Mensaje dentro de la aplicación
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Button 2 Clicks' %} La generación de informes para el _botón 2 clics_ sólo funciona cuando especificas el **identificador para la generación de** informes como "1" en el mensaje dentro de la aplicación.

<span class="calculation-line">Cálculo: (Botón 2 Clics) / (Impresiones)</span>

{% endapi %}

{% api %}

### Análisis de campaña

{% apitags %}
Banderas de características
{% endapitags %}

El rendimiento del mensaje a través de varios canales. Las métricas mostradas dependen del canal de mensajería seleccionado y de si el [experimento de la Bandera de características]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/experiments/#campaign-analytics) es una prueba multivariante.

{% endapi %}

{% api %}

### Opciones presentadas

{% apitags %}
Mensaje dentro de la aplicación
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Choices Submitted' %}

{% endapi %}

{% api %}

### Tasa de clics abiertos

{% apitags %}
Correo electrónico
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Click-to-Open Rate' %}

<span class="calculation-line">Cálculo: (Clics únicos) / (Aperturas únicas) (para correo electrónico)</span>

{% endapi %}

{% api %}

### Entregas Confirmadas por RCS o Entregas Confirmadas por SMS

{% apitags %}
SMS/MMS, RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confirmed Deliveries' %} Como cliente de Braze, las entregas se cargan a tu asignación de SMS. 

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Entregas confirmadas</i>: Cuenta</li>
        <li><i>Tasa de entrega confirmada</i>: (Entregas confirmadas) / (Envíos)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Confianza

{% apitags %}
Tarjetas de contenido, correo electrónico, mensajes dentro de la aplicación, push web, push de iOS, push de Android, webhook, SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confidence' %}

{% endapi %}

{% api %}

### Botón de página de confirmación

{% apitags %}
Mensaje dentro de la aplicación
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confirmation Page Button' %}

{% endapi %}

{% api %}

### Página de confirmación Despidos

{% apitags %}
Mensaje dentro de la aplicación
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confirmation Page Dismissals' %}

{% endapi %}

{% api %}

### Conversiones (B, C, D)

{% apitags %}
Tarjetas de contenido, correo electrónico, mensajes dentro de la aplicación, push web, push de iOS, push de Android, webhook, SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Conversions (B, C, D)' %} Este evento definido lo determinas tú al crear la campaña. 

|Canal|Información adicional|
|-------|-----------------------|
|Correo electrónico, push, webhooks|Las conversiones se siguen después del envío inicial.|
|Tarjetas de contenido|Las conversiones se contabilizan cuando el usuario ve una tarjeta de contenido por primera vez.|
|Mensajes dentro de la aplicación|Se cuenta una conversión si el usuario ha recibido y visto la campaña de mensajería dentro de la aplicación, y posteriormente realiza el evento de conversión específico dentro de la ventana de conversión definida, independientemente de si ha hecho clic en el mensaje o no.<br><br>Las conversiones se atribuyen al último mensaje recibido. Si se habilita la reelegibilidad, la conversión se asignará al último mensaje dentro de la aplicación recibido, siempre que se produzca dentro de la ventana de conversión definida. Sin embargo, si al mensaje dentro de la aplicación ya se le ha asignado una conversión, no se podrá registrar la nueva conversión para ese mensaje concreto. Esto significa que cada entrega de mensaje dentro de la aplicación está asociada a una sola conversión.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endapi %}

{% api %}

### Conversiones totales

{% apitags %}
Mensaje dentro de la aplicación
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Conversions' %}

Cuando un usuario ve una campaña de mensajería dentro de la aplicación una sola vez, sólo se cuenta una conversión, aunque realice el evento de conversión varias veces más tarde. Sin embargo, si la reelegibilidad está activada y el usuario ve la campaña de mensajería dentro de la aplicación varias veces, *el Total de conversiones* puede aumentar una vez por cada vez que el usuario registre una impresión para una nueva instancia de la campaña de mensajería dentro de la aplicación. 

Por ejemplo, si un usuario desencadena un mensaje dentro de la aplicación dos veces y convierte después de cada impresión de mensaje dentro de la aplicación (lo que da lugar a dos conversiones), *el Total de conversiones* aumentará en dos. Sin embargo, si sólo hubo una impresión de mensaje dentro de la aplicación seguida de dos eventos de conversión, sólo se registrará una conversión, y *el Total de conversiones* aumentará en uno.

{% endapi %}

{% api %}

### Cerrar mensaje

{% apitags %}
Mensaje dentro de la aplicación
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Close Message' %}

{% endapi %}

{% api %}

### Tasa de conversión

{% apitags %}
Tarjetas de contenido, correo electrónico, mensajes dentro de la aplicación, push web, push de iOS, push de Android, webhook, SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Conversion Rate' %}

|Canal|Información adicional|
|-------|-----------------------|
|Mensajes dentro de la aplicación|La métrica del total de <i>impresiones únicas</i> diarias se utiliza para calcular la <i>tasa de conversión</i> de los mensajes dentro de la aplicación.<br><br>Las impresiones de los mensajes dentro de la aplicación sólo pueden contarse una vez al día. Por otra parte, el número de veces que un usuario completa una acción deseada (una "conversión") puede aumentar en un periodo de 24 horas. Mientras que las conversiones pueden producirse más de una vez al día, las impresiones no. Por lo tanto, si un usuario completa una conversión varias veces en un día, la <i>tasa de conversión</i> puede aumentar en consecuencia, pero las impresiones sólo se contarán una vez.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><b>Mensajes dentro de la aplicación</b>: (Conversiones primarias) / (Impresiones únicas)</li>
        <li><b>Otros canales</b>: (Conversiones primarias) / (Destinatarios únicos)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Ventana de conversión

{% apitags %}
Todos
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Conversion Window' %}

{% endapi %}

{% api %}

### Entregas

{% apitags %}
Correo electrónico, Web Push, iOS Push, Android Push, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Deliveries' %}

|Canal|Información adicional|
|-------|-----------------------|
|Correo electrónico|Se refiere al número total de mensajes (Sends) enviados y recibidos con éxito por las partes que pueden enviar correos electrónicos.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Entregas</i>: Cuenta</li>
        <li><i>% de entregas</i>: (Envíos - Rebotes) / (Envíos)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Fallos en la entrega de RCS o fallos en la entrega de SMS

{% apitags %}
SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Delivery Failures' %}

Ponte en contacto con <a href="/docs/braze_support/">el soporte de Braze</a> para que te ayude a comprender las razones de los fallos en la entrega.

<span class="calculation-line">Cálculo: (Envía) - (Envía al operador)</span>

{% endapi %}

{% api %}

### Fallos en la entrega

{% apitags %}
RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Delivery Failures RCS' %}

Ponte en contacto con <a href="/docs/braze_support/">el soporte de Braze</a> para que te ayude a comprender las razones de los fallos en la entrega.

<span class="calculation-line">Cálculo: (Envía) - (Envía al operador)</span>

{% endapi %}

{% api %}

### Tasa de entregas fallidas

{% apitags %}
SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Failed Delivery Rate' %}

Ponte en contacto con <a href="/docs/braze_support/">el soporte de Braze</a> para que te ayude a comprender las razones de los fallos en la entrega.

<span class="calculation-line">Cálculo: (Fallos de entrega) / (Envíos)</span>

{% endapi %}

{% api %}

### Direct Opens

{% apitags %}
Push iOS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Direct Opens' %}

<span class="calculation-line">Cálculo: (Direct Opens) / (Entregas)</span>

{% endapi %}

{% api %}

### Envío por correo electrónico

{% apitags %}
Correo electrónico
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Emailable' %}

<span class="calculation-line">Cálculo: Cuenta</span>

{% endapi %}

{% api %}

### Errores

{% apitags %}
Webhook
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Errors' %} Los errores se incluyen en el recuento de <i>Envíos</i>, pero no en el de <i>Destinatarios únicos</i>.

{% endapi %}

{% api %}

### Estimación de Aperturas Reales

{% apitags %}
Correo electrónico
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Estimated Real Opens' %}

{% endapi %}

{% api %}

### Fallas

{% apitags %}
WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Failures' %} Los fallos se incluyen en el recuento de <i>Envíos</i>, pero no en el de <i>Entregas</i>.</td>

<span class="calculation-line">Cálculo<i>(tasa de fallos</i>): (Fallos) / (Envíos)</span>

{% endapi %}

{% api %}

### Bandera de características rendimiento del experimento

{% apitags %}
Banderas de características
{% endapitags %}

Métricas de rendimiento del mensaje en un experimento de Bandera de características. Las métricas específicas mostradas variarán en función del canal de mensajería y de si el experimento era o no una prueba multivariante.

{% endapi %}

{% api %}

### Rebote duro

{% apitags %}
Correo electrónico
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Hard Bounce' %} 

Cuando esto ocurre, Braze marca la dirección de correo electrónico como no válida, pero no actualiza el estado de suscripción del usuario. Si un correo electrónico recibe un rebote duro, detendremos cualquier solicitud futura a esta dirección de correo electrónico.

{% endapi %}

{% api %}

### Ayuda

{% apitags %}
SMS/MMS, RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Help' %} Una respuesta de usuario se mide cada vez que un usuario envía un mensaje entrante en las cuatro horas siguientes a la recepción de tu mensaje.

{% endapi %}

{% api %}

### Influenced Opens

{% apitags %}
Push iOS, Push Android
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Influenced Opens' %}

<span class="calculation-line">Cálculo: (Influenced Opens) / (Entregas)</span>

{% endapi %}

{% api %}

### Ingresos de toda la vida

{% apitags %}
Tarjetas de contenido, correo electrónico, mensajes dentro de la aplicación, push web, push de iOS, push de Android, webhook, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Lifetime Revenue' %}

{% endapi %}

{% api %}

### Valor de duración del ciclo de vida por usuario

{% apitags %}
Tarjetas de contenido, correo electrónico, mensajes dentro de la aplicación, push web, push de iOS, push de Android, webhook, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Lifetime Value Per User' %}

{% endapi %}

{% api %}

### Ingresos medios diarios

{% apitags %}
Tarjetas de contenido, correo electrónico, mensajes dentro de la aplicación, push web, push de iOS, push de Android, webhook, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Average Daily Revenue' %}

{% endapi %}

{% api %}

### Compras diarias

{% apitags %}
Tarjetas de contenido, correo electrónico, mensajes dentro de la aplicación, push web, push de iOS, push de Android, webhook, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Daily Purchases' %}

{% endapi %}

{% api %}

### Ingresos diarios por usuario

{% apitags %}
Tarjetas de contenido, correo electrónico, mensajes dentro de la aplicación, push web, push de iOS, push de Android, webhook, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Daily Revenue Per User' %}

{% endapi %}

{% api %}

### La máquina se abre

{% apitags %}
Correo electrónico
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Machine Opens' %} Esta métrica es objeto de seguimiento a partir del 11 de noviembre de 2021 para SendGrid y del 2 de diciembre de 2021 para SparkPost. Para Amazon SES, los análisis aparecerán como _Abiertos_. Sin embargo, se admitirá el filtrado de bots por clics.

{% endapi %}

{% api %}

### Abre

{% apitags %}
Web Push, iOS Push, Android Push
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Opens' %}

{% endapi %}

{% api %}

### Adhesión voluntaria

{% apitags %}
SMS/MMS, RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Opt-Out' %} Una respuesta de usuario se mide cada vez que un usuario envía un mensaje entrante en las cuatro horas siguientes a la recepción de tu mensaje.

{% endapi %}

{% api %}

### Otros Abre

{% apitags %}
Correo electrónico
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Other Opens' %} Ten en cuenta que un usuario también puede abrir un correo electrónico (como el recuento de aperturas para Otras aperturas) antes de que se registre un recuento de Aperturas de máquina. Si un usuario abre un correo electrónico una vez (o más) después de un evento de apertura de máquina desde un buzón de entrada que no es de Apple Mail, entonces la cantidad de veces que el usuario abre el correo electrónico se calcula para Otras aperturas y sólo una vez para Aperturas únicas.

{% endapi %}

{% api %}

### Reintento pendiente

{% apitags %}
Correo electrónico
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Pending Retry' %}

{% endapi %}

{% api %}

### Conversiones primarias (A) o evento de conversión primaria

{% apitags %}
Tarjetas de contenido, correo electrónico, mensajes dentro de la aplicación, push web, push de iOS, push de Android, webhook, SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Primary Conversions (A) or Primary Conversion Event' %} 

|Canal|Información adicional|
|-------------|----------------------|
|Correo electrónico, push, webhooks|Tras el envío inicial.|
|Tarjetas de contenido, mensajes dentro de la aplicación|Cuando el usuario ve la tarjeta de contenido o el mensaje por primera vez.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Conversiones primarias (A) o evento de conversión primaria</i>: Cuenta</li>
        <li><i>Conversiones primarias (A) %</i> o <i>tasa del evento de conversión primaria</i>: (Conversiones primarias) / (Destinatarios únicos)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Lee

{% apitags %}
WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Reads' %}

{% endapi %}

{% api %}

### Tasa de lectura

{% apitags %}
WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Read Rate' %}

<span class="calculation-line">Cálculo: (Lecturas con recibos de lectura) / (Envíos)</span>

{% endapi %}

{% api %}

### Recibido

{% apitags %}
Correo electrónico, tarjetas de contenido, mensajes dentro de la aplicación, push web, push de iOS, push de Android, SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Received' %} 

|Canal|Información adicional|
|-------|-------|
|Tarjetas de contenido|Se recibe cuando los usuarios ven la tarjeta en la aplicación.|
|Push|Se recibe cuando se envían mensajes desde el servidor Braze al proveedor push.|
|Correo electrónico|Se recibe cuando se envían mensajes desde el servidor Braze al proveedor de correo electrónico.|
|SMS/MMS|"Entregado" después de que el proveedor de SMS reciba la confirmación del operador de origen y del dispositivo de destino.|
|Mensaje dentro de la aplicación|Recibida en el momento de la visualización en función de la acción desencadenante definida.|
|WhatsApp|Recibida en el momento de la visualización en función de la acción desencadenante definida.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endapi %}

{% api %}

### Rechazos RCS o Rechazos SMS

{% apitags %}
SMS/MMS, RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Rejections' %} Como cliente de Braze, los rechazos se cargan a tu asignación de SMS.

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Rechazos</i>: Cuenta</li>
        <li><i>Tasa de rechazo</i>: (Rechazos) / (Envíos)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Ingresos

{% apitags %}
Correo electrónico
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Revenue' %}

{% endapi %}

{% api %}

### Enviado

{% apitags %}
SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Sent' %}

<span class="calculation-line">Cálculo: Cuenta</span>

{% endapi %}

{% api %}

### Envía

{% apitags %}
Tarjetas de contenido, correo electrónico, mensajes dentro de la aplicación, push web, push de iOS, push de Android, webhook, SMS/MMS, RCS, WhatsApp, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Sends' %} Esta métrica la proporciona Braze. Ten en cuenta que al lanzar una campaña programada, esta métrica incluirá todos los mensajes enviados, independientemente de si ya se han enviado o no, debido a la limitación de tasa.

{% alert tip %}
Para las tarjetas de contenido, esta métrica se calcula de forma diferente dependiendo de lo que hayas seleccionado para la [creación de la tarjeta]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/):

- **En el lanzamiento o en la entrada escalonada:** El número de tarjetas creadas y disponibles para ver. Esto no cuenta si los usuarios vieron la tarjeta.
- **En la primera impresión:** El número de tarjetas mostradas a los usuarios.
{% endalert %}

<span class="calculation-line">Cálculo: Cuenta</span>

{% endapi %}

{% api %}

### Mensajes enviados

{% apitags %}
Tarjetas de contenido, correo electrónico, mensaje dentro de la aplicación, push web, push de iOS, push de Android, webhook, SMS/MMS, WhatsApp, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Messages Sent' %}  Esta métrica la proporciona Braze. Ten en cuenta que al lanzar una campaña programada, esta métrica incluirá todos los mensajes enviados, independientemente de si ya se han enviado o no, debido a la limitación de tasa.

{% alert tip %}
Para las tarjetas de contenido, esta métrica se calcula de forma diferente dependiendo de lo que hayas seleccionado para la [creación de la tarjeta]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/):

- **En el lanzamiento o en la entrada escalonada:** El número de tarjetas creadas y disponibles para ver. Esto no cuenta si los usuarios vieron la tarjeta.
- **En la primera impresión:** El número de tarjetas mostradas a los usuarios.
{% endalert %}

<span class="calculation-line">Cálculo: Cuenta</span>

{% endapi %}

{% api %}

### Envía al operador

{% apitags %}
SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Sends to Carrier' %} 

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Envía al operador</i>: Cuenta</li>
        <li><i>Envía a la tasa del operador</i>: (Envía al operador) / (Envía)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Rebote blando

{% apitags %}
Correo electrónico
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Soft Bounce' %} Nota que _los Rebotes blandos_ difieren de _los Aplazamientos_. Si no se entregó correctamente ningún correo electrónico durante este periodo de reintento, Braze enviará un evento de rebote blando por cada intento de envío de campaña. Antes del 25 de febrero de 2025, estos reintentos se contabilizaban como múltiples rebotes blandos para 1 envío de campaña.

Aunque los rebotes blandos no son objeto de seguimiento en los análisis de tu campaña, puedes controlar los rebotes blandos en el [Registro de actividad de mensajes]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/). También puedes excluir a estos usuarios de tus envíos o consultar la cantidad de rebotes blandos de los últimos 30 días con el [filtro de segmento Rebote blando]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#soft-bounced). En el Registro de actividad de mensajes, también puedes ver el motivo de los rebotes blandos y comprender las posibles discrepancias entre los "envíos" y las "entregas" de tus campañas de correo electrónico.

{% endapi %}

{% api %}

### Correo no deseado

{% apitags %}
Correo electrónico
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Spam' %}

{% alert note %}
Las reclamaciones por correo no deseado las gestionan directamente los proveedores de servicios de correo electrónico y luego se transmiten a Braze a través de un bucle de retroalimentación. La mayoría de los bucles de respuesta sólo informan de una parte de las quejas reales, por lo que la métrica _del correo no deseado_ suele representar una fracción del total real. Sólo los proveedores de servicios de correo electrónico pueden ver el volumen real de reclamaciones por correo no deseado, lo que significa que _el Spam_ debe considerarse una métrica indicativa, no exhaustiva.
{% endalert %}

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Correo no deseado</i>: Cuenta</li>
        <li><i>% de correo no deseado</i> o <i>% de tasa de correo no deseado</i>: (Marcado como correo no deseado) / (Envía)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Página del cuestionario Despidos

{% apitags %}
Mensaje dentro de la aplicación
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Survey Page Dismissals' %}

{% endapi %}

{% api %}

### Envío de cuestionarios

{% apitags %}
Mensaje dentro de la aplicación
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Survey Submissions' %}

{% endapi %}

{% api %}

### Clics totales

{% apitags %}
Correo electrónico, tarjetas de contenido, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Clicks' %}

|Canal|Información adicional|
|-------|-------|
|LÍNEA|Seguimiento una vez alcanzado un umbral mínimo de 20 mensajes diarios. Los correos electrónicos AMP incluyen clics registrados tanto en versión HTML como en texto plano. Este número puede estar inflado artificialmente por las herramientas anti-spam.|
|Pancartas|El número total (y porcentaje) de usuarios que hicieron clic en el mensaje entregado, independientemente de si el mismo usuario hace clic varias veces.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><b>Correo electrónico:</b> (Clics totales) / (Entregas)</li>
        <li><b>Tarjetas de contenido:</b> (Clics totales) / (Impresiones totales)</li>
        <li><b>SMS:</b> (Aperturas por clic) / (Entregas)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Total Despidos

{% apitags %}
Tarjetas de contenido
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Dismissals' %} Si un usuario recibe dos tarjetas diferentes de la misma campaña y descarta ambas, este recuento aumentará en dos. La reelegibilidad te permite incrementar _el Total de Descartes_ una vez cada vez que un usuario recibe una tarjeta; cada tarjeta es un mensaje diferente.

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Total de despidos:</i> Cuenta</li>
        <li><i>Tasa total de despidos:</i> Despidos totales / Impresiones totales</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Impresiones totales

{% apitags %}
Mensaje dentro de la aplicación, tarjetas de contenido
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Impressions' %} Este número es la suma del número de eventos de impresión que Braze recibe de los SDK.

|Canal|Información adicional|
|-------|-----------------------|
|Tarjetas de contenido|El recuento total de impresiones registradas para una determinada tarjeta de contenido. Esto puede incrementarse varias veces para el mismo usuario.|
|Mensajes dentro de la aplicación|Si hay varios dispositivos y la reelegibilidad está desactivada, el usuario sólo debería ver el mensaje dentro de la aplicación una vez. Aunque el usuario utilice varios dispositivos, sólo lo verá en el primer dispositivo al que se dirija. Esto supone que el perfil tiene dispositivos consolidados y que un usuario tiene un ID de usuario con el que ha iniciado sesión en todos los dispositivos. Si la reelegibilidad está activada, se registra una impresión cada vez que el usuario ve el mensaje dentro de la aplicación.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

<span class="calculation-line">Cálculo: Cuenta</span>

{% endapi %}

{% api %}

### Aperturas totales

{% apitags %}
Correo electrónico, iOS Push, Android Push, Web Push, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Opens' %}

|Canal|Información adicional|
|-------|-----------------------|
|LÍNEA|Seguimiento una vez alcanzado un umbral mínimo de 20 mensajes diarios.|
|Correos electrónicos AMP|El total se abre para las versiones HTML y texto sin formato.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><b><i>Aperturas totales</i> del correo electrónico:</b> Cuenta</li>
        <li><b><i>Tasa de apertura total del</i> correo electrónico:</b> (Aperturas) / (Entregas)</li>
        <li><b>Web push <i>Total Aperturas</i>:</b> Recuento de <i>Direct Opens</i> </li>
        <li><b>Web push <i>Tasa total de apertura</i>:</b> (Aperturas totales) / (Entregas)</li>
        <li><b>iOS, Android y Kindle push <i>Aperturas totales</i>:</b> (Direct Opens) + (Influenced Opens)</li>
        <li><b>iOS, Android y Kindle push <i>Tasa total de apertura</i>:</b> (Aperturas totales) / (Entregas)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Total Ingresos

{% apitags %}
Tarjetas de contenido, correo electrónico, mensajes dentro de la aplicación, push web, push de iOS, push de Android, webhook, SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Revenue' %} Esta métrica sólo está disponible en los Informes de Comparación de Campañas a través del <a href='https://braze.com/docs/user_guide/data_and_analytics/reporting/report_builder/'>Generador de informes</a>

{% endapi %}

{% api %}

### Clics únicos

{% apitags %}
Correo electrónico, tarjetas de contenido, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Clicks' %}

Esto incluye los clics en los enlaces para cancelar suscripción proporcionados por Braze.

|Canal|Información adicional|
|-------|-----------------------|
|Correo electrónico|Seguimiento durante un periodo de siete días.|
|LÍNEA|Seguimiento una vez alcanzado un umbral mínimo de 20 mensajes diarios.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Clics únicos</i>: Cuenta</li>
        <li><b>Tarjetas de contenido</b> <i>% de clics únicos</i> o <i>tasa de clics únicos</i>: (Clics únicos) / (Impresiones únicas)</li>
        <li><i>Porcentaje de clics únicos</i> <b>por correo electrónico</b> o <i>tasa de clics únicos</i>: (Clics únicos) / (Entregas)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Despidos únicos

{% apitags %}
Tarjetas de contenido
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Dismissals' %}

<span class="calculation-line">Cálculo: (Despidos únicos) / (Impresiones únicas)</span>

{% endapi %}

{% api %}

### Impresiones únicas

{% apitags %}
Mensaje dentro de la aplicación, tarjetas de contenido
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Impressions' %} 

|Canal|Información adicional|
|-------|-----------------------|
|Mensajes dentro de la aplicación|Las impresiones únicas pueden incrementarse de nuevo al cabo de 24 horas si la reelegibilidad está activada y un usuario realiza la acción desencadenante. Si la reelegibilidad está activada, <i>Impresiones únicas</i> = <i>Destinatarios únicos</i>.|
|Tarjetas de contenido|El recuento no debe incrementarse la segunda vez que un usuario ve una tarjeta.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

<span class="calculation-line">Cálculo: Cuenta</span>

{% endapi %}

{% api %}

### Unique Opens

{% apitags %}
Correo electrónico, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Opens' %}

|Canal|Información adicional|
|-------|-----------------------|
|Correo electrónico|Seguimiento durante un periodo de 7 días.|
|LÍNEA|Seguimiento una vez alcanzado un umbral mínimo de 20 mensajes diarios.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Unique Opens</i>: Cuenta</li>
        <li><i>Unique Opens %</i> o <i>tarifa abierta única</i>: (Unique Opens) / (Entregas)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Destinatarios únicos

{% apitags %}
Todos
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Recipients' %}

Dado que un espectador puede ser un destinatario único cada día, debes esperar que sea superior a <i>Impresiones únicas</i>. Para las tarjetas de contenido, cada tarjeta de contenido sólo puede recibirse una vez, por lo que ver la misma tarjeta de contenido una segunda vez, independientemente del día, no incrementará este recuento.<br><br>Este número se recibe de Braze y se basa en la dirección `user_id`. Los destinatarios únicos se cuentan a nivel de campaña o paso en Canvas, no a nivel de <a href='https://braze.com/docs/api/identifier_types/#send-identifier'>identificador de envío</a>.

<span class="calculation-line">Cálculo: Cuenta</span>

{% endapi %}

{% api %}

### Cancelar suscripción o darse de baja

{% apitags %}
Correo electrónico
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unsubscribers or Unsub' %}

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Cancelar suscripción</i> o <i>darse de baja</i>: Cuenta</li>
        <li><i>Suscriptores %</i> o <i>tasa de cancelación de suscripciones</i>: (Cancelaciones de suscripción) / (Entregas)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Cancelar suscripción

{% apitags %}
Correo electrónico
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unsubscribes' %}

<span class="calculation-line">Cálculo: (Cancelaciones de suscripción) / (Entregas)</span>

{% endapi %}

{% api %}

### Variación

{% apitags %}
Tarjetas de contenido, correo electrónico, mensajes dentro de la aplicación, push web, push de iOS, push de Android, webhook, SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Variation' %}

<span class="calculation-line">Cálculo: Cuenta</span>

{% endapi %}