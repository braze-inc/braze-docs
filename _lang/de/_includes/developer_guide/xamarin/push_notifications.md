{% multi_lang_include developer_guide/prerequisites/xamarin.md %}

## Push-Benachrichtigungen einrichten

{% tabs %}
{% tab android %}
{% alert tip %}
In unserer [Xample-Beispielanwendung auf GitHub](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/samples/android-net-maui/BrazeAndroidMauiSampleApp/BrazeAndroidMauiSampleApp) können Sie sehen, wie sich Namespaces zwischen Java und C# ändern.
{% endalert %}

Um Push-Benachrichtigungen für Xamarin zu integrieren, müssen Sie die Schritte für native Android-Push-Benachrichtigungen ausführen. Die folgenden Schritte sind nur eine Zusammenfassung. Eine vollständige Anleitung finden Sie in der [Anleitung für native Push-Benachrichtigungen]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/?tab=android/).

### Schritt 1: Aktualisieren Sie Ihr Projekt

1. Fügen Sie Firebase zu Ihrem Android-Projekt hinzu.
2. Fügen Sie die Cloud Messaging-Bibliothek zu `build.gradle` Ihres Android-Projekts hinzu:
  ```gradle
  implementation "google.firebase:firebase-messaging:+"
  ```

### Schritt 2: Erstellen Sie Ihre JSON-Anmeldeinformationen

1. Aktivieren Sie in Google Cloud die [Firebase Cloud Messaging API](https://console.cloud.google.com/apis/library/fcm.googleapis.com).
2. Wählen Sie **Servicekonten** > Ihr Projekt > **Servicekonto erstellen** und geben Sie dann den Namen, die ID und die Beschreibung eines Servicekontos ein. Wenn Sie fertig sind, wählen Sie **Erstellen und fahren Sie fort**.
3. Suchen Sie im Feld **Rolle** nach **Firebase Cloud Messaging API Admin** und wählen Sie es in der Liste der Rollen aus.
4. Wählen Sie in **Servicekonten** Ihr Projekt und wählen Sie dann <i class="fa-solid fa-ellipsis-vertical"></i> **Aktionen** > **Schlüssel verwalten** > **Schlüssel hinzufügen** > **Neuen Schlüssel erstellen**. Wählen Sie **JSON** und wählen Sie dann **Erstellen**.

### Schritt 3: Laden Sie Ihre JSON-Anmeldedaten hoch

1. Wählen Sie in Braze <i class="fa-solid fa-gear"></i> **Einstellungen** > **App-Einstellungen**. Wählen Sie unter den **Push-Benachrichtigungseinstellungen** Ihrer Android-App **Firebase**, dann **JSON-Datei hochladen** und laden Sie die zuvor generierten Anmeldeinformationen hoch. Wenn Sie fertig sind, wählen Sie **Speichern**.
2. Aktivieren Sie in der Firebase-Konsole die automatische FCM-Token-Registrierung. Öffnen Sie Ihr Projekt und wählen Sie dann <i class="fa-solid fa-gear"></i> **Einstellungen** > **Projekteinstellungen**. Wählen Sie **Cloud Messaging** und kopieren Sie dann unter **Firebase Cloud Messaging API (V1)** die Nummer in das Feld **Absender-ID**.
3. Fügen Sie Folgendes zur `braze.xml` Ihres Android Studio-Projekts hinzu.

  ```xml
  <bool translatable="false" name="com_braze_firebase_cloud_messaging_registration_enabled">true</bool>
  <string translatable="false" name="com_braze_firebase_cloud_messaging_sender_id">FIREBASE_SENDER_ID</string>
  ```

{% alert important %}
Um zu verhindern, dass Braze jedes Mal, wenn Sie stille Push-Benachrichtigungen senden, unnötige Netzwerkanfragen auslöst, entfernen Sie alle automatischen Netzwerkanfragen, die in der Methode `onCreate()` der Klasse `Application` konfiguriert sind. Weitere Informationen finden Sie unter [Android Developer Reference: Application](https://developer.android.com/reference/android/app/Application).
{% endalert %}
{% endtab %}

{% tab ios %}
### Schritt 1: Vervollständigen Sie die Ersteinrichtung

In den [Anleitungen zur Swift-Integration]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) finden Sie Informationen zum Einrichten Ihrer Anwendung mit Push und zum Speichern Ihrer Anmeldedaten auf unserem Server. Weitere Einzelheiten finden Sie in der [iOS MAUI](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/samples/ios-net-maui/BrazeiOSMauiSampleApp) Beispielanwendung.

### Schritt 2: Genehmigung für Push-Benachrichtigungen anfordern

Unser Xamarin SDK unterstützt jetzt die automatische Push-Einrichtung. Richten Sie die Push-Automatisierung und die Berechtigungen ein, indem Sie den folgenden Code zur Konfiguration Ihrer Braze-Instanz hinzufügen:

```csharp
configuration.Push.Automation = new BRZConfigurationPushAutomation(true);
configuration.Push.Automation.RequestAuthorizationAtLaunch = false;
```

Weitere Einzelheiten finden Sie in der [iOS MAUI](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/samples/ios-net-maui/BrazeiOSMauiSampleApp) Beispielanwendung. Weitere Einzelheiten finden Sie in der Xamarin-Dokumentation für [Enhanced User Notifications in Xamarin.iOS](https://learn.microsoft.com/en-us/previous-versions/xamarin/ios/platform/user-notifications/enhanced-user-notifications?tabs=macos).
{% endtab %}
{% endtabs %}
