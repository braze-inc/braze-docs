---
nav_title: Resumen del SDK
article_title: Resumen del SDK para desarrolladores
description: "Este artículo de referencia sobre la incorporación proporciona un resumen técnico para desarrolladores del SDK de Braze. Habla de los análisis predeterminados de los que hace seguimiento el SDK, del bloqueo de la recopilación automática de datos y de la versión en vivo del SDK de tu aplicación."
page_order: 0
---

# [![Curso de Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/path/developer/sdk-integration-basics){: style="float:right;width:120px;border:0;" class="noimgborder"}Resumen del SDK para desarrolladores

> Antes de empezar a integrar los SDK de Braze, puede que te preguntes qué estás construyendo e integrando exactamente. Quizá tengas curiosidad por saber cómo puedes personalizar el SDK para adaptarlo aún más a tus necesidades. Este artículo puede ayudarte a responder a todas tus preguntas sobre el SDK. 

¿Eres especialista en marketing y buscas un resumen básico del SDK? Echa un vistazo a nuestro [resumen de especialistas en marketing]({{site.baseurl}}/user_guide/getting_started/web_sdk/).

En resumen, el SDK de Braze:
* Recoge y sincroniza los datos de usuario en un perfil de usuario consolidado.
* Recoge automáticamente datos de sesión, información del dispositivo y tokens de notificaciones push
* Captura datos de interacción con los clientes de marketing y datos personalizados específicos de tu empresa.
* Potencia las notificaciones push, los mensajes dentro de la aplicación y los canales de mensajería de la tarjeta de contenido

## Rendimiento de la aplicación

Braze no debería tener ningún impacto negativo en el rendimiento de tu aplicación.

Los SDK de Braze ocupan muy poco espacio. Cambiamos automáticamente la tasa de vaciado de datos de usuario en función de la calidad de la red, además de permitir el control manual de la red. Agrupamos automáticamente las solicitudes de API del SDK para asegurarnos de que los datos se registren rápidamente y se mantenga, al mismo tiempo, la máxima eficiencia de la red. Por último, la cantidad de datos enviados desde el cliente a Braze en cada llamada a la API es extremadamente pequeña.

## Compatibilidad SDK

El SDK de Braze está diseñado para comportarse muy bien y no interferir en otros SDK presentes en tu aplicación. Si tienes algún problema que crees que puede deberse a la incompatibilidad con otro SDK, ponte en contacto con el soporte de Braze.

## Análisis predeterminados y gestión de sesiones

Nuestro SDK recopila automáticamente determinados datos de usuario, por ejemplo, la primera aplicación utilizada, la última aplicación utilizada, el recuento total de sesiones, el sistema operativo del dispositivo, etc. Si sigues nuestras guías de integración para implementar nuestros SDK, podrás aprovechar esta [recopilación de datos predeterminada]({{site.baseurl}}/user_guide/data/user_data_collection/sdk_data_collection/). Comprobar esta lista puede ayudarte a evitar almacenar la misma información sobre los usuarios más de una vez. A excepción del inicio y el final de la sesión, el resto de los datos de seguimiento automático no cuentan para tu asignación de puntos de datos.

{% alert note %}
Todas nuestras características son configurables, pero es una buena idea implementar completamente el modelo predeterminado de recopilación de datos.

<br>Si es necesario para tu caso de uso, puedes [limitar la recogida de determinados datos](#blocking-data-collection) una vez finalizada la integración.
{% endalert %}

## Carga y descarga de datos

El SDK de Braze almacena en caché los datos (sesiones, eventos personalizados, etc.) y los carga periódicamente. Sólo cuando se hayan cargado los datos se actualizarán los valores en el panel. El intervalo de subida tiene en cuenta el estado del dispositivo y se rige por la calidad de la conexión a la red:

|Calidad de la conexión a la red |    Intervalo de descarga de datos|
|---|---|
|Genial    |10 segundos|
|Bien    |30 segundos|
|Pobre    |60 segundos|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Si no hay conexión de red, los datos se almacenan en caché localmente en el dispositivo hasta que se restablezca la conexión de red. Cuando se restablezca la conexión, los datos se cargarán en Braze.

Braze envía datos al SDK al inicio de una sesión en función de los segmentos en los que se encuentra el usuario en el momento de la sesión. Los nuevos mensajes dentro de la aplicación no se actualizarán durante la sesión. Sin embargo, los datos de usuario durante la sesión se procesarán continuamente a medida que se envíen desde el cliente. Por ejemplo, un usuario caducado (que utilizó la aplicación por última vez hace más de 7 días) seguirá recibiendo contenido dirigido a usuarios caducados en su primera sesión de vuelta a la aplicación.

## Bloqueo de la recopilación de datos

Es posible (aunque no se sugiere) bloquear la recopilación automática de ciertos datos de tu integración de SDK, o permitir procesos de lista que lo hagan. 

No se recomienda bloquear la recopilación de datos porque eliminar los datos de análisis reduce la capacidad de personalización y orientación de tu plataforma. Por ejemplo:

- Si decides no realizar una integración completa para la ubicación en uno de los SDK, no podrás personalizar tu mensajería en función del idioma o la ubicación. 
- Si decides no realizar la integración para la zona horaria, es posible que no puedas enviar mensajes dentro de la zona horaria de un usuario. 
- Si decides no realizar la integración para la información visual de un dispositivo específico, es posible que el contenido de los mensajes no esté optimizado para ese dispositivo.

Recomendamos encarecidamente integrar completamente los SDK para aprovechar al máximo las capacidades de nuestro producto.

{% tabs %}
{% tab SDK Web %}

Puedes simplemente no integrar determinadas partes del SDK, o utilizar [`disableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disablesdk) para un usuario. Este método sincronizará los datos registrados antes de que se llamara a `disableSDK()`, y hará que se ignoren todas las llamadas posteriores al SDK de la Web de Braze para esta página y para futuras cargas de páginas. Si deseas reanudar la recopilación de datos en un momento posterior, puedes utilizar el método [`enableSDK()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#enablesdk) para reanudar la recopilación de datos en el futuro. Puedes obtener más información al respecto en nuestro artículo [Desactivar el seguimiento Web]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?sdktab=web).

{% endtab %}
{% tab SDK para Android %}

Puedes utilizar [`setDeviceObjectAllowlist`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-device-object-allowlist.html?query=fun%20setDeviceObjectAllowlist(deviceObjectAllowlist:%20EnumSet%3CDeviceKey%3E):%20BrazeConfig.Builder) para configurar el SDK para que sólo envíe un subconjunto de claves o valores del objeto dispositivo según una lista de permitidos establecida. Esto debe habilitarse mediante [`setDeviceObjectAllowlistEnabled`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-device-object-allowlist-enabled.html?query=fun%20setDeviceObjectAllowlistEnabled(enabled:%20Boolean):%20BrazeConfig.Builder).

{% alert important %}
Si la lista de permitidos está vacía, **no se** enviarán datos de dispositivo a Braze.
{% endalert %}

{% endtab %}
{% tab SDK de Swift %}

Puedes asignar un conjunto de campos elegibles a [`configuration.devicePropertyAllowList`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/devicepropertyallowlist) en tu `Braze.Configuration` para especificar una lista de permitidos para los campos del dispositivo que recoge el SDK. La lista completa de campos se define en [`Braze.Configuration.DeviceProperty`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/deviceproperty). Para desactivar la recopilación de todos los campos del dispositivo, establece el valor de esta propiedad en un conjunto vacío (`[]`).

{% alert important %}
De manera predeterminada, todos los campos son recogidos por el SDK Swift de Braze. Eliminar algunas propiedades del dispositivo puede desactivar las características del SDK.
{% endalert %}

Para más detalles de uso, consulta [Almacenamiento]({{site.baseurl}}/developer_guide/storage/?tab=swift) en la documentación del SDK Swift.

{% endtab %}
{% endtabs %}

## ¿En qué versión del SDK estoy?

Puedes utilizar el panel para ver la versión del SDK de una aplicación concreta visitando **Configuración > Configuración de la aplicación.** La **Versión del SDK en vivo** muestra la versión más alta del SDK de Braze utilizada por tu aplicación en vivo más reciente para al menos el 5% de tus usuarios.

![Una aplicación llamada Swifty en un espacio de trabajo. La versión del SDK en vivo es la 6.6.0.]({% image_buster /assets/img/live-sdk-version.png %}){: style="max-width:80%"} 

{% alert tip %}
Si tienes una aplicación iOS, puedes confirmar que estás utilizando el [SDK Swift]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift) en lugar del [SDK Objective-C de iOS]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/overview/) heredado si la **versión de tu SDK en vivo** es igual o superior a la 5.0.0, que fue la primera versión publicada del SDK Swift.
{% endalert %}

