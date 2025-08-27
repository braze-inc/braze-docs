---
nav_title: Recopilación de datos del SDK
article_title: Recopilación de datos del SDK
page_order: 1
page_type: reference
description: "Este artículo de referencia aborda los datos que recopila el SDK a través de una integración personalizada, una integración recopilada automáticamente y una integración mínima."

---

# Recopilación de datos del SDK

> Cuando integras el SDK de Braze con tu aplicación o sitio, Braze recopila automáticamente determinados tipos de datos. Algunos de estos datos son esenciales para nuestros procesos y otros pueden activarse o desactivarse en función de tus necesidades. También puedes configurar Braze para que recopile tipos de datos adicionales para potenciar aún más tu segmentación y mensajería.

Braze está diseñado para permitir una recopilación de datos flexible, por lo que puedes integrar el SDK de Braze de las siguientes formas:

- **[Integración mínima](#minimum-integration):** Braze recopila automáticamente los datos necesarios para comunicarse con los servicios de Braze.
- **[Datos opcionales recopilados por defecto](#optional-data-collected-by-default):** Braze captura automáticamente algunos datos que son ampliamente útiles para la mayoría de tus casos de uso. Puedes optar por desactivar la recopilación automática de estos datos si no es esencial para la comunicación con los servicios de Braze.
- **[Datos opcionales no recogidos por defecto](#data-not-collected-by-default):** Braze capta algunos datos que son útiles para determinados casos de uso y no habilita automáticamente la recopilación por motivos de cumplimiento general. Puedes optar por recoger estos datos cuando se adapten a tus casos de uso.
- **[Integración personalizada](#personalized-integration):** Braze te da flexibilidad para recopilar datos además de los datos opcionales predeterminados.

## Integración mínima

A continuación se enumeran los datos estrictamente necesarios que genera y recibe Braze cuando inicializas el SDK. Estos datos no son configurables y son esenciales en las funciones básicas de la plataforma. Excepto el inicio y el final de la sesión, el resto de los datos de seguimiento automático no cuentan para tu asignación de puntos de datos.

| Atributo | Descripción | Por qué se recoge |
| --------- | ----------- | ------------------ |
| App-Version-Name /<br> App-Version-Code | La versión más reciente de la aplicación | Este atributo se utiliza para enviar mensajes relacionados con la compatibilidad de la versión de la aplicación a los dispositivos correctos. Puede utilizarse para notificar a los usuarios interrupciones del servicio o fallos. |
| País | País identificado por la geolocalización de la dirección IP. Si la geolocalización de la dirección IP no está disponible, se identifica por la [localización del dispositivo](#optional-data-collected-by-default). Alternativamente, el valor podría ser el que establezcan directamente los SDK con `setCountry`, pero ten en cuenta que pasar un valor de atributo por SDK o API consumirá datapoints.| Este atributo se utiliza para dirigir mensajes en función de la ubicación. |
| ID del dispositivo | Identificador del dispositivo, una cadena generada aleatoriamente | Este atributo se utiliza para diferenciar los dispositivos de los usuarios y enviar mensajes al dispositivo correcto. |
| Sistema operativo y versión del sistema operativo | Dispositivo o navegador del que se informa actualmente y versión del dispositivo o navegador | Este atributo se utiliza para enviar mensajes sólo a dispositivos compatibles. También puede utilizarse dentro de la segmentación para dirigirse a los usuarios con el fin de actualizar las versiones de las aplicaciones. |
| Inicio y fin de la sesión | Cuando el usuario comienza a utilizar su aplicación o sitio integrado | El SDK de Braze informa de los datos de sesión utilizados por el panel de control de Braze para calcular la participación de los usuarios y otros análisis esenciales para comprender a sus usuarios. El desarrollador[(Android]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=android), [iOS]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=swift), [Web]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=web)) puede configurar el momento exacto en que su aplicación o sitio web llama al inicio y al final de la sesión. |
| Datos de interacción del mensaje SDK | Aperturas directas push, interacciones con mensajes in-app, interacciones con tarjetas de contenido | Este atributo se utiliza con fines de control de calidad, como comprobar que se ha recibido un mensaje y que el envío no está duplicado. |
| Versión del SDK | Versión actual del SDK | Este atributo se utiliza para enviar mensajes sólo a dispositivos compatibles y evitar interrupciones del servicio. |
| ID y fecha de la sesión | Identificador de sesión, una cadena generada aleatoriamente y una marca de tiempo de sesión | Se utiliza para determinar si el usuario está iniciando una sesión nueva o ya existente y para determinar la reelegibilidad de los mensajes destinados a este usuario.<br><br>Algunos canales de mensajería, como los mensajes dentro de la aplicación y las tarjetas de contenido, se sincronizan con el dispositivo al iniciar la sesión. Nuestro backend utilizará entonces los datos relacionados con la última vez que contactó con los servidores Braze (que el dispositivo almacena y devuelve) para saber si el usuario puede recibir nuevos mensajes.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### Métricas calculadas

Braze genera métricas calculadas sobre datos SDK, datos de interacción de mensajes relacionados con mensajes no SDK e información derivada. Para mayor claridad, estos datos calculados no son rastreados por el SDK sino generados por los servicios Braze, y un perfil de usuario mostrará tanto los datos rastreados como los generados. 

Las métricas calculadas incluyen los siguientes atributos.

| Atributo                                      | Descripción                                                          |
|-----------------------------------------------|----------------------------------------------------------------------|
| Primera aplicación usada                                 | Tiempo                                                                 |
| Última aplicación utilizada                                  | Tiempo                                                                 |
| Recuento total de sesiones                            | Número                                                               |
| Tarjeta clicada                                   | Número                                                               |
| Último mensaje recibido                     | Tiempo                                                                 |
| Última campaña de correo electrónico recibida                   | Tiempo                                                                 |
| Última campaña de empuje recibida                    | Tiempo                                                                 |
| Número de comentarios                       | Número                                                               |
| Número de sesiones en los últimos Y días          | Número y hora                                                      |
| Mensaje recibido de la campaña                  | Booleano. Este filtro se dirige a los usuarios en función de si han recibido una campaña anterior.                               |
| Mensaje recibido de la campaña con la etiqueta        | Booleano. Este filtro se dirige a los usuarios en función de si han recibido una campaña que actualmente tiene una etiqueta.                  |
| Campaña de reorientación                              | Booleano. Este filtro se dirige a los usuarios en función de si han abierto o han hecho clic en un correo electrónico específico, push o mensaje dentro de la aplicación en el pasado. |
| Desinstalada                                    | Booleano y hora |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert important %}
Si sólo te interesa la integración mínima, y te integras con mParticle, Segment, Tealium o GTM, toma nota de lo siguiente:
- **Plataformas móviles**: Debes actualizar manualmente el código para estas configuraciones. mParticle y Segment no ofrecen una forma de hacerlo a través de su plataforma. 
- **Web**: La integración de Braze debe realizarse de forma nativa para permitir la mínima configuración de integración. Los administradores de etiquetas no ofrecen la posibilidad de hacerlo a través de su plataforma.
{% endalert %} 

## Datos opcionales recogidos por defecto

Además de los datos mínimos de integración, Braze captura automáticamente los siguientes atributos cuando inicializas la integración de SDK. Puedes [optar por no]({{site.baseurl}}/developer_guide/platform_integration_guides/sdk_primer/#blocking-data-collection) recopilar estos atributos para permitir una integración mínima.

| Atributo               | Plataforma          | Descripción                                                                        | Por qué se recoge                                                                                                                                                      |
|-------------------------|-------------------|------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Nombre del navegador            | Web               | Nombre del navegador                                                                | Este atributo se utiliza para enviar mensajes sólo a los exploradores compatibles. También puede utilizarse para la segmentación basada en el navegador.                                     |
| Configuración regional del dispositivo           | Android, iOS      | La configuración regional por defecto del dispositivo                                                   | Este atributo se utiliza para traducir mensajes al idioma preferido del usuario.                                                                                            |
| Localización más reciente del dispositivo           | Android, iOS      | La localización predeterminada más reciente del dispositivo                                                   | Este atributo procede de la configuración del dispositivo del usuario y se utiliza para traducir mensajes al idioma preferido del usuario. Es independiente del atributo `Most Recent Location`.                                                                                            |
| Modelo de dispositivo            | Android, iOS      | El hardware específico del dispositivo                                                | Este atributo se utiliza para enviar mensajes sólo a dispositivos compatibles. También puede utilizarse dentro de la segmentación.                                                 |
| Marca del dispositivo            | Android           | La marca del dispositivo (por ejemplo, Samsung)                                         | Este atributo se utiliza para enviar mensajes sólo a dispositivos compatibles.                                                                                          |
| Operador de telefonía celular del dispositivo | Android, iOS      | El operador de telefonía móvil                                                                 | Este atributo se utiliza opcionalmente para la orientación de los mensajes.<br><br>**Nota:** Este campo ha quedado obsoleto a partir de iOS 16 y pasará por defecto a `--` en una futura versión de iOS. |
| Idioma                | Android, iOS, Web | Idioma del dispositivo o navegador, tomado de la localización del dispositivo                                                            | Este atributo se utiliza para traducir mensajes al idioma preferido del usuario. Se basa en la localización del dispositivo.                                                                                            |
| Configuración de la notificación   | Android, iOS, Web | Si esta aplicación tiene activadas las notificaciones push.                                   | Este atributo se utiliza para activar las notificaciones push.                                                                                                                    |
| Resolución              | Android, iOS, Web | Resolución del dispositivo o navegador                                                          | Se utiliza opcionalmente para la orientación de mensajes basada en dispositivos. El formato de este valor es "`<width>`x`<height>`".                                                                 |
| Zona horaria               | Android, iOS, Web | Zona horaria del dispositivo o navegador                                                           | Este atributo se utiliza para enviar mensajes a la hora adecuada, según la zona horaria local de cada usuario.                                                   |
| Agente de usuario              | Web               | [Agente de usuario](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent) | Este atributo se utiliza para enviar mensajes sólo a dispositivos compatibles. También puede utilizarse dentro de la segmentación.                                                 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

Para saber más sobre el seguimiento de las propiedades a nivel de dispositivo (como operador inalámbrico del dispositivo, zona horaria, resolución y otros), consulta la documentación específica de la plataforma: [Android]({{site.baseurl}}/developer_guide/storage/?tab=android), [iOS]({{site.baseurl}}/developer_guide/storage/?tab=swift), [Web]({{site.baseurl}}/developer_guide/storage/#cookies).

## Datos no recopilados por defecto

Por defecto, no se recogen los siguientes atributos. Cada atributo debe integrarse manualmente.

| Atributo                  | Plataforma     | Descripción                                                                                                                                                                                                                                                                                                               | Por qué no se recoge                                                                                                                                                                                                                                                                 |
|----------------------------|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Seguimiento de anuncios por dispositivo activado | Android, iOS | En iOS:<br>[`set(adTrackingEnabled:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(adtrackingenabled:))<br><br>En Android:<br>[`Braze.setGoogleAdvertisingId()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/set-google-advertising-id.html) | Esta propiedad requiere permisos adicionales a nivel de aplicación, que deben ser concedidos por el integrador.                                                                                                                                                                                      |
| Identificador para anunciantes (IDFA) del dispositivo                | iOS          | Identificador de dispositivo para anunciantes                                                                                                                                                                                                                                                                                         | Esto requiere el marco de transparencia de seguimiento de anuncios, lo que provocará una revisión adicional de la privacidad por parte de la App Store. Para más información, consulte [`set(identifierForAdvertiser:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforadvertiser:)) |
| ID de publicidad de Google      | Android      | Identificador para publicidad en aplicaciones de Google Play                                                                                                                                                                                                                                                                        | Esto requiere que la aplicación recupere el GAID y se lo pase a Braze. Para más detalles, consulta [ID opcional de publicidad de Google]({{site.baseurl}}/developer_guide/platform_integration_guides/android/sdk_integration#google-advertising-id).                                         |
| Ubicación más reciente | Android, iOS | Es la última ubicación GPS conocida del dispositivo del usuario. Se actualiza al iniciar la sesión y se almacena en el perfil del usuario. | Esto requiere que el usuario conceda permiso de ubicación a tu aplicación. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
El SDK de Braze no almacena ninguna dirección IP localmente.
{% endalert %}

## Integración personalizada

Para sacar el máximo partido de Braze, nuestros integradores de SDK a menudo implementan los SDK de Braze y registran [atributos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#setting-custom-attributes), [eventos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#logging-custom-events) y [eventos de compra]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events/#logging-purchase-events) que son pertinentes para su negocio, además de los datos recopilados automáticamente.

Una integración personalizada permite una comunicación adaptada a la experiencia de los usuarios.

{% alert important %}
Braze prohibirá o bloqueará a los usuarios con más de 5.000.000 de sesiones ("usuarios ficticios") y dejará de ingerir sus eventos SDK. Para más información, consulta [Bloqueo de correo no deseado]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#spam-blocking).
{% endalert %}


