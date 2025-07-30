---
nav_title: "Habilitación y suscripción push"
article_title: Habilitación y suscripción push
page_order: 3
page_type: reference
description: "En este artículo de referencia se cubren los conceptos de los estados de habilitación push y suscripción push en Braze, incluyendo las diferencias fundamentales de comportamiento entre iOS, Android y Web."
channel:
  - push

---

# Habilitación y suscripción push

> En este artículo de referencia se cubren los conceptos de habilitación push y estados de suscripción push en Braze, incluidas las diferencias fundamentales de comportamiento entre iOS, Android y Web.

## Estados de suscripción push {#push-sub-states}

Un "Estado de suscripción push" en Braze identifica la preferencia global de un **usuario** en cuanto a su deseo de recibir notificaciones push. Dado que el estado de suscripción se basa en el usuario, no es específico de ninguna aplicación concreta. Los estados de suscripción se convierten en banderas útiles a la hora de decidir a qué usuarios dirigir las notificaciones push.

{% alert note %}
El estado de suscripción push de un usuario se aplica a todo su perfil de usuario, que incluye todos los dispositivos del usuario.
{% endalert %}

Hay tres opciones de estado de suscripción push: `Subscribed`, `Opted-In` y `Unsubscribed`.

Por defecto, para que tu usuario reciba tus mensajes a través de push, su estado de suscripción push debe ser `Subscribed` o `Opted-In`, y debe estar [habilitado para push](#push-enabled). Puede anular esta configuración si es necesario al redactar un mensaje.

|Estado de adhesión voluntaria|Descripción|
|---|---|
|`Subscribed`| Estado predeterminado de la suscripción push cuando se crea un perfil de usuario en Braze. |
|`Opted-In`| Un usuario ha expresado explícitamente su preferencia por recibir notificaciones push. Braze cambiará automáticamente el estado de adhesión voluntaria de un usuario a `Opted-In` si acepta un mensaje de adhesión voluntaria.<br><br>Esto no se aplica a los usuarios de Android 12 o inferior.|
|`Unsubscribed`| Un usuario se da de baja explícitamente de push a través de tu aplicación o de otros métodos que tu marca pone a tu disposición. Por defecto, las campañas push de Braze sólo se dirigen a los usuarios que están en `Subscribed` o `Opted-in` para push.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Braze no cambia automáticamente el estado de suscripción push de un usuario a `Unsubscribed`. Recuerde que si el estado de suscripción push de un usuario es `Unsubscribed`, entonces el filtro `Push Enabled` del usuario en la segmentación será `false`.
{% endalert %}

### Actualización de los estados de suscripción push {#update-push-subscription-state}

Existen tres formas de actualizar el estado de suscripción push de un usuario:

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

Puedes actualizar el estado de suscripción de un usuario con la API REST de Braze utilizando el [punto final`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) para actualizar su [`push_subscribe`]({{site.baseurl}}/api/objects_filters/user_attributes_object) atributo.

### Comprobación del estado de la suscripción push

![Perfil de usuario de John Doe con su estado de suscripción push establecido en Suscrito.]({% image_buster /assets/img/push_example.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Hay dos formas de comprobar el estado de la suscripción push de un usuario con Braze:

1. **Perfil del usuario**: Puedes acceder a los perfiles de usuario individuales a través del panel de Braze en la sección **[Búsqueda de usuarios]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/)** de usuarios. Después de encontrar el perfil de un usuario (a través de la dirección de correo electrónico, el número de teléfono o el ID de usuario externo), puede seleccionar la pestaña **Compromiso** para ver y ajustar manualmente el estado de suscripción de un usuario.
<br><br>
2. **Exportación de API REST**: Puedes exportar perfiles de usuario individuales en formato JSON utilizando los puntos finales de exportación [Usuarios por segmento]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/) o [Usuarios por identificador]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/). Braze devolverá un objeto de tokens push que contiene información de habilitación push por dispositivo.

## Permiso de notificaciones push

Todas las plataformas compatibles con push (iOS, Web y Android) requieren un consentimiento explícito a través de una solicitud del sistema a nivel del sistema operativo, con algunas ligeras diferencias que se describen a continuación.

Dado que la decisión de un usuario es definitiva y no puedes volver a preguntarle después de que se niegue, utilizar mensajes [push primer]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/) dentro de la aplicación es una estrategia importante para aumentar tus tasas de adhesión voluntaria.

**Peticiones de permisos push del SO nativo**

|Plataforma|Captura de pantalla|Descripción|
|--|--|--|
|iOS| ![Una notificación push nativa de iOS que pregunta "A mi aplicación le gustaría enviarte notificaciones" con dos botones, "No permitir" y "Permitir" en la parte inferior del mensaje.]({% image_buster /assets/img/push_implementation_guide/ios-push-prompt.png %}){: style="max-width:410px;"} | Esto no se aplica cuando se solicita un[ permiso push provisional](#provisional-push).|
|Android| ![Un mensaje push de Android que pregunta "¿Permitir que Kitchenerie te envíe notificaciones?" con dos botones, "Permitir" y "No permitir", en la parte inferior del mensaje.]({% image_buster /assets/img/push_implementation_guide/android-push-prompt.png %}){: style="max-width:410px;"} | Este permiso push se introdujo en Android 13. Antes de Android 13, no se necesitaba permiso para enviar push.|
|Web| ![Un aviso push nativo del navegador web que pregunta "Braze.com desea mostrar notificación" con dos botones, "Bloquear" y "Permitir" en la parte inferior del mensaje.]({% image_buster /assets/img/push_implementation_guide/web-push-prompt.png %}){: style="max-width:410px;"} | |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Android

Antes de Android 13, no se necesitaba permiso para enviar notificaciones push. En Android 12 e inferiores, todos los usuarios se consideran `Subscribed` en su primera sesión cuando Braze solicita automáticamente un token de notificaciones push. En este punto, el usuario está **habilitado para push** con un token push válido para ese dispositivo y un estado de suscripción predeterminado de `Subscribed`.

A partir de [Android 13]({{site.baseurl}}/developer_guide/platforms/android/android_13/), el permiso push debe ser solicitado y concedido por el usuario. Tu aplicación puede pedir permiso manualmente al usuario en los momentos oportunos, pero si no, se lo pedirá automáticamente cuando tu aplicación cree un [canal de notificación](https://developer.android.com/reference/android/app/NotificationChannel).

### iOS

![Una notificación en el centro de notificaciones del sistema con un mensaje en la parte inferior que pregunta: "¿Seguir recibiendo notificaciones de la aplicación Yachtr?" con dos botones debajo para "Seguir" o "Desactivar"]({% image_buster /assets/img/push_implementation_guide/ios-provisional-push.png %}){: style="float:right;max-width:430px;width:40%;margin-left:15px;border:0"}

Su aplicación puede solicitar push provisional o push autorizado. 

El push autorizado requiere el permiso explícito de un usuario antes de enviar cualquier notificación, mientras que [el push provisional](https://www.braze.com/resources/articles/mastering-provisional-push) te permite enviar notificaciones __silenciosamente__, directamente al centro de notificaciones sin ningún sonido o alerta.

#### Autorización provisional y push silencioso {#provisional-push}

Antes de iOS 12 (lanzado en 2018), todos los usuarios debían optar explícitamente por recibir notificaciones push.

En iOS 12, Apple introdujo [la autorización provisional](https://www.braze.com/resources/articles/mastering-provisional-push), que permite a las marcas enviar notificaciones push silenciosas al centro de notificaciones de sus usuarios antes de que se adhieran voluntariamente de forma explícita, lo que te da la oportunidad de demostrar el valor de tus mensajes antes de tiempo. Consulte la [autorización provisional]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/#provisional-push-authentication--quiet-notifications) para obtener más información.

### Web

Para la Web, debe solicitar el consentimiento explícito del usuario a través del cuadro de diálogo de permisos del navegador nativo.

A diferencia de iOS y Android, que permiten que tu aplicación muestre el aviso de permiso en cualquier momento, algunos navegadores modernos sólo lo muestran si se activa mediante un "gesto del usuario" (clic del ratón o pulsación de una tecla). Si tu sitio intenta solicitar permiso de notificación push al cargar la página, es probable que el navegador lo ignore o lo silencie.

En consecuencia, debe pedir permiso sólo cuando un usuario haga clic en algún lugar de su sitio web y no aleatoriamente cuando se cargue una página.

## Tokens de notificaciones push

[Los tokens de notificaciones push]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/) son un identificador único anónimo generado por el dispositivo de un usuario y enviado a Braze para identificar dónde enviar la notificación de cada destinatario.

Hay dos formas de clasificar un [token de notificaciones push]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/) que son esenciales para entender cómo se puede enviar una notificación push a tus usuarios.

1. **Foreground push** ofrece la posibilidad de enviar notificaciones push visibles de forma regular al primer plano del dispositivo de un usuario.
2. **El push en segundo plano** está disponible independientemente de si un dispositivo concreto ha optado por recibir notificaciones push de esa marca. El push en segundo plano permite a las marcas enviar notificaciones push silenciosas -notificaciones que intencionadamente no se muestran- a los dispositivos para dar soporte a funcionalidades clave como [el seguimiento de desinstalaciones]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking/).

Cuando un perfil de usuario tiene un token push válido en primer plano asociado a una aplicación, Braze considera que el usuario está "registrado push" para la aplicación en cuestión. Braze, entonces, proporciona un filtro de segmentación específico, `Push Enabled for App,` para ayudar a identificar a estos usuarios.

{% alert note %}
El filtro `Push Enabled for App` sólo tiene en cuenta la presencia de un token push válido en primer y segundo plano para la aplicación en cuestión. Sin embargo, el filtro más genérico [`Push Enabled`](#push-enabled) segmenta a los usuarios que han activado explícitamente las notificaciones push para cualquier aplicación de su área de trabajo. Este recuento incluye sólo los push en primer plano y no incluye a los usuarios que se han dado de baja. Puede obtener más información sobre estos y otros filtros en [Filtros de segmentación]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters).
{% endalert %}

### Varios usuarios en un dispositivo

Los tokens push son específicos tanto de un dispositivo como de una aplicación, por lo que no es posible utilizarlos para distinguir entre varios usuarios que utilicen el mismo dispositivo.

Por ejemplo, supongamos que tiene dos usuarios: Charlie y Kim. Si Charlie ha activado las notificaciones push para tu aplicación en su teléfono y Kim utiliza el teléfono de Charlie para salir del perfil de Charlie e iniciar sesión en el suyo, el token push se reasignará al perfil de Kim. El token push permanecerá asignado al perfil de Kim en ese dispositivo hasta que se desconecte y Charlie vuelva a conectarse.

Una aplicación o sitio web sólo puede tener una suscripción push por dispositivo. Así, cuando un usuario se desconecta de un dispositivo o sitio web y otro nuevo se conecta, el token push se reasigna al nuevo usuario. Esto se refleja en el perfil del usuario, en la sección **Configuración de contactos** de la pestaña **Compromiso**:

![Registro de cambios del token de notificaciones push en la pestaña \*\*Interacción** del perfil de un usuario, que enumera cuándo se trasladó el token de notificaciones push a otro usuario, y cuál era el token.]({% image_buster /assets/img/push_token_changelog.png %})

Dado que los proveedores de push (APN/FCM) no pueden distinguir entre varios usuarios en un mismo dispositivo, pasamos el token de push al último usuario que inició sesión para determinar a qué usuario se debe enviar el push en el dispositivo.

### Varios dispositivos y un usuario

El estado de la suscripción push se basa en el usuario y no es específico de ninguna aplicación concreta. El estado de la suscripción push es el valor que se estableció por última vez. Así, si un usuario ha optado por recibir notificaciones push, su estado de suscripción push es `Opted-in` en todos los dispositivos elegibles. Si más tarde un usuario se da de baja explícitamente de las notificaciones push a través de tu aplicación o de otros métodos que proporcione tu marca, su estado de suscripción push se actualiza a `Unsubscribed` y ningún dispositivo registrado como push puede recibir notificaciones push.

## Filtro de notificaciones push habilitadas {#push-enabled}

`Push Enabled` es un filtro de segmentación en Braze que permite a los profesionales del marketing identificar fácilmente a los usuarios que permiten a Braze enviar notificaciones push y a los usuarios que no han expresado preferencias para no recibir notificaciones push. 

El filtro `Push Enabled` tiene en cuenta lo siguiente:
- Posibilidad de que Braze envíe una notificación push (token push en primer plano).
- La preferencia general del usuario para recibir push en cualquiera de sus dispositivos (estado de suscripción push)

![Una captura de pantalla del panel que muestra que un usuario es "Push Registrado para Marketing (iOS)"]({% image_buster /assets/img/push_enablement.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

Se considera que un usuario está "habilitado para push" o "registrado para push" si tiene un token push activo en primer plano para una aplicación dentro de su espacio de trabajo, lo que significa que el estado de habilitación para push es específico de la aplicación. 

{% alert note %}
Para obtener información sobre cómo comprobar el estado del registro push, visita [Estado del registro push]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/#checking-push-registration-status)
{% endalert %}

## Otros escenarios específicos de la plataforma

{% tabs %}
{% tab Android %}

Si un usuario habilitado para push en primer plano desactiva push en la configuración de su SO, entonces al inicio de la siguiente sesión:
- Braze los marca como deshabilitados para push en primer plano y ya no intenta enviarles mensajes push.
- El filtro `Push Enabled for App (Android)` y el filtro de segmentación `Push Enabled` (suponiendo que ninguna otra aplicación en el perfil del usuario tenga un token push de primer plano válido) devolverán `false`.

En este caso, como seguirá existiendo un token push en segundo plano, puede seguir enviando notificaciones push en segundo plano (silenciosas) con el filtro de segmentación `Background Push Enabled = true`.

Para Android, Braze considerará que un usuario ha desactivado el push si:

- Un usuario desinstala la aplicación de su dispositivo.
- No se ha podido entregar un mensaje push debido a un rebote. Esto suele deberse a una desinstalación, pero también puede deberse a actualizaciones de la aplicación, a una nueva versión del token push o al formato. 
- Falla el registro push en Firebase Cloud Messaging (a veces debido a malas conexiones de red o a un fallo en la conexión con o en FCM para devolver un token válido).
- El usuario bloquea las notificaciones push de la aplicación en la configuración de su dispositivo y, a continuación, inicia una sesión.

{% endtab %}
{% tab iOS %}

Independientemente de que el usuario acepte el mensaje de adhesión voluntaria push en primer plano, podrás enviar una notificación push en segundo plano si tienes habilitadas las notificaciones remotas en Xcode y tu aplicación llama a [`registerForRemoteNotifications()`](https://developer.apple.com/documentation/uikit/uiapplication/1623078-registerforremotenotifications).

Si tu aplicación está autorizada provisionalmente o el usuario ha optado por push, recibirá un token push en primer plano, lo que te permitirá enviarle todo tipo de push. En Braze, consideramos que un usuario de iOS que tiene activada la función push en primer plano lo está de forma explícita (a nivel de aplicación) o provisional (a nivel de dispositivo).

Si un usuario rechaza recibir notificaciones push a nivel de sistema operativo, su estado de suscripción push será `Subscribed`, y su perfil no mostrará que se ha registrado un token push en primer plano. 

En el caso de que un usuario, que inicialmente optó en el nivel del sistema operativo, deshabilite las notificaciones push en la configuración de su sistema operativo, en el siguiente inicio de sesión, ocurrirá lo siguiente:
- Braze los marca como deshabilitados para push en primer plano y ya no intenta enviar mensajes push.
- El filtro `Push Enabled for App (iOS)` y el filtro de segmentación `Push Enabled` (suponiendo que ninguna otra aplicación en el perfil del usuario tenga un token push de primer plano válido) devolverán `false`.

En este caso, como seguirá existiendo un token push en segundo plano, puede seguir enviando notificaciones push en segundo plano (silenciosas) con el filtro de segmentación `Background Push Enabled = true`.

{% endtab %}
{% tab Web %}

Cuando un usuario acepte la solicitud de permiso push nativo, su estado de suscripción cambiará a `opted in`.

Para gestionar las suscripciones, puede utilizar el método de usuario [`setPushNotificationSubscriptionType`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setpushnotificationsubscriptiontype) para crear una página de configuración de preferencias en su sitio, tras lo cual podrá filtrar a los usuarios por estado de exclusión en el panel de control.

Si un usuario desactiva las notificaciones en su navegador, la siguiente notificación push enviada a ese usuario rebotará, y Braze actualizará el token push del usuario en consecuencia. Se utiliza para gestionar la elegibilidad para los filtros habilitados para push (`Background Push Enabled`, `Push Enabled` y `Push Enabled for App`). El estado de suscripción establecido en el perfil del usuario es una configuración a nivel de usuario y no cambia cuando un push rebota.

{% alert note %}
Las plataformas web no permiten el push en segundo plano o silencioso.
{% endalert %}
{% endtab %}
{% endtabs %}

## Buenas prácticas

Consulte nuestro artículo dedicado a [las mejores prácticas de Push]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices) para obtener información detallada sobre cómo optimizar el uso de Push en Braze.

