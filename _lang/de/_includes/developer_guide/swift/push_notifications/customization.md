{% multi_lang_include developer_guide/prerequisites/swift.md %} Bitte [richten]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) Sie auch [Push-Benachrichtigungen ein]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift).

## Anpassen von Aktions-Buttons {#push-action-buttons-integration}

Das Braze Swift SDK bietet Unterstützung für Push-Action-Buttons bei der URL-Verarbeitung. Es gibt vier Sätze von standardmäßigen Push-Action-Buttons für die Standard-Push-Kategorien von Braze: `Accept/Decline`, `Yes/No`, `Confirm/Cancel` und `More`.

![Ein GIF, das eine Push-Nachricht zeigt, die nach unten gezogen wird, um zwei anpassbare Aktions-Buttons anzuzeigen.]({% image_buster /assets/img_archive/iOS8Action.gif %}){: style="max-width:60%"}

### Manuelles Registrieren von Aktions-Buttons

{% alert important %}
Die manuelle Registrierung von Push-Action-Buttons wird nicht empfohlen.
{% endalert %}

Wenn Sie [Push-Benachrichtigungen]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) über die`configuration.push.automation`Konfigurationsoption [einrichten]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift), registriert Braze automatisch die Aktions-Buttons für die Standard-Push-Kategorien und übernimmt die Analytics-Daten für Klicks auf die Push-Action-Buttons sowie das URL-Routing.

Sie können jedoch auch die Push-Action-Buttons manuell registrieren.

#### Schritt 1: Hinzufügen von Braze Standard Push-Kategorien {#registering}

Verwenden Sie den folgenden Code, um sich für die Standard Push-Kategorien zu registrieren, wenn Sie sich für [Push anmelden]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-4-register-push-tokens-with-braze):

{% tabs %}
{% tab swift %}
a
```swift
UNUserNotificationCenter.current().setNotificationCategories(Braze.Notifications.categories)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[[UNUserNotificationCenter currentNotificationCenter] setNotificationCategories:BRZNotifications.categories];
```

{% endtab %}
{% endtabs %}

{% alert note %}
Wenn Sie auf Push-Action-Buttons mit Hintergrundaktivierung klicken, wird nur die Benachrichtigung verworfen und die App nicht geöffnet. Wenn der Nutzer die App das nächste Mal öffnet, werden die Analytics für die Klicks auf diese Aktionen auf den Server übertragen.
{% endalert %}

#### Schritt 2: Aktivierung der interaktiven Push-Bearbeitung {#enable-push-handling}

Um die Verarbeitung von Push-Action-Buttons, einschließlich Click Analytics und URL-Routing, zu aktivieren, fügen Sie den folgenden Code in die Delegate-Methode `didReceive(_:completionHandler:)` Ihrer App ein:

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.notifications.handleUserNotification(response: response, withCompletionHandler: completionHandler)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[AppDelegate.braze.notifications handleUserNotificationWithResponse:response
                                              withCompletionHandler:completionHandler];
```

{% endtab %}
{% endtabs %}

Wenn Sie das `UNNotification` Framework verwenden und die [Braze-Benachrichtigungsmethoden]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-5-enable-push-handling) implementiert haben, sollten Sie diese Methode bereits integriert haben. 

## Anpassung der Push-Kategorien {#customizing-push-categories}

Braze bietet nicht nur eine Reihe von Standard Push-Kategorien, sondern unterstützt auch angepasste Benachrichtigungskategorien und Aktionen. Nachdem Sie Kategorien in Ihrer Anwendung registriert haben, können Sie das Braze-Dashboard verwenden, um diese angepassten Benachrichtigungskategorien an Ihre Nutzer:innen zu senden.

Hier ist ein Beispiel, das die `LIKE_CATEGORY` nutzt, die auf dem Gerät angezeigt wird:

![Eine Push-Nachricht, die zwei Push-Action-Buttons „Gefällt mir nicht“ und „Gefällt mir“ anzeigt.]({% image_buster /assets/img_archive/push_example_category.png %})

### Schritt 1: Eine Kategorie registrieren

Um eine Kategorie in Ihrer App zu registrieren, gehen Sie ähnlich vor wie im Folgenden beschrieben:

{% tabs %}
{% tab swift %}

```swift
Braze.Notifications.categories.insert(
  .init(identifier: "LIKE_CATEGORY",
        actions: [
          .init(identifier: "LIKE_IDENTIFIER", title: "Like", options: [.foreground]),
          .init(identifier: "UNLIKE_IDENTIFIER", title: "Unlike", options: [.foreground])
        ],
        intentIdentifiers: []
       )
)
UNUserNotificationCenter.current().setNotificationCategories(Braze.Notifications.categories)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
NSMutableSet<UNNotificationCategory *> *categories = [BRZNotifications.categories mutableCopy];

UNNotificationAction *likeAction = [UNNotificationAction actionWithIdentifier:@"LIKE_IDENTIFIER"
                                                                        title:@"Like"
                                                                      options:UNNotificationActionOptionForeground];

UNNotificationAction *unlikeAction = [UNNotificationAction actionWithIdentifier:@"UNLIKE_IDENTIFIER"
                                                                          title:@"Unlike"
                                                                        options:UNNotificationActionOptionForeground];

UNNotificationCategory *likeCategory = [UNNotificationCategory categoryWithIdentifier:@"LIKE_CATEGORY"
                                                                              actions:@[likeAction, unlikeAction]
                                                                    intentIdentifiers:@[]
                                                                              options:UNNotificationCategoryOptionNone];

[categories addObject:likeCategory];
[UNUserNotificationCenter.currentNotificationCenter setNotificationCategories:categories];
```

{% endtab %}
{% endtabs %}

{% alert note %}
Wenn Sie eine `UNNotificationAction` erstellen, können Sie eine Liste von Aktionsoptionen angeben. Beispielsweise können Ihre Nutzer:`.foreground`innen Ihre App öffnen, nachdem sie auf den Aktions-Button getippt haben. Dies ist notwendig für navigatorische On-Click-Verhaltensweisen wie "Open App" und "Deep Link Into Application". Wenn Sie einen Aktions-Button wünschen, der die Benachrichtigung einfach schließt, ohne die Öffnung der App zu verursachen, lassen Sie ihn aus dem Array`.foreground` `options`der Aktion weg. Für weitere Informationen siehe [`UNNotificationActionOptions`](https://developer.apple.com/documentation/usernotifications/unnotificationactionoptions).
{% endalert %}

### Schritt 2: Wählen Sie Ihre Kategorien aus

Nachdem Sie eine Kategorie registriert haben, verwenden Sie das Braze-Dashboard, um Benachrichtigungen dieses Typs an Nutzer:innen zu senden.

{% alert tip %}
Sie müssen lediglich Aktions-Buttons im Braze-Dashboard für Verhaltensweisen definieren, die nicht lokal in Ihrem SWIFT-Code erstellt werden können, wie beispielsweise Deeplinking zu Ihrer App oder Weiterleitungen zu einer Web-URL. Diese Aktionen müssen im Dashboard konfiguriert werden, damit sie festlegen können, welche URL oder welcher Deeplink geöffnet werden soll. Für Aktions-Buttons, die die Benachrichtigung einfach schließen, ohne die App zu öffnen, ist keine Konfiguration im Dashboard erforderlich – das Schließen wird automatisch von iOS übernommen. Bitte registrieren Sie Ihre angepasste Kategorie und die zugehörigen Aktionen in Ihrem App-Code und geben Sie anschließend den entsprechenden Kategorienamen im Dashboard ein.
{% endalert %}

1. Wählen Sie im Braze-Dashboard **Messaging** > **Push-Benachrichtigungen** und wählen Sie dann Ihre iOS [Push-Kampagne]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message).
2. Schalten Sie unter **Push-Benachrichtigung verfassen** die **Aktions-Buttons** ein.
3. Wählen Sie in der Dropdown-Liste **iOS-Benachrichtigungskategorie** die Option **Vorregistrierte, angepasste iOS-Kategorie eingeben**.
4. Geben Sie schließlich eine der Kategorien ein, die Sie zuvor erstellt haben. Das folgende Beispiel verwendet die angepasste Kategorie: `LIKE_CATEGORY`.

![Das Dashboard für Kampagnen mit Push-Benachrichtigungen mit der Einrichtung für benutzerdefinierte Kategorien.]({% image_buster /assets/img_archive/ios-notification-category.png %})

### Beispiel: Angepasste Push-Kategorie {#example-custom-push-category}

Angenommen, Sie möchten eine Push-Benachrichtigung mit zwei Aktions-Buttons erstellen: **Verwalten**, das Deeplinks mit Ihrer App setzt, und **Beibehalten**, das die Benachrichtigung einfach schließt.

Im folgenden Beispiel enthält die`MANAGE_IDENTIFIER`Aktion die`.foreground`Option, die die App beim Antippen öffnet. Dies ist erforderlich, da Deeplinks zu einem bestimmten Teil der App gesetzt werden. Die`KEEP_IDENTIFIER`Aktion verwendet ein leeres Optionsarray, was bedeutet, dass die Benachrichtigung geschlossen wird, ohne eine Öffnung der App zu verursachen.

{% tabs %}
{% tab swift %}

```swift
Braze.Notifications.categories.insert(
  .init(identifier: "YOUR_CATEGORY",
        actions: [
          .init(identifier: "KEEP_IDENTIFIER", title: "Keep", options: []),
          .init(identifier: "MANAGE_IDENTIFIER", title: "Manage", options: [.foreground])
        ],
        intentIdentifiers: []
       )
)
UNUserNotificationCenter.current().setNotificationCategories(Braze.Notifications.categories)
```

{% endtab %}
{% endtabs %}

Da es sich um`MANAGE_IDENTIFIER`Deeplinks in die App handelt, würden Sie diesen Aktions-Button im Braze-Dashboard mit der zugehörigen Deeplink-URL einrichten. Es ist jedoch nicht erforderlich, einen Button auf dem Dashboard zu definieren,`KEEP_IDENTIFIER`da dieser lediglich die Benachrichtigung schließt. Auf dem Dashboard müssen Sie lediglich den Kategorienamen eingeben (zum Beispiel )`YOUR_CATEGORY`, der mit dem Namen übereinstimmt, den Sie in Ihrem App-Code registriert haben.

## Anpassen von Badges

Badges sind kleine Symbole, die dazu dienen, die Aufmerksamkeit eines Benutzers zu gewinnen. Sie können die Anzahl der Badges auf dem Tab [**„Einstellungen“**]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=swift#swift_settings) festlegen, wenn Sie eine Push-Benachrichtigung über das Braze-Dashboard erstellen. Sie können die Anzahl der Badges auch manuell über die Eigenschaft [`applicationIconBadgeNumber`](https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIApplication_Class/index.html#//apple_ref/occ/instp/UIApplication/applicationIconBadgeNumber) Ihrer Anwendung oder die [remote Benachrichtigungs-Payload](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CreatingtheNotificationPayload.html#//apple_ref/doc/uid/TP40008194-CH10-SW1) aktualisieren. 

Braze löscht automatisch die Anzahl der Badges, wenn eine Braze-Benachrichtigung empfangen wird, während die App im Vordergrund ist. Wenn Sie die Badge-Nummer manuell auf 0 setzen, werden auch die Benachrichtigungen in der Benachrichtigungszentrale gelöscht. 

Wenn Sie nicht vorhaben, die Badges im Rahmen des normalen Betriebs der App oder durch das Senden von Push-Nachrichten zu löschen, sollten Sie die Badges löschen, wenn die App aktiv wird, indem Sie den folgenden Code in die Delegate-Methode `applicationDidBecomeActive:` Ihrer App einfügen:

{% tabs %}
{% tab swift %}

```swift
// For iOS 16.0+
let center = UNUserNotificationCenter.current()
do {
  try await center.setBadgeCount(0)
} catch {
  // Handle errors
}

// Prior to iOS 16. Deprecated in iOS 17+.
UIApplication.shared.applicationIconBadgeNumber = 0
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
// For iOS 16.0+
UNUserNotificationCenter *center = [UNUserNotificationCenter currentNotificationCenter];
[center setBadgeCount:0 withCompletionHandler:^(NSError * _Nullable error) {
    if (error != nil) {
        // Handle errors
    }
}];

// Prior to iOS 16. Deprecated in iOS 17+.
[UIApplication sharedApplication].applicationIconBadgeNumber = 0;
```

{% endtab %}
{% endtabs %}

## Anpassen von Sounds

### Schritt 1: Integrieren Sie den Ton in Ihre App.

Benutzerdefinierte Push-Benachrichtigungstöne müssen lokal innerhalb des Haupt-Bundles Ihrer App gehostet werden. Die folgenden Audiodatenformate werden akzeptiert:

- Lineare PCM
- MA4
- µLaw
- aLaw

Sie können die Audiodaten in eine AIFF-, WAV- oder CAF-Datei packen. In Xcode fügen Sie die Sounddatei als nicht lokalisierte Ressource des Anwendungsbundles zu Ihrem Projekt hinzu.

{% alert note %}
Benutzerdefinierte Sounds müssen beim Abspielen unter 30 Sekunden bleiben. Wenn ein angepasster Sound dieses Limit überschreitet, wird stattdessen der standardmäßige Systemton abgespielt.
{% endalert %}

#### Konvertieren von Tondateien

Sie können das Tool afconvert verwenden, um Töne zu konvertieren. Um zum Beispiel den linearen 16-Bit-PCM-Systemton Submarine.aiff in IMA4-Audio in einer CAF-Datei zu konvertieren, verwenden Sie den folgenden Befehl im Terminal:

```bash
afconvert /System/Library/Sounds/Submarine.aiff ~/Desktop/sub.caf -d ima4 -f caff -v
```

{% alert tip %}
Sie können einen Sound untersuchen, um sein Datenformat zu bestimmen, indem Sie ihn im QuickTime Player öffnen und im Menü **Film** die Option **Filminspektor anzeigen** wählen.
{% endalert %}

### Schritt 2: Bitte geben Sie eine Protokoll-URL für den Ton an.

Sie müssen eine Protokoll-URL angeben, die auf den Speicherort der Sounddatei in Ihrer App verweist. Hierzu gibt es gibt zwei Methoden:

* Verwenden Sie den Parameter `sound` des [Apple Push-Objekts]({{site.baseurl}}/api/objects_filters/messaging/apple_object#apple-push-object), um die URL an Braze zu übergeben.
* Geben Sie die URL im Dashboard an. Wählen Sie im [Push Composer]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#step-3-select-notification-type-ios-and-android) **Einstellungen** und geben Sie die Protokoll-URL in das Feld **Sound** ein. 

![Der Push-Composer im Braze-Dashboard]({% image_buster /assets/img_archive/sound_push_ios.png %})

Wenn die angegebene Sounddatei nicht existiert oder das Schlüsselwort "default" eingegeben wird, verwendet Braze den standardmäßigen Alarmton des Geräts. Neben unserem Dashboard kann der Ton auch über unsere [Messaging-API] konfiguriert werden.

Weitere Informationen finden Sie in der Apple-Entwicklerdokumentation zur [Vorbereitung von benutzerdefinierten Warntönen](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/SupportingNotificationsinYourApp.html).

## Einstellungen

Wenn Sie über das Dashboard eine Push-Kampagne erstellen, klicken Sie im Schritt **„Erstellen“** auf die Registerkarte **„Einstellungen“,** um die verfügbaren erweiterten Einstellungen anzuzeigen.

![]({% image_buster /assets/img_archive/ios_advanced_settings.png %})

### Schlüssel-Wert-Paare

Braze erlaubt Ihnen, angepasste String-Schlüssel-Wert-Paare, bekannt als `extras`, zusammen mit einer Push-Benachrichtigung an Ihre Anwendung zu senden. Extras können über das Dashboard oder die API definiert werden und stehen dann als Schlüssel-Wert-Paare im Wörterbuch `notification` zur Verfügung, das an Ihre Push-Delegate-Implementierungen weitergegeben wird.

### Meldungsoptionen

Wählen Sie das Kontrollkästchen **„Benachrichtigungsoptionen“** aus, um ein Dropdown-Menü mit Schlüsselwerten anzuzeigen, mit denen Sie die Darstellung der Benachrichtigung auf Geräten anpassen können.

### Hinzufügen eines Flags für verfügbaren Content

Aktivieren Sie das Kontrollkästchen **Flag für verfügbaren Content hinzufügen**, um die Geräte anzuweisen, neue Inhalte im Hintergrund herunterzuladen. In der Regel können Sie diese Option aktivieren, wenn Sie [stille Benachrichtigungen]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift) versenden möchten.

### Hinzufügen eines Flags für veränderbaren Content

Aktivieren Sie das Kontrollkästchen **Flag für veränderbare Inhalte hinzufügen**, um die erweiterte Empfängeranpassung zu aktivieren. Dieses Flag wird automatisch gesendet, wenn Sie eine [Rich-Benachrichtigung]({{site.baseurl}}/developer_guide/push_notifications/rich/?sdktab=swift) verfassen, unabhängig vom Wert dieses Kontrollkästchens.

### Reduzierungs-ID

Geben Sie eine ID an, um ähnliche Benachrichtigungen zusammenzufassen. Wenn Sie mehrere Benachrichtigungen mit der gleichen Collapse ID senden, zeigt das Gerät nur die zuletzt empfangene Benachrichtigung an. Lesen Sie die Dokumentation von Apple über [zusammengefasste Benachrichtigungen](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1).

### Ablauf

Wenn Sie das Kontrollkästchen **Ablauf** aktivieren, können Sie eine Ablaufzeit für Ihre Nachricht festlegen. Sollte das Gerät eines Nutzers:innen die Verbindung verlieren, wird Braze weiterhin versuchen, die Nachricht bis zur angegebenen Zeit zu senden. Wenn dieser Wert nicht eingestellt ist, wird die Plattform standardmäßig auf einen Ablauf von 30 Tagen eingestellt. Beachten Sie, dass Push-Benachrichtigungen, die vor der Zustellung ablaufen, nicht als fehlgeschlagen gelten und nicht als Bounce registriert werden.
