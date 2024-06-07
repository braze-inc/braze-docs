---
nav_title: SDK の初期セットアップ
article_title: ウェブ用 SDK の初期セットアップ
platform: Web
page_order: 0
page_type: reference
description: "この記事では、Braze Web SDK の SDK の初期セットアップについて説明します。"
search_rank: 4
---

# SDK の初期セットアップ

> この参考記事では、Braze Web SDK のインストール方法について説明します。Braze Web SDKを使用すると、アナリティクスを収集し、豊富なアプリ内メッセージ、プッシュ、コンテンツカードメッセージをウェブユーザーに表示できます。

詳細なテクニカルリファレンスについては、[JavaScriptドキュメントを参照してください][9]。

{% multi_lang_include archive/web-v4-rename.md %}

## ステップ 1:Braze ライブラリをインストールする

Web SDKを統合して分析コンポーネントとメッセージングコンポーネントをサイトに組み込むには、3つの簡単な方法があります。Web [プッシュ機能を使用する予定がある場合は、必ず Push 統合ガイドをご覧ください][16]。

ウェブサイトでが使用されている場合は`Content-Security-Policy`、以下の統合手順に加えて、[CSP ヘッダーガイドに従ってください][19]。

{% alert important %}
ほとんどの広告ブロッカーはBraze Web SDKをブロックしませんが、より制限の厳しい広告ブロッカーが問題を引き起こすことが知られています。
{% endalert %}

### オプション 1: NPMまたはヤーン {#install-npm}

サイトで NPM または Yarn パッケージマネージャーを使用している場合は、[Braze NPM パッケージを依存関係として追加できます](https://www.npmjs.com/package/@braze/web-sdk)。

タイプスクリプト定義はv3.0.0で含まれるようになりました。[2.x から 3.x へのアップグレードに関する注意事項については、変更履歴を参照してください。][17]

\`\`\`bash
npm インストール--保存 @braze /web-sdk
# または、糸を使う：
# ヤーン追加 @braze /web-sdk
\`\`\`

インストールしたら、`import`通常の方法でライブラリを操作できます`require`。

```typescript
import * as braze from "@braze/web-sdk";
// or, using `require`
const braze = require("@braze/web-sdk");
```

### オプション 2: Google tag manager {#install-gtm}

Braze Web SDK は Google タグマネージャーテンプレートライブラリからインストールできます。次の 2 つのタグがサポートされています。

1. 初期化タグ:Web SDK を Web サイトに読み込み、オプションで外部ユーザー ID を設定します。
2. アクションタグ:カスタムイベントの起動、購入、ユーザー ID の変更、または SDK トラッキングの切り替えに使用されます。

詳しくは、[Google タグマネージャー統合ガイドをご覧ください][18]。

### オプション 3: ブレイズ CDN {#install-cdn}

ライブラリを非同期で読み込むCDNホストスクリプトを参照して、Braze Web SDKをHTMLに直接追加してください。

<script src="https://braze-inc.github.io/embed-like-gist/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Floading-snippet.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>


## ステップ 2: Braze の初期化

Braze Web SDK がウェブサイトに追加されたら、Braze ダッシュボードの **[設定] > [**アプリ設定**]** にある API キーと [SDK エンドポイント URL]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints) を使用してライブラリを初期化します。

{% alert note %}
[古いナビゲーションを使用している場合は]({{site.baseurl}}/navigation)**、この情報は **[設定の管理] > [設定]** で確認できます。**
{% endalert %}

{% alert note %}
タグマネージャーで Braze の初期化オプションを設定した場合は、この手順をスキップできます。
{% endalert %}

のオプションの完全なリストについては、`braze.initialize()` [JavaScriptのドキュメントを参照してください](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize)。

\`\`\`javascript
SDK の初期化
braze.initialize ('あなたの-API-KEY-HERE',); {
baseUrl: "YOUR-SDK-ENDPOINT-HERE"
}

//オプションで、カスタム処理なしですべてのアプリ内メッセージを表示します
braze.automaticallyShowInAppMessages();

// if you use Content Cards
braze.subscribeToContentCardsUpdates(function(cards){
// cards have been updated
});

// optionally set the current user's external ID before starting a new session
// you can also call `changeUser` セッションの後半で、ユーザーがログインした後
if (isLoggedIn){
braze.changeUser(userIdentifier);
    ()

//最後に、`openSession``changeUser`そしての後に呼び出す必要があります `automaticallyShowInAppMessages`
braze.openSession();
\`\`\`

その他すべての [JavaScript メソッドについては、JavaScript リファレンスドキュメントを参照してください][9]。

{% alert note %}
モバイルデバイスまたは Web デバイスの匿名ユーザーが [MAU]({{site.baseurl}}/user_guide/data_and_analytics/reporting/understanding_your_app_usage_data/#monthly-active-users) にカウントされる場合があります。そのため、条件付きで SDK をロードまたは初期化して、これらのユーザーを MAU カウントから除外したい場合があります。
{% endalert %}

## ステップ 3: Web push (optional)

Web プッシュ通知を使用するには、追加の設定が必要です。手順については、「[プッシュ通知][16]」を参照してください。

## トラブルシューティング {#error-logging}

トラブルシューティングに役立つように、SDK で詳細ロギングを有効にできます。これは開発には便利ですが、すべてのユーザーに表示されるので、このオプションを削除するか、`braze.setLogger()`本番環境では代替ロガーを用意する必要があります。 

詳細ログを有効にするには、`enableLogging`初期化オプションを使用するか、SDK `toggleLogging()` がすでに初期化された後の任意の時点で使用します。

Web サイトに URL `?brazeLogging=true` パラメータとして追加して、詳細なログを有効にすることもできます。

\`\`\`javascript
braze.initialize (「あなたのAPIキーはこちら」,); {
baseUrl: "YOUR-API-ENDPOINT",
enableLogging: true
}

//または、初期化後:

braze.toggleLogging()
\`\`\`

[サーバーサイドのレンダリングフレームワークを使用している場合は、[Viteまたはその他のSSRフレームワークを統合するための追加の統合手順をご覧ください](#vite)。](#ssr)詳細ロギングを行っても、追加のユーザー情報や新しいユーザー情報が Braze に送信されることはありません。


## SDK のアップグレード

{% multi_lang_include archive/web-v4-rename.md %}

たとえば、コンテンツ配信ネットワークからBraze Web SDKを参照すると`https://js.appboycdn.com/web-sdk/a.a/braze.min.js`（デフォルトの統合手順で推奨されているとおり）、ユーザーはサイトを更新したときに自動的にマイナーアップデート（バグ修正と下位互換性のある機能、`a.a.a``a.a.z`上記の例ではバージョンまで）を受け取ります。

ただし、大きな変更がリリースされた場合は、Braze Web SDKを手動でアップグレードして、インテグレーションが重大な変更の影響を受けないようにする必要があります。さらに、SDKをダウンロードして自分でホストした場合、自動的にバージョン更新を受け取ることはないため、最新の機能やバグ修正を受けるには手動でアップグレードする必要があります。

ご希望のRSSリーダーまたはサービスを使用して、[リリースフィードに従って最新リリースを入手することができます](https://github.com/braze-inc/braze-web-sdk/tags.atom)。また、Web [SDKのリリース履歴の詳細については変更履歴を参照してください](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)。Braze Web SDK をアップグレードするには:

- のバージョン番号`https://js.appboycdn.com/web-sdk/[OLD VERSION NUMBER]/braze.min.js`、またはパッケージマネージャーの依存関係を変更して、Braze ライブラリのバージョンを更新してください。
- Web Push を統合している場合は、サイトの Service Worker ファイルを更新します。デフォルトでは、これはサイトのルートディレクトリにありますが、一部の統合では場所をカスタマイズできます。`/service-worker.js`サービスワーカーファイルをホストするには、ルートディレクトリにアクセスする必要があります。

これらの 2 つのファイルは、正しく機能するように相互に調整して更新する必要があります。

## 代替統合方法

### サーバーサイドレンダリングフレームワーク {#ssr}

Next.js などのサーバー側のレンダリングフレームワークを使用する場合、SDK はブラウザー環境で実行されることを想定しているため、エラーが発生する可能性があります。これらの問題は、SDK を動的にインポートすることで解決できます。

その場合でも、SDK の必要な部分を別のファイルにエクスポートし、そのファイルをコンポーネントに動的にインポートすることで、ツリーシェイクの利点を維持できます。

\`\`\`javascript
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
            \`\`\`

また、webpack を使用してアプリをバンドルしている場合は、そのマジックコメントを利用して、SDK の必要な部分だけを動的にインポートすることもできます。

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

### バイトサポート {#vite}

Vite を使用していて、循環依存関係に関する警告が表示される場合や`Uncaught TypeError: Class extends value undefined is not a constructor or null`、Braze SDK [を依存関係の検出から除外する必要がある場合があります](https://vitejs.dev/guide/dep-pre-bundling.html#customizing-the-behavior)。

```
optimizeDeps: {
    exclude: ['@braze/web-sdk']
},
```

### 電子サポート {#electron}

Electronはウェブプッシュ通知を公式にはサポートしていません（[このGitHubの問題を参照](https://github.com/electron/electron/issues/6697)）。Braze [でテストされていないオープンソースの回避策は他にもあります](https://github.com/MatthieuLemoine/electron-push-receiver)。

### AMD モジュールローダー

RequireJSやその他のAMDモジュールローダーを使用する場合は、ライブラリのコピーをセルフホストし、他のリソースと同じように参照することをお勧めします。

```javascript
require(['path/to/braze.min.js'], function(braze) {
  braze.initialize('YOUR-API-KEY-HERE', { baseUrl: 'YOUR-SDK-ENDPOINT' });
  braze.automaticallyShowInAppMessages();
  braze.openSession();
});
```
### 代替案:AMDインストールなし

サイトでRequireJSまたは別のAMDモジュールローダーを使用しているが、上記の他のオプションのいずれかを使用してBraze Web SDKをロードしたい場合は、AMDサポートを含まないバージョンのライブラリをロードできます。このバージョンのライブラリは、次の CDN ロケーションからロードできます。

<script src="https://braze-inc.github.io/embed-like-gist/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Fno-amd-library.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

### ティーリアム iQ
Tealium iQは、基本的なターンキー方式のBrazeインテグレーションを提供しています。統合を設定するには、Tealiumタグ管理インターフェースでBrazeを検索し、ダッシュボードからWeb SDK APIキーを入力します。

Tealiumの設定に関する詳細や詳細なサポートについては、[統合ドキュメントを確認するか]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/#about-tealium)、Tealiumアカウントマネージャーにお問い合わせください。

### その他のタグマネージャー
Brazeは、カスタムHTMLタグ内の統合手順に従うことで、他のタグ管理ソリューションと互換性がある場合もあります。これらのソリューションの評価についてサポートが必要な場合は、Braze の担当者にお問い合わせください。

### Jest フレームワークのトラブルシューティング {#jest}

Jest を使用すると、`SyntaxError: Unexpected token 'export'`と同様のエラーが表示される場合があります。これを修正するには、Braze SDK `package.json` を無視するように設定を調整してください。

```
"jest": {
  "transformIgnorePatterns": [
    "/node_modules/(?!@braze)"
  ]
}
```

[9]: https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html "JSDocs"
[16]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration/
[17]: https://github.com/braze-inc/braze-web-sdk/blob/master/UPGRADE_GUIDE.md
[18]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/google_tag_manager/
[19]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/content_security_policy/
<!-- wesley wanted an empty line at the end -->
