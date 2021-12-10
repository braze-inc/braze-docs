---
nav_title: "Configuration du pipeline ETL Event"
article_title: Configuration du pipeline d'événement Snowflake ETL
page_order: 2
description: "Cette page partenaire offre un exemple de mise en place d'une requête Email Clicks à référencer lors de la configuration de vos propres requêtes."
page_type: partenaire
search_tag: Partenaire
---

# Configuration du pipeline d'événement ETL

> Cette page partenaire offre un exemple de mise en place d'une requête Email Clicks à référencer lors de la configuration de vos propres requêtes.

Vous pouvez utiliser cette requête de clics de courriel pour analyser les interactions avec des e-mails spécifiques dans vos campagnes Braze et Canvases.

## Configurer cette requête

Créer une base de données pour `BRAZE`, puis créer une base de données si aucune n'existe pour `BRAZE_CURRENTS ;`:

```sql
utiliser le schéma BRAZE_CURRENTS.public;

créer ou remplacer stage braze_currents.public. raze_data
url='s3://tl-braze/'
identifiants = (AWS_KEY_ID = 'XXXXXXXXX' AWS_SECRET_KEY = 'YYYYYY' );

créer un format de fichier brise_currents. ublic.currents_avro type = 'avro' compression = 'auto';

alter stage braze_currents.public.braze_data set file_format = braze_currents.public.currents_avro;

show stages;
```

_Utilisez la commande suivante pour créer votre table:_

```sql
CRÉER UN TABLE
  braze_currents.public. sers_messages_email_click (
    id STRING,
    user_id STRING,
    external_user_id STRING,
    heure INT,
    fuseau horaire STRING,
    campaign_id STRING,
    campaign_name STRING,
    message_variation_id STRING,
    CANvas_id STRING,
    STRING,
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

_Utilisez la commande suivante pour créer ou remplacer votre tube :_

```sql
CRÉER OU REMPLACER UNE PIPE
  pipe_users_messages_email_click
    auto_ingest=true COMME

COPY INTO
  braze_currents.public. sers_messages_email_clic
  À partir de
  (sélectionnez
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
    @braze_currents. ublic.braze_data/currents/dataexport.prod-03.S3.integration.YOUR_INTEGRATION_ID_HERE/event_type=users.messages.email.click/);

montrer des tuyaux ;
```

## Faites plus avec cet exemple de requête

Copiez la `notification_channel` depuis la sortie de la commande ci-dessus et utilisez-la lors de la configuration des notifications S3.

Synchronisation manuelle de S3 vers Snowflake pour le nom du tube donné ci-dessous:

```sql
ALTER PIPE
  pipe_users_messages_email_click
  rafraîchir ;
```

Vérifiez l'état du tuyau qui s'affichera lorsque le message a été transmis de S3 à Snowflake.

```sql
SELECTIONNEZ
  SYSTEM$PIPE_STATUS(
    'pipe_users_messages_email_click'
)
```

Enfin, afficher l'historique de la copie de la table en sélectionnant `*` de

```sql
table(braze_currents.information_schema.copy_history(table_name=>'users_messages_email_click', start_time=> dateadd(hours, -1, current_timestamp())));
```