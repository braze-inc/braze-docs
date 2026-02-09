---
nav_title: iOS 17 upgrade guide
article_title: iOS 17 Upgrade Guide
page_order: 7
platform: 
  - iOS
description: "This article covers insights into the iOS 17 release to help you upgrade your SDK seamlessly."
hidden: true
noindex: true
---

# iOS 17 upgrade guide

> Curious about how Braze is preparing for the upcoming iOS release? This article summarizes our insights into the iOS 17 release to help you create a seamless experience for you and your users.

## iOS 17 and Xcode 15 compatibility

The Braze Swift SDK and Objective-C SDK are both backward compatible with Xcode 14 and Xcode 15, and compatible with iOS 17 devices.

## Changes in iOS 17

### Link tracking and UTM parameter stripping

One of the important changes in iOS 17 is blocking UTM parameters in Safari. UTM parameters are pieces of code that are added to URLs, which are frequently used in marketing campaigns to measure the effectiveness of email, SMS, and other messaging channels. 

This change does not impact Braze email click tracking and SMS link shortening sends.

### App Tracking Transparency

Apple announced its commitment to expand the scope of [Ad Tracking Transparency (ATT)](https://support.apple.com/en-us/HT212025), which enables users to control whether an app can access their activity on apps and websites belonging to other companies. The iOS 17 release contains two key ATT features: privacy manifests and code signing.

#### Privacy manifests

Apple now requires a privacy manifest file that describes the reason your app and third-party SDKs collect data, along with their data-collection methods. Starting with iOS 17.2, Apple will block all declared tracking endpoints in your app until the end-user accepts the ATT prompt.

Braze has released our own privacy manifest, along with new flexible APIs that automatically reroute declared tracking data to dedicated `-tracking` endpoints. For more information, see the [Braze privacy manifest]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?sdktab=swift#swift_privacy-manifest).

#### Code signing

Code signing allows developers who use a third-party SDK in their application to validate that the same developer signed it as previous versions in Xcode. 

### Braze SDK and privacy

Apple has also announced that they will release a list of third-party SDKs that are considered "privacy impacting" in late 2023. These SDKs are expected to have an especially high impact on user privacy by Apple.

Unlike traditional tracking SDKs that are designed to monitor users across multiple websites and applications, the Braze SDK focuses on first-party data messaging and user experiences.

While we do not expect the Braze SDK to be included in this list, we intend to monitor this situation closely and release any necessary updates.
