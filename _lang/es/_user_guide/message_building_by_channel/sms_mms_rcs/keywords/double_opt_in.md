---
nav_title: Doble adhesión voluntaria
article_title: Doble adhesión voluntaria
description: "Este artículo de referencia cubre la característica de doble adhesión voluntaria, y explica cómo habilitar la característica, seleccionar palabras clave de adhesión voluntaria y mensajes de respuesta, e introducir usuarios en el flujo de trabajo de doble adhesión voluntaria a través de las actualizaciones de suscripción que se producen en la API REST, el SDK y las actualizaciones del centro de preferencias."
page_type: reference
page_order: 2
channel:
  - SMS
  - MMS
  - RCS
---

# Doble adhesión voluntaria

> La característica de doble adhesión voluntaria te permite exigir a los usuarios que confirmen explícitamente su intención de adhesión voluntaria antes de que puedan recibir mensajes SMS, MMS o RCS. Esto te ayuda a centrarte en los usuarios que tienen más probabilidades de interactuar o están interactuando con el canal, y a seguir las mejores prácticas de cumplimiento.

Cuando está activada la doble adhesión voluntaria, se envía a los usuarios un mensaje en el que se les pide su consentimiento explícito antes de que puedan recibir mensajes de tus campañas o Lienzos. 

Aunque no es un requisito explícito de la Ley de Protección del Consumidor Telefónico de 1991 (TCPA), Braze recomienda que configures la doble adhesión voluntaria para confirmar que los usuarios son conscientes y consienten en formar parte de tu programa de SMS, MMS o RCS. Para obtener más información sobre el cumplimiento, consulta [Leyes, normativas y prevención de abusos para SMS, MMS y RCS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/laws_and_regulations/).

## Flujos de trabajo de doble adhesión voluntaria

La doble adhesión voluntaria te permite obtener el consentimiento explícito mediante campañas de adhesión entrantes y salientes.

### Salida

Cuando un usuario facilita su número de teléfono, se le envía un mensaje en el que se le pide su consentimiento.

¡\![Captura de pantalla de un mensaje SMS saliente con el texto de la marca: "¡Bienvenido a las actualizaciones de texto de BRAND! 1 msg a la semana para las últimas ofertas. Responde Y para la adhesión voluntaria", los usuarios responden "Y", y la marca responde "¡Gracias! Ahora estás adherido voluntariamente a las alertas de BRAND. Aquí tienes un código promocional SMS10 para un 10% de descuento en tu primera compra!"]({% image_buster /assets/img/double_opt_in_outbound.png %}){:style="max-width:40%;"}

### Entrada

Cuando un usuario envía un mensaje que contiene una palabra clave de adhesión voluntaria, se le envía un mensaje que solicita su consentimiento.

Captura de pantalla de un mensaje SMS entrante en el que un usuario envía "ÚNETE" y recibe la respuesta "Responde Y para confirmar que quieres UNIRTE a nuestro programa de SMS. 3msg/semana, envía un mensaje de texto a STOP en cualquier momento para PARAR, luego envía un mensaje de texto a "Y".]({% image_buster /assets/img/double_opt_in_inbound.png %}){:style="max-width:40%;"}

## Habilitación de la doble adhesión voluntaria

Para activar la doble adhesión voluntaria, ve a la tabla **Palabras clave globales** del grupo de suscripción correspondiente y haz clic en **Editar** en la **categoría Palabras clave de adhesión voluntaria**. A continuación, selecciona tu método de adhesión voluntaria**(Opt-In** o **Doble Opt-In**). Al seleccionar **Doble adhesión** voluntaria se ampliará la página para mostrar [campos configurables](#configurable-fields) adicionales.

En la sección Método de adhesión voluntaria puedes elegir entre dos métodos de adhesión voluntaria: Adhesión voluntaria y doble adhesión.]({% image_buster /assets/img/double_opt_in_method.png %}){:style="max-width:50%;"}

### Campos configurables {#configurable-fields}

| Categoría   |    Campos    | Descripción   
| ----------- |----------- |---------------- 
| Mensaje de adhesión voluntaria | Palabras clave | Estas son las palabras clave que un usuario puede escribir para indicar su intención de adhesión voluntaria. `START` es una palabra clave obligatoria. Este mensaje de adhesión voluntaria también se enviará al usuario cuando se actualice su estado de suscripción mediante las fuentes indicadas en la sección [Fuentes de suscripción](#subscription-sources).
| | Mensaje de respuesta | Es la respuesta inicial que recibirá un usuario tras enviar un mensaje de texto con una palabra clave de adhesión voluntaria (por ejemplo, "Responde Y para confirmar que deseas recibir mensajes de este número. Msg&Data Pueden aplicarse tasas". )
| Confirmación de adhesión voluntaria doble | Palabras clave | Estas son las palabras clave con las que un usuario puede responder para confirmar su intención de adhesión voluntaria. Se requiere al menos una palabra clave. Estas palabras clave deben especificarse en el campo **Mensaje de adhesión voluntaria de respuesta**.
| | Mensaje de respuesta | Esta es la respuesta de confirmación que recibirá un usuario después de que haya confirmado explícitamente su adhesión voluntaria y ahora pueda recibir mensajes. El estado del grupo de suscripción del usuario se establecerá en `Subscribed`.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Cuando un usuario recibe un mensaje de adhesión voluntaria, dispone de 30 días para confirmar su intención de adhesión. Si un usuario desea suscribirse una vez transcurrido el plazo de 30 días, debe enviar un mensaje de texto con una palabra clave de adhesión voluntaria para iniciar de nuevo el flujo de trabajo de doble adhesión.

Los campos configurables tienen dos secciones, Solicitud de adhesión voluntaria y Confirmación de adhesión voluntaria doble, cada una con los campos Palabras clave y Mensaje de respuesta.]({% image_buster /assets/img/double_opt_in_fields.png %})

## Estado del grupo de suscripción

Sólo después de que el usuario complete el flujo de trabajo de doble adhesión, su [estado del grupo de suscripción]({{site.baseurl}}/sms_rcs_subscription_groups/) se actualiza a `Subscribed`. Si el usuario comienza el flujo de trabajo pero no lo completa, permanece en `Unsubscribed` y no se le pueden enviar mensajes desde ese grupo de suscripción.

Los usuarios también pueden entrar en el flujo de trabajo de adhesión voluntaria doble si están [suscritos desde otras fuentes]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group#how-users-sms-subscription-groups-get-set) (por ejemplo, API REST, SDK).

## Fuentes de suscripción {#subscription-sources}

Los usuarios también pueden entrar en el flujo de trabajo de la doble adhesión voluntaria a través de las actualizaciones de suscripción que se producen fuera de los mensajes entrantes. Estas fuentes incluyen actualizaciones de la API REST, el SDK y el centro de preferencias. Cuando un usuario entra en el flujo de trabajo de adhesión voluntaria doble a través de estas fuentes, recibirá el **mensaje de respuesta a la solicitud de adhesión voluntaria**.

Cada fuente de suscripción tiene un comportamiento de inscripción diferente, como se describe en la tabla siguiente.

Fuente    | Comportamiento de adhesión voluntaria doble   
----------- | -----------
SDK | Los usuarios entrarán automáticamente en el flujo de trabajo de doble adhesión voluntaria cuando se suscriban a través del SDK de Braze.
API REST | Los usuarios pueden entrar en el flujo de trabajo cuando el estado de suscripción se establece a través de `/subscription/status/set`, `/v2/subscription/status/set` o `/users/track` y el parámetro opcional `use_double_opt_in_logic` se pasa como `true` (por ejemplo, [{"subscription_group_id": "subscription_group_identifier", "subscription_state": "suscrito", "use_double_opt_in_logic": true}]). Si se omite este parámetro, los usuarios no entrarán en el flujo de trabajo de doble adhesión voluntaria.
Shopify | Los usuarios no entrarán en el flujo de trabajo de adhesión voluntaria doble cuando su estado de suscripción esté configurado por nuestra integración de Shopify.
Importación de usuarios | Los usuarios no entrarán en el flujo de trabajo de adhesión voluntaria doble cuando su estado de suscripción se establezca mediante la Importación de usuarios.
[Centro de preferencias]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center) | Los usuarios entrarán automáticamente en el flujo de trabajo de doble adhesión voluntaria cuando se suscriban a través de un centro de preferencias.
Paso de actualización de usuario | Los usuarios pueden entrar en el flujo de trabajo de adhesión voluntaria doble cuando se establece su estado de suscripción a través del paso Actualización de usuario y se pasa el parámetro opcional `use_double_opt_in_logic` como `true`. Si se omite este parámetro, los usuarios no entrarán en el flujo de trabajo de doble adhesión voluntaria.
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Soporte multilingüe
Para los mensajes entrantes, se admite la doble adhesión voluntaria para todos los idiomas definidos en el grupo de suscripción. Esto significa que puedes definir tus autorespuestas en diferentes idiomas y Braze enviará la autorespuesta asociada a un idioma específico cuando se reciba una palabra clave que coincida.

A los usuarios que entren en el flujo de trabajo de doble adhesión voluntaria a través de actualizaciones de suscripción que se produzcan fuera de los mensajes entrantes (por ejemplo, SDK, API REST, Shopify) sólo se les enviarán las palabras clave en inglés.

