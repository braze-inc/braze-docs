---
nav_title: Deep Linking
article_title: Deep Linking for Android and FireOS
platform: 
  - Android
  - FireOS
page_order: 0
description: "This article covers how to implement the universal deep linking delegate for your Android or FireOS app, as well as examples on how to deep link to app settings or a News Feed."

---

# Android deep linking

## Universal deep link delegate

The Android SDK provides the ability to set a single delegate object to custom handle all deep links opened by Braze across Content Cards, in-app messages, and push notifications.

Your delegate object should implement the [`IBrazeDeeplinkHandler`][udl-3] interface and be set using [`BrazeDeeplinkHandler.setBrazeDeeplinkHandler()`][udl-2]. In most cases, the delegate should be set in your app's `Application.onCreate()`.

The following is an example of overriding the default [`UriAction`][udl-1] behavior with custom intent flags and custom behavior for YouTube URLs:

{% tabs %}
{% tab JAVA %}

```java
public class CustomDeeplinkHandler implements IBrazeDeeplinkHandler {
  private static final String TAG = BrazeLogger.getBrazeLogTag(CustomDeeplinkHandler.class);

  @Override
  public void gotoNewsFeed(Context context, NewsfeedAction newsfeedAction) {
    newsfeedAction.execute(context);
  }

  @Override
  public void gotoUri(Context context, UriAction uriAction) {
    String uri = uriAction.getUri().toString();
    // Open YouTube URLs in the YouTube app and not our app
    if (!StringUtils.isNullOrBlank(uri) && uri.contains("youtube.com")) {
      uriAction.setUseWebView(false);
    }

    CustomUriAction customUriAction = new CustomUriAction(uriAction);
    customUriAction.execute(context);
  }

  public static class CustomUriAction extends UriAction {

    public CustomUriAction(@NonNull UriAction uriAction) {
      super(uriAction);
    }

    @Override
    protected void openUriWithActionView(Context context, Uri uri, Bundle extras) {
      Intent intent = getActionViewIntent(context, uri, extras);
      intent.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK | Intent.FLAG_ACTIVITY_CLEAR_TOP | Intent.FLAG_ACTIVITY_SINGLE_TOP);
      if (intent.resolveActivity(context.getPackageManager()) != null) {
        context.startActivity(intent);
      } else {
        BrazeLogger.w(TAG, "Could not find appropriate activity to open for deep link " + uri + ".");
      }
    }
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
class CustomDeeplinkHandler : IBrazeDeeplinkHandler {

  override fun gotoNewsFeed(context: Context, newsfeedAction: NewsfeedAction) {
    newsfeedAction.execute(context)
  }

  override fun gotoUri(context: Context, uriAction: UriAction) {
    val uri = uriAction.uri.toString()
    // Open YouTube URLs in the YouTube app and not our app
    if (!StringUtils.isNullOrBlank(uri) && uri.contains("youtube.com")) {
      uriAction.useWebView = false
    }

    val customUriAction = CustomUriAction(uriAction)
    customUriAction.execute(context)
  }

  class CustomUriAction(uriAction: UriAction) : UriAction(uriAction) {

    override fun openUriWithActionView(context: Context, uri: Uri, extras: Bundle) {
      val intent = getActionViewIntent(context, uri, extras)
      intent.flags = Intent.FLAG_ACTIVITY_NEW_TASK or Intent.FLAG_ACTIVITY_CLEAR_TOP or Intent.FLAG_ACTIVITY_SINGLE_TOP
      if (intent.resolveActivity(context.packageManager) != null) {
        context.startActivity(intent)
      } else {
        BrazeLogger.w(TAG, "Could not find appropriate activity to open for deep link $uri.")
      }
    }
  }

  companion object {
    private val TAG = BrazeLogger.getBrazeLogTag(CustomDeeplinkHandler::class.java)
  }
}
```

{% endtab %}
{% endtabs %}

## Deep linking to app settings

To allow deep links to directly open your app's settings, you'll need a custom `BrazeDeeplinkHandler`. In the following example, the presence of a custom key-value pair called `open_notification_page` will make the deep link open the app's settings page:

{% tabs %}
{% tab JAVA %}

```java
BrazeDeeplinkHandler.setBrazeDeeplinkHandler(new IBrazeDeeplinkHandler() {
  @Override
  public void gotoUri(Context context, UriAction uriAction) {
    final Bundle extras = uriAction.getExtras();
    if (extras.containsKey("open_notification_page")) {
      Intent intent = new Intent();
      intent.setAction("android.settings.APP_NOTIFICATION_SETTINGS");
      intent.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK);

      //for Android 5-7
      intent.putExtra("app_package", context.getPackageName());
      intent.putExtra("app_uid", context.getApplicationInfo().uid);

      // for Android 8 and later
      intent.putExtra("android.provider.extra.APP_PACKAGE", context.getPackageName());
      context.startActivity(intent);
    }
  }

  @Override
  public void gotoNewsFeed(Context context, NewsfeedAction newsfeedAction) {}
});
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
BrazeDeeplinkHandler.setBrazeDeeplinkHandler(object : IBrazeDeeplinkHandler {
  override fun gotoUri(context: Context, uriAction: UriAction) {
    val extras = uriAction.extras
    if (extras.containsKey("open_notification_page")) {
      val intent = Intent()
      intent.action = "android.settings.APP_NOTIFICATION_SETTINGS"
      intent.flags = Intent.FLAG_ACTIVITY_NEW_TASK

      //for Android 5-7
      intent.putExtra("app_package", context.packageName)
      intent.putExtra("app_uid", context.applicationInfo.uid)

      // for Android 8 and later
      intent.putExtra("android.provider.extra.APP_PACKAGE", context.packageName)
      context.startActivity(intent)
    }
  }

  override fun gotoNewsFeed(context: Context, newsfeedAction: NewsfeedAction) {}
})
```

{% endtab %}
{% endtabs %}

## Deep linking to the News Feed {#Android_Deep_Advance}

To deep link to the Braze News Feed from a push notification, [create a custom deep link][1] for your News Feed activity.

Then, as you set up your push notification campaign (either through the [dashboard][2] or [API][3]), configure the notification to navigate to your News Feed deep link.

## Custom WebView activity {#Custom_Webview_Activity}

By default, when website deeplinks are opened inside the app by Braze, they are handled by [`BrazeWebViewActivity`][udl-4]. To change this:

**1.** Create a new Activity that handles the target URL from `Intent.getExtras()` with the key `com.appboy.Constants.BRAZE_WEBVIEW_URL_EXTRA`. See [`BrazeWebViewActivity.java`][udl-8] for an example.<br><br>
**2.** Add that activity to `AndroidManifest.xml` and set `exported` to `false`.

```xml
<activity
    android:name=".MyCustomWebViewActivity"
    android:exported="false" />
```

**3.** Set your custom Activity in a `BrazeConfig` [builder object][udl-6]. Build the builder and pass it to [`Braze.configure()`][udl-5] in your [`Application.onCreate()`][udl-7]

{% tabs %}
{% tab JAVA %}

```java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
    .setCustomWebViewActivityClass(MyCustomWebViewActivity::class)
    ...
    .build();
Braze.configure(this, brazeConfig);
```

 {% endtab %}
 {% tab KOTLIN %}

```kotlin
val brazeConfig = BrazeConfig.Builder()
    .setCustomWebViewActivityClass(MyCustomWebViewActivity::class.java)
    ...
    .build()
Braze.configure(this, brazeConfig)
```

 {% endtab %}
 {% endtabs %}


[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-4-add-deep-links
[2]: {{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message
[3]: {{site.baseurl}}/api/endpoints/messaging/
[udl-1]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.ui.actions/-uri-action/index.html
[udl-2]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.ui/-braze-deeplink-handler/set-braze-deeplink-handler.html
[udl-3]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.ui/-braze-deeplink-handler/index.html
[udl-4]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.ui/-braze-web-view-activity/index.html
[udl-5]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/index.html#-1864418529%2FFunctions%2F-1725759721
[udl-6]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-custom-web-view-activity-class.html
[udl-7]: https://developer.android.com/reference/android/app/Application.html#onCreate()
[udl-8]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/src/main/java/com/braze/ui/BrazeWebViewActivity.java
