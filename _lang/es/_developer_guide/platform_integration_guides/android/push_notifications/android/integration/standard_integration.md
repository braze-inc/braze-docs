---
nav_title: Integración estándar
article_title: Integración estándar de notificaciones push para Android
platform: Android
page_order: 0
description: "Este artículo explica cómo integrar notificaciones push en tu aplicación Android."
channel:
  - push
search_rank: 3
---

# Integración push estándar de Android

> Aprende a integrar notificaciones push en tu aplicación Android.

Con las notificaciones push, puedes reactivar la interacción de los usuarios de tu aplicación enviándoles contenido relevante y urgente directamente a la pantalla de su dispositivo, aunque la aplicación esté cerrada. Cuando hayas terminado de integrar push en tu aplicación, asegúrate de consultar nuestras [mejores prácticas de push]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/).

{% alert important %}
Si tu integración push de Android ya está configurada y quieres migrar desde la API [de mensajería en la nube obsoleta de Google, consulta Migrar a la API de Firebase Cloud Messaging]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/migrating_to_firebase_cloud_messaging).
{% endalert %}

## Límite de velocidad

La API de Firebase Cloud Messaging (FCM) tiene un límite de velocidad predeterminado de 600 000 solicitudes por minuto. Si alcanzas este límite, Braze lo volverá a intentar automáticamente en unos minutos. Para solicitar un aumento, ponte en contacto con [el servicio de asistencia de Firebase](https://firebase.google.com/support).

## Registro para push

En esta sección, aprenderás a registrarte para push utilizando la API de Firebase Cloud Messaging (FCM) de Google. Si quieres ver una aplicación de ejemplo que utiliza FCM con el SDK para Android de Braze, consulta [Braze: Aplicación de ejemplo de push Firebase](https://github.com/braze-inc/braze-android-sdk/tree/master/samples/firebase-push).

### Paso 1: Añade Firebase a tu proyecto

Primero, añade Firebase a tu proyecto de Android. Para obtener instrucciones paso a paso, consulta la [guía de configuración de Firebase](https://firebase.google.com/docs/android/setup) de Google.

### Paso 2: Añade Mensajería en la Nube a tus dependencias

A continuación, añade la biblioteca Cloud Messaging a las dependencias de tu proyecto. En tu proyecto Android, abre `build.gradle`, y añade la siguiente línea a tu bloque `dependencies`.

```gradle
implementation "google.firebase:firebase-messaging:+"
```

Tus dependencias deben tener un aspecto similar al siguiente:

```gradle
dependencies {
  implementation project(':android-sdk-ui')
  implementation "com.google.firebase:firebase-messaging:+"
}
```

### Paso 3: Habilitar la API de mensajería en la nube de Firebase

En Google Cloud, selecciona el proyecto que utiliza tu aplicación Android y, a continuación, habilita la [API de mensajería de Firebase Cloud](https://console.cloud.google.com/apis/library/fcm.googleapis.com).

![Habilitada la API Firebase Cloud Messaging (FCM)]({% image_buster /assets/img/android/push_integration/create_a_service_account/firebase-cloud-messaging-api-enabled.png %}){: style="max-width:80%;"}

### Paso 4: Crear una cuenta de servicio

A continuación, crea una nueva cuenta de servicio, para que Braze pueda realizar llamadas autorizadas a la API al registrar tokens de FCM. En Google Cloud, ve a **Service Accounts (Cuentas de servicio)** y elige tu proyecto. En la página **Cuentas de servicio**, selecciona **Crear cuenta de servicio**.

![Página de inicio de la cuenta de servicio de un proyecto con la opción "Crear cuenta de servicio" resaltada.]({% image_buster /assets/img/android/push_integration/create_a_service_account/select-create-service-account.png %})

Introduce un nombre de cuenta de servicio, un ID y una descripción, luego selecciona **Crear y continuar**.

![El formulario para "Detalles de la cuenta de servicio".]({% image_buster /assets/img/android/push_integration/create_a_service_account/enter-service-account-details.png %})

En el campo **Rol**, busca y selecciona **Administrador de la API de mensajería en la nube de Firebase** en la lista de roles. Para un acceso más restrictivo, crea un [rol personalizado](https://cloud.google.com/iam/docs/creating-custom-roles) con el permiso `cloudmessaging.messages.create` y, en su lugar, elígelo de la lista. Cuando hayas terminado, selecciona **Hecho**.

{% alert warning %}
Asegúrate de seleccionar **Firebase Cloud Messaging _API_ Admin**, no **Firebase Cloud Messaging Admin**.
{% endalert %}

![El formulario para "Conceder a esta cuenta de servicio acceso al proyecto" con "Firebase Cloud Messaging API Admin" seleccionado como rol.]({% image_buster /assets/img/android/push_integration/create_a_service_account/add-fcm-api-admin.png %})

### Paso 5: Generar credenciales JSON

A continuación, genera las credenciales JSON de tu cuenta del servicio FCM. En Google Cloud IAM & Admin, ve a **Service Accounts (Cuentas de servicio)** y elige tu proyecto. Localiza la cuenta de servicio FCM [que creaste anteriormente](#step-3-create-a-service-account) y, a continuación, selecciona <i class="fa-solid fa-ellipsis-vertical"></i> **Acciones** > **Gestionar claves**.

![La página de inicio de la cuenta de servicio del proyecto con el menú "Acciones" abierto.]({% image_buster /assets/img/android/push_integration/generate_json_credentials/select-manage-keys.png %})

Selecciona **Añadir clave** > **Crear nueva clave**.

![La cuenta de servicio seleccionada con el menú "Añadir clave" abierto.]({% image_buster /assets/img/android/push_integration/generate_json_credentials/select-create-new-key.png %})

Elige **JSON** y selecciona **Crear**. Si creaste tu cuenta de servicio utilizando un ID de proyecto de Google Cloud distinto del ID de tu proyecto de FCM, tendrás que actualizar manualmente el valor asignado a `project_id` en tu archivo JSON.

Asegúrate de recordar dónde descargaste la clave: la necesitarás en el siguiente paso.

![El formulario para crear una clave privada con "JSON" seleccionado.]({% image_buster /assets/img/android/push_integration/generate_json_credentials/select-create.png %}){: style="max-width:65%;"}

{% alert warning %}
Las claves privadas pueden suponer un riesgo para la seguridad si se ponen en peligro. Guarda tus credenciales JSON en una ubicación segura por ahora: eliminarás tu clave después de subirla a Braze.
{% endalert %}

### Paso 6: Sube tus credenciales JSON a Braze

A continuación, carga tus credenciales JSON en tu panel de Braze. En Braze, selecciona <i class="fa-solid fa-gear"></i> **Configuración** > Configuración de la aplicación **.**

![El menú "Configuración" se abre en Braze con la opción "Configuración de la aplicación" resaltada.]({% image_buster /assets/img/android/push_integration/upload_json_credentials/select-app-settings.png %})

En la **configuración de notificaciones push** de tu aplicación Android, elige **Firebase**, luego selecciona **Cargar archivo JSON** y carga las credenciales [que generaste anteriormente](#step-4-generate-json-credentials). Cuando hayas terminado, selecciona **Guardar**.

![El formulario de "Configuración de notificaciones push" con "Firebase" seleccionado como proveedor de notificaciones push.]({% image_buster /assets/img/android/push_integration/upload_json_credentials/upload-json-file.png %})

{% alert warning %}
Las claves privadas pueden suponer un riesgo para la seguridad si se ponen en peligro. Ahora que tu clave está cargada en Braze, borra el archivo [que generaste anteriormente](#step-4-generate-json-credentials).
{% endalert %}

### Paso 7: Configurar el registro automático de tokens

Cuando uno de tus usuarios opta por recibir notificaciones push, tu aplicación necesita generar un token de FCM en su dispositivo antes de que puedas enviarle notificaciones push. Con el SDK de Braze, puedes habilitar el registro automático del token FCM para cada dispositivo de usuario en los archivos de configuración Braze de tu proyecto.

Primero, ve a la Consola Firebase, abre tu proyecto y selecciona <i class="fa-solid fa-gear"></i> **Configuración** > **Configuración del proyecto**.

![El proyecto Firebase con el menú "Configuración" abierto.]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/select-project-settings.png %})

Selecciona **Mensajería en la nube** y, a continuación, en **API de mensajería en la nube de Firebase (V1)**, copia el número en el campo **ID del remitente**.

![La página "Cloud Messaging" del proyecto Firebase con el "Sender ID" resaltado.]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/copy-sender-id.png %})

A continuación, abre tu proyecto de Android Studio y utiliza tu ID de remitente de Firebase para habilitar el registro automático del token de FCM en tu `braze.xml` o `BrazeConfig`.

{% tabs local %}
{% tab braze.xml %}
Para configurar el registro automático de tokens de FCM, añade las siguientes líneas a tu archivo `braze.xml`:

```xml
<bool translatable="false" name="com_braze_firebase_cloud_messaging_registration_enabled">true</bool>
<string translatable="false" name="com_braze_firebase_cloud_messaging_sender_id">FIREBASE_SENDER_ID</string>
```

Sustituye `FIREBASE_SENDER_ID` por el valor que copiaste de la configuración de tu proyecto Firebase. Tu `braze.xml` debe tener un aspecto similar al siguiente:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <string translatable="false" name="com_braze_api_key">12345ABC-6789-DEFG-0123-HIJK456789LM</string>
  <bool translatable="false" name="com_braze_firebase_cloud_messaging_registration_enabled">true</bool>
<string translatable="false" name="com_braze_firebase_cloud_messaging_sender_id">603679405392</string>
</resources>
```
{% endtab %}
{% tab BrazeConfig %}
Para configurar el registro automático de tokens de FCM, añade las siguientes líneas a tu `BrazeConfig`:

{% subtabs global %}
{% subtab JAVA %}
```java
.setIsFirebaseCloudMessagingRegistrationEnabled(true)
.setFirebaseCloudMessagingSenderIdKey("FIREBASE_SENDER_ID")
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
.setIsFirebaseCloudMessagingRegistrationEnabled(true)
.setFirebaseCloudMessagingSenderIdKey("FIREBASE_SENDER_ID")
```
{% endsubtab %}
{% endsubtabs %}

Sustituye `FIREBASE_SENDER_ID` por el valor que copiaste de la configuración de tu proyecto Firebase. Tu `BrazeConfig` debe tener un aspecto similar al siguiente:

{% subtabs global %}
{% subtab JAVA %}
```java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
  .setApiKey("12345ABC-6789-DEFG-0123-HIJK456789LM")
  .setCustomEndpoint("sdk.iad-01.braze.com")
  .setSessionTimeout(60)
  .setHandlePushDeepLinksAutomatically(true)
  .setGreatNetworkDataFlushInterval(10)
  .setIsFirebaseCloudMessagingRegistrationEnabled(true)
  .setFirebaseCloudMessagingSenderIdKey("603679405392")
  .build();
Braze.configure(this, brazeConfig);
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
val brazeConfig = BrazeConfig.Builder()
  .setApiKey("12345ABC-6789-DEFG-0123-HIJK456789LM")
  .setCustomEndpoint("sdk.iad-01.braze.com")
  .setSessionTimeout(60)
  .setHandlePushDeepLinksAutomatically(true)
  .setGreatNetworkDataFlushInterval(10)
  .setIsFirebaseCloudMessagingRegistrationEnabled(true)
  .setFirebaseCloudMessagingSenderIdKey("603679405392")
  .build()
Braze.configure(this, brazeConfig)
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert tip %}
Si quieres registrar manualmente los tokens de FCM, puedes llamar a [`Braze.setRegisteredPushToken()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/registered-push-token.html) dentro del método [`onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate()) de tu aplicación.
{% endalert %}

### Paso 8: Elimina las solicitudes automáticas en tu clase de aplicación

Para evitar que Braze desencadene solicitudes de red innecesarias cada vez que envíes notificaciones push silenciosas, elimina cualquier solicitud de red automática configurada en el método `onCreate()` de tu clase `Application`. Para más información, consulta [Referencia para desarrolladores de Android: Aplicación](https://developer.android.com/reference/android/app/Application).

## Recepción y visualización de push {#displaying-push}

Después de completar esta sección, deberías poder recibir y mostrar las notificaciones push enviadas por Braze.

### Paso 1: Registrar el servicio de mensajería Firebase de Braze

{% alert warning %}
Si ya tienes registrado un servicio de mensajería Firebase, no completes este paso. En su lugar, ve a [Utilizar tu propio servicio de mensajería Firebase](#using-your-own-firebase-messaging-service) y completa los pasos que allí se indican.
{% endalert %}

Braze incluye un servicio para gestionar la recepción push y las intenciones abiertas. Nuestra clase `BrazeFirebaseMessagingService` deberá registrarse en tu `AndroidManifest.xml`:

```xml
<service android:name="com.braze.push.BrazeFirebaseMessagingService"
  android:exported="false">
  <intent-filter>
    <action android:name="com.google.firebase.MESSAGING_EVENT" />
  </intent-filter>
</service>
```

Nuestro código de notificación también utiliza `BrazeFirebaseMessagingService` para gestionar el seguimiento de las acciones de apertura y clic. Este servicio debe estar registrado en `AndroidManifest.xml` para funcionar correctamente. Además, recuerda que Braze antepone una clave única a las notificaciones procedentes de nuestro sistema, de modo que sólo reproduzcamos las notificaciones enviadas desde nuestros sistemas. Puedes registrar servicios adicionales por separado para recibir notificaciones enviadas desde otros servicios de FCM. Consulta [`AndroidManifest.xml`](https://github.com/braze-inc/braze-android-sdk/blob/master/samples/firebase-push/src/main/AndroidManifest.xml "`AndroidManifest.xml`") en el ejemplo de aplicación push de Firebase.

{% alert important %}
Antes del SDK de Braze 3.1.1, se utilizaba `AppboyFcmReceiver` para gestionar el push de FCM. La clase `AppboyFcmReceiver` debe eliminarse de tu manifiesto y sustituirse por la integración anterior.
{% endalert %}

#### Utilizar un servicio de mensajería Firebase alternativo

Si tienes otro servicio de mensajería Firebase que también te gustaría utilizar, también puedes especificar un servicio de mensajería Firebase alternativo al que llamar si tu aplicación recibe un push que no procede de Braze.

En tu `braze.xml`, especifica:

```xml
<bool name="com_braze_fallback_firebase_cloud_messaging_service_enabled">true</bool>
<string name="com_braze_fallback_firebase_cloud_messaging_service_classpath">com.company.OurFirebaseMessagingService</string>
```

o mediante la [configuración en tiempo de ejecución:]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/runtime_configuration/)

{% tabs %}
{% tab JAVA %}

```java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
        .setFallbackFirebaseMessagingServiceEnabled(true)
        .setFallbackFirebaseMessagingServiceClasspath("com.company.OurFirebaseMessagingService")
        .build();
Braze.configure(this, brazeConfig);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val brazeConfig = BrazeConfig.Builder()
        .setFallbackFirebaseMessagingServiceEnabled(true)
        .setFallbackFirebaseMessagingServiceClasspath("com.company.OurFirebaseMessagingService")
        .build()
Braze.configure(this, brazeConfig)
```

{% endtab %}
{% endtabs %}

#### Utilizar tu propio servicio de mensajería Firebase

Si ya tienes registrado un servicio de mensajería Firebase, puedes pasar [`RemoteMessage`](https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage) objetos a Braze a través de [`BrazeFirebaseMessagingService.handleBrazeRemoteMessage()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.push/-braze-firebase-messaging-service/-companion/handle-braze-remote-message.html). Este método sólo mostrará una notificación si el objeto [`RemoteMessage`](https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage) objeto procede de Braze y lo ignorará de forma segura en caso contrario.

{% tabs %}
{% tab JAVA %}

```java
public class MyFirebaseMessagingService extends FirebaseMessagingService {
  @Override
  public void onMessageReceived(RemoteMessage remoteMessage) {
    super.onMessageReceived(remoteMessage);
    if (BrazeFirebaseMessagingService.handleBrazeRemoteMessage(this, remoteMessage)) {
      // This Remote Message originated from Braze and a push notification was displayed.
      // No further action is needed.
    } else {
      // This Remote Message did not originate from Braze.
      // No action was taken and you can safely pass this Remote Message to other handlers.
    }
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
class MyFirebaseMessagingService : FirebaseMessagingService() {
  override fun onMessageReceived(remoteMessage: RemoteMessage?) {
    super.onMessageReceived(remoteMessage)
    if (BrazeFirebaseMessagingService.handleBrazeRemoteMessage(this, remoteMessage)) {
      // This Remote Message originated from Braze and a push notification was displayed.
      // No further action is needed.
    } else {
      // This Remote Message did not originate from Braze.
      // No action was taken and you can safely pass this Remote Message to other handlers.
    }
  }
}
```

{% endtab %}
{% endtabs %}

### Paso 2: Ajustar los iconos pequeños a las directrices de diseño

Para obtener información general sobre los iconos de notificación de Android, visita el [resumen de Notificaciones](https://developer.android.com/guide/topics/ui/notifiers/notifications).

A partir de Android N, debes actualizar o eliminar los activos de los iconos de notificación pequeños que impliquen color. El sistema Android (no el SDK de Braze) ignora todos los canales no alfa y de transparencia en los iconos de acción y en el icono pequeño de notificación. En otras palabras, Android convertirá todas las partes de tu pequeño icono de notificación en monocromo, excepto las regiones transparentes.

Para crear correctamente un activo de icono pequeño de notificación:
- Elimina todos los colores de la imagen excepto el blanco.
- Todas las demás regiones no blancas del activo deben ser transparentes.

{% alert note %}
Un síntoma común de un activo incorrecto es que el pequeño icono de notificación se muestre como un cuadrado monocromo sólido. Esto se debe a que el sistema Android no puede encontrar ninguna región transparente en el activo del icono pequeño de notificación.
{% endalert %}

Los siguientes íconos grandes y pequeños son ejemplos de íconos correctamente diseñados:

![Un icono pequeño que aparece en la esquina inferior de un icono grande junto a un mensaje que dice "Oye, voy de camino al bar pero..."]({% image_buster /assets/img_archive/large_and_small_notification_icon.png %} "Icono de notificación grande y pequeño")

### Paso 3: Configurar iconos de notificación

#### Especificar íconos en braze.xml

Braze te permite configurar tus iconos de notificación especificando recursos dibujables en tu `braze.xml`:

```xml
<drawable name="com_braze_push_small_notification_icon">REPLACE_WITH_YOUR_ICON</drawable>
<drawable name="com_braze_push_large_notification_icon">REPLACE_WITH_YOUR_ICON</drawable>
```

Es necesario configurar un pequeño icono de notificación. **Si no estableces ninguno, Braze utilizará por defecto el icono de la aplicación como icono pequeño de notificación, lo que puede parecer poco óptimo.**

Configurar un icono de notificación grande es opcional pero recomendable.

#### Especificar el color de acento del icono

El color de acento del icono de notificación se puede anular en tu `braze.xml`. Si no se especifica el color, el color predeterminado es el mismo gris que Lollipop utiliza para las notificaciones del sistema.

```xml
<integer name="com_braze_default_notification_accent_color">0xFFf33e3e</integer>
```

También puedes utilizar opcionalmente una referencia de color:

```xml
<color name="com_braze_default_notification_accent_color">@color/my_color_here</color>
```

### Paso 4: Añadir vínculos profundos

#### Habilitación de la apertura automática de vínculos profundos

Para habilitar Braze para que abra automáticamente tu aplicación y cualquier vínculo profundo cuando se haga clic en una notificación push, configura `com_braze_handle_push_deep_links_automatically` en `true`, en tu `braze.xml`:

```xml
<bool name="com_braze_handle_push_deep_links_automatically">true</bool>
```

Esta bandera también se puede establecer mediante [la configuración en tiempo de ejecución]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/runtime_configuration/):

{% tabs %}
{% tab JAVA %}

```java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
        .setHandlePushDeepLinksAutomatically(true)
        .build();
Braze.configure(this, brazeConfig);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val brazeConfig = BrazeConfig.Builder()
        .setHandlePushDeepLinksAutomatically(true)
        .build()
Braze.configure(this, brazeConfig)
```

{% endtab %}
{% endtabs %}

Si quieres gestionar de forma personalizada los vínculos profundos, tendrás que crear una devolución de llamada push que escuche las intenciones push recibidas y abiertas de Braze. Consulta nuestro artículo [Gestión personalizada de recibos push y aperturas]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#android-push-listener-callback) para obtener más información.

#### Crear vínculos profundos personalizados

Sigue las instrucciones que se encuentran en la [documentación para desarrolladores de Google](http://developer.android.com/training/app-indexing/deep-linking.html "AndroidDocumentación de") sobre vinculación en profundidad si aún no has añadido vínculos en profundidad a tu aplicación. Para saber más sobre qué son los vínculos profundos, consulta nuestro [artículo de Preguntas frecuentes]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking).

#### Añadir vínculos profundos

El panel de Braze admite la configuración de vínculos profundos o URL de Web en campañas de notificaciones push y Lienzos que se abrirán cuando se haga clic en la notificación.

![La configuración de "Comportamiento al hacer clic" en el panel de Braze con la opción "Vinculación profunda con la aplicación" seleccionada en el menú desplegable.]({% image_buster /assets/img_archive/deep_link_click_action.png %} "Acción de clic de vinculación profunda")

#### Personalizar el comportamiento de la pila de actividades

El SDK de Android, de forma predeterminada, colocará la actividad principal iniciadora de tu aplicación anfitriona en la pila de actividades cuando se sigan vínculos profundos push. Braze te permite configurar una actividad personalizada para que se abra en la pila de actividades en lugar de tu actividad principal iniciadora o desactivar por completo la pila de actividades.

Por ejemplo, para establecer una actividad llamada `YourMainActivity` como actividad de la pila trasera mediante la [configuración en tiempo de ejecución]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/runtime_configuration/):

{% tabs %}
{% tab JAVA %}

```java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
        .setPushDeepLinkBackStackActivityEnabled(true)
        .setPushDeepLinkBackStackActivityClass(YourMainActivity.class)
        .build();
Braze.configure(this, brazeConfig);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val brazeConfig = BrazeConfig.Builder()
        .setPushDeepLinkBackStackActivityEnabled(true)
        .setPushDeepLinkBackStackActivityClass(YourMainActivity.class)
        .build()
Braze.configure(this, brazeConfig)
```

{% endtab %}
{% endtabs %}

Consulta la configuración equivalente para tu `braze.xml`. Nota que el nombre de la clase debe ser el mismo que devuelve `Class.forName()`.

```xml
<bool name="com_braze_push_deep_link_back_stack_activity_enabled">true</bool>
<string name="com_braze_push_deep_link_back_stack_activity_class_name">your.package.name.YourMainActivity</string>
```

### Paso 5: Definir canales de notificación

El SDK para Android de Braze es compatible con [los canales de notificación de Android](https://developer.android.com/preview/features/notification-channels.html). Si una notificación Braze no contiene el ID de un canal de notificación o que una notificación Braze contiene un ID de canal no válido, Braze mostrará la notificación con el canal de notificación predeterminado definido en el SDK. Los usuarios de Braze utilizan [los canales de notificación de Android]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/notification_channels/) dentro de la plataforma para agrupar notificaciones.

Para configurar el nombre de usuario del canal de notificación predeterminado de Braze, utiliza [`BrazeConfig.setDefaultNotificationChannelName()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-default-notification-channel-name.html).

Para configurar la descripción orientada al usuario del canal de notificación predeterminado de Braze, utiliza [`BrazeConfig.setDefaultNotificationChannelDescription()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-default-notification-channel-description.html).

Actualiza cualquier campaña de la API con el parámetro de [objeto push de Android]({{site.baseurl}}/api/objects_filters/messaging/android_object/) para incluir el campo `notification_channel`. Si no se especifica este campo, Braze enviará la carga útil de la notificación con el ID del canal [alternativo del panel]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/notification_channels/#dashboard-fallback-channel).

Aparte del canal de notificación predeterminado, Braze no creará ningún canal. Todos los demás canales deben ser definidos mediante programación por la aplicación anfitriona y luego introducidos en el panel de Braze.

El nombre y la descripción predeterminados del canal también se pueden configurar en `braze.xml`.

```xml
<string name="com_braze_default_notification_channel_name">Your channel name</string>
<string name="com_braze_default_notification_channel_description">Your channel description</string>
```

### Paso 6: Visualización y análisis de las notificaciones de las pruebas

#### Pantalla de pruebas

En este punto, deberías poder ver las notificaciones enviadas desde Braze. Para probarlo, ve a la página **Campañas** de tu panel de Braze y crea una campaña de **Notificación push**. Elige **Android Push** y diseña tu mensaje. A continuación, haz clic en el icono del ojo en el compositor para obtener el remitente de la prueba. Introduce el ID de usuario o la dirección de correo electrónico de tu usuario actual y haz clic en **Enviar prueba**. Deberías ver aparecer el push en tu dispositivo.

![La pestaña "Prueba" de una campaña de notificación push en el panel de Braze.]({% image_buster /assets/img_archive/android_push_test.png %} "Android Push Test")

Para problemas relacionados con la visualización push, consulta nuestra [guía de solución de problemas]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/troubleshooting/).

#### Análisis de pruebas

En este punto, también deberías tener un registro de análisis de las aperturas de notificaciones push. Si haces clic en la notificación cuando llegue, las **Direct Opens** de la página de resultados de tu campaña aumentarán en 1. Consulta nuestro artículo [sobre los informes push]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_reporting/) para obtener más información sobre los análisis push.

Para problemas relacionados con los análisis push, consulta nuestra [guía de solución de problemas]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/troubleshooting/).

#### Pruebas desde la línea de comandos

Si quieres probar las notificaciones dentro de la aplicación y las notificaciones push a través de la interfaz de línea de comandos, puedes enviar una única notificación a través del terminal mediante cURL y la [API de mensajería]({{site.baseurl}}/api/endpoints/messaging/). Tendrás que sustituir los siguientes campos por los valores correctos para tu caso de prueba:

- `YOUR_API_KEY` (Ve a **Configuración** > **Claves de API**).
- `YOUR_EXTERNAL_USER_ID` (Busca un perfil en la página **Buscar usuarios** ).
- `YOUR_KEY1` (opcional)
- `YOUR_VALUE1` (opcional)

{% alert note %}
Si utilizas la [navegación antigua]({{site.baseurl}}/navigation), estas páginas se encuentran en una ubicación diferente: <br>- **Las claves de API** se encuentran en **Consola para desarrolladores** > **Configuración de API** <br>- **Buscar usuarios** se encuentra en **Usuarios** > **Búsqueda de usuarios**
{% endalert %}

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {YOUR_API_KEY}" -d '{
  "external_user_ids":["YOUR_EXTERNAL_USER_ID"],
  "messages": {
    "android_push": {
      "title":"Test push title",
      "alert":"Test push",
      "extra": {
        "YOUR_KEY1":"YOUR_VALUE1"
      }
    }  
  }
}' https://rest.iad-01.braze.com/messages/send
```

Este ejemplo utiliza la instancia `US-01`. Si no estás en esta instancia, sustituye el punto final `US-01` por [tu punto final]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/).

## Personalización de la visualización de notificaciones

### Paso 1: Crea tu fábrica de notificaciones personalizada

En algunos casos, es posible que desees personalizar las notificaciones push de formas que serían engorrosas o no estarían disponibles en el servidor. Para darte un control completo de la visualización de notificaciones, hemos añadido la posibilidad de definir tus propias [`IBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html) objetos de notificación para que los muestre Braze.

Si se configura un `IBrazeNotificationFactory` personalizado, Braze llamará al método `createNotification()` de tu fábrica tras la recepción push antes de que se muestre la notificación al usuario. Braze pasará un `Bundle` que contiene datos push de Braze y otro `Bundle` que contiene pares clave-valor personalizados enviados a través del panel o de las API de mensajería:

Braze pasará un archivo [`BrazeNotificationPayload`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.push/-braze-notification-payload/index.html) que contiene los datos de la notificación push de Braze.

{% tabs %}
{% tab JAVA %}

```java
// Factory method implemented in your custom IBrazeNotificationFactory
@Override
public Notification createNotification(BrazeNotificationPayload brazeNotificationPayload) {
  // Example of getting notification title
  String title = brazeNotificationPayload.getTitleText();

  // Example of retrieving a custom KVP ("my_key" -> "my_value")
  String customKvp = brazeNotificationPayload.getBrazeExtras().getString("my_key");
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
// Factory method implemented in your custom IBrazeNotificationFactory
override fun createNotification(brazeNotificationPayload: BrazeNotificationPayload): Notification {
  // Example of getting notification title
  val title = brazeNotificationPayload.getTitleText()

  // Example of retrieving a custom KVP ("my_key" -> "my_value")
  val customKvp = brazeNotificationPayload.getBrazeExtras().getString("my_key")
}
```

{% endtab %}
{% endtabs %}

Puedes devolver `null` desde tu método personalizado `createNotification()` para no mostrar la notificación en absoluto, utilizar `BrazeNotificationFactory.getInstance().createNotification()` para obtener nuestro objeto predeterminado `notification` para esos datos y modificarlo antes de mostrarlo, o generar un objeto `notification` completamente independiente para mostrarlo.

{% alert note %}
Para obtener documentación sobre las teclas de datos push de Braze, consulta el [SDK de Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-constants/index.html).
{% endalert %}

### Paso 2: Configura tu fábrica de notificaciones personalizada

Para indicar a Braze que utilice tu fábrica de notificaciones personalizada, utiliza el método `setCustomBrazeNotificationFactory` para configurar tus [`IBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html):

{% tabs %}
{% tab JAVA %}


```java
setCustomBrazeNotificationFactory(IBrazeNotificationFactory brazeNotificationFactory);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
setCustomBrazeNotificationFactory(brazeNotificationFactory: IBrazeNotificationFactory)
```

{% endtab %}
{% endtabs %}

El lugar recomendado para configurar tu `IBrazeNotificationFactory` personalizado es el método de ciclo de vida de la aplicación `Application.onCreate()` (no la actividad). Esto permitirá que la fábrica de notificaciones se configure correctamente siempre que el proceso de tu aplicación esté activo.

{% alert important %}
Crear tu propia notificación desde cero es un caso de uso avanzado y sólo debe hacerse con pruebas exhaustivas y un conocimiento profundo de la funcionalidad push de Braze. Por ejemplo, debes asegurarte de que tus registros de notificación push se abren correctamente.
{% endalert %}

Para desactivar tu sistema personalizado [`IBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html) y volver a la gestión predeterminada de Braze para push, pasa `null` a nuestro configurador de fábrica de notificaciones personalizadas:

{% tabs %}
{% tab JAVA %}


```java
setCustomBrazeNotificationFactory(null);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
setCustomBrazeNotificationFactory(null)
```

{% endtab %}
{% endtabs %}

## Push primers

Las campañas push primer animan a tus usuarios a habilitar las notificaciones push de tu aplicación en sus dispositivos. Esto puede hacerse sin necesidad de personalizar el SDK utilizando nuestro [primer push sin código]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/).

