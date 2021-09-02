---
nav_title: Customization
article_title: Content Card Customization for iOS
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

Because Content Cards have a maximum size of 2 KB for content you enter in the dashboard (including message text, image URLs, links, and all key-value pairs), make sure to check the size before sending. Exceeding this amount will prevent the card from sending.

{% alert note %}
Be sure to upload the `@2x` and `@3x` versions of the images as well to accommodate different phone sizes.
{% endalert %}

{% alert note %}
Note that overriding default images is currently not supported in our Xamarin iOS integration.
{% endalert %}

## Customizing the Content Cards Feed

You can create your own Content Cards interface by extending `ABKContentCardsTableViewController` to customize all UI elements and Content Cards behavior. The Content Card cells may also be subclassed and then used programmatically or by introducing a custom Storyboard that registers the new classes. See the [Content Cards sample app](https://github.com/Appboy/appboy-ios-sdk/tree/master/Samples/ContentCards/BrazeContentCardsSampleApp) for a complete example. Alternatively, you can create a completely custom view controller and [subscribe for data updates]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/data_model/). In the latter case, you would need to log all view events, dismissed events, and clicks manually.

### Customizing UI

The following code snippets show an example of how to build custom Content Cards with key-value pairs using the methods provided by the SDK. There are two distinct ways to do this, the dynamic UI method, which allows you to update card UI on a per-card basis, or the static method, which will update the UI across all cards. 

{% tabs local %}
{% tab Dynamic UI %}
Using the Content Card `apply` method, you can reference the card object and pass it the key-value pairs that will be used to update the UI.

{% subtabs global %}
{% subtab Objective-C %}
```objc

```
{% endsubtab %}
{% subtab Swift %}
```swift
override func apply(_ captionedImageCard: ABKCaptionedImageContentCard!) {
  super.apply(captionedImageCard)
     
  applyToBaseView(captionedImageCard)
  applyToCaptionedImageView(captionedImageCard)
}
 
extension ABKBaseContentCardCell {
  var BrazeBackgroundColor: UIColor {
    return .systemBackground
  }
 
  func applyToBaseView(_ card: ABKContentCard) {
    if let backgroundColor = card.extras?[ContentCardKey.backgroundColor.rawValue] as? String,
       let backgroundColorValue = backgroundColor.colorValue() {
      rootView.backgroundColor = backgroundColorValue
    } else {
      rootView.backgroundColor = BrazeBackgroundColor
    }
  }
}
 
extension ABKCaptionedImageContentCardCell {
  var BrazeLabelColor: UIColor {
    return .label
  }  
 
  func applyToCaptionedImageView(_ card: ABKContentCard) {
    if let labelColor = card.extras?[ContentCardKey.labelColor.rawValue] as? String,
       let labelColorValue = labelColor.colorValue() {
      titleLabel.textColor = labelColorValue
      descriptionLabel.textColor = labelColorValue
    } else {
      titleLabel.textColor = BrazeLabelColor
      descriptionLabel.textColor = BrazeLabelColor
    }
  }
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Static UI %}
{% subtabs global %}


{% subtab Objective-C %}
```objc
#import "CustomClassicContentCardCell.h"  
 
@implementation CustomClassicContentCardCell
 
- (void)setUpUI {
  [super setUpUI];
  self.rootView.backgroundColor = [UIColor lightGrayColor];
  self.rootView.layer.borderColor = [UIColor purpleColor].CGColor;
  self.unviewedLineView.backgroundColor = [UIColor redColor];
  self.titleLabel.font = [UIFont italicSystemFontOfSize:20];
}
```
{% endsubtab %}
{% subtab Swift %}
```swift

```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Providing Custom Interfaces

Custom interfaces can be provided by registering custom classes for each desired card type.

{% tabs %}
{% tab Objective-C %}
```objc
- (void)registerTableViewCellClasses {
  [super registerTableViewCellClasses];
 
  // Replace the default class registrations with custom classes for these two types of cards
  [self.tableView registerClass:[CustomCaptionedImageContentCardCell class] forCellReuseIdentifier:@"ABKCaptionedImageContentCardCell"];
  [self.tableView registerClass:[CustomClassicContentCardCell class] forCellReuseIdentifier:@"ABKClassicCardCell"];
}
```
{% endtab %}
{% tab Swift %}
```swift

```
{% endtab %}
{% endtabs %}

### Overriding Populated Content Cards

Content Cards components can be overridden by using the `getContentCards` method along with the `isKindOfClass` method to reference the desired card and push updates.

{% tabs %}
{% tab Objective-C %}
```objc
- (void)populateContentCards {
  NSMutableArray<ABKContentCard *> *cards = [NSMutableArray arrayWithArray:[Appboy.sharedInstance.contentCardsController getContentCards]];
  for (ABKContentCard *card in cards) {
    // Replaces the card description for all Classic content cards
    if ([card isKindOfClass:[ABKClassicContentCard class]]) {
      ((ABKClassicContentCard *)card).cardDescription = @"Custom Feed Override title [classic cards only]!";
    }
  }
  super.cards = cards;
}
```
{% endtab %}
{% tab Swift %}
```swift

```
{% endtab %}
{% endtabs %}

## Handling Clicks Manually

You can manually handle Content Card clicks by implementing the [ABKContentCardsTableViewControllerDelegate](https://appboy.github.io/appboy-ios-sdk/docs/protocol_a_b_k_content_cards_table_view_controller_delegate-p.html) protocol and setting your delegate object as the `delegate` property of the `ABKContentCardsTableViewController`. See the [Content Cards sample app](https://github.com/Appboy/appboy-ios-sdk/tree/master/Samples/ContentCards/BrazeContentCardsSampleApp) for an example. 

{% tabs %}
{% tab Objective-C %}
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
{% tab Swift %}
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
