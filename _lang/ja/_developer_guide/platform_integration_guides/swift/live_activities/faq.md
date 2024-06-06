---
nav_title: FAQ
article_title: ライブ活動FAQ
page_order: 20
description: "このページでは、Swift SDK のライブアクティビティに関するよくある質問への回答を提供します。"
tool: Live Activities
platform:
  - iOS
---

# よくある質問

> この記事では、Live Activitiesに関するよくある質問の回答を紹介します。

## 機能性とサポート

### ライブアクティビティをサポートするプラットフォームは?

Live Activities は現在、iOS 固有の機能です。Live Activitiesの記事では、Braze Swift SDKを使用してLive Activitiesを管理するための[前提条件][2]について説明します。

### React NativeアプリはLive Activitiesをサポートしていますか?

はい、React Native SDK 3.0.0+ は、Braze Swift SDK 経由のライブアクティビティをサポートしています。つまり、React Native iOS コードをBraze Swift SDK の上に直接書き込む必要があります。 

Apple が提供するLive Activities 機能では、JavaScript で変換できない言語が使用されるため、React ネイティブ固有のJavaScript コンビニエンスAPI はありません(たとえば、Swift 同時実行性、ジェネリック、SwiftUI)。

###  Braze はキャンペーンまたはキャンバスステップとしてライブアクティビティをサポートしていますか?

いいえ、これは現在サポートされていません。

## プッシュ通知とライブアクティビティ

### ライブアクティビティがアクティブな間にプッシュ通知が送信されると、どうなりますか? 

![ブルズ対ベアーズのスポーツゲームのライブアクティビティを画面の中央に向けて表示し、画面の下部にある通知lorem ipsumテキストをプッシュします。][4]{: style="max-width:30%;float:right;margin-left:15px;"}

ライブアクティビティとプッシュ通知は、異なる画面の不動産を占有し、ユーザの画面上で競合しません。

### Live Activities がプッシュメッセージ機能を活用する場合、プッシュ通知はLive Activities を受信するために有効にする必要がありますか?

Live Activities は更新のプッシュ通知に依存しますが、異なるユーザ設定によって制御されます。ユーザはLive Activities を選択することはできますが、プッシュ通知は行わず、その逆も可能です。 

Apple では、たとえば注文するなどして、App で何らかのアクションを実行して、ユーザーがLive Activity を開始する必要があります。このLive Activity トークンは8 時間後に期限切れになります。 

### ライブアクティビティにはプッシュプライマーが必要ですか?

[プッシュプライマー][1] は、アプリから通知をプッシュすることを選択するようにユーザーに促すベストプラクティスです。ただし、Live Activities を選択するシステムプロンプトはありません。ユーザーは、iOS 16.1+ にアップグレードすると、デフォルトでLive Activities に選択されます。

## 技術的なトピックとトラブルシューティング

### Live Activities にエラーがあるかどうかは、どうすればわかりますか?

ライブアクティビティエラーは、[Message Activity Log]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) にあるBraze ダッシュボードに記録されます。ここで、"LiveActivity Errors" でフィルタリングできます。

### `live_activity/update` エンドポイントを使用しようとすると、Access Denied レスポンスを受け取ります。その理由は?

使用するAPI キーには、異なるBraze API エンドポイントにアクセスするための正しい権限が付与されている必要があります。以前に作成したAPIキーを使用している場合は、その権限の更新を怠った可能性があります。リフレッシュを行うには、[APIキーセキュリティ概要][3]をお読みください。

### `messages/send` エンドポイント共有レート制限は`messages/live_activity/update` エンドポイントにありますか? 

`messages/live_activity/update` エンドポイントには、他の Braze エンドポイントとは別のレート制限があります。デフォルトでは、`messages/live_activity/update` エンドポイントのレート制限は、1 時間あたりのワークスペースあたり250,000 リクエストです。詳しくは[レートリミット記事][5]を参照してください。

### プッシュトークンが生成されないのはなぜですか?

iOS 17.2 以降では、Apple は`pushToStartToken` および`pushToStartTokenUpdates` API を制限しています。実際には、最初のインストール後の`application(_:didFinishLaunchingWithOptions:)` での最初のアプリの起動時にのみ、プッシュ開始トークンが生成されます。この手順を繰り返す必要がある場合は、アプリを再起動して再インストールした後、またはLive Activity の新しいインスタンスを手動で作成した後にのみ、トークンを生成できます。

### トラブルシューティングの際には、他にどのようなことに注意する必要がありますか?

- 認証に`.p8` キーを使用していることを確認します。
- プッシュプロビジョニングプロファイルがテスト対象の環境と一致することを確認します。ユニバーサル証明書は、開発環境または本番環境のApple Push Notification サービス(APNs)環境のいずれかに送信するように、Braze ダッシュボードで設定できます。実稼働アプリ用の開発証明書または開発アプリ用の実稼働証明書は動作しません。


[1]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/live_activities/live_activities/#prerequisites
[3]: {{site.baseurl}}/api/basics/#rest-api-key-security
[4]: {% image_buster /assets/img/push-vs-live-activities.png %}
[5]: {{site.baseurl}}/api/api_limits/