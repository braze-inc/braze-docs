---
nav_title: Recursos de Meta
article_title: Recursos de Meta
page_order: 12
description: "Este artículo proporciona documentación, información y recursos útiles de Meta para mejorar tu comprensión de la integración de WhatsApp."
alias: /meta_resources/
page_type: reference
channel:
  - WhatsApp

---

# Recursos de Meta

## Documentación de Meta

Revisa la siguiente documentación de Meta para obtener orientación sobre nombres para mostrar, números de teléfono, etc.

- [Orientación sobre el nombre para mostrar](https://www.facebook.com/business/help/757569725593362)
- [Habilitación de Meta Insights](https://www.facebook.com/business/help/218116047387456)
- [Requisitos del número de teléfono](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers)
- [Límites de mensajería](https://developers.facebook.com/docs/whatsapp/messaging-limits)
- [Puntuación de calidad](https://www.facebook.com/business/help/896873687365001)

## Actualizaciones de productos de WhatsApp

### Junio de 2026: ID de usuario con alcance de negocio
*Última actualización marzo 2026*

- Meta está introduciendo ID de usuario para reemplazar el uso compartido de números de teléfono por motivos de privacidad
- Braze está trabajando en una solución antes del lanzamiento
- Lanzamiento previsto por Meta en junio de 2026

### Noviembre de 2025: [API de mensajes de marketing para WhatsApp](https://developers.facebook.com/documentation/business-messaging/whatsapp/marketing-messages/overview/) (anteriormente Marketing Messages Lite API)
*Última actualización marzo 2026*

- Reemplaza los límites estáticos de Cloud API con límites dinámicos basados en la interacción
- No disponible en EMEA, Japón ni Corea del Sur para entrega optimizada
- Los mensajes de utilidad/autenticación continúan a través de Cloud API automáticamente

### Octubre de 2025: Cambio en el proceso de aprobación de cuenta oficial de empresa (OBA)
*Última actualización marzo 2026*

- Anteriormente abierto a todos los clientes a través de WhatsApp Manager
- Ahora restringido a: gobierno/grandes anunciantes de Meta, anunciantes directos o a través de un BSP como Braze (hasta 5 por semana)
- Nuevos requisitos previos: verificación de empresa, verificación en dos pasos, nombre para mostrar aprobado, notoriedad
- Ponte en contacto con tu administrador del éxito del cliente para obtener asistencia

### Octubre de 2025: Reducciones de tarifas regionales
*Última actualización marzo 2026*

- Tarifas más bajas de utilidad/autenticación en Argentina, Egipto, México, Norteamérica
- Tarifas de marketing más bajas en México (vigentes a partir del 1 de octubre de 2025)

### Octubre de 2025: Los límites de mensajería cambian de por teléfono a por portafolio de negocio
*Última actualización marzo 2026*

- Los límites ahora se comparten entre todos los números de teléfono de un portafolio
- Los portafolios heredan el límite existente más alto
- Acceso más rápido a límites más altos (en 6 horas)
- Riesgo: las empresas sin un número "ilimitado" pueden ver una disminución en los límites agregados

### 1 de julio de 2025: Reestructuración de precios
*Última actualización marzo 2026*

- La facturación por mensaje reemplazó la facturación por conversación
- Los mensajes de utilidad enviados en una ventana de servicio de 24 horas pasaron a ser gratuitos
- Tarifas actualizadas de utilidad/autenticación en múltiples mercados, con nuevos niveles por volumen
- Nuevas reglas sobre la categorización incorrecta de plantillas de utilidad: las empresas pueden enfrentar el rechazo de plantillas y restricciones de envío

### Abril de 2025: Pausa de mensajes de marketing a números de teléfono de EE. UU.
*Última actualización agosto 2025*

Meta detendrá la entrega de todos los mensajes de plantillas de marketing a los usuarios de WhatsApp que tengan un número de teléfono de Estados Unidos (un número compuesto por un código de marcación `+1` y un código de área de Estados Unidos). Actualmente no hay fecha prevista para el levantamiento de esta pausa.

Cualquier intento de enviar una plantilla a un usuario de WhatsApp con un número de teléfono de EE. UU. dará lugar al error `131049`.

### Marzo de 2025: Restricciones por uso indebido de categoría de plantilla
*Última actualización marzo 2026*

- Meta introdujo medidas de cumplimiento para empresas que hacen un uso indebido de la categorización de utilidad/marketing
- Puede resultar en restricciones de 7 a 30 días en la creación de plantillas y revisiones de categoría

### Marzo de 2025: Límites de mensajes de plantillas de marketing por usuario
*Última actualización agosto 2025*

Meta limitará el número de mensajes de plantillas de marketing que un usuario puede recibir de todas las empresas en un periodo de tiempo determinado, empezando por los mensajes que tienen menos probabilidades de ser leídos.

Una excepción es que, si una persona responde a un mensaje de marketing, se iniciará una ventana de servicio al cliente de 24 horas. Los mensajes de marketing enviados dentro de esta ventana no contarán para el límite de esa persona.

El límite específico varía según el usuario, dependiendo de su nivel de interacción. Obtén más información sobre los límites de mensajes de plantilla de marketing por usuario de WhatsApp [aquí](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-message-templates#per-user-marketing-template-message-limits).

### Enero de 2025: WhatsApp pausa el envío de mensajes de marketing a usuarios de EE. UU. a partir del 1 de abril
*Última actualización enero 2025*

WhatsApp interrumpirá el envío de mensajes de marketing a usuarios estadounidenses (personas con números de teléfono estadounidenses) a partir del 1 de abril de 2025. [Los mensajes de utilidad, servicio y autenticación](https://developers.facebook.com/docs/whatsapp/pricing/) y los [mensajes de respuesta]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create#response-messages) seguirán estando permitidos en EE. UU.

El envío de mensajes de marketing (además de todos los demás tipos de mensajes) a todos los demás países o regiones sigue estando permitido y no se verá afectado.

Meta nos ha informado de que están realizando esta actualización para mantener la salud del ecosistema de WhatsApp en EE. UU., donde WhatsApp está creciendo rápidamente, pero aún se encuentra en una fase inicial (por ejemplo, los mensajes de marketing tienen menos interacción que en otras regiones). Seguirán evaluando cuándo el mercado estadounidense está preparado para reanudar los mensajes de marketing.

La entrega de mensajes de marketing a números de teléfono con códigos de área de EE. UU. será rechazada por WhatsApp y devolverá un código de error 131049.

### Noviembre de 2024: Cambios en la política de adhesión voluntaria de WhatsApp
*Última actualización enero 2025*

Meta ha actualizado recientemente su [política de adhesión voluntaria](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/). En lugar de requerir el consentimiento específico del canal, ahora las empresas pueden enviar mensajes a los usuarios en la plataforma si:

1. La persona ha proporcionado su número de teléfono.
2. La persona dio su permiso de adhesión voluntaria para mensajería general, no solo para WhatsApp.

Las empresas siguen teniendo que cumplir todas las leyes locales y seguir los siguientes requisitos al obtener la adhesión voluntaria:

- Las empresas deben indicar claramente que una persona está dando su adhesión voluntaria para recibir comunicaciones de la empresa
- Las empresas deben indicar claramente el nombre de la empresa de la que una persona está optando por recibir mensajes
- Las empresas deben cumplir la legislación aplicable

Aunque WhatsApp ha flexibilizado su política, Braze sigue recomendando recopilar adhesiones voluntarias específicas para el canal de WhatsApp con el fin de fomentar la mejor experiencia del cliente y las mejores tasas de interacción. Como siempre, consulta con tu equipo jurídico para ver qué tiene sentido para tu marca.

### Noviembre de 2024: Actualizaciones del límite de plantilla de marketing por usuario para personas en EE. UU., antes de la temporada navideña
*Última actualización diciembre 2024*

Desde que Meta implementó el límite de plantillas de marketing por usuario, se han observado mejoras significativas en las tasas de lectura y en el sentimiento de los usuarios.
 
A partir de ahora, en vísperas de las fiestas navideñas, las personas en EE. UU. recibirán menos conversaciones de marketing nuevas. Meta espera que este cambio genere audiencias más comprometidas, lo que en última instancia conduce a mejores resultados para las empresas. Esto puede dar lugar a tasas de entrega más bajas para tu empresa si envías mensajes de marketing a números de teléfono de EE. UU., lo que puedes monitorizar con el código de error `131049` a través de Braze Currents y el registro de actividad de mensajes.

Las empresas en EE. UU. pueden seguir entregando mensajes de marketing en otras zonas geográficas, y no hay impacto en los mensajes de utilidad, autenticación o servicio, ni en los mensajes de plantillas de marketing enviados dentro de una ventana de conversación iniciada por el usuario (por ejemplo, un anuncio de clic a WhatsApp o una plantilla de carrusel de productos o cupones que se envía como parte de una conversación).

### Noviembre de 2024: WhatsApp amplía las medidas de cumplimiento basadas en la calidad para incluir las tasas de lectura
*Última actualización diciembre 2024*

WhatsApp invierte continuamente en nuevas formas de ayudar a las empresas a crear experiencias de calidad para sus clientes, como reducir el comportamiento similar al correo no deseado en su plataforma.

El 22 de noviembre, WhatsApp empezó a ampliar sus controles de calidad a nivel de cuenta en las cuentas de empresa de WhatsApp (WABA) con tasas de lectura extremadamente bajas. Este cambio se aplicará en todo el mundo.

Cuando la tasa de lectura de una cuenta disminuye significativamente (por ejemplo, la mayoría de los mensajes enviados por la cuenta no son leídos), se aplicarán bloqueos de mensajería en la cuenta. La gravedad del bloqueo aumentará si las tasas de lectura a escala son constantemente bajas.

Si la tasa de lectura de la cuenta es extremadamente baja, se tomarán las siguientes medidas:

- La cuenta quedará bloqueada para el envío de mensajes iniciados por la empresa. Aún podrá responder a los mensajes iniciados por los clientes. Este bloqueo inicial es un "bloqueo suave" y puede reconocerse seleccionando el botón de confirmación en Calidad de cuenta para comenzar a enviar mensajes de nuevo.
- Si la tasa de lectura sigue bajando o se mantiene baja tras el bloqueo suave, las empresas pueden enfrentarse a un aumento gradual de las medidas de cumplimiento (por ejemplo, unos días de restricciones de mensajería).
- Las empresas tendrán que esperar a que se levante el límite forzoso para volver a enviar mensajes. Si la tasa de lectura sigue siendo baja después de repetidos bloqueos suaves, la cuenta acabará siendo excluida.

#### Cómo estar al día de estas advertencias y medidas de cumplimiento

De forma similar a las medidas de cumplimiento existentes en la plataforma, las empresas recibirán una notificación sobre estas acciones y podrán reconocerlas utilizando la página Calidad de la cuenta en WhatsApp Business Manager. Confirma que tienes los datos de contacto correctos en WhatsApp Business Manager para todos los administradores necesarios, ya que los correos electrónicos de notificación de cumplimiento se enviarán basándose en esa información.

Las notificaciones sobre infracciones graves de correo no deseado serán:

- Mostradas en el centro de notificaciones de WhatsApp Business Manager
- Mostradas en un banner en WhatsApp Manager
- Enviadas como correo electrónico a todos los administradores configurados en WhatsApp Business Manager

### Mayo de 2024: Cloud API en vivo en Turquía
*Última actualización mayo 2024*

Meta ahora proporciona a las empresas de Cloud API acceso a Turquía para mensajería empresarial. Anteriormente, las empresas en Turquía podían utilizar WhatsApp Cloud API, pero los usuarios de WhatsApp con números turcos no podían enviar ni recibir mensajes enviados a través de Cloud API.

Meta siempre deja claro a los usuarios cuándo están chateando con un negocio alojado en Meta, y se requiere que todos los usuarios acepten los Términos de servicio y la Política de privacidad de WhatsApp correspondientes para proceder con la mensajería de negocios. La actualización de 2021 de los Términos de servicio y la Política de privacidad en Turquía se había suspendido, pero ya está en marcha. Esto no cambia el compromiso de Meta con la privacidad: las conversaciones personales siguen estando protegidas por cifrado de extremo a extremo, lo que significa que solo tú y el destinatario pueden verlas. La actualización permite a los usuarios turcos acceder a características opcionales para empresas si así lo desean y ofrece más transparencia sobre el funcionamiento de WhatsApp.  
 
Las empresas de Cloud API ya pueden iniciar conversaciones con usuarios de WhatsApp con números turcos, que ahora devolverán un webhook como conversación "enviada", en lugar del código de error 131026 actual.

Para que un mensaje comercial sea "entregado" o "leído" es necesario que el usuario acepte los términos de WhatsApp. No se cobrará a las empresas a menos que se entregue el mensaje.

Los usuarios que reciban o intenten enviar un mensaje a un negocio de Cloud API recibirán una notificación dentro de la aplicación sobre la actualización de los términos, que aclara que no pueden enviar mensajes a un negocio de Cloud API hasta que hayan aceptado la actualización de WhatsApp. Además, a los usuarios que registren o vuelvan a registrar la aplicación en su teléfono se les pedirá que acepten la actualización de WhatsApp.

Cuando un usuario acepte la actualización, verá el aviso de mensaje del sistema de Cloud API existente cuando chatee con un negocio de Cloud API.

### Mayo de 2024: Límites de mensajes de plantillas de marketing por usuario
*Última actualización mayo 2024*

Meta está desplegando nuevos enfoques para mantener experiencias de usuario de alta calidad y maximizar la interacción con los mensajes de plantillas de marketing en la plataforma WhatsApp. A partir del 23 de mayo de 2024, limitarán el número de mensajes de plantillas de marketing que cada usuario individual puede recibir de todas las empresas con las que interactúa durante un periodo de tiempo determinado, empezando por un pequeño número de conversaciones que tienen menos probabilidades de ser leídas. Ten en cuenta que el límite se determina en función del número de mensajes de plantillas de marketing que esa persona ya ha recibido de cualquier empresa, y no está relacionado específicamente con tu marca. Sin embargo, esto puede afectar a la capacidad de entrega de tus mensajes de plantillas de marketing.

El límite solo se aplica a los mensajes de plantillas de marketing que normalmente abrirían una nueva conversación de marketing. Si ya hay una conversación de marketing abierta entre tu marca y un usuario de WhatsApp, los mensajes de plantillas de marketing enviados al usuario no se verán afectados.

Si un mensaje de plantilla de marketing no se entrega a un usuario determinado debido al límite, Cloud API devolverá el código de error 131026. Ten en cuenta, sin embargo, que estos códigos de error cubren una amplia gama de problemas que pueden resultar en la no entrega de un mensaje, y por razones de privacidad, Meta no revelará si de hecho el mensaje no fue entregado debido al límite. Consulta el [documento de solución de problemas](https://developers.facebook.com/docs/whatsapp/cloud-api/support#troubleshooting) de Cloud API para obtener descripciones de los motivos de no entrega y lo que puedes hacer para determinar su causa subyacente.

Si recibes uno de estos códigos de error y sospechas que se debe al límite, evita reenviar inmediatamente el mensaje de plantilla, ya que solo dará lugar a otra respuesta de error.

Para obtener más información sobre esta actualización de la capacidad de entrega, incluidos los detalles sobre la monitorización de tu capacidad de entrega y otras prácticas recomendadas para la mensajería de marketing en WhatsApp, consulta nuestra reciente [publicación en el blog](https://www.braze.com/resources/articles/meta-introduces-deliverability-updates-for-whatsapp?utm_campaign=fy25-q2-global-customer-customer-meta-deliverability-updates-for-whatsapp&utm_medium=email-cdb&utm_source=braze&utm_content=blog-meta-deliverability-updates-for-wa-blog).

### Abril de 2024: Ritmo de plantillas para plantillas de utilidad
*Última actualización abril 2024*

El año pasado, WhatsApp introdujo el ritmo de plantillas para los mensajes de marketing como una nueva forma de ayudar a las empresas a mejorar la interacción con sus plantillas y crear experiencias de usuario valiosas. A partir del 30 de abril, ampliarán el ritmo de plantillas a los mensajes de utilidad. Si una plantilla de utilidad de una cuenta se pone en pausa debido a los comentarios de los usuarios, se aplicará el ritmo a las nuevas plantillas de utilidad que se creen durante los siete días siguientes.

### Abril de 2024: Las tasas de lectura afectarán a la puntuación de calidad de las plantillas de marketing
*Última actualización marzo 2024*

WhatsApp está probando nuevos enfoques, empezando con los consumidores en la India, para crear experiencias más valiosas y maximizar la interacción con las conversaciones de marketing de las empresas. Esto puede incluir limitar el número de conversaciones de marketing que una persona recibe de cualquier empresa en un periodo determinado, empezando por un pequeño número de conversaciones que tengan menos probabilidades de ser leídas. Braze obtendrá un código de error si no se entrega un mensaje.

WhatsApp empezará a considerar las tasas de lectura como parte de la puntuación de calidad para las plantillas de marketing, junto con las métricas tradicionales como los bloqueos y los informes. WhatsApp puede pausar temporalmente las campañas de mensajes de marketing con bajas tasas de lectura, dando tiempo a las empresas para iterar sobre las plantillas con la menor interacción antes de escalar el volumen a partir del 1 de abril de 2024.

### Febrero de 2024: Experimentación sobre conversaciones de marketing
*Última actualización febrero 2024*

A partir del 6 de febrero de 2024, WhatsApp está probando nuevos enfoques, comenzando con los consumidores de la India, para crear experiencias más valiosas y maximizar la interacción de los clientes con las conversaciones de marketing de tu marca. Esto puede incluir limitar el número de conversaciones de marketing que un usuario recibe de tu marca en un periodo determinado, empezando por un número reducido de conversaciones que tengan menos probabilidades de ser leídas.

### Octubre de 2023: Ritmo de plantillas
*Última actualización octubre 2023*

A partir del 12 de octubre de 2023, WhatsApp introducirá un concepto llamado "ritmo de plantillas" para los mensajes de marketing. En lugar de enviar el mensaje a toda la audiencia de la campaña simultáneamente, el "ritmo de plantillas" envía inicialmente el mensaje a un subconjunto más pequeño de usuarios para recopilar comentarios en tiempo real de los destinatarios de la campaña antes de enviar el resto de mensajes.

El "límite de ritmo" (el subconjunto inicial de mensajes enviados) es variable en función de la plantilla. Tras el envío inicial, WhatsApp retendrá los mensajes restantes durante un máximo de 30 minutos. Durante este periodo de espera, evalúan la calidad de la plantilla basándose en los comentarios de los clientes. Si la respuesta es positiva, indicativa de una plantilla de alta calidad, se entregarán los mensajes restantes. Si la respuesta es negativa, eliminan el resto de mensajes no entregados, lo que evita que una mayor parte de tus clientes reciban comentarios negativos y te ayuda a evitar posibles problemas de cumplimiento de calidad (como impactos en la puntuación de calidad del número de teléfono).

Ten en cuenta que WhatsApp utiliza el mismo sistema para evaluar la calidad de la plantilla en el ritmo de plantillas que para la pausa de plantillas. Así, los mensajes no entregados durante el ritmo de plantillas (debido a plantillas de baja calidad) son los mismos que se habrían pausado a mayor escala.

En última instancia, esta actualización te proporciona un ciclo de retroalimentación más rápido (30 minutos frente a horas o días con la pausa de plantillas), para que puedas ajustar tus plantillas y ofrecer una mejor experiencia al cliente.

**Si tienes más preguntas sobre esta actualización, ponte en contacto con tu representante socio de Meta.**

### Junio de 2023: Experimentación con mensajes
*Última actualización junio 2023*

A partir del 14 de junio de 2023, Meta introducirá nuevas prácticas de experimentación en la plataforma WhatsApp con el fin de evaluar el impacto de los mensajes de marketing en la experiencia y la interacción de los consumidores. Este experimento puede afectar a tus mensajes de marketing enviados a través de la API de WhatsApp Business con Braze.

Meta tiene la intención de seguir experimentando en la plataforma WhatsApp. Consulta [la documentación de Meta](https://developers.facebook.com/docs/whatsapp/on-premises/guides/experiments?content_id=86oue5PtwEgcBJl) para obtener más información.

**La experimentación de WhatsApp solo afecta a los mensajes de marketing.** Este experimento puede influir en la entrega de los mensajes de plantillas de marketing. Las plantillas de utilidad y autenticación seguirán entregándose sin impacto de la experimentación.

En el experimento, Meta elige aleatoriamente a aproximadamente el 1 % de los consumidores de WhatsApp como participantes. Si son seleccionados, Meta no entregará plantillas de mensajes de marketing a estos consumidores a menos que se cumpla una de las siguientes condiciones:

- Si un consumidor te ha respondido en las últimas 24 horas;
- Si hay una conversación de marketing existente abierta; o
- Si el consumidor ha hecho clic en un anuncio de WhatsApp en las últimas 72 horas.

## Preguntas frecuentes {#faq}

### ¿Cómo sabré si mi mensaje de marketing se ha visto afectado por el experimento de Meta?

Si un mensaje no se entrega debido al experimento, aparecerá un código de error específico en el registro de actividad y dentro de Currents. El mensaje también se contabilizará como un fallo y se incorporará a tus métricas de fallos de WhatsApp en todos los informes del dashboard de Braze. No se te cobrará por estos mensajes.

Este código de error 130472 dirá "User's number is part of an experiment." Consulta [la documentación de Meta](https://developers.facebook.com/docs/whatsapp/cloud-api/support/error-codes?content_id=8SJRLBEjYGvXO9k) para obtener más información sobre los códigos de error de WhatsApp Cloud API.

### ¿Puedo excluirme del experimento de Meta?

No, Meta no permite la exclusión voluntaria de ningún experimento. Todos los proveedores y usuarios de la API de WhatsApp Business están sujetos a este experimento de Meta.

### ¿Puedo intentar reenviar una plantilla más tarde?

No hay un tiempo fijo para este experimento. Por lo tanto, un consumidor puede seguir sujeto al experimento.

### ¿Qué puedo hacer si mis mensajes de marketing no se entregan debido al experimento de Meta?

Recomendamos utilizar otros canales de Braze, como el correo electrónico, los SMS, las notificaciones push o los mensajes dentro de la aplicación, para enviar un mensaje con contenido similar a los usuarios a los que va dirigido.