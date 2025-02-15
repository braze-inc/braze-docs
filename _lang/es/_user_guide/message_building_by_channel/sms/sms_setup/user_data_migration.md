---
nav_title: "Migración de datos de usuario"
article_title: Migración de datos de usuario
page_order: 4
description: "Este artículo de referencia repasa todas las consideraciones que deberá tener en cuenta al migrar sus datos de usuario a Braze."
page_type: reference
channel:
  - SMS
noindex: true

---

# Migración de datos de usuario

> Este artículo repasará todas las consideraciones que deberá tener en cuenta al migrar sus datos de usuario a Braze.

## Formatear los números de teléfono de los usuarios según las normas del operador

Las compañías telefónicas tienen un tipo específico de formato que esperan llamado E.164, que es el plan de numeración telefónica internacional que garantiza que cada dispositivo tenga un número único a nivel mundial. Esto es lo que permite que las llamadas telefónicas y los mensajes de texto se dirijan correctamente a teléfonos individuales de distintos países. Los números E.164 tienen el formato que se muestra en la siguiente imagen, y pueden tener un máximo de 15 dígitos.

![E.164 consta del signo más, el prefijo del país, el prefijo de la zona y el número de teléfono][picture]{: style="max-width:50%;border: 0;"}

Para más información, consulte [Números de teléfono de usuario][userphone].

## Actualizar la información histórica sobre los estados de suscripción de los usuarios

Si dispone de información histórica sobre los [estados de suscripción][subscriptionstate] ] de sus usuarios para sus distintos canales de mensajería, asegúrese de actualizar esta información en Braze.

## Ejemplo de pasos de migración

Antes de empezar a componer campañas de SMS a través de Braze, tendrás que actualizar tus datos de usuario para asegurarte de que todo esto funciona.

**Aquí tienes un resumen rápido de los datos de usuario que tendrás que actualizar en Braze:**

1. **Importar los números de teléfono de los usuarios en el formato correcto** ([E.164][0]) requiere un signo más (+) y un código de país. Un ejemplo es +12408884782. Para más información sobre cómo importar números de teléfono de usuario, consulte [Números de teléfono de usuario][userphone].
    * Utiliza el [punto final`/users/track` ][1] para asignar el valor `phone`.<br><br>

2. **Asigne el SMS de su usuario [estado de suscripción][subscriptionstate]** (como suscrito o no suscrito) si dispone de esta información.
    * Utilice el [punto final`/subscription/status/set` ][6] para establecer a los usuarios como suscritos o dados de baja de sus Grupos de Suscripción SMS.

{% alert note %}
Cuando hayas configurado los grupos de suscripción a SMS en tu panel, podrás obtener la dirección `subscription_group_id` asociada, que necesitarás para tu solicitud de API.
{% endalert %}

[0]: https://en.wikipedia.org/wiki/E.164
[userphone]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/
[1]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[2]: {{site.baseurl}}/api/endpoints/user_data/post_user_alias/
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#aliasing-users
[4]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/#aliasing-users
[5]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/#aliasing-users
[6]: {{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/
[picture]: {% image_buster /assets/img/sms/e164.jpg %}
[customkeyword]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/custom_keyword_handling/
[subscriptionstate]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#sms-subscription-states
