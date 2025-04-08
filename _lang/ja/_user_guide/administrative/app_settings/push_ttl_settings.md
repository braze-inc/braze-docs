---
nav_title: プッシュ TTL の設定
article_title: プッシュ TTL の設定
page_order: 16
page_type: reference
description: "このリファレンス記事では、Braze ダッシュボードの [プッシュ TTL の設定] ページについて説明します。"
channel: push

---

# プッシュ TTL の設定

> Braze ダッシュボードの [プッシュ TTL の設定] ページについて学びましょう。

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

1. [**設定**] > [**設定の管理**] > [**プッシュ TTL の設定**] に移動します。
2. Android プラットフォームごとに、デフォルトの有効期限値を定義します。より正確な制御を行うには、時間や秒などのより小さな増分を設定できます。
3. **Save**を選択して変更を適用します。

![「設定の管理」の「プッシュ TTL の設定」タブ][1]


[1]: {% image_buster /assets/img/push_ttl.png %}
