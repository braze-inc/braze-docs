---
nav_title: コンテンツセキュリティポリシーヘッダー
article_title: Webのコンテンツセキュリティポリシーヘッダー
platform: Web
page_order: 25
page_type: reference
description: "この記事では、Braze Web SDKに必要なコンテンツセキュリティポリシーヘッダーについて説明します。"

---

# コンテンツセキュリティポリシーのヘッダー

> Content-Security-Policy は、Web サイトでコンテンツを読み込むする方法と場所を制限することで、追加のセキュリティーを提供します。このリファレンス記事では、Web SDKに必要なコンテンツセキュリティポリシーヘッダーについて説明します。

{% alert important %}
この記事は、Cサービスプロバイダー規則を施行し、Brazeと統合するWeb サイトsに取り組む開発者を対象としています。これは、あなたがどのようにセキュリティーに侵入するのかについてのアドバイスとして意図されたものではありません。
{% endalert %}

{% multi_lang_include archive/web-v4-rename.md %}

## ノンス属性s {#nonce}

`nonce` 値を`script-src` ディレクティブまたは`style-src` ディレクティブで使用する場合は、その値を`contentSecurityNonce` 初期化オプションに渡して、SDKによって生成された新しく作成されたスクリプトおよびスタイルに伝播します。

```javascript
import * as braze from "@braze/web-sdk";

braze.initialize(apiKey, {
  baseUrl: baseUrl,
  contentSecurityNonce: "YOUR-NONCE-HERE", // assumes a "nonce-YOUR-NONCE-HERE" CSP value
});
```

## 指令 {#directives}

### connect-src {#connect-src}

- `connect-src https://sdk.iad-01.braze.com`: SDKがBraze API と通信できるようにします。
  - このURL を変更して、`baseUrl` 初期化オプションの[API SDKエンドポイント]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) に合わせます。

### script-src {#script-src}

- `script-src https://js.appboycdn.com`: CDN ホスト統合を使用する場合に必要です。
- `script-src 'unsafe-eval'`: 参照を含む統合スニペットを使用する場合は必須 `appboyQueue`
  - このディレクティブの使用を避けるには、代わりにNPMを使用して統合します。
- `script-src 'nonce-...'` または`script-src 'unsafe-inline'`:特定のアプリ内メッセージs (カスタムHTMLなど) に必要です。

### img-src {#img-src}
- `img-src: appboy-images.com braze-images.com cdn.braze.eu`: Braze CDN ホスト"画像 s を使用する場合に必要です。これらのホスト名は、ダッシュボードクラスターによって異なります。

## フォントアウェゾーム {#font-awesome}

Font Awesome の自動インクルードを無効にするには、`doNotLoadFontAwesome` 初期化オプションを使用します。

```javascript
import * as braze from "@braze/web-sdk";

braze.initialize(apiKey, {
  baseUrl: baseUrl,
  doNotLoadFontAwesome: true,
});
```

Font Awesome を使用する場合は、次のCサービスプロバイダー ディレクティブが必要です。

- `style-src https://use.fontawesome.com`
- `style-src 'nonce-...'` または `style-src 'unsafe-inline'`
- `font-src https://use.fontawesome.com`
