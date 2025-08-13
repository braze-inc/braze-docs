---
nav_title: 一般的なプッシュ・エラー・メッセージ
article_title: 一般的なプッシュ・エラー・メッセージ
page_order: 22
page_type: reference
description: "この記事では、iOSとAndroidでよく見られるプッシュ関連のエラーメッセージを取り上げ、潜在的なソリューションについて説明する。"
channel: push
platform:
- iOS
- Android
---

# 一般的なプッシュエラーメッセージ

> このページでは、プッシュメッセージングの一般的なエラーメッセージについて説明します。

{% tabs %}
{% tab Android %} 
### プッシュバウンス: MismatchSenderId
`MismatchSenderId` は認証が失敗したことを示します。Firebase クラウドメッセージング (FCM) の認証には、senderID と FCM API キーという2つの重要なデータが使用されます。 これら2つの正確性を検証する必要があります。詳細については、この問題に関する[Androidのドキュメントを](https://firebase.google.com/docs/cloud-messaging/http-server-ref#error-codes)参照のこと。

よくある失敗には、次のものがあります。
- 不正な[送信者ID]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#step-1-enable-firebase)
- 別のプッシュサービスに別の送信者IDで登録した場合、多重登録される。

### プッシュバウンス: InvalidRegistration
`InvalidRegistration` は、プッシュトークンの形式が正しくない場合に発生します。よくある失敗には、次のものがあります。
- ユーザはBraze登録トークンを手動で渡していますが、`getToken()` を呼び出さないでください。例えば、インスタンス ID 全体が渡される場合があります。エラーのトークンは`&#124;ID&#124;1&#124;:[regular token]` のようになります。  
- 複数のサービスに登録しています。現在、プッシュ登録のインテントが古いスタイルで到着することを期待しているため、人々が複数の場所で登録し、他のサービスからのインテントをキャッチした場合、不正なプッシュトークンを取得する可能性がある。

### プッシュバウンス: NotRegistered
`NotRegistered` 通常、アプリがデバイスから削除されたことを意味する（アンインストールの合図など）。これは、複数の登録が行われていて、2回目の登録がBrazeが受け取るプッシュトークンを無効にしている場合にも発生する可能性がある。

{% endtab %}
{% tab iOS %}

### プッシュバウンス: BadToken

`BadToken` エラーはいくつかの理由で発生する可能性があります。
- 現在、`[[Appboy sharedInstance] registerPushToken:]` でプッシュトークンが正しく送られてこない
	- [Message Activity Log]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/)のトークンを確認してください。通常は、文字と数字の長い文字列のように見えます (例: `6e407a9be8d07f0cdeb9e714733a89445f57a89ec890d63867c482a483506fa6`)。そうでない場合は、Brazeのプッシュトークンエラー送信に関わるコードをチェックする。<br><br>
- プロビジョニング環境の不一致：
	- 開発用の証明書で登録し、本番用の証明書で送信しようとすると、このようなエラーが表示される。  
	- Braze は、本番環境のユニバーサル証明書のみをサポートしています。ユニバーサル証明書を使用した開発環境でのプッシュテストは機能しない。 
	- このレポートは、プロダクションではバウンスを送信しますが、開発では送信しません。<br><br>
- プロビジョニング・プロファイルの不一致：
	- この問題は、証明書がトークンの取得に使用された証明書と一致しない場合に発生する可能性があります。これが疑われる場合、次のステップは次のようになります。
		- Brazeダッシュボードからのプッシュ送信に使用するプッシュ証明書とプロビジョニングプロファイルが正しく設定されていることを確認する。
		- APNS 証明書を再作成し、APNS 証明書が `app_id` に設定された後にプロビジョニングプロファイルを再作成します。これによって、より目に見える問題が解決されることもある。

### プッシュバウンス: APNSフィードバックサービスが削除された

これは通常、誰かがアンインストールしたときに起こる。Brazeは毎晩APNSフィードバックサービスに問い合わせ、無効なトークンのリストを取得する。詳細については、Appleの「[Communicating with APNs](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CommunicatingwithAPNs.html)」を参照のこと。

{% endtab %}
{% endtabs %}
