---
nav_title: Customization
platform: iOS
page_order: 2
description: "This article covers customization options for your Content Cards in your iOS application."
channel:
  - content cards

---

# Customization

## Overriding Default Images

{% alert important %}
__Note that integration of `SDWebImage` is required if you plan on using our Braze UI for displaying images__ within iOS In-App Messages, News Feed, or Content Cards.
{% endalert %}

Braze allows clients to replace existing default images with their own custom images. To accomplish this, create a new `png` file with the custom image and add it to the app’s image bundle. Then, rename the file with the image’s name (see below) to override the default image in our library. Images available for override in Content Cards include:

- Placeholder image: `appboy_cc_noimage_lrg`.
- Pinned icon image: `appboy_cc_icon_pinned`.

Because Content Cards have a maximum size of **2kb** (including images, links, and all content) make sure to check the size before sending. Exceeding this amount will prevent the card from sending.

{% alert note %}
Be sure to upload the `@2x` and `@3x` versions of the images as well to accommodate different phone sizes.
{% endalert %}

{% alert note %}
Note that overriding default images is currently not supported in our Xamarin iOS integration.
{% endalert %}

## Customizing the Content Cards Feed

You can create your own Content Cards interface by extending `ABKContentCardsTableViewController` to customize all UI elements and Content Cards behavior. The Content Card cells may also be subclassed and then used programmatically or by introducing a custom Storyboard that registers the new classes. See the [Content Cards sample app](https://github.com/Appboy/appboy-ios-sdk/tree/master/Samples/ContentCards/BrazeContentCardsSampleApp) for a more complete example. Alternatively, you can create a completely custom view controller and [subscribe for data updates]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/data_model/). In the latter case, you would need to log all view events, dismissed events, and clicks manually.

## Handling Clicks Manually

You can manually handle Content Card clicks by implementing the [ABKContentCardsTableViewControllerDelegate](https://appboy.github.io/appboy-ios-sdk/docs/protocol_a_b_k_content_cards_table_view_controller_delegate-p.html) protocol and setting your delegate object as the `delegate` property of the `ABKContentCardsTableViewController`. See the [Content Cards sample app](https://github.com/Appboy/appboy-ios-sdk/tree/master/Samples/ContentCards/BrazeContentCardsSampleApp) for an example. 

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
contentCardsTableViewController.delegate = delegate;

// Methods to implement in delegate
- (BOOL)contentCardTableViewController:(ABKContentCardsTableViewController *)viewController
                 shouldHandleCardClick:(NSURL *)url {
  if ([[url.host lowercaseString] isEqualToString:@"my-domain.com"]) {
    // Custom handle link here
    NSLog(@"Manually handling content card click with URL %@", url.absoluteString);
    return NO;
  }
  // Let the Braze SDK handle the click action
  return YES;
}

- (void)contentCardTableViewController:(ABKContentCardsTableViewController *)viewController
                    didHandleCardClick:(NSURL *)url {
  NSLog(@"Braze SDK handled content card click with URL %@", url.absoluteString);
}
```

{% endtab %}
{% tab swift %}

```swift
contentCardsTableViewController.delegate = delegate

// Methods to implement in delegate
func contentCardTableViewController(_ viewController: ABKContentCardsTableViewController!,
                                    shouldHandleCardClick url: URL!) -> Bool {
  if (url.host?.lowercased() == "my-domain.com") {
    // Custom handle link here
    NSLog("Manually handling content card click with URL %@", url.absoluteString)
    return false
  }
  // Let the Braze SDK handle the click action
  return true
}

func contentCardTableViewController(_ viewController: ABKContentCardsTableViewController!,
                                    didHandleCardClick url: URL!) {
  NSLog("Braze SDK handled content card click with URL %@", url.absoluteString)
}
```

{% endtab %}
{% endtabs %}

{% alert important %}
If you override the `handleCardClick:` method in `ABKContentCardsTableViewController`, then these delegate methods might not be called.
{% endalert %}
