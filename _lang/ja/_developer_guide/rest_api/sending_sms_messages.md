---
nav_title: SMSメッセージを送信する
article_title: REST APIを使用したSMSメッセージの送信
page_order: 2
page_type: reference
description: "この参考記事では、Braze REST APIとAPIキャンペーンを使ってSMSメッセージを送信する方法を説明する。"
channel:
  - SMS
---

# REST APIを使用したSMSメッセージの送信

> Braze REST APIを使って、バックエンドからトランザクションSMSメッセージをリアルタイムで送信する。この手法を使えば、プログラムでSMSメッセージを送信するサービスを構築できる。同時に、Brazeダッシュボード上で他のキャンペーンやキャンバスと並行して配信分析のトラッキングができる。

これは特に、バックエンドシステムで内容が定義されている大量のトランザクションメッセージングにおいて有用である。例えば、他のユーザーからメッセージが届いた際に消費者に通知し、自社Web サイトにアクセスして受信トレイを確認するよう促すことができる。

この方法を使えば、次のことができる：

- バックエンドからリアルタイムでSMSメッセージを送信する。
- マーケティング部門が所有する全てのキャンペーンとキャンバスと共に、分析データを追跡する。
- メッセージ遅延、フォローアップリターゲティング、AB テストといった追加のBraze機能でユースケースを拡張する。
- 必要に応じて、[APIトリガー]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/)配信に切り替えることで、メッセージテンプレートをBrazeダッシュボードで定義しつつ、送信はバックエンドからトリガーし続けることができる。

REST API経由でSMSメッセージを送信するには、BrazeダッシュボードでAPIキャンペーンを設定し、その後[`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/)エンドポイントを使用してメッセージを送信する必要がある。

## 前提条件

このガイドを完了するには、以下のものが必要だ：

| 必要条件 | 説明 |
| --- | --- |
| Braze REST API キー | 権限`messages.send`を持つ鍵。作成するには、**設定**＞**APIと識別子**＞**API キー**へ移動する。 |
| SMSサブスクリプショングループ | Brazeワークスペースで設定されたSMSサブスクリプショングループ。 |
| バックエンドサービス | Braze REST APIに対してHTTP POSTリクエストを送信できるバックエンドサービスまたはスクリプト環境。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## ステップ 1: APIキャンペーンを作成する

1. Brazeのダッシュボードで、**メッセージング**＞**キャンペーン**に移動する。
2. **キャンペーン作成**を選択し、次に**APIキャンペーン**を選択する。
3. キャンペーンの名前と説明を入力する。例えば「SMS通知」など。
4. 識別とトラッキングのために関連タグを追加する。
5. 「**メッセージングチャネルを追加」**を選択し、次に**「SMS」**を選択する。
6. キャンペーンページに表示されている**キャンペーンID**と**メッセージバリエーションID**をメモしておけ。APIリクエストを構築する際には、両方の値が必要だ。

## ステップ 2:APIを使ってSMSメッセージを送信する

エンド[`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/)ポイントへのPOSTリクエストを構築する。リクエストペイロードにキャンペーンID、受信者の外部ユーザー ID、およびSMSコンテンツを含める。

{% alert important %}
参照されている各受信者は、`external_user_ids`既にBrazeに存在していなければならない。API経由のみの送信では、新しいユーザープロファイルは作成されない。送信の一部としてユーザーを作成する必要がある場合は、まず[この方法[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)]を使用するか、代わりに[APIトリガー型キャンペーン]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/)を使用する。
{% endalert %}

### リクエスト例

```
POST YOUR_REST_ENDPOINT/messages/send
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

を、ワークスペースの[RESTエンドポイント]({{site.baseurl}}/api/basics/#endpoints)URL`YOUR_REST_ENDPOINT`に置き換える。

{% raw %}
```json
{
  "campaign_id": "YOUR_CAMPAIGN_ID",
  "external_user_ids": ["user123"],
  "messages": {
    "sms": {
      "app_id": "YOUR_APP_ID",
      "subscription_group_id": "YOUR_SMS_SUBSCRIPTION_GROUP_ID",
      "message_variation_id": "YOUR_MESSAGE_VARIATION_ID",
      "body": "Hi {{${first_name}}}, you have a new message in your inbox. Check it out at https://yourwebsite.com/messages. Text STOP to opt out."
    }
  }
}
```
{% endraw %}

プレースホルダーの値を実際のIDに置き換える。この`body`フィールドは[Liquidパーソナライゼーション]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/)をサポートしているため、メッセージの内容を各受信者に合わせて調整できる。SMSメッセージングオブジェクトがサポートするパラメータの完全な一覧については、[SMSオブジェクトを]({{site.baseurl}}/api/objects_filters/messaging/sms_object/)参照せよ。

リクエストを構築した後、バックエンドサービスからBraze REST APIへPOSTリクエストを送信する。

## ステップ 3:統合を確認せよ

設定を完了したら、統合を確認する：

1. [ステップ2](#step-2-send-an-sms-message-using-the-api)で説明した通り、APIリクエストを送信する。その際、受信者として自身のユーザー ID を使用する。
2. SMSメッセージが自分の携帯電話に届いていることを確認する。
3. Brazeのダッシュボードで、キャンペーン結果ページに移動し、送信が記録されていることを確認する。
4. キャンペーンを拡大するにつれて、結果を注意深く監視せよ。

## 考慮事項

- SMSキャンペーンが関連規制および通信事業者の要件に準拠していることを確認せよ。すべてのメッセージにオプトアウトの手順（「STOPと送信してオプトアウト」など）を含めること。詳細については、[SMSに関する法令およびオプトイン]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/laws_and_regulations/)[・オプトアウトキーワードを]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/optin_optout/)参照のこと。
- Brazeの[パーソナライゼーション機能]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/)を使って、SMSコンテンツをエンドユーザーに合わせてパーソナライズする。これにはダイナミックなコンテンツやユーザー固有のデータが含まれる。
- Braze REST APIは、メッセージのスケジュール設定やキャンペーンのトリガーなどを行うための追加の[メッセージングエンドポイント]({{site.baseurl}}/api/endpoints/messaging/)を提供する。
