---
nav_title: "ユーザーデータの移行"
article_title: ユーザーデータの移行
page_order: 4
description: "このリファレンス記事では、ユーザーデータをBrazeに移行する際に注意すべき点をすべて説明しています。"
page_type: reference
channel:
  - SMS
noindex: true

---

# ユーザーデータの移行

> この記事では、ユーザーデータをBrazeに移行する際に注意すべき点を説明します。

## ユーザーの電話番号をキャリアの標準に合わせる

電話キャリアは、E.164と呼ばれる国際電話番号計画で、各デバイスがグローバルに一意な番号を持つことを保証する、特定の種類のフォーマットを期待している。これにより、電話やテキストメッセージが、異なる国の個々の電話に正しくルーティングされる。E.164番号は以下の画像のようにフォーマットされ、最大15桁まで設定できます。

E.164形式はプラス記号、国番号、市外局番、電話番号で構成される][写真]。{: style="max-width:50%;border: 0;"}

詳しくは、[ユーザーの電話][userphone]番号を参照してください。

## ユーザーの購読状態に関する履歴情報の更新

様々なメッセージングチャンネルのユーザーの[購読状態][subscriptionstate]に関する履歴情報がある場合は、必ずBrazeで更新してください。

## 移行手順の例

Brazeを使ってSMSキャンペーンを作成する前に、ユーザーデータを更新して、このすべてが機能するようにする必要があります。

**Brazeで更新する必要があるユーザーデータを簡単にまとめました：**

1. **ユーザーの電話番号を正しいフォーマット**[（E.164][0]**）でインポート**する フォーマットには、プラス記号（+）と国コードが必要です。例えば、+12408884782である。ユーザーの電話番号をインポートする方法の詳細については、[ユーザーの電話番号を][userphone]ご覧ください。
    * `phone` の値を割り当てるには、[`/users/track` エンドポイントを][1]使用する。<br><br>

2. **ユーザーのSMS[購読状態][subscriptionstate]**(購読済みや購読解除など)の情報があれば、**それを割り当てて**ください。
    * [`/subscription/status/set` エンドポイントを][6]使用して、ユーザーを SMS サブスクリプショングループの購読または購読解除に設定します。

{% alert note %}
ダッシュボードでSMSサブスクリプショングループを設定したら、APIリクエストに必要な関連`subscription_group_id` 。
{% endalert %}

[0]: https://en.wikipedia.org/wiki/E.164
[userphone]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/
[1]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[2]: {{site.baseurl}}/api/endpoints/user_data/post_user_alias/
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#aliasing-users
[4]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/#aliasing-users
[5]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/#aliasing-users
[6]: {{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/
[写真]： {% image_buster /assets/img/sms/e164.jpg %}
[customkeyword]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/custom_keyword_handling/
[subscriptionstate]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#sms-subscription-states
