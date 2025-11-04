---
nav_title: Swift package manager
article_title: Swift Package Manager Integration for iOS
platform: iOS
page_order: 3
description: "This tutorial covers installing the Braze SDK using Swift Package Manager for iOS."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Swift Package Manager integration

Installing the iOS SDK via [Swift Package Manager](https://swift.org/package-manager/) (SPM) automates the majority of the installation process for you. Before beginning this process, ensure that you use Xcode 12 or greater.

{% alert note %}
tvOS is not currently available via Swift Package Manager.
{% endalert %}

## Step 1: Adding the dependency to your project

### Import SDK version

Open your project and navigate to your project's settings. Select the **Swift Packages** tab and click on the <i class="fas fa-plus"></i> add button below the packages list.

![]({% image_buster /assets/img/ios/spm/swiftpackages.png %})

When importing SDK version `3.33.1` or later, enter the URL of our iOS SDK repository (`https://github.com/braze-inc/braze-ios-sdk`) in the text field and click **Next**. 

For versions `3.29.0` through `3.32.0`, use the URL `https://github.com/Appboy/Appboy-ios-sdk`.

![]({% image_buster /assets/img/ios/spm/importsdk_example.png %})

On the next screen, select the SDK version and click **Next**. Versions `3.29.0` and later are compatible with Swift Package Manager.

![]({% image_buster /assets/img/ios/spm/select_version.png %})

### Select packages

Select the package that best suits your needs and click **Finish**. Make sure you select either `AppboyKit` or `AppboyUI`. Including both packages can lead to undesired behavior:

- `AppboyUI`
  - Best suited if you plan to use UI components provided by Braze.
  - Includes `AppboyKit` automatically.
- `AppboyKit`
  - Best suited if you don't need to use any of the UI components provided by Braze (for example, Content Cards, in-app messages, etc.).
- `AppboyPushStory`
  - Include this package if you have integrated Push Stories in your app. This is supported as of version `3.31.0`.
  - In the dropdown under `Add to Target`, select your `ContentExtension` target instead of your main app's target. 

![]({% image_buster /assets/img/ios/spm/add_package.png %})

## Step 2: Configuring your project

Next, navigate to your project **build settings** and add the `-ObjC` flag to the **Other Linker Flags** setting. This flag must be added and any [errors](https://developer.apple.com/library/archive/qa/qa1490/_index.html) resolved in order to further integrate the SDK.

![]({% image_buster /assets/img/ios/spm/buildsettings.png %})

{% alert note %}
If you do not add the `-ObjC` flag, parts of the API may become missing and behavior will be undefined. You may encounter unexpected errors such as "unrecognized selector sent to class", application crashes, and other issues.
{% endalert %}

## Step 3: Editing the target's scheme
{% alert important %}
If you are using Xcode 12.5 or newer, skip this step. 
{% endalert %}

If you are using Xcode 12.4 or earlier, edit the scheme of the target including the Appboy package (**Product > Scheme > Edit Scheme** menu item):
1. Expand the **Build** menu and select **Post-actions**. Press the plus (+) button and select **New Run Script Action**.
2. In the **Provide build settings from** dropdown, select your app's target.
3.  Copy this script into the open field:
```sh
# iOS
bash "$BUILT_PRODUCTS_DIR/Appboy_iOS_SDK_AppboyKit.bundle/Appboy.bundle/appboy-spm-cleanup.sh"
# macOS (if applicable)
bash "$BUILT_PRODUCTS_DIR/Appboy_iOS_SDK_AppboyKit.bundle/Contents/Resources/Appboy.bundle/appboy-spm-cleanup.sh"
```

![]({% image_buster /assets/img/ios/spm/swiftmanager_buildmenu.png %})

## Next steps

Follow the instructions for [completing the integration]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/completing_integration/).

