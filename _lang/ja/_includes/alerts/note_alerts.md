{% if include.alert == 'Content Cards frequency capping' %}

{% alert note %}
フリークエンシーキャップは、コンテンツカードには適用されません。
{% endalert %}

{% endif %}

{% if include.alert == 'Custom Attributes time attribute' %}

{% alert note %}
「12-1-2021」や「12/1/2021」などの日付文字列は、日時オブジェクトに変換され、[時間属性]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#time)として扱われます。
{% endalert %}

{% endif %}

{% if include.alert == 'Manage custom data storage' %}

{% alert note %}
ユーザープロファイルのすべてのデータ (カスタムイベント、カスタム属性、カスタムデータ) は、それらのプロファイルがアクティブである限り保存されます。
{% endalert %}

{% endif %}

{% if include.alert == 'Segment profiles first app use' %}

{% alert note %}
Braze は、ユーザーが初めてアプリを使用するまでプロファイルを生成しないため、アプリをまだ開封していないユーザーをターゲットにすることはできません。
{% endalert %}

{% endif %}

{% if include.alert == 'Shopify attributes REST API' %}

{% alert note %}
すべての属性のソースは Braze REST API です。
{% endalert %}

{% endif %}