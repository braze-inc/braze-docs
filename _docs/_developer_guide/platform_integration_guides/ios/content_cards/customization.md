---
nav_title: Customization
article_title: Content Card Customization for iOS
platform: iOS
page_order: 2
description: "This article covers customization options for your Content Cards in your iOS application."
channel:
  - Content Cards

---

# Customization

Customizing Content Cards and the feed they are located in must be done during in the integration process. Before customizing, developers should work with their marketing team to determine what customization approach works best for your brand needs. At Braze, we highlight three approaches to customization based on the associated level of effort and flexibility provided: crawl, walk, or run. Learn more about these [customization approaches][1] in our user guide.

It's also important to consider whether you should use a subclassing strategy versus a complete view controller customization. For example, if you subclass the `ABKContentCardsTableViewController`, you can use the `populateContentCards` method ([below](#overriding-populated-content-cards)) to filter and order cards (recommended). However, if you use a complete view controller customization, you have more control over the card behavior—such as displaying in a carousel or adding interactive elements—but you then have to rely on a observer to implement ordering and filtering logic. You must also implement the respective analytics methods to ensure impressions, dismissal events, and clicks are properly logged.

## Overriding default images

{% alert important %}
Integration of `SDWebImage` is required if you plan on using our Braze UI for displaying images within iOS in-app messages, News Feed, or Content Cards.
{% endalert %}

Braze allows clients to replace existing default images with their own custom images. To accomplish this, create a new `png` file with the custom image and add it to the app's image bundle. Then, rename the file with the image's name (see below) to override the default image in our library. Images available for override in Content Cards include:

- Placeholder image: `appboy_cc_noimage_lrg`.
- Pinned icon image: `appboy_cc_icon_pinned`.

Because Content Cards have a maximum size of 2 KB for content you enter in the dashboard (including message text, image URLs, links, and all key-value pairs), make sure to check the size before sending. Exceeding this amount will prevent the card from sending.

{% alert note %}
Be sure to upload the `@2x` and `@3x` versions of the images to accommodate different phone sizes.
{% endalert %}

{% alert note %}
Overriding default images is currently not supported in our Xamarin iOS integration.
{% endalert %}

## Customizing the Content Cards feed

You can create your own Content Cards interface by extending `ABKContentCardsTableViewController` to customize all UI elements and Content Cards behavior. The Content Card cells may also be subclassed and then used programmatically or by introducing a custom Storyboard that registers the new classes. See the [Content Cards sample app](https://github.com/Appboy/appboy-ios-sdk/tree/master/Samples/ContentCards/BrazeContentCardsSampleApp) for a complete example. Alternatively, you can create a completely custom view controller and [subscribe for data updates]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/data_model/). In the latter case, you would need to log all view events, dismissed events, and clicks manually.

### Customizing UI

The following code snippets show how to style and change out-of-the-Box Content Cards to fit your UI needs using methods provided by the SDK. These methods allow you to customize all aspects of the Content Card UI, such as including custom fonts, customized color components, customized text, and more. 

There exist two distinct ways to customize Content Card UI: 
- Dynamic method: update card UI on a per-card basis
- Static method: update the UI across all cards

#### Dynamic UI

The Content Card `applyCard` method can reference the card object and pass it key-value pairs that will be used to update the UI.

{% tabs %}
{% tab Objective-C %}
```objc
- (void)applyCard:(ABKCaptionedImageContentCard *)captionedImageCard {
  [super applyCard:captionedImageCard];    
 
  if ([card.extras objectForKey:ContentCardKeyBackgroundColorValue]) {
    NSString *backgroundColor = [card.extras objectForKey:ContentCardKeyBackgroundColor];
    if ([backgroundColor colorValue]) {
      self.rootView.backgroundColor = [backgroundColor colorValue];
    } else {
      self.rootView.backgroundColor = [UIColor lightGray];
    }
  } else {
    self.rootView.backgroundColor = [UIColor lightGray];
  }  
}
```
{% endtab %}
{% tab Swift %}
```swift
override func apply(_ captionedImageCard: ABKCaptionedImageContentCard!) {
  super.apply(captionedImageCard)         
 
  if let backgroundColor = card.extras?[ContentCardKey.backgroundColor.rawValue] as? String,
     let backgroundColorValue = backgroundColor.colorValue() {
    rootView.backgroundColor = backgroundColorValue
  } else {
    rootView.backgroundColor = .lightGray
  }
}
```
{% endtab %}
{% endtabs %}

#### Static UI

The `setUpUI` method can assign values to the static Content Card components across all cards. 

{% tabs %}
{% tab Objective-C %}
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
{% endtab %}
{% tab Swift %}
```swift
override func setUpUI() {
  super.setUpUI()
     
  rootView.backgroundColor = .lightGray
  rootView.layer.borderColor = UIColor.purple.cgColor
  unviewedLineViewColor = .red
  titleLabel.font = .italicSystemFont(ofSize: 20)
}
```
{% endtab %}
{% endtabs %}

### Providing custom interfaces

Custom interfaces can be provided by registering custom classes for each desired card type. 

![Custom Classes]({% image_buster /assets/img/interface1.png %}){: style="max-width:35%;margin-left:15px;"}
![Custom Classes]({% image_buster /assets/img/interface2.png %}){: style="max-width:25%;margin-left:15px;"}
![Custom Classes]({% image_buster /assets/img/interface3.png %}){: style="max-width:18%;margin-left:15px;"}

Braze provides three Content Card templates (banner, captioned image, and classic). Alternatively, if you would like to provide your own custom interfaces, reference the following code snippets:

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
override func registerTableViewCellClasses() {
  super.registerTableViewCellClasses()
     
  // Replace the default class registrations with custom classes
  tableView.register(CustomCaptionedImageContentCardCell.self, forCellReuseIdentifier: "ABKCaptionedImageContentCardCell")
  tableView.register(CustomBannerContentCardCell.self, forCellReuseIdentifier: "ABKBannerContentCardCell")
  tableView.register(CustomClassicImageContentCardCell.self, forCellReuseIdentifier: "ABKClassicImageCardCell")
  tableView.register(CustomClassicContentCardCell.self, forCellReuseIdentifier: "ABKClassicCardCell")
}
```
{% endtab %}
{% endtabs %}

### Overriding populated Content Cards

Content Cards can be changed programmatically using the `populateContentCards` method.

{% tabs %}
{% tab Objective-C %}
```objc
- (void)populateContentCards {
  NSMutableArray<ABKContentCard *> *cards = [NSMutableArray arrayWithArray:[Appboy.sharedInstance.contentCardsController getContentCards]];
  for (ABKContentCard *card in cards) {
    // Replaces the card description for all Classic Content Cards
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
override func populateContentCards() {
  guard let cards = Appboy.sharedInstance()?.contentCardsController.contentCards else { return }
  for card in cards {
    // Replaces the card description for all Classic Content Cards
    if let classicCard = card as? ABKClassicContentCard {
      classicCard.cardDescription = "Custom Feed Override title [classic cards only]!"
    }
  }
  super.cards = (cards as NSArray).mutableCopy() as? NSMutableArray
}
```
{% endtab %}
{% endtabs %}

## Handling clicks manually

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
    NSLog(@"Manually handling Content Card click with URL %@", url.absoluteString);
    return NO;
  }
  // Let the Braze SDK handle the click action
  return YES;
}

- (void)contentCardTableViewController:(ABKContentCardsTableViewController *)viewController
                    didHandleCardClick:(NSURL *)url {
  NSLog(@"Braze SDK handled Content Card click with URL %@", url.absoluteString);
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
    NSLog("Manually handling Content Card click with URL %@", url.absoluteString)
    return false
  }
  // Let the Braze SDK handle the click action
  return true
}

func contentCardTableViewController(_ viewController: ABKContentCardsTableViewController!,
                                    didHandleCardClick url: URL!) {
  NSLog("Braze SDK handled Content Card click with URL %@", url.absoluteString)
}
```
{% endtab %}
{% endtabs %}

{% alert important %}
If you override the `handleCardClick:` method in `ABKContentCardsTableViewController`, these delegate methods might not be called.
{% endalert %}

## Use case: Carousel view

![Sample news app showing carousel of Content Cards in an article]({% image_buster/assets/img_archive/cc_politer_carousel.png %}){: style="max-width:35%;float:right;margin-left:15px;border:none;"}

This section covers how to implement a multi-card carousel feed where a user can swipe horizontally to view additional featured cards. In order to integrate a carousel view, you'll need to use a fully customized Content Card implementation—the "run" phase of the [crawl, walk, run approach][1].

With this approach, you will not use Braze’s views and default logic, but will instead display the Content Cards in a completely custom manner by using your own views populated with data from the Braze models.

In terms of level of development effort, the key differences between the out-of-the-box implementation and the carousel implementation include:

- Building your own views
- Logging Content Card analytics
- Introducing additional client-side logic to dictate how many and which cards to show in the carousel

### Implementation

#### Step 1: Create a custom view controller

To create the Content Cards carousel, create your own custom view controller (such as `UICollectionViewController`) and [subscribe for data updates]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/data_model/#getting-the-data). Note that you won't be able to extend or subclass Braze's default `ABKContentCardTableViewController`, as it's only able to handle our default Content Card types.

#### Step 2: Implement analytics

When creating a fully custom view controller, Content Card impressions, clicks, and dismissals are not automatically logged. You must implement the respective analytics methods to ensure impressions, dismissal events, and clicks get properly logged back to Braze's dashboard analytics.

For information on the analytics methods, refer to [Card methods]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/data_model/#card-methods). 

{% alert note %}
The same page also details the different properties inherited from our generic Content Card model class, which you may find useful during your view implementation.
{% endalert %}

#### Step 3: Create a Content Card observer

Create a [Content Card observer]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/multiple_feeds/#step-2-set-up-a-content-card-listener) that is responsible for handling the arrival of Content Cards, and implement conditional logic to display a specific number of cards in the carousel at any one time. By default, Content Cards are sorted by created date (newest first), and a user sees all cards they are eligible for.

That said, you could order and apply additional display logic in a variety of ways. For example, you could select the first five Content Card objects from the array, or introduce key-value pairs (the `extras` property in the data model) to build conditional logic around.

If you're implementing a carousel as a secondary Content Cards feed, please refer to [Using multiple Content Card feeds]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/multiple_feeds/) to ensure you sort cards into the correct feed based on key-value pairs.

{% alert important %}
It's important to ensure your marketing and developer teams coordinate on which key-value pairs will be used (e.g, `feed_type = brand_homepage`), as any key-value pairs marketers input into the Braze dashboard must exactly match the key-value pairs which the developers build into the app logic.
{% endalert %}

For iOS-specific developer documentation on the Content Cards class, methods, and attributes, refer to the iOS [ABKContentCard Class Reference](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_content_card.html).

### Considerations

- By using completely custom views, you will not be able to extend or subclass the methods used in `ABKContentCardsController`. Instead, you'll need to integrate the data model methods and properties yourself.
- The logic and implementation of the carousel view is not a default type of Content Card in Braze, and therefore the logic for achieving the use case must be supplied and supported by your development team.
- You will need to implement client-side logic to display a specific number of cards in the carousel at any one time.

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/content_cards/customize/#customization-approaches
