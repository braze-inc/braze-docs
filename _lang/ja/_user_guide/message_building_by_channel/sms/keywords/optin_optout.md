---
nav_title: Opt-In &amp; Opt-Out キーワード
article_title: SMSオプトイン/オプトアウトキーワード
page_order: 0
description: "ここでは、Braze がSMS メッセージングの基本的なオプトインおよびオプトアウトキーワードを処理する方法について説明します。"
page_type: reference
tool:
  - Dashboard

channel:
  - SMS
---

# オプトインおよびオプトアウトキーワード

> すべてのオプトイン、オプトアウト、ヘルプ/情報キーワード回答に対する回答があることが規定されている。Braze は、以下の_厳密、シングルワード、大文字と小文字を区別しない_メッセージを自動的に処理し、すべての着信リクエストで、ユーザーの[サブスクリプショングループの状態]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/)とそれに関連付けられた電話番号を自動的に更新します。

## キーワードの概要

Braze は次のキーワードs を自動的に処理し、すべての着信リクエストの電話番号のサブスクリプショングループステートを更新します。これらのデフォルト キーワードsとレスポンスもカスタマイズできることに注意してください。 

| タイプ| キーワード| 変更|
\|-|-------|---|
|Opt-in| `START`<br> `YES`<br> `UNSTOP` | これらの`Opt-In` キーワード s のいずれかを含む受信リクエストは、サブスクリプショングループステートを`subscribed` に変更します。さらに、そのサブスクリプショングループに関連付けられた番号の集まりが、その顧客にSMS メッセージを送信できるようになります。<br><br>ユーザーは、定義されたOpt-In 自動応答を受け取ります。|
|Opt-out| `STOP`<br> `STOPALL`<br> `UNSUBSCRIBE`<br> `CANCEL`<br> `END`<br> `QUIT` | これらの`Opt-Out` キーワード s のいずれかを含む受信リクエストは、サブスクリプショングループステートを`unsubscribed` に変更します。さらに、そのサブスクリプショングループに関連付けられている番号の集まりは、その顧客にSMS メッセージを送信できなくなります。<br><br>ユーザーは、定義されたOpt-Out 自動応答を受け取ります。|
| ヘルプ| `HELP`<br> `INFO` | ユーザーは定義されたヘルプ自動応答を受け取ります。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

**exact, single-word message**のみが処理されます(大文字と小文字を区別しません)。`STOP PLEASE` などのキーワードは、[fuzzy opt-out][fuzzylink] がオンになっていない限り無視されます。

受信者がキーワードs `HELP`または`INFO`を使用する場合、レスポンスは自動的にトリガーされます。これらの自動応答メッセージのSMS テンプレートは、[オンボーディング][oblink]および電話番号の取得期間中に設定されます。これらのレスポンスは、最初のオンボーディングの後も更新し続けることができることに注意してください。

{% alert tip %}
オプトアウト処理の拡大に関心があるか?受信メッセージがオプトアウトキーワードと一致せず、オプトアウトインテントを示すときに認識を試みる機能である、[fuzzy opt-out]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/fuzzy_opt_out/) を試します。
{% endalert %}

[oblink]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#setup-process
[fuzzylink]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/fuzzy_opt_out/
