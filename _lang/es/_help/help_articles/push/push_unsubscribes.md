---
nav_title: Seguimiento de las cancelaciones de suscripción push
article_title: Seguimiento de las cancelaciones de suscripción push
page_type: solution
description: "Este artículo de ayuda proporciona algunos consejos para realizar un seguimiento de las cancelaciones de suscripción push."
channel: push
---

# Seguimiento de las cancelaciones de suscripción push

Las cancelaciones de suscripción push dependen de las actualizaciones del estado push de un usuario por parte de proveedores como Apple o Google. Estas actualizaciones pueden ser poco frecuentes e impredecibles. Como resultado, las cancelaciones de suscripción push no se incluyen como métrica en los análisis de las campañas push. 

Sin embargo, el seguimiento manual de las cancelaciones de suscripción push puede proporcionar información valiosa sobre la respuesta de los usuarios a la frecuencia de tus notificaciones y la relevancia del contenido. Aquí tienes dos opciones para el seguimiento de las cancelaciones de suscripción push.

## Opción 1: Utilizar filtros de segmento

Como solución, puedes crear un segmento para identificar a los usuarios que no estén habilitados para push, es decir, que no estén suscritos o hayan dado su adhesión voluntaria y no tengan un [token de notificaciones push en primer plano]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/#push-tokens). Por ejemplo, para ver el número de cancelaciones de suscripción en tu aplicación Android, utilizarías la combinación de los siguientes segmentos: 

- `Background or Foreground Push Enabled for App "TEST (Android)" is false`
- `Has Uninstalled`

![La sección Creador de segmentos con el filtro "Push de fondo o primer plano habilitado para la aplicación" para la aplicación PRUEBA (Android) es falsa, y el filtro "Ha desinstalado" están seleccionados para mostrar 2.393 usuarios alcanzables.]({% image_buster /assets/img/push_unsub_segment_example.png %})

Ten en cuenta que los filtros de segmentación serán aproximados y no podrán vincularse específicamente a una fecha y a una campaña.

## Opción 2: Utilizar un evento personalizado

{% alert important %}
Ten en cuenta que el registro de un evento personalizado para el cambio de suscripción consumirá [puntos de datos]({{site.baseurl}}/user_guide/data_and_analytics/data_points#consumption-count). Alternativamente, utiliza filtros de segmento para identificar y dirigirte a los usuarios que no están habilitados para push.
{% endalert %}

Para una solución diferente, también recomendamos crear un evento personalizado para las cancelaciones de suscripción push en función de si el estado de habilitación push de un usuario es `true` o `false`, con el fin de hacer un seguimiento de esta métrica.

_Última actualización: 13 de junio de 2024_
