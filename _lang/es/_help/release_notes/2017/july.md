---
nav_title: Julio
page_order: 6
noindex: true
page_type: update
description: "Este artículo contiene notas de la versión de julio de 2017."
---

# Julio de 2017

## Imágenes grandes en la notificación push web

Hemos añadido compatibilidad con imágenes grandes para notificación push web en Chrome para Windows y Android, dándote la posibilidad de crear experiencias del cliente enriquecidas y atractivas. Más información sobre [notificaciones push web][58].

## Actualizaciones de los campos de correo electrónico

Ahora puedes bloquear correos electrónicos a un conjunto específico de direcciones de origen, para asegurarte de que no introduces accidentalmente una dirección incorrecta. El formulario de composición de correo electrónico se rellenará previamente con las direcciones utilizadas en los últimos 6 meses para agilizar el proceso. Consulta [las mejores prácticas de correo electrónico][57] para obtener más información.

## Actualizaciones de la API de detalles de campaña

El punto final `/campaign/details` ahora proporciona información sobre sus mensajes, permitiéndote extraer los campos asunto, cuerpo HTML, dirección del remitente y responder a mediante la API. Más información sobre [las API Braze][56].

## Actualizaciones de la plantilla Liquid

Hemos añadido la posibilidad de crear plantillas de atributos de variantes en Lienzos y campañas. En Canvas, ahora puedes crear plantillas tanto para el ID de la API de la variante como para el nombre de la variante, y en las campañas ahora puedes crear plantillas para `message_api_id` y `message_name` de un mensaje. Ambas actualizaciones permiten una mayor flexibilidad en tus mensajes, permitiéndote crear campañas personalizadas. Más información sobre [mensajería personalizada][55].

## Nuevo editor de correo electrónico HTML

Ahora puedes escribir y probar fácilmente correos electrónicos con un editor HTML a pantalla completa que habilita la vista previa en vivo, la personalización mediante Liquid y un editor de texto a pantalla completa mejorado con números de línea y resaltado de sintaxis. Más información sobre [la composición del correo electrónico][54].

## Actualizaciones de vistas previas

Ahora puedes seguir la ventana de la pantalla mientras te desplazas por las vistas previas de mensajes en campañas y Lienzos, asegurándote de que siempre puedes ver reflejados los cambios. Más información sobre [la vista previa y las pruebas][53].

## Nuevo filtro de membresía de segmento

Hemos añadido el [filtro de pertenencia a segmentos][52], que te habilita para dirigirte a los usuarios en función de su pertenencia a cualquiera de tus segmentos existentes. Además, hemos añadido la posibilidad de utilizar la lógica "Y" y "O" en los filtros de segmentos, así como la posibilidad de anidar segmentos entre sí. Estas actualizaciones te habilitan para enviar mensajes personalizados a tus clientes con mayor precisión. 

## Actualización a la vista previa de Android

Hemos actualizado la [vista previa][51] de Android para reflejar las versiones más recientes de Android desde Android N.


[51]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/#step-5-preview-message
[52]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#targeting-filters
[53]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/campaigns_in_multiple_languages/#step-6-preview-message
[54]: {{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_template/#creating-an-email-template
[55]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/personalized_messaging/#personalized-messaging
[56]: {{site.baseurl}}/developer_guide/rest_api/basics/#what-is-a-rest-api
[57]: {{site.baseurl}}/help/troubleshooting_guide/troubleshooting_guide/#email
[58]: {{site.baseurl}}/user_guide/message_building_by_channel/push/web
[98]:{{site.baseurl}}/user_guide/onboarding/platform_administrative_features/#authentication-rules
