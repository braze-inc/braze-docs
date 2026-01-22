---
nav_title: Customize feed
article_title: Customizing Content Card Feed for iOS
platform: iOS
page_order: 2
description: "This article covers Content Card feed customization options in your iOS application."
channel:
  - content cards
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Customize the Content Cards feed

You can create your own Content Cards interface by extending `ABKContentCardsTableViewController` to customize all UI elements and Content Cards behavior. The Content Card cells may also be subclassed and then used programmatically or by introducing a custom storyboard that registers the new classes. Check out the Content Cards [sample app](https://github.com/Appboy/appboy-ios-sdk/tree/master/Samples/ContentCards/BrazeContentCardsSampleApp) for a complete example. 

It's also important to consider whether you should use a subclassing strategy versus a completely custom view controller and [subscribe for data updates]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/content_cards/integration/). For example, if you subclass the `ABKContentCardsTableViewController`, you can use the [`populateContentCards` method](#overriding-populated-content-cards) to filter and order cards (recommended). However, if you use a complete view controller customization, you have more control over the card behavior—such as displaying in a carousel or adding interactive elements—but you then have to rely on an observer to implement ordering and filtering logic. You must also implement the respective analytics methods to properly log impressions, dismissal events, and clicks.

## Customizing UI

The following code snippets show how to style and change Content Cards to fit your UI needs using methods provided by the SDK. These methods allow you to customize all aspects of the Content Card UI, including custom fonts, customized color components, customized text, and more. 

There exist two distinct ways to customize Content Card UI: 
- Dynamic method: update card UI on a per-card basis
- Static method: update the UI across all cards

### Dynamic UI

The Content Card `applyCard` method can reference the card object and pass it key-value pairs that will be used to update the UI:

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

### Static UI

The `setUpUI` method can assign values to the static Content Card components across all cards:

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

## Providing custom interfaces

Custom interfaces can be provided by registering custom classes for each desired card type. 

![A banner Content Card. A banner Content Card shows an image to the right of the banner with the text "Thanks for downloading Braze Demo!".]({% image_buster /assets/img/interface1.png %}){: style="max-width:35%;margin-left:15px;"}
![A captioned image Content Card. A captioned Content Card shows a Braze image with the caption overlaid across the bottom "Thanks for downloading Braze Demo!". ]({% image_buster /assets/img/interface2.png %}){: style="max-width:25%;margin-left:15px;"}
![A classic Content Card. A classic Content Card shows an image in the center of the card with the words "Thanks for downloading Braze Demo" underneath.]({% image_buster /assets/img/interface3.png %}){: style="max-width:18%;margin-left:15px;"}

Braze provides three Content Card templates (banner, captioned image, and classic). Alternatively, if you want to provide your own custom interfaces, reference the following code snippets:

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

## Overriding populated Content Cards

Content Cards can be changed programmatically using the `populateContentCards` method:

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