---
nav_title: ベストプラクティス
hidden: true
---

# ユーザーライフサイクルと識別子のベストプラクティス

## データ収集

Braze でのデータの収集方法について詳しくは、以下を参照してください。
- [SDK によるデータ収集]({{site.baseurl}}/user_guide/data/user_data_collection/sdk_data_collection/)
- [データ収集のベストプラクティス]({{site.baseurl}}/user_guide/data/user_data_collection/best_practices/)
- [ユーザープロファイルのライフサイクル]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/)

## ブレイズ識別子

- `braze_id`:Brazeが割り当てた識別子で、変更不可能であり、当社のデータベース内で作成されたときに特定のユーザーと関連付けられる。
- `external_id`:顧客が割り当てた識別子で、通常はUUIDである。ユーザーを一意に識別できる場合、`external_id` を割り当てることを推奨する。ユーザーが特定された後、匿名に戻すことはできない。
- `user_alias`:`external_id` が割り当てられる前に、ID によってユーザーを参照する手段として、顧客が割り当てることができる一意の代替識別子。ユーザーエイリアスは、Braze [ユーザー識別]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/)エンドポイントを通じて利用可能になったときに、後で他のエイリアスまたは `external_id` とマージできます。
    - [ユーザー識別]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/)エンドポイント内では、`merge_behavior` フィールドを使用して、ユーザーエイリアスプロファイルのどのデータを既知のユーザープロファイルで永続化するかを指定できます。
    - ユーザーエイリアスを送信可能なプロファイルにするには、メールまたは電話番号あるいはこの両方をプロファイルに標準属性として含める必要があることに注意してください。
- `device_id`:自動的に生成される、機器固有の識別子。ユーザープロファイルには、複数の`device_ids` を関連付けることができます。たとえば、仕事用コンピューター、ホームコンピューター、タブレット、および iOS アプリでアカウントにログインしたユーザーは、プロファイルに4つの `device_ids` が関連付けられます。
- メールアドレス& 電話番号:
    - Braze のユーザー追跡エンドポイントで識別子としてサポートされます。 
    - リクエスト内でメールアドレスまたは電話番号を識別子として使用する場合、3つの結果が考えられます。
        1. このメールアドレス/電話番号を持つユーザーがBraze内に存在しない場合、メールアドレスのみ/電話番号のみのユーザープロファイルが作成され、リクエスト内のデータがプロファイルに追加される。
        2. このメール/電話番号を含むプロファイルが Braze 内にすでに存在する場合、リクエストで送信されたすべてのデータが含まれるようにこのプロファイルが更新される。
        3. このメール/電話番号を含むプロファイルが複数あるユースケースでは、最後に更新されたプロファイルが優先される。
    - メールのみ/電話番号のみのユーザープロファイルが存在し、同じメール/電話番号を含む識別プロファイルが作成された場合 (同じメールアドレスと external ID を持つ別のプロファイルなど)、Braze では2つ目のプロファイルが作成されることに注意してください。それ以降の更新は、外部IDを持つプロファイルに送られる。
        - 2つのプロファイルは、Braze[/merge/users]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/)エンドポイントを使用してマージできる。

## 匿名ユーザーの取り扱い

`external_id` にアクセスすることなく、Brazeでユーザープロファイルを作成または更新する必要があるユースケースの場合、電子メールアドレスや電話番号などの別の識別子をBraze[Export user by identifier]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/)エンドポイントに渡すことで、そのユーザーのプロファイルがBraze内に存在するかどうかを判断することができる。 

```json
{
 "email_address": "test@braze.com",
 "fields_to_export": ["braze_id", "user_aliases"]
}
```

Braze内にそのメールアドレスまたは電話番号を持つユーザーが存在する場合、そのユーザーのプロフィールが返される。そうでなければ、空の "users "配列が返される。エクスポート・エンドポイントを使用して、その電子メール・アドレスを持つユーザーがすでに存在するかどうかを判断する利点は、匿名ユーザー・プロファイルがそのユーザーに関連付けられているかどうかを判断できるようになることである。たとえば、SDK で作成された匿名プロファイル (`braze_id` を含むプロファイル) や、以前に作成されたユーザーエイリアスプロファイルなどです。 

リクエストがユーザープロファイルを返さない場合は、ユーザーエイリアスを作成するか、メールのみのユーザーを作成するかを選択できます。

### ユーザーエイリアス

ユーザートラックエンドポイントを使用して、エイリアス名として選択した識別子を使用して、ユーザエイリアスを作成する。新しいユーザーエイリアスが定義されている属性、イベント、または購入オブジェクトに `_update_existing_only` を `false` として含めることで、エイリアスプロファイルを作成し、そのプロファイルに属性、イベント、購入を同時に追加できます。 

ユーザーエイリアスを送信可能なプロファイルにするには、以下に示すように、`email` フィールドにメールアドレスを含める必要があります。

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

後でこのユーザーエイリアスが[ユーザー識別]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/)エンドポイントで使用可能になったときに、このユーザーエイリアスを特定して `external_id` にマージできます。 

### メールのみのユーザーの作成

ユーザートラックエンドポイントの識別子として電子メールアドレスを使用する。 

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
この機能は初期アクセスです。
{% endalert %}

## ユーザープロファイルにデータを同期する

[ユーザートラック]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)
- これは、ユーザープロファイルへの属性の記録など、Brazeでユーザーを作成および更新できる一般にアクセス可能なエンドポイントである。このエンドポイントには、1分あたり50,000件のリクエストというレート制限がワークスペースレベルで適用されています。
- このエンドポイントを使用する場合は、パートナーのドキュメントに記載されているように、`partner` キーを含めます。

[クラウドデータ取り込み]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/cloud_ingestion/overview/#what-is-cloud-data-ingestion)
- ユーザートラックエンドポイントと同様に、クラウドデータ取り込みを介してデータをユーザープロファイルに同期できます。このツールを使用する場合、目的の Braze ワークスペースに同期するデータウェアハウスのテーブルまたはビューを設定して接続することで、属性、イベント、および購入がプロファイルに記録されます。

[データポイント]({{site.baseurl}}/user_guide/data/data_points/)
- Braze には、値が変更されたかどうかに関係なく、ユーザープロファイルへの「書き込み」ごとにデータポイントs が記録されるデータポイントがあります。このため、変更のあった属性のみをBrazeに送信することを推奨する。 

## Braze へのユーザーオーディエンスの送信

[コホートインポート同期パートナーのドキュメント]({{site.baseurl}}/partners/isv_partners/cohort_import/)<br>
- ユーザーのオーディエンスは、Braze Cohort Import API エンドポイントを使用して、コホートとして Braze と動機できます。これらのオーディエンスをユーザー属性としてユーザープロファイルに保存するのではなく、お客様がBraze のセグメンテーションツール内のパートナーブランドフィルターを使用して、このコホートを作成し、ターゲットに設定できます。これにより、特定のSegmentのユーザーs をより効率的に見つけて対象にすることができます。
- コホートインポートエンドポイントはパブリックではなく、各パートナーに固有です。このため、コホートエンドポイントへの同期は、顧客のワークスペースのレート制限にカウントされない。 

[ユーザートラック]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)<br>
- これは、一般にアクセス可能なエンドポイントであり、ユーザー属性を通じて特定のオーディエンスのユーザーを示すことで、Brazeでユーザーを作成するためにすぐに使用できる。このエンドポイントとコホートインポートエンドポイントの主な違いは、このエンドポイントを使用して送信されたオーディエンスはユーザープロファイルに保存されるのに対し、コホートインポートエンドポイントではセグメンテーションツールでフィラーとして表示されることです。このエンドポイントには、1分あたり50,000件のリクエストというレート制限がワークスペースレベルで適用されています。
- このエンドポイントを使用する場合は、パートナーの[ドキュメント]({{site.baseurl}}/partners/isv_partners/api_partner)に記載されているように、`partner` キーを必ず含めてください。

[データポイント]({{site.baseurl}}/user_guide/data/data_points/)<br>
- Braze には、値が変更されたかどうかに関係なく、ユーザープロファイルへの「書き込み」ごとにデータポイントs が記録されるデータポイントがあります。
- データポイントは、コホートインポートエンドポイントとユーザートラックエンドポイントの両方で発生します。

## パートナーへのエンゲージメント分析ストリーミング

### Currents

Currents は、Braze のほぼリアルタイムのメッセージエンゲージメント分析ストリーミングツールです。これにより、お客様のワークスペースから送信されたキャンペーンおよびキャンバスのすべての送信、配信、開封、クリックなどに関するユーザーレベルのデータがストリーミングされます。いくつかの注意点があります。Currents の価格は、お客様のコネクターあたりの価格であるため、すべての新しい Currents パートナーは EA プロセスを実施する必要があります。カスタムブランドのUIを構築し、コネクタを一般に公開する前に、パートナーはEAの一部として5社の顧客を持つようお願いしている。 
- [パートナーのドキュメント]({{site.baseurl}}/partners/isv_partners/currents_integration/)
- [メッセージエンゲージメントイベント]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) \- Currents コネクターを購入したすべてのお客様はこのイベントにアクセスできます。
- [ユーザー行動イベント]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/)\- Current コネクターを購入したすべてのお客様が、このイベントが含まれている「すべてのイベント」コネクターを購入するとは限りません。 

### Snowflake データシェア

Snowflake データシェアコネクターを購入したお客様は、メッセージエンゲージメントイベントとユーザー行動イベントの両方に自動的にアクセスできるようになります。Snowflake データシェアがパートナー連携として使用されている場合、Braze はお客様に代わってパートナーの Snowflake インスタンスに共有をプロビジョニングします。クロスリージョンのデータ共有はお客様にとって価格が高いポイントであるため、Snowflake との統合を希望するパートナーに対し、`US-EAST-1` および/または`EU-CENTRAL-1` にアカウントが必要であるというガイダンスを依頼します。
- [パートナーのドキュメント]({{site.baseurl}}/partners/isv_partners/currents_integration/)

## キャンペーンとキャンバスの構築とトリガー

### Brazeでアセットを作成する
Brazeは、顧客やパートナーが顧客のワークスペース内でメールテンプレートやコンテンツブロックを作成/更新できるようにするエンドポイントを多数提供している。これらのテンプレートとコンテンツブロックは、お客様の Braze キャンペーンおよびキャンバス全体で使用できます。
- メールテンプレート
    - [テンプレートエンドポイントを作成する]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template/)
    - [テンプレートのエンドポイントを更新する]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template/#rate-limit)
- [コンテンツブロック]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks#content-blocks) 
    - [コンテンツブロックエンドポイントを作成する]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block/)
    - [コンテンツブロックエンドポイントを更新する]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block/)

### API によりトリガーされるキャンペーンとキャンバス

顧客はキャンペーンやキャンバスが API によりトリガーされるように設定できます。これらのキャンペーンをトリガーする API リクエストを使用して、API トリガープロパティとオーディエンスパラメーターまたは受信者パラメーターを渡すことで、キャンペーンをさらにパーソナライズおよびセグメント化できます。 
- [API を使用したキャンペーンのトリガー]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/#request-body)
    - キャンペーンとは、個々のEメールのような単発のメッセージのことである。
- [API を使用したキャンバスのトリガー]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/#request-body)
    - キャンバスは、マーケターが複数のメッセージとステップでキャンペーンを作成し、一貫性のあるジャーニーを形成するための統合インターフェイスです。キャンバスをトリガーすると、キャンバスフローにユーザーを入力することになり、キャンバスの条件に合わなくなるまで、メッセージングを受け取り続けることになる。 
- [APIトリガープロパティ/キャンバスエントリープロパティ]({{site.baseurl}}/api/objects_filters/trigger_properties_object) 
    - 送信時にメッセージに動的に入力できるデータ。

### APIキャンペーン
API キャンペーン (上記の API によりトリガーされるキャンペーンとは異なります) を作成する場合、Braze ダッシュボードは `campaign_id` を生成するためにのみ使用されます。これによりお客様はキャンペーンレポートのために分析を追跡できます。キャンペーンメッセージ自体はAPIリクエストの中で定義される。 
- [API キャンペーンをすぐに送信する]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/)
- [API キャンペーンをスケジュールする]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages/)

### IDを送信する
Braze エンドポイントを使用して送信 ID を生成し、キャンペーン分析を送信別に分類できるようにします。たとえば、ロケーションごとに `campaign_id` (API キャンペーン) が作成されている場合、送信ごとに送信 ID を生成して、特定のロケーションに対して異なるメッセージングがどの程度適切に実行されているかを追跡できます。 
- [IDを送信する]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids/)

## コネクテッドコンテンツ

コネクテッドコンテンツを任意のチャネルタイプ内で使用して、送信時に指定されたエンドポイントに対して API リクエストを実行し、応答で返された内容をメッセージに取り込むことができます。

コネクテッドコンテンツはその汎用性から、多くのお客様が Braze で存続しないまたは存続できないコンテンツを挿入するために使用する機能になりました。一般的な使用例としては、以下のようなものがある：
- ブログや記事の内容をメッセージにテンプレート化する
- コンテンツレコメンデーション
- 製品メタデータ
- ローカライゼーションと翻訳

以下の点に注意してください。
- Braze はAPI コールの料金を請求せず、データポイント使用量にカウントされません。
- コネクテッドコンテンツ応答には 1 MB の制限があります。
- コネクテッド・コンテンツの呼び出しは、メッセージの送信時に行われるが、アプリ内メッセージは例外で、メッセージの閲覧時にこの呼び出しが行われる。
- コネクテッドコンテンツ呼び出しが redirects.Braze に従っていない場合、パフォーマンス上の理由からサーバー応答時間が2秒未満でなければなりません。サーバーの応答時間が2秒よりも長い場合、コンテンツが挿入されません。
- Braze は、各受信者に複数回、同じコネクテッドコンテンツ API 呼び出しを行うことができます。これは、状況によっては Braze がメッセージペイロードを表示するためにコネクテッドコンテンツ API 呼び出しを行う必要があり、メッセージペイロードは、検証、再試行ロジック、またはその他の内部目的のために、受信者ごとに複数回レンダリングされることがあるためです。 

コネクテッド・コンテンツの詳細については、以下の記事を参照されたい：
- [コネクテッドコンテンツ呼び出しを実行する]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/)
- [コネクテッドコンテンツを中止する]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content)
- [コネクテッドコンテンツの再試行]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/connected_content_retries)

