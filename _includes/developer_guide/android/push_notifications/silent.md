{% multi_lang_include developer_guide/prerequisites/android.md %} You'll also need to [set up push notifications]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android).

## Setting up silent push notifications

Silent notifications are available through the Braze [Messaging API]({{site.baseurl}}/api/endpoints/messaging/). To take advantage of them, you need to set the `send_to_sync` flag to `true` within the [Android push object]({{site.baseurl}}/api/objects_filters/messaging/android_object/) and ensure there are no `title` or `alert` fields set as it will cause errors when used alongside `send_to_sync`&#8212;however, you can include data `extras` within the object.

### Handling silent push notifications

To handle silent push notifications in your Android app, you'll need to implement a service that extends `FirebaseMessagingService`:

```java
public class MyFirebaseMessagingService extends FirebaseMessagingService {
  @Override
  public void onMessageReceived(RemoteMessage remoteMessage) {
    Map<String, String> data = remoteMessage.getData();
    
    // Check if this is a silent push (no notification payload)
    if (remoteMessage.getNotification() == null) {
      // Handle your silent push data here
      // Update content, sync data, etc.
    }
  }
}
```

Don't forget to register this service in your `AndroidManifest.xml`:

```xml
<service
  android:name=".MyFirebaseMessagingService"
  android:exported="false">
  <intent-filter>
    <action android:name="com.google.firebase.MESSAGING_EVENT" />
  </intent-filter>
</service>
```

### Dashboard preview vs. actual behavior

{% alert note %}
**Important:** The Braze dashboard preview will display a visual representation of your push notification even for silent pushes. This is for preview purposes only and does not reflect how the notification will behave on a device. On the device, properly configured silent notifications will not display any UI or play any sounds.
{% endalert %}

## Android limitations

Android silent push notifications have fewer limitations than iOS, but there are still some considerations:

- **Battery optimization**: On devices with battery optimization enabled, silent push delivery may be delayed
- **Background restrictions**: Android may restrict background processing on some devices, especially in Doze mode
- **Vendor customizations**: Some OEM-specific Android versions (like MIUI, EMUI) may have additional restrictions
- **Android 12+**: Additional restrictions on background activities and silent notifications for apps that haven't been recently used

## Best practices

For reliable silent push notifications:

1. **Keep payloads small**: Large payloads may be rejected or delayed
2. **Handle gracefully**: Design your app to function even if silent pushes are delayed or missed
3. **Test on multiple devices**: Different Android versions and OEM customizations can affect behavior
4. **Battery awareness**: Consider the user's battery state before performing intensive operations
5. **Rate limiting**: Limit frequency to prevent system throttling

## For more information

For a comprehensive guide on silent push notifications across platforms, including troubleshooting and best practices, see our [Silent Push Notifications Guide]({{site.baseurl}}/user_guide/message_building_by_channel/push/silent_push_notifications_guide/).