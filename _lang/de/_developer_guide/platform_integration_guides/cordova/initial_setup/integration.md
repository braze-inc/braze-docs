---
nav_title: Integration
article_title: Einbindung des Cordova Braze SDK
page_order: 0
---

# Einbindung des Cordova Braze SDK

> Erfahren Sie, wie Sie das Cordova Braze-SDK in Ihre iOS- oder Android-App integrieren. Wenn Sie fertig sind, können Sie [das SDK weiter anpassen]({{site.baseurl}}/developer_guide/platform_integration_guides/cordova/initial_setup/customizations/).

## Einbinden des SDK

### Schritt 1: Fügen Sie das SDK zu Ihrem Projekt hinzu

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
Sie können jederzeit zwischen `master` und `geofence-branch` wechseln, indem Sie Schritt 1 wiederholen.
{% endalert %}

### Schritt 2: Konfigurieren Sie Ihr Projekt

Als nächstes fügen Sie die folgenden Einstellungen zum Element `platform` in der Datei `config.xml` Ihres Projekts hinzu.

{% tabs %}
{% tab ios %}
```xml
<preference name="com.braze.api_key" value="BRAZE_API_KEY" />
<preference name="com.braze.ios_api_endpoint" value="CUSTOM_API_ENDPOINT" />
```
{% endtab %}

{% tab android %}
```xml
<preference name="com.braze.api_key" value="BRAZE_API_KEY" />
<preference name="com.braze.android_api_endpoint" value="CUSTOM_API_ENDPOINT" />
```
{% endtab %}
{% endtabs %}

Ersetzen Sie Folgendes:

| Wert                 | Beschreibung                                                                                                                      |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------|
| `BRAZE_API_KEY`       | Ihr [Braze REST API-Schlüssel]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/#rest-api-keys).              |
| `CUSTOM_API_ENDPOINT` | Ein benutzerdefinierter API-Endpunkt. Dieser Endpunkt wird verwendet, um Ihre Braze-Instanzdaten an die richtige App-Gruppe in Ihrem Braze-Dashboard weiterzuleiten. |

Das Element `platform` in Ihrer Datei `config.xml` sollte etwa so aussehen wie das folgende:

{% tabs %}
{% tab ios %}
```xml
<platform name="ios">
    <preference name="com.braze.api_key" value="BRAZE_API_KEY" />
    <preference name="com.braze.ios_api_endpoint" value="sdk.fra-01.braze.eu" />
</platform>
```
{% endtab %}

{% tab android %}
```xml
<platform name="android">
    <preference name="com.braze.api_key" value="BRAZE_API_KEY" />
    <preference name="com.braze.android_api_endpoint" value="sdk.fra-01.braze.eu" />
</platform>
```
{% endtab %}
{% endtabs %}

## Deaktivieren des automatischen Sitzungs-Trackings (nur Android)

Standardmäßig verfolgt das Android Cordova Plugin Sitzungen automatisch. Um das automatische Sitzungs-Tracking zu deaktivieren, fügen Sie die folgende Einstellung zum Element `platform` in der Datei `config.xml` Ihres Projekts hinzu:

```xml
<platform name="android">
    <preference name="com.braze.android_disable_auto_session_tracking" value="true" />
</platform>
```

Um das Sitzungs-Tracking erneut zu starten, rufen Sie `BrazePlugin.startSessionTracking()` auf. Denken Sie daran, dass nur Sitzungen verfolgt werden, die nach der nächsten `Activity.onStart()` gestartet werden.
