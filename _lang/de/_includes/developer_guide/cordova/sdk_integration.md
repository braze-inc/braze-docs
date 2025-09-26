## Integration des Cordova SDK

### Voraussetzungen

Bevor Sie beginnen, überprüfen Sie, ob Ihre Umgebung von der [neuesten Braze Cordova SDK Version](https://github.com/braze-inc/braze-cordova-sdk?tab=readme-ov-file#minimum-version-requirements) unterstützt wird.

### Schritt 1: Fügen Sie das SDK zu Ihrem Projekt hinzu

{% alert warning %}
Fügen Sie das Braze Cordova SDK nur mit den unten aufgeführten Methoden hinzu. Versuchen Sie nicht, die Installation mit anderen Methoden durchzuführen, da dies zu einer Sicherheitsverletzung führen könnte.
{% endalert %}

Wenn Sie Cordova 6 oder höher verwenden, können Sie das SDK direkt von GitHub hinzufügen. Alternativ können Sie auch eine ZIP-Datei des [GitHub-Repositorys](https://github.com/braze-inc/braze-cordova-sdk) herunterladen und das SDK manuell hinzufügen.

{% tabs local %}
{% tab Geofence deaktiviert %}
Wenn Sie nicht vorhaben, Standorterfassung und Geofences zu nutzen, verwenden Sie den Branch `master` von GitHub.

```bash
cordova plugin add https://github.com/braze-inc/braze-cordova-sdk#master
```
{% endtab %}

{% tab Geofence aktiviert %}
Wenn Sie vorhaben, Standorterfassung und Geofences zu nutzen, verwenden Sie `geofence-branch` von GitHub.

```bash
cordova plugin add https://github.com/braze-inc/braze-cordova-sdk#geofence-branch
```
{% endtab %}
{% endtabs %}

{% alert tip %}
Sie können jederzeit zwischen `master` und `geofence-branch` wechseln, indem Sie diesen Schritt wiederholen.
{% endalert %}

### Schritt 2: Konfigurieren Sie Ihr Projekt

Als nächstes fügen Sie die folgenden Einstellungen zum Element `platform` in der Datei `config.xml` Ihres Projekts hinzu.

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

Ersetzen Sie Folgendes:

| Wert                 | Beschreibung                                                                                                                      |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `BRAZE_API_KEY`       | Ihr [Braze REST API-Schlüssel]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/#rest-api-keys).              |
| `CUSTOM_API_ENDPOINT` | Ein benutzerdefinierter API-Endpunkt. Dieser Endpunkt wird verwendet, um Ihre Braze-Instanzdaten an die richtige App-Gruppe in Ihrem Braze-Dashboard weiterzuleiten. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Das Element `platform` in Ihrer Datei `config.xml` sollte etwa so aussehen wie das folgende:

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

## Plattformspezifische Syntax

Der folgende Abschnitt behandelt die plattformspezifische Syntax bei der Verwendung von Cordova mit iOS oder Android.

### Ganze Zahlen

{% tabs %}
{% tab ios %}
Präferenzen mit ganzen Zahlen werden wie im folgenden Beispiel als String gelesen:

```xml
<platform name="ios">
    <preference name="com.braze.ios_flush_interval_seconds" value="10" />
    <preference name="com.braze.ios_session_timeout" value="5" />
</platform>
```
{% endtab %}

{% tab android %}
Aufgrund der Art und Weise, wie das Cordova 8.0.0+ Framework Präferenzen verarbeitet, müssen Präferenzen, die nur ganze Zahlen enthalten (z. B. Sender-IDs), wie im folgenden Beispiel als Strings mit vorangestelltem `str_` festgelegt werden:

```xml
<platform name="android">
    <preference name="com.braze.android_fcm_sender_id" value="str_64422926741" />
    <preference name="com.braze.android_default_session_timeout" value="str_10" />
</platform>
```
{% endtab %}
{% endtabs %}

### Boolesche Werte

{% tabs %}
{% tab ios %}
Boolesche Präferenzen werden vom SDK wie im folgenden Beispiel mit den Schlüsselwörtern `YES` und `NO` als String-Darstellung gelesen:

```xml
<platform name="ios">
    <preference name="com.braze.should_opt_in_when_push_authorized" value="YES" />
    <preference name="com.braze.ios_disable_automatic_push_handling" value="NO" />
</platform>
```
{% endtab %}

{% tab android %}
Boolesche Präferenzen werden vom SDK wie im folgenden Beispiel mit den Schlüsselwörtern `true` und `false` als String-Darstellung gelesen:

```xml
<platform name="android">
    <preference name="com.braze.should_opt_in_when_push_authorized" value="true" />
    <preference name="com.braze.is_session_start_based_timeout_enabled" value="false" />
</platform>
```
{% endtab %}
{% endtabs %}

## Optionale Konfigurationen {#optional}

Sie können jede der folgenden Einstellungen zum Element `platform` in der Datei `config.xml` Ihres Projekts hinzufügen:

{% tabs %}
{% tab ios %}
| Methode | Beschreibung |
| ------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ios_api_key` | Legt den API-Schlüssel für Ihre Anwendung fest.                                                                                                                                                                                                                |
| `ios_api_endpoint` | Legt den [SDK-Endpunkt]({{site.baseurl}}/api/basics/#endpoints) für Ihre Anwendung fest.                                                                                                                                                                 |
| `ios_disable_automatic_push_registration` | Legt fest, ob die automatische Push-Registrierung deaktiviert werden soll.                                                                                                                                                                                          |
| `ios_disable_automatic_push_handling` | Legt fest, ob die automatische Push-Behandlung deaktiviert werden soll.                                                                                                                                                                                              |
| `ios_enable_idfa_automatic_collection` | Legt fest, ob das Braze SDK automatisch die IDFA-Informationen sammeln soll. Weitere Informationen finden Sie in [der Dokumentation zur IDFA-Methode von Braze](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforadvertiser:)/). |
| `enable_location_collection` | Legt fest, ob die automatische Erfassung von Standorten aktiviert ist (sofern der Nutzer:innen dies zulässt). Die `geofence-branch` |
| `geofences_enabled` | Legt fest, ob Geofences aktiviert sind.                                                                                                                                                                                                                   |
| `ios_session_timeout` | Legt das Braze-Session-Timeout für Ihre Anwendung in Sekunden fest. Der Standardwert ist 10 Sekunden.                                                                                                                                                               |
| `sdk_authentication_enabled` | Legt fest, ob das [SDK Authentication]({{site.baseurl}}/developer_guide/platform_wide/sdk_authentication#sdk-authentication) Feature aktiviert werden soll.                                                                                              |
| `display_foreground_push_notifications` | Legt fest, ob Push-Benachrichtigungen angezeigt werden sollen, während sich die Anwendung im Vordergrund befindet.                                                                                                                                                       |
| `ios_disable_un_authorization_option_provisional` | Legt fest, ob `UNAuthorizationOptionProvisional` deaktiviert werden soll.                                                                                                                                                                                   |
| `trigger_action_minimum_time_interval_seconds` | Legt das minimale Zeitintervall in Sekunden zwischen Triggern fest. Der Standardwert ist 30 Sekunden.                                                                                                                                                                   |
| `ios_push_app_group` | Legt die ID der App-Gruppe für iOS-Push-Erweiterungen fest.                                                                                                                                                                                                        |
| `ios_forward_universal_links` | Legt fest, ob das SDK universelle Links automatisch erkennen und an die Systemmethoden weiterleiten soll.                                                                                                                                                     |
| `ios_log_level` | Legt die minimale Protokollierungsstufe für `Braze.Configuration.Logger` fest.                                                                                                                                                                                      |
| `ios_use_uuid_as_device_id` | Legt fest, ob eine zufällig generierte UUID als ID für das Gerät verwendet werden soll.                                                                                                                                                                                    |
| `ios_flush_interval_seconds` | Legt das Intervall in Sekunden zwischen automatischen Datenflushs fest. Der Standardwert ist 10 Sekunden.                                                                                                                                                                  |
| `ios_use_automatic_request_policy` | Legt fest, ob die Richtlinie für Anfragen an `Braze.Configuration.Api` automatisch oder manuell sein soll.                                                                                                                                                          |
| `should_opt_in_when_push_authorized` | Legt fest, ob der Status des Abos für die Push-Benachrichtigung eines Nutzers:in automatisch auf `optedIn` gesetzt werden soll, wenn die Push-Berechtigungen autorisiert werden.                                                                                                                       |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert tip %}
Ausführlichere Informationen finden Sie unter [GitHub: Braze iOS Cordova Plugin](https://github.com/braze-inc/braze-cordova-sdk/blob/master/src/ios/BrazePlugin.m).
{% endalert %}
{% endtab %}

{% tab android %}
| Methode | Beschreibung |
| ----------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `android_api_key` | Legt den API-Schlüssel für Ihre Anwendung fest.                                                                                                                                                        |
| `android_api_endpoint` | Legt den [SDK-Endpunkt]({{site.baseurl}}/api/basics/#endpoints) für Ihre Anwendung fest.                                                                                                         |
| `android_small_notification_icon` | Legt das kleine Benachrichtigungssymbol fest.                                                                                                                                                             |
| `android_large_notification_icon` | Legt das große Symbol für Benachrichtigungen fest.                                                                                                                                                             |
| `android_notification_accent_color` | Legt die Akzentfarbe der Benachrichtigung in hexadezimaler Darstellung fest.                                                                                                                        |
| `android_default_session_timeout` | Legt das Braze-Session-Timeout für Ihre Anwendung in Sekunden fest. Der Standardwert ist 10 Sekunden.                                                                                                       |
| `android_handle_push_deep_links_automatically` | Legt fest, ob das Braze SDK Push Deeplinks automatisch verarbeiten soll.                                                                                                                       |
| `android_log_level` | Legt die Protokollstufe für Ihre Anwendung fest. Die Standard-Protokollstufe ist 4\. Sie protokolliert nur minimale Informationen. Um die ausführliche Protokollierung für die Fehlersuche zu aktivieren, verwenden Sie die Protokollstufe 2\.                                    |
| `firebase_cloud_messaging_registration_enabled` | Legt fest, ob Firebase Cloud Messaging für Push-Benachrichtigungen verwendet werden soll.                                                                                                                          |
| `android_fcm_sender_id` | Legt die Firebase Cloud Messaging ID des Senders fest.                                                                                                                                                  |
| `enable_location_collection` | Legt fest, ob die automatische Erfassung von Standorten Enablement ist (wenn der Nutzer:in erlaubt).                                                                                                              |
| `geofences_enabled` | Legt fest, ob Geofences aktiviert sind.                                                                                                                                                           |
| `android_disable_auto_session_tracking` | Deaktivieren Sie das Android Cordova Plugin für das automatische Tracking von Sitzungen. Weitere Informationen finden Sie unter [Deaktivieren des automatischen Session Tracking](#cordova_disable-automatic-session-tracking) |
| `sdk_authentication_enabled` | Legt fest, ob das [SDK Authentication]({{site.baseurl}}/developer_guide/platform_wide/sdk_authentication#sdk-authentication) Feature aktiviert werden soll.                                      |
| `trigger_action_minimum_time_interval_seconds` | Legt das minimale Zeitintervall in Sekunden zwischen Triggern fest. Der Standardwert ist 30 Sekunden.                                                                                                           |
| `is_session_start_based_timeout_enabled` | Legt fest, ob der Sitzungs-Timeout entweder auf Sitzungsstart- oder Sitzungsend-Ereignissen basieren soll.                                                                                          |
| `default_notification_channel_name` | Legt den Namen des Nutzers:innen fest, wie er über `NotificationChannel.getName` für den Braze-Standard `NotificationChannel` zu sehen ist.                                                                              |
| `default_notification_channel_description` | Legt die Nutzer:innen-Beschreibung fest, wie sie über `NotificationChannel.getDescription` für den Braze-Standard `NotificationChannel` zu sehen ist.                                                                |
| `does_push_story_dismiss_on_click` | Legt fest, ob eine Push-Story beim Klicken automatisch beendet wird.                                                                                                                            |
| `is_fallback_firebase_messaging_service_enabled` | Legt fest, ob die Verwendung eines Fallback Firebase Cloud Messaging Dienstes aktiviert ist.                                                                                                               |
| `fallback_firebase_messaging_service_classpath` | Legt den Klassenpfad für den Fallback Firebase Cloud Messaging Dienst fest.                                                                                                                         |
| `is_content_cards_unread_visual_indicator_enabled` | Legt fest, ob die visuelle Anzeigeleiste für ungelesene Content-Cards aktiviert ist.                                                                                                                       |
| `is_firebase_messaging_service_on_new_token_registration_enabled` | Legt fest, ob das Braze SDK Token automatisch in `com.google.firebase.messaging.FirebaseMessagingService.onNewToken` registrieren soll.                                                         |
| `is_push_deep_link_back_stack_activity_enabled` | Legt fest, ob Braze eine Aktivität zum Back Stack hinzufügt, wenn es automatisch Deeplinks für Push folgt.                                                                                   |
| `push_deep_link_back_stack_activity_class_name` | Legt die Aktivität fest, die Braze zum Back Stack hinzufügt, wenn es automatisch Deeplinks für Push folgt.                                                                                     |
| `should_opt_in_when_push_authorized` | Legt fest, ob Braze bei der Autorisierung von Push automatisch ein Opt-in für den Nutzer:innen durchführen soll.                                                                                                                   |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert tip %}
Ausführlichere Informationen finden Sie unter [GitHub: Braze Android Cordova Plugin](https://github.com/braze-inc/braze-cordova-sdk/blob/master/src/android/BrazePlugin.kt).
{% endalert %}
{% endtab %}
{% endtabs %}

Im Folgenden finden Sie ein Beispiel für eine `config.xml` Datei mit zusätzlichen Konfigurationen:

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

## Deaktivieren des automatischen Session Tracking (nur Android) {#disable-automatic-session-tracking}

Standardmäßig verfolgt das Android Cordova Plugin Sitzungen automatisch. Um das automatische Sitzungs-Tracking zu deaktivieren, fügen Sie die folgende Einstellung zum Element `platform` in der Datei `config.xml` Ihres Projekts hinzu:

```xml
<platform name="android">
    <preference name="com.braze.android_disable_auto_session_tracking" value="true" />
</platform>
```

Um das Sitzungs-Tracking erneut zu starten, rufen Sie `BrazePlugin.startSessionTracking()` auf. Denken Sie daran, dass nur Sitzungen verfolgt werden, die nach der nächsten `Activity.onStart()` gestartet werden.
