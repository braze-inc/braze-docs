---
nav_title: AMPサポート
article_title: Web 向けの AMP サポート
platform: Web
page_order: 5
page_type: reference
description: "このリファレンス記事では、AMP の Web サポートと、AMP ページへの Braze の統合方法について説明します。"

---

# AMPサポート

{% alert note %}
このセクションは、AMPページにBrazeを統合しようとしている場合を除いて、統合する必要はありません。
{% endalert %}

> このリファレンス記事では、AMP の Web サポートと、AMP ページへの Braze の統合方法について説明します。Accelerated Mobile Pages (AMP) は、JavaScript の使用を制限することを含む特定の標準を強制することによって、モバイルデバイスでのページ読み込み時間を改善するために設計された Google 支援のプロジェクトです。

その結果、Braze SDK を AMP ページに読み込むことができません。ただし、AMP プロジェクトには Web プッシュをサポートするコンポーネントが用意されています。[次の指示](https://www.ampproject.org/docs/reference/components/amp-web-push)は、そのコンポーネントを設定する方法を詳述し、`amp-web-push`コンポーネントに関する次のドキュメントを参照します。

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

AMP Web プッシュコンポーネントは、プッシュサブスクリプションを処理するポップアップを作成することで機能します。その結果、プロジェクトにいくつかのヘルパーファイルを含める必要があります。ヘルパー[ファイルiframe.html](https://cdn.ampproject.org/v0/amp-web-push-helper-frame.html)をダウンロードして、[許可dialog.html](https://cdn.ampproject.org/v0/amp-web-push-permission-dialog.html)ファイルをダウンロードして、サイトに保存してください。 

## ステップ 4:サービスワーカーファイルを作成する

次の内容の`service-worker.js`ファイルを作成し、Web サイトのルートディレクトリに配置します:

<script src="https://braze-inc.github.io/embed-like-gist/embed.js?target=https://github.com/braze-inc/braze-web-sdk/blob/master/sample-builds/cdn/service-worker.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

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

特に、`service-worker-URL`はクエリパラメータとして`apiKey`と`baseUrl`（https://dev.appboy.com/api/v3）を追加する必要があります。

AMPページでプッシュサブスクリプションとサブスクリプション解除の設定が完了しました。 
