---
nav_title: プッシュ設定
article_title: プッシュ設定
page_order: 16
page_type: reference
description: "この記事では、Braze ダッシュボードのプッシュ設定の概要について説明します。"
channel: push

---

# プッシュ設定

> **Push Settings** ページでは、Push Time to Live (TTL) やAndroid キャンペーンのデフォルトのFCM 優先度など、プッシュ通知のキー設定を行うことができます。これらの設定により、プッシュ通知の配信と効果が最適化され、ユーザーの体験が向上します。

## プッシュTTLとは。

Push Time to Live (TTL) は、キャンペーンの送信時にオフラインのデバイスにBraze がプッシュ通知を配信しようとする時間を制御します。TTL の有効期限が切れた後にデバイスが再接続された場合、メッセージは配信されません。この設定では、ユーザのデバイスがすでに受信している通知は削除されません。プッシュプロバイダが通知を配信しようとする時間のみが制御されます。

## デフォルトのプッシュTTL 値の設定

デフォルトでは、Braze はプッシュ TTL を各プッシュメッセージングサービスの最大値に設定します。 

| プッシュメッセージングサービス | 最大TTL |
| --- | --- |
| ウェブ(FCM または Web プッシュサービス経由) | 28日 |
| Firebase クラウドメッセージング (FCM) | 28日 |
| Kindle (ADM) | 31日 |
| Huawei (HMS) | 15日間 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

これらの設定は、特定のメッセージに別のTTL が設定されていない限り、すべてのプッシュキャンペーンにグローバルに適用されます。メッセージのTTL を調整するには、[詳細なキャンペーン設定]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/advanced_campaign_settings/#ttl)を参照してください。

別のデフォルトのプッシュTTL を設定するには:

1. [**設定**] > [**設定の管理**] > [**プッシュ設定**] に移動します。
2. Android プラットフォームごとに、デフォルトの有効期限値を定義します。より正確な制御を行うには、時間や秒などのより小さな増分を設定できます。
3. **Save**を選択して変更を適用します。

![Firebase、Web、Kindle、HuaweiデバイスのTTL設定をプッシュする。]({% image_buster /assets/img/push_ttl.png %})

## Android キャンペーンのデフォルトのFCM 優先順位

すべてのAndroid プッシュキャンペーンのデフォルトのFirebase Cloud Messaging (FCM) 優先順位を設定できます。この優先度によって、プッシュ通知をユーザーのデバイスに配信する方法が決まります。

FCM の優先順位オプションは次のとおりです。

| 優先順位 | 説明 | ユースケース |
| --- | --- | --- |
| 通常 | バッテリーの使用量に合わせて最適化された標準の配信優先度 | 即座に注意を払う必要のないコンテンツ |
| 高 | メッセージはすぐに送信されます | 迅速な配信を必要とする時間的制約がある通知 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

デフォルトの FCM 優先度を設定するには、次のようにします。

1. [**設定**] > [**設定の管理**] > [**プッシュ設定**] に移動します。
2. [FCM 優先度] セクションで、デフォルト設定として [通常] または [高] のいずれかを選択します。
3. **Save**を選択して変更を適用します。

![Androidの配信優先度設定。]({% image_buster /assets/img/push_fcm_priority_settings.png %})

この設定は、特定のキャンペーンの作成時に別の優先順位が選択されていない限り、すべての新しいAndroid プッシュキャンペーンにグローバルに適用されます。 

{% alert note %}
ユーザーに表示される通知やユーザーの関与が発生しない優先度の高いメッセージがアプリから頻繁に送信されることをFCMが検出した場合、それらのメッセージは自動的に通常の優先度に廃止される可能性があります。
{% endalert %}

FCM の優先順位レベルと非劣化の詳細については、[詳細なキャンペーン設定]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/advanced_campaign_settings/#fcm-priority)を参照してください。

