## Utilizing the push error logs

Braze provides push notification errors within the message activity log. This error log provides a variety of warnings which can be very helpful for identifying why your campaigns aren't working as expected. Clicking on an error message will redirect you to relevant documentation to help you troubleshoot a particular incident.

![]({% image_buster /assets/img_archive/message_activity_log.png %})

## Troubleshooting scenarios

### No "push registered" users showing in the Braze dashboard (prior to sending messages)

- Ensure that your app is correctly configured to allow push notifications.
- Ensure that the Client ID and Client Secret configured in your Braze dashboard is correct.

### Push notifications not displayed on users' devices

There are a few reasons why this could be occurring:

- If you force quit your application, your push notifications will not be displayed while your app is not running.
- Make sure the [Notification Priority]({{ site.baseurl }}/developer_guide/platform_integration_guides/android/push_notifications/fireos/customization/advanced_settings/#notification-display-priority) setting is set to `HIGH` in your campaign.
- The ADM API key in your `api_key.txt` is incorrect or contains invalid characters.
- The `BrazeAmazonDeviceMessagingReceiver` is not properly registered in `AndroidManifest.xml` with intent filters for `<action android:name="com.amazon.device.messaging.intent.RECEIVE" />` and `<action android:name="com.amazon.device.messaging.intent.REGISTRATION" />`.

### "Push registered" users no longer enabled after sending messages

This typically occurs when users have uninstalled the application, causing their ADM Registration ID to become invalid.
