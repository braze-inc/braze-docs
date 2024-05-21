---
nav_title: "ユーザーオプトインの収集"
article_title: ユーザSMS Opt-Ins を収集するためのベストプラクティス
page_order: 7
description: "この参照記事では、ユーザーオプトインを収集するための3つのベストプラクティスについて説明します。"
page_type: reference
channel:
  - SMS
  
---

# ユーザーオプトインの収集

> 次の記事では、いくつかの一般的なSMSオプトインメソッドをリストします。

## オプション 1:ユーザに短いコードまたは長いコードのテキストを要求する

ユーザにテキスト"START"、"UNSTOP"、"YES"、またはカスタムのopt-inキーワードを番号に入力してサブスクリプショングループに自動的に追加するように依頼します。ウェブサイト、モバイルアプリ、または広告では、ユーザにオプトインするようにこれを要求することができ、助けになるならインセンティブを提供することができます。

## オプション 2:アプリ内メッセージでユーザーがオプトイン

アプリ内メッセージからSMSを選択できるようにするには、Brazeが提供する[電話番号キャプチャフォーム]({{site.baseurl}}//user_guide/message_building_by_channel/in-app_messages/drag_and_drop/templates/phone_number_capture/)を使用して、電話番号を収集し、SMSリストを拡大できるブランドフォームを作成します。

![][3]{: style="max-width:30%;"}

また、[SMS double opt-in]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/sms_double_opt_in/)機能を使用することをお勧めします。この機能は、アプリ内メッセージ電話番号キャプチャフォームで自動的に動作し、フォーム経由で電話番号を送信した後、ユーザに自分の意図を確認するように促します。

## オプション 3: サインアップフロー

新しいユーザーがウェブサイトやアプリにサインアップしたり登録したりするときは、電話番号やメールアドレスを尋ねてください。プロモーションメールやSMSを受信するには、チェックボックスを選択します。 

ユーザーがサインアップしたら、次の手順を実行します。

1. [`/subscription/status/set` endpoint]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/#update-users-subscription-group-status) を使用してユーザーを作成し、その属性を保存します。

```json
POST 'https://rest.iad-03.braze.com/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_group_id": "xyz-abcd-1234567",
  "subscription_state": "subscribed",
  "external_id": "external_identifier",
  "phone": "+12223334444"
}
'
```

{: start="2"}
2\.ユーザをSMS に登録するには、[`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) を使用します。

```json
POST `https://rest.aid-03.braze.com/users/track` \
--header `Content-Type: application/json` \
--header `Authorization: Bearer YOUR-REST-API-KEY` \
--data-raw `{
"attributes" : [
Unknown macro: { "external_id" }
]
}
```

[1]: {% image_buster /assets/img/sms/opt-in1.png %}
[2]: {% image_buster /assets/img/sms/opt-in2.png %}
[3]: {% image_buster /assets/img_archive/dnd_iam_phone_capture_select.png %}