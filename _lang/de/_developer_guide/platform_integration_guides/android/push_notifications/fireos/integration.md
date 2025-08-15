---
nav_title: Integration
article_title: Push-Integration für FireOS
platform: FireOS
page_order: 0
page_type: solution
description: "Dieser referenzierte Artikel zeigt Ihnen, wie Sie Push-Benachrichtigungen von Braze in Ihre FireOS-Anwendung integrieren können."
channel: push
search_rank: 0.9
---

# FireOS Push-Integration

> Dieser referenzierte Artikel zeigt Ihnen, wie Sie Push-Benachrichtigungen von Braze in Ihre FireOS-Anwendung integrieren können.

Eine Push-Benachrichtigung ist eine Benachrichtigung außerhalb der App, die auf dem Bildschirm des Nutzers erscheint, wenn ein wichtiges Update erfolgt. Push-Benachrichtigungen sind eine wertvolle Möglichkeit, Ihre Nutzer:innen mit zeitkritischen und relevanten Inhalten zu versorgen und sie wieder in Ihre App zu holen.

ADM (Amazon Device Messaging) wird auf Nicht-Amazon-Geräten nicht unterstützt. Um Kindle Push zu testen, müssen Sie ein [FireOS Gerät](https://developer.amazon.com/appsandservices/apis/engage/device-messaging/tech-docs/04-integrating-your-app-with-adm) besitzen. In unserem [Hilfeartikel]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/fireos/troubleshooting/) finden Sie weitere bewährte Verfahren.

Braze sendet Push-Benachrichtigungen an Amazon Geräte über [Amazon Device Messaging (ADM](https://developer.amazon.com/public/apis/engage/device-messaging)).

## Schritt 1: Enablement von ADM

1. Erstellen Sie ein Konto im [Amazon Apps & Games Entwickler:in Portal](https://developer.amazon.com/public), falls Sie dies noch nicht getan haben.
2. Suchen Sie die [OAuth-Zugangsdaten (Client-ID und Client-Geheimnis) und einen ADM API-Schlüssel](https://developer.amazon.com/public/apis/engage/device-messaging/tech-docs/02-obtaining-adm-credentials).
3. Aktivieren Sie **Automatische ADM-Registrierung aktiviert** im Unity Braze-Konfigurationsfenster. 
  - Alternativ können Sie auch die folgende Zeile in Ihre `res/values/braze.xml` Datei einfügen, um die ADM Registrierung zu aktivieren:

  ```xml
  <bool name="com_braze_push_adm_messaging_registration_enabled">true</bool>
  ```

## Schritt 2: AndroidManifest.xml aktualisieren

Fügen Sie in Ihrer App AndroidManifest.xml den Namespace von Amazon zum Tag `<>manifest</>` hinzu:

```xml
  xmlns:amazon="http://schemas.amazon.com/apk/res/android"
```

Als Nächstes deklarieren Sie die für die Unterstützung von ADM erforderlichen Berechtigungen, indem Sie die Elemente `<>permission</>` und `<>uses-permission</>` nach `<>manifest</> element` hinzufügen:

  ```xml
  <manifest xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:amazon="http://schemas.amazon.com/apk/res/android"
    package="[YOUR PACKAGE NAME]"
    android:versionCode="1"
    android:versionName="1.0">

  <!-- This permission verifies that no other application can intercept your ADM messages. -->
  <permission
    android:name="[YOUR PACKAGE NAME].permission.RECEIVE_ADM_MESSAGE"
    android:protectionLevel="signature" />
  <uses-permission android:name="[YOUR PACKAGE NAME].permission.RECEIVE_ADM_MESSAGE" />

   <!-- This permission allows your app access to receive push notifications from ADM. -->
  <uses-permission android:name="com.amazon.device.messaging.permission.RECEIVE" />

  <!-- ADM uses WAKE_LOCK to keep the processor from sleeping when a message is received. -->
  <uses-permission android:name="android.permission.WAKE_LOCK" />
    ...
  </manifest>
```

Als nächstes erklären Sie, dass Ihre App das Feature ADM des Geräts verwendet und dass Ihre App so konzipiert ist, dass sie auch ohne ADM auf dem Gerät funktioniert (`android:required="false"`), indem Sie dem Anwendungselement des Manifests ein `amazon:enable-feature` Element hinzufügen. Es ist sicher, `android:required` als `"false"` einzustellen, da sich der Code von Braze ADM sanft zurückentwickelt, wenn ADM nicht auf dem Gerät vorhanden ist:

  ```xml
  ...
  <application
    android:icon="@drawable/ic_launcher"
    android:label="@string/app_name"
    android:theme="@style/AppTheme">

    <amazon:enable-feature android:name="com.amazon.device.messaging" android:required="false"/>
  ...
  ```

Fügen Sie schließlich Filter für Absichten hinzu, um `REGISTRATION`- und `RECEIVE`\- Absichten von ADM in Ihrer `AndroidManifest.xml`-Datei von Braze zu behandeln. Unmittelbar nach `amazon:enable-feature` fügen Sie die folgenden Elemente hinzu:

```xml
    <receiver
      android:name="com.braze.push.BrazeAmazonDeviceMessagingReceiver"
      android:exported="true"
      android:permission="com.amazon.device.messaging.permission.SEND">
      <intent-filter>
        <action android:name="com.amazon.device.messaging.intent.RECEIVE" />
        <action android:name="com.amazon.device.messaging.intent.REGISTRATION" />

        <category android:name="${applicationId}" />
      </intent-filter>
    </receiver>
```

## Schritt 3: Speichern Sie Ihren ADM API-Schlüssel

Speichern Sie zunächst Ihren ADM API-Schlüssel in einer Datei mit dem Namen `api_key.txt` und speichern Sie diese im Ordner [`Assets/Plugins/Android/assets`][54] Ihres Projekts. Als Nächstes [fordern Sie einen ADM API-Schlüssel für Ihre App an](https://developer.amazon.com/public/apis/engage/device-messaging/tech-docs/02-obtaining-adm-credentials).

Amazon wird Ihren Schlüssel nicht erkennen, wenn `api_key.txt` Leerzeichen enthält, wie z.B. einen Zeilenumbruch am Ende.

## Schritt 4: Deeplinks hinzufügen

#### Enablement der automatischen Öffnung von Deeplinks

Um Braze zu ermöglichen, Ihre App und alle Deeplinks automatisch zu öffnen, wenn eine Push-Benachrichtigung angeklickt wird, setzen Sie `com_braze_handle_push_deep_links_automatically` auf `true` in Ihrem `braze.xml`:

```
<bool name="com_braze_handle_push_deep_links_automatically">true</bool>
```

Wenn Sie Deeplinks anpassen möchten, müssen Sie einen Push-Callback erstellen, der auf empfangene Push-Nachrichten und geöffnete Absichten von Braze wartet. Weitere Informationen finden Sie unter [Angepasste Handhabung von Push-Eingängen und Öffnungen]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#android-push-listener-callback) in der Android Push-Dokumentation.

## Schritt 5: Client-Geheimnis und Client-ID zum Braze-Dashboard hinzufügen

Schließlich müssen Sie das Client-Geheimnis und die Client-ID, die Sie in [Schritt 1](#step-1-enable-adm) erhalten haben, auf der Seite Einstellungen verwalten des Braze-Dashboards hinzufügen.

![]({% image_buster /assets/img_archive/fire_os_dashboard.png %})

## Manuelle Push-Registrierung

Braze empfiehlt die manuelle Registrierung nicht, aber wenn Sie die ADM-Registrierung selbst durchführen müssen, fügen Sie Folgendes in Ihre [braze.xml](https://developer.amazon.com/public/apis/engage/device-messaging/tech-docs/03-setting-up-adm) ein:

```xml
<!-- This will disable automatic registration for ADM via the Braze SDK-->
<bool name="com_braze_push_adm_messaging_registration_enabled">false</bool>
```
Als Nächstes verwenden Sie [`Braze.setRegisteredPushToken()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/registered-push-token.html), um die ADM-`registration_id` des oder der Nutzer:in an Braze zu übergeben:

{% tabs local %}
{% tab Java %}

```java
Braze.getInstance(context).setRegisteredPushToken(registration_id);
```

{% endtab %}
{% tab Kotlin %}

```kotlin
Braze.getInstance(context).registeredPushToken = registration_id
```

{% endtab %}
{% endtabs %}

## ADM-Extras

Nutzer:innen können angepasste Schlüssel-Wert-Paare mit einer Kindle Push Nachricht als `extras` für [Deeplinks]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/deep_linking/), Tracking URLs, etc. senden. Anders als bei Android Push können Nutzer:innen von Kindle Push keine reservierten Braze-Schlüssel als Schlüssel verwenden, wenn sie `extra` Schlüssel-Wert-Paare definieren.

Reservierte Schlüssel sind enthalten:

- `_ab`
- `a`
- `cid`
- `p`
- `s`
- `t`
- `ttl`
- `uri`

Wenn ein reservierter Kindle-Schlüssel erkannt wird, gibt Braze `Status Code 400: Kindle Push Reserved Key Used` zurück.

