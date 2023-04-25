---
nav_title: Swift Package Manager
article_title: Swift Package Manager Integration for iOS
platform: Swift
page_order: 1
description: "This tutorial covers installing the Braze Swift SDK using Swift Package Manager for iOS."

---

# Swift Package Manager integration

> Installing the Swift SDK via [Swift Package Manager][1] (SPM) automates the majority of the installation process for you. Before beginning this process, check the [version information][2] to ensure that your environment is supported by Braze.

## Adding the dependency to your project

### Import SDK version

Open your project and navigate to your project's settings. Select the **Swift Packages** tab and click on the <i class="fas fa-plus"></i> add button below the packages list.

![][3]

Enter the URL of our iOS Swift SDK repository "https://github.com/braze-inc/braze-swift-sdk" in the text field. Under the **Dependency Rule** section, select the SDK version. Finally, click **Add Package**. 

![][4]

### Select packages

The Braze Swift SDK separates features into standalone libraries to provide developers with more control over which features to import into their projects.

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

 Select the package that best suits your needs and click **Add Package**. Make sure you select `BrazeKit` at a minimum. 

![][5]

## Next steps

Follow the instructions for [completing the integration]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/completing_integration/).

[1]: https://swift.org/package-manager/
[2]: https://github.com/braze-inc/braze-swift-sdk#version-information
[3]: {% image_buster /assets/img/swiftpackages.png %}
[4]: {% image_buster /assets/img/importsdk_example.png %}
[5]: {% image_buster /assets/img/add_package.png %}
