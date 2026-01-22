## ネットワーク・トラフィック・コントロール

### 加工方針を要請する

Braze では、ユーザーに対し、以下のプロトコルを使用してネットワーク トラフィックを制御するオプションが提供されます。

{% tabs local %}
{% tab automatic %}
デフォルトでは、`RequestPolicy` enumの値は`automatic` に設定されている。設定すると、アプリ内メッセージなどユーザー向けデータがBraze機能に必要な場合に、即時サーバーリクエストが実行される。

Braze SDK では、以下を含むすべてのサーバー通信が自動的に処理されます。

- カスタムイベントと属性データの Braze サーバーへのフラッシュ
- コンテンツカードとジオフェンスの更新
- 新しいアプリ内メッセージのリクエスト

サーバーの負荷を最小限に抑えるため、Braze では新規ユーザーデータの定期フラッシュが数秒ごとに実行されます。
{% endtab %}

{% tab manual %}
`RequestPolicy` 列挙値が`manual` の場合、それ以外は自動リクエスト処理と同じパフォーマンスをする：

- カスタム属性とカスタムイベントデータが、ユーザーセッションを通じてサーバーに自動でフラッシュされません。
- Braze で、アプリ内メッセージのリクエスト、アプリ内メッセージの Liquid テンプレート、ジオフェンス、位置情報の追跡などの内部機能に対する自動ネットワークリクエストが実行されます。詳細については、`Braze.Configuration.Api.RequestPolicy.manual` の[ドキュメント](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/api-swift.class/requestpolicy-swift.enum/manual)を参照してください。これらの内部リクエストが行われると、リクエストタイプによっては、Brazeはローカルに保存されたカスタム属性やカスタムイベントデータをBrazeサーバーにフラッシュすることがある。
{% endtab %}
{% endtabs %}

### ユーザーデータの手動フラッシュ

データは、次の方法を使用して、いつでも手動で Braze サーバーにフラッシュできます。

{% tabs %}
{% tab swift %}
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

### リクエスト処理ポリシーの設定

これらのポリシーは、アプリの起動時に Braze 構成を初期化する際に設定できます。`configuration` オブジェクトで、次のコードスニペットに示すように [[`Braze.Configuration.Api.RequestPolicy`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/api-swift.class/requestpolicy-swift.enum)] を設定します:

{% tabs %}
{% tab swift %}
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
