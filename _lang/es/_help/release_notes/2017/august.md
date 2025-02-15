---
nav_title: Agosto
page_order: 5
noindex: true
page_type: update
description: "Este artículo contiene notas de la versión de agosto de 2017."
---

# Agosto de 2017

## Actualizar para pulsar botones de acción push

Hemos añadido soporte para [botones de acción push][70] a nuestros puntos finales de mensajería de la API REST.

## Actualización de la plantilla Liquid

Ahora puedes [personalizar un mensaje][69] basándote en:
- El dispositivo al que se envió,
- ID del dispositivo,
- Operador,
- IDFA,
- Modelo,
- SO y
- Plataforma

## Canvas desencadenado por API

Ahora puedes desencadenar un [Canvas][68] a través de los puntos finales de la API (enviar, programar, actualizar, eliminar) que coinciden con los existentes para las campañas, lo que te permite automatizar y optimizar aún más tu marketing.

## Botones de acción para notificación push web

Hemos añadido compatibilidad con botones de acción para push en el SDK Web para Chrome, lo que te permitirá aumentar tu interacción dando a tus usuarios opciones contextuales que simplifiquen sus ajetreadas vidas. Consulta las [mejores prácticas para las notificaciones push][66].

## Nuevos puntos finales de la API

Hemos expuesto nuevos puntos finales de la API, /email/hard_bounces, que te permite obtener los rebotes duros por dirección de correo electrónico o en un intervalo de fechas determinado, y /messages/scheduled_broadcasts, que te permite obtener la próxima vez que comenzarán las campañas programadas y los Canvas de entrada programada. Estos nuevos puntos finales te permiten una mayor personalización y optimización de tus campañas. Más información sobre nuestros [puntos finales de la API][65].

## Geovallas

Hemos añadido una nueva característica, las geovallas, que te permiten desencadenar mensajes en tiempo real cuando los clientes entran y salen de zonas geográficas definidas, habilitando una comunicación personalizada y relevante con tus clientes. Más información sobre [marketing de ubicación][64].

## Actualizar al editor de correo electrónico

Hemos añadido el autocompletado dinámico a nuestro nuevo editor de correo electrónico, por lo que ahora puedes autocompletar con los atributos personalizados y eventos reales de tus clientes cuando utilices Liquid, lo que te facilitará la vida. Aprende más sobre las mejores prácticas de correo electrónico en [la Academia][63].

## Actualizar a filtros de fecha

Hemos añadido un filtro de fecha "nunca" para que puedas dirigirte a los clientes que nunca han recibido o interactuado con uno de tus mensajes, lo que te habilita para tener listas de clientes limpias y garantizar la capacidad de entrega del correo electrónico. Más información sobre [los filtros][62].

## Actualizar a Canvas

Hemos añadido porcentajes en la parte superior de cada variante en Canvas, así que ahora puedes ver de un vistazo qué variantes rinden más. Más información sobre [Canvas][61].

## Canvas con Intelligent Selection

Canvas dispone ahora de Intelligent Selection, que te permite probar tus Canvas con mayor eficacia. Más información sobre nuestra [Intelligence Suite][60].

## Actualización de los nombres para mostrar por correo electrónico

Hemos añadido compatibilidad con caracteres especiales UTF-8 en los nombres para mostrar del correo electrónico, para que puedas crear correos electrónicos aún más personalizados para tus clientes. Más información sobre [las mejores prácticas de correo electrónico][67].

## Agregación CSV de informes de interacción

Ahora, puedes recibir datos consolidados para cada campaña y cada Canvas en dos archivos separados, independientemente del número de campañas o Canvases seleccionados, lo que te permite disponer de todos los datos que necesitas, cuando los necesitas. Más información sobre [los informes de interacción][59].

> Como se indica en nuestras [notas de la versión de septiembre de 2017]({{site.baseurl}}/help/release_notes/2017/september/), ahora puedes agregar datos de un periodo de tiempo específico, así como programar exportaciones para que se ejecuten de forma recurrente.


[59]: {{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/
[60]: {{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/
[61]: {{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/
[62]: {{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#segmentation-filters
[63]: {{site.baseurl}}/help/troubleshooting_guide/troubleshooting_guide/#email
[64]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/locations_and_geofences/
[65]: {{site.baseurl}}/developer_guide/rest_api/basics/#what-is-a-rest-api
[66]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/
[67]: {{site.baseurl}}/help/troubleshooting_guide/troubleshooting_guide/#email
[68]: {{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/
[69]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/personalized_messaging/#personalized-messaging
[70]: {{site.baseurl}}/user_guide/message_building_by_channel/push/push_action_buttons/#how-to-use-action-buttons
[98]:{{site.baseurl}}/user_guide/onboarding/platform_administrative_features/#authentication-rules
