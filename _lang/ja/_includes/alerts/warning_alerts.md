{% if include.alert == 'User profile external_id' %}

{% alert warning %}
ユーザープロファイルを一意に識別する前に、`external_id` を割り当てないこと。ユーザーを識別した後、匿名ユーザーに戻すことはできません。
<br><br>
`external_id` は[`/users/external_ids/rename` エンドポイントを使って]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename/)更新できる。しかし、ユーザーのセッション中に異なる`external_id` を設定しようとすると、新しい`external_id` に関連付けられた新しいユーザープロファイルが作成される。2 つのプロファイル間でデータは渡されません。
{% endalert %}

{% endif %}

{% if include.alert == 'Segment Currents multiple connectors' %}

{% alert warning %}
同じCurrentsコネクターを複数作成する場合(たとえば、2 つのメッセージエンゲージメントイベントコネクター)、それらは別々のワークスペースにする必要があります。Braze Segment Currents の統合では、1つのワークスペース内で異なるアプリケーションごとにイベントを分離することはできないため、そのようにできない場合、不必要なデータの重複排除やデータの損失が発生します。
{% endalert %}

{% endif %}

{% if include.alert == 'Canvas race condition audience trigger' %}

{% alert warning %}
オーディエンスフィルターと同じトリガー (属性の変更やカスタムイベントの実行など) でアクションベースのキャンペーンやキャンバスを設定しないでください。[競合条件が]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions)発生すると、ユーザーがトリガーイベントを実行した時点でオーディエンスにおらず、キャンペーンを受け取れなかったり、キャンバスに入れなかったりする。
{% endalert %}

{% endif %}
