---
nav_title: ディスパッチIDの動作
article_title: ディスパッチIDの動作
page_order: 0

page_type: solution
description: "このヘルプ記事では、使用法、影響、および制限を含むディスパッチIDの動作について説明します。"
---

# ディスパッチIDの動作

`dispatch_id`はメッセージ配信のIDであり、Brazeから送信される各「送信」の一意のIDです。スケジュールされたメッセージが送信されたユーザーは、同じ`dispatch_id`を受け取ります。通常、アクションベースまたはAPIトリガーのメッセージはユーザーごとに一意の`dispatch_id`を受け取りますが、他のメッセージと近接して送信されたメッセージは複数のユーザー間で同じ`dispatch_id`を共有する場合があります。

これは、メッセージが異なる時間に送信された場合、単一のキャンペーンに対して異なるディスパッチIDを持つ2人の異なるユーザーが存在する可能性があることを意味します。これは、多くの場合、APIリクエストが別々に行われたためです。両方のユーザーが同じ{キャンペーン}オーディエンスに単一の送信で含まれていた場合、彼らの配信IDは同じになります。

## キャンペーンにおけるディスパッチIDの動作

スケジュールされたキャンペーンメッセージは同じ`dispatch_id`を取得します。アクションベースまたはAPIトリガーのキャンペーンメッセージは、ユーザーごとに一意の`dispatch_id`を取得する場合や、上記のように近接して送信されたり同じAPI呼び出し内で送信されたりする場合に複数のユーザーで`dispatch_id`が同じになる場合があります。例えば、スケジュールされたキャンペーンのオーディエンスにいる2人のユーザーは、キャンペーンがスケジュールされるたびに同じ`dispatch_id`を持つことになります。ただし、API トリガー キャンペーンのオーディエンス内の 2 人のユーザーは、別々の API 呼び出しで送信され、互いに近接していない場合、異なるディスパッチ ID を持つことがあります。

マルチチャネルキャンペーンは、その配信タイプについて説明されているのと同じ動作をします。

{% alert warning %}
すべてのキャンバスステップに対して`dispatch_id`がランダムに生成されます。なぜなら、Brazeはキャンバスステップを「スケジュールされた」場合でもトリガーイベントとして扱うからです。これにより、IDの生成に不整合が生じる可能性があります。場合によっては、キャンバスコンポーネントは送信ごとにユーザーごとに一意の`dispatch_id`を持つこともあれば、送信ごとにユーザー間で共有されるディスパッチIDを持つこともあります。
{% endalert %}

## メッセージにLiquidを使用してテンプレートディスパッチID

メッセージ内からメッセージの送信を追跡したい場合（たとえば、URL内など）、`dispatch_id`にテンプレートを使用できます。この書式設定は、キャンバス属性の下にある[サポートされているパーソナライゼーションタグ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/)のリストにあります。

これはちょうど`api_id`のように動作します。つまり、`api_id`はキャンペーン作成時には利用できないため、プレースホルダーとしてテンプレート化され、`dispatch_id_for_unsent_campaign`としてプレビューされます。IDはメッセージが送信される前に生成され、送信時に含まれます。

{% alert warning %}
Liquidのテンプレート`dispatch_id_for_unsent_campaign`はアプリ内メッセージでは機能しません。なぜなら、アプリ内メッセージには`dispatch_id`がないからです。
{% endalert %}

## ディスパッチID Currents フィールド メール用

私たちのCurrents機能を引き続き強化するために、`dispatch_id`はすべてのコネクタタイプにわたるCurrentsメールイベントのフィールドでもあります。`dispatch_id` は、Braze プラットフォームから送信される各伝送または配信に対して生成される一意のIDです。

すべての顧客がスケジュールされたメッセージを受け取ると同じ`dispatch_id`を受け取りますが、アクションベースまたはAPIトリガーメッセージを受け取る顧客は、メッセージごとに一意の`dispatch_id`を受け取ります。`dispatch_id`フィールドにより、どのリカーリングキャンペーンのインスタンスがコンバージョンの原因であるかを特定できるため、どのタイプのキャンペーンがビジネス目標の達成に役立っているかについての洞察と情報を提供します。

`dispatch_id` を [パーソナライゼーション タグ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#supported-personalization-tags) として、[メッセージ エンゲージメント イベント]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/message_engagement_events/) で使用するか、[Segment]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment_for_currents/#integration-details)、[Mixpanel]({{site.baseurl}}/partners/insights/behavioral_analytics/mixpanel_for_currents/#email-events)、または Currents 用の [Amplitude]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/amplitude/amplitude_for_currents/) を使用する場合に使用できます。

_最終更新日：2021年7月15日_
