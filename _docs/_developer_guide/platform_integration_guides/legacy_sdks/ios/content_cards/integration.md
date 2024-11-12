---
nav_title: Integration
article_title: Content Card View Controller Integration for iOS
platform: iOS
page_order: 1
description: "This reference article covers the integration steps, data models, and card-specific properties available for your iOS application."
channel:
  - content cards
search_rank: 3
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Content Card integration

## Content Cards data model

The Content Cards data model is available in the iOS SDK.

### Getting the data

To access the Content Cards data model, subscribe to Content Cards update events:

{% tabs %}
{% tab OBJECTIVE-C %}
```objc
// Subscribe to Content Cards updates
// Note: you should remove the observer where appropriate
[[NSNotificationCenter defaultCenter] addObserver:self
                                         selector:@selector(contentCardsUpdated:)
                                             name:ABKContentCardsProcessedNotification
                                           object:nil];
```

```objc
// Called when Content Cards are refreshed (via `requestContentCardsRefresh`)
- (void)contentCardsUpdated:(NSNotification *)notification {
  BOOL updateIsSuccessful = [notification.userInfo[ABKContentCardsProcessedIsSuccessfulKey] boolValue];
  if (updateIsSuccessful) {
    // get the cards using [[Appboy sharedInstance].contentCardsController getContentCards];
  }
}
```
{% endtab %}
{% tab swift %}
```swift
// Subscribe to content card updates
// Note: you should remove the observer where appropriate
NotificationCenter.default.addObserver(self, selector:
  #selector(contentCardsUpdated),
  name:NSNotification.Name.ABKContentCardsProcessed, object: nil)
```

```swift
// Called when the Content Cards are refreshed (via `requestContentCardsRefresh`)
@objc private func contentCardsUpdated(_ notification: Notification) {
  if let updateIsSuccessful = notification.userInfo?[ABKContentCardsProcessedIsSuccessfulKey] as? Bool {
    if (updateIsSuccessful) {
      // get the cards using Appboy.sharedInstance()?.contentCardsController.contentCards
    }
  }
}
```
{% endtab %}
{% endtabs %}

If you want to change the card data after it's been sent by Braze, we recommend storing a deep copy of the card data locally, updating the data, and displaying it yourself. The cards are accessible via [`ABKContentCardsController`](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_content_cards_controller.html).

## Content Card model

Braze offers three Content Card types: banner, captioned image, and classic. Each type inherits common properties from a base `ABKContentCard` class and has the following additional properties.

### Base Content Card model properties - ABKContentCard

|Property|Description|
|---|---|
|`idString` | (Read only) The card's ID set by Braze. |
| `viewed` | This property reflects whether the user viewed the card or not.|
| `created` | (Read only) This property is the unix timestamp of the card's creation time from Braze. |
| `expiresAt` | (Read only) This property is the unix timestamp of the card's expiration time.|
| `dismissible` | This property reflects if the user can dismiss the card.|
| `pinned` | This property reflects if the card was set up as "pinned" in the dashboard.|
| `dismissed` | This property reflects if the user has dismissed the card.|
| `url` | The URL that will be opened after the card is clicked on. It can be an HTTP(s) URL or a protocol URL.|
| `openURLInWebView` | This property determines whether the URL will be opened within the app or in an external web browser.|
| `extras`| An optional `NSDictionary` of `NSString` values.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Banner Content Card properties - ABKBannerContentCard

|Property|Description|
|---|---|
| `image` | This property is the URL of the card's image.|
| `imageAspectRatio` | This property is the aspect ratio of the card's image and serves as a hint before image loading completes. Note that the property may not be supplied in certain circumstances. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Captioned image Content Card properties - ABKCaptionedImageCard

|Property|Description|
|---|---|
| `image` | This property is the URL of the card's image.|
| `imageAspectRatio` | This property is the aspect ratio of the card's image.|
| `title` | The title text for the card.|
| `cardDescription` | The body text for the card.|
| `domain` | The link text for the property URL, like @"blog.braze.com". It can be displayed on the card's UI to indicate the action/direction of clicking on the card.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Classic Content Card properties - ABKClassicContentCard

|Property|Description|
|---|---|
| `image` | (Optional) This property is the URL of the card's image.|
| `title` | The title text for the card. |
| `cardDescription` | The body text for the card. |
| `domain` | The link text for the property URL, like @"blog.braze.com". It can be displayed on the card's UI to indicate the action and direction of clicking on the card. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Card methods

|Method|Description|
|---|---|
| `logContentCardImpression` | Manually log an impression to Braze for a particular card. |
| `logContentCardClicked` | Manually log a click to Braze for a particular card. The SDK will only log a card click when the card has the `url` property with a valid value. |
| `logContentCardDismissed` | Manually log a dismissal to Braze for a particular card. The SDK will only log a card dismissal if the card's `dismissed` property is not already set to `true`. |
| `isControlCard` | Determine if a card is the Control card for an A/B test. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

For more details, refer to the [class reference documentation](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_content_card.html)

## Content Cards view controller integration

Content Cards can be integrated with two view controller contexts: navigation or modal.

### Navigation context

Example of pushing a `ABKContentCardsTableViewController` instance into a navigation controller:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
ABKContentCardsTableViewController *contentCards = [[ABKContentCardsTableViewController alloc] init];
contentCards.title = @"Content Cards Title";
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

### Modal context

This modal is used to present the view controller in a modal view, with a navigation bar on top and a **Done** button on the side of the bar.

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
ABKContentCardsViewController *contentCards = [[ABKContentCardsViewController alloc] init];
contentCards.contentCardsViewController.title = @"Content Cards Title";
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

For view controller examples, check out our [Content Cards sample app](https://github.com/Appboy/appboy-ios-sdk/tree/master/Samples/ContentCards/BrazeContentCardsSampleApp).

{% alert note %}
To customize the header, set the title property of the `navigationItem` belonging to the `ABKContentCardsTableViewController` instance embedded in the parent `ABKContentCardsViewController` instance.
{% endalert %}
