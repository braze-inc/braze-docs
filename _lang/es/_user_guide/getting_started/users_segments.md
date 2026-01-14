---
nav_title: Usuarios y segmentos
article_title: "Cómo empezar: Usuarios y segmentos"
page_order: 2
page_type: reference
description: "Este artículo ofrece un resumen de los usuarios y los segmentos, destacando su importancia y cómo pueden aprovecharse para interactuar con tu audiencia."

---

# Cómo empezar: Usuarios y segmentos

Comprender a tus usuarios y dirigirte a ellos con eficacia es crucial para enviar campañas de marketing personalizadas y dirigidas. Este artículo ofrece un resumen de los usuarios y los segmentos, destacando su importancia y cómo pueden aprovecharse para interactuar con tu audiencia.

## Usuarios

En Braze, la información sobre tu audiencia se almacena en perfiles de usuario. Un [perfil de usuario]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/) es una colección completa de información y atributos que describen a un consumidor individual. Sirve como repositorio central para almacenar y gestionar datos relacionados con su comportamiento, preferencias y detalles demográficos.

### Partes de un perfil de usuario

Al comprender los perfiles de usuario, puedes obtener información sobre tu audiencia e interactuar con ella a un nivel personalizado y específico. El perfil de un usuario contiene mucha información, pero aquí tienes algunas de las partes clave:

- **Identificador de usuario:** Cada perfil de usuario está identificado de forma única por un ID de usuario, llamado `external_id`. Este identificador permite a Braze seguir y asociar los datos de usuario en diferentes canales y dispositivos, proporcionando una visión unificada de las interacciones de cada usuario con tu marca. [Los perfiles de usuario anónimos]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/anonymous_users/) (usuarios que visitan tu sitio web o aplicación sin iniciar sesión) no tienen un `external_id`, pero se les pueden asignar [alias de usuario]({{site.baseurl}}/user_guide/data/user_data_collection/anonymous_users/#assigning-user-aliases) como identificador alternativo.
- [Atributos](#attributes)**:** Son datos concretos sobre el usuario, como su nombre, edad, ubicación o cualquier otra información demográfica. Puedes utilizar estos atributos para segmentar tu audiencia y personalizar tu mensajería.
- [Eventos](#events)**:** Son acciones que realiza el usuario, como hacer una compra, hacer clic en un enlace o abrir una aplicación. Braze realiza un seguimiento de estos eventos para ayudarte a comprender el comportamiento y la interacción del usuario. De forma similar a los atributos, también puedes utilizar los eventos para segmentar y personalizar.
- **Compras:** Esta sección registra el historial de compras del usuario. Es crucial para comprender los hábitos de compra y las preferencias del usuario.
- **Dispositivos:** Esta sección enumera los dispositivos que el usuario ha utilizado para interactuar con tu marca. Puede incluir dispositivos móviles, navegadores web y dispositivos conectados (como wearables y televisiones inteligentes).
- **La interacción:** Esta sección contiene información sobre las interacciones del usuario con los mensajes que le envías, a qué segmentos pertenece, estado de suscripción, etc.
- **Historial de mensajes:** Se trata de un registro de todos los mensajes que se han enviado al usuario desde el canal de mensajería correspondiente (como correo electrónico o push).

{% alert tip %}
Los SDK de la plataforma Braze recogen automáticamente 27 atributos y eventos diferentes. Utilizando estos eventos y atributos estándar, puedes crear segmentos en cuanto integres el SDK.
{% endalert %}

### Atributos

Los atributos son características o propiedades específicas asociadas a un usuario. Estos atributos te ayudan a segmentar y dirigirte a los usuarios en función de sus rasgos e intereses únicos. Hay dos tipos de atributos en Braze: atributos estándar y atributos personalizados.

#### Atributos estándar

Los atributos estándar son atributos predefinidos que puedes seguir con Braze tras integrar el SDK en tu aplicación. Son datos comunes del usuario que la mayoría de las aplicaciones encontrarían útiles, como datos demográficos y datos de dispositivo. Algunos ejemplos son:

- Nombre
- Apellidos
- Correo electrónico
- Género
- Fecha de nacimiento
- País
- Ciudad
- Última aplicación utilizada
- Lengua
- Zona horaria

#### Atributos personalizados

[Los atributos personalizados]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/) son atributos que defines en función de las necesidades específicas de tu empresa. Te permiten hacer un seguimiento de la información que es única para tu aplicación o negocio. 

Por ejemplo, una aplicación de streaming de música puede hacer un seguimiento de atributos personalizados como:

- Género favorito
- Número de canciones reproducidas
- Suscriptor Premium (Sí/No)
- Artista favorito

Por otra parte, una aplicación de comercio minorista puede hacer un seguimiento de atributos personalizados como:

- Talla de ropa preferida
- Marca favorita
- Número de compras
- Miembro del programa de fidelización (Sí/No)

Los atributos personalizados te dan flexibilidad para recopilar y analizar los datos más relevantes para tu negocio. Sin embargo, requieren una configuración adicional.

Tanto los atributos estándar como los personalizados pueden utilizarse para segmentar tu audiencia y personalizar tus mensajes de marketing. Por ejemplo, podrías enviar una oferta especial a los usuarios de una determinada ciudad (atributo estándar) que hayan realizado más de 10 compras (atributo personalizado).

### Eventos

Los eventos representan acciones o comportamientos específicos realizados por los usuarios dentro de tu aplicación o sitio web. Ejemplos de eventos pueden ser lanzamientos de aplicaciones, compras, visualizaciones de contenidos o cualquier otra acción. Mediante el seguimiento y el análisis de estos eventos, puedes obtener información sobre el comportamiento de los usuarios y las pautas de interacción.

#### Eventos estándar

[Los eventos estándar]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/events#standard-events) son eventos predefinidos que Braze sigue automáticamente después de integrar el SDK en tu aplicación o sitio web. Algunos ejemplos de actos estándar son

- **Inicio de la sesión:** Este evento se desencadena cuando un usuario abre la aplicación.
- **Fin de sesión:** Este evento se desencadena cuando un usuario cierra la aplicación.
- **Compra:** Este evento se desencadena cuando un usuario realiza una compra dentro de la aplicación.
- **Clic en notificación push:** Este evento se desencadena cuando un usuario hace clic en una notificación push.

#### Eventos personalizados

[Los eventos personalizados]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) son eventos que defines en función de las acciones específicas que quieres seguir dentro de tu aplicación o sitio web. Por ejemplo, una aplicación de streaming de música puede hacer un seguimiento de eventos personalizados como:

- Canción reproducida
- Lista de reproducción creada
- Anuncio omitido

Por otro lado, una aplicación de fitness puede hacer un seguimiento de eventos personalizados como:

- Entrenamiento iniciado
- Entrenamiento completado
- Conjunto de registros personales

Los eventos personalizados te dan la flexibilidad de hacer un seguimiento de las acciones más relevantes para tu aplicación y tu negocio. Sin embargo, al igual que los atributos personalizados, requieren una configuración adicional.

### Puntos de datos

Braze utiliza puntos de datos para ayudarte a definir la información más impactante para tu negocio. Los puntos de datos son una parte crucial del funcionamiento de Braze y se utilizan para la facturación, la fijación de precios y, lo que es más importante, la personalización y optimización de tus campañas de marketing.

Los puntos de datos se consumen cuando se actualizan los datos del perfil de un usuario o cuando éste realiza acciones específicas. Estas acciones pueden incluir iniciar una sesión, finalizarla, grabar un evento personalizado o realizar una compra. Es importante tener en cuenta que no todos los datos recopilados por Braze cuentan como puntos de datos. Por ejemplo, los datos y eventos predeterminados por los Servicios Braze, como los tokens de notificaciones push, la información del dispositivo y todos los eventos de seguimiento de la interacción de la campaña, como las aperturas de correo electrónico y los clics en notificaciones push, no se cuentan como puntos de datos.

Al considerar detenidamente qué información rastrear como puntos de datos, te diriges a los datos de mayor impacto para la experiencia de tus usuarios. Tu director de cuentas Braze te ayudará a recomendar las mejores prácticas de datos que se ajusten a tus necesidades.

Visita nuestro artículo dedicado para saber más sobre [los puntos de datos]({{site.baseurl}}/user_guide/data/data_points/).

## Segmentos

[La segmentación]({{site.baseurl}}/user_guide/engagement_tools/segments) te permite dirigirte a los usuarios en función de sus características y acciones demográficas, de comportamiento, sociales o técnicas (es decir, atributos y eventos). El uso creativo e inteligente de la segmentación y la automatización de la mensajería te habilita para mover fácilmente a tus usuarios a través de su recorrido por el ciclo de vida del cliente.

Consejos para trabajar con segmentos:

- Los segmentos en Braze son dinámicos: los usuarios siempre entran y salen de los segmentos, ya que no siempre se ajustan a los criterios. Los usuarios que se ajusten a los criterios de un segmento en el momento del envío serán los destinatarios de esa campaña o Canvas.
    - Si quieres que tu segmento sea estático, puedes utilizar Extensiones de segmento. Las extensiones de segmento (con [la regeneración desactivada]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/#extension-regeneration)) representan a tu audiencia como una única instantánea en el tiempo.
- No estás limitado a utilizar un filtro cada vez. Crea segmentos finos y granulares superponiendo varios filtros.
- Puedes utilizar las acciones o inacciones de tus usuarios para saber cómo llegar a ellos allí donde quieren interactuar contigo. Estas acciones pueden ser eventos personalizados, interacción con una campaña o Canvas existente, o incluso un mensaje específico dentro de un Canvas.

### Casos de uso

Supongamos que diriges una tienda de ropa online y has configurado un flujo de mensajería para enviar una serie de correos electrónicos a los usuarios que han añadido un artículo a su cesta pero no han completado la compra. Este flujo de carritos abandonados podría incluir un correo electrónico recordatorio inicial, un correo electrónico de seguimiento ofreciendo un descuento y un correo electrónico recordatorio final.

\![]({% image_buster /assets/img/getting_started/segment_example.png %}){: style="max-width:70%" }

Podrías crear un segmento de usuarios que han desencadenado el evento personalizado "Artículo añadido a la cesta" pero no han desencadenado el evento personalizado "Compra completada". Luego, dentro de este segmento, podrías identificar aún más a los usuarios que han abierto el correo electrónico recordatorio inicial (interacción con un mensaje específico) pero no han realizado una compra.

\![]({% image_buster /assets/img/getting_started/segment_example_breakdown.png %})

Este segmento podría ser objeto de una campaña más agresiva para intentar convertir a estos usuarios en compradores. Por ejemplo, podrías enviarles una oferta especial o una recomendación personalizada basada en los artículos de su cesta.

Éste es sólo un ejemplo de cómo puedes utilizar las acciones e inacciones de los usuarios, los eventos personalizados y los datos de interacción para crear segmentos y adaptar tus estrategias de marketing en Braze.

