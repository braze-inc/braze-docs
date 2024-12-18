---
nav_title: Glosario de métricas de los informes
article_title: Glosario de métricas de los informes
layout: report_metrics
page_order: 0
excerpt_separator: ""
page_type: glossary
description: "Este glosario define los términos que encontrará en los informes de su cuenta Braze."
tool: Reports
---

<style>
  .calculation-line {
    color: #76848C;
    font-size: 14px;
  }
</style>

{% api %}

### Clics en páginas móviles aceleradas

{% apitags %}
Correo electrónico
{% endapitags %}

{% multi_lang_include metrics.md metric='Clics AMP' %}

{% endapi %}

{% api %}

### Aperturas de páginas móviles aceleradas

{% apitags %}
Correo electrónico
{% endapitags %}

{% multi_lang_include metrics.md metric='Aperturas AMP' %}

{% endapi %}

{% api %}

### Audiencia

{% apitags %}
Todo
{% endapitags %}

{% multi_lang_include metrics.md metric='Audiencia' %}

<span class="calculation-line">Cálculo: (Número de destinatarios en la variante) / (Destinatarios únicos)</span>

{% endapi %}

{% api %}

### Rebotes

{% apitags %}
Correo electrónico, notificación push web, push de iOS
{% endapitags %}

{% multi_lang_include metrics.md metric='Rebotes' %} Esto puede ocurrir porque no hay un token de notificaciones push válido, el usuario se dio de baja después de lanzar campañas o la dirección de correo electrónico es inexacta o está desactivada.

#### Correo electrónico

Un rebote de correo electrónico para clientes que utilizan SendGrid consiste en rebotes duros, correo no deseado (`spam_report_drops`) y correos enviados a direcciones no válidas (`invalid_emails`).

Para el correo electrónico, *el % de rebote* o *tasa de rebote* es el porcentaje de mensajes que se enviaron sin éxito o se designaron como "devueltos" o "no recibidos" de los servicios de envío utilizados o no recibidos por los usuarios destinatarios del correo electrónico.

#### Push

Estos usuarios se han dado de baja automáticamente de todas las notificaciones push futuras. 

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Rebotes</i>:Contar</li>
        <li><i>% de rebote</i> o <i>tasa de rebote %</i>: (Envíos - Rebotes) / (Envíos)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Clics en el cuerpo

{% apitags %}
Push iOS, Push Android
{% endapitags %}

{% multi_lang_include metrics.md metric='Cuerpo clic' %}

<span class="calculation-line">Cálculo: (Clics en el cuerpo) / (Impresiones)</span>

{% endapi %}

{% api %}

### Clics del cuerpo

{% apitags %}
Mensaje dentro de la aplicación
{% endapitags %}

{% multi_lang_include metrics.md metric='Clics en el cuerpo' %} Para más detalles, consulta los registros de cambios del SDK para [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/changelog/objc_changelog#3310) y [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/changelog#1100).

<span class="calculation-line">Cálculo: (Clics en el cuerpo) / (Impresiones)</span>

{% endapi %}

{% api %}

### Clics en botón 1

{% apitags %}
Mensaje dentro de la aplicación
{% endapitags %}

{% multi_lang_include metrics.md metric='Clics en el botón 1' %}

<span class="calculation-line">Cálculo: (Clics en el botón 1) / (Impresiones)</span>

{% endapi %}

{% api %}

### Clics en botón 2

{% apitags %}
Mensaje dentro de la aplicación
{% endapitags %}

{% multi_lang_include metrics.md metric='Botón 2 clics' %}

<span class="calculation-line">Cálculo: (Clics en el botón 2) / (Impresiones)</span>

{% endapi %}

{% api %}

### Selecciones presentadas

{% apitags %}
Mensaje dentro de la aplicación
{% endapitags %}

{% multi_lang_include metrics.md metric='Opciones presentadas' %}

{% endapi %}

{% api %}

### Tasa de clics de apertura

{% apitags %}
Correo electrónico
{% endapitags %}

{% multi_lang_include metrics.md metric='Tasa de clics por apertura' %}

<span class="calculation-line">Cálculo: (Clics únicos) / (Aperturas únicas) (para correo electrónico)</span>

{% endapi %}

{% api %}

### Entregas confirmadas

{% apitags %}
SMS
{% endapitags %}

{% multi_lang_include metrics.md metric='Entregas confirmadas' %} Como cliente de Braze, las entregas se cargan a tu asignación de SMS. 

<span class="calculation-line">Cálculo: Recuento</span>

{% endapi %}

{% api %}

### Confianza

{% apitags %}
Tarjetas de contenido, correo electrónico, mensajes dentro de la aplicación, Web Push, iOS Push, Android Push, Webhook, SMS, WhatsApp
{% endapitags %}

{% multi_lang_include metrics.md metric='Confianza' %}

{% endapi %}

{% api %}

### Botón de la página de confirmación

{% apitags %}
Mensaje dentro de la aplicación
{% endapitags %}

{% multi_lang_include metrics.md metric='Botón de página de confirmación' %}

{% endapi %}

{% api %}

### Descartes de página de confirmación

{% apitags %}
Mensaje dentro de la aplicación
{% endapitags %}

{% multi_lang_include metrics.md metric='Página de confirmación de despidos' %}

{% endapi %}

{% api %}

### Conversiones (B, C, D)

{% apitags %}
Tarjetas de contenido, correo electrónico, mensajes dentro de la aplicación, Web Push, iOS Push, Android Push, Webhook, SMS
{% endapitags %}

{% multi_lang_include metrics.md metric='Conversiones (B, C, D)' %} Este evento definido lo determinas tú al crear la campaña. En el caso del correo electrónico, push y webhooks, comenzamos a realizar el seguimiento de las conversiones después del envío inicial. Para las tarjetas de contenido, este recuento comienza cuando ven una tarjeta de contenido por primera vez.

#### Mensajes dentro de la aplicación

Para los mensajes dentro de la aplicación, se cuenta una conversión si el usuario ha recibido y visto la campaña de mensajería dentro de la aplicación, y posteriormente realiza el evento de conversión específico dentro de la ventana de conversión definida, independientemente de si ha hecho clic en el mensaje o no.

Las conversiones se atribuyen al último mensaje recibido. Si se habilita la reelegibilidad, la conversión se asignará al último mensaje dentro de la aplicación recibido, siempre que se produzca dentro de la ventana de conversión definida. Sin embargo, si al mensaje dentro de la aplicación ya se le ha asignado una conversión, no se podrá registrar la nueva conversión para ese mensaje concreto. Esto significa que cada entrega de mensaje dentro de la aplicación está asociada a una sola conversión.

{% endapi %}

{% api %}

### Total de conversiones

{% apitags %}
Mensaje dentro de la aplicación
{% endapitags %}

{% multi_lang_include metrics.md metric='Conversiones totales' %}

Cuando un usuario ve una campaña de mensajería dentro de la aplicación una sola vez, sólo se cuenta una conversión, aunque realice el evento de conversión varias veces más tarde. Sin embargo, si la reelegibilidad está activada y el usuario ve la campaña de mensajería dentro de la aplicación varias veces, *el Total de conversiones* puede aumentar una vez por cada vez que el usuario registre una impresión para una nueva instancia de la campaña de mensajería dentro de la aplicación. 

Por ejemplo, si un usuario desencadena un mensaje dentro de la aplicación dos veces y convierte después de cada impresión de mensaje dentro de la aplicación (lo que da lugar a dos conversiones), *el Total de conversiones* aumentará en dos. Sin embargo, si sólo hubo una impresión de mensaje dentro de la aplicación seguida de dos eventos de conversión, sólo se registrará una conversión, y *el Total de conversiones* aumentará en uno.

{% endapi %}

{% api %}

### Tasa de conversión

{% apitags %}
Tarjetas de contenido, correo electrónico, mensajes dentro de la aplicación, Web Push, iOS Push, Android Push, Webhook, SMS
{% endapitags %}

{% multi_lang_include metrics.md metric='Conversion Rate' %}

#### Mensajes dentro de la aplicación

La métrica del total de <i>impresiones únicas</i> diarias se utiliza para calcular la <i>tasa de conversión</i> de los mensajes dentro de la aplicación.

Las impresiones de los mensajes dentro de la aplicación sólo pueden contarse una vez al día. Por otra parte, el número de veces que un usuario completa una acción deseada (una "conversión") puede aumentar en un periodo de 24 horas. Mientras que las conversiones pueden producirse más de una vez al día, las impresiones no. Por lo tanto, si un usuario completa una conversión varias veces en un día, la <i>tasa de conversión</i> puede aumentar en consecuencia, pero las impresiones sólo se contarán una vez.

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
Todo
{% endapitags %}

{% multi_lang_include metrics.md metric='Ventana de conversión' %}

{% endapi %}

{% api %}

### Entregas

{% apitags %}
Correo electrónico, notificación push web, push de iOS, push de Android, WhatsApp
{% endapitags %}

{% multi_lang_include metrics.md metric='Entregas' %} En el caso de los correos electrónicos, *las Entregas* son el número total de mensajes (Envíos) enviados y recibidos correctamente por las partes que pueden enviar correos electrónicos.

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Entregas</i>: Recuento</li>
        <li><i>% de entregas</i>: (Envíos - Rebotes) / (Envíos)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Fallos de entrega

{% apitags %}
SMS
{% endapitags %}

{% multi_lang_include metrics.md metric='Fallos en la entrega' %}

Ponte en contacto con <a href="/docs/braze_support/">el soporte de Braze</a> para que te ayude a comprender las razones de los fallos en la entrega.

<span class="calculation-line">Cálculo: (Envíos) - (Envíos al operador)</span>

{% endapi %}

{% api %}

### Direct Opens

{% apitags %}
Push de iOS
{% endapitags %}

{% multi_lang_include metrics.md metric='Direct Opens' %}

<span class="calculation-line">Cálculo: (Direct Opens) / (Entregas)</span>

{% endapi %}

{% api %}

### Envío por correo electrónico

{% apitags %}
Correo electrónico
{% endapitags %}

{% multi_lang_include metrics.md metric='Envío por correo electrónico' %}

<span class="calculation-line">Cálculo: Recuento</span>

{% endapi %}

{% api %}

### Errores

{% apitags %}
Webhook
{% endapitags %}

{% multi_lang_include metrics.md metric='Errores' %} Los errores se incluyen en el recuento de <i>Envíos</i>, pero no en el de <i>Destinatarios únicos</i>.

{% endapi %}

{% api %}

### Estimación de Aperturas Reales

{% apitags %}
Correo electrónico
{% endapitags %}

{% multi_lang_include metrics.md metric='Aperturas reales estimadas' %}

{% endapi %}

{% api %}

### Errores

{% apitags %}
WhatsApp
{% endapitags %}

{% multi_lang_include metrics.md metric='Fallos' %} Los fallos se incluyen en el recuento de <i>Envíos</i>, pero no en el de <i>Entregas</i>.</td>

<span class="calculation-line">Cálculo<i>(tasa de fallos</i>): (Fallos) / (Envíos)</span>

{% endapi %}

{% api %}

### Rebote duro

{% apitags %}
Correo electrónico
{% endapitags %}

{% multi_lang_include metrics.md metric='Hard Bounce' %} 

Cuando esto ocurre, Braze marca la dirección de correo electrónico como no válida, pero no actualiza el [estado de suscripción]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/) del usuario. Si un correo electrónico recibe un rebote duro, detendremos cualquier solicitud futura a esta dirección de correo electrónico.

{% endapi %}

{% api %}

### Ayuda

{% apitags %}
SMS
{% endapitags %}

{% multi_lang_include metrics.md metric='Ayuda' %} La respuesta a un usuario se mide cada vez que un usuario envía un mensaje entrante en las cuatro horas siguientes a la recepción de tu mensaje.

{% endapi %}

{% api %}

### Influenced Opens

{% apitags %}
Push iOS, Push Android
{% endapitags %}

{% multi_lang_include metrics.md metric='Influenced Opens' %}

<span class="calculation-line">Cálculo: (Influenced Opens) / (Entregas)</span>

{% endapi %}

{% api %}

### Ingresos del ciclo de vida

{% apitags %}
Tarjetas de contenido, correo electrónico, mensajes dentro de la aplicación, push web, push de iOS, push de Android, webhook, SMS, LINE
{% endapitags %}

{% multi_lang_include metrics.md metric='Ingresos de toda la vida' %}

{% endapi %}

{% api %}

### Valor de duración del ciclo de vida por usuario

{% apitags %}
Tarjetas de contenido, correo electrónico, mensajes dentro de la aplicación, push web, push de iOS, push de Android, webhook, SMS, LINE
{% endapitags %}

{% multi_lang_include metrics.md metric='Valor de duración del ciclo de vida por usuario' %}

{% endapi %}

{% api %}

### Ingresos medios diarios

{% apitags %}
Tarjetas de contenido, correo electrónico, mensajes dentro de la aplicación, push web, push de iOS, push de Android, webhook, SMS,LINE
{% endapitags %}

{% multi_lang_include metrics.md metric='Ingresos medios diarios' %}

{% endapi %}

{% api %}

### Compras diarias

{% apitags %}
Tarjetas de contenido, correo electrónico, mensajes dentro de la aplicación, push web, push de iOS, push de Android, webhook, SMS, LINE
{% endapitags %}

{% multi_lang_include metrics.md metric='Compras diarias' %}

{% endapi %}

{% api %}

### Ingresos diarios por usuario

{% apitags %}
Tarjetas de contenido, correo electrónico, mensajes dentro de la aplicación, push web, push de iOS, push de Android, webhook, SMS, LINE
{% endapitags %}

{% multi_lang_include metrics.md metric='Ingresos diarios por usuario' %}

{% endapi %}

{% api %}

### Machine Opens (Aperturas automáticas)

{% apitags %}
Correo electrónico
{% endapitags %}

{% multi_lang_include metrics.md metric='Máquina Abre' %} Esta métrica es objeto de seguimiento a partir del 11 de noviembre de 2021 para SendGrid y del 2 de diciembre de 2021 para SparkPost.

{% endapi %}

{% api %}

### Aperturas

{% apitags %}
Web Push, iOS Push, Android Push
{% endapitags %}

{% multi_lang_include metrics.md metric='Abre' %}

{% endapi %}

{% api %}

### Cancelación

{% apitags %}
SMS
{% endapitags %}

{% multi_lang_include metrics.md metric='Opt-Out' %} La respuesta a un usuario se mide cada vez que un usuario envía un mensaje entrante en las cuatro horas siguientes a la recepción de tu mensaje.

{% endapi %}

{% api %}

### Otras aperturas

{% apitags %}
Correo electrónico
{% endapitags %}

{% multi_lang_include metrics.md metric='Otras aperturas' %} Ten en cuenta que un usuario también puede abrir un correo electrónico (como las aperturas que cuentan para Otras aperturas) antes de que se registre un recuento de Aperturas de máquina. Si un usuario abre un correo electrónico una vez (o más) después de un evento de apertura de máquina desde un buzón de entrada que no es de Apple Mail, entonces la cantidad de veces que el usuario abre el correo electrónico se calcula para Otras aperturas y sólo una vez para Aperturas únicas.

{% endapi %}

{% api %}

### Pendiente de reintento

{% apitags %}
Correo electrónico
{% endapitags %}

{% multi_lang_include metrics.md metric='Reintento pendiente' %}

{% endapi %}

{% api %}

### Conversiones primarias (A) o evento de conversión primaria

{% apitags %}
Tarjetas de contenido, correo electrónico, mensajes dentro de la aplicación, Web Push, iOS Push, Android Push, Webhook, SMS, WhatsApp
{% endapitags %}

{% multi_lang_include metrics.md metric='Conversiones primarias (A) o evento de conversión primaria' %} En el caso del correo electrónico, push y webhooks, empezamos a hacer el seguimiento de las conversiones después del envío inicial. En el caso de las tarjetas de contenido y los mensajes dentro de la aplicación, este recuento comienza cuando ven una tarjeta de contenido o un mensaje por primera vez.

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Conversiones primarias (A) o evento de conversión primaria</i>: Recuento</li>
        <li><i>Conversiones primarias (A) %</i> o <i>tasa del evento de conversión primaria</i>: (Conversiones primarias) / (Destinatarios únicos)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Lecturas

{% apitags %}
WhatsApp
{% endapitags %}

{% multi_lang_include metrics.md metric='Lecturas' %}

{% endapi %}

{% api %}

### Recibido

{% apitags %}
Correo electrónico, tarjetas de contenido, mensajes dentro de la aplicación, notificación push web, push de iOS, push de Android, SMS, WhatsApp
{% endapitags %}

{% multi_lang_include metrics.md metric='Recibido' %} 

- Tarjetas de contenido: Se recibe cuando los usuarios ven la tarjeta en la aplicación.
- Push: Se recibe cuando los mensajes se envían desde el servidor Braze al proveedor push.
- Correo electrónico: Se recibe cuando los mensajes se envían desde el servidor Braze al proveedor de servicios de correo electrónico.
- SMS/MMS: "Entregado" después de que el proveedor de SMS reciba la confirmación del operador de origen y del dispositivo de destino.
- Mensaje en la aplicación: Recibido en el momento de la visualización en función de la acción de activación definida.
- WhatsApp: Recibido en el momento de la visualización en función de la acción de activación definida.

{% endapi %}

{% api %}

### Rechazos

{% apitags %}
SMS
{% endapitags %}

{% multi_lang_include metrics.md metric='Rechazos' %} Como cliente de Braze, los rechazos se cargan a tu asignación de SMS.

<span class="calculation-line">Cálculo: Recuento</span>

{% endapi %}

{% api %}

### Ingresos

{% apitags %}
Correo electrónico
{% endapitags %}

{% multi_lang_include metrics.md metric='Ingresos' %}

{% endapi %}

{% api %}

### Enviadas

{% apitags %}
SMS
{% endapitags %}

{% multi_lang_include metrics.md metric='Enviado' %}

<span class="calculation-line">Cálculo: Recuento</span>

{% endapi %}

{% api %}

### Envíos

{% apitags %}
Tarjetas de contenido, correo electrónico, mensaje dentro de la aplicación, notificación push web, push de iOS, push de Android, webhook, SMS, WhatsApp, LINE
{% endapitags %}

{% multi_lang_include metrics.md metric='Envíos' %} Esta métrica la proporciona Braze. Tenga en cuenta que al lanzar una campaña programada, esta métrica incluirá todos los mensajes enviados, independientemente de si se han enviado ya debido a la limitación de velocidad.

{% alert tip %}
Para las tarjetas de contenido, esta métrica se calcula de forma diferente dependiendo de lo que hayas seleccionado para la [creación de la tarjeta]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/):

- **En el lanzamiento o en la entrada escalonada:** El número de tarjetas creadas y disponibles para ver. Esto no cuenta si los usuarios vieron la tarjeta.
- **En la primera impresión:** El número de tarjetas mostradas a los usuarios.
{% endalert %}

<span class="calculation-line">Cálculo: Recuento</span>

{% endapi %}

{% api %}

### Mensajes enviados

{% apitags %}
Tarjetas de contenido, correo electrónico, mensaje dentro de la aplicación, notificación push web, push de iOS, push de Android, webhook, SMS, WhatsApp, LINE
{% endapitags %}

{% multi_lang_include metrics.md metric='Mensajes enviados' %} Esta métrica la proporciona Braze. Tenga en cuenta que al lanzar una campaña programada, esta métrica incluirá todos los mensajes enviados, independientemente de si se han enviado ya debido a la limitación de velocidad.

{% alert tip %}
Para las tarjetas de contenido, esta métrica se calcula de forma diferente dependiendo de lo que hayas seleccionado para la [creación de la tarjeta]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/):

- **En el lanzamiento o en la entrada escalonada:** El número de tarjetas creadas y disponibles para ver. Esto no cuenta si los usuarios vieron la tarjeta.
- **En la primera impresión:** El número de tarjetas mostradas a los usuarios.
{% endalert %}

<span class="calculation-line">Cálculo: Recuento</span>

{% endapi %}

{% api %}

### Envíos a operador

{% apitags %}
SMS
{% endapitags %}

{% multi_lang_include metrics.md metric='Envía al operador' %} 

<span class="calculation-line">Cálculo: Recuento</span>

{% endapi %}

{% api %}

### Rebote suave

{% apitags %}
Correo electrónico
{% endapitags %}

{% multi_lang_include metrics.md metric='Rebote blando' %} Si un correo electrónico recibe un rebote blando, normalmente lo reintentaremos en un plazo de 72 horas, pero el número de intentos de reintento varía de un receptor a otro.

{% endapi %}

{% api %}

### Correo no deseado

{% apitags %}
Correo electrónico
{% endapitags %}

{% multi_lang_include metrics.md metric='Correo no deseado' %}

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Correo no deseado</i>: Recuento</li>
        <li><i>% de correo no deseado</i> o <i>% de tasa de correo no deseado</i>: (Marcado como correo no deseado) / (Envía)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Descartes de página de cuestionario

{% apitags %}
Mensaje dentro de la aplicación
{% endapitags %}

{% multi_lang_include metrics.md metric='Página del cuestionario Despidos' %}

{% endapi %}

{% api %}

### Envío de cuestionarios

{% apitags %}
Mensaje dentro de la aplicación
{% endapitags %}

{% multi_lang_include metrics.md metric='Envíos de cuestionarios' %}

{% endapi %}

{% api %}

### Clics totales

{% apitags %}
Correo electrónico, tarjetas de contenido, SMS, LINE
{% endapitags %}

{% multi_lang_include metrics.md metric='Clics totales' %} En el caso de LINE, se realiza un seguimiento una vez alcanzado un umbral mínimo de 20 mensajes al día. Para los correos electrónicos AMP, es el total de clics en las versiones HTML y de texto sin formato.

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><b>Correo electrónico:</b> (Clics totales) / (Entregas)</li>
        <li><b>Tarjetas de contenido:</b> (Clics totales) / (Impresiones totales)</li>
        <li><b>SMS:</b> (Clics abiertos) / (Entregas)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Total de descartes

{% apitags %}
Tarjetas de contenido
{% endapitags %}

{% multi_lang_include metrics.md metric='Total de despidos' %}

<span class="calculation-line">Cálculo: Recuento</span>

{% endapi %}

{% api %}

### Impresiones totales

{% apitags %}
Mensaje en la aplicación, tarjetas de contenido
{% endapitags %}

{% multi_lang_include metrics.md metric='Impresiones totales' %} Esta cifra es la suma del número de eventos de impresión que Braze recibe de los SDK. Para las tarjetas de contenido, es el recuento total de impresiones registradas para una tarjeta de contenido determinada. Esto puede incrementarse varias veces para el mismo usuario.

Para los mensajes dentro de la aplicación, si hay varios dispositivos y la reelegibilidad está desactivada, el usuario sólo debería ver el mensaje dentro de la aplicación una vez. Aunque el usuario utilice varios dispositivos, sólo lo verá en el primer dispositivo al que se dirija. Esto supone que el perfil tiene dispositivos consolidados y que un usuario tiene un ID de usuario con el que ha iniciado sesión en todos los dispositivos. Si la reelegibilidad está activada, se registra una impresión cada vez que el usuario ve el mensaje dentro de la aplicación.

<span class="calculation-line">Cálculo: Recuento</span>

{% endapi %}

{% api %}

### Total de aperturas

{% apitags %}
Correo electrónico, push de iOS, push de Android, notificación push web, LINE
{% endapitags %}

{% multi_lang_include metrics.md metric='Aperturas totales' %} En el caso de LINE, se realiza un seguimiento una vez alcanzado un umbral mínimo de 20 mensajes al día. Para los correos electrónicos AMP, es el total de aperturas de las versiones HTML y en texto plano. 

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><b>Correo electrónico:</b> (Aperturas) / (Entregas)</li>
        <li><b>Notificación push web:</b> (Aperturas directas) / (Entregas)</li>
        <li><b>Push de iOS, Android y Kindle:</b> (Unique Opens) / (Entregas)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Ingresos totales

{% apitags %}
Tarjetas de contenido, correo electrónico, mensajes dentro de la aplicación, Web Push, iOS Push, Android Push, Webhook, SMS, WhatsApp
{% endapitags %}

{% multi_lang_include metrics.md metric='Ingresos totales' %} Esta métrica sólo está disponible en los Informes de Comparación de Campañas a través del <a href='https://braze.com/docs/user_guide/data_and_analytics/reporting/report_builder/'>generador de informes</a>

{% endapi %}

{% api %}

### Clics únicos

{% apitags %}
Correo electrónico, Tarjetas de contenido, LINE
{% endapitags %}

{% multi_lang_include metrics.md metric='Clics únicos' %} Se realiza un seguimiento durante un periodo de siete días para el correo electrónico. Esto incluye los clics en los enlaces de cancelación de suscripción proporcionados por Braze. En el caso de LINE, el seguimiento se realiza una vez alcanzado un umbral mínimo de 20 mensajes diarios.

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Clics únicos</i>: Recuento</li>
        <li><b>Tarjetas de contenido</b> <i>% de clics únicos</i> o <i>tasa de clics únicos</i>: (Clics únicos) / (Impresiones únicas)</li>
        <li><i>Porcentaje de clics únicos</i> <b>por correo electrónico</b> o <i>tasa de clics únicos</i>: (Clics únicos) / (Entregas)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Descartes únicos

{% apitags %}
Tarjetas de contenido
{% endapitags %}

{% multi_lang_include metrics.md metric='Despidos únicos' %}

<span class="calculation-line">Cálculo: (Descartes únicos) / (Impresiones únicas)</span>

{% endapi %}

{% api %}

### Impresiones únicas

{% apitags %}
Mensaje en la aplicación, tarjetas de contenido
{% endapitags %}

{% multi_lang_include metrics.md metric='Impresiones únicas' %} En el caso de los mensajes dentro de la aplicación, las impresiones únicas pueden incrementarse de nuevo al cabo de 24 horas si la reelecibilidad está activada y un usuario realiza la acción desencadenante. Si la reeligibilidad está activada, <i>Impresiones únicas</i> = <i>Destinatarios únicos</i>. <br><br>Para las tarjetas de contenido, el recuento no debe incrementarse la segunda vez que un usuario ve una tarjeta. 

<span class="calculation-line">Cálculo: Recuento</span>

{% endapi %}

{% api %}

### Aperturas únicas

{% apitags %}
Correo electrónico, LINE
{% endapitags %}

{% multi_lang_include metrics.md metric='Unique Opens' %} En el caso del correo electrónico, se realiza un seguimiento durante un periodo de 7 días. En el caso de LINE, el seguimiento se realiza una vez alcanzado un umbral mínimo de 20 mensajes diarios.

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Unique Opens</i>: Recuento</li>
        <li><i>Unique Opens %</i> o <i>tarifa abierta única</i>: (Unique Opens) / (Entregas)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Destinatarios únicos

{% apitags %}
Todo
{% endapitags %}

{% multi_lang_include metrics.md metric='Destinatarios únicos' %}

Dado que un espectador puede ser un destinatario único cada día, debes esperar que sea superior a <i>Impresiones únicas</i>. Este número se recibe de Braze y se basa en la dirección `user_id`.

<span class="calculation-line">Cálculo: Recuento</span>

{% endapi %}

{% api %}

### Cancelar suscripción o darse de baja

{% apitags %}
Correo electrónico
{% endapitags %}

{% multi_lang_include metrics.md metric='Cancelar suscripción o darse de baja' %}

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Cancelar suscripción</i> o <i>darse de baja</i>: Recuento</li>
        <li><i>Suscriptores %</i> o <i>tasa de cancelación de suscripciones</i>: (Cancelaciones de suscripción) / (Entregas)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Cancelaciones de suscripción

{% apitags %}
Correo electrónico
{% endapitags %}

{% multi_lang_include metrics.md metric='Anulaciones de suscripción' %}

<span class="calculation-line">Cálculo: (Cancelaciones) / (Entregas)</span>

{% endapi %}

{% api %}

### Variación

{% apitags %}
Tarjetas de contenido, correo electrónico, mensajes dentro de la aplicación, Web Push, iOS Push, Android Push, Webhook, SMS, WhatsApp
{% endapitags %}

{% multi_lang_include metrics.md metric='Variación' %}

<span class="calculation-line">Cálculo: Recuento</span>

{% endapi %}