---
nav_title: Push Primer In-App Messages
article_title: Push Primer In-App Messages
page_order: 1
page_type: reference
description: "This article covers the prerequisites for push primer in-app messages and how to set them up."
channel: push

---

# Push primer in-app messages

![Push primer in-app message for streaming app. The notification reads "Get push notifications from Movie Cannon? Notifications may include new movies, TV shows, or other notices and can be turned off at any time."][1]{: style="float:right;max-width:40%;margin-left:15px;border:none;"}

> You only get one chance to ask users for push permission, so optimizing your push registration is crucial to maximize the reach of your push messages. To help achieve this, you can use in-app messages to explain what type of messages your users can expect to receive if they choose to opt in, before showing them the native push prompt. This is referred to as a push primer.

To create a push primer in-app message in Braze, you can use the button on-click behavior "Request Push Permission" when creating an in-app message for iOS, Android, or Web.

## Prerequisites

This guide uses a button [on-click behavior](#button-actions) that is only supported on newer SDK versions. Note that some of these SDKs may not be released yet. Visit the following links to check the current version:

{% sdk_min_versions swift:5.4.0 android:21.0.0 web:4.0.3 %}

### Notes for development teams

#### Android

- **Android 12 and under:** Implementing push primers is not recommended because push is opted-in by default.
- **Android 13 and above:** If you'd like to see the prompt several times while testing, go into device settings and disable push for the app to allow the primer to display again.

#### iOS

- The iOS prompt can be displayed only once per install, enforced by the operating system.
- The prompt will not display if the app's push setting is explicitly on or off, it will only display for users with [provisional authorization](https://developer.apple.com/documentation/usernotifications/asking_permission_to_use_notifications#3544375).
  - If we find the app's push setting is on, Braze does not show the in-app message as the user is already opted-in.
  - If the app's push setting is off, you should forward the user to the app's notification settings in the settings app.

##### Manual code removal

The in-app message that you set up using this tutorial will call the native push prompt code automatically when a user clicks on the in-app message button. To avoid requesting push notification permission twice, or at the wrong time, a developer should modify any existing push notification integration they implemented to make sure that your in-app message is the first push notification primer your users see.

The developer should review their implementation of push notifications for your app or site and manually remove any code that would request push permission. For example, look for and remove references to the following code:

{% tabs %}
{% tab OBJECTIVE-C %}
```objc
requestAuthorizationWithOptions
```
{% endtab %}
{% tab swift %}
```swift
requestAuthorization
```
{% endtab %}
{% tab JavaScript %}
```javascript
braze.requestPushPermission()
// or
appboy.registerAppboyPushMessages()
```
{% endtab %}
{% tab Java %}
```java
android.permission.POST_NOTIFICATIONS
```
{% endtab %}
{% endtabs %}

## Step 1: Create an in-app message

[Create an in-app message][2] as you usually would.

Select a message type and layout. To give you enough space to explain what push notifications your users can expect (and to allow for buttons), Braze suggests either a full screen or modal message. Note that for a fullscreen in-app message, an image is required. 

## Step 2: Build your message

Now it's time to add your copy! Remember that a push primer is supposed to prime the user to turn on push notifications. In your message body, we suggest highlighting the reasons your users should have push notifications turned on. Be specific about what type of notifications you want to send and what value they can provide.

For example, a news app might use the following push primer:

> Breaking news on the go! Enable push notifications to get alerts for major stories and topics that matter to you.

While a streaming app might use the following:

> Get push notifications from Movie Cannon? Notifications may include new movies, TV shows, or other notices and can be turned off at any time.

For best practices and additional resources, refer to [Creating custom opt-in prompts][3].

## Step 3: Specify button behavior {#button-actions}

To add buttons to your in-app message, drag two **Button** blocks into your message, which will act as the primary and secondary buttons in your in-app message. You can also drag a row into your message, and then drag the buttons into the row, so that the buttons are on the same horizontal row (as opposed to stacked on top of each other). We recommend "Allow notifications" and "Not now" as starter buttons, but there are many different button prompts you could assign.

After you've added button copy, specify the on-click behavior for each button:

- **Button 1:** Set this to "Close Message". This is your secondary button, or the "Not now" option.
- **Button 2:** Set this to "Request Push Permission". This is your primary button, or the "Allow notifications" option.

![In-app message composer with two buttons: "Allow notifications" and "Not now".][4]

## Step 4: Schedule delivery

To set your push primer to send at a relevant time, you must schedule your in-app message as an action-based message with **Perform Custom Event** as the trigger action.

While the ideal time will vary, Braze suggests waiting until a user completes some sort of [high-value action](https://www.braze.com/resources/videos/mapping-high-value-actions), indicating that they're starting to see value in your app or site, or when there's a compelling need that push notifications can address (such as after they've placed an order and you want to offer them shipping tracking information). This way, the prompt is beneficial to the customer rather than only to your brand.

![Action-based delivery settings to send to users who performed the custom event of "Add to Watch List".][5]

## Step 5: Target users

Since the goal of a push primer campaign is to prompt users to opt in to push messaging, you don't want to target users who are already opted in. To do so, add a segment or filter where `Push Subscription Status is not Opted In`.

Beyond that, you can decide what additional segments you feel are most appropriate. For example, you might target users that have completed a second purchase, users that have just made an account to become a member, or even users that visit your app more than twice a week. Targeting users for these crucial segments increases the likelihood of users opting in and becoming push enabled.

## Step 6: Conversion events

Braze suggests default settings for conversions, but you may want to set up [conversion events]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) surrounding push primers.

[1]: {% image_buster /assets/img_archive/push_primer_iam.png %}
[2]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/
[3]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/creating_custom_opt-in_prompts/
[4]: {% image_buster /assets/img_archive/push_primer_button_behavior.png %}
[5]: {% image_buster /assets/img_archive/push_primer_trigger.png %}
