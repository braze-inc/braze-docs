---
page_order: 20
nav_title: Buenas prácticas
article_title: Buenas prácticas de push
description: "Esta página contiene buenas prácticas y casos de uso de push para asegurarte de que tus mensajes push inspiran interacción en lugar de molestia."
channel: push
---

# Buenas prácticas de push

Las notificaciones push son herramientas potentes para interactuar con los usuarios de tu aplicación, pero deben utilizarse con cuidado para garantizar que transmiten mensajes oportunos y relevantes. Antes de enviar tu mensaje push, consulta las siguientes buenas prácticas para conocer los aspectos que debes tener en cuenta y comprobar.

{% alert important %}
Tus mensajes push deben ajustarse a las directrices de las políticas de la App Store de Apple y la Play Store de Google, concretamente en lo que respecta al uso de mensajes push como publicidad, correo no deseado, promociones, etc. Más información sobre [la normativa push móvil]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/#mobile-push-regulations-for-apps).
{% endalert %}

## Redacta tu mensaje push

Como buena práctica, Braze recomienda mantener cada línea de texto, tanto para el título opcional como para el cuerpo del mensaje, en aproximadamente 30-40 caracteres en una notificación push móvil. Ten en cuenta que el contador de caracteres del compositor no tiene en cuenta los caracteres Liquid. Esto significa que el recuento final de caracteres de un mensaje depende de cómo se renderice Liquid para cada usuario. En caso de duda, sé breve y conciso.

## Reducir el tamaño de la carga útil de las notificaciones push

El tamaño máximo de la carga útil depende de la plataforma.

| Plataforma | Tamaño máximo de la carga útil |
| --- | --- |
| Web | 3.807 bytes |
| Android | 3.930 bytes |
| iOS | 3.960 bytes |
| Kindle | 5.985 bytes |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Si tu push supera el tamaño máximo de carga útil, es posible que el mensaje no se envíe. Como buena práctica, mantén tu carga útil en unos pocos cientos de bytes.

### ¿Qué es una carga útil push?

Los proveedores de servicios push calculan si tu notificación push puede mostrarse a un usuario teniendo en cuenta el tamaño en bytes de toda la carga útil push. La carga útil está limitada a **4 KB (4.096 bytes)** para la mayoría de los servicios push, incluidos los siguientes:

- Servicio de notificaciones push de Apple (APN)
- Firebase Cloud Messaging de Android (FCM)
- Notificación push web
- Huawei push

Estos servicios push rechazarán cualquier notificación que supere este límite.

Braze reserva una parte de la carga útil push para fines de integración y análisis. Por tanto, el tamaño máximo de nuestra carga útil es de **3.807 bytes**. Si tu push supera este tamaño, es posible que el mensaje no se envíe. Como buena práctica, mantén tu carga útil en unos pocos cientos de bytes.

Los siguientes elementos de tu push constituyen la carga útil push:

- Texto, como el título y el cuerpo del mensaje
- Renderizado final de cualquier personalización Liquid
- URL de las imágenes (pero no el tamaño de la propia imagen)
- URL de los destinos de clic
- Nombres de los botones
- Pares clave-valor

### Consejos para reducir el tamaño de la carga útil

Para reducir el tamaño de la carga útil:

- Haz que tu mensaje sea breve. Una buena pauta general es hacerlo accionable y útil en menos de 40 caracteres.
- Omite los espacios en blanco y los saltos de línea en tu texto.
- Ten en cuenta cómo se renderizará Liquid en el envío. Dado que el renderizado final de cualquier personalización Liquid variará de un usuario a otro, Braze no puede determinar si una carga útil push superará el límite de tamaño cuando se incluya Liquid. Si tu Liquid genera un mensaje más corto, puede que no haya problema. Sin embargo, si tu Liquid da lugar a un mensaje más largo, tu push puede superar el límite de tamaño de la carga útil. Prueba siempre tu mensaje push en un dispositivo real antes de enviarlo a los usuarios.
- Considera la posibilidad de acortar las URL utilizando un acortador de URL.

## Optimizar la segmentación

### Recopilar datos relevantes de los usuarios

Las notificaciones push deben tratarse con cuidado para llegar a los usuarios con notificaciones oportunas y relevantes. Braze recopilará información útil sobre el dispositivo y el uso que puede utilizarse para dirigirse a segmentos relevantes. Esta información debe complementarse con eventos personalizados y atributos específicos de tu aplicación. Con esos datos, puedes orientar cuidadosamente los mensajes para aumentar las tasas de apertura y reducir los casos de usuarios que desactivan las notificaciones push.

### Crear una página de configuración de notificaciones

Puedes crear una página de configuración en tu aplicación que permita a los usuarios indicarte qué notificaciones quieren recibir. Un enfoque común es crear un atributo personalizado booleano en Braze correspondiente al estado de configuración de la aplicación. Por ejemplo, una aplicación de noticias podría tener opciones de suscripción para noticias de última hora, deportes o política.

Cuando la aplicación de noticias quiere crear una campaña dirigida solo a usuarios interesados en política, añade el filtro de atributo `Subscribes to Politics` al segmento. Cuando se establece en true, solo los usuarios que se suscriban a las notificaciones las recibirán.

Para obtener más información sobre la configuración de atributos personalizados, consulta los siguientes artículos para [iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=swift), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_custom_attributes/#setting-custom-attributes) o [API REST]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-attributes-object-specification).

## Aumentar las adhesiones voluntarias y la relevancia

### Obtener el permiso del usuario

Las estadísticas generales de push habilitado estarán relacionadas con si el usuario ha aprobado las notificaciones con su sistema operativo. Si los usuarios desactivan las notificaciones en iOS, se eliminarán automáticamente de nuestro sistema, ya que Apple no permitirá que se envíe el token de notificaciones push.

A partir de Android 13 es necesario obtener permiso para mostrar las notificaciones push. Las versiones más antiguas de Android suscriben a los usuarios a las notificaciones de forma predeterminada.

### Prepara a los usuarios para las notificaciones push

Solo tienes una oportunidad para pedir permiso a un usuario y, si lo rechaza, es muy difícil convencerlo de que vuelva a habilitarlo en la configuración de su dispositivo. Por este motivo, debes preparar a los usuarios para las notificaciones push mediante un mensaje dentro de la aplicación antes de mostrar el aviso del sistema. Consulta [Mensajes push primer dentro de la aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/) para saber más sobre cómo aumentar las adhesiones voluntarias.

### Añadir controles de suscripción push

Para evitar que los usuarios desactiven las notificaciones a nivel de dispositivo, lo que elimina por completo su token push en primer plano, permite que los usuarios controlen su suscripción push directamente dentro de tu aplicación. Consulta [Actualización de los estados de suscripción push]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions#update-push-subscription-state) para obtener más detalles.

### Comprender los estados de suscripción push

El estado de suscripción push no garantiza que se entregue una notificación push: los usuarios también deben tener las notificaciones push habilitadas para recibir notificaciones. Esto se debe a que un perfil de usuario puede tener varios dispositivos con diferentes permisos push en primer plano, pero un único estado de suscripción push.

Si un usuario no tiene un token push válido en primer plano para una aplicación (es decir, desactiva los tokens push a nivel de dispositivo a través de la configuración, optando por no recibir notificaciones), su estado de suscripción puede seguir considerándose `subscribed` a push. Sin embargo, este usuario no sería `Foreground Push Enabled for App` en Braze, ya que el token de notificaciones push en primer plano no es válido.

Además, si un perfil de usuario no tiene ningún token push válido o registrado para ninguna otra aplicación, su filtro `Foreground Push Enabled` en la segmentación también será falso.

## Implementar una política de extinción para usuarios que no responden

Incluso cuando solo envías notificaciones push relevantes y oportunas, algunos usuarios pueden seguir sin responder a ellas y considerarlas correo no deseado. Supongamos que un usuario muestra un historial de ignorar repetidamente tus notificaciones push. En ese caso, es buena idea dejar de enviarle notificaciones push antes de que se moleste con las comunicaciones de tu aplicación o la desinstale por completo.

Para ello, crea una [política de extinción]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/sunset_policies) que, con el tiempo, deje de enviar notificaciones push a los usuarios que no hayan tenido una apertura directa o influenciada durante mucho tiempo.

1. Identifica a los usuarios que no responden basándote en Direct Opens o Influenced Opens.
2. Deja gradualmente de enviar notificaciones push a esos usuarios.
3. Antes de eliminar por completo las notificaciones push, envía una última notificación explicando por qué dejarán de recibirlas. Esto da a los usuarios la oportunidad de demostrar su interés en seguir recibiendo notificaciones push abriendo esa notificación.
4. Tras la entrada en vigor de la política de extinción, utiliza un [mensaje dentro de la aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/) para recordar a estos usuarios que, aunque ya no recibirán notificaciones push, los canales de mensajería dentro de la aplicación seguirán ofreciendo información interesante y útil.

Aunque puedas ser reacio a dejar de enviar notificaciones push a los usuarios que originalmente optaron por recibirlas, recuerda que otros canales de mensajería pueden llegar más eficazmente a estos usuarios, especialmente si previamente han ignorado tus notificaciones push. Si el usuario abre tus correos electrónicos, las campañas por correo electrónico son una buena forma de llegar a él fuera de tu aplicación. Si no es así, los mensajes dentro de la aplicación son la mejor forma de ofrecer contenido sin arriesgarte a que el usuario desinstale tu aplicación.

## Establecer eventos de conversión para las aperturas de aplicaciones

Al asignar [eventos de conversión]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) a una campaña push, puedes realizar un seguimiento de las aperturas de la aplicación durante un periodo determinado tras la recepción de la campaña. Establecer un evento de conversión para las aperturas de aplicaciones proporciona información diferente de las estadísticas de resultados que normalmente recibes tras una campaña push.

Mientras que todos los resultados de las campañas push desglosan las aperturas directas y las aperturas de un mensaje (que incluyen tanto las aperturas directas como las [Influenced Opens]({{site.baseurl}}/user_guide/analytics/tracking/influenced_opens/)), el seguimiento de conversiones rastreará cualquier tipo de apertura, ya sea directa o influenciada.

Además, al utilizar el evento de conversión "abre la aplicación", estás haciendo un seguimiento de las aperturas de la aplicación que se producen antes de ese plazo de conversión (por ejemplo, tres días). Esto difiere de una apertura influenciada en que el tiempo que un usuario tiene para registrar una apertura influenciada puede variar de persona a persona, dependiendo del comportamiento de interacción anterior de cada usuario.

## Artículos relacionados

¿No encontraste lo que buscabas? Consulta estos otros artículos sobre buenas prácticas:

- [Especificaciones de imágenes y texto para push]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/#push)
- [Mensajes push primer dentro de la aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/)
- [Capacidad de entrega para dispositivos Android chinos]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/chinese_push_deliverability/)
- [Lo que debes saber antes de enviar: canales]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/know_before_send/)