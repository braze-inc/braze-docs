---
nav_title: Anpassen der Kartenstile
article_title: Inhaltskartenstile anpassen
page_order: 1
description: "Dieser Artikel behandelt die Gestaltungsmöglichkeiten für Ihre Inhaltskarten."
channel:
  - content cards
platform:
  - Android
  - FireOS
  - Swift
  - Web
---

# Anpassen von Content-Card-Stilen

> Braze Content Cards werden mit einem Standard-Look and Feel geliefert. Dieser Artikel befasst sich mit den Styling-Optionen für Ihre Content Cards, die Sie an Ihre Markenidentität anpassen können. Einen grundlegenden Überblick über die Arten von Anpassungsmöglichkeiten, die Sie mit Content Cards haben, finden Sie unter [Übersicht über die Anpassung]({{site.baseurl}}/developer_guide/getting_started/customization_overview). 

## Anpassen von Stilen

Die Standard-Benutzeroberfläche für Content Cards wird aus der Benutzeroberflächenschicht des Braze SDK importiert. Von dort aus können Sie bestimmte Teile des Designs der Karte, die Reihenfolge der Karten und die Art und Weise, wie der Feed Ihren Nutzern angezeigt wird, optimieren.

![Zwei Inhaltskarten, eine mit der Standardschriftart und quadratischen Ecken und eine mit abgerundeten Ecken und einer geschweiften Schriftart]({% image_buster/assets/img/content_cards/content-card-customization-attributes.png %})

{% alert note %}
Eigenschaften von Content-Cards wie `title`, `cardDescription`, `imageUrl` usw. können direkt über das [Dashboard]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details) bearbeitet werden, was die bevorzugte Methode zum Ändern dieser Details ist.
{% endalert %}


{% tabs %}
{% tab Android %}

Standardmäßig entsprechen die Android und FireOS SDK Content Cards den Standardrichtlinien für die Android-Benutzeroberfläche, um ein nahtloses Erlebnis zu bieten. Sie können diese Standardstile in der Datei [`res/values/styles.xml`](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/res/values/styles.xml) in der Braze SDK-Distribution sehen:

```xml
  <style name="Braze.ContentCards.CaptionedImage.Description">
    <item name="android:textColor">@color/com_braze_description</item>
    <item name="android:textSize">15.0sp</item>
    <item name="android:includeFontPadding">false</item>
    <item name="android:paddingBottom">8.0dp</item>
    <item name="android:layout_marginLeft">10.0dp</item>
    <item name="android:layout_marginRight">10.0dp</item>
    <item name="android:layout_marginTop">8.0dp</item>
    <item name="android:layout_width">match_parent</item>
    <item name="android:layout_below">@id/com_braze_content_cards_captioned_image_card_title_container</item>
  </style>
```

Um den Stil Ihrer Content-Cards anzupassen, können Sie dieses Standardstile einfach überschreiben. Um einen Stil zu überschreiben, kopieren Sie ihn in seiner Gesamtheit in die Datei `styles.xml` Ihres Projekts und nehmen Sie die gewünschten Änderungen vor. Der gesamte Stil muss in Ihre lokale Datei `styles.xml` kopiert werden, damit alle Attribute korrekt gesetzt werden.

{% subtabs local %}
{% subtab Correct style override %}

```xml
<style name="Braze.ContentCardsDisplay">
  <item name="android:background">@color/mint</item>
  <item name="android:cacheColorHint">@color/mint</item>
  <item name="android:divider">@android:color/transparent</item>
  <item name="android:dividerHeight">16.0dp</item>
  <item name="android:paddingLeft">12.5dp</item>
  <item name="android:paddingRight">5.0dp</item>
  <item name="android:scrollbarStyle">outsideInset</item>
</style>
```

{% endsubtab %}
{% subtab Incorrect style override %}

```xml
<style name="Braze.ContentCardsDisplay">
  <item name="android:background">@color/mint</item>
  <item name="android:cacheColorHint">@color/mint</item>
</style>
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Jetpack Compose %}

Standardmäßig entsprechen die Android und FireOS SDK Content Cards den Standardrichtlinien für die Android-Benutzeroberfläche, um ein nahtloses Erlebnis zu bieten.

Es gibt zwei Möglichkeiten, einen Stil anzuwenden. Die erste besteht darin, `ContentCardListStyling` und `ContentCardStyling` wie im folgenden Beispiel an `ContentCardsList()` zu übergeben:

```kotlin
ContentCardsList(
    style = ContentCardListStyling(listBackgroundColor = Color.Red),
    cardStyle = ContentCardStyling(
        titleTextStyle = TextStyle(
            fontFamily = fontFamily,
            fontSize = 25.sp
        ),
        shadowRadius = 10.dp,
        shortNewsContentCardStyle = BrazeShortNewsContentCardStyling(
            shadowRadius = 15.dp
        )
    )
)
```

Die zweite Möglichkeit ist, BrazeStyle zu verwenden, um einen globalen Stil für Braze-Komponenten zu erstellen. Siehe hierzu das folgende Beispiel:

```kotlin
BrazeStyle(
    contentCardStyle = ContentCardStyling(
        textAnnouncementContentCardStyle = BrazeTextAnnouncementContentCardStyling(
            cardBackgroundColor = Color.Red,
            descriptionTextStyle = TextStyle(
                fontFamily = fontFamily,
                fontSize = 25.sp,
            )
        ),
        titleTextColor = Color.Magenta
    )
) {
    // Your app here, including any ContentCardsList() in it
}
```

{% endtab %}
{% tab iOS %}

Mit dem View Controller für Content-Cards können Sie das Aussehen und Verhalten aller Zellen über die Struktur [`BrazeContentCardUI.ViewController.Attributes`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct) anpassen. Die Konfiguration von Content Cards mit `Attributes` ist eine einfache Option, mit der Sie Ihre Content Cards-Benutzeroberfläche mit minimaler Einrichtung starten können. 

{% alert important %}
Die Anpassung über `Attributes` ist nur in Swift möglich.
{% endalert %}

{% subtabs %}
{% subtab Swift %}

**Ändern von `Attributes.default`**

Passen Sie das Aussehen aller Instanzen des Braze Content Card UI View Controllers an, indem Sie die statische Variable [`Attributes.defaults`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/defaults) direkt ändern.

So ändern Sie beispielsweise die Standardbildgröße und den Eckenradius für alle Zellen:

```swift
BrazeContentCardUI.ViewController.Attributes.defaults.cellAttributes.cornerRadius = 20
BrazeContentCardUI.ViewController.Attributes.defaults.cellAttributes.classicImageSize = CGSize(width: 65, height: 65)
```

**Initialisierung des View Controllers mit Attributen**

Wenn Sie nur eine bestimmte Instanz des Braze Content Card UI View Controllers ändern möchten, verwenden Sie den Initialisierer [`init(braze:attributes:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/init(braze:attributes:)/), um eine angepasste Struktur `Attributes` an den View Controller zu übergeben.

So können Sie zum Beispiel die Bildgröße und den Eckenradius für eine bestimmte Instanz des View Controllers ändern:

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.cellAttributes.cornerRadius = 20
attributes.cellAttributes.classicImageSize = CGSize(width: 65, height: 65)

let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)
```

**Anpassen von Zellen mithilfe von Unterklassen**

Alternativ können Sie auch angepasste Schnittstellen erstellen, indem Sie angepasste Klassen für jeden gewünschten Kartentyp registrieren. Um anstelle der Standardzelle eine Unterklasse zu verwenden, ändern Sie die Eigenschaft [`cells`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/cells) in der Struktur `Attributes`. Zum Beispiel:

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
// Register your own custom cell
attributes.cells[BrazeContentCardUI.ClassicImageCell.identifier] = CustomClassicImageCell.self

let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)
```

**Programmatisches Ändern von Content-Cards**

Content-Cards können programmatisch geändert werden, indem der Funktionsabschluss [`transform`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/transform) in der Struktur `Attributes` zugewiesen wird. Das folgende Beispiel ändert die `title` und `description` von kompatiblen Karten:

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.transform = { cards in
  cards.map { card in
    var card = card
    if let title = card.title {
      card.title = "[modified] \(title)"
    }
    if let description = card.description {
      card.description = "[modified] \(description)"
    }
    return card
  }
}

let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)
```

In der [Beispiel-App Examples](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/Swift) finden Sie ein vollständiges Beispiel.

{% endsubtab %}
{% subtab Objective-C %}

Die Anpassung von Content-Cards über `Attributes` wird von Objective-C nicht unterstützt.

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Web %}

Die Standardstile von Braze sind im Braze SDK in CSS definiert. Indem Sie ausgewählte Stile in Ihrer Anwendung außer Kraft setzen, können Sie unseren Standard-Feed mit Ihren eigenen Hintergrundbildern, Schriftfamilien, Stilen, Größen, Animationen und vielem mehr anpassen. Das folgende Beispiel ist eine Überschreibung, die bewirkt, dass Content-Cards mit einer Breite von 800 Pixeln angezeigt werden:

``` css
body .ab-feed {
  width: 800px;
}
```

{% endtab %}
{% endtabs %}

## Vorgehensweisen bei Anpassungen 

Im Folgenden werden einige hilfreiche Vorgehensweisen für gängige Anpassungen beschrieben.

### Eigene Schriftart

Durch die Anpassung der in Ihren Content Cards verwendeten Schriftart können Sie Ihre Markenidentität wahren und ein visuell ansprechendes Erlebnis für Ihre Benutzer schaffen. Wenden Sie diese Vorgehensweisen an, wenn Sie die Schriftart für alle Content-Cards programmatisch festlegen möchten. 

{% tabs %}
{% tab Android %}

Um die Standardschriftart programmatisch zu ändern, legen Sie einen Stil für Karten fest und verwenden das Attribut `fontFamily`, um Braze anzuweisen, Ihre eigene Schriftfamilie zu verwenden.

Wenn Sie beispielsweise die Schriftart für alle Titel von Bildkarten mit Bildunterschriften aktualisieren möchten, überschreiben Sie den Stil `Braze.ContentCards.CaptionedImage.Title` und verweisen auf Ihre eigene Schriftfamilie. Der Wert des Attributs sollte auf eine Schriftfamilie in Ihrem Verzeichnis `res/font` verweisen.

Hier ist ein verkürztes Beispiel mit einer benutzerdefinierten Schriftfamilie, `my_custom_font_family`, auf die in der letzten Zeile verwiesen wird:

```xml
  <style name="Braze.ContentCards.CaptionedImage.Title">
    <item name="android:layout_width">wrap_content</item>
    ...
    <item name="android:fontFamily">@font/my_custom_font_family</item>
    <item name="fontFamily">@font/my_custom_font_family</item>
  </style>
```

Weitere Informationen zur Anpassung von Schriftarten im Android SDK finden Sie in der [Anleitung zur Schriftfamilie]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/font_customization/#font-customization).
{% endtab %}
{% tab Jetpack Compose %}
Um die Standardschriftart programmatisch zu ändern, können Sie `titleTextStyle` von `ContentCardStyling` festlegen.

Sie können auch `titleTextStyle` für einen bestimmten Kartentyp einstellen, indem Sie es auf `BrazeShortNewsContentCardStyling` einstellen und an `shortNewsContentCardStyle` von `ContentCardStyling` übergeben.

```kotlin
val fontFamily = FontFamily(
    Font(R.font.sailec_bold)
)

ContentCardStyling(
    titleTextStyle = TextStyle(
        fontFamily = fontFamily
    )
)
```
{% endtab %}
{% tab iOS %}
{% subtabs %}
{% subtab Swift %}

Passen Sie Ihre Schriftarten an, indem Sie `Attributes` der Instanz-Eigenschaft [`cellAttributes`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/cellattributes/) anpassen. Zum Beispiel:

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.cellAttributes.titleFont = .preferredFont(textStyle: .callout, weight: .bold)
attributes.cellAttributes.descriptionFont = .preferredFont(textStyle: .footnote, weight: .regular)
attributes.cellAttributes.domainFont = .preferredFont(textStyle: .footnote, weight: .medium)

let viewController = BrazeContentCardUI.ViewController.init(braze: braze, attributes: attributes)
```

{% endsubtab %}
{% subtab Objective-C %}

Das Anpassen von Schriftarten über `Attributes` wird in Objective-C nicht unterstützt. 

In der [Beispielanwendung Examples](https://github.com/braze-inc/braze-swift-sdk/blob/main/Examples/ObjC/Sources/ContentCards-Custom-UI/CardsInfoViewController.m#L97) finden Sie ein Beispiel für die Erstellung Ihrer eigenen Benutzeroberfläche mit benutzerdefinierten Schriftarten.

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Web %}

Sie können das Aussehen von Content-Cards wie jedes andere Web-Element ganz einfach über CSS anpassen. Verwenden Sie in Ihrer CSS-Datei oder in Inline-Styles die Eigenschaft `font-family` und geben Sie den gewünschten Schriftnamen oder den Schriftstapel an.

```css
/* CSS selector targeting the Content Card element */
.card-element {
  font-family: "Helvetica Neue", Arial, sans-serif;
}
```

{% endtab %}
{% endtabs %}

### Angepasste gepinnte Symbole

Bei der Erstellung einer Content-Card haben Marketer die Möglichkeit, die Karte zu pinnen. Eine angeheftete Karte wird oben im Feed eines Benutzers angezeigt und kann vom Benutzer nicht abgewählt werden. Beim Ändern der Kartenstile können Sie auch das Aussehen des gepinnten Symbols ändern.

![Side-by-Side-Vorschau der Content-Cards in Braze für Mobilgeräte und Web mit aktivierter Option "Diese Karte oben im Feed pinnen".]({% image_buster /assets/img/cc_pin_to_top.png %}){:style="border:none"}

{% tabs %}
{% tab Android %}

Um ein angepasstes gepinntes Symbol festzulegen, überschreiben Sie den Stil `Braze.ContentCards.PinnedIcon`. Ihr benutzerdefiniertes Bild-Asset sollte in dem Element `android:src` deklariert werden. Zum Beispiel:

```xml
  <style name="Braze.ContentCards.PinnedIcon">
    <item name="android:src">@drawable/{my_custom_image_here}</item>

    <item name="android:layout_width">wrap_content</item>
    <item name="android:layout_height">wrap_content</item>
    <item name="android:layout_alignParentRight">true</item>
    <item name="android:layout_alignParentTop">true</item>
    <item name="android:contentDescription">@null</item>
    <item name="android:importantForAccessibility">no</item>
  </style>
```

{% endtab %}
{% tab Jetpack Compose %}

Um das standardmäßige gepinnte Symbol zu ändern, können Sie `pinnedResourceId` von `ContentCardStyling` festlegen.  Zum Beispiel:

```kotlin
ContentCardStyling(
    pinnedResourceId = R.drawable.pushpin,
    pinnedImageAlignment = Alignment.TopCenter
)
```

Sie können auch einen Composable in `pinnedComposable` von `ContentCardStyling` angeben. Wenn `pinnedComposable` angegeben wird, wird der Wert `pinnedResourceId` überschrieben.

```kotlin
ContentCardStyling(
    pinnedComposable = {
        Box(Modifier.fillMaxWidth()) {
            Text(
                modifier = Modifier
                    .align(Alignment.Center)
                    .width(50.dp),
                text = "This message is not read. Please read it."
            )
        }
    }
)
```
{% endtab %}
{% tab iOS %}
{% subtabs %}
{% subtab Swift %}

Passen Sie das Pin-Symbol an, indem Sie die Eigenschaften `pinIndicatorColor` und `pinIndicatorImage` der Instanz-Eigenschaft [`cellAttributes`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/cellattributes/) ändern. Zum Beispiel:

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.cellAttributes.pinIndicatorColor = .red
attributes.cellAttributes.pinIndicatorImage = UIImage(named: "my-image")

let viewController = BrazeContentCardUI.ViewController.init(braze: braze, attributes: attributes)
```

Sie können auch Unterklassen verwenden, um Ihre eigene Version von `BrazeContentCardUI.Cell` zu erstellen, die den Pin-Indikator enthält. Zum Beispiel: 

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.cells[BrazeContentCardUI.ClassicImageCell.identifier] = CustomClassicImageCell.self

let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)
```

{% endsubtab %}
{% subtab Objective-C %}

Das Anpassen der Pin-Anzeige über `Attributes` wird in Objective-C nicht unterstützt.

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Web %}

Die Struktur des gepinnten Symbols für Content-Cards lautet wie folgt:

```css
<div class="ab-pinned-indicator">
  <i class="fa fa-star"></i>
</div>
```

Wenn Sie ein anderes FontAwesome-Symbol verwenden möchten, können Sie einfach den Klassennamen des Elements `i` durch den Klassennamen des gewünschten Symbols ersetzen. 

Wenn Sie das Symbol ganz austauschen möchten, entfernen Sie das Element `i` und fügen das benutzerdefinierte Symbol als untergeordnetes Element von `ab-pinned-indicator` hinzu. Es gibt verschiedene Möglichkeiten, wie Sie vorgehen können, aber eine einfache Methode wäre, `replaceChildren()` im Element `ab-pinned-indicator` zu verwenden.

Zum Beispiel:

```javascript
// Get the parent element
const pinnedIndicator = document.querySelector('.ab-pinned-indicator');

// Create a new custom icon element
const customIcon = document.createElement('span');
customIcon.classList.add('customIcon');

// Replace the existing icon with the custom icon
pinnedIndicator.replaceChildren(customIcon);
```

{% endtab %}
{% endtabs %}

### Ändern der Farbe der Ungelesen-Anzeige

Inhaltskarten enthalten eine blaue Linie am unteren Rand der Karte, die anzeigt, ob die Karte bereits angesehen wurde oder nicht. 

![Zwei Inhaltskarten werden nebeneinander angezeigt. Die erste Karte hat eine blaue Linie am unteren Rand, was bedeutet, dass sie nicht gesehen wurde. Die zweite Karte hat keine blaue Linie, was bedeutet, dass sie bereits gesehen wurde.]({% image_buster /assets/img/braze-content-cards-seen-unseen-behavior.png %})

{% tabs %}
{% tab Android %}

Ändern Sie die Farbe des Balkens für die Ungelesen-Anzeige, indem Sie den Wert in `com_braze_content_cards_unread_bar_color` in Ihrer `colors.xml` Datei ändern:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <!-- The color used to highlight unread Content Cards at their bottom edge -->
  <color name="com_braze_content_cards_unread_bar_color">#1676d0</color>
</resources>
```

{% endtab %}
{% tab Jetpack Compose %}

Um die Farbe des Balkens für die Ungelesen-Anzeige zu ändern, ändern Sie den Wert von `unreadIndicatorColor` in `ContentCardStyling`:

```kotlin
ContentCardStyling(
    unreadIndicatorColor = Color.Red
)
```

{% endtab %}
{% tab iOS %}

{% subtabs %}
{% subtab Swift %}

Ändern Sie die Farbe des Balkens für die Anzeige ungelesener Dokumente, indem Sie der Farbe Ihrer `BrazeContentCardUI.ViewController` Instanz einen Wert zuweisen:

```swift
let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze)
viewController.view.tintColor = .systemGreen
```

Wenn Sie jedoch nur die Nicht-aufgerufen-Anzeige ändern möchten, können Sie auf die Eigenschaft `unviewedIndicatorColor` der Struktur `BrazeContentCardUI.ViewController.Attributes` zugreifen. Wenn Sie in Braze `UITableViewCell`-Implementierungen verwenden, sollten Sie auf die Eigenschaft zugreifen, bevor die Zelle gezeichnet wird.

So setzen Sie beispielsweise die Farbe der Nicht-aufgerufen-Anzeige auf Rot:

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.cellAttributes.unviewedIndicatorColor = .red

let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)
```

In der [Beispiel-App Examples](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/Swift) finden Sie ein vollständiges Beispiel.

{% endsubtab %}
{% subtab Objective-C %}

Ändern Sie die Farbe des Balkens für die Anzeige ungelesener Dokumente, indem Sie der Farbe Ihres `BRZContentCardUIViewController` einen Wert zuweisen:

```objc
BRZContentCardUIViewController *viewController = [[BRZContentCardUIViewController alloc] initWithBraze:AppDelegate.braze];
[viewController.view setTintColor:[UIColor systemGreenColor]];
```

Es ist nicht möglich, in Objective-C über `Attributes` nur die Nicht-aufgerufen-Anzeige anzupassen.

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Web %}

Um die Farbe der Ungelesen-Anzeige einer Karte zu ändern, fügen Sie Ihrer Webseite ein benutzerdefiniertes CSS hinzu. So setzen Sie beispielsweise die Farbe der Nicht-aufgerufen-Anzeige auf Grün:

```css
.ab-unread-indicator { background-color: green; }
```

{% endtab %}
{% endtabs %}

### Ungelesen-Anzeige deaktivieren

{% tabs %}
{% tab Android %}

Blenden Sie die Leiste für die Anzeige ungelesener Dokumente aus, indem Sie [`setUnreadBarVisible`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.view/-content-card-view-holder/set-unread-bar-visible.html?query=fun%20setUnreadBarVisible(isVisible:%20Boolean)) auf `ContentCardViewHolder` auf `false` setzen. 

{% endtab %}

{% tab Jetpack Compose %}
Die Deaktivierung der Anzeige für ungelesene Nachrichten wird in Jetpack Compose nicht unterstützt.
{% endtab %}

{% tab iOS %}
{% subtabs %}
{% subtab Swift %}

Blenden Sie den Balken für die Ungelesen-Anzeige aus, indem Sie die Eigenschaft `attributes.cellAttributes.unviewedIndicatorColor` in der Struktur `Attributes` auf `.clear` setzen. 

{% endsubtab %}
{% subtab Objective-C %}

Es ist nicht möglich, in Objective-C über `Attributes` nur die Nicht-aufgerufen-Anzeige anzupassen.

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Web %}

Blenden Sie die Leiste für die Anzeige ungelesener Dokumente aus, indem Sie den folgenden Stil zu Ihrem `css` hinzufügen:

```css
.ab-unread-indicator { display: none; }
```

{% endtab %}
{% endtabs %}

