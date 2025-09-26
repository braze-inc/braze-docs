---
nav_title: "ユーザーのオプトインの収集"
article_title: ユーザーの SMS オプトイン収集のベストプラクティス
page_order: 7
description: "このリファレンス記事では、ユーザーのオプトインを収集するための3つのベストプラクティスについて説明します。"
page_type: reference
channel:
  - SMS
  
---

# ユーザーのオプトインの収集

> 次の記事では、一般的なSMSオプトイン方法をいくつか紹介します。

## オプション 1: ユーザーに短いコードまたは長いコードをテキストするように依頼します

ユーザーに「START」、「UNSTOP」、「YES」、またはカスタムオプトインキーワードをあなたの番号にテキストメッセージで送信するように依頼して、サブスクリプショングループに自動的に追加します。Web サイト、モバイルアプリ、またはさらに広告で、ユーザーにこの操作によるオプトインを依頼し、役立つ場合はインセンティブを提供できます。

## オプション 2: ユーザーがアプリ内メッセージでオプトインします

ユーザーがアプリ内メッセージからSMSにオプトインできるようにするには、Brazeが提供する[電話番号キャプチャフォーム]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/templates/phone_number_capture/)を使用して、電話番号を収集し、SMSリストを拡大するためのブランド化されたフォームを作成します。

![電話番号をキャプチャするためのテンプレートが表示されているアプリ内メッセージ作成画面。]({% image_buster /assets/img_archive/dnd_iam_phone_capture_select.png %}){: style="max-width:80%;"}

Brazeは、[SMSダブルオプトイン]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/double_opt_in/)機能も使用することをお勧めします。この機能は、アプリ内メッセージの電話番号キャプチャフォームと自動的に連携し、ユーザーがフォームから電話番号を送信した後にその意志を確定するように促します。

## オプション 3: サインアップフロー

新規ユーザーが Web サイトやアプリにサインアップしたり、登録したりするときに、電話番号とメールアドレスを入力するように求めます。プロモーションメールとSMSを受信するためのチェックボックスを含めてください。 

ユーザーがサインアップした後、次のことを行ってください:

1. [`/subscription/status/set`エンドポイント]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/#update-users-subscription-group-status)を使用してユーザーを作成し、その属性を保存します。

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
2\.[`/users/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)を使用して、ユーザーをSMSに登録します。

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

