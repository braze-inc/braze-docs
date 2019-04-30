---
nav_title: Content Cards for iOS
permalink: /content_cards_ios/

---
# Content Cards for iOS

Content Cards are Braze’s new messaging channel which will allow you to create individual messages that appear in a user’s message inbox. This feature is set to, in the future, replace the legacy feature _News Feed channel_, as it provides superior behavior and functionality.

With Content Cards, you can send a highly targeted, dynamic stream of rich content to your customers right within the apps they love, without interrupting their experience. In addition, Content Cards support more personalized features, including card pinning, card dismissal, API-based delivery, custom card expiration times, card [analytics]({{ site.baseurl }}/content_cards/#content-cards-analytics), and easy coordination with push notifications.

## Example Content Card


![Content Card Example][1]


## Content Cards View Controller Integration

Content Cards can be integrated with two view controller contexts: Navigation or Modal.

### Navigation Context

Set the instance's title and navigation items before pushing it into a navigation controller:

```objc
ABKContentCardsTableViewController *contentCards = [ABKContentCardsTableViewController getNavigationFeedViewController];
[self.navigationController pushViewController:contentCards animated:YES];
```

### Modal Context

This modal is used to present the view controller in a modal view, with a navigation bar on top and a Done button on the right side of the bar.

Set the modal's title via the `navigationBarTitle` property:

```objc
ABKContentCardsViewController *contentCards = [[ABKContentCardsViewController alloc] init];
[self.navigationController presentViewController:contentCards animated:YES completion:nil];
```
For examples of these view controllers, check out the [Stopwatch Sample Project](https://github.com/Appboy/appboy-ios-sdk/tree/master/Example/Stopwatch).

## Requesting Unread Content Card Counts: Badges

If you would like to display the number of unread content cards your user has, we suggest you request a card count and represent it with a Badge. Badges are a great way to call attention to new content awaiting your users in the Content Cards. If you'd like to add a badge to your Content Cards, the Braze SDK provides methods to query the following:

- Unviewed Content Cards for the current user
- Total Viewable Content Cards for the current user

The method declarations in [ABKContentCardsController](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_content_cards_controller.html) below describe this in detail:

```
/*!
 * This method returns the number of currently active content cards which have not been viewed.
 * A "view" happens when a card becomes visible in the Content Cards view.  This differentiates
 * between cards which are off-screen in the scrolling view, and those which
 * are on-screen; when a card scrolls onto the screen, it's counted as viewed.
 *
 * Cards are counted as viewed only once -- if a card scrolls off the screen and
 * back on, it's not re-counted.
 *
 * Cards are counted only once even if they appear in multiple Content Cards views or across multiple devices.
 */
- (NSInteger)unviewedContentCardCount;
/*!
 * This method returns the total number of currently active content cards. Cards are
 * counted only once even if they appear in multiple Content Cards views.
 */
- (NSInteger)contentCardCount;
```


### Displaying Number of Unviewed Content Cards on App Badge Count

In addition to serving as push notification reminders for an app, Badges can also be utilized to denote unviewed items in the user's Content Cards feed. Updating the badge count based off unviewed Content Cards updates can be a valuable tool in attracting users back to your app and increasing sessions.

This method records the badge count once the app is closed and the user's session ends:

```objc
(void)applicationDidEnterBackground:(UIApplication *)application
```

Within the above method, implement the following code which actively updates the badge count while the user views cards during a given session:

```objc
[UIApplication sharedApplication].applicationIconBadgeNumber = [[Appboy sharedInstance].contentCardsController unviewedContentCardCount];
```

For more information see the [`Appboy.h` header file](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/headers/AppboyKitLibrary/Appboy.h).


## Refreshing Content Cards

You can manually request Braze to refresh the user's Content Cards in `Appboy.h` using `- (void)requestContentCardsRefresh;`. For example:

```objc
[[Appboy sharedInstance] requestContentCardsRefresh];
```

For more information see the [`Appboy.h` header file](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/headers/AppboyKitLibrary/Appboy.h).


## Customizing the Content Cards Feed

You can create your own Content Cards interface by extending `ABKContentCardsTableViewController`. You can customize all UI elements and Content Cards behavior in this way. Or you can create a completely custom view controller and subscribe for data updates. In this case you would need to log all view and dismissed events and clicks manually.


### Disabling the Unviewed Indicator

You can choose to disable the blue line at the bottom of the cards which indicates whether or not the card has been viewed by setting the `disableUnviewedIndicator` property in `ABKContentCardsTableViewController` to YES.

## Content Cards Data Model
The Content Cards data model is available in the iOS SDK.

### Getting the Data

To access the Content Cards data model, subscribe to Content Cards update events:

{% tabs %}
{% tab OBJECTIVE-C %}
```objc
// Subscribe to content cards updates
// Note: you should remove the observer where appropriate
[[NSNotificationCenter defaultCenter] addObserver:self
                                         selector:@selector(contentCardsUpdated:)
                                             name:ABKContentCardsProcessedNotification
                                           object:nil];
```

```objc
// Called when content cards are refreshed (via `requestContentCardsRefresh`)
- (void)contentCardsUpdated:(NSNotification *)notification {
  BOOL updateIsSuccessful = [notification.userInfo[ABKContentCardsProcessedIsSuccessfulKey] boolValue];
  // check for success
  // get the cards using [[Appboy sharedInstance].contentCardsController getContentCards];
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
// Called when the content cards are refreshed (via `requestContentCardsRefresh`)
private func contentCardsUpdated(_ notification: Notification) {
  if let updateSuccessful = notification.userInfo?[ABKContentCardsProcessedIsSuccessfulKey] as? Bool {
    // check for success
    // get the cards using Appboy.sharedInstance()?.contentCardsController.getContentCards();
  }
}
```
{% endtab %}
{% endtabs %}

If you want to change the card data after it's been sent by Braze, we recommend storing (deep copy) the card data locally, updating the data and displaying yourself. The cards are accessible via [ABKContentCardsController].

### Base Card Model

Braze has three unique card types that share a base model. Each type of card also has additional properties that are specific to each card which are listed below.

#### Base Content Card Model Properties

|Model|Description|
|---|---|
|`idString` | (read only) The card's ID set by Braze. |
| `viewed` | This property reflects if the card is viewed or not viewed by the user|
| `created` | (read only) This property is the unix timestamp of the card's creation time from Braze. |
| `expiresAt` | (read only) This property is the unix timestamp of the card's expiration time.|
| `dismissible` | This property reflects if the card can be dismissed by the user.|
| `pinned` | This property reflects if the card has been pinned by the user.|
| `dismissed` | This property reflects if the card has been dismissed by the user.|
| `url` | The URL that will be opened after the card is clicked on. It can be a http(s) URL or a protocol URL.|
| `openURLInWebView` | This property determines whether the URL will be opened within the app or in an external web browser.|
| `extras`| An optional NSDictionary of NSString values.|

#### Banner Content Card Properties

|Model|Description|
|---|---|
| `image` | This property is the URL of the card's image.|
| `imageAspectRatio` | This property is the aspect ratio of the card's image.|

#### Captioned Image Content Card Properties

|Model|Description|
|---|---|
| `image` | This property is the URL of the card's image.|
| `imageAspectRatio` | This property is the aspect ratio of the card's image.|
| `title` | The title text for the card.|
| `cardDescription` | The body text for the card.|
| `domain` | The link text for the property URL, like @"blog.braze.com". It can be displayed on the card's UI to indicate the action/direction of clicking on the card.|

#### Classic Content Card Properties

|Model|Description|
|---|---|
| `image` | (optional) This property is the URL of the card's image.|
| `title` | The title text for the card. |
| `cardDescription` | The body text for the card. |
| `domain` | The link text for the property url, like @"blog.braze.com". It can be displayed on the card's UI to indicate the action/direction of clicking on the card. |

## Card Methods

|Method|Description|
|---|---|
| `logContentCardImpression` | Manually log an impression to Braze for a particular card. |
| `logContentCardClicked` | Manually log a click to Braze for a particular card. The SDK will only log a card click when the card has the `url` property with a valid value. |
| `logContentCardDismissed` | Manually log a dismissal to Braze for a particular card.|

## Log Content Cards Display

When displaying the Content Cards in your own user interface, you can manually record Content Cards impressions via `- (void)logContentCardsDisplayed;`. For example:

```objc
[[Appboy sharedInstance] logContentCardsDisplayed];
```

[1]:{% image_buster /assets/img_archive/contentcard.png %}
