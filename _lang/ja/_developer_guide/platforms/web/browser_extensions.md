---
nav_title: ブラウザの拡張機能
article_title: Web のブラウザーエクステンション統合
platform: Web
page_order: 20
page_type: reference
description: "この記事では、Braze Web SDK をブラウザーエクステンション (Google Chrome、Firefox) 内で使用する方法について説明します。"

---

# ブラウザ拡張子

> この記事では、Braze Web SDK をブラウザーエクステンション (Google Chrome、Firefox) 内で使用する方法について説明します。

Braze Web SDK をブラウザーエクステンション内に統合し、分析を収集して、豊富なメッセージをユーザーに表示します。これには、**Google Chrome Extensions**と**Firefox Add-Ons**の両方が含まれます。

## サポートされるもの

通常、拡張機能はHTML およびJavaScript であるため、以下にBraze を使用できます。

* **分析**:カスタムイベント、属性をキャプチャし、エクステンション内の繰り返しユーザーの識別も行います。これらのプロファイル特性を使用して、クロスチャネルメッセージングを強化します。
* **アプリ内メッセージ**:ユーザーがネイティブまたはカスタムの HTML メッセージングを使用してエクステンション内でアクションを取ったときに、アプリ内メッセージをトリガーします。
* **コンテンツカード**:オンボーディングまたはプロモーションコンテンツの拡張機能に、ネイティブカードのフィードを追加します。
* **Web プッシュ**:Web ページが現在開かれていない場合でも、タイムリーに通知を送信します。

## サポートされていないもの

* サービスワーカーは Braze Web SDK ではサポートされていませんが、このサポートについては将来検討される予定です。

## 拡張子の種類

Braze は、エクステンションの以下の領域に含めることができます。

| エリア | 詳細 | サポートされるもの |
|--------|-------|------|
| ポップアップページ | [ポップアップ](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Popups)ページは、ブラウザーのツールバーで拡張機能のアイコンをクリックするとユーザーに表示されるダイアログです。| 分析、アプリ内メッセージ、およびコンテンツカード |
| バックグラウンドスクリプト | [バックグラウンドスクリプト](https://developer.chrome.com/extensions/background_pages) (マニフェスト v2のみ) は、エクステンションで、ユーザーナビゲーションの調査および相互作用や、Web ページの変更を行えるようにします (広告ブロッカーがページ上のコンテンツを検出および変更する方法など)。 | 分析、アプリ内メッセージ、コンテンツカード。<br><br>バックグラウンドスクリプトはユーザーには表示されないため、メッセージングを行う場合は、メッセージを表示するときにブラウザーのタブやポップアップページで通信する必要があります。 |
| オプションページ | [[オプションページ](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Options_pages)] を使用して、ユーザーはエクステンション内で設定を切り替えることができます。これは、新しいタブを開封するスタンドアロンのHTMLページです。 | 分析、アプリ内メッセージ、およびコンテンツカード |
{: .reset-td-br-1 .reset-td-br-2, .reset-td-br-3 role="presentation" }

## 権限

Braze SDK (`braze.min.js`) をエクステンションとバンドルされたローカルファイルとして統合する場合、`manifest.json` で追加の権限は必要ありません。 

ただし、[Googleタグマネージャ]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/google_tag_manager/)を使用するか、外部URLからBraze SDKを参照するか、拡張子に厳密なコンテンツセキュリティポリシーを設定した場合は、`manifest.json`の[`content_security_policy`](https://developer.chrome.com/extensions/contentSecurityPolicy)設定を調整して、リモートスクリプトソースを許可する必要があります。

## はじめに

{% alert tip %}
作業を始める前に、Web SDKの[初期SDK設定ガイド]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web)を読んで、JavaScriptの統合全般について理解してください。 <br><br>また、[JavaScript SDK リファレンス](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html) をブックマークして、さまざまなSDK方法と設定オプションの詳細を確認することもできます。
{% endalert %}

Braze Web SDKを統合するには、まず最新のJavaScriptライブラリーをダウンロードする必要がある。これは、NPM を使用するか、[Braze の CDN](https://js.appboycdn.com/web-sdk/latest/braze.min.js) から直接的に読み込むことで実行できます。

または、[Google Tag Manager]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/google_tag_manager/) を使用するか、Braze SDK の外部でホストされたコピーを使用する場合は、外部リソースを読み込むには [`content_security_policy`](https://developer.chrome.com/extensions/contentSecurityPolicy) 設定を `manifest.json` で調整する必要があることに注意してください。

ダウンロードしたら、`braze.min.js` ファイルをエクステンションのディレクトリーの任意の場所にコピーします。

### 拡張機能ポップアップ {#popup}

拡張ポップアップにBrazeを追加するには、通常のWeb サイトと同様に、`popup.html` でローカルJavaScript ファイルを参照します。Google Tag Manager を使用している場合は、代わりに、[Google Tag Manager テンプレート]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/google_tag_manager/)を使用して Braze を追加できます。

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

エクステンションのバックグラウンドスクリプト内で Braze を使用するには、Braze ライブラリーを `background.scripts` 配列の `manifest.json` に追加します。これにより、グローバル`braze` 変数がバックグラウンド スクリプトコンテキストで使用できるようになります。


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

オプションページを (`options` または `options_ui` マニフェストプロパティを介して)使用する場合、[`popup.html` の説明](#popup)で行ったのと同じ方法で Braze を組み込むことができます。

## 初期化

SDK が組み込まれると、通常どおりにライブラリーを初期化できるようになります。 

Cookie はブラウザーエクステンションではサポートされていないため、`noCookies: true` で初期化することで Cookie を無効にできます。

```javascript
braze.initialize("YOUR-API-KEY-HERE", {
    baseUrl: "YOUR-API-ENDPOINT",
    enableLogging: true,
    noCookies: true
});
```

サポートされている初期化オプションの詳細については、[[Web SDK リファレンス](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize)] を参照してください。

## プッシュ

拡張ポップアップダイアログでは、プッシュプロンプトは使用できません(ナビゲーションにURL バーはありません)。このため、エクステンションのポップアップダイアログ内でプッシュ通知の権限を登録して要求するには、[代替プッシュドメイン]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/push_notifications/alternate_push_domain)で説明されているように、代替ドメインの回避策を使用する必要があります。

