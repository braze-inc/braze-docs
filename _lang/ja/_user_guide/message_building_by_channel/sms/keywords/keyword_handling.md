---
nav_title: カスタム・キーワード・ハンドリング
article_title: カスタム・キーワード・ハンドリング
page_order: 3
description: "この参考記事では、Brazeが双方向SMSメッセージングと自動応答をどのように扱うかを取り上げている。これには、キーワード・トリガーの仕組みやカスタム・キーワード・カテゴリー、多言語サポートについての説明が含まれる。"
page_type: reference
channel:
  - SMS

---

# カスタム・キーワード・ハンドリング

> この参考記事では、Brazeが双方向SMSメッセージングと自動応答をどのように扱うかを取り上げている。これには、キーワード・トリガーの仕組みやカスタム・キーワード・カテゴリー、多言語サポートについての説明が含まれる。

## 双方向メッセージング（カスタムキーワードレスポンス）

双方向メッセージングでは、メッセージを送信し、それに対する応答を処理することができる。エンドユーザーがBrazeにキーワードを送る必要があり、それに対してユーザーが自動返信を受け取る。正しく適用すれば、双方向メッセージングは、顧客マーケティングのシンプルで、即時的で、ダイナミックなソリューションとなり、その過程で時間とリソースを節約することができる。

## キーワードと自動応答を管理する

BrazeのSMSでは、キーワード・トリガー、カスタム・レスポンス、多言語キーワード・セットの定義、カスタム・キーワード・カテゴリの設定ができる。 

{% tabs %}
{% tab キーワード・トリガーを追加する %}

#### キーワード・トリガーを追加する

デフォルトのオプトインおよびオプトアウトキーワードに加えて、オプトイン、オプトアウト、およびヘルプ応答をトリガする独自のキーワードを定義することもできる。

独自のキーワードを定義するには、以下のようにする：

1. Brazeダッシュボードで、**Audience**>**Subscription Groupsに**進み、SMS購読グループを選択する。<br><br>
2. **SMSグローバルキーワードの**下で、キーワードを追加したいキーワードカテゴリの横にある鉛筆アイコンをクリックする。![]({% image_buster /assets/img/sms/sms_keywords.png %})<br><br>
3. 開いたタブで、このキーワード・カテゴリーをトリガーしたいキーワードを追加する。キーワードは大文字小文字を区別せず、`START` 、`YES` 、`UNSTOP` のようなユニバーサルキーワードは変更できないことに注意。![オプトイン」のキーワードを編集中追加されたキーワードは、"START"、"UNSTOP"、"YES "である。返信メッセージ欄には「この番号からのメッセージの配信を停止しました」と表示される。ヘルプに返信する。配信停止するにはSTOPと返信する。メッセージ料金とデータ料金が適用される場合がある。"]({% image_buster /assets/img/sms/keyword_edit2.png %})

キーワードとキーワード回答には以下のルールが適用される：

| キーワード | キーワード回答 |
| -------- | ----------------- |
| \- 有効なUTF-8エンコード文字<br>\- 各カテゴリー合計で最大20キーワード<br>\- 最大34文字<br>\- 1文字以上 <br>\- スペースを含むことはできない<br>\- 大文字と小文字を区別せず、サブスクリプション・グループ全体で一意である必要がある。 | \- 空白は許されない<br>\- 最大300文字<br>\- 有効なUTF-8文字 |
{: .reset-td-br-1 .reset-td-br-2}

{% alert tip %}
これらのキーワードをキャンペーンやキャンバスでどのように使用し、リターゲティングやメッセージのトリガーとするかに興味がある。詳しくは[SMSリターゲティングの]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/)記事をご覧いただきたい。
{% endalert %}
{% endtab %}

{% tab 回答を管理する %}

#### 回答を管理する

ユーザーが特定のキーワードカテゴリーにキーワードをテキスト入力した後に送信される独自のレスポンスを管理することができる。

1. Brazeダッシュボードで、**Audience**>**Subscription Groupsに**進み、SMS購読グループを選択する。<br><br>
2. **SMSグローバルキーワードの**下で、鉛筆のアイコンを選択し、回答を編集するキーワードカテゴリーを選択する。![]({% image_buster /assets/img/sms/sms_keywords.png %})<br><br> 
3. 開いたタブで、回答を編集する。回答を作成する際には、[コンプライアンスを正しく理解するための6つのルールに]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_laws_and_regulations/#the-six-rules-to-get-compliance-right)留意し、キーワードとキーワード回答に適用される以下のルールを読むこと。![レスポンス]({% image_buster /assets/img/sms/keyword_home.png %})<br><br>
4. 回答中の静的URLを自動的に短縮するには、**リンク短縮**トグルを選択する。文字数カウンターが更新され、短縮URLの予想される長さが表示される。![リンク短縮」トグルがオンになっているときに更新される文字カウンターを示すGIF。]({% image_buster /assets/img/sms/link_shortening.gif %}){: style="max-width:50%;"}

##### 考慮事項

| キーワード | キーワード回答 |
| -------- | ----------------- |
| \- 有効なUTF-8エンコード文字<br>\- 各カテゴリー合計で最大20キーワード<br>\- 最大34文字<br>\- 1文字以上 <br>\- スペースを含むことはできない<br>\- 大文字と小文字を区別せず、サブスクリプション・グループ全体で一意である必要がある。 | \- 空白は許されない<br>\- 最大300文字<br>\- 有効なUTF-8文字 |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% endtabs %}

{% alert tip %}
アクションベースのキャンバスが受信SMSメッセージによってトリガーされる場合、キャンバスの最初の[メッセージステップで]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/)SMSプロパティを参照できる。
{% endalert %}

## 多言語サポート

特定の国に送信する場合、送信者はインバウンドのキーワードとアウトバウンドの返信を現地語でサポートする必要がある場合がある。これをサポートするために、Brazeでは言語固有のキーワード設定を作成することができる。
![][16]{: style="float:right;max-width:40%;margin-left:10px;"}

### 言語固有のキーワードを作成する

**Add a Languageを**クリックし、ターゲット言語を選択するか、ドロップダウンで言語を検索する。

{% alert important %}
他の言語には、英語のようなキーワードやレスポンスがプリセットされていないため、送信者はマーケティングチームや法務チームと協力して、このセットに必要なキーワードを追加する必要がある。そうでない場合、Brazeはそれらの言語にローカライズされた受信メッセージを処理しない。
{% endalert %}

言語を削除する必要がある場合は、右下の**Delete Language**ボタンをクリックする。

![フランス語」タブを選択したSMSグローバルキーワードのページ。追加された言語ごとに追加のタブが存在する。][5]

## カスタム・キーワード・カテゴリー

デフォルトの3つのキーワードカテゴリ（オプトイン、オプトアウト、ヘルプ）に加えて、独自のキーワードカテゴリを最大25個まで作成できる。これにより、任意のキーワードを特定し、ビジネスに特化した対応を設定することができる。カテゴリーの例としては、「PROMO」や「DISCOUNT」などがあり、今月開催されるプロモについての返答を促すことができる。 

これらのカスタム・キーワードは、「常時オン」で動作する。つまり、メッセージ・サービスに加入しているユーザーなら誰でも、いつでもキーワードをテキストで送信し、応答を受け取ることができる。この動作に加え、ユーザーのライフサイクルの[特定のポイントでのみ]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/keyword_handling/#lifecycle-specific-keywords)送信できる特定のキーワードを定義するオプションもある。 

![ダブルオプティン」カテゴリーのキーワード。もしユーザーが "Y "と入力すると、"Hair Cuttery SMSへの登録を確認いただきありがとうございます "というメッセージが表示される。][12]

### カスタム・カテゴリーを作成する

カスタム・キーワード・カテゴリーを作成するには、以下のようにする：

1. 適切な購読グループを編集する。
2. **Add custom keywordを**クリックする。 ![][13]{: style="max-width:90%;"}
3. キーワード・カテゴリー名を指定し、ユーザーが返信メッセージを受信するために入力できるキーワードを定義する。

このキーワードカテゴリが作成されると、キャンペーンやキャンバスで[フィルタリングやトリガーをかける]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/)ことができるようになる。

カスタムキーワードカテゴリで作成されたキーワードは、新しいキーワードの作成に関するすべてのルールとバリデーションに従う。 

### ライフサイクル固有のキーワード

顧客のライフサイクルの間（例えば、最初のオンボーディングの間）に特定のキーワードを送信して応答を受け取ることができるタイミングを制限したいユースケースがある場合、キャンペーンまたはキャンバスの**キーワードカテゴリOTHER内のサブスクリプショングループに**トリガー**Sent inbound SMSを**使用して、ユーザーがある時点で送信できるキーワードを定義することができる。

このトリガーは、ユーザーの入力を検証するための正規表現ルールにマッチするかしないかだけでなく、メッセージのisかisでない比較を使って、特定のインバウンドメッセージのフィルタリングをサポートする。

#### キャンバス

![アクションベースのキャンバスステップで、トリガーは、メッセージ本文が正規表現 "キャレットシンボルスキップ "にマッチするキーワードカテゴリー "その他 "内のサブスクリプショングループ "メッセージングサービス "にインバウンドSMSを送信する。][14]{: style="max-width:90%;"}

#### Campaign

![キーワードカテゴリー "Other "内の "Marketing Message Service A "にインバウンドSMSを送信し、メッセージ本文が "Keyword1 "または "Keyword2 "または "Keyword A "でないことをトリガーとするアクションベースのキャンペーン。][15]{: style="max-width:90%;"}

### 未知のキーワードに対処する

必須ではないが、ユーザーが既存のキーワードと一致しないSMSキーワードをインバウンド送信した場合の自動応答を設定することを強く推奨する。このメッセージは、キーワードが認識されていないことをユーザーに通知し、いくつかのガイダンスを提供する。 

これは、"Sorry "のようなメッセージのSMSキャンペーンを作成することで可能である！STOPで止まれ、HELPで助けろというキーワードがわからなかったんだ」。次に、配信ステップで、**アクションベースの配信を**選択し、**キーワードカテゴリーOTHER内の購読グループにインバウンドSMSを送信**したトリガーを使用する。

![]({% image_buster /assets/img/sms/sms_other.png %})

{% alert tip %}
キャンペーンやキャンバスで、これらのキーワードやキーワード・カテゴリーをどのように使い、リターゲティングやメッセージのトリガーにできるかを見てみたい。詳しくは[SMSリターゲティングの]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/)記事をご覧いただきたい。
{% endalert %}

[oblink]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#setup-process
[1]: {% image_buster /assets/img/sms/keyword_edit2.png %}
[2]: {% image_buster /assets/img/sms/keyword_home.png %}
\[unknown]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/unknown_phone_numbers/
\[エンドポイント] ：{{site.baseurl}}/api/endpoints/user_data/post_user_alias/
\[IMAGE2] ： {% image_buster /assets/img/sms/sms_message_body.png %}
[5]: {% image_buster /assets/img/sms/multi-language2.png %}
[12]: {% image_buster /assets/img/sms/sms_custom_keyword.png %}
[13]: {% image_buster /assets/img/sms/sms_custom_step.png %}
[14]: {% image_buster /assets/img/sms/canvas_trigger.png %}
[15]: {% image_buster /assets/img/sms/campaign_trigger.png %}
[16]: {% image_buster /assets/img/sms/multi-language.png %}
