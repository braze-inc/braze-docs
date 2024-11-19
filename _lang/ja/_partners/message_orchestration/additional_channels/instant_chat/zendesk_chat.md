---
nav_title: Zendesk
article_title: ゼンデスク・チャット
description: "Zendesk ChatとBrazeを統合し、双方向のSMS会話を設定する方法を学習する。"
alias: /partners/zendesk_chat/
page_type: partner
search_tag: Partner

---

# ゼンデスク・チャット

> [Zendesk Chat は](https://www.zendesk.com/service/messaging/)、各プラットフォームの Webhook を使用して、双方向の SMS 会話を設定する。ユーザーがサポートを要請すると、Zendeskにチケットが作成される。エージェントのレスポンシブは、APIトリガーのSMSキャンペーンを通じてBrazeに転送され、ユーザーの返信はZendeskに送り返される。

## 前提条件


| 前提条件 | 説明 |
|---|---|
| Zendeskアカウント | このパートナーシップを利用するには、Zendeskのアカウントが必要である。|
| Zendesk Basic 認証トークン | Zendesk Basic Authorizationトークンは、BrazeからZendeskへのアウトバウンドWebhookリクエストに使用される。|
| Braze REST APIキー  | `campaigns.trigger.send` 権限を持つ Braze REST API キー。これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。|

## ユースケース

Braze SMS機能とZendeskライブエージェントレスポンスを組み合わせることで、カスタマーサポートの効率を高め、ユーザーからの問い合わせに迅速に人的サポートで対応する。

## Zendeskチャットを統合する

### ステップ1:ZendeskでWebhookを作成する

1. Zendesk 開発者コンソールで、Webhooks にアクセスする： {% raw %}`https://{{url}}.zendesk.com/admin/apps-integrations/webhooks/webhooks`{% endraw %}
2. **Create Webhookで**、**トリガーまたはオートメーションを**選択する。
3. **エンドポイントURLには**、**/campaign/trigger/send**エンドポイントを追加する。
4. **認証]**で、[**ベアラートークン]**を選択し、`campaigns.trigger.send` 権限を持つ Braze REST API キーを追加する。

![Zendesk Webhook の例。][1]{: style="max-width:70%;"}

### ステップ2:アウトバウンドSMSキャンペーンを作成する

次に、ZendeskからのWebhookをリッスンし、顧客にカスタムSMSレスポンスを送信するSMSキャンペーンを作成する。

#### ステップ 2.1:メッセージを作成する

Zendesk が API 経由でメッセージを送信する際の形式は、次のようになる：

```
**----------------------------------------------\n\n{Replier Name}, {Replier Date}\n\n{Message}**
```

したがって、この文字列からメッセージに表示したい詳細を抽出する必要がある。

![フォーマットなしのSMSの例。][2]{: style="max-width:40%;"}

**メッセージテキストボックスに**、以下のメッセージングコードと、オプトアウト言語、その他の静的コンテンツを追加する：

{% raw %}
```liquid
{% assign body = {{api_trigger_properties.${msg_body}}} %}
{% assign msg = body | split: "
" %}
New message from Zendesk: 
{{msg[2]}}
 
Feel free to respond directly to this number!
```
{% endraw %}

![フォーマット付きSMSの例。][3]{: style="max-width:70%;"}

#### ステップ 2.2:配達のスケジュールを立てる

配信タイプは**API-トリガー配信を**選択し、次のステップで使用するキャンペーンIDをコピーする。

![APIトリガー配信][4]{: style="max-width:70%;"}

最後に、「**配信コントロール**」で「再資格」をオンにする。

!["デリバリーコントロール "の下でイネーブルメントを有効にする。][5]

### ステップ 3:Zendeskでエージェントの返信先をBrazeに転送するトリガーを作成する。

**オブジェクトとルール**>**ビジネスルール**>**トリガーに**進む。

1. 新しい**カテゴリーを**作成する（例えば、**トリガーメッセージ**）。
2. 新しい**トリガーを**作成する（例えば、**Respond via SMS Braze**）。
3. **条件**」で選択する：
- **チケット>コメントが** **存在し、要求者がコメントを見ることができる**ため、チケット更新に新しいパブリックコメントが含まれるたびにメッセージがトリガーされる。
- **チケット発行** *>更新は* **Webサービス(API)ではないので**、ユーザーがBrazeからメッセージを送っても携帯電話に転送されない。Zendeskからのメッセージのみが転送される。

![SMS Brazeで対応する。][6]{: style="max-width:70%;"}

**アクション]**で[**Webhookで通知]**を選択し、ステップ1で作成したエンドポイントを選択する。次に、APIコールのボディを指定する。[ステップ2.](#step-22-schedule-the-delivery)2の`campaign_id` をリクエストボディに入力する。

![SMS Braze JSONボディで応答する。][7]{: style="max-width:70%;"}

{% raw %}
```liquid
{
    "campaign_id": "{{YOUR_CAMPAIGN_ID}}",
    "recipients": [
        {
            "external_user_id": "{{ticket.requester.custom_fields.braze_external_id}}",
			"trigger_properties": {
    "msg_body": "{{ticket.latest_public_comment_html}}"
		},
		"attributes": {
        "zendesk_ticket" : "{{ticket.id}}",
	"zendesk_ticket_open" : "true"
    }
        }
    ]
}
```
{% endraw %}


### ステップ4:チケットのクローズ時にユーザーを更新するトリガーをZendeskに作成する

チケットがクローズされたことをユーザーに通知したい場合は、Brazeでレスポンシブボディのテンプレートを使って新しいキャンペーンを作成する。

![チケットがクローズされたときにユーザーを更新する。][8]{: style="max-width:70%;"}

**APIトリガー配信を**選択し、キャンペーンIDをコピーする。

次に、チケットがクローズされたときにBrazeに通知するトリガーを設定する：
- カテゴリー**トリガーメッセージ**
- 条件」で**「チケット」>「チケット発行ステータス**」を選択し、「**解決済み**」に変更する。

![Zendeskに設定されたチケットを解決した。][9]{: style="max-width:70%;"}

**アクション]**で[**Webhookで通知]**を選択し、先ほど作成した2番目のエンドポイントを選択する。そこから、APIコールのボディを指定する必要がある：

![解決したチケットのJSON本体。][10]{: style="max-width:70%;"}

{% raw %}
```liquid
{
    "campaign_id": "{{YOUR_API_KEY}}",
    "recipients": [
        {
            "external_user_id": "{{ticket.requester.custom_fields.braze_external_id}}",
"trigger_properties": {
    "msg_body": "Your ticket has been closed"
		},
,
			"attributes": {
	"zendesk_ticket_open" : "false"
    }
        }
    ]
}
```
{% endraw %}

### ステップ 5: Zendesk でカスタムユーザーフィールドを追加する

管理センターで、サイドバーの[**People]**を選択し、[**Configuration**]>[**User fields**]を選択する。カスタム・ユーザー・フィールド`braze_external_id` を追加する。

### ステップ 6:インバウンドSMS転送の設定

次に、Brazeで新しいWebhookキャンペーンを2つ作成し、顧客からの受信トレイをZendeskの受信トレイに転送できるようにする。

| Campaign           | 目的                                                                              |
|--------------------|--------------------------------------------------------------------------------------|
| Webhook キャンペーン 1 | Zendesk に新しいチケットを作成する。                                                     |
| Webhook キャンペーン 2 | 顧客からZendeskに送信されたすべての会話型SMSレスポンスを転送する。 |
{: .reset-td-br-1 .reset-td-br-2 }

#### ステップ6.1：SMSキーワードカテゴリを作成する

Brazeのダッシュボードで、**オーディエンス**に移動し、**SMSサブスクリプショングループ**を選択して、**カスタムキーワードを追加**を選択します。以下のフィールドに入力して、Zendesk専用のSMSキーワードカテゴリを作成する。

| フィールド            | 説明                                                                                                               |
|------------------|---------------------------------------------------------------------------------------------------------------------------|
| キーワードカテゴリ | キーワードカテゴリの名前、例えば`ZendeskSMS1`。                                                                 |
| キーワード         | あなたのカスタムキーワード、例えば`SUPPORT`。                                                                                  |
| 返信メッセージ    | キーワードが検出されたときに送信されるメッセージ。例えば、"A customer service rep will reach out to you shortly."（顧客サービス担当者がまもなくご連絡します）など。 |
{: .reset-td-br-1 .reset-td-br-2 }

![BrazeのSMSキーワードカテゴリーの例。][11]{: style="max-width:70%;"}

#### ステップ6.2：最初のWebhookキャンペーンを作成する

Brazeダッシュボードで、最初のWebhookキャンペーンを作成する。このメッセージはZendeskにサポートが要求されていることを知らせる。

Webhook composerで、以下のフィールドに記入する：
- Webhook URL:{% raw %}https://{{url}}.zendesk.com/api/v2/tickets{% endraw %}
- HTTP メソッド:POST
- リクエストヘッダー：
- Content-Type: application/json
- 認証: Basic {{Token}}
- リクエスト本文： 

{% raw %}
```liquid
{
  "ticket": {
    "subject": "Action Needed",
    "comment": {
      "body": "{{sms.${inbound_message_body}}}"
    },
"requester":{
"name": "{{${first_name}}} {{${last_name}}}",
"user_fields": {
"braze_external_id": "{{${user_id}}}"
}
},
    "priority": "normal",
    "type": "problem"
  }
}
```
{% endraw %}

![つの必須ヘッダーを持つリクエスト例。][12]{: style="max-width:70%;"}


#### ステップ6.3：最初の配達をスケジュールする

**スケジュール配信**のために、**アクションベースの配信**を選択し、次にトリガータイプとして**SMS受信メッセージの送信**を選択します。また、以前に設定したSMSサブスクリプショングループとキーワードカテゴリーも追加する。

![最初のWebhookキャンペーンの「配信スケジュール」ページ。][13]

**配信コントロール]**で、[再選考]をオンにする。

![最初のWebhookキャンペーンの「配信コントロール」で再資格を選択した。][14]

#### ステップ6.4：2番目のWebhookキャンペーンを作成する

ユーザーからの残りの SMS メッセージを Zendesk に転送する Webhook キャンペーンを設定する：

Zendesk はチケット ID を文字列として送信するので、コンテンツブロックを作成して文字列を整数に変換し、Zendesk の Webhook で使用できるようにする。

{% raw %}
```liquid
{% assign var = {{custom_attribute.${zendesk_ticket}}} | to_i %}{{var}}
```
{% endraw %}

Webhook composerにある：
- Webhook URL:{% raw %}https://{{url}}.zendesk.com/api/v2/tickets/{{content_blocks.${to_int}}}.json{% endraw %}
- リクエストだ：PUT:
- KVPだ：
    - Content-Type:application/JSON
    - 認証:Basic {{Token}}

ボディのサンプル： 

{% raw %}
```liquid
{
  "ticket": {
    "comment": {
      "body": "Inbound message from {{${first_name}}} {{${last_name}}}: {{sms.${inbound_message_body}}}"
    }
}
}
```
{% endraw %}

#### ステップ6.5：2つ目のWebhookキャンペーンのセットアップを完了する。
- その他」のカテゴリーでインバウンドメッセージを送信したユーザーに対して、アクションベースのトリガーを設定する。
- 再資格基準を設定する。
- 該当するオーディエンス（この場合、カスタム属性**zendesk_ticket_open**が**true**）を追加する。

[1]: {% image_buster /assets/img/zendesk/instant_chat/chat1.png %}
[2]: {% image_buster /assets/img/zendesk/instant_chat/chat2.png %}
[3]: {% image_buster /assets/img/zendesk/instant_chat/chat3.png %}
[4]: {% image_buster /assets/img/zendesk/instant_chat/chat4.png %}
[5]: {% image_buster /assets/img/zendesk/instant_chat/chat5.png %}
[6]: {% image_buster /assets/img/zendesk/instant_chat/chat6.png %}
[7]: {% image_buster /assets/img/zendesk/instant_chat/chat7.png %}
[8]: {% image_buster /assets/img/zendesk/instant_chat/chat8.png %}
[9]: {% image_buster /assets/img/zendesk/instant_chat/chat9.png %}
[10]: {% image_buster /assets/img/zendesk/instant_chat/chat10.png %}
[11]: {% image_buster /assets/img/zendesk/instant_chat/chat11.png %}
[12]: {% image_buster /assets/img/zendesk/instant_chat/chat12.png %}
[13]: {% image_buster /assets/img/zendesk/instant_chat/chat13.png %}
[14]: {% image_buster /assets/img/zendesk/instant_chat/chat14.png %}
