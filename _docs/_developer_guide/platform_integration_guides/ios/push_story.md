---
nav_title: Push Story
platform: iOS
page_order: 5

---

# Push Story Setup

The Push Story feature requires UNNotification Framework and iOS 10. The feature is only available from iOS SDK version 3.2.1.

## Step 1: Enable Push In Your App

Please follow [The Push notification Integration][1] to enable push in your app.

## Step 2: Adding the Notification Content Extension Target

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

## Step 3: Enable Capabilities

The Background Mode in the Capabilities section of the main app target is required by the Push Story feature. After turn on the background modes, select "Background fetch" and "Remote Notification".

![Enable Background Mode][3]

You also need to add Capability `App Groups`. If you haven't had any app group in your app, go to the Capability of the main app target, turn on the `App Groups` and click the "+". Use your App's bundle ID to create the App Group. For example, if your app's bundle ID is `com.company.appname`, you can name your App Group `group.com.company.appname.xyz`. You need to turn on the `App Groups` for both the main app target and the content extension target.

![Add App Groups][4]

## Step 4: Updating the Podfile

Add the following line to your Podfile:

```ruby
target 'YourContentExtensionTarget' do
  pod 'Appboy-Push-Story', '~>3.0'
end
```

After updating the Podfile, navigate to the directory of your Xcode app project within your terminal and run `pod install`

## Step 5: Link the Braze Push Story Framework

Under `Build Phases`, click on the `+` button and add `New Copy Files Phase`.  Inside the new phase, change the Destination to `Frameworks`. Add the `AppboyPushStory.framework` in the new phase (it can be found by clicking on `Add Other...` and navigating to the `Pods` folder).

{% alert important %}
If you are using `use_frameworks!` in your Podfile and are on version 1.6.1+ on CocoaPods, __don't__ do this step of adding `AppboyPushStory.framework` to the `Copy Files` phase.
{% endalert %}

![New Copy File Phase][ios_pushstory_01]

![Add Framework][ios_pushstory_02]

To verify that this was successful, go to the `General` tab of the main application target. Under `Embedded Binaries` check that `AppboyPushStory.framework` has been added.

![Embedded Binaries][ios_pushstory_05]

Back in `Build Phases`, click on `+` button and add `New Run Script Phase`. Make sure the newly created `Run Script` section is the last step in the `Build Phases` list.  Add this text into the Script body:

```shell
APP_PATH="${TARGET_BUILD_DIR}/${WRAPPER_NAME}"

find "$APP_PATH" -name 'AppboyPushStory.framework' -type d | while read -r FRAMEWORK
do
FRAMEWORK_EXECUTABLE_NAME=$(defaults read "$FRAMEWORK/Info.plist" CFBundleExecutable)
FRAMEWORK_EXECUTABLE_PATH="$FRAMEWORK/$FRAMEWORK_EXECUTABLE_NAME"

FRAMEWORK_TMP_PATH="$FRAMEWORK_EXECUTABLE_PATH-tmp"

case "${TARGET_BUILD_DIR}" in
*"iphonesimulator")
;;
*)
if $(lipo "$FRAMEWORK_EXECUTABLE_PATH" -verify_arch "i386") ; then
lipo -output "$FRAMEWORK_TMP_PATH" -remove "i386" "$FRAMEWORK_EXECUTABLE_PATH"
rm "$FRAMEWORK_EXECUTABLE_PATH"
mv "$FRAMEWORK_TMP_PATH" "$FRAMEWORK_EXECUTABLE_PATH"
fi
if $(lipo "$FRAMEWORK_EXECUTABLE_PATH" -verify_arch "x86_64") ; then
lipo -output "$FRAMEWORK_TMP_PATH" -remove "x86_64" "$FRAMEWORK_EXECUTABLE_PATH"
rm "$FRAMEWORK_EXECUTABLE_PATH"
mv "$FRAMEWORK_TMP_PATH" "$FRAMEWORK_EXECUTABLE_PATH"
fi
;;
esac

done
```

![Run Script][ios_pushstory_03]

Go to the `General` tab of the Content Extension target and add `AppboyPushStory.framework` in the `Linked Frameworks and Libraries` section.

![Linked Frameworks][ios_pushstory_04]

## Step 6: Updating your Notification View Controller

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
                                                                  appGroup:@"YOUR-APP-GROUP"];
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
    dataSource = ABKStoriesViewDataSource(notification: notification, storiesView: storiesView, appGroup: "group.Appboy.HelloSwift")
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

## Step 7: Set the Notification Content Extension Storyboard

-		Open the Notification Content Extension storyboard and place a new `UIView` in the notification view controller. Rename the class to `ABKStoriesView`. Make the view width and height auto-resizable matching the Notification View Controller's main view frame.

![View Class][ios_pushstory_06]

![View Size][ios_pushstory_07]

-		Link the Notification View Controller's `storiesView` IBOutlet to the added `ABKStoriesView`.

![View Outlet][ios_pushstory_09]

## Step 8: Set the Notification Content Extension Plist

Open the Info.plist file of the Notification Content Extension and add/change following keys under `NSExtension \ NSExtensionAttributes`:

`UNNotificationExtensionCategory` = `ab_cat_push_story_v2` (`String` type)
`UNNotificationExtensionDefaultContentHidden` = `YES` (`Boolean` type)
`UNNotificationExtensionInitialContentSizeRatio` = `0.65` (`Number` type)

![Plist Settings][ios_pushstory_08]

## Step 9: Configure Push Story App Group in Your Main App

##### Option 1: Runtime

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

##### Option 2: Info.plist

Alternatively, to configure Push Story App Group from your `Info.plist` file, add a dictionary named `Braze` to your `Info.plist` file. Inside the `Braze` dictionary, add a string-typed `PushStoryAppGroup` subentry and set the value to your App Group identifier. Note that prior to Braze iOS SDK INSERT_VERSION_HERE, the dictionary key `Appboy` must be used in place of `Braze`.

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/
[2]: {% image_buster /assets/img_archive/add_content_extension.png %}
[3]: {% image_buster /assets/img_archive/enable_background_mode.png %}
[4]: {% image_buster /assets/img_archive/add_app_groups.png %}
[ios_pushstory_01]: {% image_buster /assets/img_archive/ios_pushstory_01.png %}
[ios_pushstory_02]: {% image_buster /assets/img_archive/ios_pushstory_02.png %}
[ios_pushstory_03]: {% image_buster /assets/img_archive/ios_pushstory_03.png %}
[ios_pushstory_04]: {% image_buster /assets/img_archive/ios_pushstory_04.png %}
[ios_pushstory_05]: {% image_buster /assets/img_archive/ios_pushstory_05.png %}
[ios_pushstory_06]: {% image_buster /assets/img_archive/ios_pushstory_06.png %}
[ios_pushstory_07]: {% image_buster /assets/img_archive/ios_pushstory_07.png %}
[ios_pushstory_08]: {% image_buster /assets/img_archive/ios_pushstory_08.png %}
[ios_pushstory_09]: {% image_buster /assets/img_archive/ios_pushstory_09.png %}
