{% multi_lang_include developer_guide/prerequisites/swift.md %} Sie müssen auch [Push-Benachrichtigungen einrichten]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift).

## Anpassen von Aktions-Buttons {#push-action-buttons-integration}

Das Braze Swift SDK bietet Unterstützung für Push-Action-Buttons bei der URL-Verarbeitung. Es gibt vier Sätze von standardmäßigen Push-Action-Buttons für die Standard-Push-Kategorien von Braze: `Accept/Decline`, `Yes/No`, `Confirm/Cancel` und `More`.

![Ein GIF einer Push-Nachricht, die nach unten gezogen wird, um zwei anpassbare Aktions-Buttons anzuzeigen.]({% image_buster /assets/img_archive/iOS8Action.gif %}){: style="max-width:60%"}

### Manuelles Registrieren von Aktions-Buttons

{% alert important %}
Die manuelle Registrierung von Push-Action-Buttons wird nicht empfohlen.
{% endalert %}

Wenn Sie [Push-Benachrichtigungen]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) mit der Konfigurationsoption `configuration.push.automation` [einrichten]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift), registriert Braze automatisch die Aktions-Buttons für die Standard-Push-Kategorien und kümmert sich um die Analytics der Push-Action-Buttons für Klicks und das URL-Routing.

Sie können jedoch auch Push-Action-Buttons manuell registrieren.

#### Schritt 1: Hinzufügen von Braze Standard Push-Kategorien {#registering}

Verwenden Sie den folgenden Code, um sich für die Standard Push-Kategorien zu registrieren, wenn Sie sich für [Push anmelden]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-4-register-push-tokens-with-braze):

{% tabs %}
{% tab schnell %}
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
{% tab schnell %}

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

## Anpassen von Push-Kategorien {#customizing-push-categories}

Braze bietet nicht nur eine Reihe von Standard Push-Kategorien, sondern unterstützt auch angepasste Benachrichtigungskategorien und Aktionen. Nachdem Sie Kategorien in Ihrer Anwendung registriert haben, können Sie das Braze-Dashboard verwenden, um diese angepassten Benachrichtigungskategorien an Ihre Nutzer:innen zu senden.

Hier ist ein Beispiel, das die `LIKE_CATEGORY` nutzt, die auf dem Gerät angezeigt wird:

![Eine Push Nachricht, die die zwei Push-Action-Buttons "unlike" und "like" zeigt.]({% image_buster /assets/img_archive/push_example_category.png %})

### Schritt 1: Eine Kategorie registrieren

Um eine Kategorie in Ihrer App zu registrieren, gehen Sie ähnlich vor wie im Folgenden beschrieben:

{% tabs %}
{% tab schnell %}

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
Wenn Sie eine `UNNotificationAction` erstellen, können Sie eine Liste von Aktionsoptionen angeben. Mit `UNNotificationActionOptions.foreground` können Ihre Nutzer zum Beispiel Ihre App öffnen, nachdem sie auf den Aktions-Button getippt haben. Dies ist notwendig für navigatorische On-Click-Verhaltensweisen wie "Open App" und "Deep Link Into Application". Für weitere Informationen siehe [`UNNotificationActionOptions`](https://developer.apple.com/documentation/usernotifications/unnotificationactionoptions).
{% endalert %}

### Schritt 2: Wählen Sie Ihre Kategorien aus

Nachdem Sie eine Kategorie registriert haben, verwenden Sie das Braze-Dashboard, um Benachrichtigungen dieses Typs an Nutzer:innen zu senden.

{% alert tip %}
Sie müssen nur angepasste Benachrichtigungskategorien für Aktions-Buttons mit _speziellen Aktionen_ definieren, wie z.B. Deeplinking in Ihre App setzen oder eine URL öffnen. Für Aktions-Buttons, die lediglich eine Benachrichtigung schließen, müssen Sie diese nicht definieren.
{% endalert %}

1. Wählen Sie im Braze-Dashboard **Messaging** > **Push-Benachrichtigungen** und wählen Sie dann Ihre iOS [Push-Kampagne]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message).
2. Schalten Sie unter **Push-Benachrichtigung verfassen** die **Aktions-Buttons** ein.
3. Wählen Sie in der Dropdown-Liste **iOS-Benachrichtigungskategorie** die Option **Vorregistrierte, angepasste iOS-Kategorie eingeben**.
4. Geben Sie schließlich eine der Kategorien ein, die Sie zuvor erstellt haben. Das folgende Beispiel verwendet die angepasste Kategorie: `LIKE_CATEGORY`.

![Das Dashboard für Push-Benachrichtigungen in Kampagnen mit der Möglichkeit, angepasste Kategorien einzurichten.]({% image_buster /assets/img_archive/ios-notification-category.png %})

## Anpassen von Badges

Badges sind kleine Symbole, die dazu dienen, die Aufmerksamkeit eines Benutzers zu gewinnen. Sie können die Anzahl der Badges in den [**Einstellungen**]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=swift#swift_settings) Tab festlegen, wenn Sie eine Push-Benachrichtigung über das Braze-Dashboard verfassen. Sie können die Anzahl der Badges auch manuell über die Eigenschaft [`applicationIconBadgeNumber`](https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIApplication_Class/index.html#//apple_ref/occ/instp/UIApplication/applicationIconBadgeNumber) Ihrer Anwendung oder die [remote Benachrichtigungs-Payload](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CreatingtheNotificationPayload.html#//apple_ref/doc/uid/TP40008194-CH10-SW1) aktualisieren. 

Braze löscht automatisch die Anzahl der Badges, wenn eine Braze-Benachrichtigung empfangen wird, während die App im Vordergrund ist. Wenn Sie die Badge-Nummer manuell auf 0 setzen, werden auch die Benachrichtigungen in der Benachrichtigungszentrale gelöscht. 

Wenn Sie nicht vorhaben, die Badges im Rahmen des normalen Betriebs der App oder durch das Senden von Push-Nachrichten zu löschen, sollten Sie die Badges löschen, wenn die App aktiv wird, indem Sie den folgenden Code in die Delegate-Methode `applicationDidBecomeActive:` Ihrer App einfügen:

{% tabs %}
{% tab schnell %}

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

## Anpassen von Klängen

### Schritt 1: Hosten Sie den Ton in Ihrer App

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

### Schritt 2: Geben Sie eine Protokoll-URL für den Sound an

Sie müssen eine Protokoll-URL angeben, die auf den Speicherort der Sounddatei in Ihrer App verweist. Hierzu gibt es gibt zwei Methoden:

* Verwenden Sie den Parameter `sound` des [Apple Push-Objekts]({{site.baseurl}}/api/objects_filters/messaging/apple_object#apple-push-object), um die URL an Braze zu übergeben.
* Geben Sie die URL im Dashboard an. Wählen Sie im [Push Composer]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#step-3-select-notification-type-ios-and-android) **Einstellungen** und geben Sie die Protokoll-URL in das Feld **Sound** ein. 

![Push Composer im Braze-Dashboard]({% image_buster /assets/img_archive/sound_push_ios.png %})

Wenn die angegebene Sounddatei nicht existiert oder das Schlüsselwort "default" eingegeben wird, verwendet Braze den standardmäßigen Alarmton des Geräts. Abgesehen von unserem Dashboard kann der Ton auch über unsere [Messaging API][12]] konfiguriert werden.

Weitere Informationen finden Sie in der Apple-Entwicklerdokumentation zur [Vorbereitung von benutzerdefinierten Warntönen](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/SupportingNotificationsinYourApp.html).

## Einstellungen

Wenn Sie eine Push-Kampagne über das Dashboard erstellen, klicken Sie im Schritt **Verfassen** auf den Tab **Einstellungen**, um die verfügbaren fortschrittlichen Einstellungen anzuzeigen.

![]({% image_buster /assets/img_archive/ios_advanced_settings.png %})

### Schlüssel-Wert-Paare

Braze erlaubt Ihnen, angepasste String-Schlüssel-Wert-Paare, bekannt als `extras`, zusammen mit einer Push-Benachrichtigung an Ihre Anwendung zu senden. Extras können über das Dashboard oder die API definiert werden und stehen dann als Schlüssel-Wert-Paare im Wörterbuch `notification` zur Verfügung, das an Ihre Push-Delegate-Implementierungen weitergegeben wird.

### Meldungsoptionen

Wählen Sie das Kontrollkästchen **Benachrichtigungsoptionen** aus, um eine Dropdown-Liste mit Schlüsselwerten anzuzeigen, mit denen Sie die Anzeige der Benachrichtigung auf den Geräten anpassen können.

### Hinzufügen eines Flags für verfügbaren Content

Aktivieren Sie das Kontrollkästchen **Flag für verfügbaren Content hinzufügen**, um die Geräte anzuweisen, neue Inhalte im Hintergrund herunterzuladen. In der Regel können Sie diese Option aktivieren, wenn Sie [stille Benachrichtigungen]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift) versenden möchten.

### Hinzufügen eines Flags für veränderbaren Content

Aktivieren Sie das Kontrollkästchen **Flag für veränderbare Inhalte hinzufügen**, um die erweiterte Empfängeranpassung zu aktivieren. Dieses Flag wird automatisch gesendet, wenn Sie eine [Rich-Benachrichtigung]({{site.baseurl}}/developer_guide/push_notifications/rich/?sdktab=swift) verfassen, unabhängig vom Wert dieses Kontrollkästchens.

### Reduzierungs-ID

Geben Sie eine ID an, um ähnliche Benachrichtigungen zusammenzufassen. Wenn Sie mehrere Benachrichtigungen mit der gleichen Collapse ID senden, zeigt das Gerät nur die zuletzt empfangene Benachrichtigung an. Lesen Sie die Dokumentation von Apple über [zusammengefasste Benachrichtigungen](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1).

### Ablauf

Wenn Sie das Kontrollkästchen **Ablauf** aktivieren, können Sie eine Ablaufzeit für Ihre Nachricht festlegen. Sollte das Gerät eines Nutzers:innen die Verbindung verlieren, wird Braze weiterhin versuchen, die Nachricht bis zur angegebenen Zeit zu senden. Wenn dieser Wert nicht eingestellt ist, wird die Plattform standardmäßig auf einen Ablauf von 30 Tagen eingestellt. Beachten Sie, dass Push-Benachrichtigungen, die vor der Zustellung ablaufen, nicht als fehlgeschlagen gelten und nicht als Bounce registriert werden.
