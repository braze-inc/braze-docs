---
nav_title: Registro de actividad de mensajes
article_title: Registro de actividad de mensajes
page_order: 5
page_type: reference
description: "Este artículo de referencia describe el Registro de actividad de mensajes le muestra los mensajes asociados a sus campañas y envíos. Aquí también encontrará información sobre cómo entender los mensajes de registro."

---

# Registro de actividad de mensajes {#dev-console-troubleshooting}

> El **registro de actividad de mensajes** le ofrece la oportunidad de ver todos los mensajes (especialmente los mensajes de error) asociados a sus campañas y envíos.

Puede ver las transacciones de campaña de la API, solucionar problemas de mensajes fallidos y obtener información sobre cómo mejorar la entrega de notificaciones o resolver problemas técnicos existentes.

Para acceder al registro, ve a **Configuración** > **Registro de actividad de mensajes**.

![Registro de actividad de mensajes]({% image_buster /assets/img_archive/message_activity_log.png %})

{% alert tip %}
Además de este artículo, también recomendamos consultar nuestro curso Braze Learning sobre [herramientas de control de calidad y depuración](https://learning.braze.com/quality-assurance-and-debugging-tools-in-the-dashboard/), que trata sobre cómo utilizar el registro de actividad de mensajes para llevar a cabo su propia solución de problemas y depuración.
{% endalert %}

Puede filtrar por el siguiente contenido registrado en el **Registro de actividad de mensajes**:

- Errores en las notificaciones push
- Errores de mensaje abortados
- Errores de webhook
- Errores de correo
- Registros de mensajes API
- Errores en los contenidos conectados
- Errores de audiencia de la API REST conectada
- Errores de asignación de alias de usuario
- Errores en las pruebas A/B
- Errores SMS/MMS
- Errores de WhatsApp
- Errores de actividad en vivo
- Errores de desencadenamiento del usuario malo

Estos mensajes pueden proceder de nuestro propio sistema, de sus aplicaciones o plataformas, o de nuestros socios externos. Esto puede dar lugar a un número infinito de mensajes que pueden aparecer en este registro.

## Comprender los mensajes de registro

Para determinar el significado de sus mensajes, preste atención a la redacción de cada mensaje y a las columnas que se corresponden con él, ya que puede ayudarle a solucionar problemas utilizando pistas contextuales. 

Por ejemplo, si tiene una entrada de registro cuyo mensaje dice "empty-cart_app" y no está seguro de lo que significa, mire a la izquierda en la columna **Tipo**. Si ves "Error de mensaje anulado", puedes suponer con seguridad que el mensaje era lo que se escribió como [mensaje anulado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/#aborting-messages) utilizando Liquid, y que el mensaje se anuló porque el destinatario del mensaje tenía un carrito vacío en tu aplicación.

### Mensajes comunes

Hay algunos tipos de mensajes comunes que puede ver, y algunos incluso pueden proporcionar enlaces de solución de problemas para ayudarle a diagnosticar y solucionar problemas.

Los siguientes mensajes se incluyen a modo de ejemplo y pueden no coincidir exactamente con lo que aparece en la columna **Mensaje** de su registro.

| Tipo de mensaje | Mensaje potencial | Descripción |
|---|---|---|
| Rebote suave | La dirección de correo electrónico same@example.com arrojó un rebote blando. | La dirección de correo electrónico era válida y el mensaje llegó al servidor de correo del destinatario, pero fue rechazado por un problema "temporal". <br><br>Entre las razones más comunes del rebote blando se incluyen: {::nomarkdown} <ul> <li> El buzón estaba lleno (el usuario ha superado su cuota) </li> <li> El servidor no funcionaba </li> <li> El mensaje era demasiado grande para la bandeja de entrada del destinatario </li>  </ul> {:/} Si un correo electrónico arroja un rebote blando, normalmente lo reintentaremos en un plazo de 72 horas, pero el número de intentos de reintento varía de un receptor a otro. |
| Rebote duro | La cuenta de correo electrónico a la que ha intentado acceder no existe. Compruebe que la dirección de correo electrónico del destinatario no contenga erratas ni espacios innecesarios. | Tu mensaje nunca llegó a la bandeja de entrada de esta persona porque no había bandeja de entrada a la que llegar. Si quieres profundizar más, los mensajes de este tipo pueden tener a veces enlaces en la columna **Ver detalles** que te permitirán ver el perfil del destinatario.|
| Bloquear | El mensaje spam es rechazado debido a la política anti-spam. | Tu mensaje ha sido clasificado como spam. Este error de correo se registra para un usuario si hemos recibido un evento del ESP indicando que el correo electrónico ha sido descartado. Puede que sólo sea para ese destinatario, pero si ves este mensaje a menudo, quizá quieras reevaluar tus hábitos de envío o el contenido de tu mensaje. Además, haz memoria: [¿calentaste tu IP]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ip_warming/)? Si no, ponte en contacto con Braze para que te asesore sobre cómo ponerlo en marcha.|
| Error de mensaje anulado | empty-cart_web | Si tiene una aplicación con un carrito o crea un envío con un mensaje de cancelación en el Líquido, puede personalizar qué mensaje se le devuelve si se cancela el envío. En este caso, el mensaje devuelto es empty-cart_web.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### ¿Por qué mi mensaje no aparece aquí?

Los mensajes del registro de actividad de mensajes pueden proceder de diversas fuentes: Braze, sus aplicaciones o plataformas, o nuestros socios terceros. Esto significa que hay un número infinito de mensajes que podrían aparecer en este registro: como puedes imaginar, ¡no podemos enumerarlos todos!

Por ejemplo, algunos posibles mensajes de "Bloqueo", además del enumerado en la tabla anterior, podrían ser:

- Lamentablemente, los mensajes de [_IP_ADDRESS_] no se enviaron. Póngase en contacto con su proveedor de servicios de Internet, ya que parte de su red está en nuestra lista de bloqueados.
- Mensaje rechazado debido a la política local.
- El mensaje fue bloqueado por el receptor como spam.
- Servicio no disponible, host del cliente [_IP_ADDRESS_] bloqueado mediante Spamhaus.

## Periodo de retención del almacenamiento

Los errores de las últimas 60 horas están disponibles en los Registros de actividad de mensajes. Los registros con más de 60 horas de antigüedad se limpian y ya no son accesibles. 

### Número de registros de errores almacenados

El número de registros guardados depende de varias condiciones. Por ejemplo, si se envía una campaña programada a miles de usuarios, podríamos ver una muestra de los errores en el Registro de actividad de mensajes en lugar de todos los errores.

Aquí tienes un resumen de las condiciones que afectan al número de registros que se guardarán:
- Se guardarán hasta 20 registros de errores de Contenido conectado para la misma campaña dentro de una hora de reloj fija.
- Se guardarán hasta 100 registros de errores del mismo tipo de error en una hora de reloj fija por espacio de trabajo para los siguientes tipos de error:
    - Errores de mensaje abortados
    - Errores de webhook
    - Errores en las notificaciones push
    - Errores de actividad en vivo
    - Errores de desencadenamiento del usuario malo

