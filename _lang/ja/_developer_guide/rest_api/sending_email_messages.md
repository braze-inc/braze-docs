---
nav_title: メールメッセージの送信
article_title: REST API を使用したメールメッセージの送信
page_order: 3
page_type: reference
description: "この参照記事では、Braze REST API と API キャンペーンを使用してメールメッセージを送信する方法について説明します。"
channel:
  - email
---

# REST API を使用したメールメッセージの送信

> Braze REST API を使用して、バックエンドからリアルタイムでトランザクションメールを送信できます。このアプローチにより、プログラムでメールを送信するサービスを構築しながら、Braze ダッシュボードで他のキャンペーンやキャンバスと一緒に配信分析を追跡できます。

これは、コンテンツがバックエンドシステムで定義されるトランザクションメッセージングに特に便利です。たとえば、消費者が別のユーザーからメッセージを受信したときに通知し、Web サイトにアクセスして受信トレイを確認するよう促すことができます。

このアプローチでは、以下のことが可能です。

- バックエンドからリアルタイムでメールをトリガーする。
- 開封、クリック数、バウンスなど、マーケティング所有のすべてのキャンペーンやキャンバスと一緒に分析を追跡する。
- メッセージインタラクションデータを使用して、フォローアップのリターゲティングなどの後続メッセージをトリガーする。
- メッセージ遅延や AB テストなど、追加の Braze 機能でユースケースを拡張する。
- オプションで、[API トリガー配信]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/)に切り替えて、Braze ダッシュボードでメールテンプレートを定義しながら、バックエンドから送信をトリガーする。

REST API を通じてメールを送信するには、Braze ダッシュボードで API キャンペーンを設定し、[`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) エンドポイントを使用してメッセージを送信する必要があります。

## 前提条件

このガイドを完了するには、以下が必要です。

| 要件 | 説明 |
| --- | --- |
| Braze REST API キー | `messages.send` 権限を持つキー。作成するには、**設定** > **API と識別子** > **API キー**に移動します。 |
| Braze アプリ ID | ワークスペース内のアプリの識別子。確認するには、**設定** > **API と識別子**に移動し、**アプリ識別子**セクションを確認します。この値はメールメッセージングオブジェクトの `app_id` フィールドに必須です。詳細については、[アプリ識別子]({{site.baseurl}}/api/identifier_types/)を参照してください。 |
| HTML メールコンテンツ | 事前に準備したメールメッセージの HTML 本文。 |
| バックエンドサービス | Braze REST API に HTTP POST リクエストを送信できるバックエンドサービスまたはスクリプティング環境。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## ステップ 1:API キャンペーンを作成する

1. Braze ダッシュボードで、**メッセージング** > **キャンペーン**に移動します。
2. **キャンペーンを作成**を選択し、**API キャンペーン**を選択します。
3. キャンペーンの名前と説明を入力します（例:「メールメッセージ通知」）。
4. 識別と追跡のために関連するタグを追加します。
5. **メッセージングチャネルを追加**を選択し、**メール**を選択します。
6. キャンペーンページに表示される**キャンペーン ID** をメモします。API リクエストを構築する際にこの値が必要です。オプションで、**メッセージバリエーション ID** もメモしてください。送信統計を特定のメッセージバリエーションに帰属させたい場合は、リクエストに含めます。

## ステップ 2:API を使用してメールを送信する

[`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) エンドポイントへの POST リクエストを構築します。リクエストペイロードにキャンペーン ID、受信者の外部ユーザー ID、およびメールコンテンツを含めます。

{% alert important %}
`external_user_ids` で参照される各受信者は、Braze にすでに存在している必要があります。API のみの送信では、新しいユーザープロファイルは作成されません。送信の一部としてユーザーを作成する必要がある場合は、まず [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) を使用するか、代わりに [API トリガーキャンペーン]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/)を使用してください。
{% endalert %}

### リクエスト例

```
POST https://YOUR_REST_ENDPOINT/messages/send
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

`YOUR_REST_ENDPOINT` をワークスペースの [REST エンドポイント URL]({{site.baseurl}}/api/basics/#endpoints) に置き換えてください。

{% raw %}
```json
{
  "campaign_id": "YOUR_CAMPAIGN_ID",
  "external_user_ids": ["user123"],
  "messages": {
    "email": {
      "app_id": "YOUR_APP_ID",
      "message_variation_id": "YOUR_MESSAGE_VARIATION_ID",
      "subject": "You have a new message!",
      "from": "Notifications <notifications@yourcompany.com>",
      "body": "<html><body><h1>You have a new message!</h1><p>Hi {{${first_name}}},</p><p>You received a new message in your inbox. Click the link below to read it:</p><a href='https://yourwebsite.com/messages'>View message</a><p>Thank you for using our service!</p></body></html>"
    }
  }
}
```
{% endraw %}

プレースホルダーの値を実際の ID に置き換えてください。`from` フィールドは `"Display Name <email@address.com>"` の形式を使用する必要があります。`body` フィールドは有効な HTML を受け付け、[Liquid パーソナライゼーション]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/)をサポートしているため、各受信者に合わせてメールコンテンツをカスタマイズできます。メールメッセージングオブジェクトでサポートされるパラメーターの完全なリストについては、[メールオブジェクト]({{site.baseurl}}/api/objects_filters/messaging/email_object/)を参照してください。

リクエストを構築したら、バックエンドサービスから Braze REST API に POST リクエストを送信します。

## ステップ 3:インテグレーションを検証する

設定が完了したら、インテグレーションを検証します。

1. [ステップ 2](#step-2-send-an-email-using-the-api) の説明に従って、自分のユーザー ID を受信者として API リクエストを送信します。
2. メールが受信トレイに配信されたことを確認します。
3. Braze ダッシュボードでキャンペーン結果ページに移動し、送信が記録されていることを確認します。
4. キャンペーンをスケールする際に、結果を注意深く監視します。

## 考慮事項

- GDPR や CAN-SPAM などの関連規制に準拠するために、必要なオプトアウトオプションとプライバシー通知を含めて、メールキャンペーンが準拠していることを確認してください。詳細については、[ユーザーサブスクリプションの管理]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/)および[メールのベストプラクティス]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/)を参照してください。
- Braze の[パーソナライゼーション機能]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/)を使用して、ダイナミックなコンテンツやユーザー固有のデータを含め、エンドユーザーごとにメールコンテンツをカスタマイズできます。
- Braze REST API は、メッセージのスケジュール設定、キャンペーンのトリガーなどのための追加の[メッセージングエンドポイント]({{site.baseurl}}/api/endpoints/messaging/)を提供しています。