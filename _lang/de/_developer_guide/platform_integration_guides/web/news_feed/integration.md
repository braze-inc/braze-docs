---
nav_title: Integration
article_title: News Feed Integration für das Web
platform: Web
page_order: 0
page_type: reference
description: "Dieser Artikel behandelt den Kartentyp \"Newsfeed\" und beschreibt, wie Sie den Newsfeed über das Braze SDK in Ihre Web-Anwendung integrieren."
channel: news feed

---

# Integration von News Feeds

> Dieser Artikel beschreibt, wie Sie einen Newsfeed für das Braze Web SDK einrichten.

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

Der News Feed ist ein vollständig anpassbarer In-App-Inhalts-Feed für Ihre Nutzer. Unser Targeting und unsere Segmentierung ermöglichen es Ihnen, einen Strom von Inhalten zu erstellen, der individuell auf die Interessen jedes Nutzers zugeschnitten ist. Je nach Position im Nutzer-Lifecycle und der Art Ihrer App kann dies ein Onboarding-Content-Server, ein Advertisement-Center, ein Achievement-Center oder ein allgemeines News-Center sein.

## Beispiel News Feed

<img src="{% image_buster /assets/img_archive/WebNewsFeed.png %}" alt="Beispiel für einen Newsfeed, der mehrere Benachrichtigungen anzeigt, z. B. Nachfragen, Update-Benachrichtigungen, Werbung und mehr." height="600" />

## Integration

Um die Anzeige des Newsfeeds über das Braze Web SDK umzuschalten, rufen Sie einfach Folgendes auf:

``` javascript
braze.toggleFeed();
```

Dies zeigt die neuesten im Cache gespeicherten News Feed-Karten an (und löst eine Aktualisierung aus, wenn diese Karten mehr als 1 Minute alt sind oder wenn der News Feed noch nie aktualisiert wurde) und aktualisiert die Anzeige automatisch, wenn neue Karten von den Braze-Servern empfangen werden, solange sie auf dem Bildschirm angezeigt wird.

Standardmäßig wird der Feed in einer fest positionierten Seitenleiste auf der rechten Seite der Website angezeigt (oder als Vollbild-Overlay auf mobilen Geräten, durch responsives CSS). Wenn Sie dieses Verhalten außer Kraft setzen und einen statisch positionierten News Feed innerhalb Ihres eigenen übergeordneten Elements anzeigen möchten, geben Sie das folgende Element als erstes Argument für `showFeed` an:

``` javascript
braze.toggleFeed(document.getElementById('my-news-feed-parent'));
```

Wenn Sie einen bestimmten statischen Satz von News Feed-Karten anzeigen, die Karten vom Server filtern oder Ihre eigene Aktualisierungssemantik bereitstellen möchten, können Sie die automatische Aktualisierung deaktivieren und Ihre eigenen Karten bereitstellen:

``` javascript
braze.subscribeToFeedUpdates(function(feed) {
  var cards = feed.cards;
  braze.showFeed(undefined, cards);
});
braze.requestFeedRefresh();
```

In den [JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showfeed) finden Sie die vollständige Dokumentation zu `showFeed`, `destroyFeed` und `toggleFeed`.

## Karten-Typen

Das Braze Web SDK unterstützt 3 einzigartige News-Feed-Kartentypen: [ClassicCard](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.classiccard.html), [Banner](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html) und [CaptionedImage](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.captionedimage.html), die sich ein Basismodell teilen: [Card](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html).

### Abfrage der Anzahl ungelesener Karten

Sie können die Anzahl der ungelesenen Karten jederzeit telefonisch erfragen:

``` javascript
braze.getCachedFeed().getUnreadCardCount();
```

Dies wird oft verwendet, um die Anzahl der ungelesenen News Feed-Karten anzuzeigen. Weitere Informationen finden Sie in den [JS Reference Docs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.feed.html). Beachten Sie, dass Braze die Newsfeed-Cards beim Laden einer neuen Seite nicht aktualisiert (und diese Funktion daher 0 zurückgibt), bis Sie den Feed anzeigen oder `braze.requestFeedRefresh();` aufrufen.

### Schlüssel-Wert-Paare

Objekte des Typs `Card` können optional Schlüssel-Wert-Paare als `extras` enthalten. Diese können verwendet werden, um Daten zusammen mit einer Karte zur weiteren Bearbeitung durch die Anwendung zu senden. Rufen Sie einfach `card.extras` auf, um auf diese Werte zuzugreifen.

## Anpassung

Die UI-Elemente von Braze sind standardmäßig an die Editoren im Braze-Dashboard angepasst und auf Konsistenz mit anderen Mobilgeräte-Plattformen von Braze ausgelegt. Die Standardstile von Braze sind im Braze SDK in CSS definiert. Indem Sie ausgewählte Stile in Ihrer Anwendung außer Kraft setzen, können Sie unseren Standard-Feed mit Ihren eigenen Hintergrundbildern, Schriftfamilien, Stilen, Größen, Animationen und vielem mehr anpassen.

Im Folgenden finden Sie ein Beispiel für eine Überschreibung, die bewirkt, dass der News Feed 800 px breit erscheint:

``` css
body .ab-feed {
  width: 800px;
}
```

## Kategorien

Instanzen des Braze News Feed können so konfiguriert werden, dass sie nur Karten aus einer bestimmten "Kategorie" empfangen. Dies ermöglicht die effektive Integration mehrerer Newsfeed-Streams in einer einzigen Anwendung.

Newsfeed-Kategorien können definiert werden, indem der dritte Parameter `allowedCategories` an `toggleFeed` übergeben wird:

``` javascript
braze.toggleFeed(undefined, undefined, [braze.Card.Category.NEWS]);
```

Sie können einen Feed auch wie im folgenden Beispiel mit einer Kombination von Kategorien füllen:

``` javascript
braze.toggleFeed(undefined, undefined, [braze.Card.Category.ANNOUNCEMENTS, braze.Card.Category.NEWS]);
```

## Indikatoren für gelesen und ungelesen

Braze bietet eine Anzeige für ungelesene und gelesene Nachrichten auf den News Feed-Karten, wie unten abgebildet:

![Eine News-Feed-Karte, die ein Bild einer Uhr zusammen mit etwas Text zeigt. In der oberen rechten Ecke des Textes befindet sich ein blaues oder graues Dreieck, das anzeigt, ob eine Karte gelesen wurde oder nicht. Ein blaues Dreieck zeigt an, dass eine Karte gelesen wurde.]({% image_buster /assets/img_archive/UnreadvsReadNewsFeedCard.png %})

### Deaktivieren der Indikatoren

Um diese Funktion zu deaktivieren, fügen Sie den folgenden Stil zu Ihrem CSS hinzu:

``` css
.ab-read-dot { display: none; }
.ab-read-indicator { display: none; }
```

