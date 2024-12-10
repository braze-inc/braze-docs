---
nav_title: CocoaPods
article_title: CocoaPods Integration for iOS
platform: Swift
page_order: 2
description: "This reference article shows how to integrate the Braze Swift SDK using CocoaPods for iOS."

---

# CocoaPods integration

## Step 1: Install CocoaPods

Installing the iOS SDK via [CocoaPods](http://cocoapods.org/) automates the majority of the installation process for you. To install CocoaPods, refer to the CocoaPods [Getting Started guide](https://guides.cocoapods.org/using/getting-started.html).

Run the following command to get started:

```bash
$ sudo gem install cocoapods
```

If you have issues regarding CocoaPods, refer to the CocoaPods [troubleshooting guide](http://guides.cocoapods.org/using/troubleshooting.html "CocoaPods Troubleshooting Guide").

## Step 2: Constructing the Podfile

Now that you've installed the CocoaPods Ruby Gem, you will need to create a file in your Xcode project directory named `Podfile`.

{% alert note %}
Starting in version 7.4.0, the Braze Swift SDK has additional distribution channels as [static XCFrameworks](https://github.com/braze-inc/braze-swift-sdk-prebuilt-static) and [dynamic XCFrameworks](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic). If you'd like to use either of these formats instead, follow the installation instructions from its respective repository.
{% endalert %}

Add the following line to your Podfile:

```
target 'YourAppTarget' do
  pod 'BrazeKit'
end
```

`BrazeKit` contains the main SDK library, providing support for analytics and push notifications.

We suggest you version Braze so pod updates automatically grab anything smaller than a minor version update. This looks like `pod 'BrazeKit' ~> Major.Minor.Build`. If you want to automatically integrate the latest Braze SDK version, even with major changes, you can use `pod 'BrazeKit'` in your Podfile.

#### Additional libraries

The Braze Swift SDK separates features into standalone libraries to provide developers with more control over which features to import into their projects. In addition to `BrazeKit`, you may add the following libraries to your Podfile:

| Library | Details |
| ------- | ------- |
| `pod 'BrazeLocation'` | Location library providing support for location analytics and geofence monitoring. |
| `pod 'BrazeUI'` | Braze-provided user interface library for in-app messages and Content Cards. |
{: .ws-td-nw-1}

##### Extension libraries

[BrazeNotificationService](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications) and [BrazePushStory](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories) are extension modules that provide additional functionality and should not be added directly to your main application target. Instead, you will need to create separate extension targets for each of these modules and import the Braze modules into their corresponding targets.

| Library | Details |
| ------- | ------- |
| `pod 'BrazeNotificationService'` | Notification service extension library providing support for rich push notifications. |
| `pod 'BrazePushStory'` | Notification content extension library providing support for Push Stories. |
{: .ws-td-nw-1}

## Step 3: Installing the Braze SDK

To install the Braze SDK CocoaPod, navigate to the directory of your Xcode app project within your terminal and run the following command:
```
pod install
```

At this point, you should be able to open the new Xcode project workspace created by CocoaPods. Make sure to use this Xcode workspace instead of your Xcode project.

![A Braze Example folder expanded to show the new `BrazeExample.workspace`.]({% image_buster /assets/img/braze_example_workspace.png %})

## Next steps

Follow the instructions for [completing the integration]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/completing_integration/).

## Updating the Braze SDK via CocoaPods

To update a CocoaPod, simply run the following command within your project directory:

```
pod update
```

