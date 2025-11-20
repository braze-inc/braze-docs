---
nav_title: Panel de rendimiento del canal
article_title: Panel de rendimiento del canal
page_order: 2
page_type: reference
description: "Este artículo de referencia cubre el Panel de Rendimiento del Canal, que te permite ver las métricas de rendimiento de canales enteros, tanto en campañas como en Lienzos."
tool: 
  - Reports

---

# Panel de rendimiento del canal

> Los paneles de rendimiento del canal muestran métricas de rendimiento agregadas de todo un canal, tanto de campañas como de Canvases. Estos paneles están actualmente disponibles para correo electrónico y SMS.

\![Panel de rendimiento del correo electrónico que muestra la interacción del canal de correo electrónico de los últimos treinta días.]({% image_buster /assets/img_archive/email_performance_dashboard_1.png %})

Puedes ver los siguientes paneles:
- [Panel de rendimiento del correo electrónico](#email-performance-dashboard)
- [Panel de información de correo electrónico](#email-insights-dashboard)
- [Panel de rendimiento de SMS](#sms-performance-dashboard)

## Panel de rendimiento del correo electrónico

Para ver tu panel de rendimiento del correo electrónico, ve a **Análisis** > **Rendimiento del correo electrónico**, y selecciona el intervalo de fechas del periodo en el que deseas ver los datos. Tu intervalo de fechas puede ser de hasta un año en el pasado.

### Cómo se calculan las métricas

Un ejemplo de campaña de correo electrónico con 335.630 envíos, con una media de 11.187,667 al día.]({% image_buster /assets/img_archive/email_performance_dashboard_2.png %}){: style="max-width:40%;float:right;margin-left:15px;border:none;"}

Los cálculos de las distintas métricas del panel de rendimiento del correo electrónico son los mismos que los del nivel de mensaje individual (como los análisis de campaña). En este panel, las métricas se agregan a todas las campañas y Canvases para el intervalo de fechas que hayas seleccionado. Para saber más sobre estas definiciones, consulta [Métricas del correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting#email-metrics).

Cada mosaico muestra primero la métrica de tasa, seguida de la métrica de recuento (a excepción de *los Envíos*, que muestra la métrica de recuento seguida de la media por día). Por ejemplo, el mosaico de clics únicos contiene la *tasa de clics únicos* de tu periodo de tiempo seleccionado y el recuento del número total de clics únicos de ese periodo de tiempo. Cada ficha muestra también la [comparación con el último periodo](#comparing-time-periods).

| Métrica | Tipo | Cálculo |
| --- | --- | ---- |
| Envía | Cuenta | Número total de envíos en cada día del intervalo de fechas |
| Tasa de entrega | Tasa | (Número total de entregas en cada día del intervalo de fechas) / (Número total de envíos en cada día del intervalo de fechas) |
| Tasa de rebote | Tasa | (Número total de rebotes en cada día del intervalo de fechas) / (Número total de envíos en cada día del intervalo de fechas) |
| Tasa de cancelación de suscripciones | Tasa | (Número total de cancelaciones de suscripción únicas en cada día del intervalo de fechas) / (Número total de entregas para un intervalo de fechas)<br><br>Esto utiliza cancelaciones de suscripción únicas, que también se utilizan en el análisis de campaña, el resumen y el generador de informes. Estas bajas se registran en todas las fuentes (como el SDK, la API REST, las importaciones CSV, los correos electrónicos y las bajas de listas). Las tasas de cancelación de suscripción en los análisis de Campaign y Canvas son las cancelaciones de suscripción que se producen como resultado de un clic de cancelación de suscripción en un correo electrónico entregado por Braze.  |
| Tasa de apertura única | Tasa | (Número total de aperturas únicas en cada día del intervalo de fechas) / (Número total de entregas para un intervalo de fechas) |
| Otras tarifas abiertas | Tasa | (Número total de otras aperturas totales en cada día del intervalo de fechas) / (Número total de entregas para el intervalo de fechas)<br><br>Otras aperturas incluye correos electrónicos que no se han identificado como aperturas de máquina, como cuando un usuario abre un correo electrónico. Esta métrica no es única y es una submétrica del total de aperturas.  |
| Tasa de clics única | Tasa | (Número total de clics únicos a lo largo de cada día en el intervalo de fechas) / (Número total de entregas para un intervalo de fechas) |
| Tasa única de clics por apertura | Tasa | (Número total de clics únicos en cada día del intervalo de fechas) / (Número total de aperturas únicas en cada día del intervalo de fechas) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Panel de información de correo electrónico 

El panel de información sobre el correo electrónico hace un seguimiento de dónde y cuándo interactúan tus clientes con tus correos electrónicos. Estos informes pueden proporcionar datos ricos y detallados sobre cómo optimizar tus envíos de correo electrónico para conseguir una mayor interacción. El panel de información del correo electrónico incluye hasta los últimos seis meses de datos. Para acceder al panel, ve a **Análisis** > **Rendimiento del correo electrónico** > Información sobre el correo electrónico **.**

### Interacción por dispositivo

El informe de **interacción por dispositivo** proporciona un desglose de los dispositivos que utilizan tus usuarios para interactuar con tu correo electrónico. Estos datos hacen un seguimiento de la interacción del correo electrónico en móviles, ordenadores de sobremesa, tabletas y otros tipos de dispositivos. Estos datos se basan en la cadena del agente de usuario transmitida desde los dispositivos de tus usuarios.

{% alert note %}
Si utilizas CloudFront como CDN, asegúrate de que el agente de usuario de tus usuarios se transmite al ESP. De lo contrario, todos los agentes de usuario serán "Amazon Cloudfront".
{% endalert %}

La categoría "Otros" incluye cualquier cadena de usuario que no pueda identificarse como ordenador de sobremesa, móvil o tableta. Por ejemplo, televisión, coche, consola de videojuegos, OTT (over-the-top o streaming) y similares. También puede incluir valores nulos o vacíos.

Para comprender mejor lo que hay en esta categoría "Otros", puedes extraer los agentes de usuario utilizando cualquiera de estas opciones:

1. [Currents]({{site.baseurl}}/user_guide/data/braze_currents) te enviará la cadena exacta del agente de usuario que se obtuvo de los dispositivos de tus usuarios.
2. Aprovecha nuestro [Constructor]({{site.baseurl}}/user_guide/analytics/query_builder) [de consultas]({{site.baseurl}}/user_guide/analytics/query_builder#generating-sql-with-the-ai-query-builder) para utilizar SQL o nuestro [Constructor de consultas AI]({{site.baseurl}}/user_guide/analytics/query_builder#generating-sql-with-the-ai-query-builder) para ver los agentes de usuario.

\![Informe de interacción por dispositivo que muestra el número de clics para móvil, ordenador de sobremesa, tableta y otros dispositivos. El mayor número de clics se produce en dispositivos móviles.]({% image_buster /assets/img/engagement_by_device_type.png %}){: style="max-width:70%;"}

Para la apertura de correo electrónico, Braze separará Google Image Proxy, Apple Image Proxy y Yahoo Mail Proxy. Estos servicios almacenarán en caché y cargarán todas las imágenes incrustadas en un correo electrónico antes de entregarlo al destinatario. Como resultado, esto desencadenará una apertura de correo electrónico desde los servidores del proveedor de buzones en lugar de desde el servidor del destinatario, lo que puede llevar a aperturas de correo electrónico infladas. Estos servicios están pensados para mejorar la privacidad, la seguridad, el rendimiento y la eficacia al cargar imágenes. Esto también puede contener aperturas reales de destinatarios, ya que estos servicios proxy enmascaran el agente de usuario, y nosotros categorizamos los datos de proxy utilizando el agente de usuario.

\![Informe de interacción por dispositivo que muestra el número de clics para móvil, ordenador de sobremesa, tableta, proxy de privacidad de Apple, proxy de imagen de Google, proxy de correo de Yahoo y otros. El mayor número de aperturas se produce en dispositivos móviles.]({% image_buster /assets/img/engagement_by_device_type_proxy.png %}){: style="max-width:70%;"}

### Interacción del proveedor de buzones

El informe de **interacción por proveedor** de buzones muestra los principales proveedores de buzones que contribuyen a tus clics o aperturas. Puedes hacer clic en proveedores de buzones premier específicos para profundizar en dominios receptores concretos. Por ejemplo, si Microsoft aparece en este informe como una de las métricas principales de tu proveedor de dominios, puedes ver más detalles de sus dominios receptores, como "outlook.com", "hotmail.com", "live.com", y más.

\![Un ejemplo de informe de interacción por proveedor de buzón con Google, Apple iCloud, Yahoo, Microsoft y Mail.Ru Group y su correspondiente número de clics.]({% image_buster /assets/img_archive/mailbox_provider_time_engagement.png %}){: style="max-width:70%;"}

### Tiempo de interacción

El informe **Tiempo de interacción** muestra datos sobre el momento en que los usuarios interactúan con tus correos electrónicos. Esto puede ayudar a responder preguntas como qué día de la semana o a qué hora hay más interacción con tus clientes. Con esta información, puedes experimentar con el mejor día u hora para enviar tus mensajes y conseguir una mayor interacción. Ten en cuenta que estas horas se basan en la zona horaria de tu empresa.

El informe de interacción **del Día de la** semana desglosa las aperturas o clics por día de la semana. 

\![Un ejemplo de informe de interacción del día de la semana con el mayor número de clics el lunes y el miércoles.]({% image_buster /assets/img_archive/time_engagement.png %})

El informe de interacción **Hora del día** desglosa las aperturas o clics por cada hora en una ventana de tiempo de 24 horas.

\![Un ejemplo de informe de interacción de la hora del día con las aperturas o clics desde las 12 de la mañana hasta las 11 de la noche.]({% image_buster /assets/img_archive/time_engagement_day.png %})

Para más información sobre el análisis de tus correos electrónicos, consulta [Informes de correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting/).

## Panel de rendimiento de SMS

Para utilizar tu panel de rendimiento de SMS, ve a **Análisis** > **Rendimiento de SMS**, y selecciona el intervalo de fechas del periodo en el que quieres ver los datos. Tu intervalo de fechas puede ser de hasta un año en el pasado.

### Cómo se calculan las métricas

\![Un ejemplo de campaña SMS con 335.630 envíos, con una media de 11.187,667 al día.]({% image_buster /assets/img_archive/email_performance_dashboard_2.png %}){: style="max-width:40%;float:right;margin-left:15px;border:none;"}

Los cálculos de las distintas métricas del panel de rendimiento de los SMS son los mismos que los de un nivel de mensaje individual (como los análisis de campaña). En este panel, las métricas se agregan a todas las campañas y Canvases para el intervalo de fechas que hayas seleccionado. Para saber más sobre estas definiciones, consulta las [métricas SMS]({{site.baseurl}}/sms_mms_rcs_reporting/).

Cada mosaico muestra primero la métrica de tasa, seguida de la métrica de recuento (a excepción de _los Envíos_, que muestra la métrica de recuento seguida de la media por día). Cada ficha muestra también la [comparación con el último periodo](#comparison-to-last-period-change-in-totals-or-rates).

| Métrica | Tipo | Cálculo |
| --- | --- | ---- |
| Envía | Cuenta | Número total de envíos en cada día del intervalo de fechas |
| Tasa de entregas confirmadas | Tasa | (Número total de entregas en cada día del intervalo de fechas) / (Número total de envíos en cada día del intervalo de fechas) |
| Tasa de fallos en la entrega | Tasa | (Número total de fallos en cada día del intervalo de fechas) / (Número total de envíos en cada día del intervalo de fechas) |
| Tasa de rechazos | Tasa | (Número total de rechazos en cada día del intervalo de fechas) / (Número total de envíos en cada día del intervalo de fechas) |
| Tasa de clics | Tasa | (Número total de clics en cada día del intervalo de fechas) / (Número total de entregas en cada día del intervalo de fechas) |
| Total de adhesiones voluntarias | Tasa | Número total de adhesiones voluntarias a mensajes entrantes cada día en el intervalo de fechas |
| Total de adhesiones voluntarias | Tasa | Número total de exclusiones voluntarias de mensajes entrantes en cada día del intervalo de fechas |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Filtros del panel de instrumentos

Puedes filtrar los datos de tu panel utilizando las siguientes opciones de filtrado:

- **Etiqueta:** Elige una etiqueta. Cuando se aplique, tu panel mostrará las métricas sólo de la etiqueta seleccionada.
- **Canvas:** Elige hasta 10 lienzos. Cuando se aplique, tu panel mostrará métricas sólo para tus Lienzos seleccionados. Si seleccionas primero un filtro de etiquetas, tus opciones de filtros de Canvas sólo incluirán los lienzos que tengan la etiqueta seleccionada.
- **Campaña:** Elige hasta 10 campañas. Cuando se aplique, tu panel mostrará las métricas sólo de las campañas seleccionadas. Si seleccionas primero un filtro de etiquetas, tus opciones para filtrar campañas sólo incluirán campañas que tengan la etiqueta seleccionada.

\![Opciones de filtrado en el panel de rendimiento del canal, donde puedes seleccionar una etiqueta y una lista de lienzos por los que filtrar.]({% image_buster /assets/img_archive/dashboard_filters.png %})

## Comparar periodos de tiempo

El panel de rendimiento del canal compara automáticamente el periodo de tiempo que has seleccionado en el intervalo de fechas con el periodo de tiempo anterior, totalizando el mismo número de días. Por ejemplo, si eliges "Últimos 7 días" como intervalo de fechas en el panel, la comparación con el último periodo comparará las métricas de los últimos siete días con las de los siete días anteriores. Si seleccionas un intervalo de fechas personalizado -digamos del 10 al 15 de mayo, que son seis días de datos-, el panel comparará las métricas de esos días con las métricas del 4 al 9 de mayo.

La comparación es el cambio porcentual entre el último periodo y el actual, calculado tomando la diferencia entre los dos periodos y dividiéndola por la métrica del último periodo.

### Visualización de los cambios en los recuentos y tasas totales

Puedes cambiar entre **Mostrar** **cambio en** **totales -que**compara los recuentos totales (como el número de correos electrónicos entregados) entre los dos periodos- y **Mostrar cambio en tasas -que**compara las tasas (como la tasa de entrega)-.

Botones de radio para cambiar entre mostrar el cambio en los totales o el cambio en las tasas para el panel de rendimiento del canal.]({% image_buster /assets/img_archive/email_performance_dashboard_3.png %}){: style="max-width:60%"}

## Preguntas más frecuentes

### ¿Por qué mi panel muestra valores vacíos?

Hay varias situaciones que pueden dar lugar a valores vacíos para una métrica:

- Braze los ceros registrados para esa métrica concreta en el intervalo de fechas que hayas seleccionado.
- No has enviado ningún mensaje durante el intervalo de fechas seleccionado.
- Aunque había métricas como aperturas, clics o cancelaciones de suscripción para un intervalo de fechas seleccionado, no había entregas ni envíos. En este caso, Braze no calculará una métrica de tasa.

Para ver más métricas, prueba a ampliar el intervalo de fechas.

### ¿Por qué mi panel de correo electrónico muestra más Otras aperturas que Aperturas únicas?

Para la métrica de _Aperturas Únicas_, Braze deduplicará las aperturas repetidas registradas por un usuario determinado (tanto si incluyen _Aperturas de Máquina_ como _Otras Aperturas_), de modo que sólo se incremente una única _Apertura Única_ si un usuario abre varias veces. Para _Otras Aperturas_, Braze no desduplica.

<!---Temporarily hidden until functionality is added

## Empty values in your data

#### If a metric displays "0%" or "0"

This means Braze recorded zero for that particular metric during the time frame you've selected.

#### If a metric displays "N/A"

This means that while Braze recorded positive counts for a particular metric for the time frame you've selected, the denominator for the rate calculation (either sends or deliveries in most cases) was zero. This can occur when emails are sent out on one day and opens and clicks are recorded the following days if your selected time frame does not include the date the messages were sent.

#### If a metric displays "--"

This means Braze hasn't recorded any data for that metric during the time you selected. If you haven't set up or sent any emails yet, learn more about how to do so in our dedicated [Email]({{site.baseurl}}/user_guide/message_building_by_channel/email) section.

--->

