---
nav_title: Privacy manifest
article_title: Privacy manifest
page_order: 7
platform: Swift
description: "Learn how to declare your Braze tracking data in your app's privacy manifest."
---

# Privacy manifest

> If your Braze SDK collects tracking data, Apple requires you to add a privacy manifest that describes your reason and method for collecting tracking data.

## What is tracking data?

Apple defines "tracking data" as data collected in your app about an end-user or device that's linked to third-party data (such as targeted advertising), or a data broker. For a complete definition with examples, see [Apple: Tracking](https://developer.apple.com/app-store/app-privacy-details/#user-tracking).

By default, the Braze SDK does not collect tracking data. However, depending on your Braze SDK configuration, you may be required to list Braze-specific data in your app's privacy manifest.

## What is a privacy manifest?

A privacy manifest is a file in your Xcode project that describes the reason your app and third-party SDKs collect data, along with their data-collection methods. Each of your third-party SDKs that track data require its own privacy manifest. When you [create your app's privacy report](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests#4239187), these privacy manifest files are automatically aggregated into a single report.

## API tracking-data domains

Starting with iOS 17.2, Apple will block all declared tracking endpoints in your app until the end-user accepts an [Ad Tracking Transparency (ATT) prompt](https://support.apple.com/en-us/HT212025). Braze automatically reroutes this data to a dedicated `-tracking` endpoint, then sends the remaining non-tracking, first-party data to the original endpoint. For example:

- **Original endpoint:** `sdk.iad-01.braze.com`
- **Tracking endpoint:** `sdk-tracking.iad-01.braze.com`

## Declaring Braze tracking data

### Step 1: Review your current policies

Review your Braze SDK's current data-collection policies with your legal team to determine whether your app collects tracking data [as defined by Apple](#what-is-tracking-data). If you're not collecting any tracking data, you don't need to customize your privacy manifest for the Braze SDK at this time.

For more information about the Braze SDK's data-collection policies, see [SDK data collection]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/).

{% alert important %}
If any of your non-Braze SDKs collect tracking data, you'll need to review those policies separately.
{% endalert %}

### Step 2: Declare your tracking data

In your Xcode project, open `AppDelegate.swift` then list each [tracking property](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/trackingproperty/) you want to declare by creating a static or dynamic tracking list. Keep in mind, Apple will block these properties until the end-user accepts their ATT prompt, so only list properties you and your legal team consider tracking.

{% alert warning %}
Be sure to follow the guide to ensure you are setting [`adTrackingEnabled`](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/e1-privacy-tracking/#Respond-to-App-Tracking-Transparency-permissions) when users accept or decline the Ad Tracking Transparency Prompt. This will improve performance and retry logic within your app.
{% endalert %}

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
In the following example, the tracking list is automatically updated after the end-user accepts the ATT prompt. The `set(adTrackingEnabled: enableAdTracking)` method is used to handle the ATT permissions, which prevents the SDK from entering an infinite retry loop.

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

### Step 3: Update the `adTrackingEnabled` field

To ensure the Braze SDK does not continue to retry blocked tracking requests, be sure to set the `adTrackingEnabled` property when a user's tracking authorization status changes:

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
{% alert tip %}
For a full walkthrough, see the [Privacy Tracking Data tutorial](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/e1-privacy-tracking/).
{% endalert %}
