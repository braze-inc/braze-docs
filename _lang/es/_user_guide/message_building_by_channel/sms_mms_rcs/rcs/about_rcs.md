---
nav_title: "Sobre RCS"
article_title: Acerca de los Servicios de Comunicación Enriquecidos (RCS)
alias: /about_rcs/
page_type: reference
page_order: 0
description: "Este artículo de referencia cubre los casos de uso generales del canal RCS y los requisitos necesarios para que tu canal RCS esté listo para su uso."
---

# Acerca de los Servicios de Comunicación Enriquecidos (RCS)

> Los Servicios de Comunicación Enriquecidos (RCS) mejoran los SMS tradicionales, habilitando a las marcas para entregar mensajes no sólo informativos, sino también mucho más interactivos. Ahora compatible tanto con Android como con iOS, RCS aporta características como medios de alta calidad, botones interactivos y perfiles de remitente de marca directamente en las aplicaciones de mensajería preinstaladas de los usuarios, eliminando la necesidad de descargar una aplicación aparte.

A diferencia de las aplicaciones de mensajería de terceros, RCS aprovecha el entorno de mensajería nativo (Mensajes de Apple y Mensajes de Google), lo que te permite llegar a los usuarios donde ya pasan la mayor parte de su tiempo e ir más allá de las experiencias tradicionales de SMS y MMS, habilitando una comunicación más rica e interactiva con los clientes. 

## Ventajas de utilizar RCS

- **Experiencias del cliente más enriquecedoras:** Entrega experiencias de usuario más ricas integrando fácilmente texto, elementos visuales e interactivos, potenciando la interacción y allanando el camino para campañas personalizadas basadas en datos.
- **Interacciones de marca de confianza:** Consigue interacciones de marca de confianza mediante un ID de remitente verificado que no sólo muestre los activos de tu marca, sino que también cumpla las normas de privacidad más exigentes del sector, aumentando la confianza y fidelización de los clientes.
- **Entrega flexible de mensajería:** Facilita una entrega de mensajería flexible y fiable con una alternativa de SMS sin interrupciones que llega a todos los segmentos de audiencia, independientemente de las capacidades del dispositivo, al tiempo que preserva una experiencia de usuario coherente.
- **Información accionable:** Desbloquea información accionable con informes avanzados que realizan un seguimiento de los KPI críticos, permitiéndote optimizar las campañas en tiempo real e impulsar un éxito mensurable.
- **Sinergia omnicanal:** Integra fácilmente RCS en tu estrategia global de marketing para entregar experiencias del cliente consistentes y a través de canales, amplificando la eficacia de la campaña y el ROI general.

## Ejemplos

| Casos de uso | Descripción |
| --- | --- |
| Promociones interactivas de productos | Da vida a las promociones de productos combinando imágenes atractivas o videos cortos con documentación detallada de los productos. Aprovecha las respuestas sugeridas (como "Añadir al carrito" o "Aprender") y las acciones de abrir URL para impulsar la exploración inmediata del producto y la conversión, todo ello dentro de una experiencia de mensajería enriquecida. |
| Actualizaciones personalizadas de fidelización y recompensas | Entrega mensajes de fidelización personalizados enriquecidos con elementos visuales de alta calidad y detalles de recompensa. Utiliza respuestas sugeridas (como "Canjear ahora" o "Ver ofertas") y acciones openURL para crear un recorrido del cliente interactivo, haciendo que cada actualización sea visualmente atractiva y esté adaptada para inspirar una interacción inmediata y una mayor retención. |
| Alertas seguras de transacciones y cuentas | Entrega alertas seguras de cuentas y notificaciones de transacciones incluyendo imágenes de recibos o documentación en PDF. Las acciones sugeridas (como "Revisar ahora" o "Contactar con soporte") y los enlaces openURL habilitan a los clientes a acceder rápidamente a más detalles o iniciar pasos de seguridad, reforzando tanto la fiabilidad como la confianza en cada interacción. |
| Mejoras en el itinerario de viaje y las reservas | Mejora la experiencia de viaje enviando itinerarios visualmente ricos, guías de destinos o tarjetas de embarque. Con las acciones openURL, los clientes pueden acceder rápidamente a las modificaciones de la reserva o a las actualizaciones en tiempo real (como los cambios de horario) sin salir de la ventana de mensajería, lo que facilita un viaje fluido y atractivo de principio a fin. |
| Opiniones de clientes y cuestionarios interactivos | Capta opiniones procesables desplegando cuestionarios interactivos que utilicen una mezcla de contenido multimedia enriquecido y texto. Integra respuestas sugeridas para respuestas rápidas y acciones openURL para acceder a formularios de cuestionarios más completos, facilitando que los clientes compartan sus opiniones, ayudando a los especialistas en marketing a perfeccionar sus estrategias basándose en los comentarios en tiempo real de todos los verticales. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Requisitos

| Requisito | Descripción |
| --- | --- |
| Créditos de los mensajes | Ponte en contacto con tu administrador de cuentas Braze para confirmar que has adquirido créditos de mensajería en tu contrato. Los Créditos de mensajes son un elemento de contrato flexible que te permite comprar y asignar volumen de mensajería a través de varios canales, como SMS, MMS, RCS y WhatsApp. |
| País elegible | Asegúrate de que estás enviando RCS a usuarios de uno de los países admitidos por Braze: Estados Unidos, Reino Unido, Alemania, México, Suecia, España, Singapur, Brasil, Francia, Italia, Colombia |
| Remitente verificado RCS | El remitente que el destinatario ve en su dispositivo para identificar de dónde procede el mensaje. Un remitente verificado por RCS consiste en un nombre de empresa, una marca visual y una señal verificada. <br><br> Braze te ayudará a solicitar y registrarte como remitente verificado de RCS en las regiones elegibles. Tendrás que proporcionar a tu representante de Braze algunos datos básicos. |
| Lista de usuarios con números de teléfono | Antes de empezar a enviar mensajes, debes añadir usuarios a tu cuenta. Además, debes conocer el tamaño aproximado de tu audiencia. Los usuarios y los números de teléfono pueden añadirse a Braze por varios métodos diferentes. Los números de teléfono deben tener un formato de 10 dígitos, así como el prefijo del país. Para saber más, consulta [Números de teléfono de usuario]({{site.baseurl}}/user_phone_numbers/). |
| Palabras clave y respuestas | Todas las palabras clave base deben tener atribuidas respuestas antes de que puedas empezar a enviar mensajes. Braze procesará la adhesión voluntaria, la exclusión voluntaria y las palabras clave de ayuda automáticamente. Existen opciones de personalización y configuraciones adicionales de palabra clave-respuesta. Para saber más, consulta las [palabras clave de adhesión voluntaria y exclusión voluntaria]({{site.baseurl}}/optin_optout/). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Términos que debe conocer

| Plazo | Definición |
|----|----|
| Grupo de suscripción | Un grupo de usuarios suscritos a un caso de uso de mensajería específico. Cada grupo de suscripción está vinculado a uno o varios "remitentes" de marca, que pueden ser remitentes verificados RCS, códigos SMS o ambos. Por ejemplo, si planeas enviar mensajes RCS transaccionales y promocionales, puedes optar por configurar dos grupos de suscripción con remitentes separados verificados por RCS en tu panel Braze. |
| Remitente verificado por RCS | La entidad remitente de un mensaje RCS, o lo que el destinatario del mensaje RCS ve en su dispositivo para identificar de dónde procede el mensaje. Los remitentes verificados por RCS contienen un nombre de empresa, un pie de foto, una marca visual y una señal verificada. Después de proporcionar a Braze la información necesaria para el registro de remitentes RCS, nosotros nos encargamos del registro y de la configuración del grupo de suscripción. |
| SMS alternativo | Si no se puede entregar un mensaje con RCS (por ejemplo, por falta de soporte de un operador en la región), Braze intentará entregar el mensaje a través de SMS cuando exista un código SMS dentro del grupo de suscripción. |
| RCS solo texto | Esta categoría incluye mensajes RCS sencillos que se limitan a texto, similares a los SMS tradicionales. Estos mensajes pueden tener hasta 160 caracteres y proporcionan un nivel básico de comunicación sin ningún elemento multimedia enriquecido.<br><br> Puedes enviar mensajes de texto de hasta 3.072 caracteres de longitud. Sin embargo, cuando superen los 160 caracteres, se facturarán igual que un mensaje RCS enriquecido (un mensaje RCS único). |
| Mensaje RCS enriquecido | Los mensajes RCS enriquecidos aprovechan las características más atractivas y enriquecidas que ofrece RCS, como medios, botones y mucho más. |
| "Básico" y "único" | Los mensajes RCS se facturan principalmente de dos formas: como mensajes Básicos y como mensajes Únicos. "Básico" corresponde a RCS sólo texto, mientras que "Único" corresponde a RCS enriquecido. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
