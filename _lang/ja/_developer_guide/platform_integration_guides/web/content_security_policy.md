---
nav_title: コンテンツセキュリティポリシーヘッダー
article_title: Webのコンテンツセキュリティポリシーヘッダー
platform: Web
page_order: 25
page_type: reference
description: "この記事では、Braze Web SDK に必要なコンテンツセキュリティポリシーヘッダーについて説明します。"

---

# コンテンツセキュリティポリシーのヘッダー

> Content-Security-Policy は、Web サイトでコンテンツを読み込むする方法と場所を制限することで、追加のセキュリティーを提供します。この参考記事では、Web SDK に必要なコンテンツセキュリティポリシーヘッダーについて説明します。

{% alert important %}
この記事は、CSP 規則を実行し、Braze と統合する Web サイトを処理する開発者を対象にしています。セキュリティ問題にどのように対処するかについての助言を目的としたものではありません。
{% endalert %}

{% multi_lang_include archive/web-v4-rename.md %}

## Nonce 属性 {#nonce}

`nonce` 値を `script-src` または `style-src` ディレクティブで使用し、その値を `contentSecurityNonce` 初期化オプションに渡して、新たに作成されたスクリプトと SDK によって生成されたスタイルにそれを伝播する場合:

```javascript
import * as braze from "@braze/web-sdk";

braze.initialize(apiKey, {
  baseUrl: baseUrl,
  contentSecurityNonce: "YOUR-NONCE-HERE", // assumes a "nonce-YOUR-NONCE-HERE" CSP value
});
```

## 指令 {#directives}

### connect-src {#connect-src}

- `connect-src https://sdk.iad-01.braze.com`: SDK が Braze API と通信できるようにします。
  - このURL を変更して、`baseUrl` 初期化オプションの[API SDKエンドポイント]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) に合わせます。

### script-src {#script-src}

- `script-src https://js.appboycdn.com`: CDN ホスト統合を使用する場合に必要です。
- `script-src 'unsafe-eval'`: `appboyQueue` への参照を含む統合スニペットを使用する場合に必要です。
  - このディレクティブの使用を避けるには、代わりにNPMを使用して統合します。
- `script-src 'nonce-...'` または`script-src 'unsafe-inline'`:特定のアプリ内メッセージs (カスタムHTMLなど) に必要です。

### img-src {#img-src}
- `img-src: appboy-images.com braze-images.com cdn.braze.eu`: Braze CDN ホスト画像を使用する場合に必要です。これらのホスト名は、ダッシュボードクラスターによって異なります。

## Font Awesome {#font-awesome}

Font Awesome の自動組み込みを無効にするには、次のように `doNotLoadFontAwesome` 初期化オプションを使用します。

```javascript
import * as braze from "@braze/web-sdk";

braze.initialize(apiKey, {
  baseUrl: baseUrl,
  doNotLoadFontAwesome: true,
});
```

Font Awesome を使用する場合は、次の CSP ディレクティブが必要です。

- `style-src https://use.fontawesome.com`
- `style-src 'nonce-...'` または `style-src 'unsafe-inline'`
- `font-src https://use.fontawesome.com`
