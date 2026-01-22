> Wenn Sie ein angepasstes UI für Content-Cards erstellen, müssen Sie Analytics wie Impressionen, Klicks und Abbrüche manuell protokollieren, da dies nur bei Standard-Kartenmodellen automatisch geschieht. Die Protokollierung dieser Ereignisse ist ein Standardbestandteil einer Content-Card-Integration und unerlässlich für genaue Kampagnenberichte und Abrechnungen. Füllen Sie dazu Ihr angepasstes UI mit Daten aus den Braze-Datenmodellen und protokollieren Sie die Events dann manuell. Sobald Sie wissen, wie man Analysen protokolliert, können Sie sehen, wie Braze-Kunden häufig [benutzerdefinierte Content Cards erstellen]({{site.baseurl}}/developer_guide/content_cards/creating_cards/). 

## Abhören von Karten-Updates

Bei der Implementierung Ihrer angepassten Content-Cards können Sie die Objekte des Typs "Content-Card" parsen und ihre Nutzlastdaten wie `title`, `cardDescription` und `imageUrl` extrahieren. Anschließend können Sie Ihre angepasste UI mit den resultierenden Modelldaten füllen. 

Abonnieren Sie Content-Card-Updates, um die Content-Card-Datenmodelle zu erhalten. Es gibt zwei Eigenschaften, auf die Sie besonders achten sollten:

* **`id`**: Stellt die Zeichenkette der Inhaltskarten-ID dar. Dies ist die eindeutige Kennung, die zur Protokollierung der Analysen von benutzerdefinierten Inhaltskarten verwendet wird.
* **`extras`**: Umfasst alle Schlüssel-Wert-Paare aus dem Dashboard von Braze. 

Alle Eigenschaften außerhalb von `id` und `extras` sind optional und können für benutzerdefinierte Inhaltskarten ausgewertet werden. Weitere Informationen über das Datenmodell finden Sie im Artikel zur Integration der jeweiligen Plattform: [Android]({{site.baseurl}}/developer_guide/content_cards/?sdktab=android), [iOS]({{site.baseurl}}/developer_guide/content_cards/?sdktab=swift), [Web]({{site.baseurl}}/developer_guide/content_cards/?sdktab=web).


{% tabs %}
{% tab android %}
{% subtabs local %}
{% subtab Java %}

### Schritt 1: Erstellen Sie eine private Abonnentenvariable

Um Karten-Updates zu abonnieren, deklarieren Sie zunächst eine private Variable in Ihrer angepassten Klasse, die Ihren Abonnenten enthält:

```java
// subscriber variable
private IEventSubscriber<ContentCardsUpdatedEvent> mContentCardsUpdatedSubscriber;
```

### Schritt 2: Updates abonnieren

Als Nächstes fügen Sie den folgenden Code – typischerweise innerhalb von `Activity.onCreate()` der angepassten Content-Card-Aktivität – hinzu, um Content-Card-Updates von Braze zu abonnieren:

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

### Schritt 3: Abmelden

Wir empfehlen Ihnen außerdem, sich abzumelden, wenn Ihre angepasste Aktivität nicht mehr sichtbar ist. Fügen Sie den folgenden Code in die Lebenszyklusmethode Ihrer Aktivität `onDestroy()` ein:

```java
Braze.getInstance(context).removeSingleSubscription(mContentCardsUpdatedSubscriber, ContentCardsUpdatedEvent.class);
```

{% endsubtab %}
{% subtab Kotlin %}

### Schritt 1: Erstellen Sie eine private Abonnentenvariable

Um Karten-Updates zu abonnieren, deklarieren Sie zunächst eine private Variable in Ihrer angepassten Klasse, die Ihren Abonnenten enthält:

```kotlin
private var contentCardsUpdatedSubscriber: IEventSubscriber<ContentCardsUpdatedEvent>? = null
```

### Schritt 2: Updates abonnieren

Als Nächstes fügen Sie den folgenden Code – typischerweise innerhalb von `Activity.onCreate()` der angepassten Content-Card-Aktivität – hinzu, um Content-Card-Updates von Braze zu abonnieren:

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

### Schritt 3: Abmelden

Wir empfehlen Ihnen außerdem, sich abzumelden, wenn Ihre angepasste Aktivität nicht mehr sichtbar ist. Fügen Sie den folgenden Code in die Lebenszyklusmethode Ihrer Aktivität `onDestroy()` ein:

```kotlin
Braze.getInstance(context).removeSingleSubscription(contentCardsUpdatedSubscriber, ContentCardsUpdatedEvent::class.java)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab schnell %}

Um auf das Content-Cards-Datenmodell zuzugreifen, rufen Sie [`contentCards.cards`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/cards) in Ihrer `braze`-Instanz auf.

{% subtabs local %}
{% subtab Swift %}

```swift
let cards: [Braze.ContentCard] = AppDelegate.braze?.contentCards.cards
```

Außerdem können Sie auch ein Abo abschließen, um Änderungen an Ihren Content-Cards zu beobachten. Sie können dies auf zwei Arten tun: 
1. Abschluss eines kündbaren Abos oder 
2. Abschluss von `AsyncStream`.

### Abbestellbar 

```swift
// This subscription is maintained through a Braze cancellable, which will observe for changes until the subscription is cancelled.
// You must keep a strong reference to the cancellable to keep the subscription active.
// The subscription is canceled either when the cancellable is deinitialized or when you call its `.cancel()` method.
let cancellable = AppDelegate.braze?.contentCards.subscribeToUpdates { [weak self] contentCards in
  // Implement your completion handler to respond to updates in `contentCards`.
}
```

### AsyncStream

```swift
let stream: AsyncStream<[Braze.ContentCard]> = AppDelegate.braze?.contentCards.cardsStream
```

{% endsubtab %}
{% subtab Objective-C %}

```objc
NSArray<BRZContentCardRaw *> *contentCards = AppDelegate.braze.contentCards.cards;
```

Wenn Sie außerdem ein Abo für Ihre Content-Cards haben möchten, können Sie [`subscribeToUpdates`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/subscribetoupdates(_:)) aufrufen:

```objc
// This subscription is maintained through Braze cancellable, which will continue to observe for changes until the subscription is cancelled.
BRZCancellable *cancellable = [self.braze.contentCards subscribeToUpdates:^(NSArray<BRZContentCardRaw *> *contentCards) {
  // Implement your completion handler to respond to updates in `contentCards`.
}];
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Internet %}

Registrieren Sie eine Callback-Funktion, um Updates zu abonnieren, wenn Karten aktualisiert werden.

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
Content-Cards werden nur dann beim Sitzungsstart aktualisiert, wenn vor `openSession()` eine Abo-Anfrage aufgerufen wird. Sie können [den Feed auch jederzeit manuell aktualisieren]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/feed/).
{% endalert %}

{% endtab %}
{% endtabs %}

## Protokollieren von Events

Wertvolle Metriken wie Impressionen, Klicks und Ausblendungen können schnell und einfach protokolliert werden. Legen Sie einen angepassten Klick-Listener fest, um diese Analytics manuell zu verarbeiten.

{% tabs %}
{% tab android %}

Die [`BrazeManager`](https://github.com/braze-inc/braze-growth-shares-android-demo-app/blob/main/app/src/main/java/com/braze/advancedsamples/BrazeManager.kt) kann Braze SDK-Abhängigkeiten referenzieren, wie z.B. die Content-Card-Objekt-Array-Liste, um die [`Card`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html) um die Braze-Protokollierungsmethoden aufzurufen. Verwenden Sie die Basisklasse `ContentCardable`, um Daten einfach zu referenzieren und an `BrazeManager` weiterzugeben. 

Um eine Impression oder einen Klick auf eine Karte zu protokollieren, rufen Sie [`Card.logClick()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-click.html) bzw. [`Card.logImpression()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-impression.html) auf. 

Sie können eine Content-Card manuell protokollieren oder mit [`isDismissed`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/is-dismissed.html) auf "ausgeblendet" festlegen. Wenn eine Karte bereits als abgelehnt markiert ist, kann sie nicht erneut als abgelehnt markiert werden.

Um einen angepassten Klick-Hörer zu erstellen, erstellen Sie eine Klasse, die [`IContentCardsActionListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.listeners/-i-content-cards-action-listener/index.html) implementiert, und registrieren Sie sie mit [`BrazeContentCardsManager`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.managers/-braze-content-cards-manager/index.html). Implementieren Sie die Methode [`onContentCardClicked()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.listeners/-i-content-cards-action-listener/on-content-card-clicked.html), die aufgerufen wird, wenn ein Nutzer auf eine Content-Card klickt. Weisen Sie Braze dann an, Ihren Klick-Listener für Content-Cards zu verwenden. 

{% subtabs local %}
{% subtab Java %}

Zum Beispiel:

```java
BrazeContentCardsManager.getInstance().setContentCardsActionListener(new IContentCardsActionListener() {
  @Override
  public boolean onContentCardClicked(Context context, Card card, IAction cardAction) {
    return false;
  }

  @Override
  public void onContentCardDismissed(Context context, Card card) {

  }
});
```

{% endsubtab %}
{% subtab Kotlin %}

Zum Beispiel:

```kotlin
BrazeContentCardsManager.getInstance().contentCardsActionListener = object : IContentCardsActionListener {
  override fun onContentCardClicked(context: Context, card: Card, cardAction: IAction): Boolean {
    return false
  }

  override fun onContentCardDismissed(context: Context, card: Card) {

  }
}
```

{% endsubtab %}
{% endsubtabs %}

{% alert important %}
Um Content-Cards als Kontrollvariante in Ihrer angepassten UI zu verarbeiten, übergeben Sie das Objekt [`com.braze.models.cards.Card`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html) und rufen dann die Methode `logImpression` auf, wie Sie es mit jedem anderen Content-Card-Typ tun würden. Das Objekt protokolliert implizit eine Kontroll-Impression, um unsere Analytics darüber zu informieren, wann ein Nutzer die Kontrollkarte gesehen hätte.{% endalert %}

{% endtab %}
{% tab schnell %}

Implementieren Sie das Protokoll [`BrazeContentCardUIViewControllerDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcarduiviewcontrollerdelegate) und legen Sie das Delegate-Objekt als Eigenschaft `delegate` von `BrazeContentCardUI.ViewController` fest. Dieser Delegat sorgt dafür, dass die Daten Ihres benutzerdefinierten Objekts zur Protokollierung an Braze zurückgegeben werden. Ein Beispiel finden Sie im [Tutorial zur Benutzeroberfläche von Content Cards](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c2-contentcardsui/).

{% subtabs local %}
{% subtab Swift %}

```swift
// Set the delegate when creating the Content Cards controller
contentCardsController.delegate = delegate

// Method to implement in delegate
func contentCard(
    _ controller: BrazeContentCardUI.ViewController,
    shouldProcess clickAction: Braze.ContentCard.ClickAction,
    card: Braze.ContentCard
  ) -> Bool {
  // Intercept the content card click action here.
  return true
}
```

{% endsubtab %}
{% subtab Objective-C %}

```objc
// Set the delegate when creating the Content Cards controller
contentCardsController.delegate = delegate;

// Method to implement in delegate
- (BOOL)contentCardController:(BRZContentCardUIViewController *)controller
                shouldProcess:(NSURL *)url
                         card:(BRZContentCardRaw *)card {
  // Intercept the content card click action here.
  return YES;
}
```
{% endsubtab %}
{% endsubtabs %}

{% alert important %}
Um Content-Cards als Kontrollvariante in Ihrer angepassten UI zu verarbeiten, übergeben Sie das Objekt [`Braze.ContentCard.Control`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/control(_:)) und rufen dann die Methode `logImpression` auf, wie Sie es mit jedem anderen Content-Card-Typ tun würden. Das Objekt protokolliert implizit eine Kontroll-Impression, um unsere Analytics darüber zu informieren, wann ein Nutzer die Kontrollkarte gesehen hätte.
{% endalert %}
{% endtab %}

{% tab Internet %}

Protokollieren Sie Impression-Events, wenn Karten von Nutzern aufgerufen werden, mit [`logContentCardImpressions`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardimpressions):

```javascript
import * as braze from "@braze/web-sdk";

braze.logContentCardImpressions([card1, card2, card3]);
```

Protokollieren Sie Klick-Events, wenn Nutzer mit einer Karte interagieren, mit [`logContentCardClick`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardclick):

```javascript
import * as braze from "@braze/web-sdk";

braze.logContentCardClick(card);
```

{% endtab %}
{% endtabs %}
