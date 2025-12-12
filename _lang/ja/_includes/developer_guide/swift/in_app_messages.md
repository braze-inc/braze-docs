{% multi_lang_include developer_guide/prerequisites/swift.md %} アプリ内メッセージs も有効にする必要があります。

## メッセージの種類

{% tabs %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/swift.md %}
{% endtabs %}

## アプリ内メッセージを有効にする

### ステップ 1: インプリメンテーションを作成する `BrazeInAppMessagePresenter`

Braze にアプリ内メッセージs を表示させるには、`BrazeInAppMessagePresenter` プロトコールのインプリメンテーションを作成し、それをBrazeインスタンスのオプションの`inAppMessagePresenter` に割り当てます。`BrazeInAppMessageUI` オブジェクトをインスタンス化することで、デフォルトの Braze UI プレゼンターを使用することもできます。

`BrazeInAppMessageUI` クラスにアクセスするには、`BrazeUI` ライブラリーをインポートする必要があることに注意してください。

{% tabs %}
{% tab SWIFT %}

```swift
AppDelegate.braze?.inAppMessagePresenter = BrazeInAppMessageUI()
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
AppDelegate.braze.inAppMessagePresenter = [[BrazeInAppMessageUI alloc] init];
```
{% endtab %}
{% endtabs %}

### ステップ 2:一致するトリガーを扱わない

[`BrazeDelegate.(_:noMatchingTriggerForEvent)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazedelegate/braze(_:nomatchingtriggerforevent:)-8rt7y/)を該当する`BrazeDelegate`クラス内に実装します。Braze は、特定のイベントに一致するトリガーを検出できない場合、このメソッドを自動的に呼び出します。
