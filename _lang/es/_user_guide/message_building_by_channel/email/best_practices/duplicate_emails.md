---
nav_title: Correos electrónicos duplicados
article_title: Correos electrónicos duplicados
page_order: 7
page_type: reference
description: "En este artículo se describen las mejores prácticas para gestionar los correos electrónicos duplicados."
channel: email

---

# Correos electrónicos duplicados

> Si varios perfiles comparten una dirección de correo electrónico y uno de ellos se da de baja, Braze actualiza otros perfiles (hasta 100) con esa dirección al mismo estado de suscripción. Esto se aplica a las cancelaciones de suscripción y a otros cambios, como el estado de suscripción global y los estados del grupo de suscripción individual.

## Actualizaciones de suscripción por correo electrónico

Braze comprueba y elimina automáticamente las direcciones de correo electrónico duplicadas cuando envía una campaña de correo electrónico. Esto evita que Braze envíe el correo electrónico más de una vez aunque varios perfiles de usuario compartan una dirección.

{% alert tip %}
Asegúrese de estar familiarizado con las herramientas que Braze proporciona para [gestionar las suscripciones de correo electrónico de los usuarios]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions) y dirigir las campañas a usuarios con determinados estados de suscripción. Estas herramientas son fundamentales para cumplir la [legislación antispam]({{site.baseurl}}/help/best_practices/spam_regulations/#spam-regulations).
{% endalert %}

Si los usuarios comparten una dirección de correo electrónico y actualizas un perfil, Braze propaga los cambios de suscripción entre esos usuarios (hasta 100).

## Comportamiento en el envío de mensajes

Dado que la deduplicación se produce cuando los usuarios objetivo se incluyen en el mismo envío, las campañas activadas (excluidas las campañas activadas por API) y los Canvases pueden dar lugar a múltiples envíos a la misma dirección de correo electrónico (incluso dentro de un periodo de tiempo en el que los usuarios podrían excluirse debido a la reeligibilidad) si distintos usuarios con correos electrónicos coincidentes registran el evento de activación en momentos diferentes.

## Ejemplos

Por ejemplo, si el usuario A y el usuario B comparten el correo electrónico `johndoe@example.com` pero su perfil se encuentra en una zona horaria diferente, cuando el evento de activación de la campaña incluya el envío en la zona horaria de un usuario, el correo electrónico `johndoe@example.com` recibirá dos correos electrónicos.

Si establece o actualiza la dirección de correo electrónico del usuario A a otra dirección de correo electrónico compartida por un usuario B existente, el usuario A heredará el estado de suscripción que ya existe del usuario B, a menos que esté activada la opción **Volver a suscribir usuarios cuando actualicen su correo electrónico**.

{% alert important %}
Si envías una campaña a través de una llamada a la API (excluidas las campañas desencadenadas por la API), y en el segmento de audiencia se especifican varios usuarios con la misma dirección de correo electrónico, la enviaremos a esa dirección tantas veces como se indique en la llamada. Esto se debe a que suponemos que las llamadas a la API se construyen intencionadamente.
<br><br>
**Campañas activadas por API**<br>
Tenga en cuenta que las campañas activadas por API deduplicarán o enviarán duplicados dependiendo de dónde se defina la audiencia. <br>\- La deduplicación puede producirse si hay correos electrónicos duplicados en un segmento de destino o correos electrónicos duplicados debido a ID duplicados en el [campo de destinatario]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) de una llamada activada por API. <br>\- Se producirán correos electrónicos duplicados si se dirigen directamente a distintos ID de usuario en el campo de destinatario de una llamada activada por API.
{% endalert %}
