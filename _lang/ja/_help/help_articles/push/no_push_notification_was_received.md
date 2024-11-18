---
nav_title: プッシュ通知を受信しない
article_title: プッシュ通知を受信しない
page_order: 3

page_type: solution
description: "このヘルプ記事では、ユーザーがプッシュ通知を受け取らない場合のトラブルシューティング手順を説明する。"
channel: push
---
# プッシュ通知を受信しない

プッシュ通知での配信に課題を感じているか？以下の点を確認してこの問題のトラブルシューティングを行うためのステップがいくつかあります。

* [プッシュ通知のサブスクリプションのステータス](#push-subscription-status)
* [セグメント](#segment)
* [プッシュ通知上限](#push-notification-caps)
* [レート制限](#rate-limits)
* [コントロールグループステータス](#control-group-status)

### プッシュ通知のサブスクリプションのステータス

**ユーザープロファイル**セクションの[Engagement][1]タブでユーザープロファイルを確認し、テストしているワークスペースのプッシュにアクティブに登録されているかどうかを確認します。複数のアプリに登録している場合は、「**Push Registered For**」フィールドに表示される：

![登録済みのプッシュ通知][2]

Brazeエクスポートエンドポイントを使用してユーザープロファイルをエクスポートすることもできる：
- [識別子によるユーザー][12]
- [セグメント別ユーザー][13]

どちらのエンドポイントも、デバイスごとのプッシュ有効化情報を含むプッシュトークンオブジェクトを返す。

### セグメント

テストではなく本番のキャンペーンの場合）ターゲットにしているセグメントに該当することを確認する。**ユーザープロフィールでは**、ユーザーが現在属しているセグメントのリストが表示される。セグメンテーションはリアルタイムで更新されるため、これは常に変化する変数であることに注意してください。

![セグメント一覧][3]

### プッシュ通知上限

グローバル周波数の上限を確認します。ワークスペースにグローバル頻度上限が設定されており、指定された時間枠のプッシュ通知上限をすでに超えているため、プッシュ通知を受け取れなかった可能性がある。

これは、ダッシュボードで[global frequency capping][4] ]をチェックすることでできる。キャンペーンがフリークエンシー・キャッピング・ルールに従うように設定されている場合、これらの設定によって影響を受けるユーザーが多数存在する。

![キャンペーン詳細][5]

### レート制限

キャンペーンまたはキャンバスにレート制限が設定されている場合、この制限を超過したためにメッセージングを受信できなくなる可能性があります。詳細については、[レート制限][9] を参照してください。

### コントロールグループステータス

これが単一チャンネルのキャンペーンや、コントロールグループのあるキャンバスであれば、コントロールグループに属している可能性がある。

  1. [バリアントの分布][6] をチェックして、コントロールグループがあるかどうかを確認します。
  2. ある場合は、[キャンペーンのコントロールグループ内][7] にセグメントフィルターを作成し、[セグメントをエクスポート][8] して、ユーザー ID がこの一覧に含まれているかどうかを確認します。

### 有効なプッシュトークン
プッシュトークンは、送信者がプッシュ通知を持つ特定の機器を対象にするために使用する識別子です。つまり、デバイスが有効なプッシュトークンを持っていなければ、そのデバイスにプッシュ通知を送ることはできない。 

### プッシュ通知タイプ

正しい種類のプッシュ通知を使用しているか確認する。例えば、FireTVをターゲットにしたい場合は、Androidのプッシュ・キャンペーンではなく、Kindleのプッシュ通知を使うことになる。Brazeのワークフローを理解するための詳細については、以下の記事をチェックしてほしい：
- [Appleプッシュ通知]][10]
- [Firebase クラウドメッセージング][11]

それでもサポートが必要な場合は、[サポートチケットを]({{site.baseurl}}/braze_support/)を登録してください。

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