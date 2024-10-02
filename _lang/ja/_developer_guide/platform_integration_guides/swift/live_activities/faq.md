---
nav_title: FAQ
article_title: ライブアクティビティのよくある質問
page_order: 20
description: "このページでは、Swift SDK のライブアクティビティに関するよくある質問に対する回答を提供します。"
tool: Live Activities
platform:
  - iOS
---

# よくある質問

> この記事では、ライブ・アクティビティに関するよくある質問に対する回答を紹介する。

## 機能性とサポート

### ライブアクティビティをサポートしているプラットフォームは？

ライブアクティビティは現在、iOS 特有の機能です。ライブアクティビティの記事では、Braze Swift SDK を使用してライブアクティビティを管理するための[前提条件][2]について説明しています。

### React Nativeアプリはライブ・アクティビティをサポートしているか？

はい、React Native SDK 3.0.0 以降は、Braze Swift SDK 経由でライブアクティビティをサポートしています。つまり、Braze Swift SDK の上に直接 React Native iOS のコードを記述する必要があります。 

Apple が提供するライブアクティビティ機能は、JavaScript では翻訳不可能な言語 (例えば、Swift Concurrency、generics、SwiftUI) を使用しているため、ライブアクティビティ用の React Native 固有のJavaScript の便利な API は存在しません。

### Brazeはキャンペーンやキャンバスのステップとしてのライブ活動をサポートしているか？

いや、これは現在サポートされていない。

## プッシュ通知とライブ活動

### ライブ・アクティビティがアクティブな状態でプッシュ通知が送信された場合はどうなるのか？ 

![ブルズ対ベアーズのスポーツ中継が画面中央に、プッシュ通知 lorem ipsum のテキストが画面下部に表示された携帯電話の画面。][4]{: style="max-width:30%;float:right;margin-left:15px;"}

ライブアクティビティとプッシュ通知は、異なる画面領域を占有するため、ユーザーの画面上で競合することはありません。

### ライブ・アクティビティがプッシュ・メッセージ機能を活用する場合、ライブ・アクティビティを受信するためにプッシュ通知を有効にする必要があるか？

ライブアクティビティはプッシュ通知に依存して更新を行いますが、それらは異なるユーザー設定によってコントロールされています。ユーザーはライブアクティビティにオプトインできますが、プッシュ通知はオプトアウトでき、その逆も可能です。 

Apple では、ユーザーがアプリで何らかのアクション (注文など) を行ってライブアクティビティを開始することが必要です。このライブアクティビティトークンの有効期限は8時間です。 

### ライブアクティビティにはプッシュプライマーが必要ですか？

[プッシュプライマーは][1]、ユーザーにアプリからのプッシュ通知をオプトインするよう促すベストプラクティスです。しかし、ライブアクティビティにオプトインするためのシステムプロンプトはありません。iOS 16.1 以降にアップグレードすると、ユーザーはデフォルトでライブアクティビティにオプトインされます。

## 技術的な話題とトラブルシューティング

### ライブアクティビティにエラーがあるかどうかを知るには？

ライブアクティビティエラーは、Braze ダッシュボードの[メッセージアクティビティログ]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/)に記録されます。ここでは、「LiveActivity Errors」でフィルターできます。

### `live_activity/update` エンドポイントを使おうとすると、アクセス拒否応答が表示されます。なぜでしょう？

使用するAPIキーには、さまざまなBraze APIエンドポイントにアクセスするための適切なパーミッションを与える必要がある。以前に作成したAPIキーを使用している場合、その権限の更新を怠っている可能性がある。[API キーセキュリティの概要][3]を読んで再確認してください。

### `messages/send` エンドポイントは、`messages/live_activity/update` エンドポイントとレート制限を共有しているか？ 

デフォルトでは、`messages/live_activity/update` エンドポイントのレート制限は、ワークスペースごとに、複数のエンドポイントにわたって、1時間あたり250,000リクエストです。詳しくは \[API レート制限][5] を参照してください。

### なぜプッシュ・トゥ・スタートのトークンが生成されないのか？

iOS 17.2 以降から、Apple は `pushToStartToken` と `pushToStartTokenUpdates` API に制限を設けています。実際には、「push-to-start」トークンは、初回インストール後のアプリケーション `application(_:didFinishLaunchingWithOptions:)` での初回アプリ起動時にのみ生成されます。このステップを繰り返す必要がある場合、トークンはアプリを再起動して再インストールした後、または手動でそのライブ・アクティビティの新しいインスタンスを作成した後にのみ、再度生成することができる。

### トラブルシューティング中に他に気をつけるべきことは？

- 認証に`.p8` キーを使用していることを確認する。
- プッシュ・プロビジョニング・プロファイルがテストしている環境と一致していることを確認する。ユニバーサル証明書は、開発または実稼働の Apple Push Notification service (APNs) 環境のいずれかに送信するように Braze ダッシュボードで構成できます。実稼働アプリ用の開発証明書または開発アプリ用の実稼働証明書は動作しません。


[1]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/live_activities/live_activities/#prerequisites
[3]: {{site.baseurl}}/api/basics/#rest-api-key-security
[4]: {% image_buster /assets/img/push-vs-live-activities.png %}
[5]: {{site.baseurl}}/api/api_limits/