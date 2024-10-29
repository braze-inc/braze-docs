---
nav_title: Manual Integration
article_title: Manual Integration for iOS
platform: Swift
page_order: 3
description: "This reference article shows how to integrate the Braze Swift SDK using manual installation."
toc_headers: "h2"
---

# Manual integration

> If you don't have access to a package manager, such as [Swift Package Manager]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/installation_methods/swift_package_manager/) or [CocoaPods]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/installation_methods/cocoapods/), you can manually integrate the Swift SDK instead.

## Step 1: Download the Braze SDK

Go to the [Braze SDK release page on GitHub](https://github.com/braze-inc/braze-swift-sdk/releases), then download `braze-swift-sdk-prebuilt.zip`.

!["The Braze SDK release page on GitHub."]({% image_buster /assets/img/swift/sdk_integration/download-braze-swift-sdk-prebuilt.png %})

## Step 2: Choose your frameworks

The Braze Swift SDK contains a variety of standalone XCFrameworks, which gives you the freedom to integrate the features you want&#8212;without needing to integrate them all. Reference the following table to choose your XCFrameworks:

| Package                    | Required? | Description                                                                                                                                                                                                                                                                                                              |
| -------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `BrazeKit`                 | Yes       | Main SDK library that provides support for analytics and push notifications.                                                                                                                                                                                                                                             |
| `BrazeLocation`            | No        | Location library that provides support for location analytics and geofence monitoring.                                                                                                                                                                                                                                   |
| `BrazeUI`                  | No        | Braze-provided user interface library for in-app messages and Content Cards.                                                                                                                                                                                                                                             |
| `BrazeNotificationService` | No        | Notification service extension library that provides support for rich push notifications. Do not add this library directly to your main application target, instead [add the `BrazeNotificationService` library separately](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications).     |
| `BrazePushStory`           | No        | Notification content extension library that provides support for Push Stories. Do not add this library directly to your main application target, instead [add the `BrazePushStory` library separately](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories).                                     |
| `BrazeKitCompat`           | No        | Compatibility library containing all the `Appboy` and `ABK*` classes and methods that were available in the `Appboy-iOS-SDK` version 4.X.X. For usage details, refer to the minimal migration scenario in the [migration guide](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/appboy-migration-guide/). |
| `BrazeUICompat`            | No        | Compatibility library containing all the `ABK*` classes and methods that were available in the `AppboyUI` library from `Appboy-iOS-SDK` version 4.X.X. For usage details, refer to the minimal migration scenario in the [migration guide](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/appboy-migration-guide/). |
| `SDWebImage`               | No        | Dependency used only by `BrazeUICompat` in the minimal migration scenario. |

{: .ws-td-nw-1 .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Step 3: Prepare your files

Decide whether you want to use **Static** or **Dynamic** XCFrameworks, then prepare your files:

{% tabs %}
{% tab dynamic %}
1. Create a temporary directory for your XCFrameworks.
2. In `braze-swift-sdk-prebuilt`, open the `dynamic` directory and move `BrazeKit.xcframework` into your directory. Your directory should be similar to the following:
    ```bash
    temp_dir
    └── BrazeKit.xcframework
    ```
3. Move each of your [chosen XCFrameworks](#step-2-choose-your-frameworks) into your temporary directory. Your directory should be similar to the following:
    ```bash
    temp_dir
    ├── BrazeKit.xcframework
    ├── BrazeKitCompat.xcframework
    ├── BrazeLocation.xcframework
    └── SDWebImage.xcframework
    ```
{% endtab %}

{% tab static %}
### Step 3.1: Prepare your frameworks

1. Create a temporary directory for your XCFrameworks.
2. In `braze-swift-sdk-prebuilt`, open the `static` directory and move `BrazeKit.xcframework` into your directory. Your directory should be similar to the following:
   ```bash
   temp_frameworks_dir
   └── BrazeKit.xcframework
   ```
3. Move each of your [chosen XCFrameworks](#step-2-choose-your-frameworks) into your temporary directory. Your directory should be similar to the following:
   ```bash
   temp_frameworks_dir
   ├── BrazeKit.xcframework
   ├── BrazeKitCompat.xcframework
   ├── BrazeLocation.xcframework
   └── SDWebImage.xcframework
   ```

### Step 3.2: Prepare your bundles

1. Create a temporary directory for your bundles.
2. Open the `bundles` directory and move `BrazeKit.bundle` into your directory. Your directory should be similar to the following:
   ```bash
   temp_bundles_dir
   └── BrazeKit.bundle
   ```
3. If you're using the `BrazeLocation`, `BrazeUI`, `BrazeUICompat`, or `SDWebImage` XCFrameworks, move their corresponding bundles into your temporary directory. Your directory should be similar to the following:
   ```bash
   temp_bundles_dir
   ├── BrazeLocation.bundle
   ├── BrazeUI.bundle
   ├── BrazeUICompat.bundle
   └── SDWebImage.bundle
   ```
{% alert note %}
Only move over bundles for the [frameworks you prepared](#step-31-prepare-your-frameworks).
{% endalert %}
{% endtab %}
{% endtabs %}

## Step 4: Integrate your frameworks

Next, integrate the **Dynamic** or **Static** XCFrameworks you [prepared previously](#step-3-prepare-your-files):

{% tabs %}
{% tab dynamic %}
In your Xcode project, select your build target, then **General**. Under **Frameworks, Libraries, and Embedded Content**, drag and drop the [files you prepared previously](#step-3-prepare-your-files).

!["An example Xcode project with each Braze library set to 'Embed & Sign.'"]({% image_buster /assets/img/swift/sdk_integration/embed-and-sign.png %})

{% alert tip %}
To enable GIF support, add `SDWebImage.xcframework`, located in `braze-swift-sdk-prebuilt/dynamic`.
{% endalert %}
{% endtab %}

{% tab static %}
In your Xcode project, select your build target, then **General**. Under **Frameworks, Libraries, and Embedded Content**, drag and drop the [frameworks you prepared previously](#step-31-prepare-your-frameworks). Next to each framework, choose **Do Not Embed**. 

!["An example Xcode project with each Braze library set to 'Do Not Embed.'"]({% image_buster /assets/img/swift/sdk_integration/do-not-embed-and-sign.png %})

{% alert tip %}
To enable GIF support, add `SDWebImage.xcframework`, located in `braze-swift-sdk-prebuilt/static`.
{% endalert %}

While in your build target, select **Build Phases**. Under **Copy Bundle Resources** drag and drop the [bundles you prepared previously](#step-32-prepare-your-bundles).

!["An example Xcode project with bundles added under 'Copy Bundle Resources.'"]({% image_buster /assets/img/swift/sdk_integration/copy-bundle-resources.png %})
{% endtab %}
{% endtabs %}

## Common errors for Objective-C projects

If your Xcode project only contains Objective-C files, you may get "missing symbol" errors when you try to build your project. To fix these errors, open your project and add an empty Swift file to your file tree. This will force your build toolchain to embed [Swift Runtime](https://support.apple.com/kb/dl1998) and link to the appropriate frameworks during build time.

```bash
FILE_NAME.swift
```

Replace `FILE_NAME` with any non-spaced string. Your file should look similar to the following:

```bash
empty_swift_file.swift
```
