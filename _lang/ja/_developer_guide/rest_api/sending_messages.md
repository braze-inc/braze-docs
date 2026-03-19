---
nav_title: メッセージングを行う
article_title: REST API を使ってメッセージを送信する
page_order: 1
page_type: reference
description: "この参考記事では、Braze REST API を使用してプログラムでメッセージを送信する二つの方法について説明する。"
---

# REST API を使ってメッセージを送信する

> バックエンドからリアルタイムでメッセージを送信するには、2つの異なるBrazeエンドポイントを使用できる。それぞれリクエストの形式が異なる。一つはリクエストにメッセージ全文を要求する。もう一つはキャンペーンIDを要求し、ダッシュボードで定義された内容を送信する。

この方法は、APIがサポートするあらゆるメッセージングチャネル（WhatsApp、メール、SMS、プッシュ通知、コンテンツカード、Webhookなど）で機能する。

## 送る方法は二つある

| | [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) | [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) |
| --- | --- | --- |
| **キャンペーン ID** | オプション。ダッシュボードでのキャンペーントラッキングなしで送信する場合は省略する。または、各メッセージにAPIキャンペーンIDと`message_variation_id`「+」を付加してダッシュボードでトラッキングする。 | 必須です。 |
| **メッセージの内容** | リクエストには必ず`messages`オブジェクトを含めなければならない（例：`messages.whats_app`、`messages.email`）。 | 受理されない。メッセージの内容は、Brazeダッシュボード内のキャンペーンで定義される。 |
| **ユースケース** | APIリクエストで内容を完全に指定したメッセージを送信する。 | APIを介して、特定の受信者に対して事前作成されたキャンペーン（ダッシュボード内のコンテンツ）をトリガーする。 |

完全なリクエストとレスポンスの詳細については、「[メッセージを即時送信（APIのみ）]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/)」および[「APIトリガー配信]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/)エンドポイント[を使用したキャンペーン送信」]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/)のエンドポイント参照を参照せよ。

---

## オプション 1: リクエスト`/messages/send`にメッセージ内容を添えて送信する

APIリクエストでメッセージの全文を指定したい場合、このエンドポイントを使用する。オブジェクト`messages`を含め**なければならない**（例えば、,`messages.email``messages.whats_app` , または `messages.sms`など）。キャンペーントラッキングなしで送信するには`campaign_id`省略できる。または、`message_variation_id`各メッセージにAPIキャンペーンIDとを含めることで、ダッシュボードで送信をトラッキングできる（詳細は[エンドポイントリファレンス]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/)を参照）。

**必須：**権限`messages.send`付きのAPI キー。

{% alert important %}
各受信者は、Brazeに既に`external_user_ids`存在している必要がある。送信の一部としてユーザーを作成するには、まず[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)を使用するか、代わりに[オプション2](#option-2-trigger-a-campaign-with-content-in-the-dashboard-campaignstriggersend)（APIトリガー型キャンペーン）を使用する。
{% endalert %}

### 例: WhatsAppのテンプレートメッセージ

```
POST YOUR_REST_ENDPOINT/messages/send
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "external_user_ids": ["user123"],
  "messages": {
    "whats_app": {
      "app_id": "YOUR_APP_ID",
      "subscription_group_id": "YOUR_WHATSAPP_SUBSCRIPTION_GROUP_ID",
      "message_type": "template_message",
      "message": {
        "template_name": "new_message_received",
        "template_language_code": "en_US"
      }
    }
  }
}
```

WhatsAppオブジェクトの完全な仕様については、[WhatsAppオブジェクトを]({{site.baseurl}}/api/objects_filters/messaging/whats_app_object/)参照せよ。

{% alert note %}
この`/messages/send`エンドポイントは、TEXT または 画像（写真）ヘッダーを持つ WhatsApp テンプレートのみをサポートする。DOCUMENT、動画、その他のメディアヘッダータイプについては、代わりに[APIトリガー型キャンペーンエンドポイント]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/)またはBrazeダッシュボードを使用する。
{% endalert %}

### 例: メール

```json
{
  "external_user_ids": ["user123"],
  "messages": {
    "email": {
      "app_id": "YOUR_APP_ID",
      "subject": "Your order has shipped",
      "from": "no-reply@example.com",
      "body": "<p>Your order #12345 is on its way.</p>"
    }
  }
}
```

他のチャネルについては、[メッセージングオブジェクトを]({{site.baseurl}}/api/objects_filters/#messaging-objects)参照せよ。

---

## オプション 2: ダッシュボード`/campaigns/trigger/send`でコンテンツを使ってキャンペーンを開始する

メッセージの内容がBrazeダッシュボードで作成された場合（APIトリガー型キャンペーン）、このエンドポイントを使用する。**必要な**`campaign_id`送信元と受信者を送る。オブジェクト`messages`は送らない。

**必須：**権限`campaigns.trigger.send`付きのAPI キー。

### ステップ 1: APIトリガー型キャンペーンを作成する

1. Brazeのダッシュボードで、**メッセージング**＞**キャンペーン**に移動する。
2. 「**キャンペーン作成」**を選択し、次に「**APIトリガー型キャンペーン**」（「APIキャンペーン」ではない）を選択する。
3. メッセージ送信チャネル（WhatsApp、メール、SMSなど）を追加し、ダッシュボードでメッセージ内容を作成する。
4. **キャンペーンID**（複数のバリアントを使用する場合は**送信ID**も）をメモしておくこと。これらをAPIリクエストで使用する。

APIトリガー型キャンペーンの作成に関する詳細は、[APIトリガー型配信]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/)を参照のこと。

### ステップ 2:API経由でキャンペーンのトリガーを行う

POSTリクエストを  に送信する`/campaigns/trigger/send`。パラメータは`campaign_id`  と`recipients`  （または `broadcast`/`audience`）とする。オブジェクトを含めるな`messages`——コンテンツはキャンペーンから来る。

```
POST YOUR_REST_ENDPOINT/campaigns/trigger/send
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "campaign_id": "YOUR_CAMPAIGN_ID",
  "recipients": [
    {
      "external_user_id": "user123"
    }
  ]
}
```

リクエスト本文全体（、`send_to_existing_only`、`attributes`、などを`trigger_properties`含む）については、[APIトリガー配信]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/#request-body)エンドポイント[を使用したキャンペーン送信]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/#request-body)のリファレンスを参照のこと。

---

## 統合を確認せよ

1. 上記のいずれかの方法でリクエストを送信する。その際、自分のユーザー ID を受信者として指定する。
2. メッセージが送信されたことを確認する。
3. オプション2を使用する場合、Brazeダッシュボードでキャンペーンを確認し、送信が記録されていることを確認せよ。

## 考慮事項

- 対応している場合は、Brazeの[パーソナライゼーション機能]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/)を使ってコンテンツをカスタマイズする。
- メッセージングが関連規制に準拠していることを確認し、必要なオプトアウトオプションとプライバシー通知を含めること。
- その他のエンドポイント（スケジューリング、キャンバストリガーなど）については、[メッセージングエンドポイントを]({{site.baseurl}}/api/endpoints/messaging/)参照せよ。
