---
nav_title: ブラウザ関連
article_title: Web のブラウザエクステンションインテグレーション
platform: Web
page_order: 20
page_type: reference
description: "ここでは、ブラウザエクステンション(Google Chrome、Firefox)内のBraze Web SDKの使用方法について説明します。"

---

# ブラウザ拡張子

> ここでは、ブラウザエクステンション(Google Chrome、Firefox)内のBraze Web SDKの使用方法について説明します。

ブラウザー拡張機能内にBraze Web SDKを統合して、分析を収集し、豊富なメッセージングをユーザー s に表示します。これには、**Google Chrome Extensions**と**Firefox Add-Ons**の両方が含まれます。

## サポートされるもの

通常、拡張機能はHTML およびJavaScript であるため、以下にBraze を使用できます。

* **分析**:カスタムイベントs、属性s をキャプチャし、拡張子内の繰り返しユーザーs を識別することもできます。これらのプロファイル特性を使用して電源をクロスチャネルメッセージングにします。
* **In-アプリメッセージ**:ユーザー s が、ネイティブまたはカスタムHTML メッセージングを使用して、拡張機能内でアクションを取得したときに、アプリ内メッセージ s をトリガします。
* **コンテンツカード**:オンボーディングまたはプロモーションコンテンツの拡張機能に、ネイティブカードのフィードを追加します。
* **Webプッシュ**:現在ホームページが開封になっていないときでも、タイムリーに通知sを送信できます。

## サポートされていないもの

* マニフェストv3 サービスワーカーは、Web 環境用のモジュールのインポートをサポートしていません。

## 拡張子の種類

Brazeは、拡張機能の以下の領域に含めることができます。

| エリア | 詳細 | サポートされるもの |
|--------|-------|------|
| ポップアップページ | [ポップアップ][1]ページは、ブラウザーのツールバーで拡張機能のアイコンをクリックするとユーザーに表示されるダイアログです。| 分析、アプリ内メッセージ、およびコンテンツカード |
| バックグラウンドスクリプト | [Background Scripts][2] (マニフェストv2 のみ) は、拡張機能がユーザーナビゲーションを検査して操作したり、Web ページを変更したりすることを許可します(たとえば、広告ブロックがページ上のコンテンツを検出および変更する方法)。 | 分析、アプリ内メッセージ、コンテンツカード。<br><br>バックグラウンドスクリプトはユーザー s には表示されないため、メッセージングでは、メッセージを表示するときにブラウザタブまたはポップアップページと通信する必要があります。 |
| オプションページ | [Options Page][3]を使用すると、ユーザーは拡張子内の設定を切り替えることができます。これは、新しいタブを開封するスタンドアロンのHTMLページです。 | 分析、アプリ内メッセージ、およびコンテンツカード |
{: .reset-td-br-1 .reset-td-br-2, .reset-td-br-3}

## 権限

Braze SDK(`braze.min.js`) を拡張子にバンドルされたローカルファイルとして統合する場合、`manifest.json` に追加の権限は必要ありません。 

ただし、\[Googleタグマネージャ][8]を使用するか、外部URLからBraze SDKを参照するか、拡張子に厳密なコンテンツセキュリティポリシーを設定した場合は、`manifest.json`の[`content_security_policy`][6]設定を調整して、リモートスクリプトソースを許可する必要があります。

## はじめに

{% alert tip %}
作業を始める前に、Web SDKの[初期SDK設定ガイド]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/)を読んで、JavaScriptの統合全般について理解してください。 <br><br>また、[JavaScript SDK リファレンス](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html) をブックマークして、さまざまなSDK方法と設定オプションの詳細を確認することもできます。
{% endalert %}

Braze のWeb SDKを統合するには、まず最新のJavaScript ライブラリーを読み込むする必要があります。これは、NPMを使用するか、[BrazeのCDN][7]から直接的に読み込むすることで実行できます。

または、\[Googleタグマネージャ][8]を使用するか、Braze SDKの外部ホストコピーを使用する場合は、外部リソースを使用する読み込むで、`manifest.json`の[`content_security_policy`][6]設定を調整する必要があることに留意してください。

ed を読み込むしたら、`braze.min.js` ファイルを拡張子のディレクトリーのどこかにコピーしてください。

### 拡張機能ポップアップ {#popup}

拡張ポップアップにBrazeを追加するには、通常のWeb サイトと同様に、`popup.html` でローカルJavaScript ファイルを参照します。Google Tag Manager を使用している場合は、代わりに\[Google Tag Manager テンプレート s][8] を使用してBrazeを追加できます。

```html
<html>
    <title>popup.html</title>
    <!-- Add the Braze library -->
    <script src="/relative/path/to/braze.min.js"></script>
    <script>
    // Initialize Braze here
    </script>
</html>
```

### バックグラウンドスクリプト(マニフェストv2 のみ) {#background-script}

拡張のバックグラウンド 内でBraze を使用するには、`background.scripts` 配列の`manifest.json` にBraze ライブラリーを追加します。これにより、グローバル`braze` 変数がバックグラウンド スクリプトコンテキストで使用できるようになります。


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

### オプションページ {#options-page}

オプションページ(`options` または`options_ui` マニフェストプロパティーを使用) を使用する場合は、[`popup.html` 命令](#popup) と同じようにBrazeを含めることができます。

## 初期化

SDKを含めると、通常どおりにライブラリーを初期化できます。 

Cookie s はブラウザ拡張ではサポートされていないため、`noCookies: true` で初期化することでCookie s を無効にできます。

```javascript
braze.initialize("YOUR-API-KEY-HERE", {
    baseUrl: "YOUR-API-ENDPOINT",
    enableLogging: true,
    noCookies: true
});
```

サポートされている初期化オプションの詳細については、\[Web SDK reference][10] を参照してください。

## プッシュ

拡張ポップアップダイアログでは、プッシュプロンプトは使用できません(ナビゲーションにURL バーはありません)。したがって、拡張のポップアップダイアログ内でプッシュ許可を登録して要求するには、\[代替プッシュドメイン][11]]で説明されているように、代替ドメインの回避策を使用する必要があります。

[1]: https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Popups
[2]: https://developer.chrome.com/extensions/background_pages
[3]: https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Options_pages
[6]: https://developer.chrome.com/extensions/contentSecurityPolicy
[7]: https://js.appboycdn.com/web-sdk/latest/braze.min.js
[8]: {{ site.baseurl }}/developer_guide/platform_integration_guides/web/google_tag_manager/
[10]: https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize
[11]: {{ site.baseurl }}/developer_guide/platform_integration_guides/web/push_notifications/alternate_push_domain
