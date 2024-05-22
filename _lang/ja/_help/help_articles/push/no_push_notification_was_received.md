---
nav_title: プッシュ通知の欠落
article_title: プッシュ通知の欠落
page_order: 3

page_type: solution
description: "このヘルプ記事では、ユーザがプッシュ通知を受信していない場合に実行できるトラブルシューティング手順について説明します。"
channel: push
---
# プッシュ通知がありません

プッシュ通知で配信の課題を経験していますか?この問題をトラブルシューティングするには、次の手順を実行します。

* [プッシュサブスクリプションステータス](#push-subscription-status)
* [セグメント](#segment)
* [プッシュ通知キャップ](#push-notification-caps)
* [レート制限](#rate-limits)
* [コントロールグループのステータス](#control-group-status)

### プッシュサブスクリプションステータス

**User Profile**セクションの[Engagement][1]タブでユーザープロファイルを確認し、テストしているワークスペースにプッシュ用にアクティブに登録されているかどうかを確認します。複数のアプリに登録されている場合は、**Push Registered For**に表示されます。 field:

![登録を押してください][2]

ブレーズエクスポートエンドポイントを使用して、ユーザープロファイルをエクスポートすることもできます。
\- [識別子によるユーザ][12]
\- [セグメント別利用者数][13]

どちらのエンドポイントも、デバイスごとにプッシュ有効化情報を含むプッシュトークンオブジェクトを返します。

### セグメント

ターゲットとするセグメントに属していることを確認します(これがテストではなくライブキャンペーンの場合)。**User Profile**には、現在ユーザが属しているセグメントのリストが表示されます。セグメンテーションがリアルタイムで更新されるため、これは常に変化する変数であることを覚えておいてください。

![セグメント一覧][3]

### プッシュ通知キャップ

グローバル周波数の上限を確認します。ワークスペースにはグローバル周波数上限が設定されており、指定した時間枠のプッシュ通知上限をすでに満たしているため、プッシュ通知を受信しなかった可能性があります。

これを行うには、ダッシュボードで[グローバル周波数上限][4] をチェックします。キャンペーンが周波数制限ルールに従うように設定されている場合、これらの設定によって影響を受けるユーザが多数存在します

![キャンペーン詳細][5]

### レート制限

キャンペーンまたはキャンバスにレート制限が設定されている場合は、この制限を超過したためにメッセージを受信できなくなっている可能性があります。詳細は、[レートリミット][9]を参照してください。

### コントロールグループのステータス

これが単一のチャンネルキャンペーンまたはコントロールグループを持つキャンバスの場合、コントロールグループに分類される可能性があります。

  1. [variant distribution][6] をチェックして、コントロールグループがあるかどうかを確認します。
  2. その場合は、[campaign control group][7] で[segment filtering] を作成し、[export the segment][8] を実行して、ユーザID がこのリストにあるかどうかを確認します。

### 有効なプッシュトークン
プッシュトークンは、送信者がプッシュ通知を使用して特定のデバイスをターゲットにするために使用する識別子です。そのため、デバイスに有効なプッシュトークンがない場合、プッシュ通知を送信する方法はありません。 

### プッシュ通知タイプ

正しいタイプのプッシュ通知を使用していることを確認します。たとえば、FireTV をターゲットにする場合は、Android プッシュキャンペーンではなくKindle プッシュ通知を使用します。以下の記事を参照して、Braze ワークフローの理解の詳細を確認してください。
\- [Apple プッシュ通知][10]
\- [Firebaseクラウドメッセージング][11]

それでも助けが必要ですか?[サポートチケット]({{site.baseurl}}/braze_support/)を開きます。

_最終更新日2021年1月21日_

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