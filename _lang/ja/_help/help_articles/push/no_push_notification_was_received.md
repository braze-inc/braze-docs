---
nav_title: プッシュ通知の欠落
article_title: プッシュ通知の欠落
page_order: 3

page_type: solution
description: "このヘルプ記事では、ユーザーがプッシュ通知を受け取らない場合のトラブルシューティングのステップを説明する。"
channel: push
---
# プッシュ通知の欠落

プッシュ通知の配信に課題を感じている？この問題を解決するために、いくつかのステップを踏むことができる：

* [サブスクリプションのステータスをプッシュする](#push-subscription-status)
* [セグメント](#segment)
* [プッシュ通知キャップ](#push-notification-caps)
* [レート制限](#rate-limits)
* [コントロールグループのステータス](#control-group-status)

### サブスクリプションのステータスをプッシュする

ユーザープロファイ**ル**]セクションの[\[エンゲージメント]][1]タブでユーザープロファイルを確認し、テスト対象のワークスペースでアクティブにプッシュ登録されているかどうかを確認する。複数のアプリに登録している場合は、「**Push Registered For**」フィールドにそれらのアプリが表示される：

![プッシュ登録][2]

Brazeエクスポートエンドポイントを使ってユーザープロファイルをエクスポートすることもできる：
- \[識別子によるユーザー][12]
- \[セグメント別ユーザー数][13]

どちらのエンドポイントも、デバイスごとのプッシュイネーブルメント情報を含むプッシュトークンオブジェクトを返す。

### セグメント

ターゲットにしているセグメンテーションに該当していることを確認する（テストではなく本番キャンペーンの場合）。**ユーザープロファイルでは**、ユーザーが現在属しているセグメンテーションのリストが表示される。セグメンテーションはリアルタイムで更新されるため、これは常に変化する変数であることを忘れてはならない。

![セグメンテーション一覧][3]

### プッシュ通知キャップ

グローバル・フリークエンシー・キャップをチェックする。ワークスペースにグローバルフリークエンシーキャップが設定されており、指定された時間枠のプッシュ通知キャップにすでに達しているため、プッシュ通知を受け取れなかった可能性がある。

これは、ダッシュボードで\[グローバル・フリークエンシーキャップ][4] ] をチェックすることで可能だ。キャンペーンがフリークエンシーキャップルールに従うように設定されている場合、これらの設定によって影響を受けるユーザーが多数存在する。

![キャンペーン詳細][5]

### レート制限

キャンペーンやキャンバスにレート制限を設定している場合、この制限を超えたためにメッセージングの受信から外れてしまう可能性がある。詳しくは「レート制限][9] 」を参照のこと。

### コントロールグループのステータス

これがシングルチャネルのキャンペーンや、コントロールグループのあるキャンバスであれば、コントロールグループに属している可能性がある。

  1. バリアント分布][6] 、コントロールグループがあるかどうかを確認する。
  2. もしそうなら、\[キャンペーンコントロールグループ][7] で]セグメントフィルターを作成し、\[セグメント][8] をエクスポートし、ユーザーIDがこのリストにあるかどうかをチェックする。

### 有効なプッシュトークン
プッシュトークンは、送信者が特定のデバイスにプッシュ通知を行うための識別子である。つまり、デバイスが有効なプッシュトークンを持っていなければ、そのデバイスにプッシュ通知を送ることはできない。 

### プッシュ通知タイプ

正しい種類のプッシュ通知を使用しているか確認する。例えば、FireTVをターゲットにしたいのであれば、Androidのプッシュキャンペーンではなく、Kindleのプッシュ通知を使うことになる。Brazeのワークフローを理解するための詳細は、以下の記事を参照されたい：
- \[Appleプッシュ通知][10]
- \[Firebaseクラウドメッセージング][11]

まだ助けが必要か？[サポートチケットを]({{site.baseurl}}/braze_support/)開封する。

_最終更新日：2021年1月21日_

[1]: {{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/#engagement-tab
[2]: {% image_buster /assets/img_archive/trouble1.png %}
[3]: {% image_buster /assets/img_archive/trouble2.png %}
[4]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#freq-cap-feat-over
[5]: {% image_buster /assets/img_archive/trouble3.png %}
[6]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing/#step-5-distribute-users-among-your-variants
[7]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/#in-campaign-control-group-filter
[8]: {{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/segment_data_to_csv/#exporting-to-csv
[9]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#rate-limiting
[10]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/troubleshooting/
[11]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/troubleshooting
[12]: {{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier
[13]: {{site.baseurl}}/api/endpoints/export/user_data/post_users_segment