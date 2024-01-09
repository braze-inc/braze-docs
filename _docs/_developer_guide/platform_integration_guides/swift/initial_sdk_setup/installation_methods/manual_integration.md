---
nav_title: Manual Integration
article_title: Manual Integration for iOS
platform: Swift
page_order: 3
description: "This reference article shows how to integrate the Braze Swift SDK using manual installation."

---

# Manual integration

{% alert tip %}
We strongly recommend that you implement the SDK via a package manager such as [Swift Package Manager](../swift_package_manager/) or [CocoaPods](../cocoapods/). It will save you a lot of time and automate much of the process. However, if you are unable to do so, you may follow these instructions to integrate manually.
{% endalert %}

## Step 1: Downloading the Braze SDK
You have the option of using either dynamic or static XCFrameworks. Both can be found in [the releases section of the Braze Swift SDK repository](https://github.com/braze-inc/braze-swift-sdk/releases). The `braze-swift-sdk-prebuilt.zip` archive under "Assets" includes everything needed for this guide.

## Step 2: Select libraries to use
The Braze Swift SDK separates features into standalone libraries to provide developers with more control over which features to import into their projects. Each library corresponds to one of the XCFrameworks you downloaded. In the next step, you can add any combination of these to your project.

| Package | Details |
| ------- | ------- |
| `BrazeKit` | Main SDK library providing support for analytics and push notifications. |
| `BrazeLocation` | Location library providing support for location analytics and geofence monitoring. |
| `BrazeUI` | Braze-provided user interface library for in-app messages and Content Cards. |
| `BrazeNotificationService` | Notification service extension library providing support for rich push notifications. |
| `BrazePushStory` | Notification content extension library providing support for push stories. |
{: .ws-td-nw-1}

{% alert warning %}
[BrazeNotificationService](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications) and [BrazePushStory](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories) are extension modules that provide additional functionality and should not be added directly to your main application target. Instead follow the linked guides to integrate them separately into their respective target extensions.
{% endalert %}

## Step 3: Linking against the frameworks
{% tabs %}

{% tab dynamic %}
1. Drag and drop each **dynamic** XCFramework you wish to use into the file navigator in your Xcode project. Make sure to at least include `BrazeKit.xcframework`.
2. Open your project settings and select your build target. For each Braze framework listed under the "Frameworks, Libraries, and Embedded Content" section, set the "Embed" status to "Embed & Sign".
3. The `SDWebImage` framework is required to support GIFs within Braze Content Cards and in-app messaging UI. If you wish to enable GIF functionality, also include the `SDWebImage.xcframework` file included in `braze-swift-sdk-prebuilt/dynamic`.
{% endtab %}

{% tab static %}
1. Drag and drop each **static** XCFramework you wish to use into the file navigator in your Xcode project. Make sure to at least include `BrazeKit.xcframework`.
2. Open your project settings and select your build target. For each Braze framework listed under the "Frameworks, Libraries, and Embedded Content" section, set the "Embed" status to "Do Not Embed".
3. You must add the corresponding bundle for `BrazeKit` to your project. Additionally, If you included any of `BrazeLocation`, `BrazeUI`, or `BrazeUICompat`, you must also add the corresponding bundle for each of those frameworks that you included as well. The bundles can be found in `braze-swift-sdk-prebuilt/bundle`.
    * To add the bundles, select your build target in Xcode project settings, select the "Build Phases" tab, and then add each required bundle under the "Copy Bundle Resources" section.
4. The `SDWebImage` framework is required to support GIFs within Braze Content Cards and in-app messaging UI. If you wish to enable GIF functionality, also include the `SDWebImage.xcframework` file included in `braze-swift-sdk-prebuilt/static`. You do not need a matching bundle for `SDWebImage.xcframework`.
{% endtab %}

{% endtabs %}

### Note: Using the Braze Swift SDK with pure Objective-C projects
If you are integrating Braze into a project which currently consists entirely of Objective-C files, attempting to build the project after adding Braze XCFrameworks will generate missing symbol errors. To fix this, simply add a blank Swift file (`.swift` file extension) into your project. This forces the build toolchain to embed the Swift runtime and link to Swift frameworks when building the project.