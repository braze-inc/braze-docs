## Estados de suscripción push {#push-sub-states}

Un "Estado de suscripción push" en Braze identifica la preferencia global de un **usuario** en cuanto a su deseo de recibir notificaciones push. Dado que el estado de suscripción se basa en el usuario, no es específico de ninguna aplicación concreta. Los estados de suscripción se convierten en banderas útiles a la hora de decidir a qué usuarios dirigir las notificaciones push.

{% alert note %}
El estado de suscripción push de un usuario se aplica a todo su perfil de usuario, que incluye todos los dispositivos del usuario.
{% endalert %}

Existen las siguientes opciones de estado de suscripción: `Subscribed`, `Opted-In`, y `Unsubscribed`.

De forma predeterminada, para que tus usuarios puedan recibir tus mensajes a través de notificaciones push, su estado de suscripción a las notificaciones push debe ser  o`Subscribed` `Opted-In`, y deben tener habilitadas las notificaciones push en primer plano. Puede anular esta configuración si es necesario al redactar un mensaje.

|Estado de adhesión voluntaria|Descripción|
|---|---|
|`Subscribed`| Estado predeterminado de la suscripción push cuando se crea un perfil de usuario en Braze. |
|`Opted-In`| Un usuario ha expresado explícitamente su preferencia por recibir notificaciones push. Braze cambia automáticamente el estado de adhesión voluntaria de un usuario a`Opted-In`  si este acepta un mensaje de push a nivel del sistema operativo.<br><br>Esto no se aplica a los usuarios de Android 12 o inferior.|
|`Unsubscribed`| Un usuario se da de baja explícitamente de push a través de tu aplicación o de otros métodos que tu marca pone a tu disposición. De forma predeterminada, las campañas push de Braze se dirigen únicamente a los usuarios que están`Subscribed`  o`Opted-in`  para push.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Braze no cambia automáticamente el estado de suscripción push de un usuario a `Unsubscribed`. Recuerda que si el estado de la suscripción push de un usuario es `Unsubscribed`, entonces el filtro `Foreground Push Enabled`del usuario en la segmentación es `false`.
{% endalert %}

### Actualización de los estados de suscripción push {#update-push-subscription-state}

Revisa las siguientes formas de actualizar el estado de la suscripción push de un usuario:

#### Inscripción automática (por defecto)

Por defecto, Braze establece el estado de suscripción push de un usuario en `Opted-In` cuando autoriza por primera vez las notificaciones push para tu aplicación. Braze también lo hace cuando un usuario vuelve a activar los permisos push en la configuración del sistema tras haberlos desactivado previamente.

{% tabs local %}
{% tab android %}
Para desactivar este comportamiento predeterminado, añada la siguiente propiedad al archivo `braze.xml` de su proyecto de Android Studio:

```xml
<bool name="com_braze_optin_when_push_authorized">false</bool>
```
{% endtab %}

{% tab swift %}
A partir de [la versión 7.5.0 del SDK de Braze Swift](https://github.com/braze-inc/braze-swift-sdk/releases/tag/7.5.0), puedes desactivar o personalizar aún más este comportamiento añadiendo la configuración `optInWhenPushAuthorized` al archivo `AppDelegate.swift` de tu proyecto Xcode:

```swift
configuration.optInWhenPushAuthorized = false // disables the default behavior

let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```
{% endtab %}
{% endtabs %}

#### Integración de SDK

Puede actualizar el estado de suscripción de un usuario con el SDK Braze utilizando el método `setPushNotificationSubscriptionType` en [Web](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setpushnotificationsubscriptiontype), [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/set-push-notification-subscription-type.html) o [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/set(pushnotificationsubscriptionstate:)). Por ejemplo, puedes utilizar este método para crear una página de configuración en tu aplicación en la que los usuarios puedan activar o desactivar manualmente las notificaciones push.

#### API REST

Puedes actualizar el estado de suscripción de un usuario con la API REST de Braze utilizando el[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) [ punto final]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) para actualizar su[`push_subscribe`]({{site.baseurl}}/api/objects_filters/user_attributes_object)  atributo.

### Comprobación del estado de la suscripción push

![Perfil de usuario de John Doe con su estado de suscripción push establecido en Suscrito.]({% image_buster /assets/img/push_example.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Puedes comprobar el estado de la suscripción push de un usuario con Braze de cualquiera de las siguientes maneras:

* **Perfil del usuario:** Puedes acceder a los perfiles de usuario individuales a través del panel de Braze en la página **[de búsqueda de usuarios]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/)**. Después de encontrar el perfil de un usuario (a través de la dirección de correo electrónico, el número de teléfono o el ID de usuario externo), puede seleccionar la pestaña **Compromiso** para ver y ajustar manualmente el estado de suscripción de un usuario.
* **Exportación de la API REST:** Puedes exportar perfiles de usuario individuales en formato JSON utilizando los puntos finales Exportar [usuarios por segmento]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/) o [Exportar usuarios por identificador]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/). Braze devuelve un objeto de tokens de notificaciones push que contiene información sobre la habilitación de push por dispositivo.