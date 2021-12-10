---
nav_title: Transférer des données depuis Amazon S3 vers Snowflake
article_title: Transférer des données depuis Amazon S3 vers Snowflake
page_order: 7
page_type: tutoriel
description: "Cet article vous guidera à travers le transfert de données depuis le stockage cloud (comme Amazon S3) vers un entrepôt (comme Snowflake) en utilisant le processus ETL."
tool: Courants
---

# Transférer des données depuis Amazon S3 vers Snowflake

> Si vos données sont actuellement installées dans Amazon S3, vous pouvez le transférer vers Snowflake ou un autre entrepôt de données relationnelles en utilisant le processus ELT (Extract Load Transform).

{% alert note %}
Si vous avez des cas d'utilisation plus spécifiques et que vous souhaitez que Braze serve votre instance de Devises, contactez votre gestionnaire de compte Braze et demandez-leur des services professionnels de Braze Data.
{% endalert %}

## Processus de charge automatisé

Ce processus de chargement automatisé déplace les données dans [Snowflake](https://www.snowflake.com/), qui vous permettra d'utiliser les [Braze Looker Blocks](https://looker.com/platform/blocks/directory?utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct#braze) pour visualiser ces données dans Looker afin d'aider à recueillir des informations et des commentaires dans vos campagnes, Canvases, et Segments.

Une fois que vous avez des courants d'exportation S3 configurés et que vous recevez des données d'événements en direct, il est temps de configurer votre pipeline live ELT en Snowflake en configurant les composants suivants :

-   [Queues AWS SQS](#aws-sqs-queues)
-   [Motoneiges automatiques](#auto-ingest-snowpipes)

### Queues AWS SQS

**Les Snowpipes auto-ingest** dépendent des files d'attente SQS pour envoyer des notifications de S3 à Snowpipe. Ce processus est géré par Snowflake après la configuration de SQS.

#### Configurer l'étape S3 externe

{% alert note %}
Les tables de votre base de données sont créées à partir de cette étape.
{% endalert %}

Lorsque vous configurez des courants au Brésil, spécifiez un chemin de dossier à suivre dans votre compartiment S3. Ici, nous utilisons `courants`, le chemin du dossier par défaut.

Dans AWS, créez une nouvelle **paire de clés publiques privées** pour le compartiment S3 désiré, avec des subventions en fonction des exigences de sécurité de votre organisation.

Puis, dans Snowflake, créez une base de données et un schéma de votre choix (nommé `courants` et `public` dans l'exemple ci-dessous).

Ensuite, créez un Snowflake S3 Stage (appelé `braze_data` ci-dessous) :

```sql
CRÉER OU REMPLACER DES STAGES
    currents.public.braze_data
    url='s3://snowpipe-demo/'
    identifiants = (AWS_KEY_ID = '...' AWS_SECRET_KEY = '...' );
affiche les étapes;
```

Ensuite, définissez le format de fichier AVRO pour votre scène.

```sql
CRÉER UN FORMAT DE FICHIER
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
CRÉER OU REMPLACER
  pipe_users_messages_pushnotification_open
    auto_ingest=true COMME

COPY INTO
  users_messages_pushnotification_open
          À partir de
           (SELECT
             $1:id::STRING,
             $1:user_id::STRING,
             $1:external_user_id::STRING,
              $1:time::INT,
              $1:fuseau horaire::STRING,
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
@currents. ublic.braze_data/currents/dataexport.prod-01.S3.integration.INTEGRATION_ID_GOES_HERE/event_type=users.messages.pushnotification.Open/);
```

Enfin, utilisez la commande `afficher les tubes ;` pour afficher vos informations SQS. Le nom de la file d'attente SQS sera visible dans une nouvelle colonne appelée `NOTIFICATION_CHANNEL` depuis que ce pipe a été créé comme un tuyau auto-ingest.

#### Créer des événements de bucket

Dans AWS, accédez au seau correspondant de la nouvelle étape du flocon de neige. Puis, sous l'onglet **Propriétés** , allez à **Événements**.

!\[Propriétés AWS\]\[1\]{: height="50%" width="50%"}

Dans **Événements**, créez de nouveaux événements pour chaque ensemble de données courantes, au besoin ([Messaging]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/message_engagement_events/) et/ou [comportement utilisateur]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/customer_behavior_events/)).

!\[Evénements AWS\]\[2\]{: height="50%" width="50%"}

Cochez la case appropriée pour les notifications de création d'objet, ainsi que le ARN en bas du formulaire (à partir de la colonne du canal de notification dans Snowflake).

### Configuration de Snowpipe

Afin que la configuration ci-dessus produise les bonnes tables, vous devez définir la structure des données entrantes correctement en utilisant les exemples ci-dessous et les structures déterminées dans notre documentation [Message Engagement ou Messaging Events]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/message_engagement_events/) et/ou [User ou Customer Behavior Events]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/customer_behavior_events/) Courants.

Il est essentiel que vos tables soient structurées selon les schémas des courants de Braze, car les courants de Braze chargeront en permanence les données via des champs spécifiques avec des types de données spécifiques (un `user_id` sera toujours chargé comme une chaîne de caractères et appelé un `user_id` dans les données des courants).

{% alert note %}
  Selon votre intégration de Courants, vous pouvez avoir des événements différents que vous devez configurer ([Message Engagement ou Messaging Events]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/message_engagement_events/), [Evénements de comportement utilisateur ou client]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/customer_behavior_events/), ou les deux).  Vous pouvez également écrire un script pour une partie ou la totalité de ce processus.
{% endalert %}

{% tabs %}
  {% tab User Behavior Events %}

Tout d'abord, créez une table `INTO` que nous allons charger en continu en utilisant la structure suivante du schéma courant :

```sql
CREATE TABLE
  users_behaviors_app_firstsession (
        id STRING,
        user_id STRING, 

        external_user_id STRING,
        STRING de l'app_id
        temps INT,
        session_id STRING,
        SÉCURITÉ,
        pays STRING,
        Fuseau horaire STRING,
        langue STRING,
        appareil_id STRING,
        Sdk_version STRING,
        plateforme STRING,
        os_version STRING,
        device_model STRING
);
```

Ensuite, créez le tuyau `auto_ingest` et spécifiez
1. Quelle table à charger, et
2. Comment charger la table suivante.

```sql
CRÉER OU REMPLACER UNE PIPE
  pipe_users_behaviors_app_firstsession
    auto_ingest=true COMME

COPY INTO
  utilisateurs_behaviors_app_firstsession
          À partir de
            (SELECT
              $1:id::STRING,
              $1:user_id::STRING,
              $1:external_user_id::STRING,
              $1:app_id::STRING,
              $1:time::INT,
              $1:session_id::STRING,
              $1:gender::STRING,
              $1:country::STRING,
              $1:fuseau horaire::STRING,
              $1:language::STRING,
              $1:device_id::STRING,
              $1:sdk_version::STRING,
              $1:platform::STRING,
              $1:os_version::STRING,
              $1:device_model::STRING

              FROM
@currents. ublic.braze_data/currents/dataexport.prod-01.S3.integration.INTEGRATION_ID_GOES_HERE/event_type=users.behaviors.app.FirstSession/);
```

{% alert warning %}
Vous devez répéter les commandes `CREATE TABLE` et `CREATE PIPE` pour chaque type d'événement.
{% endalert %}

 {% endtab %}
 {% tab Messaging Events %}

Tout d'abord, créez une table `INTO` que nous chargerons continuellement en utilisant la structure suivante :

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

Ensuite, créez le tube de charge continue AUTO et spécifiez 1\. quelle table à charger et 2\. comment charger la table suivante.

```sql
CRÉER OU REMPLACER
  pipe_users_messages_pushnotification_open
    auto_ingest=true COMME

COPY INTO
  users_messages_pushnotification_open
          À partir de
           (SELECT
             $1:id::STRING,
             $1:user_id::STRING,
             $1:external_user_id::STRING,
              $1:time::INT,
              $1:fuseau horaire::STRING,
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
@currents. ublic.braze_data/currents/dataexport.prod-01.S3.integration.INTEGRATION_ID_GOES_HERE/event_type=users.messages.pushnotification.Open/);
```

{% alert warning %}
Vous devez répéter les commandes `CREATE TABLE` et `CREATE PIPE` pour chaque type d'événement.
{% endalert %}

  {% endtab %}
{% endtabs %}

Pour voir les types d'analyses que vous pouvez effectuer en utilisant des courants de Braze, veuillez consulter [notre Looker Blocks](https://github.com/llooker?q=braze).

{% alert note %}
Contactez votre gestionnaire de compte Braze si vous avez des questions ou si vous souhaitez que Braze vous guide tout au long de ce processus.
{% endalert %}
[1]: {% image_buster /assets/img/aws-properties.png %} [2]: {% image_buster /assets/img/aws-events.png %}
