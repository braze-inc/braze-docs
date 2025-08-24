---
nav_title: Silent Push Notifications Guide
article_title: Silent Push Notifications Guide
page_order: 4
page_type: reference
description: "This comprehensive guide covers silent push notifications across platforms, including implementation, troubleshooting, and best practices."
channel: push
---

# Silent push notifications guide

> Silent push notifications allow you to send data to your apps without alerting users. They're used to update content in the background, refresh data, synchronize state, and support features like geofencing, uninstall tracking, and feature flag syncing.

## How silent push notifications work

![A visual diagram showing how silent push notifications flow from the server to the user's device without displaying UI]({% image_buster /assets/img/silent_push_flow.png %}){: style="max-width:75%;"}

Silent push notifications differ from standard push notifications in a few key ways:

| Regular Push | Silent Push |
|-------------|-------------|
| Displays message and/or sound | No visible UI or sound |
| Requires user interaction | Processes data in the background |
| Counted in push analytics | May not appear in standard analytics |
| Throttled by OS algorithms | Subject to stricter OS limitations |
{: .reset-td-br-1 .reset-td-br-2}

## Implementation by platform

{% tabs %}
{% tab iOS %}

### iOS silent push notifications

To implement silent push notifications on iOS:

1. **Enable background modes**:
   - In Xcode, select your target
   - Go to **Signing & Capabilities** tab
   - Add the **Background Modes** capability
   - Enable **Remote notifications**

   ![Xcode showing the "remote notifications" mode checkbox under "capabilities".]({% image_buster /assets/img_archive/background_mode.png %})

2. **Send silent notifications**:
   - Set `content-available: 1` in your push payload
   - **Do not include** `title` or `body` fields to ensure the notification remains silent
   - Optionally include `custom_data` to pass information to your app

3. **Handle in your app**:
   - Implement `application:didReceiveRemoteNotification:fetchCompletionHandler:` method
   - Process the notification data and perform background work
   - Call the completion handler with appropriate result

```swift
func application(
  _ application: UIApplication,
  didReceiveRemoteNotification userInfo: [AnyHashable: Any],
  fetchCompletionHandler completionHandler: @escaping (UIBackgroundFetchResult) -> Void
) {
  // Check if this is a Braze internal notification (optional)
  if !Braze.Notifications.isInternalNotification(userInfo) {
    // Process your silent notification
    // Update data, refresh content, etc.
    completionHandler(.newData) // or .noData or .failed
  } else {
    completionHandler(.noData)
  }
}
```

{% alert important %}
The system will not launch your app into the background if the user has force-quit it. The user must explicitly launch the app or reboot the device before it can be launched automatically in the background.
{% endalert %}

### iOS limitations

iOS imposes several limitations on silent push notifications:

- **Throttling**: iOS may throttle delivery based on device state, battery level, and frequency
- **Priority**: Lower priority than user-visible notifications
- **Coalescing**: Multiple silent notifications may be delivered together
- **App state**: Not delivered if the app is in the foreground
- **App force-quit**: Not delivered if the user has force-quit the app
- **Documentation**: See Apple's [documentation on pushing background updates](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/pushing_background_updates_to_your_app)

{% endtab %}
{% tab Android %}

### Android silent push notifications

To implement silent push notifications on Android:

1. **Configure your app**:
   - Ensure you have FCM set up with Braze
   - Use a Firebase service to handle incoming silent push notifications

2. **Send silent notifications**:
   - Use the `send_to_sync: true` flag in your push payload
   - **Do not include** `title` or `alert` fields, as they will cause errors when used with `send_to_sync`
   - Optionally include `extras` to pass additional data

3. **Handle in your app**:
   - Implement a Firebase Messaging Service
   - Process the notification data in `onMessageReceived`

```java
public class MyFirebaseMessagingService extends FirebaseMessagingService {
  @Override
  public void onMessageReceived(RemoteMessage remoteMessage) {
    if (remoteMessage.getData().size() > 0) {
      // Process your silent notification data
      // Update app state, refresh content, etc.
    }
  }
}
```

### Android limitations

Android has fewer limitations on silent push notifications than iOS, but still has some constraints:

- **Battery optimization**: Devices with battery optimization may delay delivery
- **Background restrictions**: Android may restrict background processing on some devices
- **Vendor customizations**: Some OEM-specific Android versions limit background operations
- **Android 12+**: Additional restrictions on background activities

{% endtab %}
{% tab Web %}

### Web push silent notifications

Web push silent notifications work differently than mobile:

1. **Configure your service worker**:
   - Set up a service worker to handle push events
   - Register for push notifications

2. **Send silent notifications**:
   - Send a push without notification data
   - Include custom data in the payload

3. **Handle in your service worker**:
   - Process the push event without showing a notification
   - Update your web app state

```javascript
// In your service worker
self.addEventListener('push', function(event) {
  const data = event.data.json();
  
  // Check if this is a silent notification
  if (data.silent === true) {
    // Process silent notification without showing UI
    // Update caches, sync data, etc.
    
    // No need to show notification
    return;
  }
  
  // Regular notification handling...
});
```

### Web limitations

Web push has its own set of limitations:

- **Browser visibility**: Some browsers prioritize push events differently based on site engagement
- **Throttling**: Browsers may throttle push messages from sites with low engagement
- **Service worker**: Requires an active service worker to process messages
- **User permissions**: Still requires user permission for push (even silent ones)

{% endtab %}
{% endtabs %}

## Setting up in the Braze dashboard

### Configuration in the dashboard

To send a silent push notification via the Braze dashboard:

1. Create a new push campaign or Canvas step
2. Build your push notification normally
3. Go to the **Settings** tab in the push composer
4. Enable the appropriate silent push option:
   - iOS: Check the **Content-Available** checkbox
   - Android: Check the **Send to Sync** checkbox
5. **Important**: Remove any text from the **Title** and **Message** fields to ensure the notification remains silent

![The Braze dashboard showing the "content-available" checkbox found in the "settings" tab of the push composer.]({% image_buster /assets/img_archive/remote_notification.png %})

{% alert warning %}
**Dashboard Preview vs. Reality**: The dashboard preview will show a visual representation of your push notification even for silent pushes. This is for clarity in the composer but does not represent the actual behavior on the device, where silent pushes will not display UI.
{% endalert %}

### Configuration via API

To send a silent push notification via the Braze API:

#### iOS Example:
```json
{
  "apple_push": {
    "content-available": true,
    "custom_data": {
      "your_key": "your_value"
    }
  }
}
```

#### Android Example:
```json
{
  "android_push": {
    "send_to_sync": true,
    "extras": {
      "your_key": "your_value"
    }
  }
}
```

#### Web Example:
```json
{
  "web_push": {
    "silent": true,
    "custom_data": {
      "your_key": "your_value"
    }
  }
}
```

## Badge count with silent push

{% tabs %}
{% tab iOS %}

On iOS, you can update the app badge count with a silent push notification:

1. Enable the **Content-Available** flag in your push
2. Set a badge number in your push payload
3. Do not include a title or message

### Via Dashboard:
![Setting badge count with content-available in the dashboard]({% image_buster /assets/img/badge_count_silent_push.png %})

### Via API:
```json
{
  "apple_push": {
    "badge": 5,
    "content-available": true
  }
}
```

{% alert note %}
To use badge count in the composer, the `badge_count_in_composer` feature flag must be enabled for your app group. Contact support to enable this feature.
{% endalert %}

{% endtab %}
{% tab Android %}

On Android 8.0+ devices, you can set a notification badge with a silent push, but the implementation varies by device manufacturer:

```json
{
  "android_push": {
    "send_to_sync": true,
    "notification_count": 5
  }
}
```

Note that Android automatically handles app badging for push, so there are no customization settings for badging in Braze.

{% endtab %}
{% endtabs %}

## Common use cases

### Data synchronization

Use silent push to trigger a sync operation in your app:

```json
{
  "apple_push": {
    "content-available": true,
    "custom_data": {
      "sync_type": "full_refresh",
      "priority": "high"
    }
  }
}
```

### Content pre-fetching

Pre-fetch content before the user opens the app:

```json
{
  "apple_push": {
    "content-available": true,
    "custom_data": {
      "fetch_content": true,
      "content_ids": ["article123", "video456"]
    }
  }
}
```

### Geofence updates

Update geofence data for location-based features:

```json
{
  "apple_push": {
    "content-available": true,
    "custom_data": {
      "update_geofences": true,
      "region_id": "downtown"
    }
  }
}
```

### Feature flag sync

Trigger your app to check for updated feature flags:

```json
{
  "apple_push": {
    "content-available": true,
    "custom_data": {
      "feature_flags_sync": true
    }
  }
}
```

## Troubleshooting

### Common issues and solutions

| Issue | Possible Causes | Solution |
|-------|----------------|----------|
| **Silent push not received** | • App force-quit<br>• OS limitations<br>• Low battery<br>• High frequency | • Check device logs<br>• Verify implementation<br>• Reduce frequency<br>• Use high priority only when needed |
| **App not waking up** | • Missing background capability<br>• Implementation error | • Check Xcode capabilities<br>• Verify handler implementation<br>• Test with debugger attached |
| **Dashboard shows notification but device is silent** | • Dashboard preview vs. reality<br>• Title/body included | • Normal behavior - preview is visual<br>• Remove title and body fields |
| **Badge count not updating** | • Feature flag not enabled<br>• Implementation issue | • Contact support to enable `badge_count_in_composer`<br>• Verify badge number is included |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### Debugging silent push

#### iOS:
1. Attach your device to Xcode
2. Enable console logging
3. Filter console logs with: `process:tccd OR process:UserNotificationsServer OR process:SpringBoard`
4. Send a test silent push
5. Look for logs indicating reception or failure

#### Android:
1. Enable adb logging
2. Filter logs with: `adb logcat -s "FCM", "FirebaseMessaging"`
3. Send a test silent push
4. Check logs for message reception and processing

### Delivery analytics

Silent push notifications may not appear in standard push analytics. To track delivery:

1. Include a unique identifier in your silent push payload
2. When received, log a custom event with that identifier
3. Compare sent vs. received counts to measure delivery rate

## Best practices

- **Battery efficiency**: Limit the frequency of silent pushes to preserve battery life
- **Graceful degradation**: Design your app to work even if silent pushes fail
- **Critical data**: Don't rely solely on silent push for mission-critical data delivery
- **Prioritization**: Know that user-facing notifications take priority over silent ones
- **Error handling**: Implement robust error handling for failed background operations
- **Testing**: Test across different OS versions and device states (low battery, poor connection, etc.)
- **Fallbacks**: Implement fallback mechanisms like periodic background fetch
- **Rate limiting**: Implement server-side rate limiting to avoid OS throttling
- **Internal notifications**: Use `Braze.Notifications.isInternalNotification` to avoid conflicts with Braze's system notifications

## Related links

- [Push Notification Setup]({{site.baseurl}}/developer_guide/push_notifications/)
- [Badge Count Guide]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/utilizing_badge_count/)
- [iOS Background Modes](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/pushing_background_updates_to_your_app)
- [Android Background Processing Guide]({{site.baseurl}}/developer_guide/platforms/android/background_processing/)