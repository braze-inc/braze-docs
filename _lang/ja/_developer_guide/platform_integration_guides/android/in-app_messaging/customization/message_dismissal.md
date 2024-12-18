---
nav_title: メッセージ却下
article_title: アンドロイド と FireOS のアプリ内メッセージ却下
platform: 
  - Android
  - FireOS
page_order: 5
description: "このリファレンス記事では、Android または FireOS アプリケーションのアプリ内メッセージ却下について説明します。"
channel:
  - in-app messages

---

# メッセージ却下

> このリファレンス記事では、Android または FireOS アプリケーションのアプリ内メッセージ却下について説明します。

## [戻る] ボタンによる却下の無効化

デフォルトでは、ハードウェアの [戻る] ボタンにより Braze のアプリ内メッセージは閉じます。この動作は、[`BrazeInAppMessageManager.setBackButtonDismissesInAppMessageView()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-manager-base/set-back-button-dismisses-in-app-message-view.html)を使用してメッセージごとに無効にできます。 

次の例にある`disable_back_button`は、アプリ内メッセージに設定されているカスタムのキーと値のペアで、[戻る] ボタンでメッセージを閉じることを許可するかどうかを示します。

{% tabs %}
{% tab JAVA %}
```java
BrazeInAppMessageManager.getInstance().setCustomInAppMessageManagerListener(new DefaultInAppMessageManagerListener() {
  @Override
  public void beforeInAppMessageViewOpened(View inAppMessageView, IInAppMessage inAppMessage) {
    super.beforeInAppMessageViewOpened(inAppMessageView, inAppMessage);
    final Map<String, String> extras = inAppMessage.getExtras();
    if (extras != null && extras.containsKey("disable_back_button")) {
      BrazeInAppMessageManager.getInstance().setBackButtonDismissesInAppMessageView(false);
    }
  }

  @Override
  public void afterInAppMessageViewClosed(IInAppMessage inAppMessage) {
    super.afterInAppMessageViewClosed(inAppMessage);
    BrazeInAppMessageManager.getInstance().setBackButtonDismissesInAppMessageView(true);
  }
});
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
BrazeInAppMessageManager.getInstance().setCustomInAppMessageManagerListener(object : DefaultInAppMessageManagerListener() {
  override fun beforeInAppMessageViewOpened(inAppMessageView: View, inAppMessage: IInAppMessage) {
    super.beforeInAppMessageViewOpened(inAppMessageView, inAppMessage)
    val extras = inAppMessage.extras
    if (extras != null && extras.containsKey("disable_back_button")) {
      BrazeInAppMessageManager.getInstance().setBackButtonDismissesInAppMessageView(false)
    }
  }

  override fun afterInAppMessageViewClosed(inAppMessage: IInAppMessage) {
    super.afterInAppMessageViewClosed(inAppMessage)
    BrazeInAppMessageManager.getInstance().setBackButtonDismissesInAppMessageView(true)
  }
})
```
{% endtab %}
{% endtabs %}

{% alert note %}
この機能が無効になっている場合は、代わりにホストアクティビティのハードウェアの [戻る] ボタンのデフォルト動作が使用されることに注意してください。これにより、[戻る] ボタンで表示されるアプリ内メッセージではなく、アプリケーションが終了することがあります。
{% endalert %}

## 外側のタップでモーダルを閉じる

デフォルトと履歴値は`false`です。つまり、モーダルの外側をクリックしてもモーダルは閉じません。この値を`true`に設定した場合、ユーザーがアプリ内メッセージの外側をタップすると、モーダルアプリ内メッセージが閉じられます。この動作は、以下を呼び出すことで切り替えることができます。

```java
BrazeInAppMessageManager.getInstance().setClickOutsideModalViewDismissInAppMessageView(true)
```

