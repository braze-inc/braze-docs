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

The Braze Swift SDK contains a variety of standalone XCframeworks, which gives you the freedom to integrate the features you want rather than needing to integrate them all. First, decide whether you'd like to use static or dynamic XCframeworks.

{% tabs %}
{% tab dynamic %}
In `braze-swift-sdk-prebuilt`, open the `dynamic` directory. Each subdirectory represents an XCFramework. After you decide which XCFramworks you'd like to use, create a temporary directory to store your chosen frameworks.

You *must* at least include `BrazeKit` in addition to any other XCFrameworks.

| Package                    | Required? | Description                                                                                                                                                                                                                                                                                                           |
|----------------------------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `BrazeKit`                 | Yes       | Main SDK library that provides support for analytics and push notifications.                                                                                                                                                                                                                                          |
| `BrazeLocation`            | No        | Location library that provides support for location analytics and geofence monitoring.                                                                                                                                                                                                                                |
| `BrazeUI`                  | No        | Braze-provided user interface library for in-app messages and Content Cards.                                                                                                                                                                                                                                          |
| `BrazeNotificationService` | No        | Notification service extension library that provides support for rich push notifications.  Do not add this library directly to your main application target, instead [add the `BrazeNotificationService` library separately](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications). |
| `BrazePushStory`           | No        | Notification content extension library that provides support for push stories. Do not add this library directly to your main application target, instead [add the `BrazePushStory` library separately](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories).                                  |
{: .ws-td-nw-1 .reset-td-br-1 .reset-td-br-2}
{% endtab %}

{% tab static %}
In `braze-swift-sdk-prebuilt`, open the `static` directory. Each subdirectory represents an XCFramework. After you decide which XCFramworks you'd like to use, create a temporary directory to store your chosen frameworks.

You *must* at least include `BrazeKit` in addition to any other XCFrameworks.

| Package                    | Required? | Description                                                                                                                                                                                                                                                                                                           |
|----------------------------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `BrazeKit`                 | Yes       | Main SDK library that provides support for analytics and push notifications.                                                                                                                                                                                                                                          |
| `BrazeLocation`            | No        | Location library that provides support for location analytics and geofence monitoring.                                                                                                                                                                                                                                |
| `BrazeUI`                  | No        | Braze-provided user interface library for in-app messages and Content Cards.                                                                                                                                                                                                                                          |
| `BrazeNotificationService` | No        | Notification service extension library that provides support for rich push notifications.  Do not add this library directly to your main application target, instead [add the `BrazeNotificationService` library separately](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications). |
| `BrazePushStory`           | No        | Notification content extension library that provides support for push stories. Do not add this library directly to your main application target, instead [add the `BrazePushStory` library separately](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories).                                  |
{: .ws-td-nw-1 .reset-td-br-1 .reset-td-br-2}

For each of the following frameworks, you'll also need the corresponding bundle located in the `bundle` directory. Create a second temporary directory for your framework bundles.

- `BrazeKit`
- `BrazeLocation`
- `BrazeUI`
- `BrazeUICompat`
{% endtab %}
{% endtabs %}

## Step 3: Integrate your frameworks

Follow the steps for your chosen XCframework type:

{% tabs %}
{% tab dynamic %}
In your Xcode project, select your build target, then **General**. Under **Frameworks, Libraries, and Embedded Content**, drag and drop the frameworks [you set aside previously](#step-1-download-the-braze-sdk).

!["An example Xcode project with each Braze library set to 'Embed & Sign.'"]({% image_buster /assets/img/swift/sdk_integration/embed-and-sign.png %})

{% alert note %}
To enable GIF support, add `SDWebImage.xcframework`, located in `braze-swift-sdk-prebuilt/dynamic`.
{% endalert %}
{% endtab %}
{% tab static %}
In your Xcode project, select your build target, then **General**. Under **Frameworks, Libraries, and Embedded Content**, drag and drop the frameworks [you set aside previously](#step-1-download-the-braze-sdk). Next to each framework, choose **Do Not Embed**. 

!["An example Xcode project with each Braze library set to 'Do Not Embed.'"]({% image_buster /assets/img/swift/sdk_integration/do-not-embed-and-sign.png %})

{% alert note %}
To enable GIF support, add `SDWebImage.xcframework`, located in `braze-swift-sdk-prebuilt/static`.
{% endalert %}

While still in your build target, select **Build Phases**. Under **Copy Bundle Resources** drag and drop the bundles [you set aside previously](#step-1-download-the-braze-sdk).

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
