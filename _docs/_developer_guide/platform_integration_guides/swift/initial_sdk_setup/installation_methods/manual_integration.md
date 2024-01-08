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
You have the option of using either dynamic or static XCFrameworks. Both can be found in [the releases section of the Braze Swift SDK repository](https://github.com/braze-inc/braze-swift-sdk/releases). The `braze-swift-sdk-prebuilt.zip` folder under "Assets" includes everything needed for this guide.

## Step 2: Linking against the frameworks
{% tabs %}

{% tab dynamic %}
1. Drag and drop each **dynamic** XCFramework you wish to use into the file navigator in your Xcode project. Make sure to at least include `BrazeKit.xcframework`.
2. Open your project settings and select your build target. For each Braze framework listed under the "Frameworks, Libraries, and Embedded Content" section, set the "Embed" status to "Embed & Sign".
3. The `SDWebImage` framework is required to support GIFs within Braze Content Cards and in-app messaging UI. If you wish to enable GIF functionality, also include the `SDWebImage.xcframework` file included in `braze-swift-sdk-prebuilt/dynamic`.
{% endtab %}

{% tab static %}
1. Drag and drop each **static** XCFramework you wish to use into the file navigator in your Xcode project. Make sure to at least include `BrazeKit.xcframework`.
2. Open your project settings and select your build target. For each Braze framework listed under the "Frameworks, Libraries, and Embedded Content" section, set the "Embed" status to "Do Not Embed".
3. You must add the corresponding bundle for `BrazeKit` to your project. Additionally, If you included any of `BrazeLocation`, `BrazeUI`, or `BrazeUICompat`, you must also add the corresponding bundle for each of those frameworks that you included as well. The bundles can be found in the `braze-swift-sdk-prebuilt` release asset's `bundle` sub-directory.
    * To add the bundles, select your build target in Xcode project settings, select the "Build Phases" tab, and then add each required bundle under the "Copy Bundle Resources" section.
4. The `SDWebImage` framework is required to support GIFs within Braze Content Cards and in-app messaging UI. If you wish to enable GIF functionality, also include the `SDWebImage.xcframework` file included in `braze-swift-sdk-prebuilt/static`. You do not need a matching bundle for `SDWebImage.xcframework`.
{% endtab %}

{% endtabs %}