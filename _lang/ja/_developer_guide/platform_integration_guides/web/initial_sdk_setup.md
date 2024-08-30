---
nav_title: SDK の初期セットアップ
article_title: Braze Web SDKの初期設定
platform: Web
page_order: 0
page_type: reference
---

# ウェブ用SDKの初期セットアップ

> この参考記事では、Braze Web SDKのインストール方法について説明する。Braze Web SDKを使えば、アナリティクスを収集し、リッチなアプリ内メッセージ、プッシュ、コンテンツカードメッセージをウェブユーザーに表示することができる。完全な技術リファレンスは[JavaScriptドキュメントを][9]参照のこと。

{% multi_lang_include archive/web-v4-rename.md %}

## ステップ 1:Brazeライブラリをインストールする

Brazeライブラリは、以下のいずれかの方法でインストールできる。ウェブサイトが`Content-Security-Policy` を使用している場合、ライブラリをインストールする前に、[コンテンツ・セキュリティ・ポリシー・ヘッダ・ガイドを]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_security_policy/)参照のこと。

{% alert important %}
ほとんどの広告ブロッカーはBraze Web SDKをブロックしないが、一部の制限の厳しい広告ブロッカーは問題を引き起こすことが知られている。
{% endalert %}

{% tabs local %}
{% tab パッケージマネージャ %}
あなたのサイトがNPMまたはYarnパッケージマネージャを使用している場合、依存関係として[Braze NPMパッケージを](https://www.npmjs.com/package/@braze/web-sdk)追加することができる。

v3.0.0からタイプスクリプトの定義が含まれるようになった。2.xから3.xへのアップグレードに関する注意事項は、[変更履歴を](https://github.com/braze-inc/braze-web-sdk/blob/master/UPGRADE_GUIDE.md)参照のこと。

```bash
npm install --save @braze/web-sdk
# or, using yarn:
# yarn add @braze/web-sdk
```

インストールが完了したら、`import` または`require` ライブラリを通常の方法でインストールすることができる：

```typescript
import * as braze from "@braze/web-sdk";
// or, using `require`
const braze = require("@braze/web-sdk");
```
{% endtab %}

{% tab グーグルタグマネージャー %}
Braze Web SDKは、Google Tag Manager Template Libraryからインストールできる。つのタグがサポートされている：

1. 初期化タグ：Web SDKをウェブサイトにロードし、オプションで外部ユーザーIDを設定する。
2. Actionsタグ：カスタムイベントのトリガー、購入、ユーザーIDの変更、SDKトラッキングの切り替えに使用する。

詳しくは[Google Tag Manager統合ガイドを]({{site.baseurl}}/developer_guide/platform_integration_guides/web/google_tag_manager/)参照。
{% endtab %}

{% tab ブレイズCDN %}
Braze Web SDKをHTMLに直接追加するには、当社のCDNホストスクリプトを参照し、ライブラリを非同期で読み込む。

<script src="https://braze-inc.github.io/embed-like-gist/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Floading-snippet.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>
{% endtab %}
{% endtabs %}

## ステップ2:SDK の初期化

WebサイトにBraze Web SDKを追加したら、Brazeダッシュボード内の**Settings**>**App Settingsに**あるAPIキーと[SDKエンドポイントURLで]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints)ライブラリを初期化する。

{% alert note %}
タグマネージャーでBrazeの初期化オプションを設定している場合は、このステップを省略できる。
{% endalert %}

他のJavaScriptメソッドとともに、`braze.initialize()` のオプションの完全なリストについては、[JavaScriptのドキュメントを](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize)参照のこと。

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
モバイルやウェブデバイスの匿名ユーザーは、[MAUに]({{site.baseurl}}/user_guide/data_and_analytics/reporting/understanding_your_app_usage_data/#monthly-active-users)カウントされる可能性がある。その結果、これらのユーザーをMAUカウントから除外するために、条件付きでSDKをロードするか、初期化したい場合がある。
{% endalert %}

## ステップ 3:プッシュ通知を設定する（オプション）

Braze Web SDKのプッシュ通知を設定するには、追加の設定が必要である。詳しい説明は、[プッシュ通知（ウェブ版]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration/)）を参照のこと。

## ロギング

素早くロギングを有効にするには、ウェブサイトのURLにパラメータとして`?brazeLogging=true` 。あるいは、[基本](#basic-logging)ロギングまたは[カスタム・](#custom-logging)ロギングを有効にすることもできる。

### 基本的なロギング

{% tabs local %}
{% tab 初期化前 %}
`enableLogging` 、SDKが初期化される前に、基本的なデバッグメッセージをjavascriptコンソールに記録する。

```javascript
enableLogging: true
```

あなたのやり方は次のようなものであるべきだ：

```javascript
braze.initialize('API-KEY', {
    baseUrl: 'API-ENDPOINT',
    enableLogging: true
});
braze.openSession();
```
{% endtab %}

{% tab 初期化後 %}
`braze.toggleLogging()` 、SDKが初期化された後、基本的なデバッグメッセージをjavascriptコンソールに記録する。あなたのやり方は次のようなものであるべきだ：

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
基本ログはすべてのユーザーが見ることができる。 [`setLogger`](#custom-logging)に切り替えることを検討すること。
{% endalert %}

### カスタム・ロギング

`setLogger` 、カスタム・デバッグ・メッセージをJavaScriptコンソールに記録する。基本ログとは異なり、これらのログはユーザーには見えない。

```javascript
setLogger(loggerFunction: (message: STRING) => void): void
```

`STRING` 、1つの文字列パラメータとしてあなたのメッセージに置き換える。あなたのやり方は次のようなものであるべきだ：

```javascript
braze.initialize('API-KEY');
braze.setLogger(function(message) {
    console.log("Braze Custom Logger: " + message);
});
braze.openSession();
```

## SDKをアップグレードする

{% multi_lang_include archive/web-v4-rename.md %}

Braze Web SDKを当社のコンテンツデリバリーネットワーク、例えば`https://js.appboycdn.com/web-sdk/a.a/braze.min.js` （当社のデフォルトの統合手順で推奨されている）から参照すると、ユーザーがサイトを更新したときに、マイナーアップデート（バグフィックスと下位互換機能、上記の例ではバージョン`a.a.a` ～`a.a.z` ）を自動的に受け取ることができる。

ただし、弊社が大きな変更をリリースする際には、Braze Web SDKを手動でアップグレードしていただき、お客様のインテグレーションが変更によって影響を受けることがないようにしています。さらに、当社のSDKをダウンロードして自分でホスティングする場合、バージョン・アップデートを自動的に受け取ることはできないので、最新の機能やバグ修正を受け取るには手動でアップグレードする必要がある。

RSSリーダーやお好みのサービスを使って[、リリース・フィードをフォローすることで](https://github.com/braze-inc/braze-web-sdk/tags.atom)、最新のリリース情報を入手することができる。また、Web SDKのリリース履歴については、[変更履歴を](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)参照されたい。Braze Web SDKをアップグレードする：

- `https://js.appboycdn.com/web-sdk/[OLD VERSION NUMBER]/braze.min.js` 、またはパッケージマネージャの依存関係のバージョン番号を変更して、Brazeライブラリのバージョンを更新する。
- ウェブプッシュを統合している場合、サイトのサービスワーカーファイルを更新する。デフォルトでは、このファイルはサイトのルートディレクトリの`/service-worker.js` にあるが、統合によっては場所がカスタマイズされることもある。サービスワーカーファイルをホストするには、ルートディレクトリにアクセスしなければならない。

これら2つのファイルは、適切な機能を発揮するために、互いに連携して更新されなければならない。

## 別の統合方法

### サーバーサイド・レンダリング・フレームワーク {#ssr}

Next.js のようなサーバーサイド・レンダリング・フレームワークを使用している場合、SDKはブラウザ環境で実行されることを想定しているため、エラーが発生する可能性がある。これらの問題は、SDKを動的にインポートすることで解決できる。

その際、SDKの必要な部分を別のファイルにエクスポートし、そのファイルをコンポーネントに動的にインポートすることで、ツリーシェイキングの利点を維持することができる。

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

あるいは、アプリのバンドルにwebpackを使用している場合、そのマジックコメントを利用して、必要なSDKの部分だけを動的にインポートすることもできる。

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

Viteを使用していて、循環依存関係や`Uncaught TypeError: Class extends value undefined is not a constructor or null` に関する警告が表示される場合は、Braze SDKを[依存関係の発見から](https://vitejs.dev/guide/dep-pre-bundling.html#customizing-the-behavior)除外する必要があるかもしれない：

```
optimizeDeps: {
    exclude: ['@braze/web-sdk']
},
```

### 電子サポート {#electron}

Electronは公式にはウェブプッシュ通知をサポートしていない（参照：[GitHub issue](https://github.com/electron/electron/issues/6697)）。Brazeがテストしていない[オープンソースの回避策を](https://github.com/MatthieuLemoine/electron-push-receiver)試すこともできる。

### AMDモジュール・ローダー

RequireJSや他のAMDモジュールローダーを使用する場合は、我々のライブラリのコピーをセルフホストし、他のリソースと同じように参照することを推奨する：

```javascript
require(['path/to/braze.min.js'], function(braze) {
  braze.initialize('YOUR-API-KEY-HERE', { baseUrl: 'YOUR-SDK-ENDPOINT' });
  braze.automaticallyShowInAppMessages();
  braze.openSession();
});
```
### 代替案 AMDを設置しない

あなたのサイトがRequireJSまたは他のAMDモジュールローダーを使用しているが、上記の他のオプションのいずれかを使用してBraze Web SDKをロードすることを好む場合、AMDサポートを含まないバージョンのライブラリをロードすることができる。このバージョンのライブラリーは、以下のCDNの場所からロードできる：

<script src="https://braze-inc.github.io/embed-like-gist/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Fno-amd-library.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

### ティーリウムiQ
Tealium iQは、基本的なターンキーBrazeインテグレーションを提供する。統合を設定するには、Tealium Tag ManagementインターフェイスでBrazeを検索し、ダッシュボードからWeb SDK APIキーを提供する。

詳細や詳細なTealium設定サポートについては、[統合ドキュメントを]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/#about-tealium)ご覧になるか、Tealiumアカウントマネージャーにお問い合わせいただきたい。

### その他のタグ・マネージャー
Brazeは、カスタムHTMLタグの中で当社の統合指示に従うことにより、他のタグ管理ソリューションと互換性を持つこともできる。これらのソリューションの評価についてサポートが必要な場合は、Brazeの担当者に連絡すること。

### Jestフレームワークのトラブルシューティング {#jest}

Jestを使用している場合、`SyntaxError: Unexpected token 'export'` のようなエラーが表示されることがある。これを修正するには、`package.json` の設定を調整して、Braze SDKを無視するようにする：

```
"jest": {
  "transformIgnorePatterns": [
    "/node_modules/(?!@braze)"
  ]
}
```

[9]: https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html "JSDocs"