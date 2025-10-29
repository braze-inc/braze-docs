---
nav_title: カレントのイベント変更履歴
page_order: 6
description: "このページには、各Currentsリリースのイベント変更が含まれている。"
tool: Currents
---

# カレントの変更履歴

## バージョン3の変更点（リリース日：2025-10-08）

* 新しいイベントタイプ`users.messages.rcs.Click` を追加した。

* 新しいイベントタイプ`users.messages.rcs.Rejection` を追加した。

* 新しいイベントタイプ`users.messages.line.Abort` を追加した。

* 新しいイベントタイプ`users.messages.line.Send` を追加した。

* 新しいイベントタイプ`users.messages.line.InboundReceive` を追加した。

* 新しいイベントタイプ`users.messages.line.Click` を追加した。

* 新しいイベントタイプ`users.messages.rcs.Delivery` を追加した。

* 新しいイベントタイプ`users.messages.rcs.InboundReceive` を追加した。

* 新しいイベントタイプ`users.messages.rcs.Read` を追加した。

* 新しいイベントタイプ`users.messages.rcs.Send` を追加した。

* 新しいイベントタイプ`users.messages.rcs.Abort` を追加した。

* フィールドはイベントタイプ`users.messages.whatsapp.Send` に変更される：
    * `string` フィールド`flow_id` を追加した：WhatsApp マネージャー内のフロー固有のID。WhatsApp フローに返信するための CTA がメッセージに含まれている場合に表示される。
    * `string` フィールドを追加`template_name` ：[PII] WhatsAppマネージャーのテンプレート名。テンプレートメッセージを送信する場合に提示する。
    * `string` フィールド`message_id` を追加した：このメッセージに対してMetaが生成した一意のID。

* フィールドはイベントタイプ`users.messages.whatsapp.Read` に変更される：
    * `string` フィールドを追加`template_name` ：[PII] WhatsAppマネージャーのテンプレート名。テンプレートメッセージを送信する場合に提示する。
    * `string` フィールド`message_id` を追加した：このメッセージに対してMetaが生成した一意のID。
    * `string` フィールド`flow_id` を追加した：WhatsApp マネージャー内のフロー固有のID。WhatsApp フローに返信するための CTA がメッセージに含まれている場合に表示される。

* フィールドはイベントタイプ`users.messages.whatsapp.InboundReceive` に変更される：
    * `string` フィールド`catalog_id` を追加した：インバウンドメッセージで製品が参照されている場合は、その製品のカタログID。それ以外は空である。
    * `string` フィールド`product_id` を追加した：受信メッセージで製品が参照されている場合は、製品SKU。それ以外は空である。
    * `string` フィールド`flow_id` を追加した：WhatsApp マネージャー内のフロー固有のID。ユーザーがWhatsAppフローに応答している場合に表示される。
    * 新しい`string` フィールド`flow_response_json` を追加した：[PII] ユーザーが回答したフォームの値。ユーザーがWhatsAppフローに応答している場合に表示される。
    * `string` フィールド`message_id` を追加した：このメッセージに対してMetaが生成した一意のID。
    * `string` フィールド`in_reply_to` を追加した：このメッセージが返信したメッセージのmessage_id 

* フィールドはイベントタイプ`users.messages.whatsapp.Failure` に変更される：
    * `string` フィールド`message_id` を追加した：このメッセージに対してMetaが生成した一意のID。
    * `string` フィールドを追加`template_name` ：[PII] WhatsAppマネージャーのテンプレート名。テンプレートメッセージを送信する場合に提示する。
    * `string` フィールド`flow_id` を追加した：WhatsApp マネージャー内のフロー固有のID。WhatsApp フローに返信するための CTA がメッセージに含まれている場合に表示される。

* フィールドはイベントタイプ`users.messages.whatsapp.Delivery` に変更される：
    * `string` フィールド`flow_id` を追加した：WhatsApp マネージャー内のフロー固有のID。WhatsApp フローに返信するための CTA がメッセージに含まれている場合に表示される。
    * `string` フィールドを追加`template_name` ：[PII] WhatsAppマネージャーのテンプレート名。テンプレートメッセージを送信する場合に提示する。
    * `string` フィールド`message_id` を追加した：このメッセージに対してMetaが生成した一意のID。

* フィールドはイベントタイプ`users.messages.sms.Rejection` に変更される：
    * `boolean` フィールド`is_sms_fallback` を追加した：拒否されたRCSメッセージのためにSMSフォールバックメッセージが送信されたことを示す。このメッセージは、配信、配信の失敗、または拒否の原因となる場合があります。これは、送信IDとディスパッチIDを介してRCS拒否イベントにリンクすることができる。
送信 ID とディスパッチ ID を介して RCS 拒否イベントにリンクできます。(イベントプロパティ)

* フィールドはイベントタイプ`users.messages.sms.DeliveryFailure` に変更される：
    * `boolean` フィールド`is_sms_fallback` を追加した：拒否されたRCSメッセージのためにSMSフォールバックメッセージが送信されたことを示す。このメッセージは、配信、配信の失敗、または拒否の原因となる場合があります。これは、送信IDとディスパッチIDを介してRCS拒否イベントにリンクすることができる。

* フィールドはイベントタイプ`users.messages.sms.Delivery` に変更される：
    * `boolean` フィールド`is_sms_fallback` を追加した：拒否されたRCSメッセージのためにSMSフォールバックメッセージが送信されたことを示す。このメッセージは、配信、配信の失敗、または拒否の原因となる場合があります。これは、送信IDとディスパッチIDを介してRCS拒否イベントにリンクすることができる。

