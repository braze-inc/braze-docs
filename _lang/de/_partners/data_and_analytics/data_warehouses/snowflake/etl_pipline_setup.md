---
nav_title: "ETL Ereignis-Pipeline einrichten"
article_title: Snowflake ETL Ereignis-Pipeline einrichten
page_order: 2
description: "Auf dieser Partnerseite finden Sie ein Beispiel für die Einrichtung einer E-Mail-Klick-Abfrage, auf das Sie bei der Einrichtung Ihrer eigenen Abfragen referenzieren können."
page_type: partner
search_tag: Partner

---

# ETL Ereignis-Pipeline einrichten

> Auf dieser Partnerseite finden Sie ein Beispiel für die Einrichtung einer E-Mail-Klick-Abfrage, auf das Sie bei der Einrichtung Ihrer eigenen Abfragen referenzieren können.

Sie können diese Abfrage für E-Mail-Klicks verwenden, um die Interaktionen mit bestimmten E-Mails in Ihren Kampagnen und Canvase von Braze zu analysieren.

## Richten Sie diese Abfrage ein

Erstellen Sie eine Datenbank für `BRAZE`, dann erstellen Sie eine Datenbank für `BRAZE_CURRENTS;`, falls keine existiert:

```sql
use schema BRAZE_CURRENTS.public;

create or replace stage braze_currents.public.braze_data
url='s3://tl-braze/'
credentials = (AWS_KEY_ID = 'XXXXXXXXX' AWS_SECRET_KEY = 'YYYYYY' );

create file format braze_currents.public.currents_avro type = 'avro' compression = 'auto';

alter stage braze_currents.public.braze_data set file_format = braze_currents.public.currents_avro;

show stages;
```

Verwenden Sie den folgenden Befehl, um Ihre Tabelle zu erstellen:

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

Verwenden Sie den folgenden Befehl, um Ihre Pipe zu erstellen oder zu ersetzen:

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

## Machen Sie mehr mit diesem Abfragebeispiel

Kopieren Sie die `notification_channel` aus der Ausgabe des vorangegangenen Befehls und verwenden Sie diese bei der Konfiguration von S3-Bucket-Benachrichtigungen.

Manuelle Synchronisierung von S3 zu Snowflake für den folgenden angegebenen Pipe-Namen:
```sql
ALTER PIPE
  pipe_users_messages_email_click
  refresh ;
```

Prüfen Sie den Pipe-Status, der anzeigt, wann die Nachricht von S3 an Snowflake weitergeleitet wurde:
```sql
SELECT
  SYSTEM$PIPE_STATUS(
    'pipe_users_messages_email_click'
  )
```

Zeigen Sie schließlich den Verlauf des Kopierens der Tabelle an, indem Sie `*` auswählen:
```sql
table(braze_currents.information_schema.copy_history(table_name=>'users_messages_email_click', start_time=> dateadd(hours, -1, current_timestamp())));
```