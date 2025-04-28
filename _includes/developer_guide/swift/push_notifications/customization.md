{% multi_lang_include developer_guide/prerequisites/swift.md %} You'll also need to [set up push notifications]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift).

## Customizing action buttons {#push-action-buttons-integration}

The Braze Swift SDK provides URL handling support for push action buttons. There are four sets of default push action buttons for Braze default push categories: `Accept/Decline`, `Yes/No`, `Confirm/Cancel`, and `More`.

![A GIF of a push message being pulled down to display two customizable action buttons.]({% image_buster /assets/img_archive/iOS8Action.gif %}){: style="max-width:60%"}

### Manually registering action buttons

{% alert important %}
Manually registering push action buttons are not recommended.
{% endalert %}

If you [set up push notifications]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) using the `configuration.push.automation` configuration option, Braze automatically registers the action buttons for the default push categories and handles the push action button click analytics and URL routing.

However, you can choose to manually register push action buttons instead.

#### Step 1: Adding Braze default push categories {#registering}

Use the following code to register for the default push categories when you [register for push]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-4-register-push-tokens-with-braze):

{% tabs %}
{% tab swift %}
a
```swift
UNUserNotificationCenter.current().setNotificationCategories(Braze.Notifications.categories)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[[UNUserNotificationCenter currentNotificationCenter] setNotificationCategories:BRZNotifications.categories];
```

{% endtab %}
{% endtabs %}

{% alert note %}
Clicking on push action buttons with background activation mode will only dismiss the notification and not open the app. The next time the user opens the app, the button click analytics for these actions will be flushed to the server.
{% endalert %}

#### Step 2: Enable interactive push handling {#enable-push-handling}

To enable our push action button handling, including click analytics and URL routing, add the following code to your app's `didReceive(_:completionHandler:)` delegate method:

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.notifications.handleUserNotification(response: response, withCompletionHandler: completionHandler)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[AppDelegate.braze.notifications handleUserNotificationWithResponse:response
                                              withCompletionHandler:completionHandler];
```

{% endtab %}
{% endtabs %}

If you use the `UNNotification` framework and have implemented the Braze [notification methods]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-5-enable-push-handling), you should already have this method integrated. 

## Customizing push categories {#customizing-push-categories}

In addition to providing a set of default push categories, Braze supports custom notification categories and actions. After you register categories in your application, you can use the Braze dashboard to send these custom notification categories to your users.

Here's an example that leverages the `LIKE_CATEGORY` displayed on the device:

![A push message displaying two push action buttons "unlike" and "like".]({% image_buster /assets/img_archive/push_example_category.png %})

### Step 1: Register a category

To register a category in your app, use a similar approach to the following:

{% tabs %}
{% tab swift %}

```swift
Braze.Notifications.categories.insert(
  .init(identifier: "LIKE_CATEGORY",
        actions: [
          .init(identifier: "LIKE_IDENTIFIER", title: "Like", options: [.foreground]),
          .init(identifier: "UNLIKE_IDENTIFIER", title: "Unlike", options: [.foreground])
        ],
        intentIdentifiers: []
       )
)
UNUserNotificationCenter.current().setNotificationCategories(Braze.Notifications.categories)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
NSMutableSet<UNNotificationCategory *> *categories = [BRZNotifications.categories mutableCopy];

UNNotificationAction *likeAction = [UNNotificationAction actionWithIdentifier:@"LIKE_IDENTIFIER"
                                                                        title:@"Like"
                                                                      options:UNNotificationActionOptionForeground];

UNNotificationAction *unlikeAction = [UNNotificationAction actionWithIdentifier:@"UNLIKE_IDENTIFIER"
                                                                          title:@"Unlike"
                                                                        options:UNNotificationActionOptionForeground];

UNNotificationCategory *likeCategory = [UNNotificationCategory categoryWithIdentifier:@"LIKE_CATEGORY"
                                                                              actions:@[likeAction, unlikeAction]
                                                                    intentIdentifiers:@[]
                                                                              options:UNNotificationCategoryOptionNone];

[categories addObject:likeCategory];
[UNUserNotificationCenter.currentNotificationCenter setNotificationCategories:categories];
```

{% endtab %}
{% endtabs %}

{% alert note %}
When you create a `UNNotificationAction`, you can specify a list of action options. For example, `UNNotificationActionOptions.foreground` let's your users open your app after tapping the action button. This is necessary for navigational on-click behaviors, such as "Open App" and "Deep Link into Application". For more information, see [`UNNotificationActionOptions`](https://developer.apple.com/documentation/usernotifications/unnotificationactionoptions).
{% endalert %}

### Step 2: Select your categories

After you register a category, use the Braze dashboard to send notifications of that type to users.

{% alert tip %}
You only need to define custom notification categories for action buttons with _special actions_, such as deep linking into your app or opening a URL. You do not need to define them for action buttons that only dismiss a notification.
{% endalert %}

1. In the Braze dashboard, select **Messaging** > **Push Notifications**, then choose your iOS [push campaign]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message).
2. Under **Compose push notification**, turn on **Action Buttons**.
3. In the **iOS Notification Category** dropdown, select **Enter pre-registered custom iOS Category**.
4. Finally, enter one of the categories you created earlier. The following example, uses the custom category: `LIKE_CATEGORY`.

![The push notification campaign dashboard with the setup for custom categories.]({% image_buster /assets/img_archive/ios-notification-category.png %})

## Customizing badges

Badges are small icons that are ideal for getting a user's attention. You can specify a badge count in the [**Settings**]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=swift#swift_settings) tab when you compose a push notification using the Braze dashboard. You may also update your badge count manually through your application's [`applicationIconBadgeNumber`](https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIApplication_Class/index.html#//apple_ref/occ/instp/UIApplication/applicationIconBadgeNumber) property or the [remote notification payload](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CreatingtheNotificationPayload.html#//apple_ref/doc/uid/TP40008194-CH10-SW1). 

Braze will automatically clear the badge count when a Braze notification is received while the app is in the foreground. Manually setting the badge number to 0 will also clear notifications in the notification center. 

If you do not have a plan for clearing badges as part of normal app operation or by sending pushes that clear the badge, you should clear the badge when the app becomes active by adding the following code to your app's `applicationDidBecomeActive:` delegate method:

{% tabs %}
{% tab swift %}

```swift
// For iOS 16.0+
let center = UNUserNotificationCenter.current()
do {
  try await center.setBadgeCount(0)
} catch {
  // Handle errors
}

// Prior to iOS 16. Deprecated in iOS 17+.
UIApplication.shared.applicationIconBadgeNumber = 0
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
// For iOS 16.0+
UNUserNotificationCenter *center = [UNUserNotificationCenter currentNotificationCenter];
[center setBadgeCount:0 withCompletionHandler:^(NSError * _Nullable error) {
    if (error != nil) {
        // Handle errors
    }
}];

// Prior to iOS 16. Deprecated in iOS 17+.
[UIApplication sharedApplication].applicationIconBadgeNumber = 0;
```

{% endtab %}
{% endtabs %}

## Customizing sounds

### Step 1: Host the sound in your app

Custom push notification sounds must be hosted locally within the main bundle of your app. The following audio data formats are accepted:

- Linear PCM
- MA4
- µLaw
- aLaw

You can package the audio data in an AIFF, WAV, or CAF file. In Xcode, add the sound file to your project as a non-localized resource of the application bundle.

{% alert note %}
Custom sounds must be under 30 seconds when played. If a custom sound is over that limit, the default system sound is played instead.
{% endalert %}

#### Converting sound files

You can use the afconvert tool to convert sounds. For example, to convert the 16-bit linear PCM system sound Submarine.aiff to IMA4 audio in a CAF file, use the following command in the terminal:

```bash
afconvert /System/Library/Sounds/Submarine.aiff ~/Desktop/sub.caf -d ima4 -f caff -v
```

{% alert tip %}
You can inspect a sound to determine its data format by opening it in QuickTime Player and choosing **Show Movie Inspector** from the **Movie** menu. 
{% endalert %}

### Step 2: Provide a protocol URL for the sound

You must specify a protocol URL that directs to the location of the sound file in your app. There are two methods for doing this:

* Use the `sound` parameter of the [Apple push object]({{site.baseurl}}/api/objects_filters/messaging/apple_object#apple-push-object) to pass the URL to Braze.
* Specify the URL in the dashboard. In the [push composer]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#step-3-select-notification-type-ios-and-android), select **Settings** and enter the protocol URL in the **Sound** field. 

![The push composer in the Braze dashboard]({% image_buster /assets/img_archive/sound_push_ios.png %})

If the specified sound file doesn't exist or the keyword "default" is entered, Braze will use the default device alert sound. Aside from our dashboard, sound can also be configured via our [messaging API][12].

See the Apple Developer Documentation regarding [preparing custom alert sounds](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/SupportingNotificationsinYourApp.html) for additional information.

## Settings

When creating a push campaign through the dashboard, click the **Settings** tab on the **Compose** step to view the advanced settings available.

![]({% image_buster /assets/img_archive/ios_advanced_settings.png %})

### Key-value pairs

Braze allows you to send custom-defined string key-value pairs, known as `extras`, along with a push notification to your application. Extras can be defined via the dashboard or API and will be available as key-value pairs within the `notification` dictionary passed to your push delegate implementations.

### Alert options

Select the **Alert Options** checkbox to see a dropdown of key-values available to adjust how the notification appears on devices.

### Adding content-available flag

Check the **Add Content-Available Flag** checkbox to instruct devices to download new content in the background. Most commonly, this can be checked if you are interested in sending [silent notifications]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift).

### Adding mutable-content flag

Check the **Add Mutable-Content Flag** checkbox to enable advanced receiver customization. This flag will automatically be sent when composing a [rich notification]({{site.baseurl}}/developer_guide/push_notifications/rich/?sdktab=swift), regardless of the value of this checkbox.

### Collapse ID

Specify a collapse ID to coalesce similar notifications. If you send multiple notifications with the same collapse ID, the device will only show the most recently received notification. Refer to Apple's documentation on [coalesced notifications](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1).

### Expiry

Checking the **Expiry** checkbox will allow setting an expiration time for your message. Should a user's device lose connectivity, Braze will continue to try and send the message until the specified time. If this is not set, the platform will default to an expiration of 30 days. Note that push notifications that expire before delivery are not considered failed and will not be recorded as a bounce.
