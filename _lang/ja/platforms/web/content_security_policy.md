---
nav_title: コンテンツセキュリティポリシーのヘッダー
article_title: Webのコンテンツセキュリティポリシーヘッダー
platform: Web
page_order: 21
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

### `connect-src` {#connect-src}

{% alert warning %}
URL は、選択した `baseUrl` 初期化オプションの [ API SDKエンドポイント]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/)と一致しなければなりません。
{% endalert %}

|URL|インフォメーション|
|---|-----------|
|`connect-src https://sdk.iad-01.braze.com`|SDK が Braze API と通信できるようにします。このURL を、選択した`baseUrl` 初期化オプションの[API SDK エンドポイント]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) に一致するように変更します。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### `script-src` {#script-src}

|URL|インフォメーション|
|---|-----------|
|`script-src https://js.appboycdn.com`|CDN ホスト統合を使用する場合に必要です。|
|`script-src 'unsafe-eval'`|`appboyQueue` への参照を含む統合スニペットを使用する場合に必要です。このディレクティブの使用を避けるには、[代わりにNPM]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/?tab=package%20manager)を使用してSDKを統合します。|
|`script-src 'nonce-...'`<br>または<br>`script-src 'unsafe-inline'`|カスタムHTML など、特定のアプリ内メッセージに必要です。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### `img-src` {#img-src}

|URL|インフォメーション|
|---|-----------|
|`img-src: appboy-images.com braze-images.com cdn.braze.eu`|Braze CDN ホスト画像を使用する場合に必要です。ホスト名はダッシュボードクラスタによって異なる場合があります。<br><br>**重要:**カスタムフォントを使用している場合は、`font-src` も含める必要があります。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

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

- `font-src https://use.fontawesome.com`
- `style-src https://use.fontawesome.com`
- `style-src 'nonce-...'` または `style-src 'unsafe-inline'`
