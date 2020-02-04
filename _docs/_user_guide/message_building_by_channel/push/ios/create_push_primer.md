---
nav_title: "Create a Push Primer Campaign"
page_order: 5
page_type: tutorial
description: "This walkthrough will show you how to get your users qualified and ready to receive your push messages."

channel:
  - Push
tool:
  - Docs
  - Dashboard
  - Campaigns
---

#include that these messages can be redelivered

# Create a Push Primer Campaign

> This article will walk you through setting up and sending a Push Primer campaign to new or non-push enabled users. <br><br> Push Primer campaigns encourage your users to enable push on their device for your app. Getting permission from users to send messages directly to their device can be complex, but our guides can help!

Push Primer campaigns are useful because they address the issue of the dreaded iOS notification prompt that user recieve upon opening any new iOS application. These prompts are disruptive and uninformative, with users likely choosing to opt out of push notifications. This prompt is only ever shown once. Once those notifications are turned off, theres very little we can do to get users to turn them back on. This becomes a problem when we want to use our Push Channel for marketing, but not many users are push enabled. 

To address this, Braze offers steps on how to set up Push Primers Campaigns. Push Primers allow you to hold off on delivering that initial disruptive push message, letting you decide when and how you want to prompt your users for a push opt-in. These Push Primers can provide users valuable information on why notifications for your application are important.

For a user to qualify to receive your Push Messages, they must enable Push at the app-level _and_ the device-level. Please note that these levels translate differently for iOS and Android. You can learn more about them here:
- [Android Push Enabled]({{ site.baseurl }}/)
- [iOS Push Enabled]({{ site.baseurl }}/)

{% alert note %}
__Should I be using Push Primers?__ Depends on your iOS version.<br><br>
- __iOS 12__: With the iOS 12 update adding provisional authorization, allowing this inital push prompt to be delivered silently to your notification center, some may find Push Primers not needed, other may and choose to still use Push Primers. We recommend meeting with your Customer Success Manager to discuss if this is the right move.
- __iOS 11 and Later__: Because these iOS version only allow foreground Push, those intrusive iOS Push messages will still get sent, in turn costing you marketablility to those users. We strongly suggest setting up Push Primers for these verisons. 
{% endalert %}

## Step 1: Select you Channel of Choice

From the Campaigns pane within the Dashboard, select In-App Messaging as the messaging channel under Create Campaign.

![push_primer][push_primer1]{: height="100px"}{: float:right :}

## Step 2: Set Up Initial Campaign Options

Once you have a blank In-App Messaging campaign to work on, you must name your campaign, select where you would like your Push Primer campaign to send to, select the message type, and pick the layout type (text and image or image only). For your basic Push Primer campaign message type, we suggest either a full screen or modal message. 

## Step 3: Customize your Message

![push_primer][push_primer2]

After you have chosen how you want your push primer to look, you can customize your message content and add buttons.

Remember that a push primer is supposed to prime the user to turn on push notifications. In your message body, we suggest including the reason they should have push notifications turned on. 

Here are some example Push Primer Messages:

![push_primer_example_1][push_primer3]{: height="300px"} ![push_primer_example_2][push_primer4]{: height="300px"} ![push_primer_example_3][push_primer5]{: height="300px"}

To Add buttons, you will find a Button1 text box and Button2 text box. Here you can choose the text that will show on these buttons. We recommend "Turn on Notifications" and "Close" as starter buttons, but there are many different button prompts you could assign. In later steps, we will be assigning these buttons to certain actions. 

If you would like even further customization options, you can also set the message type to Custom code, and provide the HTML.

(examples)

## Step 4: Setting up the Back End - Assembling a functional push primer message:

Now you have your Push Primer message made, with all the settings you want. But as of now, there are quite a few more steps to make this in-app message a true Push Primer message. Because Push Primer Campaigns are not an out-of-the-box feature, your developers must set up the backend. We have included the code snippets required below.

### Push Primer Integration

{% tabs %}
{% tab OBJECTIVE-C %}

Add the following line of code to your `AppDelegate.m` file instead of the standard integration:

```objc
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
...
if (@available(iOS 10.0, *)) {
    UNUserNotificationCenter *center = [UNUserNotificationCenter currentNotificationCenter];
    [center getNotificationSettingsWithCompletionHandler:^(UNNotificationSettings * _Nonnull settings) {
      if (settings.authorizationStatus != UNAuthorizationStatusNotDetermined) {
        // authorization has already been requested, need to follow usual steps
        [center requestAuthorizationWithOptions:(UNAuthorizationOptionAlert | UNAuthorizationOptionSound | UNAuthorizationOptionBadge) completionHandler:^(BOOL granted, NSError * _Nullable error) {
          [[Appboy sharedInstance] pushAuthorizationFromUserNotificationCenter:granted];
        }];
        center.delegate = self;
        [center setNotificationCategories:[ABKPushUtils getAppboyUNNotificationCategorySet]];
        [[UIApplication sharedApplication] registerForRemoteNotifications];
      }
    }];
  } else {
    UIApplication *sharedApplication = [UIApplication sharedApplication];
    UIUserNotificationSettings *notificationSettings = [sharedApplication currentUserNotificationSettings];
    if (notificationSettings.types) {
      UIUserNotificationSettings *settings = [UIUserNotificationSettings settingsForTypes:(UIUserNotificationTypeBadge | UIUserNotificationTypeAlert | UIUserNotificationTypeSound) categories:[ABKPushUtils getAppboyUIUserNotificationCategorySet]];
      [sharedApplication registerUserNotificationSettings:settings];
      [sharedApplication registerForRemoteNotifications];
    }
  }
```
{% endtab %}
{% tab swift %}
```swift
if #available(iOS 10, *) {
  let center = UNUserNotificationCenter.current()
  center.getNotificationSettings(completionHandler: { (settings) in
    if settings.authorizationStatus != .notDetermined {
      // authorization has already been requested, need to follow usual steps
      center.requestAuthorization(options: [.alert, .sound, .badge]) { (granted, error) in
      Appboy.sharedInstance()?.pushAuthorization(fromUserNotificationCenter: granted)
      }
      center.delegate = self as? UNUserNotificationCenterDelegate
      center.setNotificationCategories(ABKPushUtils.getAppboyUNNotificationCategorySet())
      UIApplication.shared.registerForRemoteNotifications()
    }
  })
} else {
  let notificationSettiings = UIApplication.shared.currentUserNotificationSettings
  if notificationSettiings?.types != nil {
    let setting = UIUserNotificationSettings(types: [.alert, .badge, .sound], categories:nil)
    UIApplication.shared.registerUserNotificationSettings(setting)
    UIApplication.shared.registerForRemoteNotifications()
  }
}
```
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab OBJECTIVE-C %}
Add the following line of code to your `AppDelegate.m` in addition to the one above.

Checks if a custom event needs to be fired.
```objc
if (@available(iOS 10.0, *)) {
    UNUserNotificationCenter *center = [UNUserNotificationCenter currentNotificationCenter];
    [center getNotificationSettingsWithCompletionHandler:^(UNNotificationSettings * _Nonnull settings) {
      if (settings.authorizationStatus == UNAuthorizationStatusNotDetermined) {
        // ...
        // fire custom event
        // ...
      }
    }];
  } else {
    UIUserNotificationSettings *notificationSettings = [[UIApplication sharedApplication] currentUserNotificationSettings];
    if (!notificationSettings.types) {
        // …
        // fire custom event
        // ...
    }
  }
```
{% endtab %}
{% tab swift %}
```swift
if #available(iOS 10, *) {
  let center = UNUserNotificationCenter.current()
  center.getNotificationSettings(completionHandler: { (settings) in
    if settings.authorizationStatus == .notDetermined {
      // ...
      // fire custom event
      // ...
    }
  })
} else {
let notificationSettiings = UIApplication.shared.currentUserNotificationSettings
  if notificationSettiings?.types != nil {
    // ...
    // fire custom event
    // ...
```
}
}
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab OBJECTIVE-C %}
Deep Link Handler
For more information on deep linking check out our [documentation][].
```objc
  // ...
  // check that this deep link relates to the push prompt
  // ...
  if (@available(iOS 10.0, *)) {
    UNUserNotificationCenter *center = [UNUserNotificationCenter currentNotificationCenter];
    [center requestAuthorizationWithOptions:(UNAuthorizationOptionAlert | UNAuthorizationOptionSound | UNAuthorizationOptionBadge) completionHandler:^(BOOL granted, NSError * _Nullable error) {
      [[Appboy sharedInstance] pushAuthorizationFromUserNotificationCenter:granted];
    }];
    center.delegate = self;
    [center setNotificationCategories:[ABKPushUtils getAppboyUNNotificationCategorySet]];
    [[UIApplication sharedApplication] registerForRemoteNotifications];
  } else {
    UIUserNotificationSettings *settings = [UIUserNotificationSettings settingsForTypes:(UIUserNotificationTypeBadge | UIUserNotificationTypeAlert | UIUserNotificationTypeSound) categories:[ABKPushUtils getAppboyUIUserNotificationCategorySet]];
      UIApplication *sharedApplication = [UIApplication sharedApplication];
      [sharedApplication registerUserNotificationSettings:settings];
      [sharedApplication registerForRemoteNotifications];
  }
```
{% endtab %}
{% tab swift %}
```swift
  // ...
  // check that this deep link relates to the push prompt
  // ...
  if #available(iOS 10, *) {
    let center = UNUserNotificationCenter.current()
    center.delegate = self as? UNUserNotificationCenterDelegate
    center.requestAuthorization(options: [.alert, .sound, .badge]) { (granted, error) in
    Appboy.sharedInstance()?.pushAuthorization(fromUserNotificationCenter: granted)
  }
  UIApplication.shared.registerForRemoteNotifications()
  } else {
    let setting = UIUserNotificationSettings(types: [.alert, .badge, .sound], categories:nil)
    UIApplication.shared.registerUserNotificationSettings(setting)
    UIApplication.shared.registerForRemoteNotifications()
  }
```
{% endtab %}
{% endtabs %}

## Step 5: Selecting Delivery Method
To set your Push Primer to trigger when you want it to, you must set __Perform Custom Event__ as the trigger action, choosing the custom event you want the push primer to trigger from. 

## Step 6: Targeting Users
For Push Primer Campaigns, you must target all users. 

## Step 7: Conversions
Do we want conversions. 

[deeplink]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/advanced_use_cases/linking/#deep-links
[push_primer1]: {% image_buster /assets/img/push_primer/push_primer_1.jpg %}
[push_primer2]: {% image_buster /assets/img/push_primer/push_primer_2.jpg %}
[push_primer3]: {% image_buster /assets/img/push_primer/push_primer_3.png %}
[push_primer4]: {% image_buster /assets/img/push_primer/push_primer_4.png %}
[push_primer5]: {% image_buster /assets/img/push_primer/push_primer_5.png %}
