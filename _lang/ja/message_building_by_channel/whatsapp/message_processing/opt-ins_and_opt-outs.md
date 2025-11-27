---
nav_title: オプトインとオプトアウト
article_title: WhatsAppのオプトインとオプトアウト
description: "この参考記事では、WhatsAppのオプトインとオプトアウトの様々な方法を取り上げている。"
page_type: partner
search_tag: Partner
page_order: 5
channel:
  - WhatsApp
alias: /user_guide/message_building_by_channel/whatsapp/opt-ins_and_opt-outs/
---

# オプトインとオプトアウト

> WhatsApp のオプトインとオプトアウトの処理は非常に重要です。これは、WhatsApp が[電話番号の品質評価](https://www.facebook.com/business/help/896873687365001)を監視しており、評価が低いとメッセージの上限を低下する可能性があるためです。<br><br>高品質の評価を構築する1つの方法は、ユーザーがビジネスをブロックしたり、報告したりしないようにすることです。これは、[質の高いメッセージング](https://developers.facebook.com/docs/whatsapp/messaging-limits#quality-rating-and-messaging-limits)（ユーザーにとっての価値など）を提供し、メッセージの頻度をコントロールし、顧客が今後のコミュニケーション受信をオプトアウトできるようにすることで実現できる。<br><br>このページでは、オプトインとオプトアウトの設定方法、"regex"と"is"修飾子の違いについて説明します。

オプトインは、外部ソースから、または SMS、アプリ内、ブラウザ内のメッセージなど、Braze の方法で取得できます。オプトアウトは、Braze で設定したキーワードと WhatsApp のマーケティングボタンで処理できます。オプトインとオプトアウトの設定については、以下の方法を参照されたい。

#### オプトイン方法
- [外部から Braze へのオプトイン方法](#external-to-braze-opt-in-methods)
  - [外部に作成されたオプトインリスト](#externally-built-opt-in-list)
  - [カスタマーサポートの WhatsApp チャネルのアウトバウンドメッセージ](#outbound-message-in-customer-support-whatsapp-channel)
  - [インバウンドの WhatsApp メッセージ](#inbound-whatsapp-message)
- [ブレーズを利用したオプトイン・メソッド](#braze-powered-opt-in-methods)

#### オプトアウトの方法
- [一般的なオプトアウトのキーワード](#general-opt-out-keywords)
- [[Marketing opt-out] の選択](#marketing-opt-out-selection)

## Braze WhatsAppチャンネルのオプトインを設定する

WhatsApp のオプトインについては、[WhatsApp の要件](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/)を満たす必要があります。また、Braze に以下の情報を提供する必要があります。
- 各ユーザーの`external_id` 、[電話番号]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_phone_numbers/)、更新された購読状況。これは、[SDK](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)/)を使用するか、[`/users/track` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)経由で、電話番号と購読ステータスを更新することで実行できます。

{% alert note %}
Braze が改良してリリースした `/users/track` エンドポイントでは購読ステータスの更新が可能になり、[購読グループ]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/#update-subscription-status)で確認できます。ただし、すでに [`/v2/subscription/status/set` エンドポイントを]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status_v2/)使用してオプトインプロトコルを作成している場合は、引き続きそれを使用できます。
{% endalert %}

### 外部から Braze へのオプトイン方法

お客様のアプリまたはウェブサイト（アカウント登録、チェックアウトページ、アカウント設定、クレジットカード端末）をBrazeに提供する。

既にEメールやテキストでのマーケティング同意を得ている場合は、WhatsApp用のセクションを追加する。オプトインしたユーザーには、`external_id`、[電話番号]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_phone_numbers/)、および更新後の購読ステータスが必要です。これを行うには、Braze のインストール方法に応じて、[`/subscription/status/set` エンドポイント]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/)を活用するか、[SDK](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)/)を使用します。

#### 外部に作成されたオプトインリスト

以前WhatsAppを利用したことがあれば、WhatsAppの要件に沿ったオプトインでユーザーリストを作成済みかもしれない。この場合は、CSV をアップロードするか、API を使用して、[以下の情報]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import#csv)を Braze に取り込みます。

#### カスタマーサポートWhatsAppチャンネルのアウトバウンドメッセージ

カスタマーサポートチャネルでは、解決済みの問題のフォローアップに、マーケティングメッセージングにオプトインするかどうかを尋ねる自動メッセージを追加します。ここでの機能は、選択したカスタマーサポートツールの機能が使用できるかどうかと、ユーザー情報の保存場所によって異なります。

1. WhatsApp Businessの電話番号から[メッセージリンクを](https://business.facebook.com/business/help/890732351439459?ref=search_new_0)送信する。
2. 顧客が「はい」を返信すると、オプトインが表明される[クイック返信アクション]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/user_messages/#quick-replies)を指定します。
3. カスタムキーワードトリガーを設定する。
4. どちらのアイディアにせよ、おそらく次のようなパスが必要だろう：
	- [`/users/track` エンドポイントを]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)呼び出して、ユーザーを更新するか、作成します。
	- [`/subscription/status/set` エンドポイント]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/)を利用するか、[SDK](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)/) を使用します。

#### WhatsAppのインバウンドメッセージ 

顧客にWhatsApp番号にインバウンドメッセージを送ってもらう。

これは、新しいチャンネルでユーザーに確認メッセージを受け取らせるかどうかによって、キャンバスまたはキャンペーンとして設定できる。

1. インバウンドメッセージのアクションベースの配信トリガーでキャンペーンを作成する。
2. ウェブフックキャンペーンを作成する。Webhook の例については、[購読グループ]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/opt-ins_and_opt-outs/#update-subscription-status)を参照してください。

{% alert tip %}
WhatsAppチャンネルに参加するためのURLやQRコードは、[WhatsAppマネージャー](https://business.facebook.com/wa/manage/phone-numbers/)内の「**電話番号**」>「**メッセージリンク**」から作成できる。<br>![WhatsApp QR コード作成画面。]({% image_buster /assets/img/whatsapp/whatsapp115.png %})({: style="max-width:55%;"})
{% endalert %}

### ブレーズを利用したオプトイン・メソッド 

#### SMSメッセージ

キャンバスで、次のいずれかの方法を使用して、WhatsApp メッセージの受信にオプトインするかどうかを顧客に尋ねるキャンペーンを設定します。
- 顧客セグメント: 米国外のマーケティング購読グループ
- カスタムキーワードのトリガー設定

ユーザープロファイルの購読ステータスの更新については、[購読グループ]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/#update-subscription-status)を参照してください。

#### アプリ内またはブラウザ内のメッセージ

WhatsApp の使用にオプトインするように顧客に促すアプリ内メッセージまたはブラウザー内ポップアップを作成します。

Braze SDK とのインターフェイスに、[HTML アプリ内メッセージ](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates/4-sms-capture-modal)と [JavaScript の「bridge」]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/html_in-app_messages#javascript-bridge)を使用します。WhatsAppの購読グループIDを必ず使用すること。 

#### 電話番号取得フォーム

アプリ内メッセージ用の[電話番号取得フォーム]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/templates/phone_number_capture/)テンプレートをドラッグ＆ドロップエディターで使い、ユーザーの電話番号を収集してWhatsApp購読グループを増やそう。

## Braze WhatsAppチャンネルのオプトアウトを設定する

### 一般的なオプトアウト・キーワード

特定の単語をメッセージ送信することで、ユーザーが今後のメッセージングからオプトアウトできるキャンペーンやキャンバスを設定できます。キャンバスは、オプトアウトが成功したことを確認するフォローアップメッセージを含めることができるので、特に有益です。 

#### ステップ 1:「インバウンドの WhatsApp メッセージ」のトリガーを持つキャンバスの作成
 
![WhatsApp インバウンドメッセージを送信するユーザーをエントリさせるアクションベースのキャンバスエントリステップ。]({% image_buster /assets/img/whatsapp/whatsapp116.png %}){: style="max-width:85%;"}

キーワードトリガーを選択する際には、「Stop」や「No Message」といった単語を含める。この方法を選択した場合は、必ず顧客にオプトアウトの言葉を伝えてください。例えば、最初のオプトインを受信した後、「これらのメッセージからオプトアウトするには、いつでも『Stop』のメッセージを送信してください」などのフォローアップ応答を含めます。 

![メッセージ本文が「STOP」または「NO MESSAGE」である WhatsApp 受信メッセージを送信するメッセージステップ]({% image_buster /assets/img/whatsapp/whatsapp117.png %})({: style="max-width:85%;"})

#### ステップ 2: ユーザーのプロフィールを更新する

[購読グループ]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/#update-subscription-status)で説明されている方法のいずれかを使用して、ユーザープロファイルを更新します。

### マーケティング・オプトアウトの選択

WhatsApp のメッセージテンプレート作成画面で、[marketing opt-out] オプションを含めることができます。これを含むときはいつでも、テンプレートがサブスクリプショングループ変更のための後続ステップを持つキャンバスで使用されていることを確認すること。 

1. マーケティングオプトアウト」クイック返信でメッセージテンプレートを作成する。<br>!["Marketing opt-out"のフッターオプションを持つメッセージテンプレート。]({% image_buster /assets/img/whatsapp/whatsapp121.png %})<br><br>![マーケティングオプトアウトボタンを設定するセクション。]({% image_buster /assets/img/whatsapp/whatsapp122.png %})<br><br>
2. このメッセージテンプレートを使ってキャンバスを作成する。<br><br>
3. 前述の例のステップに従うが、トリガーテキストは "STOP PROMOTIONS "とする。<br><br>
4. [購読グループ]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/#update-subscription-status)で説明されている方法のいずれかを使用して、ユーザーの購読ステータスを更新します。

## オプトインとオプトアウトのワークフローを設定する

WhatsAppのキーワード応答ワークフローは、この2つの方法で「START」と「STOP」を設定できる：

- [ユーザー更新ステップ](#user-update-step)
- [Webhookキャンペーンで2つ目のWhatsAppキャンペーンをトリガーする](#webhook-campaign-to-trigger-a-second-whatsapp-campaign)

### ユーザー更新ステップ

[ユーザー更新ステップでは]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/)、ユーザーがWhatsApp購読グループの電話番号にキーワードを送信すると、そのユーザーの電話番号をWhatsApp購読グループに追加することができる。

ユーザー更新ステップでは、ユーザーの電話番号が購読グループに追加されないとユーザーはキャンバスの次のステップに進まないため、競合状態が回避されます。また、設定手順も他の方法より少ないため、Braze では一般的にこの方法をお勧めしています。

1. アクションベースのステップ「**WhatsAppインバウンドメッセージを送信**」でキャンバスを作成する。[**メッセージ本文の場所**] をオンにして、[**次に該当する**] に「START」と入力します。

{% alert important %}
「STOP」メッセージの場合は、オプトアウトを確認するメッセージステップと、ユーザー更新ステップの順序を逆にします。そうしないと、ユーザーはまず購読グループからオプトアウトされ、確認メッセージを受け取る資格がなくなる。
{% endalert %}

![メッセージ本文が「START」であるWhatsApp メッセージステップ。]({% image_buster /assets/img/whatsapp/whatsapp_inbound_message.png %}){: style="max-width:80%;"}

{: start="2"}
2\.キャンバスで、[**ユーザーの更新を設定**] ステップを作成し、[**アクション**] で [**高度な JSON エディター**] を選択します。<br><br>![アクションが「高度なJSONエディター」であるユーザー更新ステップ。]({% image_buster /assets/img/whatsapp/user_update.png %})<br><br>
3\.**ユーザー更新オブジェクト**に次の JSON ペイロードを入力し、`XXXXXXXXXXX` を購読グループ ID に置き換えます。

{% raw %}
```json
{
    "attributes": [
        {
            "subscription_groups": [
                {
                    "subscription_group_id": "XXXXXXXXXXX",
                    "subscription_state": "subscribed"
                }
            ]
        }
    ]
}
```
{% endraw %}

{: start="4"}
4\.後続のWhatsAppメッセージステップを追加する。<br><br>![キャンバスの「ユーザの更新」ステップ]({% image_buster /assets/img/whatsapp/message_step.png %}){: style="max-width:25%;"}

#### 考慮事項

Brazeは[User Updateステップの]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/)リクエストをバッチ処理するため、更新の完了速度はまちまちかもしれない。

### Webhookキャンペーンで2つ目のWhatsAppキャンペーンをトリガーする

Webhookキャンペーンは、ユーザーの電話番号をWhatsApp購読グループに追加した後、ユーザーが購読グループの電話番号にキーワードを送信すると、2つ目のキャンペーンへのエントリーをトリガーすることができる。

{% alert important %}
STOPメッセージにこの方法を使う必要はない。確認メッセージは、ユーザーが購読グループから削除される前に送信されるため、他の 2つのステップのいずれかを使用できます。
{% endalert %}

1. アクションベースのステップ [**WhatsApp インバウンドメッセージを送信**] を含むキャンペーンまたはキャンバスを作成します。[**メッセージ本文の場所**] をオンにして、[**次に該当する**] に「START」と入力します。

![メッセージ本文が「START」であるWhatsApp メッセージステップ。]({% image_buster /assets/img/whatsapp/whatsapp_inbound_message.png %}){: style="max-width:85%;"}

{: start="2"}
2\.キャンペーンまたはキャンバスで、Webhook メッセージステップを作成し、[**リクエスト本文**] を [**生のテキスト**] に変更します。

![Webhook のメッセージステップ。]({% image_buster /assets/img/whatsapp/webhook_step.png %})({: style="max-width:85%;"})

{: start="3"}
3\.[**Webhook URL**] に顧客の[エンドポイント URL ]({{site.baseurl}}/api/basics/)を入力し、その後にエンドポイントのリンク `campaigns/trigger/send` を付加します。たとえば `https://dashboard-02.braze.eu/campaigns/trigger/send` です。

![「Webhook を作成」セクションの下のWebhook URL フィールド。]({% image_buster /assets/img/whatsapp/campaigns_webhook_url.png %}){: style="max-width:70%;"}

{: start="4"}
4\.[生のテキスト] に次の JSON ペイロードを入力し、`XXXXXXXXXXX` を購読グループ ID に置き換えます。2 つ目のキャンペーンの作成後に、`campaign_id` を置き換える必要があります。

{% raw %}
```json
{
    "campaign_id": "XXXXXXXXXXX",
    "recipients": [
        {
            "external_user_id": "{{${user_id}}}",
            "attributes": {
                "subscription_groups": [
                    {
                        "subscription_group_id": "XXXXXXXXXXX",
                        "subscription_state": "subscribed"
                    }
                ]
            }
        }
    ]
}
```
{% endraw %}

{: start="5"}
5. WhatsAppキャンペーン（2つ目のキャンペーン）を作成し、トリガーをAPIに設定する。必ず、この `campaign_id` を最初のキャンペーンの JSON ペイロードにコピーしてください。

#### 考慮事項

- キャンバスの API トリガー JSON ペイロード内からの属性更新はまだサポートされていないため、WhatsApp 応答メッセージについてのみ WhatsApp キャンペーンをトリガーできます (ステップ 2 と同様)。
- 応答メッセージとして送信するには、WhatsApp テンプレートの承認を受ける必要があります。なぜなら、クイックレスポンスには、インバウンドメッセージのトリガーが同じキャンペーンまたはキャンバス内にあることが必要だからだ。[ユーザー更新ステップ](#user-update-step)を使用すると、Meta の承認なしでクイック応答メッセージを送信できます。

## "regex"と"is"修飾子の違いを理解する

このテーブルでは、`STOP` がトリガーワードの例として使用され、修飾子の動作を示しています。

| Modifier | トリガーワード | アクション (Action) |
| --- | --- | --- |
| `Is` | `STOP` | 大文字と小文字に関係なく、「stop」に完全一致する単語の使用をすべて検出します。たとえば、"stop"はキャッチしますが、"はストップ"はキャッチしません。 |
| `Matches regex` | `STOP` | そのユースケースで "STOP "が使われた場合はすべてキャッチする。例えば、これは「STOP」と「PLEASE STOP」はキャッチするが、「STOP」はキャッチしない。 |
| `Matches regex` | `(?i)STOP(?-i)` | 大文字と小文字に関係なく「STOP」の使用をすべて検出します。例えば 「stop」、「please stop」、「never stop sending me messages」を検出します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

