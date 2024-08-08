---
nav_title: よくあるプッシュのエラーメッセージ
article_title: よくあるプッシュのエラーメッセージ
page_order: 2

page_type: solution
description: "このヘルプ記事では、iOSとAndroidでよく見られるプッシュ関連のエラーメッセージを取り上げ、潜在的なソリューションについて説明する。"
channel: push
platform:
- iOS
- Android
---

# よくあるプッシュのエラーメッセージ

プッシュ・メッセージングのよくあるエラーメッセージをチェックしよう：

{% tabs %}
{% tab Android %} 
### プッシュが跳ねた：送信者IDの不一致
`MismatchSenderId` は認証が失敗したことを示します。Firebase Cloud Messaging (FCM)は、送信者IDとFCM APIキーという2つのキーで認証を行う。 いずれも正確性を検証する必要がある。詳細については、この問題に関する[Androidのドキュメントを](https://firebase.google.com/docs/cloud-messaging/http-server-ref#error-codes)参照のこと。

よくある故障には、以下のようなものがある：
- 不正な[送信者ID]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#step-1-enable-firebase)
- 別のプッシュサービスに別の送信者IDで登録した場合、多重登録される。

### プッシュが跳ねた：InvalidRegistration
`InvalidRegistration` プッシュトークンが不正な形をしている場合に起こりうる。よくある故障には、以下のようなものがある：
- 人々はBrazeの登録トークンを手動で渡しているが、`getToken()` 。例えば、インスタンスID全体を渡すこともできる。エラーメッセージのトークンは`&#124;ID&#124;1&#124;:[regular token]` のようだ。  
- 人々は複数のサービスに登録している。現在のところ、プッシュ登録のインテントが古いスタイルで到着することを期待しているため、人々が複数の場所で登録していて、他のサービスからのインテントをキャッチした場合、不正なプッシュトークンを取得する可能性がある。

### プッシュが跳ねた：NotRegistered
`NotRegistered` 通常、アプリがデバイスから削除されたことを意味する（アンインストールの合図など）。これは、複数の登録が行われていて、2回目の登録がBrazeが受け取るプッシュトークンを無効にしている場合にも発生する可能性がある。

{% endtab %}
{% tab iOS %}

### プッシュが跳ねた：不正なプッシュトークンへの送信エラー

このエラーはいくつかの理由で発生する可能性がある：
- でプッシュトークンが正しく送信されていない。 `[[Appboy sharedInstance] registerPushToken:]`
	- **メッセージアクティビティログで**トークンを確認する。一般的には、文字と数字の長い文字列のように見えるはずである。(e.g `6e407a9be8d07f0cdeb9e714733a89445f57a89ec890d63867c482a483506fa6`) そうでない場合は、Brazeのプッシュトークンエラー送信に関わるコードをチェックする。<br><br>
- プロビジョニング環境の不一致：
	- 開発用の証明書で登録し、本番用の証明書で送信しようとすると、このようなエラーが表示される。  
	- Brazeは本番環境用のユニバーサル証明書しかサポートしていない。ユニバーサル証明書を使用した開発環境でのプッシュテストは機能しない。 
	- このレポートは本番ではバウンスを送信するが、開発者には送信しない。<br><br>
- プロビジョニング・プロファイルの不一致：
	- これは、トークンを取得するために使用された証明書と、あなたの証明書が一致しない場合に起こる可能性がある。これが疑われる場合、次のステップがある：
		- ダッシュボードからのプッシュ送信に使用するプッシュ証明書とプロビジョニングプロファイルが正しく設定されていることを確認する。
		- APNS証明書を再作成し、APNS証明書を`app_id` に設定した後、プロビジョニングプロファイルを再作成する。これによって、より目に見える問題が解決されることもある。

### プッシュが跳ねた：APNフィードバックサービス削除

これは通常、誰かがアンインストールしたときに起こる。Brazeは毎晩APNフィードバックサービスに問い合わせ、無効なトークンのリストを取得する。詳細については、Appleの[APNとの](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CommunicatingwithAPNs.html)コミュニケーションを参照のこと。


{% endtab %}
{% endtabs %}

_最終更新日：2021年1月24日_
