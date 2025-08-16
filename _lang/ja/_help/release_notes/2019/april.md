---
nav_title: 4月
page_order: 9
noindex: true
page_type: update
description: "この記事には2019年4月のリリースノートが含まれている。"
---

# 2019年4月

## Currents の新しいイベントとフィールド

セクションの一部修正に加えて、新しい [サブスクリプションイベント]({{ site.baseurl}}/user_guide/data_and_analytics/braze_currents/message_engagement_events/#subscription-events) が [メッセージエンゲージメントイベント] ページに追加されました。 

サブスクリプショングループの状態変更データを、Braze から [Segment]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment_for_currents/#integration-details) と [mParticle]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/mParticle/mparticle_for_currents/)、および [Mixpanel]({{site.baseurl}}/partners/data_and_analytics/analytics/mixpanel/) のそのイベントとインストールアトリビューションイベントにエクスポートできるようになりました。

また、利用可能な[コンバージョンイベント]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/message_engagement_events/#conversion-events)にプロパティ`canvas_step_id`が追加されました。

{% alert important %}
これらの更新を活用するには、Currents コネクターの設定を編集し、使用するイベントを有効にする必要があります。ご不明な点があれば、担当のアカウント・マネージャーにお問い合わせいただきたい。
{% endalert %}

## サブスクリプショングループのアーカイブ

これで[アーカイブサブスクリプショングループ]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#archiving-groups)が可能になりました!アーカイブされたサブスクリプショングループは編集できず、セグメントフィルターに表示されなくなります。 メール、キャンペーン、キャンバスでセグメントフィルターとして使用されているグループをアーカイブしようとすると、エラーメッセージが表示され、そのグループの使用をすべて削除するまでアーカイブできない。
