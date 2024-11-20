---
nav_title: クリック時のカスタム動作
article_title: iOS のアプリ内メッセージクリック動作のカスタマイズ
platform: Swift
page_order: 5
description: "このリファレンス記事では、Swift SDK の iOS アプリ内メッセージングに関するクリック時のカスタム動作について説明します。"
channel:
  - in-app messages
---

# クリック時のカスタム動作

> 各`Braze.InAppMessage` オブジェクトには対応する [`ClickAction`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/clickaction) が含まれ、これによってクリック時の動作が定義されます。 

この動作をカスタマイズするために、以下のサンプルを参照して `clickAction` プロパティを変更できます。

{% tabs %}
{% tab SWIFT %}

```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI, 
  prepareWith context: inout BrazeInAppMessageUI.PresentationContext
) {
  if let newUrl = URL(string: "{your-url}") {
    context.message.clickAction = .url(newUrl, useWebView: true)
  }
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

`inAppMessage(_:prepareWith:)` メソッドは、Objective-C では利用できません。

{% endtab %}
{% endtabs %}

## クリックアクションのタイプ

`Braze.InAppMessage` の`clickAction` プロパティは `.none` にデフォルト設定されていますが、次のうちいずれかの値に設定できます。

| `ClickAction` | クリック時動作 |
| -------------------------- | -------- |
| `.url(URL, useWebView: Bool)` | 指定されたURLを外部ブラウザで開く。`useWebView` が`true` に設定されていれば、ウェブビューで開く。 |
| `.newsFeed` | メッセージがクリックされるとニュースフィードが表示され、メッセージは解除される。<br><br>**注:**ニュースフィードは非推奨になります。詳しくは[マイグレーション・ガイドを]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/)チェックしてほしい。 |
| `.none` | クリックするとメッセージが却下されます。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
ボタンを含むアプリ内メッセージの場合、ボタンテキストを追加する前にクリックアクションが追加されると、メッセージ `clickAction` も最終ペイロードに含まれます。
{% endalert %}

## アプリ内メッセージとボタンクリックのカスタマイズ

アプリ内メッセージがクリックされると、次の [`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate) デリゲートメソッドが呼び出されます。アプリ内メッセージボタンと HTML アプリ内メッセージボタン（リンク）のクリックについては、ボタン ID がオプションのパラメータとして提供されます。

{% tabs %}
{% tab SWIFT %}

```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI,
  shouldProcess clickAction: Braze.InAppMessage.ClickAction,
  buttonId: String?,
  message: Braze.InAppMessage,
  view: InAppMessageView
) -> Bool
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (BOOL)inAppMessage:(BrazeInAppMessageUI *)ui
       shouldProcess:(enum BRZInAppMessageRawClickAction)clickAction
                 url:(NSURL *)uri
            buttonId:(NSString *)buttonId
             message:(BRZInAppMessageRaw *)message
                view:(UIView *)view;
```

{% endtab %}
{% endtabs %}

このメソッドは、Braze がクリックアクションを実行し続けるかどうかを示すブール値を返します。

