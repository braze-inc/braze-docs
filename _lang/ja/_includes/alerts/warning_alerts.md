{% if include.alert == 'User profile external_id' %}

{% alert warning %}
ユーザープロファイルを一意に識別する前に、`external_id` を割り当てないこと。ユーザーを識別した後、匿名ユーザーに戻すことはできません。
<br><br>
An [は、エンド`/users/external_ids/rename`ポイント]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename/)`external_id`を使って更新できる。ただし、ユーザーのセッション中に`external_id`異なる設定を試みると、新しい設定`external_id`が関連付けられた新しいユーザープロファイルが作成される。2 つのプロファイル間でデータは渡されません。
{% endalert %}

{% endif %}

{% if include.alert == 'Segment Currents multiple connectors' %}

{% alert warning %}
同じCurrentsコネクターを複数作成する場合(たとえば、2 つのメッセージエンゲージメントイベントコネクター)、それらは別々のワークスペースにする必要があります。Braze Segment Currents の統合では、1つのワークスペース内で異なるアプリケーションごとにイベントを分離することはできないため、そのようにできない場合、不必要なデータの重複排除やデータの損失が発生します。
{% endalert %}

{% endif %}

{% if include.alert == 'Canvas race condition audience trigger' %}

{% alert warning %}
オーディエンスフィルターと同じトリガー (属性の変更やカスタムイベントの実行など) でアクションベースのキャンペーンやキャンバスを設定しないでください。[競合状態]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions)が発生する可能性がある。その場合、ユーザーがトリガーイベントを実行した時点でオーディエンスに含まれていないため、キャンペーンを受け取ったりキャンバスに入ったりしない。
{% endalert %}

{% endif %}
