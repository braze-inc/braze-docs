---
nav_title: Meta Recursos
article_title: Meta Recursos
page_order: 81
description: "Este artículo proporciona documentación, información y recursos útiles de Meta para mejorar tu comprensión de la integración de WhatsApp."
page_type: reference
channel:
  - WhatsApp

---

# Meta recursos

## Metadocumentación

Revisa la siguiente documentación de Meta para obtener orientación sobre nombres para mostrar, números de teléfono, etc.

- [Orientación sobre el nombre para mostrar](https://www.facebook.com/business/help/757569725593362) 
- [Habilitación de Meta Insights](https://www.facebook.com/business/help/218116047387456)
- [Requisitos del número de teléfono](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers)
- [Límites de mensajería](https://developers.facebook.com/docs/whatsapp/messaging-limits)
- [Puntuación de calidad](https://www.facebook.com/business/help/896873687365001)

## Actualizaciones de productos WhatsApp

### Mayo de 2024: Lanzamiento en vivo de Cloud API en Turquía
*Última actualización: mayo de 2024*

Meta proporciona ahora a las empresas de Cloud API acceso a Turquía para mensajería empresarial. Anteriormente, las empresas turcas podían utilizar WhatsApp Cloud API, pero los usuarios de WhatsApp con números turcos no podían enviar ni recibir mensajes enviados a través de Cloud API. 

Meta siempre deja claro a los usuarios cuándo están chateando con un negocio alojado en Meta, y se requiere que todos los usuarios acepten los Términos de Servicio y la Política de Privacidad de WhatsApp correspondientes para proceder con la mensajería de negocios. La actualización de 2021 de las condiciones de servicio y la política de privacidad en Turquía se había suspendido, pero ya está en marcha. Esto no cambia el compromiso de Meta con la privacidad: las conversaciones personales siguen estando protegidas por cifrado de extremo a extremo, lo que significa que sólo tú y el destinatario pueden verlas. La actualización permite a los usuarios turcos acceder a funciones opcionales para empresas si así lo desean y ofrece más transparencia sobre el funcionamiento de WhatsApp.  
 
Las empresas de la API en la nube ya pueden iniciar conversaciones con usuarios de WhatsApp con números turcos, que ahora devolverán un webhook como conversación "enviada", en lugar del código de error 131026 actual.

Para que un mensaje comercial sea "entregado" o "leído" es necesario que el usuario acepte las condiciones de WhatsApp. No se cobrará a las empresas a menos que se entregue el mensaje.

Los usuarios que reciban o intenten enviar un mensaje a un negocio de Cloud API recibirán una notificación dentro de la aplicación sobre la actualización de los términos que aclara que no pueden enviar mensajes a un negocio de Cloud API hasta que hayan aceptado la actualización de WhatsApp. Además, a los usuarios que registren o vuelvan a registrar la aplicación en su teléfono, se les pedirá que acepten la actualización de WhatsApp.

Cuando un usuario acepte la actualización, verá el aviso de mensaje del sistema Cloud API existente cuando chatee con un Cloud API Business.

### Mayo de 2024: Límites de mensajes de plantillas de marketing por usuario
*Última actualización: mayo de 2024*

Meta está desplegando nuevos enfoques para mantener experiencias de usuario de alta calidad y maximizar el compromiso de los mensajes de las plantillas de marketing en la plataforma WhatsApp. A partir del 23 de mayo de 2024, limitarán el número de mensajes de plantillas de marketing que cada usuario individual puede recibir de todas las empresas con las que interactúa durante un periodo de tiempo determinado, empezando por un pequeño número de conversaciones que tienen menos probabilidades de ser leídas. Tenga en cuenta que el límite se determina en función del número de mensajes de plantillas de marketing que esa persona ya ha recibido de cualquier empresa, y no está relacionado específicamente con su marca. Sin embargo, esto puede afectar a la capacidad de entrega de sus mensajes de plantillas de marketing.

El límite sólo se aplica a los mensajes de plantillas de marketing que normalmente abrirían una nueva conversación de marketing. Si ya hay una conversación de marketing abierta entre su marca y un usuario de WhatsApp, los mensajes de plantillas de marketing enviados al usuario no se verán afectados.

Si un mensaje de plantilla de marketing no se entrega a un usuario determinado debido al límite, Cloud API devolverá el código de error 131026. Tenga en cuenta, sin embargo, que estos códigos de error cubren una amplia gama de problemas que pueden resultar en la no entrega de un mensaje, y por razones de privacidad, Meta no revelará si de hecho el mensaje no fue entregado debido al límite. Consulta [el documento Solución de problemas](https://developers.facebook.com/docs/whatsapp/cloud-api/support#troubleshooting) de Cloud API para obtener descripciones de los motivos de no entrega y lo que puedes hacer para determinar su causa subyacente.

Si recibe uno de estos códigos de error y sospecha que se debe al límite, evite reenviar inmediatamente el mensaje de plantilla, ya que sólo dará lugar a otra respuesta de error. 

Para obtener más información sobre esta actualización de la capacidad de entrega, incluidos los detalles sobre la supervisión de la capacidad de entrega y otras prácticas recomendadas para la mensajería de marketing en WhatsApp, consulte nuestra reciente [publicación en el blog](https://www.braze.com/resources/articles/meta-introduces-deliverability-updates-for-whatsapp?utm_campaign=fy25-q2-global-customer-customer-meta-deliverability-updates-for-whatsapp&utm_medium=email-cdb&utm_source=braze&utm_content=blog-meta-deliverability-updates-for-wa-blog).

### Abril de 2024: Plantillas de servicios públicos
*Última actualización: abril de 2024*

El año pasado, WhatsApp introdujo el ritmo de plantillas para los mensajes de marketing como una nueva forma de ayudar a las empresas a mejorar el compromiso de sus plantillas y crear experiencias de usuario valiosas. A partir del 30 de abril, ampliarán el ritmo de las plantillas a los mensajes de servicios públicos. Si una plantilla de servicios públicos de una cuenta se pone en pausa debido a los comentarios de los usuarios, seguirán el ritmo de las nuevas plantillas de servicios públicos que se creen durante los siete días siguientes.

### Abril de 2024: Los índices de lectura afectarán a la calificación de calidad de las plantillas de marketing 
*Última actualización: marzo de 2024*

WhatsApp está probando nuevos enfoques, empezando con los consumidores en la India, para crear experiencias más valiosas y maximizar el compromiso con las conversaciones de marketing de las empresas. Esto puede incluir limitar el número de conversaciones de marketing que una persona recibe de cualquier empresa en un periodo determinado, empezando por un pequeño número de conversaciones que tengan menos probabilidades de ser leídas. Braze obtendrá un código de error si no se entrega un mensaje.

WhatsApp empezará a considerar las tasas de lectura como parte de nuestra calificación de calidad para las plantillas de marketing, junto con las métricas tradicionales como los bloques y los informes. WhatsApp puede pausar temporalmente las campañas de mensajes de marketing con bajas tasas de lectura, dando tiempo a las empresas para iterar sobre las plantillas con el compromiso más bajo antes de escalar el volumen a partir del 1 de abril de 2024. 

### Febrero de 2024: Experimentación sobre conversaciones de marketing
*Última actualización: febrero de 2024*

A partir del 6 de febrero de 2024, WhatsApp está probando nuevos enfoques, comenzando con los consumidores de la India, para crear experiencias más valiosas y maximizar el compromiso de los clientes con las conversaciones de marketing de su marca. Esto puede incluir limitar el número de conversaciones de marketing que un usuario recibe de su marca en un periodo determinado, empezando por un número reducido de conversaciones que tengan menos probabilidades de ser leídas.

### Octubre de 2023: Ritmo de plantillas 
*Última actualización: octubre de 2023*

A partir del 12 de octubre de 2023, WhatsApp introducirá un concepto llamado "ritmo de plantillas" para los mensajes de marketing. En lugar de enviar el mensaje a toda la audiencia de la campaña simultáneamente, el "ritmo de plantillas" envía inicialmente el mensaje a un subconjunto más pequeño de usuarios para recopilar comentarios en tiempo real de los destinatarios de la campaña antes de enviar el resto de mensajes. 

El "límite de ritmo" (el subconjunto inicial de mensajes enviados) es variable en función de la plantilla. Tras el envío inicial, WhatsApp retendrá los mensajes restantes durante un máximo de 30 minutos. Durante este periodo de espera, evalúan la calidad de la plantilla basándose en los comentarios de los clientes. Si la respuesta es positiva, indicativa de una plantilla de alta calidad, se entregarán los mensajes restantes. Si la respuesta es negativa, eliminan el resto de mensajes no entregados, lo que evita que una mayor parte de sus clientes sigan haciendo comentarios negativos y le ayuda a evitar posibles problemas de aplicación de la calidad (como impactos en la calificación de la calidad del número de teléfono). 

Tenga en cuenta que WhatsApp utiliza el mismo sistema para evaluar la calidad de la plantilla en el ritmo de la plantilla que para la pausa de la plantilla. Así, los mensajes no entregados durante la pausa de plantillas (debido a plantillas de baja calidad) son los mismos que se habrían pausado a mayor escala. 

En última instancia, esta actualización le proporciona un bucle de retroalimentación más rápido (30 minutos frente a horas o días con la pausa de la plantilla), para que pueda ajustar sus plantillas y ofrecer una mejor experiencia al cliente.

**Si tienes más preguntas sobre esta actualización, ponte en contacto con tu representante de Meta.**

### Junio de 2023: Experimentación con mensajes 
*Última actualización: junio de 2023*

A partir del 14 de junio de 2023, Meta introducirá nuevas prácticas de experimentación en la plataforma WhatsApp con el fin de evaluar el impacto de los mensajes de marketing en la experiencia y el compromiso de los consumidores. Este experimento puede afectar a tus mensajes de marketing enviados en la API de WhatsApp Business con Braze.

Meta tiene la intención de seguir experimentando con la plataforma WhatsApp. Consulta [la documentación de Meta](https://developers.facebook.com/docs/whatsapp/on-premises/guides/experiments?content_id=86oue5PtwEgcBJl) para obtener más información.

**La experimentación de WhatsApp sólo afecta a los mensajes de marketing.** Este experimento puede influir en la difusión de los mensajes de las plantillas de marketing. Las plantillas de utilidades y autenticación seguirán suministrándose sin impacto en la experimentación.

En el experimento, Meta elige aleatoriamente a aproximadamente el 1% de los consumidores de WhatsApp como participantes. Si se selecciona, Meta no entregará plantillas de mensajes de marketing a estos consumidores a menos que se cumpla una de las siguientes condiciones:

- Si un consumidor le ha respondido en las últimas 24 horas;
- Si está abierta una conversación de marketing; o
- Si el consumidor ha hecho clic en un anuncio de WhatsApp en las últimas 72 horas.

## Preguntas más frecuentes {#faq}

### ¿Cómo sabré si mi mensaje de marketing se ha visto afectado por el experimento de Meta?

Si un mensaje no se entrega debido al experimento, aparecerá un código de error específico en Registro de actividad y dentro de Corrientes. El mensaje también se contabilizará como un fallo y se incorporará a sus métricas de Fallos de WhatsApp en todos los informes del panel Braze. No se le cobrará por estos mensajes.

Este código de error 130472 dirá "El número del usuario es parte de un experimento". Consulta [la documentación de Meta](https://developers.facebook.com/docs/whatsapp/cloud-api/support/error-codes?content_id=8SJRLBEjYGvXO9k) para obtener más información sobre los códigos de error de la API de WhatsApp Cloud.

### ¿Puedo excluirme del experimento de Meta?

No, Meta no permite la exclusión voluntaria de ningún experimento. Todos los proveedores y usuarios de la API de WhatsApp Business están sujetos a este Meta experimento.

### ¿Puedo intentar reenviar una plantilla más tarde?

No hay una hora fija para este experimento. De este modo, el consumidor puede seguir sujeto del experimento.

### ¿Qué puedo hacer si mis mensajes de marketing no llegan debido al experimento de Meta?

Recomendamos utilizar otros canales Braze, como el correo electrónico, los SMS, las notificaciones push o los mensajes in-app para enviar un mensaje con contenido similar a los usuarios a los que va dirigido.
