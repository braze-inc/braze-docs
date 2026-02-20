---
nav_title: 非推奨
article_title: 非推奨
page_order: 9
page_type: reference
description: "このページには、非推奨の記事への参照と、非推奨の機能およびサポート対象外の機能のリストが含まれています。"
---

# 非推奨

テクノロジーは、Braze の内外を問わず常に進化しています。当社は、それに追いつくために最善を尽くしています。ここでは、Brazeの起源とその技術、そして私たちが "Before Time"-とにかく今より前...-でどのように人々を支えてきたかを知ることができる。

ここでは、存在しなくなった統合や機能の用語を検索してみましょう。これは、テクノロジー業界における当社の進歩と動向について、皆様に常に最新情報を提供することを目的としています。以下のリンクから、非推奨の機能とサポート対象外の機能のリストを確認し、非推奨の記事を読むことができます。

## 非推奨記事

- [Android用カスタム・プッシュ・ブロードキャスト・レシーバー]({{site.baseurl}}/releases/deprecations/custom_broadcast_receiver/)
- [Eclipse SDKのセットアップ]({{site.baseurl}}/releases/deprecations/eclipse_setup_deprecated/)
- [TLS 1.0 および1.1 の非推奨]({{site.baseurl}}/releases/deprecations/tls_deprecation/)
- [Twilio webhookの統合]({{site.baseurl}}/releases/deprecations/twilio/)
- [Apptimize のパートナーシップ]({{site.baseurl}}/releases/deprecations/apptimize/)
- [Grouparoo のパートナーシップ]({{site.baseurl}}/releases/deprecations/grouparoo)
- [Shopify`checkout.liquid` 非推奨]({{site.baseurl}}/releases/deprecations/shopify_checkout/)

## 非推奨ログ

### Shopify `checkout.liquid`

**サポートの撤回**: 2024年8月（第1フェーズ）、2025年8月（第2フェーズ）

Shopify `checkout.liquid` は、2024年8月に非推奨になり、2025年8月に終了します。Shopifyは、より安全で、パフォーマンスが高く、カスタマイズ可能な[Checkout Extensibilityに](https://www.shopify.com/enterprise/blog/checkout-extensibility-winter-editions)移行する予定だ。

### Android用カスタム・プッシュ・ブロードキャスト・レシーバー

**サポートの撤回**: 2022年10月

プッシュ通知にカスタム`BroadcastReceiver` を使用することは廃止された。代わりに [` subscribeToPushNotificationEvents()`]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=android#android_using-a-callback-for-push-events)で代用する。

### Grouparoo のパートナーシップ

**サポートの撤回**: 2022年4月

Grouparoo のサポートは、2022年4月に終了しました。

### Braze Windows SDK

**2022年3 月24 日**:Braze Windows SDK は非推奨となり、Braze ダッシュボードで新しい Windows アプリを作成することはできません。<br>
**2022年9 月15 日**:Windowsアプリに新しいメッセージを送ることはできない。既存のメッセージやデータ収集に影響はない。<br>
**2024年1 月11 日**:Brazeは、Windowsアプリからのメッセージ配信やデータ収集を行わない。

### Baiduプッシュ統合

**2022年3 月24 日**:BrazeのBaiduプッシュ統合は非推奨となり、Brazeダッシュボードで新しいBaiduアプリを作成することはできない。<br>
**2022年9 月15 日**:新しいBaiduプッシュメッセージは作成できない。既存のメッセージやデータ収集に影響はない。<br>
**2024年1 月11 日**:Brazeは今後、Baiduアプリからのメッセージ配信やデータ収集は行わない。

### appboyBridge グローバル変数

**サポートの撤回**: 2021年5月<br>
**置換**: `brazeBridge`

グローバル変数`appboyBridge` は非推奨となり、`brazeBridge` に置き換えられました。`appboyBridge` は既存のお客様は引き続き使用できますが、`appboyBridge` を使用している場合は `brazeBridge` に移行することをお勧めします。

### Amazon Momentsパートナーシップ

**サポートの撤回**: 2020年6月

Amazon Momentsのサポートは2020年6月をもって終了した。Amazon MomentsはAmazon Advertisingに統合され、APIと我々の統合は廃止された。

### 事実上のパートナーシップ

**サポートの撤回**: 2020年6月

Factual のサポートは、2020年6月に終了しました。Factualは最近Foursquareに買収され、Braze Platformとの統合はなくなった。

### Twilio webhookの統合

**サポートの撤回**: 2020年1月

[Twilio Webhookインテグレーション]({{site.baseurl}}/partners/twilio/)の対応は2020年1月31日をもって終了しました。BrazeでもSMSサービスにアクセスしたい場合は、[SMSのドキュメントを]({{site.baseurl}}/user_guide/message_building_by_channel/sms/)参照のこと。

### Apptimize のパートナーシップ

**サポートの撤回**: 2019年8月

現在[Braze]({{site.baseurl}}/releases/deprecations/apptimize)でApptimizeを使用している場合、サービスの中断は発生しません。Apptimize のカスタム属性を Braze のユーザープロファイルに設定することもできます。ただし、パートナーとの正式なエスカレーションサポートは提供されません。

### アプリ内オリジナルメッセージ

****サポートの終了**:**2019年2月<br>
**置換**: [アプリ内メッセージング]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/create/)

Brazeは、最新のUXとUIのベストプラクティスに準拠するため、アプリ内メッセージのルック＆フィールを改善し、オリジナルのアプリ内メッセージのサポートは終了した。

Braze は、以下の SDK リリースでアプリ内メッセージの新しい形式に移行しました。
- iOS: `2.19.0`
- Android: `1.13.0`
- Web: `1.3.0`

これらのリリース以前は、Brazeは "アプリ内オリジナルメッセージ "をサポートしていた。これまでは、新しいリリース前にアプリ内キャンペーンを実行したすべてのお客様に対して、元のアプリ内メッセージのサポートが提供されていました。すべてのキャンペーン統計はこの変更の影響を受けず、オリジナルのアプリ内メッセージを送信した人は、**キャンペーン**ページの「**キャンペーンを作成」**ボタンから他のメッセージを送信することができた。

### フィードバック・ウィジェット

**サポートの撤回**: 2019年7月1日

Braze SDKは、アプリに追加できるフィードバックウィジェットを提供し、ユーザーが`submitfeedback` メソッドを使ってフィードバックを残し、それをDesk.com またはZendeskに渡し、ダッシュボードで管理できるようにした。

### Google Cloud Messaging (GCM)

**サポートの撤回**: Braze のサポート終了: 2018年7月、Googleによるサポートの削除:2019年5月29日<br>
**置換**: [Firebase クラウドメッセージング (FCM)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#step-1-enable-firebase)

Google は、2019年5月29日をもって [GCMのサポートを終了](https://developers.googleblog.com/2018/04/time-to-upgrade-from-gcm-to-fcm.html)しました。Brazeは2018年7月にAndroid SDKからGCMのサポートを打ち切ったが、これは当社の[Android SDKの変更履歴に](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)記載されている。これは、既存のGCMトークンが引き続き機能し、既存のユーザーにメッセージを送ることができることを意味する。ただし、新規ユーザーにメッセージを送ることはできません。

まだ[Firebase Cloud Messaging (FCM)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#step-1-enable-firebase)に移行していない顧客は、この変更の影響を受ける可能性がある。

FCMに移行していない場合、GCMプッシュトークンの登録はすべて失敗する。アプリが現在GCMをサポートしている場合は、[GCMからFirebase Cloud Messaging (FCM)](https://developers.google.com/cloud-messaging/android/android-migrate-fcm)への移行時に開発チームと連携する必要があります。

### Eclipse

**サポートの撤回**: 2014～2015年<br>
**置換**: [Android Studio]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#using-android-studio)

Google が Eclipse Android Developer Tools (ADT) プラグインの[サポートを終了](http://android-developers.blogspot.com/2015/06/an-update-on-eclipse-android-developer.html)したため、Braze は Eclipse IDE のサポートを中止しました。 

移行前に Eclipse の統合に関するサポートが必要な場合は、[サポート]({{site.baseurl}}/support_contact/)にお問い合わせください。

### Raw Event Stream (RES)

**サポートの撤回**: 2018年7月<br>
**置換**: [Currents]({{site.baseurl}}/user_guide/data/braze_currents/)

Raw Event Stream は [Currents]({{site.baseurl}}/user_guide/data/braze_currents/) の前身であり、Braze データの将来に備えて廃止されました。

### アイドル時のディレイ - GCM機能

**サポートの撤回**: 2016年11月

Delay While Idleパラメータは、以前は[GCMプッシュオプション](https://developers.google.com/cloud-messaging/http-server-ref)の一部でした。Googleは2016年11月15日にこのオプションのサポートを撤回した。以前は、**true**に設定した場合、デバイスがアクティブになるまでメッセージを送信しないことを示していました。

### カスタムエンドポイント

**サポートの撤回**: 2019年12月

カスタムエンドポイントの削除。カスタムエンドポイントを持っている場合は、それを使い続けることができるが、Brazeはもうそれを提供しない。


