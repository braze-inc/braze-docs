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

> WhatsAppのオプトインとオプトアウトの処理は非常に重要で、WhatsAppは[電話番号の品質評価を](https://www.facebook.com/business/help/896873687365001)監視しているため、評価が低いとメッセージの上限が減る可能性がある。質の高い評価を確保する一つの方法は、ユーザーによるブロックや報告を防ぐことだ。これは、[質の高いメッセージング](https://developers.facebook.com/docs/whatsapp/messaging-limits#quality-rating-and-messaging-limits)（ユーザーにとっての価値など）を提供し、メッセージの頻度をコントロールし、顧客が今後のコミュニケーション受信をオプトアウトできるようにすることで実現できる。 

オプトインは、外部ソースから、またはSMSやアプリ内、ブラウザ内メッセージなどのブレイズメソッドから来ることができる。オプトアウトは、Brazeで設定したキーワードとWhatsAppのマーケティングボタンで対応できる。オプトインとオプトアウトの設定については、以下の方法を参照されたい。

#### オプトインの方法
- [外部からのオプトイン方式](#external-to-braze-opt-in-methods)
  - [外部オプトインリスト](#externally-built-opt-in-list)
  - [カスタマーサポートWhatsAppチャンネルのアウトバウンドメッセージ](#outbound-message-in-customer-support-whatsapp-channel)
  - [WhatsAppのインバウンドメッセージ](#inbound-whatsapp-message)
- [ブレーズを利用したオプトイン・メソッド](#braze-powered-opt-in-methods)

#### オプトアウトの方法
- [一般的なオプトアウト・キーワード](#general-opt-out-keywords)
- [マーケティング・オプトアウトの選択](#marketing-opt-out-selection)

## Braze WhatsAppチャンネルのオプトインを設定する

WhatsAppのオプトインについては、[WhatsAppの要件に](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/)準拠する必要がある。また、Brazeに以下の情報を提供する必要がある：
- 各ユーザーの`external_id` 、[電話番号]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_phone_numbers/)、更新された購読状況。これは、[SDKを](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_user.html#a74092a50fcda364bb159013d0222e287)使用するか、[`/users/track` エンドポイントを通じて](https://www.braze.com/docs/api/endpoints/user_data/post_user_track/)、電話番号と契約ステータスを更新することで行うことができる。 

{% alert note %}
Brazeは、`/users/track` 、[Subscription]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/#update-subscription-status)グループで知ることができる購読ステータスの更新を可能にするエンドポイントの改良をリリースした。ただし、[`/v2/subscription/status/set` エンドポイントを]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status_v2/)使用してすでにオプトイン・プロトコルを作成している場合は、そちらで引き続き作成することができる。
{% endalert %}

### 外部からのオプトイン方式

お客様のアプリまたはウェブサイト（アカウント登録、チェックアウトページ、アカウント設定、クレジットカード端末）をBrazeに提供する。

既にEメールやテキストでのマーケティング同意を得ている場合は、WhatsApp用のセクションを追加する。ユーザーがオプトインした後、`external_id` 、[電話番号]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_phone_numbers/)、更新された購読ステータスが必要となる。これを行うには、Brazeのインストール方法に応じて、[`/subscription/status/set` エンドポイントを]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/)活用するか、[SDKを](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_user.html#a74092a50fcda364bb159013d0222e287)使用する。

#### 外部オプトインリスト

以前WhatsAppを利用したことがあれば、WhatsAppの要件に沿ったオプトインでユーザーリストを作成済みかもしれない。この場合、[以下の情報を]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import#csv)CSVまたはAPIでBrazeにアップロードする。

#### カスタマーサポートWhatsAppチャンネルのアウトバウンドメッセージ

カスタマー・サポート・チャネルでは、解決された問題に対して、マーケティング・メッセージングのオプトインを希望するかどうかを尋ねる自動メッセージでフォローアップする。ここでの機能は、選択したカスタマー・サポート・ツールで利用可能な機能と、ユーザー情報を保管する場所に依存する。

1. WhatsApp Businessの電話番号から[メッセージリンクを](https://business.facebook.com/business/help/890732351439459?ref=search_new_0)送信する。
2. 顧客がオプトインを示すために「はい」と答える[クイック返信アクションを]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/user_messages/#quick-replies)提供する。
3. カスタムキーワードトリガーを設定する。
4. どちらのアイディアにせよ、おそらく次のようなパスが必要だろう：
	- [`/users/track` エンドポイントを]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)呼び出し、ユーザーを更新または作成する。 
	- [`/subscription/status/set` のエンドポイントを]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/)利用するか、[SDKを](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_user.html#a74092a50fcda364bb159013d0222e287)使用する。 

#### WhatsAppのインバウンドメッセージ 

顧客にWhatsApp番号にインバウンドメッセージを送ってもらう。

これは、新しいチャンネルでユーザーに確認メッセージを受け取らせるかどうかによって、キャンバスまたはキャンペーンとして設定できる。

1. インバウンドメッセージのアクションベースの配信トリガーでキャンペーンを作成する。
2. ウェブフックキャンペーンを作成する。Webhookの例については、[Subscription groupsを]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/opt-ins_and_opt-outs/#update-subscription-status)参照のこと。

{% alert tip %}
[WhatsApp](https://business.facebook.com/wa/manage/phone-numbers/)チャンネルに参加するためのURLやQRコードは、[WhatsAppマネージャー](https://business.facebook.com/wa/manage/phone-numbers/)内の「**電話番号**」>「**メッセージリンク**」から作成できる。<br>![]({% image_buster /assets/img/whatsapp/whatsapp115.png %}){: style="max-width:55%;"}
{% endalert %}

### ブレーズを利用したオプトイン・メソッド 

#### SMSメッセージ

CANVASでキャンペーンを設定し、以下のいずれかの方法でWhatsAppメッセージの受信をオプトインするかどうかを顧客に尋ねる：
- 顧客セグメント：米国外の購読マーケティンググループ
- カスタム・キーワード・トリガーの設定

[サブスクリプション グループを]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/#update-subscription-status)表示して、ユーザー プロファイルのサブスクリプション ステータスを更新する方法について学ぶ。

#### アプリ内またはブラウザ内のメッセージ

アプリ内メッセージやブラウザ内ポップアップを作成し、WhatsApp利用のオプトインを促す。

BrazeSDKとのインターフェースに[JavaScriptの「ブリッジ」を]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/html_in-app_messages#javascript-bridge)使用した[HTMLアプリ内メッセージを](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates/4-sms-capture-modal)使用する。WhatsAppの購読グループIDを必ず使用すること。 

#### 電話番号取得フォーム

アプリ内メッセージ用の[電話番号取得フォーム]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/templates/phone_number_capture/)テンプレートをドラッグ＆ドロップエディターで使い、ユーザーの電話番号を収集してWhatsApp購読グループを増やそう。

## Braze WhatsAppチャンネルのオプトアウトを設定する

### 一般的なオプトアウト・キーワード

キャンペーンやキャンバスを設定することで、特定の単語でメッセージを送ったユーザーが、今後のメッセージングをオプトアウトできるようにすることができる。キャンバスは、オプトアウトが成功したことを確認するフォローアップメッセージを含めることができるので、特に有益である。 

#### ステップ 1:トリガーを "Inbound WhatsApp Message "としてキャンバスを作成する。
 
![][6]{: style="max-width:85%;"}

キーワードトリガーを選択する際には、「Stop」や「No Message」といった単語を含める。この方法を選択する場合は、顧客にオプトアウトの言葉を確実に伝えること。例えば、最初のオプトインを受け取った後、「これらのメッセージをオプトアウトするには、いつでも "Stop "とメッセージしてください」といったフォローアップの返答を含める。 

![][7]

#### ステップ 2:ユーザーのプロフィールを更新する

[サブスクリプション・グループで]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/#update-subscription-status)説明されている方法のいずれかを使用して、ユーザーのプロファイルを更新する。

### マーケティング・オプトアウトの選択

WhatsAppメッセージテンプレート作成機能では、「マーケティングオプトアウト」オプションを設定することができる。これを含むときはいつでも、テンプレートがサブスクリプショングループ変更のための後続ステップを持つキャンバスで使用されていることを確認すること。 

1. マーケティングオプトアウト」クイック返信でメッセージテンプレートを作成する。<br>![][11]<br><br>![][12]<br><br>
2. このメッセージテンプレートを使ってキャンバスを作成する。<br><br>
3. 前述の例のステップに従うが、トリガーテキストは "STOP PROMOTIONS "とする。<br><br>
4. [サブスクリプション・グループで]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/#update-subscription-status)説明されている方法のいずれかを使用して、ユーザーのサブスクリプション・ステータスを更新する。

## オプトインとオプトアウトのワークフローを設定する

WhatsAppのキーワード応答ワークフローは、この2つの方法で「START」と「STOP」を設定できる：

- [ユーザー更新ステップ](#user-update-step)
- [Webhookキャンペーンで2つ目のWhatsAppキャンペーンをトリガーする](#webhook-campaign-to-trigger-a-second-whatsapp-campaign)

### ユーザー更新ステップ

[ユーザー更新ステップでは]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/)、ユーザーがWhatsApp購読グループの電話番号にキーワードを送信すると、そのユーザーの電話番号をWhatsApp購読グループに追加することができる。

ユーザー更新ステップは、ユーザーが自分の電話番号がサブスクリプショングループに追加される前にキャンバスの次のステップに進まないので、競合状態を回避する。また、セットアップの手順も他の方法より少ないので、ブレイズは一般的にこの方法を推奨している。

1. アクションベースのステップ「**WhatsAppインバウンドメッセージを送信**」でキャンバスを作成する。**Where message body "**を選択し、**"Is "**に "START "を入力する。

{% alert important %}
STOP」メッセージについては、オプトアウトを確認するメッセージステップとユーザー更新ステップを反転させる。そうしないと、ユーザーはまず購読グループからオプトアウトされ、確認メッセージを受け取る資格がなくなる。
{% endalert %}

![][13]{: style="max-width:70%;"}

{: start="2"}
2\.キャンバスで、**Set Up User Update**ステップを作成し、**Actionに** **Advanced JSON Editorを**選択する。<br><br>![][14]<br><br>
3\.以下のJSONペイロードを**User Updateオブジェクトに**投入し、`XXXXXXXXXXX` をあなたのサブスクリプショングループIDに置き換える：

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
4\.後続のWhatsAppメッセージステップを追加する。<br><br>![][15]{: style="max-width:20%;"}

#### 考慮事項

Brazeは[User Updateステップの]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/)リクエストをバッチ処理するため、更新の完了速度はまちまちかもしれない。

### Webhookキャンペーンで2つ目のWhatsAppキャンペーンをトリガーする

Webhookキャンペーンは、ユーザーの電話番号をWhatsApp購読グループに追加した後、ユーザーが購読グループの電話番号にキーワードを送信すると、2つ目のキャンペーンへのエントリーをトリガーすることができる。

{% alert important %}
STOPメッセージにこの方法を使う必要はない。確認メッセージは、ユーザーが購読グループから削除される前に送信されるので、他の2つのステップのいずれかを使用することができる。
{% endalert %}

1. キャンペーンまたはキャンバスにアクションベースのステップを作成する**WhatsAppインバウンドメッセージを送信する**。**Where message body "**を選択し、**"Is "**に "START "を入力する。<br><br>![][13]{: style="max-width:70%;"}<br><br>
2. キャンペーンまたはキャンバスで、Webhook Messageステップを作成し、**Request Bodyを** **Raw Textに**変更する。<br><br>![][16]<br><br>
3. **Webhook URLに**顧客の[エンドポイントURLを]({{site.baseurl}}/api/basics/)入力し、続いてエンドポイントリンク`campaigns/trigger/send` を入力する。例えば、`https://dashboard-02.braze.eu/campaigns/trigger/send` 。<br><br>![19]{: style="max-width:70%;"}<br><br>
4. 生テキストに、以下のJSONペイロードを入力し、`XXXXXXXXXXX` をあなたの購読グループIDに置き換える。2つ目のキャンペーンを作成したら、`campaign_id` 。

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
5. WhatsAppキャンペーン（2つ目のキャンペーン）を作成し、トリガーをAPIに設定する。この`campaign_id` 、最初のキャンペーンのJSONペイロードにコピーしておくこと。

#### 考慮事項

- Canvas APIトリガーJSONペイロード内からの属性更新はまだサポートされていないため、WhatsAppレスポンスメッセージに対してのみWhatsAppキャンペーンをトリガーすることができる（ステップ2と同様）。
- レスポンスメッセージとして送信するには、WhatsAppテンプレートを承認する必要がある。なぜなら、クイックレスポンスには、インバウンドメッセージのトリガーが同じキャンペーンまたはキャンバス内にあることが必要だからだ。[User Updateステップを](#user-update-step)使えば、Metaの承認なしにクイックレスポンスメッセージを送ることができる。


[1]: {% image_buster /assets/img/whatsapp/whatsapp111.png %}
[2]: {% image_buster /assets/img/whatsapp/whatsapp112.png %}
[3]: {% image_buster /assets/img/whatsapp/whatsapp113.png %}
[4]: {% image_buster /assets/img/whatsapp/whatsapp114.png %}
[5]: {% image_buster /assets/img/whatsapp/whatsapp115.png %}
[6]: {% image_buster /assets/img/whatsapp/whatsapp116.png %}
[7]: {% image_buster /assets/img/whatsapp/whatsapp117.png %}
[8]: {% image_buster /assets/img/whatsapp/whatsapp118.png %}
[9]: {% image_buster /assets/img/whatsapp/whatsapp119.png %}
[10]: {% image_buster /assets/img/whatsapp/whatsapp120.png %}
[11]: {% image_buster /assets/img/whatsapp/whatsapp121.png %}
[12]: {% image_buster /assets/img/whatsapp/whatsapp122.png %}
[13]: {% image_buster /assets/img/whatsapp/whatsapp_inbound_message.png %}
[14]: {% image_buster /assets/img/whatsapp/user_update.png %}
[15]: {% image_buster /assets/img/whatsapp/message_step.png %}
[16]: {% image_buster /assets/img/whatsapp/webhook_step.png %}
[17]: {% image_buster /assets/img/whatsapp/webhook_url.png %}
[18]: {% image_buster /assets/img/whatsapp/request_parameters.png %}
[19]: {% image_buster /assets/img/whatsapp/campaigns_webhook_url.png %} 
