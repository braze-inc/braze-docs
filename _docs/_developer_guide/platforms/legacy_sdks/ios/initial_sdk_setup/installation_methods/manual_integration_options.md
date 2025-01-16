---
nav_title: Manual
article_title: Manual Integration Options for iOS
platform: iOS
page_order: 4
description: "This reference article shows how to manually integrate the Braze SDK for iOS."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Manual integration

{% alert tip %}
We strongly recommend that you implement the SDK via a package manager such as [Swift Package Manager](../swift_package_manager/), [CocoaPods](../cocoapods/), or [Carthage](../carthage_integration/). It will save you a lot of time and automate much of the process. However, if you are unable to do so, you may complete the integration manually by following the instructions.
{% endalert %}

## Step 1: Downloading the Braze SDK

### Option 1: Dynamic XCFramework

1. Download `Appboy_iOS_SDK.xcframework.zip` from the [release page](https://github.com/appboy/appboy-ios-sdk/releases) and extract the file.
2. In Xcode, drag and drop this `.xcframework` into your project.
3. Under the **General** tab of the project, select **Embed & Sign** for `Appboy_iOS_SDK.xcframework`.

### Option 2: Static XCFramework for static integration

1. Download `Appboy_iOS_SDK.zip` from the [release page](https://github.com/appboy/appboy-ios-sdk/releases).<br><br>
2. In Xcode, from the project navigator, select the destination project or group for Braze<br><br>
3. Navigate to **File > Add Files > Project_Name**.<br><br>
4. Add the `AppboyKit` and `AppboyUI` folders to your project as a group.
	- Make sure that the **Copy items into destination group's folder** option is selected if you are integrating for the first time. Expand **Options** in the file picker to select **Copy items if needed** and **Create groups**.
	- Delete the `AppboyKit/include` and `AppboyUI/include` directories.<br><br>
5. (Optional) If one of the following applies to you:
  - You only want the core analytics features of the SDK and do not use any UI features (for example, in-app messages or Content Cards).
  - You have custom UI for Braze UI features and handle the image downloading yourself.<br><br>You can use the core version of the SDK by removing the file `ABKSDWebImageProxy.m` and `Appboy.bundle`. This will remove the `SDWebImage` framework dependency and all the UI-related resources (for example, Nib files, images, localization files) from the SDK.

{% alert warning %}
If you try to use the core version of the SDK without Braze UI features, in-app messages will not display. Trying to display Braze Content Cards UI with the core version will lead to unpredictable behavior.
{% endalert %}

## Step 2: Adding required iOS libraries

1. Click on the target for your project (using the left-side navigation), and select the **Build Phases** tab.<br><br>
2. Click the <i class="fas fa-plus"></i> button under **Link Binary With Libraries**.<br><br>
3. In the menu, select `SystemConfiguration.framework`.<br><br>
4. Mark this library as required using the pull-down menu next to `SystemConfiguration.framework`.<br><br>
5. Repeat to add each of the following required frameworks to your project, marking each as "required".
	- `QuartzCore.framework`
	- `libz.tbd`
	- `CoreImage.framework`
	- `CoreText.framework`
	- `WebKit.framework`<br><br>
6. Add the following frameworks and mark them as optional:
	- `CoreTelephony.framework`<br><br>
7. Select the **Build Settings** tab. In the **Linking** section, locate the **Other Linker Flags** setting and add the `-ObjC` flag.<br><br>
8. The `SDWebImage` framework is required for Content Cards and in-app messaging to function properly. `SDWebImage` is used for image downloading and displaying, including GIFs. If you intend to use Content Cards or in-app messages, follow the SDWebImage integration steps.

### SDWebImage integration

To install `SDWebImage`, follow their [instructions](https://github.com/SDWebImage/SDWebImage/wiki/Installation-Guide#build-sdwebimage-as-xcframework) and then drag and drop the resulting `XCFramework` into your project.

### Optional location tracking

1. Add the `CoreLocation.framework` to enable location tracking.
2. You must authorize location for your users using `CLLocationManager` in your app.

## Step 3: Objective-C bridging header

{% alert note %}
If your project only uses Objective-C, skip this step.
{% endalert %}

If your project uses Swift, you will need a bridging header file.

If you do not have a bridging header file, create one and name it `your-product-module-name-Bridging-Header.h` by choosing **File > New > File > (iOS or OS X) > Source > Header File**. Then, add the following line of code to the top of your bridging header file:
```
#import "AppboyKit.h"
```

In your project's **Build Settings**, add the relative path of your header file to the `Objective-C Bridging Header` build setting under `Swift Compiler - Code Generation`.

## Next steps

Follow the instructions for [completing the integration]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/completing_integration/).
