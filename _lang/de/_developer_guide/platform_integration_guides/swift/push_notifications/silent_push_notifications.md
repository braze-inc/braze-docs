---
nav_title: Stille Push-Benachrichtigungen
article_title: Stille Push-Benachrichtigungen für iOS
platform: Swift
page_order: 4
description: "Dieser Artikel beschreibt, wie Sie stille iOS Push-Benachrichtigungen für das Swift SDK implementieren."
channel:
  - push

---

# Stille Push-Benachrichtigungen für iOS

> Mit Push-Benachrichtigungen können Sie von Ihrer App aus Benachrichtigungen versenden, wenn wichtige Ereignisse eintreten. 

Sie könnten beispielsweise eine Push-Benachrichtigung senden, wenn Sie einen wichtigen Hinweis für einen Nutzer haben. Push-Benachrichtigungen können auch stumm sein, d.h. sie enthalten keine Warnmeldung und keinen Ton und dienen nur dazu, die Oberfläche Ihrer App zu aktualisieren oder Hintergrundarbeiten auszulösen. Stille Push-Benachrichtigungen können Ihre App aus dem Zustand "Angehalten" oder "Nicht ausgeführt" aufwecken, um Inhalte zu aktualisieren oder bestimmte Aufgaben auszuführen, ohne dass Ihre Benutzer darüber informiert werden.

Braze verfügt über mehrere Features, die auf stille Push-Benachrichtigungen angewiesen sind:

|Feature|Benutzererfahrung|
|---|---|
|[Uninstall-Tracking]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/uninstall_tracking/) | Nutzer erhalten nachts einen stillen Uninstall-Tracking-Push.|
|[Geofences]({{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences) | Stille Synchronisierung von Geofences vom Server zum Gerät.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Stille Push-Benachrichtigungen einrichten

Wenn Sie stille Push-Benachrichtigungen verwenden möchten, um Aufgaben im Hintergrund zu triggern, müssen Sie Ihre App so konfigurieren, dass sie auch dann Benachrichtigungen erhält, wenn sie sich im Hintergrund befindet. Dazu fügen Sie die Funktion "Background Modes" über das Fenster **Signing & Capabilities** zum Ziel der Haupt-App in Xcode hinzu. Aktivieren Sie das Kontrollkästchen **Fernbenachrichtigungen**.

![Xcode mit dem Kontrollkästchen für den Modus "remote notifications" unter "capabilities".]({% image_buster /assets/img_archive/background_mode.png %} "Hintergrundmodus aktiviert")

Auch wenn der Hintergrundmodus für Remote-Benachrichtigungen aktiviert ist, startet das System Ihre App nicht im Hintergrund, wenn der Nutzer das Beenden der Anwendung erzwungen hat. Der Benutzer muss die Anwendung explizit starten oder das Gerät neu starten, bevor die Anwendung vom System automatisch im Hintergrund gestartet werden kann.

Weitere Informationen finden Sie unter [Pushing Background Updates](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/pushing_background_updates_to_your_app) und in der [Dokumentation](https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIApplicationDelegate_Protocol/index.html#//apple_ref/occ/intfm/UIApplicationDelegate/application:didReceiveRemoteNotification:fetchCompletionHandler:) `application:didReceiveRemoteNotification:fetchCompletionHandler:`.

## Stille Push-Benachrichtigungen senden

Um eine stille Push-Benachrichtigung zu senden, setzen Sie das Flag `content-available` in der Nutzlast einer Push-Benachrichtigung auf `1`. 

{% alert note %}
Was Apple als Remote-Benachrichtigung bezeichnet, ist eine normale Push-Benachrichtigung, bei der das Kennzeichen `content-available` gesetzt ist.
{% endalert %}

Das `content-available` Flag kann sowohl im Braze Dashboard als auch in unserem [Apple Push-Objekt]({{site.baseurl}}/api/objects_filters/messaging/apple_object/) in der [Messaging-API]({{site.baseurl}}/api/endpoints/messaging/) gesetzt werden.

{% alert warning %}
Es wird davon abgeraten, einen Titel und einen Textkörper mit `content-available=1` anzuhängen, da dies zu undefiniertem Verhalten führen kann. Um sicherzustellen, dass eine Benachrichtigung wirklich stumm ist, schließen Sie sowohl den Titel als auch den Text aus, wenn Sie das `content-available` Flag auf `1.` setzen. Weitere Einzelheiten finden Sie in der offiziellen [Apple-Dokumentation über Hintergrundaktualisierungen](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/pushing_background_updates_to_your_app).
{% endalert %}

![Braze-Dashboard mit dem Kontrollkästchen "content-available" auf dem Tab "Einstellungen" des Push-Composers.]({% image_buster /assets/img_archive/remote_notification.png %} "Inhalt verfügbar")

Wenn Sie eine stille Push-Benachrichtigung senden, möchten Sie vielleicht auch einige Daten in die Nutzlast der Benachrichtigung aufnehmen, damit Ihre Anwendung das Event referenzieren kann. Dies könnte Ihnen einige Netzwerkanfragen ersparen und die Reaktionsfähigkeit Ihrer App verbessern.

## Einschränkungen bei stillen Benachrichtigungen unter iOS

Das iOS-Betriebssystem kann Benachrichtigungen für einige Funktionen ausblenden. Sollten Sie Schwierigkeiten mit diesen Features haben, könnte das iOS-Gate für stille Benachrichtigungen die Ursache sein.

Weitere Einzelheiten finden Sie in der Dokumentation zu Apples [Instanzmethode](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623013-application) und [nicht empfangenen Benachrichtigungen](https://developer.apple.com/library/content/technotes/tn2265/_index.html#//apple_ref/doc/uid/DTS40010376-CH1-TNTAG23).

