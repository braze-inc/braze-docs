{% multi_lang_include developer_guide/prerequisites/android.md %} [プッシュ通知の設定も]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android)必要だ。

## サイレント・プッシュ通知を設定する

サイレント通知は Braze[Messaging API]({{site.baseurl}}/api/endpoints/messaging/) を通じて利用できます。サイレント通知を利用するには、[Android プッシュオブジェクト]({{site.baseurl}}/api/objects_filters/messaging/android_object/)内で `send_to_sync` フラグを `true` に設定します。また、`title` または `alert` フィールドを `send_to_sync` とともに使用するとエラーが発生するため、それらが設定されていないことを確認する必要があります。ただし、オブジェクト内にデータ `extras` を含めることはできます。
