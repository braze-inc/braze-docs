---
nav_title: ディープリンクのトラブルシューティング
article_title: ディープリンクのトラブルシューティング
description: "iOSにおける一般的なディープリンクの問題とその診断方法。カスタムスキームリンク、ユニバーサルリンク、メールリンク、Branchなどのサードパーティプロバイダーを含む。"
page_order: 1.2
channel:
  - push notifications
  - in-app messages
  - content cards
  - email
---

# ディープリンクのトラブルシューティング

> このページでは、iOSにおける一般的なディープリンクの問題と、その診断方法について説明する。適切なリンクタイプを選ぶための助けが必要な場合は、[iOSディープリンクガイドを]({{site.baseurl}}/developer_guide/push_notifications/ios_deep_linking_guide)参照せよ。実装の詳細については、[ディープリンクを]({{site.baseurl}}/developer_guide/push_notifications/deep_linking/?sdktab=swift)参照せよ。

## カスタムスキームのディープリンクが正しいビューを開かない

カスタムスキームのディープリンク（例：`myapp://products/123`）がアプリを開くが、意図した画面に移動しない場合：

1. **スキームが登録されていることを確認せよ。**Xcodeでは、スキーマが の`CFBundleURLTypes`下にリスト`Info.plist`されていることを確認せよ。
2. **ハンドラーを確認しろ。**にブレークポイントを設定し、`application(_:open:options:)`それが呼び出されていることを確認し、パラメータ`url`を検査する。
3. **リンクを独立系でテストする。**ターミナルから次のコマンドを実行して、Brazeの外でディープリンクをテストする。
   ```bash
   xcrun simctl openurl booted "myapp://products/123"
   ```
   リンクがここで機能しない場合、問題はアプリ側のURL処理にある。Braze側ではない。
4. **URLの形式を確認しろ。**キャンペーン内のURLが、ハンドラーが期待するものと一致しているか確認せよ。よくある間違いには、パスコンポーネントの欠落や大文字小文字の誤りがある。

## ユニバーサルリンクはアプリではなくSafariで開封する

ユニバーサルリンク（例：`https://myapp.com/products/123`）がアプリではなくSafariで開封する場合：

### 関連ドメインの権限を確認する

Xcodeで、アプリターゲット＞**署名&**＞**機能**に移動し、**関連付けられたドメイン**の下に「」`applinks:yourdomain.com`がリストされていることを確認する。

### AASAファイルを検証する

Apple アプリサイト協会（AASA）ファイルは、以下のいずれかの場所にホストされなければならない：

- `https://yourdomain.com/.well-known/apple-app-site-association`
- `https://yourdomain.com/apple-app-site-association`

以下のことを確認せよ：

- そのファイルは有効な証明書を使ってHTTPS経由で提供されている。
- それは`Content-Type`である`application/json`。
- ファイルサイズは128キロバイト未満だ。
- チームIDとバンドルID`appID`が一致する（例：`ABCDE12345.com.example.myapp`）。
- 配列`paths`には`components`、期待するURLパターンが含まれている。

AASAの検証は[、Appleの検索検証ツール](https://search.developer.apple.com/appsearch-validation-tool/)を使うか、以下のコマンドを実行することで行える：

```bash
swcutil dl -d yourdomain.com
```

### 確認しろ `AppDelegate`

が`application(_:continue:restorationHandler:)`実装されていることを確認し、`AppDelegate`が`NSUserActivity`正しく処理されるようにせよ：

```swift
func application(_ application: UIApplication,
                 continue userActivity: NSUserActivity,
                 restorationHandler: @escaping ([UIUserActivityRestoring]?) -> Void) -> Bool {
  guard userActivity.activityType == NSUserActivityTypeBrowsingWeb,
        let url = userActivity.webpageURL else {
    return false
  }
  // Handle the URL
  return true
}
```

### Braze SDKの設定を確認する

Braze配信のプッシュ通知、アプリ内メッセージ、またはコンテンツカードからユニバーサルリンクを使用している場合、以下の`forwardUniversalLinks`設定が有効になっていることを確認せよ：

```swift
let configuration = Braze.Configuration(apiKey: "<BRAZE_API_KEY>", endpoint: "<BRAZE_ENDPOINT>")
configuration.forwardUniversalLinks = true
```

{% alert note %}
ユニバーサルリンクを転送するには、アプリケーション権限にアクセスできる必要があります。シミュレータで実行している場合、これらの権限は直接利用できない。シミュレータでテストするには、**Copy Bundle Resources**ビルドフェーズにファイル`.entitlements`を追加する。
{% endalert %}

### 長押しの問題を確認する

ユニバーサルリンクを長押しして「**開封**」を選択すると、iOSはそのドメインのユニバーサルリンク関連付けを解除する可能性がある。これはiOSの既知の動作だ。リセットするには、リンクをもう一度長押しして**［アプリ名］で開封**を選択する。

## メールからのディープリンクでアプリが開かない

メール内のリンクは、メールサービスプロバイダー (ESP)のトラッキングシステムを経由する。このシステムはリンクを追跡用ドメイン（例：`https://click.yourdomain.com/...`）で囲む。メールからユニバーサルリンクを機能させるには、トラッキングドメイン上でAASAファイルを設定する必要がある。メインドメインだけではなく、トラッキングドメインでも設定しなければならない。

### トラッキングドメインAASAを確認せよ

1. メールサービスプロバイダー (ESP) の設定（SendGrid、SparkPost、またはAmazon SES）から、クリックトラッキング用のドメインを識別する。
2. AASAファイルをホストする`https://your-click-tracking-domain/.well-known/apple-app-site-association`。
3. クリックトラッキングドメイン上のAASAファイルが、同じ`appID`かつ有効なパスパターンを含んでいることを確認せよ。

ESP固有の設定手順については、[ユニバーサルリンクとアプリリンクを]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links/)参照せよ。

### リダイレクトの連鎖を確認せよ

一部のメールサービスプロバイダー (ESP) は、クリックトラッキングURLから最終的なURLへリダイレクトを行う。ユニバーサルリンクは、iOSが*最初の*ドメイン（クリックトラッキングドメイン）をあなたのアプリに関連付けられていると認識した場合にのみ機能する。リダイレクトがAASAチェックを回避した場合、リンクはSafariで開封される。

テストのため：

1. テストメールを自分に送れ。
2. リンクを長押ししてURLを確認しろ——これがクリックトラッキング用のURLだ。
3. このドメインに有効なAASAファイルがあることを確認せよ。

## ディープリンクはプッシュ通知からは機能するが、アプリ内メッセージからは機能しない（あるいはその逆も同様だ）。

### BrazeDelegateを確認せよ

実装する場合は`BrazeDelegate.braze(_:shouldOpenURL:)`、リンクが全チャネルで一貫して処理されることを確認せよ。その`context`パラメータはソースチャネルを含む。特定のチャネルからのリンクを誤ってフィルターで除外する可能性のある条件付きロジックを探せ。

### 詳細ログの有効化

[詳細ログのイネーブルメントを有効にして]({{site.baseurl}}/developer_guide/verbose_logging)、問題を再現する。ログ`Opening`エントリを探せ：

```
Opening '<URL>':
- channel: <SOURCE_CHANNEL>
- useWebView: <true/false>
- isUniversalLink: <true/false>
```

動作中のチャネルと動作していないチャネルのログ出力を比較せよ。または`useWebView`の差異は、SDKがリンクを異なる`isUniversalLink`方法で解釈していることを示す。

### カスタム表示デリゲートを確認する

カスタムのアプリ内メッセージ表示デリゲートやコンテンツカードのクリックハンドラーを使用する場合、リンクイベントがBraze SDKに正しく渡され、処理されることを確認せよ。

## アプリ内でWebURLを開くと、空白ページや表示されないページが表示される

**アプリ内でWeb URLを開封**すると、WebViewが空白または破損する場合：

1. **URLがHTTPSを使用していることを確認せよ。**SDKのWebViewはATS準拠のURLを必要とする。HTTPリンクは黙って失敗する。
2. **コンテンツセキュリティポリシーのヘッダーを確認する。**対象のWebページが\`set\``X-Frame-Options: DENY`または制限的な`set`を設定`Content-Security-Policy`している場合、WebViewでのレンダリングをブロックする。
3. **カスタムスキームへのリダイレクトを確認せよ。**ウェブページがカスタムスキーム（例：`myapp://`）にリダイレクトする場合、WebViewはそれを処理できない。
4. **SafariでURLを試す。**そのデバイス上のSafariでページが読み込まれない場合、WebViewでも読み込まれない。

## トラブルシューティングBranchとBraze {#branch}

[Branchを]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking/)リンクプロバイダーとして使用する場合：

### BrazeDelegateのBranchへのルーティングを確認する

Branchリンクを必ずインターセプトし、Branch`BrazeDelegate` SDKに渡さなければならない。以下のことを確認せよ：

```swift
func braze(_ braze: Braze, shouldOpenURL context: Braze.URLContext) -> Bool {
  if let host = context.url.host, host.contains("app.link") {
    // Route to Branch SDK
    Branch.getInstance.handleDeepLink(context.url)
    return false
  }
  // Let Braze handle other links
  return true
}
```

Branchリンクに対してreturns`true`が`shouldOpenURL`返された場合、BrazeはBranchへルーティングせず、直接処理する。

### Branchリンクのドメインを確認せよ

Branchのドメインが実際の`BrazeDelegate`Branchリンクドメインと一致していることを確認せよ。Branchはいくつかのドメイン形式を使用する：

- `yourapp.app.link` (デフォルト)
- `yourapp-alternate.app.link` (代替)
- カスタムドメイン（Branchダッシュボードで設定されている場合）

### 両方のSDKのログ記録をイネーブルメントする

連鎖の中でどこでリンクが切れているかを診断するには：

1. [Brazeの詳細ログを]({{site.baseurl}}/developer_guide/verbose_logging)イネーブルメントする。SDKがリンクを受信したことを確認するため、ログ`Opening '<URL>':`エントリを探す。
2. [Branchテストモードを](https://help.branch.io/developers-hub/docs/ios-basic-integration#test-deep-linking)有効にする — リンククリックイベントについてはBranchダッシュボードを確認せよ。
1. [Brazeの詳細ログ記録を]({{site.baseurl}}/developer_guide/verbose_logging)有効にする。SDKがリンクを受信したことを確認するための`Opening '<URL>':`エントリを探す。
2. [Branchテストモードを](https://help.branch.io/developers-hub/docs/ios-basic-integration#test-deep-linking)有効にする。Branchのダッシュボードでリンククリックイベントを確認せよ。
3. Brazeがリンクを記録しているのに、Branchがクリックを認識しない場合、ルーティング`BrazeDelegate`ロジックに問題がある可能性が高い。

### Branchダッシュボードの設定を確認する

Branchダッシュボードで、次のことを確認する：

- お前のアプリの**バンドルID**と**チームID**は、お前のXcodeプロジェクトと一致している。
- **関連ドメイン**にはBranchリンクドメインが含まれる。
- あなたのBranch AASAファイルは有効だ（Branchはこれを自動的にドメイン`app.link`上にホストしている）。

### テストBranchのリンクは独立系で動作する

問題の特定のため、Brazeの外でBranchリンクをテストする。

1. お使いの端末でSafariを開き、Branchリンクをクリックせよ。アプリが開かない場合、問題はBranchまたはAASAの設定にある。Brazeの問題ではない。
2. Branchのリンクをメモアプリに貼り付けてタップする。ユニバーサルリンクは、SafariのアドレスバーからよりもNotesからの方が確実に動作する。

## 一般的なデバッグのコツ

### 詳細なログを出力する

[詳細ログをイネーブル]({{site.baseurl}}/developer_guide/verbose_logging)すると、SDKがリンクをどのように処理しているかを正確に確認できる。探すべき重要なエントリ：

| ログのエントリ | 意味 |
|---|---|
| `Opening '<URL>': - channel: notification` | SDKはプッシュ通知からのリンクを処理している |
| `Opening '<URL>': - channel: inAppMessage` | SDKはアプリ内メッセージからのリンクを処理している |
| `Opening '<URL>': - channel: contentCard` | SDKはコンテンツカードからのリンクを処理している |
| `useWebView: true` | SDKはアプリ内のWebViewでURLを開く |
| `isUniversalLink: true` | SDKはURLをユニバーサルリンクの識別子として識別した |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

これらのログの読み方について詳しくは、[「詳細ログの読み方」]({{site.baseurl}}/developer_guide/verbose_logging)を参照せよ。

### リンクを個別にテストする

Braze経由でテストする前に、ディープリンクまたはユニバーサルリンクが単独で動作することを確認せよ：

- **カスタムスキーム**：ターミナルで`xcrun simctl openurl booted "myapp://path"`実行せよ。
- **ユニバーサルリンク**：URLを物理端末のメモアプリに貼り付けてタップする。Safariのアドレスバーからテストするな。iOSは入力されたURLとタップされたリンクを別々に扱うからだ。
- **Branchリンク**：端末のNotesアプリからBranchリンクを開け。

### 実機でテストする

ユニバーサルリンクはiOSシミュレータでは限定的なサポートしか受けられない。正確な結果を得るためには、必ず実機でテストすること。シミュレータでテストする必要がある場合、**Copy Bundle Resources**ビルドフェーズにファイル`.entitlements`を追加せよ。