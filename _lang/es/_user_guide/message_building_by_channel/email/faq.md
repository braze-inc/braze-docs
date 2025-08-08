---
nav_title: Preguntas frecuentes
article_title: Preguntas frecuentes sobre el correo electrónico
page_order: 14
description: "Esta página ofrece respuestas a las preguntas más frecuentes sobre los mensajes de correo electrónico."
channel: email

---

# Preguntas más frecuentes

> Este artículo da respuesta a algunas preguntas frecuentes sobre el correo electrónico.

### ¿Qué ocurre cuando se envía un correo electrónico y varios perfiles tienen la misma dirección de correo electrónico?

Si varios usuarios con correos electrónicos coincidentes están todos en un segmento para recibir una campaña, se elige un perfil de usuario aleatorio con esa dirección de correo electrónico en el momento del envío. De este modo, el correo electrónico sólo se envía una vez y se deduplica, lo que garantiza que no llegue varias veces a la misma dirección de correo electrónico.

Ten en cuenta que esta deduplicación se produce si los usuarios a los que se dirige están incluidos en el mismo envío. Las campañas activadas pueden dar lugar a múltiples envíos a la misma dirección de correo electrónico (incluso dentro de un período de tiempo en el que los usuarios podrían ser excluidos debido a la reelegibilidad) si diferentes usuarios con direcciones de correo electrónico coincidentes registran el evento de activación en diferentes momentos. Los usuarios no son deducidos por correo electrónico al entrar en el Canvas, por lo que es posible que los usuarios no sean deducidos más allá del primer paso de un Canvas si están progresando en tiempos ligeramente diferentes debido a la tasa de entrada limitada. Cuando un usuario vinculado a una dirección de correo electrónico determinada abre o hace clic en un correo electrónico, todos los perfiles de usuario que comparten la dirección de correo electrónico se marcan como que han abierto y hecho clic en la campaña.

#### Excepción: Campañas activadas por API

Las campañas desencadenadas por la API deduplicarán o enviarán deduplicados en función de dónde esté definida la audiencia. En resumen, los correos electrónicos duplicados deben dirigirse directamente como `user_ids` separado dentro de la llamada a la API para recibir múltiples detalles. A continuación se presentan tres posibles escenarios para campañas desencadenadas por API.

- **Escenario 1: Correos electrónicos duplicados en el segmento de destino:** Si el mismo correo electrónico aparece en varios perfiles de usuario agrupados en los filtros de audiencia del panel de control para una campaña activada por API, sólo uno de los perfiles recibirá el correo electrónico.
- **Escenario 2: Correos duplicados en diferentes `user_ids` dentro del objeto destinatarios:** Si el mismo correo electrónico aparece dentro de varios `External_user_IDs` referenciados por el objeto `recipients``, el correo electrónico se enviará dos veces.
- **Escenario 3: Correos duplicados debido a user_ids duplicados en el objeto destinatario:** Si intenta añadir el mismo perfil de usuario dos veces, sólo uno de los perfiles recibirá el correo electrónico.

### ¿Cómo compruebo si una dirección de correo electrónico ya está asociada a un usuario?

Antes de crear un usuario a través de la API o el SDK, llama al punto final [`/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) y especifica la dirección `email_address` del usuario. Si devuelve un perfil de usuario, ese usuario Braze ya está asociado a esa dirección de correo electrónico.

Te recomendamos encarecidamente que busques direcciones de correo electrónico únicas cuando se creen nuevos usuarios, y que evites pasar o importar usuarios con la misma dirección de correo electrónico. De lo contrario, puedes tener consecuencias no deseadas que afecten al envío de mensajes, la segmentación, los informes y otras características.

Por ejemplo, supongamos que tienes perfiles duplicados, pero determinados atributos o eventos personalizados residen sólo en un perfil. Cuando intentas desencadenar campañas o Lienzos con criterios múltiples, Braze no puede identificar al usuario como elegible porque hay dos perfiles de usuario. O, si una campaña se dirige a una dirección de correo electrónico compartida por dos usuarios, la página **Buscar usuarios** mostrará que ambos perfiles de usuario han recibido la campaña.

### ¿Se aplicarán retroactivamente las actualizaciones de mi configuración de correo electrónico saliente?

No. Las actualizaciones realizadas en la configuración del correo electrónico saliente no afectan retroactivamente a los envíos existentes. Por ejemplo, cambiar el nombre de visualización predeterminado en la configuración de correo electrónico no sustituirá automáticamente el nombre de visualización predeterminado existente en sus campañas activas o lienzos. 

### ¿Qué es una "buena" tasa de entrega de correo electrónico?

Normalmente, el "número mágico" se sitúa en torno al 98% de mensajes entregados con una tasa de rebote no superior al 3%. Si el parto cae por debajo de esa cifra, suele ser motivo de preocupación.

Sin embargo, una tasa puede ser superior al 98 % y seguir teniendo problemas de capacidad de entrega. Por ejemplo, si todos los rebotes proceden de un dominio concreto, es una señal clara de que hay un problema de reputación con ese proveedor.

Además, es posible que los mensajes se entreguen y acaben en Spam, lo que indica problemas de reputación potencialmente graves. Es importante controlar no sólo el número de mensajes que se entregan, sino también las tasas de apertura y clics para determinar si los usuarios ven realmente los mensajes en sus bandejas de entrada. Dado que los proveedores no suelen informar de todos los casos de spam, una tasa de spam de incluso el 1% podría ser motivo de preocupación y análisis más detallado.

Por último, su negocio y los tipos de correos electrónicos que envía también pueden afectar a la entrega. Por ejemplo, alguien que envíe principalmente [correos electrónicos transaccionales]({{site.baseurl}}/api/api_campaigns/transactional_api_campaign) debería esperar obtener una tasa mejor que alguien que envíe muchos mensajes de marketing.

### ¿Por qué mis métricas de entrega de correo electrónico no suman el 100 %?

Las métricas de entrega de correo electrónico (entregas, rebotes y tasa de spam) pueden no sumar el 100% debido a los correos electrónicos que son rebotados suavemente y luego no se entregan después del período de reintento de hasta 72 horas.

Los rebotes blandos son correos electrónicos que rebotan debido a un problema temporal o transitorio, como "buzón lleno", "servidor temporalmente no disponible", etc. Si un correo electrónico que arroja un rebote blando sigue sin entregarse después de 72 horas, no se tendrá en cuenta en las métricas de entrega de la campaña.

### ¿Qué son los píxeles de seguimiento de apertura?

[Los píxeles de seguimiento de apertura]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#changing-location-of-tracking-pixel) aprovechan el dominio de seguimiento de clics de correo electrónico de un remitente para realizar un seguimiento de los eventos de apertura de correo electrónico. El píxel es una etiqueta de imagen que se añade al código HTML del correo electrónico. Suele ser el último elemento HTML dentro de la etiqueta del cuerpo. Cuando un usuario carga su correo electrónico, se realiza una solicitud para rellenar la imagen desde el dominio de seguimiento de marca, que registra un evento de apertura.

### ¿Qué ocurre cuando se interrumpe una campaña de correo electrónico o Canvas?

Se impedirá a los usuarios entrar en el Lienzo y no se enviarán más mensajes. Para las campañas de correo electrónico y los lienzos, el botón de parada no significa que el envío se detenga inmediatamente. Esto se debe a que cuando se envían las solicitudes de envío, no se puede impedir que se entreguen al usuario.

### ¿Por qué veo más clics en los correos electrónicos que aperturas?

Puede que veas más clics que aperturas por alguna de las siguientes razones:
- Los usuarios hacen varios clics en el cuerpo del correo electrónico con una sola apertura.
- Los usuarios hacen clic en algunos enlaces de correo electrónico dentro del panel de vista previa de sus teléfonos. En este caso, Braze registra este correo electrónico como pulsado pero no abierto.
- Los usuarios vuelven a abrir un correo electrónico que habían previsualizado anteriormente.

### ¿Por qué no veo ni aperturas ni clics en los correos electrónicos?

Puede que no veas ni aperturas ni clics en el correo electrónico si hay un error de configuración en tu dominio de seguimiento. Esto puede deberse a cualquiera de las siguientes razones:
- Hay un problema de SSL en el que las URL de seguimiento son `http` en lugar de `https`.
- Hay un problema con tu CDN por el que no se rellena la cadena del agente de usuario en los eventos de apertura, de clic o en ambos.

### ¿Cuáles son los riesgos potenciales de provocar clics en el servidor?

Ciertos elementos de un mensaje de correo electrónico, como los mensajes demasiado largos o con demasiados signos de exclamación, pueden desencadenar respuestas de seguridad. Estas respuestas pueden afectar a los informes, a la reputación de la IP y pueden hacer que los usuarios se den de baja. 

Para conocer las mejores prácticas sobre cómo gestionar estas respuestas, consulte [Cómo gestionar el aumento del porcentaje de clics]({{site.baseurl}}/help/help_articles/email/open_rates/).

### ¿Cómo puedo eliminar una dirección de correo electrónico de la lista de correo no deseado o rebotado?

Puedes eliminar los correos electrónicos rebotados y los de la lista de correo no deseado con los siguientes puntos finales:
- [`/email/bounce/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_hard_bounces)
- [`/email/spam/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_spam)

### ¿Cómo puedo comprobar el grupo de suscripción de correo electrónico de un usuario?

- **Perfil del usuario:** Se puede acceder a los perfiles de usuario individuales a través del panel Braze desde la página [Buscar usuarios]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/#access-profiles). Aquí puede buscar perfiles de usuario por dirección de correo electrónico, número de teléfono o ID de usuario externo. Dentro del perfil de un usuario, en la pestaña Compromiso, puede ver los grupos de suscripción de correo electrónico de un usuario.
- **API REST:** El grupo de suscripción de perfiles de usuario individuales se puede ver mediante el [punto final Listar grupos de suscripción de usuario]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/) o [Listar estado de grupo de suscripción de usuario]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/) mediante la API REST de Braze. 

### ¿Cómo puedo actualizar el grupo de suscripción de correo electrónico de un usuario?

Se impedirá a los usuarios entrar en el Lienzo y no se enviarán más mensajes. Para las campañas de correo electrónico y los lienzos, el botón de parada no significa que el envío se detenga inmediatamente. Esto se debe a que, una vez enviadas las solicitudes de envío, no se puede impedir que se entreguen al usuario.

### ¿Puede Braze hacer un seguimiento de los enlaces para cancelar suscripción contabilizados en la métrica "Cancelar suscripción"?

Braze rastrea los enlaces de cancelación de suscripción si se utiliza el siguiente Liquid en los correos electrónicos: {%raw%}`${set_user_to_unsubscribed_url}`{%endraw%}

### ¿Puedo añadir un enlace "ver este correo en un navegador" a mis correos electrónicos?

No, Braze no ofrece esta funcionalidad. Esto se debe a que una mayoría cada vez mayor del correo electrónico se abre en dispositivos móviles y clientes de correo modernos, que renderizan imágenes y contenidos sin problemas.

**Solución:** Para lograr este mismo resultado, puede alojar el contenido de su correo electrónico en una página de destino externa (como su sitio web), a la que se puede enlazar desde la campaña de correo electrónico que está creando utilizando la herramienta **Enlace** al editar el cuerpo del correo electrónico.

