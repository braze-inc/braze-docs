## Setting up uninstall tracking

### Step 1: Enable background push

In your Xcode project, go to **Capabilities** and ensure you have **Background Modes** enabled. For more information, see [silent push notification]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift).

### Step 2: Ignore internal push notifications

The Swift Braze SDK uses background push notifications to collect uninstall tracking analytics. To ensure your app doesn't make unwanted actions when these are sent, you'll need to ensure that [internal push notifications are ignored]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift#swift_ignoring-internal-push-notifications).

### Step 3: Send a test push (optional)

Next, send yourself a test push notification from the Braze dashboard (don't worry&#8212;it won't update your user profile).

1. Go to **Messaging** > **Campaigns** and create a push notification campaign using the relevant platform.
2. Go to **Settings** > **App Settings** and add the `appboy_uninstall_tracking` key with relevant `true` value, then check **Add Content-Available Flag**.
3. Use the **Preview** page to send yourself a test uninstall tracking push.
4. Check that your app does not make any unwanted automatic actions when it receives a push notification.

{% alert note %}
A badge number will be sent along with the test push notification&#8212;however a real uninstall tracking push won't send any badge numbers.
{% endalert %}

### Step 3: Enable uninstall tracking

Finally, enable uninstall tracking in Braze. For a full walkthrough, see [Enable uninstall tracking]({{site.baseurl}}/user_guide/data_and_analytics/tracking/uninstall_tracking/#uninstall-tracking).

{% alert important %}
Tracking uninstalls can be imprecise. The metrics you see on Braze may be delayed or inaccurate.
{% endalert %}
