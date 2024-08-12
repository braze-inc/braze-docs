---
nav_title: ベストプラクティス
hidden: true
---

# ユーザーライフサイクルと識別子のベストプラクティス

## データ収集

Braze がデータを収集する方法の詳細については、以下をご覧ください。
-[SDK データ収集]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/)
-[データ収集のベストプラクティス]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/best_practices/)
-[ユーザープロファイルのライフサイクル]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/)

## Braze識別子

- `braze_id`:BRAZE で割り当てられた識別子。データベース内で作成すると変更できず、特定のユーザーに関連付けられます。
- `external_id`:顧客によって割り当てられた識別子 (通常は UUID)。`external_id`ユーザーを一意に識別できる場合は、を割り当てることをお勧めします。いったんユーザーを特定すると、そのユーザーを匿名に戻すことはできません。
- `user_alias`:ID `external_id` が割り当てられる前に ID でユーザーを参照する手段としてユーザーが割り当てることができる一意の代替識別子。ユーザーエイリアスは、後で他のエイリアスとマージすることも、`external_id` [Brazeのユーザー識別エンドポイントから利用可能になったときにマージすることもできます]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/)。
    - [ユーザー識別エンドポイント内では]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/)、`merge_behavior`このフィールドを使用して、ユーザーエイリアスプロファイルのどのデータを既知のユーザープロファイルに保持するかを指定できます。
    - ユーザーエイリアスを送信可能なプロファイルにするには、プロファイルの標準属性として電子メールや電話を含める必要があることに注意してください。
- `device_id`:自動的に生成されるデバイス固有の識別子。ユーザープロファイルには、`device_ids`複数のユーザープロファイルを関連付けることができます。たとえば、職場のコンピューター、自宅のコンピューター、タブレット、iOSアプリでアカウントにログインしたユーザーのプロファイルには、`device_ids` 4つが関連付けられます。
- Eメールアドレスと電話番号:
    - Braze の追跡ユーザーエンドポイントの識別子としてサポートされています。 
    - 電子メールアドレスまたは電話番号をリクエスト内の ID として使用すると、次の 3 つの結果が生じる可能性があります。
        1. このメールを持っているユーザーの場合/phone does not exist within Braze, an email-only/phone-only user profile will be created, and any data in the request will be added to the profile.
        2. このメールアドレス/電話番号のプロフィールが既に Braze 内に存在する場合、リクエスト内で送信されたデータを含むように更新されます。
        3. このメール/電話で複数のプロファイルを使用するユースケースでは、最後に更新されたプロファイルが優先されます。
    - メールのみの場合は、ご注意ください/phone-only user profile exists and then an identified profile with the same email/phone is created (such as another profile with the same email address AND an external ID), Braze will create a second profile. Subsequent updates will go to the profile with the external ID.
        - 2 つのプロファイルは、Braze [/merge/users]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/)エンドポイントを使用してマージできます。

## 匿名ユーザーの処理

にアクセスせずに Braze でユーザープロファイルを作成または更新する必要があるユースケースでは`external_id`、[メールアドレスや電話番号などの別の識別子を識別子エンドポイントによって Braze Export ユーザーに渡して、そのユーザーのプロファイルが]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) Braze 内に存在するかどうかを判断できます。 

```json
{
 "email_address": "test@braze.com",
 "fields_to_export": ["braze_id", "user_aliases"]
}
```

Braze 内にそのメールアドレスまたは電話番号を持つユーザーが存在する場合、そのユーザーのプロフィールが返されます。それ以外の場合は、空の「users」配列が返されます。エクスポートエンドポイントを使用して、その電子メールアドレスを持つユーザーがすでに存在するかどうかを判断する利点は、これにより、そのユーザーに関連付けられている匿名のユーザープロファイルが存在するかどうかを判断できることです。たとえば、SDK で作成された匿名プロファイル (あるはずです`braze_id`) や、以前に作成したユーザーエイリアスプロファイルなどです。 

リクエストでユーザープロファイルが返されない場合は、ユーザーエイリアスを作成するか、メールのみのユーザーを作成するかを選択できます。

### ユーザーエイリアス

ユーザートラックエンドポイントを使用して、選択した識別子をエイリアス名として使用してユーザーエイリアスを作成します。新しいユーザーエイリアスが定義されている属性、イベント、または購入オブジェクトに `_update_existing_only` as `false` を含めることで、エイリアスプロファイルを作成し、そのプロファイルに属性、イベント、購入を同時に追加できます。 

ユーザーエイリアスを送信可能なプロファイルにするには、以下に示すように、`email`フィールドにメールアドレスを含める必要があります。

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

後でこのユーザーエイリアスを識別して、Identify [users `external_id`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) エンドポイントから利用可能になったら、とを統合できます。 

### メール専用ユーザーの作成

電子メールアドレスをユーザートラックエンドポイントの識別子として使用します。 

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
{% alert note %}
この機能は現在先行アクセス中です。
{% endalert %}

## ユーザープロファイルへのデータの同期

[ユーザートラック]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)
-これは一般にアクセス可能なエンドポイントで、Brazeでユーザーを作成および更新できます（ユーザープロファイルへの属性のロギングなど）。このエンドポイントには、ワークスペースレベルで適用される1分あたり50,000リクエストのレート制限があります。
-このエンドポイントを使用するときは、`partner`パートナーのドキュメントに示されているキーを含めてください。

[クラウドデータ取り込み]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/cloud_ingestion/overview/#what-is-cloud-data-ingestion)
-ユーザートラッキングエンドポイントと同様に、データはクラウドデータインジェストを通じてユーザープロファイルに同期できます。このツールを使用すると、必要なBrazeワークスペースに同期したいデータウェアハウステーブルまたはビューを設定して接続することで、属性、イベント、購入がプロファイルに記録されます。

[データポイント]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points#data-points)
-Brazeにはデータポイント消費モデルがあり、値が変更されたかどうかに関係なく、ユーザープロファイルへの「書き込み」ごとにデータポイントが発生します。このため、変更された属性のみを Braze に送信することをおすすめします。 

## ユーザーのオーディエンスを Braze に送信

[コホートインポート同期パートナー文書]({{site.baseurl}}/partners/isv_partners/cohort_import/)<br>
-BrazeのコホートインポートAPIエンドポイントを使用して、ユーザーのオーディエンスをコホートとしてBrazeに同期できます。これらのオーディエンスをユーザー属性としてユーザープロファイルに保存するのではなく、お客様はセグメンテーションツール内のパートナーブランドフィルターを使用してこのコホートを構築し、ターゲットを絞ることができます。これにより、特定のユーザーセグメントを顧客にとってより簡単かつ簡単に見つけてターゲティングできるようになります。
-コホートインポートのエンドポイントは公開されておらず、各パートナーに固有です。このため、コホートエンドポイントへの同期は、お客様のワークスペースのレート制限にはカウントされません。 

[ユーザートラック]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)<br>
-これはパブリックにアクセス可能なエンドポイントで、ユーザー属性を使用して特定のオーディエンスのユーザーを示すことで、Brazeですぐにユーザーを作成できます。このエンドポイントとコホートインポートエンドポイントの主な違いは、このエンドポイントを使用して送信されたオーディエンスはユーザープロファイルに保存されるのに対し、コホートインポートエンドポイントはセグメンテーションツールでフィラーとして表示されることです。このエンドポイントには、ワークスペースレベルで適用される1分あたり50,000リクエストのレート制限があります。
-このエンドポイントを使用するときは、`partner`[パートナー向けドキュメントに示されているキーが含まれていることを確認してください]({{site.baseurl}}/partners/isv_partners/api_partner)。

[データポイント]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points#data-points)<br>
-Brazeにはデータポイント消費モデルがあり、値が変更されたかどうかに関係なく、ユーザープロファイルへの「書き込み」ごとにデータポイントが発生します。
-データポイントは、コホートインポートとユーザートラックのエンドポイントの両方で発生します。

## パートナーへのエンゲージメント分析ストリーミング

### Currents

Currents は Braze のほぼリアルタイムのメッセージエンゲージメント分析ストリーミングツールです。これにより、顧客のワークスペースから送信されたキャンペーンやキャンバスのすべての送信、配信、開封、クリックなどに関するユーザーレベルのデータがストリーミングされます。注意すべき点がいくつかあります。Currentsはお客様ごとにコネクタごとに価格設定されるため、Currentsの新規パートナーはEAプロセスを経る必要があります。カスタムブランドの UI を構築してコネクタを公開する前に、パートナーに EA の一部として 5 人の顧客がいることをお願いしています。
-[パートナー向け文書]({{site.baseurl}}/partners/isv_partners/currents_integration/)
-[メッセージエンゲージメントイベント]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events)-Currents コネクタを購入したすべてのお客様は、これらのイベントにアクセスできます。
-[ユーザー行動イベント]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events)-現在のコネクタを購入したすべてのお客様が、これらのイベントを含む「すべてのイベント」コネクタを購入するわけではありません。 

### スノーフレークデータシェア

Snowflake Data Share Connectorを購入したお客様は、メッセージエンゲージメントとユーザー行動イベントの両方に自動的にアクセスできるようになります。Snowflakeデータ共有をパートナー統合として使用する場合、Brazeは顧客に代わってパートナーのSnowflakeインスタンスに共有をプロビジョニングします。注意点として、クロスリージョンのデータ共有はお客様にとってより高い価格帯となるため、Snowflakeとの統合を希望するパートナーには、アカウントおよび/またはアカウントが必要であるというガイダンスをお願いします `US-EAST-1` `EU-CENTRAL-1`
-[パートナー向け文書]({{site.baseurl}}/partners/isv_partners/currents_integration/)

## キャンペーンとキャンバスの構築と起動

### Braze でのアセットの作成
Brazeは、顧客とパートナーが顧客のワークスペース内でメールテンプレートとコンテンツブロックを作成/更新できるエンドポイントを多数提供しています。これらのテンプレートとコンテンツブロックは、お客様のBrazeキャンペーンとキャンバスで順番に使用できます。
メールテンプレート
    -[テンプレートエンドポイントの作成]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template/)
    -[テンプレートエンドポイントの更新]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template/#rate-limit)
- [コンテンツブロック]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks#content-blocks)
    -[コンテンツブロックエンドポイントの作成]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block/)
    -[コンテンツブロックエンドポイントの更新]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block/)

### API トリガーキャンペーンとキャンバス

顧客はキャンペーンとキャンバスをAPIトリガーに設定できます。これらのキャンペーンをトリガーする API リクエストを使用して、APIトリガープロパティとオーディエンスまたは受信者パラメーターを渡すことで、キャンペーンをさらにパーソナライズしてセグメント化できます。
-API [経由でキャンペーンをトリガーする]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/#request-body)
    -キャンペーンは、個別のメールなどの単一のメッセージです。
-API [によるキャンバスのトリガー]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/#request-body)
    -Canvasは、マーケティング担当者が複数のメッセージとステップを含むキャンペーンを作成し、まとまりのあるジャーニーを形成できる統合インターフェイスです。Canvasを起動すると、Canvasフローにユーザーが入力されます。Canvasフローでは、Canvasの基準を満たさなくなるまでメッセージを受信し続けます。
-[API トリガープロパティ/キャンバスエントリプロパティ]({{site.baseurl}}/api/objects_filters/trigger_properties_object)
    -送信時にメッセージに動的に入力できるデータ。

### API キャンペーン
APIキャンペーン（上記のAPIトリガーキャンペーンとは異なります）を作成する場合、Brazeダッシュボードはキャンペーンレポートの生成にのみ使用されます。これにより`campaign_id`、顧客はキャンペーンレポートの分析を追跡できます。キャンペーンメッセージ自体は API リクエスト内で定義されます。
-[API キャンペーンをすぐに送信]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/)
-[API キャンペーンをスケジュールする]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages/)

### ID を送信
Brazeのエンドポイントを使用して送信IDを生成し、これを使用してキャンペーン分析を送信ごとに分類できます。たとえば、`campaign_id`（APIキャンペーン）をロケーションごとに作成する場合、送信ごとに送信IDを生成して、特定のロケーションでのさまざまなメッセージングのパフォーマンスを追跡できます。
-[ID を送信]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids/)

## コネクテッドコンテンツ

コネクテッドコンテンツはどのチャンネルタイプでも使用でき、送信時に指定されたエンドポイントに API リクエストを送信し、応答で返された内容をメッセージに入力できます。

コネクテッドコンテンツは汎用性が高いため、Braze には存在しない、または表示できないコンテンツを挿入する場合に多くのお客様がこの機能を使用しています。一般的な使用例としては、次のようなものがあります。
-ブログや記事のコンテンツをメッセージにテンプレート化する
-おすすめコンテンツ
-製品メタデータ
-ローカリゼーションと翻訳

注意すべき点:
-Braze は API 呼び出しに対して課金せず、データポイントの割り当てにもカウントされません。
-コネクテッドコンテンツのレスポンスには 1 MB の制限があります。
-Connected Contentの呼び出しは、メッセージが送信されたときに行われます。ただし、アプリ内メッセージは、メッセージが表示されたときにこの呼び出しが行われます。
-接続コンテンツの呼び出しはリダイレクトには従いません。Braze では、パフォーマンス上の理由からサーバーの応答時間が 2 秒未満である必要があります。サーバーが応答するまでに 2 秒以上かかる場合、コンテンツは挿入されません。
-Braze のシステムは、受信者1人につき同一のコネクテッドコンテンツ API 呼び出しを複数回行う場合があります。これは、Braze がメッセージペイロードをレンダリングするために Connected Content API 呼び出しを行う必要がある場合があり、メッセージペイロードは、検証、再試行ロジック、またはその他の内部目的で受信者ごとに複数回レンダリングされる可能性があるためです。 

コネクテッドコンテンツの詳細については、次の記事を参照してください。
-[コネクテッドコンテンツ通話を行う][1]
-[接続コンテンツの中止][2]
- [コネクテッドコンテンツの再試行][3]

[1]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/
[2]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content
[3]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/connected_content_retries
