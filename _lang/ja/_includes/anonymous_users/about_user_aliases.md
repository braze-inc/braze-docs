匿名ユーザーは`external_ids` 、代わりに[ユーザーエイリアスを]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/#user-aliases)割り当てることができる。ユーザーエイリアスを割り当てる必要があるのは、ユーザーに他の識別子を追加したいが、そのユーザーの`external_id` がわからない場合である（たとえば、ログインしていない）。ユーザーエイリアスを使えば、こんなこともできる：

- Braze APIを使用して、匿名ユーザーに関連するイベントと属性を記録する。
- [外部ユーザーIDが空白の]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#external-user-id)セグメンテーションフィルターを使用して、匿名ユーザーをメッセージングのターゲットにする。

{% if include.section == "user_guide" %}
{% alert tip %}
完全なウォークスルーは、[Braze SDKを参照のこと：ユーザーエイリアスの設定]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/#setting-a-user-id).
{% endalert %}
{% endif %}