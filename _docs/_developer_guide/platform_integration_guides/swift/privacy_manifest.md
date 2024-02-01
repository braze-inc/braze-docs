---
nav_title: Privacy manifest files 
article_title: Privacy manifest files 
page_order: 7
platform: 
  - iOS
description: "This article describes Braze's privacy manifest file used to declare data collection in your iOS app."
---

# Braze's privacy manifest

> If your Braze SDK collects tracking data, Apple requires you to add a privacy manifest that describes your reason and method for collecting tracking data.

## What is tracking data?

Apple defines "tracking data" as data collected in your app about an end-user or device that's linked to Third-Party Data (such as targeted advertising), or a data broker. For a complete definition with examples, see [Apple: Tracking](https://developer.apple.com/app-store/app-privacy-details/#user-tracking).

By default, the Braze SDK does not collect tracking data. However, depending on your Braze SDK configuration, you may be required to add a privacy manifest to your app.

## What is a privacy manifest?

A privacy manifest is a file in your Xcode project that describes the reason your app and third-party SDKs collect data, along with the data-collection method. Each of your third-party SDKs that track data require its own privacy manifest file. When you [create your app's privacy report](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests#4239187), these privacy manifest files are automatically aggregated into a single report.

When an end-user launches your app for the first time, your app's privacy report will be used to generate an Ad Tracking Transparency agreement. Starting with iOS 17.2, Apple will block all tracking data in your app until the end-user accepts this agreement.

## Declaring Braze tracking data

### Step 1: Review your current policies

Review your Braze SDK's current data-collection policies with your legal team to determine whether your app collects tracking data [as defined by Apple](#what-is-tracking-data). If you're not collecting any tracking data, you don't need to add a privacy manifest at this time. For more information about the Braze SDK's data-collection policies, see [SDK data collection]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/).

{% alert important %}
If any of your non-Braze SDKs collect tracking data, you'll need to review those policies separately.
{% endalert %}

### Step 2: Add the Braze privacy manifest

[Download the Braze privacy manifest](https://github.com/braze-inc/braze-swift-sdk/blob/main/Sources/BrazeKitResources/Resources/PrivacyInfo.xcprivacy) from GitHub, then open your Xcode project and move the file into `Brazekit.bundle`.

### Step 3: Declare your tracking data

{% alert tip %}
For a full walkthrough, see [Tutorial: Privacy Tracking Data](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/e1-privacy-tracking/).
{% endalert %}

Open `AppDelegate.swift`, then list each [tracking property](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/trackingproperty/) you want to declare. Your declaration should be similar to the following, where `dateOfBirth`, `customEvent`, and `customAttribute` represent declared tracking properties. 

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

Next, configure your tracking list, so data points are added and removed automatically. In the following example, the tracking list is set to automatically update after a user accepts the Ad Tracking Transparency agreement.

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

## API tracking-data domains

The Braze Swift SDK helps you keep track of data you've collected by appending `-tracking` to the hostname of relevant API endpoints. For example, if you initialize the SDK with an endpoint of `sdk.iad-01.braze.com`, Braze will send your declared tracking data to `sdk-tracking.iad-01.braze.com`.
