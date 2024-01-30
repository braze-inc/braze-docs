---
nav_title: Apple Privacy Manifest
article_title: Apple Privacy Manifest
page_order: 7
platform: 
  - iOS
description: "This article describes the Braze Privacy Manifest used to declare data collection in your iOS app"
---

# Apple Privacy Manifest

The [Privacy Manifest](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files) is a file published alongside the Braze Swift SDK that describes the data collection practices and "required reasons" APIs.

By default, Braze does not collect any "[tracking data](https://developer.apple.com/app-store/app-privacy-details/#user-tracking)" which Apple describes as data collected and shared with 3rd parties.

The Braze privacy manifest, along with other privacy manifests you collect from other SDKs used, will be aggregated and displayed in the App Store to form your Privacy Nutrition label.

If you collect other 1st party data in your app, be sure to include that when generating your [Privacy Report](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests#4239187) in Xcode.

As of iOS 17.2, Apple will block any "tracking data" by default, until the user accepts the Ad Tracking Transparency prompt.

## Data Collection

You can review the default data collection policies in our [SDK Data Collection Guide](https://www.braze.com/docs/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/). This list includes attributes the Braze SDK collects to help brands perform better 1st party messaging and segmentation to power meaningful engagement between brands and their users.

Remember, you can always [opt-out](https://www.braze.com/docs/developer_guide/platform_integration_guides/sdk_primer#blocking-data-collection) of the optional data points the Braze SDK collects by default, and your integration determines what additional custom events and attributes you collect.

## Tracking vs. Non-Tracking Data

In addition the default data Braze declares in the Privacy Manifest, you may choose to add additional data to declare as "tracking" prior to publishing your app.

Apple requires that you declare which data types you collect are used for "tracking" vs. "non-tracking" usage. The Braze Swift SDK provides flexible APIs to help you adhere to Apple policies while ensure end-users' privacy is respected.

To support this privacy enhancement, Braze has added new features to our Swift SDK:

### New Tracking Domains

Braze has added new SDK API domains intended for "tracking" data. These domains will prefix `tracking-` to the hostname of your API endpoint and is automatically configured with no integration update needed. For example, if you initialize the SDK with an endpoint of `sdk.iad-01.braze.com`, Braze will send your declared tracking data to `sdk-tracking.iad-01.braze.com`.

### Declaring Tracking Data

If you choose to collect user information through the Braze Swift SDK with plans to use this data for [tracking](https://developer.apple.com/app-store/app-privacy-details/#user-tracking) (as described by Apple), you will need to declare this data when submitting your app to the App Store.

Braze provides a [flexible approach](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/e1-privacy-tracking/) allowing you to dynamically add and remove individual data points from your tracking list.

For example, to include date of birth, and a few custom events and attributes in your "tracking" list, use the sample code below to reroute these individual data points to the Braze tracking domain. These data points will require a user to have accepted the Ad Tracking Transparency prompt in order to be send succesfully.

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


To dynamically update (add or remove) data points from your tracking configuration - for example, after a user accepts the Ad Tracking Transparency prompt:

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

For a complete tutorial, see our [Braze Swift SDK Tutorial on Privacy Tracking](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/e1-privacy-tracking/).
