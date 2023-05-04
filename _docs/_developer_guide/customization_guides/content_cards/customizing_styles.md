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

### Custom font

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam convallis velit eget bibendum vulputate. Praesent sed mauris nec turpis faucibus bibendum vel et enim. Suspendisse potenti. Donec eleifend, arcu non molestie laoreet, mauris mauris sodales nunc, vitae euismod augue metus eu justo. Vivamus eleifend interdum ipsum, vitae hendrerit libero auctor sit amet. Fusce sodales ipsum sit amet risus venenatis ultricies. Etiam elementum risus vel lorem tincidunt varius. Sed euismod elit vel enim volutpat, quis dapibus mauris convallis. Sed nec quam a est tempor imperdiet id id ante. Sed in tortor vel libero placerat tincidunt.

{% tabs %}
{% tab Android %}

Braze allows setting a custom font using the [font family guide][40]. To use it, override a style for cards and use the `fontFamily` attribute to instruct Braze to use your custom font family.

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

{% subtabs %}
{% subtab Java %}

Java content

{% endsubtab %}
{% subtab Kotlin %}

Kotlin content

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab iOS %}

iOS content

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

Web content

{% endtab %}
{% endtabs %}

### Custom pinned icons
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam convallis velit eget bibendum vulputate. Praesent sed mauris nec turpis faucibus bibendum vel et enim. Suspendisse potenti. Donec eleifend, arcu non molestie laoreet, mauris mauris sodales nunc, vitae euismod augue metus eu justo. Vivamus eleifend interdum ipsum, vitae hendrerit libero auctor sit amet. Fusce sodales ipsum sit amet risus venenatis ultricies. Etiam elementum risus vel lorem tincidunt varius. Sed euismod elit vel enim volutpat, quis dapibus mauris convallis. Sed nec quam a est tempor imperdiet id id ante. Sed in tortor vel libero placerat tincidunt.

NOTE TO JOSH: Should these be called "badges" or "pinned icons" or what?

{% tabs %}
{% tab Android %}

Android content

{% subtabs %}
{% subtab Java %}

Java content

{% endsubtab %}
{% subtab Kotlin %}

Kotlin content

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab iOS %}

iOS content

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

Web content

{% endtab %}
{% endtabs %}

### Customizing the read and unread indicators
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam convallis velit eget bibendum vulputate. Praesent sed mauris nec turpis faucibus bibendum vel et enim. Suspendisse potenti. Donec eleifend, arcu non molestie laoreet, mauris mauris sodales nunc, vitae euismod augue metus eu justo. Vivamus eleifend interdum ipsum, vitae hendrerit libero auctor sit amet. Fusce sodales ipsum sit amet risus venenatis ultricies. Etiam elementum risus vel lorem tincidunt varius. Sed euismod elit vel enim volutpat, quis dapibus mauris convallis. Sed nec quam a est tempor imperdiet id id ante. Sed in tortor vel libero placerat tincidunt.

{% tabs %}
{% tab Android %}

Android content

{% subtabs %}
{% subtab Java %}

Java content

{% endsubtab %}
{% subtab Kotlin %}

Kotlin content

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab iOS %}

iOS content

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

Web content

{% endtab %}
{% endtabs %}

[1]: {% image_buster/assets/img/content_cards/content-card-customization-attributes.png %}