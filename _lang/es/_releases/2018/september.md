---
nav_title: Septiembre
page_order: 5
noindex: true
page_type: update
description: "Este artículo contiene notas de la versión de septiembre de 2018."
---
# Septiembre de 2018

## Grupos de notificaciones de iOS 12: Capacidades adicionales

¡Ya puedes acceder a [las características del grupo de notificaciones de Apple]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#notification-groups) utilizando Braze! Puedes añadir Argumentos de Resumen y Grupos, utilizar Alertas Críticas, filtrar por usuarios Autenticados Provisionalmente y ver el estado Autenticado Provisionalmente en los perfiles de usuario.

## Tiempo de silencio

Ahora los clientes pueden especificar [horas tranquilas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-5-select-your-send-settings) (el tiempo durante el cual no se enviarán tus mensajes) para Canvas. Sólo tienes que ir a tu **configuración de envío de Canvas** y marcar "Habilitar horas tranquilas". A continuación, selecciona tus Horas Tranquilas en la hora local de tu usuario y qué acción seguirá si el mensaje se desencadena dentro de esas Horas Tranquilas.

Las campañas ahora también utilizan la Hora de Silencio en lugar de "envía este mensaje durante una parte específica del día".

## Ajustar clientes

Los clientes de Braze que utilicen [Adjust]({{site.baseurl}}/partners/message_orchestration/attribution/adjust/) ahora pueden ver su clave de API de Braze y la URL de su instancia de Braze, que luego utilizarán en la plataforma Adjust para la integración.

## No en el filtro de segmentos

Ahora los clientes pueden crear un segmento a partir de los usuarios que [no están incluidos en un segmento determinado]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#retargeting).

## Exportaciones CSV de destinatarios de Canvas

Ahora los clientes pueden [exportar datos]({{site.baseurl}}/user_guide/data/export_braze_data/export_canvas_data/) sobre los usuarios que han entrado en un Canvas. El CSV generado será similar al CSV de la campaña.

## Filtro de segmentos de iOS 12 autorizado provisionalmente

Se ha añadido un [filtro de segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#other) que te permite encontrar usuarios que están provisionalmente autorizados en iOS 12 para una aplicación determinada.

## Cargador de imágenes de mensajes dentro de la aplicación

El cargador de imágenes para mensajes dentro de la aplicación se ha movido del panel de diseño al panel de composición.

## Permisos de sólo lectura en la página Perfil de usuario

Antes de esta versión, los clientes podían cambiar el estado de la suscripción y la dirección de correo electrónico en el perfil de usuario con [permisos de sólo lectura]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#available-limited-and-team-role-permissions). Cambiamos el nombre del permiso `import_user` a permiso `import_and_update_user` y restringimos el acceso de edición al estado de la suscripción y a la dirección de correo electrónico. Ahora, cuando un desarrollador se hace pasar por alguien de sólo lectura o carece de este permiso, no puede cambiar el estado de la suscripción ni la dirección de correo electrónico.
