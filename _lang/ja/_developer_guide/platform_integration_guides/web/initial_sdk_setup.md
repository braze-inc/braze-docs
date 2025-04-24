---
nav_title: SDK の初期セットアップ
article_title: Braze Web SDKの初期設定
platform: Web
page_order: 0
page_type: reference
---

# ウェブ用SDKの初期セットアップ

> このリファレンス記事では、Braze Web SDK のインストール方法について説明します。Braze Web SDK を使えば、分析を収集し、豊富なアプリ内メッセージ、プッシュ、コンテンツカードメッセージを Web ユーザーに表示することができます。完全なテクニカルリファレンスについては、[JavaScript Documentation](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html "JSDocs")を参照してください。

{% multi_lang_include archive/web-v4-rename.md %}

## ステップ 1:Brazeライブラリをインストールする

Brazeライブラリは、以下のいずれかの方法でインストールできます。ウェブサイトが`Content-Security-Policy` を使用している場合、ライブラリをインストールする前に、[コンテンツ・セキュリティ・ポリシー・ヘッダ・ガイドを]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_security_policy/)参照してください。

{% alert important %}
ほとんどの広告ブロッカーはBraze Web SDKをブロックしないが、一部の制限の厳しい広告ブロッカーは問題を引き起こすことが知られています。
{% endalert %}

{% tabs local %}
{% tab package manager %}
あなたのサイトがNPMまたはYarnパッケージマネージャを使用している場合、依存関係として[Braze NPMパッケージを](https://www.npmjs.com/package/@braze/web-sdk)追加することができます。

v3.0.0 からタイプスクリプトの定義が含まれるようになりました。2.x から 3.x へのアップグレードに関する注意事項については、[changelog](https://github.com/braze-inc/braze-web-sdk/blob/master/UPGRADE_GUIDE.md) を参照してください。

```bash
npm install --save @braze/web-sdk
# or, using yarn:
# yarn add @braze/web-sdk
```

インストール後は、通常の方法でライブラリを `import` または `require` できます。

```typescript
import * as braze from "@braze/web-sdk";
// or, using `require`
const braze = require("@braze/web-sdk");
```
{% endtab %}

{% tab Google Tag Manager %}
Braze Web SDK は、Google Tag Manager テンプレートライブラリからインストールできます。２つのタグがサポートされています：

1. 初期化タグ：Web SDKをウェブサイトにロードし、オプションで外部ユーザーIDを設定します。
2. アクションタグ： カスタムイベント、購入、ユーザー ID の変更、または SDK トラッキングの切り替えをトリガーするために使用されます。

詳しくは [Google Tag Manager 統合ガイドを]({{site.baseurl}}/developer_guide/platform_integration_guides/web/google_tag_manager/)参照してください。
{% endtab %}

{% tab Braze cdn %}
Braze Web SDKをHTMLに直接追加するには、当社のCDNホストスクリプトを参照し、ライブラリを非同期で読み込みます。

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Floading-snippet.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>
{% endtab %}
{% endtabs %}

## ステップ2:SDK の初期化

Braze Web SDK を Web サイトに追加したら、Braze ダッシュボードの [**設定**] > [**アプリ設定**] にある API キーと [SDK エンドポイント URL]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints) を使用してライブラリを初期化します。

{% alert note %}
タグマネージャーでBrazeの初期化オプションを設定している場合は、このステップを省略できます。
{% endalert %}

`braze.initialize()` およびその他の JavaScript メソッドのオプションの完全なリストについては、[JavaScript のドキュメント](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize)を参照してください。

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
モバイルデバイスまたは Web デバイスの匿名ユーザーは、[MAU]({{site.baseurl}}/user_guide/data_and_analytics/reporting/understanding_your_app_usage_data/#monthly-active-users) にカウントされる場合があります。その結果、これらのユーザーをMAUカウントから除外するために、条件付きでSDKをロードするか、初期化したい場合があります。
{% endalert %}

## ステップ 3:プッシュ通知を設定する（オプション）

Braze Web SDK のプッシュ通知を設定するには、追加の設定が必要です。詳しい説明は、[プッシュ通知（ウェブ版]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration/)）を参照してください。

## ロギング

ロギングをすばやく有効にするには、`?brazeLogging=true` をパラメーターとして Web サイト URL に追加します。あるいは、[基本](#basic-logging)ロギングまたは[カスタム・](#custom-logging)ロギングを有効にすることもできます。

### 基本的なロギング

{% tabs local %}
{% tab 初期化前 %}
`enableLogging` を使用して、SDK が初期化される前に基本的なデバッグメッセージを javascript コンソールに記録します。

```javascript
enableLogging: true
```

メソッドは次のようになるはずです。

```javascript
braze.initialize('API-KEY', {
    baseUrl: 'API-ENDPOINT',
    enableLogging: true
});
braze.openSession();
```
{% endtab %}

{% tab 初期化後 %}
SDK の初期化後に基本的なデバッグメッセージを javascript コンソールに記録するには、`braze.toggleLogging()` を使用します。メソッドは次のようになるはずです。

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
基本ログはすべてのユーザーに表示されるため、コードを本番環境にリリースする前に、無効にすることを検討するか、[`setLogger`](#custom-logging) に切り替えてください。
{% endalert %}

### カスタムロギング

`setLogger` を使用して、カスタムデバッグメッセージを javascript コンソールに記録します。基本ログとは異なり、これらのログはユーザーには見えません。

```javascript
setLogger(loggerFunction: (message: STRING) => void): void
```

`STRING` を1つの文字列パラメーターとしてメッセージに置き換えます。メソッドは次のようになるはずです。

```javascript
braze.initialize('API-KEY');
braze.setLogger(function(message) {
    console.log("Braze Custom Logger: " + message);
});
braze.openSession();
```

## SDKをアップグレードする

{% multi_lang_include archive/web-v4-rename.md %}

Braze Web SDKを当社のコンテンツデリバリーネットワーク、例えば`https://js.appboycdn.com/web-sdk/a.a/braze.min.js` （当社のデフォルトの統合手順で推奨されている）から参照すると、ユーザーがサイトを更新したときに、マイナーアップデート（バグフィックスと下位互換機能、上記の例ではバージョン`a.a.a` ～`a.a.z` ）を自動的に受け取ることができます。

ただし、当社が大きな変更をリリースする場合は、Braze Web SDK を手動でアップグレードして、統合に重大な変更の影響がないようにする必要があります。さらに、当社のSDKをダウンロードして自分でホスティングする場合、バージョン・アップデートを自動的に受け取ることはできないので、最新の機能やバグ修正を受け取るには手動でアップグレードする必要があります。

RSS Reader または任意のサービスを使用して、[リリースフィードに従って](https://github.com/braze-inc/braze-web-sdk/tags.atom)最新のリリースを取得できます。また、Web SDK のリリース履歴の詳細については、[変更ログ](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)を参照してください。Braze Web SDKをアップグレードします：

- バージョン番号 `https://js.appboycdn.com/web-sdk/[OLD VERSION NUMBER]/braze.min.js` を変更するか、パッケージマネージャーの依存関係で、Braze ライブラリのバージョンを更新します。
- Web プッシュが統合されている場合は、サイトのサービスワーカーファイルを更新します。デフォルトでは、このファイルはサイトのルートディレクトリの`/service-worker.js` にありますが、統合によっては場所がカスタマイズされている場合があります。サービスワーカーファイルをホストするには、ルートディレクトリにアクセスしなければなりません。

これら2つのファイルを適切に機能させるには、相互に連携して更新する必要があります。

## 別の統合方法

### サーバーサイド・レンダリング・フレームワーク {#ssr}

Next.js のようなサーバーサイド・レンダリング・フレームワークを使用している場合、SDKはブラウザ環境で実行されることを想定しているため、エラーが発生する可能性があります。これらの問題は、SDKを動的にインポートすることで解決できます。

必要な SDK の部分を別のファイルにエクスポートし、そのファイルをコンポーネントに動的にインポートすることで、ツリーシェイクの利点を維持できます。

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

あるいは、アプリのバンドルにwebpackを使用している場合、そのマジックコメントを利用して、必要なSDKの部分だけを動的にインポートすることもできます。

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

### Vite でのサポート {#vite}

Viteを使用していて、循環依存関係や`Uncaught TypeError: Class extends value undefined is not a constructor or null` に関する警告が表示される場合は、Braze SDKを[依存関係の発見から](https://vitejs.dev/guide/dep-pre-bundling.html#customizing-the-behavior)除外する必要があるかもしれません：

```
optimizeDeps: {
    exclude: ['@braze/web-sdk']
},
```

### Electron でのサポート {#electron}

Electron は公式には Web プッシュ通知をサポートしていません (参照： この [GitHub issue](https://github.com/electron/electron/issues/6697))。Brazeがテストしていない[オープンソースの回避策を](https://github.com/MatthieuLemoine/electron-push-receiver)試すこともできます。

### AMDモジュール・ローダー

RequireJS または他の AMD モジュールローダーを使用する場合は、ライブラリのコピーをセルフホスティングし、他のリソースと同様に参照することをお勧めします。

```javascript
require(['path/to/braze.min.js'], function(braze) {
  braze.initialize('YOUR-API-KEY-HERE', { baseUrl: 'YOUR-SDK-ENDPOINT' });
  braze.automaticallyShowInAppMessages();
  braze.openSession();
});
```
### 代替案 AMDを設置しない

サイトで RequireJS または別の AMD モジュールローダーを使用しているが、上記の他のオプションのいずれかを使用して Braze Web SDK をロードしたい場合は、AMD サポートを含まないバージョンのライブラリをロードできます。このバージョンのライブラリーは、以下のCDNの場所からロードできます：

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Fno-amd-library.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

### Tealium iQ
Tealium iQは、基本的なターンキー Braze 統合を提供します。統合を構成するには、Tealium Tag Management インターフェイスで Braze を検索し、ダッシュボードから Web SDK API キーを指定します。

詳細または Tealium 構成サポートに関する詳細については、[統合ドキュメント]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/#about-tealium)を確認するか、Tealium アカウントマネージャーにお問い合わせください。

### その他のタグ・マネージャー
Brazeは、カスタムHTMLタグの中で当社の統合指示に従うことにより、他のタグ管理ソリューションと互換性を持つこともできます。これらのソリューションの評価についてサポートが必要な場合は、Brazeの担当者にご連絡ください。

### Jestフレームワークのトラブルシューティング {#jest}

Jestを使用している場合、`SyntaxError: Unexpected token 'export'` のようなエラーが表示されることがあります。これを修正するには、Braze SDK を無視するように `package.json` の設定を調整します。

```
"jest": {
  "transformIgnorePatterns": [
    "/node_modules/(?!@braze)"
  ]
}
```
