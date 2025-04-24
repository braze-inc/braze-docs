{% multi_lang_include developer_guide/prerequisites/unreal_engine.md %}

## Push-Benachrichtigungen einrichten

### Schritt 1: Richten Sie Ihr Projekt ein

{% tabs %}
{% tab Android %}
Fügen Sie zunächst Firebase zu Ihrem Android-Projekt hinzu. Eine schrittweise Anleitung finden Sie in der [Firebase-Einrichtungsanleitung](https://firebase.google.com/docs/android/setup) von Google.
{% endtab %}

{% tab iOS %}
{% multi_lang_include developer_guide/swift/apns_token.md %}
{% endtab %}
{% endtabs %}

### Schritt 2: Enablement von Push-Benachrichtigungen

{% tabs %}
{% tab Android %}
Fügen Sie die folgenden Zeilen in die Datei `engine.ini` Ihres Projekts ein. Stellen Sie sicher, dass Sie `YOUR_SEND_ID` durch die [ID des Absenders in Ihrem Firebase-Projekt](https://firebase.google.com/docs/cloud-messaging/concept-options#credentials) ersetzen.

```ini
bEnableFirebaseCloudMessagingSupport=true
bIsFirebaseCloudMessagingRegistrationEnabled=true
FirebaseCloudMessagingSenderIdKey=YOUR_SENDER_ID
```

Erstellen Sie in demselben Verzeichnis wie [BrazeUPLAndroid.xml](./BrazeSample/Plugins/Braze/Source/Braze/BrazeUPLAndroid.xml)erstellen Sie ein neues Verzeichnis mit dem Namen `AndroidCopies` und fügen Sie Ihre Datei `google-services.json` hinzu.
{% endtab %}

{% tab iOS %}
Gehen Sie in Ihrem Projekt zu **Einstellungen** > **Projekteinstellungen** > **iOS** > **Online** und aktivieren Sie **die** Option **Unterstützung für Fernbenachrichtigungen aktivieren**. Wenn Sie fertig sind, überprüfen Sie, ob Ihre Bereitstellung Push-Funktionen aktiviert hat.

{% alert important %}
Um Push-Funktionen für iOS zu aktivieren, muss Ihr Projekt aus dem Quellcode erstellt worden sein. Weitere Informationen finden Sie unter [Unreal Engine: Bauen aus dem Quellcode](https://dev.epicgames.com/documentation/en-us/unreal-engine/building-unreal-engine-from-source).
{% endalert %}
{% endtab %}
{% endtabs %}

## Optionale Konfigurationen

{% tabs %}
{% tab Android %}
#### Kleine und große Icons einstellen

Zum Einstellen der [kleinen und großen Benachrichtigungssymbole]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android&tab=android#configure-icons):

1. Fügen Sie die Symbole in den entsprechenden Drawable-Ordner (standardmäßig`drawable` ) innerhalb des Ordners `AndroidCopies/res` ein.
2. Fügen Sie `braze.xml` zum Ordner `AndroidCopies/res/values` hinzu, um die Symbole festzulegen. Eine sehr einfache braze.xml Datei:
    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <resources>
        <drawable name="com_braze_push_small_notification_icon">@drawable/notification_small_icon</drawable>
        <drawable name="com_braze_push_large_notification_icon">@drawable/notification_large_icon</drawable>
    </resources>
    ```

{% alert note %}
Die Dateien aus dem Ordner `AndroidCopies` werden in die generierte Android-Projektstruktur kopiert, wie in `BrazeUPLAndroid.xml` definiert.
{% endalert %}
{% endtab %}

{% tab iOS %}
#### Benachrichtigungen zum Fernstart

Ab Unreal Engine Version 4.25.3 fehlt in UE4 die Unterstützung für den Empfang einer Remote-Benachrichtigung, die den ersten Start der Anwendung verursacht. Um den Empfang dieser Benachrichtigung zu unterstützen, haben wir zwei Git-Patches erstellt, die Sie anwenden können - einen für UE4 und einen für das Braze SDK Plugin.

1. Wenden Sie in Ihrem UE4 Engine `Source` Verzeichnis den Git-Patch `UE4_Engine-Cache-Launch-Remote-Notification.patch` an.
2. Wenden Sie in Ihrem Braze Unreal SDK-Verzeichnis den git-Patch `Braze_SDK-Read-Cached-Remote-Launch-Notification.patch` an.
{% endtab %}
{% endtabs %}
