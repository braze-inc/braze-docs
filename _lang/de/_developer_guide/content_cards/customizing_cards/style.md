---
nav_title: Stil
article_title: Passen Sie den Stil der Content-Cards an
page_order: 1
description: "Dieser Artikel behandelt die Gestaltungsmöglichkeiten für Ihre Content-Cards."
channel:
  - content cards
platform:
  - Android
  - FireOS
  - Swift
  - Web
---

# Passen Sie den Stil der Content-Cards an

> Braze Content-Cards werden mit einem Standard-Look-and-Feel geliefert. Dieser Artikel befasst sich mit den Styling-Optionen für Ihre Content-Cards, damit Sie sie an Ihre Markenidentität anpassen können. Eine vollständige Liste der Content-Card-Typen finden Sie unter [Über Content-Cards]({{site.baseurl}}/developer_guide/content_cards/).

## Einen angepassten Stil erstellen

Die Standard-UI für Content-Cards wird aus der UI-Schicht des Braze SDK importiert. Von dort aus können Sie bestimmte Teile des Kartendesigns, die Reihenfolge der Karten und die Art und Weise, wie der Feed Ihren Nutzer:innen angezeigt wird, anpassen.

![Zwei Content-Cards, eine mit der Standard-Schriftart und eckigen Ecken und eine mit abgerundeten Ecken und einer geschwungenen Schriftart]({% image_buster/assets/img/content_cards/content-card-customization-attributes.png %})

{% alert note %}
Eigenschaften von Content-Cards wie `title`, `cardDescription`, `imageUrl` usw. können direkt über das [Dashboard]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details) bearbeitet werden – das ist die bevorzugte Methode, um diese Details zu ändern.
{% endalert %}


{% tabs %}
{% tab web %}

Die Standardstile von Braze sind in CSS innerhalb des Braze SDK definiert. Durch das Überschreiben ausgewählter Stile in Ihrer Anwendung können Sie unseren Standard-Feed mit Ihren eigenen Hintergrundbildern, Schriftarten, Stilen, Größen, Animationen und vielem mehr anpassen. Das folgende Beispiel zeigt eine Überschreibung, die bewirkt, dass Content-Cards mit einer Breite von 800 px angezeigt werden:

``` css
body .ab-feed {
  width: 800px;
}
```

Eine vollständige Liste der Eigenschaften, die Sie ändern können, finden Sie unter [Braze SDK-Konfigurationsoptionen](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html).

{% endtab %}
{% tab android %}

Standardmäßig entsprechen die Content-Cards des Android- und FireOS-SDK den Standard-Android-UI-Richtlinien, um ein nahtloses Erlebnis zu bieten. Sie können diese Standardstile in der Datei [`res/values/styles.xml`](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/res/values/styles.xml) in der Braze-SDK-Distribution einsehen:

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

Um den Stil Ihrer Content-Cards anzupassen, überschreiben Sie diesen Standardstil. Um einen Stil zu überschreiben, kopieren Sie ihn vollständig in die Datei `styles.xml` Ihres Projekts und nehmen Sie die gewünschten Änderungen vor. Der gesamte Stil muss in Ihre lokale Datei `styles.xml` kopiert werden, damit alle Attribute korrekt gesetzt werden.

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

Standardmäßig entsprechen die Content-Cards des Android- und FireOS-SDK den Standard-Android-UI-Richtlinien, um ein nahtloses Erlebnis zu bieten.

Es gibt zwei Möglichkeiten, einen Stil anzuwenden. Die erste besteht darin, ein [`ContentCardListStyling`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-list-styling/index.html) und [`ContentCardStyling`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-styling/index.html) an [`ContentCardsList`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards/-content-cards-list.html) zu übergeben, wie im folgenden Beispiel:

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

Die zweite Möglichkeit ist die Verwendung von [`BrazeStyle`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose/-braze-style.html), um ein globales Styling für Braze-Komponenten zu erstellen, wie im folgenden Beispiel:

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
{% tab swift %}

Mit dem View Controller für Content-Cards können Sie das Aussehen und Verhalten aller Zellen über die Struktur [`BrazeContentCardUI.ViewController.Attributes`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct) anpassen. Die Konfiguration von Content-Cards mit `Attributes` ist eine unkomplizierte Option, mit der Sie Ihre Content-Cards-UI mit minimalem Aufwand starten können. 

{% alert important %}
Die Anpassung über `Attributes` ist nur in Swift möglich.
{% endalert %}

{% subtabs %}
{% subtab Swift %}

**`Attributes.default` ändern**

Passen Sie das Aussehen aller Instanzen des Braze Content-Card-UI-View-Controllers an, indem Sie die statische Variable [`Attributes.defaults`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/defaults) direkt ändern.

So ändern Sie beispielsweise die Standardbildgröße und den Eckenradius für alle Zellen:

```swift
BrazeContentCardUI.ViewController.Attributes.defaults.cellAttributes.cornerRadius = 20
BrazeContentCardUI.ViewController.Attributes.defaults.cellAttributes.classicImageSize = CGSize(width: 65, height: 65)
```

**Den View Controller mit Attributes initialisieren**

Wenn Sie nur eine bestimmte Instanz des Braze Content-Card-UI-View-Controllers ändern möchten, verwenden Sie den Initialisierer [`init(braze:attributes:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/init(braze:attributes:)/), um eine angepasste `Attributes`-Struktur an den View Controller zu übergeben.

So können Sie zum Beispiel die Bildgröße und den Eckenradius für eine bestimmte Instanz des View Controllers ändern:

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.cellAttributes.cornerRadius = 20
attributes.cellAttributes.classicImageSize = CGSize(width: 65, height: 65)

let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)
```

**Zellen mithilfe von Unterklassen anpassen**

Alternativ können Sie angepasste Schnittstellen erstellen, indem Sie angepasste Klassen für jeden gewünschten Kartentyp registrieren. Um anstelle der Standardzelle eine Unterklasse zu verwenden, ändern Sie die Eigenschaft [`cells`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/cells) in der `Attributes`-Struktur. Zum Beispiel:

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
// Register your own custom cell
attributes.cells[BrazeContentCardUI.ClassicImageCell.identifier] = CustomClassicImageCell.self

let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)
```

**Content-Cards programmatisch ändern**

Sie können Content-Cards programmatisch ändern, indem Sie die [`transform`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/transform)-Closure Ihrer `Attributes`-Struktur zuweisen. Das folgende Beispiel ändert `title` und `description` kompatibler Karten:

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

Ein vollständiges Beispiel finden Sie in der [Beispiel-App „Examples"](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/Swift).

{% endsubtab %}
{% subtab Objective-C %}

Die Anpassung von Content-Cards über `Attributes` wird in Objective-C nicht unterstützt.

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Beispiele für Anpassungen

### Eigene Schriftart

Durch die Anpassung der in Ihren Content-Cards verwendeten Schriftart können Sie Ihre Markenidentität wahren und ein visuell ansprechendes Erlebnis für Ihre Nutzer:innen schaffen. Verwenden Sie die folgenden Vorgehensweisen, um die Schriftart für alle Content-Cards programmatisch festzulegen. 

{% tabs %}
{% tab web %}

Sie können das Aussehen von Content-Cards wie jedes andere Web-Element ganz einfach über CSS anpassen. Verwenden Sie in Ihrer CSS-Datei oder in Inline-Styles die Eigenschaft `font-family` und geben Sie den gewünschten Schriftnamen oder Font-Stack an.

```css
/* CSS selector targeting the Content Card element */
.card-element {
  font-family: "Helvetica Neue", Arial, sans-serif;
}
```

{% endtab %}
{% tab android %}

Um die Standardschriftart programmatisch zu ändern, legen Sie einen Stil für Karten fest und verwenden Sie das Attribut `fontFamily`, um Braze anzuweisen, Ihre eigene Schriftfamilie zu verwenden.

Wenn Sie beispielsweise die Schriftart für alle Titel von Bildkarten mit Bildunterschriften aktualisieren möchten, überschreiben Sie den Stil `Braze.ContentCards.CaptionedImage.Title` und verweisen Sie auf Ihre eigene Schriftfamilie. Der Attributwert sollte auf eine Schriftfamilie in Ihrem Verzeichnis `res/font` verweisen.

Hier ist ein gekürztes Beispiel mit einer angepassten Schriftfamilie `my_custom_font_family`, auf die in der letzten Zeile verwiesen wird:

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
Um die Standardschriftart programmatisch zu ändern, können Sie [`titleTextStyle`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-styling/index.html#715371549%2FProperties%2F-1725759721) von `ContentCardStyling` setzen.

Sie können `titleTextStyle` auch für einen bestimmten Kartentyp festlegen, indem Sie es auf [`BrazeShortNewsContentCardStyling`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-braze-short-news-content-card-styling/index.html) setzen und an [`shortNewsContentCardStyle`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-styling/index.html#8580250%2FProperties%2F-1725759721) von `ContentCardStyling` übergeben.

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
{% tab swift %}
{% subtabs %}
{% subtab Swift %}

Passen Sie Ihre Schriftarten an, indem Sie die `Attributes` der Instanz-Eigenschaft [`cellAttributes`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/cellattributes/) ändern. Zum Beispiel:

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

Ein Beispiel für die Erstellung Ihrer eigenen UI mit angepassten Schriftarten finden Sie in der [Beispiel-App „Examples"](https://github.com/braze-inc/braze-swift-sdk/blob/main/Examples/ObjC/Sources/ContentCards-Custom-UI/CardsInfoViewController.m#L97).

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Angepasste Pin-Symbole

Bei der Erstellung einer Content-Card haben Marketer die Möglichkeit, die Karte zu pinnen. Eine gepinnte Karte wird oben im Feed der Nutzer:innen angezeigt und kann nicht geschlossen werden. Wenn Sie Ihre Kartenstile anpassen, können Sie auch das Aussehen des Pin-Symbols ändern.

![Side-by-Side-Vorschau der Content-Cards in Braze für Mobilgeräte und Internet mit aktivierter Option „Diese Karte oben im Feed pinnen".]({% image_buster /assets/img/cc_pin_to_top.png %}){:style="border:none"}

{% tabs %}
{% tab web %}

Die Struktur des Pin-Symbols für Content-Cards lautet wie folgt:

```css
<div class="ab-pinned-indicator">
  <i class="fa fa-star"></i>
</div>
```

Wenn Sie ein anderes FontAwesome-Symbol verwenden möchten, ersetzen Sie den Klassennamen des `i`-Elements durch den Klassennamen des gewünschten Symbols. 

Wenn Sie das Symbol vollständig austauschen möchten, entfernen Sie das `i`-Element und fügen Sie das angepasste Symbol als untergeordnetes Element von `ab-pinned-indicator` hinzu. Es gibt mehrere Möglichkeiten, das Symbol zu ändern. Eine einfache Methode besteht darin, `replaceChildren()` auf dem `ab-pinned-indicator`-Element zu verwenden.

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
{% tab android %}

Um ein angepasstes Pin-Symbol festzulegen, überschreiben Sie den Stil `Braze.ContentCards.PinnedIcon`. Ihr angepasstes Bild-Asset sollte im Element `android:src` deklariert werden. Zum Beispiel:

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

Um das Standard-Pin-Symbol zu ändern, können Sie [`pinnedResourceId`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-styling/index.html#794044424%2FProperties%2F-1725759721) von `ContentCardStyling` setzen. Zum Beispiel:

```kotlin
ContentCardStyling(
    pinnedResourceId = R.drawable.pushpin,
    pinnedImageAlignment = Alignment.TopCenter
)
```

Sie können auch ein Composable in [`pinnedComposable`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-styling/index.html#1460938052%2FProperties%2F-1725759721) von `ContentCardStyling` angeben. Wenn `pinnedComposable` angegeben ist, überschreibt es den Wert von `pinnedResourceId`.

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
{% tab swift %}
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

Das Anpassen des Pin-Indikators über `Attributes` wird in Objective-C nicht unterstützt.

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Farbe der Ungelesen-Anzeige ändern

Content-Cards enthalten eine blaue Linie am unteren Rand der Karte, die anzeigt, ob die Karte bereits angesehen wurde oder nicht. 

![Zwei Content-Cards werden nebeneinander angezeigt. Die erste Karte hat eine blaue Linie am unteren Rand, was bedeutet, dass sie noch nicht gesehen wurde. Die zweite Karte hat keine blaue Linie, was darauf hinweist, dass sie bereits angesehen wurde.]({% image_buster /assets/img/braze-content-cards-seen-unseen-behavior.png %})

{% tabs %}
{% tab web %}

Um die Farbe der Ungelesen-Anzeige einer Karte zu ändern, fügen Sie Ihrer Webseite angepasstes CSS hinzu. So setzen Sie beispielsweise die Farbe der Ungelesen-Anzeige auf Grün:

```css
.ab-unread-indicator { background-color: green; }
```

{% endtab %}
{% tab android %}

Ändern Sie die Farbe des Ungelesen-Balkens, indem Sie den Wert von `com_braze_content_cards_unread_bar_color` in Ihrer `colors.xml`-Datei anpassen:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <!-- The color used to highlight unread Content Cards at their bottom edge -->
  <color name="com_braze_content_cards_unread_bar_color">#1676d0</color>
</resources>
```

{% endtab %}
{% tab Jetpack Compose %}

Um die Farbe des Ungelesen-Balkens zu ändern, passen Sie den Wert von [`unreadIndicatorColor`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-styling/index.html#-1669590042%2FProperties%2F-1725759721) in `ContentCardStyling` an:

```kotlin
ContentCardStyling(
    unreadIndicatorColor = Color.Red
)
```

{% endtab %}
{% tab swift %}

{% subtabs %}
{% subtab Swift %}

Ändern Sie die Farbe des Ungelesen-Balkens, indem Sie der Tint-Farbe Ihrer `BrazeContentCardUI.ViewController`-Instanz einen Wert zuweisen:

```swift
let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze)
viewController.view.tintColor = .systemGreen
```

Wenn Sie jedoch nur den Indikator für nicht angesehene Karten ändern möchten, können Sie auf die Eigenschaft `unviewedIndicatorColor` Ihrer `BrazeContentCardUI.ViewController.Attributes`-Struktur zugreifen. Wenn Sie Braze-`UITableViewCell`-Implementierungen verwenden, greifen Sie auf die Eigenschaft zu, bevor die Zelle gezeichnet wird.

So setzen Sie beispielsweise die Farbe der Nicht-angesehen-Anzeige auf Rot:

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.cellAttributes.unviewedIndicatorColor = .red

let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)
```

Ein vollständiges Beispiel finden Sie in der [Beispiel-App „Examples"](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/Swift).

{% endsubtab %}
{% subtab Objective-C %}

Ändern Sie die Farbe des Ungelesen-Balkens, indem Sie der Tint-Farbe Ihres `BRZContentCardUIViewController` einen Wert zuweisen:

```objc
BRZContentCardUIViewController *viewController = [[BRZContentCardUIViewController alloc] initWithBraze:AppDelegate.braze];
[viewController.view setTintColor:[UIColor systemGreenColor]];
```

Die Anpassung ausschließlich der Nicht-angesehen-Anzeige über `Attributes` wird in Objective-C nicht unterstützt.

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Dark Mode

Um je nach Dark Mode oder Light Mode des Geräts unterschiedliche Bilder oder Stile anzuzeigen, verwenden Sie [Schlüssel-Wert-Paare]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details#key-value-pairs) in Ihrer Content-Card-Nachricht. Fügen Sie beispielsweise ein Schlüssel-Wert-Paar wie `dark_mode_image` mit der URL Ihres Dark-Mode-Bild-Assets hinzu. Fügen Sie dann in Ihrer App eine angepasste Logik hinzu, um den aktuellen Darstellungsmodus des Geräts zu prüfen und das entsprechende Bild anzuzeigen.

{% tabs %}
{% tab swift %}

```swift
if let darkImageUrl = card.extras["dark_mode_image"],
   view.traitCollection.userInterfaceStyle == .dark {
  // Use darkImageUrl for the image
}
```

{% endtab %}
{% tab android %}

```kotlin
val darkModeImage = card.extras["dark_mode_image"]
val isDarkMode = (resources.configuration.uiMode and Configuration.UI_MODE_NIGHT_MASK) == Configuration.UI_MODE_NIGHT_YES
if (isDarkMode && darkModeImage != null) {
    // Use darkModeImage for the image
}
```

{% endtab %}
{% tab web %}

```javascript
const darkModeImage = card.extras?.dark_mode_image;
const isDarkMode = window.matchMedia("(prefers-color-scheme: dark)").matches;
if (isDarkMode && darkModeImage) {
  // Use darkModeImage for the image
}
```

{% endtab %}
{% endtabs %}

Dieses Muster funktioniert für alle darstellungsabhängigen Inhalte, einschließlich Text, Farben oder Layouts. Laden Sie Ihre Dark-Mode-Bild-Assets in die [Mediathek]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library) hoch und referenzieren Sie sie dann in einem Schlüssel-Wert-Paar.

### Ungelesen-Anzeige deaktivieren

{% tabs %}
{% tab web %}

Blenden Sie den Ungelesen-Balken aus, indem Sie den folgenden Stil zu Ihrem `css` hinzufügen:

```css
.ab-unread-indicator { display: none; }
```

{% endtab %}

{% tab android %}

Blenden Sie den Ungelesen-Balken aus, indem Sie [`setUnreadBarVisible`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.view/-content-card-view-holder/set-unread-bar-visible.html?query=fun%20setUnreadBarVisible(isVisible:%20Boolean)) auf `ContentCardViewHolder` auf `false` setzen. 

{% endtab %}

{% tab Jetpack Compose %}
Die Deaktivierung der Ungelesen-Anzeige wird in Jetpack Compose nicht unterstützt.
{% endtab %}
{% tab swift %}
{% subtabs %}
{% subtab Swift %}

Blenden Sie den Ungelesen-Balken aus, indem Sie die Eigenschaft `attributes.cellAttributes.unviewedIndicatorColor` in Ihrer `Attributes`-Struktur auf `.clear` setzen. 

{% endsubtab %}
{% subtab Objective-C %}

Die Anpassung ausschließlich der Nicht-angesehen-Anzeige über `Attributes` wird in Objective-C nicht unterstützt.

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}