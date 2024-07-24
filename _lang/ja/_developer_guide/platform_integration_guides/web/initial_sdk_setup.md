---
nav_title: SDK の初期セットアップ
article_title: Braze Web SDKの初期設定
platform: Web
page_order: 0
page_type: reference
---

# Web用の初期SDKセットアップ

> このリファレンス記事では、Braze Web SDK のインストール方法について説明します。Braze Web SDKを使用すると、分析を収集し、リッチなアプリ内メッセージ、プッシュ、およびコンテンツカードメッセージをWebユーザーに表示できます。完全な技術リファレンスについては、[JavaScriptドキュメント][9]をご覧ください。

{% multi_lang_include archive/web-v4-rename.md %}

## ステップ 1:Brazeライブラリーをインストールする

次の方法のいずれかを使用して、Brazeライブラリーをインストールできます。あなたのWeb サイトが`Content-Security-Policy`を使用している場合は、ライブラリーをインストールする前に、[コンテンツセキュリティポリシーヘッダーガイド]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_security_policy/)を参照してください。

{% alert important %}
ほとんどの広告ブロッカーはBraze Web SDKをブロックしませんが、より制限の厳しい広告ブロッカーは問題を引き起こすことが知られています。
{% endalert %}

{% tabs local %}
{% tab package manager %}
サイトでNPMまたはYarnパッケージマネージャーを使用している場合、依存関係として[Braze NPMパッケージ](https://www.npmjs.com/package/@braze/web-sdk)を追加できます。

TypeScriptの定義はv3.0.0から含まれています。2.x から 3.x へのアップグレードに関する注意事項については、[変更履歴](https://github.com/braze-inc/braze-web-sdk/blob/master/UPGRADE_GUIDE.md)をご覧ください。

```bash
npm install --save @braze/web-sdk
# or, using yarn:
# yarn add @braze/web-sdk
```

インストールが完了すると、通常の方法でライブラリーを`import`または`require`できます。

```typescript
import * as braze from "@braze/web-sdk";
// or, using `require`
const braze = require("@braze/web-sdk");
```
{% endtab %}

{% tab google tag manager %}
Braze Web SDKはGoogle Tag Managerテンプレートライブラリーからインストールできます。サポートされているタグは2つです:

1. 初期化タグ: Web SDKをWebサイトにロードし、オプションで外部ユーザーIDを設定します。
2. アクションタグ: カスタムイベント、購入、ユーザーIDの変更、またはSDKトラッキングの切り替えをトリガーするために使用されます。

[Google Tag Manager]({{site.baseurl}}/developer_guide/platform_integration_guides/web/google_tag_manager/)インテグレーションガイドをご覧ください。
{% endtab %}

{% tab braze cdn %}
CDNホストのスクリプトを参照して、ライブラリーを非同期にロードすることで、Braze Web SDKを直接HTMLに追加します。

<script src="https://braze-inc.github.io/embed-like-gist/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Floading-snippet.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>
{% endtab %}
{% endtabs %}

## ステップ2:SDK の初期化

Braze Web SDK を Web サイトに追加したら、Braze ダッシュボードの **設定** > **アプリ設定** にある API キーと [SDKエンドポイント URL]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints) を使用してライブラリーを初期化します。

{% alert note %}
Brazeの初期化オプションをタグマネージャーで設定している場合は、このステップをスキップできます。
{% endalert %}

オプションの完全なリストについては`braze.initialize()`、および他のJavaScriptメソッドについては、[JavaScriptドキュメント](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize)を参照してください。

```javascript
// initialize the SDK
braze.initialize('YOUR-API-KEY-HERE', {
    baseUrl: "YOUR-SDK-ENDPOINT-HERE"
});

// optionally show all in-app messages without custom handling
braze.automaticallyShowInAppMessages();

// if you use Content Cards
braze.subscribeToContentCardsUpdates(function(cards){
    // cards have been updated
});

// optionally set the current user's external ID before starting a new session
// you can also call `changeUser` later in the session after the user logs in
if (isLoggedIn){
    braze.changeUser(userIdentifier);
}

// `openSession` should be called last - after `changeUser` and `automaticallyShowInAppMessages`
braze.openSession();
```

{% alert important %}
モバイルまたはWebデバイスの匿名ユーザーは、[MAU]({{site.baseurl}}/user_guide/data_and_analytics/reporting/understanding_your_app_usage_data/#monthly-active-users)にカウントされる場合があります。その結果、これらのユーザーをMAUカウントから除外するために、条件付きでSDKを読み込むまたは初期化することを検討するかもしれません。
{% endalert %}

## ステップ 3:プッシュ通知を設定する（オプション）

Braze Web SDKのプッシュ通知を設定するには、追加の設定が必要です。完全なウォークスルーについては、[Webのプッシュ通知]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration/)を参照してください。

## ログイン

ログをすばやく有効にするには、`?brazeLogging=true` を Web サイトの URL にパラメーターとして追加できます。あるいは、[基本的な](#basic-logging)または[カスタム](#custom-logging)ロギングを有効にすることができます。

### 基本的なロギング

{% tabs local %}
{% tab before initialization %}
SDKを初期化する前に、基本的なデバッグメッセージをjavascriptコンソールに記録するために`enableLogging`を使用します。

```javascript
enableLogging: true
```

あなたの方法は次のようにする必要があります:

```javascript
braze.initialize('API-KEY', {
    baseUrl: 'API-ENDPOINT',
    enableLogging: true
});
braze.openSession();
```
{% endtab %}

{% tab after initialization %}
SDKが初期化された後、基本的なデバッグメッセージをjavascriptコンソールに記録するには`braze.toggleLogging()`を使用します。あなたの方法は次のようにする必要があります:

```javascript
braze.initialize('API-KEY', {
    baseUrl: 'API-ENDPOINT',
});
braze.openSession();
...
braze.toggleLogging();
```
{% endtab %}
{% endtabs %}

{% alert important %}
基本的なログはすべてのユーザーに表示されるため、無効にするか、[ `setLogger` ](#custom-logging) に切り替えてから、コードを本番環境にリリースすることを検討してください。
{% endalert %}

### カスタムロギング

`setLogger` を使用して、カスタムデバッグメッセージをJavaScriptコンソールに記録します。基本的なログとは異なり、これらのログはユーザーには表示されません。

```javascript
setLogger(loggerFunction: (message: STRING) => void): void
```

メッセージを単一の文字列パラメータとして`STRING`に置き換えます。あなたの方法は次のようにする必要があります:

```javascript
braze.initialize('API-KEY');
braze.setLogger(function(message) {
    console.log("Braze Custom Logger: " + message);
});
braze.openSession();
```

## SDKのアップグレード

{% multi_lang_include archive/web-v4-rename.md %}

コンテンツ配信ネットワークからBraze Web SDKを参照する場合、例えば`https://js.appboycdn.com/web-sdk/a.a/braze.min.js`（デフォルトの統合手順で推奨されているように）、ユーザーはサイトをリフレッシュするたびにマイナーアップデート（バグ修正および後方互換性のある機能、上記の例ではバージョン`a.a.a`から`a.a.z`まで）を自動的に受け取ります。

ただし、重要な変更をリリースする場合、統合に影響を与える可能性のある重大な変更がないようにするために、Braze Web SDKを手動でアップグレードする必要があります。さらに、SDKをダウンロードして自分でホストする場合、自動的にバージョンアップデートを受け取ることはできず、最新の機能やバグ修正を受け取るためには手動でアップグレードする必要があります。

RSSリーダーやお好みのサービスでリリースフィードをフォローすることで、最新のリリース情報を常に把握できます。また、Web SDKのリリース履歴の全容については、変更履歴をご覧ください。Braze Web SDKをアップグレードするには:

- {更新} {Braze} {ライブラリー} バージョンを変更することによって `https://js.appboycdn.com/web-sdk/[OLD VERSION NUMBER]/braze.min.js` のバージョン番号を変更するか、パッケージ{マネージャー}の依存関係で変更します。
- Web プッシュが統合されている場合、サイトのサービスワーカーファイルを更新してください。デフォルトでは、これはサイトのルートディレクトリの`/service-worker.js`にありますが、いくつかの統合では場所がカスタマイズされている場合があります。サービスワーカーファイルをホストするには、ルートディレクトリにアクセスする必要があります。

これらの2つのファイルは、適切な機能のために互いに調整して更新する必要があります。

## 代替統合方法

### サーバーサイドレンダリングフレームワーク {#ssr}

サーバーサイドレンダリングフレームワーク（Next.jsなど）を使用する場合、SDKはブラウザ環境で実行されることを前提としているため、エラーが発生する可能性があります。これらの問題は、SDKを動的にインポートすることで解決できます。

その際に必要な部分のSDKを別のファイルにエクスポートし、そのファイルを動的にコンポーネントにインポートすることで、ツリーシェイキングの利点を保持できます。

```javascript
// MyComponent/braze-exports.js
// export the parts of the SDK you need here
export { initialize, openSession } from "@braze/web-sdk";

// MyComponent/MyComponent.js
// import the functions you need from the braze exports file
useEffect(() => {
    import("./braze-exports.js").then(({ initialize, openSession }) => {
        initialize("YOUR-API-KEY-HERE", {
            baseUrl: "YOUR-SDK-ENDPOINT",
            enableLogging: true,
        });
        openSession();
    });
}, []);
```

あるいは、アプリのバンドルにwebpackを使用している場合、マジックコメントを利用して、必要な部分だけを動的にインポートすることができます。

```javascript
// MyComponent.js
useEffect(() => {
    import(
        /* webpackExports: ["initialize", "openSession"] */
        "@braze/web-sdk"
    ).then(({ initialize, openSession }) => {
        initialize("YOUR-API-KEY-HERE", {
            baseUrl: "YOUR-SDK-ENDPOINT",
            enableLogging: true,
        });
        openSession();
    });
}, []);
```

### Viteサポート{#vite}

Viteを使用していて、循環依存関係や`Uncaught TypeError: Class extends value undefined is not a constructor or null`に関する警告が表示される場合は、Braze SDKをその[依存関係の検出](https://vitejs.dev/guide/dep-pre-bundling.html#customizing-the-behavior)から除外する必要があるかもしれません。

```
optimizeDeps: {
    exclude: ['@braze/web-sdk']
},
```

### エレクトロンのサポート {#electron}

Electron は Web プッシュ通知を公式にサポートしていません（参照：この [GitHub issue](https://github.com/electron/electron/issues/6697)）。他の[開封ソースの回避策](https://github.com/MatthieuLemoine/electron-push-receiver)も試してみることができますが、Brazeによってテストされていません。

### AMDモジュールローダー

RequireJSや他のAMDモジュールローダーを使用する場合は、他のリソースと同様にライブラリーのコピーをセルフホスティングして参照することをお勧めします。

```javascript
require(['path/to/braze.min.js'], function(braze) {
  braze.initialize('YOUR-API-KEY-HERE', { baseUrl: 'YOUR-SDK-ENDPOINT' });
  braze.automaticallyShowInAppMessages();
  braze.openSession();
});
```
### 代替案 No AMD インストール

あなたのサイトがRequireJSや他のAMDモジュールローダーを使用しているが、上記の他のオプションのいずれかを通じてBraze Web SDKを読み込みたい場合、AMDサポートを含まないバージョンのライブラリーを読み込むことができます。このバージョンのライブラリーは、次のCDNの場所からロードできます:

<script src="https://braze-inc.github.io/embed-like-gist/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Fno-amd-library.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

### Tealium iQ
Tealium iQは基本的なターンキーBraze統合を提供します。統合を構成するには、Tealiumタグ管理インターフェイスでBrazeを検索し、ダッシュボードからWeb SDK APIキーを提供します。

詳細や詳細なTealium構成サポートについては、[統合ドキュメント]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/#about-tealium)をご覧いただくか、Tealiumのアカウントマネージャーにお問い合わせください。

### 他のタグマネージャー
Brazeは、カスタムHTMLタグ内の統合手順に従うことで、他のタグ管理ソリューションとも互換性がある場合があります。これらのソリューションの評価に関して支援が必要な場合は、Brazeの担当者に連絡してください。

### Jestフレームワークのトラブルシューティング {#jest}

Jestを使用する際に、`SyntaxError: Unexpected token 'export'`と同様のエラーが表示されることがあります。これを修正するには、`package.json`の設定をAdjustしてBraze SDKを無視するようにします。

```
"jest": {
  "transformIgnorePatterns": [
    "/node_modules/(?!@braze)"
  ]
}
```

[9]: https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html "JSDocs"