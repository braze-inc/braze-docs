---
nav_title: Usuarios y segmentos
article_title: "Cómo empezar: Usuarios y segmentos"
page_order: 2
page_type: reference
description: "Este artículo ofrece una visión general de los usuarios y los segmentos, destacando su importancia y cómo pueden aprovecharse para atraer a su audiencia."

---

# Cómo empezar: Usuarios y segmentos

Comprender a sus usuarios y dirigirse a ellos con eficacia es crucial para enviar campañas de marketing personalizadas y específicas. Este artículo ofrece una visión general de los usuarios y los segmentos, destacando su importancia y cómo pueden aprovecharse para atraer a su audiencia.

## Usuarios

En Braze, la información sobre su público se almacena en perfiles de usuario. Un [perfil de usuario]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/) es una colección completa de información y atributos que describen a un consumidor individual. Sirve de repositorio central para almacenar y gestionar datos relacionados con su comportamiento, preferencias y detalles demográficos.

### Partes de un perfil de usuario

Si conoce los perfiles de los usuarios, podrá conocer mejor a su audiencia y relacionarse con ella de forma personalizada y específica. El perfil de un usuario contiene mucha información, pero he aquí algunas de las partes clave:

- **Identificador de usuario:** Cada perfil de usuario se identifica unívocamente mediante un identificador de usuario, denominado `external_id`. Este identificador permite a Braze rastrear y asociar los datos de los usuarios a través de diferentes canales y dispositivos, proporcionando una visión unificada de las interacciones de cada usuario con su marca. [Los perfiles de usuario anónimos]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/anonymous_users/) (usuarios que visitan tu sitio web o aplicación sin iniciar sesión) no tienen un `external_id`, pero se les pueden asignar [alias de usuario]({{site.baseurl}}/user_guide/data/user_data_collection/anonymous_users/#assigning-user-aliases) como identificador alternativo.
- [Atributos](#attributes)**:** Son datos específicos sobre el usuario, como su nombre, edad, ubicación o cualquier otra información demográfica. Puede utilizar estos atributos para segmentar su audiencia y personalizar sus mensajes.
- [Eventos](#events)**:** Son acciones que realiza el usuario, como comprar, hacer clic en un enlace o abrir una aplicación. Braze realiza un seguimiento de estos eventos para ayudarle a comprender el comportamiento y la participación del usuario. De forma similar a los atributos, también puede utilizar los eventos para segmentar y personalizar.
- **Compras:** Esta sección registra el historial de compras del usuario. Es crucial para comprender los hábitos de compra y las preferencias del usuario.
- **Dispositivos:** Esta sección enumera los dispositivos que el usuario ha utilizado para interactuar con su marca. Puede incluir dispositivos móviles, navegadores web y dispositivos conectados (como wearables y televisores inteligentes).
- **Compromiso:** Esta sección contiene información sobre las interacciones del usuario con los mensajes que le envías, a qué segmentos pertenece, estado de suscripción, etc.
- **Historial de mensajes:** Se trata de un registro de todos los mensajes que se han enviado al usuario desde el canal de mensajería correspondiente (como correo electrónico o push).

{% alert tip %}
Los SDK de la plataforma Braze recopilan automáticamente 27 atributos y eventos diferentes. Utilizando estos eventos y atributos estándar, puede crear segmentos tan pronto como integre el SDK.
{% endalert %}

### Atributos

Los atributos son características o propiedades específicas asociadas a un usuario. Estos atributos le ayudan a segmentar y dirigirse a los usuarios en función de sus rasgos e intereses únicos. Existen dos tipos de atributos en Braze: atributos estándar y atributos personalizados.

#### Atributos estándar

Los atributos estándar son atributos predefinidos que puedes seguir con Braze tras integrar el SDK en tu aplicación. Se trata de información común sobre los usuarios que la mayoría de las aplicaciones consideran útil, como datos demográficos y del dispositivo. Algunos ejemplos son:

- Nombre
- Apellido
- Correo electrónico
- Género
- Fecha de nacimiento
- País
- Localidad
- Última aplicación usada
- Idioma
- Zona horaria

#### Atributos personalizados

[Los atributos personalizados]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/) son atributos que usted define en función de sus necesidades empresariales específicas. Permiten realizar un seguimiento de la información exclusiva de su aplicación o negocio. 

Por ejemplo, una aplicación de streaming de música puede hacer un seguimiento de atributos personalizados como:

- Género favorito
- Número de canciones reproducidas
- Abonado Premium (Sí/No)
- Artista favorito

Por otro lado, una aplicación de comercio minorista podría rastrear atributos personalizados como:

- Talla de ropa preferida
- Marca favorita
- Número de compras
- Miembro del programa de fidelidad (Sí/No)

Los atributos personalizados le ofrecen la flexibilidad necesaria para recopilar y analizar los datos más relevantes para su empresa. Sin embargo, requieren una configuración adicional.

Tanto los atributos estándar como los personalizados pueden utilizarse para segmentar su audiencia y personalizar sus mensajes de marketing. Por ejemplo, podría enviar una oferta especial a los usuarios de una determinada ciudad (atributo estándar) que hayan realizado más de 10 compras (atributo personalizado).

### Eventos

Los eventos representan acciones o comportamientos específicos realizados por los usuarios dentro de su aplicación o sitio web. Ejemplos de eventos pueden ser lanzamientos de aplicaciones, compras, visualizaciones de contenidos o cualquier otra acción. Mediante el seguimiento y el análisis de estos eventos, puede obtener información sobre el comportamiento de los usuarios y los patrones de participación.

#### Eventos estándar

[Los eventos estándar]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/events#standard-events) son eventos predefinidos que Braze rastrea automáticamente después de integrar el SDK en su aplicación o sitio. Algunos ejemplos de actos estándar son:

- **Inicio de la sesión:** Este evento se activa cuando un usuario abre la aplicación.
- **Fin de la sesión:** Este evento se activa cuando un usuario cierra la aplicación.
- **Compra:** Este evento se activa cuando un usuario realiza una compra dentro de la aplicación.
- **Clic en notificación push:** Este evento se activa cuando un usuario hace clic en una notificación push.

#### Eventos personalizados

[Los eventos personalizados]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) son eventos que usted define en función de las acciones específicas que desea rastrear dentro de su aplicación o sitio. Por ejemplo, una aplicación de streaming de música podría rastrear eventos personalizados como:

- Canción reproducida
- Lista de reproducción creada
- Anuncio omitido

Una aplicación de fitness, por otro lado, podría realizar un seguimiento de eventos personalizados como:

- Entrenamiento iniciado
- Entrenamiento completado
- Récord personal establecido

Los eventos personalizados le ofrecen la flexibilidad necesaria para realizar un seguimiento de las acciones más relevantes para su aplicación y su negocio. Sin embargo, al igual que los atributos personalizados, requieren una configuración adicional.

### Puntos de datos

Braze utiliza puntos de datos para ayudarle a definir la información más impactante para su negocio. Los puntos de datos son una parte crucial del funcionamiento de Braze y se utilizan para la facturación, la fijación de precios y, lo que es más importante, la personalización y optimización de sus campañas de marketing.

Los puntos de datos se consumen cuando se actualizan los datos del perfil de un usuario o cuando éste realiza acciones específicas. Estas acciones pueden incluir el inicio de una sesión, la finalización de una sesión, la grabación de un evento personalizado o la realización de una compra. Es importante tener en cuenta que no todos los datos recopilados por Braze cuentan como puntos de datos. Por ejemplo, los datos y eventos recopilados de forma predeterminada por los Servicios Braze, como los tokens push, la información del dispositivo y todos los eventos de seguimiento de participación en campañas, como las aperturas de correos electrónicos y los clics en notificaciones push, no se contabilizan como puntos de datos.

Al considerar cuidadosamente qué información rastrear como puntos de datos, está apuntando a los datos de mayor impacto para la experiencia de sus usuarios. Su gestor de cuenta Braze le ayudará a recomendar las mejores prácticas de datos que se adapten a sus necesidades.

Visita nuestro artículo dedicado para saber más sobre [los puntos de datos]({{site.baseurl}}/user_guide/data/data_points/).

## Segmentos

[La segmentación]({{site.baseurl}}/user_guide/engagement_tools/segments) permite dirigirse a los usuarios en función de sus características y acciones demográficas, de comportamiento, sociales o técnicas (es decir, atributos y eventos). El uso creativo e inteligente de la segmentación y la automatización de la mensajería le permite mover a sus usuarios a través del ciclo de vida del cliente.

Consejos para trabajar con segmentos:

- Los segmentos en Braze son dinámicos: los usuarios siempre entran y salen de los segmentos, ya que no siempre se ajustan a los criterios. Los usuarios que se ajusten a los criterios de un segmento en el momento del envío serán los destinatarios de esa campaña o Canvas.
    - Si desea que su segmento sea estático, puede utilizar Extensiones de segmento. Las extensiones de segmento (con [la regeneración desactivada]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/#extension-regeneration)) representan a su audiencia como una única instantánea en el tiempo.
- No estás limitado a utilizar un filtro cada vez. Cree segmentos granulares finamente ajustados superponiendo varios filtros.
- Puede utilizar las acciones o inacciones de sus usuarios para saber cómo llegar a ellos allí donde quieren relacionarse con usted. Estas acciones pueden ser eventos personalizados, participación en una campaña o lienzo existentes, o incluso un mensaje específico dentro de un lienzo.

### Caso de uso

Supongamos que tiene una tienda de ropa online y ha configurado un flujo de mensajería para enviar una serie de correos electrónicos a los usuarios que han añadido un artículo a su cesta pero no han completado la compra. Este flujo de carritos abandonados podría incluir un correo electrónico de recordatorio inicial, un correo electrónico de seguimiento ofreciendo un descuento y un correo electrónico de recordatorio final.

![]({% image_buster /assets/img/getting_started/segment_example.png %}){: style="max-width:70%" }

Podría crear un segmento de usuarios que han activado el evento personalizado "Artículo añadido al carro" pero no han activado el evento personalizado "Compra completada". A continuación, dentro de este segmento, podría identificar a los usuarios que han abierto el correo electrónico recordatorio inicial (compromiso con un mensaje específico) pero que no han realizado una compra.

![]({% image_buster /assets/img/getting_started/segment_example_breakdown.png %})

Este segmento podría ser objeto de una campaña más agresiva para intentar convertir a estos usuarios en compradores. Por ejemplo, puede enviarles una oferta especial o una recomendación personalizada basada en los artículos de su cesta.

Este es sólo un ejemplo de cómo puede utilizar las acciones e inacciones de los usuarios, los eventos personalizados y los datos de participación para crear segmentos y adaptar sus estrategias de marketing en Braze.

