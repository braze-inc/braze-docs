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
The default Content Cards UI can be integrated from the `BrazeUI` library of the Braze SDK. 

Braze provides five Content Card default templates: banner, captioned image, classic, classic image, and control. 

{% alert important %}
Content card properties such as title, description, image, etc. are directly available on the Braze/ContentCard data type. Configuring these [content cards properties through the Braze dashboard]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details) is the preferred way to customize these properties.
{% endalert %}

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

You will configure and use `BrazeUI/BrazeContentCardsUI` to display Content Cards to your users. Create the Content Cards [view controller]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/content_cards/integration#content-cards-ui-integration) using the `braze` instance. 

Depending on the type of Content Card, the `BrazeUI` module defaults to one of the cells below for display:

* `ClassicCell`

* `ClassicImageCell`

* `BannerCell`

* `CaptionedImageCell`

* `Control`

The Content Cards view controller allows you to customize the appearance and behavior of all cells via the [`BrazeContentCardUI.ViewController.Attributes`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct) struct. Configuring Content Cards using `Attributes` is the simplest option, allowing you to launch your Content Cards UI with minimal setup. 

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
If you wish to modify only a specific instance of the Braze Content Card UI view controller, use the [init(braze:attributes:)](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/init(braze:attributes:) initializer to pass a custom `Attributes` struct to the view controller.

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

Web content

{% endtab %}
{% endtabs %}



## Custom font
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

## Custom pinned icons
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

## Custom card rendering
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

## Dark theme customization 
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
