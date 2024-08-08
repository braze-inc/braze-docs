---
nav_title: AMP サポート
article_title: ウェブ向けAMPサポート
platform: Web
page_order: 5
page_type: reference
description: "このリファレンス記事では、Web の AMP サポートと、AMP ページに Braze を統合する方法について説明します。"

---

# AMP サポート

{% alert note %}
Braze を AMP ページに統合しようとしている場合を除き、このセクションを統合する必要はありません。
{% endalert %}

> このリファレンス記事では、Web の AMP サポートと、AMP ページに Braze を統合する方法について説明します。Accelerated Mobile Pages (AMP) は、JavaScript の使用制限を含む特定の標準を適用することで、モバイル デバイスでのページの読み込み時間を短縮することを目的として設計された、Google が支援するプロジェクトです。

その結果、Braze SDK を AMP ページに読み込むことができません。ただし、AMP プロジェクトでは Web プッシュをサポートするコンポーネントが提供されています。[以下の手順では、](https://www.ampproject.org/docs/reference/components/amp-web-push) そのコンポーネントの設定方法と、次のドキュメントの参照方法を詳しく説明します。 `amp-web-push` 成分。

## ステップ 1:AMP ウェブプッシュスクリプトを含める

次の非同期スクリプト タグをヘッドに追加します。

\`\`\`js
<script async custom-element="amp-web-push" src="https://cdn.ampproject.org/v0/amp-web-push-0.1.js"></script>
```

## ステップ 2: 購読と購読解除のウィジェットを追加する

ユーザーがプッシュを購読および購読解除できるようにするウィジェットを追加する必要があります。これは HTML の本文内に記述する必要があり、必要に応じてスタイルを設定できます。 

\`\`\`js
<!-- A subscription widget -->
<amp-web-push-widget visibility="unsubscribed" layout="fixed" width="250" height="80">
  <button on="tap:amp-web-push.subscribe">Subscribe to Notifications</button>
</amp-web-push-widget>

<!-- An unsubscription widget -->
<amp-web-push-widget visibility="subscribed" layout="fixed" width="250" height="80">
  <button on="tap:amp-web-push.unsubscribe">Unsubscribe from Notifications</button>
</amp-web-push-widget>
```

## ステップ 3: ダウンロードヘルパー iFrame と許可ダイアログ

AMP Web Push コンポーネントは、プッシュ サブスクリプションを処理するポップアップを作成することで機能します。そのため、プロジェクトにいくつかのヘルパー ファイルを含める必要があります。[helper-iframe.html](https://cdn.ampproject.org/v0/amp-web-push-helper-frame.html) ファイルと [permission-dialog.html](https://cdn.ampproject.org/v0/amp-web-push-permission-dialog.html) ファイルをダウンロードし、サイトに保存します。 

## ステップ 4: サービスワーカーファイルを作成する

作成する `service-worker.js` 次の内容のファイルを作成し、Web サイトのルート ディレクトリに配置します。

<script src="https://braze-inc.github.io/embed-like-gist/embed.js?target=https://github.com/braze-inc/braze-web-sdk/blob/master/sample-builds/cdn/service-worker.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

## ステップ 5: AMPウェブプッシュHTML要素を構成する

次に、 `amp-web-push` ページに HTML 要素を追加します。次の HTML コードをドキュメントの本文に挿入します。

\`\`\`js
<amp-web-push
レイアウト="表示なし"
id="amp-web-push"
helper-iframe-url="FILE\_PATH\_TO\_YOUR\_HELPER\_IFRAME"
permission-dialog-url="許可ダイアログへのファイルパス"
service-worker-url="FILE\_PATH\_TO\_YOUR\_SERVICE\_WORKER?apiKey={YOUR\_API\_KEY}&baseUrl={YOUR\_BASE\_URL}"
>
\`\`\`

特に、 `service-worker-URL` 追加が必要です `apiKey` そして `baseUrl` （https://dev.appboy.com/api/v3) as query parameters.

これで、AMP ページでプッシュ サブスクリプションとサブスクリプション解除が構成されるはずです。 
