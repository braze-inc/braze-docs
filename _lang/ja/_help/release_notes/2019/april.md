---
nav_title: 4月
page_order: 9
noindex: true
page_type: update
description: "この記事には2019年4月のリリースノートが含まれている。"
---

# 2019年4月

## 百花繚乱のイベント＆フィールド

セクションのいくつかの修正に加え、新しい \[購読イベント]({{ site.baseurl}}/user_guide/data_and_analytics/braze_currents/message_engagement_events/#subscription-events) )がメッセージ・エンゲージメント・イベント・ページに追加された。 

Brazeから[Segment]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment_for_currents/#integration-details)および[mParticle]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/mParticle/mparticle_for_currents/)にサブスクリプショングループの状態変更データをエクスポートできるようになりました。また、[Mixpanel]({{site.baseurl}}/partners/insights/behavioral_analytics/mixpanel_for_currents)でインストールアトリビューションイベントもエクスポートできます。

さらに、利用可能な[コンバージョンイベントに]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/message_engagement_events/#conversion-events)プロパティ`canvas_step_id` が追加された。

{% alert important %}
これらのアップデートを利用するには、Currentsコネクタの設定を編集し、使用したいイベントを有効にする必要がある。ご不明な点があれば、担当のアカウント・マネージャーにお問い合わせいただきたい。
{% endalert %}

## 購読グループのアーカイブ

[購読グループをアーカイブ]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#archiving-groups)できるようになった！アーカイブされた購読グループは編集できず、セグメントフィルターに表示されなくなる。 メール、キャンペーン、キャンバスでセグメントフィルターとして使用されているグループをアーカイブしようとすると、エラーメッセージが表示され、そのグループの使用をすべて削除するまでアーカイブできない。
