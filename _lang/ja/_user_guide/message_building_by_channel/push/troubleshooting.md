---
nav_title: トラブルシューティング
article_title: トラブルシューティング
page_order: 23
page_type: reference
description: "このページでは、Pushメッセージングチャネルに関するさまざまな問題のトラブルシューティングステップを紹介する。"
channel: push
---

# トラブルシューティング

> このページは、Pushメッセージングチャネルで発生する可能性のあるさまざまな問題のトラブルシューティングに役立つ。

## プッシュ通知を受信しない

プッシュ通知での配信に課題を感じているか？以下の点を確認してこの問題のトラブルシューティングを行うためのステップがいくつかあります。

- [プッシュ通知のサブスクリプションのステータス](#push-subscription-status)
- [セグメント](#segment)
- [プッシュ通知上限](#push-notification-caps)
- [レート制限](#rate-limits)
- [コントロールグループステータス](#control-group-status)
- [有効なプッシュトークン](#valid-push-token)
- [プッシュ通知タイプ](#push-notification-type)
- [現在のアプリ](#current-app)

#### プッシュ通知のサブスクリプションのステータス

プッシュは、サブスクライバーまたはオプトインしたユーザーにのみ送信できる。**ユーザー**プロファイル[]セクションの[エンゲージメント]][1]タブでユーザープロファイルを確認し、テスト対象のワークスペースでアクティブにプッシュ登録されているかどうかを確認する。複数のアプリに登録している場合は、「**Push Registered For**」フィールドにリストアップされる：

![登録済みのプッシュ通知][2]

Brazeエクスポートエンドポイントを使用してユーザープロファイルをエクスポートすることもできる：
- [識別子によるユーザー][12]
- [セグメント別ユーザー][13]

どちらのエンドポイントも、デバイスごとのプッシュ有効化情報を含むプッシュトークンオブジェクトを返す。

#### セグメント

テストではなく本番のキャンペーンの場合）ターゲットにしているセグメントに該当することを確認する。**ユーザープロフィールでは**、ユーザーが現在属しているセグメントのリストが表示される。セグメンテーションはリアルタイムで更新されるため、これは常に変化する変数であることに注意してください。

![セグメント一覧][3]

また、セグメンテーションを作成する際に、**User Lookupを**使用することで、ユーザーがセグメンテーションの一部であることを確認することができる。

![検索フィールドを備えたユーザー検索セクション。][14]{: style="max-width:80%;"}

#### プッシュ通知上限

グローバル周波数の上限を確認します。ワークスペースにグローバル頻度上限が設定されており、指定された時間枠のプッシュ通知上限をすでに超えているため、プッシュ通知を受け取れなかった可能性がある。

これは、ダッシュボードで[global frequency capping][4] ]をチェックすることでできる。キャンペーンがフリークエンシー・キャッピング・ルールに従うように設定されている場合、これらの設定によって影響を受けるユーザーが多数存在する。

![キャンペーン詳細][5]

#### レート制限

キャンペーンまたはキャンバスにレート制限が設定されている場合、この制限を超過したためにメッセージングを受信できなくなる可能性があります。詳細については、[レート制限][9] を参照してください。

#### コントロールグループステータス

これが単一チャンネルのキャンペーンや、コントロールグループのあるキャンバスであれば、コントロールグループに属している可能性がある。

  1. [バリアントの分布][6] をチェックして、コントロールグループがあるかどうかを確認します。
  2. ある場合は、[キャンペーンのコントロールグループ内][7] にセグメントフィルターを作成し、[セグメントをエクスポート][8] して、ユーザー ID がこの一覧に含まれているかどうかを確認します。

#### 有効なプッシュトークン
プッシュトークンは、送信者がプッシュ通知を持つ特定の機器を対象にするために使用する識別子です。つまり、デバイスが有効なプッシュトークンを持っていなければ、そのデバイスにプッシュ通知を送ることはできない。 

#### プッシュ通知タイプ

正しい種類のプッシュ通知を使用しているか確認する。例えば、FireTVをターゲットにしたい場合は、Androidのプッシュ・キャンペーンではなく、Kindleのプッシュ通知を使うことになる。同様に、Androidをターゲットにしたい場合は、iOSのプッシュキャンペーンではなく、Androidのプッシュ通知を使う。Brazeのワークフローを理解するための詳細については、以下の記事をチェックしてほしい：
- [Appleプッシュ通知]][10]
- [Firebase クラウドメッセージング][11]

#### 現在のアプリ

内部ユーザーでプッシュ通知をテストする場合、プッシュ通知を受け取りたいユーザーが現在関連アプリにログインしていることを確認する。これは、ユーザーがプッシュを受け取らなかったり、セグメンテーションされていないと思われるプッシュを受け取ったりすることにつながる。

それでもサポートが必要な場合は、[サポートチケットを]({{site.baseurl}}/braze_support/)を登録してください。

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
[11]: {{site.baseurl}}/developer_guide/platforms/android/push_notifications/troubleshooting/
[12]: {{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier
[13]: {{site.baseurl}}/api/endpoints/export/user_data/post_users_segment
[14]: {% image_buster /assets/img_archive/user_lookup.png %}