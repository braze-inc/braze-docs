---
nav_title: Integration
platform: FireOS
page_order: 1

---
## Integration {#in-app-messaging-integration}

### Step 1: Braze In-App Message Manager Registration

In-App Message display is managed by the [`AppboyInAppMessageManager`][34] class. Every activity in your app must be registered with the `AppboyInAppMessageManager` to allow it to add in-app message views to the view hierarchy. There are two ways to accomplish this:

#### Activity Lifecycle Callback Integration (Recommended)

The [Activity Lifecycle Callback Integration][59] handles in-app message registration automatically, no extra integration is required. This is the recommended integration for handling in-app message registration.

#### Manual In-App Message Registration

A manual in-app message registration requires 3 steps.

>  If you did the activity lifecycle integration, then you should *not* do a manual in-app message integration.

* In your [`Application.onCreate()`][82], [`ensureSubscribedToInAppMessageEvents()`][69] should be called.

```java
AppboyInAppMessageManager.getInstance().ensureSubscribedToInAppMessageEvents(context);
```

* In every activity where in-app messages can be shown, [`registerInAppMessageManager()`][80] should be called in that activity's `onResume()`.

```java
@Override
public void onResume() {
  super.onResume();
  // Registers the AppboyInAppMessageManager for the current Activity. This Activity will now listen for
  // in-app messages from Braze.
  AppboyInAppMessageManager.getInstance().registerInAppMessageManager(activity);
}
```

* In every activity where [`registerInAppMessageManager()`][80] was called, [`unregisterInAppMessageManager()`][81] should be called in that activity's `onPause()`.

```java
@Override
public void onPause() {
  super.onPause();
  // Unregisters the AppboyInAppMessageManager for the current Activity.
  AppboyInAppMessageManager.getInstance().unregisterInAppMessageManager(activity);
}
```


[34]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/ui/inappmessage/AppboyInAppMessageManager.html
[59]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-4-tracking-user-sessions-in-android
[69]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/ui/inappmessage/AppboyInAppMessageManager.html#ensureSubscribedToInAppMessageEvents-android.content.Context-
[80]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/ui/inappmessage/AppboyInAppMessageManager.html#registerInAppMessageManager-android.app.Activity-
[81]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/ui/inappmessage/AppboyInAppMessageManager.html#unregisterInAppMessageManager-android.app.Activity-
[82]: https://developer.android.com/reference/android/app/Application.html#onCreate()
