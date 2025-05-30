---
nav_title: Style
article_title: Personnaliser le style des cartes de contenu
page_order: 1
description: "Cet article traite des options de style pour vos cartes de contenu."
channel:
  - content cards
platform:
  - Android
  - FireOS
  - Swift
  - Web
---

# Personnaliser le style des cartes de contenu

> Les cartes de contenu de Braze ont une présentation par défaut. Cet article couvre les options de style pour vos cartes de contenu afin de vous aider à correspondre à l'identité de votre marque. Pour obtenir la liste complète des types de cartes de contenu, voir [À propos des cartes de contenu.]({{site.baseurl}}/developer_guide/content_cards/)

## Création d'un style personnalisé

L'interface utilisateur par défaut des cartes de contenu est importée de la couche d'interface utilisateur du SDK de Braze. À partir de là, vous pouvez modifier certaines parties du style de la carte, l'ordre dans lequel les cartes sont affichées et la façon dont le flux est présenté à vos utilisateurs.

![Deux cartes de contenu, l'une avec la police par défaut et des coins carrés, l'autre avec des coins arrondis et une police bouclée]({% image_buster/assets/img/content_cards/content-card-customization-attributes.png %})

{% alert note %}
Les propriétés des cartes de contenu telles que `title`, `cardDescription`, `imageUrl`, etc., sont directement modifiables dans le [tableau de bord]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details), ce qui constitue la méthode préférée pour modifier ces informations.
{% endalert %}


{% tabs %}
{% tab Android %}

Par défaut, les cartes de contenu SDK Android et FireOS correspondent aux directives d'interface utilisateur standard d'Android afin d'offrir une expérience fluide. Vous pouvez voir ces styles par défaut dans le fichier [`res/values/styles.xml`](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/res/values/styles.xml) dans la distribution du SDK de Braze :

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

Pour personnaliser le style des cartes de contenu, remplacez ce style par défaut. Pour remplacer un style, copiez-le dans son intégralité dans le fichier `styles.xml` dans votre projet et apportez des modifications. L'ensemble du style doit être copié dans votre fichier local `styles.xml` pour que tous les attributs soient correctement définis.

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

Par défaut, les cartes de contenu SDK Android et FireOS correspondent aux directives d'interface utilisateur standard d'Android afin d'offrir une expérience fluide.

Vous pouvez appliquer la stylisation de deux manières. La première consiste à passer un `ContentCardListStyling` et un `ContentCardStyling` à un `ContentCardsList()`, comme dans l'exemple suivant :

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

La seconde consiste à utiliser BrazeStyle pour créer un style global pour les composants de Braze, comme dans l'exemple suivant :

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

Le contrôleur de vue des cartes de contenu vous permet de personnaliser l'apparence et le comportement de toutes les cellules via la structure [`BrazeContentCardUI.ViewController.Attributes`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct). La configuration des cartes de contenu à l'aide des `Attributes` est une option facile, qui vous permet de lancer votre interface utilisateur de cartes de contenu avec une configuration minimale. 

{% alert important %}
La personnalisation via `Attributes` n'est possible qu'en Swift.
{% endalert %}

{% subtabs %}
{% subtab Swift %}

**Modifier `Attributes.default`**

Personnalisez l'aspect et la convivialité de toutes les instances du contrôleur de vue de l'interface utilisateur des cartes de contenu de Braze en modifiant directement la variable statique [`Attributes.defaults`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/defaults).

Par exemple, pour modifier la taille de l'image et le rayon d'angle par défaut pour toutes les cellules :

```swift
BrazeContentCardUI.ViewController.Attributes.defaults.cellAttributes.cornerRadius = 20
BrazeContentCardUI.ViewController.Attributes.defaults.cellAttributes.classicImageSize = CGSize(width: 65, height: 65)
```

**Initialisation du contrôleur de vue avec des attributs**

Si vous souhaitez modifier uniquement une instance spécifique du contrôleur de vue de l'interface utilisateur de la carte contenu de Braze, utilisez l'initialisateur [`init(braze:attributes:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/init(braze:attributes:)/) pour transmettre une structure `Attributes` personnalisée au contrôleur de vue.

Par exemple, vous pouvez modifier la taille de l'image et le rayon des coins pour une instance spécifique du contrôleur de vue :

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.cellAttributes.cornerRadius = 20
attributes.cellAttributes.classicImageSize = CGSize(width: 65, height: 65)

let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)
```

**Personnalisation des cellules par sous-classement**

Vous pouvez également créer des interfaces personnalisées en enregistrant des classes personnalisées pour chaque type de carte souhaité. Pour utiliser votre sous-classe au lieu de la cellule par défaut, modifiez la propriété [`cells`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/cells) dans la structure `Attributes`. Par exemple :

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
// Register your own custom cell
attributes.cells[BrazeContentCardUI.ClassicImageCell.identifier] = CustomClassicImageCell.self

let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)
```

**Modifier les cartes de contenu par programmation**

Les cartes de contenu peuvent être modifiées par programme en assignant la fermeture [`transform`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/transform) à votre structure `Attributes`. L'exemple ci-dessous modifie les adresses `title` et `description` des cartes compatibles :

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

Consultez l'[exemple d'application Exemples](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/Swift) pour un exemple complet.

{% endsubtab %}
{% subtab Objective-C %}

La personnalisation des cartes de contenu via `Attributes` n'est pas prise en charge avec Objective-C.

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Web %}

Les styles par défaut de Braze sont définis en CSS dans le SDK de Braze. En écrasant des styles sélectionnés dans votre application, il est possible de personnaliser notre fil standard avec vos propres images de fond, des familles de polices, des styles, des tailles, des animations, et bien plus encore. Par exemple, voici un exemple d'override qui fera apparaître les cartes de contenu en 800 px de large :

``` css
body .ab-feed {
  width: 800px;
}
```

{% endtab %}
{% endtabs %}

## Exemples de personnalisation

### Police personnalisée

Personnaliser la police utilisée dans vos cartes de contenu vous permet de préserver l'identité de votre marque et de créer une expérience visuellement attrayante pour vos utilisateurs. Utilisez ces recettes pour définir par programme la police de toutes les cartes de contenu. 

{% tabs %}
{% tab Android %}

Pour modifier la police par défaut de manière programmatique, définissez un style pour les cartes et utilisez l'attribut `fontFamily` pour demander à Braze d'utiliser votre famille de polices personnalisée.

Par exemple, pour mettre à jour la police sur tous les titres des cartes image sous-titrées, remplacez le style `Braze.ContentCards.CaptionedImage.Title` et référencez votre famille de polices personnalisée. La valeur d’attribut doit pointer vers une famille de polices dans votre répertoire `res/font`.

Voici un exemple tronqué avec une famille de polices personnalisées `my_custom_font_family`, référencé sur la dernière ligne :

```xml
  <style name="Braze.ContentCards.CaptionedImage.Title">
    <item name="android:layout_width">wrap_content</item>
    ...
    <item name="android:fontFamily">@font/my_custom_font_family</item>
    <item name="fontFamily">@font/my_custom_font_family</item>
  </style>
```

Pour plus d'informations sur la personnalisation des polices dans le SDK Android, consultez le [guide des familles de polices]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/font_customization/#font-customization).
{% endtab %}
{% tab Jetpack Compose %}
Pour modifier la police par défaut par programmation, vous pouvez définir le `titleTextStyle` de `ContentCardStyling`.

Vous pouvez également définir `titleTextStyle` pour un type de carte spécifique en le définissant sur `BrazeShortNewsContentCardStyling` et en le transmettant au `shortNewsContentCardStyle` de `ContentCardStyling`.

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

Personnalisez vos polices en personnalisant les `Attributes` de la propriété d'instance [`cellAttributes`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/cellattributes/). Par exemple :

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.cellAttributes.titleFont = .preferredFont(textStyle: .callout, weight: .bold)
attributes.cellAttributes.descriptionFont = .preferredFont(textStyle: .footnote, weight: .regular)
attributes.cellAttributes.domainFont = .preferredFont(textStyle: .footnote, weight: .medium)

let viewController = BrazeContentCardUI.ViewController.init(braze: braze, attributes: attributes)
```

{% endsubtab %}
{% subtab Objective-C %}

La personnalisation des polices via `Attributes` n'est pas prise en charge en Objective-C. 

Consultez l'[exemple d'application Examples](https://github.com/braze-inc/braze-swift-sdk/blob/main/Examples/ObjC/Sources/ContentCards-Custom-UI/CardsInfoViewController.m#L97) pour savoir comment créer votre propre interface utilisateur avec des polices personnalisées.

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Web %}

Comme tout autre élément Web, vous pouvez facilement personnaliser l'apparence des cartes de contenu à l'aide de CSS. Dans votre fichier CSS ou dans les styles d'insertion CSS, utilisez la propriété `font-family` et spécifiez le nom de la police ou la pile de polices souhaitée.

```css
/* CSS selector targeting the Content Card element */
.card-element {
  font-family: "Helvetica Neue", Arial, sans-serif;
}
```

{% endtab %}
{% endtabs %}

### Icônes épinglées personnalisées

Lors de la création d'une carte de contenu, les marketeurs ont la possibilité d'épingler la carte. Une carte épinglée s’affiche en haut d’un flux d’un utilisateur et ne peut pas être rejetée par l’utilisateur. Lorsque vous personnalisez vos styles de cartes, vous avez la possibilité de modifier l'aspect de l'icône épinglée.

![Aperçu côte à côte de la carte de contenu dans Braze pour mobile et Web avec l'option "Épingler cette carte en haut du flux" sélectionnée.]({% image_buster /assets/img/cc_pin_to_top.png %}){:style="border:none"}

{% tabs %}
{% tab Android %}

Pour définir une icône épinglée personnalisée, remplacez le style `Braze.ContentCards.PinnedIcon`. Votre actif d’image personnalisé doit être déclaré dans l’élément `android:src`. Par exemple :

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

Pour modifier l'icône épinglée par défaut, vous pouvez définir le `pinnedResourceId` de `ContentCardStyling`.  Par exemple :

```kotlin
ContentCardStyling(
    pinnedResourceId = R.drawable.pushpin,
    pinnedImageAlignment = Alignment.TopCenter
)
```

Vous pouvez également spécifier un Composable dans `pinnedComposable` de `ContentCardStyling`. Si `pinnedComposable` est spécifié, il remplace la valeur de `pinnedResourceId`.

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

Personnalisez l'icône de l'épingle en modifiant les propriétés `pinIndicatorColor` et `pinIndicatorImage` de la propriété d'instance [`cellAttributes`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/cellattributes/) instance. Par exemple :

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.cellAttributes.pinIndicatorColor = .red
attributes.cellAttributes.pinIndicatorImage = UIImage(named: "my-image")

let viewController = BrazeContentCardUI.ViewController.init(braze: braze, attributes: attributes)
```

Vous pouvez également utiliser la sous-classe pour créer votre propre version personnalisée de `BrazeContentCardUI.Cell`, qui inclut l'indicateur d'épingle. Par exemple : 

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.cells[BrazeContentCardUI.ClassicImageCell.identifier] = CustomClassicImageCell.self

let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)
```

{% endsubtab %}
{% subtab Objective-C %}

La personnalisation de l'indicateur de broche via `Attributes` n'est pas prise en charge en Objective-C.

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Web %}

La structure de l'icône épinglée de la carte de contenu est la suivante :

```css
<div class="ab-pinned-indicator">
  <i class="fa fa-star"></i>
</div>
```

Si vous souhaitez utiliser une autre icône FontAwesome, il vous suffit de remplacer le nom de classe de l'élément `i` par le nom de classe de l'icône souhaitée. 

Si vous souhaitez remplacer complètement l'icône, supprimez l'élément `i` et ajoutez l'icône personnalisée en tant qu'enfant de `ab-pinned-indicator`. Il y a plusieurs façons de procéder, mais une méthode simple consiste à `replaceChildren()` sur l'élément `ab-pinned-indicator`.

Par exemple :

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

### Modification de la couleur de l'indicateur messages non lus

Les cartes de contenu contiennent une ligne bleue au bas de la carte qui indique si la carte a été consultée ou non. 

![Deux cartes de contenu affichées côte à côte. La première carte a une ligne bleue en bas, indiquant qu’elle n’a pas été vue. La deuxième carte ne comporte pas de ligne bleue, ce qui indique qu'elle a déjà été vue.]({% image_buster /assets/img/braze-content-cards-seen-unseen-behavior.png %})

{% tabs %}
{% tab Android %}

Modifiez la couleur de la barre de l'indicateur messages non lus en modifiant la valeur de `com_braze_content_cards_unread_bar_color` dans votre fichier `colors.xml`:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <!-- The color used to highlight unread Content Cards at their bottom edge -->
  <color name="com_braze_content_cards_unread_bar_color">#1676d0</color>
</resources>
```

{% endtab %}
{% tab Jetpack Compose %}

Pour changer la couleur de la barre de l'indicateur messages non lus, modifiez la valeur de `unreadIndicatorColor` dans `ContentCardStyling`:

```kotlin
ContentCardStyling(
    unreadIndicatorColor = Color.Red
)
```

{% endtab %}
{% tab iOS %}

{% subtabs %}
{% subtab Swift %}

Modifiez la couleur de la barre de l'indicateur messages non lus en attribuant une valeur à la couleur de teinte de votre instance `BrazeContentCardUI.ViewController`:

```swift
let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze)
viewController.view.tintColor = .systemGreen
```

Cependant, si vous souhaitez modifier uniquement l'indicateur non visualisé, vous pouvez accéder à la propriété `unviewedIndicatorColor` de votre structure `BrazeContentCardUI.ViewController.Attributes`. Si vous utilisez les implémentations `UITableViewCell` de Braze, vous devez accéder à la propriété avant que la cellule ne soit dessinée.

Par exemple, pour définir la couleur de l’indicateur non visionné en rouge :

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.cellAttributes.unviewedIndicatorColor = .red

let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)
```

Consultez l'[exemple d'application Exemples](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/Swift) pour un exemple complet.

{% endsubtab %}
{% subtab Objective-C %}

Modifiez la couleur de la barre de l'indicateur messages non lus en attribuant une valeur à la couleur de teinte de votre `BRZContentCardUIViewController`:

```objc
BRZContentCardUIViewController *viewController = [[BRZContentCardUIViewController alloc] initWithBraze:AppDelegate.braze];
[viewController.view setTintColor:[UIColor systemGreenColor]];
```

La personnalisation de l'indicateur non affiché uniquement via `Attributes` n'est pas prise en charge en Objective-C.

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Web %}

Pour modifier la couleur de l’indicateur de messages non lus d’une carte, ajoutez un CSS personnalisé à votre page Web. Par exemple, pour définir la couleur de l'indicateur non visualisé en vert :

```css
.ab-unread-indicator { background-color: green; }
```

{% endtab %}
{% endtabs %}

### Désactivation de l'indicateur messages non lus

{% tabs %}
{% tab Android %}

Masquez la barre de l'indicateur messages non lus en paramétrant [`setUnreadBarVisible`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.view/-content-card-view-holder/set-unread-bar-visible.html?query=fun%20setUnreadBarVisible(isVisible:%20Boolean)) sur `ContentCardViewHolder` à `false`. 

{% endtab %}

{% tab Jetpack Compose %}
La désactivation de l'indicateur de messages non lus n'est pas prise en charge dans Jetpack Compose.
{% endtab %}

{% tab iOS %}
{% subtabs %}
{% subtab Swift %}

Masquez la barre d'indicateurs non lus en définissant la propriété `attributes.cellAttributes.unviewedIndicatorColor` de votre structure `Attributes` sur `.clear`. 

{% endsubtab %}
{% subtab Objective-C %}

La personnalisation de l'indicateur non affiché uniquement via `Attributes` n'est pas prise en charge en Objective-C.

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Web %}

Masquez la barre d'indicateurs non lus en ajoutant le style suivant à votre site `css`:

```css
.ab-unread-indicator { display: none; }
```

{% endtab %}
{% endtabs %}
