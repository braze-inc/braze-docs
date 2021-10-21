---
nav_title: Push Stories
article_title: Push Stories for iOS
platform: iOS
page_order: 28
description: "This article shows how to set up Push Stories for your iOS application."
channel:
  - push

---

# Push story setup

The Push Story feature requires UNNotification Framework and iOS 10. The feature is only available from iOS SDK version 3.2.1.

## Step 1: enable push in your app

Please follow [The Push notification Integration][1] to enable push in your app.

## Step 2: adding the notification content extension target

In your app project, go to menu "File"->"New"->"Target...", add a new "Notification Content Extension" target and activate it.

![Add Content Extension][2]

Xcode should generate a new target for you and create files automatically for you including:

{% tabs %}
{% tab OBJECTIVE-C %}

- `NotificationViewController.h`
- `NotificationViewController.m`
- `MainInterface.storyboard`

{% endtab %}
{% tab swift %}

- `NotificationViewController.swift`
- `MainInterface.storyboard`

{% endtab %}
{% endtabs %}

## Step 3: enable capabilities

The Background Mode in the Capabilities section of the main app target is required by the Push Story feature. After turn on the background modes, select "Background fetch" and "Remote Notification".

![Enable Background Mode][3]

You also need to add `Capability App Groups`. If you haven't had any app group in your app, go to the Capability of the main app target, turn on the `App Groups` and click the "+". Use your App's bundle ID to create the App Group. For example, if your app's bundle ID is `com.company.appname`, you can name your App Group `group.com.company.appname.xyz`. You need to turn on the `App Groups` for both the main app target and the content extension target.

{% alert important %}
Note: `App Groups` in this context refer to Apple's [_App Groups Entitlement_](https://developer.apple.com/documentation/bundleresources/entitlements/com_apple_security_application-groups) and not your Braze App Group ID.
{% endalert %}

![Add App Groups][4]

## Step 4: adding the push story framework to your app

### Swift package manager

After following the [Swift Package Manager integration guide][5], simply add `AppboyPushStory` to your Notification Content Extension:

![Add AppboyPushStory][6]

![Add AppboyPushStory][7]

### Cocoapods

add the following line to your podfile:

```ruby
target 'YourContentExtensionTarget' do
  pod 'Appboy-Push-Story'
end
```

After updating the Podfile, navigate to the directory of your Xcode app project within your terminal and run `pod install`

### Manual integration

Download the latest `AppboyPushStory.zip` from the [Github release page][8], unzip it and add the following files to your project's Notification Content Extension:
- `Resources/ABKPageView.nib`
- `AppboyPushStory.xcframework`

![Add AppboyPushStory.xcframework][9]

{% alert important %}
Make sure that `Do Not Embed` is selected for `AppboyPushStory.xcframework` under the `Embed` column.
{% endalert %}

Add the `-ObjC` flag to your project's Notification Content Extension in _Build Settings->Other Linker Flags_.

## Step 5: updating your notification view controller

{% tabs %}
{% tab OBJECTIVE-C %}

In your `NotificationViewController.h`, add following lines to add new properties and import the header files:

```objc
#import <AppboyPushStory/AppboyPushStory.h>
```

```objc
@property (nonatomic) IBOutlet ABKStoriesView *storiesView;
@property (nonatomic) ABKStoriesViewDataSource *dataSource;
```

In your `NotificationViewController.m`, remove the default implementation and add following code:

```objc
@implementation NotificationViewController

- (void)didReceiveNotification:(UNNotification *)notification {
  self.dataSource = [[ABKStoriesViewDataSource alloc] initWithNotification:notification
                                                               storiesView:self.storiesView
                                                                  appGroup:@"YOUR-APP-GROUP-IDENTIFIER"];
}

- (void)didReceiveNotificationResponse:(UNNotificationResponse *)response
                     completionHandler:(void (^)(UNNotificationContentExtensionResponseOption option))completion {
  UNNotificationContentExtensionResponseOption option = [self.dataSource didReceiveNotificationResponse:response];
  completion(option);
}

- (void)viewWillDisappear:(BOOL)animated {
  [self.dataSource viewWillDisappear];
  [super viewWillDisappear:animated];
}

@end
```

{% endtab %}
{% tab swift %}

In your `NotificationViewController.swift`, add following line to import the header files:

```swift
import AppboyPushStory
```

Next, remove the default implementation and add following code:

```swift
class NotificationViewController: UIViewController, UNNotificationContentExtension {

  @IBOutlet weak var storiesView: ABKStoriesView!
  var dataSource: ABKStoriesViewDataSource?
    
  func didReceive(_ notification: UNNotification) {
    dataSource = ABKStoriesViewDataSource(notification: notification, storiesView: storiesView, appGroup: "YOUR-APP-GROUP-IDENTIFIER")
  }
    
  func didReceive(_ response: UNNotificationResponse, completionHandler completion: @escaping (UNNotificationContentExtensionResponseOption) -> Void) {
    if dataSource != nil {
      let option: UNNotificationContentExtensionResponseOption = dataSource!.didReceive(response)
      completion(option)
    }
  }
    
  override func viewWillDisappear(_ animated: Bool) {
    dataSource?.viewWillDisappear()
    super.viewWillDisappear(animated)
  }
}
```

{% endtab %}
{% endtabs %}

## Step 6: set the notification content extension storyboard

-		Open the Notification Content Extension storyboard and place a new `UIView` in the notification view controller. Rename the class to `ABKStoriesView`. Make the view width and height auto-resizable matching the Notification View Controller's main view frame.

![View Class][10]

![View Size][11]

-		Link the Notification View Controller's `storiesView` IBOutlet to the added `ABKStoriesView`.

![View Outlet][13]

## Step 7: set the notification content extension plist

Open the Info.plist file of the Notification Content Extension and add/change following keys under `NSExtension \ NSExtensionAttributes`:

`UNNotificationExtensionCategory` = `ab_cat_push_story_v2` (`String` type)
`UNNotificationExtensionDefaultContentHidden` = `YES` (`Boolean` type)
`UNNotificationExtensionInitialContentSizeRatio` = `0.65` (`Number` type)

![Plist Settings][12]

## Step 8: updating the braze integration in your main app

##### Option 1: runtime

In the `appboyOptions` dictionary used to configure your Braze instance, add a `ABKPushStoryAppGroupKey` entry and set the value to your App Group identifier.

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
NSMutableDictionary *appboyOptions = [NSMutableDictionary dictionary];
appboyOptions[ABKPushStoryAppGroupKey] = @"YOUR-APP-GROUP-IDENTIFIER";
[Appboy startWithApiKey:@"YOUR-API-KEY"
          inApplication:application
      withLaunchOptions:launchOptions
      withAppboyOptions:appboyOptions];
```

{% endtab %}
{% tab swift %}

```swift
let appboyOptions: [AnyHashable: Any] = [
  ABKPushStoryAppGroupKey : "YOUR-APP-GROUP-IDENTIFIER"
]
Appboy.start(withApiKey: "YOUR-API-KEY", in:application, withLaunchOptions:launchOptions, withAppboyOptions:appboyOptions)
```

{% endtab %}
{% endtabs %}

##### Option 2: info.plist

Alternatively, to configure Push Story App Group from your `Info.plist` file, add a dictionary named `Braze` to your `Info.plist` file. Inside the `Braze` dictionary, add a string-typed `PushStoryAppGroup` subentry and set the value to your App Group identifier. Note that prior to Braze iOS SDK v4.0.2, the dictionary key `Appboy` must be used in place of `Braze`.

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/
[2]: {% image_buster /assets/img/ios/push_story/add_content_extension.png %}
[3]: {% image_buster /assets/img/ios/push_story/enable_background_mode.png %}
[4]: {% image_buster /assets/img/ios/push_story/add_app_groups.png %}
[5]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/installation_methods/swift_package_manager/
[6]: {% image_buster /assets/img/ios/push_story/spm1.png %}
[7]: {% image_buster /assets/img/ios/push_story/spm2.png %}
[8]: https://github.com/Appboy/appboy-ios-sdk/releases
[9]: {% image_buster /assets/img/ios/push_story/manual1.png %}
[10]: {% image_buster /assets/img/ios/push_story/abkstoriesview_class.png %}
[11]: {% image_buster /assets/img/ios/push_story/abkstoriesview_size.png %}
[12]: {% image_buster /assets/img/ios/push_story/notificationcontentextension_plist.png %}
[13]: {% image_buster /assets/img/ios/push_story/abkstoriesview_outlet.png %}
