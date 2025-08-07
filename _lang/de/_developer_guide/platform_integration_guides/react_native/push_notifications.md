---
nav_title: Push-Benachrichtigungen
article_title: Push-Benachrichtigungen für React Native
platform: React Native
page_order: 2
toc_headers: h2
description: "Dieser Artikel behandelt die Implementierung von Push-Benachrichtigungen in React Native."
channel: push

---

# Integration von Push-Benachrichtigungen

> Dieser Referenzartikel beschreibt, wie Sie Push-Benachrichtigungen für React Native einrichten. Für die Integration von Push-Benachrichtigungen muss jede native Plattform separat eingerichtet werden. Folgen Sie den jeweiligen Anleitungen, um die Installation abzuschließen.

## Schritt 1: Vervollständigen Sie die Ersteinrichtung

{% tabs %}
{% tab Expo %}
Legen Sie die Optionen `enableBrazeIosPush` und `enableFirebaseCloudMessaging` in der Datei `app.json` fest, um Push für iOS bzw. Android zu aktivieren. Weitere Einzelheiten finden Sie in der Konfigurationsanleitung [hier]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/react_sdk_setup/#step-2-complete-native-setup).

Beachten Sie, dass Sie diese Einstellungen anstelle der nativen Einrichtungsanweisungen verwenden müssen, wenn Sie auf zusätzliche Push-Benachrichtigungsbibliotheken wie [Expo Notifications](https://docs.expo.dev/versions/latest/sdk/notifications/) angewiesen sind.
{% endtab %}

{% tab Android %}
### Schritt 1.1: Für Push registrieren

Registrieren Sie sich für Push mit der Firebase Cloud Messaging (FCM)-API von Google. Eine ausführliche Anleitung finden Sie in den folgenden Schritten der [Native Android Push Integration Anleitung]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/):

1. [Fügen Sie Firebase zu Ihrem Projekt hinzu]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-1-add-firebase-to-your-project).
2. [Fügen Sie Cloud Messaging zu Ihren Abhängigkeiten hinzu]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-2-add-cloud-messaging-to-your-dependencies).
3. [Erstellen Sie ein Dienstkonto]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-3-create-a-service-account).
4. [Generieren Sie JSON-Zugangsdaten]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-4-generate-json-credentials).
5. [Laden Sie Ihre JSON-Anmeldedaten auf Braze hoch]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-5-upload-your-json-credentials-to-braze).

### Schritt 1.2: Fügen Sie Ihre Google Absender-ID hinzu

Gehen Sie zunächst zur Firebase-Konsole, öffnen Sie Ihr Projekt und wählen Sie dann <i class="fa-solid fa-gear"></i> **Einstellungen** > **Projekteinstellungen**.

![Das Firebase-Projekt mit geöffnetem Menü "Einstellungen".]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/select-project-settings.png %})

Wählen Sie **Cloud Messaging** und kopieren Sie dann unter **Firebase Cloud Messaging API (V1)** die **Absender-ID** in Ihre Zwischenablage.

![Die Seite "Cloud Messaging" des Firebase-Projekts mit hervorgehobener "Sender-ID".]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/copy-sender-id.png %})

Als nächstes öffnen Sie die Datei `app.json` Ihres Projekts und setzen die Eigenschaft `firebaseCloudMessagingSenderId` auf die Absender-ID in Ihrer Zwischenablage. Zum Beispiel:

```
"firebaseCloudMessagingSenderId": "693679403398"
```

### Schritt 1.3: Fügen Sie den Pfad zu Ihrem Google Services JSON hinzu

Fügen Sie in der Datei `app.json` Ihres Projekts den Pfad zu Ihrer Datei `google-services.json` hinzu. Diese Datei wird benötigt, wenn Sie `enableFirebaseCloudMessaging: true` in Ihrer Konfiguration festlegen.

```json
{
  "expo": {
    "android": {
      "googleServicesFile": "PATH_TO_GOOGLE_SERVICES"
    },
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          "androidApiKey": "YOUR-ANDROID-API-KEY",
          "iosApiKey": "YOUR-IOS-API-KEY",
          "enableBrazeIosPush": true,
          "enableFirebaseCloudMessaging": true,
          "firebaseCloudMessagingSenderId": "YOUR-FCM-SENDER-ID",
          "androidHandlePushDeepLinksAutomatically": true
        }
      ],
    ]
  }
}
```
{% endtab %}

{% tab iOS %}
### Schritt 1.1: APNs-Zertifikate hochladen

Generieren Sie ein Apple Push Notification Service (APNs)-Zertifikat und laden Sie es in das Braze- Dashboard hoch. Eine vollständige Anleitung finden Sie unter [Hochladen Ihres APNs-Zertifikats]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-1-upload-your-apns-certificate).

### Schritt 1.2: Wählen Sie eine Integrationsmethode

Wenn Sie nicht vorhaben, beim Starten der App Push-Berechtigungen anzufordern, lassen Sie den Aufruf `requestAuthorizationWithOptions:completionHandler:` in Ihrem AppDelegate weg und fahren Sie mit [Schritt 2](#step-2-request-push-notifications-permission) fort. Andernfalls folgen Sie der [nativen iOS-Integrationsanleitung]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/?tab=objective-c#automatic-push-integration).

Wenn Sie fertig sind, fahren Sie mit [Schritt 1.3](#step-13-migrate-your-push-key) fort.

### Schritt 1.3: Push-Schlüssel migrieren

Wenn Sie zuvor `expo-notifications` zur Verwaltung Ihres Push-Schlüssels verwendet haben, führen Sie `expo fetch:ios:certs` aus dem Stammordner Ihrer Anwendung aus. Dadurch wird Ihr Push-Schlüssel (eine .p8-Datei) heruntergeladen, die Sie dann auf das Braze-Dashboard hochladen können.
{% endtab %}
{% endtabs %}

## Schritt 2: Genehmigung für Push-Benachrichtigungen anfordern

Verwenden Sie die Methode `Braze.requestPushPermission()` (verfügbar ab v1.38.0), um die Berechtigung für Push-Benachrichtigungen von iOS- und Android 13+-Nutzern anzufordern. Bei Android 12 und früheren Versionen ist diese Methode nicht anwendbar.

Diese Methode nimmt einen erforderlichen Parameter auf, der angibt, welche Berechtigungen das SDK vom iOS-Nutzer anfordern soll. Diese Optionen haben keine Auswirkungen auf Android.

```javascript
const permissionOptions = {
  alert: true,
  sound: true,
  badge: true,
  provisional: false
};

Braze.requestPushPermission(permissionOptions);
```

### Schritt 2.1: Auf Push-Benachrichtigungen warten (optional)

Sie können zusätzlich Ereignisse abonnieren, bei denen Braze eine eingehende Push-Benachrichtigung erkannt und verarbeitet hat. Verwenden Sie den Listener-Schlüssel `Braze.Events.PUSH_NOTIFICATION_EVENT`.

{% alert important %}
Empfangene iOS-Push-Events werden nur für Benachrichtigungen im Vordergrund sowie für Benachrichtigungen im Hintergrund mit `content-available` getriggert. Für Benachrichtigungen, die während der Beendigung empfangen werden, oder für Benachrichtigungen im Hintergrund ohne das Feld `content-available` werden sie nicht getriggert.
{% endalert %}

```javascript
Braze.addListener(Braze.Events.PUSH_NOTIFICATION_EVENT, data => {
  console.log(`Push Notification event of type ${data.payload_type} seen. Title ${data.title}\n and deeplink ${data.url}`);
  console.log(JSON.stringify(data, undefined, 2));
});
```

#### Ereignisfelder für Push-Benachrichtigungen

Eine vollständige Liste der Felder für Push-Benachrichtigungen finden Sie in der unten stehenden Tabelle:

| Feldname         | Typ      | Beschreibung |
| ------------------ | --------- | ----------- |
| `payload_type`     | String    | Gibt den Nutzlasttyp der Benachrichtigung an. Die beiden Werte, die vom Braze React Native-SDK gesendet werden, sind `push_opened` und `push_received`. |
| `url`              | String    | Gibt die URL an, die durch die Benachrichtigung geöffnet wurde. |
| `use_webview`      | Boolesch   | Wenn Sie `true` wählen, wird die URL in der App in einer modalen Webansicht geöffnet. Wenn Sie `false` wählen, wird die URL im Browser des Geräts geöffnet. |
| `title`            | String    | Stellt den Titel der Benachrichtigung dar. |
| `body`             | String    | Stellt den Textkörper oder Inhalt der Benachrichtigung dar. |
| `summary_text`     | String    | Stellt den zusammenfassenden Text der Benachrichtigung dar. Dieser wird von `subtitle` unter iOS zugeordnet. |
| `badge_count`      | Zahl   | Stellt die Anzahl der Ausweise in der Benachrichtigung dar. |
| `timestamp`        | Zahl | Stellt den Zeitpunkt dar, zu dem die Nutzdaten von der Anwendung empfangen wurden. |
| `is_silent`        | Boolesch   | Wenn Sie `true` auswählen, wird die Nutzlast still empfangen. Einzelheiten zum Senden von stillen Push-Benachrichtigungen unter Android finden Sie unter [Stille Push-Benachrichtigungen unter Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/silent_push_notifications). Einzelheiten zum Senden von stillen Push-Benachrichtigungen unter iOS finden Sie unter [Stille Push-Benachrichtigungen unter iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/). |
| `is_braze_internal`| Boolesch   | Dies ist `true`, wenn eine Benachrichtigungsnutzlast für eine interne SDK-Funktion gesendet wurde, wie z. B. die Synchronisierung von Geofences, die Synchronisierung von Feature-Flags oder das Uninstall-Tracking. Die Nutzdaten werden für den Benutzer unbemerkt empfangen. |
| `image_url`        | String    | Gibt die URL an, die mit dem Benachrichtigungsbild verknüpft ist. |
| `braze_properties` | Objekt    | Stellt die mit der Kampagne verbundenen Braze-Eigenschaften dar (Schlüssel-Wert-Paare). |
| `ios`              | Objekt    | Stellt iOS-spezifische Felder dar. |
| `android`          | Objekt    | Stellt Android-spezifische Felder dar. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Schritt 3: Deeplinking aktivieren (optional)

Damit Braze Deeplinks innerhalb von React-Komponenten verarbeiten kann, wenn auf eine Push-Benachrichtigung geklickt wird, führen Sie die zusätzlichen Schritte aus.

{% tabs %}
{% tab Expo %}
Unsere [BrazeProject-Beispielanwendung](https://github.com/braze-inc/braze-react-native-sdk/tree/master/BrazeProject) enthält ein vollständiges Beispiel für implementierte Deep Links. Weitere Informationen zu Deeplinks finden Sie in unserem [FAQ-Artikel]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking).

{% endtab %}
{% tab Android %}
Für Android ist die Einrichtung von Deep Links identisch mit der [Einrichtung von Deep Links in nativen Android-Apps]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration#step-4-add-deep-links). Wenn Push-Deeplinks automatisch vom Braze-SDK verarbeitet werden sollen, legen Sie `androidHandlePushDeepLinksAutomatically: true` in der `app.json` fest.

{% endtab %}
{% tab iOS %}
### Schritt 3.1: Deeplinking-Funktionen hinzufügen

Fügen Sie für iOS `populateInitialUrlFromLaunchOptions` zur Methode `didFinishLaunchingWithOptions` des AppDelegate hinzu. Zum Beispiel:

```objc
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
  self.moduleName = @"BrazeProject";
  self.initialProps = @{};

  BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:apiKey endpoint:endpoint];
  configuration.triggerMinimumTimeInterval = 1;
  configuration.logger.level = BRZLoggerLevelInfo;
  Braze *braze = [BrazeReactBridge initBraze:configuration];
  AppDelegate.braze = braze;

  [self registerForPushNotifications];
  [[BrazeReactUtils sharedInstance] populateInitialUrlFromLaunchOptions:launchOptions];

  return [super application:application didFinishLaunchingWithOptions:launchOptions];
}
```

### Schritt 3.2: Verarbeitung von Deep Links konfigurieren

Verwenden Sie die Methode `Linking.getInitialURL()` für Deeplinks, die Ihre App öffnen, und die Methode `Braze.getInitialURL` für Deeplinks in Push-Benachrichtigungen, die Ihre App öffnen, wenn sie nicht ausgeführt wird. Zum Beispiel:

```javascript
Linking.getInitialURL()
  .then(url => {
    if (url) {
      console.log('Linking.getInitialURL is ' + url);
      showToast('Linking.getInitialURL is ' + url);
      handleOpenUrl({ url });
    }
  })
  .catch(err => console.error('Error getting initial URL', err));

// Handles deep links when an iOS app is launched from a hard close via push click.
Braze.getInitialURL(url => {
  if (url) {
    console.log('Braze.getInitialURL is ' + url);
    showToast('Braze.getInitialURL is ' + url);
    handleOpenUrl({ url });
  }
});
```
{% alert note %}
Braze bietet diese Problemumgehung an, da die Linking-API von React Native dieses Szenario aufgrund einer Race-Condition beim Starten der App nicht unterstützt.
{% endalert %}
{% endtab %}
{% endtabs %}

## Schritt 4: Test der Anzeige von Push-Benachrichtigungen

Sie sollten nun in der Lage sein, Benachrichtigungen an die Geräte zu senden. Führen Sie die folgenden Schritte durch, um Ihre Push-Integration zu testen.

{% alert note %}
Ab macOS 13 können Sie auf bestimmten Geräten iOS Push-Benachrichtigungen mithilfe eines Simulators für iOS 16+ testen, der unter Xcode 14 oder höher läuft. Weitere Einzelheiten finden Sie in den [Release Notes zu Xcode 14](https://developer.apple.com/documentation/xcode-release-notes/xcode-14-release-notes).
{% endalert %}

1. Legen Sie einen aktiven Nutzer in der React-Anwendung fest, indem Sie die Methode `Braze.changeUserId('your-user-id')` aufrufen.
2. Gehen Sie zu **Kampagnen** und erstellen Sie eine neue Push-Benachrichtigungskampagne. Wählen Sie die Plattformen, die Sie testen möchten.
3. Verfassen Sie Ihre Testbenachrichtigung und gehen Sie auf die Registerkarte **Test**. Fügen Sie die gleiche `user-id` wie der Testbenutzer hinzu und klicken Sie auf **Test senden**. Sie sollten die Benachrichtigung in Kürze auf Ihrem Gerät erhalten.

![Eine Push-Kampagne von Braze, bei der Sie Ihre eigene Benutzer-ID als Testempfänger hinzufügen können, um Ihre Push-Benachrichtigung zu testen.]({% image_buster /assets/img/react-native/push-notification-test.png %} "Push Campaign Test")

## Weiterleitung von Android Push an zusätzliche FMS

Wenn Sie einen zusätzlichen Firebase Messaging Service (FMS) verwenden möchten, können Sie einen Fallback-FMS angeben, der aufgerufen wird, wenn Ihre Anwendung einen Push erhält, der nicht von Braze stammt. Zum Beispiel:

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          ...
          "androidFirebaseMessagingFallbackServiceEnabled": true,
          "androidFirebaseMessagingFallbackServiceClasspath": "com.company.OurFirebaseMessagingService"
        }
      ]
    ]
  }
}
```

## Konfigurieren von App-Erweiterungen mit Expo

### Aktivieren von umfangreichen Push-Benachrichtigungen für iOS

{% alert tip %}
Rich-Push-Benachrichtigungen sind für Android standardmäßig verfügbar.
{% endalert %}

Um Rich-Push-Benachrichtigungen unter iOS mit Expo zu aktivieren, legen Sie die Eigenschaft `enableBrazeIosRichPush` im Objekt `expo.plugins`der `app.json` auf `true` fest:

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          ...
          "enableBrazeIosRichPush": true
        }
      ]
    ]
  }
}
```

Fügen Sie dann den Bundle-Bezeichner für diese App-Erweiterung zur Konfiguration der Zugangsdaten Ihres Projekts hinzu: `<your-app-bundle-id>.BrazeExpoRichPush`. Weitere Einzelheiten zu diesem Vorgang finden Sie unter [Verwendung von App-Erweiterungen mit Expo Application Services](#app-extensions).

### Aktivieren von Push Stories für iOS

{% alert tip %}
Push-Nachrichten sind für Android standardmäßig verfügbar.
{% endalert %}

Um Push-Storys unter iOS mit Expo zu aktivieren, stellen Sie sicher, dass Sie eine App-Gruppe für Ihre Anwendung definiert haben. Weitere Informationen finden Sie unter [Hinzufügen einer App-Gruppe]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/push_story/#adding-an-app-group).

Konfigurieren Sie als Nächstes die Eigenschaft `enableBrazeIosPushStories` auf `true` und weisen Sie Ihre App-Gruppen-ID `iosPushStoryAppGroup` in Ihrem `expo.plugins` -Objekt auf `app.json` zu:

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          ...
          "enableBrazeIosPushStories": true,
          "iosPushStoryAppGroup": "group.com.company.myApp.PushStories"
        }
      ]
    ]
  }
}
```

Fügen Sie dann den Bundle-Bezeichner für diese App-Erweiterung zur Konfiguration der Zugangsdaten Ihres Projekts hinzu: `<your-app-bundle-id>.BrazeExpoPushStories`. Weitere Einzelheiten zu diesem Vorgang finden Sie unter [Verwendung von App-Erweiterungen mit Expo Application Services](#app-extensions).

{% alert warning %}
Wenn Sie Push-Storys mit Expo Application Services verwenden, stellen Sie sicher, dass Sie das Flag `EXPO_NO_CAPABILITY_SYNC=1` verwenden, wenn Sie `eas build` ausführen. Es gibt ein bekanntes Problem in der Befehlszeile, das die App-Gruppen-Funktion aus dem Provisioning-Profil der Erweiterung entfernt.
{% endalert %}

### Verwendung von App-Erweiterungen mit Expo Application Services {#app-extensions}

Wenn Sie Expo Application Services (EAS) verwenden und `enableBrazeIosRichPush` oder `enableBrazeIosPushStories` aktiviert haben, müssen Sie die entsprechenden Bundle-Bezeichner für jede App-Erweiterung in Ihrem Projekt deklarieren. Es gibt mehrere Möglichkeiten für diesen Schritt. Diese hängen von der Konfiguration Ihres Projekt für die Verwaltung der Codesignierung mit EAS ab.

Eine Möglichkeit besteht darin, die Konfiguration `appExtensions` in der Datei `app.json` zu verwenden. Weitere Informationen hierzu finden Sie in der [Expo-Dokumentation zu App-Erweiterungen](https://docs.expo.dev/build-reference/app-extensions/). Alternativ können Sie die Einstellung `multitarget` in der Datei `credentials.json` einrichten. Weitere Informationen hierzu finden Sie in der [Expo-Dokumentation zu lokalen Zugangsdaten](https://docs.expo.dev/app-signing/local-credentials/#multi-target-project).

