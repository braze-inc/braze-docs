---
nav_title: Customizing Card Styles
article_title: Customizing Content Card Styles
page_order: 1
description: "This article covers custom styling options for your Content Cards."
channel:
  - content cards
---

# Customizing Content Card styles

> Braze Content Cards come with a default look and feel. This article covers custom styling options for your Content Cards.

## Customizing styling

Braze provides five Content Card templates: banner, captioned image, classic, classic image, and control. The default Content Cards UI can be integrated from the `BrazeUI` library of the Braze SDK. Then, you can tweak certain parts of the card's styling. 

<!--- Question: Is `BrazeUI` a concept that all platform SDKs share, or is the term here inappropriate when used outside of the Swift SDK? --->

![Two content cards, one with the default font and square corners, and one with rounded corners and a curly font][1]

{% alert important %}
Content card properties such as title, description, image, etc. are directly available on the Braze/ContentCard data type. Configuring these [content cards properties]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details) through the Braze dashboard is the preferred way to customize these properties.
{% endalert %}


{% tabs %}
{% tab Android %}

By default, Android and FireOS SDK Content Cards match the standard Android UI guidelines to provide a seamless experience. You can see these default styles in the [`res/values/styles.xml`](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/res/values/styles.xml) file in the Braze SDK distribution:

```xml
  <!-- Content Cards Example -->
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

To customize your Content Card stylings, override this default style. To override a style, copy it in its entirety to the `styles.xml` file in your project and make modifications. The entire style must be copied over to your local `styles.xml` file for all attributes to be correctly set.

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
{% tab iOS %}

The Content Cards view controller allows you to customize the appearance and behavior of all cells via the [`BrazeContentCardUI.ViewController.Attributes`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct) struct. Configuring Content Cards using `Attributes` is an easy option, allowing you to launch your Content Cards UI with minimal setup. 

> Customization via `Attributes` is only available in Swift.

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

If you wish to modify only a specific instance of the Braze Content Card UI view controller, use the [init(braze:attributes:)](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/init(braze:attributes:)/) initializer to pass a custom `Attributes` struct to the view controller.

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
{% tab Web %}

Braze’s default styles are defined in CSS within the Braze SDK. By overriding selected styles in your application, it is possible to customize our standard feed with your own background images, font families, styles, sizes, animations, and more. For instance, the following is an example override that will cause Content Cards to appear 800 px wide:

``` css
body .ab-feed {
  width: 800px;
}
```

{% endtab %}
{% endtabs %}

## Customization recipes 

Here are multiple recipes for common customization use cases.

### Custom font

Customizing the font used in your Content Cards allows you to maintain your brand identity and create a visually appealing experience for your users. Use these recipes to set the font for all Content Cards programmatically. 

{% tabs %}
{% tab Android %}

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
{% tab iOS %}

<!--- To do: Add recipe for customizing font on iOS --->

{% subtabs %}
{% subtab Swift %}

Swift content

{% endsubtab %}
{% subtab Objective-C %}

Objective-C content

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Web %}

<!--- To do: Add recipe for customizing font through CSS --->

Web content

{% endtab %}
{% endtabs %}

### Custom pinned icons

When creating a Content Card, marketers have the option of pinning the card. A pinned card will display at the top of a user's feed and can't be dismissed by the user. As you customize your card styles, you have the ability to change what the pinned icon looks like.

![Side-by-side of the Content Card preview in Braze for Mobile and Web with the option "Pin this card to the top of the feed" selected.][2]{:style="border:none"}

{% tabs %}
{% tab Android %}

To set a custom pinned icon, override the `Braze.ContentCards.PinnedIcon` style. Your custom image asset should be declared in the `android:src` element.

{% endtab %}
{% tab iOS %}

<!--- To do: Add recipe for customizing the pinned icon on iOS --->

{% subtabs %}
{% subtab Swift %}

Swift content

{% endsubtab %}
{% subtab Objective-C %}

Objective-C content

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Web %}

<!--- To do: Add recipe for customizing font through CSS --->

Web content

{% endtab %}
{% endtabs %}

### Changing the unread indicator color

Content Cards contain a blue line at the bottom of the card which indicates whether or not the card has been viewed. 

![Two Content Cards displayed side by side. The first card has a blue line at the bottom, indicating it has not been seen. The second card does not have a blue line, indicating it has already been seen.][3]{: style="max-width:80%"}

{% tabs %}
{% tab Android %}

Change the color of the unread indicator bar by altering the value in `com_braze_content_cards_unread_bar_color` in your `colors.xml` file:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <!-- The color used to highlight unread Content Cards at their bottom edge -->
  <color name="com_braze_content_cards_unread_bar_color">#1676d0</color>
</resources>
```

{% endtab %}
{% tab iOS %}

{% subtabs %}
{% subtab Swift %}

The color of the unviewed indicator can be set by assigning a value to the tint color of your `BrazeContentCardUI.ViewController` instance:

```swift
let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze)
viewController.view.tintColor = .systemGreen
```

However, if you wish to modify only the unviewed indicator, you can access the `unviewedIndicatorColor` property of your `BrazeContentCardUI.ViewController.Attributes` struct. If you utilize Braze's `UITableViewCell` implementations, you should access the property before the cell is drawn.

For example, to set the color of the unviewed indicator to red:

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.cellAttributes.unviewedIndicatorColor = .red

let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)
```

{% endsubtab %}
{% subtab Objective-C %}

The color of the unviewed indicator can be set by assigning a value to the tint color of your `BRZContentCardUIViewController`:

```objc
BRZContentCardUIViewController *viewController = [[BRZContentCardUIViewController alloc] initWithBraze:AppDelegate.braze];
[viewController.view setTintColor:[UIColor systemGreenColor]];
```

Customization of only the unviewed indicator via `Attributes` is not supported in Objective-C.

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Web %}

To change the color of the unread indicator of a card, add custom CSS to your webpage. For example, changing it to green with the following CSS:

```css
.ab-unread-indicator { background-color: green !important; }
```

{% endtab %}
{% endtabs %}

### Disabling unread indicator

To disable the unread indicator, hide the indicator bar by setting its color to clear or none.

{% tabs %}
{% tab Android %}

Hide the unread indicator bar by altering the value in `com_braze_content_cards_unread_bar_color` in your `colors.xml` file:

  <!-- TO DO: What color should be used here? -->

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <!-- The color used to highlight unread Content Cards at their bottom edge -->
  <color name="com_braze_content_cards_unread_bar_color">#1676d0</color>
</resources>
```

{% endtab %}
{% tab iOS %}
{% subtabs %}
{% subtab Swift %}

Hide the unread indicator bar by setting the `attributes.cellAttributes.unviewedIndicatorColor` property in your `Attributes` struct to `.clear`. 

{% endsubtab %}
{% subtab Objective-C %}

Customization of only the unviewed indicator via `Attributes` is not supported in Objective-C.

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Web %}

Hide the unread indicator bar by adding the following style to your `css`:

```css
.ab-unread-indicator { display: none; }
```

{% endtab %}
{% endtabs %}

[1]: {% image_buster/assets/img/content_cards/content-card-customization-attributes.png %}
[2]: {% image_buster /assets/img/cc_pin_to_top.png %}
[3]: {% image_buster /assets/img/braze-content-cards-seen-unseen-behavior.png %}