## プッシュエラーログの活用

Braze は、プッシュ通知エラーをメッセージアクティビティログに出力します。このエラーログは、キャンペーンが期待どおりに機能していない理由を特定するのに非常に役立つさまざまな警告を提供します。エラーメッセージをクリックすると、特定のインシデントのトラブルシューティングに役立つ関連ドキュメントにリダイレクトされます。

![]({% image_buster /assets/img_archive/message_activity_log.png %})

## トラブルシューティングのシナリオ

### Braze ダッシュボードに「プッシュ登録された」ユーザーが表示されない (メッセージ送信前)

- アプリがプッシュ通知を許可するように正しく構成されていることを確認してください。
- Braze ダッシュボードで設定されたクライアント ID とクライアントシークレットが正しいことを確認してください。

### プッシュ通知がユーザーのデバイスに表示されない

この問題が発生する理由はいくつか考えられます。

- アプリケーションを強制終了すると、アプリケーションが実行されていない間はプッシュ通知が表示されません。
- キャンペーンの[通知優先度]({{ site.baseurl }}/developer_guide/platform_integration_guides/android/push_notifications/fireos/customization/advanced_settings/#notification-display-priority) ]設定が`HIGH` に設定されていることを確認する。
- `api_key.txt` の ADM API キーが間違っているか、無効な文字を含んでいます。
- `BrazeAmazonDeviceMessagingReceiver` は、`<action android:name="com.amazon.device.messaging.intent.RECEIVE" />` および `<action android:name="com.amazon.device.messaging.intent.REGISTRATION" />` のインテントフィルターを使用して `AndroidManifest.xml` に適切に登録されていません。

### 「プッシュ登録済み」ユーザーがメッセージ送信後に有効でなくなる

これは通常、ユーザーがアプリケーションをアンインストールし、ADM 登録 ID が無効になった場合に発生します。
