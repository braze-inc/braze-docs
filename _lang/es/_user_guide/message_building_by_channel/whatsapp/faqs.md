---
nav_title: Preguntas frecuentes
article_title: Preguntas frecuentes sobre WhatsApp
page_order: 80
description: "Este artículo aborda algunas de las preguntas más frecuentes que surgen al configurar campañas de WhatsApp."
page_type: FAQ
channel:
  - WhatsApp

---

# Preguntas más frecuentes

> En esta página intentaremos responder a tus preguntas más exigentes sobre WhatsApp.<br><br>Estas FAQ no pretenden ofrecer asesoramiento jurídico ni pueden considerarse como tal. El uso del canal WhatsApp está sujeto a requisitos específicos de Meta Platforms, Inc. Para asegurarse de que está utilizando el canal WhatsApp de conformidad con todos los requisitos aplicables y cualquier ley a la que pueda estar sujeto específicamente, debe solicitar el asesoramiento de su asesor jurídico.

## Temas de las preguntas frecuentes
- [Cuentas de WhatsApp para empresas](#whatsapp-business-accounts)
- [Número de teléfono de la cuenta de WhatsApp para empresas](#whatsapp-business-account-phone-numbers)
- [Adhesión voluntaria y gestión de suscripciones](#opt-in-and-subscription-management) 
- [Límites de mensajería](#messaging-limits) 
- [Plantillas de WhatsApp](#whatsapp-templates)
- [Capacidad de entrega](#deliverability) 
- [Varios](#miscellaneous)

### Cuentas de WhatsApp para empresas 

#### ¿Cómo puedo crear una cuenta de WhatsApp para empresas? 
Te recomendamos que crees tu cuenta de WhatsApp para empresas (WABA) a través del flujo de registro integrado en el panel de control de Braze. 

#### Ya tengo una cuenta de empresa Meta. ¿Sigo necesitando una cuenta de WhatsApp para empresas? 
Sí, sigue siendo necesario crear una cuenta de WhatsApp para empresas. Te recomendamos que [anides tu WABA debajo de tu cuenta principal de empresa Meta]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/). 

#### ¿Cómo accedo a mi cuenta de WhatsApp Business? 
Después de completar el flujo de registro integrado, puedes acceder a tu cuenta en business.facebook.com accediendo a la [sección WhatsApp](https://business.facebook.com/wa/manage/home). 

#### ¿Puedo conectar varios WABA a Braze? 
Sí, puedes añadir hasta 10 cuentas de WhatsApp Business por espacio de trabajo, y cada cuenta de empresa puede estar anidada bajo un administrador de Meta Business diferente.

![Diagrama del ecosistema de Braze y WhatsApp, que muestra cómo se conectan entre sí los espacios de trabajo y las cuentas de WhatsApp Business: puedes conectar un grupo de suscripción a un número de teléfono, varias cuentas de WhatsApp Business a un espacio de trabajo y un espacio de trabajo a varias carteras Meta Business.]({% image_buster /assets/img/whatsapp/whatsapp_braze_ecosystem.png %}) 

### Números de teléfono de las cuentas de WhatsApp para empresas 

#### ¿Necesito un número de teléfono para mi cuenta de WhatsApp Business? 
Sí, necesita un número al que tenga acceso. Se te pedirá que verifiques tu número de teléfono con la autenticación de 2 factores cuando pases por el flujo de registro integrado. El número de teléfono no puede utilizarse para otras cuentas de WhatsApp (profesionales o personales).

#### ¿Qué tipos de números de teléfono admite WhatsApp? 
Consulte los requisitos de Meta para los [números de teléfono](https://developers.facebook.com/docs/whatsapp/phone-numbers) para obtener más información. 

#### ¿Puedo utilizar un mismo número de teléfono en varios WABA? 
No. Un número de teléfono no puede compartirse entre varios WABA. 

#### ¿Necesito un tipo específico de número de teléfono para enviar mensajes a determinados países? 
No. WhatsApp le permite enviar mensajes a usuarios finales desde cualquier número de teléfono compatible en cualquier país. Consulte los requisitos de Meta para los [números de teléfono](https://developers.facebook.com/docs/whatsapp/phone-numbers) para obtener más información. 

#### ¿Necesito utilizar un número de teléfono específico para enviar a determinados países?
No. Con WhatsApp, cualquier número de teléfono compatible puede enviar a usuarios finales de cualquier país compatible.

### Adhesión voluntaria y gestión de suscripciones 

#### ¿Necesito recabar el consentimiento para enviar mensajes de marketing a los usuarios finales en WhatsApp? 
Sí, WhatsApp exige a las empresas que [recaben el consentimiento expreso](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/) para enviar mensajes de marketing a los usuarios finales.

#### ¿Puedo enviar mensajes proactivos a los usuarios finales en WhatsApp para recabar su consentimiento? 
Si decide enviar mensajes de forma proactiva a los usuarios finales, el primer mensaje iniciado por la empresa debe preguntar al usuario si desea recibir mensajes de marketing de su empresa y debe cumplir los requisitos de Meta para [obtener la aceptación](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/). Ten en cuenta que WhatsApp controlará la reputación de tu empresa en el canal, por lo que la mejor práctica recomendada es ser explícito con los usuarios finales y enviar únicamente mensajes que hayan indicado que quieren recibir.
 
#### ¿Tengo que recoger el número de teléfono del usuario final cuando recopilo la adhesión voluntaria? 
Necesitas tener el número de teléfono del usuario final en el perfil de Braze para enviarle un mensaje. 
- Si ya tienes su número, no necesitas recopilarlo durante la adhesión voluntaria. 
- Si no dispone del número del usuario final, su método de opt-in debe incluir la captura del número de teléfono. 

#### ¿Cómo actualizo el estado de suscripción de los usuarios finales que se registran? 
La gestión de suscripciones del Canal WhatsApp funciona de forma similar a como lo hace en otros canales Braze. Consulte [Gestión de suscripciones de usuarios]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/) para obtener más información.  

#### Si ya tengo una lista de usuarios que han optado por recibir mensajes de marketing en WhatsApp, ¿cómo actualizo su estado de suscripción en Braze? 
Puede actualizar su estado de suscripción mediante [la importación de usuarios]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import#importing-custom-data). 

#### ¿Qué métodos debo utilizar para recopilar las adhesiones voluntarias? 
Braze recomienda consultar [las directrices de Meta sobre los métodos de adhesión voluntaria](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/) para mantener el cumplimiento. Consulta el siguiente recurso para obtener [ideas y sugerencias sobre el canal Braze y la adhesión voluntaria](https://docs.google.com/document/d/1rNKnKN2oIn-e9bXdYEvnwdlzlCsEOKs-xREcdVvPBE8/edit).

#### ¿Es necesaria la doble adhesión voluntaria para WhatsApp? 
No, la doble adhesión voluntaria no es necesaria. 

#### ¿Cómo pueden excluirse mis usuarios de los mensajes de WhatsApp? 
Sus usuarios pueden excluirse de dos maneras:
1. Configure un mensaje entrante de WhatsApp con una palabra de exclusión específica y utilice un webhook para actualizar el estado de suscripción del usuario.
2. Añade una respuesta rápida de exclusión dentro de la plantilla de WhatsApp, con un webhook correspondiente para actualizar. 

### Límites de mensajería 

#### ¿Cuáles son los límites de la mensajería? 
Los límites de mensajería son un concepto de construcción de la integridad de WhatsApp. Determinan el número máximo de conversaciones iniciadas por empresas que cada número de teléfono puede iniciar en un periodo móvil de 24 horas. Hay cuatro niveles de límite de mensajería: 1000, 10 000, 100 000 e ilimitado.

#### ¿Cómo puedo aumentar mi límite de mensajes? 
WhatsApp aumentará tu límite de mensajes si cumples las siguientes condiciones:
1. [El estado del número de teléfono](https://www.facebook.com/business/help/896873687365001) es **Conectado** 
2. [La calidad del número de teléfono](https://www.facebook.com/business/help/896873687365001) es **media** o **alta**
3. En los últimos siete días, has iniciado X o más conversaciones con usuarios únicos, donde X es tu límite de mensajería actual dividido por 2 

Así, para pasar de 100 000 a ilimitado, debes enviar al menos 50 000 conversaciones iniciadas por empresas en un período de 7 días. 

#### ¿Cuánto se tarda en aumentar mis límites de mensajería? 
Si se cumplen todas las condiciones anteriores, puedes aumentar tu límite de mensajería de 1k a ilimitado en 4 días. 

#### ¿Dónde puedo ver mi límite actual de mensajes? 
Puedes comprobar tus límites de mensajería actuales en **WhatsApp Manager > Panel general >** pestaña Insights. 

#### ¿Qué ocurre si intento enviar mensajes cuando ya he alcanzado mi límite de mensajes?
Si intentas enviar una campaña o Canvas a más usuarios únicos de los que permite tu límite actual, los mensajes no se enviarán. Braze continuará intentando reenviar los mensajes si/cuando tu límite de mensajería aumente durante un máximo de un día. 

#### ¿Puede disminuir mi límite de mensajería?
Sí, si el índice de calidad de tu número de teléfono baja demasiado, corres el riesgo de que WhatsApp disminuya tu límite de mensajes. Braze te recomienda suscribirte y recibir notificaciones de actualizaciones de WhatsApp relacionadas con la calidad, incluidas las actualizaciones del estado de tu número de teléfono y el nivel de límite de mensajes. Puedes suscribirte a las notificaciones directamente en el panel de WhatsApp Manager. 

#### ¿Cuál es el límite de rendimiento de Meta?
Meta tiene su propio límite de rendimiento independiente del límite de mensajería de WABA. El límite predeterminado que admite la API de la nube es de 80 mensajes por segundo. Si cree que sus campañas superarán este límite, puede [solicitar](https://developers.facebook.com/docs/whatsapp/cloud-api/overview/#throughput) que se aumente su límite. Meta recomienda que envíes esta solicitud al menos tres días antes del envío de la campaña.

### Plantillas de WhatsApp 

#### ¿Qué es una plantilla de WhatsApp? 
WhatsApp exige que todos los mensajes iniciados por empresas comiencen utilizando una plantilla aprobada. La plantilla incluye el texto del mensaje, junto con medios enriquecidos opcionales como imágenes, llamadas a la acción y botones de respuesta rápida. Una vez que WhatsApp apruebe las plantillas, podrán utilizarse para redactar un mensaje de WhatsApp en Braze. 

#### ¿Dónde puedo crear, editar y gestionar mis plantillas de WhatsApp? 
Crearás, editarás, gestionarás y enviarás plantillas para su aprobación directamente en el administrador de WhatsApp. Una vez que tu WABA esté conectada a Braze, verás todas tus plantillas en el panel de control con un indicador de estado. Si se rechaza una plantilla, volverá a enviarla directamente a través del gestor de WhatsApp. **Las plantillas no pueden crearse ni editarse directamente en Braze.**

#### ¿Cuánto tarda WhatsApp en revisar el envío de una plantilla? 
El proceso de aprobación puede tardar hasta 24 horas, pero a menudo las plantillas se procesan en cuestión de horas o minutos. 

#### ¿Cuántas plantillas puedo tener a la vez? 
El límite de su plantilla de mensajes depende del estado de verificación de su empresa. Puedes comprobar tu límite en la página **Administrador de WhatsApp > Plantillas de mensajes**. 

#### ¿Cómo personalizo la copia de plantilla y los medios enriquecidos en Braze? 
WhatsApp permite insertar parámetros variables en las plantillas de mensajes. Los mensajes no pueden empezar ni terminar con un parámetro variable. Los parámetros variables pueden rellenarse con lógica líquida en la plataforma Braze. Consulte [redactar un mensaje de WhatsApp en Braze]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create#step-2-compose-your-whatsapp-message) para obtener más información sobre los parámetros variables. 

#### Mi plantilla ha sido rechazada. ¿Puede Braze ayudarme a que me lo aprueben? 
El equipo Braze no tiene visibilidad sobre los rechazos de plantillas. Deberá trabajar directamente con su gestor de WhatsApp Business para editar y volver a enviar la plantilla. Asegúrese de proporcionar una plantilla de muestra cuando sea necesario. Comprueba que tu plantilla sigue las políticas [comerciales](https://www.whatsapp.com/legal/business-policy/?fbclid=IwAR2qWg6yFKdyjDMxJkbNSM38FLGsxXxffC1qStY2gaHOyp-gl_8g72rZNIw) o [empresariales](https://www.whatsapp.com/legal/commerce-policy/?fbclid=IwAR3bzN3LTZ-7kO-wnO7X3smtPKGy0asxaFod-U1Ub8B9JUpnrfy1_y7LpAQ) de Meta.

#### ¿Se pueden dirigir o personalizar los medios enriquecidos en Braze? 
Las imágenes se pueden cargar desde la biblioteca multimedia, pero no se pueden orientar dinámicamente. En el caso de las URL, la última parte del enlace puede rellenarse dinámicamente con Liquid. 

### Capacidad de entrega 

#### ¿Por qué no se entrega un mensaje? 
Hay varias razones por las que un mensaje no puede ser entregado, incluyendo problemas de red y el dispositivo está apagado. 

#### Si un mensaje no se entrega, ¿se me facturará? 
No. Si un mensaje no se entrega, no se le facturará. 

#### ¿Qué ocurre si un usuario final bloquea mi negocio? 
Si un usuario final bloquea tu empresa, los mensajes posteriores que intentes enviar no se entregarán y no se te facturarán. 

#### ¿Qué ocurre si un usuario final notifica un mensaje? 
Si un usuario final notifica un mensaje, puede seguir enviándole mensajes posteriores. Sin embargo, la presentación de informes puede afectar a su calificación de calidad en el canal. 

#### Si un usuario final bloquea o denuncia mi empresa, ¿se actualizará su estado de suscripción en Braze? 
No. Su estado de suscripción a Braze no se actualizará. 

### Varios

#### ¿Es Braze compatible con casos de uso de asistencia al cliente como chatbots y chat asistido por humanos para WhatsApp? 
No admitimos chatbots ni chat asistido por humanos dentro de Braze ni a través de integraciones directas. 

Si ya utilizas WhatsApp como canal de atención al cliente, te recomendamos que mantengas tu configuración actual y crees un nuevo WABA a través de Braze para la mensajería de marketing. Este WABA requerirá un nuevo número de teléfono. 

#### ¿Cómo puedo "salvar la distancia" entre mis mensajes de asistencia al cliente y mis mensajes de marketing a través de Braze? 
Puede utilizar las propiedades de WhatsApp Liquid para reenviar el contenido de los mensajes entrantes de WhatsApp (incluido el cuerpo del mensaje y las URL multimedia) desde Braze a otras plataformas, incluida cualquier herramienta de atención al cliente. Para más detalles, consulte nuestras [Etiquetas de personalización con soporte]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/). 

Para enviar información a Braze, por ejemplo, para indicar que un usuario está en una conversación de soporte activa, puede registrar un atributo personalizado (como un booleano "tiene chat de soporte existente = verdadero/falso") y utilizarlo como criterio de segmentación en sus campañas de marketing. También puede establecer enlaces profundos entre dos hilos de chat para dirigir a los usuarios al hilo de asistencia desde el hilo de marketing y viceversa. 

#### ¿Braze almacena las respuestas de los usuarios? 
Los mensajes sólo se almacenan el tiempo necesario para procesarlos. Para acceder a los mensajes de los usuarios, utilice Currents. 

#### ¿Cómo deben almacenarse los números de teléfono de los usuarios en Braze? 
Los números de teléfono de los usuarios deben almacenarse en [formatoE.164 ]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_phone_numbers/#formatting).

#### ¿Qué tipo de rich media admiten las plantillas de WhatsApp? 
Puede añadir imágenes, llamadas a la acción (URL o número de teléfono) y botones de respuesta rápida a las plantillas de WhatsApp. Puede añadir estos elementos cuando cree plantillas directamente en WhatsApp. 

#### ¿Puedo importar los números de teléfono de los usuarios? 
Sí. Puede [importar los números de teléfono de los usuarios]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_phone_numbers/). 

#### ¿Qué es la verificación empresarial? 
La verificación del negocio es un concepto de WhatsApp utilizado para garantizar que la marca es un negocio legítimo. Se puede completar en el Gestor de WhatsApp. La verificación empresarial también es necesaria para escalar la mensajería. Sin verificación empresarial, los clientes sólo pueden enviar hasta 250 usuarios finales únicos en un periodo de 24 horas consecutivas. 

#### ¿Qué es una cuenta oficial de negocios? 
OBA le da la marca de verificación verde junto a su nombre para mostrar y es opcional. Puede solicitar una cuenta de empresa oficial después de completar la verificación de la empresa. Ten en cuenta que la verificación empresarial y una cuenta empresarial oficial son conceptos de WhatsApp diferentes. 

#### ¿Qué métricas están disponibles en el panel de Braze? 
Puede ver destinatarios únicos, envíos, entregas, lecturas y fallos en el panel Braze. Tenga en cuenta que los recibos de lectura de los usuarios finales deben estar "Activados" para que Braze realice un seguimiento de las lecturas. También puede configurar eventos de conversión para supervisar el rendimiento de la campaña, de forma similar a otros canales. 

#### ¿Qué es una conversación de WhatsApp? 
WhatsApp es un canal centrado en la mensajería bidireccional y, por tanto, se centra en las conversaciones (en lugar del número de mensajes individuales). Una conversación es un hilo de 24 horas entre una empresa y un usuario final.

- **Conversación iniciada por la empresa**: Una conversación en la que la empresa comienza enviando un mensaje de plantilla aprobado al usuario final. Cuando la empresa envía un mensaje en respuesta, comienza el plazo de 24 horas.
- **Conversación iniciada por el usuario**: Una conversación en la que el usuario final envía un mensaje a la empresa. Cuando la empresa envía un mensaje en respuesta, comienza el plazo de 24 horas.

#### ¿Qué factores afectan a la calificación de la calidad del número de teléfono y qué ocurre cuando mi calificación de calidad baja demasiado? 
Entre los factores que afectan a la calificación de la calidad del número de teléfono se incluyen el bloqueo de una empresa por parte de un usuario final (y las razones que aduce cuando bloquea una empresa) y la denuncia de una empresa por parte de un usuario final. 

Cuando el índice de calidad es bajo, el estado del número de teléfono cambia de **Conectado** a **Señalado**. Si la calidad no mejora en siete días, el estado vuelve a ser **Conectado**. Sin embargo, el límite de mensajes disminuirá al siguiente nivel. Por ejemplo, un número de teléfono que antes tenía un límite de 100.000 mensajes ahora tiene un límite de 10.000 mensajes.
