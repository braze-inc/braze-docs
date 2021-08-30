---
nav_title: CocoaPods Integration
platform: iOS
page_order: 2
description: "This reference article shows how to integrate the Braze SDK using CocoaPods for iOS."

---

# CocoaPods Integration

## Step 1: Install CocoaPods

Installing the iOS SDK via [CocoaPod][apple_initial_setup_1] automates the majority of the installation process for you. Before beginning this process please ensure that you are using [Ruby version 2.0.0][apple_initial_setup_2] or greater. Don't worry, knowledge of Ruby syntax isn't necessary to install this SDK.

Simply run the following command to get started:

```bash
$ sudo gem install cocoapods
```

__Note__: If you are prompted to overwrite the `rake` executable please refer to the [Getting Started Directions on CocoaPods.org][apple_initial_setup_3] for further details.

__Note__: If you have issues regarding CocoaPods, please refer to the [CocoaPods Troubleshooting Guide][apple_initial_setup_25].

## Step 2: Constructing the Podfile

Now that you've installed the CocoaPods Ruby Gem, you're going to need to create a file in your Xcode project directory named `Podfile`.

Add the following line to your Podfile:

```
target 'YourAppTarget' do
  pod 'Appboy-iOS-SDK'
end
```

__Note__: We suggest you version Braze so pod updates automatically grab anything smaller than a minor version update. This looks like 'pod 'Appboy-iOS-SDK' ~> Major.Minor.Build'. If you want to integrate the latest version of Braze SDK automatically even with major changes, you can use `pod 'Appboy-iOS-SDK'` in your Podfile.

> We recommend that integrators import our full SDK as outlined above. However, if you are certain that you are only going to integrate a particular Braze feature then you have the option to import just the desired UI subspec instead of the full SDK.

| Subspec | Details |
| ------- | ------- |
| `pod 'Appboy-iOS-SDK/InAppMessage'` | The `InAppMessage` subspec contains the Braze In-App Message UI and the Core SDK.|
| `pod 'Appboy-iOS-SDK/ContentCards'` | The `ContentCards` subspec contains the Braze Content Card UI and the Core SDK. |
| `pod 'Appboy-iOS-SDK/NewsFeed'` | The `NewsFeed` subspec contains the Braze News Feed UI and the Core SDK. |
| `pod 'Appboy-iOS-SDK/Core'` | The `Core` subspec contains support for analytics, such as custom events and attributes. |
{: .ws-td-nw-1}

## Step 3: Installing the Braze SDK

To install the Braze SDK Cocoapod, navigate to the directory of your Xcode app project within your terminal and run the following command:
```
pod install
```

At this point, you should be able to open the new Xcode project workspace created by CocoaPods.

![New Workspace][apple_initial_setup_15]

## Next Steps

Follow the instructions for [Completing the Integration]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/completing_integration/).

## Updating the Braze SDK via CocoaPods

To update a Cocoapod, simply run the following commands within your project directory:

```
pod update
```

[apple_initial_setup_1]: http://cocoapods.org/
[apple_initial_setup_2]: https://www.ruby-lang.org/en/installation/
[apple_initial_setup_3]: http://guides.cocoapods.org/using/getting-started.html "CocoaPods Installation Directions"
[apple_initial_setup_5]: https://github.com/braze-inc/braze-ios-sdk/blob/master/AppboyKit/include/Appboy.h
[apple_initial_setup_15]: {% image_buster /assets/img_archive/podsworkspace.png %}
[apple_initial_setup_25]: http://guides.cocoapods.org/using/troubleshooting.html "CocoaPods Troubleshooting Guide"
