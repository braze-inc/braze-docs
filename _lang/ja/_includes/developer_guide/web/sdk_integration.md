## Web Braze SDKについて

Web Braze SDKを使えば、分析データを収集し、ウェブユーザー向けにリッチなアプリ内メッセージ、プッシュ通知、コンテンツカードメッセージを表示できる。詳細については、[Braze JavaScriptリファレンスドキュメントを](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html)参照せよ。

{% multi_lang_include archive/web-v4-rename.md %}

## Web SDK を連携

Web Braze SDKは次の方法で統合できる。追加のオプションについては、[他の統合方法を](#web_other-integration-methods)参照せよ。

- **コードベースの統合：**お好みのパッケージマネージャーかBraze CDNを使って、Web Braze SDKをコードベースに直接組み込む。これにより、SDKを読み込む方法と設定方法を完全にコントロールできる。
- **Google Tag Manager：**サイトのコードを変更せずにWeb Braze SDKを統合できるノーコードソリューションだ。詳細については、[Braze SDK を使用した Google Tag Manager]({{site.baseurl}}/developer_guide/sdk_integration/google_tag_manager/) を参照のこと。

{% alert important %}
[NPM統合方式]({{site.baseurl}}/developer_guide/sdk_integration/?subtab=package%20manager&sdktab=web)の使用を推奨する。メリットには、SDKライブラリーをWeb サイトにローカル保存できること、広告ブロック拡張機能の影響を受けないこと、バンドラーサポートの一環として読み込み速度の向上に寄与することが含まれる。
{% endalert %}

{% tabs local %}
{% tab code-based integration %}
### ステップ 1: Brazeライブラリをインストールする

Brazeライブラリは、以下のいずれかの方法でインストールできます。ただし、Web サイトがコンテンツセキュリティポリシーを使用している`Content-Security-Policy`場合は、続行する前にその[ポリシー]({{site.baseurl}}/developer_guide/platforms/web/content_security_policy/)を確認すること。

{% alert important %}
ほとんどの広告ブロッカーはBraze Web SDKをブロックしないが、より制限の厳しい広告ブロッカーでは問題が発生することが知られている。
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

{% alert important %}
Safariのデフォルト設定である**「クロスサイトトラッキングの防止」**は、CDN統合方式を使用する場合、バナーやコンテンツカードなどのアプリ内メッセージタイプの表示を妨げる可能性がある。この問題を回避するには、NPM統合方式を使用する。そうすればSafariがこれらのメッセージをクロスサイト通信として分類せず、ウェブユーザーは全ての対応ブラウザでそれらを確認できる。
{% endalert %}

{% endsubtab %}
{% endsubtabs %}

### ステップ2:SDK の初期化

Braze Web SDKをWeb サイトに追加した後、Brazeダッシュボードの「**設定**」＞「**アプリ設定**」にあるAPI キーと[SDKエンドポイントURL]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints)でライブラリーを初期化する。のオプションの完全な一覧と`braze.initialize()`、その他のJavaScriptメソッドについては、[Braze JavaScriptドキュメントを](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize)参照せよ。

{% alert note %}
**Web SDKリクエストにおけるカスタムドメインはサポートされていない**。Web SDKはBraze `baseUrl`SDKのエンドポイントでなければならない（例：`sdk.iad-05.braze.com`）。Brazeは、CNAMEレコードを介して顧客所有のドメインを経由するWeb SDKトラフィックのルーティングをサポートしない。Web SDKのリクエストを自身のドメインから発信する必要がある場合は、Brazeサポートに連絡すること。
{% endalert %}

```javascript
// initialize the SDK
braze.initialize('YOUR-API-KEY-HERE', {
    baseUrl: "YOUR-SDK-ENDPOINT-HERE",
    enableLogging: false, // set to `true` for debugging
    allowUserSuppliedJavascript: false, // set to `true` to support custom HTML messages
});

// Enable automatic display of in-app messages
// Required if you want in-app messages to display automatically when triggered
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
**アプリ内メッセージ表示**：アプリ内メッセージがトリガーされた際に自動的に表示するには、を呼び出す必要がある`braze.automaticallyShowInAppMessages()`。この呼び出しがないと、アプリ内メッセージは自動的には表示されない。メッセージ表示を手動で管理したい場合は、この呼び出しを削除し、代わりに`braze.subscribeToInAppMessage()`を使用せよ。詳細については、[アプリ内メッセージ配信を]({{site.baseurl}}/developer_guide/in_app_messages/delivery/)参照せよ。
{% endalert %}

#### 匿名ユーザーにおけるセッション消失のトラブルシューティング

「セッションが欠落している」という現象が発生している場合、またはWeb上で匿名のままのユーザーのセッションをトラッキングできない場合は、初期化中に統合`braze.openSession()`が呼び出されていることを確認せよ。

- **シナリオ:**匿名ユーザーはBraze IDを返すが、セッションデータは空白か欠落している。
- **原因：**実装は呼び出さない`braze.openSession()`。
- **決議：**初期化後は必ず`braze.openSession()`呼び出すこと（external IDを設定した場合は`braze.changeUser()`その後も）。

詳細については、ステップ2[を参照せよ。SDKを初期化する]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web&tab=code-based%20integration#step-2-initialize-the-sdk)。

{% alert important %}
モバイルデバイスまたは Web デバイスの匿名ユーザーは、[MAU]({{site.baseurl}}/user_guide/data_and_analytics/reporting/understanding_your_app_usage_data/#monthly-active-users) にカウントされる場合があります。その結果、これらのユーザーをMAUカウントから除外するために、条件付きでSDKをロードするか、初期化したい場合があります。
{% endalert %}
{% endtab %}

{% tab Google Tag Manager %}
{% multi_lang_include developer_guide/web/google_tag_manager/initialization_tag.md %}
{% endtab %}
{% endtabs %}

## ボットトラフィックのフィルター {#bot-filtering}

MAUにはボットユーザーの割合が含まれる場合があり、それによって月間アクティブユーザー数が水増しされる。Braze Web SDKには、検索エンジンのボットやソーシャルメディアのプレビューボットなど、一般的なウェブクローラーの検出機能が組み込まれている。しかし、SDKの更新だけでは常に新しいボットをすべて検出できるわけではないため、ボットを検出するための堅牢なソリューションを積極的に導入することが特に重要だ。

### SDK側のボット検出の限界

Web SDKには、既知のクローラーを除外する基本的なユーザーエージェントベースのボット検出機能が組み込まれている。しかし、この方法には限界がある：

- **新しいボットが次々と現れる**：AI企業やその他の関係者は、検出を避けるために偽装する可能性のある新しいボットを定期的に作成している。
- **ユーザーエージェント偽装**：高度なボットは、正当なブラウザのユーザーエージェントを模倣できる。
- **カスタムボット**：技術的知識のないユーザーでも、大規模言語モデル（LLM）を使って簡単にボットを作成できるようになった。これによりボットの挙動は予測不能になる。

### ボットフィルターの実装

{% alert important %}
以下に述べるソリューションは一般的な提案である。ボットフィルターのロジックを、独自の環境とトラフィックパターンに合わせて調整せよ。
{% endalert %}

最も堅牢なソリューションは、Braze SDKを初期化する前に独自のボットフィルターロジックを実装することだ。一般的な手法には以下が含まれる：

#### ユーザーの操作が必要だ

ユーザーがCookie同意バナーの承諾、スクロール、クリックなどの意味のある操作を行うまで、SDKの初期化を遅らせることを検討せよ。この手法は実装が容易な場合が多く、ボットトラフィックのフィルターに非常に効果的である。

{% alert important %}
SDKの初期化をユーザー操作まで遅らせると、バナーやコンテンツカードもその操作が行われるまで表示されない可能性がある。
{% endalert %}

#### カスタムボット検出

特定のボットトラフィックパターンに基づいてカスタム検出を実装する。例えば：

- トラフィックで識別したパターンについて、ユーザーエージェント文字列を分析する
- ヘッドレスブラウザの指標を確認する
- サードパーティのボット検出サービスを利用する
- サイト固有の行動シグナルを監視する

**条件付き初期化の例：**

```javascript
// Only initialize Braze if your custom bot detection determines this is not a bot
if (!isLikelyBot()) {
  braze.initialize('YOUR-API-KEY-HERE', {
    baseUrl: "YOUR-SDK-ENDPOINT-HERE"
  });
  braze.automaticallyShowInAppMessages();
  braze.openSession();
}
```

### ベストプラクティス

- MAUデータとWebトラフィックのパターンを定期的に分析し、新たなボットの行動を識別する。
- ボットフィルターが正当なユーザーのトラッキングを妨げないよう、徹底的にテストせよ。
- 環境内で観察されるボットのトラフィックパターンに基づいて、フィルターロジックを更新せよ。

## オプション設定

### ロギング

ロギングをすばやく有効にするには、`?brazeLogging=true` をパラメーターとして Web サイト URL に追加します。あるいは、[基本](#web_basic-logging)ロギングまたは[カスタム・](#web_custom-logging)ロギングを有効にすることもできます。すべてのプラットフォームにわたる一元的な概要については、[詳細ログを]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging)参照せよ。

#### 基本的なロギング

{% tabs local %}
{% tab before initialization %}
SDKが初期化される前に、基本的なデバッグメッセージをJavaScriptコンソールに記録するには`enableLogging``use`を使用する。

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
SDKが初期化された後、基本的なデバッグメッセージをJavaScriptコンソールに記録するには`braze.toggleLogging()``use`を使用する。メソッドは次のようになるはずです。

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

カスタムデバッグメッセージをJavaScriptコンソールに記録するには、\``setLogger`log`を使用する。基本ログとは異なり、これらのログはユーザーには見えません。

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

例えば、当社のコンテンツ配信ネットワークからBraze Web SDKを参照する場合（デフォルトの統合手順で推奨されている通り）`https://js.appboycdn.com/web-sdk/a.a/braze.min.js`、ユーザーはサイトを更新する際にマイナー更新（バグ修正や下位互換性のある機能、上記の例で`a.a.z`バージョン`a.a.a`からまでの更新）を自動的に受け取る。

ただし、主要な変更をリリースする際には、互換性を損なう変更が統合に影響しないよう、Braze Web SDKを手動でアップグレードする必要がある。さらに、当社のSDKをダウンロードして自身でホストする場合、バージョン更新は自動的には行われない。最新の機能やバグ修正を受けるには、手動でアップグレードする必要がある。

RSS Reader または任意のサービスを使用して、[リリースフィードに従って](https://github.com/braze-inc/braze-web-sdk/tags.atom)最新のリリースを取得できます。また、Web SDK のリリース履歴の詳細については、[変更ログ](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)を参照してください。Braze Web SDKをアップグレードします：

- バージョン番号 `https://js.appboycdn.com/web-sdk/[OLD VERSION NUMBER]/braze.min.js` を変更するか、パッケージマネージャーの依存関係で、Braze ライブラリのバージョンを更新します。
- Web プッシュが統合されている場合は、サイトのサービスワーカーファイルを更新します。デフォルトでは、このファイルはサイトのルートディレクトリの`/service-worker.js` にありますが、統合によっては場所がカスタマイズされている場合があります。サービスワーカーファイルをホストするには、ルートディレクトリにアクセスしなければなりません。

これらの2つのファイルは、正常に機能させるために互いに連携して更新しなければならない。

## その他の統合方法

### アクセラレイテッド・モバイル・ページズ（AMP）
{% details See more %}
#### ステップ 1: AMP Web プッシュスクリプトを含める

次の非同期スクリプトタグをヘッドに追加します：

```js
<script async custom-element="amp-web-push" src="https://cdn.ampproject.org/v0/amp-web-push-0.1.js"></script>
```

#### ステップ 2:サブスクリプションウィジェットを追加する

HTMLの本文にウィジェットを追加し、ユーザーがプッシュ通知の登録と配信停止を行えるようにする。

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

#### ステップ 3:追加`helper-iframe`する `permission-dialog`

AMP Web プッシュコンポーネントは、プッシュサブスクリプションを処理するためのポップアップを作成する。このイネーブルメントを行うには、プロジェクトに以下のヘルパーファイルを追加する必要がある：

- [`helper-iframe.html`](https://cdn.ampproject.org/v0/amp-web-push-helper-frame.html)
- [`permission-dialog.html`](https://cdn.ampproject.org/v0/amp-web-push-permission-dialog.html)

#### ステップ 4: サービスワーカーファイルを作成する

Web サイトのルートディレクトリにファイル`service-worker.js`を作成し、以下のスニペットを追加する：

<script src="{{site.baseurl}}/assets/js/embed.js?target=https://github.com/braze-inc/braze-web-sdk/blob/master/sample-builds/cdn/service-worker.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

#### ステップ 5: AMP Web プッシュ HTML 要素を構成する

HTMLのbodyに次の`amp-web-push`HTML要素を追加せよ。覚えておけ、と[`apiKey`](https://documenter.getpostman.com/view/4689407/SVYrsdsG)を[`baseUrl`](https://documenter.getpostman.com/view/4689407/SVYrsdsG)クエリパラメータとしてに追加する必要がある`service-worker-URL`。

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

もしあなたのサイトがRequireJSや他のAMDモジュールローダーを使用しているが、このリストにある他のオプションのいずれかでBraze Web SDKを読み込みたい場合、AMDサポートを含まないバージョンのライブラリーを読み込むことができる。このバージョンのライブラリーは、以下のCDNの場所からロードできます：

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Fno-amd-library.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

#### モジュールローダー

RequireJS または他の AMD モジュールローダーを使用する場合は、ライブラリのコピーをセルフホスティングし、他のリソースと同様に参照することをお勧めします。

```javascript
require(['path/to/braze.min.js'], function(braze) {
  braze.initialize('YOUR-API-KEY-HERE', { baseUrl: 'YOUR-SDK-ENDPOINT' });
  // Required if you want in-app messages to display automatically
  braze.automaticallyShowInAppMessages();
  braze.openSession();
});
```

### 電子 {#electron}

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

サーバーサイドレンダリング（SSR）フレームワークを使用する場合、SDKはブラウザ環境での実行を想定しているため、エラーが発生するNext.js可能性がある。これらの問題は、SDKを動的にインポートすることで解決できます。

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

詳細やTealiumの設定に関する深いサポートが必要な場合は、[統合ドキュメント]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/#about-tealium)を参照するか、Tealiumのアカウントマネージャーに連絡する。

### ヴィテ {#vite}

Viteを使用していて、循環依存関係や`Uncaught TypeError: Class extends value undefined is not a constructor or null` に関する警告が表示される場合は、Braze SDKを[依存関係の発見から](https://vitejs.dev/guide/dep-pre-bundling.html#customizing-the-behavior)除外する必要があるかもしれません：

```
optimizeDeps: {
    exclude: ['@braze/web-sdk']
},
```

### その他のタグ・マネージャー

Brazeは、カスタムHTMLタグの中で当社の統合指示に従うことにより、他のタグ管理ソリューションと互換性を持つこともできます。これらのソリューションの評価について支援が必要な場合は、Brazeの担当者にお問い合わせください。
