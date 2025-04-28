{% multi_lang_include developer_guide/prerequisites/unreal_engine.md %}

## Setting up push notifications

### Step 1: Set up your project

{% tabs %}
{% tab Android %}
First, add Firebase to your Android project. For step-by-step instructions, see Google's [Firebase setup guide](https://firebase.google.com/docs/android/setup).
{% endtab %}

{% tab iOS %}
{% multi_lang_include developer_guide/swift/apns_token.md %}
{% endtab %}
{% endtabs %}

### Step 2: Enable push notifications

{% tabs %}
{% tab Android %}
Add the following lines to your project's `engine.ini` file. Be sure to replace `YOUR_SEND_ID` with the [Sender ID in your Firebase Project](https://firebase.google.com/docs/cloud-messaging/concept-options#credentials).

```ini
bEnableFirebaseCloudMessagingSupport=true
bIsFirebaseCloudMessagingRegistrationEnabled=true
FirebaseCloudMessagingSenderIdKey=YOUR_SENDER_ID
```

Within the same directory as [BrazeUPLAndroid.xml](./BrazeSample/Plugins/Braze/Source/Braze/BrazeUPLAndroid.xml), create a new directory named `AndroidCopies` and add your `google-services.json` file to it.
{% endtab %}

{% tab iOS %}
In your project, go to **Settings** > **Project Settings** > **iOS** > **Online** then check **Enable Remote Notifications Support**. When you're finished, verify that your provision has push capabilities enabled.

{% alert important %}
To enable push capabilities for iOS, your project must have been built from source. For more information, see [Unreal Engine: Building from source](https://dev.epicgames.com/documentation/en-us/unreal-engine/building-unreal-engine-from-source).
{% endalert %}
{% endtab %}
{% endtabs %}

## Optional configurations

{% tabs %}
{% tab Android %}
#### Setting small and large icons

To set the [small and large notification icons]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android&tab=android#configure-icons):

1. Add icons to the appropriate drawable folder (`drawable` by default) inside of the `AndroidCopies/res` folder.
2. Add `braze.xml` to the `AndroidCopies/res/values` folder to set the icons. A very basic braze.xml file:
    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <resources>
        <drawable name="com_braze_push_small_notification_icon">@drawable/notification_small_icon</drawable>
        <drawable name="com_braze_push_large_notification_icon">@drawable/notification_large_icon</drawable>
    </resources>
    ```

{% alert note %}
The files from the `AndroidCopies` folder will be copied into the generated Android project structure as defined in the `BrazeUPLAndroid.xml`.
{% endalert %}
{% endtab %}

{% tab iOS %}
#### Remote launch notifications

As of Unreal Engine version 4.25.3, UE4 lacks proper support to receive a remote notification that causes the initial launch of the application. In order to support receiving this notification, we've created two git patches to apply - one for UE4 and one for the Braze SDK plugin.

1. In your UE4 Engine `Source` directory, apply the git patch `UE4_Engine-Cache-Launch-Remote-Notification.patch`.
2. In your Braze Unreal SDK directory, apply the git patch `Braze_SDK-Read-Cached-Remote-Launch-Notification.patch`.
{% endtab %}
{% endtabs %}
