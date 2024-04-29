---
nav_title: ベストプラクティス
hidden: true
---

# ユーザーライフサイクルと識別子のベストプラクティス

## データ収集

Brazeによるデータ収集方法の詳細:
・[SDKデータ収集]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/)
-[データ収集のベストプラクティス]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/best_practices/)
-[ユーザープロファイルライフサイクル]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/)

## Braze identifiers

- `braze_id`:Brazeが割り当てた識別子で、当社のデータベース内で作成された場合、変更できず、特定のユーザーに関連付けられます。
- `external_id`:顧客が割り当てた識別子。通常はUUID。ユーザを一意に識別できる場合に`external_id`を割り当てることをお勧めします。ユーザーが特定されると、匿名に戻すことはできません。
- `user_alias`:割り当てられる`external_id`の前に、IDによってユーザーを参照する手段として顧客が割り当てることができる一意の代替識別子。ユーザーエイリアスは、Brazeの[ユーザー識別]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/)エンドポイントを通じて他のエイリアスや`external_id`が利用可能になったときに、後でマージすることができます。
    - [[ユーザー識別]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/)エンドポイント]内の[`merge_behavior`]フィールドを使用して、ユーザーエイリアスプロファイルから既知のユーザープロファイルに保持するデータを指定できます。
    - ユーザエイリアスを送信可能なプロファイルにするには、プロファイルの標準属性として電子メールおよび/または電話を含める必要があることに注意してください。
- `device_id`:自動的に生成されるデバイス固有の識別子。ユーザプロファイルには、多数の`device_ids`を関連付けることができます。例えば、職場のパソコン、自宅のパソコン、タブレット、iOSアプリでアカウントにログインしたユーザーは、プロフィールに4つの`device_ids`が関連付けられます。
- メールアドレス&電話番号:
    - Brazeのトラックユーザーエンドポイントの識別子としてサポートされています。 
    - メールアドレスまたは電話番号をリクエスト内の識別子として使用する場合、次の3つの結果が考えられます。
        1. このメール/phone does not exist within Braze, an email-only/phone-only user profile will be created, and any data in the request will be added to the profile.を持つユーザーが
        2. このEメール/電話を持つプロファイルがすでにBraze内に存在する場合、リクエスト内に送信されたデータが含まれるように更新されます。
        3. このメール/電話で複数のプロファイルを持つユースケースでは、最後に更新されたプロファイルが優先されます。
    - なお、電子メール専用/phone-only user profile exists and then an identified profile with the same email/phone is created (such as another profile with the same email address AND an external ID), Braze will create a second profile. Subsequent updates will go to the profile with the external ID.の
        - 2つのプロファイルは、Braze[/merge/users]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/)エンドポイントを使用してマージできます

## 匿名ユーザーの取り扱い

`external_id`にアクセスせずにBrazeでユーザープロファイルを作成または更新する必要があるユースケースでは、メールアドレスや電話番号のような別の識別子を識別子エンドポイントによってBraze[エクスポートユーザー]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/)に渡して、ユーザーのプロファイルがBraze内に存在するかどうかを判断できます。 

```json
{
 "email_address": "test@braze.com",
 "fields_to_export": ["braze_id", "user_aliases"]
}
```

そのメールや電話を持つユーザーがBraze内に存在する場合、そのユーザーのプロファイルが返されます。それ以外の場合、空の "users" 配列が返されます。エクスポートエンドポイントを使用して、そのメールアドレスを持つユーザーがすでに存在するかどうかを判断する利点は、匿名ユーザープロファイルがユーザーに関連付けられているかどうかを確認できることです。たとえば、SDKを介して作成された匿名プロファイル（`braze_id`を持つことになる）や、以前に作成されたユーザーエイリアスプロファイルなどです。 

要求がユーザプロファイルを返さない場合は、ユーザエイリアスを作成するか、電子メールのみのユーザを作成するかを選択できます。

### ユーザーのエイリアス

ユーザ追跡エンドポイントを使用して、選択した識別子をエイリアス名として使用し、ユーザエイリアスを作成します。新しいユーザエイリアスが定義されている属性、イベント、または購入オブジェクト内に`_update_existing_only`を`false`として含めることで、エイリアスプロファイルを作成し、そのプロファイルに属性、イベント、および購入を同時に追加できます。 

ユーザエイリアスを送信可能なプロファイルにするには、次に示すように、[`email`]フィールドに電子メールアドレスを含める必要があります。

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

このユーザーエイリアスは、[ユーザーの識別]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/)エンドポイントを通じて`external_id`が利用可能になったときに、後で識別してマージできます。 

### メール専用ユーザーの作成

ユーザー追跡エンドポイントで電子メールアドレスを識別子として使用します。 

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
この機能は現在早期アクセス中です。
{% endalert %}

## ユーザープロファイルへのデータの同期

[ユーザートラック]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)
-これは、ユーザープロファイルへのロギング属性など、Brazeでユーザーを作成および更新できるパブリックアクセス可能なエンドポイントです。このエンドポイントには、ワークスペースレベルで1分間に50,000リクエストというレート制限が適用されます。
-このエンドポイントを使用する場合は、パートナーのドキュメントに示すように`partner`キーを含めます。

[クラウドデータ取り込み]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/cloud_ingestion/overview/#what-is-cloud-data-ingestion)
-ユーザートラックのエンドポイントと同様に、Cloud Data Ingestionを介してユーザープロファイルにデータを同期できます。このツールを使用すると、同期したいデータウェアハウステーブルまたはビューを任意のBrazeワークスペースに設定して接続することで、属性、イベント、購入がプロファイルに記録されます。

[データポイント]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points#data-points)
-Brazeにはデータポイント消費モデルがあり、値が変更されたかどうかに関係なく、ユーザープロファイルへの「書き込み」ごとにデータポイントが発生します。そのため、属性が変更されたもののみをBrazeに送信することをお勧めします。 

## Brazeにユーザーのオーディエンスを送る

[コホートインポート同期パートナードキュメント]({{site.baseurl}}/partners/isv_partners/cohort_import/)<br>
-BrazeのCohort Import APIエンドポイントを使用して、ユーザーのオーディエンスをコホートとしてBrazeに同期できます。これらのオーディエンスをユーザー属性としてユーザープロファイルに保存するのではなく、セグメンテーションツール内のパートナーブランドのフィルターを通して、お客様はこのコホートを構築し、ターゲティングすることができます。これにより、特定のセグメントのユーザーを見つけ、ターゲティングすることが、顧客にとってより簡単でシンプルになります。
-コホートインポートのエンドポイントは公開されておらず、各パートナーに固有です。このため、コホートエンドポイントへの同期は、顧客のワークスペースレート制限にカウントされません。 

[ユーザートラック]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)<br>
-これは公開アクセス可能なエンドポイントで、ユーザー属性を通じて特定のオーディエンスのユーザーを示すことで、Brazeでユーザーを作成するためにすぐに使用できます。このエンドポイントとコホートインポートエンドポイントの主な違いは、このエンドポイントを使用して送信されたオーディエンスがユーザープロファイルに保存されるのに対し、コホートインポートエンドポイントはセグメンテーションツールでフィラーとして表示されることです。このエンドポイントには、ワークスペースレベルで1分間に50,000リクエストというレート制限が適用されます。
-このエンドポイントを使用する場合は、[パートナードキュメント]({{site.baseurl}}/partners/isv_partners/api_partner)に示されているように、`partner`キーが含まれていることを確認してください。

[データポイント]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points#data-points)<br>
-Brazeにはデータポイント消費モデルがあり、値が変更されたかどうかに関係なく、ユーザープロファイルへの「書き込み」ごとにデータポイントが発生します。
-データポイントは、コホートインポートとユーザートラックのエンドポイントの両方で発生します。

## パートナーへのエンゲージメント分析ストリーミング

### Currents

Currentsは、Brazeのほぼリアルタイムのメッセージエンゲージメント分析ストリーミングツールです。これにより、顧客のワークスペースから送信されたキャンペーンやキャンバスのすべての送信、配信、開封、クリックなどのユーザーレベルのデータがストリーミングされます。いくつか注意点があります。電流はお客様のコネクタごとに価格設定されるため、まったく新しい電流パートナーはEAプロセスを受ける必要があります。カスタムブランドのUIを構築し、コネクタを一般に公開する前に、EAの一部としてパートナーのお客様が5社存在するようにしてください。
-[パートナー向けドキュメント]({{site.baseurl}}/partners/isv_partners/currents_integration/)
-[メッセージエンゲージメントイベント]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events)-Currentsコネクタを購入したすべてのお客様がこれらのイベントにアクセスできます。
-[ユーザー動作イベント]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events)-Currentコネクタを購入したすべてのお客様が、これらのイベントを含む「すべてのイベント」コネクタを購入するとは限りません。 

### Snowflake データ共有

Snowflake Data Shareコネクタを購入すると、メッセージエンゲージメントとユーザー行動イベントの両方に自動的にアクセスできます。Snowflake Data Shareをパートナーインテグレーションとして利用する場合、Brazeは顧客に代わってパートナーのSnowflakeインスタンスにシェアをプロビジョニングします。注意：地域をまたいだデータ共有は、お客様にとって価格が高くなるため、Snowflakeとの統合を希望するパートナー様には、`US-EAST-1`および/または`EU-CENTRAL-1`にアカウントが必要であるというガイダンスを
-[パートナー向けドキュメント]({{site.baseurl}}/partners/isv_partners/currents_integration/)

## キャンペーンとキャンバスの構築とトリガー

### Brazeでアセットを作成する
Brazeは、顧客とパートナーが顧客のワークスペース内でメールテンプレートとコンテンツブロックを作成/更新できる多数のエンドポイントを提供します。これらのテンプレートとコンテンツブロックは、順次、顧客のBrazeキャンペーンとCanvasesで使用することができます。
メールテンプレート
    -[テンプレートエンドポイントの作成]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template/)
    -[テンプレートエンドポイントの更新]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template/#rate-limit)
 つのコンテンツブロック
    [-コンテンツブロックエンドポイントの作成]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block/)
    -コンテンツブロックエンドポイントの[更新]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block/)

### APIを利用したキャンペーンとキャンバス

顧客はキャンペーンやCanvasesをAPIトリガーに設定できる。これらのキャンペーンをトリガーするAPIリクエストは、APIトリガーのプロパティとオーディエンスまたは受信者のパラメータを渡すことで、キャンペーンをさらにパーソナライズしてセグメント化するために使用できます。
[-APIによるキャンペーンのトリガー]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/#request-body)
    -キャンペーンは、個別のメールなど、単独のメッセージです。
[-API経由でキャンバスを起動する]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/#request-body)
    -Canvasは、マーケティング担当者が複数のメッセージとステップでキャンペーンを作成し、一貫したジャーニーを形成するための統一されたインターフェイスです。Canvasをトリガーする場合、Canvasフローにユーザーを入力することになります。ユーザーは、Canvasの条件に適合しなくなるまでメッセージを受け取り続けます。
[-APIトリガーのプロパティ/キャンバスエントリのプロパティ]({{site.baseurl}}/api/objects_filters/trigger_properties_object)
    -送信時にメッセージに動的に入力できるデータ。

### API キャンペーン
APIキャンペーンを作成する場合（前述のAPIトリガーキャンペーンとは異なる ） 、 Brazeダッシュボードは`campaign_id`を生成するためだけに使用され、これにより顧客はキャンペーンレポートのためのアナリティクスを追跡できます。キャンペーンメッセージ自体はAPIリクエスト内で定義されています。
[-APIキャンペーンをすぐに送信]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/)
-[APIキャンペーンのスケジュール]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages/)

### IDを送信する
Brazeのエンドポイントを使用して送信IDを生成し、送信ごとにキャンペーン分析を分解できます。たとえば、ロケーションごとに`campaign_id`（APIキャンペーン）を作成した場合、送信ごとに送信IDを生成して、特定のロケーションで異なるメッセージングがどの程度適切に実行されているかを追跡できます。
- [SEND ID]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids/)

## コネクテッドコンテンツ

コネクテッドコンテンツは、任意のチャネルタイプ内で使用でき、送信時に指定されたエンドポイントにAPIリクエストを行い、応答で返される内容をメッセージに入力できます。

Connected Contentsの汎用性は、Brazeに存在しない、または存在しないコンテンツを挿入するために多くのお客様が使用している機能です。私たちが目にするより一般的な使用例としては、
-ブログや記事のコンテンツをメッセージにまとめる
-コンテンツの推奨
-製品のメタデータ
-ローカリゼーションと翻訳

注意点：
-BrazeはAPIコールに課金されず、データポイントの割り当てにカウントされません。
-コネクテッドコンテンツのレスポンスには1MBの制限があります。
-コネクテッドコンテンツの呼び出しは、メッセージが送信されたときに行われます。ただし、アプリ内メッセージの場合は、メッセージが表示されたときにこの呼び出しが行われます。
-Connected Contentの呼び出しはリダイレクトに従いません。Brazeでは、パフォーマンス上の理由からサーバーの応答時間が2秒未満である必要があります。サーバーの応答に2秒以上かかる場合、コンテンツは挿入されません。
-Brazeのシステムは、同じConnected Content API呼び出しを受信者1人につき複数回行う場合があります。なぜなら、BrazeはメッセージペイロードをレンダリングするためにConnected Content APIの呼び出しが必要になる場合があり、メッセージペイロードは検証、再試行ロジック、またはその他の内部目的のために受信者ごとに複数回レンダリングできるからです。 

コネクテッドコンテンツの詳細については、以下の記事を参照してください。
[-コネクテッドコンテンツの通話][1]
-[接続コンテンツの中断][2]
コネクテッドコンテンツの再試行

[1]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/
[2]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content
[3]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/connected_content_retries
