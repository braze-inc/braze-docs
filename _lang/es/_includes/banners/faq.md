# Pancartas: Preguntas frecuentes

> Éstas son las respuestas a las preguntas más frecuentes sobre los Banners en Braze. Para más información general, consulta [Acerca de los banners]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners{% endif %}).

## ¿Cuándo aparecen las actualizaciones del Banner para los usuarios?

Los banners se actualizan con los datos más recientes cada vez que llamas al método de actualización, sin necesidad de reenviar o actualizar tu campaña de banners.

## ¿Cuántas colocaciones puedo solicitar en una sesión?

En una única solicitud de actualización, puedes solicitar un máximo de 10 colocaciones. Por cada uno que solicites, Braze te devolverá el Banner de mayor prioridad para el que el usuario sea elegible. Las solicitudes adicionales devolverán un error.

Para más información, consulta [Solicitudes de colocación]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners#requests{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners#requests{% endif %}).

## ¿Cuántas campañas de Banner pueden estar activas simultáneamente?

Cada espacio de trabajo puede albergar hasta 200 campañas de Banner activas. Si se alcanza este límite, tendrás que [archivar o desactivar]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/about_statuses/#changing-the-status) una campaña existente antes de crear una nueva.

## Para las campañas que comparten un emplazamiento, ¿qué Banner se muestra primero?

Si un usuario cumple los requisitos para varias campañas de Banner que comparten la misma ubicación, se mostrará el Banner con la prioridad más alta. Para más información, consulta [Prioridad del Banner]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners/#priority{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners#priority{% endif %}).

## ¿Puedo utilizar banners en mi fuente existente de tarjetas de contenido?

Los banners son diferentes de las tarjetas de contenido, lo que significa que no puedes utilizar banners y tarjetas de contenido en la misma fuente. Para sustituir las fuentes existentes de tarjetas de contenido por banners, tendrás que [crear ubicaciones en tu aplicación o sitio web]({{site.baseurl}}/developer_guide/banners/placements/).

## ¿Puedo desencadenar un banner en función de las acciones de los usuarios?

Aunque los banners no admiten [la entrega basada en acciones]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery), puedes dirigirte a los usuarios en función de sus acciones anteriores utilizando la segmentación y la prioridad.

Por ejemplo, para mostrar un Banner especial sólo a los usuarios que hayan completado un evento de `purchase`:
1. **Orientación:** En tu campaña, dirígete a un segmento de usuarios que hayan realizado el evento personalizado `purchase` al menos una vez.
2. **Prioridad:** Si tienes un Banner general para todos los usuarios y este Banner específico para los compradores que se dirigen a la misma ubicación, establece la prioridad del Banner específico en **Alta** y la del Banner general en **Media** o **Baja**.

Cuando el usuario inicia una nueva sesión o actualiza Banners después de realizar la acción, Braze evalúa su elegibilidad. Si coinciden con el segmento "Compra", se mostrará el Banner de alta prioridad.


## ¿Pueden los usuarios descartar manualmente un Banner?

No. Los usuarios no pueden rechazar manualmente los Banners. Sin embargo, puedes controlar la visibilidad del Banner gestionando la elegibilidad de los segmentos de usuarios. Cuando un usuario ya no cumpla los criterios de segmentación de una campaña de Banner, no volverá a verla en su próxima sesión.

Por ejemplo, si muestras un Banner promocional hasta que un usuario realice una compra, el registro de un evento como `purchase_completed` puede eliminar a ese usuario del segmento objetivo, ocultando de forma efectiva el Banner en sesiones posteriores.

## ¿Puedo exportar análisis de campañas de Banners utilizando la API de Braze?

Sí. Puedes utilizar el [endpoint`/campaigns/data_series` ]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/) para obtener datos sobre cuántas campañas de Banner fueron vistas, hicieron clic o se convirtieron.

## ¿Cuándo se segmenta a los usuarios?

Los usuarios se segmentan al inicio de la sesión. Si los segmentos segmentados de una campaña dependen de atributos personalizados, eventos personalizados u otros atributos de segmentación, deben estar presentes en el usuario al inicio de la sesión.

## ¿Cómo puedo componer Banners para garantizar la menor latencia?

Cuanto más sencilla sea la mensajería de tu Banner, más rápido se renderizará. Lo mejor es probar tu campaña de Banner con la latencia esperada para tu caso de uso. Por ejemplo, asegúrate de probar atributos Liquid como `catalog_items`.

## ¿Son compatibles todas las etiquetas de Liquid?

No. Sin embargo, la mayoría de las etiquetas de Liquid son compatibles con los mensajes de Banner, excepto `catalog_items` que se vuelve a renderizar utilizando la [etiqueta`:rerender` ]({{site.baseurl}}/user_guide/data/activation/catalogs/using_catalogs/#using-liquid).

## ¿Puedo capturar eventos de clic?

Los eventos de clic sólo se capturan si se establece una acción al hacer clic en un elemento `logClick` y se llama utilizando el [puente JS]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/html_in-app_messages/#javascript-bridge).
