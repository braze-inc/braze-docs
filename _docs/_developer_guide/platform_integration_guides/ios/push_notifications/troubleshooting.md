---
nav_title: Troubleshooting
article_title: Push Notification Troubleshooting for iOS
platform: iOS
page_order: 30
description: "This article covers potential troubleshooting topics for your iOS push implementation."
channel:
  - push

---

# Troubleshooting {#push-troubleshooting}

## Understanding the Braze/APNs workflow

The Apple Push Notification service (APNs) is Apple's infrastructure for push notifications sending to iOS and OS X applications. Here is the simplified structure of how push notifications are enabled for your users' devices and how Braze can send push notifications to them:

1. You configure the push certificate and provisioning profile
2. Devices register for APNs and provide Braze with push tokens
3. You launch a Braze push campaign
4. Braze removes invalid tokens

#### Step 1: Configuring the push certificate and provisioning profile

In developing your app, you'll need to create an SSL certificate to enable push notifications. This certificate will be included in the provisioning profile your app is built with and will also need to be uploaded to the Braze dashboard. The certificate allows Braze to tell APNs that we are allowed to send push notifications on your behalf.

There are two types of [provisioning profiles][2] and certificates: development and distribution. We recommend just using distribution profiles and certificates to avoid any confusion. If you choose to use different profiles and certificates for development and distribution, ensure that the certificate uploaded to the dashboard matches the provisioning profile you are currently using.

{% alert warning %}
Do not change the push certificate environment (development versus production). Changing the push certificate to the wrong environment can lead to your users having their push token accidentally removed, making them unreachable by push. 
{% endalert %}

#### Step 2: Devices register for APNs and provide Braze with push tokens

When users open your app, they will be prompted to accept push notifications. If they accept this prompt, APNs will generate a push token for that particular device. The iOS SDK will immediately and asynchronously send up the push token for apps using the default [automatic flush policy][40]. After we have a push token associated with a user, they will show as "Push Registered" in the dashboard on their user profile under the **Engagement** tab and will be eligible to receive push notifications from Braze campaigns.

{% alert note %}
This does not work with the iOS Simulator. You cannot test push notifications with the iOS Simulator as a result.
{% endalert %}

#### Step 3: Launching a Braze push campaign

When a push campaign is launched, Braze will make requests to APNs to deliver your message. Braze will use the SSL push certificate uploaded in the dashboard to authenticate and verify that we are allowed to send push notifications to the push tokens provided. If a device is online, the notification should be received shortly after the campaign has been sent. Note that Braze sets the default APNs [expiration date](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/sending_notification_requests_to_apns#2947607) for notifications to 30 days.

#### Step 4: Removing invalid tokens

If [APNs][20] informs us that any of the push tokens we were attempting to send a message to are invalid, we remove those tokens from the user profiles they were associated with.

## Utilizing the push error logs

Braze provides a log of push notification errors within the [message activity log][27]. This error log provides a variety of warnings which can be very helpful for identifying why your campaigns aren't working as expected. Clicking on an error message will redirect you to relevant documentation to help you troubleshoot a particular incident.

![Push error logs displaying the time the error occurred, the app name, the channel, error type, and error message.][26]

Common errors you might see here include user-specific notifications, such as ["Received Unregistered Sending to Push Token"][35].

In addition, Braze also provides a push changelog on the user profile under the **Engagement** tab. This changelog provides insight into push registration behavior such as token invalidation, push registration errors, tokens being moved to new users, etc.

![][1]{: style="max-width:50%;" }

## Push registration issues

To add verification for your application's push registration logic, implement Braze's [push unit testing][41].

#### No push registration prompt

If the application does not prompt you to register for push notifications, there is likely an issue with your push registration integration. Ensure you have followed our [documentation][21] and correctly integrated our push registration. You can also set breakpoints in your code to ensure the push registration code is running.

#### No "push registered" users showing in the dashboard

- Check that your app is prompting you to allow push notifications. Typically, this prompt will appear upon your first open of the app, but it can be programmed to appear elsewhere. If it does not appear where it should be, the problem is likely with the basic configuration of your app's push capabilities.
  - Verify the steps for [push integration][21] were successfully completed.
  - Check that the provisioning profile your app was built with includes permissions for push. Make sure that you're pulling down all of the available provisioning profiles from your Apple developer account. To confirm this, perform the following steps:
    1. In Xcode, navigate to **Preferences > Accounts** (Or use the keyboard shortcut <kbd>Command</kbd>+<kbd>,</kbd>).
    2. Select the Apple ID you use for your developer account and click **View Details**.
    3. On the next page, click **<i class="fas fa-redo-alt"></i> Refresh** and confirm that you're pulling all available provisioning profiles.
- Check you have [properly enabled push capability][29] in your app.
- Check your push provisioning profile matches the environment you're testing in. Universal certificates may be configured in the Braze dashboard to send to either the development or production APNs environment. Using a development certificate for a production app or a production certificate for a development app will not work.
- Check that you are calling our `registerPushToken` method by setting a breakpoint in your code.
- Check that you are on a device (push will not work on a simulator) and have good network connectivity.

## Devices not receiving push notifications

#### Users no longer "push registered" after sending a push notification

This would likely indicate that the user had an invalid push token. This can happen for several reasons:

##### Dashboard and app certificate mismatch

If the push certificate you uploaded in the dashboard is not the same one in the provisioning profile that your app was built with, APNs will reject the token. Verify that you have uploaded the correct certificate and completed another session in the app before attempting another test notification.

##### Uninstalls

If a user has uninstalled your application, their push token will be invalid and removed upon the next send.

##### Regenerating your provisioning profile

As a last resort, starting over fresh and creating a whole new provisioning profile can clear up configuration errors that come from working with multiple environments, profiles, and apps at the same time. There are many "moving parts" in setting up push notifications for iOS apps, so sometimes, it is best to retry from the beginning. This will also help isolate the problem if you need to continue troubleshooting.

#### Users still "push registered" after sending a push notification

##### App is foregrounded

On iOS versions that do not integrate push via the `UserNotifications` framework, if the app is in the foreground when the push message is received, it will not be displayed. You should background the app on your test devices before sending test messages.

##### Test notification scheduled incorrectly

Check the schedule you set for your test message. If it is set to local time zone delivery or [Intelligent Timing]({{site.baseurl}}/user_guide/intelligence/intelligent_timing/), you may have just not received the message yet (or had the app in the foreground when it was received).

#### User not "push registered" for the app being tested

Check the user profile of the user you are trying to send a test message to. Under the **Engagement** tab, there should be a list of "pushable apps". Verify the app you are trying to send test messages to is in this list. Users will show up as "Push Registered" if they have a push token for any app in your app group, so this could be something of a false positive.

The following would indicate a problem with push registration or that the user's token had been returned to Braze as invalid by APNs after being pushed:

![A user profile displaying the contact settings of a user. Here, you can see what apps push is registered for.][25]{: style="max-width:50%"}

## Message activity log errors

#### Received unregistered sending to push token {#received-unregistered-sending}

- Make sure that the push token being sent to Braze from the method `[[Appboy sharedInstance] registerPushToken:]` is valid. You can look in the [message activity log][27] to see the push token. It should look something like `6e407a9be8d07f0cdeb9e724733a89445f57a89ec890d63867c482a483506fa6`, a long string containing a mix of letters and numbers. If your push token looks different, check your [code][37] for sending Braze the push tokens.
- Ensure that your push provisioning profile matches the environment you're testing. Universal certificates may be configured in the Braze dashboard to send to either the development or production APNs environment. Using a development certificate for a production app or a production certificate for a development app will not work.
 - Check that the push token you have uploaded to Braze matches the provisioning profile you used to build the app you sent the push token from.

#### Device token not for topic

This error indicates that your app's push certificate and bundle ID are mismatched. Check that the push certificate you uploaded to Braze matches the provisioning profile used to build the app from which the push token was sent.

#### BadDeviceToken sending to push token

The `BadDeviceToken` is an APNs error code and does not originate from Braze. There could be a number of reasons for this response being returned, including the following:

- The app received a push token that was invalid for the credentials uploaded to the dashboard.
- Push was disabled for this app group.
- The user has opted out of push.
- The app was uninstalled.
- Apple refreshed the push token, which invalidated the old token.
- The app was built for a production environment, but the push credentials uploaded to Braze are set for a development environment (or the other way around).

## Issues after push delivery

To add verification for your application's push handling, implement Braze's [push unit tests][41] .

#### Push clicks not logged {#push-clicks-not-logged}

- If this is only occurring on iOS 10, make sure you have followed the push integration steps for [iOS 10][30].
- Braze does not handle push notifications received silently in the foreground (e.g., default foreground push behavior prior to the `UserNotifications` framework). This means that links will not be opened, and push clicks will not be logged. If your application has not yet integrated the `UserNotifications` framework, Braze will not handle push notifications when the application state is `UIApplicationStateActive`. You should ensure that your app does not delay calls to Braze's [push handling methods][30]; otherwise, the iOS SDK may treat push notifications as silent foreground push events and not handing them.

#### Web links from push clicks not opening

iOS 9+ requires links to be ATS compliant to be opened in web views. Ensure that your web links use HTTPS. Refer to our [ATS compliance][38] article for more information.

#### Deep links from push clicks not opening

Most of the code that handles deep links also handles push opens. First, ensure that push opens are being logged. If not, [fix that issue][34] (as the fix often fixes link handling).

If opens are being logged, check whether it is an issue with the deep link in general or with the deep linking push click handling. To do this, test to see if a deep link from an in-app message click works.

[1]: {% image_buster /assets/img_archive/push_changelog.gif %}
[20]: https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1
[21]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/
[25]: {% image_buster /assets/img_archive/registration_problem.png %}
[26]: {% image_buster /assets/img_archive/message_activity_log.png %}
[27]: https://dashboard-01.braze.com/app_settings/developer_console/activitylog/
[14]: https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/sending_notification_requests_to_apns#2947607
[2]: https://developer.apple.com/library/content/documentation/IDEs/Conceptual/AppDistributionGuide/MaintainingProfiles/MaintainingProfiles.html
[29]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/#step-2-enable-push-capabilities
[30]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/#step-5-enable-push-handling
[34]: #push-clicks-not-logged
[35]: #received-unregistered-sending
[37]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/#step-4-register-push-tokens-with-braze
[38]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/linking/#app-transport-security-ats
[40]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/fine_network_traffic_control/#automatic-request-processing
[41]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/unit_tests/

