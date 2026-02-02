---
nav_title: Visión general del SDK
article_title: Resumen del SDK 
page_order: 9
page_type: reference
description: "Este artículo de referencia cubre los aspectos básicos del SDK de Braze."
---

# Visión general del SDK 

> El SDK de Braze recopila datos de sesión, identifica usuarios y registra compras y eventos personalizados a través de tu sitio web o aplicación. También puedes utilizar el SDK para interactuar con los usuarios enviando mensajes dentro de la aplicación y notificaciones push directamente desde el panel de Braze.

En resumen, el SDK de Braze:
* Recoge y sincroniza los datos de los usuarios en un perfil de usuario consolidado.
* Captura datos de compromiso de marketing y datos personalizados específicos de su empresa.
* Potencia las notificaciones push, los mensajes dentro de la aplicación y los canales de mensajería de la tarjeta de contenido

## ¿Qué es un SDK?
Un kit de desarrollo de software (SDK) es un conjunto de herramientas prefabricadas (pequeños bloques de código) que pueden añadirse a las aplicaciones digitales para dar soporte a nuevas capacidades. El SDK de Braze se utiliza para enviar y obtener información desde y hacia tu aplicación o sitio web. Está diseñado para ofrecer funciones esenciales desde el principio: creación de perfiles de usuario, registro de eventos personalizados, activación de notificaciones push, etc. 

Como esta funcionalidad viene por defecto de Braze, sus desarrolladores quedan libres para centrarse en su negocio principal. Sin un SDK, cada cliente de Braze tendría que crear toda la infraestructura y herramientas para el procesamiento de datos, lógica de segmentación, opciones de entrega, gestión de usuarios anónimos, análisis de campañas y mucho más completamente desde cero. Eso llevaría mucho más tiempo y sería mucho más molesto que la hora o así que se tarda en incorporar nuestro SDK.

## Aplicación

Para incorporar un SDK a tu aplicación o sitio web, alguien tendrá que añadir el código del SDK a la base de código general de la aplicación. Esto significa que tu equipo de ingeniería estará implicado, básicamente uniendo nuestras aplicaciones para que la información y las acciones fluyan entre ellas. Pero aunque tus desarrolladores estén implicados, el SDK está diseñado para ser ligero y fácil de integrar. 

Para ahorrarle tiempo y garantizar una integración sin problemas, le recomendamos que usted y su equipo de ingeniería configuren los eventos personalizados, los atributos personalizados y el SDK al mismo tiempo. Obtenga más información sobre los pasos que sus equipos de marketing e ingeniería tendrán que pensar juntos leyendo nuestro [artículo sobre implementación]({{site.baseurl}}/user_guide/getting_started/integration/). 

## Agregación de datos

El SDK de Braze captura automáticamente datos a nivel de usuario, proporcionándote métricas clave para tu aplicación y tu base de usuarios. Agrupa aplicaciones similares en un único espacio de trabajo (por ejemplo, las versiones de iOS y Android juntas) para ver los datos recopilados en todas las plataformas y construir una imagen completa de la actividad del usuario. Para más información, consulte el artículo de la [página de inicio]({{site.baseurl}}/user_guide/analytics/dashboard/home_dashboard/).

## Mensajería en la aplicación

Utiliza el SDK para redactar y enviar mensajes dentro de la aplicación directamente. Puedes elegir mensajes deslizables, modales o a pantalla completa en función de tu estrategia de campaña. Para más detalles sobre la composición, consulta [Crear un mensaje dentro de la aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/create/).

![Push visualizado en un navegador web]({% image_buster /assets/img_archive/web_push_macbook.png %}){: style="float:right;max-width:45%;margin-left:20px;border:0;"}

## Notificaciones push

Las notificaciones push son otra gran opción para interactuar con sus usuarios y son especialmente útiles para gestionar llamadas a la acción sensibles al tiempo. Las notificaciones push móviles aparecen en los dispositivos de sus usuarios, y las notificaciones push web aparecen incluso cuando su sitio no está abierto. Para más información sobre el uso de las notificaciones push, consulta nuestro [artículo sobre notificaciones push]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/).

Los usuarios de su sitio web o aplicación deben registrarse para recibir notificaciones push. Consulta la [preparación push]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/) para más detalles. 

## Reglas de segmentación y entrega

Por defecto, una campaña que contenga mensajes in-app se enviará a todas las versiones de la aplicación en ese espacio de trabajo. Por ejemplo, el mensaje se enviará tanto a usuarios de web como de móvil. Para enviar un mensaje in-app exclusivamente a web o móvil, tendrás que segmentar tu campaña en consecuencia, lo que se admite por defecto a través del SDK de Braze. 

Puedes crear un segmento de usuarios de tu Web configurando **Aplicaciones** **y sitios web dirigidos** a **Usuarios de aplicaciones específicas**, y luego seleccionar sólo tu sitio web para las **Aplicaciones específicas**.

![Página de detalles del segmento con la aplicación Web en primer plano]({% image_buster /assets/img_archive/web-users-segment.png %}){:style="max-width:60%"}

Esto le permitirá dirigirse a los usuarios en función de su comportamiento de forma inteligente. Si quisiera dirigirse a usuarios de Internet para animarles a descargar su aplicación móvil, crearía este segmento como público objetivo. Si desea enviar una campaña de mensajería que incluya un mensaje móvil dentro de la aplicación, pero no un mensaje web, deberá desmarcar el icono de su sitio web en su segmento.

## Plataformas compatibles

Braze proporciona SDKs para múltiples plataformas, como Web, Android y Swift. Para ver la lista completa, consulta la [Guía del desarrollador de Braze]({{site.baseurl}}/developer_guide/home).
