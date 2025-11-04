{% multi_lang_include developer_guide/prerequisites/android.md %}

## Einen universellen Delegierten erstellen

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

## Anpassen der WebView-Aktivität {#Custom_Webview_Activity}

Standardmäßig werden Deeplinks auf Websites, die innerhalb der App von Braze geöffnet werden, von [`BrazeWebViewActivity`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui/-braze-web-view-activity/index.html) verarbeitet. Um dies zu ändern:

1. Erstellen Sie eine neue Aktivität, die die Ziel-URL von `Intent.getExtras()` mit dem Schlüssel `com.braze.Constants.BRAZE_WEBVIEW_URL_EXTRA` behandelt. Für ein Beispiel, siehe [`BrazeWebViewActivity.java`](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/java/com/braze/ui/BrazeWebViewActivity.kt).
2. Fügen Sie diese Aktivität zu `AndroidManifest.xml` hinzu und setzen Sie `exported` auf `false`.
    ```xml
    <activity
        android:name=".MyCustomWebViewActivity"
        android:exported="false" />
    ```
3. Legen Sie Ihre angepasste Aktivität in einem `BrazeConfig` [builder Objekt](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-custom-web-view-activity-class.html) fest. Erstellen Sie den Builder und übergeben Sie ihn an [`Braze.configure()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/index.html#-1864418529%2FFunctions%2F-1725759721) in Ihrem [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate()).
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

## Jetpack Compose verwenden

Zur Behandlung von Deeplinks bei der Verwendung von Jetpack Compose mit NavHost:

1. Vergewissern Sie sich, dass die Aktivität, die Ihren Deeplink verarbeitet, im Android Manifest registriert ist.
    ```xml
    <activity
      ...
      <intent-filter>
        <action android:name="android.intent.action.VIEW" />
        <category android:name="android.intent.category.BROWSABLE" />
        <category android:name="android.intent.category.DEFAULT" />
        <data
            android:host="articles"
            android:scheme="myapp" />
      </intent-filter>
    </activity>
    ```
2. Geben Sie in NavHost an, welche Deeplinks er verarbeiten soll.
    ```kotlin
    composableWithCompositionLocal(
        route = "YOUR_ROUTE_HERE",
        deepLinks = listOf(navDeepLink {
            uriPattern = "myapp://articles/{${MainDestinations.ARTICLE_ID_KEY}}"
        }),
        arguments = listOf(
            navArgument(MainDestinations.ARTICLE_ID_KEY) {
                type = NavType.LongType
            }
        ),
    ) { backStackEntry ->
        val arguments = requireNotNull(backStackEntry.arguments)
        val articleId = arguments.getLong(MainDestinations.ARTICLE_ID_KEY)
        ArticleDetail(
            articleId
        )
    }
    ```
3. Je nach Architektur Ihrer App müssen Sie möglicherweise auch die neue Absicht behandeln, die an Ihre aktuelle Aktivität gesendet wird.
    ```kotlin
    DisposableEffect(Unit) {
        val listener = Consumer<Intent> {
            navHostController.handleDeepLink(it)
        }
        addOnNewIntentListener(listener)
        onDispose { removeOnNewIntentListener(listener) }
    }
    ```
