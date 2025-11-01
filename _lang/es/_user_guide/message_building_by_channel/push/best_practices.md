---
page_order: 20
nav_title: Buenas prácticas
article_title: Mejores prácticas de push
description: "Esta página contiene las mejores prácticas de push y casos de uso para asegurarte de que tus mensajes push inspiran interacción en lugar de molestia."
channel: push
---

# Mejores prácticas de push

Las notificaciones push son herramientas poderosas para la interacción con los usuarios de tu aplicación, pero deben utilizarse con cuidado para garantizar que entregan mensajes oportunos y relevantes. Antes de enviar tu mensaje push, consulta las siguientes prácticas recomendadas para saber qué cosas debes saber y comprobar.

{% alert important %}
Tus mensajes push deben cumplir las directrices de las políticas de la App Store de Apple y de la Play Store de Google, específicamente en lo que respecta al uso de mensajes push como publicidad, correo no deseado, promociones, etc. Más información sobre [la normativa push móvil]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/#mobile-push-regulations-for-apps).
{% endalert %}

## Redacta tu mensaje push

Como mejor práctica, Braze recomienda mantener cada línea de texto, tanto para el título opcional como para el cuerpo del mensaje, en aproximadamente 30-40 caracteres en una notificación push móvil. Nota que el contador de caracteres del compositor no tiene en cuenta los caracteres Liquid. Esto significa que el recuento final de caracteres de un mensaje depende de cómo se renderice Liquid para cada usuario. En caso de duda, hazlo breve y dulce.

## Reducir el tamaño de la carga útil de las notificaciones push

El tamaño máximo de la carga útil depende de la plataforma.

| Plataforma | Tamaño máximo de la carga útil |
| --- | --- |
| Web | 3.807 bytes |
| Android | 3.930 bytes |
| iOS | 3.960 bytes |
| Kindle | 5.985 bytes |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Si tu push supera el tamaño máximo de carga útil, es posible que el mensaje no se envíe. Como práctica recomendada, mantén tu carga útil en unos pocos cientos de bytes.

### ¿Qué es una carga útil push?

Los proveedores de servicios push calculan si tu notificación push puede mostrarse a un usuario teniendo en cuenta el tamaño en bytes de toda la carga útil push. La carga útil está limitada a **4 KB (4.096 bytes** ) para la mayoría de los servicios push, incluidos:

- Servicio de notificaciones push de Apple (APN)
- Mensajería en la nube Firebase de Android (FCM)
- Web push
- Huawei push

Estos servicios push rechazarán cualquier notificación que supere este límite.

Braze reserva una parte de la carga útil push para fines de integración y análisis. Por tanto, el tamaño máximo de nuestra carga útil es de **3.807 bytes**. Si tu push supera este tamaño, es posible que el mensaje no se envíe. Como práctica recomendada, mantén tu carga útil en unos pocos cientos de bytes.

Los siguientes elementos de tu push constituyen la carga útil de tu push:

- Copia, como el título y el cuerpo del mensaje
- Render final de cualquier personalización Liquid
- URL de las imágenes (pero no el tamaño de la propia imagen)
- URL para objetivos de clic
- Nombres de los botones
- Pares clave-valor

### Consejos para reducir el tamaño de la carga útil

Para reducir el tamaño de la carga útil:

- Haz que tu mensaje sea breve. Una buena pauta general es hacerlo procesable y beneficioso en menos de 40 caracteres.
- Omite los espacios en blanco y los saltos de línea en tu copia.
- Ten en cuenta cómo se representará Liquid en el envío. Dado que la representación final de cualquier personalización de Liquid variará de un usuario a otro, Braze no puede determinar si una carga útil push superará el límite de tamaño cuando se incluya Liquid. Si tu Liquid muestra un mensaje más corto, puede que te vaya bien. Sin embargo, si tu Liquid da lugar a un mensaje más largo, tu push puede superar el límite de tamaño de la carga útil. Prueba siempre tu mensaje push en un dispositivo real antes de enviarlo a los usuarios.
- Considera la posibilidad de acortar las URL utilizando un acortador de URL.

## Optimizar la orientación

### Recoger datos de usuario relevantes

Las notificaciones push deben tratarse con cuidado para llegar a los usuarios con notificaciones oportunas y relevantes. Braze recopilará información útil sobre el dispositivo y el uso que puede utilizarse para dirigirse a segmentos relevantes. Esta información debe complementarse con eventos personalizados y atributos específicos de tu aplicación. Con esos datos, puedes orientar cuidadosamente los mensajes para aumentar las tasas abiertas y reducir las instancias en las que los usuarios desactivan el push.

### Crear una página de configuración de notificaciones

Puedes crear una página de configuración en tu aplicación que permita a los usuarios decirte qué notificaciones quieren recibir. Un método habitual es crear un atributo personalizado booleano en Braze que corresponda al estado de configuración de la aplicación. Por ejemplo, una aplicación de noticias podría tener configuraciones de suscripción para noticias de última hora, deportes o política.

Cuando la aplicación de noticias quiere crear una campaña dirigida sólo a usuarios interesados en Política, añade el filtro de atributos `Subscribes to Politics` al segmento. Si se establece en verdadero, sólo los usuarios suscritos a las notificaciones las recibirán.

Para obtener más información sobre la configuración de atributos personalizados, consulta los siguientes artículos para [iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=swift), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_custom_attributes/#setting-custom-attributes) o [API REST]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-attributes-object-specification).

## Aumenta las adhesiones voluntarias y la relevancia

### Obtener permiso del usuario

Las estadísticas generales de las notificaciones push habilitadas se referirán a si el usuario ha aprobado las notificaciones con su sistema operativo. Si los usuarios desactivan las notificaciones en iOS, se eliminarán automáticamente de nuestro sistema, ya que Apple no permitirá que se envíe el token de notificaciones push.

A partir de Android 13 es necesario obtener permiso para mostrar las notificaciones push. Las versiones antiguas de Android suscribirán a los usuarios a las notificaciones de forma predeterminada.

### Preparación de los usuarios para las notificaciones push

Sólo tienes una oportunidad de pedir permiso push a un usuario, y después de que lo rechace, es muy difícil convencerle de que vuelva a habilitar push en la configuración de su dispositivo. Por esta razón, debes preparar a los usuarios para el push utilizando un mensaje dentro de la aplicación antes de mostrar el aviso del sistema. Consulta [Mensajes push primer dentro de la]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/) aplicación para saber más sobre cómo aumentar las adhesiones voluntarias.

### Añadir controles de suscripción push

Para evitar que los usuarios desactiven las notificaciones a nivel de dispositivo, lo que elimina por completo su token de notificaciones push en primer plano, deja que los usuarios controlen su suscripción push directamente dentro de tu aplicación. Consulta [Actualizar los estados de suscripción push]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions#update-push-subscription-state) para más detalles.

### Comprender los estados de suscripción push

El estado de la suscripción push no garantiza que se vaya a entregar un push: los usuarios también deben estar habilitados para recibir notificaciones push. Esto se debe a que un perfil de usuario puede tener varios dispositivos con diferentes permisos push en primer plano, pero un único estado de suscripción push.

Si un usuario no tiene un token de notificaciones push válido para una aplicación (es decir, desactiva los tokens de notificaciones push a nivel de dispositivo a través de la configuración, optando por no recibir notificaciones), su estado de suscripción puede seguir considerándose `subscribed` a push. Sin embargo, este usuario no sería `Foreground Push Enabled for App` en Braze, ya que el token de notificaciones push en primer plano no es válido.

Además, si un perfil de usuario no tiene ningún token de notificaciones push válido o registrado para ninguna otra aplicación, su filtro `Foreground Push Enabled` en la segmentación también será falso.

## Aplicar una política de extinción para usuarios que no responden

Aunque sólo envíes notificaciones push relevantes y puntuales, algunos usuarios pueden seguir sin responder a ellas y considerarlas spam. Supón que un usuario muestra un historial de ignorar repetidamente tus notificaciones push. En ese caso, es una buena idea dejar de enviarles push antes de que se molesten con las comunicaciones de tu aplicación o la desinstalen por completo. 

Para ello, crea una [política de extinción]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/sunset_policies) que, con el tiempo, deje de enviar notificaciones push a los usuarios que no hayan tenido una apertura directa o influenciada durante mucho tiempo.

1. Identifica a los usuarios que no responden basándote en las aperturas directas o influenciadas.
2. Deja gradualmente de enviar notificaciones push a esos usuarios.
3. Antes de eliminar por completo las notificaciones push, entrega una última notificación explicando por qué dejarán de recibirlas. Esto da a los usuarios la oportunidad de demostrar su interés en que continúen los push abriendo esa notificación.
4. Cuando entre en vigor la política de suspensión, utiliza un [mensaje dentro de la aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/) para recordar a estos usuarios que, aunque ya no recibirán push, los canales de mensajería dentro de la aplicación seguirán entregando información interesante y útil.

Aunque puede que seas reacio a dejar de enviar push a los usuarios que originalmente optaron por ellos, recuerda que otros canales de mensajería pueden llegar más eficazmente a estos usuarios, especialmente si anteriormente han ignorado tus push. Si el usuario abre tus correos electrónicos, las campañas de correo electrónico son una buena forma de llegar a él fuera de tu aplicación. Si no, los mensajes dentro de la aplicación son la mejor forma de entregar contenido sin arriesgarse a que el usuario desinstale tu aplicación.

## Configurar eventos de conversión para aperturas de aplicaciones

Al asignar [eventos de conversión]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) a una campaña push, puedes hacer un seguimiento de las aperturas de la aplicación durante un determinado periodo tras la recepción de la campaña. Establecer un evento de conversión para las aperturas de aplicaciones proporciona una información diferente de las estadísticas de resultados que normalmente recibes tras una campaña push.

Mientras que todos los resultados de las campañas de mensajería push desglosan las aperturas y aperturas directas de un mensaje (lo que incluye tanto [las aperturas]({{site.baseurl}}/user_guide/analytics/tracking/influenced_opens/) directas como las influenciadas), el seguimiento de la conversión hará un seguimiento de cualquier tipo de apertura, ya sea directa o influenciada.

Además, al utilizar el evento de conversión "abre la aplicación", estás haciendo un seguimiento de las aperturas de la aplicación que se producen antes de ese plazo de conversión (por ejemplo, tres días). Esto difiere de una apertura influida en que el tiempo que tiene un usuario para registrar una apertura influida puede variar de una persona a otra, dependiendo del comportamiento de interacción anterior de cada usuario.

## Artículos relacionados

¿No has encontrado lo que buscabas? Consulta estos otros artículos sobre buenas prácticas:

- [Formatos de mensajes push e imágenes]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/message_format/)
- [Push primer mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/)
- [Capacidad de entrega para dispositivos Android chinos]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/chinese_push_deliverability/)
- [Saber antes de enviar: canales]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/know_before_send/)
