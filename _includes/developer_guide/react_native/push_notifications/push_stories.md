## Enabling push stories for iOS

{% alert tip %}
For the React Native SDK, push stories are available for Android by default.
{% endalert %}

To enable Push Stories on iOS using Expo, ensure you have an app group defined for your application. For more information, see [Adding an App Group]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/push_story/#adding-an-app-group).

Next, configure the `enableBrazeIosPushStories` property to `true` and assign your app group ID to `iosPushStoryAppGroup` in your `expo.plugins` object in `app.json`:

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          ...
          "enableBrazeIosPushStories": true,
          "iosPushStoryAppGroup": "group.com.company.myApp.PushStories"
        }
      ]
    ]
  }
}
```

Lastly, add the bundle identifier for this app extension to your project's credentials configuration: `<your-app-bundle-id>.BrazeExpoPushStories`. For further details on this process, refer to [Using app extensions with Expo Application Services](#app-extensions).

{% alert warning %}
If you are using Push Stories with Expo Application Services, be sure to use the `EXPO_NO_CAPABILITY_SYNC=1` flag when running `eas build`. There is a known issue in the command line which removes the App Groups capability from your extension's provisioning profile.
{% endalert %}
