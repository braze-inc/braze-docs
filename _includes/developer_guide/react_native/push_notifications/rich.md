{% multi_lang_include developer_guide/prerequisites/react_native.md %} You'll also need to [set up push notifications]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=react%20native).

## Using Expo to enable rich push notifications

For the React Native SDK, **rich push notifications are available for Android by default**.

To enable rich push notifications on iOS using Expo, configure the `enableBrazeIosRichPush` property to `true` in your `expo.plugins` object in `app.json`:

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          ...
          "enableBrazeIosRichPush": true
        }
      ]
    ]
  }
}
```

Lastly, add the bundle identifier for this app extension to your project's credentials configuration: `<your-app-bundle-id>.BrazeExpoRichPush`. For further details on this process, refer to [Using app extensions with Expo Application Services]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=react%20native#reactnative_app-extensions).
