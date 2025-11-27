---
nav_title: APIの使用例
article_title: APIの使用例
description: "このリファレンス記事は、あなたが熟練した開発者であろうと、最小限の開発者リソースしか持たないマーケターであろうと、Braze REST API のパワーを活用してさまざまなタスクを達成し、カスタマーエンゲージメント戦略を強化する方法を理解するのに役立つように設計されています。"
page_type: reference
page_order: 4.8
---

# APIの使用例

> [Braze REST API]({{site.baseurl}}/api/basics/) は、カスタマーエンゲージメント戦略の管理と最適化を支援するために設計された幅広いエンドポイントを提供します。この記事では、カタログ、Eメールリストとアドレス、エクスポート、メッセージ、プリファレンスセンター、SMS、購読グループ、テンプレート、ユーザーデータなど、各エンドポイントコレクションの使用例をいくつか紹介します。<br><br>各セクションでは、ステップバイステップのガイド、コードサンプル、期待される結果とともにシナリオを紹介しています。この記事を読み終わる頃には、顧客エンゲージメント活動を強化するためのBraze REST APIの使い方をより深く理解できるようになります。

## カタログの複数の項目を削除する

キッチン用品を専門とする小売ブランド、キッチネリー (Kitchenerie) は新年を迎え、新商品を発表しました。Brazeのダッシュボードでは、Kitchenerieの食器コレクションに「Dishware」というカタログが設定されています。また、今年は以下の製品を食器のコレクションから外すことになります。

* プレーンビスク
* パール磁器
* ピンクシマー

これらの商品をカタログから削除するには、Kitchener は [`/catalogs/{catalog_name}/items` エンドポイント]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk/)を使って商品 ID を渡すことができます。

これがリクエストの例です：

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

この有料読み込むを送った後、レスポンスは、Brazeがキチネリーの食器カタログから3つのコレクションをうまく削除したことを確認します。

```json
{
  "message": "success"
}
```

## Brazeのスパムリストからメールを削除する

ストリーミング・サービスを提供するMovieCanon社では、開発者チームが定期的に電子メール・リストを監査し、電子メール・キャンペーンに登録しているユーザーを特定し、維持する役割を担っています。この監査の一環として、MovieCanon はこのメールのリストをスパムリストから削除したいと考えています：

- august.author.example.com
- betty.benson@example.com
- charlie.chase@example.com
- delilah.york@example.com
- evergreen.rebecca@example.com

このタスクを達成するために、開発者チームは `/email/spam/remove` エンドポイントを使用するための `email.spam.remove` 権限を持つ API キーが必要となります。このエンドポイントは、BrazeのスパムリストとMovieCanonのメールプロバイダーが管理するスパムリストからメールアドレスを削除します。

このリクエストを送るには、文字列のEメールアドレスか、修正するEメールアドレスを50個まで並べた配列のどちらかを含めます。削除する電子メールのリストが50以下なので、MovieCanonは以下のリクエスト・ボディでこのタスクを達成できます：

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "email": ["august.author.example.com","betty.benson@example.com","charlie.chase@example.com","delilah.york@example.com","evergreen.rebecca@example.com"]
}
```

この有料読み込むを正常に送信した後、このレスポンスは、Brazeがムービーキャノンのスパム一覧からメールを削除したことを確認します。

```json
{
  "message": "success"
}
```

## すべてのキャンバスを監査します

Siege Valley Health は、数千人の患者を抱える10の稼働中の病院と研究センターからなる病院組織です。同社のマーケティングチームはインフルエンザ予防接種の予約を促すために過去3年間に Braze を使用して患者に送信したキャンバスを比較したいと考えています。Siege Valley Health のマーケティングチームも、キャンバスのリストと分析のサマリーの両方を素早く効率的に確認する方法を必要としています。

Siege Valley Healthが、Brazeのダッシュボードでフィルタリングするのではなく、エンドポイントの組み合わせを使って、この2つのタスクをどのように達成できるかを見てみましょう。

キャンバスを監査する最初のタスクとして、[`/canvas/list` エンドポイント]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases/)を使い、名前とタグを含むキャンバスのリストをエクスポートします。リクエストの例を挙げます：

{% details Here’s the response that the Siege Valley Health marketing team would receive. %}
```json
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

Siege Valley Health のキャンバスリストから最初のキャンバスの分析サマリーを確認するという次のタスクに移りましょう。そのためには、以下のリクエストパラメーターで [`/canvas/data_summary` エンドポイント]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary/)を使用します。

* `canvas_id`
* `ending_at`:2023-07-10T23:59:59
* `starting_at`:2020-07-10T23:59:59

リクエストの例を挙げます：

```
curl --location -g --request GET 'https://rest.iad-01.braze.com/canvas/data_summary?canvas_id={{canvas_identifier_2}}&ending_at=2023-07-10T23:59:59&starting_at=2020-07-10T23:59:59&length=5&include_variant_breakdown=false&include_step_breakdown=false&include_deleted_step_data=false' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## 今後スケジュールされているキャンペーンとキャンバスをチェックする

オンラインと店舗で衣料品と美容製品を販売する小売ブランド、Flash & Thread にとって、一年で最も忙しい時期が間近に迫っています。同社のマーケティングチームは、2024年3月31日午後12時までに、Braze のダッシュボードから今後のキャンペーンとキャンバスをチェックしたいと考えています。これは、[`/messages/scheduled_broadcasts` エンドポイント]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/get_messages_scheduled/)を使って実現できます。

これがリクエストの例です：

```
curl --location --request GET 'https://rest.iad-01.braze.com/messages/scheduled_broadcasts?end_time=2024-03-31T12:00:00' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

このエンドポイントは、今後のキャンペーンとキャンバスのリストを返します。ここから、マーケティングチームは、レスポンス内のキャンペーンとキャンバスの`name` フィールドを参照することで、メッセージのリストを確認することができます。

## 古いユーザー設定センターを表示します

PoliterWeekly はデジタル雑誌で、購読者にはメールで連絡を取ることができます。購読者のユーザージャーニーをよりよく理解するために、マーケティングチームはPoliterWeeklyのプリファレンスセンターの詳細を確認し、それがいつ作成され、最後に更新されたかを確認しましょう。

マーケティングチームは、[`/preference_center/v1/{preferenceCenterExternalID}` エンドポイント]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center/)を使用して、次のようにパスパラメーターとしてユーザー設定センターの外部 ID を挿入するだけで済みます。

```
curl --location -g --request GET https://rest.iad-01.braze.com/preference_center/v1/politer_weekly_preference_center_api_id \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

{% details Here’s the response the PoliterWeekly marketing team would receive. %}

```json
{
  "name": "PoliterWeekly Notification Preferences",
  "preference_center_api_id": "user_engage_pref_123",
  "created_at": "2021-04-03T12:00:00",
  "updated_at": "2024-08-15T15:00:00",
  "preference_center_title": "Manage Your PoliterWeekly Notification Preferences",
  "preference_center_page_html": "<!DOCTYPE html><html><head><title>Your PoliterWeekly Newsletter Preferences</title><style>body { font-family: Arial, sans-serif; margin: 0; padding: 20px; }.container { max-width: 600px; margin: auto; }h1 { color: #333; }.preference { margin-bottom: 20px; }.preference label { font-size: 16px; }.preference input[type=\"checkbox\"] { margin-right: 10px; }.submit-btn { background-color: #007bff; color: white; padding: 10px 20px; border: none; cursor: pointer; }</style></head><body><div class=\"container\"><h1>Manage your notification preferences</h1><p>Select the types of updates you wish to receive from us:</p><form id=\"preferencesForm\"><div class=\"preference\"><label><input type=\"checkbox\" name=\"newsUpdates\" checked> News Updates</label></div><div class=\"preference\"><label><input type=\"checkbox\" name=\"editorialPicks\"> Editorial Picks</label></div><div class=\"preference\"><label><input type=\"checkbox\" name=\"events\"> Events & Webinars</label></div><div class=\"preference\"><label><input type=\"checkbox\" name=\"specialOffers\"> Special Offers & Promotions</label></div><button type=\"submit\" class=\"submit-btn\">Save Preferences</button></form></div><script>document.getElementById('preferencesForm').addEventListener('submit', function(e) {e.preventDefault();alert('Your preferences have been saved!');});</script></body></html>",
  "confirmation_page_html": "<!DOCTYPE html><html><head><title>PoliterWeekly Preferences Updated</title></head><body><h1>You're good to go!</h1><p>Braze updated your preferences successfully.</p></body></html>",
  "redirect_page_html": null,
  "preference_center_options": {
    "meta-viewport-content": "width=device-width, initial-scale=1"
  },
  "state": "active"
}
```

この応答から、マーケティングチームは、ユーザー設定センターが最新のアップデートの3年前に作成されたことがわかります。この情報を念頭に置いて、マーケティングチームは新しいユーザー設定センターを作成し、立ち上げることができました。

{% enddetails %}

## 無効な電話番号を削除する

CashBlastr の主な目標は、迅速な送金と受取りの方法を簡素化することです。金融サービス会社である、CashBlastr は顧客の電話番号リストを最新で正確な状態に保ちたいと考えています。開発者チームは、マーケティングチームの SMS メッセージが CashBlastr 社の適切な顧客に届くように、「無効」とマークされた以下の電話番号リストを削除するよう指示されています。

- 12223135467
- 12183095514
- 14235662245
- 14324567892

[`/sms/invalid_phone_numbers/remove` エンドポイント]({{site.baseurl}}/api/endpoints/sms/post_remove_invalid_numbers/)でリクエストを送信するには、電話番号は [e.164 形式](https://en.wikipedia.org/wiki/E.164)の文字列の配列にする必要があり、リクエストごとに最大50個の電話番号を指定できます。リストは50電話番号を超えないので、ここにCashBlastrの開発チームが送るリクエストボディの例を示します：

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "phone_numbers": ["12183095514","14255551212"]
}
```

この有料読み込むを送信した後、レスポンスは、BrazeがBraze不正リストからCashBlastrから不正な電話番号を削除したことを確認します。

```json
{
  "message": "success"
}
```

## ユーザーのサブスクリプショングループのステータスを表示する

SandwichEmperorは米国のクイックサービス・レストラン・チェーンであり、そのマーケティング・チームは、SMSのために無作為化されたユーザー・リストの購読グループ・ステータスをチェックしたいと考えています。SandwichEmperor は、[`/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/) エンドポイントを使用して、以下のリクエストの例で個々のユーザーに対してこのタスクを実行できます。

{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/subscription/status/get?subscription_group_id={{subscription_group_id}}&phone=+11232223333' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

このエンドポイントでは、メールのユーザーのサブスクリプショングループ ステータスも一覧表示します。マルチユーザーs のサブスクリプショングループ ステータスを表示するには、このボタンを使用します。

## メールメッセージ用のHTMLテンプレートをチェックする

異なる業界の労働者間のつながりを構築するのに役立つソーシャルネットワークである WorkFriends では、マーケティングチームがユーザーにメールキャンペーンを送信する役割を担っています。これらのキャンペーンには、地域イベントのリマインダー、毎週のニュースレター、プロフィール活動のハイライトなどが含まれることがよくあります。

このシナリオでは、WorkFriends はこれまで、レガシーブランディングで単一の HTML テンプレートを使用してきました。WorkFriends は、ブランドアイデンティティの統一を図るため、新しいテンプレートに移行する前に、この HTML テンプレートに活用できる有用な情報があるかどうかを確認したいと考えています。

{% details Here’s the response that the WorkFriends team would receive. %}

```json
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

このテンプレート情報を確認した後、WorkFriends は [`/templates/email/update` エンドポイント]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template/)を使用して、API を通じてメールテンプレートを更新することもできます。BrazeダッシュボードのEメールテンプレートには、これらの編集が反映されます。
