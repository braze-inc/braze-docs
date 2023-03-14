---
nav_title: Transférer des données d’Amazon S3 vers Snowflake
article_title: Transférer des données d’Amazon S3 vers Snowflake
page_order: 7
page_type: tutorial
description: "Cet article « how-to » vous explique comment transférer des données d’un stockage cloud (comme Amazon S3) vers un entrepôt (comme Snowflake) en utilisant le processus ETL."
tool: Currents

---

# Transférer des données d’Amazon S3 vers Snowflake

> Si vos données sont actuellement dans Amazon S3, vous pouvez les transférer vers Snowflake ou vers un autre entrepôt de données relationnelles en utilisant le processus ELT (Extract Load Transformation).

{% alert note %}
Si vous avez des cas d’utilisation plus spécifiques et souhaitez que Braze serve votre instance Currents, contactez votre gestionnaire de compte Braze et demandez-leur les services de données de Braze Data Professional Services.
{% endalert %}

## Processus de chargement automatisé

Ce processus de chargement automatisé déplace les données vers [Snowflake](https://www.snowflake.com/), qui vous permettra d’utiliser [les Blocs Looker de Braze](https://looker.com/platform/blocks/directory?utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct#braze) pour visualiser ces données dans Looker pour vous aider à obtenir des informations et des commentaires sur vos campagnes, Canvas et segments.

Une fois que vous avez configuré un export de Currents vers S3 et reçu des données d’événements en direct, il est temps de configurer votre pipeline ELT live dans Snowflake en configurant les composants suivants :

-   [Queues AWS SQS](#aws-sqs-queues)
-   [Auto-Ingest Snowpipe](#auto-ingest-snowpipes)

### Queues AWS SQS

**Auto-Ingest Snowpipe** utilise les files d’attente SQS pour envoyer des notifications de S3 à Snowpipe. Ce processus est géré par Snowflake après avoir configuré SQS.

#### Configurer l’étage S3 externe

{% alert note %}
Les tables de votre base de données sont créées à partir de ce stage.
{% endalert %}

Lorsque vous configurez Braze Currents, spécifiez un chemin de dossier pour vos fichiers Currents dans votre compartiment S3. Nous utilisons ici ```currents```, le chemin de dossier par défaut.

Dans AWS, créez une nouvelle **paire de clés publique-privée** pour le compartiment S3 souhaité, avec des permissions conformes aux exigences de sécurité de votre organisation.

Ensuite, dans Snowflake, créez une base de données et le schéma que vous désirez (appelés ```currents```et ```public``` dans l’exemple suivant).

Créez ensuite un Stage Snowflake S3 (appelée `braze_data`) :

```sql
CREATE OR REPLACE STAGE
    currents.public.braze_data
    url='s3://snowpipe-demo/'
    credentials = (AWS_KEY_ID = '...' AWS_SECRET_KEY = '...' );
show stages;
```

Définissez ensuite le format de fichier AVRO pour votre stage.

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

Enfin, utilisez la commande `show pipes (montrer les pipes)` pour afficher vos informations SQS. Le nom de la file d’attente SQS sera visible dans une nouvelle colonne appelée `NOTIFICATION_CHANNEL` car ce pipe a été créé comme un tuyau auto-ingéré.

#### Créer des événements de compartiment

Dans AWS, naviguez jusqu’au compartiment correspondant au nouveau stage Snowflake. Ensuite, sous l’onglet **Properties (Propriétés)**, allez sur **Events (Événements)**.

![Onglet Propriétés AWS][1]{: height="50%" width="50%"}

Dans **Événements**, créez de nouveaux événements pour chaque ensemble de données Currents, selon les besoins ([Messages]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/message_engagement_events/) et/ou [Comportement Utilisateurs]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/customer_behavior_events/)).

![Créer un nouvel événement dans AWS][2]{: height="50%" width="50%"}

Cochez la case appropriée pour l’objet Créer des notifications, ainsi que l’ARN au bas du formulaire (dans la colonne de canal de notification dans Snowflake).

### Configuration de Snowpipe

Pour que la configuration précédente produise les tableaux corrects, vous devez définir correctement la structure des données entrantes en utilisant les exemples suivants, ainsi que les structures décrites dans notre documentation Currents sur les [Événements Message ou Événements d’Engagement sur les Messages ]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/message_engagement_events/) et/ou sur les[ Événements de comportement client/Utilisateur]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/customer_behavior_events/).

Il est essentiel que vos tableaux soient structurés conformément aux schémas de Braze Currents, car Currents y chargera en continu des données dans des champs spécifiques avec des types de données spécifiques (un `user_id` sera toujours chargé comme une chaîne de caractères et appelé `user_id` dans les données Currents).

{% alert note %}
  Selon votre intégration Currents, vous pouvez avoir des événements différents à configurer ([Engagement des messages ou événements de messagerie]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/message_engagement_events/), [Événements de comportement utilisateur/client ou]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/customer_behavior_events/) les deux).  Vous pouvez également écrire un script pour tout ou partie de ce processus.
{% endalert %}

{% tabs %}
  {% tab User Behavior Events %}

Commencez par créer un tableau `INTO` dans laquelle nous allons continuellement charger des données, en utilisant la structure de schéma Currents suivante :

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

Ensuite, créez le pipe `auto_ingest` et spécifiez
1. Quel tableau doit être chargé, et
2. Comment charger le tableau suivant.

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
Vous devez répéter les commandes `CREATE TABLE (créer un tableau)` et `CREATE PIPE (créer un pipe)` pour chaque type d’événement.
{% endalert %}

 {% endtab %}
 {% tab Messaging Events %}

Commencez par créer un tableau `INTO` dans lequel nous allons continuellement charger des données, en utilisant la structure de schéma Currents suivante :

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

Créez alors un pipe de chargement en continu AUTO et spécifiez
1\. quel tableau doit être chargé, et
2\. comment charger le tableau suivant.

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
Vous devez répéter les commandes `CREATE TABLE (créer un tableau)` et `CREATE PIPE (créer un pipe)` pour chaque type d’événement.
{% endalert %}

  {% endtab %}
{% endtabs %}

Pour voir les types d’analyses que vous pouvez effectuer grâce aux currents Braze, consultez nos [Blocs Looker](https://github.com/llooker?q=braze).

{% alert note %}
Contactez votre gestionnaire de compte Braze si vous avez des questions ou si vous souhaitez que Braze vous guide dans ce processus.
{% endalert %}

[1]: {% image_buster /assets/img/aws-properties.png %}
[2]: {% image_buster /assets/img/aws-events.png %}
