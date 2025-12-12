---
nav_title: "Habilitación push y suscripción"
article_title: Habilitación push y suscripción
page_order: 3
page_type: reference
description: "Este artículo de referencia cubre los conceptos de los estados de habilitación push y suscripción push en Braze, incluyendo las diferencias fundamentales de comportamiento entre iOS, Android y Web."
channel:
  - push

---

# Habilitación push y suscripción push

> Este artículo de referencia cubre los conceptos de habilitación push y estados de suscripción push en Braze, incluyendo las diferencias fundamentales de comportamiento entre iOS, Android y Web.

## Estados de suscripción push {#push-sub-states}

Un "Estado de suscripción push" en Braze identifica la preferencia global de un **usuario** en cuanto a su deseo de recibir notificaciones push. Como el estado de suscripción se basa en el usuario, no es específico de ninguna aplicación concreta. Los estados de suscripción se convierten en banderas útiles a la hora de decidir a qué usuarios dirigir las notificaciones push.

{% alert note %}
El estado de suscripción push de un usuario se aplica a todo su perfil de usuario, que incluye todos los dispositivos del usuario.
{% endalert %}

Hay tres opciones de estado de suscripción push: `Subscribed`, `Opted-In`, y `Unsubscribed`.

Por defecto, para que tu usuario reciba tus mensajes a través de push, su estado de suscripción push debe ser `Subscribed` o `Opted-In`, y debe estar [habilitado para push](#foreground-push-enabled). Puedes anular esta configuración si es necesario al redactar un mensaje.

|Estado de adhesión voluntaria|Descripción|
|---|---|
|`Subscribed`| Estado predeterminado de la suscripción push cuando se crea un perfil de usuario en Braze. |
|`Opted-In`| Un usuario ha expresado explícitamente su preferencia por recibir notificaciones push. Braze cambiará automáticamente el estado de adhesión voluntaria de un usuario a `Opted-In` si acepta un mensaje de adhesión voluntaria.<br><br>Esto no se aplica a los usuarios de Android 12 o inferior.|
|`Unsubscribed`| Un usuario se da de baja explícitamente de push a través de tu aplicación o de otros métodos que tu marca proporcione. Por defecto, las campañas push de Braze sólo se dirigen a los usuarios que están en `Subscribed` o `Opted-in` para push.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Braze no cambia automáticamente el estado de suscripción push de un usuario a `Unsubscribed`. Recuerda que si el estado de suscripción push de un usuario es `Unsubscribed`, entonces el filtro `Foreground Push Enabled` del usuario en la segmentación será `false`.
{% endalert %}

### Actualización de los estados de suscripción push {#update-push-subscription-state}

Hay tres formas de actualizar el estado de suscripción push de un usuario:

#### Adhesión voluntaria automática (predeterminada)

De forma predeterminada, Braze establece el estado de suscripción push de un usuario en `Opted-In` cuando autoriza por primera vez las notificaciones push de tu aplicación. Braze también lo hace cuando un usuario vuelve a habilitar los permisos push en su configuración del sistema tras haberlos deshabilitado previamente.

{% tabs local %}
{% tab android %}
Para desactivar este comportamiento predeterminado, añade la siguiente propiedad al archivo `braze.xml` de tu proyecto de Android Studio:

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

Puedes actualizar el estado de suscripción de un usuario con el SDK de Braze utilizando el método `setPushNotificationSubscriptionType` en [Web](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setpushnotificationsubscriptiontype), [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/set-push-notification-subscription-type.html) o [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/set(pushnotificationsubscriptionstate:)). Por ejemplo, puedes utilizar este método para crear una página de configuración en tu aplicación en la que los usuarios puedan habilitar o deshabilitar manualmente las notificaciones push.

#### API REST

Puedes actualizar el estado de suscripción de un usuario con la API REST de Braze utilizando el [punto final`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) para actualizar su [`push_subscribe`]({{site.baseurl}}/api/objects_filters/user_attributes_object) atributo.

### Comprobación del estado de la suscripción push

\![Perfil de usuario de John Doe con su estado de suscripción push establecido en Suscrito.]({% image_buster /assets/img/push_example.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Hay dos formas de comprobar el estado de la suscripción push de un usuario con Braze:

1. **Perfil de usuario** Puedes acceder a los perfiles de usuario individuales a través del panel de Braze en la pantalla **[Búsqueda de usuarios]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/)** de Usuario. Tras encontrar el perfil de un usuario (a través de la dirección de correo electrónico, el número de teléfono o el ID externo de usuario), puedes seleccionar la pestaña **Interacción** para ver y ajustar manualmente el estado de suscripción de un usuario.
2. **Exportación de API REST:** Puedes exportar perfiles de usuario individuales en formato JSON utilizando los puntos finales de exportación [Usuarios por segmento]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/) o [Usuarios por identificador]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/). Braze devolverá un objeto token de notificaciones push que contiene información de habilitación push por dispositivo.

## Push permiso

Todas las plataformas habilitadas para push -iOS, Web y Android- requieren una adhesión voluntaria explícita a través de un aviso del sistema a nivel de sistema operativo, con algunas ligeras diferencias que se describen a continuación.

Dado que la decisión de un usuario es definitiva y no puedes volver a preguntarle después de que se niegue, utilizar mensajes [push primer]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/) dentro de la aplicación es una estrategia importante para aumentar tus tasas de adhesión voluntaria.

**Peticiones de permiso push para SO nativos**

|Plataforma|Captura de pantalla|Descripción|
|--|--|--|
|iOS| Un mensaje push nativo de iOS que pregunta "Mi aplicación desea enviarte notificaciones" con dos botones, "No permitir" y "Permitir", en la parte inferior del mensaje.]({% image_buster /assets/img/push_implementation_guide/ios-push-prompt.png %}){: style="max-width:410px;"} | Esto no se aplica cuando se solicita [un](#provisional-push) permiso [push provisional](#provisional-push).|
|Android| \![Un mensaje push de Android que pregunta "¿Permitir que Kitchenerie te envíe notificaciones?" con dos botones, "Permitir" y "No permitir", en la parte inferior del mensaje.]({% image_buster /assets/img/push_implementation_guide/android-push-prompt.png %}){: style="max-width:410px;"} | Este permiso push se introdujo en Android 13. Antes de Android 13, no se necesitaba permiso para enviar push.|
|Web| \![Un aviso push nativo del navegador web que pregunta "Braze.com desea mostrar notificación" con dos botones, "Bloquear" y "Permitir" en la parte inferior del mensaje.]({% image_buster /assets/img/push_implementation_guide/web-push-prompt.png %}){: style="max-width:410px;"} | |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Android

Antes de Android 13, no se necesitaba permiso para enviar notificaciones push. En Android 12 e inferiores, todos los usuarios se consideran `Subscribed` en su primera sesión cuando Braze solicita automáticamente un token de notificaciones push. En este punto, el usuario está **habilitado para push** con un token de notificaciones push válido para ese dispositivo y un estado de suscripción predeterminado de `Subscribed`.

A partir de [Android 13]({{site.baseurl}}/developer_guide/platforms/android/android_13/), el permiso push debe ser solicitado y concedido por el usuario. Tu aplicación puede solicitar permiso manualmente al usuario en los momentos oportunos, pero si no lo hace, se le pedirá automáticamente cuando tu aplicación cree un [canal de notificación](https://developer.android.com/reference/android/app/NotificationChannel).

### iOS

Una notificación en el centro de notificaciones del sistema con un mensaje en la parte inferior que pregunta: "¿Seguir recibiendo notificaciones de la aplicación Yachtr?" con dos botones debajo para "Seguir" o "Desactivar".]({% image_buster /assets/img/push_implementation_guide/ios-provisional-push.png %}){: style="float:right;max-width:430px;width:40%;margin-left:15px;border:0"}

Tu aplicación puede solicitar push provisional o push autorizado. 

El push autorizado requiere el permiso explícito de un usuario antes de enviar cualquier notificación, mientras que [el push provisional](https://www.braze.com/resources/articles/mastering-provisional-push) te permite enviar notificaciones __silenciosamente__, directamente al centro de notificaciones sin ningún sonido o alerta.

#### Autorización provisional y push silencioso {#provisional-push}

Antes de iOS 12 (lanzado en 2018), todos los usuarios debían optar explícitamente por recibir notificaciones push.

En iOS 12, Apple introdujo [la autorización provisional](https://www.braze.com/resources/articles/mastering-provisional-push), que permite a las marcas enviar notificaciones push silenciosas al centro de notificaciones de sus usuarios antes de que se adhieran voluntariamente de forma explícita, lo que te da la oportunidad de demostrar el valor de tus mensajes antes de tiempo. Consulta la [autorización provisional]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/#provisional-push-authentication--quiet-notifications) para saber más.

### Web

Para Web, debes solicitar la adhesión voluntaria explícita del usuario a través del diálogo de permiso del navegador nativo.

A diferencia de iOS y Android, que permiten a tu aplicación mostrar la solicitud de permiso en cualquier momento, algunos navegadores modernos sólo la muestran si la desencadena un "gesto del usuario" (clic del ratón o pulsación de una tecla). Si tu sitio intenta solicitar permiso de notificación push al cargar la página, es probable que el navegador lo ignore o lo silencie.

En consecuencia, debes pedir permiso sólo cuando un usuario haga clic en algún lugar de tu sitio web y no aleatoriamente cuando se cargue una página.

## Tokens de notificaciones push

[Los tokens de notificaciones push]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/) son un identificador único anónimo generado por el dispositivo de un usuario y enviado a Braze para identificar dónde enviar la notificación de cada destinatario.

Hay dos formas de clasificar un [token de notificaciones push]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/) que son esenciales para entender cómo se puede enviar una notificación push a tus usuarios.

1. **La función push en primer plano** permite enviar notificaciones push visibles de forma regular al primer plano del dispositivo de un usuario.
2. **El push en segundo plano** está disponible independientemente de si un dispositivo concreto ha optado por recibir notificaciones push de esa marca. El push en segundo plano permite a las marcas enviar notificaciones push silenciosas -notificaciones que intencionadamente no se muestran- a los dispositivos para apoyar funcionalidades clave como [el seguimiento de la desinstalación]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking/).

Cuando un perfil de usuario tiene un token de notificaciones push válido asociado a una aplicación, Braze considera que el usuario está "registrado push" para la aplicación en cuestión. Braze, por tanto, proporciona un filtro de segmentación específico, `Foreground Push Enabled for App,` para ayudar a identificar a estos usuarios.

{% alert note %}
El filtro `Foreground Push Enabled for App` sólo tiene en cuenta la presencia de un token de notificaciones push válido en primer y segundo plano para la aplicación en cuestión. Sin embargo, el filtro más genérico [`Foreground Push Enabled`](#foreground-push-enabled) filtra segmentos de usuarios que hayan activado explícitamente notificaciones push para cualquier aplicación de tu espacio de trabajo. Este recuento sólo incluye el push en primer plano y no incluye a los usuarios que se han dado de baja. Puedes obtener más información sobre estos y otros filtros en [Filtros de segmentación]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters).
{% endalert %}

### Varios usuarios en un dispositivo

Los tokens de notificaciones push son específicos de un dispositivo y de una aplicación, por lo que no es posible utilizar tokens de notificaciones push para distinguir entre varios usuarios que utilicen el mismo dispositivo.

Por ejemplo, supongamos que tienes dos usuarios: Charlie y Kim. Si Charlie ha habilitado las notificaciones push para tu aplicación en su teléfono y Kim utiliza el teléfono de Charlie para salir del perfil de Charlie e iniciar sesión en el suyo, el token de notificaciones push se reasignará al perfil de Kim. El token de notificaciones push permanecerá asignado al perfil de Kim en ese dispositivo hasta que se desconecte y Charlie vuelva a conectarse.

Una aplicación o sitio web sólo puede tener una suscripción push por dispositivo. Así, cuando un usuario se desconecta de un dispositivo o sitio web, y un nuevo usuario se conecta, el token de notificaciones push se reasigna al nuevo usuario. Esto se refleja en el perfil del usuario, en la sección **Configuración de contacto** de la pestaña **Interacción**:

Registro de cambios del token de notificaciones push en la pestaña \*\*Interacción** del perfil de un usuario, que enumera cuándo se trasladó el token de notificaciones push a otro usuario, y de qué token se trataba.]({% image_buster /assets/img/push_token_changelog.png %})

Como los proveedores de push (APN/FCM) no tienen forma de distinguir entre varios usuarios de un mismo dispositivo, pasamos el token de notificaciones push al último usuario que haya iniciado sesión para determinar a qué usuario del dispositivo hay que enviar la notificación push.

### Varios dispositivos y un usuario

El estado de suscripción push se basa en el usuario y no es específico de ninguna aplicación individual. El estado de la suscripción push es el valor que se configuró por última vez. Así, si un usuario ha optado por las notificaciones push, su estado de suscripción push es `Opted-in` en todos los dispositivos elegibles. Si más tarde un usuario se da de baja explícitamente de las notificaciones push a través de tu aplicación o de otros métodos que proporcione tu marca, su estado de suscripción push se actualiza a `Unsubscribed` y ningún dispositivo registrado como push puede recibir notificaciones push.

## Primer plano Push Filtrar habilitado {#foreground-push-enabled}

`Foreground Push Enabled` es un filtro de segmentación en Braze que permite a los especialistas en marketing identificar fácilmente a los usuarios que permiten a Braze enviar notificaciones push y a los usuarios que no han expresado su preferencia por no recibir notificaciones push. 

El filtro `Foreground Push Enabled` tiene en cuenta lo siguiente:
- Posibilidad de que Braze envíe una notificación push (token de notificaciones push en primer plano).
- La preferencia general del usuario para recibir push en cualquiera de sus dispositivos (estado de suscripción push)

\![Una captura de pantalla del panel que muestra que un usuario es "Push registrado para marketing (iOS)"]({% image_buster /assets/img/push_enablement.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

Se considera que un usuario está "habilitado para push" o "registrado para push" si tiene un token de notificaciones push activo para una aplicación dentro de tu espacio de trabajo, lo que significa que el estado de habilitación para push es específico de cada aplicación. 

{% alert note %}
Para obtener información sobre cómo comprobar el estado del registro push, visita el [estado del registro push]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/#checking-push-registration-status)
{% endalert %}

## Otros escenarios específicos de la plataforma

{% tabs %}
{% tab Android %}

Si un usuario habilitado para push en primer plano desactiva push en la configuración de su SO, al inicio de la siguiente sesión:
- Braze los marca como deshabilitados para push en primer plano y ya no intenta enviarles mensajes push.
- El filtro `Foreground Push Enabled for App (Android)` y el filtro de segmentación `Foreground Push Enabled` (suponiendo que ninguna otra aplicación del perfil de usuario tenga un token de notificaciones push válido) devolverán `false`.

En este caso, como seguirá existiendo un token de notificaciones push en segundo plano, puedes seguir enviando notificaciones push en segundo plano (silenciosas) con el filtro de segmentación `Background or Foreground Push Enabled = true`.

Para Android, Braze considerará que un usuario ha desactivado el push si:

- Un usuario desinstala la aplicación de su dispositivo.
- No se ha podido entregar un mensaje push debido a un rebote. Esto suele deberse a una desinstalación, pero también puede deberse a actualizaciones de la aplicación, a una nueva versión del token de notificaciones push o al formato. 
- Falla el registro push en Firebase Cloud Messaging (a veces debido a malas conexiones de red o a un fallo en la conexión con o en FCM para devolver un token válido).
- El usuario bloquea las notificaciones push de la aplicación en la configuración de su dispositivo y, posteriormente, inicia una sesión.

{% alert note %}
Sólo puedes interceptar una notificación push de Android cuando la aplicación está en primer o segundo plano (pero sigue ejecutándose). No puedes interceptar las notificaciones cuando la aplicación se cierra o se mata por completo.
{% endalert %}

{% endtab %}
{% tab iOS %}

Independientemente de que el usuario acepte el mensaje de adhesión voluntaria push en primer plano, podrás enviar una notificación push en segundo plano si tienes habilitadas las notificaciones remotas en Xcode y tu aplicación llama a [`registerForRemoteNotifications()`](https://developer.apple.com/documentation/uikit/uiapplication/1623078-registerforremotenotifications).

Si tu aplicación está autorizada provisionalmente o el usuario ha optado por el push, recibe un token de notificaciones push en primer plano, que te permite enviarle todo tipo de push. En Braze, consideramos que un usuario de iOS habilitado para push en primer plano está habilitado para push, ya sea explícitamente (a nivel de aplicación) o provisionalmente (a nivel de dispositivo).

Si un usuario rechaza recibir notificaciones push a nivel de SO, su estado de suscripción push será `Subscribed`, y su perfil no mostrará que se ha registrado un token de notificaciones push en primer plano. 

En el caso de que un usuario, que inicialmente optó por la adhesión voluntaria a nivel de SO, deshabilite las notificaciones push en la configuración de su SO, al iniciar la siguiente sesión ocurrirá lo siguiente:
- Braze los marca como deshabilitados para push en primer plano y ya no intenta enviar mensajes push.
- El filtro `Foreground Push Enabled for App (iOS)` y el filtro de segmentación `Foreground Push Enabled` (suponiendo que ninguna otra aplicación del perfil de usuario tenga un token de notificaciones push válido) devolverán `false`.

En este caso, como seguirá existiendo un token de notificaciones push en segundo plano, puedes seguir enviando notificaciones push en segundo plano (silenciosas) con el filtro de segmentación `Background or Foreground Push Enabled = true`.

{% alert note %}
iOS no permite que las aplicaciones intercepten una notificación push antes de que ésta se muestre. Esto significa que las aplicaciones (y Braze) no tienen control sobre si puedes mostrar u ocultar la notificación. Un usuario puede optar por no recibir notificaciones push de una aplicación en la configuración del dispositivo, pero eso lo controla el sistema operativo.
{% endalert %}

{% endtab %}
{% tab Web %}

Cuando un usuario acepte la solicitud de permiso push nativo, su estado de suscripción cambiará a `opted in`.

Para gestionar las suscripciones, puedes utilizar el método de usuario [`setPushNotificationSubscriptionType`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setpushnotificationsubscriptiontype) para crear una página de configuración de preferencias en tu sitio, después de lo cual puedes filtrar a los usuarios por estado de adhesión voluntaria en el panel.

Si un usuario desactiva las notificaciones en su navegador, la siguiente notificación push enviada a ese usuario rebotará, y Braze actualizará el token de notificaciones push del usuario en consecuencia. Se utiliza para gestionar la elegibilidad para los filtros habilitados para push (`Background or Foreground Push Enabled`, `Foreground Push Enabled` y `Foreground Push Enabled for App`). El estado de suscripción establecido en el perfil de usuario es una configuración a nivel de usuario y no cambia cuando rebota un push.

{% alert note %}
Las plataformas Web no permiten el push en segundo plano o silencioso.
{% endalert %}
{% endtab %}
{% endtabs %}

## Buenas prácticas

Consulta nuestro artículo dedicado a [las mejores prácticas de Push]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices) para obtener orientación detallada sobre cómo optimizar tu uso de push en Braze.

