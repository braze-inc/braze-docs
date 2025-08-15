---
nav_title: ユーザ・リターゲティング
article_title: ユーザーのリターゲット
description: "この参照記事では、ユーザーの SMS インタラクションと RCS インタラクションを使用してメッセージをリターゲティングする方法について説明します。"
page_type: reference
page_order: 4
alias: /sms_mms_rcs_user_retargeting/
tool:
  - Campaigns
channel:
  - SMS
  - MMS
  - RCS

---

# ユーザー リターゲティング

> ユーザーのサブスクリプション状態を変更し、受信キーワードに基づいて自動応答を送信することに加えて、Brazeはフィルタリングおよびメッセージのトリガーのためにユーザープロファイルに対話を記録します。<br><br>これらのフィルターとトリガーを使用すると、SMS、MMS、および RCS キャンペーンが送信されたユーザーまたはこれらのキャンペーンに応答したユーザーに基づいてアクションをフィルタリングすることや、短縮 URL をクリックしたユーザーとさらにエンゲージすることができます。

{% alert tip %}
これらのリターゲティングオプションを活用するためのカスタムキーワードと双方向メッセージングの設定方法について詳しくは、当社の[カスタムキーワード]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/keyword_handling/)記事をご覧ください。
{% endalert %}  

## リターゲティングオプション

{% alert note %}
ユーザーリターゲティングを使用してオーディエンスを構築する際に、ユーザーの好みに基づいて特定のユーザーを含めたり除外したりすることを希望する場合があります。また、CUPの下での「販売または共有しない」権利などのプライバシー法を遵守するために必要です。マーケターは、キャンバスおよび/またはキャンペーンエントリ基準内でユーザーの適格性に関連するフィルターを実装する必要があります。
{% endalert %}

### SMS、MMS、およびRCS によるユーザのフィルタリング

ユーザーは、最後に SMS、MMS、または RCSを受信した時点、または特定のキャンペーンから SMS、MMS、またはRCSを受信しているかどうかに基づいてフィルタリングできます。フィルターはキャンペーンビルダーの**ターゲットオーディエンス**ステップで設定できます。 

**最後に受信した SMS/MMS/RCS に基づくフィルター処理**<br>
![セグメンテーションフィルター「最後に受信した SMS は2020年12月8日より後」。]({% image_buster /assets/img/sms/filter2.png %})

**SMS/MMS/RCS キャンペーンから受信したメッセージに基づくフィルター処理**<br>
特定のキャンペーンからメッセージを受信したユーザーをフィルタリングします。このフィルタを使用すると、キャンペーンからメッセージを受信していないものをフィルタリングすることもできます。<br>
![セグメンテーションフィルター「キャンペーン「SMS retargeting」からメッセージを受信した」。]({% image_buster /assets/img/sms/filter1.png %})

### ユーザーがSMS、MMS、またはRCSを受信するときにメッセージをトリガーします {#trigger-messages}

ユーザーが特定のキャンペーンから SMS、MMS、または RCS メッセージを受信したときにメッセージをトリガーするには、アクションベースのキャンペーンのトリガーアクションとして [**キャンペーンと対話**] を選択します。次に、[**SMS を受信する**] と、使用する SMS、MMS、または RCS キャンペーンを選択します。

![]({% image_buster /assets/img/sms/trigger.png %})

### 高度なトラッキングリンクによるフィルター処理

キャンペーンをクリックしたユーザーをリターゲティングするには、[高度なトラッキングリンク]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/link_shortening/)を使用します。
高度なトラッキングが有効になっているキャンペーンのみが、次のドロップダウンに表示されます:

**特定のSMS、MMS、またはRCSキャンペーンをクリックしたユーザーを再ターゲットする**
1. **クリックされた/開封されたキャンペーン**フィルターを使用してセグメントを作成します。
2. [**クリック済み SMS 短縮リンク**] を選択します。
3. 希望のキャンペーンを選択してください。

![]({% image_buster /assets/img/sms/retargeting5.png %})

**特定のキャンバスステップをクリックしたユーザーをリターゲティングする**
1. **クリック/オープンされたステップ**フィルターを使用してセグメントを作成します。
2. [**クリック済み SMS 短縮リンク**] を選択します。
3. 目的のキャンバスとキャンバスステップを選択します。

![]({% image_buster /assets/img/keyword_example1.jpg %})

## キーワード カテゴリ固有のリターゲティング

デフォルトの 3 つのキーワードカテゴリ (Opt-in、Opt-out、および Help) に加えて、独自のキーワードカテゴリを最大 25 個作成して、任意のキーワードと応答を識別できます。これらのカテゴリは、フィルタリングおよびリターゲティングに使用できます。Globalキーワードカテゴリとその設定方法の詳細については、[キーワード処理]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/)を参照してください。 

### 最近度によるフィルター処理

SMS、MMS、またはRCS プログラムに応答するユーザーの最新情報をフィルタリングします。このフィルタは、ユーザがキーワードカテゴリのいずれかに含まれるインバウンドメッセージを送信した最後の日付を評価します。 

![セグメンテーションフィルター「2020年8月11日以降にサブスクリプショングループ「Marketing SMS」に最後に送信され、キーワード「オプトイン」を含む SMS」。]({% image_buster /assets/img/sms/retargeting1.png %})

### キャンペーンまたはキャンバスアトリビューションでフィルター

特定の SMS、MMS、RCS キャンペーンまたはキャンバスコンポーネント、キーワードカテゴリ、またはタグに応答したユーザーのフィルターです。

**キーワードカテゴリを含む特定のキャンペーンへの応答に基づくフィルター処理**<br>
![キャンペーン「SMS-283」の「プロモーション」で「SMS に応答」のフィルターを指定したキャンペーン。このフィルターの下に「このフィルターは、アクティブなキャンペーンで使用されていない場合、「プロモーション」から最後のメッセージが送信されてから25か月後に期限切れになります」と表示されています。]({% image_buster /assets/img/sms/clicked_opened_campaign.png %})

**特定のタグを持つキャンペーンまたはキャンバスへの応答によるフィルター**
![タグ「Curbside Messaging Service C」を含むキャンペーンまたはキャンバスで「SMS に応答」のフィルターが指定されたキャンペーン。]({% image_buster /assets/img/sms/clicked_opened_campaign_canvas_tag.png %})

**特定のステップへの応答によるフィルター処理**
![ステップ「SMS ダブルオプト」の「ステップ - ヘルプ」で「SMS に応答」のフィルターが指定されたキャンペーン。]({% image_buster /assets/img/sms/clicked_opened_step.png %})

### キーワードによるメッセージのトリガー

メッセージは、ユーザーがキーワードカテゴリ（ユーザーがキーワードのいずれかを送信した場合）または他のキーワード（ユーザーが既存のカテゴリのいずれかに該当しないキーワードを送信した場合）に基づいてメッセージを送信するとトリガーされることがあります。これらのトリガーは、キャンペーンビルダーの配信ステップで設定します。

定義されたトリガーイベントに受信メッセージが一致するかどうかを評価する際、評価が始まる前に前後のスペースが削除されます。

{% alert tip %}
アクションベースのキャンバスがインバウンド SMS または MMS メッセージによってトリガーされる場合、次のアクションパスまで、任意のキャンバスステップで[サポートされている SMS Liquid プロパティ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/)を参照できます。
{% endalert %}

**インバウンドのキーワードカテゴリによるトリガー**<br>
![セグメンテーションフィルター「キーワード「オプトイン」をサブスクリプショングループ「Marketing SMS」に送信した」が指定されているアクションベースの SMS キャンペーン。]({% image_buster /assets/img/sms/retargeting2.png %}){: style="margin-top:10px;"}

**任意のキーワードによるトリガー**<br>
「その他」のキーワード応答でメッセージをトリガーする場合、キーワード本文を正確なテキスト一致で評価する機会があります。この一致は、次のルールに従います。唯一の**正確な単語のメッセージ**が処理されます（大文字と小文字の_区別なし_）。`Hello Braze!` のキーワード送信は、次の例に示す基準に一致しません。
![キーワードカテゴリが「その他」で、メッセージ本文が正確に「Hello」または「Hey」のアクションベースの SMS キャンペーン]({% image_buster /assets/img/sms/retargeting3.png %}){: style="margin-top:10px;"}

**キーワードのテンプレート化**<br>
インバウンドの SMS または MMS でキャンペーンやキャンバスコンポーネントをトリガーする場合、Liquid を使用して、ユーザーが送信したテキストやメディア添付ファイルをキャンペーンやキャンバスの本文にテンプレート化することができます。これにより、ユーザーの応答にアクセスして、その応答を返信に含めたり、条件付きロジックを適用したり、Liquid で可能なあらゆることを実行したりできます。 

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

[16]: {% image_buster /assets/img/keyword_example1.jpg %}
[16]: {% image_buster /assets/img/sms/retargeting4.png %}
