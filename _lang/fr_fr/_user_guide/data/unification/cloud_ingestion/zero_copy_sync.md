---
nav_title: Personnalisation sans copie
article_title: "Personnalisation sans copie à l'aide du CDI"
page_order: 4
page_type: reference
description: "Cette page donne un aperçu de la manière de déclencher des toiles Braze à l'aide du CDI."
---

# Personnalisation sans copie à l'aide du CDI

> Découvrez comment synchroniser les déclencheurs de Canvas à l'aide de CDI pour une personnalisation sans copie. Cette fonctionnalité permet d'accéder à des informations spécifiques à l'utilisateur à partir de votre solution de stockage de données et de les transmettre à un Canvas de destination. Les étapes du canvas peuvent éventuellement inclure des champs de personnalisation qui ne sont pas conservés dans les profils utilisateurs de Braze.

{% alert important %}
Les déclencheurs CDI Canvas sont actuellement en accès anticipé. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à l'accès anticipé.
{% endalert %}

## Synchronisation des déclencheurs Canvas

### Démarrage rapide

Si vous connaissez déjà le CDI de Braze, notez que la configuration d'un déclencheur de synchronisation Canvas suit de près le processus d'[intégration de données utilisateur dans le CDI]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/), avec les mises en garde suivantes :

- Seuls les ID externes ou les alias d'utilisateurs sont pris en charge. Les e-mails et les numéros de téléphone ne sont pas des identifiants pris en charge.  
- Seuls les utilisateurs existants de Braze peuvent être synchronisés. Il n'est pas possible de créer de nouveaux utilisateurs.  
- `properties` remplace la colonne `payload`. Il s'agit d'une chaîne de caractères JSON des champs que vous souhaitez utiliser comme propriétés d'entrée dans Canvas pour la personnalisation.

Pour commencer, sélectionnez le type de données **Déclencheurs de toile** lors de la création d'une nouvelle synchronisation.

### Utilisation des déclencheurs Canvas 

#### Étape 1 : Configuration de la source de données pour les déclencheurs Canvas

{% tabs %}
{% tab Snowflake %}

##### Étape 1.1 : Configurez votre table source dans Snowflake

Vous pouvez utiliser les noms de l'exemple suivant ou choisir vos propres noms de base de données, de schéma et de table. Vous pouvez également utiliser une vue ou une vue matérialisée au lieu d'une table.  

```sql
CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
CREATE OR REPLACE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.CANVAS_TRIGGERS_SYNC (
     UPDATED_AT TIMESTAMP_NTZ(9) NOT NULL DEFAULT SYSDATE(),
     --at least one of external_id or alias_name and alias_label is required  
     EXTERNAL_ID VARCHAR(16777216),
     --if using user alias, both alias_name and alias_label are required
     ALIAS_LABEL VARCHAR(16777216),
     ALIAS_NAME VARCHAR(16777216),
     PROPERTIES VARCHAR(16777216)
);
```

Vous pouvez nommer la base de données, le schéma et la table comme vous le souhaitez, mais les noms des colonnes doivent correspondre à la définition précédente.

* `UPDATED_AT`: Heure à laquelle cette ligne a été mise à jour ou ajoutée au tableau. Seules les lignes ajoutées ou mises à jour depuis la dernière synchronisation seront synchronisées.  
* Soit `external_id`, soit `alias_name` et `alias_label` comme colonne d'identification de l'utilisateur. Ceux-ci identifient les utilisateurs pour lesquels vous souhaitez déclencher l'envoi de messages canvas.  
  * `EXTERNAL_ID`: Identifie l'utilisateur à entrer dans le Canvas. Cette valeur devrait correspondre à la valeur `external_id` utilisée dans Braze.  
  * `ALIAS_NAME` et `ALIAS_LABEL`: Ces colonnes créent un objet alias d'utilisateur. `alias_name` doit être un identifiant unique et `alias_label` spécifie le type d'alias. Les utilisateurs peuvent avoir plusieurs alias avec des libellés différents, mais un seul alias_name par `alias_label`.  
* `PROPERTIES`: Une chaîne JSON de caractères de champs à rendre disponibles en tant que propriétés de personnalisation dans votre Canvas. Elle doit contenir des informations spécifiques à l'utilisateur.

{% alert note %}
Les propriétés ne sont pas nécessaires pour chaque ligne ou chaque utilisateur. Cependant, les valeurs des propriétés doivent être des chaînes de caractères JSON valides. Saisissez une chaîne vide `{}` caractères s'il n'y a pas de propriétés pour la ligne.
{% endalert %}

##### Étape 1.2 : Créer des informations d'identification

Définissez un rôle, un entrepôt et un utilisateur, et accordez les autorisations appropriées. Si vous disposez déjà d'informations d'identification provenant d'une synchronisation existante, vous pouvez les réutiliser, mais veillez à étendre l'accès à la table source des déclencheurs Canvas.  

```sql

CREATE ROLE BRAZE_INGESTION_ROLE;

GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.CANVAS_TRIGGERS_SYNC TO ROLE BRAZE_INGESTION_ROLE;

CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;
GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;

CREATE USER BRAZE_INGESTION_USER;
GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;

```

##### Étape 1.3 : Configurer les politiques de réseau

Si votre compte dispose de politiques de réseau, autorisez la liste des IP de Braze pour permettre la connexion au service CDI. Pour connaître la liste des IP, reportez-vous à la section [Ingestion de données dans le cloud]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=snowflake#step-15-allow-braze-ips-in-snowflake-network-policy-optional).  

{% endtab %}
{% tab Redshift %}

##### Étape 1.1 : Configurez votre table source dans Redshift

Vous pouvez utiliser les noms de l'exemple suivant ou choisir vos propres noms de base de données, de schéma et de table. Vous pouvez également utiliser une vue ou une vue matérialisée au lieu d'une table.

```sql
CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
CREATE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.CANVAS_TRIGGERS_SYNC (
    updated_at timestamptz default sysdate not null,
    --at least one of external_id or alias_name and alias_label is required
    external_id varchar not null,.
    --if using user alias, both alias_name and alias_label are required
    alias_label varchar,
    alias_name varchar,
    properties varchar(max)
 );
```

Vous pouvez nommer la base de données, le schéma et la table comme vous le souhaitez, mais les noms des colonnes doivent correspondre à la définition précédente.

* `UPDATED_AT`: Heure à laquelle cette ligne a été mise à jour ou ajoutée au tableau. Seules les lignes ajoutées ou mises à jour depuis la dernière synchronisation seront synchronisées.  
* Soit `external_id`, soit `alias_name` et `alias_label` comme colonne d'identification de l'utilisateur. Ceux-ci identifient les utilisateurs pour lesquels vous souhaitez déclencher l'envoi de messages canvas.  
  * `EXTERNAL_ID`: Identifie l'utilisateur à entrer dans le Canvas. Cette valeur devrait correspondre à la valeur `external_id` utilisée dans Braze.  
  * `ALIAS_NAME` et `ALIAS_LABEL`: Ces colonnes créent un objet alias d'utilisateur. `alias_name` doit être un identifiant unique et alias_label spécifie le type d'alias. Les utilisateurs peuvent avoir plusieurs alias avec des libellés différents, mais un seul `alias_name` par `alias_label`.  
* `PROPERTIES`: Une chaîne JSON de caractères de champs à rendre disponibles en tant que propriétés de personnalisation dans votre Canvas. Elle doit contenir des informations spécifiques à l'utilisateur.

{% alert note %}
Les propriétés ne sont pas nécessaires pour chaque ligne ou chaque utilisateur. Cependant, les valeurs des propriétés doivent être une chaîne de caractères JSON valide. Saisissez une chaîne vide `{}` caractères s'il n'y a pas de propriétés pour la ligne.
{% endalert %}

##### Étape 1.2 : Créer des informations d'identification

Définissez un rôle, un entrepôt et un utilisateur et accordez les autorisations appropriées. Si vous disposez déjà d'informations d'identification provenant d'une synchronisation existante, vous pouvez les réutiliser, mais veillez à étendre l'accès à la table source des déclencheurs Canvas.

```sql
CREATE USER braze_user PASSWORD '{password}';
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT SELECT ON TABLE CANVAS_TRIGGERS_SYNC TO braze_user;
```

##### Étape 1.3 : Configurer les politiques de réseau 

Si votre compte dispose de politiques de réseau, autorisez la liste des IP de Braze pour permettre la connexion au service CDI. Pour connaître la liste des IP, reportez-vous à la section [Ingestion de données dans le cloud]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=redshift#step-13-allow-access-to-braze-ips).

{% endtab %}
{% tab BigQuery %}

##### Étape 1.1 : Créez un nouveau projet ou un nouveau jeu de données pour votre table source (facultatif).

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

##### Étape 1.2 : Configurez votre table source dans BigQuery
Reportez-vous à ce qui suit lorsque vous créez votre tableau source :  

| Nom du champ | Type | Nécessaire ? | 
| :---- | :---- | :---- | 
| **`UPDATED_AT`** | Horodatage | Oui | 
| **`PROPERTIES`** | JSON | Oui | 
| **`EXTERNAL_ID`** | CHAÎNE DE CARACTÈRES | NULLABLE | 
| **`ALIAS_NAME`** | CHAÎNE DE CARACTÈRES | NULLABLE | 
| **`ALIAS_LABEL`** | CHAÎNE DE CARACTÈRES | NULLABLE |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Les propriétés ne sont pas nécessaires pour chaque ligne ou chaque utilisateur. Cependant, les valeurs des propriétés doivent être une chaîne de caractères JSON valide. Saisissez une chaîne vide `{}` caractères s'il n'y a pas de propriétés pour la ligne.
{% endalert %}

```sql
CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.CANVAS_TRIGGERS_SYNC`
(
  updated_at TIMESTAMP DEFAULT current_timestamp,
  --At least one of external_id or alias_name and alias_label is required  
  external_id STRING,
  --If using user alias, both alias_name and alias_label are required
  alias_name STRING,
  alias_label STRING,
  properties JSON
);
```

##### Étape 1.3 : Créer des informations d'identification

Créez un utilisateur et accordez-lui des autorisations. Si vous disposez déjà d'informations d'identification provenant d'une autre synchronisation, vous pouvez les réutiliser tant qu'elles ont accès à la table des déclencheurs de canevas.

| Permission | Objectif |
| :---- | :---- |
| Utilisateur de la connexion BigQuery | Permet à Braze de se connecter. |
| Utilisateur de BigQuery | Permet à Braze d'exécuter des requêtes, de lire des métadonnées et de répertorier des tables. |
| Visualisateur de données BigQuery | Permet à Braze de visualiser les ensembles de données et leur contenu. |
| BigQuery Job User | Permet à Braze d'exécuter des travaux. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Après avoir accordé les autorisations, générez une clé JSON. Reportez-vous à la section [Création et suppression de clés](https://cloud.google.com/iam/docs/keys-create-delete) pour plus d'informations. Vous le téléchargerez plus tard dans le tableau de bord de Braze.

##### Étape 1.4 : Configurer les politiques de réseau 
Si votre compte dispose de politiques de réseau, autorisez la liste des IP de Braze pour permettre la connexion au service CDI. Pour connaître la liste des IP, reportez-vous à la section [Ingestion de données dans le cloud]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=bigquery#step-13-allow-access-to-braze-ips).

{% endtab %}
{% tab Databricks %}

##### Étape 1.1 : Créez un catalogue ou un schéma pour votre table source.

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

#### Étape 1.2 : Configurez votre table source dans Databricks

Reportez-vous à ce qui suit lorsque vous créez votre tableau source :

| Nom du champ | Type | Exigée |
| :---- | :---- | :---- |
| `UPDATED_AT` | Horodatage | Oui |
| `PROPERTIES` | JSON | Oui |
| `EXTERNAL_ID` | CHAÎNE DE CARACTÈRES |  NULLABLE |
| `ALIAS_NAME` | CHAÎNE DE CARACTÈRES | NULLABLE |
| `ALIAS_LABEL` | CHAÎNE DE CARACTÈRES | NULLABLE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Vous pouvez nommer le schéma et la table comme vous le souhaitez, mais les noms des colonnes doivent correspondre à la définition précédente.

* `UPDATED_AT`: Heure à laquelle cette ligne a été mise à jour ou ajoutée au tableau. Seules les lignes ajoutées ou mises à jour depuis la dernière synchronisation seront synchronisées.  
* Soit `external_id`, soit `alias_name` et `alias_label` comme colonne d'identification de l'utilisateur. Ceux-ci identifient les utilisateurs pour lesquels vous souhaitez déclencher l'envoi de messages canvas.  
  * `EXTERNAL_ID`: Identifie l'utilisateur à entrer dans le Canvas. Cette valeur devrait correspondre à la valeur `external_id` utilisée dans Braze.  
  * `ALIAS_NAME` et `ALIAS_LABEL`: Ces colonnes créent un objet alias d'utilisateur. `alias_name` doit être un identifiant unique et `alias_label` spécifie le type d'alias. Les utilisateurs peuvent avoir plusieurs alias avec des libellés différents, mais un seul alias_name par `alias_label`.  
* `PROPERTIES`: Une chaîne de caractères ou une structure de champs à rendre disponible en tant que propriétés de personnalisation dans votre Canvas. Elle doit contenir des informations spécifiques à l'utilisateur.

{% alert note %}
Les propriétés ne sont pas nécessaires pour chaque ligne ou chaque utilisateur. Cependant, les valeurs des propriétés doivent être des chaînes JSON valides. Saisissez une chaîne vide `{}` caractères s'il n'y a pas de propriétés pour la ligne.
{% endalert %}

```sql
CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC`
(
  updated_at TIMESTAMP DEFAULT current_timestamp(),
  --At least one of external_id or alias_name and alias_label is required  
  external_id STRING,
  --If using user alias, both alias_name and alias_label are required
  alias_name STRING,
  alias_label STRING,
  properties STRING, STRUCT, or MAP
);
```

##### Étape 1.3 : Créer des informations d'identification 

Créez un jeton d'accès personnel dans Databricks :

1. Sélectionnez votre nom d'utilisateur, puis sélectionnez **Paramètres de l'utilisateur.**  
2. Dans l'onglet **Jetons d'accès**, sélectionnez **Générer un nouveau jeton**.  
3. Ajoutez un commentaire pour identifier le jeton, par exemple "Braze CDI".  
4. Laissez le champ **Durée de vie (jours)** vide pour ne pas avoir d'expiration, puis sélectionnez **Générer**.  
5. Copiez et enregistrez le jeton en toute sécurité pour l'utiliser dans le tableau de bord de Braze.

##### Étape 1.4 : Configurer les politiques de réseau 

Si votre compte dispose de politiques de réseau, autorisez la liste des IP de Braze pour permettre la connexion au service CDI. Pour connaître la liste des IP, reportez-vous à la section [Ingestion de données dans le cloud]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=databricks#step-13-allow-access-to-braze-ips).

{% endtab %}
{% tab Fabric %}

##### Étape 1.1 : Configurez votre tableau source dans Fabric

```sql
CREATE OR ALTER TABLE [warehouse].[schema].[CDI_table_name] 
(
  UPDATED_AT DATETIME2(6) NOT NULL,
  PROPERTIES VARCHAR NOT NULL,
  --at least one of external_id or alias_name and alias_label is required  
  EXTERNAL_ID VARCHAR,
  --if using user alias, both alias_name and alias_label are required
  ALIAS_NAME VARCHAR,
  ALIAS_LABEL VARCHAR
)
GO
```

##### Étape 1.2 : Créer des informations d'identification 

Créez un principal de service et accordez des autorisations. Si vous disposez déjà d'informations d'identification provenant d'une autre synchronisation, vous pouvez les réutiliser - assurez-vous simplement qu'elles ont accès à la table des comptes.

##### Étape 1.3 : Configurer les politiques de réseau 

Si votre compte dispose de politiques de réseau, autorisez la liste des IP de Braze pour permettre la connexion au service CDI. Pour connaître la liste des IP, reportez-vous à la section [Ingestion de données dans le cloud]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=microsoft%20fabric#step-15-allow-braze-ips-in-firewall-optional).

{% endtab %}
{% tab File Storage %}

Pour synchroniser les déclencheurs Canvas à partir du stockage de fichiers, créez un fichier source contenant les champs suivants.

| Champ d'application | Exigée | Description |
| :---- | :---- | :---- |
| `EXTERNAL_ID` | Oui, l'un des sites `external_id` ou `alias_name`, et `alias_label` | Il identifie l'utilisateur que vous souhaitez mettre à jour. Cette valeur devrait correspondre à la valeur `external_id` utilisée dans Braze. |
| `ALIAS_NAME` et `ALIAS_LABEL` | Oui, l'un des sites `external_id` ou `alias_name` et `alias_label` | Ces deux colonnes créent un objet alias d'utilisateur. `alias_name` doit être un identifiant unique et `alias_label` spécifie le type d'alias. Les utilisateurs peuvent avoir plusieurs alias avec des libellés différents, mais un seul `alias_name` par `alias_label`. |
| `PROPERTIES` | Oui | Chaîne de caractères JSON des champs à rendre disponibles en tant que propriétés de personnalisation dans votre Canvas. Elle doit contenir des informations spécifiques à l'utilisateur. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert tip %}
Les noms de fichiers doivent respecter les règles AWS et être uniques. Ajoutez des horodatages pour garantir l'unicité. Pour en savoir plus sur la synchronisation Amazon S3, consultez la rubrique [Intégrations de stockage de fichiers](https://www.braze.com/docs/user_guide/data/cloud_ingestion/file_storage_integrations).
{% endalert %}

{% endtab %}
{% endtabs %}

#### Étape 2 : Configurez votre Canvas de destination

1. Configurez vos déclencheurs Canvas for Canvas de destination. Créez un nouveau canvas ou sélectionnez un canvas existant déclenché par l'API. Reportez-vous à la section [Types de planification d'entrée]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas#entry-schedule-types) pour savoir comment créer un canvas avec un type de planification de réception/distribution déclenché par l'API.
2. Après avoir sélectionné le type de planification de réception/distribution déclenchée par l'API, poursuivez la configuration de Canvas et créez votre Canvas. Les canevas peuvent aller du simple envoi d'un message unique à des flux de travail complexes pour les clients, avec plusieurs étapes.
3. Dans vos étapes du canvas, utilisez les [propriétés d'entrée du canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties) pour personnaliser les messages avec les champs de propriétés que vous prévoyez de synchroniser à partir de votre table source.
  * Par exemple, si à l'étape 1 vous avez instrumenté un champ de propriétés pour `account_balance`, vous utiliserez le modèle Liquid suivant pour personnaliser votre message : `\{\{canvas_entry_properties.\$\{account_balance\}\}\}`.
5. Après avoir créé votre Canvas, lancez-le et passez à l'[étape 3.](#step-3-create-your-zero-copy-sync)

#### Étape 3 : Créez votre copie zéro de synchronisation

Une fois la configuration de la source terminée et le Canvas de destination lancé, créez une nouvelle synchronisation des données :

1. Dans Braze, accédez à **Paramètres des données** > **Ingestion de données dans le cloud**.
1. Établissez la connexion en saisissant les détails de la connexion (ou en réutilisant les informations d'identification existantes) et le tableau source de l'[étape 1.](#step-1-set-up-data-source-for-canvas-triggers)
2. Donnez un nom à l'intégration.
3. Sélectionnez le type de données des **déclencheurs Canvas**.
4. Choisissez votre canvas de destination (à partir de l'[étape du](#step-2-configure-your-destination-canvas) canvas [2)](#step-2-configure-your-destination-canvas).
5. Choisissez une fréquence de synchronisation.
6. Définir les préférences de notification.
7. Sélectionnez **Tester la connexion** pour confirmer que tout fonctionne comme prévu. Si vous vous connectez à Snowflake, ajoutez d'abord la clé publique affichée sur le tableau de bord à l'utilisateur créé pour Braze afin de vous connecter à Snowflake. Pour réaliser cette étape, vous devez disposer d'un accès **SECURITYADMIN** ou supérieur dans Snowflake. 
8. Enregistrez la synchronisation pour commencer à synchroniser les déclencheurs de Canvas.

Lorsque la synchronisation s'exécute, les utilisateurs de votre table source commencent à entrer dans le Canvas. Utilisez l'analyse/analytique Canvas et la page des journaux de synchronisation de l'ingestion de données dans le cloud pour surveiller les performances.

{% alert tip %}  
Passez en revue l'ensemble de votre configuration (du comportement de synchronisation à la configuration de Canvas) afin d'éviter les envois inattendus. Les paramètres du canvas, tels que la limite de débit, la limite de fréquence et les filtres de segmentation, permettent d'affiner encore l'envoi des messages.<br><br>Nous vous recommandons de procéder à un essai avec une audience réduite ou test avant de mettre en œuvre des cas d'utilisation en production.
{% endalert %}

### Considérations

Les déclencheurs CDI Canvas utilisent la limite de débit de votre API REST pour `/canvas/trigger/send`. Si vous utilisez cet endpoint simultanément avec des déclencheurs CDI Canvas et votre intégration REST API, attendez-vous à ce que l'utilisation combinée soit prise en compte dans votre limite de débit.

Bien que les déclencheurs CDI Canvas soient en accès anticipé, tenez compte des détails suivants :

* Jusqu'à 5 synchronisations actives du déclencheur Canvas par espace de travail  
* Chaque cycle de synchronisation entrera les utilisateurs dans leur canvas de destination respectif à un rythme maximum d'environ 3,75 millions d'utilisateurs par heure.  
  * Préparez-vous à des délais d'entrée plus longs entre la source et le canvas lorsque :  
    * Synchronisation de plus de 3,75 millions d'utilisateurs par cycle de synchronisation.  
    * Utiliser les déclencheurs CDI Canvas lorsque vous saturez déjà la limite de débit de votre API REST pour [ `/canvas/trigger/send`.]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/#rate-limit)