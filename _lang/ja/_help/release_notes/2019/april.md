---
nav_title: 4月
page_order: 9
noindex: true
page_type: update
description: "この記事には2019年4月のリリースノートが含まれている。"
---

# 2019年4月

## 百花繚乱のイベント＆フィールド

セクションのいくつかの修正に加え、新しい\[サブスクリプション・イベント]({{ site.baseurl}}/user_guide/data_and_analytics/braze_currents/message_engagement_events/#subscription-events) )がメッセージ・エンゲージメント・イベント・ページに追加された。 

サブスクリプショングループの状態変化データを、Brazeから[セグメンテーションと]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment_for_currents/#integration-details) [mParticleに]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/mParticle/mparticle_for_currents/)エクスポートできるようになった。

さらに、利用可能な[コンバージョンイベントに]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/message_engagement_events/#conversion-events)プロパティ（`canvas_step_id` ）が追加された。

{% alert important %}
これらの更新を利用するには、Currentsコネクタ設定を編集し、使用したいイベントをイネーブルメントにする必要がある。ご不明な点があれば、アカウントマネージャーにご相談を。
{% endalert %}

## サブスクリプショングループのアーカイブ化

[サブスクリプショングループをアーカイブ]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#archiving-groups)できるようになった！アーカイブされたサブスクリプショングループは編集できず、セグメンテーションフィルターにも表示されなくなる。 メール、キャンペーン、キャンバスでセグメンテーションフィルターとして使用されているグループをアーカイブしようとすると、エラーメッセージが表示され、そのグループの使用をすべて削除するまでアーカイブできない。
