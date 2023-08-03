---
nav_title: iOS 17 Upgrade Guide
article_title: iOS 17 Upgrade Guide
page_order: 7
platform: 
  - iOS
description: "This refernce article covers iOS 17, SDK updates, and more."
---

## Changes in iOS 17

### Link Tracking & UTM Parameter Stripping

Apple's latest security measures encompass a noteworthy inclusion: the blocking of UTM parameters in Safari. UTM parameters are code fragments appended to URLs, commonly utilized in marketing to gauge the effectiveness of campaigns. Since Braze encodes all links that utilize click-tracking, we do not foresee this impacting integrations. 

### Privacy Impacting SDKs

Apple will release a list of Privacy-Impacting SDKs later this fall (2023) - these are third-party SDKs that have a particularly high impact on user privacy.

## Preparing for iOS 17 {#next-steps}

Braze is continuously monitoring any impacts that both the Link Tracking and Privacy updates will have on integrations, if any, and will keep this page up to date with any downstream impacts that either will have. 

We expect that both our Swift SDK and our legacy Obj-C SDK will be compatible with both XCode 15 and iOS 17.
