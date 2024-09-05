---
nav_title: ベストプラクティス
hidden: true
---

# ユーザーライフサイクルと識別子のベストプラクティス

## データ収集

Brazeのデータ収集方法について詳しく知る：
- [SDK によるデータ収集]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/)
- [データ収集のベストプラクティス]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/best_practices/)
- [ユーザープロファイルのライフサイクル]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/)

## ブレイズ識別子

- `braze_id`:Brazeが割り当てた識別子で、変更不可能であり、当社のデータベース内で作成されたときに特定のユーザーと関連付けられる。
- `external_id`:顧客が割り当てた識別子で、通常はUUIDである。ユーザーを一意に識別できる場合、`external_id` を割り当てることを推奨する。ユーザーが特定された後、匿名に戻すことはできない。
- `user_alias`:`external_id` が割り当てられる前に、IDによってユーザーを参照する手段として、顧客が割り当てることができる一意の代替識別子。ユーザーエイリアスは、Brazeの[ユーザー識別]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/)エンドポイントを介して利用可能になったときに、後で他のエイリアスまたは`external_id` 。
    - [User identify]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/)エンドポイント内では、`merge_behavior` フィールドを使用して、ユーザーエイリアスプロファイルのどのデータを既知のユーザープロファイルに永続させるかを指定することができる。
    - ユーザーエイリアスを送信可能なプロファイルとするためには、プロファイルの標準属性としてEメールおよび/または電話を含める必要があることに注意すること。
- `device_id`:自動的に生成される、機器固有の識別子。ユーザープロファイルには、いくつかの`device_ids` 。例えば、職場のコンピューター、自宅のコンピューター、タブレット、iOSアプリでアカウントにログインしているユーザーは、自分のプロフィールに4つの`device_ids` 。
- Eメールアドレスと電話番号
    - Brazeのtrack user endpointの識別子としてサポートされている。 
    - リクエストの識別子としてメールアドレスや電話番号を使用する場合、3つの結果が考えられる：
        1. このメールアドレス/電話番号を持つユーザーがBraze内に存在しない場合、メールアドレスのみ/電話番号のみのユーザープロファイルが作成され、リクエスト内のデータがプロファイルに追加される。
        2. このEメール/電話番号のプロフィールがBraze内にすでに存在する場合、リクエスト内で送信されたデータが含まれるように更新される。
        3. このEメール／電話番号で複数のプロフィールがあるユースケースでは、最も新しく更新されたプロフィールが優先される。
    - Eメールのみ/電話のみのユーザープロファイルが存在し、同じEメール/電話の識別プロファイルが作成された場合（同じEメールアドレスと外部IDを持つ別のプロファイルなど）、Brazeは2つ目のプロファイルを作成することに注意。それ以降の更新は、外部IDを持つプロファイルに送られる。
        - 2つのプロファイルは、Braze[/merge/users]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/)エンドポイントを使用してマージできる。

## 匿名ユーザーを扱う

`external_id` にアクセスすることなく、Brazeでユーザープロファイルを作成または更新する必要があるユースケースの場合、電子メールアドレスや電話番号などの別の識別子をBraze[Export user by identifier]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/)エンドポイントに渡すことで、そのユーザーのプロファイルがBraze内に存在するかどうかを判断することができる。 

```json
{
 "email_address": "test@braze.com",
 "fields_to_export": ["braze_id", "user_aliases"]
}
```

Braze内にそのメールアドレスまたは電話番号を持つユーザーが存在する場合、そのユーザーのプロフィールが返される。そうでなければ、空の "users "配列が返される。エクスポート・エンドポイントを使用して、その電子メール・アドレスを持つユーザーがすでに存在するかどうかを判断する利点は、匿名ユーザー・プロファイルがそのユーザーに関連付けられているかどうかを判断できるようになることである。例えば、SDK経由で作成された匿名プロファイル（`braze_id` ）や、以前に作成されたユーザーエイリアスプロファイルなどである。 

リクエストがユーザープロファイルを返さない場合、ユーザーエイリアスを作成するか、電子メールのみのユーザーを作成するかを選択できる：

### ユーザーエイリアス

ユーザートラックエンドポイントを使用して、エイリアス名として選択した識別子を使用して、ユーザエイリアスを作成する。新しいユーザー・エイリアスが定義されている属性、イベント、または購入オブジェクト内に`false` として`_update_existing_only` を含めることで、エイリアス プロファイルを作成し、そのプロファイルに属性、イベント、および購入を同時に追加することができる。 

ユーザーエイリアスを送信可能なプロファイルとするためには、以下のように、`email` フィールドに電子メールアドレスを含める必要がある。

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

このユーザーエイリアスを後で特定し、[Identify users]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/)エンドポイントを通じて`external_id` 。 

### Eメールのみのユーザーを作成する

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
この機能は現在、早期アクセスとなっている。
{% endalert %}

## ユーザープロファイルにデータを同期する

[ユーザートラック]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)
- これは、ユーザープロファイルへの属性の記録など、Brazeでユーザーを作成および更新できる一般にアクセス可能なエンドポイントである。このエンドポイントには、ワークスペース・レベルで適用される毎分50,000リクエストのレート制限がある。
- このエンドポイントを使用する場合は、パートナーのドキュメントに示されているように、`partner` キーを含める。

[クラウドデータ取り込み]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/cloud_ingestion/overview/#what-is-cloud-data-ingestion)
- ユーザートラックエンドポイントと同様に、データはCloud Data Ingestionを通じてユーザプロファイルに同期することができる。このツールを使用する場合、同期させたいデータウェアハウスのテーブルやビューを設定し、希望のBrazeワークスペースに接続することで、属性、イベント、購入がプロファイルに記録される。

[データポイント]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points#data-points)
- Brazeのデータポイント消費モデルでは、値が変更されたかどうかにかかわらず、ユーザープロファイルへの「書き込み」ごとにデータポイントが発生する。このため、変更のあった属性のみをBrazeに送信することを推奨する。 

## ユーザーのオーディエンスをBrazeに送る

[コーホート・インポート・シンク・パートナーのドキュメント]({{site.baseurl}}/partners/isv_partners/cohort_import/)<br>
- ユーザーのオーディエンスは、BrazeのコホートインポートAPIエンドポイントを使用して、コホートとしてBrazeに同期できる。これらのオーディエンスは、ユーザー属性としてユーザー・プロファイルに保存されるのではなく、当社のセグメンテーション・ツール内のパートナー・ブランドのフィルターを通じて、このコホートを構築し、ターゲットを絞ることができる。これにより、顧客は特定のユーザー・セグメントを見つけやすくなり、ターゲットを絞りやすくなる。
- コホート・インポートのエンドポイントは公開されておらず、各パートナーに固有のものである。このため、コホートエンドポイントへの同期は、顧客のワークスペースのレート制限にカウントされない。 

[ユーザートラック]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)<br>
- これは、一般にアクセス可能なエンドポイントであり、ユーザー属性を通じて特定のオーディエンスのユーザーを示すことで、Brazeでユーザーを作成するためにすぐに使用できる。このエンドポイントとコホート・インポート・エンドポイントの主な違いは、このエンドポイントを使用して送信されたオーディエンスはユーザー・プロファイルに保存されるのに対し、コホート・インポート・エンドポイントはセグメンテーション・ツールにフィラーとして表示されることである。このエンドポイントには、ワークスペース・レベルで適用される毎分50,000リクエストのレート制限がある。
- このエンドポイントを使用する際は、[パートナーのドキュメントに]({{site.baseurl}}/partners/isv_partners/api_partner)示されているように、`partner` キーを含めていることを確認すること。

[データポイント]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points#data-points)<br>
- Brazeのデータポイント消費モデルでは、値が変更されたかどうかにかかわらず、ユーザープロファイルへの「書き込み」ごとにデータポイントが発生する。
- データポイントは、コホートインポートとユーザートラックのエンドポイントの両方で発生する。

## パートナーへのエンゲージメント分析ストリーミング

### Currents

Currentsは、Brazeのほぼリアルタイムのメッセージエンゲージメント分析ストリーミングツールである。これは、顧客のワークスペースから送信されたキャンペーンとキャンバスのすべての送信、配信、開封、クリックなどに関するユーザーレベルのデータをストリーミングする。注意すべき点がいくつかある：カレントの価格は顧客向けのコネクターごとに設定されているため、新規のカレント・パートナーはすべてEAプロセスを経なければならない。カスタムブランドのUIを構築し、コネクタを一般に公開する前に、パートナーはEAの一部として5社の顧客を持つようお願いしている。 
- [パートナーの文書]({{site.baseurl}}/partners/isv_partners/currents_integration/)
- [メッセージ・エンゲージメント・イベント]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events)\- Currentsコネクタを購入したすべての顧客は、これらのイベントにアクセスできる。
- [ユーザー行動イベント]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events)\- Currentコネクタを購入するすべての顧客が、これらのイベントを含む「すべてのイベント」コネクタを購入するとは限らない。 

### スノーフレーク・データ・シェア

Snowflake Data Shareコネクタを購入した顧客は、メッセージのエンゲージメントとユーザー行動の両方のイベントに自動的にアクセスできるようになる。Snowflake Data Shareがパートナー統合として使用される場合、Brazeが顧客に代わってパートナーのSnowflakeインスタンスに共有をプロビジョニングする。注意点として、リージョンをまたいだデータ共有は、顧客にとってより高い価格設定となるため、Snowflakeとの統合を希望するパートナーには、`US-EAST-1` および/または `EU-CENTRAL-1`
- [パートナーの文書]({{site.baseurl}}/partners/isv_partners/currents_integration/)

## キャンペーンとキャンバスの構築とトリガー

### Brazeでアセットを作成する
Brazeは、顧客やパートナーが顧客のワークスペース内でメールテンプレートやコンテンツブロックを作成/更新できるようにするエンドポイントを多数提供している。これらのテンプレートとコンテンツブロックは、顧客のBrazeキャンペーンとキャンバス全体で使用することができる。
- メールテンプレート
    - [テンプレート・エンドポイントを作成する]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template/)
    - [テンプレートのエンドポイントを更新する]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template/#rate-limit)
- [コンテンツブロック]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks#content-blocks) 
    - [コンテンツ・ブロック・エンドポイントを作成する]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block/)
    - [コンテンツ・ブロックのエンドポイントを更新する]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block/)

### APIトリガー・キャンペーンとキャンバス

顧客はAPIトリガーでキャンペーンやキャンバスを設定できる。これらのキャンペーンをトリガーするためのAPIリクエストは、APIトリガープロパティとオーディエンスまたは受信者パラメータを渡すことによって、キャンペーンをさらにパーソナライズおよびセグメント化するために使用することができる。 
- [API経由でキャンペーンをトリガーする]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/#request-body)
    - キャンペーンとは、個々のEメールのような単発のメッセージのことである。
- [API経由でキャンバスをトリガーする]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/#request-body)
    - Canvasは、マーケターが複数のメッセージとステップを持つキャンペーンを作成し、まとまったジャーニーを形成できる統一されたインターフェイスである。キャンバスをトリガーすると、キャンバスフローにユーザーを入力することになり、キャンバスの条件に合わなくなるまで、メッセージングを受け取り続けることになる。 
- [APIトリガープロパティ/キャンバスエントリープロパティ]({{site.baseurl}}/api/objects_filters/trigger_properties_object) 
    - 送信時にメッセージに動的に入力できるデータ。

### APIキャンペーン
APIキャンペーン（上記で言及したAPIトリガーキャンペーンとは異なる）を作成する場合、Brazeダッシュボードは`campaign_id` を生成するためにのみ使用される。キャンペーンメッセージ自体はAPIリクエストの中で定義される。 
- [APIキャンペーンをすぐに送信する]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/)
- [APIキャンペーンをスケジュールする]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages/)

### IDを送信する
Brazeのエンドポイントを使用して送信IDを生成し、送信ごとにキャンペーン分析を分解するために使用できる。例えば、`campaign_id` （APIキャンペーン）をロケーションごとに作成した場合、送信ごとに送信IDを生成し、特定のロケーションに対して異なるメッセージングがどの程度うまく機能しているかを追跡することができる。 
- [IDを送信する]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids/)

## コネクテッドコンテンツ

コネクテッド・コンテンツは、送信時に指定されたエンドポイントにAPIリクエストを行い、レスポンスで返された内容をメッセージに入力するために、どのチャネル・タイプでも使用できる。

Connected Contentsの多機能性により、Brazeにはない、あるいはBrazeにはないコンテンツを挿入するために、多くの顧客がこの機能を利用している。一般的な使用例としては、以下のようなものがある：
- ブログや記事の内容をメッセージにテンプレート化する
- 推奨コンテンツ
- 製品メタデータ
- ローカリゼーションと翻訳

注意しなければならないことがある：
- BrazeはAPIコールには課金せず、データポイントの割り当てにはカウントしない。
- コネクテッド・コンテンツの回答には1MBの制限がある。
- コネクテッド・コンテンツの呼び出しは、メッセージの送信時に行われるが、アプリ内メッセージは例外で、メッセージの閲覧時にこの呼び出しが行われる。
- コネクテッド・コンテンツの呼び出しは、redirects.Braze 、パフォーマンス上の理由からサーバーの応答時間が2秒未満であることを要求している。サーバーの応答に2秒以上かかる場合、コンテンツは挿入されない。
- Brazeのシステムは、受信者ごとに同じConnected Content APIコールを複数回行う場合がある。なぜなら、Brazeは、メッセージペイロードをレンダリングするためにConnected Content APIをコールする必要があるかもしれないし、メッセージペイロードは、検証、再試行ロジック、その他の内部的な目的のために、受信者ごとに複数回レンダリングされる可能性があるからだ。 

コネクテッド・コンテンツの詳細については、以下の記事を参照されたい：
- [コネクテッド・コンテンツに電話をかける][1]
- [接続されたコンテンツを中止する][2]
- [コネクテッド・コンテンツの再試行][3]

[1]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/
[2]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content
[3]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/connected_content_retries
