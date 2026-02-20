## Integración del SDK de Cordova

### Requisitos previos

Antes de empezar, comprueba que tu entorno es compatible con la [última versión del SDK de Braze Cordova](https://github.com/braze-inc/braze-cordova-sdk?tab=readme-ov-file#minimum-version-requirements).

### Paso 1: Añade el SDK a tu proyecto

{% alert warning %}
Añade sólo el SDK Braze Cordova utilizando los métodos que se indican a continuación. No intentes instalarlo utilizando otros métodos, ya que podrías provocar una violación de la seguridad.
{% endalert %}

Si utilizas Cordova 6 o posterior, puedes añadir el SDK directamente desde GitHub. También puedes descargar un ZIP del [repositorio de GitHub](https://github.com/braze-inc/braze-cordova-sdk) y añadir el SDK manualmente.

{% tabs local %}
{% tab geofence disabled %}
Si no piensas utilizar la recopilación de ubicaciones ni las geovallas, utiliza la rama `master` de GitHub.

```bash
cordova plugin add https://github.com/braze-inc/braze-cordova-sdk#master
```
{% endtab %}

{% tab geofence enabled %}
Si piensas utilizar la recopilación de ubicaciones y geovallas, utiliza la página `geofence-branch` de GitHub.

```bash
cordova plugin add https://github.com/braze-inc/braze-cordova-sdk#geofence-branch
```
{% endtab %}
{% endtabs %}

{% alert tip %}
Puedes cambiar entre `master` y `geofence-branch` en cualquier momento repitiendo este paso.
{% endalert %}

### Paso 2: Configura tu proyecto

A continuación, añade las siguientes preferencias al elemento `platform` del archivo `config.xml` de tu proyecto.

{% tabs %}
{% tab ios %}
```xml
<preference name="com.braze.ios_api_key" value="BRAZE_API_KEY" />
<preference name="com.braze.ios_api_endpoint" value="CUSTOM_API_ENDPOINT" />
```
{% endtab %}

{% tab android %}
```xml
<preference name="com.braze.android_api_key" value="BRAZE_API_KEY" />
<preference name="com.braze.android_api_endpoint" value="CUSTOM_API_ENDPOINT" />
```
{% endtab %}
{% endtabs %}

Sustituye lo siguiente:

| Valor                 | Descripción                                                                                                                      |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `BRAZE_API_KEY`       | Tu [clave de API REST de Braze]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/#rest-api-keys).              |
| `CUSTOM_API_ENDPOINT` | Un punto final de API personalizado. Este punto final se utiliza para dirigir los datos de tu instancia de Braze al grupo de aplicaciones correcto en tu panel de Braze. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

El elemento `platform` de tu archivo `config.xml` debe ser similar al siguiente:

{% tabs %}
{% tab ios %}
```xml
<platform name="ios">
    <preference name="com.braze.ios_api_key" value="BRAZE_API_KEY" />
    <preference name="com.braze.ios_api_endpoint" value="sdk.fra-01.braze.eu" />
</platform>
```
{% endtab %}

{% tab android %}
```xml
<platform name="android">
    <preference name="com.braze.android_api_key" value="BRAZE_API_KEY" />
    <preference name="com.braze.android_api_endpoint" value="sdk.fra-01.braze.eu" />
</platform>
```
{% endtab %}
{% endtabs %}

## Sintaxis específica de la plataforma

La siguiente sección cubre la sintaxis específica de la plataforma cuando se utiliza Cordova con iOS o Android.

### Enteros

{% tabs %}
{% tab ios %}
Las preferencias de enteros se leen como representaciones de cadenas, como en el siguiente ejemplo:

```xml
<platform name="ios">
    <preference name="com.braze.ios_flush_interval_seconds" value="10" />
    <preference name="com.braze.ios_session_timeout" value="5" />
</platform>
```
{% endtab %}

{% tab android %}
Debido a la forma en que el marco Cordova 8.0.0+ gestiona las preferencias, las preferencias de sólo números enteros (como los ID de remitente) deben establecerse en cadenas precedidas de `str_`, como en el siguiente ejemplo:

```xml
<platform name="android">
    <preference name="com.braze.android_fcm_sender_id" value="str_64422926741" />
    <preference name="com.braze.android_default_session_timeout" value="str_10" />
</platform>
```
{% endtab %}
{% endtabs %}

### Booleanos

{% tabs %}
{% tab ios %}
El SDK lee las preferencias booleanas utilizando las palabras clave `YES` y `NO` como representación de cadena, como en el siguiente ejemplo:

```xml
<platform name="ios">
    <preference name="com.braze.should_opt_in_when_push_authorized" value="YES" />
    <preference name="com.braze.ios_disable_automatic_push_handling" value="NO" />
</platform>
```
{% endtab %}

{% tab android %}
El SDK lee las preferencias booleanas utilizando las palabras clave `true` y `false` como representación de cadena, como en el siguiente ejemplo:

```xml
<platform name="android">
    <preference name="com.braze.should_opt_in_when_push_authorized" value="true" />
    <preference name="com.braze.is_session_start_based_timeout_enabled" value="false" />
</platform>
```
{% endtab %}
{% endtabs %}

## Configuraciones opcionales {#optional}

Puedes añadir cualquiera de las siguientes preferencias al elemento `platform` del archivo `config.xml` de tu proyecto:

{% tabs %}
{% tab ios %}
| Método Descripción
| ------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ios_api_key` | Establece la clave de API para tu aplicación.                                                                                                                                                                                                                |
| `ios_api_endpoint` | Establece el [punto final SDK]({{site.baseurl}}/api/basics/#endpoints) para tu aplicación.                                                                                                                                                                 |
| `ios_disable_automatic_push_registration` | Establece si se debe desactivar el registro push automático.                                                                                                                                                                                          |
| `ios_disable_automatic_push_handling` | Establece si se debe desactivar la gestión automática de push.                                                                                                                                                                                              |
| `ios_enable_idfa_automatic_collection` | Establece si el SDK de Braze debe recopilar automáticamente la información IDFA. Para más información, consulta [la documentación del método IDFA de Braze](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforadvertiser:)/). |
| `enable_location_collection` | Establece si se habilita la recogida automática de ubicaciones (si el usuario lo permite). El `geofence-branch` |
| `geofences_enabled` | Establece si las geovallas están habilitadas.                                                                                                                                                                                                                   |
| `ios_session_timeout` | Establece el tiempo de espera de la sesión Braze para tu aplicación en segundos. Predeterminado a 10 segundos.                                                                                                                                                               |
| `sdk_authentication_enabled` | Establece si se habilita la característica [de Autenticación SDK]({{site.baseurl}}/developer_guide/platform_wide/sdk_authentication#sdk-authentication).                                                                                              |
| `display_foreground_push_notifications` | Establece si las notificaciones push deben mostrarse mientras la aplicación está en primer plano.                                                                                                                                                       |
| `ios_disable_un_authorization_option_provisional` | Establece si `UNAuthorizationOptionProvisional` debe estar desactivado.                                                                                                                                                                                   |
| `trigger_action_minimum_time_interval_seconds` | Establece el intervalo de tiempo mínimo en segundos entre desencadenamientos. Predeterminado a 30 segundos.                                                                                                                                                                   |
| `ios_push_app_group` | Establece el ID del grupo de aplicaciones para las extensiones push de iOS.                                                                                                                                                                                                        |
| `ios_forward_universal_links` | Establece si el SDK debe reconocer y reenviar automáticamente los enlaces universales a los métodos del sistema.                                                                                                                                                     |
| `ios_log_level` | Establece el nivel mínimo de registro para `Braze.Configuration.Logger`.                                                                                                                                                                                      |
| `ios_use_uuid_as_device_id` | Establece si se debe utilizar un UUID generado aleatoriamente como ID del dispositivo.                                                                                                                                                                                    |
| `ios_flush_interval_seconds` | Establece el intervalo en segundos entre las descargas automáticas de datos. Predeterminado a 10 segundos.                                                                                                                                                                  |
| `ios_use_automatic_request_policy` | Establece si la política de solicitud de `Braze.Configuration.Api` debe ser automática o manual.                                                                                                                                                          |
| `should_opt_in_when_push_authorized` | Establece si el estado de suscripción a notificaciones de un usuario debe establecerse automáticamente en `optedIn` cuando se autorizan los permisos push.                                                                                                                       |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert tip %}
Para obtener información más detallada, consulta [GitHub: Plugin de Braze iOS Cordova](https://github.com/braze-inc/braze-cordova-sdk/blob/master/src/ios/BrazePlugin.m).
{% endalert %}
{% endtab %}

{% tab android %}
| Método Descripción
| ----------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `android_api_key` | Establece la clave de API para tu aplicación.                                                                                                                                                        |
| `android_api_endpoint` | Establece el [punto final SDK]({{site.baseurl}}/api/basics/#endpoints) para tu aplicación.                                                                                                         |
| `android_small_notification_icon` | Establece el icono pequeño de notificación.                                                                                                                                                             |
| `android_large_notification_icon` | Establece el icono grande de notificación.                                                                                                                                                             |
| `android_notification_accent_color` | Establece el color de acento de la notificación utilizando una representación hexadecimal.                                                                                                                        |
| `android_default_session_timeout` | Establece el tiempo de espera de la sesión Braze para tu aplicación en segundos. Predeterminado a 10 segundos.                                                                                                       |
| `android_handle_push_deep_links_automatically` | Establece si el SDK de Braze debe gestionar automáticamente los vínculos profundos push.                                                                                                                       |
| `android_log_level` | Establece el nivel de registro de tu aplicación. El nivel de registro predeterminado es 4 y registrará mínimamente la información. Para habilitar el registro detallado para la depuración, utiliza el nivel de registro 2\.                                    |
| `firebase_cloud_messaging_registration_enabled` | Establece si se utiliza la mensajería en la nube de Firebase para las notificaciones push.                                                                                                                          |
| `android_fcm_sender_id` | Establece el ID de remitente de Firebase Cloud Messaging.                                                                                                                                                  |
| `enable_location_collection` | Establece si se habilita la recogida automática de ubicaciones (si el usuario lo permite).                                                                                                              |
| `geofences_enabled` | Establece si las geovallas están habilitadas.                                                                                                                                                           |
| `android_disable_auto_session_tracking` | Desactiva el plugin Android Cordova para que no realice un seguimiento automático de las sesiones. Para más información, consulta [Desactivar el seguimiento automático de la sesión](#cordova_disable-automatic-session-tracking) |
| `sdk_authentication_enabled` | Establece si se habilita la característica [de Autenticación SDK]({{site.baseurl}}/developer_guide/platform_wide/sdk_authentication#sdk-authentication).                                      |
| `trigger_action_minimum_time_interval_seconds` | Establece el intervalo de tiempo mínimo en segundos entre desencadenamientos. Predeterminado a 30 segundos.                                                                                                           |
| `is_session_start_based_timeout_enabled` | Establece que el comportamiento del tiempo de espera de la sesión se base en eventos de inicio o fin de sesión.                                                                                          |
| `default_notification_channel_name` | Establece el nombre de cara al usuario visto a través de `NotificationChannel.getName` para el predeterminado de Braze `NotificationChannel`.                                                                              |
| `default_notification_channel_description` | Establece la descripción de cara al usuario vista a través de `NotificationChannel.getDescription` para el predeterminado de Braze `NotificationChannel`.                                                                |
| `does_push_story_dismiss_on_click` | Establece si una historia push se descarta automáticamente al hacer clic.                                                                                                                            |
| `is_fallback_firebase_messaging_service_enabled` | Establece si se habilita el uso de un servicio alternativo de mensajería en la nube Firebase.                                                                                                               |
| `fallback_firebase_messaging_service_classpath` | Establece la ruta de clase para el servicio de mensajería en la nube Firebase de alternativa.                                                                                                                         |
| `is_content_cards_unread_visual_indicator_enabled` | Establece si está habilitada la barra de indicación visual de tarjetas de contenido no leídas.                                                                                                                       |
| `is_firebase_messaging_service_on_new_token_registration_enabled` | Establece si el SDK de Braze registrará tokens automáticamente en `com.google.firebase.messaging.FirebaseMessagingService.onNewToken`.                                                         |
| `is_push_deep_link_back_stack_activity_enabled` | Establece si Braze añadirá una actividad a la pila posterior al seguir automáticamente los vínculos profundos para push.                                                                                   |
| `push_deep_link_back_stack_activity_class_name` | Establece la actividad que Braze añadirá a la pila posterior cuando siga automáticamente los vínculos en profundidad para push.                                                                                     |
| `should_opt_in_when_push_authorized` | Establece si Braze debe autorizar automáticamente la adhesión voluntaria del usuario cuando se autoriza push.                                                                                                                   |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert tip %}
Para obtener información más detallada, consulta [GitHub: Plugin Braze Android Cordova](https://github.com/braze-inc/braze-cordova-sdk/blob/master/src/android/BrazePlugin.kt).
{% endalert %}
{% endtab %}
{% endtabs %}

A continuación se muestra un archivo `config.xml` de ejemplo con configuraciones adicionales:

{% tabs %}
{% tab ios %}
```xml
<platform name="ios">
    <preference name="com.braze.ios_disable_automatic_push_registration" value="NO"/"YES" />
    <preference name="com.braze.ios_disable_automatic_push_handling" value="NO"/"YES" />
    <preference name="com.braze.ios_enable_idfa_automatic_collection" value="YES"/"NO" />
    <preference name="com.braze.enable_location_collection" value="NO"/"YES" />
    <preference name="com.braze.geofences_enabled" value="NO"/"YES" />
    <preference name="com.braze.ios_session_timeout" value="5" />
    <preference name="com.braze.sdk_authentication_enabled" value="YES"/"NO" />
    <preference name="com.braze.display_foreground_push_notifications" value="YES"/"NO" />
    <preference name="com.braze.ios_disable_un_authorization_option_provisional" value="NO"/"YES" />
    <preference name="com.braze.trigger_action_minimum_time_interval_seconds" value="30" />
    <preference name="com.braze.ios_push_app_group" value="PUSH_APP_GROUP_ID" />
    <preference name="com.braze.ios_forward_universal_links" value="YES"/"NO" />
    <preference name="com.braze.ios_log_level" value="2" />
    <preference name="com.braze.ios_use_uuid_as_device_id" value="YES"/"NO" />
    <preference name="com.braze.ios_flush_interval_seconds" value="10" />
    <preference name="com.braze.ios_use_automatic_request_policy" value="YES"/"NO" />
    <preference name="com.braze.should_opt_in_when_push_authorized" value="YES"/"NO" />
</platform>
```
{% endtab %}

{% tab android %}
```xml
<platform name="android">
    <preference name="com.braze.android_small_notification_icon" value="RESOURCE_ENTRY_NAME_FOR_ICON_DRAWABLE" />
    <preference name="com.braze.android_large_notification_icon" value="RESOURCE_ENTRY_NAME_FOR_ICON_DRAWABLE" />
    <preference name="com.braze.android_notification_accent_color" value="str_ACCENT_COLOR_INTEGER" />
    <preference name="com.braze.android_default_session_timeout" value="str_SESSION_TIMEOUT_INTEGER" />
    <preference name="com.braze.android_handle_push_deep_links_automatically" value="true"/"false" />
    <preference name="com.braze.android_log_level" value="str_LOG_LEVEL_INTEGER" />
    <preference name="com.braze.firebase_cloud_messaging_registration_enabled" value="true"/"false" />
    <preference name="com.braze.android_fcm_sender_id" value="str_YOUR_FCM_SENDER_ID" />
    <preference name="com.braze.enable_location_collection" value="true"/"false" />
    <preference name="com.braze.geofences_enabled" value="true"/"false" />
    <preference name="com.braze.android_disable_auto_session_tracking" value="true"/"false" />
    <preference name="com.braze.sdk_authentication_enabled" value="true"/"false" />
    <preference name="com.braze.trigger_action_minimum_time_interval_seconds" value="str_MINIMUM_INTERVAL_INTEGER" />
    <preference name="com.braze.is_session_start_based_timeout_enabled" value="false"/"true" />
    <preference name="com.braze.default_notification_channel_name" value="DEFAULT_NAME" />
    <preference name="com.braze.default_notification_channel_description" value="DEFAULT_DESCRIPTION" />
    <preference name="com.braze.does_push_story_dismiss_on_click" value="true"/"false" />
    <preference name="com.braze.is_fallback_firebase_messaging_service_enabled" value="true"/"false" />
    <preference name="com.braze.fallback_firebase_messaging_service_classpath" value="FALLBACK_FIREBASE_MESSAGING_CLASSPATH" />
    <preference name="com.braze.is_content_cards_unread_visual_indicator_enabled" value="true"/"false" />
    <preference name="com.braze.is_firebase_messaging_service_on_new_token_registration_enabled" value="true"/"false" />
    <preference name="com.braze.is_push_deep_link_back_stack_activity_enabled" value="true"/"false" />
    <preference name="com.braze.push_deep_link_back_stack_activity_class_name" value="DEEPLINK_BACKSTACK_ACTIVITY_CLASS_NAME" />
    <preference name="com.braze.should_opt_in_when_push_authorized" value="true"/"false" />
</platform>
```
{% endtab %}
{% endtabs %}

## Desactivar el seguimiento automático de la sesión (sólo Android) {#disable-automatic-session-tracking}

De manera predeterminada, el plugin de Android Cordova hace un seguimiento automático de las sesiones. Para desactivar el seguimiento automático de la sesión, añade la siguiente preferencia al elemento `platform` del archivo `config.xml` de tu proyecto:

```xml
<platform name="android">
    <preference name="com.braze.android_disable_auto_session_tracking" value="true" />
</platform>
```

Para volver a iniciar el seguimiento de las sesiones, llama a `BrazePlugin.startSessionTracking()`. Ten en cuenta que sólo se hará un seguimiento de las sesiones iniciadas después de la siguiente `Activity.onStart()`.
