---
nav_title: Resumen de la integración
article_title: Resumen de la integración
page_order: 2
description: "En este artículo se ofrece un resumen básico del proceso de incorporación."
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

# Primeros pasos de [![Curso de Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/sdk-integration-basics){: style="float:right;width:120px;border:0;" class="noimgborder"}: Resumen de la integración

> En este artículo se ofrece un resumen básico del proceso de incorporación.

![Un diagrama de Venn de cuatro círculos -descubrimiento, integración, garantía de calidad y mantenimiento- centrado en el "tiempo para obtener valor".]({% image_buster /assets/img/getting-started/getting-started-integrate-flower.png %}){: style="max-width:50%;float:right;margin-left:15px;border:none;"} 

Como recurso técnico, potenciarás a tu equipo integrando Braze en tu pila tecnológica. A grandes rasgos, la incorporación se divide en cuatro pasos:
* [Descubrimiento y planificación](#discovery): Trabaja con tu equipo para alinear el alcance, planificar una estructura para los datos y las campañas, y crear una estructura adecuada del espacio de trabajo. 
* [Integración](#integration): Ejecuta tu plan integrando el SDK y la API, habilitando canales de mensajería y configurando la importación y exportación de datos. 
* [Control de calidad](#qa): Confirma que el bucle de datos y mensajería entre la plataforma Braze y tu aplicación o sitio funciona como se espera.
* [Mantenimiento](#maintenance): Una vez que hayas pasado Braze a tu equipo de marketing, seguirás asegurándote de que todo siga funcionando sin problemas.

<br>
{% alert tip %}
Reconocemos que cada organización tiene sus propias necesidades, y Braze está construido para atender a una diversa gama de opciones de personalización que pueden adaptarse a tus requisitos específicos. Los tiempos de integración variarán en función de tu caso de uso. 
{% endalert %}

## Descubrimiento y planificación {#discovery}

Durante esta fase, trabajarás con tu equipo para delimitar las tareas de incorporación y asegurarte de que todas las partes interesadas están alineadas en un objetivo común. 

Tu equipo realizará una planificación de extremo a extremo de tus casos de uso para asegurarse de que todo puede construirse como se espera, con los datos correctos disponibles para ello. Esta fase incluye al jefe de proyecto, al jefe de CRM, a los ingenieros de front-end y back-end, a los propietarios del producto y a los especialistas en marketing. 

La fase de descubrimiento y planificación dura, en promedio, unas seis semanas. Los jefes de ingeniería pueden dedicar de 2 a 4 horas a la semana durante esta fase. Los desarrolladores que trabajen con el producto pueden esperar dedicar entre 10 y 20 horas semanales a Braze durante la fase de descubrimiento y planificación. 

{% alert tip %}
Durante el periodo de incorporación de tu empresa, Braze organizará sesiones de resumen técnico. Recomendamos encarecidamente a los ingenieros que asistan a estas sesiones. Las sesiones de resumen técnico te ofrecen la oportunidad de mantener conversaciones sobre la escalabilidad de la arquitectura de la plataforma y ver ejemplos prácticos de cómo empresas de tu tamaño han tenido éxito anteriormente con casos de uso similares.
{% endalert %}

![Iconos para diferentes canales, como correo electrónico, carrito de la compra, imágenes, geolocalización, etc.]({% image_buster /assets/img/getting-started/data-graphic-2.png %}){: style="max-width:40%;float:right;margin-left:15px;"} 

### Planificación de campañas

Tu equipo de CRM planificará los casos de uso de la mensajería que lanzarás en un futuro próximo. Esto incluye lo siguiente:
* [Canal]({{site.baseurl}}/user_guide/message_building_by_channel) (por ejemplo, notificaciones push o mensajes dentro de la aplicación)
* [Método de entrega]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types) (por ejemplo, entrega programada o entrega basada en acciones)
* [Audiencia objetivo]({{site.baseurl}}/user_guide/engagement_tools/segments)
* [Métricas de éxito]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/)

Por ejemplo, una campaña para nuevos clientes podría ser: un correo electrónico enviado diariamente a las 10 de la mañana a un segmento de clientes que iniciaron ayer su primera sesión. El evento de conversión (la métrica del éxito) está registrando una sesión.

<br>
{% alert important %}
La integración no puede comenzar hasta que se haya completado el paso de planificación de la campaña. Este paso determinará qué partes y piezas de Braze deben configurarse durante la fase de integración.
{% endalert %}

### Crear requisitos de datos

A continuación, tu equipo de CRM debe definir qué datos son necesarios para lanzar las campañas que han planificado, creando requisitos de datos. 

Muchos tipos comunes de atributos de usuario, como nombre, correo electrónico, fecha de nacimiento, país y similares, son objeto de seguimiento automático tras la integración del SDK de Braze. Otros tipos de datos deberán definirse como datos personalizados.

Como desarrollador, trabajarás con tu equipo para definir qué datos adicionales y personalizados tiene sentido seguir. Tus datos personalizados influirán en cómo se clasificará y segmentará tu base de usuarios. Configurarás una taxonomía de eventos en toda tu stack de crecimiento, estructurando tus datos para que sean compatibles con tus sistemas cuando entren y salgan de Braze.

{% alert tip %}
Mantén la nomenclatura de los datos coherente en todas las herramientas. Por ejemplo, tu almacén de datos puede registrar la "oferta de compra por tiempo limitado" de una forma determinada. Tendrás que decidir si es necesario un evento personalizado en Braze para que coincida con este formato.
{% endalert %}

Más información sobre [datos recopilados automáticamente y datos personalizados]({{site.baseurl}}/developer_guide/analytics/).

### Planificación de personalizaciones

Habla con tus especialistas en marketing sobre las personalizaciones que desean. Por ejemplo, ¿quieres implementar las tarjetas de contenido Braze predeterminadas? ¿Quieres modificar ligeramente su aspecto para que se ajuste a las directrices de tu marca? ¿Quieres desarrollar una interfaz de usuario completamente nueva para un componente y que Braze haga un seguimiento de sus análisis? Diferentes niveles de personalización requieren diferentes niveles de alcance.

### Acceder al panel de control

El panel de Braze es nuestra interfaz de usuario Web. Los especialistas en marketing utilizarán el panel para hacer su trabajo y crear contenidos. Los desarrolladores utilizan el panel para administrar configuraciones para integrar aplicaciones, como claves de API y credenciales de notificación push.

El administrador de tu equipo debe añadirte a ti (y a todos los demás miembros del equipo que necesiten acceso a Braze) como usuarios en tu panel.

### Espacios de trabajo y claves de API

El administrador de tu equipo también creará diferentes [espacios de trabajo]({{site.baseurl}}/user_guide/administrative/app_settings/workspaces/). Los espacios de trabajo agrupan tus datos -usuarios, segmentos, claves de API- en una sola ubicación. Como práctica recomendada, te sugerimos que sólo agrupes diferentes versiones de la misma aplicación o de aplicaciones muy similares en un mismo espacio de trabajo. 

Es importante destacar que los espacios de trabajo proporcionan claves de API para múltiples plataformas (como iOS y Android). Utilizarás las claves de API correlacionadas para asociar los datos del SDK a un espacio de trabajo concreto. Navega hasta tus espacios de trabajo para acceder a la clave de API de cada una de tus aplicaciones. Asegúrate de que cada clave de API tiene los permisos correctos para realizar el trabajo que le has asignado. Para más detalles, consulta [el artículo sobre el aprovisionamiento de la API]({{site.baseurl}}/api/basics/#rest-api-key).

{% alert important %}
Es importante que configures entornos diferentes para desarrollo y producción. Configurar un entorno de pruebas evitará que gastes dinero real durante la incorporación y el control de calidad. Para crear un entorno de pruebas, configura un espacio de trabajo de pruebas y asegúrate de utilizar su clave de API para no llenar tu espacio de trabajo de producción con datos de prueba.
{% endalert %}  

## Integración {#integration}

![Gráfico piramidal abstracto que representa el flujo de información desde un origen de datos hasta un dispositivo de usuario.]({% image_buster /assets/img/getting-started/data-graphic.png %}){: style="max-width:45%;float:right;margin-left:15px;"} 

Braze es compatible con aplicaciones iOS, aplicaciones Android, aplicaciones web y mucho más. También puedes optar por utilizar un SDK envolvente multiplataforma, como React Native o Unity. Normalmente, los clientes realizan la integración en un plazo de 1 a 6 semanas. Muchos clientes han integrado Braze con un solo ingeniero, en función de su amplitud de conocimientos técnicos y ancho de banda. Depende totalmente del alcance específico de tu integración y del tiempo que tu equipo dedique al proyecto Braze. 

Necesitarás desarrolladores que estén familiarizados con:
* Trabajar en la capa nativa de tu aplicación o sitio web
* Crear procesos para golpear nuestra API REST
* Pruebas de integración 
* Autenticación con token web JSON
* Conocimientos generales de gestión de datos
* Configuración de registros de DNS

### Socios de integración de CDP

Muchos clientes utilizan la incorporación a Braze como una oportunidad para integrarse también con una plataforma de datos de los clientes (CDP) como socio de integración. Braze proporciona seguimiento y análisis de datos, mientras que un CDP puede proporcionar enrutamiento y orquestación de datos adicionales. Braze ofrece una integración sin problemas con muchos CDP, como [mParticle]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/mparticle/mparticle/) y [Segment]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/segment/segment/). 

Si realizas una integración en paralelo con un CDP, mapearás las llamadas del SDK de tu CDP al SDK de Braze. Esencialmente, harás lo siguiente:
* Mapea las llamadas identificadoras a `changeUser` [(Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/change-user.html), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/changeuser(userid:sdkauthsignature:fileid:line:)/), [Web](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser)) y establece atributos.
* Llamadas de datos mapeados a `requestImmediateDataFlush` [(Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/request-immediate-data-flush.html?query=abstract%20fun%20requestImmediateDataFlush()), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/requestimmediatedataflush()), [web](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestimmediatedataflush)).
* Registra eventos personalizados o compras.

Puede haber ejemplos de integración entre el SDK de Braze y el CDP que elijas, dependiendo de la plataforma que hayas elegido. Consulta nuestra [lista de socios tecnológicos de CDP]({{site.baseurl}}/partners/data_and_analytics/) para obtener más información. 

### Integración de SDK Braze

El SDK de Braze proporciona dos funciones fundamentales: recopila y sincroniza los datos de usuario en un perfil de usuario consolidado, y potencia canales de mensajería como las notificaciones push, los mensajes dentro de la aplicación y las tarjetas de contenido. 

{% alert tip %}
Cuando se integra completamente con tu aplicación o sitio web, el SDK de Braze ofrece un nivel integral de sofisticación de marketing. Si pospones la integración del SDK de Braze, algunas de las funciones descritas en la documentación no estarán disponibles.
{% endalert %}

Durante la implementación del SDK, harás lo siguiente:

* Escribe el código de integración de SDK para cada plataforma que quieras admitir.
* Activa los canales de mensajería de cada plataforma, asegurándote de que el SDK de Braze hace un seguimiento de los datos de las interacciones con tus clientes a través de correo electrónico, SMS, notificaciones push y otros canales.
* Crea cualquier personalización prevista de los componentes de la interfaz de usuario (por ejemplo, tarjetas de contenido personalizadas). Para un contenido completamente personalizado, tendrás que registrar los análisis, ya que la recopilación de datos automática del SDK no tendrá en cuenta tus nuevos componentes. Puedes seguir el patrón de esta implementación en nuestros componentes predeterminados.

### Uso de la API Braze

Utilizarás nuestra API REST para diferentes tareas en distintos momentos a lo largo del tiempo que utilices Braze. La API Braze es útil para:

1. Importar datos históricos; y
2. Actualizaciones continuas que no se desencadenan en Braze. Por ejemplo, un perfil de usuario se actualiza a VIP sin que inicie sesión en una aplicación, por lo que la API debe comunicar esta información a Braze.

Empieza a utilizar [la API Braze]({{site.baseurl}}/api/basics).

{% alert important %}
Cuando utilices la API, asegúrate de que realizas las solicitudes por lotes y de que sólo envías valores delta. Braze reescribe todos los atributos que se envían. No actualices ningún atributo personalizado si su valor no ha cambiado.
{% endalert %}

### Configuración de los análisis de productos

Braze se centra en los datos. Los datos en Braze se almacenan en el perfil de usuario. 

Los puntos de datos son una estructura mediante la cual te aseguras de que estás captando los datos adecuados para tus especialistas en marketing, y no "cualquier" dato que puedas conseguir. Familiarízate con los [puntos de datos]({{site.baseurl}}/user_guide/data/data_points/).

### Migración de datos de usuario heredados

Puedes utilizar el programa Braze [`/users/track endpoint`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) para migrar datos históricos registrados fuera de Braze. Algunos ejemplos de datos importados habitualmente son los tokens de notificaciones push y las compras anteriores. Este punto final puede utilizarse para importaciones puntuales o actualizaciones periódicas por lotes. 

También puedes importar usuarios y actualizar los valores de los atributos de los clientes mediante una única [carga de CSV]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import#importing-a-csv) al panel. Cargar CSV puede ser útil para los especialistas en marketing, mientras que nuestra API REST permite una mayor flexibilidad.

### Configuración del seguimiento de la sesión

El SDK de Braze genera puntos de datos de "sesión abierta" y "sesión cerrada". El SDK de Braze también descarga los datos a intervalos regulares. Consulta estos enlaces para conocer los valores predeterminados de seguimiento de sesión, todos ellos personalizables[(Android]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=android), [iOS]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=swift), [Web]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=web)).

### Seguimiento de eventos personalizados, atributos y eventos de compra

Coordínate con tu equipo para configurar el esquema de datos previsto, incluidos los eventos personalizados, los atributos de usuario y los eventos de compra. Tu [esquema de datos personalizado]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) se introducirá utilizando el panel y debe coincidir exactamente con lo que implementes durante la integración de SDK.

{% alert tip %}
Los ID de usuario, llamados `external_id`s en Braze, deben establecerse para todos los usuarios conocidos. Deben ser inmutables y accesibles cuando un usuario abra la aplicación, permitiéndote hacer un seguimiento de tus usuarios en todos los dispositivos y plataformas. Consulta el artículo [Ciclo de vida del usuario]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/) para conocer las mejores prácticas.
{% endalert %}

### Otras herramientas

Según tu caso de uso, puede haber otras herramientas que necesites configurar. Por ejemplo, puede que necesites configurar una herramienta como [las geovallas]({{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences#about-locations-and-geofences/) para realizar tus historias de usuario. Hemos comprobado que los clientes que tienen la posibilidad de configurar estas herramientas adicionales después de completar los pasos esenciales de la integración son los que tienen más éxito.

## Garantía de calidad {#qa}
A medida que ejecutes tu integración, proporcionarás una garantía de calidad para asegurarte de que todo lo que estás configurando funciona según lo esperado. Esta GC se divide en dos categorías generales: la ingesta de datos y los canales de mensajes.

{% alert important %}
Asegúrate de que tus entornos de producción y pruebas están configurados antes de empezar el control de calidad.
{% endalert %}

| **Ingesta de datos de control de calidad**  | **Mensajería de control de calidad**                                              |
|---------------------------|---------------------------------------------------------------|
| Realizarás el control de calidad de la forma en que se ingieren, almacenan y exportan los datos. | Te asegurarás de que tus mensajes se envían correctamente a tus usuarios y de que todo tiene un aspecto excelente. |
| Realiza pruebas para confirmar que los datos se almacenan correctamente. | Crea segmentos de usuarios. |
| Confirma que los datos de la sesión se atribuyen correctamente al espacio de trabajo previsto dentro de Braze. | Lanza campañas y lonas con éxito. |
| Confirma que se están grabando los inicios y los finales de sesión. | Confirma que se están mostrando las campañas correctas a los segmentos de usuarios correctos. |
| Confirma que la información sobre los atributos del usuario se registra correctamente en los perfiles de usuario. | Confirma que los tokens de notificaciones push se están registrando correctamente. |
| Comprueba que los datos de clientes se registran correctamente en los perfiles de usuario. | Confirma que los tokens de notificaciones push se han eliminado correctamente. |
| Crea perfiles de usuario anónimos. | Comprueba que las campañas push se envían correctamente a los dispositivos y que se registra la interacción. |
| Confirma que los perfiles de usuario anónimos se convierten en perfiles de usuario conocidos cuando se llama al método `changeUser()`. | Comprueba que se entregan los mensajes dentro de la aplicación y que se registran las métricas. |
|                           | Comprueba que se entregan las tarjetas de contenido y se registran las métricas. |
|                           | Facilita contenidos conectados (por ejemplo, AccuWeather). |
|                           | Confirma que todas las integraciones del canal de mensajería funcionan correctamente. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert note %}
Mientras realizas el control de calidad de tu integración de SDK, utiliza [el depurador de SDK]({{site.baseurl}}/developer_guide/sdk_integration/debugging) para solucionar problemas sin activar el registro detallado de tu aplicación.
{% endalert %}

### Pasar Braze a los especialistas en marketing

Una vez que hayas integrado tu plataforma o sitio web, querrás implicar a tu equipo de marketing para pasarles la propiedad de la plataforma. Este proceso es diferente en cada empresa, pero puede incluir lo siguiente:

* Componer la compleja [lógica Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid#about-liquid)
* Ayudar a facilitar el [calentamiento de IP del correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ip_warming/)
* Asegurarse de que otras partes interesadas comprenden el tipo de datos que se están siguiendo

### Desarrollar para el futuro

¿Alguna vez has heredado una base de código y no tenías ni idea de lo que estaba pensando el desarrollador inicial? Peor aún, ¿alguna vez has escrito código, lo has entendido completamente y luego te has sentido totalmente desconcertado cuando has vuelto a él un año después? 

Cuando incorpores Braze, las decisiones colectivas que tomes en relación con los datos, los perfiles de usuario, qué integraciones estaban y no estaban dentro de su alcance, cómo se supone que deben funcionar las personalizaciones, y mucho más, te parecerán recientes y, por tanto, obvias. Cuando tu equipo quiera ampliar Braze o cuando se asignen otros recursos técnicos a tu proyecto Braze, esta información será oscura.

Crea un recurso para consolidar la información que aprendiste durante tus sesiones de resumen técnico. Este recurso te ayudará a reducir el tiempo de incorporación de los nuevos desarrolladores que se incorporen a tu equipo (o te servirá de recordatorio cuando necesites ampliar tu actual implementación de Braze). 

## Mantenimiento {#maintenance}

Tras el traspaso a tus especialistas en marketing, seguirás siendo un recurso para el mantenimiento. Prestarás atención a las actualizaciones de iOS y Android que puedan afectar al SDK de Braze y te asegurarás de que tus proveedores externos estén al día. 

Realizarás un seguimiento de las actualizaciones de la plataforma Braze a través de Braze [GitHub](https://github.com/braze-inc/). Ocasionalmente, tu administrador también recibirá correos electrónicos sobre actualizaciones urgentes y correcciones de errores directamente de Braze. 

## Límites de velocidad SDK 

### Usuarios activos al mes CY 24-25 

Para los clientes que han comprado Usuarios activos al mes - CY 24-25, Braze aplica límites de tasa en el servidor a las solicitudes de API utilizadas por nuestros SDK para actualizar sesiones, atributos de usuario, eventos y otros datos de perfil del usuario. Esto se hace para garantizar la estabilidad de la plataforma y mantener un servicio rápido y fiable. 

* Los límites de velocidad por hora se establecen en función del tráfico de SDK previsto en tu cuenta, que puede corresponder al número de usuarios activos al mes (MAU) que hayas adquirido, al sector, a la estacionalidad o a otros factores. Cuando se alcance el límite de velocidad por hora, Braze ralentizará las peticiones hasta la hora siguiente.
* El SDK reintenta automáticamente todas las solicitudes con límite de tasa.
* Las solicitudes del SDK se correlacionan con la cantidad de datos personalizados recopilados en tu implementación. Si estás constantemente cerca o en tu límite de velocidad por hora, considera:
    * Revisa tu integración de SDK para reducir la recopilación excesiva de datos.
    * Bloquea los datos personalizados que no sean esenciales para tus casos de uso de marketing.
* Los límites de velocidad de ráfaga son límites de velocidad de corta duración que se aplican cuando llega un gran volumen de solicitudes en un periodo muy corto (es decir, en cuestión de segundos). No es necesario que actúes cuando se produzcan límites de ráfagas, y el SDK volverá a intentarlo poco después.

### Encontrar tus límites de velocidad

Para encontrar los límites actuales basados en el rendimiento esperado del SDK, ve a **Configuración** > **API e identificadores** > **Límites de API y SDK**.

Para el uso histórico, ve a **Configuración** > **API e identificadores** > **Panel de API y SDK**.

### Cambios y apoyo

Braze puede modificar los límites de velocidad para proteger la estabilidad del sistema o permitir un mayor caudal de datos en tu cuenta. Ponte en contacto con el soporte de Braze o con tu administrador del éxito del cliente si tienes preguntas o dudas sobre los límites de velocidad y cómo afectan a tu negocio.
