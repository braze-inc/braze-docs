---
nav_title: AMPサポート
article_title: Web 向けの AMP サポート
platform: Web
page_order: 5
page_type: reference
description: "この参考記事では、Web の AMP サポートと、AMP ページに Braze を統合する方法について説明します。"

---

# AMPサポート

{% alert note %}
このセクションは、AMPページにBrazeを統合しようとしている場合を除いて、統合する必要はありません。
{% endalert %}

> この参考記事では、Web の AMP サポートと、AMP ページに Braze を統合する方法について説明します。Accelerated Mobile Pages (AMP) は、JavaScript の使用を制限するなど、特定の基準を適用することで、モバイル端末のページ読み込み時間を改善するように設計された Google が支援するプロジェクトです。

その結果、Braze SDK を AMP ページに読み込むことはできません。ただし、AMP プロジェクトには Web プッシュをサポートするコンポーネントが用意されています。[以下の手順](https://www.ampproject.org/docs/reference/components/amp-web-push) では、そのコンポーネントを設定し、`amp-web-push` コンポーネントに関する以下のドキュメントを参照する方法を説明しています。

## ステップ 1:AMP Web プッシュスクリプトを含める

次の非同期スクリプトタグをヘッドに追加します：

```js
<script async custom-element="amp-web-push" src="https://cdn.ampproject.org/v0/amp-web-push-0.1.js"></script>
```

## ステップ2:サブスクリプションとサブスクリプション解除ウィジェットを追加

プッシュ通知の購読と配信停止をユーザーが行えるウィジェットを追加する必要があります。これはHTMLの本文内に配置され、好きなようにスタイルを適用できます。

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

## ステップ 3:ダウンロードヘルパーiFrameと許可ダイアログ

AMP Web プッシュコンポーネントは、プッシュサブスクリプションを処理するポップアップを作成することで機能します。その結果、プロジェクトにいくつかのヘルパーファイルを含める必要があります。[helper-iframe.html](https://cdn.ampproject.org/v0/amp-web-push-helper-frame.html) ファイルおよび [permission-dialog.html](https://cdn.ampproject.org/v0/amp-web-push-permission-dialog.html) ファイルをダウンロードして、サイトに保存してください。

## ステップ 4:サービスワーカーファイルを作成する

次の内容の`service-worker.js`ファイルを作成し、Web サイトのルートディレクトリに配置します:

<script src="{{site.baseurl}}/assets/js/embed.js?target=https://github.com/braze-inc/braze-web-sdk/blob/master/sample-builds/cdn/service-worker.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

## ステップ 5: AMP Web プッシュ HTML 要素を構成する

これで、ページに`amp-web-push` HTML要素を追加する必要があります。次のHTMLコードをドキュメントの本文にドロップします:

```js
<amp-web-push
layout="nodisplay"
id="amp-web-push"
helper-iframe-url="FILE_PATH_TO_YOUR_HELPER_IFRAME"
permission-dialog-url="FILE_PATH_TO_YOUR_PERMISSION_DIALOG"
service-worker-url="FILE_PATH_TO_YOUR_SERVICE_WORKER?apiKey={YOUR_API_KEY}&baseUrl={YOUR_BASE_URL}"
>
```

特に、`service-worker-URL` はクエリパラメーターして `apiKey` と `baseUrl` (https://dev.appboy.com/api/v3) を追加する必要があります。

AMP ページでプッシュサブスクリプションとサブスクリプション解除の設定が完了しました。
