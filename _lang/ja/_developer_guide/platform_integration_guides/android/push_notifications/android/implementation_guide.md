---
nav_title: 上級実装ガイド (オプション)
article_title: Android 向け上級プッシュ通知の実装 (オプション)
platform: Android
page_order: 29
description: "この上級実装ガイドでは、メッセージ内にユーザー固有の情報を表示するようにプッシュ通知のレイアウトをカスタマイズする方法について説明します。また、Braze チームが作成したユースケースの例、付属のコードスニペット、ロギング分析に関するガイダンスも含まれています。"
channel:
  - push
---

<br>
{% alert important %}
基本的なプッシュ通知開発者統合ガイドをお探しの場合は、ここで見つけてください[here]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/).
{% endalert %}

# 上級実装ガイド

> このオプションの上級実装ガイドでは、カスタムの FirebaseMessagingService サブクラスを活用してプッシュメッセージを最大限に活用する方法について説明します。Braze チームが作成したカスタムのユースケース、付属のコードスニペット、ロギング分析に関するガイダンスも含まれています。[こちらから](https://github.com/braze-inc/braze-growth-shares-android-demo-app) Braze Demo リポジトリにアクセスしてください。この実装ガイドは、Kotlin 実装を中心に扱っていますが、興味のある方のために Java のスニペットが提供されています。

## カスタム通知レイアウト

Braze の通知は[データメッセージ](https://firebase.google.com/docs/cloud-messaging/concept-options)として送信されます。つまり、アプリケーションはバックグラウンド実行されているときでも、いつでも応答し、適切な動作を実行できます（それとは対照的に、通知メッセージは、アプリがバックグラウンドで実行されているときはシステムによって自動的に処理されます）。そのため、通知トレイに配信される通知にパーソナライズされた UI 要素を表示するなどして、アプリケーションでエクスペリエンスをカスタマイズできます。この方法でプッシュを実装することに慣れていない方もいるかもしれませんが、Braze でよく知られている機能の 1 つである[プッシュ通知ストーリー]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_stories/)は、カスタムビューコンポーネントを使用して魅力的なエクスペリエンスを生み出す機能の良い例です。

#### 要件

Android では、カスタム通知ビューを実装するために使用できるコンポーネントにいくつかの制限があります。通知ビューレイアウトには、[RemoteViews](https://developer.android.com/reference/android/widget/RemoteViews) フレームワークと互換性のある View オブジェクト_のみ_を含める必要があります。

### パーソナライズされたプッシュ通知

プッシュ通知では、カスタムビュー階層内にユーザー固有の情報を表示できます。次の例は、ユーザーが特定のタスク (Braze ラーニングコース) を完了した後で送られるプッシュ通知であり、通知を展開して進捗状況を確認することをユーザーに促しています。ここで提供される情報はユーザー固有であり、セッションが完了するか、API トリガーを利用して特定のユーザーアクションが実行されたときに呼び出すことができます。 

![パーソナライズされたプッシュダッシュボードの例]({% image_buster /assets/img/push_implementation_guide/android_push_custom_layout.png %}){: style="max-width:65%;border:0"}

#### ダッシュボード設定

パーソナライズされたプッシュをダッシュボードで設定するには、表示する特定のカテゴリを登録する必要があります。標準の Liquid を使用して、メッセージに表示する適切なユーザー属性をキーと値のペア内で設定します。これらのビューは、特定のユーザープロファイルの特定のユーザー属性に基づいてカスタマイズできます。

![パーソナライズされたプッシュダッシュボードの例]({% image_buster /assets/img/push_implementation_guide/push5.png %}){: style="max-width:60%;"}

##### 分析をログに記録する準備ができましたか?
データフローの詳細については、[次のセクション](#logging-analytics)を参照してください。

## 分析のロギング

### Braze API を使用したロギング (推奨)

ロギング分析は、[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) エンドポイントに到達する顧客のサーバーの助けを借りて、リアルタイムでのみ実行できます。分析をログに記録するには、`braze_id` 値をキーと値のペアフィールド (次のスクリーンショットを参照) に送信し、更新するユーザープロファイルを識別します。

![パーソナライズされたプッシュダッシュボードの例]({% image_buster /assets/img/push_implementation_guide/android_braze_id_configuration.png %}){: style="max-width:80%;"}

### 手動ロギング 

手動ロギングを行うには、ペイロードに含まれているエクストラに基づいて、`FirebaseMessagingService.onMessageReceived` 実装内またはスタートアップアクティビティ内から必要な要素をログに記録します。ただし、覚えておくべき重要な注意点として、Android システムによって[フラグが立てられたり終了されたりする](https://firebase.google.com/docs/cloud-messaging/android/receive)のを避けるため、`FirebaseMessagingService` サブクラスは呼び出しから 10 秒以内に実行を終了する_必要があります_。 


