---
nav_title: iOS 17 Upgrade Guide
article_title: iOS 17 Upgrade Guide
page_order: 7
platform: 
  - iOS
description: "This reference article covers iOS 17, SDK updates, and more."
---

## Changes in iOS 17

### Link Tracking & UTM Parameter Stripping

One of the important changes introduced at WWDC this year was the blocking UTM parameters in Safari. UTM parameters are pieces of code that are added to URLs, which are frequently used in marketing campaigns to measure the effectiveness of Email, SMS and other campaigns. 

Braze email and SMS products encode links in a way that is not  impacted by this change.  

### Continued Privacy Changes

Apple announced its commitment to further expand the scope of App Tracking Transparency (ATT), which enables users to control whether an app can access their activity across various apps and websites belonging to other companies. With this in mind, Apple announced two new key features to support this.

The first is the introduction of privacy manifests, which allows developers to outline the privacy practices of the their app - including third party SDKs - in a standardized format. With privacy manifests, Apple also plans to offer additional privacy protection for users, by identifying and blocking iOS APIs that might be used for fingerprinting. If applications are using any one of these APIs, they will be required to list a “required reason” for using that API in the privacy manifest as well. 

The second feature introduced is code signing, which allows developers using a third party SDK in their application to validate within XCode that it was signed by the same developer as previous versions. 

Related to privacy in gerenal, Apple has also announced that they will release a list of third party SDKs that are considered “privacy impacting” later this year - these SDKs are expected to be considered having an especially high impact on user privacy by Apple.

Unlike traditional tracking SDKs that are designed to monitor users across multiple websites and applications, the Braze SDK focuses on first-party data messaging and user experiences.

While we do not expect to be included in this list, we will monitor this closely and release any required updates if necessary.

## Preparing for iOS 17 {#next-steps}

Braze is continuously monitoring any impacts that both the Link Tracking and Privacy updates will have on integrations, if any, and will keep this page up to date with any downstream impacts that either will have. 

We expect that both our Swift SDK and our legacy Objective-C SDK will be compatible with both iOS 17 and XCode 15.

