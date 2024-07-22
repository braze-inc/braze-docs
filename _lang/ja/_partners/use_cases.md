---
nav_title: API ユースケース
article_title: API ユースケース
description: "この参考記事は、熟練した開発者でも、最小限の開発者リソースしか持たないマーケティング担当者でも、Braze REST API の力を活用してさまざまなタスクを実行し、顧客エンゲージメント戦略を強化する方法を理解するのに役立つように設計されています。"
page_type: reference
page_order: 4.8
---

# API ユースケース

> [Braze REST APIは]({{site.baseurl}}/api/basics/)、顧客エンゲージメント戦略の管理と最適化に役立つように設計された幅広いエンドポイントを提供します。この記事では、カタログ、メールリストとアドレス、エクスポート、メッセージ、プリファレンスセンター、SMS、サブスクリプショングループ、テンプレート、ユーザーデータなど、各エンドポイントコレクションのいくつかのユースケースについて説明します。<br><br>各セクションでは、ステップバイステップガイド、コードサンプル、および期待される結果を含むシナリオを紹介します。この記事を読み終える頃には、Braze REST API を使用してカスタマーエンゲージメントを強化する方法をよりよく理解できるようになります。

## カタログ内の複数のアイテムを削除する

キッチン用品専門小売ブランド「キッチナリー」では、新年を迎えます。Brazeダッシュボードでは、キッチネリーの食器コレクションの「Dishware」という名前のカタログが設定されています。この新年は、食器コレクションから以下の製品を削除することも意味します。

* プレーン・ビスク
* パールポーセリン
* ピンクシマー

これらの製品をカタログから削除するために、Kitchener [`/catalogs/{catalog_name}/items`はエンドポイントを使用してアイテム]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk/) ID を渡すことができます。

リクエストの例は次のとおりです。

```
curl --location --request DELETE 'https://rest.iad-03.braze.com/catalogs/dishware/items' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "items": [
    {"id": "plainbisque"},
    {"id": "pearlporcelain"},
    {"id": "pinkshimmer"}
  ]
}'
```

このペイロードを送信すると、次の応答により、3 つのコレクションが Kitchenerie の食器カタログから正常に削除されたことが確認されます。

```json
{
  "message": "success"
}
```

## Braze 迷惑メールリストからメールを削除する

ストリーミングサービス会社のMovieCanonでは、開発チームが定期的にメーリングリストを監査して、メールキャンペーンに登録しているユーザーを特定して維持する責任があります。この監査の一環として、MovieCanonは次のメールリストをスパムリストから削除したいと考えています。

- august.author.example.com
- betty.benson@example.com
- charlie.chase@example.com
- delilah.york@example.com
- evergreen.rebecca@example.com

このタスクを実行するには、`email.spam.remove``/email/spam/remove`開発チームはエンドポイントを使用する権限のある API キーを必要とします。このエンドポイントは、BrazeスパムリストとMovieCanonのメールプロバイダーが管理するスパムリストからメールアドレスを削除します。

このリクエストを送信するには、文字列形式のメールアドレスか、変更するメールアドレスの配列を最大 50 個まで含めてください。削除するメールのリストが50件未満であるため、MovieCanonは次のリクエストボディを使用してこのタスクを実行できます。

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "email": ["august.author.example.com","betty.benson@example.com","charlie.chase@example.com","delilah.york@example.com","evergreen.rebecca@example.com"]
}
```

このペイロードが正常に送信されると、この応答により、メールがMovieCanonのスパムリストから削除されたことが確認されます。

```json
{
  "message": "success"
}
```

## すべてのキャンバスを監査する

Siege Valley Healthは、数千人の患者を抱える10の手術病院と研究センターを含む病院システムです。マーケティングチームは、患者に送られたキャンバスを比較して、過去3年間Brazeを使用したときのインフルエンザの予防接種の予約をするように促したいと考えています。Siege Valley Healthのマーケティングチームも、キャンバスのリストと分析概要の両方をすばやく効率的に確認する方法を求めています。

Siege Valley Healthが、Brazeダッシュボードでフィルタリングするのではなく、エンドポイントを組み合わせてこれら2つのタスクを実行する方法について詳しく見ていきましょう。

Canvasesを監査する最初のタスクでは、[`/canvas/list`エンドポイントを使用して名前とタグを含むCanvasesのリストをエクスポートします]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases/)。リクエストの例は次のとおりです。

{% details シージバレーヘルスのマーケティングチームが受け取る回答は次のとおりです。 %}
```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "canvases" : [
  	{
  		"id": "canvas_identifier_1",
  		"last_edited": "2020-07-10T23:59:59",
  		"name": "PatientReminder_FluShot_2020",
  		"tags": {
        "flu_shots", "patienthealth", "2020"
      },
  	},
  	{
  		"id": "canvas_identifier_2",
  		"last_edited": "2020-07-30T23:59:59",
  		"name": "PatientReminder2_FluShot_2020",
  		"tags": {
        "flu_shots", "patienthealth", "reminder", "2020"
      },
  	},
    ... (more Canvases)
  ],
  "message": 'success'
}
```
{% enddetails %}

次のタスクに移りましょう。Siege Valley Healthのキャンバスリストにある最初のキャンバスの分析概要を確認しましょう。そのためには、[`/canvas/data_summary`以下のリクエストパラメータを持つエンドポイントを使用します]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary/)。

* `canvas_id`: "canvas_identifier_2"
* `ending_at`:2023-07-10T 23:59:59
* `starting_at`:2020-07-10T 23:59:59

リクエストの例は次のとおりです。

```
curl --location -g --request GET 'https://rest.iad-01.braze.com/canvas/data_summary?canvas_id={{canvas_identifier_2}}&ending_at=2023-07-10T23:59:59&starting_at=2020-07-10T23:59:59&length=5&include_variant_breakdown=false&include_step_breakdown=false&include_deleted_step_data=false' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## 今後予定されているキャンペーンとキャンバスを確認する

衣料品や美容製品をオンラインや店舗で販売する小売ブランド、フラッシュ＆スレッドにとって、一年で最も忙しい時期が間近に迫っています。マーケティングチームは、2024年3月31日午後12時までに、Brazeダッシュボードから今後のキャンペーンとキャンバスを確認したいと考えています。[`/messages/scheduled_broadcasts`これはエンドポイントを使用して実行できます]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/get_messages_scheduled/)。 

リクエストの例は次のとおりです。

```
curl --location --request GET 'https://rest.iad-01.braze.com/messages/scheduled_broadcasts?end_time=2024-03-31T12:00:00' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

このエンドポイントは、今後のキャンペーンとキャンバスのリストを返します。ここから、`name`マーケティングチームは応答内のキャンペーンとキャンバスのフィールドを参照してメッセージのリストを確認できます。

## 古いプリファレンスセンターを表示する

PoliterWeeklyは、購読者に電子メールで連絡できるデジタルマガジンです。購読者のユーザージャーニーをより深く理解するために、マーケティングチームは PoliterWeekly のプリファレンスセンターの詳細を確認して、作成日と最終更新日を確認したいと考えています。

[`/preference_center/v1/{preferenceCenterExternalID}`エンドポイントを使用すると]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center/)、マーケティングチームは次のようなプリファレンスセンターの外部IDをパスパラメータとして挿入するだけで済みます。

```
curl --location -g --request GET https://rest.iad-01.braze.com/preference_center/v1/politer_weekly_preference_center_api_id \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

{% details PoliterWeeklyのマーケティングチームが受け取る回答は次のとおりです。 %}

```json
{
  "name": "PoliterWeekly Notification Preferences",
  "preference_center_api_id": "user_engage_pref_123",
  "created_at": "2021-04-03T12:00:00",
  "updated_at": "2024-08-15T15:00:00",
  "preference_center_title": "Manage Your PoliterWeekly Notification Preferences",
  "preference_center_page_html": "<!DOCTYPE html><html><head><title>Your PoliterWeekly Newsletter Preferences</title><style>body { font-family: Arial, sans-serif; margin: 0; padding: 20px; }.container { max-width: 600px; margin: auto; }h1 { color: #333; }.preference { margin-bottom: 20px; }.preference label { font-size: 16px; }.preference input[type=\"checkbox\"] { margin-right: 10px; }.submit-btn { background-color: #007bff; color: white; padding: 10px 20px; border: none; cursor: pointer; }</style></head><body><div class=\"container\"><h1>Manage your notification preferences</h1><p>Select the types of updates you wish to receive from us:</p><form id=\"preferencesForm\"><div class=\"preference\"><label><input type=\"checkbox\" name=\"newsUpdates\" checked> News Updates</label></div><div class=\"preference\"><label><input type=\"checkbox\" name=\"editorialPicks\"> Editorial Picks</label></div><div class=\"preference\"><label><input type=\"checkbox\" name=\"events\"> Events & Webinars</label></div><div class=\"preference\"><label><input type=\"checkbox\" name=\"specialOffers\"> Special Offers & Promotions</label></div><button type=\"submit\" class=\"submit-btn\">Save Preferences</button></form></div><script>document.getElementById('preferencesForm').addEventListener('submit', function(e) {e.preventDefault();alert('Your preferences have been saved!');});</script></body></html>",
  "confirmation_page_html": "<!DOCTYPE html><html><head><title>PoliterWeekly Preferences Updated</title></head><body><h1>You're good to go!</h1><p>Your preferences have been updated successfully.</p></body></html>",
  "redirect_page_html": null,
  "preference_center_options": {
    "meta-viewport-content": "width=device-width, initial-scale=1"
  },
  "state": "active"
}
```

この回答から、マーケティングチームは、プリファレンスセンターが最新の更新の 3 年前に作成されたことを確認できます。この情報を念頭に置いて、マーケティングチームは新しいプリファレンスセンターを作成して立ち上げることができます。

{% enddetails %}

## 無効な電話番号を削除する

CashBlastrの主な目標は、人々が迅速な支払いを送受信する方法を合理化することです。金融サービス企業であるCashBlastrは、顧客の電話番号のリストを最新かつ正確に保ちたいと考えています。開発チームには、マーケティングチームのSMSメッセージが適切なCashBlastrの顧客に届くように、「無効」とマークされた以下の電話番号のリストを削除する任務があります。

- 12223135467
- 12183095514
- 14235662245
- 14324567892

[`/sms/invalid_phone_numbers/remove`エンドポイントでリクエストを送信するには]({{site.baseurl}}/api/endpoints/sms/post_remove_invalid_numbers/)、[e.164電話番号を文字列の配列形式で指定する必要があります](https://en.wikipedia.org/wiki/E.164)。リクエストごとに最大 50 個の電話番号を入力できます。リストには電話番号が 50 個を超えないため、CashBlastrの開発チームが送信するリクエスト本文の例を次に示します。

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "phone_numbers": ["12183095514","14255551212"]
}
```

このペイロードを送信した後、次の応答により、CashBlastrの無効な電話番号がBraze無効リストから削除されたことが確認されます。

```json
{
  "message": "success"
}
```

## ユーザーのサブスクリプショングループの状態を表示する

SandwicEmperorは米国のクイックサービスレストランチェーンです。同社のマーケティングチームは、サブスクリプショングループのステータスを確認して、SMS用のランダムなユーザーリストを確認したいと考えています。[`/subscription/status/get`エンドポイントを使用すると]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/)、SandwicEmperor は次のリクエスト例を使用して個々のユーザーに対してこのタスクを実行できます。

{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/subscription/status/get?subscription_group_id={{subscription_group_id}}&phone=+11232223333' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

このエンドポイントには、電子メール用のユーザーのサブスクリプショングループのステータスも一覧表示され、複数のユーザーのサブスクリプショングループのステータスを確認するために使用できます。

## メールメッセージ用の HTML テンプレートの確認

さまざまな業界の従業員同士のつながりを築くのに役立つソーシャルネットワークであるWorkFriendsでは、マーケティングチームがユーザーにメールキャンペーンを送信する責任があります。これらのキャンペーンには、多くの場合、ローカルイベントのリマインダー、週刊ニュースレター、プロフィールアクティビティのハイライトが含まれます。

このシナリオでは、WorkFriends はこれまで、従来のブランディングのある 1 つの HTML テンプレートを使用してきました。WorkFriends では、ブランドアイデンティティの統一を図るために、新しいテンプレートに移行する前に、この HTML テンプレートに活用できる有用な情報があるかどうかを確認したいと考えています。

{% details WorkFriends チームが受け取る回答は次のとおりです。 %}

```json
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
{
  "email_template_id": "WorkFriends_Email_Template_ID",
  "template_name": "Promo template",
  "description": "Promo template",
  "subject": "WorkFriends Weekly Newsletter",
  "preheader": "Another week, another WorkFriends update",
  "body": "<!DOCTYPE html><html><head><title>WorkFriends Weekly Newsletter</title><style>body {font-family: Arial, sans-serif; color: #333;}.container {padding: 20px;}.header {background-color: #f2f2f2; padding: 10px; text-align: center;}.content {margin-top: 20px;}.footer {margin-top: 20px; font-size: 12px; text-align: center; color: #777;}</style></head><body><div class=\"container\"><div class=\"header\"><h2>WorkFriends Weekly Newsletter</h2></div><div class=\"content\"><p>Hello WorkFriends,</p><p>Welcome to another edition of our weekly newsletter. We've got some exciting updates and promos for you this week!</p><!-- Add more content here --><p>Don't forget to check out our latest promos and updates. Stay connected, stay informed!</p></div><div class=\"footer\"><p>Thank you for being a part of WorkFriends.</p><p>Unsubscribe | Update Preferences</p></div></div></body></html>",
  "tags": "promo",
  "created_at": "2020-07-10 13:00:00.000",
  "updated_at": "2024-02-04 17:00:00.000"
}
```

{% enddetails %}

このテンプレート情報を確認したら、WorkFriends [`/templates/email/update`はエンドポイントを使用して]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template/) API を介してメールテンプレートを更新することもできます。Braze ダッシュボードのメールテンプレートには、これらの編集内容が反映されます。
