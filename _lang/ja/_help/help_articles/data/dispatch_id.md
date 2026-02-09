---
nav_title: ディスパッチ ID の動作
article_title: ディスパッチ ID の動作
page_order: 0

page_type: solution
description: "このヘルプ記事では、用途、影響、制限を含むディスパッチ ID の動作について説明します。"
---

# ディスパッチ ID の動作

`dispatch_id` はメッセージディスパッチの ID で、Braze から送信される各「送信」に固有の ID です。スケジュールされたメッセージが送信されたユーザーには、同じ `dispatch_id` が割り当てられます。通常、アクションベースメッセージや API トリガーメッセージには、ユーザーごとに一意の`dispatch_id` が割り当てられますが、別のユーザーに近接して送信されたメッセージでは、複数のユーザー間で同じ `dispatch_id` が共有される場合があります。

これにより、2 つの異なる時刻にメッセージが送信された場合、2 つの異なるユーザーが1 つのキャンペーンに対して異なるディスパッチID を持つことになります。これは、多くの場合、API 要求が個別に行われたためです。両方のユーザーが 1 回の送信で同じキャンペーンオーディエンスに含まれていた場合、ディスパッチ ID は同じになります。

## キャンペーンでのディスパッチ ID の動作

スケジュールされたキャンペーンメッセージの `dispatch_id` は同じになります。アクションベースキャンペーンや API トリガーキャンペーンには、ユーザーごとに一意の`dispatch_id` が割り当てられます。また、前述のように、近接範囲内または同一の API 呼び出しで送信された場合は、複数のユーザーの `dispatch_id` が同じになる場合もあります。例えば、スケジュールされたキャンペーンオーディエンス内の2人のユーザーには、キャンペーンがスケジュールされたされるたびに同じ `dispatch_id` が割り当てられます。ただし、API トリガーキャンペーンのオーディエンスに含まれる2人のユーザーは、別々の API 呼び出しで送信され、互いに近接していない場合、別々のディスパッチ ID が割り当てられることがあります。

マルチチャネルキャンペーンの動作は、配信タイプの説明と同じになります。

{% alert warning %}
Braze は、キャンバスステップが「スケジュール」されている場合でもキャンバスステップをトリガーされたイベントとして扱うため、すべてのキャンバスステップに対して `dispatch_id` がランダムに生成されます。これにより、ID の生成に不整合が生じる可能性があります。キャンバスコンポーネントには各送信でユーザーごとに一意の `dispatch_id` が割り当てられることもあれば、各送信においてユーザー間でディスパッチ ID が共有されることもあります。
{% endalert %}

## Liquid でディスパッチ ID をメッセージにテンプレート化する

(URL などで) メッセージ内からのメッセージのディスパッチを追跡する場合は、`dispatch_id` でテンプレート化できます。このための書式設定は、「[サポートされているパーソナライゼーションタグ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/)」の一覧の [キャンバスの属性] で確認できます。

これは、`api_id` と同じように動作します。つまり、`api_id` はキャンペーンの作成時に使用できないため、プレースホルダとしてテンプレート化され、`dispatch_id_for_unsent_campaign` としてプレビューされます。ID はメッセージが送信される前に生成され、送信時間として含まれます。

{% alert warning %}
アプリ内メッセージには `dispatch_id` がないため、`dispatch_id_for_unsent_campaign` の Liquid テンプレート化はアプリ内メッセージでは機能しません。
{% endalert %}

## メールのディスパッチ ID Currents フィールド

Currents の機能を継続的に強化する取り組みの一環として、すべてのコネクタータイプで `dispatch_id` は Currents のメールイベントにおけるフィールドにもなっています。`dispatch_id` は、Braze プラットフォームからの送信 (ディスパッチ) ごとに生成される一意の ID です。

スケジュール済みのメッセージを受信したすべての顧客に同じ `dispatch_id` が割り当てられますが、アクションベースメッセージや API トリガーメッセージを受信した顧客にはメッセージごとに固有の `dispatch_id` が割り当てられます。`dispatch_id` フィールドを使用すると、定期的なキャンペーンのどのインスタンスがコンバージョンを担当しているかを識別できるため、より多くのインサイトと、どのタイプのキャンペーンが業務目標の達成に役立っているかを確認できます。

`dispatch_id` を[パーソナライゼーション タグ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#supported-personalization-tags)、[メッセージエンゲージメントイベント]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/)、または[Segment]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment_for_currents/#integration-details)、[Mixpanel]({{site.baseurl}}/partners/insights/behavioral_analytics/mixpanel_for_currents/#email-events)、または[Amplitude]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_for_currents/) をCurrentsに使用できます。

_最終更新日：2021年7月15日_
