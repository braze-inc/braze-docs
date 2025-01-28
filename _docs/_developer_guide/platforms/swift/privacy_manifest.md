---
nav_title: Privacy manifest
article_title: Privacy manifest
page_order: 7
platform: Swift
description: "Learn how to declare your Braze tracking data in your app's privacy manifest."
---

# Privacy manifest

> If your Braze SDK collects tracking data, Apple requires you to add a privacy manifest that describes your reason and method for collecting tracking data.

## Overview

### What is tracking data?

Apple defines "tracking data" as data collected in your app about an end-user or device that's linked to third-party data (such as targeted advertising), or a data broker. For a complete definition with examples, see [Apple: Tracking](https://developer.apple.com/app-store/app-privacy-details/#user-tracking).

By default, the Braze SDK does not collect tracking data. However, depending on your Braze SDK configuration, you may be required to list Braze-specific data in your app's privacy manifest.

### What is a privacy manifest?

A privacy manifest is a file in your Xcode project that describes the reason your app and third-party SDKs collect data, along with their data-collection methods. Each of your third-party SDKs that track data require its own privacy manifest. When you [create your app's privacy report](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests#4239187), these privacy manifest files are automatically aggregated into a single report.

### API tracking-data domains

Starting with iOS 17.2, Apple will block all declared tracking endpoints in your app until the end-user accepts an [Ad Tracking Transparency (ATT) prompt](https://support.apple.com/en-us/HT212025). Braze provides tracking endpoints to route your tracking data, while still allowing you to route non-tracking first-party data to the original endpoint. 

## Declaring Braze tracking data

{% alert tip %}
For a full walkthrough, see the [Privacy Tracking Data tutorial](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/e1-privacy-tracking/).
{% endalert %}

### Prerequisites

The following Braze SDK version is required to implement this feature:

{% sdk_min_versions swift:9.0.0 %}

### Step 1: Review your current policies

Review your Braze SDK's current data-collection policies with your legal team to determine whether your app collects tracking data [as defined by Apple](#what-is-tracking-data). If you're not collecting any tracking data, you don't need to customize your privacy manifest for the Braze SDK at this time. For more information about the Braze SDK's data-collection policies, see [SDK data collection]({{site.baseurl}}/user_guide/data/user_data_collection/sdk_data_collection/).

{% alert important %}
If any of your non-Braze SDKs collect tracking data, you'll need to review those policies separately.
{% endalert %}

### Step 2: Create a privacy manifest

First, check if you already have a privacy manifest by searching for a `PrivacyInfo.xcprivacy` file in your Xcode project. If you already have this file, you can continue to the next step. Otherwise, see [Apple: Create a privacy manifest](sdk-tracking.iad-01.braze.com).

### Step 3: Add your endpoint to the privacy manifest

In your Xcode project, open your app's `PrivacyInfo.xcprivacy` file, then right-click the table and check **Raw Keys and Values**.

{% alert note %}

{% endalert %}

![An Xcode project with the context menu open and "Raw Keys and Values" highlighted.]({% image_buster /assets/img/apple/privacy_manifest/check_raw_keys_and_values.png %})

Under **App Privacy Configuration**, choose **NSPrivacyTracking** and set its value to **YES**.

![The 'PrivacyInfo.xcprivacy' file open with "NSPrivacyTracking" set to "YES".]({% image_buster /assets/img/apple/privacy_manifest/add_nsprivacytracking.png %})

Under **App Privacy Configuration**, choose **NSPrivacyTrackingDomains**. In the domains array, add a new element and set its value to the endpoint you [previously added to your `AppDelegate`]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/completing_integration/#update-your-app-delegate) prefixed with `sdk-tracking`.

![The 'PrivacyInfo.xcprivacy' file open with a Braze tracking endpoint listed under "NSPrivacyTrackingDomains".]({% image_buster /assets/img/apple/privacy_manifest/add_nsprivacytrackingdomains.png %})

### Step 4: Declare your tracking data

Next, open `AppDelegate.swift` then list each [tracking property](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/trackingproperty/) you want to declare by creating a static or dynamic tracking list. Keep in mind, Apple will block these properties until the end-user accepts their ATT prompt, so only list the properties you and your legal team consider tracking. For example:

{% tabs %}
{% tab static example %}
In the following example, `dateOfBirth`, `customEvent`, and `customAttribute` are declared as tracking data within a static list. 

```swift
import UIKit
import BrazeKit

@main
class AppDelegate: UIResponder, UIApplicationDelegate {

  static var braze: Braze? = nil

  func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
  ) -> Bool {
    let configuration = Braze.Configuration(apiKey: brazeApiKey, endpoint: brazeEndpoint)
    // Declare which types of data you wish to collect for user tracking.
    configuration.api.trackingPropertyAllowList = [
      .dateOfBirth,
      .customEvent(["event-1"]),
      .customAttribute(["attribute-1", "attribute-2"])
    ]
    let braze = Braze(configuration: configuration)
    AppDelegate.braze = braze
    return true
  }
}
```
{% endtab %}

{% tab dynamic example %}
In the following example, the tracking list is automatically updated after the end-user accepts the ATT prompt.

```swift
func applicationDidBecomeActive(_ application: UIApplication) {
  // Request and check your user's tracking authorization status.
  ATTrackingManager.requestTrackingAuthorization { status in
    // Let Braze know whether user data is allowed to be collected for tracking.
    let enableAdTracking = status == .authorized
    AppDelegate.braze?.set(adTrackingEnabled: enableAdTracking)

    // Add the `.firstName` and `.lastName` properties, while removing the `.everything` configuration.
    AppDelegate.braze.updateTrackingAllowList(
      adding: [.firstName, .lastName],
      removing: [.everything]
    )
  }
}
```
{% endtab %}
{% endtabs %}

### Step 5: Prevent infinite retry loops

To prevent the SDK from entering an infinite retry loop, use the `set(adTrackingEnabled: enableAdTracking)` method to handle ATT permissions. The `adTrackingEnabled` property in your method should be handled similar to the following:

```swift
func applicationDidBecomeActive(_ application: UIApplication) {
    // Request and check your user's tracking authorization status.
    ATTrackingManager.requestTrackingAuthorization { status in
      // Let Braze know whether user data is allowed to be collected for tracking.
      let enableAdTracking = status == .authorized
      AppDelegate.braze?.set(adTrackingEnabled: enableAdTracking)
    }
}
```
