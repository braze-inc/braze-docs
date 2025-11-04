---
nav_title: Resumen del SDK
article_title: Resumen del SDK 
page_order: 9
page_type: reference
description: "Este artículo de referencia cubre los aspectos básicos del SDK de Braze."
---

# Resumen del SDK 

> El SDK de Braze facilita la recopilación de datos de sesión, la identificación de usuarios y el registro de compras y eventos personalizados a través de tu sitio web o aplicación. También puedes utilizar el SDK para interactuar con tus usuarios enviando mensajes dentro de la aplicación y notificaciones push directamente desde el panel de Braze.

En resumen, el SDK de Braze:
* Recoge y sincroniza los datos de usuario en un perfil de usuario consolidado.
* Captura datos de interacción con los clientes de marketing y datos personalizados específicos de tu empresa.
* Potencia las notificaciones push, los mensajes dentro de la aplicación y los canales de mensajería de la tarjeta de contenido.

## ¿Qué es un SDK?
Un kit de desarrollo de software (SDK) es un conjunto de herramientas prefabricadas -pequeños bloques de código- que pueden añadirse a las aplicaciones digitales para dar soporte a nuevas capacidades. El SDK de Braze se utiliza para enviar y obtener información desde y hacia tu aplicación o sitio web. Está diseñado para proporcionar funciones esenciales desde el principio: crear perfiles de usuario, registrar eventos personalizados, desencadenar notificaciones push, etc. 

Como esta funcionalidad viene predeterminada de Braze, tus desarrolladores quedan libres para centrarse en tu negocio principal. Sin un SDK, cada cliente de Braze tendría que crear toda la infraestructura y las herramientas para el procesamiento de datos, la lógica de segmentación, las opciones de entrega, la gestión de usuarios anónimos, el análisis de campañas y mucho más, completamente desde cero. Eso llevaría mucho más tiempo y sería mucho más molesto que la hora o así que se tarda en incorporar nuestro SDK.

## Aplicación

Para incorporar un SDK a tu aplicación o sitio web, alguien tendrá que añadir el código del SDK a la base de código general de la aplicación. Esto significa que tu equipo de ingeniería estará implicado, básicamente uniendo nuestras aplicaciones para que la información y las acciones fluyan entre ellas. Pero aunque tus desarrolladores estén implicados, el SDK está diseñado para ser ligero y fácil de integrar. 

Para ahorrarte tiempo y garantizar una integración sin problemas, te recomendamos que tú y tu equipo de ingeniería configuréis los eventos personalizados, los atributos personalizados y el SDK al mismo tiempo. Obtén más información sobre los pasos que tus equipos de marketing e ingeniería tendrán que dar juntos leyendo nuestro [artículo sobre implementación]({{site.baseurl}}/user_guide/getting_started/integration/). 

## Agregación de datos

El SDK de Braze captura automáticamente cantidades ingentes de datos a nivel de usuario, facilitando la visualización de métricas clave para tu aplicación y tu base de usuarios. Agruparás aplicaciones similares en un único espacio de trabajo en tu panel. Por ejemplo, agruparás las versiones de iOS y Android de tu aplicación en el mismo espacio de trabajo, lo que te permitirá ver los datos recopilados de los usuarios de ambas plataformas. Esto te da una visión más completa de tus usuarios a través de los canales Web y móvil. Para más información, consulta el artículo de la [página de inicio]({{site.baseurl}}/user_guide/analytics/dashboard/home_dashboard/).

## Mensajería dentro de la aplicación

El SDK facilita la redacción y el envío de mensajes dentro de la aplicación para interactuar directamente con los usuarios. Puedes elegir enviar mensajes con deslizamiento hacia arriba, modal o a pantalla completa en función de tu estrategia de campaña. Para más información sobre cómo redactar un mensaje dentro de la aplicación, consulta nuestra página sobre cómo [crear un mensaje dentro de la aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/create/).

\![Push mostrado en un navegador web]({% image_buster /assets/img_archive/web_push_macbook.png %}){: style="float:right;max-width:45%;margin-left:20px;border:0;"}

## Notificaciones push

Las notificaciones push son otra gran opción para interactuar con tus usuarios y son especialmente útiles para gestionar llamadas a la acción sensibles al tiempo. Las notificaciones push móviles aparecen en los dispositivos de tus usuarios, y las notificaciones push web aparecen incluso cuando tu sitio no está abierto. Para más información sobre el uso de notificaciones push, consulta nuestro [artículo sobre notificaciones push]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/).

Los usuarios de tu sitio web o aplicación deben adherirse voluntariamente para recibir notificaciones push. Consulta la [preparación push]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/) para más detalles. 

## Reglas de segmentación y entrega

Por defecto, se enviará una campaña con mensajes dentro de la aplicación a todas las versiones de la aplicación en ese espacio de trabajo. Por ejemplo, el mensaje se enviará tanto a usuarios de Web como de móvil. Para enviar un mensaje dentro de la aplicación exclusivamente a la Web o al móvil, tendrás que segmentar tu campaña en consecuencia, lo que está predeterminado a través del SDK de Braze. 

Puedes crear un segmento de usuarios de tu Web configurando **Aplicaciones** **y sitios web dirigidos** a **Usuarios de aplicaciones específicas**, y luego seleccionar sólo tu sitio web para las **Aplicaciones específicas**.

\![Página de detalles del segmento con la aplicación Web en primer plano]({% image_buster /assets/img_archive/web-users-segment.png %}){:style="max-width:60%"}

Esto te permitirá dirigirte a los usuarios en función de su comportamiento de forma inteligente. Si quisieras dirigirte a los usuarios de la Web para animarles a descargar tu aplicación móvil, crearías este segmento como audiencia objetivo. Si quisieras enviar una campaña de mensajería que incluyera un mensaje dentro de la aplicación móvil, pero no un mensaje Web, desmarcarías el icono de tu sitio web en tu segmento.

## Plataformas compatibles

Braze proporciona SDKs para múltiples plataformas, como Web, Android y Swift. Para ver la lista completa, consulta la [Guía del desarrollador de Braze]({{site.baseurl}}/developer_guide/home).
