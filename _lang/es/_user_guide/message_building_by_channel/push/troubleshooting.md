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

Los push sólo pueden enviarse a usuarios suscritos o con adhesión voluntaria. Comprueba tu perfil de usuario en la pestaña [Interacción][1] de la sección **Perfil de usuario** para confirmar si estás registrado activamente para push en el espacio de trabajo que estás probando. Si estás registrado para varias aplicaciones, las encontrarás listadas en el campo **Push registrado para**:

![Push Registrado Para][2]

También puedes exportar los perfiles de usuario utilizando los puntos finales de exportación Braze:
- [Usuarios por identificador][12]
- [Usuarios por segmento][13]

Cualquiera de los dos puntos finales devolverá un objeto token de notificaciones push que incluye información de habilitación push por dispositivo.

#### Segmento

Asegúrate de que entras en el segmento al que te diriges (si se trata de una campaña en vivo y no de una prueba). En el **perfil de usuario**, verás una lista de los segmentos en los que se encuentra actualmente el usuario. Recuerda que se trata de una variable en constante cambio, ya que la segmentación se actualiza en tiempo real.

![Lista de segmentos][3]

También puedes confirmar que el usuario forma parte del segmento utilizando **la Búsqueda de usuarios** al crear un segmento.

![Sección de búsqueda de usuarios con un campo de búsqueda.][14]{: style="max-width:80%;"}

#### Límites de la notificación push

Comprueba los límites globales de frecuencia. Es posible que no recibieras la notificación push porque tu espacio de trabajo tiene establecida una limitación de frecuencia global y ya has alcanzado tu límite de notificaciones push para el periodo de tiempo especificado.

Puedes hacerlo marcando [limitación de frecuencia global][4] en el panel. Si la campaña está configurada para cumplir las normas de limitación de frecuencia, habrá una serie de usuarios afectados por esta configuración

![Detalles de la campaña][5]

#### Límites de velocidad

Si tienes configurado un límite de velocidad para tu campaña o Canvas, es posible que dejes de recibir mensajería por superar este límite. Para más información, consulta [Límite de velocidad][9].

#### Estado del grupo de control

Si se trata de una campaña de un solo canal o de un Canvas con un grupo de control, es posible que estés cayendo en el grupo de control.

  1. Comprueba la [distribución de variantes][6] para ver si hay un grupo de control.
  2. Si es así, crea un filtrado de segmentos para [en el grupo de control de campaña][7] y luego [exporta el segmento][8] y comprueba si tu ID de usuario está en esta lista.

#### Token de notificaciones push válido
Un token de notificaciones push es un identificador que los remitentes utilizan para dirigirse a dispositivos específicos con una notificación push. Por tanto, si el dispositivo no tiene un token de notificaciones push válido, no hay forma de enviarle una notificación push. 

#### Tipo de notificación push

Comprueba que estás utilizando el tipo correcto de notificación push. Por ejemplo, si quieres dirigirte a un FireTV, entonces utilizarías una notificación push de Kindle, no una campaña push de Android. Del mismo modo, si quieres dirigirte a un Android, utiliza una notificación push de Android y no una campaña push de iOS. Consulta los siguientes artículos para obtener más información sobre el flujo de trabajo de Braze:
- [Notificación push de Apple][10]
- [Firebase Cloud Messaging][11]

#### Aplicación Currents

Cuando pruebes envíos push con usuarios internos, asegúrate de que el usuario que quieres que reciba la notificación push ha iniciado sesión en la aplicación correspondiente. Esto puede hacer que el usuario no reciba un push o reciba un push para el que crees que no está segmentado.

¿Aún necesitas ayuda? Abre un [ticket de soporte]({{site.baseurl}}/braze_support/).

[1]: {{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/#engagement-tab
[2]: {% image_buster /assets/img_archive/trouble1.png %}
[3]: {% image_buster /assets/img_archive/trouble2.png %}
[4]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#freq-cap-feat-over
[5]: {% image_buster /assets/img_archive/trouble3.png %}
[6]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing/#step-5-distribute-users-among-your-variants
[7]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/#in-campaign-control-group-filter
[8]: {{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/segment_data_to_csv/#exporting-to-csv
[9]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#rate-limiting
[10]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/troubleshooting/
[11]: {{site.baseurl}}/developer_guide/platforms/android/push_notifications/troubleshooting/
[12]: {{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier
[13]: {{site.baseurl}}/api/endpoints/export/user_data/post_users_segment
[14]: {% image_buster /assets/img_archive/user_lookup.png %}