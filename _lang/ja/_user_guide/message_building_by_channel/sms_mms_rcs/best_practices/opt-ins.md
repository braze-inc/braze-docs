---
nav_title: "ユーザーのオプトインの収集"
article_title: ユーザーの SMS オプトイン収集のベストプラクティス
page_order: 7
description: "この参照記事では、ユーザーのオプトインを収集するための3つのベストプラクティスについて説明します。"
page_type: reference
channel:
  - SMS
  
---

# ユーザーのオプトインの収集

> この記事では、一般的な SMS オプトイン方法をいくつか紹介します。

## オプション 1: ユーザーにショートコードまたはロングコードへのテキスト送信を依頼する

ユーザーに「START」、「UNSTOP」、「YES」、またはカスタムオプトインキーワードをあなたの番号にテキストメッセージで送信するように依頼して、サブスクリプショングループに自動的に追加します。Web サイト、モバイルアプリ、さらには広告で、ユーザーにこの操作によるオプトインを依頼できます。必要に応じてインセンティブを提供することも可能です。

## オプション 2: ユーザーがアプリ内メッセージからオプトインする

ユーザーがアプリ内メッセージから SMS にオプトインできるようにするには、Braze が提供する[電話番号キャプチャフォーム]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/templates/phone_number_capture/)を使用して、電話番号を収集し、SMS リストを拡大するためのブランド化されたフォームを作成します。

![電話番号取得用のテンプレート付きアプリ内メッセージ作成画面。]({% image_buster /assets/img_archive/dnd_iam_phone_capture_select.png %}){: style="max-width:80%;"}

Braze では、[SMS ダブルオプトイン]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/double_opt_in/)機能も併せて使用することをお勧めします。この機能は、アプリ内メッセージの電話番号キャプチャフォームと自動的に連携し、ユーザーがフォームから電話番号を送信した後にその意思を確認するよう促します。

## オプション 3: サインアップフロー

新規ユーザーが Web サイトやアプリにサインアップまたは登録する際に、電話番号とメールアドレスの入力を求めます。プロモーションメールと SMS を受信するためのチェックボックスを含めてください。 

ユーザーがサインアップした後、以下を行います:

1. [`/subscription/status/set` エンドポイント]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/#update-users-subscription-group-status)を使用してユーザーを作成し、その属性を保存します。

```http
POST 'https://rest.iad-03.braze.com/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_group_id": "xyz-abcd-1234567",
  "subscription_state": "subscribed",
  "external_id": "external_identifier",
  "phone": "+12223334444",
  "use_double_opt_in_logic": true
}
'
```

{: start="2"}
2. [`/users/track` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)を使用して、ユーザーを SMS に登録します。

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "attributes": [
    {
      "external_id": "external_identifier",
      "phone": "+12223334444",
      "subscription_groups": [
        {
          "subscription_group_id": "xyz-abcd-1234567",
          "subscription_state": "subscribed",
          "use_double_opt_in_logic": true
        }
      ]
    }
  ]
}'
```

{% alert tip %}
REST API を通じてユーザーを登録する際に [SMS ダブルオプトイン]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/double_opt_in/)ワークフローに入れるには、リクエストで `use_double_opt_in_logic` パラメーターを `true` に設定します。このパラメーターを省略すると、ユーザーはダブルオプトインの確認を受け取ることなく登録されます。

このパラメーターは以下のエンドポイントでサポートされています:<br><br>
- [`/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/)
- [`/v2/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status_v2/)
- [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)
{% endalert %}