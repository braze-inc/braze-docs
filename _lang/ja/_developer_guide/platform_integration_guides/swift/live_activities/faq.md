---
nav_title: FAQ
article_title: ライブ活動 よくある質問
page_order: 20
description: "このページでは、Swift SDKのライブ・アクティビティに関するよくある質問に対する回答を提供する。"
tool: Live Activities
platform:
  - iOS
---

# よくある質問

> この記事では、ライブ・アクティビティに関するよくある質問に対する回答を紹介する。

## 機能性とサポート

### ライブ活動をサポートしているプラットフォームは？

ライブ・アクティビティは現在、iOS特有の機能だ。Live Activitiesの記事は、Braze Swift SDKを通してLive Activitiesを管理するための[前提][2]条件をカバーしている。

### React Nativeアプリはライブ・アクティビティをサポートしているか？

はい、React Native SDK 3.0.0+は、Braze Swift SDK経由でLive Activitiesをサポートしている。つまり、Braze Swift SDKの上に直接React Native iOSのコードを書く必要がある。 

アップルが提供するライブ・アクティビティ機能は、JavaScriptでは翻訳不可能な言語（例えば、Swiftの並行処理、ジェネリクス、SwiftUI）を使用しているため、ライブ・アクティビティ用のReact Native固有のJavaScript便利APIは存在しない。

### Brazeはキャンペーンやキャンバスのステップとしてのライブ活動をサポートしているか？

いや、これは現在サポートされていない。

## プッシュ通知とライブ活動

### ライブ・アクティビティがアクティブな状態でプッシュ通知が送信された場合はどうなるのか？ 

![ブルズ対ベアーズのスポーツ中継が画面中央に、プッシュ通知lorem ipsumのテキストが画面下部に表示された電話画面。][4]{: style="max-width:30%;float:right;margin-left:15px;"}

ライブ・アクティビティとプッシュ通知は、異なる画面領域を占有するため、ユーザーの画面上で競合することはない。

### ライブ・アクティビティがプッシュ・メッセージ機能を活用する場合、ライブ・アクティビティを受信するためにプッシュ通知を有効にする必要があるか？

ライブ・アクティビティは更新をプッシュ通知に依存しているが、それらは異なるユーザー設定によって制御されている。ユーザーはライブ・アクティビティには参加できるが、プッシュ通知には参加できない。 

アップル社は、ユーザーがアプリ内で何らかのアクションを起こし、ライブ・アクティビティを開始することを要求している。このライブ・アクティビティ・トークンの有効期限は8時間である。 

### ライブ活動にはプッシュ・プライマーが必要か？

[プッシュ・プライマーは][1]、ユーザーにアプリからのプッシュ通知をオプトインするよう促すベストプラクティスだ。しかし、ライブ・アクティビティを選択するためのシステム・プロンプトはない。iOS 16.1+にアップグレードすると、ユーザーはデフォルトでライブ・アクティビティにオプトインされる。

## 技術的な話題とトラブルシューティング

### ライブ・アクティビティにエラーがあるかどうかを知るには？

Live Activityのエラーは、Brazeダッシュボードの[Message Activity Logに]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/)記録され、"LiveActivity Errors "でフィルタリングできる。

### `live_activity/update` エンドポイントを使おうとすると、Access Denied 応答が返ってくる。なぜだ？

使用するAPIキーには、さまざまなBraze APIエンドポイントにアクセスするための適切なパーミッションを与える必要がある。以前に作成したAPIキーを使用している場合、その権限の更新を怠っている可能性がある。[APIキー・セキュリティの概要を][3]読んで復習しておこう。

### `messages/send` エンドポイントは、`messages/live_activity/update` エンドポイントとレート制限を共有しているか？ 

デフォルトでは、`messages/live_activity/update` エンドポイントのレート制限は、ワークスペースごとに、複数のエンドポイントにわたって、1時間あたり250,000リクエストである。詳しくは\[API rate limits][5] ]を参照のこと。

### なぜプッシュ・トゥ・スタートのトークンが生成されないのか？

iOS 17.2以降から、アップルは`pushToStartToken` と`pushToStartTokenUpdates` APIを制限している。実際には、push-to-startトークンは、最初のインストール後、`application(_:didFinishLaunchingWithOptions:)` 、最初のアプリ起動時にのみ生成される。このステップを繰り返す必要がある場合、トークンはアプリを再起動して再インストールした後、または手動でそのライブ・アクティビティの新しいインスタンスを作成した後にのみ、再度生成することができる。

### トラブルシューティング中に他に気をつけるべきことは？

- 認証に`.p8` キーを使用していることを確認する。
- プッシュ・プロビジョニング・プロファイルがテストしている環境と一致していることを確認する。Universal証明書は、Brazeダッシュボードで、開発または本番のApple Push Notificationサービス（APNs）環境のいずれかに送信するように設定することができる。実稼働アプリ用の開発証明書または開発アプリ用の実稼働証明書は動作しません。


[1]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/live_activities/live_activities/#prerequisites
[3]: {{site.baseurl}}/api/basics/#rest-api-key-security
[4]: {% image_buster /assets/img/push-vs-live-activities.png %}
[5]: {{site.baseurl}}/api/api_limits/