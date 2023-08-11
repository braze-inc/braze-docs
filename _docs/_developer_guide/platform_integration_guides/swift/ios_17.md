---
nav_title: iOS 17 Upgrade Guide
article_title: iOS 17 Upgrade Guide
page_order: 7
platform: 
  - iOS
description: "This article covers Braze's insights into the iOS 17 release to help you upgrade your SDK seamlessly."
---

# iOS 17 upgrade guide {#next-steps}

> Curious about how Braze is preparing for the upcoming iOS release? This article summarizes our insights into the iOS 17 release to help you create a seamless experience for you and your users.

We anticipate that both our Swift SDK and our legacy Objective-C SDK will be compatible with both iOS 17 and XCode 15.

## Changes in iOS 17

### Link tracking and UTM parameter stripping

One of the important changes in iOS 17 is blocking UTM parameters in Safari. UTM parameters are pieces of code that are added to URLs, which are frequently used in marketing campaigns to measure the effectiveness of email, SMS, and other messaging channels. 

Braze email and SMS channels encode links in a way that are not impacted by this change.  

### App Tracking Transparency

Apple announced its commitment to expand the scope of App Tracking Transparency (ATT), which enables users to control whether an app can access their activity on apps and websites belonging to other companies. The iOS 17 release contains two key ATT features: privacy manifests and code signing.

#### Privacy manifests

Privacy manifests allow developers to outline the privacy practices of their app&#8212;including third party SDKs&#8212;in a standardized format. As part of this effort, Apple plans to identify and block iOS APIs that might be used for fingerprinting. If applications are using such APIs, they will be obliged to list a "required reason" for using that API in the privacy manifest. 

#### Code signing

Code signing allows developers using a third party SDK in their application to validate that it was signed by the same developer as previous versions in XCode. 

### Braze SDK and privacy

Apple has also announced that they will release a list of third-party SDKs that are considered "privacy impacting" in late 2023. These SDKs are expected to have an especially high impact on user privacy by Apple.

Unlike traditional tracking SDKs that are designed to monitor users across multiple websites and applications, the Braze SDK focuses on first-party data messaging and user experiences.

While we do not expect the Braze SDK to be included in this list, we intend to monitor this situation closely and release any necessary updates.