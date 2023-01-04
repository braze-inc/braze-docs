---
nav_title: CocoaPods
article_title: CocoaPods Integration for iOS
platform: Swift
<<<<<<< HEAD
page_order: 2
=======
page_order: 1
>>>>>>> 17274cdfe (Add documentation for Braze Swift SDK setup)
description: "This reference article shows how to integrate the Braze SDK using CocoaPods for iOS."

---

# CocoaPods Integration

## Step 1: Install CocoaPods

<<<<<<< HEAD
Installing the iOS SDK via [CocoaPods][apple_initial_setup_1] automates the majority of the installation process for you. To install CocoaPods, refer to the CocoaPods [Getting Started guide][cocoapods_getting_started].
=======
Installing the iOS SDK via [CocoaPods][apple_initial_setup_1] automates the majority of the installation process for you. Before beginning this process, make sure you use [Ruby version 2.0.0][apple_initial_setup_2] or greater. Don't worry, knowledge of Ruby syntax isn't necessary to install this SDK.
>>>>>>> 17274cdfe (Add documentation for Braze Swift SDK setup)

Run the following command to get started:

```bash
$ sudo gem install cocoapods
```

If you have issues regarding CocoaPods, refer to the CocoaPods [troubleshooting guide][apple_initial_setup_25].

<<<<<<< HEAD
=======
{% alert note %}
If prompted to overwrite the `rake` executable, refer to the [Getting started](http://guides.cocoapods.org/using/getting-started.html "CocoaPods Installation Directions") directions on CocoaPods.org for more details.
{% endalert %}

>>>>>>> 17274cdfe (Add documentation for Braze Swift SDK setup)
## Step 2: Constructing the Podfile

Now that you've installed the CocoaPods Ruby Gem, you will need to create a file in your Xcode project directory named `Podfile`.

Add the following line to your Podfile:

```
target 'YourAppTarget' do
  pod 'BrazeKit'
end
```

`BrazeKit` contains the main SDK library, providing support for analytics and push notifications.

We suggest you version Braze so pod updates automatically grab anything smaller than a minor version update. This looks like `pod 'BrazeKit' ~> Major.Minor.Build`. If you want to automatically integrate the latest Braze SDK version, even with major changes, you can use `pod 'BrazeKit'` in your Podfile.

<<<<<<< HEAD
#### Additional libraries

The Braze Swift SDK separates features into standalone libraries to provide developers with more control over which features to import into their projects. In addition to `BrazeKit`, you may add the following libraries to your Podfile:
=======
#### Additional Libraries

Unlike the legacy AppboyKit iOS SDK, the Braze Swift SDK separates features into standalone libraries to provide developers with more control over which features to import into their projects. In addition to `BrazeKit`, you may add the following libraries to your Podfile:
>>>>>>> 17274cdfe (Add documentation for Braze Swift SDK setup)

| Library | Details |
| ------- | ------- |
| `pod 'BrazeLocation'` | Location library providing support for location analytics and geofence monitoring. |
<<<<<<< HEAD
| `pod 'BrazeUI'` | Braze-provided user interface library for in-app messages and Content Cards. |
=======
| `pod 'BrazeUI'` | Braze-provided user interface library for In-App Messages and Content Cards. |
>>>>>>> 17274cdfe (Add documentation for Braze Swift SDK setup)
| `pod 'BrazeNotificationService'` | Notification service extension library providing support for rich push notifications. |
| `pod 'BrazePushStory'` | Notification content extension library providing support for Push Stories. |
{: .ws-td-nw-1}

## Step 3: Installing the Braze SDK

To install the Braze SDK CocoaPod, navigate to the directory of your Xcode app project within your terminal and run the following command:
```
pod install
```

At this point, you should be able to open the new Xcode project workspace created by CocoaPods. Make sure to use this Xcode workspace instead of your Xcode project. 

![A Braze Example folder expanded to show the new `BrazeExample.workspace`.][apple_initial_setup_15]

## Next steps

Follow the instructions for [completing the integration]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/completing_integration/).

## Updating the Braze SDK via CocoaPods

To update a CocoaPod, simply run the following command within your project directory:

```
pod update
```

[apple_initial_setup_1]: http://cocoapods.org/
[cocoapods_getting_started]: https://guides.cocoapods.org/using/getting-started.html
[apple_initial_setup_2]: https://www.ruby-lang.org/en/installation/
[apple_initial_setup_3]: http://guides.cocoapods.org/using/getting-started.html "CocoaPods Installation Directions"
[apple_initial_setup_5]: https://github.com/braze-inc/braze-ios-sdk/blob/master/AppboyKit/include/Appboy.h
[apple_initial_setup_15]: {% image_buster /assets/img/swift/cocoapods/braze_example_workspace.png %}
[apple_initial_setup_25]: http://guides.cocoapods.org/using/troubleshooting.html "CocoaPods Troubleshooting Guide"
