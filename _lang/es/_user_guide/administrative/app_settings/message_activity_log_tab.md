---
nav_title: Registro de actividad de mensajería
article_title: Registro de actividad de mensajes
page_order: 5
page_type: reference
description: "Este artículo de referencia describe el Registro de actividad de mensajes te muestra los mensajes asociados a tus campañas y envíos. Aquí también puedes encontrar información sobre cómo entender los mensajes de registro."

---

# Registro de actividad de mensajes {#dev-console-troubleshooting}

> El **Registro de actividad de mensajes** te da la oportunidad de ver todos los mensajes (especialmente los de error) asociados a tus campañas y envíos.

Puedes ver las transacciones de la campaña de la API, solucionar problemas de mensajes fallidos y obtener información sobre cómo mejorar la entrega de notificaciones o solucionar problemas técnicos existentes.

Para acceder al registro, ve a **Configuración** > **Registro de actividad de mensajes**.

\![Registro de actividad de mensajes]({% image_buster /assets/img_archive/message_activity_log.png %})

{% alert tip %}
Además de este artículo, también te recomendamos que eches un vistazo a nuestro curso de Braze Learning [sobre Herramientas de depuración y control de calidad](https://learning.braze.com/quality-assurance-and-debugging-tools-in-the-dashboard/), que explica cómo utilizar el Registro de actividad de mensajes para llevar a cabo tu propia solución de problemas y depuración.
{% endalert %}

Puedes filtrar por el siguiente contenido registrado en el **Registro de actividad de mensajes**:

- Errores de notificación push
- Errores de mensaje abortados
- Errores del webhook
- Errores de correo
- Registros de mensajes API
- Errores de contenido conectado
- Errores de audiencia de la API REST conectada
- Errores de asignación de alias de usuario
- Errores en las pruebas A/B
- Errores SMS/MMS
- Errores de WhatsApp
- Errores de actividad en vivo
- Errores de desencadenamiento del usuario malo

Estos mensajes pueden proceder de nuestro propio sistema, de tus aplicaciones o plataformas, o de nuestros socios externos. Esto puede dar lugar a un número infinito de mensajes que pueden aparecer en este registro.

## Comprender los mensajes de registro

Para determinar el significado de tus mensajes, presta atención a la redacción de cada mensaje y a las columnas que le corresponden, ya que puede ayudarte a solucionar problemas utilizando pistas contextuales. 

Por ejemplo, si tienes una entrada de registro cuyo mensaje dice "empty-cart_app" y no estás seguro de lo que significa, mira a la izquierda en la columna **Tipo**. Si ves "Error de mensaje [abortado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/#aborting-messages) ", puedes suponer con seguridad que el mensaje era lo que se escribió como [mensaje abortado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/#aborting-messages) utilizando Liquid, y que el mensaje se abortó porque el destinatario del mensaje tenía un carrito vacío en tu aplicación.

### Mensajes comunes

Hay algunos tipos de mensajes comunes que puedes ver, y algunos incluso pueden proporcionar enlaces de solución de problemas para ayudarte a diagnosticar y solucionar problemas.

Los siguientes mensajes son a modo de ejemplo y pueden no coincidir exactamente con lo que aparece en la columna **Mensaje** de tu registro.

| Tipo de mensaje | Mensaje potencial | Descripción |
|---|---|---|
| Rebote blando | La dirección de correo electrónico same@example.com ha rebotado. | La dirección de correo electrónico era válida y el mensaje de mensajería llegó al servidor de correo del destinatario, pero fue rechazado por un problema "temporal". <br><br>Entre los motivos más comunes de rebote blando se incluyen: {::nomarkdown} <ul> <li> El buzón estaba lleno (el usuario ha superado su cuota) </li> <li> El servidor no funcionaba </li> <li> El mensaje era demasiado grande para el buzón de entrada del destinatario </li>  </ul> {:/} Si un correo electrónico ha recibido un rebote blando, normalmente lo reintentaremos en un plazo de 72 horas, pero el número de intentos de reintento varía de un receptor a otro. |
| Rebote duro | La cuenta de correo electrónico a la que has intentado acceder no existe. Comprueba dos veces que la dirección de correo electrónico del destinatario no contenga errores tipográficos o espacios innecesarios. | Tu mensaje nunca llegó al buzón de entrada de esta persona porque no había buzón de entrada al que llegar. Si quieres indagar más, los mensajes de este tipo pueden tener a veces enlaces en la columna **Ver detalles** que te permitirán ver el perfil del destinatario.|
| Bloque | El mensaje de correo no deseado se rechaza debido a la política anti-spam. | Tu mensaje ha sido clasificado como correo no deseado. Este error de correo se registra para un usuario si hemos recibido un evento del ESP indicando que el correo electrónico ha sido descartado. Puede que sólo sea para ese destinatario, pero si ves este mensaje a menudo, quizá quieras reevaluar tus hábitos de envío o el contenido de tu mensaje. Además, haz memoria: [¿calentaste tu IP]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ip_warming/)? Si no es así, ponte en contacto con Braze para que te asesore sobre cómo ponerlo en marcha.|
| Error de mensaje cancelado | empty-cart_web | Si tienes una aplicación con un carrito o creas un envío con un mensaje de cancelación en Liquid, puedes personalizar qué mensaje se te devuelve si se cancela el envío. En este caso, el mensaje devuelto es empty-cart_web.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### ¿Por qué mi mensaje no aparece aquí?

Los mensajes del Registro de Actividad de Mensajes pueden proceder de diversas fuentes: Braze, tus aplicaciones o plataformas, o nuestros socios terceros. Esto significa que hay un número infinito de mensajes que podrían aparecer en este registro; como puedes imaginar, ¡no podemos enumerarlos todos!

Por ejemplo, algunos posibles mensajes de "Bloqueo", además del enumerado en la tabla anterior, podrían ser:

- Por desgracia, los mensajes de [_IP_ADDRESS_] no se enviaron. Ponte en contacto con tu proveedor de servicios de Internet, ya que parte de su red está en nuestra lista de bloqueados.
- Mensaje rechazado debido a la política local.
- El mensaje fue bloqueado por el destinatario como correo no deseado.
- Servicio no disponible, host de cliente [_IP_ADDRESS_] bloqueado mediante Spamhaus.

## Periodo de retención del almacenamiento

Los errores de las últimas 60 horas están disponibles en los Registros de actividad de mensajes. Los registros con más de 60 horas de antigüedad se limpian y ya no son accesibles.

### Número de registros de errores almacenados

El número de registros guardados depende de varias condiciones. Por ejemplo, si se envía una campaña programada a miles de usuarios, podríamos ver una muestra de los errores en el Registro de actividad de mensajes en lugar de todos los errores. A continuación se presenta un resumen de las condiciones que afectan al número de registros que se guardarán:
- Se guardarán hasta 20 registros de errores del mismo tipo de error para la misma campaña o paso en Canvas dentro de una hora de reloj fija para los siguientes tipos de error:
    - Errores de contenido conectado
    - Abortar errores de mensaje
    - Errores del webhook
    - Errores de rechazo de SMS
    - Errores en la entrega de SMS
    - Errores de fallo de WhatsApp
    - Errores en las pruebas A/B
- Se guardarán hasta 20 registros de errores de notificación push del mismo tipo de error para la misma campaña o combinación de paso en Canvas y aplicación para los siguientes tipos de error:
    - Credencial push no válida
    - Token de notificaciones push inválido
    - Sin credenciales push
    - Errores de token
    - Cuota superada
    - Reintentos agotados
    - Carga útil no válida
    - Error inesperado
- Se guardarán hasta 100 registros de errores del mismo tipo de error para la misma aplicación dentro de una hora de reloj fija para los siguientes tipos de error:
    - Error de actividad en vivo (No hay credenciales push)
    - Error de actividad en vivo (credencial push no válida)
    - Otros errores de la actividad en vivo
    - Retroalimentación APNS Errores de token eliminados
- Se guardarán hasta 100 registros de errores del mismo tipo de error para la misma campaña o paso en Canvas dentro de una hora de reloj fija para los siguientes tipos de error:
    - Errores de rebote blando de correo electrónico
    - Errores de rebote duro de correo electrónico
    - Errores de bloqueo de correo electrónico
- Se guardarán hasta 100 registros de errores de asignación de alias de usuario para el mismo espacio de trabajo dentro de una hora de reloj fija.

