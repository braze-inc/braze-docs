---
nav_title: Benutzerdefiniertes On-Click-Verhalten
article_title: Anpassen des On-Click-Verhaltens von In-App-Nachrichten für iOS
platform: iOS
page_order: 5
description: "Dieser Referenzartikel behandelt das benutzerdefinierte On-Click-Verhalten bei In-App-Nachrichten für Ihre iOS-Anwendung."
channel:
  - in-app messages
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Anpassen des Verhaltens von In-App-Nachrichten bei Klick

{% alert note %}
Dieser Artikel enthält Informationen zum News Feed, der nicht mehr verwendet wird. Braze empfiehlt Kunden, die unser News Feed-Tool verwenden, auf unseren Nachrichtenkanal Content Cards umzusteigen - er ist flexibler, anpassbarer und zuverlässiger. Weitere Informationen finden Sie im [Migrationsleitfaden]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/).
{% endalert %}

Die Eigenschaft `inAppMessageClickActionType` von `ABKInAppMessage` definiert das Aktionsverhalten nach dem Klicken auf die In-App-Nachricht. Diese Eigenschaft ist schreibgeschützt. Wenn Sie das Klickverhalten der In-App-Nachricht ändern möchten, können Sie die folgende Methode auf `ABKInAppMessage` aufrufen:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[inAppMessage setInAppMessageClickAction:clickActionType withURI:uri];
```

{% endtab %}
{% tab schnell %}

```swift
inAppMessage.setInAppMessageClickAction(clickActionType: clickActionType, withURI: uri)
```

{% endtab %}
{% endtabs %}

Die `inAppMessageClickActionType` kann auf einen der folgenden Werte eingestellt werden:

| `ABKInAppMessageClickActionType` | On-Click-Verhalten |
| -------------------------- | -------- |
| `ABKInAppMessageDisplayNewsFeed` | Der Newsfeed wird angezeigt, wenn auf die Nachricht geklickt wird, und die Nachricht wird ausgeblendet. Beachten Sie, dass der Parameter `uri` ignoriert und die Eigenschaft `uri` von `ABKInAppMessage` auf Null gesetzt wird. |
| `ABKInAppMessageRedirectToURI` | Die angegebene URI wird angezeigt, wenn auf die Nachricht geklickt wird, und die Nachricht wird ausgeblendet. Beachten Sie, dass der Parameter `uri` nicht Null sein darf. |
| `ABKInAppMessageNoneClickAction` | Die Nachricht wird ausgeblendet, wenn sie angeklickt wird. Beachten Sie, dass der Parameter `uri` ignoriert und die Eigenschaft `uri` von `ABKInAppMessage` auf Null gesetzt wird. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Bei In-App-Nachrichten mit Buttons wird die `clickAction` der Nachricht ebenfalls in die endgültige Nutzlast aufgenommen, wenn die Klickaktion vor dem Hinzufügen des Button-Textes hinzugefügt wird.
{% endalert %}

## Anpassen von Klicks auf In-App-Nachrichtentexte

Wenn auf eine In-App-Nachricht geklickt wird, wird die folgende Delegate-Methode [`ABKInAppMessageUIDelegate`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyUI/ABKInAppMessage/ABKInAppMessageUIDelegate.h) aufgerufen:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (BOOL) onInAppMessageClicked:(ABKInAppMessage *)inAppMessage;
```

{% endtab %}
{% tab schnell %}

```swift
func onInAppMessageClicked(inAppMessage: ABKInAppMessage!) -> Bool
```

{% endtab %}
{% endtabs %}

## Anpassen von Klicks auf Buttons in In-App-Nachrichten

Für Klicks auf In-App-Nachrichten-Buttons und HTML-In-App-Nachrichten-Buttons (z. B. Links) enthält [`ABKInAppMessageUIDelegate`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyUI/ABKInAppMessage/ABKInAppMessageUIDelegate.h) die folgenden Delegate-Methoden:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (BOOL)onInAppMessageButtonClicked:(ABKInAppMessageImmersive *)inAppMessage
                             button:(ABKInAppMessageButton *)button;

- (BOOL)onInAppMessageHTMLButtonClicked:(ABKInAppMessageHTML *)inAppMessage
                             clickedURL:(nullable NSURL *)clickedURL
                               buttonID:(NSString *)buttonID;
```

{% endtab %}
{% tab schnell %}

```swift
func onInAppMessageButtonClicked(inAppMessage: ABKInAppMessageImmersive!,
                                 button: ABKInAppMessageButton) -> Bool

func onInAppMessageHTMLButtonClicked(inAppMessage: ABKInAppMessageHTML!,
                                     clickedURL: URL, buttonID: String) -> Bool
```

{% endtab %}
{% endtabs %}

Jede Methode gibt einen `BOOL`-Wert zurück, der angibt, ob Braze die Klickaktion weiter ausführen soll.

Mit dem folgenden Code können Sie auf den Typ der Klickaktion eines Buttons in einer Delegate-Methode zugreifen:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
if ([inAppMessage isKindOfClass:[ABKInAppMessageImmersive class]]) {
      ABKInAppMessageImmersive *immersiveIAM = (ABKInAppMessageImmersive *)inAppMessage;
      NSArray<ABKInAppMessageButton *> *buttons = immersiveIAM.buttons;
      for (ABKInAppMessageButton *button in buttons) {
         // Button action type is accessible via button.buttonClickActionType
      }
   }
```

{% endtab %}
{% tab schnell %}

```swift
if inAppMessage is ABKInAppMessageImmersive {
      let immersiveIAM = inAppMessage as! ABKInAppMessageImmersive;
      for button in inAppMessage.buttons as! [ABKInAppMessageButton]{
        // Button action type is accessible via button.buttonClickActionType
      }
    }
```

{% endtab %}
{% endtabs %}

Wenn eine In-App-Nachricht Buttons enthält, werden nur die Klickaktionen auf dem Modell `ABKInAppMessageButton` ausgeführt. Der Text der In-App-Nachricht kann nicht angeklickt werden, obwohl dem Modell `ABKInAppMessage` die standardmäßige Klickaktion ("Newsfeed") zugewiesen wurde.

## Methoden-Deklarationen

Weitere Informationen finden Sie in den folgenden Header-Dateien:

- [`ABKInAppMessage.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessage.h)

