---
nav_title: Reichhaltige Benachrichtigungen
article_title: Reichhaltige Push-Benachrichtigungen für iOS
platform: iOS
page_order: 3
description: "Dieser Referenzartikel behandelt die Implementierung umfangreicher Push-Benachrichtigungen in Ihrer iOS-Anwendung."
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Rich-Benachrichtigungen unter iOS 10

iOS 10 führt die Möglichkeit ein, Push-Benachrichtigungen mit Bildern, GIFs und Videos zu versenden. Um diese Funktion zu aktivieren, müssen Clients eine `Service Extension` erstellen. Dabei handelt es sich um eine neue Art von Erweiterung, die die Modifizierung einer Push-Nutzlast ermöglicht, bevor diese angezeigt wird.

## Erstellen einer Serviceerweiterung

Navigieren Sie zum Erstellen einer [`Notification Service Extension`](https://developer.apple.com/reference/usernotifications/unnotificationserviceextension) in Xcode zu **File > New > Target** und wählen Sie **Notification Service Extension** aus.

![]({% image_buster /assets/img_archive/ios10_se_at.png %}){: style="max-width:90%"}

Vergewissern Sie sich, dass **In Anwendung einbetten** so eingestellt ist, dass die Erweiterung in Ihre Anwendung eingebettet wird.

## Einrichten der Serviceerweiterung

Eine `Notification Service Extension` ist eine eigene Binärdatei, die mit Ihrer App gebündelt wird. Sie muss im [Apple Developer Portal](https://developer.apple.com) mit einer eigenen App-ID und einem eigenen Bereitstellungsprofil eingerichtet werden.

Die Bundle-ID von `Notification Service Extension` muss sich von der Bundle-ID des App-Hauptziels unterscheiden. Wenn die Bundle-ID Ihrer App zum Beispiel `com.company.appname` lautet, können Sie für die Diensterweiterung `com.company.appname.AppNameServiceExtension` verwenden.

### Konfigurieren der Serviceerweiterung für die Zusammenarbeit mit Braze

Braze sendet in der APNs-Nutzlast eine Attachment-Nutzlast unter dem Schlüssel `ab`, den wir zum Konfigurieren, Herunterladen und Anzeigen von Rich Content verwenden. Zum Beispiel:

```json
{
  "ab" :
    {
    ...

    "att" :
      {
       "url" : "http://mysite.com/myimage.jpg",
       "type" : "jpg"
       }
    },
  "aps" :
    {
    ...
    }
}
```

Die relevanten Nutzlastwerte sind:

```objc
// The Braze dictionary key
static NSString *const AppboyAPNSDictionaryKey = @"ab";

// The attachment dictionary
static NSString *const AppboyAPNSDictionaryAttachmentKey = @"att";

// The attachment URL
static NSString *const AppboyAPNSDictionaryAttachmentURLKey = @"url";

// The type of the attachment - a suffix for the file you save
static NSString *const AppboyAPNSDictionaryAttachmentTypeKey = @"type";
```

Um Push-Nachrichten mit einer Braze-Nutzlast manuell anzuzeigen, laden Sie den Inhalt aus dem Wert unter `AppboyAPNSDictionaryAttachmentURLKey` herunter, speichern Sie ihn als Datei mit dem Dateityp, der unter dem Schlüssel `AppboyAPNSDictionaryAttachmentTypeKey` gespeichert ist, und fügen Sie ihn zu den Benachrichtigungsanhängen hinzu.

### Beispiel-Code

Sie können die Diensterweiterung in Objective-C oder Swift schreiben.

Um unseren Beispiel-Code in Objective-C zu verwenden, ersetzen Sie den Inhalt der automatisch generierten `NotificationService.m` Ihres Ziels für die `Notification Service Extension` durch den Inhalt der Appboy [`NotificationService.m`](https://github.com/Appboy/appboy-ios-sdk/blob/master/Example/StopwatchNotificationService/NotificationService.m).

Um unseren Swift-Beispielcode zu verwenden, ersetzen Sie den Inhalt der automatisch generierten `NotificationService.swift` Ihres `Notification Service Extension` Ziels durch den Inhalt des Appboy [`NotificationService.swift`](https://github.com/Appboy/appboy-ios-sdk/blob/master/HelloSwift/HelloSwiftNotificationExtension/NotificationService.swift).

## Erstellen einer umfangreichen Benachrichtigung in Ihrem Dashboard

Um eine Rich Notification in Ihrem Braze Dashboard zu erstellen, erstellen Sie einen iOS-Push, hängen Sie ein Bild oder GIF an oder geben Sie eine URL an, die ein Bild, GIF oder Video enthält. Beachten Sie, dass beim Empfang von Push-Benachrichtigungen Assets heruntergeladen werden. Planen Sie deshalb große, synchrone Anfragespitzen ein, wenn Sie Ihre Inhalte hosten.

Eine Liste der unterstützten Dateitypen und -größen finden Sie unter [`unnotificationattachment`](https://developer.apple.com/reference/usernotifications/unnotificationattachment).

