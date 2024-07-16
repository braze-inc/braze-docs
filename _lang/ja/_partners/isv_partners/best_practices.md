---
nav_title: ベストプラクティス
hidden: true
---

# ユーザーライフサイクルと識別子のベストプラクティス

## データ収集

Brazeがデータを収集する方法について詳しく学びましょう:
- [SDK によるデータ収集]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/)
- [データ収集のベストプラクティス]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/best_practices/)
- [ユーザープロファイルのライフサイクル]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/)

## Braze 識別子

- `braze_id`:データベース内で作成された特定のユーザーに関連付けられた変更不可能なBraze割り当て識別子。
- `external_id`:顧客が割り当てた識別子、通常はUUID。ユーザーを一意に識別できる場合は、`external_id`を割り当てることをお勧めします。ユーザーが識別された後、匿名に戻すことはできません。
- `user_alias`:顧客がIDを使用してユーザーを参照する手段として割り当てることができる一意の代替識別子は、`external_id`が割り当てられる前に使用されます。ユーザーエイリアスは、後で他のエイリアスや`external_id`とマージすることができます。これは、Brazeの[ユーザー識別]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/)エンドポイントを通じて利用可能になったときに行われます。
    - [ユーザー識別]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/)エンドポイント内で、`merge_behavior`フィールドを使用して、ユーザーエイリアスプロファイルから既知のユーザープロファイルに保持するデータを指定できます。
    - ユーザーエイリアスが送信可能なプロファイルであるためには、プロファイルに標準属性としてメールおよび/または電話を含める必要があることに注意してください。
- `device_id`:自動生成されたデバイス固有の識別子。ユーザープロファイルには、それに関連付けられた`device_ids`の数が含まれる場合があります。例えば、職場のコンピュータ、自宅のコンピュータ、タブレット、iOSアプリでアカウントにログインしているユーザーは、プロフィールに4つの`device_ids`が関連付けられています。
- メールアドレスと電話番号：
    - Brazeのトラックユーザーエンドポイントで識別子としてサポートされています。 
    - リクエスト内で識別子としてメールアドレスまたは電話番号を使用する場合、考えられる結果は3つあります:
        1. このメールアドレスを持つユーザーの場合/phone does not exist within Braze, an email-only/phone-only user profile will be created, and any data in the request will be added to the profile.
        2. このメール/電話番号のプロファイルがBraze内に既に存在する場合、リクエスト内で送信されたデータを含むように更新されます。
        3. このメール/電話番号を持つ複数のプロファイルがある場合、最も最近更新されたプロファイルが優先されます。
    - メールのみの場合に注意してください/phone-only user profile exists and then an identified profile with the same email/phone is created (such as another profile with the same email address AND an external ID), Braze will create a second profile. Subsequent updates will go to the profile with the external ID.
        - 2つのプロファイルは、Braze [/merge/users]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) エンドポイントを使用してマージできます

## 匿名ユーザーの処理

特定の`external_id`にアクセスできない場合にBrazeでユーザープロファイルを作成または更新する必要があるユースケースでは、メールアドレスや電話番号などの別の識別子をBrazeの[識別子によるユーザーのエクスポート]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/)エンドポイントに渡して、Braze内にそのユーザーのプロファイルが存在するかどうかを確認できます。 

```json
{
 "email_address": "test@braze.com",
 "fields_to_export": ["braze_id", "user_aliases"]
}
```

そのメールアドレスまたは電話番号でBrazeにユーザーが存在する場合、そのプロフィールが返されます。それ以外の場合は、空の「ユーザー」配列が返されます。エクスポートエンドポイントを使用して、そのメールアドレスを持つユーザーが既に存在するかどうかを確認する利点は、匿名ユーザープロファイルがそのユーザーに関連付けられているかどうかを確認できることです。例えば、SDKを介して作成された匿名プロファイル（`braze_id`を持つ）または以前に作成されたユーザーエイリアスプロファイル。 

リクエストがユーザープロファイルを返さない場合、ユーザーエイリアスを作成するか、メールのみのユーザーを作成するかを選択できます。

### ユーザーエイリアス

ユーザートラックエンドポイントを使用して、選択した識別子をエイリアス名として使用してユーザーエイリアスを作成します。属性、イベント、または購入オブジェクト内に新しいユーザーエイリアスが定義されている場合、`_update_existing_only`を`false`として含めることで、エイリアスプロファイルを作成し、同時にそのプロファイルに属性、イベント、および購入を追加できます。 

ユーザーエイリアスを送信可能なプロファイルにするには、以下に示すように`email`フィールドにメールアドレスを含める必要があります。

```json
{
   "attributes": [
   {
     "user_alias" : {
       "alias_name" : "test@braze.com",
       "alias_label" : "email"
     },
     "email": "test@braze.com",
     "_update_existing_only": false,
     "string_attribute": "sherman",
     "boolean_attribute_1": true,
     "integer_attribute": 25,
     "array_attribute": ["banana", "apple"]
   }
   ]
}
```

このユーザーエイリアスは、後で`external_id`と識別してマージすることができます。利用可能になったときに、[ユーザーを識別する]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/)エンドポイントを通じて行うことができます。 

### メール専用ユーザーの作成

ユーザー トラック エンドポイントで識別子としてメール アドレスを使用します。 

```json
{
    "attributes": [
        {
            "email": "test@braze.com",
            "string_attribute": "fruit",
            "boolean_attribute_1": true,
            "integer_attribute": 25,
            "array_attribute": [
                "banana",
                "apple"
            ]
        }
    ]
}
```
{% alert important %}
この機能は現在早期アクセス中です。
{% endalert %}

## ユーザープロファイルにデータを同期中

[ユーザートラック]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)
- これは、Brazeでユーザーを作成および更新できる公開アクセス可能なエンドポイントであり、ユーザープロファイルに属性を記録することができます。このエンドポイントには、ワークスペースレベルで1分あたり50,000リクエストのレート制限が適用されています。
- このエンドポイントを使用する場合は、パートナーのドキュメントに示されているように`partner`キーを含めてください。

[クラウドデータ取り込み]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/cloud_ingestion/overview/#what-is-cloud-data-ingestion)
- ユーザートラックエンドポイントと同様に、データはクラウドデータインジェスチョンを通じてユーザープロファイルに同期できます。このツールを使用する際には、属性、イベント、および購入がプロファイルに記録されます。同期したいデータウェアハウステーブルまたはビューを設定して、目的のBrazeワークスペースに接続します。

[データポイント]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points#data-points)
- Brazeにはデータポイント消費モデルがあり、値が変更されているかどうかに関係なく、ユーザープロファイルへの「書き込み」ごとにデータポイントが発生します。このため、変更された属性のみをBrazeに送信することをお勧めします。 

## Brazeにユーザーのオーディエンスを送信する

[コホートインポート同期パートナードキュメント]({{site.baseurl}}/partners/isv_partners/cohort_import/)<br>
- ユーザーのオーディエンスは、BrazeのコホートインポートAPIエンドポイントを使用してコホートとしてBrazeに同期できます。これらのオーディエンスがユーザープロファイルにユーザー属性として保存されるのではなく、顧客はセグメンテーションツール内のパートナーブランドのフィルターを通じてこのコホートを構築し、ターゲットにすることができます。これにより、特定のユーザーセグメントを見つけてターゲットにすることが、顧客にとってより簡単でシンプルになります。
- コホートインポートエンドポイントは公開されておらず、各パートナーに固有のものです。このため、コホートエンドポイントへの同期は、顧客のワークスペースのレート制限にはカウントされません。 

[ユーザートラック]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)<br>
- これは、ユーザー属性を通じて特定のオーディエンス内のユーザーを示すことにより、Brazeでユーザーを即座に作成するために使用できる公開アクセス可能なエンドポイントです。このエンドポイントとコホートインポートエンドポイントの主な違いは、このエンドポイントを使用して送信されたオーディエンスがユーザープロファイルに保存されるのに対し、コホートインポートエンドポイントはセグメンテーションツールのフィラーとして表示されることです。このエンドポイントには、ワークスペースレベルで1分あたり50,000リクエストのレート制限が適用されています。
- このエンドポイントを使用する際は、`partner`キーを[パートナーのドキュメント]({{site.baseurl}}/partners/isv_partners/api_partner)に示されているように含めてください。

[データポイント]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points#data-points)<br>
- Brazeには、値が変更されたかどうかに関係なく、ユーザープロファイルへの「書き込み」ごとにデータポイントが発生するデータポイント消費モデルがあります。
- データポイントは、コホートインポートとユーザートラックエンドポイントの両方によって発生します。

## パートナーへのエンゲージメント分析のストリーミング

### Currents

カレントはBraze's near real-time message engagement analytics streaming tool. This will stream user-level data on all sends, deliveries, opens, clicks, etc., for campaigns and Canvases sent from the customer'のワークスペースです。いくつかの注意点:カレントは顧客ごとにコネクタごとに価格が設定されているため、新しいカレントパートナーはすべてEAプロセスを経る必要があります。私たちのパートナーには、カスタムブランドのUIを構築し、コネクタを公開する前に、EAの一環として5人の顧客を持つことを求めています。 
- [パートナーのドキュメント]({{site.baseurl}}/partners/isv_partners/currents_integration/)
- [メッセージエンゲージメントイベント]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events) \- カレンツコネクタを購入するすべての顧客がこれらのイベントにアクセスできます。
- [ユーザー行動イベント]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events) \- Currentコネクタを購入するすべての顧客が、これらのイベントを含む「すべてのイベント」コネクタを購入するわけではありません。 

### スノーフレークデータ共有

スノーフレークデータシェアコネクタを購入した顧客は、自動的にメッセージエンゲージメントとユーザー行動イベントの両方にアクセスできます。Snowflake Data Share がパートナー統合として使用される場合、Braze は顧客に代わってパートナーの Snowflake インスタンスに共有をプロビジョニングします。注として、クロスリージョンデータ共有はお客様にとって高価格帯であるため、Snowflakeと統合したいパートナーには、`US-EAST-1`および/または`EU-CENTRAL-1`にアカウントが必要であるというガイダンスを求めています。
- [パートナーのドキュメント]({{site.baseurl}}/partners/isv_partners/currents_integration/)

## キャンペーンとキャンバスの構築とトリガー

### Brazeでアセットを作成する
Brazeは、顧客とパートナーが顧客のワークスペース内でメールテンプレートとコンテンツブロックを作成/更新できるようにするいくつかのエンドポイントを提供します。これらのテンプレートとコンテンツブロックは、顧客のBrazeキャンペーンとキャンバス全体で使用できます。
- メールテンプレート
    - テンプレートエンドポイントを作成する
    - [テンプレートエンドポイントを更新]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template/#rate-limit)
- [コンテンツブロック]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks#content-blocks) 
    - [コンテンツブロックエンドポイント]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block/)
    - [コンテンツブロックエンドポイントを更新する]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block/)

### APIトリガーキャンペーンとキャンバス

顧客はキャンペーンとキャンバスをAPIトリガーに設定できます。これらのキャンペーンをトリガーするAPIリクエストは、APIトリガープロパティおよびオーディエンスまたは受信者パラメータを渡すことによって、キャンペーンをさらにパーソナライズおよびセグメント化するために使用できます。 
- [APIを介したキャンペーンのトリガー]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/#request-body)
    - キャンペーンは、個々のメールなどの単一のメッセージです。
- [APIを介してキャンバスをトリガーする]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/#request-body)
    - キャンバスは、マーケティング担当者が複数のメッセージとステップを使用して一貫したジャーニーを形成するキャンペーンを作成できる統一インターフェースです。キャンバスをトリガーすると、ユーザーはキャンバスのフローに入ります。そこで、キャンバスの基準に合わなくなるまでメッセージを受け取り続けます。 
- [API トリガー プロパティ/キャンバス エントリ プロパティ]({{site.baseurl}}/api/objects_filters/trigger_properties_object) 
    - 送信時にメッセージに動的に入力できるデータ。

### APIキャンペーン
APIキャンペーンを作成する場合（上記のAPIトリガーキャンペーンとは異なります）、Brazeダッシュボードはキャンペーンレポートの分析を追跡するための`campaign_id`を生成するためにのみ使用されます。キャンペーンメッセージ自体はAPIリクエスト内で定義されています。 
- [すぐにAPIキャンペーンを送信]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/)
- [APIキャンペーンをスケジュールする]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages/)

### IDを送信
Brazeのエンドポイントを使用して、送信ごとにキャンペーン分析を分解するために使用できる送信IDを生成します。例えば、各ロケーションごとに`campaign_id`（APIキャンペーン）が作成される場合、送信ごとに送信IDが生成され、特定のロケーションで異なるメッセージングがどのように機能しているかを追跡できます。 
- [IDを送信]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids/)

## コネクテッドコンテンツ

接続されたコンテンツは、送信時に指定されたエンドポイントにAPIリクエストを行い、応答で返された内容をメッセージに反映するために、任意のチャネルタイプ内で使用できます。

接続されたコンテンツ' versatility makes this a feature used by many of our customers to insert content that doesn'tまたはBrazeに住むことができません。私たちが目にするより一般的な使用例のいくつかは次のとおりです:
- メッセージにブログや記事のコンテンツをテンプレート化する
- コンテンツのおすすめ
- 製品メタデータ
- ローカリゼーションと翻訳

注意すべきこと：
- BrazeはAPIコールに対して料金を請求せず、データポイントの割り当てにもカウントされません。
- 接続されたコンテンツの応答には1 MBの制限があります。
- 接続されたコンテンツの呼び出しはメッセージが送信されたときに行われますが、アプリ内メッセージの場合はメッセージが表示されたときにこの呼び出しが行われます。
- 接続されたコンテンツの呼び出しはリダイレクトに従いません。Brazeはパフォーマンスの理由からサーバーの応答時間が2秒未満であることを要求します。サーバーが応答するのに2秒以上かかる場合、コンテンツは挿入されません。
- Brazeのシステムは、受信者ごとに同じConnected Content API呼び出しを複数回行う場合があります。それは、BrazeがメッセージペイロードをレンダリングするためにConnected Content APIコールを行う必要がある場合があるためです。また、メッセージペイロードは、検証、再試行ロジック、その他の内部目的のために、受信者ごとに複数回レンダリングされることがあります。 

これらの記事を参照して、接続されたコンテンツについて詳しく学んでください。
- [接続されたコンテンツの呼び出しを行う][1]
- [接続されたコンテンツを中止][2]
- [接続されたコンテンツの再試行][3]

[1]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/
[2]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content
[3]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/connected_content_retries
