---
nav_title: PREGUNTAS FRECUENTES
article_title: PREGUNTAS FRECUENTES SOBRE SMS
page_order: 12
description: "Este artículo aborda algunas de las preguntas más frecuentes que surgen al configurar campañas de SMS."
page_type: FAQ
alias: /sms_faq/
channel:
  - SMS
  
---

# Preguntas más frecuentes

> ¡En esta página intentaremos responder a tus preguntas más exigentes sobre los SMS!

### ¿Puedes incluir enlaces en un SMS?

Puedes incluir cualquier enlace en cualquier campaña de SMS que desees. Sin embargo, hay que tener en cuenta algunas preocupaciones:

- Los enlaces pueden ocupar gran parte del límite de 160 caracteres de los SMS. Si incluyes un enlace y un texto, pueden aparecer dos mensajes SMS en lugar de uno solo.
- Las empresas suelen utilizar acortadores de enlaces para limitar el impacto del número de caracteres de un enlace. Sin embargo, si envías un enlace acortado a través de un código largo, los operadores pueden bloquear o denegar el mensaje, ya que pueden sospechar de la redirección del enlace.
- Utilizar un [código abreviado]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/short_and_long_codes/) sería el tipo de número más fiable para incluir enlaces.

Braze también tiene su propia característica de acortamiento de enlaces que acortará los enlaces y proporcionará análisis de click-through automáticamente. Consulta [Acortamiento de enlaces]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/link_shortening/) para más información.

### ¿Los mensajes de texto de prueba cuentan para los límites?

Sí, lo hacen. Tenlo en cuenta cuando pruebes los mensajes.

### ¿Necesita un usuario formar parte de un grupo de suscripción SMS para recibir mensajes SMS de prueba?

Sí, lo hacen. Los usuarios deben tener un número de teléfono válido y formar parte del grupo de suscripción SMS utilizado para el envío de prueba.

### ¿Necesitas limitar la tasa de envío de mensajes SMS?

La tasa de concurrencia y el rendimiento predeterminados habilitan unos 360.000 mensajes a la hora por código abreviado. Un mayor rendimiento requiere códigos abreviados adicionales.

### ¿Cómo puedo evitar los excedentes?

Aunque no podemos prometerte que no vayas a tener ocasionalmente un excedente, puedes seguir estas precauciones para disminuir las probabilidades de sobrepasar los límites asignados:

- Presta atención al número de caracteres de tu SMS. Enviar involuntariamente más de un segmento podría causar excedentes. Para más detalles, consulta nuestro [desglose por segmentos]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/#segment-breakdown).
- Calcula cuidadosamente los caracteres de tus SMS para tener en cuenta el Contenido Líquido o Conectado. El compositor de SMS de Braze en tu panel no calcula ni tiene en cuenta el uso de ninguna de estas características.
- Ten en cuenta el tipo de codificación que utiliza tu mensaje: si tu mensaje utiliza la codificación GSM-7, normalmente puedes calcular que puedes enviar un mensaje con 128 caracteres por segmento del mensaje. Si tu mensaje utiliza la codificación [UCS-2](https://en.wikipedia.org/wiki/Universal_Coded_Character_Set), normalmente puedes estimar que puedes enviar un mensaje con 67 caracteres por segmento del mensaje.
- ¡Prueba, prueba y prueba! Prueba siempre tus mensajes SMS antes de lanzarlos, especialmente cuando utilices Liquid y Contenido conectado.

### ¿Cuáles son las mejores prácticas de envío para evitar la detección de correo no deseado en los SMS?

1. Asegúrate de que las instrucciones de adhesión voluntaria y exclusión voluntaria sean claras.
2. Asegúrate de que tú (la marca) tienes una relación con el cliente.
3. Asegúrate de que el contenido es relevante para la relación y para lo que el usuario ha optado por recibir.

Para obtener más directrices sobre cómo evitar la detección de correo no deseado, visita [Directrices sobre leyes y normativas SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/laws_and_regulations/).

### ¿Cómo se crea la lógica para la adhesión voluntaria selectiva a los SMS para que los usuarios estén en el grupo de suscripción correcto?

Las palabras clave personalizadas se escribirían como eventos personalizados, por lo que te convendría crear segmentos basados en las palabras clave que los clientes pueden escribir. Por ejemplo, si un usuario opta por los SMS para mensajes VIP pero no para alertas, puedes crear un segmento VIP y un segmento de alertas, y luego asignar al usuario al segmento apropiado.

### ¿Cuántos caracteres utiliza un emoji?

Los emojis pueden ser complicados, ya que no hay un recuento de caracteres estándar para todos los emojis. Existe el riesgo de que el emoji supere el límite de caracteres y divida el SMS en varios mensajes, a pesar de que aparezca como un solo mensaje en el compositor de Braze. Cuando pruebes tus mensajes, puedes verificar mejor si un mensaje se dividirá utilizando nuestra [calculadora de segmentos]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/#segment-calculator).

### Si un usuario envía "Stop" a nuestro código abreviado, ¿se da de baja del grupo de suscripción?

¿Qué aspecto tiene eso en el perfil de usuario? El grupo de suscripción volverá a tener 2 guiones (- -), y habrá eventos personalizados para suscribirse y cancelar suscripción.

### ¿Hay alguna forma de ver si existe un alias en un perfil de usuario?

Los alias no son visibles en el perfil de usuario. Tendrías que utilizar los puntos finales de [Exportar datos de usuario]({{site.baseurl}}/api/endpoints/export/) para confirmar que los alias están configurados.

### ¿Qué son los códigos abreviados compartidos?

Con un código abreviado compartido, todos los mensajes de texto, independientemente de la empresa u organización que los envíe, llegan al dispositivo móvil del consumidor desde el mismo número de teléfono de 5-6 dígitos. Aunque los códigos abreviados compartidos tienen un coste relativamente bajo y están disponibles de inmediato, esto significa que tu empresa no tendrá un código abreviado exclusivo.

Algunas desventajas de este enfoque son:

- Si tus clientes optan por no recibir los mensajes de otra empresa que tenga un código abreviado compartido contigo, también habrán optado por no recibir tus mensajes.
- Si una empresa infringe las normas, se suspenden los mensajes de todas las empresas.
- Cuestiones de seguridad

### ¿Cómo se autorizan las URL de los SMS?

Antes de enviar mensajes SMS que contengan URL a usuarios de determinados países (por ejemplo, Suecia o los países nórdicos), debes conseguir que estas URL se registren en el operador. Ponte en contacto con tu administrador del servicio de atención al cliente Braze para que te ayude. Este proceso durará unos cinco días.  

### ¿Qué ocurre si varios usuarios tienen el mismo número de teléfono?

Cuando varios perfiles de usuario que comparten un número de teléfono (habilitado para SMS) son elegibles para una campaña basada en acciones o un componente Canvas al mismo tiempo, desencadenado por el evento de un SMS entrante, Braze deducirá los usuarios en el nivel del componente Canvas. Esto evitará que los usuarios reciban más de un SMS de un componente de Canvas, aunque varios usuarios compartan el mismo número de teléfono. 

{% alert note %}
Braze no deduplica por número de teléfono para los Lienzos programados.
{% endalert %}

Braze utilizará el siguiente flujo para determinar el perfil del destinatario:
- Comprueba qué perfil ha recibido SMS más recientemente (hasta hace 7 días); si existe alguno, envíaselo a ese usuario.
- Si ninguno de los dos había recibido SMS hasta hace 7 días, envíalo al usuario que tenga un alias de usuario de "teléfono" que coincida con el número de teléfono.
- Si no existe ninguno, envía a un perfil aleatorio entre los disponibles. 

Si recibes una palabra clave "START" o "STOP" del número de teléfono compartido, todos los perfiles de usuario se suscribirán y habilitarán para SMS o se darán de baja. Esto también se aplica a los cambios de estado de la API. Por ejemplo, si varios perfiles con diferentes ID externos tienen los mismos números de teléfono, un cambio de estado del grupo de suscripción a través de la API actualizará todos los perfiles con ese número de teléfono, aunque sólo se especifique un ID externo.

{% alert important %}
Si escalonas a tus usuarios en un Canvas y tienes horarios diferentes para cada componente del Canvas, puedes enviar a un usuario con el mismo correo electrónico o teléfono mensajes duplicados.
{% endalert %}

### ¿Las propiedades del evento del SMS capturan palabras clave en una frase?

Para que se reconozca una palabra clave dentro de una frase, (por ejemplo, "por favor, deja de mandarme mensajes"), tendrás que utilizar una declaración Liquid en el mensaje para que se reconozca la palabra concreta. Las propiedades del evento tienen un límite de 256 caracteres; en caso contrario, no hay límite de caracteres.

### ¿Por qué el panel de Braze me advierte de que se me pueden cobrar segmentos del mensaje adicionales cuando mi mensaje tiene menos de 160 (GCM-7) o 70 (UCS-2) caracteres?

Es posible que se te cobren segmentos del mensaje adicionales si incluyes personalización de Liquid en tu mensaje. La plantilla del bloque de contenido no se produce hasta que el mensaje se está preparando para ser enviado. Cuando editas un SMS con un bloque de contenido, Braze no sabe lo que contendrá el bloque de contenido, pero proporciona una estimación aproximada. Recomendamos a los usuarios que utilicen el panel de prueba para obtener una vista previa del mensaje y comprender mejor qué esperar.

### ¿Qué es un `app_id` en el objeto SMS API?

La clave de API identificadora de la aplicación o `app_id` es un parámetro que asocia la actividad a una aplicación concreta de tu espacio de trabajo. Designa con qué aplicación del espacio de trabajo estás interactuando. Por ejemplo, tendrás un `app_id` para tu aplicación iOS, un `app_id` para tu aplicación Android y un `app_id` para tu integración Web. 

Puedes encontrar tu `app_id` navegando hasta **Configuración** > **Configuración de la aplicación** y localizando la sección **Identificación**.

### ¿Cómo se me facturarán los SMS?

Además de las tarifas de los códigos abreviados y largos, Braze proporciona una asignación de mensajes SMS para distintos países. Es decir, trabajamos contigo para establecer un determinado número de segmentos del mensaje para diferentes países, que utilizarás para enviar campañas de SMS. La facturación se realiza por el número de segmentos del mensaje enviados por país. Para saber más sobre cómo se calculan los segmentos del mensaje, consulta nuestra guía [Segmentos del mensaje y límites de copia]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/#segment-breakdown). Tu director de cuentas se pondrá en contacto contigo para informarte de si estás cerca de alcanzar tu máximo, proporcionándote informes relevantes para ayudarte a mantenerte informado. Si tienes más preguntas sobre los excedentes, ponte en contacto con tu representante de Braze.

### Si se envía un mensaje a un teléfono fijo, ¿seguirá contando para mi recuento de envíos SMS?

En EEUU, Canadá y Reino Unido:
- Si se envía un SMS a un teléfono fijo, se marcará como **No entregado**. Ten en cuenta que Twilio seguirá cobrando por intento de entrega, por lo que se facturarán los mensajes marcados como **Enviados**, **Entregados** o **No entregados** en tus registros de mensajes.
- En el Reino Unido, algunos operadores convertirán el SMS en un buzón de voz, entregando el mensaje.

En otros países:
- Twilio lanzará un error y no se te facturará el intento de mensaje SMS. 

### Si un usuario está excluido voluntariamente y envía una palabra clave a nuestro código abreviado y largo, ¿recibe la respuesta que configuramos para esa palabra clave en Braze?

Si un usuario está adherido voluntariamente y envía una palabra clave de una de las [categorías de palabras clave predeterminadas]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/optin_optout/), recibirá la respuesta para esa palabra clave. Si un usuario está excluido voluntariamente y envía una palabra clave [personalizada]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/keyword_handling/), no recibirá la respuesta para esa palabra clave. 
