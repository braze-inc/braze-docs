## Ver análisis

Una vez que hayas lanzado tu campaña, puedes volver a la página de detalles de esa campaña para ver las métricas clave. Ve a la página **Campañas** y selecciona tu campaña para abrir la página de detalles.{% if include.channel != "banner" %} Para {% if include.channel == "Content Card" %}Tarjetas de contenido {% elsif include.channel == "banner" %}Banner {% elsif include.channel == "email" %}correo electrónico {% elsif include.channel == "in-app message" %}mensajes dentro de la aplicación {% elsif include.channel == "push" %}mensajes push {% elsif include.channel == "SMS" %}mensajes SMS {% elsif include.channel == "whatsapp" %}mensajes de WhatsApp {% elsif include.channel == "webhook" %}webhooks {% endif %}enviados en Canvas, consulta [los análisis de Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/).{% endif %}

{% alert tip %}
¿Buscas definiciones de los términos y métricas que aparecen en tu informe? Consulta nuestra
  {% if include.channel == "email" %}[Glosario de análisis de correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/analytics_glossary/)
  {% elsif include.channel == "banner" %}[Informe Glosario de métricas]({{site.baseurl}}/user_guide/data/report_metrics/) y filtrar por Banners.
  {% elsif include.channel == "Content Card" %}[Glosario de métricas de informes]({{site.baseurl}}/user_guide/data/report_metrics/) y filtrar por tarjetas de contenido.
  {% elsif include.channel == "in-app message" %}[Glosario de métricas de informes]({{site.baseurl}}/user_guide/data/report_metrics/) y filtrar por mensaje dentro de la aplicación.
  {% elsif include.channel == "push" %}[Glosario de métricas de informes]({{site.baseurl}}/user_guide/data/report_metrics/) y filtrar por Push.
  {% elsif include.channel == "SMS" %}[Glosario de métricas de informes]({{site.baseurl}}/user_guide/data/report_metrics/) y filtro por SMS/MMS y RCS.
  {% elsif include.channel == "whatsapp" %}[Glosario de métricas de informes]({{site.baseurl}}/user_guide/data/report_metrics/) y filtrar por WhatsApp.
  {% elsif include.channel == "webhook" %}[Glosario de métricas de informes]({{site.baseurl}}/user_guide/data/report_metrics/) y filtrar por webhook.{% endif %}
{% endalert %}

Desde la pestaña **Análisis de campaña**, puedes ver tus informes en una serie de paneles. Puede que veas más o menos de los que se enumeran en las secciones siguientes, pero cada uno tiene su propia utilidad.

### Detalles de la campaña

El panel **Detalles de la campaña** muestra un resumen de alto nivel de todo el rendimiento de tu campaña.
  {% if include.channel == "banner" %}Banner.
  {% elsif include.channel == "Content Card" %}Tarjeta de contenido.
  {% elsif include.channel == "email" %}correo electrónico.
  {% elsif include.channel == "in-app message" %}mensaje dentro de la aplicación.
  {% elsif include.channel == "push" %}mensaje push.
  {% elsif include.channel == "SMS" %}SMS, MMS y RCS.
  {% elsif include.channel == "whatsapp" %}Mensajes de WhatApp.
  {% elsif include.channel == "webhook" %}webhook.
  {% endif %}

Revisa este panel para ver métricas generales como el número de mensajes enviados al número de destinatarios, la tasa de conversión primaria y los ingresos totales generados por este mensaje. También puedes revisar la configuración de entrega, audiencia y conversión desde esta página.

{% if include.channel == "whatsapp" %}
{% alert note %}
El canal WhatsApp incluye la tasa de lectura. Esta métrica sólo se entrega a los usuarios que tienen activados los recibos de lectura, lo que puede variar.
{% endalert %}
{% endif %}

{% if include.channel == "Content Card" %}
![Panel de detalles de la campaña con un resumen de las métricas utilizadas para determinar el rendimiento de la campaña.]({% image_buster /assets/img/cc-campaign-details.png %})

{% elsif include.channel == "banner" %}
![Panel de detalles de la campaña con un resumen de las métricas utilizadas para determinar el rendimiento de la campaña.]({% image_buster /assets/img/banners/campaign_details.png %})

{% elsif include.channel == "email" %}
![Panel de detalles de la campaña con un resumen de las métricas utilizadas para determinar el rendimiento de la campaña.]({% image_buster /assets/img/campaign_details_email.png %})

{% elsif include.channel == "push" %}
![Panel de detalles de la campaña con un resumen de las métricas utilizadas para determinar el rendimiento de la campaña.]({% image_buster /assets/img/campaign_details_push.png %})

{% elsif include.channel == "SMS" %}
![Panel de detalles de la campaña con un resumen de las métricas utilizadas para determinar el rendimiento de la campaña.]({% image_buster /assets/img/campaign_details_sms.png %})

{% elsif include.channel == "in-app message" %}
![Panel de detalles de la campaña con un resumen de las métricas utilizadas para determinar el rendimiento de la campaña.]({% image_buster /assets/img/campaign_details_iam.png %})

En Canvas, verás el rendimiento de los mensajes dentro de la aplicación mapeado en el Canvas que has creado. Puedes utilizar el panel de control de la parte superior de la página para borrar otros tipos de mensajería (canales) y ver sólo los mensajes dentro de la aplicación en tu Canvas.

![]({% image_buster /assets/img/in-app_message_canvas_reporting.png %})

{% elsif include.channel == "webhook" %}
![Panel de detalles de la campaña con un resumen de las métricas utilizadas para determinar el rendimiento de la campaña.]({% image_buster /assets/img/campaign_details_webhook.png %})

{% endif %}

{% if include.channel == "Content Card" %}

#### Grupos de control {#cc-control-group}

Para medir el impacto de una tarjeta de contenido individual, puedes añadir un [grupo de control]({{site.baseurl}}/user_guide/intelligence/multivariate_testing/#step-4-choose-a-segment-and-distribute-your-users-across-variants) a una prueba A/B. El panel de **detalles de campaña** de nivel superior no incluye métricas de la variante Grupo de control.

{% elsif include.channel == "SMS" %}

#### Grupos de control {#sms-control-group}

Para medir el impacto de un mensaje SMS, MMS o RCS individual, puedes añadir un [grupo de control]({{site.baseurl}}/user_guide/intelligence/multivariate_testing/#step-4-choose-a-segment-and-distribute-your-users-across-variants) a una prueba A/B. El panel de **detalles de campaña** de nivel superior no incluye métricas de la variante Grupo de control.

{% elsif include.channel == "whatsapp" %}

#### Grupos de control {#whatsapp-control-group}

Para medir el impacto de un mensaje individual de WhatsApp, puedes añadir un [grupo de control]({{site.baseurl}}/user_guide/intelligence/multivariate_testing/#step-4-choose-a-segment-and-distribute-your-users-across-variants) a una prueba A/B. El panel de **detalles de campaña** de nivel superior no incluye métricas de la variante Grupo de control.

{% elsif include.channel == "webhook" %}

#### Grupos de control {#webhook-control-group}

Para medir el impacto de un mensaje de webhook individual, puedes añadir un [grupo de control]({{site.baseurl}}/user_guide/intelligence/multivariate_testing/#step-4-choose-a-segment-and-distribute-your-users-across-variants) a una prueba A/B. El panel de **detalles de campaña** de nivel superior no incluye métricas de la variante Grupo de control.

{% endif %}

#### cambios desde la última visualización

El número de actualizaciones de la campaña por parte de otros miembros de tu equipo se sigue mediante la métrica *Cambios desde la última vez que se vio* en la página de resumen de la campaña. Selecciona **Cambios desde la última vez que lo viste** para ver un registro de cambios de las actualizaciones del nombre de la campaña, la programación, las etiquetas, el mensaje, la audiencia, el estado de aprobación o la configuración de acceso del equipo. Para cada actualización, puedes ver quién la realizó y cuándo. Puedes utilizar este registro de cambios para auditar los cambios en tu campaña.

<!--
### Message Performance

The **Message Performance** panel outlines how well your message has performed across various dimensions. The metrics in this panel vary depending on your chosen messaging channel, and whether or not you are running a multivariate test. You can click on the <i class="fa fa-eye preview-icon"></i> **Preview** icon to view your message for each variant or channel.
-->
{% if include.channel == "Content Card" %}
### Rendimiento de la tarjeta de contenido

El panel de **rendimiento de la tarjeta de contenido** muestra el rendimiento de tu mensaje en varias dimensiones. Las métricas de este panel varían en función del canal de mensajería elegido y de si estás realizando o no una prueba multivariante. Puedes hacer clic en el icono <i class="fa fa-eye preview-icon"></i> **Vista previa** para ver tu mensaje para cada variante o canal.

![Análisis de rendimiento de los mensajes de la tarjeta de contenido]({% image_buster /assets/img/cc-message-performance.png %})

{% elsif include.channel == "email" %}
### Rendimiento del correo electrónico

El panel **Rendimiento del correo electrónico** muestra el rendimiento de tu mensaje en varias dimensiones. Las métricas de este panel varían en función del canal de mensajería elegido y de si estás realizando o no una prueba multivariante. Puedes hacer clic en el icono <i class="fa fa-eye preview-icon"></i> **Vista previa** para ver tu mensaje para cada variante o canal.

![Análisis del rendimiento de los mensajes electrónicos]({% image_buster /assets/img_archive/email_message_performance.png %})

{% elsif include.channel == "in-app message" %}
### Rendimiento de los mensajes dentro de la aplicación

El panel **Rendimiento de los mensajes dentro de la aplicación** muestra el rendimiento de tu mensaje en varias dimensiones. Las métricas de este panel varían en función del canal de mensajería elegido y de si estás realizando o no una prueba multivariante. Puedes hacer clic en el icono <i class="fa fa-eye preview-icon"></i> **Vista previa** para ver tu mensaje para cada variante o canal.

![Análisis del rendimiento de los mensajes dentro de la aplicación]({% image_buster /assets/img_archive/iam_message_performance.png %})

{% elsif include.channel == "push" %}
### Rendimiento de push

El panel de **rendimiento push** muestra el rendimiento de tu mensaje en varias dimensiones. Las métricas de este panel varían en función del canal de mensajería elegido y de si estás realizando o no una prueba multivariante. Puedes hacer clic en el icono <i class="fa fa-eye preview-icon"></i> **Vista previa** para ver tu mensaje para cada variante o canal.

![Análisis del rendimiento de los mensajes push]({% image_buster /assets/img_archive/push_message_performance.png %})

{% elsif include.channel == "SMS" %}
### SMS/MMS/RCS Rendimiento

El panel de **rendimiento deSMS/MMS/RCS ** muestra el rendimiento de tu mensaje en varias dimensiones. Las métricas de este panel varían en función del canal de mensajería elegido y de si estás realizando o no una prueba multivariante. Puedes hacer clic en el icono <i class="fa fa-eye preview-icon"></i> **Vista previa** para ver tu mensaje para cada variante o canal.

![SMS/MMS/RCS Panel de rendimiento que incluye una tabla de métricas para un grupo de control, la variante 1 y la variante 2.]({% image_buster /assets/img_archive/sms_message_performance.png %})

{% elsif include.channel == "banner" %}
### Rendimiento de los banners

El panel de **Rendimiento del anuncio** muestra el rendimiento de tu mensaje en varias dimensiones. Estas métricas varían en función de tu canal de mensajería y de si estás realizando o no una prueba multivariante.

![Panel de rendimiento de SMS/MMS que incluye una tabla de métricas para un grupo de control, la variante 1 y la variante 2.]({% image_buster /assets/img/banners/banner_performance.png %})

{% elsif include.channel == "webhook" %}
### Rendimiento de webhook

El panel **Rendimiento del webhook** muestra el rendimiento de tu mensaje en varias dimensiones. Las métricas de este panel varían en función del canal de mensajería elegido y de si estás realizando o no una prueba multivariante. Puedes hacer clic en el icono <i class="fa fa-eye preview-icon"></i> **Vista previa** para ver tu mensaje para cada variante o canal.

![Panel de rendimiento del webhook que incluye una tabla de métricas para un grupo de control y la variante 1.]({% image_buster /assets/img/webhook_message_performance.png %})

{% elsif include.channel == "whatsapp" %}
### Rendimiento de WhatsApp

El panel de **rendimiento de WhatsApp** muestra el rendimiento de tu mensaje en varias dimensiones. Las métricas de este panel varían en función del canal de mensajería elegido y de si estás realizando o no una prueba multivariante. Puedes hacer clic en el icono <i class="fa fa-eye preview-icon"></i> **Vista previa** para ver tu mensaje para cada variante o canal.

![Panel de rendimiento de WhatsApp que incluye una tabla de métricas para la variante 1.]({% image_buster /assets/img/whatsapp_message_performance.png %})

{% endif %}

Si quieres simplificar la vista, haz clic en <i class="fas fa-plus"></i> **Añadir/Eliminar columnas** y borra las métricas que desees. Por predeterminado, se muestran todas las métricas.

{% if include.channel == "email" %}

#### Mapas de calor

Con los mapas de calor, puedes ver el éxito de los distintos enlaces de una misma campaña de correo electrónico. En la sección **Análisis de mensajes**, ve al panel **Rendimiento del correo electrónico**. Selecciona **Vista previa y** mapa de calor para ver una vista previa de tu campaña de correo electrónico y el mapa de calor. También puedes seleccionar el hipervínculo del nombre de la variante para ver el mapa de calor.

En esta vista, puedes alternar la opción **Mostrar mapa de calor** para obtener una vista visual de tu correo electrónico que muestre la frecuencia general y la ubicación de los clics dentro de la duración de la campaña. En el panel **Tabla de enlaces por clics totales**, puedes ver todos los enlaces de tu campaña de correo electrónico y ordenarlos por clics totales. Esto puede proporcionar información adicional sobre por dónde navegan tus usuarios. Para guardar una copia del mapa térmico como referencia, selecciona el botón de descarga.

![Ejemplo de la página Vista previa y mapa de calor que incluye una campaña de correo electrónico, y un panel con ejemplos de alias de enlaces con sus clics totales.]({% image_buster /assets/img_archive/email_heatmap_example.png %})

#### Imágenes

Te sugerimos que habilites CORS en las URL de tus imágenes para evitar que se rompan en las previsualizaciones y exportaciones de mapas térmicos.

{% endif %}

{% if include.channel == "Content Card" %}

#### Métrica de la tarjeta de contenido

Aquí tienes un desglose de algunas métricas clave que puedes ver al revisar el rendimiento de tus mensajes. Para ver las definiciones completas de todas las métricas de las tarjetas de contenido, consulta el [Glosario de métricas de los informes]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/) y filtra por tarjetas de contenido.

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>Métrica</th>
            <th>Definición</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#messages-sent">Mensajes enviados</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Messages Sent' %} <br><br>
                Se calcula de forma diferente según lo que hayas seleccionado para 
                <a href="/docs/user_guide/message_building_by_channel/content_cards/create/card_creation/#differences-between-creating-cards-at-launch-or-entry-versus-at-first-impression">Creación de tarjetas</a>:<br><br>
                <ul>
                    <li><b>En el lanzamiento o en la entrada escalonada:</b> El número de tarjetas creadas y disponibles para ver. Esto no cuenta si los usuarios vieron la tarjeta.</li>
                    <li><b>En la primera impresión:</b> El número de tarjetas mostradas a los usuarios.</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#total-impressions">Impresiones totales</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Total Impressions' %} Puede incrementarse varias veces para el mismo usuario.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#unique-impressions">Impresiones únicas</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Unique Impressions' %} <span style="white-space: nowrap">Este recuento</span> no se incrementa la segunda vez que un usuario ve una tarjeta de contenido.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#unique-recipients">Destinatarios únicos</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Unique Recipients' %} <br><br> Para las tarjetas de contenido, cada tarjeta de contenido sólo puede recibirse una vez, por lo que ver la misma tarjeta de contenido una segunda vez, independientemente del día, no incrementará este recuento. Dado que un espectador puede ser un destinatario único cada día, debes esperar que sea superior a <i>Impresiones únicas</i>.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#unique-clicks">Clics únicos</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Unique Clicks' %} Incluye los clics en los enlaces de cancelar suscripción proporcionados por Braze.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#unique-dismissals">Despidos únicos</a></td>
            <td>{% multi_lang_include metrics.md metric='Unique Dismissals' %}</td>
        </tr>
    </tbody>
</table>

{% alert note %}
En cuanto a cómo se registran las impresiones, hay algunos matices entre Web, Android e iOS. En términos generales, Braze registra una impresión cuando se ve una tarjeta, es decir, después de que un usuario se desplace hasta la tarjeta de contenido específica en su fuente.
{% endalert %}

#### Destinatarios únicos frente a impresiones únicas

Hay algunas métricas disponibles que cubren la visibilidad de tu mensaje. Esto incluye _Mensajes enviados_, _Destinatarios únicos_ e _Impresiones únicas_. En particular, la diferencia entre _Destinatarios únicos_ e _Impresiones únicas_ puede ser un poco confusa. Utilicemos algunos ejemplos para comprender mejor estas métricas.

Digamos que hoy ves una tarjeta de contenido, mañana recibes una nueva tarjeta de la misma campaña y pasado mañana otra vez: se te contará como _Destinatario Único_ tres veces. Sin embargo, sólo se te contabilizará una _Impresión Única_. También estarás incluido en el número de _mensajes enviados_, ya que la tarjeta estaba disponible en tu dispositivo.

A modo de un ejemplo más, imagina que ves cinco _impresiones únicas_ en una campaña de tarjeta de contenido que muestra 150 000 _mensajes enviados_. Esto significa que la tarjeta se puso a disposición (en el backend) de una audiencia de 150 000 usuarios, pero solo los dispositivos de cinco usuarios realizaron todos los pasos siguientes después de que se produjera ese envío:

1. Has iniciado una sesión o la aplicación ha solicitado explícitamente una sincronización de tarjetas de contenido (o ambas cosas)
2. Navegado a la vista Tarjetas de contenido
3. SDK grabó una impresión y la registró en el servidor

Tus _Mensajes Enviados_ se refiere a las Tarjetas de Contenido disponibles para ser vistas, mientras que _Destinatarios Únicos_ se refiere a las Tarjetas de Contenido que fueron vistas realmente.

{% elsif include.channel == "banner" %}

### Métrica del banner

Éstas son las métricas clave que debes seguir al revisar el rendimiento de tu campaña de banners. Los clics y las impresiones de los banners se siguen automáticamente con el SDK. 

Para obtener las definiciones completas de todas las métricas de Banners, consulta el [Glosario de métricas de los informes]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/) y filtra por Banners.

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>Métrica</th>
            <th>Definición</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-impressions">Impresiones totales</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Total Impressions' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-impressions">Impresiones únicas</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Unique Impressions' %} <span style="white-space: nowrap">Cada usuario sólo se cuenta una vez.</span></td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-clicks">Clics totales</a></td>
            <td class="no-split"><i>Clics totales</i> es el número total (y el porcentaje) de usuarios que hicieron clic en el mensaje entregado, independientemente de si el mismo usuario hace clic varias veces.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-clicks">Clics únicos</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Unique Clicks' %} Cada usuario sólo se cuenta una vez.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#primary-conversions">Conversiones primarias</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Primary Conversions (A) or Primary Conversion Event' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-recipients">Destinatarios únicos</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Unique Recipients' %} <br><br> Dado que un espectador puede ser un destinatario único cada día, debes esperar que sea superior a <i>Impresiones únicas</i>.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#revenue">Ingresos</a></td>
            <td>{% multi_lang_include metrics.md metric='Revenue' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#confidence">Confianza</a></td>
            <td>{% multi_lang_include metrics.md metric='Confidence' %}</td>
        </tr>
    </tbody>
</table>

#### Destinatarios únicos frente a impresiones únicas

Hay algunas métricas disponibles que cubren la visibilidad de tu mensaje. Esto incluye _Mensajes enviados_, _Destinatarios únicos_ e _Impresiones únicas_. En particular, la diferencia entre _Destinatarios únicos_ e _Impresiones únicas_ puede ser un poco confusa. Utilicemos algunos ejemplos para comprender mejor estas métricas.

Supongamos que ves un banner hoy, mañana ves el mismo banner y pasado mañana vuelves a verlo: se te contará como _destinatario único_ tres veces. Sin embargo, sólo se te contabilizará una _Impresión Única_. También estarás incluido en el número de _mensajes enviados_, ya que la tarjeta estaba disponible en tu dispositivo.

Como otro ejemplo, supón que ves cinco _impresiones únicas_ en una campaña de banners que muestra 150.000 _mensajes enviados_. Esto significa que el Banner se puso a disposición (en el backend) de una audiencia de 150.000 usuarios, pero sólo los dispositivos de cinco usuarios realizaron todos los pasos siguientes después de que se produjera ese envío:

1. Has iniciado una sesión o la aplicación ha solicitado explícitamente una sincronización con Banner (o ambas cosas)
2. Navega a la vista Banners
3. SDK grabó una impresión y la registró en el servidor

Tus _Mensajes Enviados_ se refiere a los Banners disponibles para ser vistos, mientras que _Destinatarios Únicos_ se refiere a los Banners que fueron realmente vistos.

{% elsif include.channel == "email" %}

#### Métricas de correo electrónico

Aquí tienes algunas métricas clave específicas del correo electrónico que no verás en otros canales. Para ver las definiciones completas de todas las métricas de correo electrónico utilizadas en Braze, consulta nuestro [Glosario de análisis de correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/analytics_glossary/).

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>Métrica</th>
            <th>Definición</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-clicks">Clics únicos</a></td>
            <td class="no-split">
                {% multi_lang_include metrics.md metric='Unique Clicks' %} Se realiza un seguimiento durante un periodo de siete días para el correo electrónico y se mide por <a href='https://braze.com/docs/help/help_articles/data/dispatch_id/'>dispatch_id</a>. Esto incluye los clics en los enlaces para cancelar suscripción proporcionados por Braze. Esta cifra debe estar entre el 5-10%. ¡Todo lo que supere el 10% es excepcional!
            </td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-opens">Aperturas únicas</a></td>
            <td class="no-split">
                {% multi_lang_include metrics.md metric='Unique Opens' %} En el caso del correo electrónico, se realiza un seguimiento durante un periodo de 7 días. Esta cifra debe estar entre el 30-40%. ¡Todo lo que supere el 40% es excepcional!
            </td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#click-to-open-rate">Tasa de clics de apertura</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Click-to-Open Rate' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#spam">Tasa de correo no deseado</a></td>
            <td class="no-split">
                {% multi_lang_include metrics.md metric='Spam' %} Si esta métrica es superior a 0,08, podría ser una señal de que, o bien el texto de tu mensaje es demasiado vendedor, o bien deberías reconsiderar tus métodos de recogida de direcciones de correo electrónico (para confirmar que estás enviando mensajes a quienes están interesados en tu correspondencia).
            </td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unsubscribers-or-unsub">Cancelar suscripción o darse de baja</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Unsubscribers or Unsub' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#other-opens">Otras aperturas</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Other Opens' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#estimated-real-opens">Estimación de Aperturas reales</a></td>
            <td class="no-split"> {% multi_lang_include metrics.md metric='Estimated Real Opens' %} Para más detalles, consulta la sección siguiente.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#machine-opens">Machine Opens (Aperturas automáticas)</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Machine Opens' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#bounces">Rebotes</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Bounces' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#hard-bounce">Rebote duro</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Hard Bounce' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#soft-bounce">Rebote suave</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Soft Bounce' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#deferral">Aplazamiento</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Aplazamiento' %}</td>
        </tr>
    </tbody>
</table>

##### Aplazamientos

Diferido o aplazamiento es cuando un correo electrónico no se entregó inmediatamente, pero Braze volverá a intentar el correo electrónico durante un máximo de 72 horas después de este fallo de entrega temporal para maximizar las posibilidades de éxito en la entrega antes de que se detengan los intentos para esa campaña específica. Las razones típicas de los aplazamientos incluyen la limitación de la tasa de volumen de correo electrónico basada en la reputación por parte del proveedor de correo electrónico de entrada, problemas temporales de conectividad o errores de DNS.

_Los aplazamientos_ difieren de _los rebotes blandos_. Si no se entregó correctamente ningún correo electrónico durante este periodo de reintento, Braze enviará un evento de rebote blando por cada intento de envío de campaña. Antes del 25 de febrero de 2025, estos reintentos se contabilizaban como múltiples rebotes blandos para 1 envío de campaña.

Ten en cuenta que actualmente _los Aplazamientos_ sólo están disponibles utilizando las características Currents o Braze Snowflake (como Generador de consultas, Segmento SQL, Compartir datos Snowflake). Si quieres incluirlo en los análisis de campaña o de Canvas, [envía tus comentarios sobre el producto]({{site.baseurl}}/user_guide/administrative/access_braze/portal).

##### Estimación de la tarifa abierta real {#estimated-real-open-rate}

Esta estadística utiliza un modelo de análisis propio creado por Braze para reconstruir una estimación de la tarifa abierta única de la campaña como si las aperturas de máquina no existieran. Aunque recibimos etiquetas de aperturas *de máquina* en algunos eventos de apertura de remitentes de correo electrónico (véase más arriba), estas etiquetas a menudo pueden etiquetar aperturas reales como aperturas reales. En otras palabras, las *Otras aperturas* son probablemente una subestimación de las aperturas reales (por usuarios reales). En su lugar, Braze utiliza los datos de clics de cada campaña para deducir la tasa a la que los humanos reales abrieron el mensaje. Esto compensa varios mecanismos de apertura de máquinas, incluido el MPP de Apple.

_La tasa de apertura real estimada_ se calcula 36 horas después del inicio del envío del correo electrónico y se recalcula cada 24 horas a partir de entonces. Si una campaña se repite, la estimación se vuelve a calcular 36 horas después de que se produzca otro envío.

Normalmente se necesitan unos 10.000 correos electrónicos entregados para que la estadística se calcule correctamente, aunque ese número puede variar en función de la tasa de clics. Si no se puede calcular la estadística, la columna muestra "--".

###### Limitaciones

La tasa de apertura real estimada sólo está disponible en campañas, y no se informa de ella en Eventos actuales. Esta métrica sólo se calcula retroactivamente para las campañas activas lanzadas antes del 14 de noviembre de 2023.

{% elsif include.channel == "in-app message" %}

#### Métricas de mensajes dentro de la aplicación

Aquí tienes algunas métricas clave de los mensajes dentro de la aplicación que puedes ver en tus análisis. Para ver las definiciones completas de todas las métricas de mensajes dentro de la aplicación utilizadas en Braze, consulta nuestro [Glosario de métricas de informes]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/).

{% alert note %}
Los informes para los _clics del botón 1_ y _los clics del botón 2_ sólo funcionan cuando especificas el **identificador para informes** como "0" y "1" respectivamente en el mensaje dentro de la aplicación.

![El campo "Identificador para informes" con valor "0".]({% image_buster /assets/img/identifier_for_reporting.png %}){: style="max-width:50%;"}
{% endalert %}

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>Métrica</th>
            <th>Definición</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#body-clicks">Clics del cuerpo</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Body Clicks' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#button-1-clicks">Clics en botón 1</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Button 1 Clicks' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#button-2-clicks">Clics en botón 2</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Button 2 Clicks' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-impressions">Impresiones únicas</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Unique Impressions' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-impressions">Impresiones totales</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Total Impressions' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#conversions-b-c-d">Conversiones (B, C, D)</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Conversions (B, C, D)' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-conversions">Total de conversiones</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Total Conversions' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#conversion-rate">Tasa de conversión</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Conversion Rate' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#close-message">Cerrar mensaje</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Close Message' %}</td>
        </tr>
    </tbody>
</table>

{% elsif include.channel == "push" %}

#### Métricas push

Aquí tienes un desglose de algunas métricas clave que puedes ver al revisar el rendimiento de tus mensajes. Para ver las definiciones completas de todas las métricas push, consulta el [Glosario de métricas de los informes]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/) y filtra por push.

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>Métrica</th>
            <th>Descripción</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#bounces">Rebotes</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Bounces' %} Ver <a href="#bounced-push">Notificaciones push rebotadas</a>.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#direct-opens">Direct Opens</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Direct Opens' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#opens">Aperturas</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Opens' %}</td>
        </tr>
    </tbody>
</table>

> Los servicios de notificaciones push de Apple (APN) realizan un "gran esfuerzo" en la entrega de notificaciones. No pretende entregar datos a tu aplicación, sólo notificar al usuario que hay nuevos datos disponibles. La distinción importante es que mostraremos cuántos mensajes hemos entregado con éxito a los APN, no necesariamente cuántos APN hemos entregado con éxito a los dispositivos.

##### Seguimiento de cancelaciones de suscripción

Las cancelaciones de suscripción push no se incluyen como métrica en los análisis de campaña. Consulta [Seguimiento de las cancelaciones de suscripciones push]({{site.baseurl}}/help/help_articles/push/push_unsubscribes) para saber cómo hacer un seguimiento manual de esta métrica.

##### La comprensión se abre

Aunque _Direct Opens_ e _Influenced Opens_ incluyen la palabra "opens", en realidad son métricas diferentes. _Direct Opens_ se refiere a la apertura directa de una notificación push, como se indica en la tabla anterior. _Influenced Opens_ se refiere a la apertura de una aplicación, sin abrir una notificación push en un plazo de tiempo determinado tras recibirla. Por tanto, _Influenced Opens_ se refiere a las aperturas de la aplicación, no a las aperturas de las notificaciones push.

##### Por qué los envíos push pueden superar los destinatarios únicos

El número de _Envíos_ puede superar el número de _Destinatarios Únicos_ debido a las siguientes razones:

- **La reelegibilidad está en marcha:** Cuando se habilita la reelegibilidad en la configuración de tu campaña o Canvas, los usuarios que cumplan los criterios de segmento y entrega pueden recibir la misma notificación push varias veces. El resultado es un mayor número de envíos totales.
- **Los usuarios tienen varios dispositivos:** Si no se habilita la reelegibilidad, la diferencia puede explicarse porque los usuarios tienen varios dispositivos asociados a su perfil. Por ejemplo, un usuario puede tener un smartphone y una tableta, y la notificación push se envía a todos los dispositivos registrados. Cada entrega cuenta como un envío, pero sólo se registra un destinatario único.
- **Se asignan usuarios a varias aplicaciones:** Si los usuarios están asociados a más de una aplicación (como cuando prueban una aplicación nueva), pueden recibir la misma notificación push en cada aplicación. Esto contribuye a un mayor número de envíos.

##### Por qué se producen los rebotes {#bounced-push}

{% tabs %}
{% tab Servicio de notificación push de Apple %}

Los rebotes se producen en los servicios de notificaciones push de Apple (APN) cuando una notificación push intenta entregarse a un dispositivo que no tiene instalada la aplicación prevista. APN también tiene derecho a cambiar los tokens de los dispositivos arbitrariamente. Si intentas realizar un envío al dispositivo de un usuario en el que su token de notificaciones push ha cambiado entre el momento en que registramos previamente su token (como al principio de cada sesión, cuando registramos a un usuario para obtener un token push) y el momento del envío, se produciría un rebote.

Si un usuario desactiva push en la configuración de su dispositivo al abrir una aplicación posterior, el SDK detectará que se ha desactivado push y lo notificará a Braze. En este punto actualizaremos el estado de habilitación de push para que esté deshabilitado. Cuando un usuario discapacitado recibe una campaña push antes de tener una nueva sesión, la campaña se enviaría correctamente y aparecería como entregada. El push no rebotará para este usuario. Tras una sesión posterior, cuando intentas enviar un push al usuario, Braze ya sabe si tenemos un token de notificaciones push, por lo que no se envía ninguna notificación.

Las notificaciones push que caducan antes de la entrega no se consideran fallidas y no se registrarán como rebotadas.

{% endtab %}
{% tab Mensajería en la nube Firebase %}

Firebase Cloud Messaging (FCM) puede rebotar en tres casos:

| Escenario | Descripción |
| -- | -- |
| Aplicaciones desinstaladas | Cuando se intenta entregar un mensaje a un dispositivo y la aplicación prevista se desinstala en ese dispositivo, el mensaje se descartará y se invalidará el ID de registro del dispositivo. Cualquier intento futuro de mensajería con el dispositivo devolverá un error NotRegistered. |
| Copia de seguridad de la aplicación | Cuando se hace una copia de seguridad de una aplicación, su ID de registro podría dejar de ser válido antes de que se restaure la aplicación. En este caso, FCM dejará de almacenar el ID de registro de la aplicación y ésta dejará de recibir mensajes. Por ello, los ID de registro **no** deben guardarse cuando se hace una copia de seguridad de una aplicación. |
| Aplicación actualizada | Cuando se actualiza una aplicación, el ID de registro de la versión anterior puede dejar de funcionar. Como tal, una solicitud actualizada debe sustituir a su ID de registro existente. |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% endtabs %}


{% elsif include.channel == "SMS" %}

#### Métricas de SMS, MMS y RCS

Aquí tienes un desglose de algunas métricas clave que puedes ver al revisar el rendimiento de tus mensajes. Para ver las definiciones completas de todas las métricas de SMS, MMS y RCS, consulta el [Glosario de métricas del informe]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/) y filtra por SMS/MMS y RCS.

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>Métrica</th>
            <th>Definición</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#sent">Enviadas</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Sent' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#delivery-failures">Fallos de entrega</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Delivery Failures' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#confirmed-delivery">Entrega confirmada</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Confirmed Deliveries' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#rejections">Rechazos</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Rejections' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#opt-out">Cancelación</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Opt-Out' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#help">Ayuda</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Help' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-clicks">Clics totales</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Total Clicks' %}</td>
        </tr>
    </tbody>
</table>

{% elsif include.channel == "webhook" %}

#### Métricas del webhook

Aquí tienes algunas métricas clave de webhook que puedes ver en tus análisis. Para ver las definiciones completas de todas las métricas webhook utilizadas en Braze, consulta nuestro [Glosario de Métricas de Informe]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/).

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>Métrica</th>
            <th>Definición</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-recipients">Destinatarios únicos</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Unique Recipients' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#sends">Envíos</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Sends' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#errors">Errores</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Errors' %}</td>
        </tr>
    </tbody>
</table>

{% elsif include.channel == "whatsapp" %}

#### Métricas de WhatsApp

Aquí tienes algunas métricas clave de WhatsApp que puedes ver en tus análisis. Para ver las definiciones completas de todas las métricas de WhatsApp utilizadas en Braze, consulta nuestro [Glosario de métricas de informes]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/).

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>Métrica</th>
            <th>Definición</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#sends">Envíos</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Sends' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#deliveries">Entregas</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Deliveries' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#reads">Lecturas</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Reads' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#failures">Errores</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Failures' %}</td>
        </tr>
    </tbody>
</table>

#### Métricas de bloqueo e informes de usuarios finales

Se puede acceder a métricas adicionales a través del [panel del administrador de WhatsApp](https://www.facebook.com/business/help/683499390267496?content_id=NZUBj7XjkYjYuWx), aunque es necesario [confirmar tu acceso](https://www.facebook.com/business/help/218116047387456) para acceder a todas las informaciones disponibles. 

{% endif %}

### Rendimiento histórico

El panel **Rendimiento histórico** te permite ver las métricas del panel **Rendimiento de mensajes** como un gráfico a lo largo del tiempo. Utiliza los filtros de la parte superior del panel para modificar las estadísticas y los canales que aparecen en el gráfico. El intervalo de tiempo de este gráfico siempre reflejará el intervalo de tiempo especificado en la parte superior de la página. 

Para obtener un desglose día a día, haz clic en el menú hamburguesa de <i class="fas fa-bars"></i> y selecciona **Descargar CSV** para recibir una exportación CSV del informe.

![Un gráfico del panel Rendimiento histórico con estadísticas de ejemplo para un correo electrónico de febrero de 2021 a mayo de 2022.]({% image_buster /assets/img/cc-historical-performance.png %})

{% if include.channel == "in-app message" %}

{% alert note %}
Si seleccionas enviar sólo a usuarios que puedan ver la última versión Braze de mensajes dentro de la aplicación (Generación 3), tu **Audiencia** objetivo no se ajusta para reflejar tu elección.
{% endalert %}

{% endif %}

{% if include.channel == "SMS" %}

### Respuestas a palabras clave

El panel de **Respuestas a palabras clave** te muestra una cronología de las palabras clave entrantes con las que los usuarios respondieron tras recibir tu mensaje.  

![Nivel de campaña SMS/MMS/RCS Panel de respuestas de palabras clave que incluye un gráfico de líneas de la distribución de palabras clave a lo largo del tiempo, y una sección de categorías de palabras clave con casillas de verificación seleccionadas para Adhesión voluntaria, Exclusión voluntaria, Ayuda, Otros, Más y Coaching.]({% image_buster /assets/img/sms/keyword_responses.png %})

Aquí también puedes ver la distribución de la respuesta de cada categoría de palabras clave para determinar los próximos pasos para [reorientar]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns) y [crear un segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment) convenientemente.

![La tabla que hay debajo del gráfico de líneas tiene columnas para Categoría de palabras clave, Distribución de respuestas y Reorientación, donde se te da la opción de crear un segmento con la categoría de palabras clave.]({% image_buster /assets/img/sms/keyword_segments.png %})

{% endif %}

### Detalles del evento de conversión

El panel **Detalles del evento de conversión** te muestra el rendimiento de los eventos de conversión de tu campaña. Para más información, consulta [Eventos de conversión]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/#step-3-view-results).

![El panel de detalles del evento de conversión.]({% image_buster /assets/img/cc-conversion.png %})

### Correlación de conversión

El panel **Correlación de conversiones** te da información sobre qué atributos y comportamientos de los usuarios ayudan o perjudican los resultados que estableces para las campañas. Para más información, consulta [Correlación de la conversión]({{site.baseurl}}/user_guide/engagement_tools/testing/conversion_correlation/).

![El panel Correlación de la conversión con un análisis de los atributos y el comportamiento del usuario a partir del evento de conversión primaria - A.]({% image_buster /assets/img/convcorr.png %})

{% if include.channel == "whatsapp" %}

### Metaanálisis

Además de los análisis de Braze, se puede acceder a los análisis a nivel de plantilla en el administrador de WhatsApp Business. Para más información, consulta [la documentación de Meta.](https://www.facebook.com/business/help/218116047387456) 

{% endif %}

{% if include.channel == "SMS" %}

### Eventos SMS de Currents

Al igual que el correo electrónico, Braze recibe eventos a nivel de usuario relacionados con un mensaje SMS a medida que hace su recorrido hasta un usuario. Cualquier evento SMS entrante también se enviará como evento Currents a través del evento [SMS InboundReceived]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/#sms-inbound-received-events). Esto te permite realizar acciones adicionales o informes sobre los mensajes que envían tus usuarios fuera de la plataforma Braze. 

{% alert note %}
Los mensajes entrantes se truncan a partir de 1.600 caracteres.
{% endalert %}

{% endif %}

{% if include.channel != "whatsapp" %}

## Informe de retención

Los informes de retención te muestran las tasas a las que tus usuarios han realizado un evento de retención seleccionado a lo largo de periodos de tiempo en una campaña específica{% if include.channel != "banner" %} o Canvas{% endif %}. Para más información, consulta [Informes de retención]({{site.baseurl}}/user_guide/analytics/reporting/retention_reports/).

## Informe de embudo

El informe de embudo ofrece un informe visual que te permite analizar los recorridos que realizan tus clientes tras recibir una campaña{% if include.channel != "banner" %} o Canvas{% endif %}. Si tu campaña {% if include.channel != "banner" %}o Canvas {% endif %}utiliza un grupo de control o múltiples variantes, podrás comprender cómo las diferentes variantes han impactado en el embudo de conversión a un nivel más granular y optimizar basándote en estos datos.

Para más información, consulta [Informes de embudo]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/).

{% endif %}

