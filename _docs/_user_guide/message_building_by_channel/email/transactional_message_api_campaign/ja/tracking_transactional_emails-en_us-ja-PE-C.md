---
nav_title: トランザクションメールの追跡
article_title: トランザクションメールの追跡
page_order: 1
description: "この参考記事では、トランザクションメールキャンペーンのリアルタイムトラッキングの設定方法について説明する。"
page_type: reference
tool:
  - Campaigns
channel: email

---

# トランザクションメールの追跡

> このページでは、[トランザクションメールキャンペーン]({{site.baseurl}}/user_guide/message_building_by_channel/email/transactional_message_api_campaign/)のリアルタイム追跡を設定する方法について説明します。エンドポイント自体の詳細については、[API トリガー配信を使用したトランザクションメールの送信]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message/)を参照してください。

注文の確認やパスワードの再設定など、トランザクションメールを送信する場合、それが顧客に届いているかどうかを知ることは不可欠である。Braze のトランザクション HTTP イベントポストバックを使用すると、すべてのトランザクションメールのステータスに関するインサイトをリアルタイムで取得できるため、問題が発生した場合に迅速に対応することができます。

この機能を使用して、次のことを行います。

- **リアルタイムでメールを監視する：**メッセージが送信、処理、配信されたか、問題が発生したかを即座に確認できる。
- **プロアクティブに対応する：**メッセージを再試行したり、SMSのような別のチャネルに切り替えたり、フォールバック・システムを使用して、コミュニケーションが確実に届くようにする。

## トランザクションメールのトラッキング

{% multi_lang_include http_event_postback.md %}


