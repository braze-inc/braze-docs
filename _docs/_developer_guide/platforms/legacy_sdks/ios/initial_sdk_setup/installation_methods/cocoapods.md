---
nav_title: CocoaPods
article_title: CocoaPods Integration for iOS
platform: iOS
page_order: 2
description: "This reference article shows how to integrate the Braze SDK using CocoaPods for iOS."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# CocoaPods integration

## Step 1: Install CocoaPods

Installing the iOS SDK via [CocoaPods](http://cocoapods.org/) automates the majority of the installation process for you. Before beginning this process, make sure you use [Ruby version 2.0.0](https://www.ruby-lang.org/en/installation/) or greater. Don't worry, knowledge of Ruby syntax isn't necessary to install this SDK.

Run the following command to get started:

```bash
$ sudo gem install cocoapods
```

If you have issues regarding CocoaPods, refer to the CocoaPods [troubleshooting guide](http://guides.cocoapods.org/using/troubleshooting.html).

{% alert note %}
If prompted to overwrite the `rake` executable, refer to the [Getting started](http://guides.cocoapods.org/using/getting-started.html) directions on CocoaPods.org for more details.
{% endalert %}

## Step 2: Constructing the Podfile

Now that you've installed the CocoaPods Ruby Gem, you will need to create a file in your Xcode project directory named `Podfile`.

Add the following line to your Podfile:

```
target 'YourAppTarget' do
  pod 'Appboy-iOS-SDK'
end
```

We suggest you version Braze so pod updates automatically grab anything smaller than a minor version update. This looks like `pod 'Appboy-iOS-SDK' ~> Major.Minor.Build`. If you want to automatically integrate the latest Braze SDK version, even with major changes, you can use `pod 'Appboy-iOS-SDK'` in your Podfile.

#### Subspecs

We recommend that integrators import our full SDK. However, if you are certain that you are only going to integrate a particular Braze feature, you can import just the desired UI subspec instead of the full SDK.

| Subspec | Details |
| ------- | ------- |
| `pod 'Appboy-iOS-SDK/InAppMessage'` | The `InAppMessage` subspec contains the Braze in-app message UI and the Core SDK.|
| `pod 'Appboy-iOS-SDK/ContentCards'` | The `ContentCards` subspec contains the Braze Content Card UI and the Core SDK. |
| `pod 'Appboy-iOS-SDK/NewsFeed'` | The `NewsFeed` subspec contains the Braze Core SDK. |
| `pod 'Appboy-iOS-SDK/Core'` | The `Core` subspec contains support for analytics, such as custom events and attributes. |
{: .ws-td-nw-1}

## Step 3: Installing the Braze SDK

To install the Braze SDK CocoaPods, navigate to the directory of your Xcode app project within your terminal and run the following command:
```
pod install
```

At this point, you should be able to open the new Xcode project workspace created by CocoaPods. Make sure to use this Xcode workspace instead of your Xcode project. 

![An Appboy Example folder expanded to show the new `AppbpyExample.workspace`.]({% image_buster /assets/img_archive/podsworkspace.png %})

## Next steps

Follow the instructions for [completing the integration]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/completing_integration/).

## Updating the Braze SDK via CocoaPods

To update a CocoaPod, simply run the following command within your project directory:

```
pod update
```

