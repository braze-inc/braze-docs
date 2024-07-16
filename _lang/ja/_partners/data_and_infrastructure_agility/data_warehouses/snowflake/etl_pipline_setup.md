---
nav_title: 「ETLイベント・パイプラインのセットアップ」
article_title:Snowflake ETL イベントパイプラインのセットアップ
page_order:2
description:「このパートナーページには、独自のクエリを設定するときに参照できるメールクリッククエリの設定例が掲載されています。「
page_type: partner
search_tag:Partner

---

# ETL イベントパイプラインのセットアップ

> このパートナーページには、独自のクエリを設定する際に参照できるメールクリッククエリの設定例が掲載されています。

このメールクリッククエリを使用して、Brazeキャンペーンとキャンバス内の特定のメールとのインタラクションを分析できます。

## このクエリをセットアップ

`BRAZE_CURRENTS;`次のデータベースを作成し`BRAZE`、データベースが存在しない場合は作成します。

```sql
use schema BRAZE_CURRENTS.public;

create or replace stage braze_currents.public.braze_data
url='s3://tl-braze/'
credentials = (AWS_KEY_ID = 'XXXXXXXXX' AWS_SECRET_KEY = 'YYYYYY' );

create file format braze_currents.public.currents_avro type = 'avro' compression = 'auto';

alter stage braze_currents.public.braze_data set file_format = braze_currents.public.currents_avro;

show stages;
```

次のコマンドを使用してテーブルを作成します。

```sql
CREATE TABLE
  braze_currents.public.users_messages_email_click (
    id STRING,
    user_id STRING,
    external_user_id STRING,
    time INT,
    timezone STRING,
    campaign_id STRING,
    campaign_name STRING,
    message_variation_id STRING,
    canvas_id STRING,
    canvas_name STRING,
    canvas_variation_id STRING,
    canvas_step_id STRING,
    send_id STRING,
    dispatch_id STRING,
    email_address STRING,
    url STRING,
    sending_ip STRING,
    user_agent STRING
  );
```

次のコマンドを使用してパイプを作成または置換します。

```sql
CREATE OR REPLACE PIPE
  pipe_users_messages_email_click
    auto_ingest=true AS

COPY INTO
  braze_currents.public.users_messages_email_click
  FROM
  (select
    $1:id::STRING,
    $1:user_id::STRING,
    $1:external_user_id::STRING,
    $1:time::INT,
    $1:timezone::STRING,
    $1:campaign_id::STRING,
    $1:campaign_name::STRING,
    $1:message_variation_id::STRING,
    $1:canvas_id::STRING,
    $1:canvas_name::STRING,
    $1:canvas_variation_id::STRING,
    $1:canvas_step_id::STRING,
    $1:send_id::STRING,
    $1:dispatch_id::STRING,
    $1:email_address::STRING,
    $1:url::STRING,
    $1:sending_ip::STRING,
    $1:user_agent::STRING

    FROM
    @braze_currents.public.braze_data/currents/dataexport.prod-03.S3.integration.YOUR_INTEGRATION_ID_HERE/event_type=users.messages.email.click/);

show pipes;
```

## このクエリ例をさらに活用してください

`notification_channel`前のコマンドの出力からをコピーし、S3 バケット通知を設定するときに使用します。

指定された次のパイプ名について、S3からSnowflakeに手動で同期します。
```sql
ALTER PIPE
  pipe_users_messages_email_click
  refresh ;
```

パイプステータス確認します。メッセージが S3 から Snowflakeにいつ転送されたかがわかります。
```sql
SELECT
  SYSTEM$PIPE_STATUS(
    'pipe_users_messages_email_click'
  )
```

最後に、`*`次の中から選択してテーブルのコピー履歴を表示します。
```sql
table(braze_currents.information_schema.copy_history(table_name=>'users_messages_email_click', start_time=> dateadd(hours, -1, current_timestamp())));
```