---
nav_title: 4月
page_order: 9
noindex: true
page_type: update
description: "この記事には、2019 年 4 月のリリースノートが含まれています。"
---

# 2019 年 4 月

## Currentsの新しいイベントとフィールド

セクションへのいくつかの修正に加えて、新しい [サブスクリプションイベント] ({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/message_engagement_events/#subscription-events) has been added to the Message Engagement Events page. 

[[サブスクリプショングループの状態変更データをBrazeからSegmentとmParticleにエクスポートできるようになりました]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/mParticle/mparticle_for_currents/)]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment_for_currents/#integration-details)[。また、Mixpanelにアトリビューションイベントをインストールすることもできます。]({{site.baseurl}}/partners/insights/behavioral_analytics/mixpanel_for_currents)

さらに、`canvas_step_id`[このプロパティは利用可能なコンバージョンイベントに追加されました]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/message_engagement_events/#conversion-events)。

{% alert important %}
これらの更新を利用するには、Currents コネクタの設定を編集し、使用するイベントを有効にする必要があります。ご不明な点がございましたら、アカウントマネージャーにお問い合わせください。
{% endalert %}

## 購読グループのアーカイブ

[サブスクリプショングループをアーカイブできるようになりました]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#archiving-groups)！アーカイブされたサブスクリプショングループは編集できず、セグメントフィルターに表示されなくなります。 電子メール、キャンペーン、またはキャンバスでセグメントフィルターとして使用されているグループをアーカイブしようとすると、すべての使用を削除するまでグループをアーカイブできないというエラーメッセージが表示されます。
