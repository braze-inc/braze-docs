---
nav_title: 非推奨
article_title: 非推奨
page_order: 9
page_type: reference
description: "このページには、非推奨の記事への参照が含まれており、非推奨およびサポートされていない機能の一覧を提供します。"
---

# 非推奨

テクノロジーは、Brazeの内側と外側で常に動いています。そして、私たちはそれに追いつくために最善を尽くします。ここでは、Brazeとそのテクノロジーの起源、つまり「ビフォア・タイム」に私たちがどのように人々をサポートしてきたか、そしてビフォア・ナウ...

存在しない統合または機能の用語を検索して、ここにたどり着いた可能性があります。これは、テクノロジー業界における当社の進歩と動きについてお知らせするための試みです。非推奨およびサポートされていない機能の一覧を確認し、非推奨の記事を読むには、次のリンクにアクセスしてください。

## 非推奨の記事

- [Android用のカスタムプッシュブロードキャストレシーバー]({{site.baseurl}}/help/release_notes/deprecations/custom_broadcast_receiver/)
- [Eclipse SDK のセットアップ]({{site.baseurl}}/help/release_notes/deprecations/eclipse_setup_deprecated/)
- [TLS 1.0 および 1.1 の廃止]({{site.baseurl}}/help/release_notes/deprecations/tls_deprecation/)
- [Twilio Webhook の統合]({{site.baseurl}}/help/release_notes/deprecations/twilio/)
- [Apptimizeとのパートナーシップ]({{site.baseurl}}/help/release_notes/deprecations/apptimize/)
- [Grouparooとのパートナーシップ]({{site.baseurl}}/help/release_notes/deprecations/grouparoo)

## 非推奨ログ

### Android用のカスタムプッシュブロードキャストレシーバー

**サポートの撤回:**2022年10月発売

プッシュ通知のカスタム `BroadcastReceiver` の使用は非推奨になりました。代わりに使用してください [` subscribeToPushNotificationEvents()`](/docs/developer_guide/platform_integration_guides/android/push_notifications/android/customization/custom_event_callback/) 。

### Grouparooとのパートナーシップ

**サポートの撤回:**2022年4月発売

Grouparoo のサポートは 2022 年 4 月をもって終了しています。

### Braze Windows SDK

**2022年3月24日**:Braze Windows SDKは廃止され、Brazeダッシュボードで新しいWindowsアプリを作成することはできません。<br>
**2022年9月15日**:Windows アプリに新しいメッセージを送信できません。既存のメッセージとデータ収集は影響を受けません。<br>
**2024年1月11日**:Brazeは、Windowsアプリからメッセージを提供したり、データを収集したりしなくなります。

### Baidu プッシュ統合

**2022年3月24日**:Braze Baidu プッシュ統合は廃止され、Braze ダッシュボードで新しい Baidu アプリを作成することはできません。<br>
**2022年9月15日**:新しいバイドゥプッシュメッセージは作成できません。既存のメッセージとデータ収集は影響を受けません。<br>
**2024年1月11日**:Brazeは、Baiduアプリからメッセージを配信したり、データを収集したりしなくなります。

### appboyBridge グローバル変数

**サポートの撤回:**2021年5月発売<br>
**置換後の文字列**: `brazeBridge`

グローバル変数`appboyBridge`は廃止`brazeBridge`され、 に置き換えられました。 `appboyBridge` 既存のお客様に対しては引き続き機能しますが、 を使用している場合は、に移行する`brazeBridge``appboyBridge`ことをお勧めします。

### Amazon Momentsのパートナーシップ

**サポートの撤回:**2020年6月発売

Amazon Momentsのサポートは、2020年6月をもって終了しました。Amazon MomentsはAmazon Advertisingに統合され、APIと統合は廃止されました。

### 事実上のパートナーシップ

**サポートの撤回:**2020年6月発売

2020 年 6 月をもって Factual のサポートは終了しました。Ffactualは最近Foursquareに買収され、Brazeプラットフォームと統合されなくなりました。

### Twilio Webhook の統合

**サポートの撤回:**2020年1月発売

[Twilio Webhook 統合]({{site.baseurl}}/partners/twilio/)のサポートは、2020 年 1 月 31 日をもって終了しました。BrazeでSMSサービスにアクセスしたい場合は、 [SMSのドキュメント]({{site.baseurl}}/user_guide/message_building_by_channel/sms/)をご覧ください。

### Apptimizeとのパートナーシップ

**サポートの撤回:**2019年8月発売

現在、 [ApptimizeとBrazeを併用]({{site.baseurl}}/help/release_notes/deprecations/apptimize)している場合、サービスの中断は発生しません。Apptimizeのカスタム属性をBrazeユーザープロファイルに設定することはできます。ただし、パートナーとの正式なエスカレーション サポートは提供されません。

### オリジナルのアプリ内メッセージ

**サポートの撤回:**2019年2月発売<br>
**置換後の文字列**:[アプリ内メッセージング]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creating_an_in-app_message)

Brazeは、最新のUXとUIのベストプラクティスに準拠するためにアプリ内メッセージのルック&フィールを改善し、元のアプリ内メッセージをサポートしなくなりました。

Brazeは、以下のSDKリリースで新しい形式のアプリ内メッセージに移行しました。
\- iOSの場合: `2.19.0`
-アンドロイド： `1.13.0`
-ウェブ： `1.3.0`

これらのリリース以前は、Brazeは「オリジナルのアプリ内メッセージ」をサポートしていました。 以前は、新しいリリース前にアプリ内キャンペーンを実施したすべてのお客様に、オリジナルのアプリ内メッセージのサポートが提供されていました。すべてのキャンペーン統計は変更の影響を受けず、オリジナルのアプリ内メッセージを送信したユーザーは、**キャンペーン**ページの**[キャンペーンを作成**]ボタンから他のユーザーを送信する機会がありました。

### フィードバックウィジェット

**サポートの撤回:**2019年7月1日。

Braze SDKは、ユーザーがこの `submitfeedback` メソッドを使用してフィードバックを残し、Desk.com またはZendeskに渡すことができるフィードバックウィジェットをアプリに追加できるフィードバックウィジェットを提供し、ダッシュボードで管理していました。

### Google Cloud Messaging (GCM) (英語)

**サポートの撤回:**サポートのろう付け除去:2018年7月、Googleによるサポートの削除:2019年5月29日<br>
**置換後の文字列**:[Firebase クラウド メッセージング (FCM)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#step-1-enable-firebase)

Google は 2019 年 5 月 29 日をもって [GCM のサポートを終了しました](https://developers.googleblog.com/2018/04/time-to-upgrade-from-gcm-to-fcm.html) 。Brazeは、2018年7月にAndroid SDKからのGCMのサポートを終了[しました。](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)つまり、既存の GCM トークンは引き続き機能し、既存のユーザーにメッセージを送信できるようになります。ただし、新しいユーザーにメッセージを送信することはできません。

[Firebase Cloud Messaging(FCM)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#step-1-enable-firebase)にまだ移行していないお客様は、この変更の影響を受ける可能性があります。

FCM に移行していない場合、すべての GCM プッシュ トークンの登録が失敗します。アプリが現在 GCM をサポートしている場合は、開発チームと協力して [GCM から Firebase Cloud Messaging(FCM)に移行する](https://developers.google.com/cloud-messaging/android/android-migrate-fcm)必要があります。

### 食

**サポートの撤回:**2014-2015<br>
**置換後の文字列**:[Androidスタジオ]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#using-android-studio)

Brazeは、GoogleがEclipse Android Developer Tools(ADT)プラグイン [のサポートを終了した](http://android-developers.blogspot.com/2015/06/an-update-on-eclipse-android-developer.html) ため、Eclipse IDEのサポートを終了しました。 

移行前に Eclipse 統合についてサポートが必要な場合は、 [サポート]({{site.baseurl}}/support_contact/) にお問い合わせください。

### 未加工のイベント ストリーム (RES)

**サポートの撤回:**2018年7月発売<br>
**置換後の文字列**:[Currents]({{site.baseurl}}/partners/braze_currents/about/)

Raw Event Stream は [Currents]({{site.baseurl}}/partners/braze_currents/about/) の前身であり、Braze データの将来に備えて廃止されました。

### アイドル時の遅延 - GCM 機能

**サポートの撤回:**2016年11月号

「アイドル時の遅延」パラメーターは、以前は [GCM プッシュ・オプション](https://developers.google.com/cloud-messaging/http-server-ref)の一部でした。Google は 2016 年 11 月 15 日にこのオプションのサポートを終了しました。以前は、 **true** に設定すると、デバイスがアクティブになるまでメッセージを送信しないことが示されていました。

### カスタム エンドポイント

**サポートの撤回:**2019年12月発売

カスタム エンドポイントの削除。カスタムエンドポイントがある場合は、引き続き使用できますが、Brazeはそれらを提供しなくなりました。


[15]: {% image_buster /assets/img_archive/in-app-choices.png %}
