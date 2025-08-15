---
nav_title: Descripción general del SDK 
article_title: Descripción general del SDK 
page_order: 9
page_type: reference
description: "Este artículo de referencia cubre los aspectos básicos del SDK de Braze."
---

# Visión general del SDK 

> El SDK de Braze facilita la recopilación de datos de sesión, la identificación de usuarios y el registro de compras y eventos personalizados a través de su sitio web o aplicación. También puede utilizar el SDK para interactuar con sus usuarios enviando mensajes dentro de la aplicación y notificaciones push directamente desde el panel de control de Braze.

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

El SDK de Braze captura automáticamente cantidades ingentes de datos a nivel de usuario, lo que facilita la visualización de las métricas clave de su aplicación y su base de usuarios. Agrupará aplicaciones similares en un único espacio de trabajo en su panel de control. Por ejemplo, agrupará las versiones de iOS y Android de su aplicación en el mismo espacio de trabajo, lo que le permitirá ver los datos recopilados de los usuarios de ambas plataformas. Esto le proporciona una visión más completa de sus usuarios en todos los canales web y móviles. Para más información, consulte el artículo de la [página de inicio]({{site.baseurl}}/user_guide/analytics/dashboard/home_dashboard/).

## Mensajería en la aplicación

El SDK facilita la redacción y el envío de mensajes dentro de la aplicación para interactuar directamente con los usuarios. Puede elegir entre enviar mensajes deslizantes, modales o a pantalla completa en función de la estrategia de su campaña. Para más información sobre cómo redactar un mensaje dentro de la aplicación, consulta nuestra página sobre cómo [crear un mensaje dentro de la aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/create/).

![Push mostrado en un navegador web]({% image_buster /assets/img_archive/web_push_macbook.png %}){: style="float:right;max-width:45%;margin-left:20px;border:0;"}

## Notificaciones push

Las notificaciones push son otra gran opción para interactuar con sus usuarios y son especialmente útiles para gestionar llamadas a la acción sensibles al tiempo. Las notificaciones push móviles aparecen en los dispositivos de sus usuarios, y las notificaciones push web aparecen incluso cuando su sitio no está abierto. Para más información sobre el uso de las notificaciones push, consulta nuestro [artículo sobre notificaciones push]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/).

Los usuarios de su sitio web o aplicación deben registrarse para recibir notificaciones push. Consulta la [preparación push]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/) para más detalles. 

## Reglas de segmentación y entrega

Por defecto, una campaña que contenga mensajes in-app se enviará a todas las versiones de la aplicación en ese espacio de trabajo. Por ejemplo, el mensaje se enviará tanto a usuarios de web como de móvil. Para enviar un mensaje in-app exclusivamente a web o móvil, tendrás que segmentar tu campaña en consecuencia, lo que se admite por defecto a través del SDK de Braze. 

Puedes crear un segmento de usuarios de tu Web configurando **Aplicaciones** **y sitios web dirigidos** a **Usuarios de aplicaciones específicas**, y luego seleccionar sólo tu sitio web para las **Aplicaciones específicas**.

![Página de detalles del segmento con la aplicación Web en primer plano]({% image_buster /assets/img_archive/web-users-segment.png %}){:style="max-width:60%"}

Esto le permitirá dirigirse a los usuarios en función de su comportamiento de forma inteligente. Si quisiera dirigirse a usuarios de Internet para animarles a descargar su aplicación móvil, crearía este segmento como público objetivo. Si desea enviar una campaña de mensajería que incluya un mensaje móvil dentro de la aplicación, pero no un mensaje web, deberá desmarcar el icono de su sitio web en su segmento.

## ¿Qué integraciones tiene Braze?
Braze ofrece una versión de nuestro SDK para muchas plataformas (Web, Android, iOS, Flutter, React Native, etc.), pero todas funcionan esencialmente de la misma manera. Por tanto, si ves una referencia a, por ejemplo, el "SDK Web", se trata de la versión del SDK de Braze destinada a tu sitio web.

<style>
table th:nth-child(1) {
width: 33%;
}
table th:nth-child(2) {
width: 33%;
}
table th:nth-child(3) {
width: 33%;
}
table td {
word-break: break-word;
text-align: center;
}
</style>
Integraciones destacadas   |    |   
----------- |---------------- | --------------------
[![Android]({% image_buster /assets/img/braze_icons/android.svg %})]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=android){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [Android]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android) |[![iOS]({% image_buster /assets/img/braze_icons/apple.svg %})]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift){: style="max-width:20%;margin-right:15px;border:0" class="noimgborder"} [iOS]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift) |[![Web]({% image_buster /assets/img/braze_icons/globe-02.png %})]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web){: style="max-width:25%;margin-right:15px;border:0" class="noimgborder"} [Web]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web)  

Todas las integraciones   |    |   
----------- |---------------- | --------------------
[![Cordova Android]({% image_buster /assets/img/cordova.png %})]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=cordova&tab=android){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [Cordova Android]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=cordova&tab=android) | [![Cordova iOS]({% image_buster /assets/img/cordova.png %})]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=cordova&tab=ios){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [Cordova iOS]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=cordova&tab=ios) | [![Flutter Android y iOS]({% image_buster /assets/img/flutter_icon.png %})]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=flutter){: style="max-width:20%;margin-top:5%;border:0" class="noimgborder"}  [Flutter Android e iOS]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=flutter)
[![React Native]({% image_buster /assets/img/reactnative_icon.png %})]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=react%20native){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [React Native]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=react%20native) | [![tvOS]({% image_buster /assets/img/tvos_icon.png %})]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/tvos/initial_sdk_setup/){: style="max-width:40%;margin-top:5%;border:0" class="noimgborder"}  [tvOS]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/tvos/initial_sdk_setup/) | [![MacOS]({% image_buster /assets/img/macOS_icon.png %})]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/macOS/initial_sdk_setup/){: style="max-width:40%;margin-top:15%;border:0" class="noimgborder"}  [MacOS]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/macOS/initial_sdk_setup/)
[![Unity Android]({% image_buster /assets/img/unity.png %})]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=unity){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [Unity Android]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=unity) | [![Unity iOS]({% image_buster /assets/img/unity.png %})]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=unity){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [Unity iOS]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=unity) | [![Xamarin]({% image_buster /assets/img/xamarin.png %})]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=xamarin){: style="max-width:35%;margin-top:5%;border:0" class="noimgborder"}  [Xamarin]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=xamarin) 
[![Roku]({% image_buster /assets/img/roku.png %})]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=roku){: style="max-width:40%;margin-top:5%;border:0" class="noimgborder"}  [Roku]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=roku) | [![Unreal Engine]({% image_buster /assets/img/unreal.png %})]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=unreal%20engine){: style="max-width:30%;margin-right:15px;border:0" class="noimgborder"}  [Motor Unreal Engine]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=unreal%20engine)

