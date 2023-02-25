---
hidden: true
nav_title: Live Activities
article_title: Live Activities for iOS
platform: Swift
page_order: 8
description: "This article covers using Braze to manage your Live Activities tokens."

---

# Live Activities for iOS

{% alert important %} 
Live Activities are currently in early access. Contact your Braze account manager if you're interested in participating in the early access. 
{% endalert %}

Live Activities are persistent, interactive notifications displayed on your lock screen, allowing you to keep an eye on things in real time. Because they appear on the lock screen, Live Activities ensure that your notifications won't be missed. Because they're persistent, you can display up-to-date content to your users without even having them unlock their phone. 

As a developer, you can use the Braze Swift SDK to easily manage Live Activity push tokens. You can use the Braze REST API to make Live Activity updates, and have all subscribed devices receive the update as quickly as possible. And, because you're managing Live Activities through Braze, you can use them in tandem with your other messaging channels&mdash;push notifications, in-app messages, Content Cards&mdash;to drive adoption. 

## Prerequisites 

Live Activities are only available for iPhones on iOS 16.1 and later. To use this feature, ensure that your project is targeting this iOS version.

<!--Placeholder to confirm Swift SDK version needed, remove when confirmed -->

{% sdk_min_versions swift:5.11.0 %}

## Implementing a Live Activity

To manage the lifecycle of a Live Activity, follow these four steps.

<!--TBD: Link to the headers -->

1. [Create the Live Activity.] Develop the Live Activity UI using WidgetKit and SwiftUI. Initialize a Live Activity object with the relevant data models for static and dynamic states.

2. [Register the Live Activity] Register a Live Activity with the Braze SDK using the `launchActivity` method with the Live Activity object and unique activity tag.

3. [Update the Live Activity] Publish activity content updates to the Live Activity using the Braze API endpoint `/messages/live_activity/update`.

4. [End the Live Activity] End a Live Activity for all recipients by publishing an update to `/messages/live_activity/update` with the parameter `"end_activity": true`.

## Step 1: Developing your Live Activity

<!--I see the word "activity" used in Apple's documentation somewhat generically. Is there a technical distinction between an "activity" and a "live activity"? . -->

First, ensure that you have followed [Displaying live data with Live Activities][3] in Apple’s documentation to set up Live Activities in your iOS application.

Because the exact nature of your Live Activity will be specific to your business case, you will need to set up and initialize these objects. Importantly, you will define:
* `ActivityAttributes`: This defines the static data at startup, that is, data that won’t change.
* `Activity.ContentState`: This defines the dynamic data that will be updated over the course of the activity.
* `ActivityContent`: An object that encapsulates the Live Activity's structure and additional configuration information.

You will also use SwiftUI to create the UI presentation of the lock screen. 

Make sure you're familiar with Apple's [prerequisites and limitations][2] for Live Activities, as these constraints are independent from Braze.

### Example

For this example, we have created a struct called `BrazeActivityAttributes`, but you may use your own implementation of [`ActivityAttributes`][4].

```swift
#if canImport(ActivityKit)
  import ActivityKit
#endif

@available(iOS 16.1, *)
struct BrazeActivityAttributes: ActivityAttributes {
  public struct ContentState: Codable, Hashable {
    var teamOneScore: String
    var teamTwoScore: String
  }

  var gameName: String
  var gameLocation: String
}
```

## Step 2: Registering a Live Activity

<!--Is integrating Swift push notifications a prerequisite for this step?. -->

Next, you will use Braze methods to track and manage your Live Activities. 

Updates to a Live Activity can be sent using ActivityKit (Apple’s framework for managing a Live Activity) or remote push notifications. You will use ActivityKit to get a push token, which the Braze SDK can manage for you.

1. Create an instance of your Live Activity implementation using Apple’s ActivityKit APIs.
2. Pass in the Live Activities `ActivitiesAttributes` and `ContentState` you defined. 
3. Register your activity with your Braze instance by passing it into [`launchActivity(pushTokenTag:activity:)`][5]. The `pushTokenTag` parameter is a custom string you define. It should be unique for each Live Activity you create.

Once you have registered the Live Activity, the Braze SDK will extract and observe changes in the push tokens.

<!--I found this sentence. What does it mean?. -->
It’ll be important to call out to customers that send frequent updates to update their app’s Info.plist settings in `Determine the update frequency`

### Example

For our example, we’ll create class called LiveActivityManager as an interface for our Live Activity objects. Then, we'll set the `pushTokenTag` to `"live-activity-1"`.

```swift
import BrazeKit

#if canImport(ActivityKit)
  import ActivityKit
#endif

class LiveActivityManager {
  
  @available(iOS 16.2, *)
  func createActivity() {
    let activityAttributes = BrazeActivityAttributes(gameName: "Superb Owl LVII", gameLocation: "Glendale, Arizona")
    let contentState = BrazeActivityAttributes.ContentState(teamOneScore: "0", teamTwoScore: "0")
    let activityContent = ActivityContent(state: contentState, staleDate: nil)
    if let activity = try? Activity.request(attributes: activityAttributes,
                                            content: activityContent) {
      // Register your Live Activity with Braze using the pushTokenTag
      AppDelegate.braze?.liveActivities.launchActivity(pushTokenTag: "live-activity-1",
                                                       activity: activity)
    }
  }
  
}
```

### Resuming Live Activity tracking

You will need to ensure that Braze tracks your Live Activity upon app launch.

To do this:
1. Open your `AppDelegate` file.
2. Import the `ActivityKit` module if it’s available.
3. Call [`resumeActivities(ofType:)`][6] in `application(_:didFinishLaunchingWithOptions:)` for all `ActivityAttributes` types you have registered in your application.

This allows Braze to resume tasks to track push token updates for all active Live Activities.

#### Example

```swift
import UIKit
import BrazeKit

#if canImport(ActivityKit)
  import ActivityKit
#endif

@main
class AppDelegate: UIResponder, UIApplicationDelegate {

  static var braze: Braze? = nil

  func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
  ) -> Bool {
    
    if #available(iOS 16.1, *) {
      Self.braze?.liveActivities.resumeActivities(
        ofType: Activity<BrazeActivityAttributes>.self
      )
    }

    return true
  }
}
```

## Step 3: Updating a Live Activity

We offer the `/messages/live_activity/update` endpoint as an easy way to manage the push tokens of a Live Activity. Use this endpoint to pass changes to your `ActivitiesAttributes` and `ContentState` as you want to update your Live Activity.

See the [`/messages/live_activity/update`][1] endpoint documentation for full details.

### Example

## Step 4: Ending a Live Activity 



[1]: {{site.baseurl}}/api/endpoints/messaging/live_activity/update
[2]: https://developer.apple.com/documentation/activitykit/displaying-live-data-with-live-activities#Understand-constraints
[3]: https://developer.apple.com/documentation/activitykit/displaying-live-data-with-live-activities
[4]: https://developer.apple.com/documentation/activitykit/activityattributes
[5]: braze-swift-sdk/documentation/brazekit/braze/liveactivities-swift.class/
[6]: braze-swift-sdk/documentation/brazekit/braze/liveactivities-swift.class/resumeactivities(oftype:)