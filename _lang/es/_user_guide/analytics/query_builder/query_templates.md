---
nav_title: Plantillas de consulta
article_title: Plantillas del Generador de consultas
page_order: 1
page_type: reference
toc_headers: h2
description: "Este artículo de referencia enumera los tipos de informes que puedes crear utilizando datos Braze de Snowflake en el Generador de consultas."
tool: Reports
---

# Plantillas del Generador de consultas

> Accede a las plantillas [del Generador de informes]({{site.baseurl}}/user_guide/analytics/query_builder/) seleccionando **Plantilla de consulta** al crear un informe. Todas las plantillas muestran datos de hasta los últimos 60 días, pero puedes editar directamente ese y otros valores en el editor.<br><br>Para conocer las definiciones de las métricas que pueden aparecer en tus informes del Generador de consultas, consulta el [Glosario de métricas de los informes]({{site.baseurl}}/user_guide/data/report_metrics/) y filtra por el canal correspondiente.

## Plantillas de canales

<style>
table th:nth-child(1) {
    width: 30%;
}
table th:nth-child(2) {
    width: 70%;
}
table td {
    word-break: break-word;
}
</style>

| Nombre de la consulta | Descripción | 
| --- | --- | 
| Interacción con el canal e ingresos | Este informe muestra, para cada canal, todas las métricas de interacción (como aperturas y clics), ingresos, número de transacciones y precio medio. {::nomarkdown} <ul> <li> <i>Número de transacciones:</i> Número de eventos de compra </li> <li> <i>Precio medio:</i> Ingresos divididos por transacciones </li> </ul> {:/} \![]({% image_buster /assets/img_archive/channel_engagement_revenue.png %}) |
| Compras e ingresos por segmento | Este informe muestra las métricas de los mensajes enviados para un segmento específico. <br><br> Las métricas de compra son únicas a lo largo del periodo del informe. Un usuario puede generar como máximo una compra. Los ingresos tienen en cuenta todas las compras del periodo del informe. |
| Compras e ingresos por variantes o etapas, por segmento | Este informe muestra métricas de las variantes o pasos en Canvas de los mensajes enviados a cada segmento. <br><br> Las métricas de compra son únicas a lo largo del periodo del informe. Un usuario puede generar como máximo una compra. Los ingresos tienen en cuenta todas las compras del periodo del informe. |
| Mensajería superior/inferior para compras | Este informe muestra las métricas de compra de las campañas superiores o inferiores, los Canvases o los pasos en Canvas. Cada fila es una campaña, un Canvas o un paso en Canvas. Debes especificar si quieres mostrar los mejores o los peores rendimientos, y la métrica específica para la que quieres ejecutar este análisis (como *Compras únicas al recibir*, *Ingresos al recibir*, *Destinatarios únicos*). <br><br> Las filas de los informes de mayor rendimiento se ordenarán de mejor a peor, mientras que las filas de los informes de menor rendimiento se ordenarán de peor a mejor. |
{: .reset-td-br-1 .reset-td-br-2 }

## Plantillas de campaña

| Nombre de la consulta | Descripción | 
| --- | --- | 
| Ingresos de la campaña por país | Este informe muestra los ingresos por país de una campaña concreta. Para ejecutar este informe, debes especificar el identificador API de una campaña. Puedes encontrar el identificador API de una campaña en la parte inferior de la página de detalles de esa campaña. <br><br> Este informe muestra, para cada país, la cantidad de ingresos generados, el número de pedidos, el número de devoluciones, los ingresos netos y los ingresos brutos.<br><br> {::nomarkdown} <ul> <li> <i>Pedidos:</i> Número de eventos de compra </li> <li><i> Devuelve:</i> Número de actos de compra con ingresos negativos </li> <li><i> Ingresos netos:</i> Ingresos de todas las no devoluciones </li> <li><i> Ingresos brutos:</i> Ingresos que incluyen el valor de las devoluciones </li></ul>{:/} \![]({% image_buster /assets/img_archive/campaign_revenue_country.png %}){: style="max-width:70%;"} |
{: .reset-td-br-1 .reset-td-br-2 }

## Plantillas Canvas

| Nombre de la consulta | Descripción | 
| --- | --- | 
| Ingresos de Canvas por país | Este informe muestra los ingresos por país de un Canvas concreto. Para ejecutar este informe, debes especificar el identificador de la API de un Canvas. Puedes encontrar el identificador de la API de Canvas en **Analizar variantes**. <br><br> Este informe muestra, para cada país, la cantidad de ingresos generados, el número de pedidos, el número de devoluciones, los ingresos netos y los ingresos brutos.<br><br> {::nomarkdown} <ul> <li> <i>Pedidos:</i> Número de eventos de compra </li> <li><i> Devuelve:</i> Número de actos de compra con ingresos negativos </li> <li><i> Ingresos netos:</i> Ingresos de todas las no devoluciones </li> <li><i> Ingresos brutos:</i> Ingresos que incluyen el valor de las devoluciones </li></ul>{:/} \![]({% image_buster /assets/img_archive/canvas_revenue_country.png %}){: style="max-width:70%;"} |
{: .reset-td-br-1 .reset-td-br-2 }

## Plantillas de correo electrónico

| Nombre de la consulta | Descripción | 
| --- | --- | 
| Rebotes de correo electrónico por dominio | El número de rebotes por dominio de correo electrónico, desglosado en rebotes totales, rebotes duros y rebotes blandos. <br> \![]({% image_buster /assets/img_archive/query_builder_q4.png %}){: style="max-width:60%;"} |
| Métricas de entrega de correo electrónico por día | Este informe muestra métricas de los mensajes enviados cada día, como el número de correos electrónicos enviados, entregados, rebotados blandos y rebotados duros. <br><br> Todas las métricas son únicas a lo largo del periodo del informe. Por ejemplo, si un correo electrónico de bienvenida rebotó una vez el 21 de noviembre, dos veces el 22 de noviembre y nunca se entregó: {::nomarkdown} <ul><li> La métrica <i>Rebotes blandos</i> del 21 de noviembre aumenta en uno.</li><li> La métrica <i>Rebotes blandos</i> del 22 de noviembre no se ve afectada. </li></ul>{:/} \![]({% image_buster /assets/img_archive/email_delivery_day.png %})|
|  Métricas de interacción del correo electrónico por segmento | Este informe muestra métricas de los mensajes enviados a cada segmento, como el número de correos electrónicos enviados, entregados, rebotados blandos y rebotados duros. <br><br> Todas las métricas son únicas a lo largo del periodo del informe. Por ejemplo, si un correo electrónico de bienvenida rebotó una vez el 21 de noviembre, dos veces el 22 de noviembre y nunca se entregó: {::nomarkdown} <ul><li> La métrica <i>Rebotes blandos</i> del 21 de noviembre aumenta en uno. </li><li> La métrica <i>Rebotes blandos</i> del 22 de noviembre no se ve afectada.</li></ul>{:/} \![]({% image_buster /assets/img_archive/email_engagement_segment.png %}) |
| Métricas de interacción por correo electrónico para variantes o pasos, por segmento. | Este informe muestra métricas de las variantes o pasos en Canvas de los mensajes enviados a cada segmento. Estas métricas incluyen el número de correos electrónicos enviados, entregados, rebotados blandos y rebotados duros. <br><br> Todas las métricas son únicas a lo largo del periodo del informe. Por ejemplo, si un correo electrónico de bienvenida rebotó una vez el 21 de noviembre, dos veces el 22 de noviembre y nunca se entregó: {::nomarkdown} <ul><li> La métrica <i>Rebotes blandos</i> del 21 de noviembre aumenta en uno. </li> <li> La métrica <i>Rebotes blandos</i> del 22 de noviembre no se ve afectada.</li></ul> {:/} |
| Rendimiento del correo electrónico por país | Este informe muestra las siguientes métricas para cada país: envíos, tasa de apertura indirecta y tasa de apertura directa. El país es el país del usuario en el momento del envío push. <br><br> \![]({% image_buster /assets/img_archive/query_builder_q3.png %}) |
| Registros de cambios de la suscripción por correo electrónico | Este informe muestra las métricas que se registraron sobre el cambio de suscripción de cada usuario, como su dirección de correo electrónico, su estado de suscripción, la hora en que se cambió su estado y el Canvas o campaña asociados. |
| Adhesiones y exclusiones voluntarias de grupos de suscripción por correo electrónico | Este informe muestra el número de adhesiones voluntarias y exclusiones voluntarias de usuarios únicos de cualquier grupo de suscripción por correo electrónico de cada semana. <br><br> \![]({% image_buster /assets/img_archive/query_builder_q2.png %}){: style="max-width:70%;"} |
| URL de correo electrónico clicadas | Este informe muestra el número de clics que ha tenido cada enlace de un correo electrónico. Para ejecutar este informe, tendrás que especificar el identificador API de una campaña o Canvas. Puedes encontrar el identificador API de una campaña en la parte inferior de la página de detalles de esa campaña y el identificador API de Canvas en **Analizar variantes**. <br><br> Este informe muestra enlaces despersonalizados y un recuento de clics para cada enlace. Tu descarga en CSV incluirá los ID de usuario de todos los usuarios que hicieron clic, el enlace en el que hicieron clic y una marca de tiempo de cuándo hicieron clic. <br><br> *URL despersonalizadas:* URL sin etiquetas de Liquid. <br><br> \![]({% image_buster /assets/img_archive/query_builder_q5.png %}){: style="max-width:70%;"} |
| Mensajería superior/inferior para la interacción por correo electrónico | Este informe muestra las métricas de interacción por correo electrónico de las campañas superiores o inferiores, los Canvases o los pasos en Canvas. Debes especificar si quieres mostrar los mejores o los peores resultados, y la métrica específica para la que quieres realizar este análisis (como *Enviados*, *Rebotes blandos* y *Aperturas únicas*). <br><br> Las filas de los informes de mayor rendimiento se ordenarán de mejor a peor, mientras que las filas de los informes de menor rendimiento se ordenarán de peor a mejor. <br><br> \![]({% image_buster /assets/img_archive/top-bottom-email.png %}) |
{: .reset-td-br-1 .reset-td-br-2 }

## Plantillas móviles

| Nombre de la consulta | Descripción | 
| --- | --- | 
| Operadores de dispositivos | El número de usuarios por operador del dispositivo, como Verizon y T-Mobile. <br><br> \![]({% image_buster /assets/img_archive/device_carriers.png %}){: style="max-width:50%;"} |
| Modelos de dispositivos | El número de usuarios por modelo de dispositivo, como iPhone 15 Pro y Pixel 7. <br><br> \![]({% image_buster /assets/img_archive/device_models.png %}){: style="max-width:50%;"} |
| Sistemas operativos de los dispositivos | El número de usuarios por sistema operativo, como 17.4 y Android 14. <br><br> \![]({% image_buster /assets/img_archive/os_version.png %}){: style="max-width:50%;"} |
| Resoluciones de pantalla del dispositivo | El número de usuarios por resolución de pantalla del dispositivo, como 1179x2556 y 750x1334. <br><br> \![]({% image_buster /assets/img_archive/device_screen_resolutions.png %}){: style="max-width:40%;"} |
| Códigos de error SMS | Este informe muestra el tipo de error y el número de errores de cada código de error SMS. <br><br>\![]({% image_buster /assets/img_archive/sms_errors.png %}){: style="max-width:50%;"} |
| SMS Proporcionar Errores por usuario | Este informe muestra los códigos de error de los SMS de un usuario concreto. |
{: .reset-td-br-1 .reset-td-br-2 }

## Plantillas push

| Nombre de la consulta | Descripción | 
| --- | --- | 
| Rendimiento push por país | Este informe muestra las siguientes métricas para cada país: entregas, tarifa abierta y tasa de clics. El país es el país del usuario en el momento del envío del correo electrónico. <br><br> \![]({% image_buster /assets/img_archive/query_builder_q7.png %}){: style="max-width:70%;"} |
{: .reset-td-br-1 .reset-td-br-2 }

## Desglose por segmentos

| Nombre de la consulta | Descripción |
| -- | -- |
| Métricas de interacción del correo electrónico por segmento | Este informe muestra las métricas de rendimiento del correo electrónico desglosadas por segmento a nivel de campaña o Canvas. |
| Compras e ingresos por segmento | Este informe muestra las métricas de compra e ingresos desglosadas por segmento para una campaña o Canvas específico. |
| Mensajería superior/inferior para la interacción por correo electrónico | Este informe muestra las campañas, los Canvases o los pasos en Canvas que obtuvieron el rendimiento más alto o más bajo para una métrica de interacción por correo electrónico especificada.|
| Mensajería superior/inferior para compras | Este informe muestra las campañas, los Canvases o los pasos en Canvas con mayor o menor rendimiento para una métrica de compra o de ingresos especificada. |
| Rendimiento push por segmento | Este informe muestra las métricas push desglosadas por segmentos.|
{: .reset-td-br-1 .reset-td-br-2 }