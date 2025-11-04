---
nav_title: PREGUNTAS FRECUENTES
article_title: Preguntas frecuentes sobre el correo electrónico
page_order: 14
description: "Esta página ofrece respuestas a las preguntas más frecuentes sobre el envío por correo electrónico."
channel: email

---

# Preguntas más frecuentes

> Este artículo da respuesta a algunas preguntas frecuentes sobre el correo electrónico.

### ¿Qué ocurre cuando se envía un correo electrónico y varios perfiles tienen la misma dirección de correo electrónico?

Si varios usuarios con correos electrónicos coincidentes están todos en un segmento para recibir una campaña, se elige un perfil de usuario aleatorio con esa dirección de correo electrónico en el momento del envío. De este modo, el correo electrónico sólo se envía una vez y se deduplica, lo que garantiza que el correo electrónico no llegue varias veces a la misma dirección de correo electrónico.

Ten en cuenta que esta deduplicación se produce si los usuarios a los que se dirige están incluidos en el mismo envío. Las campañas desencadenadas pueden dar lugar a múltiples envíos a la misma dirección de correo electrónico (incluso dentro de un período de tiempo en el que los usuarios podrían ser excluidos debido a la reelegibilidad) si distintos usuarios con direcciones de correo electrónico coincidentes registran el evento desencadenante en momentos diferentes. Los usuarios no son deducidos por correo electrónico a la entrada en Canvas, por lo que es posible que los usuarios no sean deducidos más allá del primer paso de un Canvas si progresan a tiempos ligeramente diferentes debido a la tasa limitada de entrada. Cuando un usuario vinculado a una dirección de correo electrónico determinada abre o hace clic en un correo electrónico, todos los perfiles de usuario que comparten la dirección de correo electrónico se marcan como que han abierto y hecho clic en la campaña.

#### Excepción: Campañas desencadenadas por la API

Las campañas desencadenadas por la API deduplicarán o enviarán deduplicados en función de dónde esté definida la audiencia. En resumen, los correos electrónicos duplicados deben dirigirse directamente como `user_ids` separado dentro de la llamada a la API para recibir múltiples detalles. Aquí tienes tres posibles escenarios para campañas desencadenadas por la API:

- **Supuesto 1: Correos electrónicos duplicados en el segmento de destino:** Si el mismo correo electrónico aparece en varios perfiles de usuario agrupados en los filtros de audiencia del panel para una campaña desencadenada por la API, sólo uno de los perfiles recibirá el correo electrónico.
- **Supuesto 2: Correos electrónicos duplicados en diferentes `user_ids` dentro del objeto destinatarios:** Si el mismo correo electrónico aparece en varios `External_user_IDs` a los que hace referencia el objeto "destinatarios", el correo electrónico se enviará dos veces.
- **Escenario 3: Correos electrónicos duplicados debido a la duplicidad de user_ids dentro del objeto destinatarios:** Si intentas añadir el mismo perfil de usuario dos veces, sólo uno de los perfiles recibirá el correo electrónico.

### ¿Se aplicarán retroactivamente las actualizaciones de mi configuración de correo electrónico saliente?

No. Las actualizaciones realizadas en la configuración del correo electrónico saliente no afectan retroactivamente a los envíos existentes. Por ejemplo, cambiar tu nombre predeterminado para mostrar en la configuración de correo electrónico no sustituirá automáticamente al nombre predeterminado existente en tus campañas activas o Lienzos. 

### ¿Qué es una "buena" tasa de entrega de correo electrónico?

Normalmente, el "número mágico" ronda el 98% de mensajes entregados con una tasa de rebote no superior al 3%. Si tu entrega cae por debajo de esa cifra, suele ser motivo de preocupación.

Sin embargo, una tasa puede ser superior al 98% y seguir teniendo problemas de capacidad de entrega. Por ejemplo, si todos tus rebotes proceden de un dominio concreto, es una señal clara de que hay un problema de reputación con ese proveedor.

Además, es posible que los mensajes se entreguen y acaben en Spam, lo que indica problemas de reputación potencialmente graves. Es importante controlar no sólo el número de mensajes que se entregan, sino también las tasas de apertura y de clics para determinar si los usuarios ven realmente los mensajes en sus buzones de entrada. Dado que los proveedores no suelen informar de todas las instancias de correo no deseado, una tasa de correos no deseados de incluso el 1% podría ser motivo de preocupación y de un análisis más detallado.

Por último, tu negocio y los tipos de correos electrónicos que envías también pueden afectar a la entrega. Por ejemplo, alguien que envíe principalmente [correos electrónicos transaccionales]({{site.baseurl}}/api/api_campaigns/transactional_api_campaign) debería esperar obtener una tasa mejor que alguien que envíe muchos mensajes de marketing.

### ¿Por qué mis métricas de entrega de correo electrónico no suman el 100%?

Las métricas de entrega de correo electrónico (entregas, rebotes y tasa de spam) pueden no sumar el 100% debido a los correos electrónicos que son rebotados suavemente y luego no entregados tras el periodo de reintento de hasta 72 horas.

Los rebotes blandos son correos electrónicos que rebotan debido a un problema temporal o transitorio, como "buzón lleno", "servidor no disponible temporalmente", etc. Si un correo electrónico rebotado suavemente sigue sin entregarse después de 72 horas, este correo electrónico no se tendrá en cuenta en las métricas de entrega de la campaña.

### ¿Qué son los píxeles de seguimiento de apertura?

[Los píxeles de seguimiento de apertura]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#changing-location-of-tracking-pixel) aprovechan el dominio de seguimiento de clics de correo electrónico de un remitente para realizar un seguimiento de los eventos de apertura de correo electrónico. El píxel es una etiqueta de imagen añadida al HTML del correo electrónico. Suele ser el último elemento HTML dentro de la etiqueta body. Cuando un usuario carga su correo electrónico, se realiza una solicitud para rellenar la imagen desde el dominio de seguimiento de marca, que registra un evento de apertura.

### ¿Qué ocurre cuando se detiene una campaña de correo electrónico o Canvas?

Se impedirá a los usuarios entrar en el Canvas y no se enviarán más mensajes. Para las campañas de correo electrónico y los lienzos, el botón de parada no significa que el envío se detenga inmediatamente. Esto se debe a que, cuando se envían las solicitudes de envío, no se puede impedir que se entreguen al usuario.

### ¿Por qué veo más clics en los correos electrónicos que aperturas?

Puede que veas más clics que aperturas por alguna de las siguientes razones:
- Los usuarios realizan varios clics en el cuerpo del correo electrónico con una sola apertura.
- Los usuarios hacen clic en algunos enlaces de correo electrónico dentro del panel de vista previa de sus teléfonos. En este caso, Braze registra este correo electrónico como clicado pero no abierto.
- Los usuarios vuelven a abrir un correo electrónico que habían visto previamente.

### ¿Por qué no veo ni aperturas ni clics en los correos electrónicos?

Puede que no veas ni aperturas ni clics en el correo electrónico si hay un error de configuración en tu dominio de seguimiento. Esto puede deberse a cualquiera de las siguientes razones:
- Hay un problema de SSL en el que las URL de seguimiento son `http` en lugar de `https`.
- Hay un problema con tu CDN por el que no se rellena la cadena del agente de usuario en los eventos de apertura, de clic o en ambos.

### ¿Cuáles son los riesgos potenciales de desencadenar clics en el servidor?

Algunos elementos de un mensaje electrónico, como los mensajes demasiado largos o demasiados signos de exclamación, pueden desencadenar respuestas de seguridad por correo electrónico. Estas respuestas pueden afectar a los informes, a la reputación de la IP y pueden hacer que los usuarios se den de baja. 

Para conocer las mejores prácticas sobre cómo gestionar estas respuestas, consulta [Manejar los aumentos de las tasas de clics]({{site.baseurl}}/help/help_articles/email/open_rates/).

### ¿Puede Braze hacer un seguimiento de los enlaces para cancelar suscripción contabilizados en la métrica "Cancelar suscripción"?

Braze realiza un seguimiento de los enlaces para cancelar suscripción si se utiliza el siguiente Liquid en los correos electrónicos: {%raw%}`${set_user_to_unsubscribed_url}`{%endraw%}

### ¿Puedo añadir un enlace "ver este correo electrónico en un navegador" a mis correos electrónicos?

No, Braze no ofrece esta funcionalidad. Esto se debe a que una mayoría cada vez mayor del correo electrónico se abre en dispositivos móviles y clientes de correo electrónico modernos, que reproducen imágenes y contenidos sin problemas.

**Solución:** Para conseguir este mismo resultado, puedes alojar el contenido de tu correo electrónico en una página de destino externa (como tu sitio web), a la que luego se puede enlazar desde la campaña de correo electrónico que estás creando utilizando la herramienta **Enlace** al editar el cuerpo del correo electrónico.

