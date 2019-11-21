---
nav_title: Customization
platform: iOS
page_order: 1
search_rank: 5
---

# Content Cards View Controller Integration

Content Cards can be integrated with two view controller contexts: Navigation or Modal.

## Navigation Context

Example of pushing a `ABKContentCardsTableViewController` instance into a navigation controller:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
ABKContentCardsTableViewController *contentCards = [ABKContentCardsTableViewController getNavigationFeedViewController];
contentCards.title = "Content Cards Title";
contentCards.disableUnreadIndicator = YES;
[self.navigationController pushViewController:contentCards animated:YES];
```

{% endtab %}
{% tab swift %}

```swift
let contentCards = ABKContentCardsTableViewController()
contentCards.title = "Content Cards Title"
contentCards.disableUnreadIndicator = true
navigationController?.pushViewController(contentCards, animated: true)
```

{% endtab %}
{% endtabs %}

{% alert note %}
To customize the navigation bar's title, set the title property of the `ABKContentCardsTableViewController` instance's `navigationItem`.
{% endalert %}

## Modal Context

This modal is used to present the view controller in a modal view, with a navigation bar on top and a Done button on the right side of the bar.

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
ABKContentCardsViewController *contentCards = [[ABKContentCardsViewController alloc] init];
contentCards.contentCardsViewController.title = "Content Cards Title";
contentCards.contentCardsViewController.disableUnreadIndicator = YES;
[self.navigationController presentViewController:contentCards animated:YES completion:nil];
```

{% endtab %}
{% tab swift %}

```swift
let contentCards = ABKContentCardsViewController()
contentCards.contentCardsViewController.title = "Content Cards Title"
contentCards.contentCardsViewController.disableUnreadIndicator = true
self.present(contentCards, animated: true, completion: nil)
```

{% endtab %}
{% endtabs %}

For examples of these view controllers, check out our [Content Cards sample app](https://github.com/Appboy/appboy-ios-sdk/tree/master/Samples/ContentCards/BrazeContentCardsSampleApp).

{% alert note %}
To customize the header, set the title property of the `navigationItem` belonging to the `ABKContentCardsTableViewController` instance embedded in the parent `ABKContentCardsViewController` instance.
{% endalert %}

## Overriding Default Images

Braze allows clients to replace existing default images with their own custom images. To accomplish this, create a new `png` file with the custom image and add it to the app’s image bundle. Then, rename the file with the image’s name (see below) to override the default image in our library. Images available for override in Content Cards include:
* Placeholder image: `appboy_cc_noimage_lrg`.
* Pinned icon image: `appboy_cc_icon_pinned`.

{% alert note %} Be sure to upload the `@2x` and `@3x` versions of the images as well to accommodate different phone sizes. {% endalert %}

 {% alert note %}
 Content Cards have a maximum size of __2kb__ (including images, links, and all content) - anything that exceeds that amount will cause an error and prevent the card from sending.
 {% endalert %}

## Customizing the Content Cards Feed

You can create your own Content Cards interface by extending `ABKContentCardsTableViewController` to customize all UI elements and Content Cards behavior. Alternatively, you can create a completely custom view controller and subscribe for data updates. In the latter case, you would need to log all view events, dismissed events, and clicks manually.
