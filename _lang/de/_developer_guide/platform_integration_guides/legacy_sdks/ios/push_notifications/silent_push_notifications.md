---
nav_title: Stille Push-Benachrichtigungen
article_title: Stille Push-Benachrichtigungen für iOS
platform: iOS
page_order: 4
description: "Dieser referenzierte Artikel behandelt die Implementierung stiller Push-Benachrichtigungen in Ihrer iOS-Anwendung."
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Stille Push-Benachrichtigungen

Push-Benachrichtigungen ermöglichen es Ihnen, Ihre App bei wichtigen Ereignissen zu benachrichtigen. Sie können eine Push-Benachrichtigung senden, wenn Sie neue Nachrichten zugestellt haben, aktuelle Nachrichten senden oder die neueste Folge der Lieblingssendung Ihres Nutzers:innen zum Herunterladen für die Offline-Nutzung bereitstellen. Push-Benachrichtigungen können auch stumm sein, d.h. sie enthalten keine Warnmeldung und keinen Ton und dienen nur dazu, die Oberfläche Ihrer App zu aktualisieren oder Hintergrundarbeiten auszulösen. 

Push-Benachrichtigungen eignen sich hervorragend für sporadische, aber unmittelbar wichtige Inhalte, bei denen die Verzögerung zwischen den Abrufen im Hintergrund möglicherweise nicht akzeptabel ist. Push-Benachrichtigungen können auch viel effizienter sein als Hintergrundabrufe, da Ihre Anwendung nur bei Bedarf gestartet wird. 

Push-Benachrichtigungen sind Rate-Limits, also haben Sie keine Angst davor, so viele zu senden, wie Ihre Anwendung benötigt. iOS und die APN Server kontrollieren, wie oft sie zugestellt werden, und Sie bekommen keine Probleme, wenn Sie zu viele senden. Wenn Ihre Push-Benachrichtigungen gedrosselt werden, werden sie möglicherweise verzögert, bis das Gerät das nächste Mal ein Keep-Alive-Paket sendet oder eine andere Benachrichtigung erhält.

## Stille Push-Benachrichtigungen senden

Um eine stille Push-Benachrichtigung zu senden, setzen Sie das Flag `content-available` in der Nutzlast einer Push-Benachrichtigung auf `1`. Wenn Sie eine stille Push-Benachrichtigung senden, möchten Sie vielleicht auch einige Daten in die Nutzlast der Benachrichtigung aufnehmen, damit Ihre Anwendung das Event referenzieren kann. Dies könnte Ihnen einige Netzwerkanfragen ersparen und die Reaktionsfähigkeit Ihrer App verbessern.

{% alert warning %}
Es wird davon abgeraten, einen Titel und einen Textkörper mit `content-available=1` anzuhängen, da dies zu undefiniertem Verhalten führen kann. Um sicherzustellen, dass eine Benachrichtigung wirklich stumm ist, schließen Sie sowohl den Titel als auch den Text aus, wenn Sie das `content-available` Flag auf `1.` setzen. Weitere Einzelheiten finden Sie in der offiziellen [Apple-Dokumentation über Hintergrundaktualisierungen](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/pushing_background_updates_to_your_app).
{% endalert %}

Das `content-available` Flag kann sowohl im Braze Dashboard als auch in unserem [Apple Push-Objekt]({{site.baseurl}}/api/objects_filters/messaging/apple_object/) in der [Messaging-API]({{site.baseurl}}/api/endpoints/messaging/) gesetzt werden.

![Braze-Dashboard mit dem Kontrollkästchen "content-available" auf dem Tab "Einstellungen" des Push-Composers.]({% image_buster /assets/img_archive/remote_notification.png %} "Inhalt verfügbar")

## Triggern von Hintergrundarbeiten mit stillen Push-Benachrichtigungen

Stille Push-Benachrichtigungen können Ihre App aus dem Zustand "Angehalten" oder "Nicht ausgeführt" aufwecken, um Inhalte zu aktualisieren oder bestimmte Aufgaben auszuführen, ohne dass Ihre Benutzer darüber informiert werden. 

Wenn Sie stille Push-Benachrichtigungen verwenden möchten, um Hintergrundarbeit zu triggern, richten Sie das Flag `content-available` gemäß den vorhergehenden Anweisungen ohne Nachricht oder Ton ein. Richten Sie den Hintergrundmodus Ihrer App ein, um `remote notifications` auf dem Tab **Fähigkeiten** in Ihren Projekteinstellungen zu aktivieren. Eine Remote-Benachrichtigung ist einfach eine normale Push-Benachrichtigung mit dem Kennzeichen `content-available`. 

![Xcode mit dem Kontrollkästchen für den Modus "remote notifications" unter "capabilities".]({% image_buster /assets/img_archive/background_mode.png %} "Hintergrundmodus aktiviert")

Für das [Uninstall-Tracking]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/uninstall_tracking/) ist die Aktivierung des Hintergrundmodus für Fernbenachrichtigungen erforderlich.

Auch wenn der Hintergrundmodus für Remote-Benachrichtigungen aktiviert ist, startet das System Ihre App nicht im Hintergrund, wenn der Nutzer das Beenden der Anwendung erzwungen hat. Der Benutzer muss die Anwendung explizit starten oder das Gerät neu starten, bevor die Anwendung vom System automatisch im Hintergrund gestartet werden kann.

Weitere Informationen finden Sie unter [Pushing von Hintergrund-Updates](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/pushing_background_updates_to_your_app?language=objc) und [`application:didReceiveRemoteNotification:fetchCompletionHandler:`](https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIApplicationDelegate_Protocol/index.html#//apple_ref/occ/intfm/UIApplicationDelegate/application:didReceiveRemoteNotification:fetchCompletionHandler:).

## Einschränkungen bei stillen Benachrichtigungen unter iOS

Das iOS-Betriebssystem kann Benachrichtigungen für einige Funktionen ausblenden. Sollten Sie Schwierigkeiten mit diesen Features haben, könnte das iOS-Gate für stille Benachrichtigungen die Ursache sein.

Braze verfügt über mehrere Features, die auf stille Push-Benachrichtigungen unter iOS angewiesen sind:

|Merkmal|Benutzererfahrung|
|---|---|
|Uninstall-Tracking | Nutzer erhalten nachts einen stillen Uninstall-Tracking-Push.|
|Geofences | Stille Synchronisierung von Geofences vom Server zum Gerät.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Weitere Einzelheiten finden Sie in der Dokumentation zu Apples [Instanzmethode](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623013-application) und [nicht empfangenen Benachrichtigungen](https://developer.apple.com/library/content/technotes/tn2265/_index.html#//apple_ref/doc/uid/DTS40010376-CH1-TNTAG23).

[8]:https://developer.apple.com/library/content/technotes/tn2265/_index.html#//apple_ref/doc/uid/DTS40010376-CH1-TNTAG23