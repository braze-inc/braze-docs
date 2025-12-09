{% multi_lang_include developer_guide/prerequisites/flutter.md %}

## Message types

{% tabs %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/android.md %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/swift.md %}
{% endtabs %}

## Enabling in-app messages

{% alert note %}
This step is for iOS only. The default implementation for in-app messages is already set up on Android.
{% endalert %}

To set up the default presenter for in-app messages on iOS, create an implementation of the `BrazeInAppMessagePresenter` protocol and assign it to the optional `inAppMessagePresenter` on your Braze instance. You can also use the default Braze UI presenter by instantiating a `BrazeInAppMessageUI` object.

You will need to import the `BrazeUI` library to access the `BrazeInAppMessageUI` class.

{% tabs %}
{% tab swift %}

```swift
import BrazeUI

override func application(
  _ application: UIApplication,
  didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil
) -> Bool {
  ...

  let braze = BrazePlugin.initBraze(configuration)

  // Initialize and assign the default `BrazeInAppMessageUI` class to the in-app message presenter.
  braze.inAppMessagePresenter = BrazeInAppMessageUI()
  AppDelegate.braze = braze

  return true
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
@import BrazeUI;

- (BOOL)application:(UIApplication *)application
    didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  ...

  Braze *braze = [BrazePlugin initBraze:configuration];

  // Initialize and assign the default `BrazeInAppMessageUI` class to the in-app message presenter.
  braze.inAppMessagePresenter = [[BrazeInAppMessageUI alloc] init];
  AppDelegate.braze = braze;

  [self.window makeKeyAndVisible];
  return YES;
}
```
{% endtab %}
{% endtabs %}

To customize your implementation further, refer to [Logging in-app message data]({{site.baseurl}}/in_app_messages/logging_message_data?sdktab=flutter).
