---
nav_title: Push primer In-App messages
article_title: Push Primer In-App Messages
page_order: 1
page_type: reference
description: "This article covers the prerequisites for push primer in-app messages and how to set them up."
channel: push

---

# Push primer in-app messages

![Push primer in-app message for streaming app. The notification reads "Get push notifications from Movie Cannon? Notifications may include new movies, TV shows, or other notices and can be turned off at any time."]({% image_buster /assets/img_archive/push_primer_iam.png %}){: style="float:right;max-width:40%;margin-left:15px;border:none;"}

> You only get one chance to ask users for push permission, so optimizing your push registration is crucial to maximize the reach of your push messages. To help achieve this, you can use in-app messages to explain what type of messages your users can expect to receive if they choose to opt in, before showing them the native push prompt. This is referred to as a push primer.

To create a push primer in-app message in Braze, you can use the button on-click behavior "Request Push Permission" when creating an in-app message for iOS, Android, or Web.

## Prerequisites

This feature requires [button on-click behavior](#button-actions), which is supported in the following minimum versions or later:

{% sdk_min_versions swift:5.4.0 android:21.0.0 web:4.0.3 %}

Additionally, note the following platform-specific details:

{% tabs local %}
{% tab android %}
|OS version|Additional information|
|----------|----------------------|
| **Android 12 and earlier** | Implementing push primers is not recommended because push is opted-in by default. |
| **Android 13+** | If a user denies your push permission prompt twice, Android blocks further prompts—including Braze push primer messages. To grant permission after this, users must manually enable push for your app in their device settings. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% endtab %}

{% tab swift %}
### General information

- The push prompt can be displayed only once per install, enforced by the operating system.
- The prompt will not display if the app's push setting is explicitly on or off, it will only display for users with [provisional authorization](https://developer.apple.com/documentation/usernotifications/asking_permission_to_use_notifications#3544375).
  - **App's push setting is on:** Braze will not show the in-app message, as the user has already opted-in.
  - **App's push setting is off:** You'll need to redirect the user to your app's push notification settings within the device settings.

### Manual code removal

The in-app message that you set up using this tutorial will call the native push prompt code automatically when a user clicks on the in-app message button. To avoid requesting push notification permission twice, or at the wrong time, a developer should modify any existing push notification integration they implemented to make sure that your in-app message is the first push notification primer your users see.

Your development team should review your implementation of push notifications for your app or site and manually remove any code that would request push permission. For example, you would remove references to the following code:

{% subtabs %}
{% subtab OBJECTIVE-C %}
```objc
requestAuthorizationWithOptions
```
{% endsubtab %}
{% subtab swift %}
```swift
requestAuthorization
```
{% endsubtab %}
{% subtab JavaScript %}
```javascript
braze.requestPushPermission()
// or
appboy.registerAppboyPushMessages()
```
{% endsubtab %}
{% subtab Java %}
```java
android.permission.POST_NOTIFICATIONS
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Step 1: Create an in-app message

First, [create an in-app message]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/), then select your message type and layout.

To ensure you have enough space for both your message and buttons, use a fullscreen or modal message layout. If you choose fullscreen, note that an image is required.

## Step 2: Build your message

Now it's time to add your copy! Remember that a push primer is supposed to prime the user to turn on push notifications. In your message body, we suggest highlighting the reasons your users should have push notifications turned on. Be specific about what type of notifications you want to send and what value they can provide.

For example, a news app might use the following push primer:

```plaintext
Breaking news on the go! Enable push notifications to get alerts for major stories and topics that matter to you.
```

While a streaming app might use the following:

```plaintext
Get push notifications from Movie Cannon? Notifications may include new movies, TV shows, or other notices and can be turned off at any time.
```

For best practices and additional resources, refer to [Creating custom opt-in prompts]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/).

## Step 3: Specify button behavior {#button-actions}

To add buttons to your in-app message, drag two **Button** blocks into your message, which will act as the primary and secondary buttons in your in-app message. You can also drag a row into your message, and then drag the buttons into the row, so that the buttons are on the same horizontal row (as opposed to stacked on top of each other). We recommend "Allow notifications" and "Not now" as starter buttons, but there are many different button prompts you could assign.

After you've added button copy, specify the on-click behavior for each button:

- **Button 1:** Set this to "Close Message". This is your secondary button, or the "Not now" option.
- **Button 2:** Set this to "Request Push Permission". This is your primary button, or the "Allow notifications" option.

![In-app message composer with two buttons: "Allow notifications" and "Not now".]({% image_buster /assets/img_archive/push_primer_button_behavior.png %})

## Step 4: Schedule delivery

To set your push primer to send at a relevant time, you must schedule your in-app message as an action-based message with **Perform Custom Event** as the trigger action.

While the ideal time will vary, Braze suggests waiting until a user completes some sort of [high-value action](https://www.braze.com/resources/videos/mapping-high-value-actions), indicating that they're starting to see value in your app or site, or when there's a compelling need that push notifications can address (such as after they've placed an order and you want to offer them shipping tracking information). This way, the prompt is beneficial to the customer rather than only to your brand.

![Action-based delivery settings to send to users who performed the custom event of "Add to Watch List".]({% image_buster /assets/img_archive/push_primer_trigger.png %})

## Step 5: Target users

Since the goal of a push primer campaign is to prompt users to opt in to push messaging, you don't want to target users who are already opted in. To do so, add a segment or filter where `Push Subscription Status is not Opted In`.

Beyond that, you can decide what additional segments you feel are most appropriate. For example, you might target users that have completed a second purchase, users that have just made an account to become a member, or even users that visit your app more than twice a week. Targeting users for these crucial segments increases the likelihood of users opting in and becoming push enabled.

## Step 6: Conversion events

Braze suggests default settings for conversions, but you may want to set up [conversion events]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) surrounding push primers.

