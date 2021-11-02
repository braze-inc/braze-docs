---
nav_title: Swift Package Manager
article_title: Swift Package Manager Integration for iOS
platform: iOS
page_order: 3
description: "This tutorial covers how to install the Braze SDK using Swift Package Manager for iOS"

---

# Swift package manager integration

## Requirements

Installing the iOS SDK via [Swift Package Manager][apple_initial_setup_1] (SPM) automates the majority of the installation process for you. Before beginning this process please ensure that you are using Xcode 12 or greater.

> Note that tvOS is not yet available via _Swift Package Manager_.

## Step 1: Adding the dependency to your project

Open your project and navigate to your project's settings. Select the tab named _Swift Packages_ and click on the add button (+) at the bottom left.

![Swift Package Manager: Menu 1][apple_initial_setup_2]

When importing SDK version `3.33.1` and above, enter the url of our iOS SDK repository (`https://github.com/braze-inc/braze-ios-sdk`) in the text field and click _Next_:

> For versions `3.29.0` through `3.32.0`, use the URL `https://github.com/Appboy/Appboy-ios-sdk`.

![Swift Package Manager: Menu 2][apple_initial_setup_3]

On the next screen, select the SDK version and click _Next_.

> Versions 3.29.0 and higher are compatible with _Swift Package Manager_.

![Swift Package Manager: Menu 3][apple_initial_setup_4]

Select the package that best fits your needs and click _Finish_:
- `AppboyUI`
  - Best suited if you plan to use UI components provided by Braze.
  - Includes `AppboyKit` automatically.
- `AppboyKit`
  - Best suited if you don't need to use any of the UI components provided by Braze (e.g. Content Cards, In-App Messages, etc.).
- `AppboyPushStory`
  - Include this package if you have integrated Push Stories in your app. This is supported as of version 3.31.0.
  - In the dropdown under `Add to Target`, select your `ContentExtension` target instead of your main app's target. 
  
> Make sure you select **either** `AppboyKit` **or** `AppboyUI`. Including both packages can lead to undesired behavior.

![Swift Package Manager: Menu 4][apple_initial_setup_5]

## Step 2: Configuring your project

Next, navigate to your project build settings and add the `-ObjC` flag to the _Other Linker Flags_ setting. Please note that this flag __must be added and [errors](https://developer.apple.com/library/archive/qa/qa1490/_index.html) resolved__ in order to further integrate the SDK.

![Swift Package Manager: Menu 5][apple_initial_setup_6]

{% alert note %}
If you do not add the `-ObjC` flag, parts of the API may become missing and behavior will be undefined. You may encounter unexpected errors such as "unrecognized selector sent to class", application crashes, and other issues.
{% endalert %}

## Step 3: Editing the target's scheme

If you are using Xcode 12.4 or earlier, edit the scheme of the target including the Appboy package (_Product > Scheme > Edit Scheme_ menu item):
- Click the expand ▶︎ next to _Build_ and select _Post-actions_. Press _+_ and select _New Run Script Action_.
- In the dropdown next to _Provide build settings from_, select your app's target.
- Copy this script into the open field:
```sh
# iOS
bash "$BUILT_PRODUCTS_DIR/Appboy_iOS_SDK_AppboyKit.bundle/Appboy.bundle/appboy-spm-cleanup.sh"
# macOS (if applicable)
bash "$BUILT_PRODUCTS_DIR/Appboy_iOS_SDK_AppboyKit.bundle/Contents/Resources/Appboy.bundle/appboy-spm-cleanup.sh"
```

{% alert note %}
You do not need to perform this step if you are using Xcode 12.5 or newer.
{% endalert %}

![Swift Package Manager: Menu 7][apple_initial_setup_7]

## Next steps

Follow the instructions for [Completing the Integration]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/completing_integration/).

[apple_initial_setup_1]: https://swift.org/package-manager/
[apple_initial_setup_2]: {% image_buster /assets/img/ios/spm/image1.png %}
[apple_initial_setup_3]: {% image_buster /assets/img/ios/spm/image2.png %}
[apple_initial_setup_4]: {% image_buster /assets/img/ios/spm/image3.png %}
[apple_initial_setup_5]: {% image_buster /assets/img/ios/spm/image4.png %}
[apple_initial_setup_6]: {% image_buster /assets/img/ios/spm/image5.png %}
[apple_initial_setup_7]: {% image_buster /assets/img/ios/spm/image6.png %}
