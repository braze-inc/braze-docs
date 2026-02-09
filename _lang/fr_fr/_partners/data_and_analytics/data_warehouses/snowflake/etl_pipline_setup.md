---
nav_title: "Configuration du pipeline d'événements ETL"
article_title: "Configuration du pipeline d'événements ETL Snowflake"
page_order: 2
description: "Cette page partenaire propose un exemple de configuration d'une requête de clics d'e-mail à consulter lors de la configuration de vos propres requêtes."
page_type: partner
search_tag: Partner

---

# Configuration du pipeline d'événements ETL

> Cette page partenaire propose un exemple de configuration d'une requête de clics d'e-mail à laquelle vous pouvez vous référer lorsque vous configurez vos propres requêtes.

Vous pouvez utiliser cette requête de clics sur les e-mails pour analyser les interactions avec des e-mails spécifiques dans vos campagnes et canevas Braze.

## Créez cette requête

Créez une base de données pour `BRAZE`, puis créez une base de données si elle n'existe pas pour `BRAZE_CURRENTS;` :

```sql
use schema BRAZE_CURRENTS.public;

create or replace stage braze_currents.public.braze_data
url='s3://tl-braze/'
credentials = (AWS_KEY_ID = 'XXXXXXXXX' AWS_SECRET_KEY = 'YYYYYY' );

create file format braze_currents.public.currents_avro type = 'avro' compression = 'auto';

alter stage braze_currents.public.braze_data set file_format = braze_currents.public.currents_avro;

show stages;
```

Utilisez la commande suivante pour créer votre tableau :

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

Utilisez la commande suivante pour créer ou remplacer votre pipeline :

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

## Faites-en plus avec cet exemple de requête

Copiez le paramètre `notification_channel` à partir de la sortie de la commande précédente et utilisez-le lors de la configuration des notifications de compartiment S3.

Synchronisez manuellement S3 vers Snowflake pour le nom de pipeline suivant donné :
```sql
ALTER PIPE
  pipe_users_messages_email_click
  refresh ;
```

Vérifiez l’état du pipeline, qui indiquera quand le message a été transmis de S3 à Snowflake :
```sql
SELECT
  SYSTEM$PIPE_STATUS(
    'pipe_users_messages_email_click'
  )
```

Enfin, affichez l'historique des copies de la table en sélectionnant `*` depuis :
```sql
table(braze_currents.information_schema.copy_history(table_name=>'users_messages_email_click', start_time=> dateadd(hours, -1, current_timestamp())));
```