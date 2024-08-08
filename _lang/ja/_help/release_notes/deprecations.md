---
nav_title: 非推奨
article_title: 非推奨
page_order: 9
page_type: reference
description: "このページでは、非推奨の記事への参照を含み、非推奨およびサポートされない機能のリストを提供する。"
---

# 非推奨

テクノロジーは常に動いている。Brazeの内部でも外部でも！そして、私たちはそれについていくためにベストを尽くしている。ここには、Brazeの原点とそのテクノロジーがある。

もう存在しない統合や機能を検索してここにたどり着いたかもしれない。これは、テクノロジー業界における我々の進歩や動きをお知らせするための試みである。以下のリンクから、非推奨およびサポートされない機能のリストや、非推奨の記事を読むことができる。

## 非推奨記事

- [Android用カスタム・プッシュ放送受信機]({{site.baseurl}}/help/release_notes/deprecations/custom_broadcast_receiver/)
- [Eclipse SDKのセットアップ]({{site.baseurl}}/help/release_notes/deprecations/eclipse_setup_deprecated/)
- [TLS 1.0および1.1の廃止]({{site.baseurl}}/help/release_notes/deprecations/tls_deprecation/)
- [Twilio Webhookの統合]({{site.baseurl}}/help/release_notes/deprecations/twilio/)
- [Apptimizeパートナーシップ]({{site.baseurl}}/help/release_notes/deprecations/apptimize/)
- [Grouparooパートナーシップ]({{site.baseurl}}/help/release_notes/deprecations/grouparoo)
- [Shopify`checkout.liquid` 非推奨]({{site.baseurl}}/help/release_notes/deprecations/shopify_checkout/)

## 非推奨ログ

### Shopify `checkout.liquid`

**支援は撤回された**：2024年8月（第1フェーズ）、2025年8月（第2フェーズ）

Shopify`checkout.liquid` のサポートは2024年8月に非推奨となり、2025年8月に終了する。Shopifyは、より安全でパフォーマンスも高く、カスタマイズ可能な[Checkout Extensibilityに](https://www.shopify.com/enterprise/blog/checkout-extensibility-winter-editions)移行する予定だ。

### Android用カスタム・プッシュ放送受信機

**支援は撤回された**：2022年10月

プッシュ通知にカスタム`BroadcastReceiver` を使用することは廃止された。代わりに [` subscribeToPushNotificationEvents()`](/docs/developer_guide/platform_integration_guides/android/push_notifications/android/customization/custom_event_callback/)で代用する。

### Grouparooパートナーシップ

**支援は撤回された**：2022年4月

Grouparooのサポートは2022年4月をもって終了した。

### Braze Windows SDK

**2022年3月24**日だ：Braze Windows SDKは非推奨であり、ダッシュボードで新しいWindowsアプリを作成することはできない。<br>
**2022年9月15**日である：Windowsアプリに新しいメッセージを送ることはできない。既存のメッセージングやデータ収集に影響はない。<br>
**2024年1月11**日だ：Brazeは今後、Windowsアプリからのメッセージ送信やデータ収集を行わない。

### 百度プッシュの統合

**2022年3月24**日だ：BrazeのBaiduプッシュ統合は非推奨となり、Brazeダッシュボードで新しいBaiduアプリを作成することはできない。<br>
**2022年9月15**日である：新しいBaiduプッシュメッセージは作成できない。既存のメッセージングやデータ収集に影響はない。<br>
**2024年1月11**日だ：Brazeは今後、Baiduアプリからのメッセージングやデータ収集を行わない。

### appboyBridge グローバル変数

**支援は撤回された**：2021年5月<br>
**に取って代わられた**： `brazeBridge`

グローバル変数`appboyBridge` は非推奨となり、`brazeBridge` に置き換えられる。`appboyBridge` は既存の顧客には引き続き機能するが、`appboyBridge` を使用している場合は、`brazeBridge` に移行することを推奨する。

### Amazon Momentsパートナーシップ

**支援は撤回された**：2020年6月

Amazon Momentsのサポートは2020年6月をもって終了した。Amazon MomentsはAmazon Advertisingに統合され、APIと我々の統合は廃止された。

### 事実上のパートナーシップ

**支援は撤回された**：2020年6月

Factualのサポートは2020年6月をもって終了した。Factualは最近Foursquareに買収され、Brazeプラットフォームとの統合はなくなった。

### Twilio Webhookの統合

**支援は撤回された**：2020年1月

[Twilio Webhook統合の]({{site.baseurl}}/partners/twilio/)サポートは2020年1月31日をもって終了した。BrazeでSMSサービスにアクセスしたい場合は、[SMSドキュメントを]({{site.baseurl}}/user_guide/message_building_by_channel/sms/)参照のこと。

### Apptimizeパートナーシップ

**支援は撤回された**：2019年8月

現在、[BrazeでApptimizeを]({{site.baseurl}}/help/release_notes/deprecations/apptimize)使用している場合、サービスが中断することはない。BrazeユーザープロファイルにApptimizeカスタム属性を設定することはできる。しかし、パートナーとの正式なエスカレーション・サポートは提供されない。

### アプリ内オリジナルメッセージ

**支援は撤回された：**2019年2月<br>
**に取って代わられた**：[アプリ内メッセージング]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creating_an_in-app_message)

Brazeは、最新のUXとUIのベストプラクティスに準拠するためにアプリ内メッセージのルック＆フィールを改善し、オリジナルのアプリ内メッセージのサポートは終了した。

Brazeは、以下のSDKリリースにより、アプリ内メッセージという新しい形態に移行した：
- iOSだ： `2.19.0`
- Android: `1.13.0`
- Web: `1.3.0`

これらのリリース以前は、Brazeは "オリジナルアプリ内メッセージ "をサポートしていた。これまで、アプリ内オリジナルメッセージのサポートは、新リリース以前にアプリ内キャンペーンを実施した顧客に対して提供されていた。すべてのキャンペーン統計はこの変更の影響を受けず、アプリ内オリジナルメッセージを送信した人は、**キャンペーン**ページの「**キャンペーンを作成**」ボタンから他のメッセージを送信することができた。

### フィードバック・ウィジェット

**支援は撤回された**：2019年7月1日

Braze SDKは、アプリに追加できるフィードバックウィジェットを提供し、ユーザーが`submitfeedback` メソッドを使ってフィードバックを残し、それをDesk.com またはZendeskに渡し、ダッシュボードで管理できるようにした。

### Googleクラウドメッセージング（GCM）

**支援は撤回された**：サポートをBrazeで取り外す：2018年7月、グーグルはサポートを打ち切った：2019年5月29日<br>
**に取って代わられた**：[Firebaseクラウドメッセージング(FCM)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#step-1-enable-firebase)

グーグルは2019年5月29日をもって[GCMのサポートを終了](https://developers.googleblog.com/2018/04/time-to-upgrade-from-gcm-to-fcm.html)した。Brazeは2018年7月にAndroid SDKからのGCMのサポートを終了しており、そのことは[Android SDKの変更履歴に](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)記載されている。これは、既存のGCMトークンが引き続き機能し、既存のユーザーにメッセージを送ることができることを意味する。ただし、新規ユーザーへのメッセージングはできない。

[Firebase Cloud Messaging (FCM]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#step-1-enable-firebase)) に移行していない顧客は、この変更の影響を受ける可能性がある。

FCMに移行していない場合、GCMのプッシュトークン登録はすべて失敗する。アプリが現在GCMをサポートしている場合、[GCMからFirebase Cloud Messaging (FCM)への移行について](https://developers.google.com/cloud-messaging/android/android-migrate-fcm)開発者と協力する必要がある。

### エクリプス

**支援は撤回された**：2014-2015<br>
**に取って代わられた**：[Android Studio]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#using-android-studio)

GoogleがEclipse Android Developer Tools（ADT）プラグインの[サポートを終了した](http://android-developers.blogspot.com/2015/06/an-update-on-eclipse-android-developer.html)ため、BrazeはEclipse IDEのサポートを終了した。 

移行前にEclipseとの統合についてサポートが必要な場合は、[サポートに]({{site.baseurl}}/support_contact/)問い合わせること。

### ロー・イベント・ストリーム（RES）

**支援は撤回された**：2018年7月<br>
**に取って代わられた**：[Currents]({{site.baseurl}}/partners/braze_currents/about/)

Rawイベントストリームは[Currentsの]({{site.baseurl}}/partners/braze_currents/about/)前身であり、Brazeデータの将来のために廃止された。

### アイドル時のディレイ - GCM機能

**支援は撤回された**：2016年11月

Delay While Idleパラメータは、以前は[GCMプッシュオプションの](https://developers.google.com/cloud-messaging/http-server-ref)一部であった。グーグルは2016年11月15日、このオプションのサポートを打ち切った。以前は、**trueに**設定すると、デバイスがアクティブになるまでメッセージを送信しないことを表していた。

### カスタムエンドポイント

**支援は撤回された**：2019年12月

顧客エンドポイントの削除。カスタムエンドポイントを持っている場合は、それを使い続けることができるが、Brazeはもうそれを提供しない。


[15]: {% image_buster /assets/img_archive/in-app-choices.png %}
