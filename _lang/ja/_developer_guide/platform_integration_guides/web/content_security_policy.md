---
nav_title: コンテンツセキュリティポリシーヘッダー
article_title: Web 用コンテンツセキュリティポリシーヘッダー
platform: Web
page_order: 25
page_type: reference
description: "この記事では、Braze Web SDK に必要なコンテンツセキュリティポリシーヘッダーについて説明します。"

---

# コンテンツセキュリティポリシーヘッダー

> Content-Security-Policyは、Webサイトにコンテンツを読み込む方法と場所を制限することにより、セキュリティを強化します。この参考記事では、Web SDKに必要なコンテンツセキュリティポリシーヘッダーについて説明します。

{% alert important %}
この記事は、CSPルールを適用し、Brazeと統合するウェブサイトを開発する開発者を対象としています。セキュリティへの取り組み方についてのアドバイスを意図したものではありません。
{% endalert %}

{% multi_lang_include archive/web-v4-rename.md %}

## ノンス属性 {#nonce}

`nonce``script-src``style-src`またはディレクティブで値を使用する場合は、`contentSecurityNonce`その値を初期化オプションに渡して、SDK によって生成された新しく作成されたスクリプトとスタイルにその値を伝えます。

\`\`\`javascript
import * as braze from "@braze/web-sdk";

ブレイズ. イニシャライズ (API キー,); {
baseUrl: baseUrl,
contentSecurityNonce: "YOUR-NONCE-HERE", // assumes a "nonce-YOUR-NONCE-HERE" CSP value
}
  \`\`\`

## 指令 {#directives}

### Connect-src {#connect-src}

- `connect-src https://sdk.iad-01.braze.com`: SDK が Braze API と通信できるようにします。
  - この URL を、`baseUrl`初期化オプションの [API SDK エンドポイントと一致するように変更してください]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/)。

### スクリプト-src {#script-src}

- `script-src https://js.appboycdn.com`: CDN ホストインテグレーションを使用する場合に必要です。
- `script-src 'unsafe-eval'`: への参照を含む統合スニペットを使用する場合は必須 `appboyQueue`
  - このディレクティブを使わないようにするには、代わりに NPM を使って統合してください。
- `script-src 'nonce-...'` または`script-src 'unsafe-inline'`:特定のアプリ内メッセージ (カスタム HTML など) に必要です。

### img-src {#img-src}
- `img-src: appboy-images.com braze-images.com cdn.braze.eu`: Braze CDN ホストイメージを使用する場合に必要です。これらのホスト名は、ダッシュボードクラスターによって異なる場合があります。

## 素晴らしいフォント {#font-awesome}

Font Awesomeの自動インクルードを無効にするには、`doNotLoadFontAwesome`初期化オプションを使用してください。

\`\`\`javascript
import * as braze from "@braze/web-sdk";

ブレイズ. イニシャライズ (API キー,); {
baseUrl: baseUrl,
doNotLoadFontAwesome: true,
}
  \`\`\`

Font Awesome を使用する場合は、次の CSP ディレクティブが必要です。

- `style-src https://use.fontawesome.com`
- `style-src 'nonce-...'` または `style-src 'unsafe-inline'`
- `font-src https://use.fontawesome.com`
