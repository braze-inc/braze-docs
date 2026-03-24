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

> Les cartes de contenu de Braze sont livrées avec une apparence par défaut. Cet article présente les options de style disponibles pour vos cartes de contenu, afin de les adapter à l'identité de votre marque. Pour consulter la liste complète des types de cartes de contenu, voir [À propos des cartes de contenu]({{site.baseurl}}/developer_guide/content_cards/).

## Créer un style personnalisé

L'interface utilisateur par défaut des cartes de contenu est importée depuis la couche UI du SDK Braze. Vous pouvez ensuite ajuster certains aspects du style des cartes, l'ordre d'affichage et la manière dont le flux est présenté à vos utilisateurs.

![Deux cartes de contenu, l'une avec la police par défaut et des coins carrés, l'autre avec des coins arrondis et une police bouclée]({% image_buster/assets/img/content_cards/content-card-customization-attributes.png %})

{% alert note %}
Les propriétés des cartes de contenu telles que `title`, `cardDescription`, `imageUrl`, etc., sont directement modifiables depuis le [tableau de bord]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details). C'est la méthode recommandée pour modifier ces informations.
{% endalert %}


{% tabs %}
{% tab web %}

Les styles par défaut de Braze sont définis en CSS au sein du SDK Braze. En surchargeant certains styles dans votre application, vous pouvez personnaliser le flux standard avec vos propres images d'arrière-plan, familles de polices, styles, tailles, animations, etc. Par exemple, voici une surcharge qui affiche les cartes de contenu avec une largeur de 800 px :

``` css
body .ab-feed {
  width: 800px;
}
```

Pour consulter la liste complète des propriétés modifiables, voir [les options de configuration du SDK Braze](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html).

{% endtab %}
{% tab android %}

Par défaut, les cartes de contenu du SDK Android et FireOS respectent les directives d'interface utilisateur standard d'Android pour offrir une expérience fluide. Vous pouvez consulter ces styles par défaut dans le fichier [`res/values/styles.xml`](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/res/values/styles.xml) de la distribution du SDK Braze :

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

Pour personnaliser le style des cartes de contenu, surchargez ce style par défaut. Pour ce faire, copiez-le intégralement dans le fichier `styles.xml` de votre projet, puis apportez vos modifications. Le style doit être copié en entier dans votre fichier local `styles.xml` pour que tous les attributs soient correctement définis.

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

Par défaut, les cartes de contenu du SDK Android et FireOS respectent les directives d'interface utilisateur standard d'Android pour offrir une expérience fluide.

Vous pouvez appliquer un style de deux manières. La première consiste à passer un [`ContentCardListStyling`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-list-styling/index.html) et un [`ContentCardStyling`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-styling/index.html) à [`ContentCardsList`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards/-content-cards-list.html), comme dans l'exemple suivant :

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

La seconde consiste à utiliser [`BrazeStyle`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose/-braze-style.html) pour créer un style global applicable aux composants Braze, comme dans l'exemple suivant :

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

Le contrôleur de vue des cartes de contenu vous permet de personnaliser l'apparence et le comportement de toutes les cellules via la structure [`BrazeContentCardUI.ViewController.Attributes`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct). Configurer les cartes de contenu à l'aide des `Attributes` est une option simple qui vous permet de lancer l'interface des cartes de contenu avec une configuration minimale. 

{% alert important %}
La personnalisation via `Attributes` n'est disponible qu'en Swift.
{% endalert %}

{% subtabs %}
{% subtab Swift %}

**Modifier `Attributes.default`**

Personnalisez l'apparence de toutes les instances du contrôleur de vue des cartes de contenu Braze en modifiant directement la variable statique [`Attributes.defaults`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/defaults).

Par exemple, pour modifier la taille d'image et le rayon des coins par défaut pour toutes les cellules :

```swift
BrazeContentCardUI.ViewController.Attributes.defaults.cellAttributes.cornerRadius = 20
BrazeContentCardUI.ViewController.Attributes.defaults.cellAttributes.classicImageSize = CGSize(width: 65, height: 65)
```

**Initialiser le contrôleur de vue avec des attributs**

Si vous souhaitez modifier uniquement une instance spécifique du contrôleur de vue des cartes de contenu Braze, utilisez l'initialisateur [`init(braze:attributes:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/init(braze:attributes:)/) pour transmettre une structure `Attributes` personnalisée au contrôleur de vue.

Par exemple, vous pouvez modifier la taille d'image et le rayon des coins pour une instance spécifique du contrôleur de vue :

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.cellAttributes.cornerRadius = 20
attributes.cellAttributes.classicImageSize = CGSize(width: 65, height: 65)

let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)
```

**Personnaliser les cellules par sous-classement**

Vous pouvez également créer des interfaces personnalisées en enregistrant des classes personnalisées pour chaque type de carte souhaité. Pour utiliser votre sous-classe au lieu de la cellule par défaut, modifiez la propriété [`cells`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/cells) dans la structure `Attributes`. Par exemple :

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
// Register your own custom cell
attributes.cells[BrazeContentCardUI.ClassicImageCell.identifier] = CustomClassicImageCell.self

let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)
```

**Modifier les cartes de contenu par programmation**

Vous pouvez modifier les cartes de contenu par programmation en assignant la closure [`transform`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/transform) à votre structure `Attributes`. L'exemple ci-dessous modifie les champs `title` et `description` des cartes compatibles :

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

Consultez l'[application d'exemple Examples](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/Swift) pour un exemple complet.

{% endsubtab %}
{% subtab Objective-C %}

La personnalisation des cartes de contenu via `Attributes` n'est pas prise en charge avec Objective-C.

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Exemples de personnalisation

### Police personnalisée

Personnaliser la police de vos cartes de contenu vous permet de préserver l'identité de votre marque et de créer une expérience visuellement attrayante pour vos utilisateurs. Utilisez ces recettes pour définir la police de toutes les cartes de contenu par programmation. 

{% tabs %}
{% tab web %}

Comme tout autre élément web, vous pouvez facilement personnaliser l'apparence des cartes de contenu via CSS. Dans votre fichier CSS ou vos styles en ligne, utilisez la propriété `font-family` et spécifiez le nom de la police ou la pile de polices souhaitée.

```css
/* CSS selector targeting the Content Card element */
.card-element {
  font-family: "Helvetica Neue", Arial, sans-serif;
}
```

{% endtab %}
{% tab android %}

Pour modifier la police par défaut par programmation, définissez un style pour les cartes et utilisez l'attribut `fontFamily` pour indiquer à Braze d'utiliser votre famille de polices personnalisée.

Par exemple, pour mettre à jour la police de tous les titres des cartes image sous-titrées, surchargez le style `Braze.ContentCards.CaptionedImage.Title` et référencez votre famille de polices personnalisée. La valeur de l'attribut doit pointer vers une famille de polices dans votre répertoire `res/font`.

Voici un exemple tronqué avec une famille de polices personnalisée `my_custom_font_family`, référencée sur la dernière ligne :

```xml
  <style name="Braze.ContentCards.CaptionedImage.Title">
    <item name="android:layout_width">wrap_content</item>
    ...
    <item name="android:fontFamily">@font/my_custom_font_family</item>
    <item name="fontFamily">@font/my_custom_font_family</item>
  </style>
```

Pour en savoir plus sur la personnalisation des polices dans le SDK Android, consultez le [guide des familles de polices]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/font_customization/#font-customization).
{% endtab %}
{% tab Jetpack Compose %}
Pour modifier la police par défaut par programmation, vous pouvez définir le paramètre [`titleTextStyle`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-styling/index.html#715371549%2FProperties%2F-1725759721) de `ContentCardStyling`.

Vous pouvez également définir `titleTextStyle` pour un type de carte spécifique en le configurant sur [`BrazeShortNewsContentCardStyling`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-braze-short-news-content-card-styling/index.html) et en le passant au paramètre [`shortNewsContentCardStyle`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-styling/index.html#8580250%2FProperties%2F-1725759721) de `ContentCardStyling`.

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

Personnalisez vos polices en modifiant les `Attributes` de la propriété d'instance [`cellAttributes`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/cellattributes/). Par exemple :

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

Consultez l'[application d'exemple Examples](https://github.com/braze-inc/braze-swift-sdk/blob/main/Examples/ObjC/Sources/ContentCards-Custom-UI/CardsInfoViewController.m#L97) pour savoir comment créer votre propre interface utilisateur avec des polices personnalisées.

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Icônes d'épingle personnalisées

Lors de la création d'une carte de contenu, les marketeurs ont la possibilité de l'épingler. Une carte épinglée s'affiche en haut du flux de l'utilisateur et ne peut pas être masquée. Lorsque vous personnalisez le style de vos cartes, vous pouvez modifier l'apparence de l'icône d'épingle.

![Aperçu côte à côte de la carte de contenu dans Braze pour mobile et web avec l'option « Épingler cette carte en haut du fil » sélectionnée.]({% image_buster /assets/img/cc_pin_to_top.png %}){:style="border:none"}

{% tabs %}
{% tab web %}

La structure de l'icône d'épingle de la carte de contenu est la suivante :

```css
<div class="ab-pinned-indicator">
  <i class="fa fa-star"></i>
</div>
```

Si vous souhaitez utiliser une autre icône FontAwesome, remplacez le nom de classe de l'élément `i` par celui de l'icône souhaitée. 

Si vous souhaitez changer complètement l'icône, supprimez l'élément `i` et ajoutez l'icône personnalisée en tant qu'enfant de `ab-pinned-indicator`. Il existe plusieurs méthodes pour modifier l'icône, mais une approche simple consiste à utiliser `replaceChildren()` sur l'élément `ab-pinned-indicator`.

Par exemple :

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

Pour définir une icône d'épingle personnalisée, surchargez le style `Braze.ContentCards.PinnedIcon`. Votre ressource d'image personnalisée doit être déclarée dans l'élément `android:src`. Par exemple :

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

Pour modifier l'icône d'épingle par défaut, vous pouvez définir le paramètre [`pinnedResourceId`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-styling/index.html#794044424%2FProperties%2F-1725759721) de `ContentCardStyling`. Par exemple :

```kotlin
ContentCardStyling(
    pinnedResourceId = R.drawable.pushpin,
    pinnedImageAlignment = Alignment.TopCenter
)
```

Vous pouvez également spécifier un Composable dans [`pinnedComposable`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-styling/index.html#1460938052%2FProperties%2F-1725759721) de `ContentCardStyling`. Si `pinnedComposable` est spécifié, il prend le pas sur la valeur de `pinnedResourceId`.

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

Personnalisez l'icône d'épingle en modifiant les propriétés `pinIndicatorColor` et `pinIndicatorImage` de la propriété d'instance [`cellAttributes`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/cellattributes/). Par exemple :

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.cellAttributes.pinIndicatorColor = .red
attributes.cellAttributes.pinIndicatorImage = UIImage(named: "my-image")

let viewController = BrazeContentCardUI.ViewController.init(braze: braze, attributes: attributes)
```

Vous pouvez également utiliser le sous-classement pour créer votre propre version personnalisée de `BrazeContentCardUI.Cell`, qui inclut l'indicateur d'épingle. Par exemple : 

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.cells[BrazeContentCardUI.ClassicImageCell.identifier] = CustomClassicImageCell.self

let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)
```

{% endsubtab %}
{% subtab Objective-C %}

La personnalisation de l'indicateur d'épingle via `Attributes` n'est pas prise en charge en Objective-C.

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Modifier la couleur de l'indicateur de non-lecture

Les cartes de contenu comportent une ligne bleue en bas de la carte qui indique si celle-ci a été consultée ou non. 

![Deux cartes de contenu affichées côte à côte. La première carte a une ligne bleue en bas, indiquant qu'elle n'a pas été vue. La deuxième carte n'a pas de ligne bleue, indiquant qu'elle a déjà été vue.]({% image_buster /assets/img/braze-content-cards-seen-unseen-behavior.png %})

{% tabs %}
{% tab web %}

Pour modifier la couleur de l'indicateur de non-lecture d'une carte, ajoutez du CSS personnalisé à votre page web. Par exemple, pour définir la couleur de l'indicateur en vert :

```css
.ab-unread-indicator { background-color: green; }
```

{% endtab %}
{% tab android %}

Modifiez la couleur de la barre d'indicateur de non-lecture en changeant la valeur de `com_braze_content_cards_unread_bar_color` dans votre fichier `colors.xml` :

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <!-- The color used to highlight unread Content Cards at their bottom edge -->
  <color name="com_braze_content_cards_unread_bar_color">#1676d0</color>
</resources>
```

{% endtab %}
{% tab Jetpack Compose %}

Pour changer la couleur de la barre d'indicateur de non-lecture, modifiez la valeur de [`unreadIndicatorColor`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-styling/index.html#-1669590042%2FProperties%2F-1725759721) dans `ContentCardStyling` :

```kotlin
ContentCardStyling(
    unreadIndicatorColor = Color.Red
)
```

{% endtab %}
{% tab swift %}

{% subtabs %}
{% subtab Swift %}

Modifiez la couleur de la barre d'indicateur de non-lecture en assignant une valeur à la couleur de teinte de votre instance `BrazeContentCardUI.ViewController` :

```swift
let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze)
viewController.view.tintColor = .systemGreen
```

Si vous souhaitez modifier uniquement l'indicateur de non-consultation, vous pouvez accéder à la propriété `unviewedIndicatorColor` de votre structure `BrazeContentCardUI.ViewController.Attributes`. Si vous utilisez les implémentations `UITableViewCell` de Braze, accédez à la propriété avant que la cellule ne soit dessinée.

Par exemple, pour définir la couleur de l'indicateur de non-consultation en rouge :

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.cellAttributes.unviewedIndicatorColor = .red

let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)
```

Consultez l'[application d'exemple Examples](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/Swift) pour un exemple complet.

{% endsubtab %}
{% subtab Objective-C %}

Modifiez la couleur de la barre d'indicateur de non-lecture en assignant une valeur à la couleur de teinte de votre `BRZContentCardUIViewController` :

```objc
BRZContentCardUIViewController *viewController = [[BRZContentCardUIViewController alloc] initWithBraze:AppDelegate.braze];
[viewController.view setTintColor:[UIColor systemGreenColor]];
```

La personnalisation de l'indicateur de non-consultation uniquement via `Attributes` n'est pas prise en charge en Objective-C.

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Mode sombre

Pour afficher différentes images ou styles selon le mode sombre ou clair de l'appareil, utilisez des [paires clé-valeur]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details#key-value-pairs) dans votre message de carte de contenu. Par exemple, ajoutez une paire clé-valeur comme `dark_mode_image` avec l'URL de votre ressource d'image en mode sombre. Ensuite, dans votre application, ajoutez une logique personnalisée pour vérifier le mode d'apparence actuel de l'appareil et afficher l'image appropriée.

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

Ce modèle fonctionne pour tout contenu dépendant de l'apparence, y compris le texte, les couleurs ou les dispositions. Téléchargez vos ressources d'image en mode sombre dans la [bibliothèque multimédia]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library), puis référencez-les dans une paire clé-valeur.

### Désactiver l'indicateur de non-lecture

{% tabs %}
{% tab web %}

Masquez la barre d'indicateur de non-lecture en ajoutant le style suivant à votre `css` :

```css
.ab-unread-indicator { display: none; }
```

{% endtab %}

{% tab android %}

Masquez la barre d'indicateur de non-lecture en définissant [`setUnreadBarVisible`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.view/-content-card-view-holder/set-unread-bar-visible.html?query=fun%20setUnreadBarVisible(isVisible:%20Boolean)) sur `ContentCardViewHolder` à `false`. 

{% endtab %}

{% tab Jetpack Compose %}
La désactivation de l'indicateur de non-lecture n'est pas prise en charge dans Jetpack Compose.
{% endtab %}
{% tab swift %}
{% subtabs %}
{% subtab Swift %}

Masquez la barre d'indicateur de non-lecture en définissant la propriété `attributes.cellAttributes.unviewedIndicatorColor` de votre structure `Attributes` sur `.clear`. 

{% endsubtab %}
{% subtab Objective-C %}

La personnalisation de l'indicateur de non-consultation uniquement via `Attributes` n'est pas prise en charge en Objective-C.

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}