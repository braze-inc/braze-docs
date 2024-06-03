---
nav_title: カスタムキーワード処理
article_title: カスタムキーワード処理
page_order: 3
description: "このリファレンス記事では、Brazeが双方向SMSメッセージングと自動応答をどのように処理するかについて説明します。これには、キーワードトリガーの仕組み、カスタムキーワードカテゴリ、多言語サポートの説明が含まれます。"
page_type: reference
channel:
  - SMS

---

# カスタムキーワード処理

> このリファレンス記事では、Brazeが双方向SMSメッセージングと自動応答をどのように処理するかについて説明します。これには、キーワードトリガーの仕組み、カスタムキーワードカテゴリ、多言語サポートの説明が含まれます。

## 双方向メッセージング(カスタムキーワード応答)

双方向メッセージングを使用すると、メッセージを送信し、それらのメッセージに対する応答を処理できます。エンドユーザーがBrazeにキーワードを送信すると、そのユーザーは自動返信を受け取ります。双方向メッセージングを正しく適用すれば、顧客マーケティングのためのシンプルで即時かつ動的なソリューションとなり、その過程で時間とリソースを節約できます。

## キーワードと自動応答を管理する

SMS with Brazeでは、キーワードトリガーの作成、カスタムレスポンスの作成、複数言語のキーワードセットの定義、カスタムキーワードカテゴリの設定を行うことができます。 

{% tabs %}
{% tab Add Keyword Triggers %}

#### キーワード トリガーを追加する

デフォルトのオプトインおよびオプトアウトキーワードに加えて、独自のキーワードを定義して、オプトイン、オプトアウト、およびヘルプの応答をトリガーすることもできます。

独自のキーワードを定義するには、次の操作を行います。

1. Braze ダッシュボードで、[ **Audience** > **Subscription Groups** ] に移動し、SMS サブスクリプショングループを選択します。<br><br>
2. **[SMS グローバルキーワード**] で、キーワードを追加するキーワード カテゴリの横にある鉛筆アイコンをクリックします。![\](){% image_buster /assets/img/sms/sms_keywords.png %}<br><br>
3. 開いたタブで、このキーワードカテゴリをトリガーするキーワードを追加します。キーワードは大文字と小文字を区別せず、、`YES``UNSTOP`などの`START`汎用キーワードは変更できないことに注意してください。 ![Editing keywords for "Opt-In" category. Added keywords are "START", "UNSTOP", and "YES". The reply message field reads "You have been unsubscribed to messages from this number. Reply HELP for help. Reply STOP to unsubscribe. Message and data rates may apply."]({% image_buster /assets/img/sms/keyword_edit2.png %})

キーワードとキーワード応答には、次のルールが適用されます。

|キーワード |キーワード応答 |
| -------- | ----------------- |
|- 有効な UTF-8 エンコード文字<br>\- カテゴリ合計で最大20個のキーワード<br>\- 最大長は 34 文字です<br>\- 最小長は 1 文字です <br>\- スペースを含めることはできません<br>\- 大文字と小文字を区別せず、サブスクリプション グループ全体で一意である必要があります |- 空白にすることはできません<br>\- 最大長は 300 文字です。<br>\- 有効な UTF-8 文字 |
{: .reset-td-br-1 .reset-td-br-2}

{% alert tip %}
これらのキーワードをキャンペーンやキャンバスで使用して、リターゲティングやメッセージのトリガーにどのように使用できるか知りたいですか?詳細については、 [SMSリターゲティング]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/) の記事をご覧ください。
{% endalert %}
{% endtab %}

{% tab Manage responses %}

#### 回答を管理する

ユーザーが特定のキーワード カテゴリにキーワードをテキスト入力した後にユーザーに送信される独自の応答を管理できます。

1. Braze ダッシュボードで、[ **Audience** > **Subscription Groups** ] に移動し、SMS サブスクリプショングループを選択します。<br><br>
2. **[SMS グローバル キーワード**] で、鉛筆アイコンを選択して応答を編集するキーワード カテゴリを選択します。![\](){% image_buster /assets/img/sms/sms_keywords.png %}<br><br> 
3. 開いたタブで、回答を編集して保存します。[コンプライアンスを正しく守るための 6 つのルール]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_laws_and_regulations/#the-six-rules-to-get-compliance-right)に留意し、キーワードとキーワードのレスポンスに適用される次のルールをお読みください。 ![Responses]({% image_buster /assets/img/sms/keyword_home.png %})

|キーワード |キーワード応答 |
| -------- | ----------------- |
|- 有効な UTF-8 エンコード文字<br>\- カテゴリ合計で最大20個のキーワード<br>\- 最大長は 34 文字です<br>\- 最小長は 1 文字です <br>\- スペースを含めることはできません<br>\- 大文字と小文字を区別せず、サブスクリプション グループ全体で一意である必要があります |- 空白にすることはできません<br>\- 最大長は 300 文字です。<br>\- 有効な UTF-8 文字 |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% endtabs %}

{% alert tip %}
アクションベースの Canvas が受信 SMS メッセージによってトリガーされた場合は、Canvas の最初の [メッセージステップ]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) で SMS プロパティを参照できます。
{% endalert %}

## 多言語サポート

特定の国に送信する場合、送信者は現地の言語で受信キーワードと送信返信をサポートする必要がある場合があります。これをサポートするために、Brazeでは言語固有のキーワード設定を作成できます。
![][16]{: style="float:right;max-width:40%;margin-left:10px;"}

### 言語固有のキーワードの作成

[ **言語を追加** ]をクリックしてターゲット言語を選択するか、ドロップダウン内で言語を検索します。

{% alert important %}
他の言語には、英語などの事前設定されたキーワードと応答が付属していないため、送信者はマーケティングチームや法務チームと協力して、必要なキーワードをこのセットに追加する必要があることに注意してください。それ以外の場合、Brazeはそれらの言語のローカライズされた受信メッセージを処理しません。
{% endalert %}

言語を削除する必要がある場合は、右下の「 **言語を削除** 」ボタンをクリックします。

![SMSグローバルキーワードページは、「フランス語」タブが選択されています。追加された言語ごとに追加のタブがあります。[5]

## カスタム キーワード カテゴリ

デフォルトの 3 つのキーワード カテゴリ(オプトイン、オプトアウト、ヘルプ)に加えて、独自のキーワード カテゴリを最大 25 個まで作成することもできます。これにより、任意のキーワードを特定し、ビジネスに固有の応答を設定できます。たとえば、「PROMO」や「DISCOUNT」などのカテゴリでは、今月行われるプロモーションに関する応答が表示される場合があります。 

これらのカスタム キーワードは "常時接続" の機能で動作するため、メッセージ サービスに登録しているすべてのユーザーがキーワードをテキスト送信し、いつでも応答を受け取ることができます。この動作に加えて、ユーザーのライフサイクルの [特定の時点で]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/keyword_handling/#lifecycle-specific-keywords) のみ送信できる特定のキーワードを定義するオプションもあります。 

![「ダブルオプチン」カテゴリのキーワード。ユーザーが「Y」とテキストメッセージを送ると、「Hair Cuttery SMSへの登録を確認していただきありがとうございます」というメッセージを受け取る[12]。

### ユーザー設定のカテゴリの作成

カスタム キーワード カテゴリを作成するには、次の操作を行います。

1. 適切なサブスクリプション グループを編集します。
2. [ **カスタム キーワードを追加]** をクリックします。 ![][13]{: style="max-width:90%;"}
3. キーワード カテゴリ名を指定し、ユーザーが応答メッセージを受信するためにテキストで入力できるキーワードを定義します。

このキーワードカテゴリが作成されると、キャンペーンやキャンバスで [フィルタリングやトリガー]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/) ができるようになります。

カスタム キーワード カテゴリで作成されたキーワードは、新しいキーワードを作成する際のすべてのルールと検証に従います。 

### ライフサイクル固有のキーワード

顧客がライフサイクル中(たとえば、最初の最初のオンボーディング中)に特定のキーワードを送信して応答を受信できるタイミングを制限するユースケースがある場合は、キャンペーンまたはキャンバスの **キーワードカテゴリ「その他」内の「サブスクリプショングループに受信SMSを送信しました** 」トリガーを使用して、ユーザーが特定の時点で送信できるキーワードを定義できます。

このトリガーは、メッセージの is または is not の比較、およびユーザーの入力を検証するための正規表現ルールの一致または一致しないを使用して、特定の受信メッセージのフィルター処理をサポートします。

#### キャンバス

![メッセージ本文が正規表現 "キャレット記号スキップ" と一致するキーワード カテゴリ "その他" 内のサブスクリプション グループ "メッセージング サービス" に受信 SMS を送信するトリガーを持つアクションベースのキャンバス ステップ。[14]{: style="max-width:90%;"}

#### キャンペーン

![メッセージ本文が "Keyword1" であるか、"Keyword2" であるか、または "Keyword A" ではない、キーワード カテゴリ "その他" 内のサブスクリプション グループ "Marketing Message Service A" に受信 SMS を送信する トリガーを持つアクションベースのキャンペーン。[15]{: style="max-width:90%;"}

### 未知のキーワードへの対処

必須ではありませんが、ユーザーが既存のキーワードと一致しない受信 SMS キーワードを送信した場合の自動応答を設定することを強くおすすめします。このメッセージは、キーワードが認識されないことをユーザーに通知し、いくつかのガイダンスを提供します。 

これは、「申し訳ありません!「STOP」と「STOP」とテキストで「STOP」と入力すると「HELP」というキーワードが認識されませんでした」 次に、配信手順で「 **アクションベースの配信** 」を選択し、 **キーワードカテゴリ「OTHER」内の「Sent inbound SMS to subscription group**」トリガーを使用します。

![\]({% image_buster /assets/img/sms/sms_other.png %})

{% alert tip %}
これらのキーワードやキーワードカテゴリをキャンペーンやキャンバスで使用して、リターゲティングやメッセージのトリガーに活用する方法に興味がありますか?詳細については、 [SMSリターゲティング]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/) の記事をご覧ください。
{% endalert %}

[oblink]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#setup-process
[1]: {% image_buster /assets/img/sms/keyword_edit2.png %}
[2]: {% image_buster /assets/img/sms/keyword_home.png %}
[unknown]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/unknown_phone_numbers/
[endpoint]: {{site.baseurl}}/api/endpoints/user_data/post_user_alias/
[画像2]: {% image_buster /assets/img/sms/sms_message_body.png %}
[5]: {% image_buster /assets/img/sms/multi-language2.png %}
[12]: {% image_buster /assets/img/sms/sms_custom_keyword.png %}
[13]: {% image_buster /assets/img/sms/sms_custom_step.png %}
[14]: {% image_buster /assets/img/sms/canvas_trigger.png %}
[15]: {% image_buster /assets/img/sms/campaign_trigger.png %}
[16]: {% image_buster /assets/img/sms/multi-language.png %}
