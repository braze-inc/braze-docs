---
nav_title: 統合
article_title: Web のプッシュ統合
platform: Web
channel: push
page_order: 0
page_type: reference
description: "この記事では、Braze SDKを介してBraze Webプッシュを統合する方法について説明する。"

local_redirect: #soft-push-prompts
  soft-push-prompts: '/docs/developer_guide/platform_integration_guides/web/push_notifications/soft_push_prompt/'
search_rank: 3
---

# プッシュ通知の統合

> プッシュ通知は、重要なアップデートが発生したときにユーザーの画面に表示されるアラートである。プッシュ通知は、ユーザーのブラウザーであなたの Web ページが開かれていないときでも受け取ることができます。プッシュ通知は、ユーザーにタイムリーで関連性の高いコンテンツを提供したり、サイトへの再アクセスを促したりする貴重な手段だ。この参考記事では、Braze Web プッシュを Braze SDK と統合する方法について説明します。

その他のリソースについては、[プッシュのベストプラクティスを]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/)参照のこと。

![]({{site.baseurl}}/assets/img_archive/web_push2.png)

Web プッシュ通知は、大部分の主要ブラウザーでサポートされている [W3C プッシュ標準](http://www.w3.org/TR/push-api/)を使用します。

プッシュプロトコルの標準とブラウザサポートの詳細については、[Apple](https://developer.apple.com/notifications/safari-push-notifications/ "Safari プッシュ通知")[Mozilla](https://developer.mozilla.org/en-us/docs/web/api/push_api#browser_compatibility "Mozilla プッシュAPI ブラウザの互換性")と[Microsoft](https://developer.microsoft.com/en-us/microsoft-edge/status/pushapi/ "Microsoft プッシュAPI")からリソースを確認できます。

{% multi_lang_include archive/web-v4-rename.md %}

## 統合

### ステップ1:サイトのサービスワーカーを設定する

- まだサービスワーカーを持っていない場合は、以下のスニペットで`service-worker.js` という名前のファイルを新規作成し、ウェブサイトのルートディレクトリに置く。
- そうではない場合に、サイトでサービスワーカーをすでに登録しているときは、次のスニペットをサービスワーカーファイルに追加し、Web SDK を初期化するときに [`manageServiceWorkerExternally`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize) 初期化オプションを `true` に設定します。

<script src="{{site.baseurl}}/assets/js/embed.js?target=https://github.com/braze-inc/braze-web-sdk/blob/master/sample-builds/cdn/service-worker.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

サービスワーカーのファイル名が `service-worker.js` ではない場合、`serviceWorkerLocation` [初期化オプション](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions)を使用する必要があります。

{% alert important %}
サービスワーカーファイルを提供するときは、Web サーバーが `Content-Type: application/javascript` を返す必要があります。
{% endalert %}

#### ルートディレクトリにサービスワーカーを登録できない場合は？

デフォルトでは、サービスワーカーは、それが登録されているのと同じディレクトリ内でのみ使用できる。たとえば、サービスワーカーファイルが `/assets/service-worker.js` に存在する場合、`example.com/assets/*`、または `assets` フォルダーのサブディレクトリー内にのみ登録でき、ホームページ (`example.com/`) には登録できません。このため、ルートディレクトリ (`https://example.com/service-worker.js` など) にサービスワーカーをホストして登録することをお勧めします。

ルートドメインにサービスワーカーを登録できない場合、別の方法として、サービスワーカーファイルを提供するときに [`Service-Worker-Allowed`](https://w3c.github.io/ServiceWorker/#service-worker-script-response)HTTP ヘッダを使うことである。サービスワーカーのレスポンスに`Service-Worker-Allowed: /` を返すようにサーバーを設定することで、ブラウザにスコープを広げ、別のディレクトリから使用できるように指示する。

#### タグマネージャを使用してサービスワーカーを作成できますか?

いいえ、サービスワーカーは Web サイトのサーバーでホストされている必要があり、タグマネージャで読み込むことはできません。

### ステップ2:ブラウザ登録

ブラウザーがプッシュ通知を受信するには、`braze.requestPushPermission()` を呼び出してプッシュ用に登録する必要があります。これは即座にユーザーにプッシュ許可を要求する。 

プッシュ許可をリクエストする前に、独自のプッシュ関連UIをユーザーに表示したい場合（ソフト・プッシュ・プロンプトとして知られている）、`braze.isPushSupported()` を使って、ユーザーのブラウザでプッシュがサポートされているかどうかをテストできる。アプリ内メッセージを使った[ソフトプッシュプロンプトの例を]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/soft_push_prompt/)参照のこと。

ユーザーへの配信停止を行うには、`braze.unregisterPush()` を呼び出します。

{% alert important %}
最近のバージョンのSafariとFirefoxでは、このメソッドを短時間のイベントハンドラから呼び出す必要がある（例えば、ボタンのクリックハンドラやソフトプッシュプロンプトから）。これは、プッシュ登録に関する [Chrome のユーザーエクスペリエンスのベストプラクティス](https://docs.google.com/document/d/1WNPIS_2F0eyDm5SS2E6LZ_75tk6XtBSnR1xNjWJ_DPE)と一致しています。
{% endalert %}

### ステップ3:Safariのプッシュを設定する（オプション） {#safari}

{% alert important %}
このステップは、macOS 13上の Safari 16では不要になりました。macOS Safariの古いバージョンをサポートしたい場合のみ、このステップを完了させる。
{% endalert %}

Mac OS X で Safari 向けのプッシュ通知をサポートする場合は、以下の追加手順に従ってください。

- [Appleへの登録](https://developer.apple.com/library/mac/documentation/NetworkingInternet/Conceptual/NotificationProgrammingGuideForWebsites/PushNotifications/PushNotifications.html#//apple_ref/doc/uid/TP40013225-CH3-SW33)手順に従って、サファリのプッシュ証明書を作成する。
- Braze ダッシュボードの [**設定**] ページ (API キーが置かれている場所) で Web アプリを選択します。[**Safari プッシュ通知を設定**]をクリックして指示に従い、生成したプッシュ証明書をアップロードします。
- `braze.initialize` を呼び出す場合は、オプションの`safariWebsitePushId` 設定オプションに、Safari プッシュ証明書の生成時に使用した Web サイトプッシュ ID を指定します。たとえば、次のようにします。`braze.initialize('YOUR-API-KEY', {safariWebsitePushId: 'web.com.example.domain'})`

## Safari Mobile のプッシュ {#safari-mobile}

iOS および iPadOS 上の Safari 16.4 以降は、[[ホーム画面に追加され]](https://support.apple.com/guide/iphone/bookmark-favorite-webpages-iph42ab2f3a7/ios#iph4f9a47bbc)、[[Web アプリケーションマニフェスト]](https://developer.mozilla.org/en-US/docs/Web/Manifest)ファイルを持つアプリの Web プッシュをサポートします。Web プッシュ通知を統合する手順を完了したら、Safari のモバイルプッシュもサポートできるようになります。 

モバイル Safari Web プッシュをサポートするには、[[このガイド]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/safari_mobile_push/)]の説明に従ってください。

## ソフトプッシュプロンプト

ソフト・プッシュ・プロンプト（「プッシュ・プライマー」とも呼ばれる）は、許可を求める際のオプトイン率を最適化するのに役立つ。

ソフトプッシュプロンプトの設定について詳しくは、[ソフトプッシュプロンプト]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/push_notifications/soft_push_prompt/)を参照してください。

## HTTPS要件

ウェブ標準は、プッシュ通知の許可を要求するドメインが安全であることを要求している。

### 何が安全なサイトを定義するのか？

サイトが以下のセキュア・オリジン・パターンのいずれかに一致する場合、そのサイトはセキュアとみなされる：

- (https, , \*)
- (wss, \*, \*)
- (, localhost, )
- (, .localhost, \*)
- (, 127/8, )
- (, ::1/128, \*)
- (file, \*, —)
- (chrome-extension, \*, —)

Braze Webプッシュが基づいているオープンスタンダード仕様のこのセキュリティ要件は、中間者攻撃を防ぐ。

### 安全なサイトが利用できない場合はどうするのか？

業界のベストプラクティスは、サイト全体をセキュアにすることですが、サイトドメインをセキュアにできない顧客は、セキュアなモーダルを使用して要件に対処できます。詳細については、[代替プッシュドメイン]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/push_notifications/alternate_push_domain)または[作業デモ](http://appboyj.com/modal-test.html)を表示するガイドを参照してください。

## サービスワーカーの詳細設定

サービスワーカーファイルは、インストール時に自動的に `skipWaiting` を呼び出します。これを避けたい場合は、Brazeをインポートする前に、以下のコードをサービスワーカーファイルに追加する：

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Fservice-worker-skip-waiting.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

## トラブルシューティング

**統合の説明書に従ったが、まだプッシュ通知を受け取っていない。**
- Web プッシュ通知では、サイトで HTTPS を使用する必要があります。
- すべてのブラウザがプッシュメッセージを受信できるわけではない。ブラウザで`braze.isPushSupported()` が`true` を返すことを確認する。
- ユーザーがサイトのプッシュアクセスを拒否した場合、ブラウザの環境設定から拒否ステータスを削除しない限り、再度許可を求めるプロンプトが表示されることはない。

