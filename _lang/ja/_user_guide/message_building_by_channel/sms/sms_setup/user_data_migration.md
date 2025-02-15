---
nav_title: "ユーザーデータ移行"
article_title: ユーザーデータ移行
page_order: 4
description: "このリファレンス記事では、ユーザーデータをBrazeに移行する際に考慮すべきすべての事項について説明します。"
page_type: reference
channel:
  - SMS
noindex: true

---

# ユーザーデータ移行

> この記事では、ユーザーデータをBrazeに移行する際に考慮すべきすべての事項について説明します。

## キャリア標準に合わせてユーザーの電話番号をフォーマットする

電話会社にはE.164と呼ばれる特定の形式があり、これは各デバイスにグローバルに一意の番号が割り当てられることを保証する国際電話番号計画です。これにより、電話やテキストメッセージが異なる国の個々の電話に正しくルーティングされるようになります。E.164番号は次の画像のようにフォーマットされ、最大15桁まで可能です。

![E.164 フォーマットは、プラス記号、国コード、地域コード、電話番号で構成されています][picture]{: style="max-width:50%;border: 0;"}

詳細については、[ユーザーの電話番号][userphone]を参照してください。

## ユーザーのサブスクリプション状態に関する履歴情報を更新する

ユーザーの[購読状態][購読状態] のさまざまなメッセージングチャネルに関する履歴情報がある場合は、必ず Braze でこの情報を更新してください。

## 例の移行手順

Brazeを通じてSMSキャンペーンを作成し始める前に、すべてが正常に機能するようにユーザーデータを更新する必要があります。

**こちらは、Brazeで更新する必要があるユーザーデータの簡単な概要です:**

1. **ユーザーの電話番号を正しい形式でインポートする** ([E.164][0]) フォーマットにはプラス記号（+）と国コードが必要です。例としては+12408884782です。ユーザーの電話番号のインポート方法の詳細については、[ユーザーの電話番号][userphone]をご覧ください。
    * [`/users/track`エンドポイント][1]を使用して`phone`値を割り当てます。<br><br>

2. 情報がある場合、**ユーザーの SMS [購読状態][購読状態] を割り当てます** (配信登録済み、配信停止済みなど)。
    * [`/subscription/status/set`エンドポイント][6]を使用して、ユーザーをSMSサブスクリプショングループにサブスクライブまたはサブスクライブ解除として設定します。

{% alert note %}
ダッシュボードでSMSサブスクリプショングループを設定した後、APIリクエストに必要な関連する`subscription_group_id`を取得できるようになります。
{% endalert %}

[0]: https://en.wikipedia.org/wiki/E.164
[userphone]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/
[1]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[2]: {{site.baseurl}}/api/endpoints/user_data/post_user_alias/
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#aliasing-users
[4]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/#aliasing-users
[5]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/#aliasing-users
[6]: {{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/
[picture]: {% image_buster /assets/img/sms/e164.jpg %}
[customkeyword]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/custom_keyword_handling/
[subscriptionstate]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#sms-subscription-states
