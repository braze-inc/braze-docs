---
nav_title: Correos electrónicos duplicados
article_title: Correos electrónicos duplicados
page_order: 7
page_type: reference
description: "Este artículo trata de las mejores prácticas para gestionar los correos electrónicos duplicados."
channel: email

---

# Correos electrónicos duplicados

> Para los correos electrónicos duplicados, si un correo electrónico se da de baja, otros perfiles (hasta 100 perfiles) con esa dirección de correo electrónico se actualizan para reflejar el mismo estado de suscripción. Esto se aplica a las cancelaciones de suscripción y otros cambios en el estado de suscripción, como el estado global de suscripción por correo electrónico y los estados individuales del grupo de suscripción.

## Actualizaciones de suscripción por correo electrónico

Braze comprueba y elimina automáticamente las direcciones de correo electrónico duplicadas cuando se envía una campaña de correo electrónico. De esta forma, un correo electrónico sólo se envía una vez y se "desduplica", lo que comprueba que no llega varias veces al mismo correo electrónico aunque varios perfiles de usuario compartan una misma dirección.

{% alert tip %}
Asegúrate de que estás familiarizado con las herramientas que Braze proporciona para [gestionar las suscripciones de correo electrónico de los usuarios]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions) y dirigir campañas a usuarios con determinados estados de suscripción. Estas herramientas son fundamentales para cumplir las [leyes contra el correo no deseado]({{site.baseurl}}/help/best_practices/spam_regulations/#spam-regulations).
{% endalert %}

Si los usuarios comparten una dirección de correo electrónico, la actualización de uno de estos usuarios propagará los cambios de suscripción entre estos usuarios (hasta 100 usuarios).

## Comportamiento de envío de mensajes

Dado que la deduplicación se produce cuando los usuarios objetivo se incluyen en el mismo envío, las campañas desencadenadas (excluidas las campañas desencadenadas por API) y los Canvases pueden dar lugar a múltiples envíos a la misma dirección de correo electrónico (incluso dentro de un periodo de tiempo en el que los usuarios podrían quedar excluidos debido a la reeligibilidad) si distintos usuarios con correos electrónicos coincidentes registran el evento desencadenante en momentos diferentes.

## Ejemplos

Por ejemplo, si el usuario A y el usuario B comparten el correo electrónico `johndoe@example.com` pero su perfil está en una zona horaria diferente, cuando el evento desencadenante de la campaña incluya el envío en la zona horaria de un usuario, el correo electrónico `johndoe@example.com` recibirá dos correos electrónicos.

Si estableces o actualizas la dirección de correo electrónico del usuario A a otra dirección de correo electrónico compartida por un usuario B existente, el usuario A heredará el estado de suscripción que ya existe del usuario B, a menos que esté activada la configuración **Reinscribir usuarios cuando actualicen su correo electrónico**.

{% alert important %}
Si envías una campaña a través de una llamada a la API (excluidas las campañas desencadenadas por la API), y en la audiencia del segmento se especifican varios usuarios con la misma dirección de correo electrónico, la enviaremos a esa dirección tantas veces como figuren en la llamada. Esto se debe a que suponemos que las llamadas a la API se construyen a propósito.
<br><br>
**Campañas desencadenadas por la API**<br>
Ten en cuenta que las campañas desencadenadas por la API deduplicarán o enviarán duplicados dependiendo de dónde esté definida la audiencia. <br>\- La deduplicación puede producirse si hay correos electrónicos duplicados en un segmento de destino o correos electrónicos duplicados debido a ID duplicados dentro del [campo del destinatario]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) de una llamada desencadenada por la API. <br>\- Se producirán correos electrónicos duplicados si te diriges directamente a ID de usuario distintos dentro del campo de destinatario de una llamada desencadenada por la API.
{% endalert %}
