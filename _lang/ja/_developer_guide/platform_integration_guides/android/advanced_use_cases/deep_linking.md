---
nav_title: ディープリンク
article_title: Android と FireOS のディープリンク
platform: 
  - Android
  - FireOS
page_order: 0
description: "この記事では、Android または FireOS アプリにユニバーサルディープリンクデリゲートを実装する方法と、アプリの設定にディープリンクする方法の例を紹介します。"

---

# ディープリンク

> [Android SDK 実装プロセスの][1]一環として、アプリがディープリンクを使用する機能を設定します。この記事では、ディープリンクのユースケースの追加例を紹介します。

ディープリンクの基本情報については、[ユーザーガイドの記事][4]を参照してください。

{% alert note %}
この記事には、廃止予定のニュースフィードの情報が含まれています。Braze では、News Feed ツールを使用するお客様は、コンテンツカードメッセージングチャネルに移動することを推奨しています。これは、より柔軟でカスタマイズ可能で、信頼性が高いチャネルです。詳しくは[マイグレーションガイド]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/)をご覧ください。
{% endalert %}

## ユニバーサルディープリンクデリゲート

Android SDK は、コンテンツカード、アプリ内メッセージ、プッシュ通知にわたって Braze によって開かれたすべてのディープリンクをカスタム処理するように単一のデリゲートオブジェクトを設定する機能を提供しています。

デリゲートオブジェクトは[`IBrazeDeeplinkHandler`][udl-3]インターフェイスを実装し、[`BrazeDeeplinkHandler.setBrazeDeeplinkHandler()`][udl-2]を使用して設定する必要があります。ほとんどの場合、デリゲートはアプリの`Application.onCreate()`で設定する必要があります。

以下は、カスタムインテントフラグと YouTube URL のカスタム動作でデフォルトの[`UriAction`][udl-1]動作を上書きする例です。

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

## アプリ設定へのディープリンク

ディープリンクでアプリの設定を直接開くようにするには、カスタムの`BrazeDeeplinkHandler`が必要です。以下の例では、`open_notification_page`と呼ばれるカスタムのキーと値のペアが存在すると、ディープリンクがアプリの設定ページを開きます。

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

## ニュースフィードへのディープリンク{#Android_Deep_Advance}

{% alert note %}
ニュースフィードは非推奨になります。Braze では、News Feed ツールを使用するお客様は、コンテンツカードメッセージングチャネルに移動することを推奨しています。これは、より柔軟でカスタマイズ可能で、信頼性が高いチャネルです。詳しくは[マイグレーションガイド]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/)をご覧ください。
{% endalert %}

プッシュ通知から Braze ニュースフィードにディープリンクするには、ニュースフィードアクティビティの[カスタムディープリンクを作成][1]します。

次に、プッシュ通知キャンペーンを設定する際に ([ダッシュボード][2]または [API][3] を通じて) 、 ニュースフィードのディープリンクに移動するように通知を構成します。

## カスタム WebView アクティビティ{#Custom_Webview_Activity}

デフォルトでは、Braze によってアプリ内でウェブサイトのディープリンクが開かれると、[`BrazeWebViewActivity`][udl-4]によって処理されます。これを変更するには、以下を行います。

**1\.**キー`com.braze.Constants.BRAZE_WEBVIEW_URL_EXTRA`で`Intent.getExtras()`から対象の URL を扱うアクティビティを新規作成します。例については、[`BrazeWebViewActivity.java`][udl-8]を参照してください。<br><br>
**2\.**そのアクティビティを`AndroidManifest.xml`に追加し、`exported`を`false`に設定します。

```xml
<activity
    android:name=".MyCustomWebViewActivity"
    android:exported="false" />
```

**3\.**カスタムアクティビティを`BrazeConfig`[ビルダーオブジェクト][udl-6]に設定します。ビルダーをビルドし、[`Application.onCreate()`][udl-7]内の[`Braze.configure()`][udl-5]に渡します。

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
[4]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking
[udl-1]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.actions/-uri-action/index.html
[udl-2]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui/-braze-deeplink-handler/-companion/set-braze-deeplink-handler.html
[udl-3]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui/-braze-deeplink-handler/index.html
[udl-4]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui/-braze-web-view-activity/index.html
[udl-5]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/index.html#-1864418529%2FFunctions%2F-1725759721
[udl-6]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-custom-web-view-activity-class.html
[udl-7]: https://developer.android.com/reference/android/app/Application.html#onCreate()
[udl-8]: https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/java/com/braze/ui/BrazeWebViewActivity.kt
