---
nav_title: Manual Integration
article_title: Manual Integration for iOS
platform: Swift
page_order: 3
description: "This reference article shows how to integrate the Braze Swift SDK using manual installation."
---

# Manual integration

> If you don't have access to a package manager, such as [Swift Package Manager]({{sitebase.url}}/docs/developer_guide/platform_integration_guides/swift/initial_sdk_setup/installation_methods/swift_package_manager/) or [CocoaPods]({{sitebase.url}}/docs/developer_guide/platform_integration_guides/swift/initial_sdk_setup/installation_methods/cocoapods/), you can manually integrate the Swift SDK instead.

## Step 1: Download the Braze SDK

Go to the [Braze SDK release page on GitHub](https://github.com/braze-inc/braze-swift-sdk/releases), then download `braze-swift-sdk-prebuilt.zip`.

!["The Braze SDK release page on GitHub."]({% image_buster /assets/img/swift/sdk_integration/download-braze-swift-sdk-prebuilt.png %})

## Step 2: Choose your frameworks

The Braze Swift SDK contains a variety of standalone XCframeworks, which gives you the freedom to integrate the features you want rather than needing to integrate them all.

First, decide whether you'd like to use static or dynamic XCframeworks, then open the relevant directory in `braze-swift-sdk-prebuilt`.

```bash
braze-swift-sdk-prebuilt
├── static
├── bundle
└── dynamic
```

Move the desired XCframwork directories to a temporary location, so you can easily access them later. To learn more about each file, reference the following:

| Package                    | Description                                                                                                                                                                                                                                                                                                           |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `BrazeKit`                 | Main SDK library that provides support for analytics and push notifications.                                                                                                                                                                                                                                          |
| `BrazeLocation`            | Location library that provides support for location analytics and geofence monitoring.                                                                                                                                                                                                                                |
| `BrazeUI`                  | Braze-provided user interface library for in-app messages and Content Cards.                                                                                                                                                                                                                                          |
| `BrazeNotificationService` | Notification service extension library that provides support for rich push notifications.  Do not add this library directly to your main application target, instead [add the `BrazeNotificationService` library separately](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications). |
| `BrazePushStory`           | Notification content extension library that provides support for push stories. Do not add this library directly to your main application target, instead [add the `BrazePushStory` library separately](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories).                                  |
{: .ws-td-nw-1}

## Step 3: Integrate your frameworks

The steps for integrating dynamic and static XCframeworks are different. Follow the corresponding steps for your desired XCframework type:

{% tabs %}
{% tab dynamic %}
In your Xcode project, drag and drop the dynamic XCFrameworks you'd like to use into your file tree. At a minimum, you'll need to add `BrazeKit.xcframework`.

!["An example Xcode project with the file tree open showing 'Brazekit.xcframework'."]()

{% alert note %}
To enable GIF support, also add `SDWebImage.xcframework` located in `braze-swift-sdk-prebuilt/dynamic`.
{% endalert %}

In your project settings, select your build target, then for each Braze framework listed under **Frameworks, Libraries, and Embedded Content**, choose **Embed & Sign**.

!["An example Xcode project with each Braze library set to 'Embed & Sign.'"]()
{% endtab %}

{% tab static %}
In your Xcode project, drag and drop the static XCFrameworks you'd like to use into your file tree. At a minimum, you'll need to add `BrazeKit.xcframework`.

!["An example Xcode project with the file tree open showing 'Brazekit.xcframework'."]()

{% alert note %}
To enable GIF support, also add `SDWebImage.xcframework` located in `braze-swift-sdk-prebuilt/static`.
{% endalert %}

In your project settings, select your build target, then for each Braze framework listed under **Frameworks, Libraries, and Embedded Content**, choose **Do Not Embed**.

!["An example Xcode project with each Braze library set to 'Do Not Embed.'"]()

Next, you'll open the `bundle` directory you [previously downloaded](#step-1-download-the-braze-sdk), and get the bundles for each of the following frameworks (if applicable):

- `BrazeKit`
- `BrazeLocation`
- `BrazeUI`
- `BrazeUICompat`

In your project settings, select your build target, then **Build Phases**. Under **Copy Bundle Resources** drag and drop each bundle to the related resource.

!["An example Xcode project with bundles added under 'Copy Bundle Resources.'"]()
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
