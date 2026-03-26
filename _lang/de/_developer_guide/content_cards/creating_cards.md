---
nav_title: Karten erstellen
article_title: Content-Cards erstellen
page_order: 0
description: "Dieser Artikel behandelt die Komponenten zur Erstellung einer angepassten Content-Card UI."
channel:
  - content cards
platform:
  - Android
  - FireOS
  - Swift
  - Web
---

# Content-Cards erstellen

> Dieser Artikel beschreibt den grundlegenden Ansatz, den Sie bei der Implementierung angepasster Content-Cards verwenden, sowie drei häufige Anwendungsfälle. Es wird davon ausgegangen, dass Sie bereits die anderen Artikel der Anleitung zur Anpassung von Content-Cards gelesen haben, um zu verstehen, was standardmäßig möglich ist und was angepassten Code erfordert. Es ist besonders hilfreich zu verstehen, wie Sie [Analytics]({{site.baseurl}}/developer_guide/content_cards/logging_analytics/) für Ihre angepassten Content-Cards [protokollieren]({{site.baseurl}}/developer_guide/content_cards/logging_analytics/) können. 

{% multi_lang_include banners/content_card_alert.md %}

## Eine Karte erstellen

### 1. Schritt: Erstellen Sie ein angepasstes UI 

{% tabs local %}
{% tab web %}

Erstellen Sie zunächst Ihre angepasste HTML-Komponente, die zum Rendern der Karten verwendet werden soll. 

{% endtab %}
{% tab android %}

Erstellen Sie zunächst Ihr eigenes angepasstes Fragment. Das standardmäßige [`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html) ist nur für unsere Standard-Content-Card-Typen gedacht, ist aber ein guter Ausgangspunkt.

{% endtab %}
{% tab swift %}

Erstellen Sie zunächst Ihre eigene angepasste View-Controller-Komponente. Der standardmäßige [`BrazeContentCardUI.ViewController`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller) ist nur für unsere Standard-Content-Card-Typen gedacht, ist aber ein guter Ausgangspunkt.

{% endtab %}
{% endtabs %}

### 2. Schritt: Updates für Karten abonnieren

Registrieren Sie eine Callback-Funktion, um Daten-Updates zu abonnieren, wenn die Karten aktualisiert werden. Sie können die Content-Card-Objekte parsen und deren Payload-Daten wie `title`, `cardDescription` und `imageUrl` extrahieren und dann die resultierenden Modelldaten verwenden, um Ihr angepasstes UI zu befüllen.

Um die Content-Card-Datenmodelle zu erhalten, abonnieren Sie Content-Card-Updates. Achten Sie dabei besonders auf die folgenden Eigenschaften:

* **`id`:** Repräsentiert den Content-Card-ID-String. Dies ist der eindeutige Bezeichner, der zum Protokollieren von Analytics aus angepassten Content-Cards verwendet wird.
* **`extras`:** Umfasst alle Schlüssel-Wert-Paare aus dem Braze-Dashboard. 

Alle Eigenschaften außer `id` und `extras` sind für angepasste Content-Cards optional zu parsen. Weitere Informationen zum Datenmodell finden Sie im Integrationsartikel der jeweiligen Plattform: [Android]({{site.baseurl}}/developer_guide/content_cards/?sdktab=android), [iOS]({{site.baseurl}}/developer_guide/content_cards/?sdktab=swift), [Web]({{site.baseurl}}/developer_guide/content_cards/?sdktab=web).

{% tabs local %}
{% tab web %}

```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToContentCardsUpdates((updates) => {
  const cards = updates.cards;
// For example:
  cards.forEach(card => {
    if (card.isControl) {
      // Do not display the control card, but remember to call `logContentCardImpressions([card])`
    }
    else if (card instanceof braze.ClassicCard || card instanceof braze.CaptionedImage) {
      // Use `card.title`, `card.imageUrl`, etc.
    }
    else if (card instanceof braze.ImageOnly) {
      // Use `card.imageUrl`, etc.
    }
  })
});

braze.openSession();
```

{% alert note %}
Content-Cards werden nur beim Sitzungsstart aktualisiert, wenn `subscribeToContentCardsUpdates()` vor `openSession()` aufgerufen wird. Sie können den [Feed auch jederzeit manuell aktualisieren]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/feed/).
{% endalert %}

{% endtab %}
{% tab android %}
{% subtabs local %}
{% subtab Java %}

#### Schritt 2a: Erstellen Sie eine private Subscriber-Variable

Um Karten-Updates zu abonnieren, deklarieren Sie zunächst eine private Variable in Ihrer angepassten Klasse, die Ihren Subscriber hält:

```java
// subscriber variable
private IEventSubscriber<ContentCardsUpdatedEvent> mContentCardsUpdatedSubscriber;
```

#### Schritt 2b: Updates abonnieren

Fügen Sie den folgenden Code hinzu, um Content-Card-Updates von Braze zu abonnieren, typischerweise innerhalb der `Activity.onCreate()` Ihrer angepassten Content-Cards-Activity:

```java
// Remove the previous subscriber before rebuilding a new one with our new activity.
Braze.getInstance(context).removeSingleSubscription(mContentCardsUpdatedSubscriber, ContentCardsUpdatedEvent.class);
mContentCardsUpdatedSubscriber = new IEventSubscriber<ContentCardsUpdatedEvent>() {
    @Override
    public void trigger(ContentCardsUpdatedEvent event) {
        // List of all Content Cards
        List<Card> allCards = event.getAllCards();

        // Your logic below
    }
};
Braze.getInstance(context).subscribeToContentCardsUpdates(mContentCardsUpdatedSubscriber);
Braze.getInstance(context).requestContentCardsRefresh();
```

#### Schritt 2c: Abo kündigen

Kündigen Sie das Abo, wenn Ihre angepasste Activity nicht mehr sichtbar ist. Fügen Sie den folgenden Code zur `onDestroy()`-Lifecycle-Methode Ihrer Activity hinzu:

```java
Braze.getInstance(context).removeSingleSubscription(mContentCardsUpdatedSubscriber, ContentCardsUpdatedEvent.class);
```

{% endsubtab %}
{% subtab Kotlin %}

#### Schritt 2a: Erstellen Sie eine private Subscriber-Variable

Um Karten-Updates zu abonnieren, deklarieren Sie zunächst eine private Variable in Ihrer angepassten Klasse, die Ihren Subscriber hält:

```kotlin
private var contentCardsUpdatedSubscriber: IEventSubscriber<ContentCardsUpdatedEvent>? = null
```

#### Schritt 2b: Updates abonnieren

Fügen Sie den folgenden Code hinzu, um Content-Card-Updates von Braze zu abonnieren, typischerweise innerhalb der `Activity.onCreate()` Ihrer angepassten Content-Cards-Activity:

```kotlin
// Remove the previous subscriber before rebuilding a new one with our new activity.
Braze.getInstance(context).subscribeToContentCardsUpdates(contentCardsUpdatedSubscriber)
Braze.getInstance(context).requestContentCardsRefresh()
  // List of all Content Cards
  val allCards = event.allCards

  // Your logic below
}
Braze.getInstance(context).subscribeToContentCardsUpdates(mContentCardsUpdatedSubscriber)
Braze.getInstance(context).requestContentCardsRefresh(true)
```

#### Schritt 2c: Abo kündigen

Kündigen Sie das Abo, wenn Ihre angepasste Activity nicht mehr sichtbar ist. Fügen Sie den folgenden Code zur `onDestroy()`-Lifecycle-Methode Ihrer Activity hinzu:

```kotlin
Braze.getInstance(context).removeSingleSubscription(contentCardsUpdatedSubscriber, ContentCardsUpdatedEvent::class.java)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab swift %}

Um auf das Content-Cards-Datenmodell zuzugreifen, rufen Sie [`contentCards.cards`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/cards) auf Ihrer `braze`-Instanz auf.

{% subtabs local %}
{% subtab Swift %}

```swift
let cards: [Braze.ContentCard] = AppDelegate.braze?.contentCards.cards
```

Zusätzlich können Sie ein Abo aufrechterhalten, um Änderungen an Ihren Content-Cards zu beobachten. Dies ist auf zwei Arten möglich: 
1. Über ein Cancellable; oder 
2. Über einen `AsyncStream`.

##### Cancellable 

```swift
// This subscription is maintained through a Braze cancellable, which will observe for changes until the subscription is cancelled.
// You must keep a strong reference to the cancellable to keep the subscription active.
// The subscription is canceled either when the cancellable is deinitialized or when you call its `.cancel()` method.
let cancellable = AppDelegate.braze?.contentCards.subscribeToUpdates { [weak self] contentCards in
  // Implement your completion handler to respond to updates in `contentCards`.
}
```

##### AsyncStream

```swift
let stream: AsyncStream<[Braze.ContentCard]> = AppDelegate.braze?.contentCards.cardsStream
```

{% endsubtab %}
{% subtab Objective-C %}

```objc
NSArray<BRZContentCardRaw *> *contentCards = AppDelegate.braze.contentCards.cards;
```

Wenn Sie zusätzlich ein Abo für Ihre Content-Cards aufrechterhalten möchten, können Sie [`subscribeToUpdates`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/subscribetoupdates(_:)) aufrufen:

```objc
// This subscription is maintained through Braze cancellable, which will continue to observe for changes until the subscription is cancelled.
BRZCancellable *cancellable = [self.braze.contentCards subscribeToUpdates:^(NSArray<BRZContentCardRaw *> *contentCards) {
  // Implement your completion handler to respond to updates in `contentCards`.
}];
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}


### 3. Schritt: Analytics implementieren

Impressionen, Klicks und Schließungen von Content-Cards werden in Ihrer angepassten Ansicht nicht automatisch protokolliert. Sie müssen [die jeweilige Methode implementieren]({{site.baseurl}}/developer_guide/content_cards/logging_analytics/), um alle Metriken ordnungsgemäß in die Braze-Dashboard-Analytics zu protokollieren.

### 4. Schritt: Testen Sie Ihre Karte (optional)

So testen Sie Ihre Content-Card:

1. Legen Sie eine:n aktive:n Nutzer:in in Ihrer Anwendung fest, indem Sie die [`changeUser()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser)-Methode aufrufen.
2. Gehen Sie in Braze zu **Kampagnen** und [erstellen Sie eine neue Content-Card-Kampagne]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create).
3. Wählen Sie in Ihrer Kampagne **Test** aus und geben Sie die `user-id` der Testnutzer:in ein. Wenn Sie bereit sind, wählen Sie **Test senden**. Sie können dann in Kürze eine Content-Card auf Ihrem Gerät starten.

![Eine Braze Content-Card-Kampagne, die zeigt, wie Sie Ihre eigene Nutzer-ID als Testempfänger:in hinzufügen können, um Ihre Content-Card zu testen.]({% image_buster /assets/img/react-native/content-card-test.png %} "Content Card Campaign Test")

## Platzierung von Content-Cards

Content-Cards können auf viele verschiedene Arten verwendet werden. Drei gängige Implementierungen sind die Verwendung als Nachrichtenzentrale, als dynamische Bildanzeige oder als Bildkarussell. Für jede dieser Platzierungen weisen Sie Ihren Content-Cards [Schlüssel-Wert-Paare]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_behavior/#key-value-pairs) (die Eigenschaft `extras` im Datenmodell) zu und passen auf der Grundlage der Werte das Verhalten, das Aussehen oder die Funktionalität der Karte während der Laufzeit dynamisch an. 

![]({% image_buster /assets/img_archive/cc_placements.png %}){: style="border:0px;"}

### Posteingang für Nachrichten

Content-Cards können verwendet werden, um eine Nachrichtenzentrale zu simulieren. In diesem Format ist jede Nachricht eine eigene Karte, die [Schlüssel-Wert-Paare]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_behavior/#key-value-pairs) enthält, die Events beim Klicken triggern. Diese Schlüssel-Wert-Paare sind die Bezeichner, anhand derer die Anwendung entscheidet, wohin navigiert wird, wenn Nutzer:innen auf eine Nachricht im Posteingang klicken. Die Werte der Schlüssel-Wert-Paare sind frei wählbar. 

#### Beispiel

Sie möchten beispielsweise zwei Messaging-Karten erstellen: einen Call-to-Action für Nutzer:innen zum Aktivieren von Leseempfehlungen und einen Gutschein-Code für Ihr neues Segment von Abonnent:innen.

Schlüssel wie `body`, `title` und `buttonText` können einfache String-Werte haben, die Ihre Marketer festlegen können. Schlüssel wie `terms` können Werte haben, die eine kleine Sammlung von Phrasen enthalten, die von Ihrer Rechtsabteilung genehmigt wurden. Schlüssel wie `style` und `class_type` haben String-Werte, die Sie festlegen können, um zu bestimmen, wie Ihre Karte in Ihrer App oder Website dargestellt wird.

{% tabs local %}
{% tab Reading recommendations %}
Schlüssel-Wert-Paare für die Leseempfehlungskarte:

| Schlüssel         | Wert                                                                |
|------------|----------------------------------------------------------------------|
| `body`       | Fügen Sie Ihre Interessen zu Ihrem Politer Weekly Profil hinzu, um persönliche Leseempfehlungen zu erhalten. |
| `style`      | info                                                                 |
| `class_type` | notification_center                                                 |
| `card_priority` | 1                                                                 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% endtab %}

{% tab New subscriber coupon %}
Schlüssel-Wert-Paare für einen neuen Abonnent:innen-Gutschein:

| Schlüssel         | Wert                                                            |
|------------|------------------------------------------------------------------|
| `title`      | Unbegrenztes Spiele-Abo                                    |
| `body`       | End of Summer Special – Hol dir 10 % Rabatt auf Politer-Spiele              |
| `buttonText` | Jetzt abonnieren                                                    |
| `style`      | promo                                                            |
| `class_type` | notification_center                                              |
| `card_priority` | 2                                                              |
| `terms`      | new_subscribers_only                                             |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% endtab %}
{% endtabs %}

{% details Zusätzliche Informationen für Android %}

Im Android und FireOS SDK wird die Logik der Nachrichtenzentrale durch den Wert `class_type` gesteuert, der durch die Schlüssel-Wert-Paare von Braze bereitgestellt wird. Mit der Methode [`createContentCardable`]({{site.baseurl}}/developer_guide/content_cards/) können Sie diese Klassentypen filtern und identifizieren.

{% tabs local %}
{% tab Kotlin %}
**Verwendung von `class_type` für On-Click-Verhalten**<br>
Wenn wir die Content-Card-Daten in unsere angepassten Klassen überführen, verwenden wir die Eigenschaft `ContentCardClass` der Daten, um zu bestimmen, welche konkrete Unterklasse zum Speichern der Daten verwendet werden soll.

```kotlin
 private fun createContentCardable(metadata: Map<String, Any>, type: ContentCardClass?): ContentCardable?{
        return when(type){
            ContentCardClass.AD -> Ad(metadata)
            ContentCardClass.MESSAGE_WEB_VIEW -> WebViewMessage(metadata)
            ContentCardClass.NOTIFICATION_CENTER -> FullPageMessage(metadata)
            ContentCardClass.ITEM_GROUP -> Group(metadata)
            ContentCardClass.ITEM_TILE -> Tile(metadata)
            ContentCardClass.COUPON -> Coupon(metadata)
            else -> null
        }
    }
```

Bei der Verarbeitung der Nutzerinteraktion mit der Nachrichtenliste können wir dann anhand des Nachrichtentyps bestimmen, welche Ansicht den Nutzer:innen angezeigt werden soll.

```kotlin
override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        //...
        listView.onItemClickListener = AdapterView.OnItemClickListener { parent, view, position, id ->
           when (val card = dataProvider[position]){
                is WebViewMessage -> {
                    val intent = Intent(this, WebViewActivity::class.java)
                    val bundle = Bundle()
                    bundle.putString(WebViewActivity.INTENT_PAYLOAD, card.contentString)
                    intent.putExtras(bundle)
                    startActivity(intent)
                }
                is FullPageMessage -> {
                    val intent = Intent(this, FullPageContentCard::class.java)
                    val bundle = Bundle()
                    bundle.putString(FullPageContentCard.CONTENT_CARD_IMAGE, card.icon)
                    bundle.putString(FullPageContentCard.CONTENT_CARD_TITLE, card.messageTitle)
                    bundle.putString(FullPageContentCard.CONTENT_CARD_DESCRIPTION, card.cardDescription)
                    intent.putExtras(bundle)
                    startActivity(intent)
                }
            }

        }
    }
```
{% endtab %}
{% tab Java %}
**Verwendung von `class_type` für On-Click-Verhalten**<br>
Wenn wir die Content-Card-Daten in unsere angepassten Klassen überführen, verwenden wir die Eigenschaft `ContentCardClass` der Daten, um zu bestimmen, welche konkrete Unterklasse zum Speichern der Daten verwendet werden soll.

```java
private ContentCardable createContentCardable(Map<String, ?> metadata,  ContentCardClass type){
    switch(type){
        case ContentCardClass.AD:{
            return new Ad(metadata);
        }
        case ContentCardClass.MESSAGE_WEB_VIEW:{
            return new WebViewMessage(metadata);
        }
        case ContentCardClass.NOTIFICATION_CENTER:{
            return new FullPageMessage(metadata);
        }
        case ContentCardClass.ITEM_GROUP:{
            return new Group(metadata);
        }
        case ContentCardClass.ITEM_TILE:{
            return new Tile(metadata);
        }
        case ContentCardClass.COUPON:{
            return new Coupon(metadata);
        }
        default:{
            return null;
        }
    }
}

```

Bei der Verarbeitung der Nutzerinteraktion mit der Nachrichtenliste können wir dann anhand des Nachrichtentyps bestimmen, welche Ansicht den Nutzer:innen angezeigt werden soll.

```java
@Override
protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState)
        //...
        listView.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id){
               ContentCardable card = dataProvider.get(position);
               if (card instanceof WebViewMessage){
                    Bundle intent = new Intent(this, WebViewActivity.class);
                    Bundle bundle = new Bundle();
                    bundle.putString(WebViewActivity.INTENT_PAYLOAD, card.getContentString());
                    intent.putExtras(bundle);
                    startActivity(intent);
                }
                else if (card instanceof FullPageMessage){
                    Intent intent = new Intent(this, FullPageContentCard.class);
                    Bundle bundle = Bundle();
                    bundle.putString(FullPageContentCard.CONTENT_CARD_IMAGE, card.getIcon());
                    bundle.putString(FullPageContentCard.CONTENT_CARD_TITLE, card.getMessageTitle());
                    bundle.putString(FullPageContentCard.CONTENT_CARD_DESCRIPTION, card.getCardDescription());
                    intent.putExtras(bundle)
                    startActivity(intent)
                }
            }

        });
    }
```

{% endtab %}
{% endtabs %}
{% enddetails %}

### Karussell

Sie können Content-Cards in Ihrem vollständig angepassten Karussell-Feed einrichten, sodass Nutzer:innen durch zusätzliche hervorgehobene Karten wischen und diese ansehen können. Standardmäßig werden Content-Cards nach Erstellungsdatum sortiert (das neueste zuerst), und Ihre Nutzer:innen sehen alle Karten, für die sie in Frage kommen.

So implementieren Sie ein Content-Card-Karussell:

1. Erstellen Sie eine angepasste Logik, die auf [Änderungen in Ihren Content-Cards]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed/#refreshing-the-feed) achtet und die Ankunft der Content-Cards behandelt.
2. Erstellen Sie eine angepasste clientseitige Logik, um eine bestimmte Anzahl von Karten gleichzeitig im Karussell anzuzeigen. Sie könnten zum Beispiel die ersten fünf Content-Card-Objekte aus dem Array auswählen oder Schlüssel-Wert-Paare einführen, um bedingte Logik aufzubauen.

{% alert tip %}
Wenn Sie ein Karussell als sekundären Content-Cards-Feed implementieren, stellen Sie sicher, dass Sie [die Karten mithilfe von Schlüssel-Wert-Paaren in den richtigen Feed einsortieren]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed/#multiple-feeds).
{% endalert %}

### Nur Bild

Content-Cards müssen nicht wie „Karten" aussehen. Content-Cards können zum Beispiel als dynamisches Bild erscheinen, das persistent auf Ihrer Homepage oder am Anfang bestimmter Seiten angezeigt wird.

Um dies zu erreichen, erstellen Ihre Marketer eine Kampagne oder einen Canvas-Schritt mit einer Content-Card vom Typ **Nur Bild**. Legen Sie dann Schlüssel-Wert-Paare fest, die für die Verwendung von [Content-Cards als ergänzende Inhalte]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_behavior/#content-cards-as-supplemental-content) geeignet sind.