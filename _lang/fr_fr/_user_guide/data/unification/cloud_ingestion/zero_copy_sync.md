---
nav_title: Personnalisation sans copie
article_title: "Personnalisation sans copie à l'aide de CDI"
page_order: 4
page_type: reference
description: "Cette page fournit un aperçu de la manière de déclencher Braze Canvases à l'aide de CDI."
---

# Personnalisation sans copie à l'aide de CDI

> Découvrez comment synchroniser les déclencheurs Canvas à l'aide de CDI pour une personnalisation sans copie. Cette fonctionnalité permet d'accéder aux informations spécifiques à l'utilisateur à partir de votre solution de stockage de données et les transmet à un canvas de destination. Les étapes du canvas peuvent éventuellement inclure des champs de personnalisation qui ne sont pas conservés dans les profils utilisateurs Braze.

{% multi_lang_include early_access_beta_alert.md feature='CDI Canvas triggers' %}

## Synchronisation des déclencheurs Canvas

### Étapes de démarrage rapide

Si vous connaissez déjà Braze CDI, veuillez noter que la configuration d'une synchronisation de déclencheur Canvas suit de près le processus d'[intégration CDI des]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/) [données utilisateur]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/), avec les réserves suivantes :

- Seuls les ID externes ou les alias d'utilisateur sont pris en charge. Les adresses de e-mail et les numéros de téléphone ne sont pas des identifiants acceptés.  
- Seuls les utilisateurs Braze existants peuvent être synchronisés. Il n'est pas possible de créer de nouveaux utilisateurs.  
- `properties` remplace la`payload`colonne. Il s'agit d'une chaîne de caractères JSON des champs que vous souhaitez utiliser comme propriétés d'entrée canvas pour la personnalisation.

Pour commencer, veuillez sélectionner le type de données **Canvas Triggers** lors de la création d'une nouvelle synchronisation.

### Utilisation des déclencheurs Canvas 

#### Étape 1 : Configurer la source de données pour les déclencheurs Canvas

{% tabs %}
{% tab Snowflake %}

##### Étape 1.1 : Configurez votre table source dans Snowflake.

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

Vous pouvez donner le nom que vous désirez à la base de données, au schéma et à la table, mais les noms de colonnes doivent correspondre à la définition précédente.

* `UPDATED_AT` : Heure à laquelle cette ligne a été mise à jour ou ajoutée au tableau. Seules les lignes ajoutées ou mises à jour depuis la dernière synchronisation seront synchronisées.  
* Soit`external_id`  soit`alias_name`  et`alias_label`  comme colonne d'identifiant utilisateur. Ces paramètres permettent d'identifier les utilisateurs pour lesquels vous souhaitez activer l'envoi de messages Canvas.  
  * `EXTERNAL_ID` : Identifie l'utilisateur autorisé à accéder à Canvas. Cela doit correspondre à la valeur `external_id` utilisée dans Braze.  
  * `ALIAS_NAME` et `ALIAS_LABEL`: Ces colonnes créent un objet d'alias d'utilisateur.`alias_name`  doit être un identifiant unique, et`alias_label`  spécifie le type d'alias. Les utilisateurs peuvent avoir plusieurs alias avec des libellés différents, mais un seul alias_name par `alias_label`.  
* `PROPERTIES` : Chaîne de caractères JSON de champs à rendre disponibles en tant que propriétés de personnalisation dans votre canvas. Ceci devrait contenir des informations spécifiques à l'utilisateur.

{% alert note %}
Les propriétés ne sont pas obligatoires pour chaque ligne ou utilisateur. Cependant, les valeurs des propriétés doivent être des chaînes de caractères JSON valides. Veuillez saisir une chaîne de caractères`{}` vide s'il n'y a aucune propriété pour la ligne.
{% endalert %}

##### Étape 1.2 : Configurer les informations d'identification

Veuillez configurer un rôle, un entrepôt et un utilisateur, puis accorder les autorisations appropriées. Si vous disposez déjà d'informations d'identification provenant d'une synchronisation existante, vous pouvez les réutiliser, mais veuillez vous assurer d'étendre l'accès à la table source des déclencheurs canvas.  

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

##### Étape 1.3 : Configurer les politiques réseau

Si votre compte est soumis à des politiques réseau, veuillez ajouter les adresses IP de Braze à la liste blanche afin de permettre la connexion au service CDI. Pour obtenir la liste des adresses IP, veuillez consulter [la section Ingestion de données dans le cloud]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=snowflake#step-15-allow-braze-ips-in-snowflake-network-policy-optional).  

{% endtab %}
{% tab Redshift %}

##### Étape 1.1 : Configurez votre table source dans Redshift.

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

Vous pouvez donner le nom que vous désirez à la base de données, au schéma et à la table, mais les noms de colonnes doivent correspondre à la définition précédente.

* `UPDATED_AT` : Heure à laquelle cette ligne a été mise à jour ou ajoutée au tableau. Seules les lignes ajoutées ou mises à jour depuis la dernière synchronisation seront synchronisées.  
* Soit`external_id`  soit`alias_name`  et`alias_label`  comme colonne d'identifiant utilisateur. Ces paramètres permettent d'identifier les utilisateurs pour lesquels vous souhaitez activer l'envoi de messages Canvas.  
  * `EXTERNAL_ID` : Identifie l'utilisateur autorisé à accéder à Canvas. Cela doit correspondre à la valeur `external_id` utilisée dans Braze.  
  * `ALIAS_NAME` et `ALIAS_LABEL`: Ces colonnes créent un objet d'alias d'utilisateur.`alias_name`  doit être un identifiant unique, etalias_label  spécifie le type d'alias. Les utilisateurs peuvent avoir plusieurs alias avec des libellés différents, mais un seul `alias_name` par `alias_label`.  
* `PROPERTIES` : Chaîne de caractères JSON de champs à rendre disponibles en tant que propriétés de personnalisation dans votre canvas. Ceci devrait contenir des informations spécifiques à l'utilisateur.

{% alert note %}
Les propriétés ne sont pas obligatoires pour chaque ligne ou utilisateur. Cependant, les valeurs des propriétés doivent être une chaîne de caractères JSON valide. Veuillez saisir une chaîne de caractères`{}` vide s'il n'y a aucune propriété pour la ligne.
{% endalert %}

##### Étape 1.2 : Configurer les informations d'identification

Veuillez configurer un rôle, un entrepôt et un utilisateur, puis attribuer les autorisations appropriées. Si vous disposez déjà d'informations d'identification provenant d'une synchronisation existante, vous pouvez les réutiliser, mais veuillez vous assurer d'étendre l'accès à la table source des déclencheurs canvas.

```sql
CREATE USER braze_user PASSWORD '{password}';
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT SELECT ON TABLE CANVAS_TRIGGERS_SYNC TO braze_user;
```

##### Étape 1.3 : Configurer les politiques réseau 

Si votre compte est soumis à des politiques réseau, veuillez ajouter les adresses IP de Braze à la liste blanche afin de permettre la connexion au service CDI. Pour obtenir la liste des adresses IP, veuillez consulter [la section Ingestion de données dans le cloud]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=redshift#step-13-allow-access-to-braze-ips).

{% endtab %}
{% tab BigQuery %}

##### Étape 1.1 : Veuillez créer un nouveau projet ou un nouvel ensemble de données pour votre table source (facultatif).

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

##### Étape 1.2 : Configurez votre table source dans BigQuery.
Veuillez vous référer aux informations suivantes lors de la création de votre table source :  

| Nom du champ | Type | Requise ? | 
| :---- | :---- | :---- | 
| **`UPDATED_AT`** | Horodatage | Oui | 
| **`PROPERTIES`** | JSON | Oui | 
| **`EXTERNAL_ID`** | CHAÎNE DE CARACTÈRES | NULLABLE | 
| **`ALIAS_NAME`** | CHAÎNE DE CARACTÈRES | NULLABLE | 
| **`ALIAS_LABEL`** | CHAÎNE DE CARACTÈRES | NULLABLE |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Les propriétés ne sont pas obligatoires pour chaque ligne ou utilisateur. Cependant, les valeurs des propriétés doivent être une chaîne de caractères JSON valide. Veuillez saisir une chaîne de caractères`{}` vide s'il n'y a aucune propriété pour la ligne.
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

##### Étape 1.3 : Configurer les informations d'identification

Veuillez créer un utilisateur et lui accorder les autorisations nécessaires. Si vous disposez déjà d'identifiants provenant d'une autre synchronisation, vous pouvez les réutiliser à condition qu'ils aient accès au tableau des déclencheurs canvas.

| Autorisation | Objectif |
| :---- | :---- |
| Utilisateur de connexion BigQuery | Permet à Braze de se connecter. |
| Utilisateur BigQuery | Permet à Braze d'exécuter des requêtes, de lire des métadonnées et de répertorier des tables. |
| Visualiseur de données BigQuery | Permet à Braze de consulter les ensembles de données et les contenus. |
| Utilisateur de tâches BigQuery | Permet à Braze d'exécuter des tâches. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Après avoir accordé les autorisations, veuillez générer une clé JSON. Veuillez consulter [la section Création et suppression de clés](https://cloud.google.com/iam/docs/keys-create-delete) pour obtenir des instructions. Vous pourrez le télécharger ultérieurement dans le tableau de bord de Braze.

##### Étape 1.4 : Configurer les politiques réseau 
Si votre compte est soumis à des politiques réseau, veuillez ajouter les adresses IP de Braze à la liste blanche afin de permettre la connexion au service CDI. Pour obtenir la liste des adresses IP, veuillez consulter [la section Ingestion de données dans le cloud]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=bigquery#step-13-allow-access-to-braze-ips).

{% endtab %}
{% tab Databricks %}

##### Étape 1.1 : Veuillez créer un catalogue ou un schéma pour votre table source.

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

#### Étape 1.2 : Configurez votre table source dans Databricks.

Veuillez vous référer aux informations suivantes lors de la création de votre table source :

| Nom du champ | Type | Requis |
| :---- | :---- | :---- |
| `UPDATED_AT` | Horodatage | Oui |
| `PROPERTIES` | JSON | Oui |
| `EXTERNAL_ID` | CHAÎNE DE CARACTÈRES |  NULLABLE |
| `ALIAS_NAME` | CHAÎNE DE CARACTÈRES | NULLABLE |
| `ALIAS_LABEL` | CHAÎNE DE CARACTÈRES | NULLABLE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Vous pouvez nommer le schéma et la table comme vous le souhaitez, mais les noms des colonnes doivent correspondre à la définition précédente.

* `UPDATED_AT` : Heure à laquelle cette ligne a été mise à jour ou ajoutée au tableau. Seules les lignes ajoutées ou mises à jour depuis la dernière synchronisation seront synchronisées.  
* Soit`external_id`  soit`alias_name`  et`alias_label`  comme colonne d'identifiant utilisateur. Ces paramètres permettent d'identifier les utilisateurs pour lesquels vous souhaitez activer l'envoi de messages Canvas.  
  * `EXTERNAL_ID` : Identifie l'utilisateur autorisé à accéder à Canvas. Cela doit correspondre à la valeur `external_id` utilisée dans Braze.  
  * `ALIAS_NAME` et `ALIAS_LABEL`: Ces colonnes créent un objet d'alias d'utilisateur.`alias_name`  doit être un identifiant unique, et`alias_label`  spécifie le type d'alias. Les utilisateurs peuvent avoir plusieurs alias avec des libellés différents, mais un seul alias_name par `alias_label`.  
* `PROPERTIES` : Une chaîne de caractères ou une structure de champs à rendre disponibles en tant que propriétés de personnalisation dans votre canvas. Ceci devrait contenir des informations spécifiques à l'utilisateur.

{% alert note %}
Les propriétés ne sont pas obligatoires pour chaque ligne ou utilisateur. Cependant, les valeurs des propriétés doivent être des chaînes de caractères JSON valides. Veuillez saisir une chaîne de caractères`{}` vide s'il n'y a aucune propriété pour la ligne.
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

##### Étape 1.3 : Configurer les informations d'identification 

Veuillez créer un jeton d'accès personnel dans Databricks :

1. Veuillez sélectionner votre nom d'utilisateur, puis choisissez **Paramètres utilisateur.**  
2. Dans l'onglet **Jetons d'accès**, veuillez sélectionner **Générer un nouveau jeton.**  
3. Veuillez ajouter un commentaire pour identifier le jeton, par exemple « Braze CDI ».  
4. Veuillez laisser **le champ Durée de vie (jours)** vide pour qu'il n'y ait pas d'expiration, puis sélectionnez **Générer**.  
5. Veuillez copier et enregistrer le jeton en toute sécurité pour l'utiliser dans le tableau de bord de Braze.

##### Étape 1.4 : Configurer les politiques réseau 

Si votre compte est soumis à des politiques réseau, veuillez ajouter les adresses IP de Braze à la liste blanche afin de permettre la connexion au service CDI. Pour obtenir la liste des adresses IP, veuillez consulter [la section Ingestion de données dans le cloud]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=databricks#step-13-allow-access-to-braze-ips).

{% endtab %}
{% tab Fabric %}

##### Étape 1.1 : Configurez votre table source dans Fabric.

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

##### Étape 1.2 : Configurer les informations d'identification 

Veuillez créer un principal de service et lui accorder les autorisations nécessaires. Si vous disposez déjà d'identifiants provenant d'une autre synchronisation, vous pouvez les réutiliser. Veuillez simplement vous assurer qu'ils ont accès au tableau des comptes.

##### Étape 1.3 : Configurer les politiques réseau 

Si votre compte est soumis à des politiques réseau, veuillez ajouter les adresses IP de Braze à la liste blanche afin de permettre la connexion au service CDI. Pour obtenir la liste des adresses IP, veuillez consulter [la section Ingestion de données dans le cloud]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=microsoft%20fabric#step-15-allow-braze-ips-in-firewall-optional).

{% endtab %}
{% tab File Storage %}

Pour synchroniser les déclencheurs canvas à partir du stockage de fichiers, veuillez créer un fichier source contenant les champs suivants.

| Champ | Requis | Description |
| :---- | :---- | :---- |
| `EXTERNAL_ID` | Oui, l'un des deux`external_id`ou `alias_name`les deux, et `alias_label` | Il identifie l'utilisateur que vous souhaitez mettre à jour. Cela doit correspondre à la valeur `external_id` utilisée dans Braze. |
| `ALIAS_NAME` et `ALIAS_LABEL` | Oui, l'un des deux`external_id`ou`alias_name`les deux. `alias_label` | Ces deux colonnes créent un objet alias d'utilisateur. `alias_name` doit être un identifiant unique et `alias_label` spécifie le type d'alias. Les utilisateurs peuvent avoir plusieurs alias avec des libellés différents, mais un seul `alias_name` par `alias_label`. |
| `PROPERTIES` | Oui | Chaîne de caractères JSON des champs à rendre disponibles en tant que propriétés de personnalisation dans votre canvas. Ceci devrait contenir des informations spécifiques à l'utilisateur. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert tip %}
Les noms de fichiers doivent respecter les règles AWS et être uniques. Ajoutez des horodatages pour garantir l'unicité. Pour plus d'informations sur la synchronisation Amazon S3, veuillez consulter [la section Intégrations de stockage de fichiers](https://www.braze.com/docs/user_guide/data/cloud_ingestion/file_storage_integrations).
{% endalert %}

{% endtab %}
{% endtabs %}

#### Étape 2 : Veuillez configurer votre destination canvas.

1. Configurez votre destination Canvas pour les déclencheurs Canvas. Veuillez créer un nouveau canvas déclenché par API ou sélectionner un canvas existant. Veuillez vous référer aux [types de planification de saisie]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas#entry-schedule-types) pour obtenir des instructions sur la manière de créer un canvas avec un type de planification de réception/distribution déclenché par API.
2. Après avoir sélectionné le type de planification de livraison déclenché par l'API, veuillez poursuivre la configuration de Canvas et créer votre Canvas. Les canevas peuvent aller de simples envois de messages à des flux de travail clients personnalisés comportant plusieurs étapes.
3. Dans vos étapes du canvas, veuillez utiliser [les propriétés d'entrée Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties) pour réaliser la personnalisation des messages avec les champs de propriétés que vous prévoyez de synchroniser à partir de votre table source.
  * Par exemple, si à l'étape 1 vous avez instrumenté un champ de propriétés pour `account_balance`, vous utiliseriez le modèle Liquid suivant pour réaliser la personnalisation de votre message : `\{\{canvas_entry_properties.\$\{account_balance\}\}\}`.
5. Une fois votre canvas créé, veuillez le lancer et passer à [l'étape 3](#step-3-create-your-zero-copy-sync).

#### Étape 3 : Veuillez créer votre synchronisation sans copie.

Une fois la configuration de la source terminée et la destination Canvas lancée, veuillez créer une nouvelle synchronisation des données :

1. Dans Braze, veuillez vous rendre dans **Paramètres des données** > **Ingestion de données cloud**.
1. Veuillez configurer la connexion en saisissant les informations de connexion (ou en réutilisant les identifiants existants) et la table source de [l'étape 1](#step-1-set-up-data-source-for-canvas-triggers).
2. Veuillez attribuer un nom à l'intégration.
3. Veuillez sélectionner le type de données **« Déclencheurs Canvas** ».
4. Veuillez sélectionner votre destination Canvas (à partir de [l'étape 2](#step-2-configure-your-destination-canvas)).
5. Veuillez sélectionner une fréquence de synchronisation.
6. Veuillez configurer vos préférences de notification.
7. Veuillez sélectionner **« Tester la connexion** » pour vérifier que tout fonctionne correctement. Si vous vous connectez à Snowflake, veuillez d'abord ajouter la clé publique affichée sur le tableau de bord de Braze à l'utilisateur créé pour Braze afin de vous connecter à Snowflake. Pour effectuer cette étape, vous devez disposer d'un accès **SECURITYADMIN** ou supérieur dans Snowflake. 
8. Enregistrez la synchronisation pour commencer à synchroniser les déclencheurs Canvas.

Lorsque la synchronisation est effectuée, les utilisateurs de votre tableau source commenceront à entrer dans Canvas. Veuillez utiliser les analyses Canvas et la page des journaux de synchronisation de l’ingestion de données pour surveiller les performances.

{% alert tip %}  
Veuillez vérifier l'ensemble de votre configuration (du comportement de synchronisation à la configuration de canvas) afin d'éviter tout envoi inattendu. Les paramètres Canvas tels que la limite de débit, la limite de fréquence et les filtres de segmentation permettent d'affiner davantage la réception/distribution des messages.<br><br>Nous vous recommandons de procéder à un essai auprès d'une audience restreinte ou test avant de mettre en œuvre des cas d'utilisation en production.
{% endalert %}

### Considérations

Les déclencheurs CDI canvas utilisent votre limite de débit API REST pour `/canvas/trigger/send`. Si vous utilisez cet endpoint simultanément avec les déclencheurs CDI Canvas et votre intégration API REST, veuillez noter que l'utilisation combinée sera prise en compte dans votre limite de débit.

Les déclencheurs CDI canvas étant actuellement en accès anticipé, veuillez prendre en considération les détails suivants :

* Jusqu'à 5 synchronisations de déclencheurs canvas actives par espace de travail  
* Chaque synchronisation permettra d'ajouter des utilisateurs à leur canvas de destination respective à un rythme maximal d'environ 3,75 millions d'utilisateurs par heure.  
  * Veuillez vous préparer à des délais plus longs entre la source et l'entrée dans canvas lorsque :  
    * Synchronisation de plus de 3,75 millions d'utilisateurs par cycle de synchronisation.  
    * Utilisation des déclencheurs CDI Canvas lorsque [la limite de débit]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/#rate-limit) de votre API REST est déjà saturée [pour `/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/#rate-limit).