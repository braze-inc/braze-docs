---
nav_title: Customizing UI
article_title: Customizing the Content Card UI
page_order: 2
description: "This article covers Content Card feed customization options in your iOS application."
channel:
  - content cards
---

# Customizing the Content Card UI

The UI components of Content Cards are available in the `BrazeUI` library of the Swift SDK, allowing you to customize their appearance and behavior. 

At Braze, we break down customization into different approaches based on the associated effort and level of flexibility provided. Configuring Content Cards using `Attributes` is the simplest option, allowing you to launch your Content Cards UI with minimal setup. Alternatively, you can create a custom view controller component that [subscribes to data updates and logs analytics]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/content_cards/integration/). The latter provides more control over the card behavior, such as displaying in a carousel or adding interactive elements, but requires you to ensure that impressions, dismissal events, and clicks are properly logged.

This article covers configuring your Content Cards using `Attributes`. For an example of implementing a custom view controller, see the [carousel view use case]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/content_cards/customization/carousel_view/).

## Customizing UI

You can customize your Content Cards UI elements by modifying the `Attributes` struct of `BrazeContentCardUI.ViewController`. `BrazeUI` offers two ways to configure this object:
- Modifying the [`Attributes.defaults`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/defaults) static variable
- Passing your `Attributes` struct to the `BrazeContentCardUI/ViewController` [initializer](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/init(braze:attributes:))

The following code snippets show how to style and change the default Content Cards using methods provided by the SDK. These methods allow you to customize all aspects of the Content Card UI, including custom fonts, customized color components, customized text, and more. 

{% alert note %}
Customization via `Attributes` is only available in Swift.
{% endalert %}

### Modifying Attributes.defaults

Customize the look and feel of all instances of the Braze Content Card UI view controller by directly modifying the static `Attributes.defaults` variable. Refer to the code snippet below for an example:

{% tabs %}
{% tab Swift %}
```swift
BrazeContentCardUI.ViewController.Attributes.defaults.cellAttributes.cornerRadius = 20
BrazeContentCardUI.ViewController.Attributes.defaults.cellAttributes.classicImageSize = CGSize(width: 65, height: 65)
```
{% endtab %}
{% endtabs %}

### Initializing the view controller with Attributes

If you wish to modify only a specific instance of the Braze Content Card UI view controller, initialize this instance with your own `Attributes` object:

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

Alternatively, you can create custom interfaces by registering custom classes for each desired card type. Braze provides five Content Card default templates: banner, captioned image, classic, classic image, and control. The Content Card cells may be subclassed and then used programmatically by overriding the [`cells`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/cells) property in the `Attributes` struct.

![A banner Content Card. A banner Content Card shows an image to the right of the banner with the text "Thanks for downloading Braze Demo!".]({% image_buster /assets/img/interface1.png %}){: style="max-width:35%;margin-left:15px;"}
![A captioned image Content Card. A captioned Content Card shows a Braze image with the caption overlayed across the bottom "Thanks for downloading Braze Demo!". ]({% image_buster /assets/img/interface2.png %}){: style="max-width:25%;margin-left:15px;"}
![A classic Content Card. A classic Content Card shows an image in the center of the card with the words "Thanks for downloading Braze Demo!" underneath.]({% image_buster /assets/img/interface3.png %}){: style="max-width:18%;margin-left:15px;"}

Alternatively, if you would like to provide your own custom interfaces, reference the following code snippets:

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

Check out the [Examples sample app](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/Swift) for a complete example.

## Modifying content cards

Content Cards can be changed programmatically by assigning the [`transform`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/transform) closure on your `Attributes` struct. The example below modifies the `title` and `description` of compatible cards:

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

## Multiple feeds

Content Cards can be filtered on your app so that only specific cards are displayed, enabling you to have multiple Content Card feeds for different use cases. For example, you can maintain both a transactional feed and a marketing feed.

### Step 1: Setting key-value pairs on cards

When creating a Content Card campaign, set key-value pair data on each card. Braze filtering logic will use this key-value pair data to categorize cards.

For this example, we'll set a key-value pair with the key `feed_type` that will designate which Content Card feed the card should be displayed. The value will be whatever your custom feeds will be, such as `Transactional`, `Marketing`, etc.

### Step 2: Filter your content cards

Refer the following code snippet to filter your Content Cards. In this example, we will only display cards with a matching key-value pair of `feed_type: "Transactional"` in the `extras` dictionary.

{% tabs %}
{% tab SWIFT %}
```swift
// Filter cards by the `Transactional` feed type based on your key-value pair.
let transactionalCards = cards.filter { $0.extras["feed_type"] as? String == "Transactional" }
```

To take it a step further with Content Cards UI, you can access the `transform` property on your `Attributes` struct to display only the cards filtered by your criteria.

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.transform = { cards in
  cards.filter { $0.extras["feed_type"] as? String == "Transactional" }
}

// Pass your attributes containing the transformed cards to the Content Card UI.
let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)
```
{% endtab %}
{% tab OBJECTIVE-C %}

```objc
// Filter cards by the `Transactional` feed type based on your key-value pair.
NSMutableArray<BRZContentCardRaw *> *transactionalCards = [[NSMutableArray alloc] init];
for (BRZContentCardRaw *card in AppDelegate.braze.contentCards.cards) {
  if ([card.extras[@"feed_type"] isEqualToString:@"Transactional"]) {
    [transactionalCards addObject:card];
  }
}
```
{% endtab %}
{% endtabs %}

For further details about customizing Content Cards, refer to the [Content Cards UI customization tutorial](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/content-cards-customization/)