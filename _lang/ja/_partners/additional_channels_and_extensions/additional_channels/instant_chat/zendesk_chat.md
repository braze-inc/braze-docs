---
nav_title: Zendesk
article_title: Zendesk Chat
description: "Zendesk ChatとBrazeを統合し、双方向のSMS会話を設定する方法を学習する。"
alias: /partners/zendesk_chat/
page_type: partner
search_tag: Partner

---

# Zendesk Chat

> [Zendesk Chat は](https://www.zendesk.com/service/messaging/)、各プラットフォームの Webhook を使用して、双方向の SMS 会話を設定する。ユーザーがサポートを要請すると、Zendeskにチケットが作成される。エージェントのレスポンシブは、APIトリガーのSMSキャンペーンを通じてBrazeに転送され、ユーザーの返信はZendeskに送り返される。

## 前提条件


| 前提条件 | 説明 |
|---|---|
| Zendeskアカウント | このパートナーシップを利用するには、Zendeskのアカウントが必要である。|
| Zendesk Basic 認証トークン | Zendesk Basic Authorization Token は、Braze から Zendesk へのアウトバウンド Webhook リクエストを行うために使用されます。|
| Braze REST APIキー  | `campaigns.trigger.send` 権限を持つ Braze REST API キー。これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。|

## ユースケース

Braze SMS機能とZendeskライブエージェントレスポンスを組み合わせることで、カスタマーサポートの効率を高め、ユーザーからの問い合わせに迅速に人的サポートで対応する。

## Zendeskチャットを統合する

### ステップ1: ZendeskでWebhookを作成する

1. Zendesk 開発者コンソールで、Webhooks にアクセスする： {% raw %}`https://{{url}}.zendesk.com/admin/apps-integrations/webhooks/webhooks`{% endraw %}
2. [**Webhook の作成**] で、[**トリガーまたはオートメーション**] を選択します。
3. **エンドポイント URL** に、**campaign/trigger/send** エンドポイントを追加します。
4. [**認証**] で [**ベアラートークン**] を選択し、`campaigns.trigger.send` 権限を持つ Braze REST API キーを追加します。

![Zendesk Webhook の例。]({% image_buster /assets/img/zendesk/instant_chat/chat1.png %}){: style="max-width:70%;"}

### ステップ2: アウトバウンドSMSキャンペーンを作成する

次に、ZendeskからのWebhookをリッスンし、顧客にカスタムSMSレスポンスを送信するSMSキャンペーンを作成する。

#### ステップ 2.1:メッセージを作成する

Zendesk が API を介してメッセージのコンテンツを送信する場合、次の形式になります。

```
**----------------------------------------------\n\n{Replier Name}, {Replier Date}\n\n{Message}**
```

そのため、メッセージ内に表示させたい詳細をこの文字列から抽出する必要があります。そうしないと、ユーザーにすべての詳細が表示されてしまいます。

![フォーマットなしのSMSの例。]({% image_buster /assets/img/zendesk/instant_chat/chat2.png %}){: style="max-width:40%;"}

**Message** テキストボックスに、次の Liquid コードとオプトアウト言語またはその他の静的コンテンツを追加します。

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

![フォーマット付きSMSの例。]({% image_buster /assets/img/zendesk/instant_chat/chat3.png %}){: style="max-width:70%;"}

#### ステップ 2.2:配達のスケジュールを立てる

配信タイプには、 [**API トリガー配信**] を選択し、次のステップで使用するキャンペーン ID をコピーします。

![API トリガー配信]({% image_buster /assets/img/zendesk/instant_chat/chat4.png %}){: style="max-width:70%;"}

最後に、[**配信コントロール**] で「再適格性」をオンにします。

![[配信コントロール] で有効になっている再適格性。]({% image_buster /assets/img/zendesk/instant_chat/chat5.png %})

### ステップ 3: Zendeskでエージェントの返信先をBrazeに転送するトリガーを作成する。

[**オブジェクトとルール**] > [**ビジネスルール**] > **[トリガー**] に移動します。

1. 新しい**カテゴリ** を作成します (たとえば、**メッセージのトリガー**)。
2. 新しい**トリガー**を作成します (たとえば、**SMS Braze で応答する**)。
3. [**条件**] で以下を選択します。
- **[Ticket] > [Comment]** が**表示され、リクエスターはコメントを確認できる**ため、新しいパブリックコメントがチケット更新に含まれるたびにメッセージがトリガーされます。
- **チケット発行** *>更新は* **Webサービス(API)ではないので**、ユーザーがBrazeからメッセージを送っても携帯電話に転送されない。Zendeskからのメッセージのみが転送される。

![SMS Braze で応答します。]({% image_buster /assets/img/zendesk/instant_chat/chat6.png %}){: style="max-width:70%;"}

[**アクション**] で [**Webhook で通知**] を選択し、ステップ1 で作成したエンドポイントを選択します。次に、APIコールのボディを指定する。[ステップ2.2](#step-22-schedule-the-delivery)の`campaign_id`をリクエスト本文に入力します。

![SMS Braze JSON 本文経由で応答します。]({% image_buster /assets/img/zendesk/instant_chat/chat7.png %}){: style="max-width:70%;"}

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

![チケットがクローズされたときにユーザーを更新します。]({% image_buster /assets/img/zendesk/instant_chat/chat8.png %}){: style="max-width:70%;"}

**API トリガー配信**を選択し、キャンペーン ID をコピーします。

次に、チケットがクローズされたときにBrazeに通知するトリガーを設定する：
- カテゴリー**メッセージのトリガー**
- [条件] で、**[チケット] > [チケットのステータス]** を選択し、[**解決済み**] に変更します。

![Zendesk に設定されたチケットを解決しました。]({% image_buster /assets/img/zendesk/instant_chat/chat9.png %}){: style="max-width:70%;"}

[**アクション**] で、[**Webhook で通知**] を選択し、作成した2番目のエンドポイントを選択します。そこから、API 呼び出しの本文を指定する必要があります。

![解決したチケットのJSON本体。]({% image_buster /assets/img/zendesk/instant_chat/chat10.png %}){: style="max-width:70%;"}

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

管理センターで、サイドバーの[**People]**を選択し、[**Configuration**]>[**User fields**]を選択する。カスタムユーザーフィールド `braze_external_id` を追加します。

### ステップ6: インバウンドSMS転送の設定

次に、Braze で2つの新しい Webhook キャンペーンを作成します。これにより、顧客からのインバウンド SMS を Zendesk の受信トレイに転送できます。

| キャンペーン           | 目的                                                                              |
|--------------------|--------------------------------------------------------------------------------------|
| Webhook キャンペーン 1 | Zendesk に新しいチケットを作成する。                                                     |
| Webhook キャンペーン 2 | 顧客からインバウンドで送信されたすべての会話型 SMS 応答を Zendesk に転送します。 |
{: .reset-td-br-1 .reset-td-br-2 }

#### ステップ6.1：SMSキーワードカテゴリを作成する

Brazeのダッシュボードで、**オーディエンス**に移動し、**SMSサブスクリプショングループ**を選択して、**カスタムキーワードを追加**を選択します。以下のフィールドに入力して、Zendesk専用のSMSキーワードカテゴリを作成する。

| フィールド            | 説明                                                                                                               |
|------------------|---------------------------------------------------------------------------------------------------------------------------|
| キーワードカテゴリ | キーワードカテゴリの名前、例えば`ZendeskSMS1`。                                                                 |
| キーワード         | あなたのカスタムキーワード、例えば`SUPPORT`。                                                                                  |
| 返信メッセージ    | キーワードが検出されたときに送信されるメッセージ。例えば、"A customer service rep will reach out to you shortly."（顧客サービス担当者がまもなくご連絡します）など。 |
{: .reset-td-br-1 .reset-td-br-2 }

![Brazeの例としてのSMSキーワードカテゴリ]({% image_buster /assets/img/zendesk/instant_chat/chat11.png %}){: style="max-width:70%;"}

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

![2つの必須ヘッダーを含むリクエストの例。]({% image_buster /assets/img/zendesk/instant_chat/chat12.png %}){: style="max-width:70%;"}


#### ステップ6.3：最初の配達をスケジュールする

**スケジュール配信**のために、**アクションベースの配信**を選択し、次にトリガータイプとして**SMS受信メッセージの送信**を選択します。また、以前に設定したSMSサブスクリプショングループとキーワードカテゴリーも追加する。

![最初のWebhookキャンペーンの「スケジュール配信」ページ。]({% image_buster /assets/img/zendesk/instant_chat/chat13.png %})

[**配信コントロール**] で「再適格性」をオンにします。

![最初の Webhook キャンペーンの [配信コントロール]で再適格性が選択されている。]({% image_buster /assets/img/zendesk/instant_chat/chat14.png %})

#### ステップ6.4：2番目のWebhookキャンペーンを作成する

ユーザーからの残りの SMS メッセージを Zendesk に転送する Webhook キャンペーンを設定する：

Zendesk はチケット ID を文字列として送信するので、コンテンツブロックを作成して文字列を整数に変換し、Zendesk の Webhook で使用できるようにする。

{% raw %}
```liquid
{% assign var = {{custom_attribute.${zendesk_ticket}}} | to_i %}{{var}}
```
{% endraw %}

Webhook composer 内で
- Webhook URL:{% raw %}https://{{url}}.zendesk.com/api/v2/tickets/{{content_blocks.${to_int}}}.json{% endraw %}
- リクエスト：PUT:
- KVP：
    - Content-Type:application/JSON
    - 認証:Basic {{Token}}

本文のサンプル： 

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
- 再適格性基準を設定します。
- 該当するオーディエンス（この場合、カスタム属性**zendesk_ticket_open**が**true**）を追加する。

[2]: {% image_buster /assets/img/zendesk/instant_chat/chat2.png %}
