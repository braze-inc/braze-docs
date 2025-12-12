---
nav_title: Style
article_title: Customizing the style of Content Cards
page_order: 1
description: "This article covers styling options for your Content Cards."
channel:
  - content cards
platform:
  - Android
  - FireOS
  - Swift
  - Web
---

# Customizing the style of Content Cards

> Braze Content Cards come with a default look and feel. This article covers styling options for your Content Cards to help you match your brand identity. For the full list of content card types, see [About Content Cards]({{site.baseurl}}/developer_guide/content_cards/).

## Creating a custom style

The default Content Cards UI is imported from the UI layer of the Braze SDK. From there, you can tweak certain parts of the card's styling, the order in which cards are displayed, and how the feed is shown to your users.

![Two content cards, one with the default font and square corners, and one with rounded corners and a curly font]({% image_buster/assets/img/content_cards/content-card-customization-attributes.png %})

{% alert note %}
Content Card properties such as `title`, `cardDescription`, `imageUrl`, etc., are directly editable through the [dashboard]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details), which is the preferred method for changing these details.
{% endalert %}


{% tabs %}
{% tab web %}

Braze’s default styles are defined in CSS within the Braze SDK. By overriding selected styles in your application, it is possible to customize our standard feed with your own background images, font families, styles, sizes, animations, and more. For instance, the following is an example override that will cause Content Cards to appear 800 px wide:

``` css
body .ab-feed {
  width: 800px;
}
```

{% endtab %}
{% tab android %}

By default, Android and FireOS SDK Content Cards match the standard Android UI guidelines to provide a seamless experience. You can see these default styles in the [`res/values/styles.xml`](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/res/values/styles.xml) file in the Braze SDK distribution:

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

To customize your Content Card styling, override this default style. To override a style, copy it in its entirety to the `styles.xml` file in your project and make modifications. The entire style must be copied over to your local `styles.xml` file for all attributes to be correctly set.

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

By default, Android and FireOS SDK Content Cards match the standard Android UI guidelines to provide a seamless experience.

You can apply styling in one of two ways. The first is to pass a [`ContentCardListStyling`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-list-styling/index.html) and [`ContentCardStyling`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-styling/index.html) to [`ContentCardsList`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards/-content-cards-list.html), like in the following example:

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

The second is to use [`BrazeStyle`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose/-braze-style.html) to create a global styling for Braze components, like in the following example:

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

The Content Cards view controller allows you to customize the appearance and behavior of all cells via the [`BrazeContentCardUI.ViewController.Attributes`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct) struct. Configuring Content Cards using `Attributes` is an easy option, allowing you to launch your Content Cards UI with minimal setup. 

{% alert important %}
Customization via `Attributes` is only available in Swift.
{% endalert %}

{% subtabs %}
{% subtab Swift %}

**Modifying `Attributes.default`**

Customize the look and feel of all instances of the Braze Content Card UI view controller by directly modifying the static [`Attributes.defaults`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/defaults) variable.

For example, to change the default image size and corner radius for all cells:

```swift
BrazeContentCardUI.ViewController.Attributes.defaults.cellAttributes.cornerRadius = 20
BrazeContentCardUI.ViewController.Attributes.defaults.cellAttributes.classicImageSize = CGSize(width: 65, height: 65)
```

**Initializing the view controller with Attributes**

If you wish to modify only a specific instance of the Braze Content Card UI view controller, use the [`init(braze:attributes:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/init(braze:attributes:)/) initializer to pass a custom `Attributes` struct to the view controller.

For example, you can change the image size and corner radius for a specific instance of the view controller:

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.cellAttributes.cornerRadius = 20
attributes.cellAttributes.classicImageSize = CGSize(width: 65, height: 65)

let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)
```

**Customizing cells by subclassing**

Alternatively, you can create custom interfaces by registering custom classes for each desired card type. To use your subclass instead of the default cell, modify the [`cells`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/cells) property in the `Attributes` struct. For example:

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
// Register your own custom cell
attributes.cells[BrazeContentCardUI.ClassicImageCell.identifier] = CustomClassicImageCell.self

let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)
```

**Modifying content cards programmatically**

Content Cards can be changed programmatically by assigning the [`transform`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/transform) closure on your `Attributes` struct. The example below modifies the `title` and `description` of compatible cards:

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

Check out the [Examples sample app](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/Swift) for a complete example.

{% endsubtab %}
{% subtab Objective-C %}

Customizing Content Cards through `Attributes` is not supported with Objective-C.

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Customization examples

### Custom font

Customizing the font used in your Content Cards allows you to maintain your brand identity and create a visually appealing experience for your users. Use these recipes to set the font for all Content Cards programmatically. 

{% tabs %}
{% tab web %}

Just like any other web element, you can easily customize the appearance of Content Cards through CSS. In your CSS file or inline styles, use the `font-family` property and specify the desired font name or font stack.

```css
/* CSS selector targeting the Content Card element */
.card-element {
  font-family: "Helvetica Neue", Arial, sans-serif;
}
```

{% endtab %}
{% tab android %}

To change the default font programmatically, set a style for cards and use the `fontFamily` attribute to instruct Braze to use your custom font family.

For example, to update the font on all titles for captioned image cards, override the `Braze.ContentCards.CaptionedImage.Title` style and reference your custom font family. The attribute value should point to a font family in your `res/font` directory.

Here is a truncated example with a custom font family, `my_custom_font_family`, referenced on the last line:

```xml
  <style name="Braze.ContentCards.CaptionedImage.Title">
    <item name="android:layout_width">wrap_content</item>
    ...
    <item name="android:fontFamily">@font/my_custom_font_family</item>
    <item name="fontFamily">@font/my_custom_font_family</item>
  </style>
```

For more information about font customization in the Android SDK, see the [font family guide]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/font_customization/#font-customization).
{% endtab %}
{% tab Jetpack Compose %}
To change the default font programmatically, you can set the [`titleTextStyle`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-styling/index.html#715371549%2FProperties%2F-1725759721) of `ContentCardStyling`.

You can also set `titleTextStyle` for a specific card type by setting it on [`BrazeShortNewsContentCardStyling`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-braze-short-news-content-card-styling/index.html) and passing it to the [`shortNewsContentCardStyle`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-styling/index.html#8580250%2FProperties%2F-1725759721) of `ContentCardStyling`.

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

Customize your fonts by customizing the `Attributes` of the [`cellAttributes`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/cellattributes/) instance property. For example:

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.cellAttributes.titleFont = .preferredFont(textStyle: .callout, weight: .bold)
attributes.cellAttributes.descriptionFont = .preferredFont(textStyle: .footnote, weight: .regular)
attributes.cellAttributes.domainFont = .preferredFont(textStyle: .footnote, weight: .medium)

let viewController = BrazeContentCardUI.ViewController.init(braze: braze, attributes: attributes)
```

{% endsubtab %}
{% subtab Objective-C %}

Customization of fonts via `Attributes` is not supported in Objective-C. 

Check out the [Examples sample app](https://github.com/braze-inc/braze-swift-sdk/blob/main/Examples/ObjC/Sources/ContentCards-Custom-UI/CardsInfoViewController.m#L97) for an example of building your own UI with custom fonts.

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Custom pinned icons

When creating a Content Card, marketers have the option of pinning the card. A pinned card will display at the top of a user's feed and can't be dismissed by the user. As you customize your card styles, you have the ability to change what the pinned icon looks like.

![Side-by-side of the Content Card preview in Braze for Mobile and Web with the option "Pin this card to the top of the feed" selected.]({% image_buster /assets/img/cc_pin_to_top.png %}){:style="border:none"}

{% tabs %}
{% tab web %}

The structure of the Content Card pinned icon is:

```css
<div class="ab-pinned-indicator">
  <i class="fa fa-star"></i>
</div>
```

If you want to use a different FontAwesome icon, you can simply replace the class name of the `i` element with the class name of the desired icon. 

If you want to swap out the icon altogether, remove the `i` element and add the custom icon as a child of `ab-pinned-indicator`. There are a few different ways you can go about it, but one simple method would be to `replaceChildren()` on the `ab-pinned-indicator` element.

For example:

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

To set a custom pinned icon, override the `Braze.ContentCards.PinnedIcon` style. Your custom image asset should be declared in the `android:src` element. For example:

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

To change the default pinned icon, you can set the [`pinnedResourceId`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-styling/index.html#794044424%2FProperties%2F-1725759721) of `ContentCardStyling`.  For example:

```kotlin
ContentCardStyling(
    pinnedResourceId = R.drawable.pushpin,
    pinnedImageAlignment = Alignment.TopCenter
)
```

You can also specify a Composable in [`pinnedComposable`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-styling/index.html#1460938052%2FProperties%2F-1725759721) of `ContentCardStyling`. If `pinnedComposable` is specified, it will override the `pinnedResourceId` value.

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

Customize the pin icon by modifying the `pinIndicatorColor` and `pinIndicatorImage` properties of the [`cellAttributes`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/cellattributes/) instance property. For example:

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.cellAttributes.pinIndicatorColor = .red
attributes.cellAttributes.pinIndicatorImage = UIImage(named: "my-image")

let viewController = BrazeContentCardUI.ViewController.init(braze: braze, attributes: attributes)
```

You can also use subclassing to create your own custom version of `BrazeContentCardUI.Cell`, which includes the pin indicator. For example: 

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.cells[BrazeContentCardUI.ClassicImageCell.identifier] = CustomClassicImageCell.self

let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)
```

{% endsubtab %}
{% subtab Objective-C %}

Customization of the pin indicator via `Attributes` is not supported in Objective-C.

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Changing the unread indicator color

Content Cards contain a blue line at the bottom of the card which indicates whether or not the card has been viewed. 

![Two Content Cards displayed side by side. The first card has a blue line at the bottom, indicating it has not been seen. The second card does not have a blue line, indicating it has already been seen.]({% image_buster /assets/img/braze-content-cards-seen-unseen-behavior.png %})

{% tabs %}
{% tab web %}

To change the color of the unread indicator of a card, add custom CSS to your webpage. For example, to set the color of the unviewed indicator to green:

```css
.ab-unread-indicator { background-color: green; }
```

{% endtab %}
{% tab android %}

Change the color of the unread indicator bar by altering the value in `com_braze_content_cards_unread_bar_color` in your `colors.xml` file:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <!-- The color used to highlight unread Content Cards at their bottom edge -->
  <color name="com_braze_content_cards_unread_bar_color">#1676d0</color>
</resources>
```

{% endtab %}
{% tab Jetpack Compose %}

To change the color of the unread indicator bar, modify the value of [`unreadIndicatorColor`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-styling/index.html#-1669590042%2FProperties%2F-1725759721) in `ContentCardStyling`:

```kotlin
ContentCardStyling(
    unreadIndicatorColor = Color.Red
)
```

{% endtab %}
{% tab swift %}

{% subtabs %}
{% subtab Swift %}

Change the color of the unread indicator bar by assigning a value to the tint color of your `BrazeContentCardUI.ViewController` instance:

```swift
let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze)
viewController.view.tintColor = .systemGreen
```

However, if you wish to modify only the unviewed indicator, you can access the `unviewedIndicatorColor` property of your `BrazeContentCardUI.ViewController.Attributes` struct. If you use Braze `UITableViewCell` implementations, you should access the property before the cell is drawn.

For example, to set the color of the unviewed indicator to red:

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.cellAttributes.unviewedIndicatorColor = .red

let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)
```

Check out the [Examples sample app](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/Swift) for a complete example.

{% endsubtab %}
{% subtab Objective-C %}

Change the color of the unread indicator bar by assigning a value to the tint color of your `BRZContentCardUIViewController`:

```objc
BRZContentCardUIViewController *viewController = [[BRZContentCardUIViewController alloc] initWithBraze:AppDelegate.braze];
[viewController.view setTintColor:[UIColor systemGreenColor]];
```

Customization of only the unviewed indicator via `Attributes` is not supported in Objective-C.

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Disabling unread indicator

{% tabs %}
{% tab web %}

Hide the unread indicator bar by adding the following style to your `css`:

```css
.ab-unread-indicator { display: none; }
```

{% endtab %}

{% tab android %}

Hide the unread indicator bar by setting [`setUnreadBarVisible`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.view/-content-card-view-holder/set-unread-bar-visible.html?query=fun%20setUnreadBarVisible(isVisible:%20Boolean)) on `ContentCardViewHolder` to `false`. 

{% endtab %}

{% tab Jetpack Compose %}
Disabling the unread indicator is not supported in Jetpack Compose.
{% endtab %}
{% tab swift %}
{% subtabs %}
{% subtab Swift %}

Hide the unread indicator bar by setting the `attributes.cellAttributes.unviewedIndicatorColor` property in your `Attributes` struct to `.clear`. 

{% endsubtab %}
{% subtab Objective-C %}

Customization of only the unviewed indicator via `Attributes` is not supported in Objective-C.

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}
