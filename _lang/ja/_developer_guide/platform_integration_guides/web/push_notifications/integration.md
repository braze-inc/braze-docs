---
nav_title: 統合
article_title: Web 向けプッシュ統合
platform: Web
channel: push
page_order: 0
page_type: reference
description: "この記事では、Braze SDK を使用して Braze ウェブプッシュを統合する方法について説明します。"

local_redirect: #soft-push-prompts
  soft-push-prompts: '/docs/developer_guide/platform_integration_guides/web/push_notifications/soft_push_prompt/'
search_rank: 3
---

# プッシュ通知の統合

> プッシュ通知は、重要な更新が発生したときにユーザーの画面に表示されるアラートです。プッシュ通知は、ウェブページがユーザーのブラウザで現在開いていない場合でも受信できます。プッシュ通知は、時間的制約があって関連性の高いコンテンツをユーザーに提供したり、ユーザーをアプリに再エンゲージしたりするための効果的な方法です。この参考記事では、Braze ウェブプッシュを Braze SDK と統合する方法について説明します。

その他のリソースについては、[プッシュのベストプラクティスを参照してください][8]。

![][27]

Web プッシュ通知は、ほとんどの主要ブラウザがサポートする [W3C プッシュ標準を使用して実装されます][1]。

[プッシュプロトコル標準とブラウザーサポートの詳細については、[Apple][5] [Mozilla][6]、Microsoft のリソースをご覧ください。][7]

{% multi_lang_include archive/web-v4-rename.md %}

## 統合

### ステップ 1:サイトのサービスワーカーを設定する

- サービスワーカーをまだ作成していない場合は、`service-worker.js`次のスニペットを含む名前の新しいファイルを作成し、それをWebサイトのルートディレクトリに配置します。
- それ以外の場合は、サイトですでにサービスワーカーを登録している場合は、次のスニペットをサービスワーカーファイルに追加し、Web SDK [`manageServiceWorkerExternally`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize)`true`を初期化するときに初期化オプションをに設定します。

<script src="https://braze-inc.github.io/embed-like-gist/embed.js?target=https://github.com/braze-inc/braze-web-sdk/blob/master/sample-builds/cdn/service-worker.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

サービスワーカーのファイル名がでない場合は`service-worker.js`、`serviceWorkerLocation`[初期化オプションを使用する必要があります](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions)。

{% alert important %}
Web サーバーは、`Content-Type: application/javascript`サービスワーカーファイルを提供するときにを返す必要があります。
{% endalert %}

#### ルートディレクトリにサービスワーカーを登録できない場合はどうなりますか?

デフォルトでは、サービスワーカーは登録されている同じディレクトリ内でのみ使用できます。たとえば、Service Worker ファイルがに存在する場合`/assets/service-worker.js`、`example.com/assets/*``assets`登録できるのはフォルダ内またはフォルダのサブディレクトリだけで、ホームページ (`example.com/`) には登録できません。このため、Service Worker をルートディレクトリ (など`https://example.com/service-worker.js`) でホストして登録することをお勧めします。

ルートドメインにサービスワーカーを登録できない場合は、サービスワーカーファイルを提供する際に [`Service-Worker-Allowed`](https://w3c.github.io/ServiceWorker/#service-worker-script-response)HTTP ヘッダーを使用する方法もあります。Service Worker `Service-Worker-Allowed: /` への応答を返すようにサーバーを設定することで、ブラウザーに範囲を広げて別のディレクトリ内から使用できるように指示します。

#### タグマネージャーを使用してサービスワーカーを作成できますか？

いいえ、サービスワーカーはウェブサイトのサーバーでホストされている必要があり、タグマネージャーでは読み込めません。

### ステップ 2: ブラウザ登録

ブラウザがプッシュ通知を受信するには、呼び出しでプッシュ通知を登録する必要があります`braze.requestPushPermission()`。これにより、ユーザーにプッシュ許可がすぐに要求されます。 

プッシュ権限 (ソフト・プッシュ・プロンプト) をリクエストする前に、独自のプッシュ関連UIをユーザーに表示したい場合は、を使用してユーザーのブラウザでプッシュがサポートされているかどうかをテストできます。`braze.isPushSupported()`[アプリ内メッセージを使用したソフトプッシュプロンプトの例を参照してください]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/soft_push_prompt/)。

ユーザーの登録を解除したい場合は、`braze.unregisterPush()`電話で行うことができます。

{% alert important %}
最近のバージョンの Safari と Firefox では、このメソッドを存続期間の短いイベントハンドラ (ボタンクリックハンドラやソフトプッシュプロンプトなど) から呼び出す必要があります。これは [Chrome のプッシュ登録に関するユーザーエクスペリエンスのベストプラクティスと一致しています](https://docs.google.com/document/d/1WNPIS_2F0eyDm5SS2E6LZ_75tk6XtBSnR1xNjWJ_DPE)。
{% endalert %}

### ステップ 3: Safari プッシュの設定 (オプション) {#safari}

{% alert important %}
macOS 13 の Safari 16 以降、このステップは不要になりました。古いバージョンの macOS Safari をサポートしたい場合にのみ、この手順を実行してください。
{% endalert %}

Mac OS X で Safari のプッシュ通知をサポートしたい場合は、以下の追加手順に従ってください。

- 「[Apple への登録][3]」の手順に従って、Safari プッシュ証明書を生成します。
- Braze **ダッシュボードの設定ページ**（API キーが保存されているページ）で、ウェブアプリを選択します。「**Safari Push の設定**」をクリックし、指示に従い、生成したプッシュ証明書をアップロードします。
- 電話をかけるときに`braze.initialize`、Safari プッシュ証明書を生成したときに使用した Web サイトのプッシュ ID とともに、`safariWebsitePushId`オプションの設定オプションを指定します。以下に例を示します。

## サファリモバイルプッシュ {#safari-mobile}

iOSおよびiPadOSのSafari 16.4+は、[ホーム画面に追加] [ホーム画面に追加] され、[Webアプリケーションマニフェスト] [マニフェストファイル] ファイルを含むアプリのWebプッシュをサポートしています。Web プッシュ通知を統合する手順を完了したら、Safari のモバイルプッシュもサポートできます。 

モバイルSafariウェブプッシュをサポートするには、[ガイドはこちら] [safari-mobile-push-guide] に従ってください。

## ソフト・プッシュ・プロンプト

ソフトプッシュプロンプト（「プッシュ入門」とも呼ばれます）は、許可を求める際のオプトイン率を最適化するのに役立ちます。

ソフトプッシュプロンプトの設定の詳細については、[ソフトプッシュプロンプト] [プッシュ入門] をご覧ください。

## HTTPS 要件

ウェブ標準では、プッシュ通知の許可をリクエストするドメインは安全であることが求められます。

### 安全なサイトとはどのようなものでしょうか？

サイトが次のセキュアオリジンパターンのいずれかに一致する場合、そのサイトは安全とみなされます。

- (https, , \*)
- (wss, \*, \*)
- (, localhost, )
- (, .localhost, \*)
- (, 127/8, )
- (, ::1/128, \*)
- (file, \*, —)
- (chrome-extension, \*, —)

Braze Web push の基盤となっているオープンスタンダード仕様のこのセキュリティ要件は、中間者攻撃を防ぎます。

### 安全なサイトが利用できない場合はどうなりますか?

業界のベストプラクティスはサイト全体を安全にすることですが、サイトドメインを保護できないお客様は、安全な方法を使用して要件を回避できます。詳細については、[代替プッシュドメイン] [28] の使用ガイドをご覧になるか、[実際のデモをご覧ください][4]。

## サービスワーカーの詳細設定

`skipWaiting`当社のサービスワーカーファイルはインストール時に自動的に呼び出されます。これを回避したい場合は、Braze をインポートする前に、サービスワーカーファイルに次のコードを追加してください。

<script src="https://braze-inc.github.io/embed-like-gist/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Fservice-worker-skip-waiting.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

## トラブルシューティング

**連携手順に従ったのに、まだプッシュ通知が届きません。**
-Webプッシュ通知では、サイトがHTTPSである必要があります。
-すべてのブラウザがプッシュメッセージを受信できるわけではありません。`braze.isPushSupported()``true`ブラウザに戻っていることを確認します。
-ユーザーがサイトプッシュアクセスを拒否した場合、ブラウザーの設定から拒否ステータスを削除しない限り、再度許可を求めるメッセージは表示されません。

[1]: http://www.w3.org/TR/push-api/
[3]: https://developer.apple.com/library/mac/documentation/NetworkingInternet/Conceptual/NotificationProgrammingGuideForWebsites/PushNotifications/PushNotifications.html#//apple_ref/doc/uid/TP40013225-CH3-SW33
[4]: http://appboyj.com/modal-test.html
[5]: https://developer.apple.com/notifications/safari-push-notifications/ "サファリプッシュ通知"
[6]: https://developer.mozilla.org/en-us/docs/web/api/push_api#browser_compatibility "Mozilla プッシュ API ブラウザーの互換性"
[7]: https://developer.microsoft.com/en-us/microsoft-edge/status/pushapi/ "マイクロソフトプッシュ API"
[8]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/
[27]: {{site.baseurl}}/assets/img_archive/web_push2.png
[7]:{{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/alternate_push_domain
[push-primer]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/soft_push_prompt/
[add-to-homescreen]: https://support.apple.com/guide/iphone/bookmark-favorite-webpages-iph42ab2f3a7/ios#iph4f9a47bbc
[manifest-file]: https://developer.mozilla.org/en-US/docs/Web/Manifest
[safari-mobile-push-guide]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/safari_mobile_push/
