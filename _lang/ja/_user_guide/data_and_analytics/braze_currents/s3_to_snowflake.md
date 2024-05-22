---
nav_title: Amazon S3 から Snowflake へのデータ転送
article_title: Amazon S3 から Snowflake へのデータ転送
page_order: 7
page_type: tutorial
description: "このハウツー記事では、ETL プロセスを使用してクラウドストレージ (Amazon S3 など) からウェアハウス (Snowflake など) にデータを転送する手順を説明します。"
tool: Currents

---

# Amazon S3 から Snowflake へのデータ転送

> 現在データが Amazon S3 にある場合は、 ELT (抽出、読み込み、変換) プロセスを使用して、Snowflake や他のリレーショナルデータウェアハウスに転送できます。

{% alert note %}
より具体的なユースケースがあり、 Currents インスタンスのサービスを Braze に希望する場合は、Braze アカウントマネージャーに Braze データプロフェッショナルサービスについてお問い合わせください。
{% endalert %}

## 自動読み込みプロセス

この自動読み込みプロセスでは、データを [Snowflake](https://www.snowflake.com/) に移動します。これにより、[Braze Looker Blocks](https://marketplace.looker.com/marketplace/directory)を使用して Looker でそのデータを可視化し、インサイトやフィードバックをキャンペーン、キャンバス、およびセグメントで活用できます。

Currents から S3 へのエクスポートを設定し、ライブイベントデータを受信したら、次のコンポーネントを設定することにより Snowflake でライブ ELT パイプラインを設定できます。

-   [AWS SQS キュー](#aws-sqs-queues)
-   [自動取り込み Snowpipe](#auto-ingest-snowpipes)

### AWS SQS キューの設定

**自動取り込み Snowpipe** は、S3 からSnowpipe への通知の送信を SQS キューに依存します。このプロセスは、SQS の設定後に Snowflake によって管理されます。

#### ステップ 1: 外部 S3 ステージの設定

{% alert note %}
データベース内のテーブルはこのステージから作成されます。
{% endalert %}

Braze で Currents を設定するときに、S3 バケットに転送する Currents ファイルのフォルダーのパスを指定します。ここでは、デフォルトのフォルダーのパスである ```currents``` を使用します。

次に、リストされた順序で以下を作成します。

1. AWSで、目的の S3 バケットの新しい**公開キーと秘密キーのペア**を作成します。このときに、組織のセキュリティ要件に応じて権限を付与します。

2. Snowflake で、任意のデータベースとスキーマ (次の例では ```currents``` と ```public``` という名前) を作成します。

3. Snowflake S3 ステージ (`braze_data` という名前) を作成します。

```sql
CREATE OR REPLACE STAGE
    currents.public.braze_data
    url='s3://snowpipe-demo/'
    credentials = (AWS_KEY_ID = '...' AWS_SECRET_KEY = '...' );
show stages;
```

次に、ステージの AVRO ファイル形式を定義します。

```sql
CREATE FILE FORMAT
    currents.public.currents_avro
    type = 'avro'
    compression = 'auto';
```

```sql
ALTER STAGE
    currents.public.braze_data
SET
    file_format = currents.public.currents_avro;
```

\`\`\`sql
CREATE OR REPLACE PIPE
  pipe\_users\_messages\_pushnotification\_open
    auto\_ingest=true AS

COPY INTO
  users\_messages\_pushnotification\_open
          FROM
           (SELECT
             $1:id::STRING,
             $1:user\_id::STRING,
             $1:external\_user\_id::STRING,
              $1:time::INT,
              $1:timezone::STRING,
              $1:app\_id::STRING,
              $1:campaign\_id::STRING,
              $1:campaign_name::STRING,
              $1:message\_variation\_id::STRING,
              $1:canvas\_id::STRING,
              $1:canvas_name::STRING,
              $1:canvas\_variation\_id::STRING,
              $1:canvas\_step\_id::STRING,
              $1:canvas\_step\_message\_variation\_id::STRING,
              $1:platform::STRING,
              $1:os\_version::STRING,
              $1:device\_model::STRING,
              $1:send\_id::STRING,
              $1:device\_id::STRING,
              $1:button\_action\_type::STRING,
              $1:button\_string::STRING

              FROM
@currents.public.braze\_data/currents/dataexport.prod-01.S3.integration.INTEGRATION_ID_GOES_HERE/event_type=users.messages.pushnotification.Open/);
\`\`\`

最後に、`show pipes;` コマンドを使用して SQS 情報を表示します。このパイプは自動取り込みパイプとして作成されたため、SQS キューの名前は `NOTIFICATION_CHANNEL` という新しい列に表示されます。

#### ステップ 2: バケットイベントの作成

AWSで、新しい Snowflake ステージの対応するバケットに移動します。次に、[**プロパティ**] タブの [**イベント**] に移動します。

![AWS の [プロパティ] タブ][1]{: height="50%" width="50%"}

必要に応じて、Currents データの各セット ([メッセージング]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/message_engagement_events/)、[ユーザー行動]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/customer_behavior_events/))、またはその両方に対して新規イベントを作成します。

![AWS での新規イベントの作成][2]{: height="50%" width="50%"}

オブジェクト作成通知のチェックボックスをオンにして、フォーム下部の ARN (Snowflake の通知チャンネル列) を確認します。

### 自動取り込み Snowpipe の設定{#auto-ingest-snowpipes}

AWS SQS の構成で正しいテーブルが生成されるようにするには、[メッセージエンゲージメントイベントまたはメッセージングイベント]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/message_engagement_events/)、[ユーザー行動イベントまたは顧客行動イベント]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/customer_behavior_events/)、あるいはその両方について、以下の例と Currents ドキュメントで決定されているスキーマを使用して、受信データの構造を適切に定義する必要があります。

Braze Currents は特定のデータ型を持つ特定のフィールドを介して継続的にデータをテーブルに読み込むため、Braze Currents のスキーマに従ってテーブルを構成することが重要です。例えば、`user_id` は文字列として読み込まれ、Currents データでは `user_id` と呼ばれます。

{% alert note %}
  Currents 連携によっては、設定が必要なイベント ([メッセージエンゲージメントイベントやメッセージングイベント]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/message_engagement_events/)、[ユーザー行動イベントや顧客行動イベントなど]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/customer_behavior_events/)) が異なる場合があります。このプロセスの一部または全部のスクリプトを作成することもできます。
{% endalert %}

{% tabs %}
  {% tab User Behavior Events %}

まず、Currents スキーマから次の構造を使用して、継続的に読み込むテーブル `INTO` を作成します。

```sql
CREATE TABLE
  users_behaviors_app_firstsession (
        id               STRING,
        user_id          STRING,
        external_user_id STRING,
        app_id           STRING,
        time             INT,
        session_id       STRING,
        gender           STRING,
        country          STRING,
        timezone         STRING,
        language         STRING,
        device_id        STRING,
        sdk_version      STRING,
        platform         STRING,
        os_version       STRING,
        device_model     STRING
    );
```

次に、`auto_ingest` パイプを作成し、以下の項目を指定します。
1\.読み込み先のテーブル
2. 以下のテーブルに読み込む方法

\`\`\`sql
CREATE OR REPLACE PIPE
  pipe\_users\_behaviors\_app\_firstsession
    auto\_ingest=true AS

COPY INTO
  users\_behaviors\_app\_firstsession
          FROM
            (SELECT
              $1:id::STRING,
              $1:user\_id::STRING,
              $1:external\_user\_id::STRING,
              $1:app\_id::STRING,
              $1:time::INT,
              $1:session\_id::STRING,
              $1:gender::STRING,
              $1:country::STRING,
              $1:timezone::STRING,
              $1:language::STRING,
              $1:device\_id::STRING,
              $1:sdk\_version::STRING,
              $1:platform::STRING,
              $1:os\_version::STRING,
              $1:device\_model::STRING

              FROM
@currents.public.braze\_data/currents/dataexport.prod-01.S3.integration.INTEGRATION_ID_GOES_HERE/event_type=users.behaviors.app.FirstSession/);
\`\`\`

{% alert warning %}
すべてのイベントタイプについて、`CREATE TABLE` コマンドと `CREATE PIPE` コマンドを繰り返す必要があります。
{% endalert %}

 {% endtab %}
 {% tab Messaging Events %}

まず、Currents スキーマから次の構造を使用して、継続的に読み込むテーブル `INTO` を作成します。

```sql
CREATE TABLE
    public_users_messages_pushnotification_open (
        id STRING,
        user_id STRING,
        external_user_id STRING,
        time INT,
        timezone STRING,
        app_id STRING,
        campaign_id STRING,
        campaign_name STRING,
        message_variation_id STRING,
        canvas_id STRING,
        canvas_name STRING,
        canvas_variation_id STRING,
        canvas_step_id STRING,
        canvas_step_message_variation_id STRING,
        platform STRING,
        os_version STRING,
        device_model STRING,
        send_id STRING,
        device_id STRING,
        button_action_type STRING,
        button_string STRING
        );
```

次に、AUTO 連続読み込みパイプを作成し、以下の項目を指定します。
1\.読み込み先のテーブル
2. 以下のテーブルに読み込む方法

\`\`\`sql
CREATE OR REPLACE PIPE
  pipe\_users\_messages\_pushnotification\_open
    auto\_ingest=true AS

COPY INTO
  users\_messages\_pushnotification\_open
          FROM
           (SELECT
             $1:id::STRING,
             $1:user\_id::STRING,
             $1:external\_user\_id::STRING,
              $1:time::INT,
              $1:timezone::STRING,
              $1:app\_id::STRING,
              $1:campaign\_id::STRING,
              $1:campaign_name::STRING,
              $1:message\_variation\_id::STRING,
              $1:canvas\_id::STRING,
              $1:canvas_name::STRING,
              $1:canvas\_variation\_id::STRING,
              $1:canvas\_step\_id::STRING,
              $1:canvas\_step\_message\_variation\_id::STRING,
              $1:platform::STRING,
              $1:os\_version::STRING,
              $1:device\_model::STRING,
              $1:send\_id::STRING,
              $1:device\_id::STRING,
              $1:button\_action\_type::STRING,
              $1:button\_string::STRING

              FROM
@currents.public.braze\_data/currents/dataexport.prod-01.S3.integration.INTEGRATION_ID_GOES_HERE/event_type=users.messages.pushnotification.Open/);
\`\`\`

{% alert warning %}
すべてのイベントタイプについて、`CREATE TABLE` コマンドと `CREATE PIPE` コマンドを繰り返す必要があります。
{% endalert %}

  {% endtab %}
{% endtabs %}

Braze Currents を使用して実行できる分析のタイプについては、「[Looker Blocks](https://github.com/llooker?q=braze)」を参照してください。

{% alert note %}
質問がある場合や、Braze によるこのプロセスのガイドに興味がある場合は、Braze のアカウントマネージャーにお問い合わせください。
{% endalert %}

[1]: {% image_buster /assets/img/aws-properties.png %}
[2]: {% image_buster /assets/img/aws-events.png %}
