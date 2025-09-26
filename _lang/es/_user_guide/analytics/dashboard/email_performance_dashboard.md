---
nav_title: Panel de rendimiento del canal
article_title: Panel de rendimiento del canal
page_order: 2
page_type: reference
description: "Este artículo de referencia cubre el Panel de Rendimiento de Canales, que le permite ver las métricas de rendimiento de canales enteros tanto en campañas como en Canvases."
tool: 
  - Reports

---

# Panel de rendimiento del canal

> Los paneles de rendimiento del canal muestran métricas de rendimiento agregadas de todo un canal, tanto de campañas como de Canvases. Estos paneles están actualmente disponibles para correo electrónico y SMS.

![Panel de rendimiento del correo electrónico que muestra la interacción del canal de correo electrónico en los últimos treinta días.]({% image_buster /assets/img_archive/email_performance_dashboard_1.png %})

Puedes ver los siguientes paneles:
- [Panel de rendimiento del correo electrónico](#email-performance-dashboard)
- [Panel de información de correo electrónico](#email-insights-dashboard)
- [Panel de rendimiento por SMS](#sms-performance-dashboard)

## Panel de rendimiento del correo electrónico

Para ver tu panel de rendimiento del correo electrónico, ve a **Análisis** > **Rendimiento del correo electrónico**, y selecciona el intervalo de fechas del periodo en el que deseas ver los datos. El intervalo de fechas puede ser de hasta un año en el pasado.

### Cómo se calculan las métricas

![]({% image_buster /assets/img_archive/email_performance_dashboard_2.png %}){: style="max-width:40%;float:right;margin-left:15px;border:none;"}

Los cálculos para las diferentes métricas en el panel de rendimiento del correo electrónico son los mismos que los que se realizan a nivel de mensaje individual (como los análisis de campaña). En este panel, las métricas se agregan a todas las campañas y Canvases para el intervalo de fechas que haya seleccionado. Para saber más sobre estas definiciones, consulta [Métricas del correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting#email-metrics).

Cada mosaico muestra primero la métrica de tasa, seguida de la métrica de recuento (con la excepción de *Envíos*, que muestra la métrica de recuento seguida de la media por día). Por ejemplo, el mosaico de clics únicos contiene la *tasa de clics únicos* del período de tiempo seleccionado y el recuento del número total de clics únicos de ese periodo de tiempo. Cada mosaico muestra también la [comparación con el último periodo](#comparison-to-last-period-change-in-totals-or-rates).

| Métrica | Tipo | Cálculo |
| --- | --- | ---- |
| Envíos | Recuento | Número total de envíos en cada día del intervalo de fechas |
| Tasa de entrega | Tasa | (Número total de entregas en cada día del intervalo de fechas) / (Número total de envíos en cada día del intervalo de fechas) |
| Tasa de rebote | Tasa | (Número total de rebotes en cada día del intervalo de fechas) / (Número total de envíos en cada día del intervalo de fechas) |
| Tasa de cancelaciones | Tasa | (Número total de bajas únicas en cada día del intervalo de fechas) / (Número total de entregas para un intervalo de fechas)<br><br>Esto utiliza cancelaciones de suscripción únicas, que también se utilizan en el análisis de campaña, el resumen y el generador de informes. Estas bajas se registran en todas las fuentes (como el SDK, la API REST, las importaciones CSV, los correos electrónicos y las bajas de listas). Las tasas de cancelación de suscripción en los análisis de Campaign y Canvas son las cancelaciones de suscripción que se producen como resultado de un clic de cancelación de suscripción en un correo electrónico entregado por Braze.  |
| Tasa de apertura única | Tasa | (Número total de aperturas únicas en cada día del intervalo de fechas) / (Número total de entregas para un intervalo de fechas) |
| Otra tasa de apertura | Tasa | (Número total de otras aperturas totales en cada día del intervalo de fechas) / (Número total de entregas para el intervalo de fechas)<br><br>Otras aperturas incluye correos electrónicos que no se han identificado como aperturas automáticas, como cuando un usuario abre un correo electrónico. Esta métrica no es única y es una submétrica del total de aperturas.  |
| Tasa de clics únicos | Tasa | (Número total de clics únicos en cada día del intervalo de fechas) / (Número total de entregas para un intervalo de fechas) |
| Tasa única de clics por apertura | Tasa | (Número total de clics únicos en cada día del intervalo de fechas) / (Número total de aperturas únicas en cada día del intervalo de fechas) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Panel de información de correo electrónico 

El panel de información sobre el correo electrónico hace un seguimiento de dónde y cuándo interactúan tus clientes con tus correos electrónicos. Estos informes pueden proporcionar datos ricos y detallados sobre cómo optimizar sus mensajes de correo electrónico para impulsar una mayor participación. El panel de información del correo electrónico incluye hasta los últimos seis meses de datos. Para acceder al panel, vaya a **Analytics** > **Email Performance** > **Email Insights**.

### Participación por dispositivo

El informe **Participación por dispositivo** ofrece un desglose de los dispositivos que utilizan los usuarios para interactuar con el correo electrónico. Estos datos hacen un seguimiento de la interacción del correo electrónico en móviles, escritorio, tabletas y otros tipos de dispositivos. Estos datos se basan en la cadena del agente de usuario transmitida desde los dispositivos de tus usuarios.

{% alert note %}
Si utilizas CloudFront como CDN, asegúrate de que el agente de usuario de tus usuarios se transmite al ESP. De lo contrario, todos los agentes de usuario serán "Amazon Cloudfront".
{% endalert %}

La categoría "Otros" incluye cualquier cadena de usuario que no pueda identificarse como ordenador de sobremesa, móvil o tableta. Por ejemplo, televisión, coche, consola de videojuegos, OTT (over-the-top o streaming) y similares. También puede incluir valores nulos o vacíos.

Para comprender mejor lo que hay en esta categoría "Otros", puedes extraer los agentes de usuario utilizando cualquiera de estas opciones:

1. [Currents]({{site.baseurl}}/user_guide/data/braze_currents) te enviará la cadena exacta del agente de usuario que se recuperó de los dispositivos de tus usuarios.
2. Aprovecha nuestro [Constructor de consultas]({{site.baseurl}}/user_guide/analytics/query_builder) para utilizar SQL o nuestro [Constructor de consultas AI]({{site.baseurl}}/user_guide/analytics/query_builder#generating-sql-with-the-ai-query-builder) para ver los agentes de usuario.

![Informe de interacción por dispositivo que muestra el número de clics para móvil, escritorio, tableta y otros. El mayor número de clics se produce en dispositivos móviles.]({% image_buster /assets/img/engagement_by_device_type.png %}){: style="max-width:70%;"}

Para las aperturas de correo electrónico, Braze separará Google Image Proxy, Apple Image Proxy y Yahoo Mail Proxy. Estos servicios almacenan en caché y cargan todas las imágenes incrustadas en un correo electrónico antes de entregarlo al destinatario. Como resultado, esto activará una apertura de correo electrónico desde los servidores del proveedor de buzones en lugar de desde el servidor del destinatario, lo que puede llevar a aperturas de correo electrónico infladas. Estos servicios están pensados para mejorar la privacidad, la seguridad, el rendimiento y la eficacia a la hora de cargar imágenes. Esto también puede contener aperturas reales de destinatarios, ya que estos servicios proxy enmascaran el agente de usuario, y nosotros categorizamos los datos proxy utilizando el agente de usuario.

![Informe de compromiso por dispositivo que muestra el número de clics para móvil, escritorio, tableta, proxy de privacidad de Apple, proxy de imagen de Google, proxy de correo de Yahoo y otros. El mayor número de aperturas se produce en dispositivos móviles.]({% image_buster /assets/img/engagement_by_device_type_proxy.png %}){: style="max-width:70%;"}

### Compromiso por proveedor de buzones

El informe **Compromiso por proveedor de buzón** muestra los principales proveedores de buzones que contribuyen a sus clics o aperturas. Puedes hacer clic en proveedores de buzones premier específicos para profundizar en dominios receptores concretos. Por ejemplo, si Microsoft aparece en este informe como uno de sus principales proveedores de buzones de correo métricos, puedes ver más detalles de sus dominios de recepción como "outlook.com", "hotmail.com", "live.com", y más.

![]({% image_buster /assets/img_archive/mailbox_provider_time_engagement.png %}){: style="max-width:70%;"}

### Hora de participación

El informe **Tiempo de interacción** muestra datos sobre el momento en que los usuarios interactúan con sus mensajes de correo electrónico. Esto puede ayudar a responder preguntas como qué día de la semana o a qué hora se produce la mayor participación de sus clientes. Con esta información, puede experimentar con el mejor día u hora para enviar sus mensajes y conseguir una mayor participación. Ten en cuenta que estas horas se basan en la zona horaria de tu empresa.

El informe de interacción **del Día de la** semana desglosa las aperturas o los clics por día de la semana. 

![]({% image_buster /assets/img_archive/time_engagement.png %})

El informe de interacción **Hora del día** desglosa las aperturas o clics por cada hora en una ventana de tiempo de 24 horas.

![]({% image_buster /assets/img_archive/time_engagement_day.png %})

Para obtener más información sobre el análisis de sus mensajes de correo electrónico, consulte [Informes de correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting/).

## Panel de rendimiento por SMS

Para utilizar tu panel de rendimiento de SMS, ve a **Análisis** > **Rendimiento de SMS** y selecciona el intervalo de fechas del periodo del que quieras ver los datos. El intervalo de fechas puede ser de hasta un año en el pasado.

### Cómo se calculan las métricas

![]({% image_buster /assets/img_archive/email_performance_dashboard_2.png %}){: style="max-width:40%;float:right;margin-left:15px;border:none;"}

Los cálculos para las diferentes métricas en el panel de rendimiento de SMS son los mismos que los que se realizan a nivel de mensaje individual (como los análisis de campaña). En este panel, las métricas se agregan a todas las campañas y Canvases para el intervalo de fechas que haya seleccionado. Para saber más sobre estas definiciones, consulta las [métricas SMS]({{site.baseurl}}/sms_mms_rcs_reporting/).

Cada mosaico muestra primero la métrica de tasa, seguida de la métrica de recuento (con la excepción de _Envíos_, que muestra la métrica de recuento seguida de la media por día). Cada mosaico muestra también la [comparación con el último periodo](#comparison-to-last-period-change-in-totals-or-rates).

| Métrica | Tipo | Cálculo |
| --- | --- | ---- |
| Envíos | Recuento | Número total de envíos en cada día del intervalo de fechas |
| Porcentaje de entregas confirmadas | Tasa | (Número total de entregas en cada día del intervalo de fechas) / (Número total de envíos en cada día del intervalo de fechas) |
| Porcentaje de entregas fallidas | Tasa | (Número total de fallos en cada día del intervalo de fechas) / (Número total de envíos en cada día del intervalo de fechas) |
| Tasa de rechazos | Tasa | (Número total de rechazos en cada día del intervalo de fechas) / (Número total de envíos en cada día del intervalo de fechas) |
| Tasa de clics | Tasa | (Número total de clics en cada día del intervalo de fechas) / (Número total de entregas en cada día del intervalo de fechas) |
| Total de adhesiones voluntarias | Tasa | Número total de solicitudes de mensajes entrantes en cada día del intervalo de fechas |
| Total de exclusiones voluntarias | Tasa | Número total de rechazos de mensajes entrantes en cada día del intervalo de fechas |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Filtros del cuadro de mandos

Puedes filtrar los datos de tu panel utilizando las siguientes opciones de filtrado:

- **Etiqueta:** Elige una etiqueta. Cuando se aplique, tu panel mostrará las métricas solo de la etiqueta seleccionada.
- **Canvas:** Elija hasta 10 lienzos. Cuando se aplique, el panel de control mostrará las métricas sólo de los lienzos seleccionados. Si selecciona primero un filtro de etiqueta, las opciones de filtros de lienzo sólo incluirán los lienzos que tengan la etiqueta seleccionada.
- **Campaña:** Elija hasta 10 campañas. Cuando se aplique, el panel de control mostrará las métricas sólo de las campañas seleccionadas. Si selecciona primero un filtro de etiqueta, las opciones de filtros de campaña sólo incluirán las campañas que tengan la etiqueta seleccionada.

![Opciones de filtrado en el panel de rendimiento del canal, donde puedes seleccionar una etiqueta y una lista de Lienzos por los que filtrar.]({% image_buster /assets/img_archive/dashboard_filters.png %})

## Comparar periodos de tiempo

El panel de rendimiento del canal compara automáticamente el periodo de tiempo que ha seleccionado en el intervalo de fechas con el periodo de tiempo anterior que totaliza el mismo número de días. Por ejemplo, si elige "Últimos 7 días" como intervalo de fechas en el cuadro de mandos, la comparación con el último período comparará las métricas de los últimos siete días con las de los siete días anteriores. Si selecciona un intervalo de fechas personalizado (por ejemplo, del 10 al 15 de mayo, que son seis días de datos), el panel comparará las métricas de esos días con las métricas del 4 al 9 de mayo.

La comparación es el cambio porcentual entre el último periodo y el actual, calculado tomando la diferencia entre los dos periodos y dividiéndola por la métrica del último periodo.

### Visualización de los cambios en los recuentos y tasas totales

Puede cambiar entre **Mostrar cambio en totales**, que compara los recuentos totales (como el número de correos electrónicos entregados) entre los dos períodos, y **Mostrar cambio en tasas**, que compara las tasas (como la tasa de entrega).

![Botones de radio para cambiar entre mostrar el cambio en los totales o el cambio en las tasas para el panel de rendimiento del canal.]({% image_buster /assets/img_archive/email_performance_dashboard_3.png %}){: style="max-width:60%"}

## Preguntas más frecuentes

### ¿Por qué mi panel de control muestra valores vacíos?

Existen varios escenarios que pueden conducir a valores vacíos para una métrica:

- Braze registró ceros para esa métrica concreta en el intervalo de fechas seleccionado.
- No has enviado ningún mensaje durante el intervalo de fechas seleccionado.
- Aunque había métricas como aperturas, clics o cancelaciones de suscripción para un intervalo de fechas seleccionado, no había entregas ni envíos. En este caso, Braze no calculará una métrica de tarifa.

Para ver más métricas, pruebe a ampliar el intervalo de fechas.

### ¿Por qué mi panel de control de correo electrónico muestra más Otras aperturas que Aperturas únicas?

Para la métrica de _Unique Opens_, Braze deduplicará las aperturas repetidas registradas por un usuario dado (tanto si incluyen _Aperturas de Máquina_ como _Otras Aperturas_) de forma que sólo se incremente una única _Unique Open_ si un usuario abre varias veces. Para _Otras aperturas_, Braze no desduplica.

<!---Temporarily hidden until functionality is added

## Empty values in your data

#### If a metric displays "0%" or "0"

This means Braze recorded zero for that particular metric during the time frame you've selected.

#### If a metric displays "N/A"

This means that while Braze recorded positive counts for a particular metric for the time frame you've selected, the denominator for the rate calculation (either sends or deliveries in most cases) was zero. This can occur when emails are sent out on one day and opens and clicks are recorded the following days if your selected time frame does not include the date the messages were sent.

#### If a metric displays "--"

This means Braze hasn't recorded any data for that metric during the time you selected. If you haven't set up or sent any emails yet, learn more about how to do so in our dedicated [Email]({{site.baseurl}}/user_guide/message_building_by_channel/email) section.

--->

