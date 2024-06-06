---
nav_title: 統合
article_title: Android と FireOS のアプリ内メッセージ統合
page_order: 1
platform: 
  - Android
  - FireOS
description: "このリファレンス記事では、Android または FireOS アプリケーションにアプリ内メッセージングを統合する方法について説明します。"
channel:
  - in-app messages
search_rank: 2
---

# アプリ内メッセージ統合

> このリファレンス記事では、Android または FireOS アプリケーションにアプリ内メッセージングを統合する方法について説明します。

[アプリ内メッセージ]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/)を使用すると、プッシュ通知でユーザーの日常を邪魔することなく、コンテンツをユーザーに届けることができます。カスタマイズされ調整されたアプリ内メッセージは、ユーザーエクスペリエンスが向上し、オーディエンスがアプリから最大限の価値を得るのに役立ちます。アプリ内メッセージでは、さまざまなレイアウトとカスタマイズツールを選択できるため、これまで以上にユーザーの関心を引き付けることができます。

アプリ内メッセージの例については、[ケーススタディ][83]をご覧ください。

## アプリ内メッセージのタイプ

Braze には、デフォルトのアプリ内メッセージタイプがいくつか用意されており、それぞれメッセージ、画像、[Font Awesome][15] アイコン、クリックアクション、分析、編集可能なスタイル、配色でカスタマイズできます。現在利用可能なタイプは以下のとおりです。

- [`Slideup`][91]
- [`Modal`][90]
- [`Full`][93]
- [`HTML`][92]

独自の[カスタムアプリ内メッセージビュー][12]を定義することもできます。

すべてのアプリ内メッセージは [`IInAppMessage`][3] インターフェイスを実装しており、これによってすべてのアプリ内メッセージの基本的な動作と特性が定義されます。[`InAppMessageBase`][27] は、`IInAppMessage` を実装し、基本的なアプリ内メッセージ実装を提供する抽象クラスです。アプリ内メッセージクラスはすべて `InAppMessageBase` のサブクラスです。

また、[`IInAppMessageImmersive`][8] と呼ばれる `IInAppMessage` のサブインターフェイスがあり、これによって、クリックアクションと分析に対応した[ボタン][50]に加え、ヘッダーテキストと閉じるボタンが追加されます。

{% alert important %}
ボタンを含むアプリ内メッセージの場合、ボタンテキストを追加する前にクリックアクションが追加されると、メッセージ `clickAction` も最終ペイロードに含まれます。
{% endalert %}

[`InAppMessageImmersiveBase`][28] は、`IInAppMessageImmersive` を実装し、基本的な `immersive` アプリ内メッセージ実装を提供する抽象クラスです。`Modal` アプリ内メッセージは `InAppMessageImmersiveBase` のサブクラスです。

HTML アプリ内メッセージは、`IInAppMessage` のもう 1 つのサブクラスである [`IInAppMessageHtml`][52] を実装する [`InAppMessageHtml`][92] インスタンスです。

### メッセージタイプ別に予想される動作

ユーザーがデフォルトのアプリ内メッセージタイプの 1 つを開くと、次のようになります。

{% tabs local %}
{% tab Slideup %}
[`Slideup`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-slideup/index.html) アプリ内メッセージは、画面の上部または下部から「スライドアップ」または「スライドダウン」するため、このような名前が付けられています。画面の一部分だけを覆い、効果的で邪魔にならないメッセージング機能を提供します。

![An in-app message sliding from the bottom of a phone screen displaying "Humans are complicated. Custom engagement shouldn't be." In the background is the same in-app message displayed in the bottom right corner of a web page.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Modal %}
[`Modal`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-modal/index.html) アプリ内メッセージは画面中央に表示され、半透明のパネルに囲まれます。より重要なメッセージングの場合に有用で、2 つのクリックアクションと分析対応ボタンを装備できます。

![A modal in-app message in the center of a phone screen displaying "Humans are complicated. Custom engagement shouldn't be." In the background is the same in-app message displayed in the center of a web page.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Full Screen %}
[`Full`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-full/index.html) アプリ内メッセージは、ユーザーコミュニケーションの内容とインパクトを最大化するのに有効です。`full` アプリ内メッセージの上半分には画像が含まれ、下半分にはテキストと最大 2 つのクリックアクションと分析対応ボタンが表示されます。

![A full screen in-app message shown across an entire phone screen displaying, "Humans are complicated. Custom engagement shouldn't be." In the background is the same in-app message displayed largely in the center of a web page.]({% image_buster /assets/img_archive/In-App_Full.png %})

{% endtab %}
{% tab Custom HTML %}
[`HTML`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-html/index.html) アプリ内メッセージは、完全にカスタマイズされたユーザーコンテンツを作成するのに便利です。ユーザー定義の HTML アプリ内のメッセージコンテンツは、`WebView` に表示され、必要に応じて画像やフォントなどの他のリッチコンテンツを含めることができます。これにより、メッセージの外観と機能を完全に制御できます。<br><br>Android アプリ内メッセージは、HTML 内から Braze Web SDK のメソッドを呼び出すための JavaScript `brazeBridge` インターフェイスをサポートしています。詳細については、<a href="{{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/">ベストプラクティス</a>を参照してください。

![An HTML in-app message with the a carousel of content and interactive buttons.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

{% alert important %}
現在、iOS と Android のプラットフォームでは、iFrame でのカスタム HTML アプリ内メッセージの表示はサポートしていません。
{% endalert %} 

{% endtab %}
{% endtabs %}

#### カスタムアプリ内メッセージタイプの定義

`slideup` アプリ内メッセージオブジェクトは [`InAppMessageBase`][27] を拡張します。
`full` および `modal` タイプのメッセージは [`InAppMessageImmersiveBase`][28] を拡張します。これらのクラスのいずれかを拡張すると、ローカルで生成されたアプリ内メッセージにカスタム機能を追加できるようになります。

## 統合 {#in-app-messaging-integration}

### ステップ 1:Braze アプリ内メッセージマネージャー登録

アプリ内メッセージ表示は [`BrazeInAppMessageManager`][34] クラスによって管理されまｓ。アプリ内のすべてのアクティビティを `BrazeInAppMessageManager` に登録して、アプリ内メッセージビューをビュー階層に追加できるようにする必要があります。これを行うには次の 2 つの方法があります。

#### アクティビティライフサイクルコールバック統合 (推奨)

[アクティビティライフサイクルコールバック統合][59]はアプリ内メッセージ登録を自動的に処理するため、追加の統合は不要です。これは、アプリ内メッセージ登録を処理するための推奨統合です。

#### アプリ内メッセージの手動登録

{% alert warning %}
アクティビティライフサイクル統合を行った場合は、アプリ内メッセージを手動で統合*しない*でください。
{% endalert %}

まず、[`Application.onCreate()`][82] で [`ensureSubscribedToInAppMessageEvents()`][69] を呼び出します。

{% tabs %}
{% tab JAVA %}

```java
BrazeInAppMessageManager.getInstance().ensureSubscribedToInAppMessageEvents(context);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
BrazeInAppMessageManager.getInstance().ensureSubscribedToInAppMessageEvents(context)
```

{% endtab %}
{% endtabs %}

次に、アプリ内メッセージを表示できるアクティビティごとに、[`registerInAppMessageManager()`][80] をそのアクティビティの `onResume()` で呼び出す必要があります。

{% tabs %}
{% tab JAVA %}

```java
@Override
public void onResume() {
  super.onResume();
  // Registers the BrazeInAppMessageManager for the current Activity. This Activity will now listen for
  // in-app messages from Braze.
  BrazeInAppMessageManager.getInstance().registerInAppMessageManager(activity);
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
public override fun onResume() {
  super.onResume()
  // Registers the BrazeInAppMessageManager for the current Activity. This Activity will now listen for
  // in-app messages from Braze.
  BrazeInAppMessageManager.getInstance().registerInAppMessageManager(this)
}
```

{% endtab %}
{% endtabs %}

最後に、[`registerInAppMessageManager()`][80] が呼び出されたアクティビティごとに、そのアクティビティの `onPause()` で [`unregisterInAppMessageManager()`][81] を呼び出す必要があります。

{% tabs %}
{% tab JAVA %}

```java
@Override
public void onPause() {
  super.onPause();
  // Unregisters the BrazeInAppMessageManager for the current Activity.
  BrazeInAppMessageManager.getInstance().unregisterInAppMessageManager(activity);
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
public override fun onPause() {
  super.onPause()
  // Unregisters the BrazeInAppMessageManager.
  BrazeInAppMessageManager.getInstance().unregisterInAppMessageManager(this)
}
```

{% endtab %}
{% endtabs %}

### ステップ 2:アプリ内メッセージマネージャー禁止リスト (オプション)

統合では、アプリ内の特定のアクティビティにアプリ内メッセージを表示しないようにする必要が生じる場合があります。[アクティビティライフサイクルコールバックの統合][59]により、これを簡単に実現できます。

次のサンプルコードでは、アプリ内メッセージ登録禁止リストに `SplashActivity` と `SettingsActivity` という 2 つのアクティビティを追加します。

{% tabs %}
{% tab JAVA %}

```java
public class MyApplication extends Application {
  @Override
  public void onCreate() {
    super.onCreate();
    Set<Class> inAppMessageBlocklist = new HashSet<>();
    inAppMessageBlocklist.add(SplashActivity.class);
    inAppMessageBlocklist.add(SettingsActivity.class);
    registerActivityLifecycleCallbacks(new BrazeActivityLifecycleCallbackListener(inAppMessageBlocklist));
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
class MyApplication : Application() {
  override fun onCreate() {
    super.onCreate()
    val inAppMessageBlocklist = HashSet<Class<*>>()
    inAppMessageBlocklist.add(SplashActivity::class.java)
    inAppMessageBlocklist.add(SettingsActivity::class.java)
    registerActivityLifecycleCallbacks(BrazeActivityLifecycleCallbackListener(inAppMessageBlocklist))
  }
}
```

{% endtab %}
{% endtabs %}


[34]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/index.html
[69]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/ensure-subscribed-to-in-app-message-events.html
[80]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/register-in-app-message-manager.html
[81]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/unregister-in-app-message-manager.html
[82]: https://developer.android.com/reference/android/app/Application.html#onCreate()
[83]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-activity-lifecycle-callback-listener/index.html
[59]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-4-tracking-user-sessions-in-android
[3]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message/index.html
[8]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message-immersive/index.html
[12]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/custom_listeners/#custom-view-factory
[15]: https://fontawesome.com/icons?d=gallery&p=2
[27]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-base/index.html
[28]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-immersive-base/index.html
[50]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-message-button/index.html
[51]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-html-full/index.html
[52]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message-html/index.html
[84]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/
[90]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-modal/index.html
[91]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-slideup/index.html
[92]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-html/index.html
[93]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-full/index.html
