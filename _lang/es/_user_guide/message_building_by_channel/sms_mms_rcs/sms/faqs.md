---
nav_title: Preguntas frecuentes
article_title: PREGUNTAS FRECUENTES SOBRE SMS
page_order: 12
description: "Este artículo aborda algunas de las preguntas más frecuentes que surgen al configurar campañas de SMS."
page_type: FAQ
alias: /sms_faq/
channel:
  - SMS
  
---

# Preguntas más frecuentes

> En esta página intentaremos responder a sus preguntas más exigentes sobre los SMS.

### ¿Se pueden incluir enlaces en un SMS?

Puede incluir cualquier enlace en cualquier campaña de SMS que desee. Sin embargo, hay que tener en cuenta algunos aspectos:

- Los enlaces pueden ocupar gran parte del límite de 160 caracteres de los SMS. Si incluye un enlace y un texto, es posible que se envíen dos SMS en lugar de uno solo.
- Las empresas suelen utilizar acortadores de enlaces para limitar el impacto del número de caracteres de un enlace. Sin embargo, si se envía un enlace acortado a través de un código largo, los operadores pueden bloquear o denegar el mensaje, ya que pueden sospechar de la redirección del enlace.
- Utilizar un [código corto]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/short_and_long_codes/) sería el tipo de número más fiable para incluir enlaces.

Braze también tiene su propia función de acortamiento de enlaces que acortará los enlaces y proporcionará análisis de clics automáticamente. Consulte [Acortamiento de enlaces]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/link_shortening/) para obtener más información.

### ¿Los mensajes de texto de prueba cuentan para los límites?

Sí, así es. Téngalo en cuenta cuando pruebe los mensajes.

### ¿Es necesario que un usuario forme parte de un grupo de suscripción SMS para recibir mensajes SMS de prueba?

Sí, así es. Los usuarios deben tener un número de teléfono válido y formar parte del grupo de suscripción SMS utilizado para el envío de prueba.

### ¿Necesitas limitar la velocidad de envío de los SMS?

La tasa de concurrencia y el rendimiento por defecto permiten enviar unos 360.000 mensajes a la hora por código corto. Para aumentar el caudal se necesitan códigos cortos adicionales.

### ¿Cómo puedo evitar los excesos?

Aunque no podemos prometerte que de vez en cuando no vayas a tener un exceso de consumo, puedes seguir estas precauciones para reducir las posibilidades de sobrepasar los límites asignados:

- Presta atención al número de caracteres de tu SMS. El envío involuntario de más de un segmento podría causar excesos de tráfico. Para más detalles, consulte nuestro [desglose por segmentos]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/#segment-breakdown).
- Calcule cuidadosamente los caracteres de sus SMS para tener en cuenta el Contenido Líquido o Conectado. El compositor Braze SMS de tu panel de control no calcula ni tiene en cuenta el uso de ninguna de estas funciones.
- Considere el tipo de codificación que utiliza su mensaje: si su mensaje utiliza codificación GSM-7, normalmente puede estimar que puede enviar un mensaje con 128 caracteres por segmento de mensaje. Si tu mensaje utiliza la codificación [UCS-2](https://en.wikipedia.org/wiki/Universal_Coded_Character_Set), normalmente, puedes estimar que puedes enviar un mensaje con 67 caracteres por segmento del mensaje.
- Probar, probar y probar. Prueba siempre tus mensajes SMS antes de lanzarlos, especialmente, cuando utilices Liquid y Contenido conectado.

### ¿Cuáles son las mejores prácticas de envío para evitar la detección de spam en los SMS?

1. Asegúrese de que las instrucciones de inclusión y exclusión son claras.
2. Asegúrese de que usted (la marca) tiene una relación con el cliente.
3. Asegúrese de que el contenido es relevante para la relación y lo que el usuario ha optado por recibir.

Para obtener más directrices sobre cómo evitar la detección de spam, visite [Directrices sobre legislación y reglamentación de SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/laws_and_regulations/).

### ¿Cómo se crea la lógica para las suscripciones selectivas a SMS de modo que los usuarios estén en el grupo de suscripción correcto?

Las palabras clave personalizadas se escribirían como eventos personalizados, por lo que debería crear segmentos basados en las palabras clave que los clientes pueden escribir. Por ejemplo, si un usuario opta por SMS para mensajes VIP pero no para alertas, puede crear un segmento VIP y un segmento de alertas, y luego asignar el usuario al segmento apropiado.

### ¿Cuántos caracteres tiene un emoji?

Los emojis pueden ser complicados, ya que no existe un recuento de caracteres estándar para todos ellos. Existe el riesgo de que el emoji exceda el límite de caracteres y rompa el SMS en varios mensajes, a pesar de que aparezca como un solo mensaje en el compositor Braze. Al probar sus mensajes, puede verificar mejor si un mensaje se dividirá utilizando nuestra [calculadora de segmentos]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/#segment-calculator).

### Si un usuario envía "Stop" a nuestro código corto, ¿se da de baja del grupo de suscripción?

¿Qué aspecto tiene eso en el perfil de usuario? El grupo de suscripción volverá a tener 2 guiones (- -), y habrá eventos personalizados para suscribirse y darse de baja.

### ¿Hay alguna forma de ver si existe un alias en el perfil de un usuario?

Los alias no son visibles en el perfil del usuario. Tendría que utilizar los puntos finales [Exportar datos de usuario]({{site.baseurl}}/api/endpoints/export/) para confirmar que se han establecido los alias.

### ¿Qué son los códigos cortos compartidos?

Con un código corto compartido, todos los mensajes de texto, independientemente de la empresa u organización que los envíe, llegan al dispositivo móvil del consumidor desde el mismo número de teléfono de 5-6 dígitos. Aunque los códigos cortos compartidos tienen un coste relativamente bajo y están disponibles de inmediato, esto significa que su empresa no tendrá un código corto dedicado.

Algunas desventajas de este enfoque son:

- Si sus clientes optan por no recibir los mensajes de otra empresa que tenga un código corto compartido con usted, también habrán optado por no recibir sus mensajes.
- Si una empresa infringe las normas, se suspenden los mensajes de todas las demás.
- Cuestiones de seguridad

### ¿Cómo se autorizan las URL de los SMS?

Antes de enviar mensajes SMS que contengan URL a usuarios de determinados países (por ejemplo, Suecia o los países nórdicos), debes conseguir que estas URL queden registradas en el operador. Póngase en contacto con el responsable del servicio de atención al cliente de Braze para que le ayude. Este proceso durará unos cinco días.  

### ¿Qué ocurre si varios usuarios tienen el mismo número de teléfono?

Cuando varios perfiles de usuario que comparten un número de teléfono (habilitado para SMS) son elegibles para una campaña basada en acciones o un componente Canvas al mismo tiempo, desencadenado por el evento de un SMS entrante, Braze deducirá los usuarios en el nivel del componente Canvas. Esto evitará que los usuarios reciban más de un SMS de un componente de Canvas, aunque varios usuarios compartan el mismo número de teléfono. 

{% alert note %}
Braze no deduplica por número de teléfono para los Lienzos programados.
{% endalert %}

Braze utilizará el siguiente flujo para determinar el perfil del destinatario:
- Comprueba qué perfil ha recibido SMS más recientemente (hasta hace 7 días); si existe, envíalo a ese usuario.
- Si ninguno de los dos había recibido SMS hasta hace 7 días, envíelo al usuario que tenga un alias de usuario "teléfono" que coincida con el número de teléfono.
- Si no existe ninguno, envía a un perfil aleatorio entre los disponibles. 

Si recibe una palabra clave "START" o "STOP" del número de teléfono compartido, todos los perfiles de usuario estarán suscritos y habilitados para SMS o dados de baja. Esto también se aplica a los cambios de estado de la API. Por ejemplo, si varios perfiles con diferentes ID externos tienen los mismos números de teléfono, un cambio de estado del grupo de suscripción a través de la API actualizará todos los perfiles con ese número de teléfono, aunque sólo se especifique un ID externo.

{% alert important %}
Si escalona a sus usuarios en un Lienzo y tiene diferentes horas de programación para cada componente del Lienzo, puede enviar a un usuario con el mismo correo electrónico o teléfono mensajes duplicados.
{% endalert %}

### ¿Las propiedades de los eventos SMS capturarán palabras clave en una frase?

Para que se reconozca una palabra clave dentro de una frase (por ejemplo, "por favor, deja de enviarme mensajes de texto"), tendrás que utilizar una frase líquida en el mensaje para que se reconozca la palabra específica. Las propiedades de evento tienen un límite de 256 caracteres; por lo demás, no hay límite de caracteres.

### ¿Por qué el panel de control de Braze me advierte de que se me pueden cobrar segmentos de mensaje adicionales cuando mi mensaje tiene menos de 160 (GCM-7) o 70 (UCS-2) caracteres?

Es posible que se le cobren segmentos de mensaje adicionales si incluye personalización de líquidos en su mensaje. La creación de plantillas de bloques de contenido no se produce hasta que el mensaje se está preparando para ser enviado. Cuando se edita un SMS con un bloque de contenido, Braze no sabe lo que contendrá el bloque de contenido, pero proporciona una estimación aproximada. Recomendamos a los usuarios que utilicen el panel de prueba para previsualizar el mensaje y saber qué esperar.

### ¿Qué es un `app_id` en el objeto SMS API?

La clave API de identificador de aplicación o `app_id` es un parámetro que asocia la actividad con una aplicación específica en su espacio de trabajo. Designa con qué aplicación del espacio de trabajo estás interactuando. Por ejemplo, tendrás un `app_id` para tu aplicación para iOS, un `app_id` para tu aplicación para Android y un `app_id` para tu integración web. 

Puedes encontrar tu `app_id` accediendo a **Ajustes** > **Ajustes de la aplicación** y localizando la sección **Identificación**.

### ¿Cómo se me facturarán los SMS?

Además de las tarifas de los códigos cortos y largos, Braze ofrece una asignación de mensajes SMS para diferentes países. Es decir, trabajamos contigo para establecer un determinado número de segmentos de mensajes para diferentes países, que utilizarás para enviar campañas de SMS. La facturación se realiza por el número de segmentos de mensajes enviados por país. Para saber más sobre cómo se calculan los segmentos de mensajes, consulte nuestra guía [Segmentos de mensajes y límites de copia]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/#segment-breakdown). Su gestor de cuenta se pondrá en contacto con usted para informarle de si está cerca de alcanzar su máximo y le facilitará los informes pertinentes para mantenerle informado. Si tienes más preguntas sobre los excedentes, ponte en contacto con tu representante de Braze.

### Si se envía un mensaje a un teléfono fijo, ¿seguirá contando para el recuento de envíos de SMS?

En Estados Unidos, Canadá y Reino Unido:
- Si se envía un SMS a un teléfono fijo, se marcará como **No entregado**. Tenga en cuenta que Twilio seguirá cobrando por intento de entrega, por lo que los mensajes marcados como **Enviados**, **Entregados** o **No entregados** en sus registros de mensajes serán facturados.
- En el Reino Unido, algunos operadores convertirán el SMS en un mensaje de voz, entregando el mensaje.

En otros países:
- Twilio lanzará un error y no se te facturará el intento de mensaje SMS. 

### Si un usuario está excluido y envía una palabra clave a nuestro código corto y largo, ¿recibe la respuesta que hemos configurado para esa palabra clave en Braze?

Si un usuario está excluido y envía una palabra clave de una de las [categorías de palabras clave predeterminadas]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/optin_optout/), recibirá la respuesta para esa palabra clave. Si un usuario está excluido y envía una [palabra clave personalizada]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/keyword_handling/), no recibirá la respuesta para esa palabra clave. 
