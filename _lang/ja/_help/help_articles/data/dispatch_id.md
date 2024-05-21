---
nav_title: ディスパッチIDの動作
article_title: ディスパッチIDの動作
page_order: 0

page_type: solution
description: "このヘルプ記事では、ディスパッチID の使用法、影響、および制限を含むディスパッチID の動作について説明します。"
---

# ディスパッチIDの動作

`dispatch_id` はメッセージディスパッチのID で、各"transmission" の一意のID です。Braze から送信されます。スケジュールされたメッセージを送信したユーザは、同じ`dispatch_id` を受け取ります。通常、アクションベースまたはAPI トリガのメッセージは、ユーザごとに一意の`dispatch_id` を受け取りますが、別のユーザに近接して送信されたメッセージは、複数のユーザ間で同じ`dispatch_id` を共有する場合があります。

これにより、メッセージが2 つの異なる時間に送信された場合、2 つの異なるユーザが1 つのキャンペーンに対して異なるディスパッチID を持つことになります。これは、多くの場合、API 要求が個別に行われたためです。両方のユーザが1 回の送信で同じキャンペーンオーディエンスにいる場合、そのディスパッチID は同じになります。

## キャンペーンでのディスパッチID の動作

スケジュールされたキャンペーンメッセージは、同じ`dispatch_id` になります。アクションベースまたはAPI トリガのキャンペーンメッセージは、ユーザごとに一意の`dispatch_id` を取得することができます。または、`dispatch_id` は、上で説明したように、近くにあるか、同じAPI コールで送信された場合、複数のユーザに対して同じになることがあります。たとえば、スケジュールされたキャンペーンオーディエンスの2 人のユーザは、キャンペーンがスケジュールされるたびに同じ`dispatch_id` を持ちます。ただし、API トリガーキャンペーンのオーディエンスの2 人のユーザは、別々のAPI コールで送信され、互いに近接していない場合、異なるディスパッチID を持つ可能性があります。

マルチチャネルキャンペーンは、配信タイプで説明されているものと同じ動作を持ちます。

{% alert warning %}
キャンバスステップが"scheduled" であっても、キャンバスステップはトリガーされたイベントとして扱われるため、`dispatch_id` はすべてのキャンバスステップに対してランダムに生成されます。これにより、ID の生成に不整合が生じる可能性があります。キャンバスコンポーネントには、送信ごとにユーザごとに一意の`dispatch_id`が含まれる場合や、送信ごとにユーザ間の共有ディスパッチIDが含まれる場合があります。
{% endalert %}

## Template dispatch ID をLiquid でメッセージに送信する

(URL などで) メッセージ内からのメッセージの配信を追跡する場合は、`dispatch_id` 内のテンプレートを使用できます。この書式設定は、[サポートされているパーソナライゼーションタグ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/) のリストの「Canvas Attributes」にあります。

これは、`api_id` と同じように動作します。つまり、`api_id` はキャンペーンの作成時に使用できないため、プレースホルダとしてテンプレート化され、`dispatch_id_for_unsent_campaign` としてプレビューされます。ID はメッセージが送信される前に生成され、送信時間として含まれます。

{% alert warning %}
アプリ内メッセージに`dispatch_id_for_unsent_campaign` は`dispatch_id` がないため、`dispatch_id_for_unsent_campaign` の液体テンプレートはアプリ内メッセージでは機能しません。
{% endalert %}

## メールのDispatch ID Currents フィールド

Currents 機能を引き続き強化するための努力で、`dispatch_id` は、すべてのコネクタタイプにわたるCurrents メールイベントのフィールドでもあります。`dispatch_id` は、Braze プラットフォームから送信される各送信またはディスパッチに対して生成される一意のID です。

スケジュールされたメッセージを送信されたすべての顧客は同じ`dispatch_id` を取得しますが、アクションベースまたはAPI トリガのいずれかのメッセージを受信する顧客は、メッセージごとに一意の`dispatch_id` を取得します。`dispatch_id` フィールドを使用すると、定期的なキャンペーンのどのインスタンスが変換を担当しているかを識別できるため、どのタイプのキャンペーンがビジネス目標の達成に役立っているかについて、より多くの洞察と情報を得ることができます。

`dispatch_id` を[personalization tag]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#supported-personalization-tags)、[メッセージエンゲージメントイベント]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/message_engagement_events/)、または[Segment]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment_for_currents/#integration-details)、[Mixpanel]({{site.baseurl}}/partners/insights/behavioral_analytics/mixpanel_for_currents/#email-events)、または[Amplitude]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/amplitude/amplitude_for_currents/) をCurrents に使用できます。

_最終更新日2021年7月15日_
