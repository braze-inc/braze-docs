{% multi_lang_include developer_guide/prerequisites/swift.md %} アプリ内メッセージも有効にする必要がある。

## メッセージの種類

{% tabs %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/swift.md %}
{% endtabs %}

## アプリ内メッセージを有効にする

### ステップ 1: の実装を作成する。 `BrazeInAppMessagePresenter`

Brazeにアプリ内メッセージを表示させるには、`BrazeInAppMessagePresenter` プロトコルの実装を作成し、Brazeインスタンスのオプション`inAppMessagePresenter` に割り当てる。`BrazeInAppMessageUI` オブジェクトをインスタンス化することで、デフォルトの Braze UI プレゼンターを使用することもできます。

`BrazeInAppMessageUI` クラスにアクセスするには、`BrazeUI` ライブラリーをインポートする必要があることに注意してください。

{% tabs %}
{% tab swift %}

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

### ステップ 2:一致するトリガーはない

実装する [`BrazeDelegate.(_:noMatchingTriggerForEvent)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazedelegate/braze(_:nomatchingtriggerforevent:)-8rt7y/)を関連する`BrazeDelegate` クラス内に実装する。Brazeは、特定のイベントに一致するトリガーが見つからない場合、自動的にこのメソッドを呼び出す。
