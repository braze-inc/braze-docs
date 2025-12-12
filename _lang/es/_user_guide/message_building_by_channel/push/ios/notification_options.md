---
nav_title: "Opciones de notificación"
article_title: Opciones de notificación de iOS
page_order: 2
page_layout: reference
description: "Este artículo de referencia cubre las opciones de notificación de iOS, como alertas críticas, notificaciones silenciosas, notificaciones push provisionales y más."

platform: iOS
channel:
  - push

---

# Opciones de notificación

> Con el lanzamiento de iOS 12 de Apple, Braze ofrece soporte para varias de sus características, como [Grupos de notificación](#notification-groups), [Notificaciones silenciosas/Autorización provisional](#provisional-push-authentication--quiet-notifications) y [Alertas críticas](#critical-alerts).

## Grupos de notificaciones

Si quieres clasificar tus mensajes y agruparlos en la bandeja de notificaciones de tu usuario, puedes utilizar la característica Grupos de notificaciones de iOS a través de Braze.

Crea tu campaña push de iOS, luego ve a la pestaña **Configuración** y abre el desplegable **Grupo de notificaciones**.

\![La pestaña "Configuración" con un desplegable "Grupo de notificaciones" que seleccionó el valor "Cupones".]({% image_buster /assets/img_archive/notification_group_dropdown.png %}){: style="max-width:50%;" }

Selecciona tus grupos de notificaciones en la lista desplegable. Si la configuración de tu grupo de notificaciones no funciona correctamente o seleccionas **Ninguno** en el desplegable, el mensaje se enviará automáticamente de forma normal a todos los usuarios definidos en el espacio de trabajo.

Si no tienes ningún grupo de notificaciones en esta lista, puedes añadir uno utilizando el ID del hilo de iOS. Necesitarás un ID de hilo de iOS por cada grupo de notificaciones que quieras añadir. A continuación, añádelo a tus grupos de notificaciones haciendo clic en **Gestionar grupos de notificaciones** en el menú desplegable y rellenando los campos necesarios en la ventana **Gestionar grupos de notificaciones push de iOS** que aparece.

Ventana para administrar grupos de notificaciones push de iOS.]({% image_buster /assets/img_archive/managenotgroups.png %}){: style="max-width:70%;" }

Crea tu campaña push para iOS, y luego mira en la parte superior del compositor. Allí verás un menú desplegable llamado **Grupos de notificaciones**.

### Resumen de argumentos

Además de agrupar las notificaciones por ID de hilo, Apple te permite editar los resúmenes que aparecen cuando se agrupan las notificaciones. Braze Los usuarios pueden especificar la categoría del resumen, el recuento del resumen y el argumento del resumen al componer una campaña push utilizando nuestra herramienta.

{% alert tip %}
Ten en cuenta que la forma en que se agrupan las notificaciones con el mismo ID de hilo en la bandeja de notificaciones está bajo el control del sistema operativo. iOS puede elegir mostrar las notificaciones con el mismo ID de hilo por separado o en grupos, dependiendo de lo que considere óptimo.
{% endalert %}

Marca la casilla **Opciones de alerta** en el **Compositor push**.

A continuación, selecciona `summary-arg` y `summary-arg-count` como claves e introduce esos valores en la columna correspondiente. Si no estableces un valor para `summary-arg`, estará predeterminado a 1.

### Categorías resumidas

Las Categorías de resumen te permiten personalizar todo el resumen que aparece cuando se agrupan las notificaciones. Puedes crear y aplicar varias categorías.

Para utilizar una categoría en tu mensaje, trabaja con tus desarrolladores para implementarla utilizando el siguiente ejemplo:

```
UNNotificationCategory *newsCategory = [UNNotificationCategory categoryWithIdentifier:@"news"
                                                      actions:@[likeAction, unlikeAction]
                                                      intentIdentifiers:@[]
                                                      hiddenPreviewsBodyPlaceholder:@""
                                                      categorySummaryFormat:@"%u more news articles from %@"
                                                       Options:0];
```

{% alert important %}
Esto no requerirá una actualización del SDK.
{% endalert %}

{% alert tip %}
Observa que `%u` y `%@` son cadenas de formato para el recuento sumario y el argumento sumario, respectivamente. Cuando se muestre el resumen, estos marcadores de posición se sustituirán por los valores de `summary-count` y `summary-arg`.
{% endalert %}

Una vez configurado esto en tu aplicación, utiliza la categoría de resumen marcando la casilla **Botones de notificación** y seleccionando **Introducir categoría de iOS prerregistrada**.

A continuación, introduce el identificador de la categoría de resumen que hayas configurado en tu aplicación.

### Autenticación push provisional y notificaciones silenciosas {#provisional-push}

Apple permite a las marcas la opción de enviar notificaciones push silenciosas a los centros de notificaciones de sus usuarios antes de que éstos se adhieran voluntaria y explícitamente, lo que te da la oportunidad de demostrar el valor de tus mensajes con antelación. Todo lo que tienes que hacer es [configurar notificaciones push provision](#set-up-provisional-push-notifications) ales en tu aplicación, entonces cualquier usuario que tenga un token de notificaciones push provisional recibirá tus mensajes.

A diferencia de un token de notificaciones push tradicional de iOS, un token de notificaciones push provisional actúa como un "pase de prueba" que permite a las marcas llegar a nuevos usuarios antes de que hayan visto y hecho clic en el mensaje de adhesión voluntaria push nativo de Apple. Con esta característica, tu notificación push se entregará directamente en la bandeja de notificaciones de tu nuevo usuario con la opción de "Mantener" o "Desactivar" futuras notificaciones. En lugar de experimentar un viaje de "adhesión voluntaria", los usuarios experimentarán algo más parecido a un viaje de "exclusión voluntaria".

{% alert tip %}
La Autorización Provisional tiene el potencial de aumentar drásticamente tu tasa de adhesión voluntaria, pero sólo si los usuarios ven valor en tus mensajes. Asegúrate de utilizar nuestras características de [segmentación de usuarios]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/), [localización]({{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences/) y [personalización]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/) para garantizar que los usuarios adecuados reciben estas notificaciones de "prueba" en el momento adecuado. Entonces, puedes animar a los usuarios a que se adhieran voluntariamente a tus notificaciones push, sabiendo que añaden valor a la experiencia de tus usuarios con tu aplicación.
{% endalert %}

Sea cual sea la opción que elija el usuario, se añadirá el token o el [estado de suscripción]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/) adecuados a su [Configuración de contacto]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/#engagement-tab), en la pestaña **Interacción** de su perfil de usuario.

\![Configuración del contacto con un estado de suscriptor push.]({% image_buster /assets/img/profile-push-prov-auth.png %}){: width="50%"}

Podrás dirigirte a tus usuarios en función de si están autorizados provisionalmente o no utilizando nuestros [filtros de segmentación]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/).

\![Panel de detalles de segmento con el filtro de segmento de muestra "Autorizado provisionalmente en Cronómetro iOS (iOS) es verdadero" para dirigirse a los usuarios.]({% image_buster /assets/img/segment-push-prov-auth.png %})

{% alert tip %}
Si los usuarios eligen "Desactivar" el push provisional, no verán más mensajes push provisionales tuyos. ¡Sé cuidadoso con el contenido y la cadencia de los mensajes enviados utilizando esta funcionalidad!
{% endalert %}

{% alert important %}
Si utilizas avisos push adicionales o [primers push dentro de la aplicación](https://www.braze.com/resources/glossary/priming-for-push/) (un mensaje dentro de la aplicación que anima a los usuarios a adherirse a las notificaciones push), ponte en contacto con tu representante de Braze para obtener orientación adicional.
{% endalert %}

#### Configurar notificaciones push provisionales

Braze te permite registrarte para la autenticación provisional actualizando tu código en el fragmento de registro de token dentro de tu implementación del SDK Braze iOS utilizando los siguientes fragmentos como ejemplo (envíalos a tus desarrolladores o asegúrate de que [implementan la autenticación push provisional durante el proceso de integración]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#using-usernotification-framework-ios-10)).

{% alert warning %}
La implementación de la autenticación push provisional sólo es compatible con iOS 12+ y dará error si el objetivo de despliegue es anterior. Puedes obtener más información al respecto [en nuestra documentación de aplicación más detallada aquí]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#using-usernotification-framework-ios-10).
{% endalert %}

{% tabs local %}
  {% tab Swift %}
**Swift**

```
var options: UNAuthorizationOptions = [.alert, .sound, .badge]
if #available(iOS 12.0, *) {
  options = UNAuthorizationOptions(rawValue: options.rawValue | UNAuthorizationOptions.provisional.rawValue)
}
```
  {% endtab %}
  {% tab Objective-C %}

**Objective-C**

```
UNUserNotificationCenter *center = [UNUserNotificationCenter currentNotificationCenter];
center.delegate = self;
UNAuthorizationOptions options = UNAuthorizationOptionAlert | UNAuthorizationOptionSound | UNAuthorizationOptionBadge;
if (@available(iOS 12.0, *)) {
    options = options | UNAuthorizationOptionProvisional;
}
```
  {% endtab %}
{% endtabs %}

### Nivel de interrupción (iOS 15+) {#interruption-level}

Con el nuevo Modo Enfoque de iOS 15, los usuarios tienen más control sobre cuándo las notificaciones de las aplicaciones pueden "interrumpirles" con un sonido o una vibración.

\![Página de configuración de notificaciones de iOS que muestra las notificaciones habilitadas para entrega inmediata y con notificaciones sensibles al tiempo habilitadas.]({% image_buster /assets/img/ios/ios15-notification-settings.png %}){: style="max-width:40%"}

Ahora las aplicaciones pueden especificar qué nivel de interrupción debe incluir una notificación, en función de su urgencia.

Para cambiar el nivel de interrupción de una notificación push de iOS, selecciona la pestaña **Configuración** y elige el nivel deseado en el menú desplegable **Nivel de interrupción**.

Desplegable para seleccionar el nivel de interrupción.]({% image_buster /assets/img/ios/interruption_level.png %}){: style="max-width:50%"}

Esta característica no tiene requisitos mínimos de versión del SDK, pero sólo se aplica a dispositivos con iOS 15+.

Ten en cuenta que, en última instancia, los usuarios son quienes controlan su atención, e incluso si se entrega una notificación sensible al tiempo, pueden especificar qué aplicaciones no pueden traspasar su atención.

Consulta la tabla siguiente para ver los niveles de interrupción y sus descripciones.

|Nivel de interrupción|Descripción|Cuándo utilizarlo|Modo de enfoque Break Through|
|--|--|--|--|
|[Pasivo](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/passive)|Envía una notificación sin sonido, vibración ni encender la pantalla.|Notificaciones que no requieren atención inmediata.|No|
|[Activo](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/active) (predeterminado)|Sólo emitirá un sonido, una vibración y encenderá la pantalla si el usuario no está en Modo Enfoque.|Notificaciones que requieren atención inmediata, a menos que el usuario tenga habilitado el Modo Enfoque.|No|
|[Sensible al tiempo](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/timesensitive)|Emitirá un sonido, vibrará y encenderá la pantalla incluso estando en Modo Enfoque. Para ello es necesario que añadas a tu aplicación en Xcode la **función de Notificaciones sensibles al tiempo**.|Notificaciones puntuales que deben molestar a los usuarios independientemente de su modo de Enfoque, como una notificación de trayecto compartido o de entrega.|Sí|
|[Crítica](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/critical)|Emitirá un sonido, vibrará y encenderá la pantalla aunque esté habilitado el interruptor **No molestar** del teléfono. Esto [requiere la aprobación explícita de Apple](https://developer.apple.com/contact/request/notifications-critical-alerts-entitlement/).|Emergencias como condiciones meteorológicas adversas o alertas de seguridad|Sí|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### Puntuación de relevancia (iOS 15+) {#relevance-score}

Un resumen de notificaciones para iOS titulado "Tu resumen vespertino" con tres notificaciones.]({% image_buster /assets/img/ios/ios15-notification-summary.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0"}

iOS 15 también introduce una nueva forma para que los usuarios programen opcionalmente un resumen agrupado de varias notificaciones en momentos determinados a lo largo del día. Esto se hace para evitar interrupciones constantes a lo largo del día por notificaciones que no necesitan atención inmediata.

Las aplicaciones pueden especificar qué notificaciones push son más relevantes estableciendo una **Puntuación de relevancia**. Apple utilizará esta puntuación para determinar qué notificaciones deben mostrarse en el Resumen de notificaciones programado, mientras que otras estarán disponibles cuando los usuarios hagan clic en el resumen. 

Todas las notificaciones seguirán siendo accesibles en el centro de notificaciones del usuario.

Para establecer la puntuación de relevancia de una notificación de iOS, introduce un valor entre `0.0` y `1.0` en la pestaña **Configuración**. Por ejemplo, el mensaje más importante debe enviarse con `1.0`, mientras que un mensaje de importancia media puede enviarse con `0.5`.

\![Puntuación de relevancia de "0,5".]({% image_buster /assets/img/ios/relevance-score.png %}){: style="max-width:80%;"}

Esta característica no tiene requisitos mínimos de versión del SDK, pero sólo se aplica a dispositivos con iOS 15+.

Para más información sobre la longitud máxima de los mensajes para los distintos tipos de mensajería, consulta los siguientes recursos:

- [Especificaciones de imagen y texto]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/#image-and-text-specifications)
- [Directrices para el recuento de caracteres de iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/#character-count)

