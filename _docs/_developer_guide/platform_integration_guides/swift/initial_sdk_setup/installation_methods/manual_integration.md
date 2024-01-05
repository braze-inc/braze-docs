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

## Source files

## Prebuilt XCFrameworks

1. Download the XCFrameworks you wish to use. You have the option of using either static ([here](https://github.com/braze-inc/braze-swift-sdk-prebuilt-static/releases) and [here](https://github.com/braze-inc/braze-swift-sdk-prebuilt-static)) or dynamic ([here](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic)) prebuilt Braze XCFrameworks.
2. Open your project in Xcode and drag and drop the XCFramework into the file navigator. Open the project settings, and under the "Frameworks, Libraries, and Embedded Content" section for your build target, set the "Embed" status for each included XCFramework to "Embed & Sign".
3. The `SDWebImage` framework is required for Content Cards and in-app messaging to function properly. `SDWebImage` is used for image downloading and displaying, including GIFs. If you intend to use Content Cards or in-app messages, follow the SDWebImage integration steps.

### SDWebImage integration

To install `SDWebImage`, follow their [instructions](https://github.com/SDWebImage/SDWebImage/wiki/Installation-Guide#build-sdwebimage-as-xcframework) and then drag and drop the resulting `XCFramework` into your project.

{% alert warning %}
If you try to use the core version of the SDK without Braze UI features, in-app messages will not display. Trying to display Braze Content Cards UI with the core version will lead to unpredictable behavior.
{% endalert %}


## Rich push notifications and push notification stories