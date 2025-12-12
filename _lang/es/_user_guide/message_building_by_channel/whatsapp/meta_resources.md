---
nav_title: Meta recursos
article_title: Meta Recursos
page_order: 11
description: "Este artículo proporciona documentación, información y recursos útiles de Meta para mejorar tu comprensión de la integración de WhatsApp."
page_type: reference
channel:
  - WhatsApp

---

# Meta recursos

## Meta documentación

Revisa la siguiente documentación de Meta para obtener orientación sobre los nombres para mostrar, los números de teléfono, etc.

- [Orientación sobre el nombre de la pantalla](https://www.facebook.com/business/help/757569725593362) 
- [Habilitación de Meta Insights](https://www.facebook.com/business/help/218116047387456)
- [Requisitos del número de teléfono](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers)
- [Límites de mensajería](https://developers.facebook.com/docs/whatsapp/messaging-limits)
- [Tasa de calidad](https://www.facebook.com/business/help/896873687365001)

## Actualizaciones de productos de WhatsApp

### Abril de 2025: Pausa de mensajes de mensajería a números de teléfono de EE.UU.
*Última actualización agosto 2025*

Meta detendrá la entrega de todos los mensajes de plantillas de marketing a los usuarios de WhatsApp que tengan un número de teléfono de Estados Unidos (un número compuesto por un código de marcación `+1` y un código de área de Estados Unidos). Actualmente no hay fecha prevista para el levantamiento de esta pausa. 

Cualquier intento de enviar una plantilla a un usuario de WhatsApp con un número de teléfono de EE.UU. dará lugar al error `131049`.

### Marzo de 2025: Límites de la plantilla de mensajes de marketing por usuario
*Última actualización agosto 2025*

Meta limitará el número de mensajes de plantillas de marketing que un usuario puede recibir en todas las empresas en un periodo de tiempo determinado, empezando por los mensajes que tienen menos probabilidades de ser leídos. 

Una excepción es que, si una persona responde a un mensaje de marketing, se iniciará una ventana de servicio al cliente de 24 horas. Los mensajes de mensajería enviados dentro de esta ventana no contarán para el límite de una persona.

El límite específico varía según el usuario, dependiendo de su nivel de interacción. Más información sobre los límites de la plantilla de mensajes de marketing por usuario de WhatsApp [aquí](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-message-templates#per-user-marketing-template-message-limits). 

### Enero de 2025: WhatsApp pausa el envío de mensajes de marketing a usuarios de EE.UU. a partir del 1 de abril
*Última actualización Enero 2025*

WhatsApp interrumpirá el envío de mensajes de marketing a usuarios estadounidenses (personas con números de teléfono estadounidenses) a partir del 1 de abril de 2025. [Los mensajes de]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create#response-messages) [utilidad, servicio, autenticación](https://developers.facebook.com/docs/whatsapp/pricing/) y [respuesta]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create#response-messages) seguirán estando permitidos en EEUU. 

El envío de mensajes de marketing (además de todos los demás tipos de mensajes) a todos los demás países o regiones sigue estando permitido y no se verá afectado.

Meta nos ha informado de que están realizando esta actualización para mantener la salud del ecosistema de WhatsApp en EE.UU., donde WhatsApp está creciendo rápidamente, pero aún se encuentra en una fase inicial (por ejemplo, los mensajes de mensajería tienen menos interacción que en otras regiones). Seguirán evaluando cuándo el mercado estadounidense está preparado para reanudar los mensajes de mensajería.

La entrega de mensajes de marketing a números de teléfono con códigos de área de EE.UU. será rechazada por WhatsApp y devolverá un código de error de 131049. 

### Noviembre de 2024: Cambios en la política de adhesión voluntaria de WhatsApp
*Última actualización Enero 2025*

Meta ha actualizado recientemente su [política de adhesión voluntaria](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/). En lugar de requerir el consentimiento específico del canal, ahora las empresas pueden enviar mensajes a los usuarios de la plataforma si:

1. La persona ha dado su número de teléfono.
2. La persona dio su permiso de adhesión voluntaria para mensajería general, no sólo para WhatsApp. 

Las empresas siguen teniendo que cumplir todas las leyes locales y seguir los siguientes requisitos al obtener la adhesión voluntaria:

- Las empresas deben indicar claramente que una persona está dando su adhesión voluntaria para recibir comunicaciones de la empresa.
- Las empresas deben indicar claramente el nombre de la empresa de la que una persona está optando por recibir mensajes
- Las empresas deben cumplir la legislación aplicable

Aunque WhatsApp ha flexibilizado su política, Braze sigue recomendando recopilar adhesiones voluntarias específicas para el canal de WhatsApp con el fin de fomentar la mejor experiencia del cliente y las mejores tasas de interacción. Como siempre, consulta con tu equipo jurídico para ver qué tiene sentido para tu marca.

### Noviembre de 2024: Actualizaciones del límite de la plantilla de marketing por usuario para los habitantes de EE.UU., antes de la temporada de vacaciones
*Última actualización diciembre 2024*

Desde que Meta ha puesto en marcha el límite de plantillas de marketing por usuario, Meta ha observado mejoras significativas en las tasas de lectura y en el sentimiento de los usuarios.
 
A partir de ahora, en vísperas de las fiestas navideñas, los estadounidenses recibirán menos conversaciones de marketing nuevas. Meta espera que este cambio cree audiencias más comprometidas, lo que en última instancia conduce a mejores resultados para las empresas. Esto puede dar lugar a tasas de entrega más bajas para tu empresa si envías mensajes de marketing a números de teléfono de EE.UU., lo que puede controlarse con el código de error `131049` a través de Braze Currents y el Registro de actividad de mensajes.

Las empresas de EE.UU. pueden seguir entregando mensajes de mensajería en otras zonas geográficas, y no afecta a los mensajes de utilidad, autenticación o servicio, ni a los mensajes de plantillas de marketing enviados dentro de una ventana de conversación iniciada por el usuario (por ejemplo, un anuncio de WhatsApp en el que se hace clic o una plantilla de carrusel de productos o cupones que se envía como parte de una conversación). 

### Noviembre de 2024: WhatsApp amplía la imposición de cuentas basadas en la calidad para incluir las tasas de lectura
*Última actualización diciembre 2024*

WhatsApp invierte continuamente en nuevas formas de ayudar a las empresas a crear experiencias de calidad para sus clientes, como reducir el comportamiento similar al correo no deseado en su plataforma. 

El 22 de noviembre, WhatsApp empezó a ampliar sus actuales controles de calidad a nivel de cuenta en las cuentas de empresa de WhatsApp (WABA) con tasas de lectura extremadamente bajas. Este cambio se aplicará en todo el mundo.

Cuando la tasa de lectura de una cuenta disminuye significativamente (por ejemplo, la mayoría de los mensajes enviados por la cuenta no son leídos), se aplicarán bloqueos de mensajería en la cuenta. La gravedad del bloqueo aumentará si las tasas de lectura a escala son constantemente bajas. 

Si la tasa de lectura de la cuenta es extremadamente baja, se tomarán las siguientes medidas:

- La cuenta quedará bloqueada para el envío de mensajes iniciados por la empresa. También pueden responder a los mensajes iniciados por los clientes. Este bloqueo inicial es un "bloqueo suave" y puede confirmarse seleccionando el botón de confirmación en Calidad de cuenta para comenzar a enviar mensajes de nuevo.
- Si la tasa de lectura sigue bajando o se mantiene baja tras el bloqueo suave, las empresas pueden enfrentarse a un aumento gradual de las medidas coercitivas (por ejemplo, unos días de restricciones de mensajería).
- Las empresas tendrán que esperar al límite forzoso para volver a enviar mensajes. Si la tasa de lectura sigue siendo baja después de repetir los bloqueos suaves, la cuenta acabará siendo excluida.

#### Cómo estar al día de estas advertencias y ejecuciones

De forma similar a la aplicación existente en la plataforma, las empresas recibirán una notificación sobre estas acciones y podrán reconocerlas utilizando la página Calidad de la cuenta en el administrador de negocios de WhatsApp. Confirma que tienes los datos de contacto correctos en la lista de WhatsApp Business Manager de todos los administradores necesarios, ya que los correos electrónicos de notificación de ejecución se enviarán basándose en esa información.

Las notificaciones sobre infracciones graves de correo no deseado serán:

- Aparece en el centro de notificaciones del administrador de WhatsApp Business
- Se muestra en un banner en el administrador de WhatsApp
- Enviado como un correo electrónico a todos los administradores configurados en el WhatsApp Business Manager

### Mayo de 2024: API en la nube en vivo en Turquía
*Última actualización Mayo 2024*

Meta ofrece ahora a las empresas la API en la nube para acceder a Türkiye para la mensajería empresarial. Anteriormente, WhatsApp Cloud API estaba disponible para que lo utilizaran las empresas de Turquía, pero los usuarios de WhatsApp con números turcos no podían enviar ni recibir mensajes enviados a través de Cloud API. 

Meta siempre deja claro a los usuarios cuándo están chateando con una empresa alojada en Meta, y todos los usuarios deben aceptar las Condiciones de servicio y la Política de privacidad de WhatsApp correspondientes para proceder a la mensajería empresarial. La actualización de las Condiciones de servicio y la Política de privacidad de 2021 en Turquía se había interrumpido, pero ya se está aplicando. Esto no cambia el compromiso de Meta con la privacidad: las conversaciones personales siguen estando protegidas por una encriptación de extremo a extremo, lo que significa que sólo tú y el destinatario podéis verlas. La actualización habilita a los usuarios turcos a acceder a características empresariales opcionales si así lo desean y proporciona más transparencia sobre el funcionamiento de WhatsApp.  
 
Las empresas de la API en la nube ya pueden iniciar conversaciones con usuarios de WhatsApp con números turcos, que ahora devolverán un webhook como conversación "enviada", en lugar del actual código de error 131026.

Para que un mensaje comercial sea "entregado" o "leído" es necesario que el usuario acepte las condiciones de WhatsApp. No se cobrará a menos que se entregue el mensaje.

A los usuarios que reciban o intenten enviar un mensaje a un negocio de la API de la Nube se les mostrará una notificación dentro de la aplicación sobre la actualización de las condiciones que aclara que no pueden enviar mensajes a un negocio de la API de la Nube hasta que hayan aceptado la actualización de WhatsApp. Además, se pedirá a los usuarios que registren o vuelvan a registrar la aplicación en su teléfono que acepten la actualización de WhatsApp.

Cuando un usuario acepte la actualización, verá el aviso de mensaje existente en el sistema de la API de la Nube cuando chatee con un Negocio de la API de la Nube.

### Mayo de 2024: Límites de la plantilla de mensajes de marketing por usuario
*Última actualización Mayo 2024*

Meta está desplegando nuevos enfoques para mantener experiencias de usuario de alta calidad y maximizar la interacción con los mensajes de la plantilla de marketing en la plataforma WhatsApp. A partir del 23 de mayo de 2024, limitarán el número de mensajes de plantillas de marketing que cada usuario individual puede recibir de todas las empresas con las que interactúa durante un periodo de tiempo determinado, empezando con un pequeño número de conversaciones que tienen menos probabilidades de ser leídas. Ten en cuenta que el límite se determina en función del número de mensajes de plantillas de marketing que esa persona ya ha recibido de cualquier empresa, y no está relacionado específicamente con tu marca. Sin embargo, esto puede afectar a la capacidad de entrega de los mensajes de tu plantilla de marketing.

El límite sólo se aplica a los mensajes de plantillas de marketing que normalmente abrirían una nueva conversación de marketing. Si ya hay una conversación de marketing abierta entre tu marca y un usuario de WhatsApp, los mensajes de la plantilla de marketing enviados al usuario no se verán afectados.

Si no se entrega un mensaje de plantilla de marketing a un usuario determinado debido al límite, Cloud API devolverá el código de error 131026. Sin embargo, ten en cuenta que estos códigos de error abarcan una amplia gama de problemas que pueden provocar que no se entregue un mensaje y, por motivos de privacidad, Meta no revelará si, de hecho, el mensaje no se entregó debido al límite. Consulta [el documento Solución de problemas](https://developers.facebook.com/docs/whatsapp/cloud-api/support#troubleshooting) de la API Nube para ver descripciones de los motivos de no entrega y lo que puedes hacer para determinar su causa subyacente.

Si recibes uno de estos códigos de error y sospechas que se debe al límite, evita reenviar inmediatamente el mensaje de la plantilla, ya que sólo conseguirás otra respuesta de error. 

Para obtener más información sobre esta actualización de la capacidad de entrega, incluidos detalles sobre la supervisión de tu capacidad de entrega y otras prácticas recomendadas para la mensajería de marketing en WhatsApp, consulta nuestra reciente [publicación en el blog](https://www.braze.com/resources/articles/meta-introduces-deliverability-updates-for-whatsapp?utm_campaign=fy25-q2-global-customer-customer-meta-deliverability-updates-for-whatsapp&utm_medium=email-cdb&utm_source=braze&utm_content=blog-meta-deliverability-updates-for-wa-blog).

### Abril de 2024: Paso de plantillas para plantillas de utilidades
*Última actualización abril 2024*

El año pasado, WhatsApp introdujo el ritmo de plantillas para mensajes de marketing como una nueva forma de ayudar a las empresas a mejorar la interacción de sus plantillas y crear experiencias de usuario valiosas. A partir del 30 de abril, ampliarán el ritmo de plantillas a los mensajes de utilidad. Si una plantilla de utilidades de una cuenta se pone en pausa debido a la opinión de los usuarios, seguirán el ritmo de las nuevas plantillas de utilidades que se creen durante los siete días siguientes.

### Abril de 2024: Las tasas de lectura afectarán a la tasa de calidad de las plantillas de marketing 
*Última actualización marzo 2024*

WhatsApp está probando nuevos enfoques, empezando por los consumidores de la India, para crear experiencias más valiosas y maximizar la interacción con las conversaciones de marketing de las empresas. Esto puede incluir limitar el número de conversaciones de marketing que una persona recibe de cualquier empresa en un periodo determinado, empezando con un pequeño número de conversaciones que tengan menos probabilidades de ser leídas. Braze obtendrá un código de error si no se entrega un mensaje.

WhatsApp empezará a tener en cuenta las tasas de lectura como parte de nuestra calificación de calidad de las plantillas de marketing, junto con métricas tradicionales como los bloques y los informes. WhatsApp podría pausar temporalmente las campañas de mensajería con tasas de lectura bajas, dando tiempo a las empresas para iterar sobre las plantillas con menor interacción antes de escalar el volumen a partir del 1 de abril de 2024. 

### Febrero de 2024: Conversaciones de marketing Experimentación
*Última actualización febrero 2024*

A partir del 6 de febrero de 2024, WhatsApp está probando nuevos enfoques, empezando por los consumidores de la India, para crear experiencias más valiosas y maximizar la interacción con los clientes en las conversaciones de marketing de tu marca. Esto puede incluir limitar el número de conversaciones de marketing que un usuario recibe de tu marca en un periodo determinado, empezando con un pequeño número de conversaciones que tengan menos probabilidades de ser leídas.

### Octubre de 2023: Plantilla Pacing 
*Última actualización octubre 2023*

A partir del 12 de octubre de 2023, WhatsApp va a introducir un concepto llamado "ritmo de plantillas" para los mensajes de mensajería. En lugar de enviar tu mensaje a toda la audiencia de tu campaña simultáneamente, el "ritmo de plantillas" entrega inicialmente el mensaje a un subconjunto más pequeño de usuarios para recopilar información en tiempo real de los destinatarios de la campaña antes de enviar el resto de mensajes. 

El "límite de ritmo" (el subconjunto inicial de mensajes enviados) es variable en función de la plantilla. Tras el envío inicial, WhatsApp retendrá los mensajes restantes durante un máximo de 30 minutos. Durante este periodo de espera, evalúan la calidad de la plantilla basándose en las opiniones de los clientes. Si la respuesta es positiva, indicativa de una plantilla de alta calidad, entregan los mensajes restantes. Si la respuesta es negativa, eliminan el resto de mensajes no entregados, lo que evita que una mayor parte de tus clientes sigan haciendo comentarios negativos y te ayuda a evitar posibles problemas de aplicación de la calidad (como impactos en la valoración de la calidad del número de teléfono). 

Ten en cuenta que WhatsApp utiliza el mismo sistema para evaluar la calidad de la plantilla en el ritmo de plantillas que en la pausa de plantillas. Así, los mensajes no entregados durante la pausa de plantillas (debido a plantillas de baja calidad) son los mismos que se habrían pausado a mayor escala. 

En última instancia, esta actualización te proporciona un bucle de retroalimentación más rápido (30 minutos frente a horas o días con la pausa de la plantilla), para que puedas ajustar tus plantillas y ofrecer una mejor experiencia del cliente.

**Si tienes más preguntas sobre esta actualización, ponte en contacto con tu representante socio de Meta.**

### Junio de 2023: Experimentación con mensajería 
*Última actualización: junio de 2023*

A partir del 14 de junio de 2023, Meta está introduciendo nuevas prácticas de experimentación en la plataforma WhatsApp para evaluar cómo influyen los mensajes de mensajería en la experiencia y la interacción de los consumidores. Este experimento puede afectar a tus mensajes de marketing enviados en la API de WhatsApp Business con Braze.

Meta tiene la intención de continuar esta experimentación en la plataforma WhatsApp. Para más información, consulta [la documentación de Meta](https://developers.facebook.com/docs/whatsapp/on-premises/guides/experiments?content_id=86oue5PtwEgcBJl).

**La experimentación de WhatsApp sólo afecta a los mensajes de marketing.** Este experimento puede influir en la entrega de mensajes de plantillas de marketing. Las plantillas de utilidad y autenticación seguirán entregándose sin ningún impacto de experimentación.

En el experimento, Meta elige aleatoriamente como participantes a aproximadamente el 1% de los consumidores de WhatsApp. Si se elige, Meta no entregará plantillas de mensajes de marketing a estos consumidores a menos que se cumpla una de las siguientes condiciones:

- Si un consumidor te ha respondido en las últimas 24 horas;
- Si está abierta una conversación de marketing existente; o bien
- Si el consumidor ha hecho clic en un anuncio de WhatsApp en las últimas 72 horas.

## Preguntas más frecuentes {#faq}

### ¿Cómo sabré si mi mensaje de marketing se ha visto afectado por el experimento de Meta?

Si no se entrega un mensaje debido al experimento, aparecerá un código de error específico en el Registro de actividades y en Currents. El mensaje también se contará como un fallo y se incorporará a tus métricas de Fallos de WhatsApp en todos los informes del panel Braze. No se te cobrará por estos mensajes.

Este código de error 130472 dirá "El número del usuario forma parte de un experimento". Consulta [la documentación de Meta](https://developers.facebook.com/docs/whatsapp/cloud-api/support/error-codes?content_id=8SJRLBEjYGvXO9k) para obtener más información sobre los códigos de error de la API de WhatsApp Cloud.

### ¿Puedo excluirme del experimento de Meta?

No, Meta no permite ninguna adhesión voluntaria al experimento. Todos los proveedores y usuarios de la API de WhatsApp Business están sujetos a este Meta experimento.

### ¿Puedo intentar reenviar una plantilla más tarde?

No hay un tiempo fijo para este experimento. Como tal, un consumidor puede seguir estando sujeto al experimento.

### ¿Qué puedo hacer si mis mensajes de marketing no se entregan debido al experimento de Meta?

Te recomendamos que utilices otros canales de Braze, como el correo electrónico, los SMS, las notificaciones push o los mensajes dentro de la aplicación para enviar un mensaje con un contenido similar a tus usuarios previstos.
