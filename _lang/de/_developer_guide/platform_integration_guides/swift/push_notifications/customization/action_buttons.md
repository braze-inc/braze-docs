---
nav_title: Aktions-Buttons
article_title: Push Action-Buttons für iOS
platform: Swift
page_order: 1
description: "Dieser Artikel beschreibt, wie Sie Aktions-Buttons in Ihre iOS Push-Benachrichtigungen für das Swift SDK implementieren."
channel:
  - push

---

# Aktions-Buttons {#push-action-buttons-integration}

> Das Braze Swift SDK bietet Unterstützung für Push-Action-Buttons bei der URL-Verarbeitung. 

Es gibt vier Sätze von standardmäßigen Push-Action-Buttons für die Standard-Push-Kategorien von Braze: `Accept/Decline`, `Yes/No`, `Confirm/Cancel` und `More`. 

![Ein GIF einer Push-Nachricht, die nach unten gezogen wird, um zwei anpassbare Aktions-Buttons anzuzeigen.]({% image_buster /assets/img_archive/iOS8Action.gif %}){: style="max-width:60%"}

Wenn Sie Ihre eigenen angepassten Benachrichtigungskategorien erstellen möchten, sehen Sie sich die [Anpassung der Aktions-Buttons an](#push-category-customization).

## Automatische Integration (empfohlen)

Bei der Integration von Push mit der Konfigurationsoption `configuration.push.automation` registriert Braze automatisch die Aktions-Buttons für die Standard-Push-Kategorien und kümmert sich um die Analytics der Push-Action-Buttons für Klicks und das URL-Routing.

## Manuelle Integration

Um diese Push-Action-Buttons manuell zu aktivieren, registrieren Sie sich zunächst für die Standard-Push-Kategorien. Verwenden Sie dann die Delegate-Methode `didReceive(_:completionHandler:)`, um Push-Action-Buttons zu aktivieren.

### Schritt 1: Hinzufügen von Braze Standard Push-Kategorien {#registering}

Verwenden Sie den folgenden Code, um sich für die Standard Push-Kategorien zu registrieren, wenn Sie sich für [Push anmelden]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-4-register-push-tokens-with-braze):

{% tabs %}
{% tab schnell %}

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

### Schritt 2: Aktivierung der interaktiven Push-Bearbeitung {#enable-push-handling}

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

## Anpassung der Push-Kategorie

Braze bietet nicht nur eine Reihe von Standard Push-Kategorien, sondern unterstützt auch angepasste Benachrichtigungskategorien und Aktionen. Nachdem Sie Kategorien in Ihrer Anwendung registriert haben, können Sie das Braze-Dashboard verwenden, um diese angepassten Benachrichtigungskategorien an Ihre Nutzer:innen zu senden.

Diese Kategorien können dann über unser Dashboard Push-Benachrichtigungen zugewiesen werden, um die Aktion-Button-Konfigurationen Ihres Designs zu triggern. 

### Beispiel angepasste Push-Kategorie

Hier ist ein Beispiel, das die `LIKE_CATEGORY` nutzt, die auf dem Gerät angezeigt wird:

![Eine Push Nachricht, die die zwei Push-Action-Buttons "unlike" und "like" zeigt.]({% image_buster /assets/img_archive/push_example_category.png %})

#### Schritt 1: Eine Kategorie registrieren

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

#### Schritt 2: Wählen Sie Ihre Kategorien aus

Nachdem Sie eine Kategorie registriert haben, verwenden Sie das Braze-Dashboard, um Benachrichtigungen dieses Typs an Nutzer:innen zu senden.

{% alert tip %}
Sie müssen nur angepasste Benachrichtigungskategorien für Aktions-Buttons mit _speziellen Aktionen_ definieren, wie z.B. Deeplinking in Ihre App setzen oder eine URL öffnen. Für Aktions-Buttons, die lediglich eine Benachrichtigung schließen, müssen Sie diese nicht definieren.
{% endalert %}

1. Wählen Sie im Braze-Dashboard **Messaging** > **Push-Benachrichtigungen** und wählen Sie dann Ihre iOS [Push-Kampagne]({{site.baseurl}}/docs/user_guide/message_building_by_channel/push/creating_a_push_message).
2. Schalten Sie unter **Push-Benachrichtigung verfassen** die **Aktions-Buttons** ein.
3. Wählen Sie in der Dropdown-Liste **iOS-Benachrichtigungskategorie** die Option **Vorregistrierte, angepasste iOS-Kategorie eingeben**.
4. Geben Sie schließlich eine der Kategorien ein, die Sie zuvor erstellt haben. Das folgende Beispiel verwendet die angepasste Kategorie: `LIKE_CATEGORY`.

![Das Dashboard für Push-Benachrichtigungen in Kampagnen mit der Möglichkeit, angepasste Kategorien einzurichten.]({% image_buster /assets/img_archive/ios-notification-category.png %})

