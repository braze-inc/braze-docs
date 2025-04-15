---
nav_title: Personnalisations
article_title: Personnalisation du SDK Cordova Braze
page_order: 1
---

# Personnalisation du SDK Cordova Braze

> Voici les personnalisations disponibles pour le SDK Cordova Braze.

{% multi_lang_include cordova/prerequisites.md %}

## Options de personnalisation

Vous pouvez ajouter l'une des préférences suivantes à l'élément `platform` dans le fichier `config.xml` de votre projet :

{% tabs %}
{% tab ios %}
| Méthode                                         | Description                                                                                                                                            |
| -----------------------------------------------| -------------------------------------------------------------------------------------------------------------------------------------------------------|
| `api_key`                                      | Définit la clé API pour votre application. |
| `ios_api_endpoint`                             | Définit le [point de terminaison SDK]({{site.baseurl}}/api/basics/#endpoints) pour votre application. |
| `ios_disable_automatic_push_registration`      | Définit si l'enregistrement automatique des notifications push doit être désactivé. |
| `ios_disable_automatic_push_handling`          | Définit si la gestion automatique des pushs doit être désactivée. |
| `ios_enable_idfa_automatic_collection`         | Définit si le SDK Braze doit collecter automatiquement les informations IDFA. Pour plus d'informations, consultez la [documentation sur la méthode IDFA de Braze](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforadvertiser:)/). |
| `enable_location_collection`                   | Définit si la collecte automatique de localisation est activée (si l'utilisateur le permet). Le `geofence-branch`
| `geofences_enabled`                            | Définit si les géorepérages sont activés. |
| `ios_session_timeout`                          | Définit le délai d'expiration de la session Braze pour votre application en secondes. Par défaut, 10 secondes.
| `sdk_authentication_enabled`                   | Définit si la fonctionnalité [Authentification SDK](https://www.braze.com/docs/developer_guide/platform_wide/sdk_authentication#sdk-authentication) est activée. |
| `display_foreground_push_notifications`        | Définit si les notifications push doivent être affichées lorsque l'application est au premier plan. |
| `ios_disable_un_authorization_option_provisional` | Définit si `UNAuthorizationOptionProvisional` doit être désactivé. |
| `trigger_action_minimum_time_interval_seconds` | Définit l'intervalle de temps minimum en secondes entre les déclenchements. Par défaut, 30 secondes.
| `ios_push_app_group` | Définit l'ID de groupe d'application pour les extensions de notification iOS. |
| `ios_forward_universal_links` | Définit si le SDK doit automatiquement reconnaître et transmettre les liens universels aux méthodes système. |
| `ios_log_level` | Définit le niveau de journalisation minimum pour `Braze.Configuration.Logger`. |
| `ios_use_uuid_as_device_id` | Définit si un UUID généré aléatoirement doit être utilisé comme identifiant de l'appareil. |
| `ios_flush_interval_seconds` | Définit l'intervalle en secondes entre les vidages automatiques de données. Par défaut, 10 secondes.
| `ios_use_automatic_request_policy` | Définit si la politique de demande pour `Braze.Configuration.Api` doit être automatique ou manuelle. |
| `should_opt_in_when_push_authorized` | Définit si l'état d'abonnement aux notifications d'un utilisateur doit être automatiquement défini sur `optedIn` lorsque les autorisations de notification push sont autorisées.

{% alert tip %}
Pour plus d'informations détaillées, voir [GitHub : Plug-in Cordova iOS Braze](https://github.com/braze-inc/braze-cordova-sdk/blob/master/src/ios/BrazePlugin.m).
{% endalert %}
{% endtab %}

{% tab android %}
| Méthode                                         | Description                                                                                                                                            |
| -----------------------------------------------| -------------------------------------------------------------------------------------------------------------------------------------------------------|
| `api_key`                                      | Définit la clé API pour votre application. |
| `android_api_endpoint`                         | Définit le [point de terminaison SDK]({{site.baseurl}}/api/basics/#endpoints) pour votre application.
| `android_small_notification_icon`              | Définit l'icône de notification petite. |
| `android_large_notification_icon`              | Définit la grande icône de notification. |
| `android_notification_accent_color`            | Définit la couleur d'accentuation de la notification en utilisant une représentation hexadécimale. |
| `android_default_session_timeout`              | Définit le délai d'expiration de la session Braze pour votre application en secondes. Par défaut, 10 secondes.
| `android_handle_push_deep_links_automatically` | Définit si le SDK Braze doit gérer automatiquement les liens profonds des notifications push. |
| `android_log_level`                            | Définit le niveau de journalisation de votre application. Le niveau de journalisation par défaut est de 4 et va enregistrer le minimum d’informations. Pour activer la journalisation verbeuse pour le débogage, utilisez le niveau 2 de journalisation.. |
| `firebase_cloud_messaging_registration_enabled`| Définit si Firebase Cloud Messaging doit être utilisé pour les notifications push. |
| `android_fcm_sender_id`                        | Définit l'identifiant de l'expéditeur Firebase Cloud Messaging. |
| `enable_location_collection`                   | Définit si la collecte automatique de la localisation est activée (si l'utilisateur le permet). |
| `geofences_enabled`                            | Définit si les géorepérages sont activés. |
| `android_disable_auto_session_tracking`        | Définit si le plug-in Cordova Android doit désactiver le suivi automatique des sessions. |
| `sdk_authentication_enabled`                   | Définit si la fonctionnalité [Authentification SDK](https://www.braze.com/docs/developer_guide/platform_wide/sdk_authentication#sdk-authentication) est activée. |
| `trigger_action_minimum_time_interval_seconds` | Définit l'intervalle de temps minimum en secondes entre les déclenchements. Par défaut, 30 secondes.
| `is_session_start_based_timeout_enabled`       | Définit si le comportement de délai d'expiration de la session doit être basé soit sur le début de la session, soit sur les événements de fin de session. |
| `default_notification_channel_name`            | Définit le nom visible par l'utilisateur tel que vu via `NotificationChannel.getName` pour le `NotificationChannel` par défaut de Braze. |
| `default_notification_channel_description`     | Définit la description visible par l'utilisateur comme vu via `NotificationChannel.getDescription` pour le `NotificationChannel` par défaut de Braze. |
| `does_push_story_dismiss_on_click`             | Définit si une histoire Push est automatiquement rejetée lorsqu'elle est cliquée. |
`is_fallback_firebase_messaging_service_enabled`| Définit si l'utilisation d'un service Firebase Cloud Messaging de secours est activée. |
`fallback_firebase_messaging_service_classpath`| Définit le chemin de classe pour le service Firebase Cloud Messaging de secours. |
`is_content_cards_unread_visual_indicator_enabled`| Définit si la barre d'indication visuelle des cartes de contenu non lues est activée. |
`is_firebase_messaging_service_on_new_token_registration_enabled`| Définit si le SDK Braze enregistrera automatiquement les jetons dans `com.google.firebase.messaging.FirebaseMessagingService.onNewToken`. |
| `is_push_deep_link_back_stack_activity_enabled` | Définit si Braze ajoutera une activité à la pile arrière lors du suivi automatique des liens profonds pour les notifications push. |
`push_deep_link_back_stack_activity_class_name` Définit l'activité que Braze ajoutera à la pile arrière lors du suivi automatique des liens profonds pour les notifications push. |
| `should_opt_in_when_push_authorized` | Définit si Braze doit automatiquement inscrire l'utilisateur lorsque les notifications push sont autorisées. |

{% alert tip %}
Pour plus d'informations détaillées, voir [GitHub : Plug-in Cordova Braze Android](https://github.com/braze-inc/braze-cordova-sdk/blob/master/src/android/BrazePlugin.kt).
{% endalert %}
{% endtab %}
{% endtabs %}

Voici un exemple de fichier `config.xml` avec des configurations supplémentaires :

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

## Syntaxe spécifique à la plateforme

### Entiers

{% tabs %}
{% tab ios %}
Les préférences entières sont lues comme des représentations de chaînes, comme dans l'exemple suivant :

```xml
<platform name="ios">
    <preference name="com.braze.ios_flush_interval_seconds" value="10" />
    <preference name="com.braze.ios_session_timeout" value="5" />
</platform>
```
{% endtab %}

{% tab android %}
En raison de la manière dont le framework Cordova 8.0.0+ gère les préférences, les préférences de nombres entiers uniquement (comme les identifiants d'expéditeur) doivent être définies sur des chaînes de caractères précédées de `str_`, comme dans l'exemple suivant :

```xml
<platform name="android">
    <preference name="com.braze.android_fcm_sender_id" value="str_64422926741" />
    <preference name="com.braze.android_default_session_timeout" value="str_10" />
</platform>
```
{% endtab %}
{% endtabs %}

### Booléens

{% tabs %}
{% tab ios %}
Les préférences booléennes sont lues par le SDK en utilisant les mots-clés `YES` et `NO` comme une représentation sous forme de chaîne de caractères, comme dans l'exemple suivant :

```xml
<platform name="ios">
    <preference name="com.braze.should_opt_in_when_push_authorized" value="YES" />
    <preference name="com.braze.ios_disable_automatic_push_handling" value="NO" />
</platform>
```
{% endtab %}

{% tab android %}
Les préférences booléennes sont lues par le SDK en utilisant les mots-clés `true` et `false` comme une représentation sous forme de chaîne de caractères, comme dans l'exemple suivant :

```xml
<platform name="android">
    <preference name="com.braze.should_opt_in_when_push_authorized" value="true" />
    <preference name="com.braze.is_session_start_based_timeout_enabled" value="false" />
</platform>
```
{% endtab %}
{% endtabs %}
