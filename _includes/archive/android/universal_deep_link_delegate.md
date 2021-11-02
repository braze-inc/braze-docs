## Universal deep link delegate

The Android SDK provides the ability to set a single delegate object to custom handle all deep links opened by Braze across Content Cards, in-app messages, and push notifications.

Your delegate object should implement the [`IAppboyNavigator`][udl-3] interface and be set using [`AppboyNavigator.setAppboyNavigator()`][udl-2]. In most cases, the delegate should be set in your app's `Application.onCreate()`.

The following is an example of overriding the default [`UriAction`][udl-1] behavior with custom intent flags and custom behavior for Youtube URLs. 

{% tabs %}
{% tab JAVA %}

```java
public class CustomNavigator implements IAppboyNavigator {
  private static final String TAG = AppboyLogger.getAppboyLogTag(CustomAppboyNavigator.class);

  @Override
  public void gotoNewsFeed(Context context, NewsfeedAction newsfeedAction) {
    newsfeedAction.execute(context);
  }

  @Override
  public void gotoUri(Context context, UriAction uriAction) {
    String uri = uriAction.getUri().toString();
    // Open Youtube URLs in the Youtube app and not our app
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
        AppboyLogger.w(TAG, "Could not find appropriate activity to open for deep link " + uri + ".");
      }
    }
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
class CustomNavigator : IAppboyNavigator {

  override fun gotoNewsFeed(context: Context, newsfeedAction: NewsfeedAction) {
    newsfeedAction.execute(context)
  }

  override fun gotoUri(context: Context, uriAction: UriAction) {
    val uri = uriAction.uri.toString()
    // Open Youtube URLs in the Youtube app and not our app
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
        AppboyLogger.w(TAG, "Could not find appropriate activity to open for deep link $uri.")
      }
    }
  }

  companion object {
    private val TAG = AppboyLogger.getAppboyLogTag(CustomAppboyNavigator::class.java)
  }
}
```

{% endtab %}
{% endtabs %}

[udl-1]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/ui/actions/UriAction.html
[udl-2]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/ui/AppboyNavigator.html#setAppboyNavigator-com.appboy.IAppboyNavigator-
[udl-3]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/IAppboyNavigator.html
