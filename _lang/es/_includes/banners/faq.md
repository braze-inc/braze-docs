# Banners: Preguntas frecuentes

> Estas son las respuestas a las preguntas más frecuentes sobre los banners en Braze. Para obtener información más general, consulta [Acerca de los banners]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners{% endif %}).

## ¿Cuándo aparecen las actualizaciones de Banner para los usuarios?

Los banners se actualizan con los datos más recientes cada vez que llamas al método de actualización, por lo que no es necesario reenviar ni actualizar tu campaña de banners.

## ¿Cuántas colocaciones puedes solicitar en una sesión?

En una sola solicitud de actualización, puedes solicitar un máximo de 10 ubicaciones. Por cada solicitud que realices, Braze devolverá el banner con mayor prioridad al que sea elegible el usuario. Las solicitudes adicionales devolverán un error.

Para obtener más información, consulta [Solicitudes de colocación]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners#requests{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners#requests{% endif %}).

## ¿Cuántas campañas de banners pueden estar activas simultáneamente?

Cada espacio de trabajo puede admitir hasta 200 campañas activas de Banner. Si se alcanza este límite, tendrás que [archivar o desactivar]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/about_statuses/#changing-the-status) una campaña existente antes de crear una nueva.

## En las campañas que comparten una ubicación, ¿qué banner se muestra primero?

Si un usuario cumple los requisitos para varias campañas de banners que comparten la misma ubicación, se mostrará el banner con mayor prioridad. Para obtener más información, consulta [Prioridad de los ]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners/#priority{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners#priority{% endif %})banners.

## ¿Puedo utilizar banners en tu fuente de tarjetas de contenido existente?

Los banners son diferentes de las tarjetas de contenido, lo que significa que no puedes usar banners y tarjetas de contenido en la misma fuente. Para sustituir las fuentes de tarjetas de contenido existentes por banners, tendrás que [crear ubicaciones en tu aplicación o sitio web]({{site.baseurl}}/developer_guide/banners/placements/).

## ¿Puedo desencadear un banner basado en las acciones del usuario?

Aunque los banners no admiten [la entrega basada en acciones]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery), puedes dirigirte a los usuarios en función de sus acciones pasadas utilizando la segmentación y la prioridad.

Por ejemplo, para mostrar un banner especial solo a los usuarios que hayan completado un`purchase`evento:
1. **Orientación:** En tu campaña, dirígete a un segmento de usuarios que hayan realizado el evento `purchase`personalizado  al menos una vez.
2. **Prioridad:** Si tienes un banner general para todos los usuarios y este banner específico para compradores que se dirige al mismo emplazamiento, establece la prioridad del banner específico en **Alta** y la del banner general en **Media** o **Baja**.

Cuando el usuario inicia una nueva sesión o actualiza los banners después de realizar la acción, Braze evalúa su elegibilidad. Si coinciden con el segmento «Compra», se mostrará el banner de alta prioridad.


## ¿Pueden los usuarios cerrar manualmente un banner?

No. Los usuarios no pueden cerrar manualmente los banners. Sin embargo, puedes controlar la visibilidad de los banners administrando la elegibilidad de los segmentos de usuarios. Cuando un usuario ya no cumple los criterios de segmentación de una campaña de banners, no volverás a verla en tu próxima sesión.

Por ejemplo, si muestras un banner promocional hasta que un usuario realiza una compra, registrar un evento como`purchase_completed`  puede eliminar a ese usuario del segmento objetivo, ocultando efectivamente el banner en sesiones posteriores.

## ¿Puedo exportar los análisis de la campaña de banners utilizando la API de Braze?

Sí. Puedes utilizar el[`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/) [ punto final]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/) para obtener datos sobre cuántas campañas de Banner se han visto, realizado un clic o convertido.

## ¿Cuándo se realiza la segmentación de los usuarios?

Los usuarios se segmentan al inicio de la sesión. Si los segmentos objetivo de una campaña dependen de atributos personalizados, eventos personalizados u otros atributos de segmentación, estos deben estar presentes en el usuario al inicio de la sesión.

## ¿Cómo puedo componer banners para garantizar la menor latencia posible?

Cuanto más sencillo sea el mensaje de tu banner, más rápido se renderizará. Lo mejor es probar tu campaña de banners comparándola con la latencia prevista para tu caso de uso. Por ejemplo, asegúrate de probar atributos líquidos como `catalog_items`.

## ¿Se admiten todas las etiquetas de Liquid?

No. Sin embargo, la mayoría de las etiquetas de Liquid son compatibles con los mensajes de Banner, excepto`catalog_items`las que se vuelven a renderizar utilizando la[`:rerender`]({{site.baseurl}}/user_guide/data/activation/catalogs/using_catalogs/#using-liquid)[etiqueta]({{site.baseurl}}/user_guide/data/activation/catalogs/using_catalogs/#using-liquid) .

## ¿Puedo capturar eventos de clic?

Sí. La forma en que se capturan los eventos de clic depende de cómo se represente tu banner:

- **Componentes estándar del editor:** Si tu banner utiliza componentes de editor estándar (imágenes, botones, texto), el seguimiento de los clics se realiza automáticamente cuando se utilizan los métodos de inserción del SDK.
- **Bloques de código personalizados:** Si deseas realizar el seguimiento de los clics en elementos dentro de un bloque de editor de código personalizado, debes llamar`brazeBridge.logClick()`a  desde tu HTML personalizado para realizar el seguimiento de los clics. Esto se aplica incluso cuando se utilizan los métodos SDK para insertar y renderizar el banner. Para obtener la referencia completa, consulta [Código personalizado y puente JavaScript para banners]({{site.baseurl}}/user_guide/message_building_by_channel/banners/custom_code/#javascript-bridge).
- **Interfaz de usuario personalizada (sin interfaz gráfica):** Si estás creando una interfaz de usuario totalmente personalizada utilizando las propiedades personalizadas del banner en lugar de renderizar el HTML del banner, llama`logClick()`al objeto Banner desde el código de tu aplicación.

Para obtener más información, consulta [Registro de clics]({{site.baseurl}}/developer_guide/banners/placements/#logging-clicks).
