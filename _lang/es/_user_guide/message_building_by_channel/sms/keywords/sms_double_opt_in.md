---
nav_title: Doble adhesión voluntaria por SMS
article_title: Doble adhesión voluntaria por SMS
description: "Este artículo de referencia trata sobre la función de opt-in doble por SMS y explica cómo activar la función, seleccionar palabras clave de opt-in y mensajes de respuesta, e introducir usuarios en el flujo de trabajo de opt-in doble por SMS mediante actualizaciones de suscripción que se producen en las actualizaciones de la API REST, el SDK y el centro de preferencias."
page_type: reference
page_order: 2
channel:
  - SMS
---

# Inscripción doble por SMS

> La característica de doble adhesión voluntaria por SMS te permite exigir a los usuarios que confirmen explícitamente su intención de adhesión antes de poder recibir mensajes SMS. Esto te ayuda a centrarte en los usuarios que tienen más probabilidades de interactuar o están interactuando con el SMS.

Cuando el doble opt-in por SMS está activado, se envía a los usuarios un mensaje SMS que solicita su consentimiento explícito antes de que puedan recibir mensajes de tus campañas o Canvases. 

Aunque no es un requisito explícito de la Ley de Protección del Consumidor Telefónico de 1991 (TCPA), Braze recomienda que configure el doble opt-in de SMS para confirmar que los usuarios son conscientes y consienten formar parte de su programa de SMS. Para obtener más información sobre el cumplimiento de SMS, consulte [las leyes, normativas y prevención de abusos de SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_laws_and_regulations/).

## Flujos de trabajo de doble adhesión voluntaria por SMS

Los usuarios pueden dar su consentimiento explícito a través de mensajes SMS salientes o entrantes.

### Doble inclusión de SMS salientes

Cuando un usuario facilita su número de teléfono, se le envía un mensaje SMS en el que se le pide su consentimiento.

![Captura de pantalla de un mensaje SMS saliente con el texto de la marca: "¡Bienvenido a las actualizaciones de texto de BRAND! 1 mensaje a la semana para las últimas ofertas. Responde Y para la adhesión voluntaria", los usuarios responden "Y", y la marca responde "¡Gracias! Ahora estás adherido voluntariamente a las alertas de BRAND. Aquí tienes un código promocional SMS10 para un 10 % de descuento en tu primera compra!"][2]{:style="max-width:40%;"}

### Doble adhesión voluntaria por SMS entrantes

Cuando un usuario envía un mensaje SMS que contiene una palabra clave opt-in, se le envía un mensaje SMS que solicita su consentimiento.

![Captura de pantalla de un mensaje SMS entrante en el que un usuario envía "JOIN" y recibe la respuesta "Reply Y to confirm you want to JOIN our SMS program. 3 msj/semana, envía un mensaje de texto a STOP en cualquier momento para PARAR, luego envía un mensaje de texto a "Y".][1]{:style="max-width:40%;"}

## Habilitación de la doble adhesión voluntaria por SMS

Para activar la adhesión voluntaria doble de SMS, vaya a la tabla **Palabras clave globales de SMS** en el grupo de suscripción correspondiente y haga clic en **Editar** en la **categoría Palabras clave de adhesión voluntaria**. A continuación, selecciona tu método de adhesión voluntaria**(Opt-In** o **Doble Opt-In**). Al seleccionar **Double Opt-In** se ampliará la página para mostrar [campos configurables](#configurable-fields) adicionales.

![En la sección Método de adhesión voluntaria puedes elegir entre dos métodos de adhesión voluntaria: Adhesión voluntaria y doble adhesión voluntaria.][3]{:style="max-width:50%;"}

### Campos configurables {#configurable-fields}

| Categoría   |    Campos    | Descripción   
| ----------- |----------- |---------------- 
| Mensaje de adhesión voluntaria | Palabras claves | Estas son las palabras clave que un usuario puede escribir para indicar su intención de inclusión. `START` es una palabra clave obligatoria. Este aviso de suscripción también se enviará al usuario cuando su estado de suscripción sea actualizado por las fuentes enumeradas en la sección [Fuentes de suscripción](#subscription-sources).
| | Mensaje de respuesta | Es la respuesta inicial que recibirá un usuario tras enviar un mensaje de texto con una palabra clave de inclusión (por ejemplo, "Responda Y para confirmar que desea recibir mensajes de este número"). Pueden aplicarse tasas de mensajes y datos.
| Confirmación de doble adhesión voluntaria | Palabras claves | Estas son las palabras clave con las que un usuario puede responder para confirmar su intención de opt-in. Se requiere al menos una palabra clave. Estas palabras clave deben especificarse en el campo **Mensaje de adhesión voluntaria de respuesta**.
| | Mensaje de respuesta | Esta es la respuesta de confirmación que recibirá un usuario después de haber confirmado explícitamente su adhesión voluntaria y que ahora puede recibir mensajes por SMS. El estado del grupo de suscripción del usuario se establecerá en `Subscribed`.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Cuando un usuario recibe un mensaje de adhesión voluntaria, dispone de 30 días para confirmar su intención de adhesión. Si un usuario desea suscribirse una vez transcurrido el plazo de 30 días, deberá enviar un mensaje de texto con una palabra clave de suscripción para iniciar de nuevo el flujo de trabajo de suscripción doble.

![Los campos configurables tienen dos secciones, Solicitud de adhesión voluntaria y Confirmación de adhesión voluntaria doble, cada una con los campos Palabras clave y Mensaje de respuesta.][4]

## Estado del grupo de suscripción

Solo después de que el usuario complete el flujo de trabajo de doble adhesión voluntaria por SMS, su [estado del grupo de suscripción]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/) se actualiza a `Subscribed`. Si el usuario inicia el flujo de trabajo pero no lo completa, permanecerá en `Unsubscribed` y no se le podrán enviar mensajes SMS desde ese grupo de suscripción.

Los usuarios también pueden entrar en el flujo de trabajo de doble adhesión por SMS si están [suscritos desde otras fuentes]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group#how-users-sms-subscription-groups-get-set) (por ejemplo, API REST, SDK).

## Fuentes de suscripción {#subscription-sources}

Los usuarios también pueden entrar en el flujo de trabajo del doble opt-in por SMS a través de actualizaciones de la suscripción que se producen fuera de los mensajes SMS entrantes. Estas fuentes incluyen actualizaciones de la API REST, el SDK y el centro de preferencias. Cuando un usuario entra en el flujo de trabajo de adhesión voluntaria doble por SMS a través de estas fuentes, recibirá el **mensaje de respuesta de solicitud de adhesión voluntaria**.

Cada fuente de suscripción tiene un comportamiento de inscripción diferente, como se describe en la siguiente tabla.

Fuente    | Comportamiento de la inscripción doble   
----------- | -----------
SDK | Los usuarios entrarán automáticamente en el flujo de trabajo de doble adhesión por SMS cuando se suscriban a través del SDK de Braze.
API REST | Los usuarios pueden introducirse en el flujo de trabajo cuando el estado de suscripción se establece a través de `/subscription/status/set`, `/v2/subscription/status/set` o `/users/track` y el parámetro opcional `use_double_opt_in_logic` se pasa como `true` (por ejemplo, [{"subscription_group_id" : "subscription_group_identifier", "subscription_state" : "subscribed", "use_double_opt_in_logic": true}]). Si se omite este parámetro, los usuarios no entrarán en el flujo de trabajo de doble adhesión voluntaria por SMS.
Shopify | Los usuarios no entrarán en el flujo de trabajo de doble adhesión por SMS cuando su estado de suscripción esté configurado por nuestra integración de Shopify.
Importación de usuarios | Los usuarios no entrarán en el flujo de trabajo de doble adhesión por SMS cuando su estado de suscripción esté configurado por la Importación de usuarios.
[Centro de preferencias]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center) | Los usuarios entrarán automáticamente en el flujo de trabajo de doble inclusión de SMS cuando se suscriban a través de un centro de preferencias.
Paso de actualización de usuario | Los usuarios pueden introducirse en el flujo de trabajo de opt-in doble por SMS cuando su estado de suscripción se establece a través del paso Actualización de usuario y el parámetro opcional `use_double_opt_in_logic` se pasa como `true`. Si se omite este parámetro, los usuarios no entrarán en el flujo de trabajo de doble adhesión voluntaria por SMS.
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Asistencia en varios idiomas
Para los mensajes entrantes, se admite la doble adhesión voluntaria por SMS para todos los idiomas definidos en el grupo de suscripción. Esto significa que puede definir sus autorespuestas en diferentes idiomas y Braze enviará la autorespuesta asociada a un idioma específico cuando se reciba una palabra clave coincidente.

A los usuarios que entren en el flujo de trabajo de opt-in doble por SMS a través de actualizaciones de suscripción que se produzcan fuera de los mensajes entrantes (por ejemplo, SDK, REST API, Shopify) sólo se les enviarán las palabras clave en inglés.

[1]: {% image_buster /assets/img/double_opt_in_inbound.png %}
[2]: {% image_buster /assets/img/double_opt_in_outbound.png %}
[3]: {% image_buster /assets/img/double_opt_in_method.png %}
[4]: {% image_buster /assets/img/double_opt_in_fields.png %}
