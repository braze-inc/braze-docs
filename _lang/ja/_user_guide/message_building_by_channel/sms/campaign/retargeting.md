---
nav_title: ユーザーのリターゲット
article_title: SMSユーザーリターゲット
description: "このリファレンス記事では、ユーザがSMSインタラクションを使用してメッセージを再ターゲットする方法について説明します。"
page_type: reference
tool:
  - Campaigns
channel:
  - SMS

---

# ユーザーのリターゲット

> ユーザのサブスクリプション状態を変更し、受信キーワードに基づいて自動応答を送信することに加えて、Braze はメッセージをフィルタリングおよびトリガするためのインタラクションもユーザプロファイルに記録します。<br><br>これらのフィルタとトリガーを使用すると、SMSメッセージを受信したユーザ、特定のSMSキャンペーンからSMSメッセージを受信したユーザ、および特定のSMSキャンペーンからSMSメッセージを受信したユーザをトリガーすることができます。 

{% alert tip %}
カスタムキーワードの詳細と、これらのリターゲットオプションを利用するための双方向メッセージングの設定方法については、[custom keyword]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/keyword_handling/) を参照してください。
{% endalert %}  

## リターゲットオプション

{% alert note %}
ユーザーのリターゲットを使用してオーディエンスを構築する場合は、ユーザーの好みに基づいて特定のユーザーを含めるか除外し、CUP の下で「売らない/共有しない」などのプライバシーに関する法律を順守することをお勧めします。マーケターは、キャンバスおよび/またはキャンペーン登録基準内で、ユーザーの適格性に関連するフィルタを実装する必要があります。
{% endalert %}

### SMSでユーザーをフィルタリングする

ユーザは、最後にSMSを受信したとき、または特定のSMSキャンペーンからSMSを受信したときによってフィルタリングできます。フィルタは、キャンペーンビルダのTarget Users ステップで設定できます。 

**最後に受信したSMSで絞り込む**<br>
![2020年12月8日以降に最後に受信したSMSをセグメンテーションフィルタ][2]

**SMSキャンペーンから受信したメッセージでフィルタリングする**<br>
特定のSMSキャンペーンからメッセージを受信したユーザをフィルタリングします。このフィルタを使用すると、SMSキャンペーンからメッセージを受信していないものをフィルタリングすることもできます。<br>
![セグメンテーションフィルタキャンペーン"SMS retargeting".][1] からメッセージを受信しました。

### ユーザがSMSを受信するときにメッセージをトリガする

ユーザが特定のキャンペーンからSMS メッセージを受信するときにメッセージをトリガするには、アクションベースのキャンペーンのトリガアクションとして**Campaign** と対話を選択します。次に、**Receive SMS**を選択し、使用するSMSキャンペーンを選択します。

![][3]

### 高度なトラッキングリンクによるフィルタリング

[高度なトラッキングリンク]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/link_shortening/)でキャンペーンをクリックしたユーザを再ターゲットします。
高度な追跡が有効になっているキャンペーンのみが、以下のドロップダウンに表示されます。

**特定のSMSキャンペーンをクリックしたユーザーを再ターゲットする**
1\.**Clicked/Opened Campaign**フィルタを使用してセグメントを作成します。
2\.**クリックしたsms**を選択します。
3\.目的のキャンペーンを選択します。

![][15]

**特定のキャンバスステップをクリックしたユーザーを再ターゲットする**
1\.**Clicked/Opened Step**フィルタを使用してセグメントを作成します。
2\.**クリックしたsms**を選択します。
3\.目的の「キャンバス」ステップと「キャンバス」ステップを選択します。

![][16]

## キーワード・カテゴリ固有のリターゲット

3 つのデフォルトのキーワードカテゴリ(Opt-in、Opt-out、およびHelp) に加えて、独自のキーワードカテゴリを最大25 個作成することもでき、任意のキーワードとレスポンスを識別できます。これらのカテゴリは、フィルタリングおよびターゲット変更に使用できます。SMSキーワードカテゴリとその設定方法の詳細については、[SMSターゲット変更]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/)を参照してください。 

### 新旧によるフィルタ

SMS プログラムに応答するユーザの新着情報をフィルタリングします。このフィルタは、ユーザがキーワードカテゴリのいずれかに含まれるインバウンドSMS を最後に送信した日付を評価します。 

![セグメンテーションフィルタ最後にSMS をサブスクリプショングループ&quot に送信しました;Marketing SMS"キーワード"Opt-in"2020年8 月11 日以降][6]

### キャンペーンまたはキャンバス属性によるフィルタ

特定のSMS キャンペーンまたはキャンバスコンポーネント、キーワードカテゴリ、またはタグに応答したユーザのフィルタ。

**特定のキャンペーンカテゴリに返信されたフィルタ**<br>
![フィルタ&quot でキャンペーン;SMS&quot に返信しました;キャンペーン"SMS-283""プロモーション".フィルタの下で、このフィルタは&quot に言及しています。このフィルタは、最後のメッセージが"Promotion" から送信されてから25 か月後に期限切れになります。アクティブなキャンペーンで使用されていない場合は、"][12]

**特定のタグを持つキャンペーンまたはキャンバスに返信されたフィルタ**
![フィルタを使用したキャンペーン"SMS&quot に返信しました。campaign またはCanvas にタグ"Curbside Messaging Service C".][13]

**特定のステップに返信されたフィルタ**
![フィルタを使用したキャンペーン"SMS&quot に返信しました;ステップ"SMS Double Opt" "ステップ- Help".][11]

### キーワードによるメッセージのトリガ

メッセージは、ユーザがキーワードカテゴリ(ユーザがいずれかのキーワードを送信)または他のキーワード(ユーザが既存のカテゴリのいずれにも該当しないキーワードを送信)に基づいてメッセージを受信したときにトリガできます。これらのトリガーは、キャンペーンビルダーの配信ステップで設定されます。

インバウンド・メッセージが定義されたトリガー・イベントを満たしているかどうかを評価する場合、評価が開始される前に先頭および末尾のスペースが除去されます。

{% alert tip %}
アクションベースのキャンバスが受信SMS メッセージによってトリガーされる場合は、キャンバスの最初の[メッセージステップ]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) でSMS プロパティを参照できます。
{% endalert %}

**着信キーワードカテゴリによるトリガ**<br>
![セグメンテーションフィルタを使用したアクションベースのSMS キャンペーンSent キーワード"Opt-in" to subscription group "Marketing SMS".][7]{: style="margin-top:10px;"}

**任意のキーワードによるトリガ**<br>
"Other" キーワードresponse でメッセージをトリガするときには、キーワードbody を正確なテキスト一致で評価する機会があります。この一致は、注記されているのと同じルールに従います。**exact, single-word message**のみが処理されます(大文字小文字の区別なし)。`Hello Braze!` のキーワードが送信された場合、次の例に示す条件と一致しません。
![キーワードカテゴリが"Other"メッセージ本文が正確に"Hello"または"Hey".][8]の、アクションベースのSMSキャンペーン{: style="margin-top:10px;"}

**テンプレートキーワード**<br>
インバウンドSMS またはMMS でキャンペーンまたはキャンバスコンポーネントをトリガーする場合、オプションで、ユーザがキャンペーンまたはキャンバスの本文に送信したテキストまたはメディア添付をLiquid でテンプレート化することができます。これにより、ユーザーの応答にアクセスできるようになります。この応答には、リプライに含めることも、条件付きロジックを適用することも、リキッドを使用して実行できることもできます。 

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
