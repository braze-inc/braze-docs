---
nav_title: Deeplinking
article_title: Deeplinking für Android und FireOS
platform: 
  - Android
  - FireOS
page_order: 0
description: "In diesem Artikel erfahren Sie, wie Sie den universellen Deeplink-Delegaten für Ihre Android- oder FireOS-App implementieren und wie Sie Deeplinks zu App-Einstellungen setzen."

---

# Deeplinks setzen

> Als Teil des [Implementierungsprozesses für Ihr Android SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-4-add-deep-links) werden Sie die Fähigkeit Ihrer App konfigurieren, Deeplinks zu verwenden. Dieser Artikel enthält weitere Beispiele für Anwendungsfälle, in denen Deeplinks gesetzt werden.

Einführende Informationen zu Deeplinks setzen finden Sie in unserem [Benutzerhandbuch]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking).

{% alert note %}
Dieser Artikel enthält Informationen zum News Feed, der nicht mehr verwendet wird. Braze empfiehlt Kunden, die unser News Feed-Tool verwenden, auf unseren Nachrichtenkanal Content Cards umzusteigen - er ist flexibler, anpassbarer und zuverlässiger. Weitere Informationen finden Sie im [Migrationsleitfaden]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/).
{% endalert %}

## Universal Deeplinks delegieren

Das Android SDK bietet die Möglichkeit, ein einzelnes Delegatenobjekt festzulegen, um alle von Braze geöffneten Deeplinks über Content-Cards, In-App-Nachrichten und Push-Benachrichtigungen anzupassen.

Ihr Delegatenobjekt sollte die [`IBrazeDeeplinkHandler`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui/-braze-deeplink-handler/index.html)-Schnittstelle implementieren und mit [`BrazeDeeplinkHandler.setBrazeDeeplinkHandler()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui/-braze-deeplink-handler/-companion/set-braze-deeplink-handler.html) festgelegt werden. In den meisten Fällen sollte der Delegat in Ihrer App in `Application.onCreate()` festgelegt werden.

Im Folgenden finden Sie ein Beispiel für das Überschreiben des Standard [`UriAction`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.actions/-uri-action/index.html) mit angepassten Absichtsflags und einem angepassten Verhalten für YouTube-URLs:

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

## Deeplinks zu den App-Einstellungen setzen

Um Deeplinks zu erlauben, die Einstellungen Ihrer App direkt zu öffnen, benötigen Sie eine nangepassten `BrazeDeeplinkHandler`. Im folgenden Beispiel bewirkt das Vorhandensein eines angepassten Schlüssel-Wert-Paares namens `open_notification_page`, dass der Deeplink die Einstellungsseite der App öffnet:

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

## Deep Linking zum Newsfeed {#Android_Deep_Advance}

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

Um von einer Push-Benachrichtigung aus einen Deep Link zum Braze Newsfeed zu erstellen, [erstellen Sie einen benutzerdefinierten Deep Link]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-4-add-deep-links) für Ihre Newsfeed-Aktivität.

Wenn Sie dann Ihre Kampagne für Push-Benachrichtigungen einrichten (entweder über das [Dashboard]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message) oder die [API]({{site.baseurl}}/api/endpoints/messaging/)), konfigurieren Sie die Benachrichtigung so, dass sie zu Ihrem Deeplink im Newsfeed navigiert.

## Angepasste WebView-Aktivität {#Custom_Webview_Activity}

Standardmäßig werden Deeplinks auf Websites, die innerhalb der App von Braze geöffnet werden, von [`BrazeWebViewActivity`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui/-braze-web-view-activity/index.html) verarbeitet. Um dies zu ändern:

**1\.** Erstellen Sie eine neue Aktivität, die die Ziel-URL von `Intent.getExtras()` mit dem Schlüssel `com.braze.Constants.BRAZE_WEBVIEW_URL_EXTRA` behandelt. Siehe [`BrazeWebViewActivity.java`](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/java/com/braze/ui/BrazeWebViewActivity.kt) für ein Beispiel.<br><br>
**2\.** Fügen Sie diese Aktivität zu `AndroidManifest.xml` hinzu und setzen Sie `exported` auf `false`.

```xml
<activity
    android:name=".MyCustomWebViewActivity"
    android:exported="false" />
```

**3\.** Legen Sie Ihre angepasste Aktivität in einem `BrazeConfig` [builder Objekt](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-custom-web-view-activity-class.html) fest. Erstellen Sie den Builder und übergeben Sie ihn an [`Braze.configure()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/index.html#-1864418529%2FFunctions%2F-1725759721) in Ihrem [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate())

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


