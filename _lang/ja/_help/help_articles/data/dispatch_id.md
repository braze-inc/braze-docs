---
nav_title: ディスパッチIDの動作
article_title: ディスパッチIDの動作
page_order: 0

page_type: solution
description: "このヘルプ記事では、ディスパッチID の使用法、影響、および制限を含むディスパッチID の動作について説明します。"
---

# ディスパッチIDの動作

`dispatch_id` は、メッセージディスパッチのID - それぞれの"transmission" Brazeから送信される一意のID です。スケジュールされたを送信したユーザは、同じ`dispatch_id` を受け取ります。通常、アクション ベースまたはAPI-トリガーメッセージ s はユーザーごとに一意の`dispatch_id` を受け取りますが、別の近くで送信されたメッセージは、複数のユーザーs 間で同じ`dispatch_id` を共有する場合があります。

これにより、2 つの異なる時刻にメッセージが送信された場合、2 つの異なるユーザーが1 つのキャンペーンに対して異なるディスパッチID を持つことになります。これは、多くの場合、API 要求が個別に行われたためです。両方のユーザーs が1 回の送信で同じキャンペーン オーディエンスにあった場合、ディスパッチID は同じになります。

## キャンペーン s でのディスパッチID の動作

スケジュールされたキャンペーンは、同じ`dispatch_id` になります。アクションベースまたはAPI-トリガーのed キャンペーンは、ユーザーごとに一意の`dispatch_id`を取得できます。または、前述のように、近くにあるか、同じAPI 呼び出しで送信された場合、`dispatch_id` は、複数のユーザーで同じになる場合があります。たとえば、スケジュールされた キャンペーン オーディエンス内の2 つのユーザーs は、キャンペーンがスケジュールされたされるたびに同じ`dispatch_id` を持ちます。ただし、API-トリガー ed キャンペーンのオーディエンスの2 つのユーザーs は、別々のAPI 呼び出しで送信され、互いに近接していない場合、別々のディスパッチID を持つことがあります。

Multi チャネル キャンペーン s は、配信種別で説明されているものと同じ動作を持ちます。

{% alert warning %}
すべてのキャンバスステップs に対して`dispatch_id` がランダムに生成されます。これは、Braze では、キャンバスステップs が"スケジュールされた" であっても、トリガーのed イベントとして扱われるためです。これにより、ID の生成に不整合が生じる可能性があります。場合によっては、キャンバスコンポーネントは、送信ごとのユーザーごとに一意の`dispatch_id` を持つか、または送信ごとにユーザー間で共有ディスパッチID を持つことがあります。
{% endalert %}

## Template dispatch ID をLiquid でメッセージに送信する

(URL などで) メッセージ内からのメッセージの配信を追跡する場合は、`dispatch_id` をテンプレートできます。このための書式設定は、[サポートされているパーソナライゼーション タグs]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/) の一覧にあります。

これは`api_id` と同じように動作します。この場合、`api_id` はキャンペーン作成時には使用できないため、プレースホルダとしてd がテンプレートされ、`dispatch_id_for_unsent_campaign` としてプレビューされます。ID はメッセージが送信される前に生成され、送信時間として含まれます。

{% alert warning %}
アプリ内メッセージ には`dispatch_id` がないため、`dispatch_id_for_unsent_campaign` のリキッドテンプレートはアプリ内メッセージ s では機能しません。
{% endalert %}

## メールのディスパッチ識別Currents フィールド

Currents機能を引き続き強化するために、`dispatch_id` は、すべてのコネクタータイプのCurrents メール事象のフィールドでもあります。`dispatch_id` は、Braze プラットフォームから送信される送信またはディスパッチごとに生成される一意のID です。

送信されたすべての顧客 s が同じ`dispatch_id` をスケジュールされたしますが、アクション ベースまたはAPI-トリガーメッセージ s を受信した顧客 s は、メッセージごとに一意の`dispatch_id` を取得します。`dispatch_id` フィールドを使用すると、定期的なキャンペーンのどのインスタンスがコンバージョンを担当しているかを識別できるため、より多くのインサイトと、どのタイプのキャンペーンが業務目標の達成に役立っているかを確認できます。

`dispatch_id` を[パーソナライゼーション タグ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#supported-personalization-tags)、[メッセージエンゲージメントイベント]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/message_engagement_events/)、または[Segment]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment_for_currents/#integration-details)、[Mixpanel]({{site.baseurl}}/partners/insights/behavioral_analytics/mixpanel_for_currents/#email-events)、または[Amplitude]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/amplitude/amplitude_for_currents/) をCurrentsに使用できます。

_2021更新7月15日昨日d_
