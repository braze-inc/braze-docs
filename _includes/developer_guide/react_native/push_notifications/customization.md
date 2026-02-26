{% multi_lang_include developer_guide/prerequisites/react_native.md %} You'll also need to [set up push notifications]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=react%20native).

## Push customization in React Native

The Braze React Native SDK does not expose push notification customization (action buttons, categories, custom notification factories) through its JavaScript API. These features require native configuration in your iOS and Android projects.

| Feature | iOS | Android |
| --- | --- | --- |
| Action buttons | Configure in native Swift/Objective-C | Configure in native Java/Kotlin |
| Push categories | Configure in native Swift/Objective-C | Configure in native Java/Kotlin |
| Custom notification factory | N/A | Configure in native Java/Kotlin |
| Badge customization | Configure in native Swift/Objective-C | N/A |
| Custom sounds | Configure in native Swift/Objective-C | Configure in native Java/Kotlin |

### iOS customization

To add push action buttons, categories, badges, or custom sounds on iOS, implement the native configuration in your `AppDelegate` (Swift or Objective-C). See [Customize push notifications – Swift]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=swift) for step-by-step instructions.

### Android customization

To add push action buttons, categories, or a custom notification factory on Android, implement the native configuration in your Android project. See [Customize push notifications – Android]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=android) for step-by-step instructions.
