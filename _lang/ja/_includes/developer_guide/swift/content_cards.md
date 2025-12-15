## 前提条件

コンテンツカードを使用するには、[ Braze Swift SDK]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift) をアプリに統合する必要があります。ただし、追加のセットアップは必要ありません。

## コントロール者コンテキストの表示

デフォルトのコンテンツカード UI は、Braze SDK の `BrazeUI` ライブラリーから統合できます。`braze` インスタンスを使用して、コンテンツカードビューコントローラーを作成します。コンテンツカードの UI ライフサイクルをインターセプトして対応するには、[`BrazeContentCardUIViewControllerDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcarduiviewcontrollerdelegate) を `BrazeContentCardUI.ViewController` のデリゲートとして実装します。

{% alert note %}
iOS ビューコントローラーのオプションに関する詳細については、[Apple の開発者向けドキュメント](https://developer.apple.com/documentation/uikit/view_controllers/showing_and_hiding_view_controllers)を参照してください。
{% endalert %}

Swift SDKの`BrazeUI` ライブラリーには、[navigation](#swift_navigation) または[モーダル](#swift_modal) という2 つのデフォルトビューコントロールコンテキストがあります。つまり、アプリやサイトに数行のコードを追加することで、これらのコンテキストにおいてコンテンツカードを統合できます。「[カスタマイズガイド]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_styles/?tab=ios)」で説明されているように、どちらのビューにもカスタマイズとスタイル指定のオプションが用意されています。Braze の標準ビューコントローラーの代わりにカスタムコンテンツカードビューコントローラーを作成して、カスタマイズオプションをさらに増やすこともできます。例については、[コンテンツカードの UI チュートリアル](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c2-contentcardsui/)を参照してください。

{% alert important %}
カスタム UI でコントロールバリアントコンテンツカードを処理するには、[`Braze.ContentCard.Control`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/control(_:)) を渡した後、他のコンテンツカードタイプと同様に `logImpression` メソッドを呼び出します。オブジェクトはコントロールインプレッションを暗黙的にログに記録して、ユーザーがいつコントロールカードを表示したかを分析に通知します。
{% endalert %}

### ナビゲーション

ナビゲーションコントローラーは、ナビゲーションインターフェイス内の1つ以上の子ビューコントローラーを管理するビューコントローラーです。以下は、`BrazeContentCardUI.ViewController` インスタンスをナビゲーションコントローラーにプッシュする例です。

{% tabs %}
{% tab swift %}

```swift
func pushViewController() {
  guard let braze = AppDelegate.braze else { return }
  let contentCardsController = BrazeContentCardUI.ViewController(braze: braze)
  // Implement and set `BrazeContentCardUIViewControllerDelegate` if you wish to intercept click actions.
  contentCardsController.delegate = self
  self.navigationController?.pushViewController(contentCardsController, animated: true)
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (void)pushViewController {
  BRZContentCardUIViewController *contentCardsController = [[BRZContentCardUIViewController alloc] initWithBraze:self.braze];
  // Implement and set `BrazeContentCardUIViewControllerDelegate` if you wish to intercept click actions.
  [contentCardsController setDelegate:self];
  [self.navigationController pushViewController:contentCardsController animated:YES];
}
```

{% endtab %}
{% endtabs %}

### モーダル

モーダルプレゼンテーションを使用して、ユーザーに重要情報の入力を求める場合などに、アプリのワークフローを一時的に中断させることができます。このモデルビューでは、上部にナビゲーションバーがあり、バーの横に [**完了**] ボタンがあります。以下は、`BrazeContentCard.ViewController` インスタンスをモーダルコントローラーにプッシュする例です。

{% tabs %}
{% tab swift %}

```swift
func presentModalViewController() {
  guard let braze = AppDelegate.braze else { return }
  let contentCardsModal = BrazeContentCardUI.ModalViewController(braze: braze)
  // Implement and set `BrazeContentCardUIViewControllerDelegate` if you wish to intercept click actions.
  contentCardsModal.viewController.delegate = self
  self.navigationController?.present(contentCardsModal, animated: true, completion: nil)
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (void)presentModalViewController {
  BRZContentCardUIModalViewController *contentCardsModal = [[BRZContentCardUIModalViewController alloc] initWithBraze:AppDelegate.braze];
  // Implement and set `BrazeContentCardUIViewControllerDelegate` if you wish to intercept click actions.
  [contentCardsModal.viewController setDelegate:self];
  [self.navigationController presentViewController:contentCardsModal animated:YES completion:nil];
}
```

{% endtab %}
{% endtabs %}

`BrazeUI` ビューコントローラーの使用例については、[サンプルアプリ](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples)で対応するコンテンツカードの UI サンプルを確認してください。

## 基準カード型式

コンテンツカードデータモデルは、Braze スウィフトSDKの`BrazeKit` モジュールで使用できます。このモジュールには、`Braze.ContentCard` タイプの実装である以下のコンテンツカードタイプが含まれています。コンテンツカードのプロパティとその使用法の完全なリストについては、[`ContentCard` class](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard) を参照してください。 

- 画像のみ
- キャプション付き画像
- クラシック
- クラシック"画像
- コントロール

コンテンツカードデータモデルにアクセスするには、`braze` インスタンスで `contentCards.cards` を呼び出します。カードデータの購読の詳細については、「[分析のロギング]({{site.baseurl}}/developer_guide/content_cards/logging_analytics/)」を参照してください。

{% alert note %}
`BrazeKit` には、Objective-C 互換のための代替[`ContentCardRaw`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcardraw) クラスが用意されています。
{% endalert %}

## カードメソッド

各カードは、カードの状態を管理するためのさまざまなメソッドを含む `Context` オブジェクトを使用して初期化されます。特定のカードオブジェクトの対応する状態プロパティを変更する場合は、これらのメソッドを呼び出します。

| 方法                               | 説明                                                                                                                              |
|--------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| `card.context?.logImpression()`      | コンテンツカードのインプレッションイベントを記録する。                                                                                                   |
| `card.context?.logClick()`           | コンテンツカードのクリックイベントを記録する。                                                                                                        |
| `card.context?.processClickAction()` | 指定された [`ClickAction`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/clickaction) の入力を処理します。 |
| `card.context?.logDismissed()`       | コンテンツカードを閉じたイベントをロギングします。                                                                                                    |
| `card.context?.logError()`           | コンテンツカードに関するエラーを記録する。                                                                                                |
| `card.context?.loadImage()`          | 指定されたコンテンツカードの画像をURLから読み込む。コンテンツカードに画像がない場合、このメソッドはゼロになる。                         |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

詳細については、[`Context` クラスのドキュメント](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcardraw/context-swift.class)を参照してください。
