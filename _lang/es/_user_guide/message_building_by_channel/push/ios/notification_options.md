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

> Con el lanzamiento de iOS 12 de Apple, Braze ofrece compatibilidad con varias de sus funciones, como [Grupos de notificaciones](#notification-groups), [Notificaciones silenciosas/Autorización provisional](#provisional-push-authentication--quiet-notifications) y [Alertas críticas](#critical-alerts).

## Grupos de notificación

Si quieres categorizar tus mensajes y agruparlos en la bandeja de notificaciones de tu usuario, puedes utilizar la función Grupos de notificaciones de iOS a través de Braze.

Crea tu campaña push para iOS, luego ve a la pestaña **Configuración** y abre el desplegable **Grupo de notificaciones**.

![La pestaña "Configuración" con un desplegable "Grupo de notificaciones" que seleccionó el valor "Cupones".]({% image_buster /assets/img_archive/notification_group_dropdown.png %}){: style="max-width:50%;" }

Seleccione sus grupos de notificación en el menú desplegable. Si la configuración del grupo de notificación no funciona correctamente o selecciona **Ninguno** en el desplegable, el mensaje se enviará automáticamente de forma normal a todos los usuarios definidos en el área de trabajo.

Si no tienes ningún grupo de notificación en esta lista, puedes añadir uno utilizando el ID de subproceso de iOS. Necesitarás un ID de subproceso de iOS por cada grupo de notificación que quieras añadir. A continuación, añádelo a tus grupos de notificación haciendo clic en **Gestionar grupos de notificación** en el menú desplegable y rellenando los campos necesarios en la ventana **Gestionar grupos de notificación push de iOS** que aparece.

![Ventana para administrar grupos de notificaciones push de iOS.]({% image_buster /assets/img_archive/managenotgroups.png %}){: style="max-width:70%;" }

Crea tu campaña push para iOS y luego mira en la parte superior del compositor. Allí verás un desplegable llamado **Grupos de notificación**.

### Resumen de los argumentos

Además de agrupar las notificaciones por Thread IDs, Apple permite editar los resúmenes que aparecen cuando se agrupan las notificaciones. Braze Los usuarios pueden especificar la categoría de resumen, el recuento de resumen y el argumento de resumen al componer una campaña push utilizando nuestra herramienta.

{% alert tip %}
Ten en cuenta que la forma en que se agrupan las notificaciones con el mismo Thread ID en la bandeja de notificaciones está bajo el control del sistema operativo. iOS puede optar por mostrar las notificaciones con el mismo Thread ID por separado o en grupos en función de lo que considere óptimo.
{% endalert %}

Marque la casilla **Opciones de alerta** en el **Push Composer**.

A continuación, seleccione `summary-arg` y `summary-arg-count` como claves e introduzca esos valores en la columna correspondiente. Si no estableces un valor para `summary-arg`, estará predeterminado en 1.

### Categorías resumidas

Las categorías de resumen permiten personalizar todo el resumen que aparece cuando se agrupan las notificaciones. Puede crear y aplicar varias categorías.

Para utilizar una categoría en su mensaje, trabaje con sus desarrolladores para implementarla utilizando el siguiente ejemplo:

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

Una vez configurado esto en su aplicación, utilice la categoría de resumen marcando la casilla **Botones de notificación** y seleccionando **Introducir categoría de iOS prerregistrada**.

A continuación, introduzca el identificador de categoría de resumen que haya establecido en su aplicación.

### Autenticación push provisional y notificaciones silenciosas {#provisional-push}

Apple permite a las marcas la opción de enviar notificaciones push silenciosas a los Centros de Notificaciones de sus usuarios antes de que éstos se inscriban de forma oficial y explícita, lo que le da la oportunidad de demostrar el valor de sus mensajes con antelación. Todo lo que tienes que hacer es [configurar notificaciones push provision](#set-up-provisional-push-notifications) ales en tu aplicación, entonces cualquier usuario que tenga un token push provisional recibirá tus mensajes.

A diferencia de los tokens push tradicionales de iOS, los tokens push provisionales actúan como un "pase de prueba" que permite a las marcas llegar a nuevos usuarios antes de que hayan visto y hecho clic en la solicitud de suscripción push nativa de Apple. Con esta función, tu notificación push llegará directamente a la bandeja de notificaciones de tu nuevo usuario con la opción de "Mantener" o "Desactivar" futuras notificaciones. En lugar de experimentar un recorrido de "adhesión voluntaria", los usuarios experimentarán algo más parecido a un recorrido de "cancelación".

{% alert tip %}
La Autorización provisional tiene el potencial de aumentar drásticamente tu tasa de adhesión voluntaria, pero solo si los usuarios ven valor en tus mensajes. Asegúrese de utilizar nuestras funciones de [segmentación de usuarios]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/), [localización]({{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences/) y [personalización]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/) para garantizar que los usuarios adecuados reciben estas notificaciones de "prueba" en el momento oportuno. A continuación, puede animar a los usuarios a aceptar plenamente sus notificaciones push, sabiendo que añaden valor a la experiencia de los usuarios con su aplicación.
{% endalert %}

Sea cual sea la opción elegida por el usuario, se añadirá el token o [estado de suscripción]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/) correspondiente a su [Configuración de contacto]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/#engagement-tab) en la pestaña **Compromiso** de su perfil de usuario.

![Configuración del contacto con un estado de suscriptor push.]({% image_buster /assets/img/profile-push-prov-auth.png %}){: width="50%"}

Podrá dirigirse a sus usuarios en función de si están autorizados provisionalmente o no utilizando nuestros [filtros de segmentación]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/).

![Panel de detalles de segmento con el filtro de segmento de ejemplo "Autorizado provisionalmente en iOS Cronómetro (iOS) es verdadero" para dirigirse a los usuarios.]({% image_buster /assets/img/segment-push-prov-auth.png %})

{% alert tip %}
Si los usuarios eligen "Desactivar" el push provisional, no verán más mensajes push provisionales tuyos. Tenga cuidado con el contenido y la cadencia de los mensajes enviados mediante esta función.
{% endalert %}

{% alert important %}
Si utiliza avisos push adicionales o [primers push dentro de la aplicación](https://www.braze.com/resources/glossary/priming-for-push/) (un mensaje dentro de la aplicación que anima a los usuarios a optar por las notificaciones push), póngase en contacto con su representante de Braze para obtener orientación adicional.
{% endalert %}

#### Configurar notificaciones push provisionales

Braze le permite registrarse para la autenticación provisional actualizando su código en su fragmento de registro de token dentro de su implementación de Braze iOS SDK utilizando los siguientes fragmentos como ejemplo (envíelos a sus desarrolladores o asegúrese de que [implementan la autenticación push provisional durante el proceso de integración]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#using-usernotification-framework-ios-10)).

{% alert warning %}
La implementación de la autenticación push provisional solo es compatible con iOS 12+ y dará error si el objetivo de despliegue es anterior. Puedes obtener más información al respecto [en nuestra documentación de implementación más detallada aquí]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#using-usernotification-framework-ios-10).
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
  {% tab Objetivo-C %}

**Objetivo-C**

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

Con el nuevo Modo Focus de iOS 15, los usuarios tienen más control sobre cuándo las notificaciones de las apps pueden "interrumpirles" con un sonido o una vibración.

![Página de configuración de notificaciones de iOS que muestra las notificaciones activadas para entrega inmediata y con notificaciones sensibles al tiempo activadas.]({% image_buster /assets/img/ios/ios15-notification-settings.png %}){: style="max-width:40%"}

Las aplicaciones pueden ahora especificar qué nivel de interrupción debe incluir una notificación, en función de su urgencia.

Para cambiar el nivel de interrupción de una notificación push de iOS, seleccione la pestaña **Ajustes** y elija el nivel deseado en el menú desplegable **Nivel de interrupción**.

![Desplegable para seleccionar el nivel de interrupción.]({% image_buster /assets/img/ios/interruption_level.png %}){: style="max-width:50%"}

Esta característica no tiene requisitos mínimos de versión del SDK, pero solo se aplica a dispositivos con iOS 15+.

Ten en cuenta que, en última instancia, los usuarios son los que controlan su atención, e incluso si se envía una notificación sensible al tiempo, pueden especificar qué aplicaciones no pueden interrumpir su atención.

Consulte en la tabla siguiente los niveles de interrupción y sus descripciones.

|Nivel de interrupción|Descripción|Cuándo utilizarlo|Modo de enfoque Break Through|
|--|--|--|--|
|[Pasivo](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/passive)|Envía una notificación sin sonido, vibración ni encender la pantalla.|Notificaciones que no requieren atención inmediata.|No|
|[Activo](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/active) (por defecto)|Sólo emitirá un sonido, una vibración y encenderá la pantalla si el usuario no está en modo de enfoque.|Notificaciones que requieren atención inmediata, a menos que el usuario tenga activado el modo de enfoque.|No|
|[Urgente](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/timesensitive)|Emitirá un sonido, vibrará y encenderá la pantalla incluso cuando esté en modo de enfoque. Para ello es necesario que añadas a tu aplicación en Xcode la **función de notificaciones sensibles al tiempo**.|Notificaciones puntuales que deben molestar a los usuarios independientemente de su modo de enfoque, como una notificación de trayecto compartido o de entrega.|Sí|
|[Crítico](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/critical)|Emitirá un sonido, vibrará y encenderá la pantalla aunque el interruptor **No molestar** del teléfono esté activado. Esto [requiere la aprobación explícita de Apple](https://developer.apple.com/contact/request/notifications-critical-alerts-entitlement/).|Emergencias como condiciones meteorológicas adversas o alertas de seguridad|Sí|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### Puntuación de relevancia (iOS 15+) {#relevance-score}

![Un resumen de notificaciones para iOS titulado "Tu resumen vespertino" con tres notificaciones.]({% image_buster /assets/img/ios/ios15-notification-summary.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0"}

iOS 15 también introduce una nueva forma para que los usuarios programen opcionalmente una agrupación de resumen de varias notificaciones en momentos determinados a lo largo del día. Esto se hace para evitar interrupciones constantes a lo largo del día por notificaciones que no necesitan atención inmediata.

Las aplicaciones pueden especificar qué notificaciones push son más relevantes estableciendo una **puntuación de relevancia**. Apple utilizará esta puntuación para determinar qué notificaciones deben mostrarse en el resumen de notificaciones programado, mientras que otras estarán disponibles cuando los usuarios hagan clic en el resumen. 

Todas las notificaciones seguirán siendo accesibles en el centro de notificaciones del usuario.

Para establecer la puntuación de relevancia de una notificación de iOS, introduzca un valor entre `0.0` y `1.0` en la pestaña **Ajustes**. Por ejemplo, el mensaje más importante debe enviarse con `1.0`, mientras que un mensaje de importancia media puede enviarse con `0.5`.

![Puntuación de relevancia de "0,5".]({% image_buster /assets/img/ios/relevance-score.png %}){: style="max-width:80%;"}

Esta característica no tiene requisitos mínimos de versión del SDK, pero solo se aplica a dispositivos con iOS 15+.

Para más información sobre la longitud máxima de los mensajes para los distintos tipos de mensajes, consulte los siguientes recursos:

- [Especificaciones de imagen y texto]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/#image-and-text-specifications)
- [Directrices sobre el recuento de caracteres en iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/#character-count)

