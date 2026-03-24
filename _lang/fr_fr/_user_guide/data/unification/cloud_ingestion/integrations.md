---
nav_title: Intégration des entrepôts de données
article_title: Intégration de l'entrepôt de données
alias: /partners/databricks/
description: "Cette page explique comment utiliser l'ingestion de données cloud de Braze pour synchroniser des données pertinentes avec votre intégration Snowflake, Redshift, BigQuery et Databricks."
page_order: 2
page_type: reference

---

# Intégration de l'entrepôt de données

> Cette page explique comment utiliser l'ingestion de données cloud (CDI) de Braze pour synchroniser des données pertinentes avec votre intégration Snowflake, Redshift, BigQuery et Databricks.

Cette page présente les étapes de synchronisation et de source actuellement en accès anticipé (EA). Pour les étapes et les images de l'expérience en disponibilité générale, consultez [Expérience en disponibilité générale](#exprience-en-disponibilit-gnrale).

## Mise en place des intégrations d'entrepôts de données

Les intégrations d'ingestion de données cloud nécessitent une configuration côté Braze et dans votre instance d'entrepôt de données. Suivez ces étapes pour configurer votre intégration :

{% tabs %}
{% tab Snowflake %}
1. Dans votre instance Snowflake, configurez les tables ou les vues que vous souhaitez synchroniser avec Braze.
2. Créez une nouvelle source Snowflake dans le tableau de bord de Braze.
3. Récupérez la clé publique fournie dans le tableau de bord de Braze et [ajoutez-la à l'utilisateur Snowflake pour l'authentification](https://docs.snowflake.com/en/user-guide/key-pair-auth.html).
4. Créez une synchronisation dans le tableau de bord de Braze, testez l'intégration et démarrez la synchronisation.

{% alert tip %}
Le [guide de démarrage rapide de Snowflake](https://quickstarts.snowflake.com/guide/braze_cdi/index.html) fournit un exemple de code et présente les étapes requises pour créer un pipeline automatisé utilisant Snowflake Streams et CDI pour synchroniser les données vers Braze.
{% endalert %}
{% endtab %}
{% tab Redshift %}
1. Assurez-vous que l'accès à Braze est autorisé pour les tables Redshift que vous souhaitez synchroniser. Braze se connecte à Redshift via Internet.
2. Dans votre instance Redshift, configurez les tables ou les vues que vous souhaitez synchroniser avec Braze.
3. Créez une nouvelle source et une synchronisation dans le tableau de bord de Braze.
4. Testez l'intégration et démarrez la synchronisation.
{% endtab %}
{% tab BigQuery %}
1. Créez un compte de service et autorisez l'accès au(x) projet(s) BigQuery et au(x) jeu(x) de données contenant les données que vous souhaitez synchroniser.  
2. Dans votre compte BigQuery, configurez les tables ou les vues que vous souhaitez synchroniser avec Braze.   
3. Créez une nouvelle source et une synchronisation dans le tableau de bord de Braze.  
4. Testez l'intégration et démarrez la synchronisation. 
{% endtab %}
{% tab Databricks %}
1. Créez un compte de service et autorisez l'accès au(x) projet(s) et jeu(x) de données Databricks contenant les données que vous souhaitez synchroniser.  
2. Dans votre compte Databricks, configurez les tables ou les vues que vous souhaitez synchroniser avec Braze.   
3. Créez une nouvelle source et une synchronisation dans le tableau de bord de Braze.
4. Testez l'intégration et démarrez la synchronisation.

{% alert important %}
Il peut y avoir un temps de préchauffage de deux à cinq minutes lorsque Braze se connecte aux instances SQL Classic et Pro, ce qui peut entraîner des retards lors de la configuration et des tests de connexion, ainsi qu'au début des synchronisations planifiées. L'utilisation d'une instance SQL serverless permet de réduire ce temps de préchauffage et d'améliorer le débit des requêtes, mais peut entraîner des coûts d'intégration légèrement plus élevés.
{% endalert %}

{% endtab %}
{% tab Microsoft Fabric %}
1. Créez un principal de service et autorisez l'accès aux API Fabric.
2. Configurez un espace de travail partagé et accordez au principal de service l'accès à celui-ci.
3. Dans l'espace de travail Fabric partagé, configurez les tables ou les vues que vous souhaitez synchroniser avec Braze.   
4. Créez une nouvelle source et une synchronisation dans le tableau de bord de Braze.  
5. Testez l'intégration et démarrez la synchronisation.
{% endtab %}
{% endtabs %}

### Étape 1 : Configurer les tables ou les vues

{% tabs %}
{% tab Snowflake %}

#### Étape 1.1 : Configurer la table

```sql
CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
CREATE OR REPLACE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC (
     UPDATED_AT TIMESTAMP_NTZ(9) NOT NULL DEFAULT SYSDATE(),
     --at least one of external_id, alias_name and alias_label, email, phone, or braze_id is required  
     EXTERNAL_ID VARCHAR(16777216),
     --if using user alias, both alias_name and alias_label are required
     ALIAS_LABEL VARCHAR(16777216),
     ALIAS_NAME VARCHAR(16777216),
     --braze_id can only be used to update existing users created through the Braze SDK
     BRAZE_ID VARCHAR(16777216),
     --If you include both email and phone, email is used as the primary identifier
     EMAIL VARCHAR(16777216),
     PHONE VARCHAR(16777216),
     PAYLOAD VARCHAR(16777216) NOT NULL
);
```

Vous pouvez nommer la base de données, le schéma et la table comme vous le souhaitez, mais les noms de colonnes doivent correspondre à la définition ci-dessus.

- `UPDATED_AT` : L'heure à laquelle cette ligne a été mise à jour ou ajoutée à la table. Braze synchronise les lignes dont la valeur `UPDATED_AT` est postérieure à la dernière valeur synchronisée. Les lignes situées exactement à l'horodatage limite peuvent être re-synchronisées si de nouvelles lignes partagent ce même horodatage.
- **Colonnes d'identification de l'utilisateur** : Votre table peut contenir une ou plusieurs colonnes d'identification de l'utilisateur. Chaque ligne ne doit contenir qu'un seul identifiant (soit `external_id`, la combinaison de `alias_name` et `alias_label`, `braze_id`, `email` ou `phone`). Une table source peut comporter des colonnes pour un, deux, trois, quatre ou les cinq types d'identifiants.
    - `EXTERNAL_ID` : Identifie l'utilisateur que vous souhaitez mettre à jour. Cette valeur doit correspondre à la valeur `external_id` utilisée dans Braze. 
    - `ALIAS_NAME` et `ALIAS_LABEL` : Ces deux colonnes créent un objet d'alias d'utilisateur. `alias_name` doit être un identifiant unique et `alias_label` spécifie le type d'alias. Les utilisateurs peuvent avoir plusieurs alias avec différentes étiquettes, mais un seul `alias_name` par `alias_label`.
    - `BRAZE_ID` : L'identifiant utilisateur Braze. Celui-ci est généré par le SDK Braze, et il n'est pas possible de créer de nouveaux utilisateurs à l'aide d'un ID Braze via l'ingestion de données cloud. Pour créer de nouveaux utilisateurs, spécifiez un ID utilisateur externe ou un alias d'utilisateur.
    - `EMAIL` : L'adresse e-mail de l'utilisateur. Si plusieurs profils avec la même adresse e-mail existent, le profil le plus récemment mis à jour est prioritaire. Si vous incluez à la fois l'e-mail et le téléphone, l'e-mail est utilisé comme identifiant principal.
    - `PHONE` : Le numéro de téléphone de l'utilisateur. Si plusieurs profils avec le même numéro de téléphone existent, le profil le plus récemment mis à jour est prioritaire.
- `PAYLOAD` : Il s'agit d'une chaîne de caractères JSON des champs que vous souhaitez synchroniser avec l'utilisateur dans Braze.

#### Étape 1.2 : Définir le rôle et les autorisations de la base de données

```sql
CREATE ROLE BRAZE_INGESTION_ROLE;

GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC TO ROLE BRAZE_INGESTION_ROLE;
```

Modifiez les noms si nécessaire, mais les autorisations doivent correspondre à l'exemple ci-dessus.

#### Étape 1.3 : Configurer l'entrepôt et donner accès au rôle Braze

```sql
CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;

GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;
```

{% alert note %}
L'entrepôt doit avoir l'option de **reprise automatique** activée. Si ce n'est pas le cas, accordez à Braze des privilèges `OPERATE` supplémentaires sur l'entrepôt pour que Braze puisse l'activer au moment de l'exécution de la requête.
{% endalert %}

#### Étape 1.4 : Configurer l'utilisateur

```sql
CREATE USER BRAZE_INGESTION_USER;

GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
```

Après cette étape, partagez les informations de connexion avec Braze pour recevoir une clé publique à ajouter à l'utilisateur.

{% alert note %}
Lorsque vous connectez différents espaces de travail au même compte Snowflake, vous devez créer un utilisateur unique pour chaque espace de travail Braze dans lequel vous créez une intégration. Au sein d'un espace de travail, vous pouvez réutiliser le même utilisateur entre les intégrations, mais la création d'une intégration échoue si un utilisateur du même compte Snowflake est dupliqué entre les espaces de travail.
{% endalert %}

#### Étape 1.5 : Autoriser les IP de Braze dans la politique réseau de Snowflake (facultatif)

Selon la configuration de votre compte Snowflake, vous devrez peut-être autoriser les adresses IP suivantes dans votre politique réseau Snowflake. Pour plus d'informations, consultez la documentation Snowflake sur la [modification d'une politique réseau](https://docs.snowflake.com/en/user-guide/network-policies.html#modifying-network-policies).

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}
{% tab Redshift %}

#### Étape 1.1 : Configurer la table 

Optionnellement, créez une nouvelle base de données et un nouveau schéma pour contenir votre table source
```sql
CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
```
Créez une table (ou vue) à utiliser pour votre intégration CDI
```sql
CREATE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC (
   updated_at timestamptz default sysdate,
   --at least one of external_id, alias_name and alias_label, or braze_id is required
   external_id varchar,
   --if using user alias, both alias_name and alias_label are required
   alias_label varchar,
   alias_name varchar,
   --braze_id can only be used to update existing users created through the Braze SDK
   braze_id varchar,
   --If you include both email and phone, email is used as the primary identifier
   email varchar,
   phone varchar,
   payload varchar(max)
)
```

Vous pouvez nommer la base de données, le schéma et la table comme vous le souhaitez, mais les noms de colonnes doivent correspondre à la définition ci-dessus.

- `UPDATED_AT` : L'heure à laquelle cette ligne a été mise à jour ou ajoutée à la table. Braze synchronise les lignes dont la valeur `UPDATED_AT` est postérieure à la dernière valeur synchronisée. Les lignes situées exactement à l'horodatage limite peuvent être re-synchronisées si de nouvelles lignes partagent ce même horodatage.
- **Colonnes d'identification de l'utilisateur** : Votre table peut contenir une ou plusieurs colonnes d'identification de l'utilisateur. Chaque ligne ne doit contenir qu'un seul identifiant (soit `external_id`, la combinaison de `alias_name` et `alias_label`, `braze_id`, `email` ou `phone`). Une table source peut comporter des colonnes pour un, deux, trois, quatre ou les cinq types d'identifiants.
    - `EXTERNAL_ID` : Identifie l'utilisateur que vous souhaitez mettre à jour. Cette valeur doit correspondre à la valeur `external_id` utilisée dans Braze. 
    - `ALIAS_NAME` et `ALIAS_LABEL` : Ces deux colonnes créent un objet d'alias d'utilisateur. `alias_name` doit être un identifiant unique et `alias_label` spécifie le type d'alias. Les utilisateurs peuvent avoir plusieurs alias avec différentes étiquettes, mais un seul `alias_name` par `alias_label`.
    - `BRAZE_ID` : L'identifiant utilisateur Braze. Celui-ci est généré par le SDK Braze, et il n'est pas possible de créer de nouveaux utilisateurs à l'aide d'un ID Braze via l'ingestion de données cloud. Pour créer de nouveaux utilisateurs, spécifiez un ID utilisateur externe ou un alias d'utilisateur.
    - `EMAIL` : L'adresse e-mail de l'utilisateur. Si plusieurs profils avec la même adresse e-mail existent, le profil le plus récemment mis à jour est prioritaire. Si vous incluez à la fois l'e-mail et le téléphone, l'e-mail est utilisé comme identifiant principal.
    - `PHONE` : Le numéro de téléphone de l'utilisateur. Si plusieurs profils avec le même numéro de téléphone existent, le profil le plus récemment mis à jour est prioritaire.
- `PAYLOAD` : Il s'agit d'une chaîne de caractères JSON des champs que vous souhaitez synchroniser avec l'utilisateur dans Braze.
 
#### Étape 1.2 : Créer un utilisateur et accorder les autorisations

```sql
CREATE USER braze_user PASSWORD '{password}';
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT SELECT ON TABLE USERS_ATTRIBUTES_SYNC TO braze_user;
```

Il s'agit des autorisations minimales requises pour cet utilisateur. Si vous créez plusieurs intégrations CDI, vous pouvez accorder des autorisations au niveau du schéma ou gérer les autorisations à l'aide d'un groupe. 

#### Étape 1.3 : Autoriser l'accès aux IP de Braze

Si vous avez un pare-feu ou d'autres politiques réseau, vous devez donner à Braze un accès réseau à votre instance Redshift. Un exemple d'endpoint URL Redshift est « example-cluster.ap-northeast-2.redshift.amazonaws.com ».

Points importants à connaître :
- Vous devrez peut-être également modifier vos groupes de sécurité pour permettre à Braze d'accéder à vos données dans Redshift.
- Veillez à autoriser explicitement le trafic entrant sur les IP du tableau et sur le port utilisé pour interroger votre cluster Redshift (5439 par défaut). Vous devez explicitement autoriser la connectivité TCP Redshift sur ce port, même si les règles d'entrée sont définies sur « Autoriser tout ».
- L'endpoint du cluster Redshift doit être accessible publiquement pour que Braze puisse se connecter à votre cluster.
     - Si vous ne souhaitez pas que votre cluster Redshift soit accessible publiquement, vous pouvez configurer un VPC et une instance EC2 pour utiliser un tunnel SSH afin d'accéder aux données Redshift. Pour plus d'informations, consultez cet [article du Centre de connaissances AWS](https://repost.aws/knowledge-center/private-redshift-cluster-local-machine).
 
Autorisez l'accès à partir des IP suivantes correspondant à la région de votre tableau de bord de Braze.

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}
{% tab BigQuery %}

#### Étape 1.1 : Configurer la table 

Optionnellement, créez un nouveau projet ou jeu de données pour contenir votre table source.

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

Créez une ou plusieurs tables à utiliser pour votre intégration CDI avec les champs suivants :

```sql
CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC`
(
  updated_at TIMESTAMP DEFAULT current_timestamp,
  --At least one of external_id, alias_name and alias_label, or braze_id is required  
  external_id STRING,
  --If using user alias, both alias_name and alias_label are required
  alias_name STRING,
  alias_label STRING,
  --braze_id can only be used to update existing users created through the Braze SDK
  braze_id STRING,
  --If you include both email and phone, email is used as the primary identifier
  email STRING,
  phone STRING,
  payload JSON
);
```

| Nom du champ | Type | Mode |
|---|---|---|
| `UPDATED_AT`| TIMESTAMP | REQUIS |
| `PAYLOAD`| JSON | REQUIS |
| `EXTERNAL_ID`| STRING | NULLABLE |
| `ALIAS_NAME`| STRING | NULLABLE |
| `ALIAS_LABEL`| STRING | NULLABLE |
| `BRAZE_ID`| STRING | NULLABLE |
| `EMAIL`| STRING | NULLABLE |
| `PHONE`| STRING | NULLABLE |

Vous pouvez nommer le projet, le jeu de données et la table comme vous le souhaitez, mais les noms de colonnes doivent correspondre à la définition ci-dessus.

- `UPDATED_AT` : L'heure à laquelle cette ligne a été mise à jour ou ajoutée à la table. Braze synchronise les lignes dont la valeur `UPDATED_AT` est postérieure à la dernière valeur synchronisée. Les lignes situées exactement à l'horodatage limite peuvent être re-synchronisées si de nouvelles lignes partagent ce même horodatage.
- **Colonnes d'identification de l'utilisateur** : Votre table peut contenir une ou plusieurs colonnes d'identification de l'utilisateur. Chaque ligne ne doit contenir qu'un seul identifiant (soit `external_id`, la combinaison de `alias_name` et `alias_label`, `braze_id`, `email` ou `phone`). Une table source peut comporter des colonnes pour un, deux, trois, quatre ou les cinq types d'identifiants.
    - `EXTERNAL_ID` : Identifie l'utilisateur que vous souhaitez mettre à jour. Cette valeur doit correspondre à la valeur `external_id` utilisée dans Braze. 
    - `ALIAS_NAME` et `ALIAS_LABEL` : Ces deux colonnes créent un objet d'alias d'utilisateur. `alias_name` doit être un identifiant unique et `alias_label` spécifie le type d'alias. Les utilisateurs peuvent avoir plusieurs alias avec différentes étiquettes, mais un seul `alias_name` par `alias_label`.
    - `BRAZE_ID` : L'identifiant utilisateur Braze. Celui-ci est généré par le SDK Braze, et il n'est pas possible de créer de nouveaux utilisateurs à l'aide d'un ID Braze via l'ingestion de données cloud. Pour créer de nouveaux utilisateurs, spécifiez un ID utilisateur externe ou un alias d'utilisateur.
    - `EMAIL` : L'adresse e-mail de l'utilisateur. Si plusieurs profils avec la même adresse e-mail existent, le profil le plus récemment mis à jour est prioritaire. Si vous incluez à la fois l'e-mail et le téléphone, l'e-mail est utilisé comme identifiant principal.
    - `PHONE` : Le numéro de téléphone de l'utilisateur. Si plusieurs profils avec le même numéro de téléphone existent, le profil le plus récemment mis à jour est prioritaire.
- `PAYLOAD` : Il s'agit d'une chaîne de caractères JSON des champs que vous souhaitez synchroniser avec l'utilisateur dans Braze.

{% alert important %}
**Partitionnement BigQuery**

CDI prend en charge les partitions pour BigQuery. Si vous partitionnez en fonction de `UPDATED_AT` (par exemple, à la granularité d'un jour, d'une semaine ou d'une heure, selon la taille de votre jeu de données), BigQuery peut élaguer les données à analyser. Cela améliore les performances et l'efficacité pour les très grandes tables.

Ne partitionnez pas selon d'autres champs. Testez différentes configurations pour trouver celle qui convient le mieux à vos données.

Toutes les requêtes CDI filtrent par `UPDATED_AT`, mais ce comportement pourrait changer. Concevez votre schéma de table de manière à _ne pas_ exiger que les requêtes incluent cette clause.

Pour plus d'informations, consultez la [documentation sur le partitionnement BigQuery](https://docs.cloud.google.com/bigquery/docs/partitioned-tables).
{% endalert %}

#### Étape 1.2 : Créer un compte de service et accorder les autorisations 

Créez un compte de service dans GCP que Braze utilisera pour se connecter et lire les données de votre/vos table(s). Le compte de service doit disposer des autorisations suivantes : 

- **BigQuery Connection User :** Permet à Braze d'établir des connexions.
- **BigQuery User :** Donne à Braze l'accès pour exécuter des requêtes, lire les métadonnées des jeux de données et lister les tables.
- **BigQuery Data Viewer :** Donne à Braze l'accès pour visualiser les jeux de données et leur contenu.
- **BigQuery Job User :** Donne à Braze l'accès pour exécuter des tâches.

Après avoir créé le compte de service et accordé les autorisations, générez une clé JSON. Pour plus d'informations, consultez [Créer et supprimer des clés de compte de service](https://cloud.google.com/iam/docs/keys-create-delete). Vous chargerez cette clé dans le tableau de bord de Braze lors d'une étape ultérieure. 

#### Étape 1.3 : Autoriser l'accès aux IP de Braze    

Si vous avez des politiques réseau en place, vous devez donner à Braze un accès réseau à votre instance BigQuery. Autorisez l'accès à partir des IP suivantes correspondant à la région de votre tableau de bord de Braze.  

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}
{% tab Databricks %}

#### Étape 1.1 : Configurer la table 

Optionnellement, créez un nouveau catalogue ou schéma pour contenir votre table source.

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

Créez une ou plusieurs tables à utiliser pour votre intégration CDI avec les champs suivants :


```sql
CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC`
(
  updated_at TIMESTAMP DEFAULT current_timestamp(),
  --At least one of external_id, alias_name and alias_label, or braze_id is required  
  external_id STRING,
  --If using user alias, both alias_name and alias_label are required
  alias_name STRING,
  alias_label STRING,
  --braze_id can only be used to update existing users created through the Braze SDK
  braze_id STRING,
  --If you include both email and phone, email is used as the primary identifier
  email STRING,
  phone STRING,
  payload STRING, STRUCT, or MAP
);
```


| Nom du champ | Type | Mode |
|---|---|---|
| `UPDATED_AT`| TIMESTAMP | REQUIS |
| `PAYLOAD`| STRING, STRUCT ou MAP | REQUIS |
| `EXTERNAL_ID`| STRING | NULLABLE |
| `ALIAS_NAME`| STRING | NULLABLE |
| `ALIAS_LABEL`| STRING | NULLABLE |
| `BRAZE_ID`| STRING | NULLABLE |
| `EMAIL`| STRING | NULLABLE |
| `PHONE`| STRING | NULLABLE |

Vous pouvez nommer le schéma et la table comme vous le souhaitez, mais les noms de colonnes doivent correspondre à la définition ci-dessus.

- `UPDATED_AT` : L'heure à laquelle cette ligne a été mise à jour ou ajoutée à la table. Braze synchronise les lignes dont la valeur `UPDATED_AT` est postérieure à la dernière valeur synchronisée. Les lignes situées exactement à l'horodatage limite peuvent être re-synchronisées si de nouvelles lignes partagent ce même horodatage.
- **Colonnes d'identification de l'utilisateur** : Votre table peut contenir une ou plusieurs colonnes d'identification de l'utilisateur. Chaque ligne ne doit contenir qu'un seul identifiant (soit `external_id`, la combinaison de `alias_name` et `alias_label`, `braze_id`, `email` ou `phone`). Une table source peut comporter des colonnes pour un, deux, trois, quatre ou les cinq types d'identifiants.
    - `EXTERNAL_ID` : Identifie l'utilisateur que vous souhaitez mettre à jour. Cette valeur doit correspondre à la valeur `external_id` utilisée dans Braze. 
    - `ALIAS_NAME` et `ALIAS_LABEL` : Ces deux colonnes créent un objet d'alias d'utilisateur. `alias_name` doit être un identifiant unique et `alias_label` spécifie le type d'alias. Les utilisateurs peuvent avoir plusieurs alias avec différentes étiquettes, mais un seul `alias_name` par `alias_label`.
    - `BRAZE_ID` : L'identifiant utilisateur Braze. Celui-ci est généré par le SDK Braze, et il n'est pas possible de créer de nouveaux utilisateurs à l'aide d'un ID Braze via l'ingestion de données cloud. Pour créer de nouveaux utilisateurs, spécifiez un ID utilisateur externe ou un alias d'utilisateur. 
    - `EMAIL` : L'adresse e-mail de l'utilisateur. Si plusieurs profils avec la même adresse e-mail existent, le profil le plus récemment mis à jour est prioritaire. Si vous incluez à la fois l'e-mail et le téléphone, l'e-mail est utilisé comme identifiant principal.
    - `PHONE` : Le numéro de téléphone de l'utilisateur. Si plusieurs profils avec le même numéro de téléphone existent, le profil le plus récemment mis à jour est prioritaire.
- `PAYLOAD` : Il s'agit d'une chaîne de caractères ou d'une structure des champs que vous souhaitez synchroniser avec l'utilisateur dans Braze.

#### Étape 1.2 : Créer un jeton d'accès  

Pour que Braze puisse accéder à Databricks, un jeton d'accès personnel doit être créé.

1. Dans votre espace de travail Databricks, sélectionnez votre nom d'utilisateur Databricks dans la barre supérieure, puis sélectionnez **User Settings** dans le menu déroulant.
2. Dans l'onglet Jetons d'accès, sélectionnez **Generate new token**.
3. Saisissez un commentaire pour identifier ce jeton, par exemple « Braze CDI », et définissez la durée de vie du jeton sur illimitée en laissant la case Durée de vie (jours) vide.
4. Sélectionnez **Generate**.
5. Copiez le jeton affiché, puis sélectionnez **Done**.

Conservez le jeton en lieu sûr jusqu'à ce que vous ayez besoin de le saisir dans le tableau de bord de Braze lors de l'étape de création des identifiants.

#### Étape 1.3 : Autoriser l'accès aux IP de Braze    

Si vous avez des politiques réseau en place, vous devez donner à Braze un accès réseau à votre instance Databricks. Autorisez l'accès à partir des IP suivantes correspondant à la région de votre tableau de bord de Braze.  

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}
{% tab Microsoft Fabric %}

#### Étape 1.1 : Configurer le principal de service et accorder l'accès
Braze se connecte à votre entrepôt Fabric à l'aide d'un principal de service avec une authentification Entra ID. Créez un nouveau principal de service dédié à Braze et accordez l'accès aux ressources Fabric selon les besoins. Braze a besoin des informations suivantes pour se connecter :    

* ID de locataire (également appelé répertoire) de votre compte Azure 
* ID du principal (également appelé ID d'application) pour le principal de service 
* Secret client pour l'authentification de Braze

1. Dans le portail Azure, accédez au centre d'administration Microsoft Entra, puis à Inscriptions d'applications. 
2. Sélectionnez **+ New registration** sous **Identity** > **Applications** > **App registrations**.
3. Saisissez un nom, puis sélectionnez `Accounts in this organizational directory only` comme type de compte pris en charge. Sélectionnez ensuite **Register**. 
4. Sélectionnez l'application (principal de service) que vous venez de créer, puis accédez à **Certificates & secrets** > **+ New client secret**.
5. Saisissez une description et une période d'expiration pour le secret. Sélectionnez ensuite **Add**. 
6. Notez le secret client créé pour l'utiliser dans la configuration de Braze. 

{% alert note %}
Azure n'autorise pas l'expiration illimitée des secrets de principaux de service. N'oubliez pas d'actualiser les identifiants avant leur expiration afin de maintenir le flux de données vers Braze.
{% endalert %}

#### Étape 1.2 : Accorder l'accès aux ressources Fabric 
Accordez à Braze l'accès pour se connecter à votre instance Fabric. Dans votre portail d'administration Fabric, accédez à **Settings** > **Governance and insights** > **Admin portal** > **Tenant settings**.    

* Dans **Developer settings**, activez **Service principals can use Fabric APIs** pour que Braze puisse se connecter via Microsoft Entra ID.
* Dans **OneLake settings**, activez **Users can access data stored in OneLake with apps external to Fabric** pour que le principal de service puisse accéder aux données depuis une application externe.

#### Étape 1.3 : Configurer un espace de travail partagé et accorder l'accès

Toutes les ressources Fabric que vous souhaitez connecter à Braze doivent être placées dans un espace de travail partagé. Si vous n'avez utilisé que l'espace **My Workspace** par défaut, créez un nouvel espace de travail partagé :

1. Dans le menu de navigation, sélectionnez **Workspaces**, puis sélectionnez **+ New workspace**.
2. Saisissez un **nom** pour l'espace de travail, puis sélectionnez **Apply**.

Une fois l'espace de travail partagé créé, accordez l'accès au principal de service :

1. Sélectionnez l'espace de travail, puis sélectionnez **Manage Access**.
2. Sélectionnez **+ Add people or groups**.
3. Recherchez et sélectionnez le nom du principal de service créé à l'étape 1.1. S'il n'apparaît pas, vérifiez que vous avez activé le paramètre **Service principals can use Fabric APIs** à l'étape 1.2.
4. Dans le menu déroulant des rôles, sélectionnez **Contributor**.

Le principal de service peut désormais accéder aux ressources de l'entrepôt Fabric dans cet espace de travail via leurs endpoints SQL, y compris l'entrepôt à utiliser pour Braze.

#### Étape 1.4 : Configurer la table
Braze prend en charge les tables et les vues dans les entrepôts Fabric. Si vous devez créer un nouvel entrepôt, créez-le dans l'espace de travail partagé de l'étape 1.3. Accédez à **Create > Data Warehouse > Warehouse** dans la console Fabric.

```sql
CREATE OR ALTER TABLE [warehouse].[schema].[CDI_table_name] 
(
  UPDATED_AT DATETIME2(6) NOT NULL,
  PAYLOAD VARCHAR NOT NULL,
  --at least one of external_id, alias_name and alias_label, email, phone, or braze_id is required  
  EXTERNAL_ID VARCHAR,
  --if using user alias, both alias_name and alias_label are required
  ALIAS_NAME VARCHAR,
  ALIAS_LABEL VARCHAR,
  --braze_id can only be used to update existing users created through the Braze SDK
  BRAZE_ID VARCHAR,
  --If you include both email and phone, email is used as the primary identifier
  EMAIL VARCHAR,
  PHONE VARCHAR
)
GO
```

Vous pouvez nommer l'entrepôt, le schéma et la table ou vue comme vous le souhaitez, mais les noms de colonnes doivent correspondre à la définition ci-dessus.

- `UPDATED_AT` : L'heure à laquelle cette ligne a été mise à jour ou ajoutée à la table. Braze synchronise les lignes dont la valeur `UPDATED_AT` est postérieure à la dernière valeur synchronisée. Les lignes situées exactement à l'horodatage limite peuvent être re-synchronisées si de nouvelles lignes partagent ce même horodatage.
- **Colonnes d'identification de l'utilisateur** : Votre table peut contenir une ou plusieurs colonnes d'identification de l'utilisateur. Chaque ligne ne doit contenir qu'un seul identifiant (soit `external_id`, la combinaison de `alias_name` et `alias_label`, `braze_id`, `email` ou `phone`). Une table source peut comporter des colonnes pour un, deux, trois, quatre ou les cinq types d'identifiants.
    - `EXTERNAL_ID` : Identifie l'utilisateur que vous souhaitez mettre à jour. Cette valeur doit correspondre à la valeur `external_id` utilisée dans Braze. 
    - `ALIAS_NAME` et `ALIAS_LABEL` : Ces deux colonnes créent un objet d'alias d'utilisateur. `alias_name` doit être un identifiant unique et `alias_label` spécifie le type d'alias. Les utilisateurs peuvent avoir plusieurs alias avec différentes étiquettes, mais un seul `alias_name` par `alias_label`.
    - `BRAZE_ID` : L'identifiant utilisateur Braze. Celui-ci est généré par le SDK Braze, et il n'est pas possible de créer de nouveaux utilisateurs à l'aide d'un ID Braze via l'ingestion de données cloud. Pour créer de nouveaux utilisateurs, spécifiez un ID utilisateur externe ou un alias d'utilisateur.
    - `EMAIL` : L'adresse e-mail de l'utilisateur. Si plusieurs profils avec la même adresse e-mail existent, le profil le plus récemment mis à jour est prioritaire. Si vous incluez à la fois l'e-mail et le téléphone, l'e-mail est utilisé comme identifiant principal.
    - `PHONE` : Le numéro de téléphone de l'utilisateur. Si plusieurs profils avec le même numéro de téléphone existent, le profil le plus récemment mis à jour est prioritaire.
- `PAYLOAD` : Il s'agit d'une chaîne de caractères JSON des champs que vous souhaitez synchroniser avec l'utilisateur dans Braze.


#### Étape 1.5 : Obtenir la chaîne de connexion de l'entrepôt
Pour récupérer l'endpoint SQL de votre entrepôt, accédez à l'**espace de travail** dans Fabric, survolez le nom de l'entrepôt dans la liste des éléments et sélectionnez **Copy SQL connection string**.

![La page « Fabric Console » dans Microsoft Azure, où les utilisateurs doivent récupérer la chaîne de connexion SQL.]({% image_buster /assets/img/cloud_ingestion/fabric_1.png %})


#### Étape 1.6 : Autoriser les IP de Braze dans le pare-feu (facultatif)

Selon la configuration de votre compte Microsoft Fabric, vous devrez peut-être autoriser les adresses IP suivantes dans votre pare-feu pour permettre le trafic en provenance de Braze. Pour plus d'informations, consultez la documentation sur l'[accès conditionnel Entra](https://learn.microsoft.com/en-us/fabric/security/protect-inbound-traffic#entra-conditional-access).

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}

{% endtabs %}

### Étape 2 : Créer une nouvelle source dans le tableau de bord de Braze

{% alert important %}
Les clients dont l'onboarding a lieu en février 2026 ou après peuvent bénéficier d'un accès anticipé à l'interface CDI avec des Sources et des Synchronisations séparées. Dans cette interface, créez d'abord une source avant de créer des synchronisations pour cette source. Plusieurs synchronisations peuvent utiliser la même source.
{% endalert %}

{% tabs %}
{% tab Snowflake %}

Dans le tableau de bord de Braze, accédez à **Data Settings** > **Cloud Data Ingestion** > **Sources**, sélectionnez **Add data source**, puis sélectionnez **Snowflake**.

#### Étape 2.1 : Ajouter les informations de connexion Snowflake

Choisissez un nom pour votre source et saisissez vos identifiants et votre configuration Snowflake, puis passez à l'étape suivante.

{% alert note %}
Dans le champ **Snowflake Account Locator**, saisissez l'[identifiant de compte](https://docs.snowflake.com/en/user-guide/admin-account-identifier) Snowflake, qui suit généralement un format tel que `xy12345.us-east-1.aws`. Il ne s'agit pas d'un nom de base de données ou d'entrepôt.
{% endalert %} 

#### Étape 2.2 : Ajouter une clé publique à l'utilisateur Braze

Après avoir saisi vos identifiants et votre configuration, cliquez sur **Save credentials** pour générer une clé RSA, puis retournez dans Snowflake pour terminer la configuration. Ajoutez la clé publique affichée sur le tableau de bord à l'utilisateur que vous avez créé pour que Braze se connecte à Snowflake.

Pour plus d'informations, consultez la [documentation Snowflake](https://docs.snowflake.com/en/user-guide/key-pair-auth.html). Si vous souhaitez effectuer une rotation des clés, Braze peut générer une nouvelle paire de clés et fournir la nouvelle clé publique.

```sql
ALTER USER BRAZE_INGESTION_USER SET RSA_PUBLIC_KEY='MIIBIjANBgkqhkiG9w0BA...';
```
{% endtab %}
{% tab Redshift %}

Dans le tableau de bord de Braze, accédez à **Data Settings** > **Cloud Data Ingestion** > **Sources**, sélectionnez **Add data source**, puis sélectionnez **Amazon Redshift**.

#### Étape 2.1 : Ajouter les informations de connexion Redshift et la table source

Choisissez un nom pour votre source et saisissez vos identifiants et votre configuration Redshift. Si vous utilisez un tunnel de réseau privé, activez le curseur et saisissez les informations du tunnel. Passez ensuite à l'étape suivante. 

{% alert note %}
Dans le tableau de bord de Braze, le champ **Database name** n'accepte que les lettres (A-Z, a-z), les chiffres (0-9) et les traits de soulignement (_), bien qu'Amazon Redshift prenne en charge des caractères supplémentaires dans les identifiants de base de données.
{% endalert %}

#### Étape 2.2 : Tester la connexion et se connecter à la source

Sélectionnez ensuite **Test connection**. En cas de succès, finalisez les paramètres restants et cliquez sur **Connect to Source**. Si la connexion échoue, un message d'erreur s'affiche pour vous aider à résoudre le problème.
{% endtab %}
{% tab BigQuery %}

Dans le tableau de bord de Braze, accédez à **Data Settings** > **Cloud Data Ingestion** > **Sources**, sélectionnez **Add data source**, puis sélectionnez **Google BigQuery**.

#### Étape 2.1 : Ajouter les informations de connexion BigQuery et la table source

Choisissez un nom pour votre source. Chargez ensuite la clé JSON et fournissez un nom pour le compte de service, puis saisissez les champs de configuration restants.

#### Étape 2.2 : Tester la connexion et se connecter à la source

Sélectionnez ensuite **Test connection**. En cas de succès, finalisez les paramètres restants et cliquez sur **Connect to Source**. Si la connexion échoue, un message d'erreur s'affiche pour vous aider à résoudre le problème.

{% endtab %}
{% tab Databricks %}

Dans le tableau de bord de Braze, accédez à **Data Settings** > **Cloud Data Ingestion** > **Sources**, sélectionnez **Add data source**, puis sélectionnez **Databricks**.

#### Étape 2.1 : Ajouter les informations de connexion Databricks et la table source

Choisissez un nom pour votre source et saisissez vos identifiants et votre configuration Databricks. Passez ensuite à l'étape suivante.

#### Étape 2.2 : Tester la connexion et se connecter à la source

Sélectionnez ensuite **Test connection**. En cas de succès, finalisez les paramètres restants et cliquez sur **Connect to Source**. Si la connexion échoue, un message d'erreur s'affiche pour vous aider à résoudre le problème.

{% alert note %}
Vous devez tester une source avec succès avant de pouvoir la créer. Si vous fermez la page de création, votre source n'est pas enregistrée.
{% endalert %}

{% endtab %}
{% tab Microsoft Fabric %}

Dans le tableau de bord de Braze, accédez à Data Settings > Cloud Data Ingestion > Sources, sélectionnez **Add data source**, puis sélectionnez **Microsoft Fabric**.

#### Étape 2.1 : Configurer une synchronisation d'ingestion de données cloud

Choisissez un nom pour votre source et saisissez vos identifiants et votre configuration Microsoft Fabric.
- **Credentials Name** est un libellé pour ces identifiants dans Braze ; vous pouvez y définir une valeur descriptive.
- Consultez les étapes de la section 1 pour savoir comment récupérer l'ID de locataire, l'ID du principal, le secret client et la chaîne de connexion.

#### Étape 2.2 : Tester la connexion et se connecter à la source

Sélectionnez ensuite **Test connection**. En cas de succès, finalisez les paramètres restants et cliquez sur **Connect to Source**. Si la connexion échoue, un message d'erreur s'affiche pour vous aider à résoudre le problème.

{% alert note %}
Vous devez tester une source avec succès avant de pouvoir la créer. Si vous fermez la page de création, votre source n'est pas enregistrée.
{% endalert %}

{% endtab %}

{% endtabs %}

### Étape 3 : Créer une nouvelle synchronisation dans le tableau de bord de Braze
Accédez à **Data Settings** > **Cloud Data Ingestion** > **Syncs**, et sélectionnez **Create data sync**.

{% tabs %}
{% tab Snowflake %}

#### Étape 3.1 : Configurer les détails de la synchronisation et tester la connexion
Choisissez un nom pour votre synchronisation. Sélectionnez ensuite une source active et saisissez votre table source pour la synchronisation. Sélectionnez un type de données et cliquez sur **Test Connection**.

En cas de succès, un aperçu des données s'affiche. Sélectionnez **Next: Notifications** pour continuer. Si la connexion échoue, un message d'erreur s'affiche pour vous aider à résoudre le problème.

{% alert note %}
Vous devez tester une synchronisation avec succès avant de passer aux étapes suivantes. Si vous devez fermer la page de création de la synchronisation, cliquez sur **Save as draft** pour conserver votre travail en cours.
{% endalert %}

#### Étape 3.2 : Ajouter les préférences de notification
Saisissez les adresses e-mail de contact pour les notifications d'erreurs de synchronisation. Braze utilise ces coordonnées pour envoyer des notifications en cas d'erreurs d'intégration, comme la perte inattendue de l'accès à la table.

Les e-mails de contact ne reçoivent que les notifications d'erreurs globales ou au niveau de la synchronisation, telles que les tables manquantes, les problèmes d'autorisations, etc. Ils ne reçoivent pas les problèmes au niveau des lignes. Les erreurs globales indiquent des problèmes critiques avec la connexion qui empêchent l'exécution des synchronisations. 

Ces problèmes peuvent inclure :

- Problèmes de connectivité
- Manque de ressources
- Problèmes d'autorisations
- (Pour les synchronisations de catalogues uniquement) Le niveau de catalogue n'a plus d'espace

#### Étape 3.3 : Planification
Enfin, configurez votre synchronisation comme non récurrente ou récurrente.

Les synchronisations non récurrentes peuvent être déclenchées manuellement ou via l'API.

Les synchronisations récurrentes peuvent avoir une fréquence allant de toutes les 15 minutes à une fois par mois. Braze utilise le fuseau horaire configuré dans votre tableau de bord de Braze pour planifier la synchronisation récurrente.

{% endtab %}

{% tab Redshift %}

#### Étape 3.1 : Configurer les détails de la synchronisation et tester la connexion
Choisissez un nom pour votre synchronisation. Sélectionnez ensuite une source active et saisissez votre table source pour la synchronisation. Sélectionnez un type de données et cliquez sur **Test Connection**.

En cas de succès, un aperçu des données s'affiche. Sélectionnez **Next: Notifications** pour continuer. Si la connexion échoue, un message d'erreur s'affiche pour vous aider à résoudre le problème.

{% alert note %}
Vous devez tester une synchronisation avec succès avant de passer aux étapes suivantes. Si vous devez fermer la page de création de la synchronisation, cliquez sur **Save as draft** pour conserver votre travail en cours.
{% endalert %}

#### Étape 3.2 : Ajouter les préférences de notification
Saisissez les adresses e-mail de contact pour les notifications d'erreurs de synchronisation. Braze utilise ces coordonnées pour envoyer des notifications en cas d'erreurs d'intégration, comme la perte inattendue de l'accès à la table.

Les e-mails de contact ne reçoivent que les notifications d'erreurs globales ou au niveau de la synchronisation, telles que les tables manquantes, les problèmes d'autorisations, etc. Ils ne reçoivent pas les problèmes au niveau des lignes. Les erreurs globales indiquent des problèmes critiques avec la connexion qui empêchent l'exécution des synchronisations. 

Ces problèmes peuvent inclure :

- Problèmes de connectivité
- Manque de ressources
- Problèmes d'autorisations

(Pour les synchronisations de catalogues uniquement) Le niveau de catalogue n'a plus d'espace

#### Étape 3.3 : Planification
Enfin, configurez votre synchronisation comme non récurrente ou récurrente.

Les synchronisations non récurrentes peuvent être déclenchées manuellement ou via l'API.

Les synchronisations récurrentes peuvent avoir une fréquence allant de toutes les 15 minutes à une fois par mois. Braze utilise le fuseau horaire configuré dans votre tableau de bord de Braze pour planifier la synchronisation récurrente.

{% endtab %}

{% tab BigQuery %}

#### Étape 3.1 : Configurer les détails de la synchronisation et tester la connexion
Choisissez un nom pour votre synchronisation. Sélectionnez ensuite une source active et saisissez votre table source pour la synchronisation. Sélectionnez un type de données et cliquez sur **Test Connection**.

En cas de succès, un aperçu des données s'affiche. Sélectionnez **Next: Notifications** pour continuer. Si la connexion échoue, un message d'erreur s'affiche pour vous aider à résoudre le problème.

{% alert note %}
Vous devez tester une synchronisation avec succès avant de passer aux étapes suivantes. Si vous devez fermer la page de création de la synchronisation, cliquez sur **Save as draft** pour conserver votre travail en cours.
{% endalert %}

#### Étape 3.2 : Ajouter les préférences de notification
Saisissez les adresses e-mail de contact pour les notifications d'erreurs de synchronisation. Braze utilise ces coordonnées pour envoyer des notifications en cas d'erreurs d'intégration, comme la perte inattendue de l'accès à la table.

Les e-mails de contact ne reçoivent que les notifications d'erreurs globales ou au niveau de la synchronisation, telles que les tables manquantes, les problèmes d'autorisations, etc. Ils ne reçoivent pas les problèmes au niveau des lignes. Les erreurs globales indiquent des problèmes critiques avec la connexion qui empêchent l'exécution des synchronisations. Ces problèmes peuvent inclure :

- Problèmes de connectivité
- Manque de ressources
- Problèmes d'autorisations

(Pour les synchronisations de catalogues uniquement) Le niveau de catalogue n'a plus d'espace

#### Étape 3.3 : Planification
Enfin, configurez votre synchronisation comme non récurrente ou récurrente.

Les synchronisations non récurrentes peuvent être déclenchées manuellement ou via l'API.

Les synchronisations récurrentes peuvent avoir une fréquence allant de toutes les 15 minutes à une fois par mois. Braze utilise le fuseau horaire configuré dans votre tableau de bord de Braze pour planifier la synchronisation récurrente.

{% endtab %}

{% tab Databricks %}

#### Étape 3.1 : Configurer les détails de la synchronisation et tester la connexion
Choisissez un nom pour votre synchronisation. Sélectionnez ensuite une source active et saisissez votre table source pour la synchronisation. Sélectionnez un type de données et cliquez sur **Test Connection**.

En cas de succès, un aperçu des données s'affiche. Sélectionnez **Next: Notifications** pour continuer. Si la connexion échoue, un message d'erreur s'affiche pour vous aider à résoudre le problème.

{% alert note %}
Vous devez tester une synchronisation avec succès avant de passer aux étapes suivantes. Si vous devez fermer la page de création de la synchronisation, cliquez sur **Save as draft** pour conserver votre travail en cours.
{% endalert %}

#### Étape 3.2 : Ajouter les préférences de notification
Saisissez les adresses e-mail de contact pour les notifications d'erreurs de synchronisation. Braze utilise ces coordonnées pour envoyer des notifications en cas d'erreurs d'intégration, comme la perte inattendue de l'accès à la table.

Les e-mails de contact ne reçoivent que les notifications d'erreurs globales ou au niveau de la synchronisation, telles que les tables manquantes, les problèmes d'autorisations, etc. Ils ne reçoivent pas les problèmes au niveau des lignes. Les erreurs globales indiquent des problèmes critiques avec la connexion qui empêchent l'exécution des synchronisations. 

Ces problèmes peuvent inclure :
- Problèmes de connectivité
- Manque de ressources
- Problèmes d'autorisations

(Pour les synchronisations de catalogues uniquement) Le niveau de catalogue n'a plus d'espace

#### Étape 3.3 : Planification
Enfin, configurez votre synchronisation comme non récurrente ou récurrente.

Les synchronisations non récurrentes peuvent être déclenchées manuellement ou via l'API.

Les synchronisations récurrentes peuvent avoir une fréquence allant de toutes les 15 minutes à une fois par mois. Braze utilise le fuseau horaire configuré dans votre tableau de bord de Braze pour planifier la synchronisation récurrente.

{% endtab %}
{% tab Microsoft Fabric %}

#### Étape 3.1 : Configurer les détails de la synchronisation et tester la connexion

Choisissez un nom pour votre synchronisation. Sélectionnez ensuite une source active et saisissez votre table source pour la synchronisation. Sélectionnez un type de données et cliquez sur **Test Connection**.

En cas de succès, un aperçu des données s'affiche. Sélectionnez **Next: Notifications** pour continuer. Si la connexion échoue, un message d'erreur s'affiche pour vous aider à résoudre le problème.

{% alert note %}
Vous devez tester une synchronisation avec succès avant de passer aux étapes suivantes. Si vous devez fermer la page de création de la synchronisation, cliquez sur **Save as draft** pour conserver votre travail en cours.
{% endalert %}

#### Étape 3.2 : Ajouter les préférences de notification
Saisissez les adresses e-mail de contact pour les notifications d'erreurs de synchronisation. Braze utilise ces coordonnées pour envoyer des notifications en cas d'erreurs d'intégration, comme la perte inattendue de l'accès à la table.

Les e-mails de contact ne reçoivent que les notifications d'erreurs globales ou au niveau de la synchronisation, telles que les tables manquantes, les problèmes d'autorisations, etc. Ils ne reçoivent pas les problèmes au niveau des lignes. Les erreurs globales indiquent des problèmes critiques avec la connexion qui empêchent l'exécution des synchronisations. 

Ces problèmes peuvent inclure :

- Problèmes de connectivité
- Manque de ressources
- Problèmes d'autorisations

(Pour les synchronisations de catalogues uniquement) Le niveau de catalogue n'a plus d'espace

#### Étape 3.3 : Planification
Enfin, configurez votre synchronisation comme non récurrente ou récurrente.

Les synchronisations non récurrentes peuvent être déclenchées manuellement ou via l'API.

Les synchronisations récurrentes peuvent avoir une fréquence allant de toutes les 15 minutes à une fois par mois. Braze utilise le fuseau horaire configuré dans votre tableau de bord de Braze pour planifier la synchronisation récurrente.

{% endtab %}
{% endtabs %}

{% alert note %}
Vous devez tester une intégration avec succès avant qu'elle ne puisse passer de l'état Brouillon à l'état Actif. Si vous fermez la page de création, votre intégration est enregistrée et vous pouvez revenir à la page de détails pour effectuer des modifications et tester.  
{% endalert %}

## Configurer des intégrations ou des utilisateurs supplémentaires (facultatif)

{% tabs %}
{% tab Snowflake %}
Vous pouvez configurer plusieurs intégrations avec Braze, mais chaque intégration doit être configurée pour synchroniser une table différente. Lors de la création de synchronisations supplémentaires, vous pouvez réutiliser les identifiants existants si vous vous connectez au même compte Snowflake.

Si vous réutilisez le même utilisateur et le même rôle entre les intégrations, vous n'avez pas besoin de repasser par l'étape d'ajout de la clé publique.
{% endtab %}
{% tab Redshift %}
Vous pouvez configurer plusieurs intégrations avec Braze, mais chaque intégration doit être configurée pour synchroniser une table différente. Lors de la création de synchronisations supplémentaires, vous pouvez réutiliser les identifiants existants si vous vous connectez au même compte Snowflake ou Redshift.

Si vous réutilisez le même utilisateur entre les intégrations, vous ne pouvez pas le supprimer dans le tableau de bord de Braze tant qu'il n'a pas été retiré de toutes les synchronisations actives.
{% endtab %}
{% tab BigQuery %}

Vous pouvez configurer plusieurs intégrations avec Braze, mais chaque intégration doit être configurée pour synchroniser une table différente. Lors de la création de synchronisations supplémentaires, vous pouvez réutiliser les identifiants existants si vous vous connectez au même compte BigQuery.

Si vous réutilisez le même utilisateur entre les intégrations, vous ne pouvez pas le supprimer dans le tableau de bord de Braze tant qu'il n'a pas été retiré de toutes les synchronisations actives.

{% endtab %}
{% tab Databricks %}

Vous pouvez configurer plusieurs intégrations avec Braze, mais chaque intégration doit être configurée pour synchroniser une table différente. Lors de la création de synchronisations supplémentaires, vous pouvez réutiliser les identifiants existants si vous vous connectez au même compte Databricks.

Si vous réutilisez le même utilisateur entre les intégrations, vous ne pouvez pas le supprimer dans le tableau de bord de Braze tant qu'il n'a pas été retiré de toutes les synchronisations actives.

{% endtab %}
{% tab Microsoft Fabric %}

Vous pouvez configurer plusieurs intégrations avec Braze, mais chaque intégration doit être configurée pour synchroniser une table différente. Lors de la création de synchronisations supplémentaires, vous pouvez réutiliser les identifiants existants si vous vous connectez au même compte Fabric.

Si vous réutilisez le même utilisateur entre les intégrations, vous ne pouvez pas le supprimer dans le tableau de bord de Braze tant qu'il n'a pas été retiré de toutes les synchronisations actives.

{% endtab %}
{% endtabs %}

## Exécuter la synchronisation

{% tabs %}
{% tab Snowflake %}
Une fois activée, votre synchronisation s'exécute selon la planification configurée lors de la mise en place. Si vous souhaitez exécuter la synchronisation en dehors de la planification normale ou récupérer les données les plus récentes, sélectionnez **Sync Now**. Cette exécution n'a pas d'impact sur les synchronisations futures régulièrement planifiées.

{% endtab %}
{% tab Redshift %}
Une fois activée, votre synchronisation s'exécute selon la planification configurée lors de la mise en place. Si vous souhaitez exécuter la synchronisation en dehors de la planification normale ou récupérer les données les plus récentes, sélectionnez **Sync Now**. Cette exécution n'a pas d'impact sur les synchronisations futures régulièrement planifiées.

{% endtab %}
{% tab BigQuery %}

Une fois activée, votre synchronisation s'exécute selon la planification configurée lors de la mise en place. Si vous souhaitez exécuter la synchronisation en dehors de la planification normale ou récupérer les données les plus récentes, sélectionnez **Sync Now**. Cette exécution n'a pas d'impact sur les synchronisations futures régulièrement planifiées.

{% endtab %}
{% tab Databricks %}

Une fois activée, votre synchronisation s'exécute selon la planification configurée lors de la mise en place. Si vous souhaitez exécuter la synchronisation en dehors de la planification normale ou récupérer les données les plus récentes, sélectionnez **Sync Now**. Cette exécution n'a pas d'impact sur les synchronisations futures régulièrement planifiées.

{% endtab %}
{% tab Microsoft Fabric %}

Une fois activée, votre synchronisation s'exécute selon la planification configurée lors de la mise en place. Si vous souhaitez exécuter la synchronisation en dehors de la planification normale ou récupérer les données les plus récentes, sélectionnez **Sync Now**. Cette exécution n'a pas d'impact sur les synchronisations futures régulièrement planifiées.

{% endtab %}

{% endtabs %}

{% details Expérience en disponibilité générale %}

## Mise en place des intégrations d'entrepôts de données

Les intégrations d'ingestion de données cloud nécessitent une configuration côté Braze et dans votre instance d'entrepôt de données. Suivez ces étapes pour configurer votre intégration :

{% tabs %}
{% tab Snowflake %}
1. Dans votre instance Snowflake, configurez les tables ou les vues que vous souhaitez synchroniser avec Braze.
2. Créez une nouvelle intégration dans le tableau de bord de Braze.
3. Récupérez la clé publique fournie dans le tableau de bord de Braze et [ajoutez-la à l'utilisateur Snowflake pour l'authentification](https://docs.snowflake.com/en/user-guide/key-pair-auth.html).
4. Testez l'intégration et démarrez la synchronisation.

{% alert tip %}
Le [guide de démarrage rapide de Snowflake](https://quickstarts.snowflake.com/guide/braze_cdi/index.html) fournit un exemple de code et présente les étapes requises pour créer un pipeline automatisé utilisant Snowflake Streams et CDI pour synchroniser les données vers Braze.
{% endalert %}
{% endtab %}
{% tab Redshift %}
1. Assurez-vous que l'accès à Braze est autorisé pour les tables Redshift que vous souhaitez synchroniser. Braze se connectera à Redshift via Internet.
2. Dans votre instance Redshift, configurez les tables ou les vues que vous souhaitez synchroniser avec Braze.
3. Créez une nouvelle intégration dans le tableau de bord de Braze.
4. Testez l'intégration et démarrez la synchronisation.
{% endtab %}
{% tab BigQuery %}
1. Créez un compte de service et autorisez l'accès au(x) projet(s) BigQuery et au(x) jeu(x) de données contenant les données que vous souhaitez synchroniser.  
2. Dans votre compte BigQuery, configurez les tables ou les vues que vous souhaitez synchroniser avec Braze.   
3. Créez une nouvelle intégration dans le tableau de bord de Braze.  
4. Testez l'intégration et démarrez la synchronisation.  
{% endtab %}
{% tab Databricks %}
1. Créez un compte de service et autorisez l'accès au(x) projet(s) et jeu(x) de données Databricks contenant les données que vous souhaitez synchroniser.  
2. Dans votre compte Databricks, configurez les tables ou les vues que vous souhaitez synchroniser avec Braze.   
3. Créez une nouvelle intégration dans le tableau de bord de Braze.  
4. Testez l'intégration et démarrez la synchronisation.

{% alert important %}
Il peut y avoir un temps de préchauffage de deux à cinq minutes lorsque Braze se connecte aux instances SQL Classic et Pro, ce qui entraînera des retards lors de la configuration et des tests de connexion, ainsi qu'au début des synchronisations planifiées. L'utilisation d'une instance SQL serverless permet de réduire ce temps de préchauffage et d'améliorer le débit des requêtes, mais peut entraîner des coûts d'intégration légèrement plus élevés.
{% endalert %}

{% endtab %}
{% tab Microsoft Fabric %}
1. Créez un principal de service et autorisez l'accès aux API Fabric.
2. Configurez un espace de travail partagé et accordez au principal de service l'accès à celui-ci.
3. Dans l'espace de travail Fabric partagé que vous avez créé à l'étape 2, configurez les tables ou les vues que vous souhaitez synchroniser avec Braze.   
4. Créez une nouvelle intégration dans le tableau de bord de Braze.  
5. Testez l'intégration et démarrez la synchronisation.
{% endtab %}
{% endtabs %}

### Étape 1 : Configurer les tables ou les vues

{% tabs %}
{% tab Snowflake %}

#### Étape 1.1 : Configurer la table

```sql
CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
CREATE OR REPLACE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC (
     UPDATED_AT TIMESTAMP_NTZ(9) NOT NULL DEFAULT SYSDATE(),
     --at least one of external_id, alias_name and alias_label, email, phone, or braze_id is required  
     EXTERNAL_ID VARCHAR(16777216),
     --if using user alias, both alias_name and alias_label are required
     ALIAS_LABEL VARCHAR(16777216),
     ALIAS_NAME VARCHAR(16777216),
     --braze_id can only be used to update existing users created through the Braze SDK
     BRAZE_ID VARCHAR(16777216),
     --If you include both email and phone, email is used as the primary identifier
     EMAIL VARCHAR(16777216),
     PHONE VARCHAR(16777216),
     PAYLOAD VARCHAR(16777216) NOT NULL
);
```

Vous pouvez nommer la base de données, le schéma et la table comme vous le souhaitez, mais les noms de colonnes doivent correspondre à la définition ci-dessus.

- `UPDATED_AT` : L'heure à laquelle cette ligne a été mise à jour ou ajoutée à la table. Braze synchronise les lignes dont la valeur `UPDATED_AT` est postérieure à la dernière valeur synchronisée. Les lignes situées exactement à l'horodatage limite peuvent être re-synchronisées si de nouvelles lignes partagent ce même horodatage.
- **Colonnes d'identification de l'utilisateur** : Votre table peut contenir une ou plusieurs colonnes d'identification de l'utilisateur. Chaque ligne ne doit contenir qu'un seul identifiant (soit `external_id`, la combinaison de `alias_name` et `alias_label`, `braze_id`, `email` ou `phone`). Une table source peut comporter des colonnes pour un, deux, trois, quatre ou les cinq types d'identifiants.
    - `EXTERNAL_ID` : Identifie l'utilisateur que vous souhaitez mettre à jour. Cette valeur doit correspondre à la valeur `external_id` utilisée dans Braze. 
    - `ALIAS_NAME` et `ALIAS_LABEL` : Ces deux colonnes créent un objet d'alias d'utilisateur. `alias_name` doit être un identifiant unique et `alias_label` spécifie le type d'alias. Les utilisateurs peuvent avoir plusieurs alias avec différentes étiquettes, mais un seul `alias_name` par `alias_label`.
    - `BRAZE_ID` : L'identifiant utilisateur Braze. Celui-ci est généré par le SDK Braze, et il n'est pas possible de créer de nouveaux utilisateurs à l'aide d'un ID Braze via l'ingestion de données cloud. Pour créer de nouveaux utilisateurs, spécifiez un ID utilisateur externe ou un alias d'utilisateur.
    - `EMAIL` : L'adresse e-mail de l'utilisateur. Si plusieurs profils avec la même adresse e-mail existent, le profil le plus récemment mis à jour est prioritaire. Si vous incluez à la fois l'e-mail et le téléphone, l'e-mail est utilisé comme identifiant principal.
    - `PHONE` : Le numéro de téléphone de l'utilisateur. Si plusieurs profils avec le même numéro de téléphone existent, le profil le plus récemment mis à jour est prioritaire.
- `PAYLOAD` : Il s'agit d'une chaîne de caractères JSON des champs que vous souhaitez synchroniser avec l'utilisateur dans Braze.

#### Étape 1.2 : Définir le rôle et les autorisations de la base de données

```sql
CREATE ROLE BRAZE_INGESTION_ROLE;

GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC TO ROLE BRAZE_INGESTION_ROLE;
```

Modifiez les noms si nécessaire, mais les autorisations doivent correspondre à l'exemple ci-dessus.

#### Étape 1.3 : Configurer l'entrepôt et donner accès au rôle Braze

```sql
CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;

GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;
```

{% alert note %}
L'entrepôt doit avoir l'option de **reprise automatique** activée. Si ce n'est pas le cas, vous devrez accorder à Braze des privilèges `OPERATE` supplémentaires sur l'entrepôt pour que nous puissions l'activer au moment de l'exécution de la requête.
{% endalert %}

#### Étape 1.4 : Configurer l'utilisateur

```sql
CREATE USER BRAZE_INGESTION_USER;

GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
```

Après cette étape, vous partagerez les informations de connexion avec Braze et recevrez une clé publique à ajouter à l'utilisateur.

{% alert note %}
Lorsque vous connectez différents espaces de travail au même compte Snowflake, vous devez créer un utilisateur unique pour chaque espace de travail Braze dans lequel vous créez une intégration. Au sein d'un espace de travail, vous pouvez réutiliser le même utilisateur entre les intégrations, mais la création d'une intégration échouera si un utilisateur du même compte Snowflake est dupliqué entre les espaces de travail.
{% endalert %}

#### Étape 1.5 : Autoriser les IP de Braze dans la politique réseau de Snowflake (facultatif)

Selon la configuration de votre compte Snowflake, vous devrez peut-être autoriser les adresses IP suivantes dans votre politique réseau Snowflake. Pour plus d'informations, consultez la documentation Snowflake sur la [modification d'une politique réseau](https://docs.snowflake.com/en/user-guide/network-policies.html#modifying-network-policies).

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}
{% tab Redshift %}

#### Étape 1.1 : Configurer la table 

Optionnellement, créez une nouvelle base de données et un nouveau schéma pour contenir votre table source
```sql
CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
```
Créez une table (ou vue) à utiliser pour votre intégration CDI
```sql
CREATE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC (
   updated_at timestamptz default sysdate,
   --at least one of external_id, alias_name and alias_label, or braze_id is required
   external_id varchar,
   --if using user alias, both alias_name and alias_label are required
   alias_label varchar,
   alias_name varchar,
   --braze_id can only be used to update existing users created through the Braze SDK
   braze_id varchar,
   --If you include both email and phone, email is used as the primary identifier
   email varchar,
   phone varchar,
   payload varchar(max)
)
```

Vous pouvez nommer la base de données, le schéma et la table comme vous le souhaitez, mais les noms de colonnes doivent correspondre à la définition ci-dessus.

- `UPDATED_AT` : L'heure à laquelle cette ligne a été mise à jour ou ajoutée à la table. Braze synchronise les lignes dont la valeur `UPDATED_AT` est postérieure à la dernière valeur synchronisée. Les lignes situées exactement à l'horodatage limite peuvent être re-synchronisées si de nouvelles lignes partagent ce même horodatage.
- **Colonnes d'identification de l'utilisateur** : Votre table peut contenir une ou plusieurs colonnes d'identification de l'utilisateur. Chaque ligne ne doit contenir qu'un seul identifiant (soit `external_id`, la combinaison de `alias_name` et `alias_label`, `braze_id`, `email` ou `phone`). Une table source peut comporter des colonnes pour un, deux, trois, quatre ou les cinq types d'identifiants.
    - `EXTERNAL_ID` : Identifie l'utilisateur que vous souhaitez mettre à jour. Cette valeur doit correspondre à la valeur `external_id` utilisée dans Braze. 
    - `ALIAS_NAME` et `ALIAS_LABEL` : Ces deux colonnes créent un objet d'alias d'utilisateur. `alias_name` doit être un identifiant unique et `alias_label` spécifie le type d'alias. Les utilisateurs peuvent avoir plusieurs alias avec différentes étiquettes, mais un seul `alias_name` par `alias_label`.
    - `BRAZE_ID` : L'identifiant utilisateur Braze. Celui-ci est généré par le SDK Braze, et il n'est pas possible de créer de nouveaux utilisateurs à l'aide d'un ID Braze via l'ingestion de données cloud. Pour créer de nouveaux utilisateurs, spécifiez un ID utilisateur externe ou un alias d'utilisateur.
    - `EMAIL` : L'adresse e-mail de l'utilisateur. Si plusieurs profils avec la même adresse e-mail existent, le profil le plus récemment mis à jour est prioritaire. Si vous incluez à la fois l'e-mail et le téléphone, l'e-mail est utilisé comme identifiant principal.
    - `PHONE` : Le numéro de téléphone de l'utilisateur. Si plusieurs profils avec le même numéro de téléphone existent, le profil le plus récemment mis à jour est prioritaire.
- `PAYLOAD` : Il s'agit d'une chaîne de caractères JSON des champs que vous souhaitez synchroniser avec l'utilisateur dans Braze.
 
#### Étape 1.2 : Créer un utilisateur et accorder les autorisations

```sql
CREATE USER braze_user PASSWORD '{password}';
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT SELECT ON TABLE USERS_ATTRIBUTES_SYNC TO braze_user;
```

Il s'agit des autorisations minimales requises pour cet utilisateur. Si vous créez plusieurs intégrations CDI, vous pouvez accorder des autorisations au niveau du schéma ou gérer les autorisations à l'aide d'un groupe. 

#### Étape 1.3 : Autoriser l'accès aux IP de Braze

Si vous avez un pare-feu ou d'autres politiques réseau, vous devez donner à Braze un accès réseau à votre instance Redshift. Un exemple d'endpoint URL Redshift est « example-cluster.ap-northeast-2.redshift.amazonaws.com ».

Points importants à connaître :
- Vous devrez peut-être également modifier vos groupes de sécurité pour permettre à Braze d'accéder à vos données dans Redshift.
- Veillez à autoriser explicitement le trafic entrant sur les IP du tableau et sur le port utilisé pour interroger votre cluster Redshift (5439 par défaut). Vous devez explicitement autoriser la connectivité TCP Redshift sur ce port, même si les règles d'entrée sont définies sur « Autoriser tout ».
- L'endpoint du cluster Redshift doit être accessible publiquement pour que Braze puisse se connecter à votre cluster.
     - Si vous ne souhaitez pas que votre cluster Redshift soit accessible publiquement, vous pouvez configurer un VPC et une instance EC2 pour utiliser un tunnel SSH afin d'accéder aux données Redshift. Consultez cet [article du Centre de connaissances AWS](https://repost.aws/knowledge-center/private-redshift-cluster-local-machine) pour plus d'informations.
 
Autorisez l'accès à partir des IP suivantes correspondant à la région de votre tableau de bord de Braze.

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}
{% tab BigQuery %}

#### Étape 1.1 : Configurer la table 

Optionnellement, créez un nouveau projet ou jeu de données pour contenir votre table source.

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

Créez une ou plusieurs tables à utiliser pour votre intégration CDI avec les champs suivants :

```sql
CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC`
(
  updated_at TIMESTAMP DEFAULT current_timestamp,
  --At least one of external_id, alias_name and alias_label, or braze_id is required  
  external_id STRING,
  --If using user alias, both alias_name and alias_label are required
  alias_name STRING,
  alias_label STRING,
  --braze_id can only be used to update existing users created through the Braze SDK
  braze_id STRING,
  --If you include both email and phone, email is used as the primary identifier
  email STRING,
  phone STRING,
  payload JSON
);
```

| Nom du champ | Type | Mode |
|---|---|---|
| `UPDATED_AT`| TIMESTAMP | REQUIS |
| `PAYLOAD`| JSON | REQUIS |
| `EXTERNAL_ID`| STRING | NULLABLE |
| `ALIAS_NAME`| STRING | NULLABLE |
| `ALIAS_LABEL`| STRING | NULLABLE |
| `BRAZE_ID`| STRING | NULLABLE |
| `EMAIL`| STRING | NULLABLE |
| `PHONE`| STRING | NULLABLE |

Vous pouvez nommer le projet, le jeu de données et la table comme vous le souhaitez, mais les noms de colonnes doivent correspondre à la définition ci-dessus.

- `UPDATED_AT` : L'heure à laquelle cette ligne a été mise à jour ou ajoutée à la table. Braze synchronise les lignes dont la valeur `UPDATED_AT` est postérieure à la dernière valeur synchronisée. Les lignes situées exactement à l'horodatage limite peuvent être re-synchronisées si de nouvelles lignes partagent ce même horodatage.
- **Colonnes d'identification de l'utilisateur** : Votre table peut contenir une ou plusieurs colonnes d'identification de l'utilisateur. Chaque ligne ne doit contenir qu'un seul identifiant (soit `external_id`, la combinaison de `alias_name` et `alias_label`, `braze_id`, `email` ou `phone`). Une table source peut comporter des colonnes pour un, deux, trois, quatre ou les cinq types d'identifiants.
    - `EXTERNAL_ID` : Identifie l'utilisateur que vous souhaitez mettre à jour. Cette valeur doit correspondre à la valeur `external_id` utilisée dans Braze. 
    - `ALIAS_NAME` et `ALIAS_LABEL` : Ces deux colonnes créent un objet d'alias d'utilisateur. `alias_name` doit être un identifiant unique et `alias_label` spécifie le type d'alias. Les utilisateurs peuvent avoir plusieurs alias avec différentes étiquettes, mais un seul `alias_name` par `alias_label`.
    - `BRAZE_ID` : L'identifiant utilisateur Braze. Celui-ci est généré par le SDK Braze, et il n'est pas possible de créer de nouveaux utilisateurs à l'aide d'un ID Braze via l'ingestion de données cloud. Pour créer de nouveaux utilisateurs, spécifiez un ID utilisateur externe ou un alias d'utilisateur.
    - `EMAIL` : L'adresse e-mail de l'utilisateur. Si plusieurs profils avec la même adresse e-mail existent, le profil le plus récemment mis à jour est prioritaire. Si vous incluez à la fois l'e-mail et le téléphone, l'e-mail est utilisé comme identifiant principal.
    - `PHONE` : Le numéro de téléphone de l'utilisateur. Si plusieurs profils avec le même numéro de téléphone existent, le profil le plus récemment mis à jour est prioritaire.
- `PAYLOAD` : Il s'agit d'une chaîne de caractères JSON des champs que vous souhaitez synchroniser avec l'utilisateur dans Braze.

{% alert important %}
**Partitionnement BigQuery**

CDI prend en charge les partitions pour BigQuery. Si vous partitionnez en fonction de `UPDATED_AT` (par exemple, à la granularité d'un jour, d'une semaine ou d'une heure, selon la taille de votre jeu de données), BigQuery peut élaguer les données à analyser. Cela améliore les performances et l'efficacité pour les très grandes tables.

Ne partitionnez pas selon d'autres champs. Testez différentes configurations pour trouver celle qui convient le mieux à vos données.

Toutes les requêtes CDI filtrent par `UPDATED_AT`, mais ce comportement pourrait changer. Concevez votre schéma de table de manière à _ne pas_ exiger que les requêtes incluent cette clause.

Pour plus d'informations, consultez la [documentation sur le partitionnement BigQuery](https://docs.cloud.google.com/bigquery/docs/partitioned-tables).
{% endalert %}

#### Étape 1.2 : Créer un compte de service et accorder les autorisations 

Créez un compte de service dans GCP que Braze utilisera pour se connecter et lire les données de votre/vos table(s). Le compte de service doit disposer des autorisations suivantes : 

- **BigQuery Connection User :** Permet à Braze d'établir des connexions.
- **BigQuery User :** Donne à Braze l'accès pour exécuter des requêtes, lire les métadonnées des jeux de données et lister les tables.
- **BigQuery Data Viewer :** Donne à Braze l'accès pour visualiser les jeux de données et leur contenu.
- **BigQuery Job User :** Donne à Braze l'accès pour exécuter des tâches.

Après avoir créé le compte de service et accordé les autorisations, générez une clé JSON. Pour plus d'informations sur la procédure, consultez [cette page](https://cloud.google.com/iam/docs/keys-create-delete). Vous la chargerez ultérieurement dans le tableau de bord de Braze. 

#### Étape 1.3 : Autoriser l'accès aux IP de Braze    

Si vous avez des politiques réseau en place, vous devez donner à Braze un accès réseau à votre instance BigQuery. Autorisez l'accès à partir des IP ci-dessous correspondant à la région de votre tableau de bord de Braze.  

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}
{% tab Databricks %}

#### Étape 1.1 : Configurer la table 

Optionnellement, créez un nouveau catalogue ou schéma pour contenir votre table source.

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

Créez une ou plusieurs tables à utiliser pour votre intégration CDI avec les champs suivants :


```sql
CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC`
(
  updated_at TIMESTAMP DEFAULT current_timestamp(),
  --At least one of external_id, alias_name and alias_label, or braze_id is required  
  external_id STRING,
  --If using user alias, both alias_name and alias_label are required
  alias_name STRING,
  alias_label STRING,
  --braze_id can only be used to update existing users created through the Braze SDK
  braze_id STRING,
  --If you include both email and phone, email is used as the primary identifier
  email STRING,
  phone STRING,
  payload STRING, STRUCT, or MAP
);
```


| Nom du champ | Type | Mode |
|---|---|---|
| `UPDATED_AT`| TIMESTAMP | REQUIS |
| `PAYLOAD`| STRING, STRUCT ou MAP | REQUIS |
| `EXTERNAL_ID`| STRING | NULLABLE |
| `ALIAS_NAME`| STRING | NULLABLE |
| `ALIAS_LABEL`| STRING | NULLABLE |
| `BRAZE_ID`| STRING | NULLABLE |
| `EMAIL`| STRING | NULLABLE |
| `PHONE`| STRING | NULLABLE |

Vous pouvez nommer le schéma et la table comme vous le souhaitez, mais les noms de colonnes doivent correspondre à la définition ci-dessus.

- `UPDATED_AT` : L'heure à laquelle cette ligne a été mise à jour ou ajoutée à la table. Braze synchronise les lignes dont la valeur `UPDATED_AT` est postérieure à la dernière valeur synchronisée. Les lignes situées exactement à l'horodatage limite peuvent être re-synchronisées si de nouvelles lignes partagent ce même horodatage.
- **Colonnes d'identification de l'utilisateur** : Votre table peut contenir une ou plusieurs colonnes d'identification de l'utilisateur. Chaque ligne ne doit contenir qu'un seul identifiant (soit `external_id`, la combinaison de `alias_name` et `alias_label`, `braze_id`, `email` ou `phone`). Une table source peut comporter des colonnes pour un, deux, trois, quatre ou les cinq types d'identifiants.
    - `EXTERNAL_ID` : Identifie l'utilisateur que vous souhaitez mettre à jour. Cette valeur doit correspondre à la valeur `external_id` utilisée dans Braze. 
    - `ALIAS_NAME` et `ALIAS_LABEL` : Ces deux colonnes créent un objet d'alias d'utilisateur. `alias_name` doit être un identifiant unique et `alias_label` spécifie le type d'alias. Les utilisateurs peuvent avoir plusieurs alias avec différentes étiquettes, mais un seul `alias_name` par `alias_label`.
    - `BRAZE_ID` : L'identifiant utilisateur Braze. Celui-ci est généré par le SDK Braze, et il n'est pas possible de créer de nouveaux utilisateurs à l'aide d'un ID Braze via l'ingestion de données cloud. Pour créer de nouveaux utilisateurs, spécifiez un ID utilisateur externe ou un alias d'utilisateur. 
    - `EMAIL` : L'adresse e-mail de l'utilisateur. Si plusieurs profils avec la même adresse e-mail existent, le profil le plus récemment mis à jour est prioritaire. Si vous incluez à la fois l'e-mail et le téléphone, l'e-mail est utilisé comme identifiant principal.
    - `PHONE` : Le numéro de téléphone de l'utilisateur. Si plusieurs profils avec le même numéro de téléphone existent, le profil le plus récemment mis à jour est prioritaire.
- `PAYLOAD` : Il s'agit d'une chaîne de caractères ou d'une structure des champs que vous souhaitez synchroniser avec l'utilisateur dans Braze.

#### Étape 1.2 : Créer un jeton d'accès  

Pour que Braze puisse accéder à Databricks, un jeton d'accès personnel doit être créé.

1. Dans votre espace de travail Databricks, sélectionnez votre nom d'utilisateur Databricks dans la barre supérieure, puis sélectionnez **User Settings** dans le menu déroulant.
2. Dans l'onglet Jetons d'accès, sélectionnez **Generate new token**.
3. Saisissez un commentaire pour identifier ce jeton, par exemple « Braze CDI », et définissez la durée de vie du jeton sur illimitée en laissant la case Durée de vie (jours) vide.
4. Sélectionnez **Generate**.
5. Copiez le jeton affiché, puis sélectionnez **Done**.

Conservez le jeton en lieu sûr jusqu'à ce que vous ayez besoin de le saisir dans le tableau de bord de Braze lors de l'étape de création des identifiants.

#### Étape 1.3 : Autoriser l'accès aux IP de Braze    

Si vous avez des politiques réseau en place, vous devez donner à Braze un accès réseau à votre instance Databricks. Autorisez l'accès à partir des IP ci-dessous correspondant à la région de votre tableau de bord de Braze.  

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}
{% tab Microsoft Fabric %}

#### Étape 1.1 : Configurer le principal de service et accorder l'accès
Braze se connectera à votre entrepôt Fabric à l'aide d'un principal de service avec une authentification Entra ID. Vous créerez un nouveau principal de service dédié à Braze et accorderez l'accès aux ressources Fabric selon les besoins. Braze aura besoin des informations suivantes pour se connecter :    

* ID de locataire (également appelé répertoire) de votre compte Azure 
* ID du principal (également appelé ID d'application) pour le principal de service 
* Secret client pour l'authentification de Braze

1. Dans le portail Azure, accédez au centre d'administration Microsoft Entra, puis à Inscriptions d'applications. 
2. Sélectionnez **+ New registration** sous **Identity** > **Applications** > **App registrations**.
3. Saisissez un nom, puis sélectionnez `Accounts in this organizational directory only` comme type de compte pris en charge. Sélectionnez ensuite **Register**. 
4. Sélectionnez l'application (principal de service) que vous venez de créer, puis accédez à **Certificates & secrets** > **+ New client secret**.
5. Saisissez une description et une période d'expiration pour le secret. Sélectionnez ensuite **Add**. 
6. Notez le secret client créé pour l'utiliser dans la configuration de Braze. 

{% alert note %}
Azure n'autorise pas l'expiration illimitée des secrets de principaux de service. N'oubliez pas d'actualiser les identifiants avant leur expiration afin de maintenir le flux de données vers Braze.
{% endalert %}

#### Étape 1.2 : Accorder l'accès aux ressources Fabric 
Vous accorderez à Braze l'accès pour se connecter à votre instance Fabric. Dans votre portail d'administration Fabric, accédez à **Settings** > **Governance and insights** > **Admin portal** > **Tenant settings**.    

* Dans **Developer settings**, activez **Service principals can use Fabric APIs** pour que Braze puisse se connecter via Microsoft Entra ID.
* Dans **OneLake settings**, activez **Users can access data stored in OneLake with apps external to Fabric** pour que le principal de service puisse accéder aux données depuis une application externe.

#### Étape 1.3 : Configurer un espace de travail partagé et accorder l'accès

Toutes les ressources Fabric que vous souhaitez connecter à Braze doivent être placées dans un espace de travail partagé. Si vous n'avez utilisé que l'espace **My Workspace** par défaut, créez un nouvel espace de travail partagé :

1. Dans le menu de navigation, sélectionnez **Workspaces**, puis sélectionnez **+ New workspace**.
2. Saisissez un **nom** pour l'espace de travail, puis sélectionnez **Apply**.

Une fois l'espace de travail partagé créé, accordez l'accès au principal de service :

1. Sélectionnez l'espace de travail, puis sélectionnez **Manage Access**.
2. Sélectionnez **+ Add people or groups**.
3. Recherchez et sélectionnez le nom du principal de service créé à l'étape 1.1. S'il n'apparaît pas, vérifiez que vous avez activé le paramètre **Service principals can use Fabric APIs** à l'étape 1.2.
4. Dans le menu déroulant des rôles, sélectionnez **Contributor**.

Le principal de service peut désormais accéder aux ressources de l'entrepôt Fabric dans cet espace de travail via leurs endpoints SQL, y compris l'entrepôt que vous utiliserez pour Braze.

#### Étape 1.4 : Configurer la table
Braze prend en charge les tables et les vues dans les entrepôts Fabric. Si vous devez créer un nouvel entrepôt, créez-le dans l'espace de travail partagé de l'étape 1.3. Accédez à **Create > Data Warehouse > Warehouse** dans la console Fabric.

```sql
CREATE OR ALTER TABLE [warehouse].[schema].[CDI_table_name] 
(
  UPDATED_AT DATETIME2(6) NOT NULL,
  PAYLOAD VARCHAR NOT NULL,
  --at least one of external_id, alias_name and alias_label, email, phone, or braze_id is required  
  EXTERNAL_ID VARCHAR,
  --if using user alias, both alias_name and alias_label are required
  ALIAS_NAME VARCHAR,
  ALIAS_LABEL VARCHAR,
  --braze_id can only be used to update existing users created through the Braze SDK
  BRAZE_ID VARCHAR,
  --If you include both email and phone, email is used as the primary identifier
  EMAIL VARCHAR,
  PHONE VARCHAR
)
GO
```

Vous pouvez nommer l'entrepôt, le schéma et la table ou vue comme vous le souhaitez, mais les noms de colonnes doivent correspondre à la définition ci-dessus.

- `UPDATED_AT` : L'heure à laquelle cette ligne a été mise à jour ou ajoutée à la table. Braze synchronise les lignes dont la valeur `UPDATED_AT` est postérieure à la dernière valeur synchronisée. Les lignes situées exactement à l'horodatage limite peuvent être re-synchronisées si de nouvelles lignes partagent ce même horodatage.
- **Colonnes d'identification de l'utilisateur** : Votre table peut contenir une ou plusieurs colonnes d'identification de l'utilisateur. Chaque ligne ne doit contenir qu'un seul identifiant (soit `external_id`, la combinaison de `alias_name` et `alias_label`, `braze_id`, `email` ou `phone`). Une table source peut comporter des colonnes pour un, deux, trois, quatre ou les cinq types d'identifiants.
    - `EXTERNAL_ID` : Identifie l'utilisateur que vous souhaitez mettre à jour. Cette valeur doit correspondre à la valeur `external_id` utilisée dans Braze. 
    - `ALIAS_NAME` et `ALIAS_LABEL` : Ces deux colonnes créent un objet d'alias d'utilisateur. `alias_name` doit être un identifiant unique et `alias_label` spécifie le type d'alias. Les utilisateurs peuvent avoir plusieurs alias avec différentes étiquettes, mais un seul `alias_name` par `alias_label`.
    - `BRAZE_ID` : L'identifiant utilisateur Braze. Celui-ci est généré par le SDK Braze, et il n'est pas possible de créer de nouveaux utilisateurs à l'aide d'un ID Braze via l'ingestion de données cloud. Pour créer de nouveaux utilisateurs, spécifiez un ID utilisateur externe ou un alias d'utilisateur.
    - `EMAIL` : L'adresse e-mail de l'utilisateur. Si plusieurs profils avec la même adresse e-mail existent, le profil le plus récemment mis à jour est prioritaire. Si vous incluez à la fois l'e-mail et le téléphone, l'e-mail est utilisé comme identifiant principal.
    - `PHONE` : Le numéro de téléphone de l'utilisateur. Si plusieurs profils avec le même numéro de téléphone existent, le profil le plus récemment mis à jour est prioritaire.
- `PAYLOAD` : Il s'agit d'une chaîne de caractères JSON des champs que vous souhaitez synchroniser avec l'utilisateur dans Braze.


#### Étape 1.5 : Obtenir la chaîne de connexion de l'entrepôt
Vous aurez besoin de l'endpoint SQL de votre entrepôt pour que Braze puisse se connecter. Pour le récupérer, accédez à l'**espace de travail** dans Fabric, et dans la liste des éléments, survolez le nom de l'entrepôt et sélectionnez **Copy SQL connection string**.

![La page « Fabric Console » dans Microsoft Azure, où les utilisateurs doivent récupérer la chaîne de connexion SQL.]({% image_buster /assets/img/cloud_ingestion/fabric_1.png %})


#### Étape 1.6 : Autoriser les IP de Braze dans le pare-feu (facultatif)

Selon la configuration de votre compte Microsoft Fabric, vous devrez peut-être autoriser les adresses IP suivantes dans votre pare-feu pour permettre le trafic en provenance de Braze. Pour plus d'informations, consultez la documentation sur l'[accès conditionnel Entra](https://learn.microsoft.com/en-us/fabric/security/protect-inbound-traffic#entra-conditional-access).

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}

{% endtabs %}

### Étape 2 : Créer une nouvelle intégration dans le tableau de bord de Braze

{% alert important %}
Les clients dont l'onboarding a lieu en février 2026 ou après peuvent bénéficier d'un accès anticipé à l'interface CDI avec des Sources et des Synchronisations séparées. Dans cette interface, créez d'abord une source avant de créer des synchronisations pour cette source. Plusieurs synchronisations peuvent utiliser la même source.
{% endalert %}

{% tabs %}
{% tab Snowflake %}

Dans le tableau de bord de Braze, accédez à **Data Settings** > **Cloud Data Ingestion**, sélectionnez **Create New Data Sync**, puis sélectionnez **Snowflake Import**.

#### Étape 2.1 : Ajouter les informations de connexion Snowflake et la table source

Saisissez les informations relatives à votre entrepôt de données Snowflake et à votre table source, puis passez à l'étape suivante.

{% alert note %}
Dans le champ **Snowflake Account Locator**, saisissez l'[identifiant de compte](https://docs.snowflake.com/en/user-guide/admin-account-identifier) Snowflake, qui suit généralement un format tel que `xy12345.us-east-1.aws`. Il ne s'agit pas d'un nom de base de données ou d'entrepôt.
{% endalert %}

#### Étape 2.2 : Configurer les détails de la synchronisation

Choisissez ensuite un nom pour votre synchronisation et saisissez les e-mails de contact. Ces coordonnées serviront à vous informer de toute erreur d'intégration, comme la suppression inattendue de l'accès à la table.

Les e-mails de contact ne recevront que les notifications d'erreurs globales ou au niveau de la synchronisation, telles que les tables manquantes, les problèmes d'autorisations, etc. Ils ne recevront pas les problèmes au niveau des lignes. Les erreurs globales indiquent des problèmes critiques avec la connexion qui empêchent l'exécution des synchronisations. Ces problèmes peuvent inclure :

- Problèmes de connectivité
- Manque de ressources
- Problèmes d'autorisations
- (Pour les synchronisations de catalogues uniquement) Le niveau de catalogue n'a plus d'espace

Vous choisirez également le type de données et la fréquence de synchronisation. La fréquence peut aller de toutes les 15 minutes à une fois par mois. Le fuseau horaire configuré dans votre tableau de bord de Braze sera utilisé pour planifier la synchronisation récurrente. Les types de données pris en charge sont les attributs personnalisés, les événements personnalisés et les événements d'achat. Le type de données d'une synchronisation ne peut pas être modifié après sa création. 

#### Ajouter une clé publique à l'utilisateur Braze

À ce stade, vous devez revenir à Snowflake pour terminer la configuration. Ajoutez la clé publique affichée sur le tableau de bord à l'utilisateur que vous avez créé pour que Braze se connecte à Snowflake.

Pour plus d'informations, consultez la [documentation Snowflake](https://docs.snowflake.com/en/user-guide/key-pair-auth.html). Si vous souhaitez effectuer une rotation des clés, nous pouvons générer une nouvelle paire de clés et vous fournir la nouvelle clé publique.

```sql
ALTER USER BRAZE_INGESTION_USER SET RSA_PUBLIC_KEY='MIIBIjANBgkqhkiG9w0BA...';
```
{% endtab %}
{% tab Redshift %}

Dans le tableau de bord de Braze, accédez à **Data Settings** > **Cloud Data Ingestion**, sélectionnez **Create New Data Sync**, puis sélectionnez **Amazon Redshift Import**.

#### Étape 2.1 : Ajouter les informations de connexion Redshift et la table source

Saisissez les informations relatives à votre entrepôt de données Redshift et à votre table source. Si vous utilisez un tunnel de réseau privé, activez le curseur et saisissez les informations du tunnel. Passez ensuite à l'étape suivante. 

{% alert note %}
Dans le tableau de bord de Braze, le champ **Database name** n'accepte que les lettres (A-Z, a-z), les chiffres (0-9) et les traits de soulignement (_), bien qu'Amazon Redshift prenne en charge des caractères supplémentaires dans les identifiants de base de données.
{% endalert %}

#### Étape 2.2 : Configurer les détails de la synchronisation

Choisissez ensuite un nom pour votre synchronisation et saisissez les e-mails de contact. Ces coordonnées serviront à vous informer de toute erreur d'intégration, comme la suppression inattendue de l'accès à la table.

Les e-mails de contact ne recevront que les notifications d'erreurs globales ou au niveau de la synchronisation, telles que les tables manquantes, les problèmes d'autorisations, etc. Ils ne recevront pas les problèmes au niveau des lignes. Les erreurs globales indiquent des problèmes critiques avec la connexion qui empêchent l'exécution des synchronisations. Ces problèmes peuvent inclure :

- Problèmes de connectivité
- Manque de ressources
- Problèmes d'autorisations
- (Pour les synchronisations de catalogues uniquement) Le niveau de catalogue n'a plus d'espace

Vous choisirez également le type de données et la fréquence de synchronisation. La fréquence peut aller de toutes les 15 minutes à une fois par mois. Le fuseau horaire configuré dans votre tableau de bord de Braze sera utilisé pour planifier la synchronisation récurrente. Les types de données pris en charge sont les attributs personnalisés, les événements personnalisés et les événements d'achat. Le type de données d'une synchronisation ne peut pas être modifié après sa création. 
{% endtab %}
{% tab BigQuery %}

Dans le tableau de bord de Braze, accédez à **Data Settings** > **Cloud Data Ingestion**, sélectionnez **Create New Data Sync**, puis sélectionnez **Google BigQuery Import**.

#### Étape 2.1 : Ajouter les informations de connexion BigQuery et la table source

Chargez la clé JSON et fournissez un nom pour le compte de service, puis saisissez les détails de votre table source.

#### Étape 2.2 : Configurer les détails de la synchronisation

Choisissez ensuite un nom pour votre synchronisation et saisissez les e-mails de contact. Ces coordonnées serviront à vous informer de toute erreur d'intégration, comme la suppression inattendue de l'accès à la table.

Les e-mails de contact ne recevront que les notifications d'erreurs globales ou au niveau de la synchronisation, telles que les tables manquantes, les problèmes d'autorisations, etc. Ils ne recevront pas les problèmes au niveau des lignes. Les erreurs globales indiquent des problèmes critiques avec la connexion qui empêchent l'exécution des synchronisations. Ces problèmes peuvent inclure :

- Problèmes de connectivité
- Manque de ressources
- Problèmes d'autorisations
- (Pour les synchronisations de catalogues uniquement) Le niveau de catalogue n'a plus d'espace

Vous choisirez également le type de données et la fréquence de synchronisation. La fréquence peut aller de toutes les 15 minutes à une fois par mois. Le fuseau horaire configuré dans votre tableau de bord de Braze sera utilisé pour planifier la synchronisation récurrente. Les types de données pris en charge sont les attributs personnalisés, les événements personnalisés, les événements d'achat et les suppressions d'utilisateurs. Le type de données d'une synchronisation ne peut pas être modifié après sa création. 

{% endtab %}
{% tab Databricks %}

Dans le tableau de bord de Braze, accédez à **Data Settings** > **Cloud Data Ingestion**, sélectionnez **Create New Data Sync**, puis sélectionnez **Databricks Import**.

#### Étape 2.1 : Ajouter les informations de connexion Databricks et la table source

Saisissez les informations relatives à votre entrepôt de données Databricks et à votre table source, puis passez à l'étape suivante.

#### Étape 2.2 : Configurer les détails de la synchronisation

Choisissez ensuite un nom pour votre synchronisation et saisissez les e-mails de contact. Ces coordonnées serviront à vous informer de toute erreur d'intégration, comme la suppression inattendue de l'accès à la table.

Les e-mails de contact ne recevront que les notifications d'erreurs globales ou au niveau de la synchronisation, telles que les tables manquantes, les problèmes d'autorisations, etc. Ils ne recevront pas les problèmes au niveau des lignes. Les erreurs globales indiquent des problèmes critiques avec la connexion qui empêchent l'exécution des synchronisations. Ces problèmes peuvent inclure :

- Problèmes de connectivité
- Manque de ressources
- Problèmes d'autorisations
- (Pour les synchronisations de catalogues uniquement) Le niveau de catalogue n'a plus d'espace

Vous choisirez également le type de données et la fréquence de synchronisation. La fréquence peut aller de toutes les 15 minutes à une fois par mois. Le fuseau horaire configuré dans votre tableau de bord de Braze sera utilisé pour planifier la synchronisation récurrente. Les types de données pris en charge sont les attributs personnalisés, les événements personnalisés, les événements d'achat et les suppressions d'utilisateurs. Le type de données d'une synchronisation ne peut pas être modifié après sa création. 

{% endtab %}
{% tab Microsoft Fabric %}

#### Étape 2.1 : Configurer une synchronisation d'ingestion de données cloud

Vous allez créer une nouvelle synchronisation de données pour Microsoft Fabric. Dans le tableau de bord de Braze, accédez à **Data Settings** > **Cloud Data Ingestion**, sélectionnez **Create New Data Sync**, puis sélectionnez **Microsoft Fabric Import**.

#### Étape 2.2 : Ajouter les informations de connexion Microsoft Fabric et la table source

Saisissez les informations relatives aux identifiants de votre entrepôt Microsoft Fabric et à la table source, puis passez à l'étape suivante.

- Le nom des identifiants est un libellé pour ces identifiants dans Braze ; vous pouvez y définir une valeur descriptive.
- Consultez les étapes de la section 1 pour savoir comment récupérer l'ID de locataire, l'ID du principal, le secret client et la chaîne de connexion.

#### Étape 2.3 : Configurer les détails de la synchronisation

Configurez ensuite les détails suivants pour votre synchronisation : 

- Nom de la synchronisation 
- Type de données : les types de données pris en charge sont les attributs personnalisés, les événements personnalisés, les événements d'achat, les catalogues et les suppressions d'utilisateurs. Le type de données d'une synchronisation ne peut pas être modifié après sa création. 
- Fréquence de synchronisation : la fréquence peut aller de toutes les 15 minutes à une fois par mois. Le fuseau horaire configuré dans votre tableau de bord de Braze sera utilisé pour planifier la synchronisation récurrente. 
  - Les synchronisations non récurrentes peuvent être déclenchées manuellement ou via l'[API]({{site.baseurl}}/api/endpoints/cdi). 

#### Étape 2.4 : Configurer les préférences de notification

Saisissez ensuite les e-mails de contact. Ces coordonnées serviront à vous informer de toute erreur d'intégration, comme la suppression inattendue de l'accès à la table, ou à vous alerter lorsque des lignes spécifiques ne sont pas mises à jour.

Par défaut, les e-mails de contact ne recevront que les notifications d'erreurs globales ou au niveau de la synchronisation, telles que les tables manquantes, les problèmes d'autorisations, etc. Les erreurs globales indiquent des problèmes critiques avec la connexion qui empêchent l'exécution des synchronisations. Ces problèmes peuvent inclure :

- Problèmes de connectivité
- Manque de ressources
- Problèmes d'autorisations
- (Pour les synchronisations de catalogues uniquement) Le niveau de catalogue n'a plus d'espace

Vous pouvez également configurer des alertes pour les problèmes au niveau des lignes, ou choisir de recevoir une alerte chaque fois qu'une synchronisation s'exécute avec succès. 

{% endtab %}

{% endtabs %}

### Étape 3 : Tester la connexion

{% tabs %}
{% tab Snowflake %}

Retournez dans le tableau de bord de Braze et sélectionnez **Test connection**. En cas de succès, vous verrez un aperçu des données. Si la connexion échoue, un message d'erreur s'affichera pour vous aider à résoudre le problème.
{% endtab %}

{% tab Redshift %}
{% subtabs local %}
{% subtab Public Network %}
Retournez dans le tableau de bord de Braze et sélectionnez **Test connection**. En cas de succès, vous verrez un aperçu des données. Si la connexion échoue, un message d'erreur s'affichera pour vous aider à résoudre le problème.
{% endsubtab %}

{% subtab Private Network %}
Retournez dans le tableau de bord de Braze et sélectionnez **Test connection**. En cas de succès, vous verrez un aperçu des données. Si la connexion échoue, un message d'erreur s'affichera pour vous aider à résoudre le problème.
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab BigQuery %}

Après avoir saisi tous les détails de configuration de votre synchronisation, sélectionnez **Test connection**. En cas de succès, vous verrez un aperçu des données. Si la connexion échoue, un message d'erreur s'affichera pour vous aider à résoudre le problème.

{% endtab %}

{% tab Databricks %}

Après avoir saisi tous les détails de configuration de votre synchronisation, sélectionnez **Test connection**. En cas de succès, vous verrez un aperçu des données. Si la connexion échoue, un message d'erreur s'affichera pour vous aider à résoudre le problème.

{% endtab %}
{% tab Microsoft Fabric %}

Après avoir saisi tous les détails de configuration de votre synchronisation, sélectionnez **Test connection**. En cas de succès, vous verrez un aperçu des données. Si la connexion échoue, un message d'erreur s'affichera pour vous aider à résoudre le problème.

{% endtab %}
{% endtabs %}

{% alert note %}
Vous devez tester une intégration avec succès avant qu'elle ne puisse passer de l'état Brouillon à l'état Actif. Si vous devez fermer la page de création, votre intégration sera enregistrée et vous pourrez revenir à la page de détails pour effectuer des modifications et tester.  
{% endalert %}

## Configurer des intégrations ou des utilisateurs supplémentaires (facultatif)

{% tabs %}
{% tab Snowflake %}
Vous pouvez configurer plusieurs intégrations avec Braze, mais chaque intégration doit être configurée pour synchroniser une table différente. Lors de la création de synchronisations supplémentaires, vous pouvez réutiliser les identifiants existants si vous vous connectez au même compte Snowflake.

Si vous réutilisez le même utilisateur et le même rôle entre les intégrations, vous **n'aurez pas** besoin de repasser par l'étape d'ajout de la clé publique.
{% endtab %}
{% tab Redshift %}
Vous pouvez configurer plusieurs intégrations avec Braze, mais chaque intégration doit être configurée pour synchroniser une table différente. Lors de la création de synchronisations supplémentaires, vous pouvez réutiliser les identifiants existants si vous vous connectez au même compte Snowflake ou Redshift.

Si vous réutilisez le même utilisateur entre les intégrations, vous ne pouvez pas le supprimer dans le tableau de bord de Braze tant qu'il n'a pas été retiré de toutes les synchronisations actives.
{% endtab %}
{% tab BigQuery %}

Vous pouvez configurer plusieurs intégrations avec Braze, mais chaque intégration doit être configurée pour synchroniser une table différente. Lors de la création de synchronisations supplémentaires, vous pouvez réutiliser les identifiants existants si vous vous connectez au même compte BigQuery.

Si vous réutilisez le même utilisateur entre les intégrations, vous ne pouvez pas le supprimer dans le tableau de bord de Braze tant qu'il n'a pas été retiré de toutes les synchronisations actives.

{% endtab %}
{% tab Databricks %}

Vous pouvez configurer plusieurs intégrations avec Braze, mais chaque intégration doit être configurée pour synchroniser une table différente. Lors de la création de synchronisations supplémentaires, vous pouvez réutiliser les identifiants existants si vous vous connectez au même compte Databricks.

Si vous réutilisez le même utilisateur entre les intégrations, vous ne pouvez pas le supprimer dans le tableau de bord de Braze tant qu'il n'a pas été retiré de toutes les synchronisations actives.

{% endtab %}
{% tab Microsoft Fabric %}

Vous pouvez configurer plusieurs intégrations avec Braze, mais chaque intégration doit être configurée pour synchroniser une table différente. Lors de la création de synchronisations supplémentaires, vous pouvez réutiliser les identifiants existants si vous vous connectez au même compte Fabric.

Si vous réutilisez le même utilisateur entre les intégrations, vous ne pouvez pas le supprimer dans le tableau de bord de Braze tant qu'il n'a pas été retiré de toutes les synchronisations actives.

{% endtab %}
{% endtabs %}

## Exécuter la synchronisation

{% tabs %}
{% tab Snowflake %}
Une fois activée, votre synchronisation s'exécutera selon la planification configurée lors de la mise en place. Si vous souhaitez exécuter la synchronisation en dehors de la planification normale ou récupérer les données les plus récentes, sélectionnez **Sync Now**. Cette exécution n'aura pas d'impact sur les synchronisations futures régulièrement planifiées.

{% endtab %}
{% tab Redshift %}
Une fois activée, votre synchronisation s'exécutera selon la planification configurée lors de la mise en place. Si vous souhaitez exécuter la synchronisation en dehors de la planification normale ou récupérer les données les plus récentes, sélectionnez **Sync Now**. Cette exécution n'aura pas d'impact sur les synchronisations futures régulièrement planifiées.

{% endtab %}
{% tab BigQuery %}

Une fois activée, votre synchronisation s'exécutera selon la planification configurée lors de la mise en place. Si vous souhaitez exécuter la synchronisation en dehors de la planification normale ou récupérer les données les plus récentes, sélectionnez **Sync Now**. Cette exécution n'aura pas d'impact sur les synchronisations futures régulièrement planifiées.

{% endtab %}
{% tab Databricks %}

Une fois activée, votre synchronisation s'exécutera selon la planification configurée lors de la mise en place. Si vous souhaitez exécuter la synchronisation en dehors de la planification normale ou récupérer les données les plus récentes, sélectionnez **Sync Now**. Cette exécution n'aura pas d'impact sur les synchronisations futures régulièrement planifiées.

{% endtab %}
{% tab Microsoft Fabric %}

Une fois activée, votre synchronisation s'exécutera selon la planification configurée lors de la mise en place. Si vous souhaitez exécuter la synchronisation en dehors de la planification normale ou récupérer les données les plus récentes, sélectionnez **Sync Now**. Cette exécution n'aura pas d'impact sur les synchronisations futures régulièrement planifiées.

{% endtab %}

{% endtabs %}

{% enddetails %}