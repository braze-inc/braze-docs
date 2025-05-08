---
nav_title: Benutzerdefiniertes On-Click-Verhalten
article_title: Anpassen des Klickverhaltens für In-App-Nachrichten für iOS
platform: Swift
page_order: 5
description: "Dieser Referenzartikel beschreibt, wie Sie das On-Click-Verhalten von iOS In-App-Nachrichten für das Swift SDK anpassen."
channel:
  - in-app messages
---

# Benutzerdefiniertes Verhalten beim Klicken

> Jedes Objekt des Typs `Braze.InAppMessage` enthält eine entsprechende [`ClickAction`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/clickaction), die das Verhalten beim Klicken definiert. 

Um dieses Verhalten anzupassen, können Sie die Eigenschaft `clickAction` ändern. Ziehen Sie dazu das folgende Beispiel zurate:

{% tabs %}
{% tab schnell %}

```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI, 
  prepareWith context: inout BrazeInAppMessageUI.PresentationContext
) {
  if let newUrl = URL(string: "{your-url}") {
    context.message.clickAction = .url(newUrl, useWebView: true)
  }
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

Die Methode `inAppMessage(_:prepareWith:)` ist in Objective-C nicht verfügbar.

{% endtab %}
{% endtabs %}

## Arten von Klickaktionen

Die Eigenschaft `clickAction` auf Ihrem `Braze.InAppMessage` ist standardmäßig auf `.none` eingestellt, kann aber auf einen der folgenden Werte gesetzt werden:

| `ClickAction` | On-Click-Verhalten |
| -------------------------- | -------- |
| `.url(URL, useWebView: Bool)` | Öffnet die angegebene URL in einem externen Browser. Wenn `useWebView` auf `true` festgelegt ist, wird sie in einer Webansicht geöffnet. |
| `.newsFeed` | Wenn auf die Nachricht geklickt wird, wird der Newsfeed angezeigt und die Nachricht ausgeblendet.<br><br>**Hinweis:** Der Newsfeed ist veraltet. Weitere Einzelheiten finden Sie in der [Migrationsanleitung]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/). |
| `.none` | Die Nachricht wird ausgeblendet, wenn sie angeklickt wird. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Bei In-App-Nachrichten mit Buttons wird die `clickAction` der Nachricht ebenfalls in die endgültige Nutzlast aufgenommen, wenn die Klickaktion vor dem Hinzufügen des Button-Textes hinzugefügt wird.
{% endalert %}

## Anpassen von In-App-Nachrichten und Button-Klicks

Wenn auf eine In-App-Nachricht geklickt wird, wird die folgende Delegate-Methode [`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate) aufgerufen: Für Klicks auf In-App-Nachrichten-Buttons und HTML-In-App Nachrichten-Buttons (Links) wird eine Button-ID als optionaler Parameter angegeben.

{% tabs %}
{% tab schnell %}

```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI,
  shouldProcess clickAction: Braze.InAppMessage.ClickAction,
  buttonId: String?,
  message: Braze.InAppMessage,
  view: InAppMessageView
) -> Bool
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (BOOL)inAppMessage:(BrazeInAppMessageUI *)ui
       shouldProcess:(enum BRZInAppMessageRawClickAction)clickAction
                 url:(NSURL *)uri
            buttonId:(NSString *)buttonId
             message:(BRZInAppMessageRaw *)message
                view:(UIView *)view;
```

{% endtab %}
{% endtabs %}

Diese Methode gibt einen booleschen Wert zurück, der angibt, ob Braze die Klickaktion weiter ausführen soll.

