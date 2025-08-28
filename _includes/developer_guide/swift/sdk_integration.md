## Integrating the Swift SDK

You can integrate and customize the Braze Swift SDK using the Swift Package Manager (SPM), CocoaPods, or manual integration methods. For more information about the various SDK symbols, see [Braze Swift reference documentation](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/).

### Prerequisites

Before you start, verify your environment is supported by the [latest Braze Swift SDK version](https://github.com/braze-inc/braze-swift-sdk#version-information).

### Step 1: Install the Braze Swift SDK

We recommend using the [Swift Package Manager (SwiftPM)](https://swift.org/package-manager/) or [CocoaPods](http://cocoapods.org/) to install the Braze Swift SDK. Alternatively, you can install the SDK manually.

{% tabs local %}
{% tab Swift Package Manager %}
#### Step 1.1: Import SDK version

Open your project and navigate to your project's settings. Select the **Swift Packages** tab and click on the <i class="fas fa-plus"></i> add button below the packages list.

![]({% image_buster /assets/img/swiftpackages.png %})

{% alert note %}
Starting in version 7.4.0, the Braze Swift SDK has additional distribution channels as [static XCFrameworks](https://github.com/braze-inc/braze-swift-sdk-prebuilt-static) and [dynamic XCFrameworks](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic). If you'd like to use either of these formats instead, follow the installation instructions from its respective repository.
{% endalert %}

Enter the URL of our iOS Swift SDK repository `https://github.com/braze-inc/braze-swift-sdk` in the text field. Under the **Dependency Rule** section, select the SDK version. Finally, click **Add Package**.

![]({% image_buster /assets/img/importsdk_example.png %})

#### Step 1.2: Select your packages

The Braze Swift SDK separates features into standalone libraries to provide developers with more control over which features to import into their projects.

| Package         | Details                                                                                                                                                         |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `BrazeKit`      | Main SDK library providing support for analytics and push notifications.                                                                                        |
| `BrazeLocation` | Location library providing support for location analytics and geofence monitoring.                                                                              |
| `BrazeUI`       | Braze-provided user interface library for in-app messages, Content Cards, and Banners. Import this library if you intend to use the default UI components. |

{: .ws-td-nw-1}

##### About Extension libraries

{% alert warning %}
[BrazeNotificationService](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications) and [BrazePushStory](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories) are extension modules that provide additional functionality and should not be added directly to your main application target. Instead follow the linked guides to integrate them separately into their respective target extensions.
{% endalert %}

| Package                    | Details                                                                               |
| -------------------------- | ------------------------------------------------------------------------------------- |
| `BrazeNotificationService` | Notification service extension library providing support for rich push notifications. |
| `BrazePushStory`           | Notification content extension library providing support for Push Stories.            |

{: .ws-td-nw-1}

Select the package that best suits your needs and click **Add Package**. Make sure you select `BrazeKit` at a minimum.

![]({% image_buster /assets/img/add_package.png %})
{% endtab %}

{% tab CocoaPods %}
#### Step 1.1: Install CocoaPods

For a full walkthrough, see CocoaPods' [Getting Started Guide](https://guides.cocoapods.org/using/getting-started.html). Otherwise, you can run the following command to get started quickly:

```bash
$ sudo gem install cocoapods
```

If you get stuck, checkout CocoaPods' [Troubleshooting Guide](http://guides.cocoapods.org/using/troubleshooting.html).

#### Step 1.2: Constructing the Podfile

Next, create a file in your Xcode project directory named `Podfile`.

{% alert note %}
Starting in version 7.4.0, the Braze Swift SDK has additional distribution channels as [static XCFrameworks](https://github.com/braze-inc/braze-swift-sdk-prebuilt-static) and [dynamic XCFrameworks](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic). If you'd like to use either of these formats instead, follow the installation instructions from its respective repository.
{% endalert %}

Add the following line to your Podfile:

```
target 'YourAppTarget' do
  pod 'BrazeKit'
end
```

`BrazeKit` contains the main SDK library, providing support for analytics and push notifications.

We suggest you version Braze so pod updates automatically grab anything smaller than a minor version update. This looks like `pod 'BrazeKit' ~> Major.Minor.Build`. If you want to automatically integrate the latest Braze SDK version, even with major changes, you can use `pod 'BrazeKit'` in your Podfile.

##### About additional libraries

The Braze Swift SDK separates features into standalone libraries to provide developers with more control over which features to import into their projects. In addition to `BrazeKit`, you may add the following libraries to your Podfile:

| Library               | Details                                                                                                                                                         |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `pod 'BrazeLocation'` | Location library providing support for location analytics and geofence monitoring.                                                                              |
| `pod 'BrazeUI'`       | Braze-provided user interface library for in-app messages, Content Cards, and Banners. Import this library if you intend to use the default UI components. |

{: .ws-td-nw-1}

###### Extension libraries

[BrazeNotificationService](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications) and [BrazePushStory](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories) are extension modules that provide additional functionality and should not be added directly to your main application target. Instead, you will need to create separate extension targets for each of these modules and import the Braze modules into their corresponding targets.

| Library                          | Details                                                                               |
| -------------------------------- | ------------------------------------------------------------------------------------- |
| `pod 'BrazeNotificationService'` | Notification service extension library providing support for rich push notifications. |
| `pod 'BrazePushStory'`           | Notification content extension library providing support for Push Stories.            |

{: .ws-td-nw-1}

#### Step 1.3: Install the SDK

To install the Braze SDK CocoaPod, navigate to the directory of your Xcode app project within your terminal and run the following command:
```
pod install
```

At this point, you should be able to open the new Xcode project workspace created by CocoaPods. Make sure to use this Xcode workspace instead of your Xcode project.

![A Braze Example folder expanded to show the new `BrazeExample.workspace`.]({% image_buster /assets/img/braze_example_workspace.png %})

#### Updating the SDK using CocoaPods

To update a CocoaPod, simply run the following command within your project directory:

```
pod update
```
{% endtab %}

{% tab Manual %}
#### Step 1.1: Download the Braze SDK

Go to the [Braze SDK release page on GitHub](https://github.com/braze-inc/braze-swift-sdk/releases), then download `braze-swift-sdk-prebuilt.zip`.

!["The Braze SDK release page on GitHub."]({% image_buster /assets/img/swift/sdk_integration/download-braze-swift-sdk-prebuilt.png %})

#### Step 1.2: Choose your frameworks

The Braze Swift SDK contains a variety of standalone XCFrameworks, which gives you the freedom to integrate the features you want&#8212;without needing to integrate them all. Reference the following table to choose your XCFrameworks:

| Package                    | Required? | Description                                                                                                                                                                                                                                                                                                                          |
| -------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `BrazeKit`                 | Yes       | Main SDK library that provides support for analytics and push notifications.                                                                                                                                                                                                                                                         |
| `BrazeLocation`            | No        | Location library that provides support for location analytics and geofence monitoring.                                                                                                                                                                                                                                               |
| `BrazeUI`                  | No        | Braze-provided user interface library for in-app messages, Content Cards, and Banners. Import this library if you intend to use the default UI components.                                                                                                                                                                      |
| `BrazeNotificationService` | No        | Notification service extension library that provides support for rich push notifications. Do not add this library directly to your main application target, instead [add the `BrazeNotificationService` library separately](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications).                 |
| `BrazePushStory`           | No        | Notification content extension library that provides support for Push Stories. Do not add this library directly to your main application target, instead [add the `BrazePushStory` library separately](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories).                                                 |
| `BrazeKitCompat`           | No        | Compatibility library containing all the `Appboy` and `ABK*` classes and methods that were available in the `Appboy-iOS-SDK` version 4.X.X. For usage details, refer to the minimal migration scenario in the [migration guide](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/appboy-migration-guide/).            |
| `BrazeUICompat`            | No        | Compatibility library containing all the `ABK*` classes and methods that were available in the `AppboyUI` library from `Appboy-iOS-SDK` version 4.X.X. For usage details, refer to the minimal migration scenario in the [migration guide](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/appboy-migration-guide/). |
| `SDWebImage`               | No        | Dependency used only by `BrazeUICompat` in the minimal migration scenario.                                                                                                                                                                                                                                                           |

{: .ws-td-nw-1 .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Step 1.3: Prepare your files

Decide whether you want to use **Static** or **Dynamic** XCFrameworks, then prepare your files:

1. Create a temporary directory for your XCFrameworks.
2. In `braze-swift-sdk-prebuilt`, open the `dynamic` directory and move `BrazeKit.xcframework` into your directory. Your directory should be similar to the following:
    ```bash
    temp_dir
    └── BrazeKit.xcframework
    ```
3. Move each of your [chosen XCFrameworks](#swift_step-2-choose-your-frameworks) into your temporary directory. Your directory should be similar to the following:
    ```bash
    temp_dir
    ├── BrazeKit.xcframework
    ├── BrazeKitCompat.xcframework
    ├── BrazeLocation.xcframework
    └── SDWebImage.xcframework
    ```

#### Step 1.4: Integrate your frameworks

Next, integrate the **Dynamic** or **Static** XCFrameworks you [prepared previously](#swift_step-3-prepare-your-files):

In your Xcode project, select your build target, then **General**. Under **Frameworks, Libraries, and Embedded Content**, drag and drop the [files you prepared previously](#swift_step-3-prepare-your-files).

!["An example Xcode project with each Braze library set to 'Embed & Sign.'"]({% image_buster /assets/img/swift/sdk_integration/embed-and-sign.png %})

{% alert note %}
Starting with the Swift SDK 12.0.0, you should always select **Embed & Sign** for the Braze XCFrameworks for both the static and dynamic variants. This ensures that the frameworks resources are properly embedded in your app bundle.
{% endalert %}

{% alert tip %}
To enable GIF support, add `SDWebImage.xcframework`, located in either `braze-swift-sdk-prebuilt/static` or `braze-swift-sdk-prebuilt/dynamic`.
{% endalert %}

#### Common errors for Objective-C projects

If your Xcode project only contains Objective-C files, you may get "missing symbol" errors when you try to build your project. To fix these errors, open your project and add an empty Swift file to your file tree. This will force your build toolchain to embed [Swift Runtime](https://support.apple.com/kb/dl1998) and link to the appropriate frameworks during build time.

```bash
FILE_NAME.swift
```

Replace `FILE_NAME` with any non-spaced string. Your file should look similar to the following:

```bash
empty_swift_file.swift
```
{% endtab %}
{% endtabs local %}

### Step 2: Set up delayed initialization (optional)

You can choose to delay when the Braze Swift SDK is initialized, which is useful if your app needs to load config or wait for user consent before starting the SDK. Delayed initialization ensures Braze push notifications are queued until the SDK is ready.

To enable this, call `Braze.prepareForDelayedInitialization()` as early as possible—ideally inside or before your `application(_:didFinishLaunchingWithOptions:)`.

{% alert note %}
This only applies to push notifications from Braze. Other push notifications are handled normally by system delegates.
{% endalert %}

{% tabs %}
{% tab Swift %}
{% subtabs local %}
{% subtab UIKit %}
```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
  // Prepare the SDK for delayed initialization
  Braze.prepareForDelayedInitialization()

  // ... Additional non-Braze setup code

  return true
}
```
{% endsubtab %}

{% subtab SwiftUI %}
```swift
@main
struct MyApp: App {
  @UIApplicationDelegateAdaptor var appDelegate: AppDelegate

  var body: some Scene {
    WindowGroup {
      ContentView()
    }
  }
}

class AppDelegate: NSObject, UIApplicationDelegate {
  func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil) -> Bool {
    // Prepare the SDK for delayed initialization
    Braze.prepareForDelayedInitialization()

    // ... Additional non-Braze setup code

    return true
  }
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Objective-C %}
```objc
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  // Prepare the SDK for delayed initialization
  [Braze prepareForDelayedInitialization];
  
  // ... Additional non-Braze setup code

  return YES;
}
```
{% endtab %}
{% endtabs %}

{% alert note %}
[`Braze.prepareForDelayedInitialization(pushAutomation:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/preparefordelayedinitialization(pushautomation:)) accepts an optional `pushAutomation` parameter. If set to `nil`, all push automation features are enabled, except requesting push authorization at launch.
{% endalert %}

### Step 3: Update your app delegate

{% alert important %}
The following assumes you've already added an `AppDelegate` to your project (which are not generated by default). If you don't plan on using one, be sure to initialize the Braze SDK as early as possible, like during the app's launch.
{% endalert %}

{% subtabs local %}
{% subtab swift %}
Add the following line of code to your `AppDelegate.swift` file to import the features included in the Braze Swift SDK:

```swift
import BrazeKit
```

Next, add a static property to your `AppDelegate` class to keep a strong reference to the Braze instance throughout your application's lifetime:

```swift
class AppDelegate: UIResponder, UIApplicationDelegate {
  static var braze: Braze? = nil
}
```

Finally, in `AppDelegate.swift`, add the following snippet to your `application:didFinishLaunchingWithOptions:` method:

```swift
let configuration = Braze.Configuration(
    apiKey: "YOUR-APP-IDENTIFIER-API-KEY",
    endpoint: "YOUR-BRAZE-ENDPOINT"
)
let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```

Update `YOUR-APP-IDENTIFIER-API-KEY` and `YOUR-BRAZE-ENDPOINT` with the correct value from your **App Settings** page. Check out our [API identifier types]({{site.baseurl}}/api/identifier_types/?tab=app%20ids) for more information on where to find your app identifier API key.

{% endsubtab %}
{% subtab OBJECTIVE-C %}

Add the following line of code to your `AppDelegate.m` file:

```objc
@import BrazeKit;
```

Next, add a static variable to your `AppDelegate.m` file to keep a reference to the Braze instance throughout your application's lifetime:

```objc
static Braze *_braze;

@implementation AppDelegate
+ (Braze *)braze {
  return _braze;
}

+ (void)setBraze:(Braze *)braze {
  _braze = braze;
}
@end
```

Finally, within your `AppDelegate.m` file, add the following snippet within your `application:didFinishLaunchingWithOptions:` method:

```objc
BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:"YOUR-APP-IDENTIFIER-API-KEY"
                                                                  endpoint:"YOUR-BRAZE-ENDPOINT"];
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```

Update `YOUR-APP-IDENTIFIER-API-KEY` and `YOUR-BRAZE-ENDPOINT` with the correct value from your **Manage Settings** page. Check out our [API documentation]({{site.baseurl}}/api/api_key/#the-app-identifier-api-key) for more information on where to find your app identifier API key.

{% endsubtab %}
{% endsubtabs local %}

## Optional configurations

### Logging

#### Log levels

The default log level for the Braze Swift SDK is `.error`&#8212;it's also the minimum supported level when logs are enabled. These are the full list of log levels:

| Swift       | Objective-C              | Description                                                  |
| ----------- | ------------------------ | ------------------------------------------------------------ |
| `.debug`    | `BRZLoggerLevelDebug`    | (Default) Log debugging information + `.info` + `.error`.    |
| `.info`     | `BRZLoggerLevelInfo`     | Log general SDK information (user changes, etc.) + `.error`. |
| `.error`    | `BRZLoggerLevelError`    | Log errors.                                                  |
| `.disabled` | `BRZLoggerLevelDisabled` | No logging occurs.                                           |

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### Setting the log level

You can assign the log level at runtime in your `Braze.Configuration` object. For complete usage details, see [`Braze.Configuration.Logger`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/logger-swift.class).

{% tabs %}
{% tab swift %}

```swift
let configuration = Braze.Configuration(
  apiKey: "<BRAZE_API_KEY>",
  endpoint: "<BRAZE_ENDPOINT>"
)
// Enable logging of general SDK information (such as user changes, etc.)
configuration.logger.level = .info
let braze = Braze(configuration: configuration)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:self.APIKey
                                                                  endpoint:self.apiEndpoint];
// Enable logging of general SDK information (such as user changes, etc.)
[configuration.logger setLevel:BRZLoggerLevelInfo];
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
```

{% endtab %}
{% endtabs %}
