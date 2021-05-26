---
nav_title: Deep Linking
platform: Android
page_order: 0
description: "This article covers how to implement the universal deep linking delegate, as well as examples on how to deep link to app settings or the a News Feed."

---

{% include archive/android/universal_deep_link_delegate.md %}

## Deep Linking to App Settings

To allow for deep links to directly open your app's settings, you'll need a custom AppboyNavigator. In the following example, the presence of a custom key-value pair called `open_notification_page` will make the deep link open the app's settings page.

{% tabs %}
{% tab JAVA %}

```java
AppboyNavigator.setAppboyNavigator(new IAppboyNavigator() {
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

      // for Android 8 and above
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
AppboyNavigator.setAppboyNavigator(object : IAppboyNavigator {
  override fun gotoUri(context: Context, uriAction: UriAction) {
    val extras = uriAction.extras
    if (extras.containsKey("open_notification_page")) {
      val intent = Intent()
      intent.action = "android.settings.APP_NOTIFICATION_SETTINGS"
      intent.flags = Intent.FLAG_ACTIVITY_NEW_TASK

      //for Android 5-7
      intent.putExtra("app_package", context.packageName)
      intent.putExtra("app_uid", context.applicationInfo.uid)

      // for Android 8 and above
      intent.putExtra("android.provider.extra.APP_PACKAGE", context.packageName)
      context.startActivity(intent)
    }
  }

  override fun gotoNewsFeed(context: Context, newsfeedAction: NewsfeedAction) {}
})
```

{% endtab %}
{% endtabs %}

## Deep Linking to the News Feed {#Android_Deep_Advance}

To deep link to the Braze News Feed from a push notification, [create a custom deep link][1] for your News Feed activity.

Then, as you set up your push notification campaign (either through the [dashboard][2] or [API][3]), configure the notification to navigate to your News Feed Deep Link.

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/#step-3-add-deep-links
[2]: {{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message
[3]: {{site.baseurl}}/developer_guide/rest_api/messaging/#messaging
