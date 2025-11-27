---
nav_title: オプトイン/オプトアウトのキーワード
article_title: SMSオプトイン/オプトアウトキーワード
page_order: 0
description: "この記事では、Braze が SMS メッセージングの基本的なオプトイン/オプトアウトのキーワードを処理する方法について説明します。"
page_type: reference
alias: /optin_optout/
tool:
  - Dashboard

channel:
  - SMS
---

# オプトインおよびオプトアウトキーワード

> 規制ではすべてのオプトイン、オプトアウト、およびヘルプ/情報のキーワード応答に対する応答があることが要求されています。Braze は、以下の_厳密、シングルワード、大文字と小文字を区別しない_メッセージを自動的に処理し、すべての着信リクエストで、ユーザーの[サブスクリプショングループの状態]({{site.baseurl}}/sms_rcs_subscription_groups/)とそれに関連付けられた電話番号を自動的に更新します。

## キーワードの概要

Braze は以下のキーワードを自動的に処理し、すべてのインバウンドリクエストの電話番号の購読グループの状態を更新します。これらのデフォルトキーワードと応答もカスタマイズできることに注意してください。 

| タイプ| キーワード| 変更|
\|-|-------|---|
|Opt-in| `START`<br> `YES`<br> `UNSTOP` | これらの `Opt-In` キーワードのいずれかを含むインバウンドリクエストは、購読グループの状態を `subscribed` に変更します。さらに、そのサブスクリプショングループに関連付けられている送信者のプールが、その顧客に (送信者がサポートしているメッセージングのタイプに応じて) SMS、MMS、または RCS メッセージを送信できるようになります。<br><br>ユーザーは、定義されているオプトイン自動応答を受け取ります。|
|Opt-out| `STOP`<br> `STOPALL`<br> `UNSUBSCRIBE`<br> `CANCEL`<br> `END`<br> `QUIT` | これらの `Opt-Out` キーワードのいずれかを含むインバウンドリクエストは、購読グループの状態を `unsubscribed` に変更します。さらに、そのサブスクリプショングループに関連付けられている番号のプールは、その顧客に SMS メッセージを送信できなくなります。<br><br>ユーザーは、定義されているオプトアウト自動応答を受け取ります。|
| ヘルプ| `HELP`<br> `INFO` | ユーザーは、定義されているヘルプ自動応答を受け取ります。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

**exact, single-word message**のみが処理されます(大文字と小文字を区別しません)。`STOP PLEASE` などのキーワードは、[fuzzy opt-out]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/fuzzy_opt_out/) がオンになっていない限り無視されます。

受信者がキーワード `HELP` または `INFO` を使用する場合、応答は自動的にトリガーされます。これらの自動応答メッセージのデフォルト応答は、[オンボーディング]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#setup-process)および電話番号の取得期間中に設定されます。これらの応答は、最初のオンボーディングの後も更新し続けることができることに注意してください。

{% alert tip %}
オプトアウト処理の拡張を検討されている場合、受信メッセージがオプトアウトキーワードと一致せず、オプトアウトインテントを示すときに認識を試みる機能である、[fuzzy opt-out]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/fuzzy_opt_out/) を試します。
{% endalert %}

