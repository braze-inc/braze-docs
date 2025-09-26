---
nav_title: Verhalten
article_title: Anpassen des Verhaltens von Content-Cards
page_order: 2
description: "In diesem Implementierungsleitfaden werden Änderungen am Verhalten von Content-Cards, das Hinzufügen von Extras wie Schlüssel-Wert-Paaren zur Nutzlast und Vorgehensweisen für gängige Anpassungen erläutert."
channel:
  - content cards
platform:
  - Android
  - FireOS
  - Swift
  - Web
---

# Anpassen des Verhaltens von Content-Cards

> In diesem Implementierungsleitfaden werden Änderungen am Verhalten von Content-Cards, das Hinzufügen von Extras wie Schlüssel-Wert-Paaren zur Nutzlast und Vorgehensweisen für gängige Anpassungen erläutert. Eine vollständige Liste der Content-Card-Typen finden Sie unter [Über Content-Cards]({{site.baseurl}}/developer_guide/content_cards/). 

## Schlüssel-Wert-Paare

Mit Braze können Sie zusätzliche Daten-Nutzlasten über Content-Cards an Nutzergeräte senden, indem Sie Schlüssel-Wert-Paare verwenden. Diese können Ihnen helfen, interne Metriken zu tracken, App-Inhalte zu aktualisieren und Eigenschaften anzupassen. [Fügen Sie Schlüssel-Wert-Paare über das Dashboard hinzu]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create#step-4-configure-additional-settings-optional). 
 
{% alert note %}
Wir raten davon ab, verschachtelte JSON-Werte als Schlüssel-Wert-Paare zu senden. Stattdessen sollten die JSON-Werte vor dem Senden durch Flatten vereinfacht werden.
{% endalert %}

{% tabs %}
{% tab android %}

Schlüssel-Wert-Paare werden in Objekten des Typs <a href="https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/#-2118252107%2FProperties%2F-1725759721" target="_blank">`card`</a> als `extras` gespeichert. Diese können verwendet werden, um Daten zusammen mit einer Karte zur weiteren Bearbeitung durch die Anwendung zu senden. Rufen Sie <a href="https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/extras.html" target="_blank">`card.extras`</a> auf, um auf diese Werte zuzugreifen.

{% endtab %}
{% tab schnell %}

Schlüssel-Wert-Paare werden in Objekten des Typs <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard" target="_blank">`card`</a> als `extras` gespeichert. Diese können verwendet werden, um Daten zusammen mit einer Karte zur weiteren Bearbeitung durch die Anwendung zu senden. Rufen Sie <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/data-swift.struct/extras" target="_blank">`card.extras`</a> auf, um auf diese Werte zuzugreifen.

{% endtab %}
{% tab Internet %}

Schlüssel-Wert-Paare werden in Objekten des Typs <a href="https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html" target="_blank">`card`</a> als `extras` gespeichert. Diese können verwendet werden, um Daten zusammen mit einer Karte zur weiteren Bearbeitung durch die Anwendung zu senden. Rufen Sie `card.extras` auf, um auf diese Werte zuzugreifen.

{% endtab %}
{% endtabs %}

{% alert tip %}
Es ist wichtig, dass sich Ihre Marketing- und Entwicklerteams darüber abstimmen, welche Schlüssel-Wert-Paare verwendet werden sollen (z.B. `feed_type = brand_homepage`), denn alle Schlüssel-Wert-Paare, die Marketer in das Braze-Dashboard eingeben, müssen exakt mit den Schlüssel-Wert-Paaren übereinstimmen, die die Entwickler in die App-Logik einbauen.
{% endalert %}

## Content Cards als zusätzlicher Inhalt

![]({% image_buster /assets/img/cc_implementation/supplementary.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0;"}

Sie können Content-Cards nahtlos in einen bestehenden Feed einfügen, sodass Daten aus mehreren Feeds gleichzeitig geladen werden können. Dadurch entsteht ein zusammenhängendes, harmonisches Erlebnis mit Braze Content-Cards und vorhandenen Feed-Inhalten.

Das Beispiel auf der rechten Seite zeigt einen Feed mit einer hybriden Liste von Artikeln, die über lokale Daten und Braze Content-Cards gefüllt werden. Auf diese Weise können Content Cards ununterscheidbar neben bestehenden Inhalten stehen.

### API-getriggerte Schlüssel-Werte-Paare

[API-gesteuerte Kampagnen]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/) sind eine gute Strategie, wenn die Werte einer Karte von externen Faktoren abhängen, um zu bestimmen, welche Inhalte dem Benutzer angezeigt werden sollen. Um zum Beispiel zusätzliche Inhalte anzuzeigen, legen Sie Schlüssel-Wert-Paare mit Liquid fest. Beachten Sie, dass `class_type` zum Zeitpunkt der Einrichtung bekannt sein sollte.

![Die Schlüssel-Wert-Paare für den Anwendungsfall mit Content-Cards. In diesem Beispiel werden verschiedene Aspekte der Karte wie "tile_id", "tile_deeplink" und "tile_title" mit Liquid festgelegt.]({% image_buster /assets/img/cc_implementation/supplementary_content.png %}){: style="max-width:60%;"}

## Content Cards als interaktive Inhalte
![Unten links im Bildschirm erscheint eine interaktive Content-Card mit einer 50-Prozent-Rabattaktion. Nachdem Sie darauf geklickt haben, wird eine Aktion auf den Warenkorb angewendet.]({% image_buster /assets/img/cc_implementation/discount2.png %}){: style="border:0;"}{: style="float:right;max-width:45%;border:0;margin-left:15px;"} 

Content-Cards können genutzt werden, um dynamische und interaktive Erlebnisse für Ihre Nutzer zu schaffen. Im Beispiel auf der rechten Seite erscheint an der Kasse ein Popup-Fenster mit einer Inhaltskarte, die den Benutzern Last-Minute-Angebote bietet. Gut platzierte Karten wie diese sind eine großartige Möglichkeit, den Nutzern einen "Anstoß" zu bestimmten Aktionen zu geben. 

Die Schlüssel-Wert-Paare für diesen Anwendungsfall umfassen einen `discount_percentage`, der als gewünschter Rabattbetrag festgelegt ist, und einen `class_type`, der als `coupon_code` festgelegt ist. Mit diesen Schlüssel-Wert-Paaren können Sie typspezifische Content-Cards im Checkout-Bildschirm filtern und anzeigen. Weitere Informationen zur Verwendung von Schlüssel-Wert-Paaren zur Verwaltung mehrerer Feeds finden Sie unter [Anpassen des Standard-Content-Card-Feeds]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed/#multiple-feeds).
<br>
<br>

![]({% image_buster /assets/img/cc_implementation/discount.png %}){: style="max-width:80%;"} 

## Content-Card-Badges

![iPhone-Startbildschirm mit einer Braze-Beispielanwendung namens Swifty und einem roten Badge, das die Zahl 7 anzeigt]({% image_buster /assets/img/cc_implementation/ios-unread-badge.png %}){: style="max-width:35%;float:right;margin-left:15px;border:none;"}

Badges sind kleine Symbole, die dazu dienen, die Aufmerksamkeit eines Nutzers zu gewinnen. Mithilfe von Badges, die den Nutzer auf neue Content-Card-Inhalte aufmerksam machen, können Sie Ihre App wieder in das Bewusstsein der Nutzer rücken und die Anzahl der Sitzungen erhöhen.

### Anzeige der Anzahl der ungelesenen Content Cards als Badge

Sie können die Anzahl der ungelesenen Content-Cards anzeigen, die Ihr Nutzer als Badge auf dem Symbol Ihrer App sieht. 

{% tabs %}
{% tab android %}

Sie können die Anzahl der ungelesenen Karten jederzeit telefonisch erfragen:

{% subtabs %}
{% subtab Java %}

```java
Braze.getInstance(context).getContentCardUnviewedCount();
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
Braze.getInstance(context).contentCardUnviewedCount
```

{% endsubtab %}
{% endsubtabs %}

Anhand dieser Informationen können Sie dann ein Badge anzeigen, das die Anzahl der ungelesenen Content-Cards angibt. Weitere Informationen finden Sie in der <a href="https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/get-content-card-unviewed-count.html" target="_blank">SDK-Referenzdokumentation</a>.


{% endtab %}
{% tab schnell %}

Das folgende Beispiel verwendet `braze.contentCards`, um die Anzahl der ungelesenen Content-Cards abzufragen und anzuzeigen. Nachdem die App geschlossen und die Sitzung des Benutzers beendet wurde, fordert dieser Code eine Kartenzählung an und filtert die Anzahl der Karten anhand der Eigenschaft `viewed`.

{% subtabs %}
{% subtab Swift %}

```swift
func applicationDidEnterBackground(_ application: UIApplication)
```

Implementieren Sie innerhalb dieser Methode den folgenden Code, der den Badge-Zähler aktiv aktualisiert, wenn der Nutzer in einer bestimmten Sitzung Karten ansieht:

```swift
let unreadCards = AppDelegate.braze?.contentCards.cards.filter { $0.viewed == false }
UIApplication.shared.applicationIconBadgeNumber = unreadCards?.count ?? 0
```

{% endsubtab %}
{% subtab Objective-C %}

```objc
(void)applicationDidEnterBackground:(UIApplication *)application
```

Implementieren Sie innerhalb dieser Methode den folgenden Code, der den Badge-Zähler aktiv aktualisiert, wenn der Nutzer in einer bestimmten Sitzung Karten ansieht:

```objc
NSInteger unreadCardCount = 0;
for (BRZContentCardRaw *card in AppDelegate.braze.contentCards.cards) {
  if (card.viewed == NO) {
    unreadCardCount += 1;
  }
}
[UIApplication sharedApplication].applicationIconBadgeNumber = unreadCardCount;
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Internet %}

Sie können die Anzahl der ungelesenen Karten jederzeit telefonisch erfragen:

```javascript
braze.getCachedContentCards().getUnviewedCardCount();
```

Anhand dieser Informationen können Sie dann ein Badge anzeigen, das die Anzahl der ungelesenen Content-Cards angibt. Weitere Informationen finden Sie in der <a href="https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.contentcards.html" target="_blank">SDK-Referenzdokumentation</a>.

{% endtab %}
{% endtabs %}


