---
nav_title: 統合
article_title: プッシュ統合
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

> プッシュ通知は、重要なアップデートが発生したときにユーザーの画面に表示されるアラートである。プッシュ通知は、あなたのウェブページがユーザーのブラウザで開いていないときでも受け取ることができる。プッシュ通知は、ユーザーにタイムリーで関連性の高いコンテンツを提供したり、サイトへの再アクセスを促したりする貴重な手段だ。この参考記事では、Braze WebプッシュをBraze SDKと統合する方法について説明する。

その他のリソースについては、[プッシュのベストプラクティスを][8]参照のこと。

![][27]

ウェブプッシュ通知は、[W3Cプッシュ標準を][1]使用して実装されており、ほとんどの主要ブラウザがサポートしている。

プッシュ・プロトコルの標準とブラウザのサポートに関する詳細は、[Apple][5] [Mozillaと][6] [Microsoftの][7]リソースを参照されたい。

{% multi_lang_include archive/web-v4-rename.md %}

## 統合

### ステップ1:サイトのサービスワーカーを設定する

- まだサービスワーカーを持っていない場合は、以下のスニペットで`service-worker.js` という名前のファイルを新規作成し、ウェブサイトのルートディレクトリに置く。
- そうでなければ、サイトがすでにサービスワーカーを登録している場合、サービスワーカーファイルに以下のスニペットを追加し、Web SDKを初期化する際に [`manageServiceWorkerExternally`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize)初期化オプションを`true` に設定する。

<script src="https://braze-inc.github.io/embed-like-gist/embed.js?target=https://github.com/braze-inc/braze-web-sdk/blob/master/sample-builds/cdn/service-worker.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

サービスワーカーのファイル名が`service-worker.js` でない場合、`serviceWorkerLocation` [初期化オプションを](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions)使わなければならない。

{% alert important %}
ウェブサーバーは、サービスワーカーファイルを提供するとき、`Content-Type: application/javascript` を返さなければならない。
{% endalert %}

#### ルートディレクトリにサービスワーカーを登録できない場合は？

デフォルトでは、サービスワーカーは、それが登録されているのと同じディレクトリ内でのみ使用できる。例えば、サービスワーカーファイルが`/assets/service-worker.js` に存在する場合、それを登録できるのは`example.com/assets/*` または`assets` フォルダのサブディレクトリ内のみで、ホームページ (`example.com/`) には登録できない。このため、ルートディレクトリ（`https://example.com/service-worker.js` など）にサービスワーカーをホストし、登録することを推奨する。

ルートドメインにサービスワーカーを登録できない場合、別の方法として、サービスワーカーファイルを提供するときに [`Service-Worker-Allowed`](https://w3c.github.io/ServiceWorker/#service-worker-script-response)HTTP ヘッダを使うことである。サービスワーカーのレスポンスに`Service-Worker-Allowed: /` を返すようにサーバーを設定することで、ブラウザにスコープを広げ、別のディレクトリから使用できるように指示する。

#### タグマネージャを使ってサービスワーカーを作成できるか？

サービスワーカーはウェブサイトのサーバーでホストする必要があり、Tag Manager経由でロードすることはできない。

### ステップ2:ブラウザ登録

ブラウザがプッシュ通知を受け取るには、`braze.requestPushPermission()` を呼び出してプッシュ登録する必要がある。これは即座にユーザーにプッシュ許可を要求する。 

プッシュ許可をリクエストする前に、独自のプッシュ関連UIをユーザーに表示したい場合（ソフト・プッシュ・プロンプトとして知られている）、`braze.isPushSupported()` を使って、ユーザーのブラウザでプッシュがサポートされているかどうかをテストできる。アプリ内メッセージを使った[ソフトプッシュプロンプトの例を]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/soft_push_prompt/)参照のこと。

ユーザーの配信停止を希望する場合は、`braze.unregisterPush()` 。

{% alert important %}
最近のバージョンのSafariとFirefoxでは、このメソッドを短時間のイベントハンドラから呼び出す必要がある（例えば、ボタンのクリックハンドラやソフトプッシュプロンプトから）。これは、プッシュ登録に関する[クロームのユーザーエクスペリエンスのベストプラクティスと](https://docs.google.com/document/d/1WNPIS_2F0eyDm5SS2E6LZ_75tk6XtBSnR1xNjWJ_DPE)一致している。
{% endalert %}

### ステップ3:Safariのプッシュを設定する（オプション） {#safari}

{% alert important %}
このステップは、macOS 13のSafari 16では必要なくなった。macOS Safariの古いバージョンをサポートしたい場合のみ、このステップを完了させる。
{% endalert %}

Mac OS XのSafariでプッシュ通知をサポートしたい場合は、以下の追加手順に従ってほしい：

- [Appleへの登録][3]手順に従って、サファリのプッシュ証明書を作成する。
- Brazeダッシュボードの**Settings**ページ（APIキーがある場所）で、Webアプリを選択する。**Configure Safari Pushを**クリックし、指示に従って先ほど生成したプッシュ証明書をアップロードする。
- `braze.initialize` を呼び出すときに、オプションの`safariWebsitePushId` 設定オプションに、Safari プッシュ証明書を生成するときに使用した Web サイト・プッシュ ID を指定する。例えば `braze.initialize('YOUR-API-KEY', {safariWebsitePushId: 'web.com.example.domain'})`

## サファリ・モバイル・プッシュ {#safari-mobile}

iOSとiPadOSのSafari 16.4+は、\[ホームスクリーンに追加]\[add-to-homescreen] ] され、\[ウェブアプリケーションマニフェスト]\[manifest-file] ] ファイルを持つアプリのウェブプッシュをサポートする。ウェブ・プッシュ通知を統合する手順を完了したら、Safariのモバイル・プッシュもサポートすることができる。 

モバイルSafariウェブプッシュをサポートするには、こちらの\[ガイド]]\[safari-mobile-push-guide].

## ソフト・プッシュ・プロンプト

ソフト・プッシュ・プロンプト（「プッシュ・プライマー」とも呼ばれる）は、許可を求める際のオプトイン率を最適化するのに役立つ。

ソフト・プッシュ・プロンプト]\[push-primer] ] で、ソフト・プッシュ・プロンプトの設定について詳しく知ることができる。

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

業界のベストプラクティスは、サイト全体をセキュアにすることだが、サイトドメインをセキュアにできない顧客は、セキュアモーダルを使用することで要件を回避することができる。詳しくは\[代替プッシュ・ドメイン][28] ]の使用ガイドを読むか、[動作デモを][4]見る。

## サービスワーカーの詳細設定

サービス・ワーカー・ファイルは、インストール時に自動的に`skipWaiting` 。これを避けたい場合は、Brazeをインポートする前に、以下のコードをサービスワーカーファイルに追加する：

<script src="https://braze-inc.github.io/embed-like-gist/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Fservice-worker-skip-waiting.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

## トラブルシューティング

**統合の説明書に従ったが、まだプッシュ通知を受け取っていない。**
- ウェブ・プッシュ通知は、あなたのサイトがHTTPSであることを要求する。
- すべてのブラウザがプッシュメッセージを受信できるわけではない。ブラウザで`braze.isPushSupported()` が`true` を返すことを確認する。
- ユーザーがサイトのプッシュアクセスを拒否した場合、ブラウザの環境設定から拒否ステータスを削除しない限り、再度許可を求めるプロンプトが表示されることはない。

[1]: http://www.w3.org/TR/push-api/
[3]: https://developer.apple.com/library/mac/documentation/NetworkingInternet/Conceptual/NotificationProgrammingGuideForWebsites/PushNotifications/PushNotifications.html#//apple_ref/doc/uid/TP40013225-CH3-SW33
[4]: http://appboyj.com/modal-test.html
[5]: https://developer.apple.com/notifications/safari-push-notifications/ "Safariプッシュ通知"
[6]: https://developer.mozilla.org/en-us/docs/web/api/push_api#browser_compatibility "Mozilla Push APIのブラウザ互換性"
[7]: https://developer.microsoft.com/en-us/microsoft-edge/status/pushapi/ "Microsoft Push API"
[8]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/
[27]: {{site.baseurl}}/assets/img_archive/web_push2.png
[28]: {{ site.baseurl }}/developer_guide/platform_integration_guides/web/push_notifications/alternate_push_domain
\[push-primer] ： {{ site.baseurl }}/developer_guide/platform_integration_guides/web/push_notifications/soft_push_prompt/
\[add-to-homescreen] ： https://support.apple.com/guide/iphone/bookmark-favorite-webpages-iph42ab2f3a7/ios#iph4f9a47bbc
\[manifest-file] ： https://developer.mozilla.org/en-US/docs/Web/Manifest
\[safari-mobile-push-guide] ： {{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/safari_mobile_push/
