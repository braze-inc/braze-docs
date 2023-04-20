---
nav_title: Live Activities
article_title: Live Activities for iOS
platform: Swift
page_order: 1
description: "This article covers using Braze to manage your Live Activities tokens."

---

# Live Activities for iOS

{% alert important %} 
Live Activities are currently in early access. Contact your Braze account manager if you're interested in participating. 
{% endalert %}

Live Activities are persistent, interactive notifications displayed on your lock screen, allowing you to keep an eye on things in real-time. Because they appear on the lock screen, Live Activities ensure that your notifications won't be missed. Because they're persistent, you can display up-to-date content to your users without even having them unlock their phone. 

![A delivery tracker live activity on an iPhone lockscreen. A status bar with a car is almost half-way filled up. Text reads "2 min until pickup"][7]{: style="max-width:40%;float:right;margin-left:15px;"}

Live Activities present a combination of static information and dynamic information that you update. For example, you can create a Live Activity that provides a status tracker for a delivery. This Live Activity would have your company's name as static information, as well as a dynamic "Time to delivery" that would be updated as the delivery driver approaches its destination.

As a developer, you can use Braze to manage your Live Activity lifecycles, make calls to the Braze REST API to make Live Activity updates, and have all subscribed devices receive the update as quickly as possible. And, because you're managing Live Activities through Braze, you can use them in tandem with your other messaging channels&mdash;push notifications, in-app messages, Content Cards&mdash;to drive adoption. 

## Prerequisites 

{% sdk_min_versions swift:5.11.0 %}

Additional prerequisites include:
* Live Activities are only available for iPhones on iOS 16.1 and later. To use this feature, ensure that your project is targeting this iOS version.
* The `Push Notification` entitlement must be added under **Signing & Capabilities** in your Xcode project.

{% alert note %}
Note that, whereas Live Activities function similarly to push notifications, they are controlled by different user settings. A user can opt into Live Activities but out of push notifications, and vice versa.
{% endalert %}

## Implementing a Live Activity

To manage the lifecycle of a Live Activity, follow these four steps.

1. [Create the Live Activity.](#developing) Develop the Live Activity UI using WidgetKit and SwiftUI. Initialize a Live Activity object with the relevant data models for your static and dynamic states.<br><br>

2. [Register the Live Activity](#registering) Register a Live Activity with the Braze SDK using the [`launchActivity`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/liveactivities-swift.class/launchactivity(pushtokentag:activity:fileid:line:)) method with the Live Activity object and unique activity tag.<br><br>

3. [Update the Live Activity](#updating) Publish updates to the Live Activity using the Braze [`/messages/live_activity/update`]({{site.baseurl}}/api/endpoints/messaging/live_activity/update) API endpoint.<br><br>

4. [End the Live Activity](#ending) End a Live Activity for all recipients by publishing an update to [`/messages/live_activity/update`]({{site.baseurl}}/api/endpoints/messaging/live_activity/update) with the parameter `"end_activity": true`.

## Step 1: Developing your Live Activity {#developing}

First, ensure that you have followed [Displaying live data with Live Activities][3] in Apple’s documentation to set up Live Activities in your iOS application. As part of this task, make sure you include `NSSupportsLiveActivities` set to `YES` in your `Info.plist`. 

Because the exact nature of your Live Activity will be specific to your business case, you will need to set up and initialize the [Activity][4] objects. Importantly, you will define:
* `ActivityAttributes`: This protocol defines the static (unchanging) and dynamic (changing) content that will appear in your Live Activity.
* `ActivityAttributes.ContentState`: This type defines the dynamic data that will be updated over the course of the activity.

You will also use SwiftUI to create the UI presentation of the lock screen and Dynamic Island on supported devices. 

Make sure you're familiar with Apple's [prerequisites and limitations][2] for Live Activities, as these constraints are independent from Braze.

{% alert note %}
If you expect to send frequent pushes to the same Live Activity, you can avoid being throttled by Apple's budget limit by setting `NSSupportsLiveActivitiesFrequentUpdates` to `YES` in your `Info.plist` file. For more details, refer to the [`Determine the update frequency`](https://developer.apple.com/documentation/activitykit/updating-and-ending-your-live-activity-with-activitykit-push-notifications#Determine-the-update-frequency) section in the ActivityKit documentation.
{% endalert %}

### Example

Let's imagine that we want to create a Live Activity to give our users updates for the Superb Owl show, where two competing wildlife rescues are given points for the owls they have in residence. For this example, we have created a struct called `BrazeActivityAttributes`, but you may use your own implementation of `ActivityAttributes`.

```swift
#if canImport(ActivityKit)
  import ActivityKit
#endif

@available(iOS 16.1, *)
struct BrazeActivityAttributes: ActivityAttributes {
  public struct ContentState: Codable, Hashable {
    var teamOneScore: Int
    var teamTwoScore: Int
  }

  var gameName: String
  var gameNumber: String
}
```

## Step 2: Registering a Live Activity {#registering}

Next, you will use Braze methods to track and manage your Live Activities. 

Updates to a Live Activity can be sent using ActivityKit (Apple’s framework for managing a Live Activity) or remote push notifications. In this instance, you will use ActivityKit to get a push token, which the Braze SDK can manage for you. This allows you to update Live Activities through the Braze API, as Braze will send the push token to the Apple Push Notification service (APNs) on the backend.

1. Create an instance of your Live Activity implementation using Apple’s ActivityKit APIs.
2. Set the `pushType` parameter as `.token`. 
3. Pass in the Live Activities `ActivitiesAttributes` and `ContentState` you defined. 
4. Register your activity with your Braze instance by passing it into [`launchActivity(pushTokenTag:activity:)`][5]. The `pushTokenTag` parameter is a custom string you define. It should be unique for each Live Activity you create.

Once you have registered the Live Activity, the Braze SDK will extract and observe changes in the push tokens.

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
    let activityAttributes = BrazeActivityAttributes(gameName: "Superb Owl", gameNumber: "Game 1")
    let contentState = BrazeActivityAttributes.ContentState(teamOneScore: "0", teamTwoScore: "0")
    let activityContent = ActivityContent(state: contentState, staleDate: nil)
    if let activity = try? Activity.request(attributes: activityAttributes,
                                            content: activityContent,
      // Setting your pushType as .token allows the Activity to generate push tokens for the server to watch.
                                            pushType: .token) {
      // Register your Live Activity with Braze using the pushTokenTag
      AppDelegate.braze?.liveActivities.launchActivity(pushTokenTag: "live-activity-1",
                                                       activity: activity)
    }
  }
  
}
```

Your Live Activity widget would display this initial content to your users. 

![A live activity on an iPhone lockscreen with two team's scores. Both the Wild Bird Fund and the Owl Rehab teams have scores of 0.][8]{: style="max-width:40%;"}

### Resuming Live Activity tracking

You will need to ensure that Braze tracks your Live Activity upon app launch.

To do this:
1. Open your `AppDelegate` file.
2. Import the `ActivityKit` module if it’s available.
3. Call [`resumeActivities(ofType:)`][6] in `application(_:didFinishLaunchingWithOptions:)` for all `ActivityAttributes` types you have registered in your application.

This allows Braze to resume tasks to track push token updates for all active Live Activities. Note that if a user has explicitly dismissed the Live Activity on their device, it is considered removed, and Braze will no longer track it.

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

## Step 3: Updating a Live Activity {#updating}

![A live activity on an iPhone lock screen with two team's scores. Both the Wild Bird Fund has 2 points and the Owl Rehab  has 4 points.][9]{: style="max-width:40%;float:right;margin-left:15px;"}

The [`/messages/live_activity/update`][1] endpoint allows you to update a Live Activity through push notifications passed through the Braze REST API. Use this endpoint to update your Live Activity's `ContentState`.

As you update your `ContentState`, your Live Activity widget will display the new information. Here's what the Superb Owl show might look like at the end of the first half.

See the [`/messages/live_activity/update`][1] endpoint documentation for full details.

## Step 4: Ending a Live Activity {#ending}

When a Live Activity is active, it is shown on both a user's lock screen and Dynamic Island. There are a few different ways for a Live Activity to end and be removed from a user's UI. 

* **User dismissal**: A user can manually dismiss a Live Activity.
* **Time out**: After a default time of 8 hours, iOS will remove the Live Activity from the user's Dynamic Island. After a default time of 12 hours, iOS will remove the Live Activity from the user's lock screen. 
* **Dismissal date**: You can provide a datetime for a Live Activity to be removed from a user's UI prior to time out. This is defined either in the Activity's `ActivityUIDismissalPolicy` or using the `dismissal_date` parameter in requests to the `/messages/live_activity/update` endpoint.
* **End activity**: You can set `end_activity` to `true` in a request to the `/messages/live_activity/update` endpoint to immediately end a Live Activity.

See the [`/messages/live_activity/update`][1] endpoint documentation for full details.

[1]: {{site.baseurl}}/api/endpoints/messaging/live_activity/update
[2]: https://developer.apple.com/documentation/activitykit/displaying-live-data-with-live-activities#Understand-constraints
[3]: https://developer.apple.com/documentation/activitykit/displaying-live-data-with-live-activities
[4]: https://developer.apple.com/documentation/activitykit/activityattributes
[5]: https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/liveactivities-swift.class
[6]: https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/liveactivities-swift.class/resumeactivities(oftype:)
[7]: {% image_buster /assets/img/LiveActivities3.png %}
[8]: {% image_buster /assets/img/LiveActivities1.png %}
[9]: {% image_buster /assets/img/LiveActivities2.png %}