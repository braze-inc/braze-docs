## Web Braze SDKについて

Web Braze SDKを使用すると、分析を収集し、リッチなアプリ内メッセージ、プッシュ、コンテンツカードメッセージをWebユーザーに表示することができます。詳しくは、[Braze JavaScriptリファレンスドキュメントを](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html)参照のこと。

{% multi_lang_include archive/web-v4-rename.md %}

## Web SDKを統合する

以下の方法でWeb Braze SDKを統合することができる。その他のオプションについては、[他の統合方法を](#web_other-integration-methods)参照のこと。

- **コードベースの統合：**お好みのパッケージマネージャーまたはBraze CDNを使用して、Web Braze SDKをコードベースに直接統合する。これにより、SDKの読み込まれ方とコンフィギュレーションを完全にコントロールできるようになる。
- **Google タグマネージャー：**サイトのコードを変更することなく、Web Braze SDKを統合できるコード不要のソリューション。詳しくは、[Google Tag Manager with Braze SDKを]({{site.baseurl}}/developer_guide/sdk_integration/google_tag_manager/)参照。

{% tabs local %}
{% tab code-based integration %}
### ステップ 1: Brazeライブラリをインストールする

Brazeライブラリは、以下のいずれかの方法でインストールできます。しかし、あなたのWebサイトが`Content-Security-Policy` 、続ける前に[コンテンツセキュリティポリシーを]({{site.baseurl}}/developer_guide/platforms/web/content_security_policy/)確認する。

{% alert important %}
ほとんどの広告ブロッカーはBraze Web SDKをブロックしないが、一部の制限の厳しい広告ブロッカーは問題を引き起こすことが知られている。
{% endalert %}

{% subtabs %}
{% subtab package manager %}
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
{% endsubtab %}

{% subtab braze cdn %}
Braze Web SDKをHTMLに直接追加するには、当社のCDNホストスクリプトを参照し、ライブラリを非同期で読み込みます。

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Floading-snippet.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>
{% endsubtab %}
{% endsubtabs %}

### ステップ2:SDK の初期化

Braze Web SDKがWebサイトに追加されたら、Brazeダッシュボード内の**設定**>**アプリ設定に**あるAPIキーと[SDKエンドポイントURLを使って]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints)、ライブラリを初期化する。他のJavaScriptメソッドと共に、`braze.initialize()` のオプションの完全なリストについては、[Braze JavaScriptドキュメントを](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize)参照のこと。

```javascript
// initialize the SDK
braze.initialize('YOUR-API-KEY-HERE', {
    baseUrl: "YOUR-SDK-ENDPOINT-HERE",
    enableLogging: false, // set to `true` for debugging
    allowUserSuppliedJavascript: false, // set to `true` to support custom HTML messages
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
{% endtab %}

{% tab Google Tag Manager %}
{% multi_lang_include developer_guide/web/google_tag_manager/initialization_tag.md %}
{% endtab %}
{% endtabs %}

## オプション構成

### ロギング

ロギングをすばやく有効にするには、`?brazeLogging=true` をパラメーターとして Web サイト URL に追加します。あるいは、[基本](#web_basic-logging)ロギングまたは[カスタム・](#web_custom-logging)ロギングを有効にすることもできます。

#### 基本的なロギング

{% tabs local %}
{% tab before initialization %}
`enableLogging` 、SDKが初期化される前にJavaScriptコンソールに基本的なデバッグメッセージを記録する。

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

{% tab after initialization %}
SDKが初期化された後、JavaScriptコンソールに基本的なデバッグメッセージを記録するには、`braze.toggleLogging()` を使用する。メソッドは次のようになるはずです。

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
基本ログはすべてのユーザーに表示されるため、コードを本番環境にリリースする前に、無効にすることを検討するか、[`setLogger`](#web_custom-logging) に切り替えてください。
{% endalert %}

#### カスタムロギング

`setLogger` を使って、カスタムデバッグメッセージをJavaScriptコンソールに記録する。基本ログとは異なり、これらのログはユーザーには見えません。

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

ただし、弊社が大きな変更をリリースする際には、変更点がお客様の統合に影響しないように、Braze Web SDKを手動でアップグレードしていただく必要があります。さらに、当社のSDKをダウンロードして自分でホスティングする場合、バージョン・アップデートを自動的に受け取ることはできないので、最新の機能やバグ修正を受け取るには手動でアップグレードする必要があります。

RSS Reader または任意のサービスを使用して、[リリースフィードに従って](https://github.com/braze-inc/braze-web-sdk/tags.atom)最新のリリースを取得できます。また、Web SDK のリリース履歴の詳細については、[変更ログ](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)を参照してください。Braze Web SDKをアップグレードします：

- バージョン番号 `https://js.appboycdn.com/web-sdk/[OLD VERSION NUMBER]/braze.min.js` を変更するか、パッケージマネージャーの依存関係で、Braze ライブラリのバージョンを更新します。
- Web プッシュが統合されている場合は、サイトのサービスワーカーファイルを更新します。デフォルトでは、このファイルはサイトのルートディレクトリの`/service-worker.js` にありますが、統合によっては場所がカスタマイズされている場合があります。サービスワーカーファイルをホストするには、ルートディレクトリにアクセスしなければなりません。

適切に機能させるためには、これら2つのファイルを連携させて更新する必要がある。

## その他の統合方法

### アクセラレイテッド・モバイル・ページ（AMP）
{% details See more %}
#### ステップ 1: AMP Web プッシュスクリプトを含める

次の非同期スクリプトタグをヘッドに追加します：

```js
<script async custom-element="amp-web-push" src="https://cdn.ampproject.org/v0/amp-web-push-0.1.js"></script>
```

#### ステップ 2:サブスクリプション・ウィジェットを追加する

HTMLの本文にウィジェットを追加し、ユーザーがプッシュ配信の登録と配信停止を行えるようにする。

```js
<!-- A subscription widget -->
<amp-web-push-widget visibility="unsubscribed" layout="fixed" width="250" height="80">
  <button on="tap:amp-web-push.subscribe">Subscribe to Notifications</button>
</amp-web-push-widget>

<!-- An unsubscription widget -->
<amp-web-push-widget visibility="subscribed" layout="fixed" width="250" height="80">
  <button on="tap:amp-web-push.unsubscribe">Unsubscribe from Notifications</button>
</amp-web-push-widget>
```

#### ステップ 3:`helper-iframe` を追加する。 `permission-dialog`

AMP Web Pushコンポーネントは、サブスクリプションを処理するためのポップアップを作成するので、この機能をイネーブルメントするためには、プロジェクトに以下のヘルパーファイルを追加する必要がある：

- [`helper-iframe.html`](https://cdn.ampproject.org/v0/amp-web-push-helper-frame.html)
- [`permission-dialog.html`](https://cdn.ampproject.org/v0/amp-web-push-permission-dialog.html)

#### ステップ 4: サービスワーカーファイルを作成する

Webサイトのルート・ディレクトリに`service-worker.js` ファイルを作成し、以下のスニペットを追加する：

<script src="{{site.baseurl}}/assets/js/embed.js?target=https://github.com/braze-inc/braze-web-sdk/blob/master/sample-builds/cdn/service-worker.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

#### ステップ 5: AMP Web プッシュ HTML 要素を構成する

以下の`amp-web-push` HTML要素をHTML本文に追加する。`service-worker-URL` にクエリーパラメーターとして[`apiKey` と`baseUrl`](https://documenter.getpostman.com/view/4689407/SVYrsdsG)を追加する必要があることに留意してほしい。

```js
<amp-web-push
layout="nodisplay"
id="amp-web-push"
helper-iframe-url="FILE_PATH_TO_YOUR_HELPER_IFRAME"
permission-dialog-url="FILE_PATH_TO_YOUR_PERMISSION_DIALOG"
service-worker-url="FILE_PATH_TO_YOUR_SERVICE_WORKER?apiKey={YOUR_API_KEY}&baseUrl={YOUR_BASE_URL}"
>
```
{% enddetails %}

### 非同期モジュール定義（AMD）

#### サポートを無効にする

あなたのサイトがRequireJSまたは他のAMDモジュールローダーを使用しているが、このリストの他のオプションのいずれかを使用してBraze Web SDKを読み込むことを好む場合、AMDサポートを含まないバージョンのライブラリを読み込むことができる。このバージョンのライブラリーは、以下のCDNの場所からロードできます：

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Fno-amd-library.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

#### モジュールローダー

RequireJS または他の AMD モジュールローダーを使用する場合は、ライブラリのコピーをセルフホスティングし、他のリソースと同様に参照することをお勧めします。

```javascript
require(['path/to/braze.min.js'], function(braze) {
  braze.initialize('YOUR-API-KEY-HERE', { baseUrl: 'YOUR-SDK-ENDPOINT' });
  braze.automaticallyShowInAppMessages();
  braze.openSession();
});
```

### エレクトロン {#electron}

Electron は公式には Web プッシュ通知をサポートしていません (参照： この [GitHub issue](https://github.com/electron/electron/issues/6697))。Brazeがテストしていない[オープンソースの回避策を](https://github.com/MatthieuLemoine/electron-push-receiver)試すこともできます。

### Jestフレームワーク {#jest}

Jestを使用している場合、`SyntaxError: Unexpected token 'export'` のようなエラーが表示されることがあります。これを修正するには、Braze SDK を無視するように `package.json` の設定を調整します。

```
"jest": {
  "transformIgnorePatterns": [
    "/node_modules/(?!@braze)"
  ]
}
```

### SSRフレームワーク {#ssr}

Next.js のようなサーバーサイド・レンダリング（SSR）フレームワークを使用している場合、SDKがブラウザ環境で実行されることを意図しているため、エラーが発生する可能性がある。これらの問題は、SDKを動的にインポートすることで解決できます。

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

### Tealium iQ

Tealium iQは、基本的なターンキー Braze 統合を提供します。統合を構成するには、Tealium Tag Management インターフェイスで Braze を検索し、ダッシュボードから Web SDK API キーを指定します。

詳細や詳細なTealium設定サポートについては、[統合ドキュメントを]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/#about-tealium)ご覧になるか、Tealiumアカウントマネージャーにお問い合わせください。

### ヴァイト {#vite}

Viteを使用していて、循環依存関係や`Uncaught TypeError: Class extends value undefined is not a constructor or null` に関する警告が表示される場合は、Braze SDKを[依存関係の発見から](https://vitejs.dev/guide/dep-pre-bundling.html#customizing-the-behavior)除外する必要があるかもしれません：

```
optimizeDeps: {
    exclude: ['@braze/web-sdk']
},
```

### その他のタグ・マネージャー

Brazeは、カスタムHTMLタグの中で当社の統合指示に従うことにより、他のタグ管理ソリューションと互換性を持つこともできます。これらのソリューションの評価についてサポートが必要な場合は、Brazeの担当者に連絡すること。
