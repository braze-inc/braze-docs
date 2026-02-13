## Intégration du SDK Cordova

### Conditions préalables

Avant de commencer, vérifiez que votre environnement est pris en charge par la [dernière version du SDK Braze Cordova](https://github.com/braze-inc/braze-cordova-sdk?tab=readme-ov-file#minimum-version-requirements).

### Étape 1 : Ajoutez le SDK à votre projet

{% alert warning %}
Ajoutez uniquement le SDK Braze Cordova à l'aide des méthodes ci-dessous. N'essayez pas d'effectuer l'installation en utilisant d'autres méthodes, car cela pourrait entraîner une violation de la sécurité.
{% endalert %}

Si vous utilisez Cordova 6 ou une version ultérieure, vous pouvez ajouter le SDK directement depuis GitHub. Vous pouvez également télécharger un ZIP du [référentiel GitHub](https://github.com/braze-inc/braze-cordova-sdk) et ajouter le SDK manuellement.

{% tabs local %}
{% tab geofence disabled %}
Si vous ne prévoyez pas d'utiliser la collecte des localisations et les géorepérages, utilisez la branche `master` de GitHub.

```bash
cordova plugin add https://github.com/braze-inc/braze-cordova-sdk#master
```
{% endtab %}

{% tab geofence enabled %}
Si vous prévoyez d'utiliser la collecte des localisations et les géorepérages, utilisez la `geofence-branch` de GitHub.

```bash
cordova plugin add https://github.com/braze-inc/braze-cordova-sdk#geofence-branch
```
{% endtab %}
{% endtabs %}

{% alert tip %}
Vous pouvez passer de `master` à `geofence-branch` à tout moment en répétant cette étape.
{% endalert %}

### Étape 2 : Configurez votre projet

Ensuite, ajoutez les préférences suivantes à l'élément `platform` dans le fichier `config.xml` de votre projet.

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

Remplacez les éléments suivants :

| Valeur                 | Description                                                                                                                      |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `BRAZE_API_KEY`       | Votre [clé API REST de Braze]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/#rest-api-keys).              |
| `CUSTOM_API_ENDPOINT` | Un endpoint d'API personnalisé. Cet endpoint est utilisé pour acheminer les données de votre instance Braze vers le groupe d'applications adéquat dans votre tableau de bord Braze. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

L'élément `platform` de votre fichier `config.xml` devrait ressembler à ce qui suit :

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

## Syntaxe spécifique à la plateforme

La section suivante couvre la syntaxe spécifique à la plateforme lorsque vous utilisez Cordova avec iOS ou Android.

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

## Configurations optionnelles {#optional}

Vous pouvez ajouter l'une des préférences suivantes à l'élément `platform` dans le fichier `config.xml` de votre projet :

{% tabs %}
{% tab ios %}
| Méthode d'évaluation de la qualité de l'eau et de l'air
| ------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ios_api_key` | Définit la clé API pour votre application.                                                                                                                                                                                                                |
| `ios_api_endpoint` | Définit le [point d'endpoint du SDK]({{site.baseurl}}/api/basics/#endpoints) pour votre application.                                                                                                                                                                 |
| `ios_disable_automatic_push_registration` | Définit si l'enregistrement automatique de la poussée doit être désactivé.                                                                                                                                                                                          |
| `ios_disable_automatic_push_handling` | Définit si la gestion automatique des poussées doit être désactivée.                                                                                                                                                                                              |
| `ios_enable_idfa_automatic_collection` | Définit si le SDK de Braze doit collecter automatiquement les informations IDFA. Pour plus d'informations, consultez [la documentation de la méthode IDFA de Braze](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforadvertiser:)/). |
| `enable_location_collection` | Définit si la collecte automatique d'emplacement/localisation est activée (si l'utilisateur le permet). Le site `geofence-branch` |
| `geofences_enabled` | Définit si les géorepérages sont activés.                                                                                                                                                                                                                   |
| `ios_session_timeout` | Définit le délai d'attente de la session Braze pour votre application en secondes. La valeur par défaut est de 10 secondes.                                                                                                                                                               |
| `sdk_authentication_enabled` | Permet d'activer ou non la fonctionnalité d'[authentification du SDK]({{site.baseurl}}/developer_guide/platform_wide/sdk_authentication#sdk-authentication).                                                                                              |
| `display_foreground_push_notifications` | Définit si les notifications push doivent être affichées lorsque l'application est au premier plan.                                                                                                                                                       |
| `ios_disable_un_authorization_option_provisional` | Définit si `UNAuthorizationOptionProvisional` doit être désactivé.                                                                                                                                                                                   |
| `trigger_action_minimum_time_interval_seconds` | Définit l'intervalle de temps minimum en secondes entre les déclencheurs. La valeur par défaut est de 30 secondes.                                                                                                                                                                   |
| `ios_push_app_group` | Définit l'ID du groupe d'applications pour les extensions push iOS.                                                                                                                                                                                                        |
| `ios_forward_universal_links` | Définit si le SDK doit reconnaître et transmettre automatiquement les liens universels aux méthodes du système.                                                                                                                                                     |
| `ios_log_level` | Définit le niveau minimum de journalisation pour `Braze.Configuration.Logger`.                                                                                                                                                                                      |
| `ios_use_uuid_as_device_id` | Définit si un UUID généré aléatoirement doit être utilisé comme ID de l'appareil.                                                                                                                                                                                    |
| `ios_flush_interval_seconds` | Définit l'intervalle en secondes entre les vidanges automatiques des données. La valeur par défaut est de 10 secondes.                                                                                                                                                                  |
| `ios_use_automatic_request_policy` | Définit si la politique de requête pour `Braze.Configuration.Api` doit être automatique ou manuelle.                                                                                                                                                          |
| `should_opt_in_when_push_authorized` | Définit si l'état de l'abonnement aux notifications d'un utilisateur doit être automatiquement défini sur `optedIn` lorsque les autorisations push sont autorisées.                                                                                                                       |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert tip %}
Pour plus d'informations détaillées, voir [GitHub : Plug-in Cordova iOS Braze](https://github.com/braze-inc/braze-cordova-sdk/blob/master/src/ios/BrazePlugin.m).
{% endalert %}
{% endtab %}

{% tab android %}
| Méthode d'évaluation de la qualité de l'eau et de l'air
| ----------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `android_api_key` | Définit la clé API pour votre application.                                                                                                                                                        |
| `android_api_endpoint` | Définit le [point d'endpoint du SDK]({{site.baseurl}}/api/basics/#endpoints) pour votre application.                                                                                                         |
| `android_small_notification_icon` | Définit la petite icône de notification.                                                                                                                                                             |
| `android_large_notification_icon` | Définit la grande icône de notification.                                                                                                                                                             |
| `android_notification_accent_color` | Définit la couleur d'accentuation de la notification à l'aide d'une représentation hexadécimale.                                                                                                                        |
| `android_default_session_timeout` | Définit le délai d'attente de la session Braze pour votre application en secondes. La valeur par défaut est de 10 secondes.                                                                                                       |
| `android_handle_push_deep_links_automatically` | Définit si le SDK de Braze doit gérer automatiquement les liens profonds de type "push".                                                                                                                       |
| `android_log_level` | Définit le niveau de journalisation pour votre application. Le niveau de journalisation par défaut est de 4 et va enregistrer le minimum d’informations. Pour activer la journalisation verbeuse pour le débogage, utilisez le niveau de journalisation 2\.                                    |
| `firebase_cloud_messaging_registration_enabled` | Définit s'il faut utiliser Firebase Cloud Messaging pour les notifications push.                                                                                                                          |
| `android_fcm_sender_id` | Définit l'ID de l'expéditeur de Firebase Cloud Messaging.                                                                                                                                                  |
| `enable_location_collection` | Définit si la collecte automatique d'emplacement/localisation est activée (si l'utilisateur le permet).                                                                                                              |
| `geofences_enabled` | Définit si les géorepérages sont activés.                                                                                                                                                           |
| `android_disable_auto_session_tracking` | Désactivez le plugin Android Cordova pour qu'il ne suive pas automatiquement les sessions. Pour plus d'informations, voir [Désactiver le suivi automatique des sessions](#cordova_disable-automatic-session-tracking).
| `sdk_authentication_enabled` | Permet d'activer ou non la fonctionnalité d'[authentification du SDK]({{site.baseurl}}/developer_guide/platform_wide/sdk_authentication#sdk-authentication).                                      |
| `trigger_action_minimum_time_interval_seconds` | Définit l'intervalle de temps minimum en secondes entre les déclencheurs. La valeur par défaut est de 30 secondes.                                                                                                           |
| `is_session_start_based_timeout_enabled` | Définit si le comportement du délai d'attente de la session doit être basé sur les événements de début ou de fin de session.                                                                                          |
| `default_notification_channel_name` | Définit le nom de l'utilisateur tel qu'il est vu via `NotificationChannel.getName` pour la valeur par défaut de Braze `NotificationChannel`.                                                                              |
| `default_notification_channel_description` | Définit la description destinée à l'utilisateur telle qu'elle est vue via `NotificationChannel.getDescription` pour la valeur par défaut de Braze `NotificationChannel`.                                                                |
| `does_push_story_dismiss_on_click` | Définit si un contenu push est automatiquement supprimé lorsqu'on clique dessus.                                                                                                                            |
| `is_fallback_firebase_messaging_service_enabled` | Définit si l'utilisation d'un service d'envoi messages Cloud Firebase de secours est activée.                                                                                                               |
| `fallback_firebase_messaging_service_classpath` | Définit le chemin d'accès pour le service d'envoi de messages Firebase Cloud de secours.                                                                                                                         |
| `is_content_cards_unread_visual_indicator_enabled` | Définit si la barre d'indication visuelle des cartes de contenu non lues est activée.                                                                                                                       |
| `is_firebase_messaging_service_on_new_token_registration_enabled` | Définit si le SDK de Braze enregistrera automatiquement les jetons dans `com.google.firebase.messaging.FirebaseMessagingService.onNewToken`.                                                         |
| `is_push_deep_link_back_stack_activity_enabled` | Définit si Braze ajoutera une activité à la pile arrière lors de la création automatique de liens profonds pour la poussée.                                                                                   |
| `push_deep_link_back_stack_activity_class_name` | Définit l'activité que Braze ajoutera à la pile arrière lors de la création automatique de liens profonds pour la poussée.                                                                                     |
| `should_opt_in_when_push_authorized` | Définit si Braze doit automatiquement procéder à l'abonnement de l'utilisateur lorsque le push est autorisé.                                                                                                                   |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

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

## Désactiver le suivi automatique des sessions (Android uniquement) {#disable-automatic-session-tracking}

Par défaut, le plugin Android Cordova assure automatiquement le suivi des sessions. Pour désactiver le suivi automatique des sessions, ajoutez la préférence suivante à l'élément `platform` du fichier `config.xml` de votre projet :

```xml
<platform name="android">
    <preference name="com.braze.android_disable_auto_session_tracking" value="true" />
</platform>
```

Pour recommencer à suivre les sessions, appelez `BrazePlugin.startSessionTracking()`. Gardez à l'esprit que seules les sessions commencées après le prochain `Activity.onStart()` seront suivies.
