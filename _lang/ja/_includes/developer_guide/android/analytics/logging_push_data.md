## Braze でのログ記録(推奨)

[`/users/track` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) を呼び出すことで、分析をリアルタイムで記録できます。分析を記録するには、Braze ダッシュボードから`braze_id` 値を送信して、更新するユーザープロファイルを識別します。

![パーソナライズされたプッシュダッシュボード例]({% image_buster /assets/img/push_implementation_guide/android_braze_id_configuration.png %}){: style="max-width:79%;"}

## データの手動ロギング

給与読み込むの内容に応じて、`FirebaseMessagingService.onMessageReceived` インプリメンテーションまたはスタートアップアクティビティ内で分析を手動で記録できます。`FirebaseMessagingService` サブクラスは、Androidシステムによって[ フラグが設定されたり、終了したりしないように、起動後9 秒で実行を終了する必要があります。
