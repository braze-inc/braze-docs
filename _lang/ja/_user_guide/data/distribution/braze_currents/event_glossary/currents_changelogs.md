---
nav_title: Currentsイベントチェンジログ
page_order: 6
description: "このページには、Currentsのリリースごとのイベント変更が含まれます。"
tool: Currents
---

# Currents変更ログ

## バージョン3 の変更点(リリース日2025-10-08)

* 新しいイベントタイプ`users.messages.rcs.Click`を追加しました。

* 新しいイベントタイプ`users.messages.rcs.Rejection`を追加しました。

* 新しいイベントタイプ`users.messages.line.Abort`を追加しました。

* 新しいイベントタイプ`users.messages.line.Send`を追加しました。

* 新しいイベントタイプ`users.messages.line.InboundReceive`を追加しました。

* 新しいイベントタイプ`users.messages.line.Click`を追加しました。

* 新しいイベントタイプ`users.messages.rcs.Delivery`を追加しました。

* 新しいイベントタイプ`users.messages.rcs.InboundReceive`を追加しました。

* 新しいイベントタイプ`users.messages.rcs.Read`を追加しました。

* 新しいイベントタイプ`users.messages.rcs.Send`を追加しました。

* 新しいイベントタイプ`users.messages.rcs.Abort`を追加しました。

* フィールドがイベントタイプ`users.messages.whatsapp.Send` に変更されました。
    * 新しい`string` フィールド `flow_id` を追加しました。WhatsAppマネージャのフローの一意のID。WhatsAppの流れに応答するためのCTAがメッセージに含まれている場合に存在する
    * 新しい`string` フィールド `template_name`: [PII] WhatsAppマネージャのテンプレートの名前を追加しました。テンプレートメッセージを送信する場合に表示します
    * 新しい`string` フィールド `message_id` を追加しました。このメッセージのメタによって生成される一意のID

* フィールドがイベントタイプ`users.messages.whatsapp.Read` に変更されました。
    * 新しい`string` フィールド `template_name`: [PII] WhatsApp マネージャーのテンプレートの名前を追加しました。テンプレートメッセージを送信する場合に表示します
    * 新しい`string` フィールド `message_id` を追加しました。このメッセージのメタによって生成される一意のID
    * 新しい`string` フィールド `flow_id` を追加しました。WhatsAppマネージャのフローの一意のID。WhatsAppの流れに応答するためのCTAがメッセージに含まれている場合に存在する

* フィールドがイベントタイプ`users.messages.whatsapp.InboundReceive` に変更されました。
    * 新しい`string` フィールド `catalog_id` を追加しました。製品がインバウンドメッセージで参照されている場合の製品のカタログ ID。それ以外の場合は、空です。
    * 新しい`string` フィールド `product_id` を追加しました。製品がインバウンドメッセージで参照されている場合の製品 SKU。それ以外の場合は、空です。
    * 新しい`string` フィールド `flow_id` を追加しました。WhatsAppマネージャのフローの一意のID。ユーザーがWhatsAppの流れに反応している場合に表示されます。
    * 新しい`string` フィールド `flow_response_json`: [PII] ユーザーが応答したフォーム値を追加しました。ユーザーがWhatsAppの流れに反応している場合に表示されます。
    * 新しい`string` フィールド `message_id` を追加しました。このメッセージのメタによって生成される一意のID
    * 新しい`string` フィールド `in_reply_to` を追加しました。このメッセージが応答していたメッセージのmessage_id

* フィールドがイベントタイプ`users.messages.whatsapp.Failure` に変更されました。
    * 新しい`string` フィールド `message_id` を追加しました。このメッセージのメタによって生成される一意のID
    * 新しい`string` フィールド `template_name`: [PII] WhatsApp マネージャーのテンプレートの名前を追加しました。テンプレートメッセージを送信する場合に表示します
    * 新しい`string` フィールド `flow_id` を追加しました。WhatsAppマネージャのフローの一意のID。WhatsAppの流れに応答するためのCTAがメッセージに含まれている場合に存在する

* フィールドがイベントタイプ`users.messages.whatsapp.Delivery` に変更されました。
    * 新しい`string` フィールド `flow_id` を追加しました。WhatsAppマネージャのフローの一意のID。WhatsAppの流れに応答するためのCTAがメッセージに含まれている場合に存在する
    * 新しい`string` フィールド `template_name`: [PII] WhatsApp マネージャーのテンプレートの名前を追加しました。テンプレートメッセージを送信する場合に表示します
    * 新しい`string` フィールド `message_id` を追加しました。このメッセージのメタによって生成される一意のID

* フィールドがイベントタイプ`users.messages.sms.Rejection` に変更されました。
    * 新しい`boolean` フィールド `is_sms_fallback` を追加しました。受信拒否されたRCSメッセージにより、SMS フォールバックメッセージが送信されたことを示します。このメッセージは、配信、配信の失敗、または拒否の原因となる場合があります。送信ID およびディスパッチID を介してRCS 拒否イベントにリンクできます
送信 ID とディスパッチ ID を介して RCS 拒否イベントにリンクできます。(事象プロパティ)

* フィールドがイベントタイプ`users.messages.sms.DeliveryFailure` に変更されました。
    * 新しい`boolean` フィールド `is_sms_fallback` を追加しました。受信拒否されたRCSメッセージにより、SMS フォールバックメッセージが送信されたことを示します。このメッセージは、配信、配信の失敗、または拒否の原因となる場合があります。送信ID およびディスパッチID を介してRCS 拒否イベントにリンクできます

* フィールドがイベントタイプ`users.messages.sms.Delivery` に変更されました。
    * 新しい`boolean` フィールド `is_sms_fallback` を追加しました。受信拒否されたRCSメッセージにより、SMS フォールバックメッセージが送信されたことを示します。このメッセージは、配信、配信の失敗、または拒否の原因となる場合があります。送信ID およびディスパッチID を介してRCS 拒否イベントにリンクできます

