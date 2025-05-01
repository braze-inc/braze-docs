---
nav_title: Anpassen des Feeds
article_title: Anpassen des standardmäßigen Content-Card Feeds
page_order: 3
description: "Dieser Artikel behandelt die Anpassungsmöglichkeiten von Content-Card-Feeds."
channel:
  - content cards
platform:
  - Android
  - FireOS
  - Swift
  - Web
---

# Anpassen des standardmäßigen Content-Card Feeds

> Ein Content-Card-Feed ist eine Abfolge von Content-Cards in Ihren Mobil- oder Web-Apps. Dieser Artikel befasst sich mit der Konfiguration, wann der Feed aktualisiert wird, der Reihenfolge der Karten, der Verwaltung mehrerer Feeds und den Fehlermeldungen "leerer Feed". Einen grundlegenden Überblick über die Arten von Anpassungsmöglichkeiten, die Sie mit Content Cards haben, finden Sie unter [Übersicht über die Anpassung]({{site.baseurl}}/developer_guide/getting_started/customization_overview). 

## Aktualisieren des Feeds

Standardmäßig wird der Content-Card-Feed in den folgenden Instanzen automatisch aktualisiert: 
1. Wenn eine neue Sitzung gestartet wird
2. Wenn das Futter geöffnet wird und seit der letzten Aktualisierung mehr als 60 Sekunden vergangen sind. Dies gilt nur für den Standard Content-Card-Feed und tritt nur einmal pro Öffnung des Feeds auf.

Sie können das SDK auch so konfigurieren, dass es zu bestimmten Zeiten manuell aktualisiert wird.

{% alert tip %}
Um aktuelle Content-Cards dynamisch anzuzeigen, ohne sie manuell zu aktualisieren, wählen Sie bei der Erstellung der Karte die Option **Beim ersten Eindruck** aus. Diese Karten werden aktualisiert, sobald sie verfügbar sind.
{% endalert %}

{% tabs local %}
{% tab Android %}

Sie können jederzeit eine manuelle Aktualisierung der Braze Content-Cards über das Android SDK anfragen, indem Sie [`requestContentCardsRefresh`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/request-content-cards-refresh.html) aufrufen. 

{% subtabs local %}
{% subtab Java %}

```java
Braze.getInstance(context).requestContentCardsRefresh();
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
Braze.getInstance(context).requestContentCardsRefresh()
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab iOS %}

Sie können jederzeit eine manuelle Aktualisierung von Braze Content-Cards über das Swift SDK anfragen, indem Sie die Methode [`requestRefresh`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/requestrefresh(_:)) in der Klasse [`Braze.ContentCards`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class) aufrufen:

{% subtabs local %}
{% subtab Swift %}

In Swift können Content-Cards entweder mit einem optionalen Completion Handler oder mit einer asynchronen Rückgabe unter Verwendung der nativen Swift Concurrency APIs aktualisiert werden.

### Completion Handler

```swift
AppDelegate.braze?.contentCards.requestRefresh { result in
  // Implement completion handler
}
```

### Async/Wartezeit

```swift
let contentCards = await AppDelegate.braze?.contentCards.requestRefresh()
```
{% endsubtab %}
{% subtab Objective-C %}

```objc
[AppDelegate.braze.contentCards requestRefreshWithCompletion:^(NSArray<BRZContentCardRaw *> * contentCards, NSError * error) {
  // Implement completion handler
}];
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Web %}

Sie können jederzeit eine manuelle Aktualisierung der Braze Content-Cards über das Web SDK anfragen, indem Sie [`requestContentCardsRefresh()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestcontentcardsrefresh) aufrufen. 

Sie können auch [`getCachedContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#getcachedcontentcards) aufrufen, um alle derzeit verfügbaren Karten von der letzten Aktualisierung der Content-Cards zu erhalten. 

```javascript
import * as braze from "@braze/web-sdk";

function refresh() {
  braze.requestContentCardsRefresh();    
}
```

{% endtab %}
{% endtabs %}


{% alert important %}
Sie können bis zu fünf Anrufe in kurzer Folge tätigen. Danach wird alle 180 Sekunden ein neuer Anruf verfügbar sein. Das System hält bis zu fünf Anrufe für Sie bereit, die Sie jederzeit nutzen können.
{% endalert %}

## Anpassen der angezeigten Kartenbestellung

Sie können die Reihenfolge ändern, in der Ihre Content-Cards angezeigt werden. So können Sie das Nutzererlebnis durch die Priorisierung bestimmter Arten von Inhalten, wie z. B. zeitkritischer Aktionen, feinabstimmen.

{% tabs %}
{% tab Android View System %}

Die [`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html) verlässt sich auf eine [`IContentCardsUpdateHandler`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.handlers/-i-content-cards-update-handler/index.html) um alle Sortierungen oder Änderungen von Content-Cards zu verarbeiten, bevor sie im Feed angezeigt werden. Einen angepassten Update Handler können Sie über [`setContentCardUpdateHandler`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/set-content-card-update-handler.html) auf Ihrer `ContentCardsFragment` eingestellt werden.

Das Folgende ist der Standard `IContentCardsUpdateHandler` und kann als Ausgangspunkt für Anpassungen verwendet werden:

{% subtabs local %}
{% subtab Java %}

```java
public class DefaultContentCardsUpdateHandler implements IContentCardsUpdateHandler {

  // Interface that must be implemented and provided as a public CREATOR
  // field that generates instances of your Parcelable class from a Parcel.
  public static final Parcelable.Creator<DefaultContentCardsUpdateHandler> CREATOR = new Parcelable.Creator<DefaultContentCardsUpdateHandler>() {
    public DefaultContentCardsUpdateHandler createFromParcel(Parcel in) {
      return new DefaultContentCardsUpdateHandler();
    }

    public DefaultContentCardsUpdateHandler[] newArray(int size) {
      return new DefaultContentCardsUpdateHandler[size];
    }
  };

  @Override
  public List<Card> handleCardUpdate(ContentCardsUpdatedEvent event) {
    List<Card> sortedCards = event.getAllCards();
    // Sort by pinned, then by the 'updated' timestamp descending
    // Pinned before non-pinned
    Collections.sort(sortedCards, new Comparator<Card>() {
      @Override
      public int compare(Card cardA, Card cardB) {
        // A displays above B
        if (cardA.getIsPinned() && !cardB.getIsPinned()) {
          return -1;
        }

        // B displays above A
        if (!cardA.getIsPinned() && cardB.getIsPinned()) {
          return 1;
        }

        // At this point, both A & B are pinned or both A & B are non-pinned
        // A displays above B since A is newer
        if (cardA.getUpdated() > cardB.getUpdated()) {
          return -1;
        }

        // B displays above A since A is newer
        if (cardA.getUpdated() < cardB.getUpdated()) {
          return 1;
        }

        // At this point, every sortable field matches so keep the natural ordering
        return 0;
      }
    });

    return sortedCards;
  }

  // Parcelable interface method
  @Override
  public int describeContents() {
    return 0;
  }

  // Parcelable interface method
  @Override
  public void writeToParcel(Parcel dest, int flags) {
    // No state is kept in this class so the parcel is left unmodified
  }
}
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
class DefaultContentCardsUpdateHandler : IContentCardsUpdateHandler {
  override fun handleCardUpdate(event: ContentCardsUpdatedEvent): List<Card> {
    val sortedCards = event.allCards
    // Sort by pinned, then by the 'updated' timestamp descending
    // Pinned before non-pinned
    sortedCards.sortWith(Comparator sort@{ cardA: Card, cardB: Card ->
      // A displays above B
      if (cardA.isPinned && !cardB.isPinned) {
        return@sort -1
      }

      // B displays above A
      if (!cardA.isPinned && cardB.isPinned) {
        return@sort 1
      }

      // At this point, both A & B are pinned or both A & B are non-pinned
      // A displays above B since A is newer
      if (cardA.updated > cardB.updated) {
        return@sort -1
      }

      // B displays above A since A is newer
      if (cardA.updated < cardB.updated) {
        return@sort 1
      }
      0
    })
    return sortedCards
  }

  // Parcelable interface method
  override fun describeContents(): Int {
    return 0
  }

  // Parcelable interface method
  override fun writeToParcel(dest: Parcel, flags: Int) {
    // No state is kept in this class so the parcel is left unmodified
  }

  companion object {
    // Interface that must be implemented and provided as a public CREATOR
    // field that generates instances of your Parcelable class from a Parcel.
    val CREATOR: Parcelable.Creator<DefaultContentCardsUpdateHandler?> = object : Parcelable.Creator<DefaultContentCardsUpdateHandler?> {
      override fun createFromParcel(`in`: Parcel): DefaultContentCardsUpdateHandler? {
        return DefaultContentCardsUpdateHandler()
      }

      override fun newArray(size: Int): Array<DefaultContentCardsUpdateHandler?> {
        return arrayOfNulls(size)
      }
    }
  }
}
```

{% endsubtab %}
{% endsubtabs %}

Den Quellcode von `ContentCardsFragment` finden Sie auf [GitHub](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/java/com/braze/ui/contentcards/ContentCardsFragment.kt).

{% endtab %}
{% tab Jetpack Compose %}
Um Content-Cards in Jetpack Compose zu filtern und zu sortieren, legen Sie den Parameter `cardUpdateHandler` fest. Zum Beispiel:

```kotlin
ContentCardsList(
    cardUpdateHandler = {
        it.sortedWith { cardA, cardB ->
            // A displays above B
            if (cardA.isPinned && !cardB.isPinned) {
                return@sortedWith -1
            }
            // B displays above A
            if (!cardA.isPinned && cardB.isPinned) {
                return@sortedWith 1
            }
            // At this point, both A & B are pinned or both A & B are non-pinned
            // A displays above B since A is newer
            if (cardA.updated > cardB.updated) {
                return@sortedWith -1
            }
            // B displays above A since A is newer
            if (cardA.updated < cardB.updated) {
                return@sortedWith 1
            }
            0
        }
    }
)
```
{% endtab %}
{% tab iOS %}

{% subtabs %}
{% subtab Swift %}

Passen Sie die Reihenfolge des Card-Feeds an, indem Sie direkt die statische Variable [`Attributes.defaults`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/defaults) ändern.

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.transform = { cards in
    cards.sorted {
        if $0.pinned && !$1.pinned {
            return true
        } else if !$0.pinned && $1.pinned {
            return false
        } else {
            return $0.createdAt > $1.createdAt
        }
    }
}
let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)
```

{% endsubtab %}
{% subtab Objective-C %}

Die Anpassung über `BrazeContentCardUI.ViewController.Attributes` ist in Objective-C nicht möglich. 

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Web %}

Passen Sie die Anzeigereihenfolge der Content-Cards in Ihrem Feed an, indem Sie den Parameter [`filterFunction`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showcontentcards) von `showContentCards():` verwenden. Zum Beispiel:

```javascript
braze.showContentCards(null, (cards) => {
  return sortBrazeCards(cards); // Where sortBrazeCards is your sorting function that returns the sorted card array
});
```

{% endtab %}
{% endtabs %}

## Anpassen der Nachricht "Leerer Feed"

Wenn sich ein:e Nutzer:in für keine Content-Cards qualifiziert, zeigt das SDK die Fehlermeldung "Leerer Feed" an: "Wir haben keine Updates. Bitte schauen Sie später noch einmal nach." Sie können diese Fehlermeldung "Leerer Feed" in etwa wie folgt anpassen:

![Eine "Leerer Feed"-Fehlermeldung, die lautet: "This is a custom empty state message."]({% image_buster/assets/img/content_cards/content-card-customization-empty.png %})

{% tabs %}
{% tab Android View System %}

Wenn [`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html) feststellt, dass der oder die Nutzer:in für keine Content-Cards in Frage kommt, zeigt es die Fehlermeldung "Leerer Feed" an.

Ein spezieller Adapter, der [`EmptyContentCardsAdapter`](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/java/com/braze/ui/contentcards/adapters/EmptyContentCardsAdapter.kt), ersetzt den Standard [`ContentCardAdapter`](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/java/com/braze/ui/contentcards/adapters/ContentCardAdapter.kt) um diese Fehlermeldung anzuzeigen. Um die angepasste Nachricht selbst einzustellen, überschreiben Sie die String-Ressource `com_braze_feed_empty`.

Den Stil, der zur Anzeige dieser Nachricht verwendet wird, finden Sie unter [`Braze.ContentCardsDisplay.Empty`](https://github.com/braze-inc/braze-android-sdk/blob/2e386dfa59a87bfc24ef7cb6ff5adf6b16f44d24/android-sdk-ui/src/main/res/values/styles.xml#L522-L530). Er wird im folgenden Code Snippet wiedergegeben:

```xml
<style name="Braze.ContentCardsDisplay.Empty">
  <item name="android:lineSpacingExtra">1.5dp</item>
  <item name="android:text">@string/com_braze_feed_empty</item>
  <item name="android:textColor">@color/com_braze_content_card_empty_text_color</item>
  <item name="android:textSize">18.0sp</item>
  <item name="android:gravity">center</item>
  <item name="android:layout_height">match_parent</item>
  <item name="android:layout_width">match_parent</item>
</style>
```

Weitere Informationen zum Anpassen der Content-Card-Stil-Elemente finden Sie unter [Stil anpassen]({{site.baseurl}}/developer_guide/content_cards/customizing_styles/).
{% endtab %}
{% tab Jetpack Compose %}
Um die Fehlermeldung "Leerer Feed" mit Jetpack Compose anzupassen, können Sie `emptyString` an `ContentCardsList` übergeben. Sie können auch `emptyTextStyle` an `ContentCardListStyling` übergeben, um diese Nachricht weiter anzupassen.

```kotlin
ContentCardsList(
    emptyString = "No messages today",
    style = ContentCardListStyling(
        emptyTextStyle = TextStyle(...)
    )
)
```

Wenn Sie ein Composable haben, das Sie stattdessen anzeigen möchten, können Sie `emptyComposable` an `ContentCardsList` übergeben. Wenn `emptyComposable` angegeben wird, wird `emptyString` nicht verwendet.

```kotlin
ContentCardsList(
    emptyComposable = {
        Image(
            painter = painterResource(id = R.drawable.noMessages),
            contentDescription = "No messages"
        )
    }
)
```
{% endtab %}
{% tab iOS %}
{% subtabs local %}
{% subtab Swift %}

Passen Sie den leeren Zustand des View Controller an, indem Sie die entsprechenden [`Attributes`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/defaults) setzen.

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.emptyStateMessage = "This is a custom empty state message"
attributes.emptyStateMessageFont = .preferredFont(forTextStyle: .title1)
attributes.emptyStateMessageColor = .secondaryLabel
```

{% endsubtab %}
{% subtab Objective-C %}

Ändern Sie die Sprache, die automatisch in leeren Content-Card-Feeds erscheint, indem Sie die lokalisierbaren Content-Card-Strings in der [`ContentCardsLocalizable.strings`](https://github.com/braze-inc/braze-swift-sdk/tree/main/Sources/BrazeUI/Resources/Localization/en.lproj)-Datei Ihrer App neu definieren.

{% alert note %}
Wenn Sie diese Nachricht in verschiedenen Lokalisierungssprachen aktualisieren möchten, suchen Sie die entsprechende Sprache in der [Ordnerstruktur Ressourcen](https://github.com/braze-inc/braze-swift-sdk/tree/main/Sources/BrazeUI/Resources/Localization) mit dem String `ContentCardsLocalizable.strings`.
{% endalert %}

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Web %}

Das Web SDK unterstützt keine programmatische Ersetzung der Sprache für "Leerer Feed". Sie können ihn bei jeder Anzeige des Feeds ersetzen. Dies ist jedoch nicht empfehlenswert, da die Aktualisierung des Feeds einige Zeit in Anspruch nehmen kann und der leere Feedtext nicht sofort angezeigt wird. 

{% endtab %}
{% endtabs %}

## Mehrere Feeds

Content-Cards können in Ihrer App gefiltert werden, sodass nur bestimmte Karten angezeigt werden. So können Sie mehrere Content-Card-Feeds für verschiedene Anwendungsfälle haben. Sie können zum Beispiel sowohl einen Transaktions-Feed als auch einen Marketing-Feed pflegen. Um dies zu erreichen, erstellen Sie verschiedene Kategorien von Content-Cards, indem Sie Schlüssel-Wert-Paare im Braze-Dashboard festlegen. Dann erstellen Sie in Ihrer App oder Website Feeds, die diese Arten von Content-Cards unterschiedlich behandeln, indem Sie einige Typen herausfiltern und andere anzeigen.

### Schritt 1: Schlüssel-Wert-Paare auf Karten setzen

Wenn Sie eine Content-Card-Kampagne erstellen, legen Sie [Daten mit Schlüssel-Wert-Paaren]({{site.baseurl}}/developer_guide/content_cards/customizing_behavior/) auf jeder Karte fest. Sie werden dieses Schlüssel-Wert-Paar verwenden, um die Karten zu kategorisieren. Schlüssel-Wert-Paare werden in der Eigenschaft `extras` im Datenmodell der Karte gespeichert.

In diesem Beispiel legen wir ein Schlüssel-Wert-Paar mit dem Schlüssel `feed_type` fest, das angibt, in welchem Content-Card-Feed die Karte angezeigt werden soll. Der Wert wird derjenige sein, den Sie für Ihre angepassten Feeds verwenden, z. B. `home_screen` oder `marketing`.

### Schritt 2: Content-Cards filtern

Sobald Sie die Schlüssel-Wert-Paare zugewiesen haben, erstellen Sie einen Feed mit einer Logik, die die gewünschten Karten anzeigt und Karten anderer Typen filtert. In diesem Beispiel werden nur Karten mit einem passenden Schlüssel-Wert-Paar von `feed_type: "Transactional"` angezeigt.

{% tabs %}
{% tab Android View System %}

Sie können Content-Cards herausfiltern, indem Sie die Schlüssel-Wert-Paare auslesen, die auf dem Dashboard über [`Card.getExtras()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/extras.html) eingelesen werden und mit einem angepassten Update Handler gefiltert (oder mit einer beliebigen anderen Logik verarbeitet) werden.

Genauer gesagt, wird Ihr Content-Card-Feed in einem [`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html) angezeigt Der Standard `IContentCardsUpdateHandler` nimmt eine [`ContentCardsUpdatedEvent`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.events/-content-cards-updated-event/index.html) aus dem Braze SDK und gibt eine Liste der anzuzeigenden Karten zurück, sortiert aber nur die Karten und führt selbst keine Entfernungen oder Filterungen durch.

Um einem `ContentCardsFragment` das Filtern zu erlauben, erstellen Sie einen angepassten [`IContentCardsUpdateHandler`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.handlers/-i-content-cards-update-handler/index.html). Ändern Sie diese `IContentCardsUpdateHandler`, um alle Karten aus der Liste zu entfernen, die nicht unserem gewünschten Wert für `feed_type` entsprechen, den wir zuvor festgelegt haben. Zum Beispiel:

{% subtabs local %}
{% subtab Java %}

```java
private IContentCardsUpdateHandler getUpdateHandlerForFeedType(final String desiredFeedType) {
  return new IContentCardsUpdateHandler() {
    @Override
    public List<Card> handleCardUpdate(ContentCardsUpdatedEvent event) {
      // Use the default card update handler for a first
      // pass at sorting the cards. This is not required
      // but is done for convenience.
      final List<Card> cards = new DefaultContentCardsUpdateHandler().handleCardUpdate(event);

      final Iterator<Card> cardIterator = cards.iterator();
      while (cardIterator.hasNext()) {
        final Card card = cardIterator.next();

        // Make sure the card has our custom KVP
        // from the dashboard with the key "feed_type"
        if (card.getExtras().containsKey("feed_type")) {
          final String feedType = card.getExtras().get("feed_type");
          if (!desiredFeedType.equals(feedType)) {
            // The card has a feed type, but it doesn't match
            // our desired feed type, remove it.
            cardIterator.remove();
          }
        } else {
          // The card doesn't have a feed
          // type at all, remove it
          cardIterator.remove();
        }
      }

      // At this point, all of the cards in this list have
      // a feed type that explicitly matches the value we put
      // in the dashboard.
      return cards;
    }
  };
}
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
private fun getUpdateHandlerForFeedType(desiredFeedType: String): IContentCardsUpdateHandler {
  return IContentCardsUpdateHandler { event ->
    // Use the default card update handler for a first
    // pass at sorting the cards. This is not required
    // but is done for convenience.
    val cards = DefaultContentCardsUpdateHandler().handleCardUpdate(event)

    val cardIterator = cards.iterator()
    while (cardIterator.hasNext()) {
      val card = cardIterator.next()

      // Make sure the card has our custom KVP
      // from the dashboard with the key "feed_type"
      if (card.extras.containsKey("feed_type")) {
        val feedType = card.extras["feed_type"]
        if (desiredFeedType != feedType) {
          // The card has a feed type, but it doesn't match
          // our desired feed type, remove it.
          cardIterator.remove()
        }
      } else {
        // The card doesn't have a feed
        // type at all, remove it
        cardIterator.remove()
      }
    }

    // At this point, all of the cards in this list have
    // a feed type that explicitly matches the value we put
    // in the dashboard.
    cards
  }
}
```

{% endsubtab %}
{% endsubtabs %}

Nachdem Sie einen `IContentCardsUpdateHandler` erstellt haben, erstellen Sie ein `ContentCardsFragment`, das den Handler verwendet. Dieser angepasste Feed kann wie jedes andere `ContentCardsFragment` verwendet werden. Zeigen Sie in den verschiedenen Bereichen Ihrer App verschiedene Content-Card-Feeds an, die auf dem Schlüssel im Dashboard basieren. Jedes `ContentCardsFragment` Futtermittel wird dank der angepassten `IContentCardsUpdateHandler` auf jedem Fragment einen eindeutigen Satz von Karten anzeigen. 

Zum Beispiel:

{% subtabs local %}
{% subtab Java %}

```java
// We want a Content Cards feed that only shows "Transactional" cards.
ContentCardsFragment customContentCardsFragment = new ContentCardsFragment();
customContentCardsFragment.setContentCardUpdateHandler(getUpdateHandlerForFeedType("Transactional"));
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
// We want a Content Cards feed that only shows "Transactional" cards.
val customContentCardsFragment = ContentCardsFragment()
customContentCardsFragment.contentCardUpdateHandler = getUpdateHandlerForFeedType("Transactional")
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Jetpack Compose %}
Um zu filtern, welche Inhaltskarten in diesem Feed angezeigt werden, verwenden Sie `cardUpdateHandler`. Zum Beispiel:

```kotlin
ContentCardsList(
     cardUpdateHandler = {
         it.filter { card ->
             card.extras["feed_type"] == "Transactional"
         }
     }
 )
 ```
{% endtab %}
{% tab iOS %}

Das folgende Beispiel zeigt den Content-Cards-Feed für Karten vom Typ `Transactional`:

{% subtabs %}
{% subtab Swift %}

```swift
// Filter cards by the `Transactional` feed type based on your key-value pair.
let transactionalCards = cards.filter { $0.extras["feed_type"] as? String == "Transactional" }
```

Um noch einen Schritt weiter zu gehen, können Sie die im View Controller angezeigten Karten filtern, indem Sie die Eigenschaft `transform` auf Ihrer `Attributes` struct so einstellen, dass nur die nach Ihren Kriterien gefilterten Karten angezeigt werden.

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.transform = { cards in
  cards.filter { $0.extras["feed_type"] as? String == "Transactional" }
}

// Pass your attributes containing the transformed cards to the Content Card UI.
let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)
```

{% endsubtab %}
{% subtab Objective-C %}

```objc
// Filter cards by the `Transactional` feed type based on your key-value pair.
NSMutableArray<BRZContentCardRaw *> *transactionalCards = [[NSMutableArray alloc] init];
for (BRZContentCardRaw *card in AppDelegate.braze.contentCards.cards) {
  if ([card.extras[@"feed_type"] isEqualToString:@"Transactional"]) {
    [transactionalCards addObject:card];
  }
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Web %}

Das folgende Beispiel zeigt den Content-Cards-Feed für Karten vom Typ `Transactional`:

```javascript

/**
 * @param {String} feed_type - value of the "feed_type" KVP to filter
 */
function showCardsByFeedType(feed_type) {
  braze.showContentCards(null, function(cards) {
    return cards.filter((card) => card.extras["feed_type"] === feed_type);
  });
}
```

Dann können Sie einen Toggle für Ihren angepassten Feed einrichten:

```javascript
// show the "Transactional" feed when this button is clicked
document.getElementById("show-transactional-feed").onclick = function() {
  showCardsByFeedType("Transactional"); 
};
```

Weitere Informationen finden Sie in der [Dokumentation zu den SDK-Methoden](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showcontentcards).

{% endtab %}
{% endtabs %}


