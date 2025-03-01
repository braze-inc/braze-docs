---
nav_title: Android
article_title: Android Push-Benachrichtigungen für Unity
platform: 
  - Unity
  - Android
channel: push
page_order: 1
description: "Dieser Referenzartikel behandelt die Integration von Android-Push-Benachrichtigungen für die Unity-Plattform."

---

# Integration von Android-Push-Benachrichtigungen

> Dieser Referenzartikel behandelt die Integration von Android-Push-Benachrichtigungen für die Unity-Plattform.

Diese Anleitung bezieht sich auf die Integration von Push mit [Firebase Cloud Messaging (FCM)](https://firebase.google.com/docs/cloud-messaging/).

Anweisungen zur ADM-Integration finden Sie in unserer [Unity ADM-Dokumentation]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/push_notifications/adm_push_notifications/).

## Schritt 1: Firebase aktivieren

Um loszulegen, folgen Sie der [Dokumentation zur Einrichtung von Firebase Unity](https://firebase.google.com/docs/unity/setup).

{% alert note %}
Durch die Integration des Firebase Unity SDK kann die `AndroidManifest.xml` überschrieben werden. Stellen Sie in diesem Fall sicher, dass Sie die ursprüngliche Datei wiederherstellen.
{% endalert %}

## Schritt 2: Legen Sie Ihre Firebase-Anmeldedaten fest

Sie müssen den Firebase-Serverschlüssel und die Sender-ID in das Braze-Dashboard eingeben. Melden Sie sich dazu in der [Firebase Developers Console](https://console.firebase.google.com/) an und wählen Sie Ihr Firebase-Projekt aus. Wählen Sie dann unter **Einstellungen** die Option **Cloud Messaging** und kopieren Sie den Serverschlüssel und die Absender-ID:<br>![]({% image_buster /assets/img_archive/finding_firebase_server_key.png %} "FirebaseServerKey")

In Braze wählen Sie Ihre Android-App auf der Seite **App-Einstellungen** unter **Einstellungen verwalten** aus. Als nächstes geben Sie Ihren Firebase Server Key in das Feld **Firebase Cloud Messaging Server Key** und die Firebase Sender ID in das Feld **Firebase Cloud Messaging Sender** ID ein.

![]({% image_buster /assets/img_archive/fcm_api_insert.png %} "FCMKey")

## Schritt 3: Automatische Push-Integration implementieren

Das Braze SDK kann automatisch die Push-Registrierung bei den Firebase Cloud Messaging-Servern übernehmen, damit die Geräte Push-Benachrichtigungen erhalten.

![Der Unity-Editor zeigt die Konfigurationsoptionen von Braze an. In diesem Editor sind die Optionen "Automate Unity Android Integration", "Push Notification Firebase Push", "Push Configuration Handle Push Deeplinks Automatically", "Push Configuration Push Notification HTML Rendering Enabled" und "Set Push Deleted/Opened/Received Listeners" festgelegt. Außerdem sind die Felder "Firebase Sender-ID", "Drawable für kleines/großes Symbol", "Standard-Akzeptfarbe für Benachrichtigungen" vorhanden.]({% image_buster /assets/img/unity/android/unity_android_push_settings_config.png %} "Android Push-Einstellungen")

- **Automatische Firebase Cloud Messaging-Registrierung Aktiviert**<br> Weist das Braze SDK an, automatisch ein FCM Push-Token für ein Gerät abzurufen und zu senden. 
- **Sender-ID für Firebase Cloud Messaging**<br> Die Absender-ID aus Ihrer Firebase-Konsole.
- **Push-Deeplinks automatisch verarbeiten**<br> Gibt an, ob das SDK das Öffnen von Deeplinks oder das Öffnen der App beim Klicken auf Push-Benachrichtigungen verarbeiten soll.
- **Drawable für kleines Benachrichtigungssymbol**<br>Das Drawable sollte beim Empfang einer Push-Benachrichtigung als kleines Symbol angezeigt werden. Wenn kein Symbol angegeben wurde, verwendet die Benachrichtigung das Anwendungssymbol als kleines Symbol.

## Schritt 4: Push-Hörer einstellen

Wenn Sie Nutzlasten von Push-Benachrichtigungen an Unity übergeben oder weitere Schritte unternehmen möchten, wenn ein Nutzer eine Push-Benachrichtigung erhält, bietet Ihnen Braze die Möglichkeit, Listener für Push-Benachrichtigungen einzurichten.

In Braze wählen Sie Ihre Android-App auf der Seite **App-Einstellungen** unter **Einstellungen verwalten** aus. Als Nächstes geben Sie Ihren Firebase-Serverschlüssel in das Feld **Einstellungen für Push-Benachrichtigungen** und die Firebase-Sender-ID in das ID-Feld der **Einstellungen für Push-Benachrichtigungen** ein.

#### Listener für Push-Empfang

Der Listener für Push-Empfang wird ausgelöst, wenn ein Nutzer eine Push-Benachrichtigung empfängt. Um die Push-Nutzlast an Unity zu senden, legen Sie den Namen Ihres Spielobjekts und die Callback-Methode für den Listener für Push-Empfang unter **Listener für Push-Empfang einrichten** fest.

#### Listener für Push-Öffnung

Der Listener für Push-Öffnung wird ausgelöst, wenn ein Nutzer die App durch Klicken auf eine Push-Benachrichtigung startet. Um die Push-Nutzlast an Unity zu senden, legen Sie den Namen Ihres Spielobjekts und die Callback-Methode für den Listener für Push-Öffnung unter **Listener für Push-Öffnung einrichten** fest.

#### Listener für Push-Löschung (nur Android)

Der Listener für gelöschte Push-Benachrichtigungen wird ausgelöst, wenn ein Benutzer eine Push-Benachrichtigung wegwischt oder ablehnt. Um die Push-Nutzlast an Unity zu senden, legen Sie den Namen Ihres Spielobjekts und die Callback-Methode für den Listener für Push-Löschung unter **Listener für Push-Löschung einrichten** fest.

#### Beispiel für die Implementierung eines Push-Listeners

Im folgenden Beispiel wird das Spielobjekt `BrazeCallback` mit einer Callback-Methode namens `PushNotificationReceivedCallback`, `PushNotificationOpenedCallback` bzw. `PushNotificationDeletedCallback` implementiert.

![Die Grafik des Implementierungsbeispiels zeigt die in den vorangegangenen Abschnitten erwähnten Konfigurationsoptionen von Braze sowie ein Code-Snippet in C#.]({% image_buster /assets/img/unity/android/unity_android_full_push_listener.png %} "Beispiel für vollständigen Android-Listener")

```csharp
public class MainMenu : MonoBehaviour {
  void PushNotificationReceivedCallback(string message) {
#if UNITY_ANDROID
    Debug.Log("PushNotificationReceivedCallback message: " + message);
    PushNotification pushNotification = new PushNotification(message);
    Debug.Log("Push Notification received: " + pushNotification);   
#elif UNITY_IOS
    ApplePushNotification pushNotification = new ApplePushNotification(message);
    Debug.Log("Push received Notification event: " + pushNotification);   
#endif  
  }

  void PushNotificationOpenedCallback(string message) {
#if UNITY_ANDROID
    Debug.Log("PushNotificationOpenedCallback message: " + message);
    PushNotification pushNotification = new PushNotification(message);
    Debug.Log("Push Notification opened: " + pushNotification);  
#elif UNITY_IOS
    ApplePushNotification pushNotification = new ApplePushNotification(message);
    Debug.Log("Push opened Notification event: " + pushNotification);   
#endif  
  }

  void PushNotificationDeletedCallback(string message) {
#if UNITY_ANDROID
    Debug.Log("PushNotificationDeletedCallback message: " + message);
    PushNotification pushNotification = new PushNotification(message);
    Debug.Log("Push Notification dismissed: " + pushNotification);  
#endif
  }
}
```

### Beispiel für die Umsetzung

Das Beispielprojekt im [Braze Unity SDK Repository](https://github.com/Appboy/appboy-unity-sdk/tree/master/unity-samples) enthält eine voll funktionsfähige Beispiel-App mit FCM.

## Deeplinking zu In-App-Ressourcen

Obwohl Braze standardmäßig Standard-Deeplinks (wie Website-URLs, Android URIs usw.) verarbeiten kann, ist für die Erstellung angepasster Deeplinks eine zusätzliche Manifest-Einrichtung erforderlich.

Eine Anleitung zur Einrichtung finden Sie unter [Deeplinking zu In-App-Ressourcen](https://developer.android.com/training/app-links/deep-linking).

## Hinzufügen von Braze Push-Benachrichtigungssymbolen

Um Ihrem Projekt Push-Symbole hinzuzufügen, erstellen Sie ein AAR-Plugin (Android Archive) oder eine Android-Bibliothek, die die Bilddateien für die Symbole enthält. Weitere Schritte und Informationen finden Sie in der Dokumentation von Unity: [Android Library-Projekte und Android-Archiv-Plug-ins](https://docs.unity3d.com/Manual/AndroidAARPlugins.html).