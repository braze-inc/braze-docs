---
nav_title: Personnalisation sans copie
article_title: "Personnalisation sans copie à l'aide de CDI"
page_order: 4
page_type: reference
description: "Cette page fournit un aperçu de la manière de déclencher des Canvas Braze à l'aide de CDI."
---

# Personnalisation sans copie à l'aide de CDI

> Découvrez comment synchroniser les déclencheurs Canvas à l'aide de CDI pour une personnalisation sans copie. Cette fonctionnalité accède aux informations spécifiques à l'utilisateur depuis votre solution de stockage de données et les transmet à un Canvas de destination. Les étapes du Canvas peuvent éventuellement inclure des champs de personnalisation qui ne sont pas conservés dans les profils utilisateurs Braze.

{% multi_lang_include early_access_beta_alert.md feature='CDI Canvas triggers' %}

## Synchronisation des déclencheurs Canvas

### Étapes de démarrage rapide

Si vous connaissez déjà Braze CDI, notez que la configuration d'une synchronisation de déclencheur Canvas suit de près le processus des [intégrations CDI de données utilisateur]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/), avec les réserves suivantes :

- Seuls les ID externes ou les alias d'utilisateur sont pris en charge. Les adresses e-mail et les numéros de téléphone ne sont pas des identifiants acceptés.  
- Seuls les utilisateurs Braze existants peuvent être synchronisés. Il n'est pas possible de créer de nouveaux utilisateurs.  
- `properties` remplace la colonne `payload`. Il s'agit d'une chaîne de caractères JSON des champs que vous souhaitez utiliser comme propriétés d'entrée Canvas pour la personnalisation.

Pour commencer, sélectionnez le type de données **Canvas Triggers** lors de la création d'une nouvelle synchronisation.

### Utilisation des déclencheurs Canvas 

#### Étape 1 : Configurer la source de données pour les déclencheurs Canvas

{% tabs %}
{% tab Snowflake %}

##### Étape 1.1 : Configurer votre table source dans Snowflake

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

Vous pouvez nommer la base de données, le schéma et la table comme vous le souhaitez, mais les noms de colonnes doivent correspondre à la définition précédente.

* `UPDATED_AT` : L'heure à laquelle cette ligne a été mise à jour ou ajoutée à la table. Braze synchronise les lignes dont la valeur `UPDATED_AT` est postérieure à la dernière valeur synchronisée. Les lignes situées exactement à l'horodatage limite peuvent être re-synchronisées si de nouvelles lignes partagent ce même horodatage.  
* Soit `external_id`, soit `alias_name` et `alias_label` comme colonne d'identifiant utilisateur. Ces paramètres identifient les utilisateurs pour lesquels vous souhaitez déclencher l'envoi de messages Canvas.  
  * `EXTERNAL_ID` : Identifie l'utilisateur qui doit entrer dans le Canvas. Cette valeur doit correspondre à la valeur `external_id` utilisée dans Braze.  
  * `ALIAS_NAME` et `ALIAS_LABEL` : Ces colonnes créent un objet d'alias d'utilisateur. `alias_name` doit être un identifiant unique, et `alias_label` spécifie le type d'alias. Les utilisateurs peuvent avoir plusieurs alias avec des libellés différents, mais un seul alias_name par `alias_label`.  
* `PROPERTIES` : Une chaîne de caractères JSON de champs à rendre disponibles en tant que propriétés de personnalisation dans votre Canvas. Elle doit contenir des informations spécifiques à l'utilisateur.

{% alert note %}
Les propriétés ne sont pas obligatoires pour chaque ligne ou utilisateur. Cependant, les valeurs des propriétés doivent être des chaînes de caractères JSON valides. Saisissez une chaîne `{}` vide s'il n'y a aucune propriété pour la ligne.
{% endalert %}

##### Étape 1.2 : Configurer les informations d'identification

Configurez un rôle, un entrepôt et un utilisateur, puis accordez les autorisations appropriées. Si vous disposez déjà d'informations d'identification provenant d'une synchronisation existante, vous pouvez les réutiliser, mais assurez-vous d'étendre l'accès à la table source des déclencheurs Canvas.  

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

##### Étape 1.3 : Configurer les politiques réseau

Si votre compte est soumis à des politiques réseau, ajoutez les adresses IP de Braze à la liste d'autorisation afin de permettre la connexion au service CDI. Pour obtenir la liste des adresses IP, consultez [Ingestion de données cloud]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=snowflake#step-15-allow-braze-ips-in-snowflake-network-policy-optional).  

{% endtab %}
{% tab Redshift %}

##### Étape 1.1 : Configurer votre table source dans Redshift

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

Vous pouvez nommer la base de données, le schéma et la table comme vous le souhaitez, mais les noms de colonnes doivent correspondre à la définition précédente.

* `UPDATED_AT` : L'heure à laquelle cette ligne a été mise à jour ou ajoutée à la table. Braze synchronise les lignes dont la valeur `UPDATED_AT` est postérieure à la dernière valeur synchronisée. Les lignes situées exactement à l'horodatage limite peuvent être re-synchronisées si de nouvelles lignes partagent ce même horodatage.  
* Soit `external_id`, soit `alias_name` et `alias_label` comme colonne d'identifiant utilisateur. Ces paramètres identifient les utilisateurs pour lesquels vous souhaitez déclencher l'envoi de messages Canvas.  
  * `EXTERNAL_ID` : Identifie l'utilisateur qui doit entrer dans le Canvas. Cette valeur doit correspondre à la valeur `external_id` utilisée dans Braze.  
  * `ALIAS_NAME` et `ALIAS_LABEL` : Ces colonnes créent un objet d'alias d'utilisateur. `alias_name` doit être un identifiant unique, et alias_label spécifie le type d'alias. Les utilisateurs peuvent avoir plusieurs alias avec des libellés différents, mais un seul `alias_name` par `alias_label`.  
* `PROPERTIES` : Une chaîne de caractères JSON de champs à rendre disponibles en tant que propriétés de personnalisation dans votre Canvas. Elle doit contenir des informations spécifiques à l'utilisateur.

{% alert note %}
Les propriétés ne sont pas obligatoires pour chaque ligne ou utilisateur. Cependant, les valeurs des propriétés doivent être une chaîne de caractères JSON valide. Saisissez une chaîne `{}` vide s'il n'y a aucune propriété pour la ligne.
{% endalert %}

##### Étape 1.2 : Configurer les informations d'identification

Configurez un rôle, un entrepôt et un utilisateur, puis attribuez les autorisations appropriées. Si vous disposez déjà d'informations d'identification provenant d'une synchronisation existante, vous pouvez les réutiliser, mais assurez-vous d'étendre l'accès à la table source des déclencheurs Canvas.

```sql
CREATE USER braze_user PASSWORD '{password}';
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT SELECT ON TABLE CANVAS_TRIGGERS_SYNC TO braze_user;
```

##### Étape 1.3 : Configurer les politiques réseau 

Si votre compte est soumis à des politiques réseau, ajoutez les adresses IP de Braze à la liste d'autorisation afin de permettre la connexion au service CDI. Pour obtenir la liste des adresses IP, consultez [Ingestion de données cloud]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=redshift#step-13-allow-access-to-braze-ips).

{% endtab %}
{% tab BigQuery %}

##### Étape 1.1 : Créer un nouveau projet ou un nouvel ensemble de données pour votre table source (facultatif)

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

##### Étape 1.2 : Configurer votre table source dans BigQuery
Référez-vous aux informations suivantes lors de la création de votre table source :  

| Nom du champ | Type | Requis ? | 
| :---- | :---- | :---- | 
| **`UPDATED_AT`** | Horodatage | Oui | 
| **`PROPERTIES`** | JSON | Oui | 
| **`EXTERNAL_ID`** | STRING | NULLABLE | 
| **`ALIAS_NAME`** | STRING | NULLABLE | 
| **`ALIAS_LABEL`** | STRING | NULLABLE |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Les propriétés ne sont pas obligatoires pour chaque ligne ou utilisateur. Cependant, les valeurs des propriétés doivent être une chaîne de caractères JSON valide. Saisissez une chaîne `{}` vide s'il n'y a aucune propriété pour la ligne.
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

##### Étape 1.3 : Configurer les informations d'identification

Créez un utilisateur et accordez-lui les autorisations nécessaires. Si vous disposez déjà d'identifiants provenant d'une autre synchronisation, vous pouvez les réutiliser à condition qu'ils aient accès à la table des déclencheurs Canvas.

| Autorisation | Objectif |
| :---- | :---- |
| BigQuery Connection User | Permet à Braze de se connecter. |
| BigQuery User | Permet à Braze d'exécuter des requêtes, de lire des métadonnées et de lister des tables. |
| BigQuery Data Viewer | Permet à Braze de consulter les ensembles de données et leur contenu. |
| BigQuery Job User | Permet à Braze d'exécuter des tâches. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Après avoir accordé les autorisations, générez une clé JSON. Consultez [Création et suppression de clés](https://cloud.google.com/iam/docs/keys-create-delete) pour les instructions. Vous la téléchargerez ultérieurement dans le tableau de bord de Braze.

##### Étape 1.4 : Configurer les politiques réseau 
Si votre compte est soumis à des politiques réseau, ajoutez les adresses IP de Braze à la liste d'autorisation afin de permettre la connexion au service CDI. Pour obtenir la liste des adresses IP, consultez [Ingestion de données cloud]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=bigquery#step-13-allow-access-to-braze-ips).

{% endtab %}
{% tab Databricks %}

##### Étape 1.1 : Créer un catalogue ou un schéma pour votre table source

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

#### Étape 1.2 : Configurer votre table source dans Databricks

Référez-vous aux informations suivantes lors de la création de votre table source :

| Nom du champ | Type | Requis |
| :---- | :---- | :---- |
| `UPDATED_AT` | Horodatage | Oui |
| `PROPERTIES` | JSON | Oui |
| `EXTERNAL_ID` | STRING |  NULLABLE |
| `ALIAS_NAME` | STRING | NULLABLE |
| `ALIAS_LABEL` | STRING | NULLABLE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Vous pouvez nommer le schéma et la table comme vous le souhaitez, mais les noms de colonnes doivent correspondre à la définition précédente.

* `UPDATED_AT` : L'heure à laquelle cette ligne a été mise à jour ou ajoutée à la table. Braze synchronise les lignes dont la valeur `UPDATED_AT` est postérieure à la dernière valeur synchronisée. Les lignes situées exactement à l'horodatage limite peuvent être re-synchronisées si de nouvelles lignes partagent ce même horodatage.  
* Soit `external_id`, soit `alias_name` et `alias_label` comme colonne d'identifiant utilisateur. Ces paramètres identifient les utilisateurs pour lesquels vous souhaitez déclencher l'envoi de messages Canvas.  
  * `EXTERNAL_ID` : Identifie l'utilisateur qui doit entrer dans le Canvas. Cette valeur doit correspondre à la valeur `external_id` utilisée dans Braze.  
  * `ALIAS_NAME` et `ALIAS_LABEL` : Ces colonnes créent un objet d'alias d'utilisateur. `alias_name` doit être un identifiant unique, et `alias_label` spécifie le type d'alias. Les utilisateurs peuvent avoir plusieurs alias avec des libellés différents, mais un seul alias_name par `alias_label`.  
* `PROPERTIES` : Une chaîne de caractères ou une structure de champs à rendre disponibles en tant que propriétés de personnalisation dans votre Canvas. Elle doit contenir des informations spécifiques à l'utilisateur.

{% alert note %}
Les propriétés ne sont pas obligatoires pour chaque ligne ou utilisateur. Cependant, les valeurs des propriétés doivent être des chaînes de caractères JSON valides. Saisissez une chaîne `{}` vide s'il n'y a aucune propriété pour la ligne.
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

##### Étape 1.3 : Configurer les informations d'identification 

Créez un jeton d'accès personnel dans Databricks :

1. Sélectionnez votre nom d'utilisateur, puis choisissez **User Settings.**  
2. Dans l'onglet **Access tokens**, sélectionnez **Generate new token.**  
3. Ajoutez un commentaire pour identifier le jeton, par exemple « Braze CDI ».  
4. Laissez le champ **Lifetime (days)** vide pour qu'il n'y ait pas d'expiration, puis sélectionnez **Generate**.  
5. Copiez et enregistrez le jeton en lieu sûr pour l'utiliser dans le tableau de bord de Braze.

##### Étape 1.4 : Configurer les politiques réseau 

Si votre compte est soumis à des politiques réseau, ajoutez les adresses IP de Braze à la liste d'autorisation afin de permettre la connexion au service CDI. Pour obtenir la liste des adresses IP, consultez [Ingestion de données cloud]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=databricks#step-13-allow-access-to-braze-ips).

{% endtab %}
{% tab Fabric %}

##### Étape 1.1 : Configurer votre table source dans Fabric

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

##### Étape 1.2 : Configurer les informations d'identification 

Créez un principal de service et accordez-lui les autorisations nécessaires. Si vous disposez déjà d'identifiants provenant d'une autre synchronisation, vous pouvez les réutiliser — assurez-vous simplement qu'ils ont accès à la table des comptes.

##### Étape 1.3 : Configurer les politiques réseau 

Si votre compte est soumis à des politiques réseau, ajoutez les adresses IP de Braze à la liste d'autorisation afin de permettre la connexion au service CDI. Pour obtenir la liste des adresses IP, consultez [Ingestion de données cloud]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=microsoft%20fabric#step-15-allow-braze-ips-in-firewall-optional).

{% endtab %}
{% tab File Storage %}

Pour synchroniser les déclencheurs Canvas à partir du stockage de fichiers, créez un fichier source contenant les champs suivants.

| Champ | Requis | Description |
| :---- | :---- | :---- |
| `EXTERNAL_ID` | Oui, `external_id` ou `alias_name` et `alias_label` | Identifie l'utilisateur que vous souhaitez mettre à jour. Cette valeur doit correspondre à la valeur `external_id` utilisée dans Braze. |
| `ALIAS_NAME` et `ALIAS_LABEL` | Oui, `external_id` ou `alias_name` et `alias_label` | Ces deux colonnes créent un objet d'alias d'utilisateur. `alias_name` doit être un identifiant unique et `alias_label` spécifie le type d'alias. Les utilisateurs peuvent avoir plusieurs alias avec des libellés différents, mais un seul `alias_name` par `alias_label`. |
| `PROPERTIES` | Oui | Chaîne de caractères JSON des champs à rendre disponibles en tant que propriétés de personnalisation dans votre Canvas. Elle doit contenir des informations spécifiques à l'utilisateur. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert tip %}
Les noms de fichiers doivent respecter les règles AWS et être uniques. Ajoutez des horodatages pour garantir l'unicité. Pour en savoir plus sur la synchronisation Amazon S3, consultez [Intégrations de stockage de fichiers](https://www.braze.com/docs/user_guide/data/cloud_ingestion/file_storage_integrations).
{% endalert %}

{% endtab %}
{% endtabs %}

#### Étape 2 : Configurer votre Canvas de destination

1. Configurez votre Canvas de destination pour les déclencheurs Canvas. Créez un nouveau Canvas déclenché par API ou sélectionnez-en un existant. Consultez [Types de planification d'entrée]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas#entry-schedule-types) pour savoir comment créer un Canvas avec un type de planification de réception déclenché par API.
2. Après avoir sélectionné le type de planification de réception déclenché par API, poursuivez la configuration et créez votre Canvas. Les Canvas peuvent aller de simples envois de messages uniques à des workflows clients complexes comportant plusieurs étapes.
3. Dans vos étapes du Canvas, utilisez les [propriétés d'entrée Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties) pour personnaliser les messages avec les champs de propriétés que vous prévoyez de synchroniser depuis votre table source.
  * Par exemple, si à l'étape 1 vous avez instrumenté un champ de propriétés pour `account_balance`, vous utiliseriez le modèle Liquid suivant pour personnaliser votre message : `\{\{canvas_entry_properties.\$\{account_balance\}\}\}`.
5. Une fois votre Canvas créé, lancez-le et passez à [l'étape 3](#step-3-create-your-zero-copy-sync).

#### Étape 3 : Créer votre synchronisation sans copie

Une fois la configuration de la source terminée et le Canvas de destination lancé, créez une nouvelle synchronisation de données :

1. Dans Braze, accédez à **Paramètres des données** > **Ingestion de données cloud**.
1. Configurez la connexion en saisissant les informations de connexion (ou en réutilisant les identifiants existants) et la table source de [l'étape 1](#step-1-set-up-data-source-for-canvas-triggers).
2. Attribuez un nom à l'intégration.
3. Sélectionnez le type de données **Canvas triggers**.
4. Choisissez votre Canvas de destination (depuis [l'étape 2](#step-2-configure-your-destination-canvas)).
5. Choisissez une fréquence de synchronisation.
6. Configurez vos préférences de notification.
7. Sélectionnez **Test Connection** pour vérifier que tout fonctionne correctement. Si vous vous connectez à Snowflake, ajoutez d'abord la clé publique affichée sur le tableau de bord à l'utilisateur créé pour permettre à Braze de se connecter à Snowflake. Pour cette étape, vous devez disposer d'un accès **SECURITYADMIN** ou supérieur dans Snowflake. 
8. Enregistrez la synchronisation pour commencer à synchroniser les déclencheurs Canvas.

Lorsque la synchronisation s'exécute, les utilisateurs de votre table source commencent à entrer dans le Canvas. Utilisez les analyses Canvas et la page des journaux de synchronisation de l'ingestion de données cloud pour surveiller les performances.

{% alert tip %}  
Vérifiez l'ensemble de votre configuration (du comportement de synchronisation à la configuration du Canvas) afin d'éviter tout envoi inattendu. Les paramètres Canvas tels que la limite de débit, la limite de fréquence et les filtres de segmentation permettent d'affiner davantage la distribution des messages.<br><br>Nous vous recommandons d'effectuer un essai avec une audience restreinte ou de test avant de mettre en œuvre des cas d'utilisation en production.
{% endalert %}

### Considérations

Les déclencheurs CDI Canvas utilisent votre limite de débit de l'API REST pour `/canvas/trigger/send`. Si vous utilisez cet endpoint simultanément avec les déclencheurs CDI Canvas et votre intégration API REST, l'utilisation combinée sera comptabilisée dans votre limite de débit.

Les déclencheurs CDI Canvas étant en accès anticipé, prenez en compte les détails suivants :

* Jusqu'à 5 synchronisations de déclencheurs Canvas actives par espace de travail  
* Chaque exécution de synchronisation fait entrer les utilisateurs dans leur Canvas de destination respectif à un rythme maximal d'environ 3,75 millions d'utilisateurs par heure.  
  * Préparez-vous à des délais plus longs entre la source et l'entrée dans le Canvas lorsque :  
    * Vous synchronisez plus de 3,75 millions d'utilisateurs par cycle de synchronisation.  
    * Vous utilisez les déclencheurs CDI Canvas alors que la [limite de débit de votre API REST pour `/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/#rate-limit) est déjà saturée.