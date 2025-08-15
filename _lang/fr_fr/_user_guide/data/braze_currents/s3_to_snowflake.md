---
nav_title: Transférer des données d’Amazon S3 vers Snowflake
article_title: Transférer des données d’Amazon S3 vers Snowflake
page_order: 7
page_type: tutorial
description: "Cet article « how-to » vous explique comment transférer des données d’un stockage cloud (comme Amazon S3) vers un entrepôt (comme Snowflake) en utilisant le processus ETL."
tool: Currents

---

# Transférer des données d’Amazon S3 vers Snowflake

> Si vos données se trouvent actuellement dans Amazon S3, vous pouvez les transférer vers Snowflake ou un autre entrepôt de données relationnel à l'aide du processus d'extraction, de chargement et de transformation (ETL). Cette page vous explique comment procéder.

{% alert note %}
Si vous avez des cas d’utilisation plus spécifiques et souhaitez que Braze serve votre instance Currents, contactez votre gestionnaire de compte Braze et demandez-leur les services de données de Braze Data Professional Services.
{% endalert %}

## Fonctionnement

Le processus d'extraction, de chargement et de transformation (ETL) est un processus automatisé qui déplace les données dans [Snowflake](https://www.snowflake.com/), ce qui vous permettra d'utiliser les [blocs Looker](https://marketplace.looker.com/marketplace/directory) de Braze pour visualiser ces données dans Looker afin d'aider à générer des informations et des retours dans vos campagnes, Canvases et segments.

Une fois que vous avez configuré une exportation Currents vers S3 et que vous recevez des données d'événements en direct, vous pouvez configurer votre pipeline ELT en direct dans Snowflake en configurant les composants suivants :

-   [Fiches d'attente AWS SQS](#aws-sqs-queues)
-   [Auto-Ingest Snowpipes](#auto-ingest-snowpipes)

## Configuration des files d'attente AWS SQS

Les **snowpipes Auto-ingest** s'appuient sur les files d'attente SQS pour envoyer les notifications de S3 à Snowpipe. Ce processus est géré par Snowflake après avoir configuré SQS.

### Étape 1 : Configurer l’étage S3 externe

{% alert note %}
Les tables de votre base de données sont créées à ce stade.
{% endalert %}

1. Lorsque vous configurez Braze Currents, spécifiez un chemin de dossier pour vos fichiers Currents dans votre compartiment S3. Nous utilisons ici ```currents```, le chemin de dossier par défaut.

2. Créez les éléments suivants dans l'ordre indiqué :
  Dans AWS, créez une nouvelle **paire de clés publique-privée** pour le compartiment S3 souhaité, avec des subventions conformes aux exigences de sécurité de votre organisation.
  2.2. Dans Snowflake, créez une base de données et un schéma de votre choix (nommés ```currents``` et ```public``` dans l'exemple suivant).
  2.3. Créez une zone de préparation S3 Snowflake (appelée `braze_data`) :

```sql
CREATE OR REPLACE STAGE
    currents.public.braze_data
    url='s3://snowpipe-demo/'
    credentials = (AWS_KEY_ID = '...' AWS_SECRET_KEY = '...' );
show stages;
```

{: start="3"}
3\. Définissez ensuite le format de fichier AVRO pour votre stage.

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

```sql
CREATE OR REPLACE PIPE
  pipe_users_messages_pushnotification_open
    auto_ingest=true AS

COPY INTO
  users_messages_pushnotification_open
          FROM
           (SELECT
             $1:id::STRING,
             $1:user_id::STRING,
             $1:external_user_id::STRING,
              $1:time::INT,
              $1:timezone::STRING,
              $1:app_id::STRING,
              $1:campaign_id::STRING,
              $1:campaign_name::STRING,
              $1:message_variation_id::STRING,
              $1:canvas_id::STRING,
              $1:canvas_name::STRING,
              $1:canvas_variation_id::STRING,
              $1:canvas_step_id::STRING,
              $1:canvas_step_message_variation_id::STRING,
              $1:platform::STRING,
              $1:os_version::STRING,
              $1:device_model::STRING,
              $1:send_id::STRING,
              $1:device_id::STRING,
              $1:button_action_type::STRING,
              $1:button_string::STRING

              FROM
@currents.public.braze_data/currents/dataexport.prod-01.S3.integration.INTEGRATION_ID_GOES_HERE/event_type=users.messages.pushnotification.Open/);
```

{: start="4"}
4\. Enfin, utilisez la commande `show pipes;`pour afficher vos informations SQS. Le nom de la file d'attente SQS sera visible dans une nouvelle colonne appelée `NOTIFICATION_CHANNEL`, car ce canal a été créé en tant que canal à ingestion automatique.

### Étape 2 : Créer des événements de compartiment

1. Dans AWS, naviguez jusqu’au compartiment correspondant au nouveau stage Snowflake. Ensuite, sous l'onglet **Propriétés**, allez dans **Événements**.

![Onglet Propriétés AWS]({% image_buster /assets/img/aws-properties.png %}){: height="50%" width="50%"}

{: start="2"}
2\. Créez de nouveaux événements pour chaque ensemble de données actuelles, selon les besoins[(envoi de messages]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/), [comportement de l'utilisateur]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/)), ou les deux.

![Création d'un nouvel événement dans AWS]({% image_buster /assets/img/aws-events.png %}){: height="50%" width="50%"}

{: start="3"}
3\. Cochez la case appropriée pour l’objet Créer des notifications, ainsi que l’ARN au bas du formulaire (dans la colonne de canal de notification dans Snowflake).

## Configuration des Snowpipes à ingestion automatique {#auto-ingest-snowpipes}

Pour que la configuration AWS SQS produise les bonnes tables, vous devez définir correctement la structure des données entrantes en utilisant les exemples suivants et les schémas déterminés dans notre documentation Currents pour les [événements d'engagement ou de messages]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/), les [événements de comportement des utilisateurs ou des clients]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/), ou les deux.

Il est essentiel de structurer vos tables conformément aux schémas de Braze Currents, car Braze Currents y chargera continuellement des données par le biais de champs spécifiques avec des types de données spécifiques. Par exemple, un `user_id` sera chargé sous forme de chaîne de caractères et appelé `user_id` dans les données de Currents.

{% alert note %}
  En fonction de votre intégration Currents, vous pouvez avoir différents événements que vous devez configurer (tels que les [événements d'engagement ou d'envoi de messages]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) et les [événements de comportement utilisateur ou client]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/)). Vous pouvez également écrire un script pour tout ou partie de ce processus.
{% endalert %}

{% tabs %}
  {% tab Événements liés au comportement de l'utilisateur %}

1. Créez une table `INTO` dans laquelle nous allons continuellement charger des données, en utilisant la structure de schéma Currents suivante :

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

{: start="2"}
2\. Créez le canal `auto_ingest` et spécifiez :
  2.1. Quel tableau charger
  2.2 Comment charger le tableau suivant

```sql
CREATE OR REPLACE PIPE
  pipe_users_behaviors_app_firstsession
    auto_ingest=true AS

COPY INTO
  users_behaviors_app_firstsession
          FROM
            (SELECT
              $1:id::STRING,
              $1:user_id::STRING,
              $1:external_user_id::STRING,
              $1:app_id::STRING,
              $1:time::INT,
              $1:session_id::STRING,
              $1:gender::STRING,
              $1:country::STRING,
              $1:timezone::STRING,
              $1:language::STRING,
              $1:device_id::STRING,
              $1:sdk_version::STRING,
              $1:platform::STRING,
              $1:os_version::STRING,
              $1:device_model::STRING

              FROM
@currents.public.braze_data/currents/dataexport.prod-01.S3.integration.INTEGRATION_ID_GOES_HERE/event_type=users.behaviors.app.FirstSession/);
```

{% alert warning %}
Vous devez répéter les commandes `CREATE TABLE` et `CREATE PIPE` pour chaque type d’événement.
{% endalert %}

 {% endtab %}
 {% tab Événements de messagerie %}

1. Créez une table `INTO` dans laquelle nous allons continuellement charger des données, en utilisant la structure de schéma Currents suivante :

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

{: start="2"}
2\. Créez le canal de charge continue AUTO et spécifiez :
  2.1. Quel tableau charger
  2.2 Comment charger le tableau suivant

```sql
CREATE OR REPLACE PIPE
  pipe_users_messages_pushnotification_open
    auto_ingest=true AS

COPY INTO
  users_messages_pushnotification_open
          FROM
           (SELECT
             $1:id::STRING,
             $1:user_id::STRING,
             $1:external_user_id::STRING,
              $1:time::INT,
              $1:timezone::STRING,
              $1:app_id::STRING,
              $1:campaign_id::STRING,
              $1:campaign_name::STRING,
              $1:message_variation_id::STRING,
              $1:canvas_id::STRING,
              $1:canvas_name::STRING,
              $1:canvas_variation_id::STRING,
              $1:canvas_step_id::STRING,
              $1:canvas_step_message_variation_id::STRING,
              $1:platform::STRING,
              $1:os_version::STRING,
              $1:device_model::STRING,
              $1:send_id::STRING,
              $1:device_id::STRING,
              $1:button_action_type::STRING,
              $1:button_string::STRING

              FROM
@currents.public.braze_data/currents/dataexport.prod-01.S3.integration.INTEGRATION_ID_GOES_HERE/event_type=users.messages.pushnotification.Open/);
```

{% alert warning %}
Vous devez répéter les commandes `CREATE TABLE` et `CREATE PIPE` pour chaque type d’événement.
{% endalert %}

  {% endtab %}
{% endtabs %}

Pour voir les types d'analyses que vous pouvez effectuer à l'aide de Braze Currents, consultez nos [blocs Looker](https://github.com/llooker?q=braze).

{% alert note %}
Contactez votre gestionnaire de compte Braze si vous avez des questions ou si vous souhaitez que Braze vous guide dans ce processus.
{% endalert %}

