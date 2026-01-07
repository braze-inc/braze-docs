[Braze SDKを統合した]({{site.baseurl}}/developer_guide/sdk_integration/)後、アプリを初めて起動したユーザーは、`changeUser` メソッドを呼び出して`external_id` を割り当てるまで、「匿名」とみなされる。一度割り当てられると、再び匿名にすることはできない。しかし、アプリをアンインストールして再インストールすると、`changeUser` が呼び出されるまで、再び匿名になる。

以前に識別されたユーザーが新しいデバイスでセッションを開始した場合、そのユーザーの`external_id` を使用してそのデバイスで`changeUser` を呼び出すと、すべての匿名アクティビティが自動的に既存のプロファイルに同期される。これには、新しいデバイスでのセッション中に収集された属性、イベント、または履歴が含まれる。

{% if include.section == "user_guide" %}
{% alert tip %}
詳しい説明は、[ユーザーIDの設定を]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/)参照のこと。
{% endalert %}
{% endif %}