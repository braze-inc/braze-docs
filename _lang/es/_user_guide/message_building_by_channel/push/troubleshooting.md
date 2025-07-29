---
nav_title: Solución de problemas
article_title: Solución de problemas Push
page_order: 23
page_type: reference
description: "Esta página contiene pasos para la solución de problemas relacionados con el canal de mensajería push."
channel: push
---

# Solución de problemas Push

> Esta página te ayuda a solucionar varios problemas que puedas experimentar con el canal de mensajería Push.

## Faltan notificaciones push

¿Tienes problemas de entrega con las notificaciones push? Hay una serie de pasos que puedes dar para solucionar este problema, comprobando el:

- [Estado de la suscripción push](#push-subscription-status)
- [Segmento](#segment)
- [Límites de la notificación push](#push-notification-caps)
- [Límites de velocidad](#rate-limits)
- [Estado del grupo de control](#control-group-status)
- [Token de notificaciones push válido](#valid-push-token)
- [Tipo de notificación push](#push-notification-type)
- [Aplicación Currents](#current-app)

#### Estado de la suscripción push

Los push sólo pueden enviarse a usuarios suscritos o con adhesión voluntaria. Comprueba tu perfil de usuario en la pestaña [Interacción]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/#engagement-tab) de la sección **Perfil de usuario** para confirmar si estás registrado activamente para push en el espacio de trabajo que estás probando. Si estás registrado para varias aplicaciones, las encontrarás listadas en el campo **Push registrado para**:

![Push Registrado Para]({% image_buster /assets/img_archive/trouble1.png %})

También puedes exportar los perfiles de usuario utilizando los puntos finales de exportación Braze:
- [Usuarios por identificador]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier)
- [Usuarios por segmento]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment)

Cualquiera de los dos puntos finales devolverá un objeto token de notificaciones push que incluye información de habilitación push por dispositivo.

#### Segmento

Asegúrate de que entras en el segmento al que te diriges (si se trata de una campaña en vivo y no de una prueba). En el **perfil de usuario**, verás una lista de los segmentos en los que se encuentra actualmente el usuario. Recuerda que se trata de una variable en constante cambio, ya que la segmentación se actualiza en tiempo real.

![Lista de segmentos]({% image_buster /assets/img_archive/trouble2.png %})

También puedes confirmar que el usuario forma parte del segmento utilizando **la Búsqueda de usuarios** al crear un segmento.

![Sección de búsqueda de usuarios con un campo de búsqueda.]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:80%;"}

#### Límites de la notificación push

Comprueba los límites globales de frecuencia. Es posible que no recibieras la notificación push porque tu espacio de trabajo tiene establecida una limitación de frecuencia global y ya has alcanzado tu límite de notificaciones push para el periodo de tiempo especificado.

Puedes hacerlo activando la [limitación de frecuencia global]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#freq-cap-feat-over) en el panel. Si la campaña está configurada para cumplir las normas de limitación de frecuencia, habrá una serie de usuarios afectados por esta configuración

![Detalles de la campaña]({% image_buster /assets/img_archive/trouble3.png %})

#### Límites de velocidad

Si tienes configurado un límite de velocidad para tu campaña o Canvas, es posible que dejes de recibir mensajería por superar este límite. Para más información, consulta [Limitación de tasa]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#rate-limiting).

#### Estado del grupo de control

Si se trata de una campaña de un solo canal o de un Canvas con un grupo de control, es posible que estés cayendo en el grupo de control.

  1. Comprueba la [distribución de variantes]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing/#step-5-distribute-users-among-your-variants) para ver si hay un grupo de control.
  2. Si es así, crea un segmento filtrando por [en grupo de control de campaña]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/#in-campaign-control-group-filter), luego [exporta el segmento]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/segment_data_to_csv/#exporting-to-csv) y comprueba si tu ID de usuario está en esta lista.

#### Token de notificaciones push válido
Un token de notificaciones push es un identificador que los remitentes utilizan para dirigirse a dispositivos específicos con una notificación push. Por tanto, si el dispositivo no tiene un token de notificaciones push válido, no hay forma de enviarle una notificación push. 

#### Tipo de notificación push

Comprueba que estás utilizando el tipo correcto de notificación push. Por ejemplo, si quieres dirigirte a un FireTV, entonces utilizarías una notificación push de Kindle, no una campaña push de Android. Del mismo modo, si quieres dirigirte a un Android, utiliza una notificación push de Android y no una campaña push de iOS. Consulta los siguientes artículos para obtener más información sobre el flujo de trabajo de Braze:
- [Notificación push de Apple]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting/?sdktab=swift)
- [Mensajería en la nube Firebase]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting/?sdktab=android)

#### Aplicación Currents

Cuando pruebes envíos push con usuarios internos, asegúrate de que el usuario que quieres que reciba la notificación push ha iniciado sesión en la aplicación correspondiente. Esto puede hacer que el usuario no reciba un push o reciba un push para el que crees que no está segmentado.

¿Aún necesitas ayuda? Abre un [ticket de soporte]({{site.baseurl}}/braze_support/).

