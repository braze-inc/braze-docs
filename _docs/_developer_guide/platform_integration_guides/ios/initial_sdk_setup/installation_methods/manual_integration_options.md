---
nav_title: Manual Integration Options
article_title: Manual Integration Options for iOS
platform: iOS
page_order: 4
description: "This reference article shows how to manually integrate the Braze SDK for iOS."

---

# Manual integration

{% alert tip %}
We strongly recommend that you implement the SDK via a package manager such as [Swift Package Manager](../swift_package_manager/), [CocoaPods](../cocoapods/), or [Carthage](../carthage_integration/). It will save you a lot of time and automate much of the process for you. However, if you are unable to do so you may complete the integration manually by following the instructions below.
{% endalert %}

## Step 1: Downloading the Braze SDK

1. Download `Appboy_iOS_SDK.zip` from the [release page](https://github.com/appboy/appboy-ios-sdk/releases).
If integrating an SDK version before 3.24.0, instead clone the Braze iOS SDK Github project:

```bash
# This command will clone both versions of the Braze SDK
$ git clone git@github.com:Appboy/appboy-ios-sdk.git
```

2. In Xcode, from the project navigator, select the destination project or group for Braze
3. Navigate to File > Add Files to “Project_Name”
4. Add the `AppboyKit` and `AppboyUI` folders to your project as a group.
	- Make sure that the "Copy items into destination group’s folder" option is checked if you are integrating for the first time. Expand "Options" in the file picker to select "Copy items if needed" and "Create groups."
	- Delete the `AppboyKit/include` and `AppboyUI/include` directories
5. (Optional) If you are one of the following:
  - You only want the core analytics features of the SDK and do not use any UI features (e.g, In-App Messages or Content Cards)
  - You have custom UI for Braze's UI features and handle the image downloading yourself

	You can use the core version of the SDK by removing the file `ABKSDWebImageProxy.m` and `Appboy.bundle`. This will remove the SDWebImage framework dependency and all the UI related resources (e.g. Nib files, images, localization files) from the SDK.

{% alert warning %}
If you try to use the core version of the SDK without Braze's UI features, in-app messages will not display. Trying to display Braze's Content Cards UI with the core version will lead to unpredictable behavior.
{% endalert %}

## Step 2: Adding required iOS libraries

1. Click on the target for your project (using the left-side navigation), and select the “Build Phases” tab
2. Click the <i class="fas fa-plus"></i> button under “Link Binary With Libraries”
3. In the menu, select `SystemConfiguration.framework`
4. Mark this library as required using the pull-down menu next to `SystemConfiguration.framework`
5. Repeat to add each of the following required frameworks to your project, marking each as “required”
	- `QuartzCore.framework`
	- `libz.tbd`
	- `CoreImage.framework`
	- `CoreText.framework`
	- `WebKit.framework`
6. Add the following frameworks and mark them as optional:
	- `CoreTelephony.framework`
7. Select the "Build Settings" tab. In the "Linking" section, locate the "Other Linker Flags" setting and add the `-ObjC` flag.
8. The SDWebImage framework is required for the Braze News Feed, Content Cards and In-App Messaging to function properly. SDWebImage is used for image downloading and displaying, including GIFs. If you intend to use the News Feed, Content Cards or In-App Messages, please follow the steps below.

### SDWebImage integration

1. Follow the SDWebImage Installation Guide's [instructions](https://github.com/SDWebImage/SDWebImage/wiki/Installation-Guide#using-sdwebimage-as-sub-xcode-project) for manually using SDWebImage as a Sub-Project in Xcode.
2. In the `SDWebImage` project settings, open the "Build Settings" tab. In the "Linking" section, locate the "Other Linker Flags" setting and add the `-ObjC` flag if it isn't already present.

### Optional location tracking

1. Add the `CoreLocation.framework` to enable location tracking
2. You must authorize location for your users using `CLLocationManager` in your app

## Step 3: Objective-C bridging header

If your project uses Swift, you will need a bridging header file.

If you do not have a bridging header file, create one and name it `your-product-module-name-Bridging-Header.h` by choosing File > New > File > (iOS or OS X) > Source > Header File. Then add the following line of code to the top of your bridging header file:
```
#import "AppboyKit.h"
```

In your project's Build Settings, add the relative path of your header file to the `Objective-C Bridging Header` build setting under `Swift Compiler - Code Generation`.

{% alert note %}
You do not need to follow these steps if your project only uses Objective-C.
{% endalert %}

## Next steps

Follow the instructions for [Completing the Integration]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/completing_integration/).
