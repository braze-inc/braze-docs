---
nav_title: Integration
article_title: News Feed Integration for iOS
platform: iOS
page_order: 0
description: "This article covers an overview of the News Feed data model, integrating the News Feed into your iOS application, and a custom view controller integration example."
channel:
  - news feed

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# News Feed integration

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

## News Feed data model

### Getting the data

To access the News Feed data model, subscribe to News Feed update events:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// Subscribe to feed updates
// Note: you should remove the observer where appropriate
[[NSNotificationCenter defaultCenter] addObserver:self
                                         selector:@selector(feedUpdated:)
                                             name:ABKFeedUpdatedNotification
                                           object:nil];
```                                           

```objc
// Called when the feed is refreshed (via `requestFeedRefresh`)
- (void)feedUpdated:(NSNotification *)notification {
  BOOL updateIsSuccessful = [notification.userInfo[ABKFeedUpdatedIsSuccessfulKey] boolValue];
  // check for success
  // get the cards using [[Appboy sharedInstance].feedController getCardsInCategories:ABKCardCategoryAll];
}
```

{% endtab %}
{% tab swift %}

```swift
// Subscribe to feed updates
// Note: you should remove the observer where appropriate
NotificationCenter.default.addObserver(self, selector:
  #selector(feedUpdated),
  name:NSNotification.Name.ABKFeedUpdated, object: nil)
```

```swift
// Called when the feed is refreshed (via `requestFeedRefresh`)
private func feedUpdated(_ notification: Notification) {
  if let updateSuccessful = notification.userInfo?[ABKFeedUpdatedIsSuccessfulKey] as? Bool {
    // check for success
    // get the cards using Appboy.sharedInstance()?.feedController.getCardsInCategories(.all);      
  }
}
```

{% endtab %}
{% endtabs %}

If you want to change the card data after it's been sent by Braze, we recommend storing (deep copy) the card data locally, updating it, and displaying it yourself. The cards are accessible via [`ABKFeedController`](http://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_feed_controller.html).

## News Feed model

Braze has five unique card types: banner image, captioned image, text announcement, and classic. Each type inherits common properties from a base model and has the following additional properties.

### Base card model properties

|Property|Description|
|---|---|
| `idString` | (Read only) The card's ID set by Braze. |
| `viewed` | This property reflects if the card is read or unread by the user. |
| `created` | (Read only) The property is the unix timestamp of the card's creation time from Braze dashboard. |
| `updated` | (Read only) The property is the unix timestamp of the card's latest update time from Braze dashboard. |
| `categories` | The list of categories assigned to the card, cards without a category will be assigned `ABKCardCategoryNoCategory`.<br><br>Available categories:<br>- `ABKCardCategoryNoCategory`<br>- `ABKCardCategoryNews`<br>- `ABKCardCategoryAdvertising`<br>- `ABKCardCategoryAnnouncements`<br>- `ABKCardCategorySocial`<br>- `ABKCardCategoryAll` |
| `extras` | An optional `NSDictionary` of `NSString` values. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Banner image card properties

|Property|Description|
|---|---|
| `image` | (Required) This property is the URL of the card's image. |
| `URL` | (Optional) The URL that will be opened after the card is clicked on. It can be an HTTP(S) URL or a protocol URL. |
| `domain` | (Optional) The link text for the property URL, like @"blog.braze.com". It can be displayed on the card's UI to indicate the action and direction of clicking on the card but is hidden in the default Braze News Feed. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Captioned image card properties

|Property|Description|
|---|---|
| `image` | (Required) This property is the URL of the card's image. |
| `title` | (Required) The title text for the card. |
| `description` (Required) The body text for the card. |
| `URL` | (Optional) The URL that will be opened after the card is clicked on. It can be an HTTP(S) URL or a protocol URL. |
| `domain` | (Optional) The link text for the property URL, like @"blog.braze.com". It can be displayed on the card's UI to indicate the action and direction of clicking on the card. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Text announcement card (captioned image without image) properties

|Property|Description|
|---|---|
| `title` | (Required) The title text for the card. |
| `description` | (Required) The body text for the card. |
| `url` | (Optional) The URL that will be opened after the card is clicked on. It can be an HTTP(S) URL or a protocol URL. |
| `domain` | (Optional) The link text for the property URL, like @"blog.braze.com". It can be displayed on the card's UI to indicate the action and direction of clicking on the card. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Classic card properties

|Property|Description|
|---|---|
| `image` | (Required) This property is the URL of the card's image. |
| `title` | (Optional) The title text for the card. |
| `description` | (Required) The body text for the card. |
| `URL` | (Optional) The URL that will be opened after the card is clicked on. It can be an HTTP(S) URL or a protocol URL. |
| `domain` | (Optional) The link text for the property URL, like @"blog.braze.com". It can be displayed on the card's UI to indicate the action and direction of clicking on the card. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Card methods

|Method|Description|
|---|---|
| `logCardImpression` | Manually log an impression to Braze for a particular card. |
| `logCardClicked` | Manually log a click to Braze for a particular card. The SDK will only log a card click when the card has the `url` property with a valid value. All subclasses of `ABKCard` have the `url` property. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Log feed display

When displaying the News Feed in your own user interface, you can manually record News Feed impressions via `- (void)logFeedDisplayed;`. For example:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] logFeedDisplayed];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.logFeedDisplayed()
```

{% endtab %}
{% endtabs %}

## News Feed view controller integration

Integrating the view controller `ABKNewsFeedViewController` will display the Braze News Feed.

You have a great deal of flexibility in how you choose to display the view controllers. There are different versions of the view controllers to accommodate different navigation structures.

{% alert note %}
The News Feed that is called by the default behavior of an in-app message click will not respect any delegates you set for the News Feed. If you want to respect that, you must [set the delegate on `ABKInAppMessageUIController`]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/in-app_messaging/customization/setting_delegates/) and implement the `ABKInAppMessageUIDelegate` delegate method [`onInAppMessageClicked:`]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/behavior_on_click/#customizing-in-app-message-body-clicks).
{% endalert %}

The News Feed can be integrated with two view controller contexts: navigation or modal.

### Navigation context - ABKFeedViewControllerNavigationContext

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
ABKNewsFeedTableViewController *newsFeed = [[ABKNewsFeedTableViewController alloc] init];
[self.navigationController pushViewController:newsFeed animated:YES];
```

{% endtab %}
{% tab swift %}

```swift
let newsFeed = ABKNewsFeedTableViewController()
self.navigationController?.pushViewController(newsFeed, animated: true)
```

{% endtab %}
{% endtabs %}

To customize the navigation bar's `title`, set the title property of the `ABKNewsFeedTableViewController` instance's `navigationItem`.

### Modal context - ABKFeedViewControllerModalContext

This modal is used present the view controller in a modal view, with a navigation bar on top and a **Done** button on the right side of the bar. To customize the modal's title, set the `title` property of the `ABKNewsFeedTableViewController` instance's `navigationItem`. 

If a delegate **is NOT set**, the **Done** button will dismiss the modal view. If a delegate **is set**, the **Done** button will call the delegate, and the delegate itself will be responsible for dismissing the view.

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
ABKNewsFeedViewController *newsFeed = [[ABKNewsFeedViewController alloc] init];
[self presentViewController:newsFeed animated:YES completion:nil];
```

{% endtab %}
{% tab swift %}

```swift
let newsFeed = ABKNewsFeedViewController()
self.present(newsFeed, animated: true, completion: nil)
```

{% endtab %}
{% endtabs %}

For view controller examples, check out our [News Feed sample app](https://github.com/Appboy/appboy-ios-sdk/tree/master/Samples/NewsFeed/BrazeNewsFeedSample).


