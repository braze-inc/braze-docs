> Beim Erstellen einer angepassten UI für Content-Cards müssen Sie Analysedaten wie Impressionen, Klicks und Ablehnungen manuell protokollieren, da dies nur für Standard-Kartenmodelle automatisch erfolgt. Die Protokollierung dieser Ereignisse ist ein Standardbestandteil der Integration von Content-Cards und für eine genaue Berichterstattung über Kampagnen und Abrechnung unerlässlich. Füllen Sie dazu Ihre angepasste UI mit Daten aus den Braze-Datenmodellen und protokollieren Sie die Ereignisse anschließend manuell. Sobald Sie wissen, wie man Analytics protokolliert, können Sie sehen, wie Braze-Kund:innen häufig [angepasste Content-Cards erstellen]({{site.baseurl}}/developer_guide/content_cards/creating_cards/). 

## Analytics protokollieren

Bei der Implementierung Ihrer angepassten Content-Cards können Sie die Objekte des Typs „Content-Card" parsen und ihre Nutzlastdaten wie `title`, `cardDescription` und `imageUrl` extrahieren. Anschließend können Sie Ihre angepasste UI mit den resultierenden Modelldaten füllen. 

Abonnieren Sie Content-Card-Updates, um die Content-Card-Datenmodelle zu erhalten. Es gibt zwei Eigenschaften, auf die Sie besonders achten sollten:

* **`id`**: Stellt den String der Content-Card-ID dar. Dies ist der eindeutige Bezeichner, der zur Protokollierung der Analytics von angepassten Content-Cards verwendet wird.
* **`extras`**: Umfasst alle Schlüssel-Wert-Paare aus dem Braze-Dashboard. 

Alle Eigenschaften außerhalb von `id` und `extras` sind optional und können für angepasste Content-Cards ausgewertet werden. Weitere Informationen über das Datenmodell finden Sie im Artikel zur Integration der jeweiligen Plattform: [Android]({{site.baseurl}}/developer_guide/content_cards/?sdktab=android), [iOS]({{site.baseurl}}/developer_guide/content_cards/?sdktab=swift), [Internet]({{site.baseurl}}/developer_guide/content_cards/?sdktab=web).


{% tabs %}
{% tab web %}

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
{% tab android %}
{% subtabs local %}
{% subtab Java %}

### 1. Schritt: Erstellen Sie eine private Abonnentenvariable

Um Karten-Updates zu abonnieren, deklarieren Sie zunächst eine private Variable in Ihrer angepassten Klasse, die Ihren Abonnenten enthält:

```java
// subscriber variable
private IEventSubscriber<ContentCardsUpdatedEvent> mContentCardsUpdatedSubscriber;
```

### 2. Schritt: Updates abonnieren

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

### 3. Schritt: Abmelden

Wir empfehlen Ihnen außerdem, sich abzumelden, wenn Ihre angepasste Aktivität nicht mehr sichtbar ist. Fügen Sie den folgenden Code in die Lebenszyklusmethode `onDestroy()` Ihrer Aktivität ein:

```java
Braze.getInstance(context).removeSingleSubscription(mContentCardsUpdatedSubscriber, ContentCardsUpdatedEvent.class);
```

{% endsubtab %}
{% subtab Kotlin %}

### 1. Schritt: Erstellen Sie eine private Abonnentenvariable

Um Karten-Updates zu abonnieren, deklarieren Sie zunächst eine private Variable in Ihrer angepassten Klasse, die Ihren Abonnenten enthält:

```kotlin
private var contentCardsUpdatedSubscriber: IEventSubscriber<ContentCardsUpdatedEvent>? = null
```

### 2. Schritt: Updates abonnieren

Als Nächstes fügen Sie den folgenden Code – typischerweise innerhalb von `Activity.onCreate()` der angepassten Content-Card-Aktivität – hinzu, um Content-Card-Updates von Braze zu abonnieren:

```kotlin
// Remove the previous subscriber before rebuilding a new one with our new activity.
Braze.getInstance(context).removeSingleSubscription(contentCardsUpdatedSubscriber, ContentCardsUpdatedEvent::class.java)
contentCardsUpdatedSubscriber = IEventSubscriber { event ->
  // List of all Content Cards
  val allCards = event.allCards

  // Your logic below
}
Braze.getInstance(context).subscribeToContentCardsUpdates(contentCardsUpdatedSubscriber)
Braze.getInstance(context).requestContentCardsRefresh(true)
```

### 3. Schritt: Abmelden

Wir empfehlen Ihnen außerdem, sich abzumelden, wenn Ihre angepasste Aktivität nicht mehr sichtbar ist. Fügen Sie den folgenden Code in die Lebenszyklusmethode `onDestroy()` Ihrer Aktivität ein:

```kotlin
Braze.getInstance(context).removeSingleSubscription(contentCardsUpdatedSubscriber, ContentCardsUpdatedEvent::class.java)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab swift %}

Um auf das Content-Cards-Datenmodell zuzugreifen, rufen Sie [`contentCards.cards`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/cards) in Ihrer `braze`-Instanz auf.

{% subtabs local %}
{% subtab Swift %}

```swift
let cards: [Braze.ContentCard] = AppDelegate.braze?.contentCards.cards
```

Außerdem können Sie ein Abo abschließen, um Änderungen an Ihren Content-Cards zu beobachten. Dafür gibt es zwei Möglichkeiten: 
1. Ein Cancellable verwenden oder 
2. Einen `AsyncStream` verwenden.

### Cancellable 

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

Wenn Sie außerdem ein Abo für Ihre Content-Cards einrichten möchten, können Sie [`subscribeToUpdates`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/subscribetoupdates(_:)) aufrufen:

```objc
// This subscription is maintained through Braze cancellable, which will continue to observe for changes until the subscription is cancelled.
BRZCancellable *cancellable = [self.braze.contentCards subscribeToUpdates:^(NSArray<BRZContentCardRaw *> *contentCards) {
  // Implement your completion handler to respond to updates in `contentCards`.
}];
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab react native %}

Um die Daten der Content-Cards abzurufen, verwenden Sie die Methode `getContentCards`:

```javascript
import Braze from "@braze/react-native-sdk";

const cards = await Braze.getContentCards();
```

Um über Updates informiert zu werden, abonnieren Sie die Update-Ereignisse der Content-Cards:

```javascript
const subscription = Braze.addListener(Braze.Events.CONTENT_CARDS_UPDATED, (update) => {
  const cards = update.cards;
  cards.forEach(card => {
    if (card.isControl) {
      // Do not display the control card, but remember to log an impression
    } else {
      // Use card.title, card.cardDescription, card.image, etc.
    }
  });
});
```

Um eine manuelle Aktualisierung der Content-Cards von den Braze-Servern anzufordern:

```javascript
Braze.requestContentCardsRefresh();
```

Um zwischengespeicherte Content-Cards ohne Netzwerkanfrage zu erhalten:

```javascript
const cachedCards = await Braze.getCachedContentCards();
```

{% endtab %}
{% endtabs %}

## Events protokollieren

Wertvolle Metriken wie Impressionen, Klicks und Ausblendungen können schnell und einfach protokolliert werden. Legen Sie einen angepassten Klick-Listener fest, um diese Analytics manuell zu verarbeiten.

{% tabs %}
{% tab web %}

Protokollieren Sie Impression-Events, wenn Karten von Nutzer:innen angesehen werden, mit [`logContentCardImpressions`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardimpressions):

```javascript
import * as braze from "@braze/web-sdk";

braze.logContentCardImpressions([card1, card2, card3]);
```

Protokollieren Sie Klick-Events, wenn Nutzer:innen mit einer Karte interagieren, mit [`logContentCardClick`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardclick):

```javascript
import * as braze from "@braze/web-sdk";

braze.logContentCardClick(card);
```

{% endtab %}
{% tab android %}

Der [`BrazeManager`](https://github.com/braze-inc/braze-growth-shares-android-demo-app/blob/main/app/src/main/java/com/braze/advancedsamples/BrazeManager.kt) kann Braze-SDK-Abhängigkeiten referenzieren, wie z. B. die Content-Card-Objekt-Array-Liste, um das [`Card`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html)-Objekt abzurufen und die Braze-Protokollierungsmethoden aufzurufen. Verwenden Sie die Basisklasse `ContentCardable`, um Daten einfach zu referenzieren und an den `BrazeManager` weiterzugeben. 

Um eine Impression oder einen Klick auf eine Karte zu protokollieren, rufen Sie [`Card.logClick()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-click.html) bzw. [`Card.logImpression()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-impression.html) auf. 

Sie können eine Content-Card manuell protokollieren oder mit [`isDismissed`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/is-dismissed.html) bei Braze als „ausgeblendet" festlegen. Wenn eine Karte bereits als ausgeblendet markiert ist, kann sie nicht erneut als ausgeblendet markiert werden.

Um einen angepassten Klick-Listener zu erstellen, erstellen Sie eine Klasse, die [`IContentCardsActionListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.listeners/-i-content-cards-action-listener/index.html) implementiert, und registrieren Sie sie mit [`BrazeContentCardsManager`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.managers/-braze-content-cards-manager/index.html). Implementieren Sie die Methode [`onContentCardClicked()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.listeners/-i-content-cards-action-listener/on-content-card-clicked.html), die aufgerufen wird, wenn ein:e Nutzer:in auf eine Content-Card klickt. Weisen Sie Braze dann an, Ihren Klick-Listener für Content-Cards zu verwenden. 

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
Um Content-Cards als Kontrollvariante in Ihrer angepassten UI zu verarbeiten, übergeben Sie das Objekt [`com.braze.models.cards.Card`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html) und rufen dann die Methode `logImpression` auf, wie Sie es mit jedem anderen Content-Card-Typ tun würden. Das Objekt protokolliert implizit eine Kontroll-Impression, um unsere Analytics darüber zu informieren, wann ein:e Nutzer:in die Kontrollkarte gesehen hätte.{% endalert %}

{% endtab %}

{% tab swift %}

Implementieren Sie das Protokoll [`BrazeContentCardUIViewControllerDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcarduiviewcontrollerdelegate) und legen Sie das Delegate-Objekt als Eigenschaft `delegate` von `BrazeContentCardUI.ViewController` fest. Dieser Delegate sorgt dafür, dass die Daten Ihres angepassten Objekts zur Protokollierung an Braze zurückgegeben werden. Ein Beispiel finden Sie im [Tutorial zur Content-Cards-UI](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c2-contentcardsui/).

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
Um Content-Cards als Kontrollvariante in Ihrer angepassten UI zu verarbeiten, übergeben Sie das Objekt [`Braze.ContentCard.Control`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/control(_:)) und rufen dann die Methode `logImpression` auf, wie Sie es mit jedem anderen Content-Card-Typ tun würden. Das Objekt protokolliert implizit eine Kontroll-Impression, um unsere Analytics darüber zu informieren, wann ein:e Nutzer:in die Kontrollkarte gesehen hätte.
{% endalert %}
{% endtab %}

{% tab react native %}

Protokollieren Sie Impression-Events, wenn Karten von Nutzer:innen angesehen werden:

```javascript
Braze.logContentCardImpression(card.id);
```

Protokollieren Sie Klick-Events, wenn Nutzer:innen mit einer Karte interagieren:

```javascript
Braze.logContentCardClicked(card.id);
```

Protokollieren Sie Ausblendungs-Events, wenn ein:e Nutzer:in eine Karte ausblendet:

```javascript
Braze.logContentCardDismissed(card.id);
```

{% endtab %}
{% endtabs %}

## Verarbeitung des Klickverhaltens

{% tabs %}
{% tab web %}

Wenn ein:e Nutzer:in in einem angepassten Feed auf eine Content-Card klickt, wird das Klickverhalten (z. B. Navigation zu einer URL, Deeplinking oder Protokollierung eines angepassten Events) nicht automatisch verarbeitet. Verwenden Sie [`handleBrazeAction`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#handlebrazeaction), um die URL der Karte zu verarbeiten und die konfigurierte Klickaktion auszuführen, einschließlich Braze-Aktionen (`brazeActions://`-URLs).

```javascript
import * as braze from "@braze/web-sdk";

// In your card click handler
function onCardClick(card) {
  // Log the click
  braze.logContentCardClick(card);

  // Handle the on-click behavior
  if (card.url) {
    braze.handleBrazeAction(card.url);
  }
}
```

| Parameter | Beschreibung |
|---|---|
| `url` | Eine gültige URL oder eine gültige Braze-Aktions-URL mit dem Schema `brazeActions://`. |
| `openLinkInNewTab` | (Optional) Ob die URL in einem neuen Tab geöffnet werden soll. Standardmäßig `false`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Wenn Sie `handleBrazeAction()` nicht aufrufen, werden im Braze-Dashboard konfigurierte Klickverhalten (wie „Angepasstes Event protokollieren" oder „Zu URL navigieren") für Karten in einem angepassten Feed nicht ausgeführt.
{% endalert %}

{% endtab %}
{% tab android %}

Das Klickverhalten wird von der Standard-Content-Cards-UI automatisch verarbeitet. Für angepasste Implementierungen verwenden Sie die Schnittstelle [`IContentCardsActionListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.listeners/-i-content-cards-action-listener/index.html), die im Abschnitt [Analytics protokollieren](#logging-analytics) oben beschrieben wird.

{% endtab %}
{% tab swift %}

Das Klickverhalten wird von der Standard-Content-Cards-UI automatisch verarbeitet. Für angepasste Implementierungen verwenden Sie das Protokoll [`BrazeContentCardUIViewControllerDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcarduiviewcontrollerdelegate), das im Abschnitt [Analytics protokollieren](#logging-analytics) oben beschrieben wird.

{% endtab %}
{% endtabs %}