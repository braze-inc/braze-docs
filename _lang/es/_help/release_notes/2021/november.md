---
nav_title: Noviembre
page_order: 1
noindex: true
page_type: update
description: "Este artículo contiene notas de la versión de noviembre de 2021."
---
# Noviembre de 2021

## Métrica de informe de la tasa de clics abiertos
Braze ha añadido una nueva métrica de correo electrónico, la tasa de clics abiertos, disponible en el [generador de informes]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/). Esta métrica representa el porcentaje de correos electrónicos abiertos en los que se ha hecho clic.

## Métrica de notificación de aperturas de máquina

Una nueva métrica de correo electrónico, [Aperturas de máquina]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/analytics_glossary/#machine-opens), está disponible en las páginas Canvas y Análisis de campaña para los correos electrónicos. Esta métrica identifica las aperturas de correo electrónico que no son humanas (como las abiertas por los servidores de Apple), mostradas como un subconjunto del total de aperturas.

## número_cubo_aleatorio Variable líquida
Se ha añadido la variable `random_bucket_number` a la lista de [variables compatibles de Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#supported-personalization-tags) para la personalización de mensajes. 

## Directrices para las notificaciones push enriquecidas de iOS 15
Se han añadido nuevas [directrices sobre notificaciones push de iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/) a los documentos enriquecidos de iOS, incluida información sobre los estados de las notificaciones y un desglose de las variables de truncamiento de texto.

## IP en lista blanca en la UE para webhooks y contenido conectado
Se han añadido IP adicionales a la lista blanca de la UE para webhooks y contenido conectado a nuestro artículo sobre [webhooks]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) y [contenido conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/). Estas nuevas IP incluyen `18.157.135.97`, `3.123.166.46`, `3.64.27.36`, `3.65.88.25`, `3.68.144.188` y `3.70.107.88`.

## Punto final de exportación de compras
Se añadió a Braze un nuevo [punto final `/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id/). Este punto final devuelve listas paginadas de ID de productos.

## Nuevas asociaciones Braze

### Adobe - Plataforma de datos de los clientes
La integración de Braze y [Adobe]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/adobe/#adobe) permite a las marcas conectar y mapear sus datos de Adobe (atributos personalizados y segmentos) con Braze en tiempo real. Las marcas pueden entonces actuar a partir de estos datos, entregando experiencias personalizadas y dirigidas a esos usuarios. 

### BlueConic - Plataforma de datos de los clientes
Con [Blueconic]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/blueconic/#blueconic), los usuarios de Braze pueden unificar los datos en perfiles persistentes e individuales y sincronizarlos después en todos los sistemas y puntos de contacto con el cliente para apoyar una amplia gama de iniciativas centradas en el crecimiento, como la orquestación del ciclo de vida del cliente, el modelado y el análisis, los productos y experiencias digitales, la monetización basada en la audiencia y mucho más.

### Digno - Contenido dinámico
La integración de Braze y [Worthy]({{site.baseurl}}/partners/message_personalization/dynamic_content/worthy/#worthy) te permite crear fácilmente experiencias ricas y personalizadas dentro de la aplicación utilizando el editor de arrastrar y soltar contenido dinámico de Worthy y entregarlas a través de Braze.

### Judo - Contenido dinámico
La integración de [Judo]({{site.baseurl}}/partners/message_personalization/dynamic_content/judo/#judo) y Braze te permite sobrescribir componentes de tu campaña y sustituirlos por experiencias Judo. Los datos de Braze pueden utilizarse para apoyar el contenido personalizado en una experiencia de Judo. Los eventos del usuario y los datos de la experiencia pueden retroalimentarse a Braze para la atribución y la orientación.

### Línea - Mensajería
La integración de [Line]({{site.baseurl}}/partners/message_orchestration/additional_channels/messaging/line/#line) y Braze te permite aprovechar los webhooks de Braze y las características avanzadas de segmentación, personalización y desencadenación para enviar mensajes a tus usuarios en Line a través de [la API de mensajería de Line](https://developers.line.biz/en/docs/messaging-api/overview/).

### RevenueCat - Pagos
La integración de [RevenueCat]({{site.baseurl}}/partners/data_and_infrastructure_agility/payments/revenuecat/#revenuecat) y Braze te permite sincronizar automáticamente los eventos del ciclo de vida de compra y suscripción de tus clientes en todas las plataformas. Esto te permite crear campañas que reaccionen a la etapa del ciclo de vida de suscripción de tus clientes, como interactuar con los clientes que se dieron de baja durante su prueba gratuita o enviar recordatorios a los clientes con problemas de facturación.

### Punchh - Fidelización
[Punchh]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/punchh/#punchh) se ha asociado con Braze para sincronizar los datos de ambas plataformas con fines de regalo y fidelización. Los datos publicados en Braze estarán disponibles para la segmentación y pueden sincronizar los datos de usuario de nuevo en Punchh a través de plantillas webhook configuradas en Braze.  