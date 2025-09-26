{% multi_lang_include developer_guide/prerequisites/unity.md %}

## Push-Benachrichtigung einrichten

### Schritt 1: Einrichten der Plattform

{% tabs %}
{% tab Android %}
#### Schritt 1.1: Firebase aktivieren

Um loszulegen, folgen Sie der [Dokumentation zur Einrichtung von Firebase Unity](https://firebase.google.com/docs/unity/setup).

{% alert note %}
Durch die Integration des Firebase Unity SDK kann die `AndroidManifest.xml` überschrieben werden. Stellen Sie in diesem Fall sicher, dass Sie die ursprüngliche Datei wiederherstellen.
{% endalert %}

#### Schritt 1.2: Legen Sie Ihre Firebase-Anmeldedaten fest

Sie müssen den Firebase-Serverschlüssel und die Sender-ID in das Braze-Dashboard eingeben. Melden Sie sich dazu in der [Firebase Developers Console](https://console.firebase.google.com/) an und wählen Sie Ihr Firebase-Projekt aus. Wählen Sie dann unter **Einstellungen** die Option **Cloud Messaging** und kopieren Sie den Serverschlüssel und die Absender-ID:<br>![]({% image_buster /assets/img_archive/finding_firebase_server_key.png %} "FirebaseServerKey")

In Braze wählen Sie Ihre Android-App auf der Seite **App-Einstellungen** unter **Einstellungen verwalten** aus. Als nächstes geben Sie Ihren Firebase Server Key in das Feld **Firebase Cloud Messaging Server Key** und die Firebase Sender ID in das Feld **Firebase Cloud Messaging Sender** ID ein.

![]({% image_buster /assets/img_archive/fcm_api_insert.png %} "FCMKey")
{% endtab %}

{% tab Swift %}
#### Schritt 1.1: Integrationsmethode überprüfen

Braze bietet eine native Unity-Lösung für die Automatisierung von iOS-Push-Integrationen an. Wenn Sie Ihre Integration stattdessen manuell einrichten und verwalten möchten, lesen Sie [Swift: Push-Benachrichtigungen]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift).

Andernfalls fahren Sie mit dem nächsten Schritt fort.

{% alert note %}
Unsere Lösung für automatische Push-Benachrichtigungen nutzt die Funktion Provisorische Autorisierung von iOS 12 und kann nicht mit dem nativen Push-Prompt-Pop-up verwendet werden.
{% endalert %}
{% endtab %}

{% tab Amazon Gerät Messaging %}
#### Schritt 1.1: Enablement von ADM

1. Erstellen Sie ein Konto im [Amazon Apps & Games Entwickler:in Portal](https://developer.amazon.com/public), falls Sie dies noch nicht getan haben.
2. Holen Sie sich die [OAuth-Zugangsdaten (Client-ID und Client-Geheimnis) und einen ADM-API-Schlüssel](https://developer.amazon.com/public/apis/engage/device-messaging/tech-docs/02-obtaining-adm-credentials).
3. Aktivieren Sie **Automatische ADM-Registrierung aktiviert** im Unity Braze-Konfigurationsfenster. 
  - Alternativ können Sie auch die folgende Zeile in Ihre `res/values/braze.xml` Datei einfügen, um die ADM Registrierung zu aktivieren:

  ```xml
  <bool name="com_braze_push_adm_messaging_registration_enabled">true</bool>
  ```
{% endtab %}
{% endtabs %}

### Schritt 2: Push-Benachrichtigungen konfigurieren

{% tabs %}
{% tab Android %}
#### Schritt 2.1: Push-Einstellungen konfigurieren

Das Braze SDK kann automatisch die Push-Registrierung bei den Firebase Cloud Messaging-Servern übernehmen, damit die Geräte Push-Benachrichtigungen erhalten. Aktivieren Sie in Unity die **Automatisierung der Unity Android Integration** und konfigurieren Sie dann die folgenden Einstellungen für **Push-Benachrichtigungen**.

| Einstellung                                | Beschreibung                                                                                                                                              |
|----------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Automatische Firebase Cloud Messaging-Registrierung Aktiviert | Weist das Braze SDK an, automatisch ein FCM Push-Token für ein Gerät abzurufen und zu senden.                                                                |
| Sender-ID für Firebase Cloud Messaging     | Die Absender-ID aus Ihrer Firebase-Konsole.                                                                                                                |
| Push-Deeplinks automatisch verarbeiten    | Gibt an, ob das SDK das Öffnen von Deeplinks oder das Öffnen der App beim Klicken auf Push-Benachrichtigungen verarbeiten soll.                                                  |
| Drawable für kleines Benachrichtigungssymbol       | Das Drawable sollte beim Empfang einer Push-Benachrichtigung als kleines Symbol angezeigt werden. Wenn kein Symbol angegeben wurde, verwendet die Benachrichtigung das Anwendungssymbol als kleines Symbol. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% endtab %}

{% tab Swift %}
#### Schritt 2.1: Laden Sie Ihr APN-Token hoch

{% multi_lang_include developer_guide/swift/apns_token.md %}

#### Schritt 2.2: Enablement von automatischem Push

Öffnen Sie die Braze-Konfigurationseinstellungen im Unity-Editor, indem Sie zu **Braze > Braze-Konfiguration** navigieren.

Aktivieren Sie die Option **Push mit Braze integrieren**, um Benutzer automatisch für Push-Benachrichtigungen zu registrieren, Push-Tokens an Braze weiterzugeben, Analysen für Push-Öffnungen zu verfolgen und die Vorteile unserer standardmäßigen Handhabung von Push-Benachrichtigungen zu nutzen.

#### Schritt 2.3: Aktivieren von Push im Hintergrund (optional)

Markieren Sie **Hintergrund-Push aktivieren**, wenn Sie `background mode` für Push-Benachrichtigungen aktivieren möchten. Dadurch kann das System Ihre Anwendung aus dem Zustand `suspended` aufwecken, wenn eine Push-Benachrichtigung eintrifft, so dass Ihre Anwendung als Reaktion auf die Push-Benachrichtigung Inhalte herunterladen kann. Das Aktivieren dieser Option ist für unsere Funktion zur Nachverfolgung von Deinstallationen erforderlich.

![Der Unity-Editor zeigt die Konfigurationsoptionen von Braze an. In diesem Editor sind die Optionen "Unity iOS-Integration automatisieren", "Push mit Braze integrieren" und "Hintergrund-Push aktivieren" aktiviert.]({% image_buster /assets/img/unity/ios/unity_ios_enable_background.png %})

#### Schritt 2.4: Automatische Registrierung deaktivieren (optional)

Benutzer, die sich noch nicht für Push-Benachrichtigungen entschieden haben, werden beim Öffnen Ihrer Anwendung automatisch für Push autorisiert. Um diese Funktion zu deaktivieren und Benutzer manuell für Push zu registrieren, markieren Sie **Automatische Push-Registrierung deaktivieren**.

- Wenn **Vorläufige Autorisierung deaktivieren** unter iOS 12 oder höher nicht aktiviert ist, wird der Benutzer vorläufig (stillschweigend) für den Empfang von Quiet Push autorisiert. Wenn diese Option aktiviert ist, wird dem Nutzer der native Push-Prompt angezeigt.
- Wenn Sie genau konfigurieren möchten, wann der Prompt zur Laufzeit angezeigt werden soll, deaktivieren Sie die automatische Registrierung im Braze-Konfigurationseditor und verwenden Sie stattdessen `AppboyBinding.PromptUserForPushPermissions()`.

![Der Unity-Editor zeigt die Konfigurationsoptionen von Braze an. In diesem Editor sind die Optionen "Unity iOS-Integration automatisieren", "Push mit Braze integrieren" und "Automatische Push-Registrierung deaktivieren" aktiviert.]({% image_buster /assets/img/unity/ios/unity_ios_disable_auto_push.png %})
{% endtab %}

{% tab Amazon Gerät Messaging %}
#### Schritt 2.1: `AndroidManifest.xml` aktualisieren

Wenn Ihre App nicht über ein `AndroidManifest.xml` verfügt, können Sie das folgende Template als Vorlage verwenden. Wenn Sie bereits eine `AndroidManifest.xml` haben, stellen Sie sicher, dass die folgenden fehlenden Abschnitte zu Ihrer bestehenden `AndroidManifest.xml` hinzugefügt werden.

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
          package="REPLACE_WITH_YOUR_PACKAGE_NAME">

  <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
  <uses-permission android:name="android.permission.INTERNET" />
  <permission
    android:name="REPLACE_WITH_YOUR_PACKAGE_NAME.permission.RECEIVE_ADM_MESSAGE"
    android:protectionLevel="signature" />
  <uses-permission android:name="REPLACE_WITH_YOUR_PACKAGE_NAME.permission.RECEIVE_ADM_MESSAGE" />
  <uses-permission android:name="com.amazon.device.messaging.permission.RECEIVE" />

  <application android:icon="@drawable/app_icon" 
               android:label="@string/app_name">

    <!-- Calls the necessary Braze methods to ensure that analytics are collected and that push notifications are properly forwarded to the Unity application. -->
    <activity android:name="com.braze.unity.BrazeUnityPlayerActivity" 
      android:label="@string/app_name" 
      android:configChanges="fontScale|keyboard|keyboardHidden|locale|mnc|mcc|navigation|orientation|screenLayout|screenSize|smallestScreenSize|uiMode|touchscreen" 
      android:screenOrientation="sensor">
      <meta-data android:name="android.app.lib_name" android:value="unity" />
      <meta-data android:name="unityplayer.ForwardNativeEventsToDalvik" android:value="true" />
      <intent-filter>
        <action android:name="android.intent.action.MAIN" />
        <category android:name="android.intent.category.LAUNCHER" />
      </intent-filter>
    </activity>

    <receiver android:name="com.braze.push.BrazeAmazonDeviceMessagingReceiver" android:permission="com.amazon.device.messaging.permission.SEND">
      <intent-filter>
          <action android:name="com.amazon.device.messaging.intent.RECEIVE" />
          <action android:name="com.amazon.device.messaging.intent.REGISTRATION" />
          <category android:name="REPLACE_WITH_YOUR_PACKAGE_NAME" />
      </intent-filter>
    </receiver>
  </application>
</manifest>
```

#### Schritt 2.2: Speichern Sie Ihren ADM API-Schlüssel

Zunächst [generieren Sie einen ADM API-Schlüssel für Ihre App](https://developer.amazon.com/public/apis/engage/device-messaging/tech-docs/02-obtaining-adm-credentials), speichern Sie dann den Schlüssel in einer Datei mit dem Namen `api_key.txt` und fügen Sie ihn in das [`Assets/`](https://docs.unity3d.com/Manual/AndroidAARPlugins.html) Verzeichnis hinzu.

{% alert important %}
Amazon wird Ihren Schlüssel nicht erkennen, wenn `api_key.txt` Leerzeichen enthält, wie z.B. einen Zeilenumbruch am Ende.
{% endalert %}

Als nächstes fügen Sie in Ihrer Datei `mainTemplate.gradle` Folgendes hinzu:

```gradle
task copyAmazon(type: Copy) {
    def unityProjectPath = $/file:///**DIR_UNITYPROJECT**/$.replace("\\", "/")
    from unityProjectPath + '/Assets/api_key.txt'
    into new File(projectDir, 'src/main/assets')
}

preBuild.dependsOn(copyAmazon)
```

#### Schritt 2.3: ADM-Jar hinzufügen

Die erforderliche ADM Jar-Datei kann gemäß der [Unity JAR-Dokumentation](https://docs.unity3d.com/Manual/AndroidJARPlugins.html) an beliebiger Stelle in Ihrem Projekt platziert werden.

#### Schritt 2.4: Fügen Sie das Client-Geheimnis und die Client-ID zu Ihrem Braze-Dashboard hinzu

Schließlich müssen Sie das Client-Geheimnis und die Client-ID, die Sie in [Schritt 1](#unity_step-1-enable-adm) erhalten haben, auf der Seite Einstellungen verwalten des Braze-Dashboards hinzufügen.

![]({% image_buster /assets/img_archive/fire_os_dashboard.png %})
{% endtab %}
{% endtabs %}

### Schritt 3: Push-Hörer einstellen

{% tabs %}
{% tab Android %}
#### Schritt 3.1: Enablement von Push-Empfangsprotokollen

Der Listener für Push-Empfang wird ausgelöst, wenn ein Nutzer eine Push-Benachrichtigung empfängt. Um die Push-Nutzlast an Unity zu senden, legen Sie den Namen Ihres Spielobjekts und die Callback-Methode für den Listener für Push-Empfang unter **Listener für Push-Empfang einrichten** fest.

#### Schritt 3.2: Enablement des Push-Öffnungs-Hörers

Der Listener für Push-Öffnung wird ausgelöst, wenn ein Nutzer die App durch Klicken auf eine Push-Benachrichtigung startet. Um die Push-Nutzlast an Unity zu senden, legen Sie den Namen Ihres Spielobjekts und die Callback-Methode für den Listener für Push-Öffnung unter **Listener für Push-Öffnung einrichten** fest.

#### Schritt 3.3: Enablement für Push gelöschter Listener

Der Listener für gelöschte Push-Benachrichtigungen wird ausgelöst, wenn ein Benutzer eine Push-Benachrichtigung wegwischt oder ablehnt. Um die Push-Nutzlast an Unity zu senden, legen Sie den Namen Ihres Spielobjekts und die Callback-Methode für den Listener für Push-Löschung unter **Listener für Push-Löschung einrichten** fest.

#### Push Listener Beispiel

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
{% endtab %}

{% tab Swift %}
#### Schritt 3.1: Enablement von Push-Empfangsprotokollen

Der Listener für Push-Empfang wird ausgelöst, wenn ein Nutzer eine Push-Benachrichtigung empfängt, während er die Anwendung aktiv nutzt (z. B. wenn sich die Anwendung im Vordergrund befindet). Legen Sie den Push-Empfangslistener im Braze-Konfigurationseditor fest. Wenn Sie den Spielobjekt-Listener zur Laufzeit konfigurieren müssen, verwenden Sie `AppboyBinding.ConfigureListener()` und geben Sie `BrazeUnityMessageType.PUSH_RECEIVED` an.

![Der Unity-Editor zeigt die Konfigurationsoptionen von Braze an. In diesem Editor ist die Option "Listener für Push-Empfang einrichten" erweitert und der "Name des Spielobjekts" (AppBoyCallback) sowie der "Name der Callback-Methode" (PushNotificationReceivedCallback) sind angegeben.]({% image_buster /assets/img/unity/ios/unity_ios_push_received.png %})

#### Schritt 3.2: Enablement des Push-Öffnungs-Hörers

Der Listener für Push-Öffnung wird ausgelöst, wenn ein Nutzer die App durch Klicken auf eine Push-Benachrichtigung startet. Um die Push-Nutzlast an Unity zu senden, legen Sie den Namen Ihres Spielobjekts und die Callback-Methode für den Listener für Push-Öffnung unter der Option **Listener für Push-Öffnung einrichten** fest:

![Der Unity-Editor zeigt die Konfigurationsoptionen von Braze an. In diesem Editor ist die Option "Listener für Push-Öffnung einrichten" erweitert und der "Name des Spielobjekts" (AppBoyCallback) sowie der "Name der Callback-Methode" (PushNotificationOpenedCallback) sind angegeben.]({% image_buster /assets/img/unity/ios/unity_ios_push_opened.png %})

Wenn Sie den Spielobjekt-Listener zur Laufzeit konfigurieren müssen, verwenden Sie `AppboyBinding.ConfigureListener()` und geben Sie `BrazeUnityMessageType.PUSH_OPENED` an.

#### Push Listener Beispiel

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
{% endtab %}

{% tab Amazon Gerät Messaging %}
Durch das Update Ihrer `AndroidManifest.xml` im [vorherigen Schritt](#unity_step-21-update-androidmanifestxml) wurden Push-Listener automatisch eingerichtet, als Sie die folgenden Zeilen hinzugefügt haben. Es ist also keine weitere Einrichtung erforderlich.

```xml
<action android:name="com.amazon.device.messaging.intent.RECEIVE" />
<action android:name="com.amazon.device.messaging.intent.REGISTRATION" />
```

{% alert note %}
Um mehr über ADM Push-Hörer zu erfahren, besuchen Sie [Amazon: Integrieren Sie Amazon Device Messaging](https://developer.amazon.com/docs/video-skills-fire-tv-apps/integrate-adm.html).
{% endalert %}
{% endtab %}
{% endtabs %}

## Optionale Konfigurationen

{% tabs %}
{% tab Android %}
#### Deeplinking zu In-App-Ressourcen

Obwohl Braze standardmäßig Standard-Deeplinks (wie Website-URLs, Android URIs usw.) verarbeiten kann, ist für die Erstellung angepasster Deeplinks eine zusätzliche Manifest-Einrichtung erforderlich.

Eine Anleitung zur Einrichtung finden Sie unter [Deeplinking zu In-App-Ressourcen](https://developer.android.com/training/app-links/deep-linking).

#### Hinzufügen von Braze Push-Benachrichtigungssymbolen

Um Ihrem Projekt Push-Symbole hinzuzufügen, erstellen Sie ein AAR-Plugin (Android Archive) oder eine Android-Bibliothek, die die Bilddateien für die Symbole enthält. Weitere Schritte und Informationen finden Sie in der Dokumentation von Unity: [Android Library-Projekte und Android-Archiv-Plug-ins](https://docs.unity3d.com/Manual/AndroidAARPlugins.html).
{% endtab %}

{% tab Swift %}
#### Push Token-Callback

Um eine Kopie der Braze-Gerätetoken vom Betriebssystem zu erhalten, setzen Sie mit `AppboyBinding.SetPushTokenReceivedFromSystemDelegate()` einen Delegaten.
{% endtab %}

{% tab Amazon Gerät Messaging %}
Zur Zeit gibt es keine optionalen Konfigurationen für ADM.
{% endtab %}
{% endtabs %}
