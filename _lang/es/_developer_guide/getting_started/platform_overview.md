---
nav_title: Resumen de la plataforma
article_title: Resumen de la plataforma
page_order: 1
description: "En este artículo se cubren las partes básicas y las capacidades de la plataforma Braze. Los enlaces de este artículo conectan con temas esenciales de Braze."
platform:
  - iOS
  - Android
  - Web
  - React Native
  - Flutter
  - Cordova
  - Roku
  - Swift
  - Unity
---

# Primeros pasos de [![Curso de Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/path/developer){: style="float:right;width:120px;border:0;" class="noimgborder"}: resumen de la plataforma

> En este artículo se cubren las partes básicas y las capacidades de la plataforma Braze. Los enlaces de este artículo conectan con temas esenciales de Braze. 

{% alert tip %}
Echa un vistazo a nuestro [curso de aprendizaje gratuito para desarrolladores](https://learning.braze.com/path/developer) junto con estos artículos.
{% endalert %}

## ¿Qué es Braze?

Braze es una plataforma de interacción con los clientes. Esto significa simplemente que Braze te ayuda a escuchar a tus usuarios, a comprender sus acciones y comportamientos, y a actuar en consecuencia. La plataforma Braze tiene tres componentes principales: el SDK, el panel y la API REST.

Si eres especialista en marketing y buscas un resumen más general de Braze, consulta la [sección Introducción para especialistas en marketing]({{site.baseurl}}/user_guide/getting_started/overview/).

![Braze tiene diferentes capas. En total, consta del SDK, la API, el panel y las integraciones de socios. Cada una de ellas aporta partes de una capa de ingesta de datos, una capa de clasificación, una capa de orquestación, una capa de personalización y una capa de acción. La capa de acción tiene varios canales, como push, mensajes dentro de la aplicación, Catálogo Conectado, webhook, SMS y correo electrónico.]({% image_buster /assets/img/getting-started/getting-started-vertically-integrated-stack.png %}){: style="max-width:55%;float:right;margin-left:15px;"}

### SDK

[Los SDK de Braze](#integrating-braze) pueden integrarse en tus aplicaciones móviles y Web para proporcionar potentes herramientas de marketing, gestión de usuarios y análisis.

En resumen, cuando está totalmente integrado, el SDK:

* Recoge y sincroniza los datos de usuario en un perfil de usuario consolidado.
* Recoge automáticamente datos de sesión, información del dispositivo y tokens de notificaciones push
* Captura datos de interacción con los clientes de marketing y datos personalizados específicos de tu empresa.
* Está diseñado para la seguridad y sometido a pruebas de penetración por terceros
* Está optimizado para dispositivos con poca batería o red lenta
* Admite firmas JWT en el servidor para mayor seguridad
* Tiene acceso de sólo escritura a tus sistemas (no puede recuperar datos de usuario)
* Potencia las notificaciones push, los mensajes dentro de la aplicación y los canales de mensajería de la tarjeta de contenido

### Interfaz de usuario del panel de control

El panel es la interfaz de usuario que controla todos los datos e interacciones en el corazón de la plataforma Braze. Los especialistas en marketing utilizarán el panel para hacer su trabajo y crear contenidos. Los desarrolladores utilizan el panel para administrar configuraciones para integrar aplicaciones, como claves de API y credenciales de notificación push.

Si acabas de empezar, el administrador de tu equipo debería añadirte a ti (y a todos los demás miembros del equipo que necesiten acceso a Braze) como [usuarios en tu panel]({{site.baseurl}}/user_guide/administrative/access_braze).

### API REST

La API de Braze te permite mover datos dentro y fuera de Braze a escala. Utiliza la API para traer actualizaciones de tu backend, almacenes de datos y otras fuentes propias y ajenas. Además, utiliza la API para añadir eventos personalizados con fines de segmentación directamente desde una aplicación basada en Web. Puedes desencadenar y enviar mensajes a través de la API, lo que permite a los recursos técnicos incluir metadatos JSON complejos como parte de tus campañas.

La API también proporciona un servicio Web en el que puedes registrar las acciones realizadas por tus usuarios directamente a través de HTTP, en lugar de a través de los SDK móviles y Web. Combinado con webhooks, esto significa que puedes hacer un seguimiento de las acciones y desencadenar actividades para los usuarios dentro y fuera de la experiencia de la aplicación. La [guía de la API]({{site.baseurl}}/api/home) enumera los puntos finales de la API de Braze disponibles y sus usos.

Para saber más sobre las partes y piezas de Braze, echa un vistazo: [Cómo empezar: Resumen de la arquitectura]({{site.baseurl}}/developer_guide/getting_started/architecture_overview/).

## Análisis de datos y acción

Los datos almacenados en Braze se conservan y pueden utilizarse para segmentación, personalización y orientación mientras seas cliente de Braze. Eso te permite actuar sobre los datos de perfil de usuario (por ejemplo, la actividad de la sesión o las compras) hasta que decidas eliminar esa información. Por ejemplo, un servicio de streaming podría hacer un seguimiento de los contenidos vistos por cada suscriptor desde su primer día en el servicio (aunque fuera hace muchos años) y utilizar esos datos para impulsar la mensajería relevante.

![Un segmento en el panel de Braze llamado "Compradores recientes" yuxtapuesto junto a una pantalla de teléfono que muestra un correo electrónico de "Las mejores recomendaciones para Linda".]({% image_buster /assets/img/getting-started/getting-started-segment.png %}){: style="max-width:80%"}

### Análisis de la aplicación

El panel de Braze muestra gráficos que se actualizan en tiempo real basándose en una serie de métricas de análisis, así como en eventos personalizados que instrumentas en tu aplicación. Medir y optimizar constantemente tus campañas con pruebas A/B, informes y análisis personalizados e inteligencia automatizada te ayuda a mantener la interacción con los clientes y a destacar entre los competidores de tu sector.

### Segmentación de usuarios

La segmentación te permite crear grupos de usuarios basados en potentes filtros de su comportamiento dentro de la aplicación, datos demográficos y similares. Braze también te permite definir cualquier acción del usuario dentro de la aplicación como un "evento personalizado" si la acción deseada no está predeterminada. Lo mismo ocurre con las características del usuario mediante "atributos personalizados". Una vez creado un segmento de usuarios en el panel, tus usuarios entrarán y saldrán del segmento a medida que cumplan (o no) los criterios definidos. Por ejemplo, puedes crear un segmento que incluya a todos los usuarios que han gastado dinero in-app y que utilizaron la aplicación por última vez hace más de dos semanas.

Para saber más sobre nuestros modelos de datos, consulta: [Cómo empezar: Resumen del análisis]({{site.baseurl}}/developer_guide/getting_started/architecture_overview/).

## Mensajería multicanal

Después de definir un segmento, las herramientas de mensajería Braze te permiten interactuar con tus usuarios de forma dinámica y personalizada. Braze se diseñó con un modelo de datos independiente del canal y centrado en el usuario. La mensajería se realiza dentro de tu aplicación o sitio web (como el envío de mensajes dentro de la aplicación o a través de elementos gráficos como carruseles de tarjetas de contenido y pancartas) o fuera de tu experiencia de la aplicación (como el envío de notificaciones push o correos electrónicos). Por ejemplo, tus especialistas en marketing pueden enviar una notificación push y un correo electrónico al segmento de ejemplo definido en la sección anterior.

![Crea y desencadena mensajes personalizados en cualquier canal, ya sea fuera o dentro de tu aplicación o sitio web.]({% image_buster /assets/img/getting-started/messaging-channels.png %}){: style="border:none" }

| Canal                                                                                              | Descripción                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Tarjetas de contenido*]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/) | Envía notificaciones in-app dinámicas y altamente personalizadas sin interrumpir al cliente. |
| [Correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/about/) | Envía mensajes HTML enriquecidos creando tu correo electrónico con el editor de texto enriquecido, nuestro editor de arrastrar y soltar, o cargando una de tus plantillas HTML existentes. |
| [Mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/) | Envía notificaciones discretas dentro de la aplicación utilizando la interfaz de usuario nativa personalizada de Braze. |
| [Push]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/) | Desencadena automáticamente notificaciones push de campañas de mensajería o noticias utilizando el servicio de notificaciones push de Apple (APN) para iOS o Firebase Cloud Messaging (FCM) para Android. |
| [SMS, MMS y RCS*]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs). | Utiliza SMS, MMS o RCS para enviar notificaciones de transacciones, compartir promociones, enviar recordatorios y mucho más. |
| [Web push]({{site.baseurl}}/user_guide/message_building_by_channel/push/web) | Envía notificaciones al navegador web, aunque tus usuarios no estén activos en tu sitio. |
| [Webhooks]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/) | Utiliza webhooks para desencadenar acciones no relacionadas con la aplicación, proporcionando a otros sistemas y aplicaciones datos en tiempo real. |
| [WhatsApp*]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/) | Conecta directamente con tus usuarios y clientes aprovechando la popular plataforma de mensajería entre iguales: WhatsApp. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

<sup>\*\*Disponible como característica adicional\*.</sup>

### Componentes personalizables

{% gallery %}
{{site.baseurl}}/assets/img/getting-started/crawl-example.png <br> Todos los componentes de Braze están diseñados para ser accesibles, adaptables y personalizables. Puedes empezar con Braze utilizando los componentes predeterminados de `BrazeUI` y personalizándolos para adaptarlos a las necesidades de tu marca y a tus casos de uso.
{{site.baseurl}}/assets/img/getting-started/walk-example.png <br> Para ir más allá de las opciones predeterminadas, puedes escribir código personalizado para actualizar el aspecto de un canal de mensajería para que se ajuste más a tu marca. Esto incluye cambiar el tipo de letra, el tamaño de letra y los colores de un componente. Los especialistas en marketing mantienen el control de la audiencia, el contenido, el comportamiento al hacer clic y la caducidad directamente en el panel de Braze.
{{site.baseurl}}/assets/img/getting-started/run-example.png <br> También puedes crear componentes completamente personalizados para controlar el aspecto de tu mensajería, cómo se comporta y cómo interactúan con otros canales de mensajería (por ejemplo, desencadenar una tarjeta de contenido basada en una notificación push). Braze proporciona métodos SDK que te permiten registrar métricas como impresiones, clics y descartes en el panel de Braze. Cada canal de mensajería dispone de un artículo de análisis para facilitar esta tarea.
{% endgallery %}

<br>
<br>

## Integración de Braze

Braze está diseñado para ponerse en marcha rápida y fácilmente. Nuestro tiempo medio de creación de valor es de seis semanas en nuestra base de clientes de cientos de marcas. Para más información sobre el proceso de integración, consulta: [Cómo empezar: Resumen de la integración]({{site.baseurl}}/developer_guide/getting_started/integration_overview/).

## Recursos para marcar

Como recurso técnico, participarás en muchos de los aspectos prácticos de Braze. Aquí tienes buenos recursos para agregar a marcadores fuera de nuestra documentación. A medida que vayas avanzando, ten a mano nuestro glosario de [Términos a Conocer]({{site.baseurl}}/user_guide/getting_started/terms_to_know/) en caso de que tengas preguntas sobre términos de Braze.

| Recursos | Lo que aprenderás|
|---|---|
| [Depurar el SDK]({{site.baseurl}}/developer_guide/sdk_integration/debugging) | Cuando resuelvas los problemas de tu integración, la herramienta de depuración del SDK te será de gran ayuda. ¡Asegúrate de tenerlo a mano! |
| [GitHub público de Braze](https://github.com/braze-inc/) | Encontrarás información detallada sobre la integración y código de muestra en nuestro repositorio de GitHub. |
| [Repositorio GitHub del SDK de Android](https://github.com/braze-inc/braze-android-sdk/) | El repositorio GitHub del SDK de Android. |
| [Referencia del SDK de Android](https://appboy.github.io/appboy-android-sdk/kdoc/index.html) | Documentación de clases para el SDK de Android. |
| [Repositorio de GitHub del SDK para iOS (Swift)](https://github.com/braze-inc/braze-swift-sdk) | El repositorio GitHub del SDK de Swift. |
| [Referencia del SDK de iOS (Swift)](https://braze-inc.github.io/braze-swift-sdk/) | Documentación de clases para el SDK de iOS. |
| [Repositorio de GitHub del SDK Web](https://github.com/braze-inc/braze-web-sdk) | El repositorio GitHub del SDK Web. |
| [Referencia del SDK Web](https://js.appboycdn.com/web-sdk/5.0/doc/modules/braze.html) | Documentación de clases para el SDK de iOS. |
| [Registros de cambios del SDK]({{site.baseurl}}/developer_guide/changelogs) | Braze tiene lanzamientos mensuales predecibles, además de lanzamientos para cualquier problema crítico y actualizaciones importantes del SO. |
| [Colección Postman de la API Braze](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest) | Descarga aquí nuestra colección Cartero.  |
| [Monitor de estado del sistema Braze](https://braze.statuspage.io/) | Nuestra página de estado se actualiza siempre que hay incidentes o cortes. Ve a esta página para suscribirte a las alertas. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

