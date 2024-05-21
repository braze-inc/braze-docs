---
nav_title: Opt-In & Opt-Out キーワード
article_title: SMSオプトイン/オプトアウトキーワード
page_order: 0
description: "このリファレンス記事では、Braze がSMS メッセージングの基本的なオプトインおよびオプトアウトキーワードを処理する方法について説明します。"
page_type: reference
tool:
  - Dashboard

channel:
  - SMS
---

# オプトインキーワードとオプトアウトキーワード

> 規則では、すべてのオプトイン、オプトアウト、およびhelp/infoキーワード応答に対する応答があることが要求されています。Braze は、以下の_正確、単語、大文字と小文字を区別しない_ メッセージを自動的に処理し、すべての受信リクエストで、ユーザとその関連する電話番号の[サブスクリプションググループの状態]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/) を自動的に更新します。

## キーワードの概要

Braze は次のキーワードを自動的に処理し、すべての着信リクエストの電話番号のサブスクリプショングループの状態を更新します。これらのデフォルトのキーワードと応答もカスタマイズできることに注意してください。 

| タイプ| キーワード| 変更|
|-|-------|---|
|Opt-in| `START`<br> `YES`<br> `UNSTOP` | これらの`Opt-In` キーワードのいずれかを含むインバウンド要求は、サブスクリプショングループの状態が`subscribed` に変わります。さらに、そのサブスクリプショングループに関連付けられた番号のプールで、その顧客にSMS メッセージを送信できるようになります。<br><br>ユーザーは、定義されたOpt-In 自動応答を受け取ります。|
|Opt-out| `STOP`<br> `STOPALL`<br> `UNSUBSCRIBE`<br> `CANCEL`<br> `END`<br> `QUIT` | これらの`Opt-Out` キーワードのいずれかを含むインバウンド要求は、サブスクリプショングループの状態が`unsubscribed` に変わります。さらに、そのサブスクリプショングループに関連付けられている番号のプールは、その顧客にSMS メッセージを送信できなくなります。<br><br>ユーザーは、定義されたOpt-Out 自動応答を受け取ります。|
| ヘルプ| `HELP`<br> `INFO` | ユーザーは定義されたヘルプ自動応答を受け取ります。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

**exact, single-word message**のみが処理されます(大文字と小文字を区別しません)。`STOP PLEASE` などのキーワードは、[fuzzy opt-out][fuzzylink] がオンになっていない限り無視されます。

受信者がキーワード`HELP` または`INFO` を使用すると、応答が自動的にトリガされます。これらの自動応答メッセージのSMSテンプレートは、[オンボーディング][oblink]および電話番号の調達期間中に設定されます。これらの応答は、最初のオンボーディング期間の後も更新し続ける可能性があることに注意してください。

{% alert tip %}
オプトアウト処理の拡大に関心があるか?[fuzzy opt-out]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/fuzzy_opt_out/) を試します。これは、受信メッセージがオプトアウトキーワードに一致しないが、オプトアウトインテントを示すときに認識しようとする機能です。
{% endalert %}

[oblink]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#setup-process
[fuzzylink]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/fuzzy_opt_out/
