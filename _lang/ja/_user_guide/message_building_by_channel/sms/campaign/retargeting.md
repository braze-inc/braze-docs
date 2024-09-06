---
nav_title: ユーザー リターゲティング
article_title: SMS ユーザー リターゲティング
description: "この記事では、ユーザーがSMSのやり取りによってメッセージをリターゲティングする方法について説明します。"
page_type: reference
tool:
  - Campaigns
channel:
  - SMS

---

# ユーザー リターゲティング

> ユーザーのサブスクリプション状態を変更し、受信キーワードに基づいて自動応答を送信することに加えて、Brazeはフィルタリングおよびメッセージのトリガーのためにユーザープロファイルに対話を記録します。<br><br>これらのフィルターとトリガーを使用すると、SMSメッセージを受信したユーザー、特定のSMSキャンペーンからSMSメッセージを受信したユーザーをフィルターし、ユーザーが特定のSMSキャンペーンからSMSメッセージを受信するときにメッセージをトリガーできます。 

{% alert tip %}
これらのリターゲティングオプションを活用するためのカスタムキーワードと双方向メッセージングの設定方法について詳しくは、当社の[カスタムキーワード]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/keyword_handling/)記事をご覧ください。
{% endalert %}  

## リターゲティングオプション

{% alert note %}
ユーザーリターゲティングを使用してオーディエンスを構築する際に、ユーザーの好みに基づいて特定のユーザーを含めたり除外したりすることを希望する場合があります。また、CUPの下での「販売または共有しない」権利などのプライバシー法を遵守するために必要です。マーケターは、キャンバスおよび/またはキャンペーンエントリ基準内でユーザーの適格性に関連するフィルターを実装する必要があります。
{% endalert %}

### SMSでユーザーをフィルター

ユーザーは、最後にSMSを受信した時期や特定のSMSキャンペーンからSMSを受信したかどうかでフィルタリングできます。フィルターはキャンペーンビルダーのターゲットユーザーステップで設定できます。 

**フィルター by last received SMS**<br>
![セグメンテーション フィルター 2020年12月8日以降に受信した最後のSMS。][2]

**フィルター by received messages from SMS キャンペーン**<br>
特定のSMSキャンペーンからメッセージを受信したユーザーをフィルタリングします。このフィルターを使用すると、SMSキャンペーンからメッセージを受信していないものをフィルターオフするオプションもあります。<br>
![セグメンテーションフィルターはキャンペーン「SMSリターゲティング」からメッセージを受信しました。][1]

### ユーザーがSMSを受信するときに{#trigger-messages}トリガーメッセージを送信する

特定のキャンペーンからSMSメッセージを受信したときにメッセージをトリガーするには、トリガーアクションとして**キャンペーンと対話**を選択します。次に、**SMSを受信**および使用したいSMSキャンペーンを選択します。

![][3]

### フィルター by advanced トラッキング links

キャンペーンをクリックしたユーザーをリターゲティングするには、[高度なトラッキングリンク]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/link_shortening/)を使用します。
高度なトラッキングが有効になっているキャンペーンのみが、次のドロップダウンに表示されます:

**リターゲティングするユーザーは特定のSMSキャンペーンをクリックしました**
1. **キャンペーン** フィルターを使用してセグメントを作成します。
2. **クリックされたSMS**を選択します。
3. 希望のキャンペーンを選択してください。

![][15]

**特定のキャンバスステップをクリックしたユーザーをリターゲティングする**
1. **クリック/オープンされたステップ**フィルターを使用してセグメントを作成します。
2. **クリックされたSMS**を選択します。
3. 希望のキャンバスとキャンバスステップを選択します。

![][16]

## キーワード カテゴリ固有のリターゲティング

デフォルトのキーワードカテゴリ（オプトイン、オプトアウト、ヘルプ）に加えて、独自のキーワードカテゴリを最大25個作成することもでき、任意のキーワードと応答を識別できます。これらのカテゴリは、フィルタリングおよびリターゲティングに使用できます。SMSキーワードカテゴリとその設定方法の詳細については、[SMSリターゲティング]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/)を参照してください。 

### フィルターで新しい順に並べ替え

ユーザーがSMSプログラムに応答する最近度のフィルター。このフィルターは、ユーザーがキーワードカテゴリの1つに含まれる受信SMSを送信した最終日付を評価します。 

![セグメンテーションフィルター 最後に送信されたSMSは、2020年8月11日以降に「オプトイン」というキーワードを含む「マーケティングSMS」というサブスクリプショングループに送信されました。][6]

### キャンペーンまたはキャンバスアトリビューションでフィルター

特定のSMSキャンペーンまたはキャンバスコンポーネント、キーワードカテゴリ、またはタグに返信したユーザーをフィルターします。

**特定のキャンペーンカテゴリに返信されたフィルター**<br>
![キャンペーン with the フィルター "Has replied to SMS" for キャンペーン "SMS-283" "Promotion".フィルターの下で、機能は「このフィルターは、アクティブなキャンペーンで使用されていない場合、「プロモーション」から最後のメッセージが送信されてから25か月後に期限切れになります。」と述べています。][12]

**フィルター by replied to a キャンペーン or キャンバス with a specific タグ**
![キャンペーン with the フィルター "Has replied to SMS" for キャンペーン or キャンバス with タグ "Curbside メッセージング Service C".][13]

**フィルター by replied to a specific ステップ**
![キャンペーン with the フィルター "Has replied to SMS" for ステップ "SMS Double Opt" "ステップ - Help".][11]

### キーワードでトリガーメッセージ

メッセージは、ユーザーがキーワードカテゴリ（ユーザーがキーワードのいずれかを送信した場合）または他のキーワード（ユーザーが既存のカテゴリのいずれかに該当しないキーワードを送信した場合）に基づいてメッセージを送信するとトリガーされることがあります。これらのトリガーは、キャンペーンビルダーの配信ステップで設定されます。

定義されたトリガーイベントに受信メッセージが一致するかどうかを評価する際、評価が始まる前に前後のスペースが削除されます。

{% alert tip %}
アクションベースのキャンバスがインバウンドSMSメッセージによってトリガーされた場合、キャンバスの最初の[メッセージステップ]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/)でSMSプロパティを参照できます。
{% endalert %}

**トリガー by inbound キーワード category**<br>
![アクションベースのSMSキャンペーンでセグメンテーションフィルターを使用し、「オプトイン」というキーワードをサブスクリプショングループ「マーケティングSMS」に送信しました。][7]{: style="margin-top:10px;"}

**トリガー by arbitrary keywords**<br>
「その他」のキーワード応答でメッセージをトリガーする場合、キーワード本文を正確なテキスト一致で評価する機会があります。この試合は、記載されたルールに従います:唯一の**正確な単語のメッセージ**が処理されます（大文字と小文字の_区別なし_）。`Hello Braze!` のキーワード送信は、次の例に示す基準に一致しません。
![アクションベースのSMSキャンペーンで、キーワードカテゴリが「その他」で、メッセージ本文が正確に「Hello」または「Hey」の場合。][8]{: style="margin-top:10px;"}

**テンプレートキーワード**<br>
インバウンドSMSまたはMMSでキャンペーンやキャンバスコンポーネントをトリガーする際に、ユーザーが送信したテキストやメディア添付ファイルをLiquidを使用してキャンペーンやキャンバスの本文にテンプレート化することができます。これにより、ユーザーの応答にアクセスできるようになり、それを返信に含めたり、条件付きロジックを適用したり、Liquidでできる他のことを行ったりすることができます。 

{% raw %}

```liquid
Sorry, we didn't recognize {{sms.${inbound_message_body}}}. Text HELP for help or STOP to stop.
```

```liquid
{% if {{sms.${inbound_message_body}}} == "SNEAKERS" %}
OK, you're subscribed to updates on all our sneaker deals!
{% elsif {{sms.${inbound_message_body}}} == "SHIRTS" %}
Shirt deals coming up for you!
{% else %}
Want to receive a specific deal? Just text us the category you're interested in. For example SHIRTS or SNEAKERS.
{% endif %}
```

{% endraw %}

[1]: {% image_buster /assets/img/sms/filter1.png %}
[2]: {% image_buster /assets/img/sms/filter2.png %}
[3]: {% image_buster /assets/img/sms/trigger.png %}
[6]: {% image_buster /assets/img/sms/retargeting1.png %}
[7]: {% image_buster /assets/img/sms/retargeting2.png %}
[8]: {% image_buster /assets/img/sms/retargeting3.png %}
[16]: {% image_buster /assets/img/keyword_example1.jpg %}
[17]: {% image_buster /assets/img/keyword_example2.jpg %}
[11]: {% image_buster /assets/img/sms/clicked_opened_step.png %}
[12]: {% image_buster /assets/img/sms/clicked_opened_campaign.png %}
[13]: {% image_buster /assets/img/sms/clicked_opened_campaign_canvas_tag.png %}
[15]: {% image_buster /assets/img/sms/retargeting5.png %}
[16]: {% image_buster /assets/img/sms/retargeting4.png %}
