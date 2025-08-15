---
nav_title: Push-Benachrichtigungen
article_title: Push-Benachrichtigungen für Flutter
platform: Flutter
page_order: 2
description: "Dieser Artikel behandelt die Implementierung und das Testen von Push-Benachrichtigungen in Flutter."
channel: push

---

# Integration von Push-Benachrichtigungen

> Dieser Referenzartikel beschreibt, wie Sie Push-Benachrichtigungen für Flutter einrichten. Für die Integration von Push-Benachrichtigungen muss jede native Plattform separat eingerichtet werden. Folgen Sie den jeweiligen Anleitungen, um die Installation abzuschließen.

## Schritt 1: Vervollständigen Sie die Ersteinrichtung

{% tabs %}
{% tab Android %}
### Schritt 1.1: Für Push registrieren

Registrieren Sie sich für Push mit der Firebase Cloud Messaging (FCM)-API von Google. Eine ausführliche Anleitung finden Sie in den folgenden Schritten der [Native Android Push Integration Anleitung]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/):

1. [Fügen Sie Firebase zu Ihrem Projekt hinzu]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-1-add-firebase-to-your-project).
2. [Fügen Sie Cloud Messaging zu Ihren Abhängigkeiten hinzu]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-2-add-cloud-messaging-to-your-dependencies).
3. [Erstellen Sie ein Dienstkonto]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-3-create-a-service-account).
4. [Generieren Sie JSON-Zugangsdaten]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-4-generate-json-credentials).
5. [Laden Sie Ihre JSON-Anmeldedaten auf Braze hoch]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-5-upload-your-json-credentials-to-braze).

### Schritt 1.2: Suchen Sie Ihre Google Sender ID

Gehen Sie zunächst zur Firebase-Konsole, öffnen Sie Ihr Projekt und wählen Sie dann <i class="fa-solid fa-gear"></i> **Einstellungen** > **Projekteinstellungen**.

![Das Firebase-Projekt mit geöffnetem Menü "Einstellungen".]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/select-project-settings.png %})

Wählen Sie **Cloud Messaging** und kopieren Sie dann unter **Firebase Cloud Messaging API (V1)** die **Absender-ID** in Ihre Zwischenablage.

![Die Seite "Cloud Messaging" des Firebase-Projekts mit hervorgehobener "Sender-ID".]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/copy-sender-id.png %})

### Schritt 1.3: Aktualisieren Sie Ihr `braze.xml`

Fügen Sie Folgendes zu Ihrer Datei `braze.xml` hinzu. Ersetzen Sie `FIREBASE_SENDER_ID` durch die Sender ID, die Sie zuvor kopiert haben.

```xml
<bool translatable="false" name="com_braze_firebase_cloud_messaging_registration_enabled">true</bool>
<string translatable="false" name="com_braze_firebase_cloud_messaging_sender_id">FIREBASE_SENDER_ID</string>
```

{% endtab %}

{% tab iOS %}
### Schritt 1.1: APNs-Zertifikate hochladen

Generieren Sie ein Apple Push Notification Service (APNs)-Zertifikat und laden Sie es in das Braze- Dashboard hoch. Eine vollständige Anleitung finden Sie unter [Hochladen Ihres APNs-Zertifikats]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-1-upload-your-apns-certificate).

### Schritt 1.2: Fügen Sie Ihrer App Unterstützung für Push-Benachrichtigungen hinzu

Folgen Sie der [Anleitung für die native iOS Integration]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/?tab=objective-c#automatic-push-integration).

{% endtab %}
{% endtabs %}

## Schritt 2: Achten Sie auf Push-Benachrichtigungen (optional)

Um auf Push-Benachrichtigungen zu warten, die Braze erkannt und verarbeitet hat, rufen Sie `subscribeToPushNotificationEvents()` auf und geben Sie ein Argument zur Ausführung an.

{% alert note %}
Die Push-Benachrichtigungen von Braze sind sowohl auf Android als auch auf iOS verfügbar. Aufgrund von Plattformunterschieden erkennt iOS Push-Ereignisse von Braze nur, wenn ein Nutzer:innen mit einer Push-Benachrichtigung interagiert hat.
{% endalert %}

```dart
// Create stream subscription
StreamSubscription pushEventsStreamSubscription;

pushEventsStreamSubscription = braze.subscribeToPushNotificationEvents((BrazePushEvent pushEvent) {
  print("Push Notification event of type ${pushEvent.payloadType} seen. Title ${pushEvent.title}\n and deeplink ${pushEvent.url}");
  // Handle push notification events
});

// Cancel stream subscription
pushEventsStreamSubscription.cancel();
```

#### Ereignisfelder für Push-Benachrichtigungen

{% alert note %}
Aufgrund von Plattformbeschränkungen unter iOS kann das Braze SDK Push-Payloads nur verarbeiten, wenn die App im Vordergrund ist. Listener werden unter iOS nur beim Ereignistyp `push_opened` getriggert, nachdem ein Nutzer mit einem Push interagiert hat.
{% endalert %}

Eine vollständige Liste der Felder für Push-Benachrichtigungen finden Sie in der unten stehenden Tabelle:

| Feldname         | Typ      | Beschreibung |
| ------------------ | --------- | ----------- |
| `payloadType`     | String    | Gibt den Nutzlasttyp der Benachrichtigung an. Die beiden Werte, die vom Braze Flutter SDK gesendet werden, sind `push_opened` und `push_received`.  Unter iOS werden nur `push_opened`-Events unterstützt. |
| `url`              | String    | Gibt die URL an, die durch die Benachrichtigung geöffnet wurde. |
| `useWebview`      | Boolesch   | Wenn Sie `true` wählen, wird die URL in der App in einer modalen Webansicht geöffnet. Wenn Sie `false` wählen, wird die URL im Browser des Geräts geöffnet. |
| `title`            | String    | Stellt den Titel der Benachrichtigung dar. |
| `body`             | String    | Stellt den Textkörper oder Inhalt der Benachrichtigung dar. |
| `summaryText`     | String    | Stellt den zusammenfassenden Text der Benachrichtigung dar. Dieser wird von `subtitle` unter iOS zugeordnet. |
| `badgeCount`      | Zahl   | Stellt die Anzahl der Ausweise in der Benachrichtigung dar. |
| `timestamp`        | Zahl | Stellt den Zeitpunkt dar, zu dem die Nutzdaten von der Anwendung empfangen wurden. |
| `isSilent`        | Boolesch   | Wenn Sie `true` auswählen, wird die Nutzlast still empfangen. Einzelheiten zum Senden von stillen Push-Benachrichtigungen unter Android finden Sie unter [Stille Push-Benachrichtigungen unter Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/silent_push_notifications). Einzelheiten zum Senden von stillen Push-Benachrichtigungen unter iOS finden Sie unter [Stille Push-Benachrichtigungen unter iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/). |
| `isBrazeInternal`| Boolesch   | Dies ist `true`, wenn eine Benachrichtigungsnutzlast für eine interne SDK-Funktion gesendet wurde, wie z. B. die Synchronisierung von Geofences, die Synchronisierung von Feature-Flags oder das Uninstall-Tracking. Die Nutzdaten werden für den Benutzer unbemerkt empfangen. |
| `imageUrl`        | String    | Gibt die URL an, die mit dem Benachrichtigungsbild verknüpft ist. |
| `brazeProperties` | Objekt    | Stellt die mit der Kampagne verbundenen Braze-Eigenschaften dar (Schlüssel-Wert-Paare). |
| `ios`              | Objekt    | Stellt iOS-spezifische Felder dar. |
| `android`          | Objekt    | Stellt Android-spezifische Felder dar. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Schritt 3: Test der Anzeige von Push-Benachrichtigungen

So testen Sie Ihre Integration, nachdem Sie Push-Benachrichtigungen in der nativen Schicht konfiguriert haben:

1. Legen Sie einen aktiven Nutzer:innen in der Flutter-Anwendung fest. Dazu initialisieren Sie das Plugin, indem Sie `braze.changeUser('your-user-id')` aufrufen.
2. Gehen Sie zu **Kampagnen** und erstellen Sie eine neue Push-Benachrichtigungskampagne. Wählen Sie die Plattformen, die Sie testen möchten.
3. Verfassen Sie Ihre Testbenachrichtigung und gehen Sie auf die Registerkarte **Test**. Fügen Sie die gleiche `user-id` wie der Testbenutzer hinzu und klicken Sie auf **Test senden**.
4. Sie sollten die Benachrichtigung in Kürze auf Ihrem Gerät erhalten. Wenn es nicht angezeigt wird, müssen Sie möglicherweise im Benachrichtigungscenter nachsehen oder die Einstellungen aktualisieren.

{% alert tip %}
Ab Xcode 14 können Sie Remote-Push-Benachrichtigungen auf einem iOS-Simulator testen.
{% endalert %}
