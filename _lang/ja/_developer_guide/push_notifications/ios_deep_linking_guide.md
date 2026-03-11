---
page_order: 1.1
nav_title: iOSディープリンクガイド
article_title: iOSディープリンクガイド
description: "iOSアプリでどのタイプのディープリンクを使うべきか、AASAファイルが必要な場合、そして実装すべきアプリデリゲートメソッドを学ぶ。"
channel:
  - push notifications
  - in-app messages
  - content cards
  - email
---

# iOSディープリンクガイド

> このガイドは、iOSアプリに適したディープリンク戦略を選ぶのに役立つ。どのメッセージングチャネルを使うか、Branchのようなサードパーティのリンクプロバイダーを利用するかどうかによって、適切な戦略を選択できる。

実装の詳細については、[ディープリンクを]({{site.baseurl}}/developer_guide/push_notifications/deep_linking/?sdktab=swift)参照せよ。トラブルシューティングについては、[ディープリンクのトラブルシューティングを]({{site.baseurl}}/developer_guide/push_notifications/deep_linking_troubleshooting)参照せよ。

## リンクの種類を選ぶ

iOSアプリ内でBrazeメッセージのリンクを処理する方法は三つある。それぞれが異なる働きをし、異なるチャネルやユースケースに適している。

| リンクの種類 | 例 | 最適な用途 | アプリがインストールされていなくても開封できるのか？ |
|---|---|---|---|
| **カスタムスキーム** | `myapp://products/123` | プッシュ通知、アプリ内メッセージ、コンテンツカード | ダメだ——リンクが失敗した |
| **ユニバーサルリンク** | `https://myapp.com/products/123` | メール、SMS、クリックトラッキング機能付きチャネル | そうだ — Webに戻る |
| **アプリ内で Web URL を開く** | 任意`https://`のURL | モーダルWebViewでWebコンテンツを表示する | N/A — WebViewに表示される |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### カスタムスキームのディープリンク

カスタムスキームのディープリンク（例：`myapp://products/123`）は、アプリを特定の画面に直接開く。それらは、リンクが第三者によって変更されないチャネルにとって最も簡単な選択肢だ。

**カスタムスキームのディープリンクを使用するのは、次の場合だ：**
- プッシュ通知、アプリ内メッセージ、またはコンテンツカードの送信
- アプリがインストールされていなければ、リンクが機能する必要はない。
- クリックトラッキング (メールESPリンクラッピング) は必要ない

**カスタムスキームのディープリンクは、以下の場合には使用しないこと：**
- メール送信時、メールサービスプロバイダー (ESP)はクリックトラッキングのためにリンクをラップする。これによりカスタムスキームが破綻する。
- アプリがインストールされていない場合、Webページにリダイレクトするためのリンクが必要だ。

### ユニバーサルリンク

ユニバーサルリンク（例：`https://myapp.com/products/123`）は標準的なHTTPS URLであり、iOSはこれをブラウザで開封する代わりにアプリへ転送できる。サーバー側の設定（AASAファイル）とアプリ側の設定（関連ドメインの権限）が必要だ。

**ユニバーサルリンクを使うのは、次の場合だ：**
- メールを送っている。メールサービスプロバイダー (ESP)はトラッキングのためにリンクをラップするから、リンクはHTTPSでなければならない。
- SMSやその他のチャネルで、リンクが包まれたり短縮されたりしている場合。
- アプリがインストールされていない場合、Webページにリダイレクトするためのリンクが必要だ。
- BranchやAppsFlyerのようなサードパーティのリンクプロバイダーを使っている。

**以下の場合にはユニバーサルリンクを使用するな：**
- 必要なのは、プッシュ通知、アプリ内メッセージ、またはコンテンツカードからのディープリンクだけだ。カスタムスキームの方が単純だ。

### アプリ内でWebURLを開く

このオプションは、アプリ内のモーダルWebView内でウェブページを開く。これは完全にBraze SDKによって処理される。URL処理のコードを`Braze.WebViewController`一切書く必要はない。

**「アプリ内でWeb URLを開く」は次の場合に使用する：**
- アプリを離れることなく、Webページ（プロモーションや記事など）を表示したい。
- そのURLは標準的なHTTPSWebページであり、特定のアプリ画面へのディープリンクではない。

**以下の場合には「アプリ内でWeb URLを開く」を使用しないこと：**
- アプリ内の特定のビューに移動する必要がある。代わりに、カスタムスキームかユニバーサルリンクを使え。
- そのWebページは認証が必要か、埋め込みをブロックするコンテンツセキュリティポリシーヘッダーを持っている。

## 各リンクタイプに必要なもの

### カスタムスキームのディープリンク

| 必要条件 | 詳細 |
|---|---|
| AASAファイル | 不要だ |
| `Info.plist` | あなたの計画をに登録し`CFBundleURLTypes`、それに追加する `LSApplicationQueriesSchemes` |
| アプリデリゲートメソッド | URLを解析して移動する`application(_:open:options:)`処理を実装する |
| Braze SDKの設定 | なし — SDKはデフォルトでカスタムスキームURLを開く |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### ユニバーサルリンク

| 必要条件 | 詳細 |
|---|---|
| AASAファイル | 必須 — ホスト先 `https://yourdomain.com/.well-known/apple-app-site-association` |
| 関連ドメイン | Xcodeの**「署名」**セクション**&**にある**「機能」**に`applinks:yourdomain.com`追加する |
| アプリデリゲートメソッド | 実装`application(_:continue:restorationHandler:)`する `NSUserActivity` |
| Braze SDKの設定 | セット `configuration.forwardUniversalLinks = true` |
| BrazeDelegate（任意） | カスタムルーティング（例：Branch）の`braze(_:shouldOpenURL:)`実装 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Braze経由でメールを送信する場合、メールサービスプロバイダー (ESP)（SendGrid、SparkPost、またはAmazon SES）はリンクをトラッキングドメインで囲む。AASAファイルは、メインドメインだけでなく、トラッキング用ドメインにもホストしなければならない。完全な設定については、[ユニバーサルリンクとアプリリンクを]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links/)参照せよ。
{% endalert %}

### アプリ内でWebURLを開く

| 必要条件 | 詳細 |
|---|---|
| AASAファイル | 不要だ |
| アプリデリゲートメソッド | 不要だ — SDKがこれを自動的に処理する |
| Braze SDKの設定 | なし — キャンペーン作成ツールで**「アプリ内でWeb URLを開封する」**を選択する |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## AASAファイルが必要な時 {#when-aasa}

**ユニバーサルリンク**を使用する場合にのみ、Apple App Site Association (AASA) ファイルが必要となる。それはiOSに、アプリが処理できるURLを伝えるものだ。

AASAファイルが必要なのは以下の場合だ：

- メールキャンペーンでディープリンクを送る（なぜならメールサービスプロバイダー (ESP) はリンクを HTTPS のトラッキング URL でラップするからだ）。
- SMSキャンペーンでディープリンクを送る（リンクがHTTPS URLに短縮される可能性があるため）。
- BranchやAppsFlyer、あるいは他のリンクプロバイダーを使っている（なぜなら彼らは独自のHTTPSドメインを使っているからだ）。
- ユニバーサルリンクは、プッシュ通知やアプリ内メッセージ、あるいはコンテンツカードから使用できる（あまり一般的ではないが、可能ではある`forwardUniversalLinks = true`）。

次の場合にはAASAファイルは必要ない：

- カスタムスキームのディープリンク（例：`myapp://`）は、プッシュ通知、アプリ内メッセージ、またはコンテンツカードからのみ使用する。
- **アプリ内でWebURLを開封する**オプションを使う。

AASAの設定手順については、[ユニバーサルリンクとアプリリンクを]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links/#setting-up-universal-links-and-app-links)参照せよ。

## アプリコードでリンクを処理する必要がある時 {#when-app-code}

どのデリゲートメソッドを実装するかは、使用するリンクの種類によって決まる。

| 委譲メソッド | 取っ手 | いつ実装するか |
|---|---|---|
| `application(_:open:options:)` | カスタムスキームの`myapp://`ディープリンク | どのチャネルからでもカスタムスキームのディープリンクを使う |
| `application(_:continue:restorationHandler:)` | ユニバーサル`https://`リンク | メールやSMSから、あるいは `forwardUniversalLinks = true` |
| `BrazeDelegate.braze(_:shouldOpenURL:)` | SDKによって開封された全てのURL | カスタムルーティングロジックが必要だ（例：Branch処理、条件分岐処理、分析など） |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert tip %}
Branchのようなサードパーティのリンクプロバイダーを使用する場合、URLをインターセプトしてプロバイダーのSDKに転送する`BrazeDelegate.braze(_:shouldOpenURL:)`実装を行う。完全な例については[、ディープリンクのBranchを]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking/)参照せよ。
{% endalert %}

## BranchをBrazeと併用する {#branch}

[Branchを]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking/)リンクプロバイダーとして使用する場合、標準的なユニバーサルリンクの設定に加えて、いくつかの追加ステップが必要となる：

1. **Branch SDK**：[Branchのドキュメント](https://help.branch.io/developers-hub/docs/native-sdks-overview)に従ってBranch SDKを統合する。
2. **関連ドメイン**：Xcodeの**「署名&」**設定で、Branchドメイン（例：`applinks:yourapp.app.link`）を追加する。
3. **BrazeDelegate**:BranchリンクをBrazeが直接処理するのではなく、Branch SDKにルーティングするように`braze(_:shouldOpenURL:)`実装する。
4. **ユニバーサルリンクを転送する**：Braze SDKの設定で`configuration.forwardUniversalLinks = true`設定せよ。

実装の詳細とデバッグのガイダンスについては、[ディープリンク用のBranchを]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking/)参照せよ。