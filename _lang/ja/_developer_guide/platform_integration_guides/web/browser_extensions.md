---
nav_title: ブラウザ拡張機能
article_title: Web用のブラウザ拡張機能の統合
platform: Web
page_order: 20
page_type: reference
description: "この記事では、ブラウザ拡張機能(Google Chrome、Firefox)内でBraze Web SDKを使用する方法について説明します。"

---

# ブラウザ拡張機能

> この記事では、ブラウザ拡張機能(Google Chrome、Firefox)内でBraze Web SDKを使用する方法について説明します。

Braze Web SDKをブラウザ拡張機能に統合して、分析を収集し、リッチメッセージをユーザーに表示します。これには **、Google Chrome 拡張機能** と **Firefox アドオンの両方が含まれます**。

## サポート対象

一般に、拡張機能はHTMLとJavaScriptであるため、Brazeは次の目的で使用できます。

* **アナリティクス**:カスタムイベントや属性をキャプチャし、拡張機能内のリピートユーザーを特定することもできます。これらのプロファイル特性を使用して、クロスチャネルメッセージングを強化します。
* **アプリ内メッセージ**:ユーザーが拡張機能内でアクションを起こしたときに、ネイティブまたはカスタムのHTMLメッセージを使用してアプリ内メッセージをトリガーします。
* **コンテンツカード**:ネイティブ カードのフィードを拡張機能に追加して、オンボーディング コンテンツやプロモーション コンテンツを作成します。
* **Webプッシュ**:Webページが現在開いていないときでも、タイムリーに通知を送信します。

## サポートされていないもの

* Manifest v3 Service Worker は、Web 環境向けのモジュールのインポートをサポートしていません。

## 拡張機能の種類

Brazeは、拡張機能の次の領域に含めることができます。

|エリア |詳細 |サポート対象 |
|--------|-------|------|
|ポップアップページ | [ポップアップ][1] ページは、ブラウザツールバーの拡張機能のアイコンをクリックしたときにユーザーに表示できるダイアログです。|アナリティクス、アプリ内メッセージ、コンテンツカード |
|バックグラウンド スクリプト | [バックグラウンド スクリプト][2] (Manifest v2 のみ) を使用すると、拡張機能でユーザー ナビゲーションを検査して操作したり、Web ページを変更したりできます (たとえば、広告ブロッカーがページ上のコンテンツを検出して変更する方法)。|分析、アプリ内メッセージ、コンテンツカード。<br><br>バックグラウンドスクリプトはユーザーには表示されないため、メッセージングの場合、メッセージを表示するときにブラウザーのタブまたはポップアップページと通信する必要があります。|
|オプション ページ | [[オプション] ページで][3] は、ユーザーは拡張機能内の設定を切り替えることができます。これは、新しいタブを開くスタンドアロンの HTML ページです。 |アナリティクス、アプリ内メッセージ、コンテンツカード |
{: .reset-td-br-1 .reset-td-br-2, .reset-td-br-3}

## 権限

Braze SDK(`braze.min.js`)を拡張機能にバンドルされたローカルファイルとして統合する場合、追加の権限は必要ありません`manifest.json`。 

ただし、[Google Tag Manager][8]を使用している場合、外部URLからBraze SDKを参照している場合、または拡張機能に厳格なコンテンツセキュリティポリシーを設定している場合は、リモートスクリプトソースを許可するように設定`manifest.json`を調整する[`content_security_policy`][6]必要があります。

## 開始:

{% alert tip %}
開始する前に、Web SDK の初期 [SDK セットアップ ガイド]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/) を読んで、JavaScript 統合全般の詳細を確認してください。 <br><br>また、 [JavaScript SDK リファレンス](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html) をブックマークして、さまざまな SDK メソッドと構成オプションの詳細を確認することもできます。
{% endalert %}

BrazeのWeb SDKを統合するには、まず最新のJavaScriptライブラリのコピーをダウンロードする必要があります。これは、NPMを使用するか、 [BrazeのCDN][7]から直接ダウンロードして行うことができます。

また、[Google Tag Manager][8]を使用したり、Braze SDKの外部でホストされているコピーを使用したりする場合は、外部リソース[`content_security_policy`][6]`manifest.json`を読み込むには、.

ダウンロードしたら、必ずファイルを拡張機能のディレクトリのどこかにコピー `braze.min.js` してください。

### 拡張機能のポップアップ {#popup}

Braze を拡張機能のポップアップに追加するには、通常の Web サイトの場合と同様に、 で `popup.html`ローカルの JavaScript ファイルを参照します。Googleタグマネージャーを使用している場合は、代わりに[Googleタグマネージャーテンプレート][8]を使用してBrazeを追加できます。

\`\`\`html
<html>
    <title>popup.html</title>
    <!-- Add the Braze library -->
    <script src="/relative/path/to/braze.min.js"></script>
    <script>
    // Initialize Braze here
    </script>
</html>
```

### バックグラウンド スクリプト (マニフェスト v2 のみ) {#background-script}

拡張機能のバックグラウンドスクリプト内で Braze を使用するには、Braze ライブラリ `manifest.json` を配列に追加します `background.scripts` 。これにより、グローバル `braze` 変数がバックグラウンドスクリプトのコンテキストで使用できるようになります。


```json
{
    "manifest_version": 2,
    "background": {
        "scripts": [
            "relative/path/to/braze.min.js",
            "background.js"
        ],
    }
}
```

### [オプション] ページ {#options-page}

オプションページ(または`options``options_ui`マニフェストプロパティを使用)を使用する場合は、手順と同じように[`popup.html`](#popup)Brazeを含めることができます。

## 初期化

SDK が含まれたら、通常どおりライブラリを初期化できます。 

Cookieはブラウザ拡張機能ではサポートされていないため、で初期化 `noCookies: true`することでCookieを無効にすることができます。

```javascript
braze.initialize("YOUR-API-KEY-HERE", {
    baseUrl: "YOUR-API-ENDPOINT",
    enableLogging: true,
    noCookies: true
});
```

サポートされている初期化オプションの詳細については、[Web SDK リファレンス][10] を参照してください。

## プッシュ

拡張機能のポップアップ ダイアログでは、プッシュ プロンプトは使用できません (ナビゲーションに URL バーがありません)。そのため、拡張機能のポップアップダイアログでプッシュ権限を登録してリクエストするには、[代替プッシュドメイン][11]で説明されているように、代替ドメインの回避策を利用する必要があります。

[1]: https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Popups
[2]: https://developer.chrome.com/extensions/background_pages
[3]: https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Options_pages
[6]: https://developer.chrome.com/extensions/contentSecurityPolicy
[7]: https://js.appboycdn.com/web-sdk/latest/braze.min.js
[8]: {{ site.baseurl }}/developer_guide/platform_integration_guides/web/google_tag_manager/
[10]: https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize
[11]: {{ site.baseurl }}/developer_guide/platform_integration_guides/web/push_notifications/alternate_push_domain
