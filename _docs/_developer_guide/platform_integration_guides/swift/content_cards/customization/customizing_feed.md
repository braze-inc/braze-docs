---
nav_title: Customizing Feed
article_title: Customizing Content Card Feed for iOS
platform: Swift
page_order: 2
description: "This article covers Content Card feed customization options in your iOS application."
channel:
  - content cards
---

# Customizing the Content Cards feed

Content Cards UI components are available in the `BrazeUI` library of the Swift SDK. You can customize your Content Cards UI elements and behavior by modifying the `Attributes` struct of `BrazeContentCardUI.ViewController`. Alternatively, the Content Card cells may also be subclassed and then used programmatically by overriding the `cells` property in the `Attributes` struct. Check out the [Examples sample app](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/Swift) for a complete example. 

It's also important to consider whether you should use a simple customization strategy with `Attributes` versus a completely custom view controller and [subscribe for data updates]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/content_cards/integration/). For example, if you configure using `Attributes`, you can launch your Content Cards UI with minimal setup. However, if you use a complete view controller customization, you have more control over the card behavior, such as displaying in a carousel or adding interactive elements, but you would have to implement the respective methods to ensure impressions, dismissal events, and clicks are properly logged.

## Customizing UI

The following code snippets show how to style and change out-of-the-Box Content Cards to fit your UI needs using methods provided by the SDK. These methods allow you to customize all aspects of the Content Card UI, including custom fonts, customized color components, customized text, and more. 

You can customize the default Braze Content Card UI by modifying the `Attributes` struct. BrazeUI offers two ways to configure this object:
- Modifying the `Attributes.defaults` static variable.
- Passing your `Attributes` struct to the `BrazeContentCardUI/ViewController` initializer.

{% alert note %}
Customization via `Attributes` is only available in Swift.
{% endalert %}

### Modifying `Attributes.defaults`

You can customize the look and feel of all instances of the Braze Content Card UI view controller, you can directly modify the static `Attributes.defaults` variable. Refer to the code snippet below for an example:

{% tabs %}
{% tab Swift %}
```swift
BrazeContentCardUI.ViewController.Attributes.defaults.cellAttributes.cornerRadius = 20
BrazeContentCardUI.ViewController.Attributes.defaults.cellAttributes.classicImageSize = CGSize(width: 65, height: 65)
```
{% endtab %}
{% endtabs %}

### Initializing the view controller with `Attributes`

If you wish to modify only a specific instance of the Braze Content Card UI view controller, you can initialize this instance with your own `Attributes` object:

{% tabs %}
{% tab Swift %}
```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.cellAttributes.cornerRadius = 20
attributes.cellAttributes.classicImageSize = CGSize(width: 65, height: 65)

let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)
```
{% endtab %}
{% endtabs %}

## Creating custom cells by subclassing

Custom interfaces can be provided by registering custom classes for each desired card type. 

![A banner Content Card. A banner Content Card shows an image to the right of the banner with the text "Thanks for downloading Braze Demo!".]({% image_buster /assets/img/interface1.png %}){: style="max-width:35%;margin-left:15px;"}
![A captioned image Content Card. A captioned Content Card shows a Braze image with the caption overlayed across the bottom "Thanks for downloading Braze Demo!". ]({% image_buster /assets/img/interface2.png %}){: style="max-width:25%;margin-left:15px;"}
![A classic Content Card. A classic Content Card shows an image in the center of the card with the words "Thanks for downloading Braze Demo" underneath.]({% image_buster /assets/img/interface3.png %}){: style="max-width:18%;margin-left:15px;"}

Braze provides five Content Card templates out of the box (banner, captioned image, classic, classic image, and control). Alternatively, if you would like to provide your own custom interfaces, reference the following code snippets:

{% tabs %}
{% tab Swift %}
```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
// Register your own custom cell
attributes.cells[BrazeContentCardUI.ClassicImageCell.identifier] = CustomClassicImageCell.self

let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)
```
{% endtab %}
{% endtabs %}

## Modifying content cards

Content Cards can be changed programmatically by assigning the `transform` closure on your `Attributes` struct. The example below modifies the `title` and `description` of compatible cards:

{% tabs %}
{% tab Swift %}
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
{% endtab %}
{% endtabs %}