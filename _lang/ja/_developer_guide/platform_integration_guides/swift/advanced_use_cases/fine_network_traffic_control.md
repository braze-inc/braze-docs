---
nav_title: きめ細かなネットワークトラフィック制御
article_title: iOS 向けのきめ細かなネットワークトラフィック制御
platform: Swift
page_order: 2
description: "この記事では、Swift SDK のきめ細かなネットワーク トラフィック制御の実装について説明します。"

---

# きめ細かなネットワークトラフィック制御

## リクエスト処理ポリシー

Braze では、ユーザーに対し、以下のプロトコルを使用してネットワーク トラフィックを制御するオプションが提供されます。

### 自動リクエスト処理

***`RequestPolicy` 列挙値: `automatic`***

これが**デフォルトのリクエストポリシー**値です。この値を使用すると、アプリ内メッセージなどの Braze 機能にユーザー向けデータが必要である場合に、即時サーバーリクエストが実行されます。

Braze SDK では、以下を含むすべてのサーバー通信が自動的に処理されます。
- カスタムイベントと属性データの Braze サーバーへのフラッシュ
- コンテンツカードとジオフェンスの更新
- 新しいアプリ内メッセージのリクエスト

サーバーの負荷を最小限に抑えるため、Braze では新規ユーザーデータの定期フラッシュが数秒ごとに実行されます。

### 手動リクエスト処理

***`RequestPolicy` 列挙値: `manual`***

このプロトコルは、次の点を除いて自動リクエスト処理と同じです。
- カスタム属性とカスタムイベントデータが、ユーザーセッションを通じてサーバーに自動でフラッシュされません。
- Braze で、アプリ内メッセージのリクエスト、アプリ内メッセージの Liquid テンプレート、ジオフェンス、位置情報の追跡などの内部機能に対する自動ネットワークリクエストが実行されます。詳細については、`Braze.Configuration.Api.RequestPolicy.manual` の[ドキュメント](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/api-swift.class/requestpolicy-swift.enum/manual)を参照してください。これらの内部リクエストが実行されると、リクエストのタイプによっては、ローカルに保存されたカスタム属性とカスタムイベントデータが Braze サーバーにフラッシュされる場合があります。

### ユーザーデータの手動フラッシュ

データは、次の方法を使用して、いつでも手動で Braze サーバーにフラッシュできます。

{% tabs %}
{% tab SWIFT %}

```swift
AppDelegate.braze?.requestImmediateDataFlush()
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[AppDelegate.braze requestImmediateDataFlush];
```

{% endtab %}
{% endtabs %}
## リクエスト処理ポリシーの設定

### 起動時のリクエストポリシーの設定

これらのポリシーは、アプリの起動時に Braze 構成を初期化する際に設定できます。`configuration` オブジェクトで、次のコードスニペットに示すように [[`Braze.Configuration.Api.RequestPolicy`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/api-swift.class/requestpolicy-swift.enum)] を設定します:

{% tabs %}
{% tab SWIFT %}

```swift
configuration.api.requestPolicy = .automatic
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
configuration.api.requestPolicy = BRZRequestPolicyAutomatic;
```

{% endtab %}
{% endtabs %}


