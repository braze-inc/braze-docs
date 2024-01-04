---
nav_title: Apple Privacy Manifest
article_title: Apple Privacy Manifest
page_order: 7
platform: 
  - iOS
description: "This article describes the Braze Privacy Manifest used to declare data collection in your iOS app"
---

# Apple Privacy Manifest

The [Privacy Manifest](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files) is a file published alongside the Braze Swift SDK that describes the data collection and "required reasons" APIs.

By default, Braze does not collect any "[tracking data](https://developer.apple.com/app-store/app-privacy-details/#user-tracking)" which Apple describes as data collected and shared with 3rd parties.

The Braze privacy manifest, along with other privacy manifests you collect from other SDKs used, will be aggregated and displayed in the App Store to form your Privacy Nutrition label.

If you collect other 1st party data in your app, be sure to include that when generating your [Privacy Report](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests#4239187) in Xcode.

In a future iOS 17 version, Apple will block any "tracking data" by default, until the user accepts the Ad Tracking Transparency prompt.

## Data Collection

You can review the default data collection policies in our [SDK Data Collection Guide](https://www.braze.com/docs/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/). This list includes attributes the Braze SDK collects to help brands perform better 1st party messaging and segmentation in order to provide meaningful engagement between brands and their users.

Remember, you can always [opt-out](https://www.braze.com/docs/developer_guide/platform_integration_guides/sdk_primer#blocking-data-collection) of the optional data points the Braze SDK collects by default, and your integration determines what additional custom events and attributes you collect.

## Tracking vs. Non-Tracking Data

In addition the default data Braze declares in the Privacy Manifest, you may choose to declare additional data prior to publishing your app.

Apple requires that you declare which data types you collect are used for "tracking" vs. "non-tracking" usage. The Braze Swift SDK provides flexible APIs to help you adhere to Apple policies while ensure end-users' privacy is respected.

One key change with this behavior is that in a future iOS 17 update, Apple will block all declared "tracking domains" by default, until the user accepts the "Ad Tracking Transparency" prompt, which asks permission to track the user across apps and websites.

To support this privacy enhancement, Braze has added new features to our Swift SDK:

### New Tracking Domains

Braze has added new SDK API domains intended for "tracking" data. These domains will be used for any data you declare as tracking in your 

### Declaring Tracking Data

If you choose to collect user information through the Braze Swift SDK with plans to use this data for [Tracking](https://developer.apple.com/app-store/app-privacy-details/#user-tracking) (as described by Apple), you will need to declare this data when submitting your app to the App Store.

Braze provides a flexible approach allowing you to 
