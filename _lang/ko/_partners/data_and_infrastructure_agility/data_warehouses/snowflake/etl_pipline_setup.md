---
nav_title: "ETL 이벤트 파이프라인 설정"
article_title: Snowflake ETL 이벤트 파이프라인 설정
page_order: 2
description: "이 파트너 페이지에서는 자체 쿼리를 설정할 때 참조할 수 있는 이메일 클릭 쿼리 설정 예제를 제공합니다."
page_type: partner
search_tag: Partner

---

# ETL 이벤트 파이프라인 설정

> 이 파트너 페이지에서는 자체 쿼리를 설정할 때 참조할 수 있는 이메일 클릭 쿼리 설정 예제를 제공합니다.

이 이메일 클릭 쿼리를 사용하여 Braze 캠페인 및 캔버스에서 특정 이메일과의 상호 작용을 분석할 수 있습니다.

## 이 쿼리 설정

`BRAZE`에 대한 데이터베이스를 생성한 다음, `BRAZE_CURRENTS;`에 대한 데이터베이스가 없는 경우 데이터베이스를 생성합니다.

```sql
use schema BRAZE_CURRENTS.public;

create or replace stage braze_currents.public.braze_data
url='s3://tl-braze/'
credentials = (AWS_KEY_ID = 'XXXXXXXXX' AWS_SECRET_KEY = 'YYYYYY' );

create file format braze_currents.public.currents_avro type = 'avro' compression = 'auto';

alter stage braze_currents.public.braze_data set file_format = braze_currents.public.currents_avro;

show stages;
```

다음 명령을 사용하여 테이블을 생성합니다:

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

다음 명령을 사용하여 파이프를 만들거나 바꾸세요:

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

## 이 쿼리 예제로 더 많은 작업을 수행하세요.

이전 명령의 출력에서 `notification_channel`을 복사하여 S3 버킷 알림을 구성할 때 이를 사용합니다.

주어진 다음 파이프 이름에 대해 S3에서 Snowflake로 수동으로 동기화합니다:
```sql
ALTER PIPE
  pipe_users_messages_email_click
  refresh ;
```

파이프 상태를 확인하면 메시지가 S3에서 Snowflake로 전달된 시점이 표시됩니다.
```sql
SELECT
  SYSTEM$PIPE_STATUS(
    'pipe_users_messages_email_click'
  )
```

마지막으로, `*`를 선택하여 표의 복사 기록을 표시합니다.
```sql
table(braze_currents.information_schema.copy_history(table_name=>'users_messages_email_click', start_time=> dateadd(hours, -1, current_timestamp())));
```