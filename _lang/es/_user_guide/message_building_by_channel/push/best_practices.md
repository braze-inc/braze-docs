---
page_order: 20
nav_title: Buenas prácticas
article_title: Mejores prácticas de Push
description: "Esta página contiene las mejores prácticas y casos de uso para asegurarse de que sus mensajes push inspiran compromiso en lugar de molestia."
channel: push
---

# Empujar las mejores prácticas

Las notificaciones push son herramientas potentes para interactuar con los usuarios de su aplicación, pero deben utilizarse con cuidado para garantizar que transmiten mensajes oportunos y pertinentes. Antes de enviar su mensaje push, consulte las siguientes prácticas recomendadas para conocer los aspectos que debe conocer y comprobar.

{% alert important %}
Tus mensajes push deben ajustarse a las directrices de las políticas de la App Store de Apple y la Play Store de Google, concretamente en lo que respecta al uso de mensajes push como publicidad, spam, promociones, etc. Más información sobre [la normativa push móvil]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/#mobile-push-regulations-for-apps).
{% endalert %}

## Redacta tu mensaje push

Como mejor práctica, Braze recomienda mantener cada línea de texto, tanto para el título opcional como para el cuerpo del mensaje, en aproximadamente 30-40 caracteres en una notificación push móvil. Nota que el contador de caracteres del compositor no tiene en cuenta los caracteres Liquid. Esto significa que el recuento final de caracteres de un mensaje depende de cómo se renderice Liquid para cada usuario. En caso de duda, sé conciso y amable.

## Optimizar la segmentación

### Recopilar datos pertinentes sobre los usuarios

Las notificaciones push deben tratarse con cuidado para llegar a los usuarios con notificaciones oportunas y pertinentes. Braze recopilará información útil sobre el dispositivo y el uso que puede utilizarse para dirigirse a segmentos relevantes. Esta información debe complementarse con eventos personalizados y atributos específicos de su aplicación. Con esos datos, puede orientar cuidadosamente los mensajes para aumentar las tasas de apertura y reducir los casos de usuarios que desactivan la función push.

### Crear una página de configuración de notificaciones

Puedes crear una página de configuración en tu aplicación que permita a los usuarios decirte qué notificaciones quieren recibir. Un enfoque común es crear un atributo booleano personalizado en Braze correspondiente al estado de configuración de la aplicación. Por ejemplo, una aplicación de noticias podría tener opciones de suscripción para noticias de última hora, deportes o política.

Cuando la aplicación de noticias quiere crear una campaña dirigida sólo a usuarios interesados en Política, añade el filtro de atributo `Subscribes to Politics` al segmento. Cuando se establece en true, sólo los usuarios que se suscriban a las notificaciones las recibirán.

Para obtener más información sobre la configuración de atributos personalizados, consulte los siguientes artículos para [iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=swift), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_custom_attributes/#setting-custom-attributes) o [REST API]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-attributes-object-specification).

## Aumenta las adhesiones voluntarias y la relevancia

### Obtener el permiso del usuario

Las estadísticas generales de las notificaciones push habilitadas estarán relacionadas con si el usuario ha aprobado las notificaciones con su sistema operativo. Si los usuarios desactivan las notificaciones en iOS, se eliminarán automáticamente de nuestro sistema, ya que Apple no permitirá que se envíe el token push.

A partir de Android 13 es necesario obtener permiso para mostrar las notificaciones push. Las versiones más antiguas de Android suscriben a los usuarios a las notificaciones por defecto.

### Usuarios preferentes para push

Sólo se tiene una oportunidad para pedir permiso a un usuario y, si lo rechaza, es muy difícil convencerle de que vuelva a activarlo en la configuración de su dispositivo. Por este motivo, debe preparar a los usuarios para el push mediante un mensaje dentro de la aplicación antes de mostrar el aviso del sistema. Consulta [Mensajes push primer dentro de la aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/) para saber más sobre cómo aumentar las adhesiones voluntarias.

### Añadir controles de suscripción push

Para evitar que los usuarios desactiven las notificaciones a nivel de dispositivo, lo que elimina por completo su token push en primer plano, permita que los usuarios controlen su suscripción push directamente dentro de su aplicación. Consulte [Actualización de los estados de suscripción push]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions#update-push-subscription-state) para obtener más detalles.

### Comprender los estados de suscripción push

El estado de suscripción push no garantiza que se envíe una notificación push: los usuarios también deben estar habilitados para recibir notificaciones push. Esto se debe a que un perfil de usuario puede tener varios dispositivos con diferentes permisos push en primer plano pero un único estado de suscripción push.

Si un usuario no tiene un token push válido en primer plano para una aplicación (es decir, desactiva los tokens push en el dispositivo a través de los ajustes, optando por no recibir notificaciones), su estado de suscripción puede seguir considerándose `subscribed` to push. Sin embargo, este usuario no sería `Push Enabled for App` en Braze, ya que el token de notificaciones push en primer plano no es válido.

Además, si un perfil de usuario no tiene ningún token push válido o registrado para ninguna otra aplicación, su filtro `Push Enabled` en la segmentación también será falso.

## Aplicar una política de extinción para usuarios que no responden

Incluso cuando sólo envías notificaciones push relevantes y oportunas, algunos usuarios pueden seguir sin responder a ellas y considerarlas spam. Supongamos que un usuario muestra un historial de ignorar repetidamente tus notificaciones push. En ese caso, es una buena idea dejar de enviarles pushes antes de que se molesten con las comunicaciones de tu aplicación o la desinstalen por completo. 

Para ello, cree una [política de extinción]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/sunset_policies) que, con el tiempo, deje de enviar notificaciones push a los usuarios que no hayan tenido abierto un directo o un influencer durante mucho tiempo.

1. Identifique a los usuarios que no responden basándose en aperturas directas o influenciadas.
2. Deje gradualmente de enviar notificaciones push a esos usuarios.
3. Antes de eliminar por completo las notificaciones push, envíe una última notificación explicando por qué dejarán de recibirlas. Esto da a los usuarios la oportunidad de demostrar su interés en seguir recibiendo pushes abriendo esa notificación.
4. Tras la entrada en vigor de la política de suspensión, utilice un [mensaje dentro]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/) de la aplicación para recordar a estos usuarios que, aunque ya no recibirán pushes, los canales de mensajería dentro de la aplicación seguirán ofreciendo información interesante y útil.

Aunque puede ser reacio a dejar de enviar mensajes push a los usuarios que originalmente optaron por ellos, recuerde que otros canales de mensajería pueden llegar más eficazmente a estos usuarios, especialmente si previamente han ignorado sus mensajes push. Si el usuario abre sus correos electrónicos, las campañas por correo electrónico son una buena forma de llegar a él fuera de su aplicación. Si no es así, los mensajes dentro de la aplicación son la mejor forma de ofrecer contenido sin arriesgarse a que el usuario desinstale la aplicación.

## Establecer eventos de conversión para las aperturas de aplicaciones

Al asignar [eventos de conversión]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) a una campaña push, puede realizar un seguimiento de las aperturas de la aplicación durante un periodo determinado tras la recepción de la campaña. Establecer un evento de conversión para las aperturas de aplicaciones proporciona una visión diferente de las estadísticas de resultados que normalmente recibe tras una campaña push.

Mientras que todos los resultados de las campañas push desglosan las aperturas directas y las aperturas directas de un mensaje (que incluyen tanto [las aperturas]({{site.baseurl}}/user_guide/analytics/tracking/influenced_opens/) directas como las influenciadas), el seguimiento de conversiones rastreará cualquier tipo de apertura, ya sea directa o influenciada.

Además, al utilizar el evento de conversión "abre la aplicación", estás haciendo un seguimiento de las aperturas de la aplicación que se producen antes de ese plazo de conversión (por ejemplo, tres días). Esto difiere de una apertura influenciada en que el tiempo que un usuario tiene para registrar una apertura influenciada puede variar de persona a persona, dependiendo del comportamiento de compromiso anterior de cada usuario.

## Artículos relacionados

¿No ha encontrado lo que buscaba? Consulte estos otros artículos sobre buenas prácticas:

- [Formatos de mensajes push e imágenes]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/message_format/)
- [Mensajes push primer dentro de la aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/)
- [Entregabilidad para dispositivos Android chinos]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/chinese_push_deliverability/)
- [Saber antes de enviar: canales]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/know_before_send/)
