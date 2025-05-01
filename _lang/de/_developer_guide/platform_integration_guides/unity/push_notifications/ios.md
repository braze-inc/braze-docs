---
nav_title: iOS
article_title: Push-Benachrichtigungen für Unity
platform:
  - Unity
  - iOS
channel: push
ex_push_payload: archive/apple/push_payload.json
page_order: 1
description: "Dieser Referenzartikel behandelt die Integration von iOS-Push-Benachrichtigungen für die Unity-Plattform."

---

# Integration von iOS-Push-Benachrichtigungen

> Dieser Referenzartikel behandelt die Integration von iOS-Push-Benachrichtigungen für die Unity-Plattform.

## Schritt 1: Wählen Sie automatische oder manuelle Push-Integration

Braze bietet eine native Unity-Lösung für die Automatisierung von iOS-Push-Integrationen an.

- Wenn Sie die Integration lieber manuell durchführen möchten, indem Sie Ihr erstelltes Xcode-Projekt ändern, folgen Sie unseren [Anweisungen für native iOS-Push]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/).
- Wenn Sie von einer manuellen Integration zu einer automatischen Integration übergehen, folgen Sie den Anweisungen unter [Übergang zu einer automatischen Integration]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/sdk_integration/ios/#transitioning-from-manual-to-automated-integration-ios).
- Unsere Lösung für automatische Push-Benachrichtigungen nutzt die Funktion Provisorische Autorisierung von iOS 12 und kann nicht mit dem nativen Push-Prompt-Pop-up verwendet werden.

## Schritt 2: Automatische Push-Integration implementieren

### Push-Benachrichtigungen konfigurieren

Folgen Sie unserer [Dokumentation zur Konfiguration von iOS-Push-Benachrichtigungen]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/), um Braze mit einer `.p8` Datei zu konfigurieren.

### Aktivieren Sie die automatische Push-Integration

Öffnen Sie die Braze-Konfigurationseinstellungen im Unity-Editor, indem Sie zu **Braze > Braze-Konfiguration** navigieren.

Aktivieren Sie die Option **Push mit Braze integrieren**, um Benutzer automatisch für Push-Benachrichtigungen zu registrieren, Push-Tokens an Braze weiterzugeben, Analysen für Push-Öffnungen zu verfolgen und die Vorteile unserer standardmäßigen Handhabung von Push-Benachrichtigungen zu nutzen.

### Aktivieren von Push im Hintergrund (optional)

Markieren Sie **Hintergrund-Push aktivieren**, wenn Sie `background mode` für Push-Benachrichtigungen aktivieren möchten. Dadurch kann das System Ihre Anwendung aus dem Zustand `suspended` aufwecken, wenn eine Push-Benachrichtigung eintrifft, so dass Ihre Anwendung als Reaktion auf die Push-Benachrichtigung Inhalte herunterladen kann. Das Aktivieren dieser Option ist für unsere Funktion zur Nachverfolgung von Deinstallationen erforderlich.

![Der Unity-Editor zeigt die Konfigurationsoptionen von Braze an. In diesem Editor sind die Optionen "Unity iOS-Integration automatisieren", "Push mit Braze integrieren" und "Hintergrund-Push aktivieren" aktiviert.]({% image_buster /assets/img/unity/ios/unity_ios_enable_background.png %})

### Automatische Registrierung deaktivieren (optional)

Benutzer, die sich noch nicht für Push-Benachrichtigungen entschieden haben, werden beim Öffnen Ihrer Anwendung automatisch für Push autorisiert. Um diese Funktion zu deaktivieren und Benutzer manuell für Push zu registrieren, markieren Sie **Automatische Push-Registrierung deaktivieren**.

- Wenn **Vorläufige Autorisierung deaktivieren** unter iOS 12 oder höher nicht aktiviert ist, wird der Benutzer vorläufig (stillschweigend) für den Empfang von Quiet Push autorisiert. Wenn diese Option aktiviert ist, wird dem Nutzer der native Push-Prompt angezeigt.
- Wenn Sie genau konfigurieren möchten, wann der Prompt zur Laufzeit angezeigt werden soll, deaktivieren Sie die automatische Registrierung im Braze-Konfigurationseditor und verwenden Sie stattdessen `AppboyBinding.PromptUserForPushPermissions()`.

![Der Unity-Editor zeigt die Konfigurationsoptionen von Braze an. In diesem Editor sind die Optionen "Unity iOS-Integration automatisieren", "Push mit Braze integrieren" und "Automatische Push-Registrierung deaktivieren" aktiviert.]({% image_buster /assets/img/unity/ios/unity_ios_disable_auto_push.png %})

## Schritt 3: Push-Hörer einstellen

Wenn Sie Nutzlasten von Push-Benachrichtigungen an Unity übergeben oder weitere Schritte unternehmen möchten, wenn ein Nutzer eine Push-Benachrichtigung erhält, bietet Ihnen Braze die Möglichkeit, Listener für Push-Benachrichtigungen einzurichten.

### Listener für Push-Empfang

Der Listener für Push-Empfang wird ausgelöst, wenn ein Nutzer eine Push-Benachrichtigung empfängt, während er die Anwendung aktiv nutzt (z. B. wenn sich die Anwendung im Vordergrund befindet). Legen Sie den Push-Empfangslistener im Braze-Konfigurationseditor fest. Wenn Sie den Spielobjekt-Listener zur Laufzeit konfigurieren müssen, verwenden Sie `AppboyBinding.ConfigureListener()` und geben Sie `BrazeUnityMessageType.PUSH_RECEIVED` an.

![Der Unity-Editor zeigt die Konfigurationsoptionen von Braze an. In diesem Editor ist die Option "Listener für Push-Empfang einrichten" erweitert und der "Name des Spielobjekts" (AppBoyCallback) sowie der "Name der Callback-Methode" (PushNotificationReceivedCallback) sind angegeben.]({% image_buster /assets/img/unity/ios/unity_ios_push_received.png %})

### Listener für Push-Öffnung

Der Listener für Push-Öffnung wird ausgelöst, wenn ein Nutzer die App durch Klicken auf eine Push-Benachrichtigung startet. Um die Push-Nutzlast an Unity zu senden, legen Sie den Namen Ihres Spielobjekts und die Callback-Methode für den Listener für Push-Öffnung unter der Option **Listener für Push-Öffnung einrichten** fest:

![Der Unity-Editor zeigt die Konfigurationsoptionen von Braze an. In diesem Editor ist die Option "Listener für Push-Öffnung einrichten" erweitert und der "Name des Spielobjekts" (AppBoyCallback) sowie der "Name der Callback-Methode" (PushNotificationOpenedCallback) sind angegeben.]({% image_buster /assets/img/unity/ios/unity_ios_push_opened.png %})

Wenn Sie den Spielobjekt-Listener zur Laufzeit konfigurieren müssen, verwenden Sie `AppboyBinding.ConfigureListener()` und geben Sie `BrazeUnityMessageType.PUSH_OPENED` an.

### Beispiel für die Implementierung eines Push-Listeners

Im folgenden Beispiel wird das Spielobjekt `AppboyCallback` mit einer Callback-Methode namens `PushNotificationReceivedCallback` bzw. `PushNotificationOpenedCallback` implementiert.

![Die Grafik des Implementierungsbeispiels zeigt die in den vorangegangenen Abschnitten erwähnten Konfigurationsoptionen von Braze sowie ein Code-Snippet in C#.]({% image_buster /assets/img/unity/ios/unity_ios_appboy_callback.png %})

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
}
```

## Erweiterte Funktionen

### Push Token-Callback

Um eine Kopie der Braze-Gerätetoken vom Betriebssystem zu erhalten, setzen Sie mit `AppboyBinding.SetPushTokenReceivedFromSystemDelegate()` einen Delegaten.

### Weitere Features

In unseren [Anweisungen für native iOS-Push-Benachrichtigungen]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/) erfahren Sie, wie Sie erweiterte Features wie Deeplinks, Badge-Zähler und angepasste Töne implementieren.

