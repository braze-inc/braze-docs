---
nav_title: "Intégration de l'entrepôt de données"
article_title: "Intégration de l'entrepôt de données"
description: "Cet article de référence explique comment utiliser Cloud Data Ingestion de Braze pour synchroniser des données pertinentes avec votre intégration Snowflake, Redshift, BigQuery et Databricks."
page_order: 2
page_type: reference

---

# Intégration de l'entrepôt de données

> Cet article explique comment utiliser Cloud Data Ingestion (CDI) de Braze pour synchroniser des données pertinentes avec votre intégration Snowflake, Redshift, BigQuery et Databricks.

## Configuration du produit

Les intégrations d'ingestion de données dans le cloud nécessitent une certaine configuration du côté de Braze et dans votre instance. Suivez ces étapes pour configurer votre intégration :

{% tabs %}
{% tab Snowflake %}
1. Dans votre instance Snowflake, paramétrez les tables ou les vues que vous voulez synchroniser avec Braze.
2. Créez une nouvelle intégration dans le tableau de bord de Braze.
3. Récupérez la clé publique fournie dans le tableau de bord de Braze et [ajoutez-la à l'utilisateur de Snowflake pour authentification](https://docs.snowflake.com/en/user-guide/key-pair-auth.html).
4. Testez l’intégration et débutez la synchronisation.
{% endtab %}
{% tab Redshift %}
1. Assurez-vous que l'accès à Braze est autorisé pour les tables Redshift que vous souhaitez synchroniser. Braze se connectera à Redshift via l'internet.
2. Dans votre instance Redshift, configurez la ou les tables ou vues que vous souhaitez synchroniser avec Braze.
3. Créez une nouvelle intégration dans le tableau de bord de Braze.
4. Testez l’intégration et débutez la synchronisation.
{% endtab %}
{% tab BigQuery %}
1. Créez un compte de service et autorisez l'accès au(x) projet(s) BigQuery et au(x) jeu(x) de données qui contiennent les données que vous souhaitez synchroniser.  
2. Dans votre compte BigQuery, configurez la ou les tables ou vues que vous souhaitez synchroniser avec Braze.   
3. Créez une nouvelle intégration dans le tableau de bord de Braze.  
4. Testez l’intégration et débutez la synchronisation.  
{% endtab %}
{% tab Databricks %}
1. Créez un compte de service et autorisez l'accès au(x) projet(s) et jeu(x) de données Databricks contenant les données que vous souhaitez synchroniser.  
2. Dans votre compte Databricks, configurez la ou les tables ou vues que vous souhaitez synchroniser avec Braze.   
3. Créez une nouvelle intégration dans le tableau de bord de Braze.  
4. Testez l’intégration et débutez la synchronisation.

{% alert important %}
Il peut y avoir un temps de préchauffage de deux à cinq minutes au moment où Braze se connecte aux instances SQL Classic et Pro, ce qui entraînera des retards lors de la configuration et des tests de connexion, ainsi qu'au début des synchronisations planifiées. L'utilisation d'une instance SQL sans serveur permet de réduire ce temps de préchauffage et d’améliorer le débit des requêtes, mais peut entraîner des coûts d'intégration légèrement plus élevés.
{% endalert %}

{% endtab %}
{% endtabs %}

### Étape 1 : Paramétrez les tables et les vues

{% tabs %}
{% tab Snowflake %}

#### Étape 1 : Configurer le tableau

```json
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
     --If you include both email and phone, we will use the email as the primary identifier
     EMAIL VARCHAR(16777216),
     PHONE VARCHAR(16777216),
     PAYLOAD VARCHAR(16777216) NOT NULL
);
```

Vous pouvez donner le nom que vous désirez à la base de données, au schéma et au tableau, mais les noms de colonnes doivent correspondre aux définitions ci-dessus.

- `UPDATED_AT` : L’heure à laquelle la rangée a été mise à jour ou ajoutée au tableau. Nous ne synchroniserons que les rangées qui ont été ajoutées ou mises à jour depuis la dernière synchronisation.
- **Colonnes d'identification de l'utilisateur** \- Votre tableau peut contenir une ou plusieurs colonnes d'identification de l'utilisateur. Chaque ligne ne doit contenir qu'un seul identifiant (soit `external_id`, soit la combinaison de `alias_name` et `alias_label`, soit `braze_id`). Un tableau source peut comporter des colonnes pour un, deux ou les trois types d'identifiants. 
    - `EXTERNAL_ID` : Ceci identifie l’utilisateur que vous désirez mettre à jour. Cela doit correspondre à la valeur `external_id` utilisée dans Braze. 
    - `ALIAS_NAME` et `ALIAS_LABEL` : Ces deux colonnes créent un objet d'alias d'utilisateur. `alias_name` doit être un identifiant unique et `alias_label` spécifie le type d'alias. Les utilisateurs peuvent avoir plusieurs alias avec différentes étiquettes, mais seulement un `alias_name` par `alias_label`.
    - `BRAZE_ID` : L’identifiant d’utilisateur Braze. Celui-ci est généré par le SDK de Braze, et il n'est pas possible de créer de nouveaux utilisateurs à l'aide d'un ID de Braze par le biais de l'ingestion de données dans le cloud. Pour créer de nouveaux utilisateurs, spécifiez un ID utilisateur externe ou un alias utilisateur.
    - `EMAIL` - L'adresse e-mail de l'utilisateur. S'il existe plusieurs profils avec la même adresse e-mail, le profil le plus récemment mis à jour sera prioritaire pour les mises à jour. Si vous indiquez à la fois l'e-mail et le téléphone, nous utiliserons l'e-mail comme identifiant principal.
    - `PHONE` - Le numéro de téléphone de l'utilisateur. S'il existe plusieurs profils avec le même numéro de téléphone, le profil le plus récemment mis à jour sera mis à jour en priorité. 
- `PAYLOAD` : Il s’agit d’une chaîne de caractères JSON des champs que vous désirez synchroniser à l’utilisateur dans Braze.

#### Étape 2 : Définir le rôle et les autorisations de la base de données

```json
CREATE ROLE BRAZE_INGESTION_ROLE;

GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC TO ROLE BRAZE_INGESTION_ROLE;
```

Changez les noms si nécessaire, mais les permissions doivent correspondre à l’exemple ci-dessus.

#### Étape 3 : Définir l’entrepôt et donner accès au rôle Braze

```json
CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;

GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;
```

{% alert note %}
L'entrepôt devra avoir l'option de **reprise automatique** activée. Si ce n'est pas le cas, vous devrez accorder à Braze des privilèges `OPERATE` supplémentaires sur l'entrepôt pour que nous puissions l'activer au moment de l'exécution de la requête.
{% endalert %}

#### Étape 4 : Configurer l’utilisateur

```json
CREATE USER BRAZE_INGESTION_USER;

GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
```

Après cette étape, vous partagerez les informations de connexion avec Braze et vous recevrez une clé publique à ajouter (append) à l’utilisateur.

{% alert note %}
Lorsque vous connectez différents espaces de travail au même compte Snowflake, vous devez créer un utilisateur unique pour chaque espace de travail Braze dans lequel vous créez une intégration. Au sein d'un espace de travail, vous pouvez réutiliser le même utilisateur entre les intégrations, mais la création d'une intégration échouera si un utilisateur du même compte Snowflake est dupliqué entre les espaces de travail.
{% endalert %}

#### Étape 5 : Autoriser les IP de Braze dans la politique réseau de Snowflake (optionnel)

Selon la configuration de votre compte Snowflake, vous pourrez avoir à autoriser les adresses IP suivantes au sein de votre politique réseau Snowflake. Pour plus d'informations sur l'activation de cette fonction, consultez la documentation pertinente de Snowflake sur la [modification d'une politique de réseau](https://docs.snowflake.com/en/user-guide/network-policies.html#modifying-network-policies).

| Pour les instances `US-01`, `US-02`, `US-03`, `US-04`, `US-05`, `US-06`, `US-07` | Pour les instances `EU-01` et `EU-02` |
|---|---|
| `23.21.118.191`| `52.58.142.242`
| `34.206.23.173`| `52.29.193.121`
| `50.16.249.9`| `35.158.29.228`
| `52.4.160.214`| `18.157.135.97`
| `54.87.8.34`| `3.123.166.46`
| `54.156.35.251`| `3.64.27.36`
| `52.54.89.238`| `3.65.88.25`
| `18.205.178.15`| `3.68.144.188`
|   | `3.70.107.88`
{% endtab %}
{% tab Redshift %}

#### Étape 1 : Configurer le tableau 

De manière optionnelle, définissez une nouvelle base de données et un nouveau schéma pour contenir votre tableau source
```json
CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
```
Créer un tableau (ou vue) à utiliser pour votre intégration CDI
```json
CREATE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC (
   updated_at timestamptz default sysdate,
   --at least one of external_id, alias_name and alias_label, or braze_id is required
   external_id varchar,
   --if using user alias, both alias_name and alias_label are required
   alias_label varchar,
   alias_name varchar,
   --braze_id can only be used to update existing users created through the Braze SDK
   braze_id varchar,
   --If you include both email and phone, we will use the email as the primary identifier
   email varchar,
   phone varchar,
   payload varchar(max)
)
```

Vous pouvez donner le nom que vous désirez à la base de données, au schéma et au tableau, mais les noms de colonnes doivent correspondre aux définitions ci-dessus.

- `UPDATED_AT` : L’heure à laquelle la rangée a été mise à jour ou ajoutée au tableau. Nous ne synchroniserons que les rangées qui ont été ajoutées ou mises à jour depuis la dernière synchronisation.
- Colonnes d’identifiant utilisateur. Votre tableau peut contenir une ou plusieurs colonnes d’identifiants utilisateur. Chaque ligne ne doit contenir qu’un seul identifiant (soit un `external_id`, la combinaison d’un `alias_name` et d’un `alias_label`, soit un `braze_id`. Un tableau source peut comporter des colonnes pour un, deux ou les trois types d'identifiants. 
    - `EXTERNAL_ID` : Ceci identifie l’utilisateur que vous désirez mettre à jour. Cela doit correspondre à la valeur `external_id` utilisée dans Braze. 
    - `ALIAS_NAME` et `ALIAS_LABEL` : Ces deux colonnes créent un objet d'alias d'utilisateur. `alias_name` doit être un identifiant unique et `alias_label` spécifie le type d'alias. Les utilisateurs peuvent avoir plusieurs alias avec différentes étiquettes, mais seulement un `alias_name` par `alias_label`.
    - `BRAZE_ID` : L’identifiant d’utilisateur Braze. Celui-ci est généré par le SDK de Braze, et il n'est pas possible de créer de nouveaux utilisateurs à l'aide d'un ID de Braze par le biais de l'ingestion de données dans le cloud. Pour créer de nouveaux utilisateurs, spécifiez un ID utilisateur externe ou un alias utilisateur.
    - `EMAIL` - L'adresse e-mail de l'utilisateur. S'il existe plusieurs profils avec la même adresse e-mail, le profil le plus récemment mis à jour sera prioritaire pour les mises à jour. Si vous indiquez à la fois l'e-mail et le téléphone, nous utiliserons l'e-mail comme identifiant principal.
    - `PHONE` - Le numéro de téléphone de l'utilisateur. S'il existe plusieurs profils avec le même numéro de téléphone, le profil le plus récemment mis à jour sera mis à jour en priorité. 
- `PAYLOAD` : Il s’agit d’une chaîne de caractères JSON des champs que vous désirez synchroniser à l’utilisateur dans Braze.
 
#### Étape 2 : Créer un utilisateur et lui accorder des autorisations 

```json
CREATE USER braze_user PASSWORD '{password}';
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT SELECT ON TABLE USERS_ATTRIBUTES_SYNC TO braze_user;
```

Il s'agit des autorisations minimales requises pour cet utilisateur. Si vous créez plusieurs intégrations CDI, vous souhaiterez peut-être accorder des autorisations à un schéma ou gérer les autorisations à l'aide d'un groupe. 

#### Étape 3 : Autoriser l'accès aux IP de Braze

Si vous avez mis en place un pare-feu ou d’autres politiques réseau, vous devez donner à Braze un accès réseau à votre instance Redshift. Un exemple d'endpoint URL Redshift est "exemple-cluster.ap-northeast-2.redshift.amazonaws.com".

Quelques points importants à connaître :
- Vous devrez peut-être également modifier vos groupes de sécurité pour permettre à Braze d'accéder à vos données dans Redshift.
- Veillez à autoriser explicitement le trafic entrant sur les IP du tableau et sur le port utilisé pour interroger votre cluster Redshift (5439 par défaut). Vous devez explicitement autoriser la connectivité TCP Redshift sur ce port, même si les règles d'entrée sont définies sur « Autoriser tout ».
- L'endpoint du cluster Redshift doit être accessible au public pour que Braze puisse se connecter à votre cluster.
     - Si vous ne souhaitez pas que votre cluster Redshift soit accessible au public, vous pouvez configurer un VPC et une instance EC2 pour utiliser un tunnel SSH afin d'accéder aux données Redshift. Pour plus d’informations, consultez cet [article du Centre de connaissances AWS](https://repost.aws/knowledge-center/private-redshift-cluster-local-machine).
 
Autorisez l'accès à partir des IP suivantes correspondant à la région de votre tableau de bord de Braze.

| Pour les instances `US-01`, `US-02`, `US-03`, `US-04`, `US-05`, `US-06`, `US-07` | Pour les instances `EU-01` et `EU-02` |
|---|---|
| `23.21.118.191`| `52.58.142.242`
| `34.206.23.173`| `52.29.193.121`
| `50.16.249.9`| `35.158.29.228`
| `52.4.160.214`| `18.157.135.97`
| `54.87.8.34`| `3.123.166.46`
| `54.156.35.251`| `3.64.27.36`
| `52.54.89.238`| `3.65.88.25`
| `18.205.178.15`| `3.68.144.188`
|   | `3.70.107.88`
{% endtab %}
{% tab BigQuery %}

#### Étape 1 : Configurer le tableau 

Si vous le souhaitez, vous pouvez créer un nouveau projet ou un nouveau jeu de données qui contiendra votre table source.

```json
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

Créez une ou plusieurs tables à utiliser pour votre intégration CDI avec les champs suivants :

```json
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
  --If you include both email and phone, we will use the email as the primary identifier
  email STRING,
  phone STRING,
  payload JSON
);
```

| Nom du champ | Type | Mode |
|---|---|---|
| `UPDATED_AT`| DATE/HEURE | REQUIS |
| `PAYLOAD`| JSON | REQUIS |
| `EXTERNAL_ID`| CHAÎNE DE CARACTÈRES | NULLABLE |
| `ALIAS_NAME`| CHAÎNE DE CARACTÈRES | NULLABLE |
| `ALIAS_LABEL`| CHAÎNE DE CARACTÈRES | NULLABLE |
| `BRAZE_ID`| CHAÎNE DE CARACTÈRES | NULLABLE |
| `EMAIL`| CHAÎNE DE CARACTÈRES | NULLABLE |
| `PHONE`| CHAÎNE DE CARACTÈRES | NULLABLE |

Vous pouvez nommer le projet, l’ensemble de données et la table comme vous le souhaitez, mais les noms des colonnes doivent correspondre à la définition précédente.

- `UPDATED_AT` : L’heure à laquelle la rangée a été mise à jour ou ajoutée au tableau. Nous ne synchroniserons que les rangées qui ont été ajoutées ou mises à jour depuis la dernière synchronisation.
- Colonnes d’identifiant utilisateur. Votre tableau peut contenir une ou plusieurs colonnes d’identifiants utilisateur. Chaque ligne ne doit contenir qu'un seul identifiant (soit `external_id`, soit la combinaison de `alias_name` et `alias_label`, soit `braze_id`). Un tableau source peut comporter des colonnes pour un, deux ou les trois types d'identifiants. 
    - `EXTERNAL_ID` : Ceci identifie l’utilisateur que vous désirez mettre à jour. Cela doit correspondre à la valeur `external_id` utilisée dans Braze. 
    - `ALIAS_NAME` et `ALIAS_LABEL` : Ces deux colonnes créent un objet d'alias d'utilisateur. `alias_name` doit être un identifiant unique et `alias_label` spécifie le type d'alias. Les utilisateurs peuvent avoir plusieurs alias avec différentes étiquettes, mais seulement un `alias_name` par `alias_label`.
    - `BRAZE_ID` : L’identifiant d’utilisateur Braze. Celui-ci est généré par le SDK de Braze, et il n'est pas possible de créer de nouveaux utilisateurs à l'aide d'un ID de Braze par le biais de l'ingestion de données dans le cloud. Pour créer de nouveaux utilisateurs, spécifiez un ID utilisateur externe ou un alias utilisateur.
    - `EMAIL` - L'adresse e-mail de l'utilisateur. S'il existe plusieurs profils avec la même adresse e-mail, le profil le plus récemment mis à jour sera prioritaire pour les mises à jour. Si vous indiquez à la fois l'e-mail et le téléphone, nous utiliserons l'e-mail comme identifiant principal.
    - `PHONE` - Le numéro de téléphone de l'utilisateur. S'il existe plusieurs profils avec le même numéro de téléphone, le profil le plus récemment mis à jour sera mis à jour en priorité.
   e-mail varchar,
   phone_number varchar,
- `PAYLOAD` : Il s’agit d’une chaîne de caractères JSON des champs que vous désirez synchroniser à l’utilisateur dans Braze.

#### Étape 2 : Créer un compte de service et accorder des autorisations 

Créez un compte de service dans GCP que Braze utilisera pour se connecter et lire les données de votre/vos table(s). Le compte de service doit disposer des autorisations suivantes : 

- **Utilisateur de connexion BigQuery :** Cela permettra à Braze d'établir des connexions
- **Utilisateur BigQuery :** Cela permettra à Braze d'accéder à l'exécution des requêtes, à la lecture des métadonnées des ensembles de données et à la liste des tableaux.
- **Visualisateur des données BigQuery :** Cela permettra à Braze d'accéder à la visualisation des ensembles de données et de leur contenu.
- **Utilisateur des tâches BigQuery :** Cela permettra à Braze d'accéder à l'exécution des travaux.

Après avoir créé le compte de service et accordé les autorisations, générez une clé JSON. Vous trouverez plus d'informations sur la manière de procéder [ici.](https://cloud.google.com/iam/docs/keys-create-delete) Vous le mettrez à jour dans le tableau de bord de Braze ultérieurement. 

#### Étape 3 : Autoriser l'accès aux IP de Braze    

Si vous avez mis en place des politiques réseau, vous devez donner à Braze un accès réseau à votre instance Big Query. Autorisez l'accès à partir des IP ci-dessous correspondant à la région de votre tableau de bord de Braze.  

| Pour les instances `US-01`, `US-02`, `US-03`, `US-04`, `US-05`, `US-06`, `US-07` | Pour les instances `EU-01` et `EU-02` |
|---|---|
| `23.21.118.191`| `52.58.142.242`
| `34.206.23.173`| `52.29.193.121`
| `50.16.249.9`| `35.158.29.228`
| `52.4.160.214`| `18.157.135.97`
| `54.87.8.34`| `3.123.166.46`
| `54.156.35.251`| `3.64.27.36`
| `52.54.89.238`| `3.65.88.25`
| `18.205.178.15`| `3.68.144.188`
|   | `3.70.107.88`

{% endtab %}
{% tab Databricks %}

#### Étape 1 : Configurer le tableau 

Si vous le souhaitez, vous pouvez créer un nouveau catalogue ou un nouveau schéma qui contiendra votre table source.

```json
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

Créez une ou plusieurs tables à utiliser pour votre intégration CDI avec les champs suivants :


```json
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
  --If you include both email and phone, we will use the email as the primary identifier
  email STRING,
  phone STRING,
  payload STRING
);
```


| Nom du champ | Type | Mode |
|---|---|---|
| `UPDATED_AT`| DATE/HEURE | REQUIS |
| `PAYLOAD`| Chaîne de caractères ou STRUCT | REQUIS |
| `EXTERNAL_ID`| CHAÎNE DE CARACTÈRES | NULLABLE |
| `ALIAS_NAME`| CHAÎNE DE CARACTÈRES | NULLABLE |
| `ALIAS_LABEL`| CHAÎNE DE CARACTÈRES | NULLABLE |
| `BRAZE_ID`| CHAÎNE DE CARACTÈRES | NULLABLE |
| `EMAIL`| CHAÎNE DE CARACTÈRES | NULLABLE |
| `PHONE`| CHAÎNE DE CARACTÈRES | NULLABLE |

Vous pouvez nommer le schéma et la table comme vous le souhaitez, mais les noms des colonnes doivent correspondre à la définition précédente.

- `UPDATED_AT` : L’heure à laquelle la rangée a été mise à jour ou ajoutée au tableau. Nous ne synchroniserons que les rangées qui ont été ajoutées ou mises à jour depuis la dernière synchronisation.
- Colonnes d’identifiant utilisateur. Votre tableau peut contenir une ou plusieurs colonnes d’identifiants utilisateur. Chaque ligne ne doit contenir qu'un seul identifiant (soit `external_id`, soit la combinaison de `alias_name` et `alias_label`, soit `braze_id`). Un tableau source peut comporter des colonnes pour un, deux ou les trois types d'identifiants. 
    - `EXTERNAL_ID` : Ceci identifie l’utilisateur que vous désirez mettre à jour. Cela doit correspondre à la valeur `external_id` utilisée dans Braze. 
    - `ALIAS_NAME` et `ALIAS_LABEL` : Ces deux colonnes créent un objet d'alias d'utilisateur. `alias_name` doit être un identifiant unique et `alias_label` spécifie le type d'alias. Les utilisateurs peuvent avoir plusieurs alias avec différentes étiquettes, mais seulement un `alias_name` par `alias_label`.
    - `BRAZE_ID` : L’identifiant d’utilisateur Braze. Celui-ci est généré par le SDK de Braze, et il n'est pas possible de créer de nouveaux utilisateurs à l'aide d'un ID de Braze par le biais de l'ingestion de données dans le cloud. Pour créer de nouveaux utilisateurs, spécifiez un ID utilisateur externe ou un alias utilisateur. 
    - `EMAIL` - L'adresse e-mail de l'utilisateur. S'il existe plusieurs profils avec la même adresse e-mail, le profil le plus récemment mis à jour sera prioritaire pour les mises à jour. Si vous indiquez à la fois l'e-mail et le téléphone, nous utiliserons l'e-mail comme identifiant principal.
    - `PHONE` - Le numéro de téléphone de l'utilisateur. S'il existe plusieurs profils avec le même numéro de téléphone, le profil le plus récemment mis à jour sera mis à jour en priorité. 
- `PAYLOAD` - Il s'agit d'une chaîne de caractères ou d'une structure des champs que vous souhaitez synchroniser avec l'utilisateur dans Braze.

#### Étape 2 : Créer un jeton d'accès  

Pour que Braze puisse accéder à Databricks, un jeton d'accès personnel doit être créé.

1. Dans votre espace de travail Databricks, sélectionnez votre nom d'utilisateur Databricks dans la barre supérieure, puis sélectionnez **User Settings** dans le menu déroulant.
2. Dans l'onglet Jetons d'accès, sélectionnez **Générer un nouveau jeton**.
3. Saisissez un commentaire qui vous aide à identifier ce jeton, par exemple « Braze CDI », et remplacez la durée de vie du jeton par aucune durée de vie en laissant vide la case Durée de vie (jours).
4. Sélectionnez **Générer**.
5. Copiez le jeton affiché, puis sélectionnez **Terminé**.

Conservez le jeton en lieu sûr jusqu'à ce que vous ayez besoin de le saisir dans le tableau de bord de Braze lors de l'étape de création d’identifiants.

#### Étape 3 : Autoriser l'accès aux IP de Braze    

Si vous avez mis en place des politiques réseau, vous devez donner à Braze un accès réseau à votre instance Databricks. Autorisez l'accès à partir des IP ci-dessous correspondant à la région de votre tableau de bord de Braze.  

| Pour les instances `US-01`, `US-02`, `US-03`, `US-04`, `US-05`, `US-06`, `US-07` | Pour les instances `EU-01` et `EU-02` |
|---|---|
| `23.21.118.191`| `52.58.142.242`
| `34.206.23.173`| `52.29.193.121`
| `50.16.249.9`| `35.158.29.228`
| `52.4.160.214`| `18.157.135.97`
| `54.87.8.34`| `3.123.166.46`
| `54.156.35.251`| `3.64.27.36`
| `52.54.89.238`| `3.65.88.25`
| `18.205.178.15`| `3.68.144.188`
|   | `3.70.107.88`

{% endtab %}

{% endtabs %}

### Étape 2 : Créer une nouvelle intégration dans le tableau de bord de Braze

{% tabs %}
{% tab Snowflake %}

Allez dans **Intégrations partenaires** > Partenaires technologiques **.** Accédez à la page Snowflake et sélectionnez **Créer une nouvelle synchronisation d'importation**.

{% alert note %}
Si vous utilisez l'[ancienne navigation]({{site.baseurl}}/navigation), accédez à **Partenaires technologiques**.
{% endalert %}

#### Étape 1 : Ajouter les informations de connexion et la table source de Snowflake

Saisissez les informations relatives à votre entrepôt de données Snowflake et à votre tableau source, puis passez à l'étape suivante.

![]({% image_buster /assets/img/cloud_ingestion/ingestion_1.png %})

#### Étape 2 : Configurer les détails de la synchronisation
Choisissez ensuite un nom pour votre synchronisation et entrez les e-mails de contact. Nous utiliserons ces coordonnées pour vous informer de toute erreur d'intégration, telle que la suppression inattendue de l'accès à la table.

Les e-mails de contact ne recevront que les notifications d'erreurs globales ou au niveau de la synchronisation, telles que les tables manquantes, les autorisations et autres. Ils ne recevront pas de problèmes au niveau de la ligne. Les erreurs globales indiquent des problèmes critiques avec la connexion qui empêchent l'exécution des synchronisations. Ces problèmes peuvent être les suivants :

- Problèmes de connectivité
- Manque de ressources
- Problèmes de permissions
- (Pour les synchronisations de catalogues uniquement) Le niveau de catalogue n'a plus d'espace.

![]({% image_buster /assets/img/cloud_ingestion/ingestion_2.png %})

Vous choisirez également le type de données et la fréquence de synchronisation. La fréquence peut être définie une fois toutes les 15 minutes jusqu’à une fois par mois. Nous utiliserons le fuseau horaire configuré dans votre tableau de bord de Braze pour planifier la synchronisation récurrente. Les types de données pris en charge sont les attributs personnalisés, les événements personnalisés et les événements d'achat. Le type de données d'une synchronisation ne peut pas être modifié après sa création. 

#### Ajouter une clé publique à l’utilisateur Braze
À ce stade, vous devez revenir à Snowflake pour terminer la configuration. Ajoutez la clé publique affichée sur le tableau de bord à l’utilisateur que vous avez créé pour que Braze se connecte à Snowflake.

Pour plus d'informations sur la manière de procéder, consultez la [documentation Snowflake](https://docs.snowflake.com/en/user-guide/key-pair-auth.html). Si vous désirez, à un moment donné, faire alterner les clés, nous pouvons générer une nouvelle paire de clés et vous fournir une nouvelle clé publique.

```json
ALTER USER BRAZE_INGESTION_USER SET rsa_public_key='Braze12345...';
```
{% endtab %}
{% tab Redshift %}

Allez dans **Intégrations partenaires** > Partenaires technologiques **.** Accédez à la page Redshift et sélectionnez **Create new import sync (Créer une nouvelle synchronisation d'importation)**.

{% alert note %}
Si vous utilisez l'[ancienne navigation]({{site.baseurl}}/navigation), accédez à **Partenaires technologiques**.
{% endalert %}

#### Étape 1 : Ajouter les informations de connexion Redshift et la table source
Saisissez les informations relatives à votre entrepôt de données Redshift et à votre table source. Si vous utilisez un tunnel de réseau privé, basculez le curseur et saisissez les informations relatives au tunnel. Passez ensuite à l'étape suivante.

![]({% image_buster /assets/img/cloud_ingestion/ingestion_6.png %})

#### Étape 2 : Configurer les détails de la synchronisation
Choisissez ensuite un nom pour votre synchronisation et entrez les e-mails de contact. Nous utiliserons ces coordonnées pour vous informer de toute erreur d'intégration, telle que la suppression inattendue de l'accès à la table.

Les e-mails de contact ne recevront que les notifications d'erreurs globales ou au niveau de la synchronisation, telles que les tables manquantes, les autorisations et autres. Ils ne recevront pas de problèmes au niveau de la ligne. Les erreurs globales indiquent des problèmes critiques avec la connexion qui empêchent l'exécution des synchronisations. Ces problèmes peuvent être les suivants :

- Problèmes de connectivité
- Manque de ressources
- Problèmes de permissions
- (Pour les synchronisations de catalogues uniquement) Le niveau de catalogue n'a plus d'espace.

![]({% image_buster /assets/img/cloud_ingestion/ingestion_7.png %})

Vous choisirez également le type de données et la fréquence de synchronisation. La fréquence peut être définie une fois toutes les 15 minutes jusqu’à une fois par mois. Nous utiliserons le fuseau horaire configuré dans votre tableau de bord de Braze pour planifier la synchronisation récurrente. Les types de données pris en charge sont les attributs personnalisés, les événements personnalisés et les événements d'achat. Le type de données d'une synchronisation ne peut pas être modifié après sa création.
{% endtab %}
{% tab BigQuery %}

Allez dans **Intégrations partenaires** > Partenaires technologiques **.** Accédez à la page BigQuery et sélectionnez **Créer une nouvelle synchronisation d'importation**.

{% alert note %}
Si vous utilisez l'[ancienne navigation]({{site.baseurl}}/navigation), accédez à **Partenaires technologiques**.
{% endalert %}

#### Étape 1 : Ajouter les informations de connexion BigQuery et la table source
Chargez la clé JSON et fournissez un nom pour le compte de service, puis saisissez les détails de votre tableau source.

![]({% image_buster /assets/img/cloud_ingestion/ingestion_11.png %})

#### Étape 2 : Configurer les détails de la synchronisation
Choisissez ensuite un nom pour votre synchronisation et entrez les e-mails de contact. Nous utiliserons ces coordonnées pour vous informer de toute erreur d'intégration, telle que la suppression inattendue de l'accès à la table.

Les e-mails de contact ne recevront que les notifications d'erreurs globales ou au niveau de la synchronisation, telles que les tables manquantes, les autorisations et autres. Ils ne recevront pas de problèmes au niveau de la ligne. Les erreurs globales indiquent des problèmes critiques avec la connexion qui empêchent l'exécution des synchronisations. Ces problèmes peuvent être les suivants :

- Problèmes de connectivité
- Manque de ressources
- Problèmes de permissions
- (Pour les synchronisations de catalogues uniquement) Le niveau de catalogue n'a plus d'espace.

![]({% image_buster /assets/img/cloud_ingestion/ingestion_12.png %})

Vous choisirez également le type de données et la fréquence de synchronisation. La fréquence peut être définie une fois toutes les 15 minutes jusqu’à une fois par mois. Nous utiliserons le fuseau horaire configuré dans votre tableau de bord de Braze pour planifier la synchronisation récurrente. Les types de données pris en charge sont les attributs personnalisés, les événements personnalisés, les événements d'achat et les suppressions d'utilisateurs. Le type de données d'une synchronisation ne peut pas être modifié après sa création. 

{% endtab %}
{% tab Databricks %}

Allez dans **Intégrations partenaires** > Partenaires technologiques **.** Accédez à la page Databricks et sélectionnez **Créer une nouvelle synchronisation d’importation**.

{% alert note %}
Si vous utilisez l'[ancienne navigation]({{site.baseurl}}/navigation), accédez à **Partenaires technologiques**.
{% endalert %}

#### Étape 1 : Ajouter les informations de connexion Databricks et la table source
Saisissez les informations relatives à votre entrepôt de données Databricks et à votre tableau source, puis passez à l'étape suivante.

![]({% image_buster /assets/img/cloud_ingestion/ingestion_16.png %})

#### Étape 2 : Configurer les détails de la synchronisation
Choisissez ensuite un nom pour votre synchronisation et entrez les e-mails de contact. Nous utiliserons ces coordonnées pour vous informer de toute erreur d'intégration, telle que la suppression inattendue de l'accès à la table.

Les e-mails de contact ne recevront que les notifications d'erreurs globales ou au niveau de la synchronisation, telles que les tables manquantes, les autorisations et autres. Ils ne recevront pas de problèmes au niveau de la ligne. Les erreurs globales indiquent des problèmes critiques avec la connexion qui empêchent l'exécution des synchronisations. Ces problèmes peuvent être les suivants :

- Problèmes de connectivité
- Manque de ressources
- Problèmes de permissions
- (Pour les synchronisations de catalogues uniquement) Le niveau de catalogue n'a plus d'espace.

![]({% image_buster /assets/img/cloud_ingestion/ingestion_12.png %})

Vous choisirez également le type de données et la fréquence de synchronisation. La fréquence peut être définie une fois toutes les 15 minutes jusqu’à une fois par mois. Nous utiliserons le fuseau horaire configuré dans votre tableau de bord de Braze pour planifier la synchronisation récurrente. Les types de données pris en charge sont les attributs personnalisés, les événements personnalisés, les événements d'achat et les suppressions d'utilisateurs. Le type de données d'une synchronisation ne peut pas être modifié après sa création. 

{% endtab %}
{% endtabs %}

### Étape 3 : Tester la connexion

{% tabs %}
{% tab Snowflake %}

Retournez dans le tableau de bord de Braze et sélectionnez **Tester la connexion**. Si vous avez réussi, vous pourrez voir un aperçu des données. Si, pour une raison quelconque, nous ne pouvons pas nous connecter, nous afficherons un message d’erreur pour vous aider à résoudre le problème.

![]({% image_buster /assets/img/cloud_ingestion/ingestion_3.png %})
{% endtab %}
{% tab Redshift %}
Retournez dans le tableau de bord de Braze et sélectionnez **Tester la connexion**. Si vous avez réussi, vous pourrez voir un aperçu des données. Si, pour une raison quelconque, nous ne pouvons pas nous connecter, nous afficherons un message d’erreur pour vous aider à résoudre le problème.

![]({% image_buster /assets/img/cloud_ingestion/ingestion_8.png %})
{% endtab %}
{% tab Réseau privé Redshift %}

Retournez dans le tableau de bord de Braze et sélectionnez **Tester la connexion**. Si vous avez réussi, vous pourrez voir un aperçu des données. Si, pour une raison quelconque, nous ne pouvons pas nous connecter, nous afficherons un message d’erreur pour vous aider à résoudre le problème.

![]({% image_buster /assets/img/cloud_ingestion/ingestion_19.png %})
{% endtab %}
{% tab BigQuery %}

Après avoir saisi tous les détails de la configuration de votre synchronisation, sélectionnez **Tester la connexion**. Si vous avez réussi, vous pourrez voir un aperçu des données. Si, pour une raison quelconque, nous ne pouvons pas nous connecter, nous afficherons un message d’erreur pour vous aider à résoudre le problème.

![]({% image_buster /assets/img/cloud_ingestion/ingestion_13.png %})

{% endtab %}
{% tab Databricks %}

Après avoir saisi tous les détails de la configuration de votre synchronisation, sélectionnez **Tester la connexion**. Si vous avez réussi, vous pourrez voir un aperçu des données. Si, pour une raison quelconque, nous ne pouvons pas nous connecter, nous afficherons un message d’erreur pour vous aider à résoudre le problème.

![]({% image_buster /assets/img/cloud_ingestion/ingestion_13.png %})

{% endtab %}
{% endtabs %}

{% alert note %}
Vous devez avoir testé une intégration avec succès avant qu’elle ne puisse passer de l’état d’ébauche à l’état actif. Si vous avez besoin de fermer la page de création, votre intégration sera sauvegardée et vous pourrez revenir à la page Détails pour effectuer des changements et les tester.  
{% endalert %}

## Définir des intégrations ou des utilisateurs supplémentaires (optionnel)

{% tabs %}
{% tab Snowflake %}
Vous pouvez également définir plusieurs intégrations avec Braze, mais chaque intégration devra être configurée pour se synchroniser à un tableau différent. Lors de la création de synchronisations supplémentaires, vous pouvez réutiliser les identifiants existants si vous vous connectez au compte Snowflake.

![]({% image_buster /assets/img/cloud_ingestion/ingestion_4.png %})

Si vous réutilisez le même utilisateur et le même rôle d'une intégration à l'autre, vous **n'aurez pas** besoin de repasser par l'étape de l'ajout de la clé publique.
{% endtab %}
{% tab Redshift %}
Vous pouvez également définir plusieurs intégrations avec Braze, mais chaque intégration devra être configurée pour se synchroniser à un tableau différent. Lors de la création de synchronisations supplémentaires, vous pouvez réutiliser les identifiants existants si vous vous connectez au même compte Snowflake ou Redshift.

![]({% image_buster /assets/img/cloud_ingestion/ingestion_9.png %})

Si vous réutilisez le même utilisateur dans plusieurs intégrations, vous ne pouvez pas le supprimer dans le tableau de bord Braze tant qu'il n'a pas été supprimé de toutes les synchronisations actives.
{% endtab %}
{% tab BigQuery %}

Vous pouvez également définir plusieurs intégrations avec Braze, mais chaque intégration devra être configurée pour se synchroniser à un tableau différent. Lors de la création de synchronisations supplémentaires, vous pouvez réutiliser les informations d'identification existantes si vous vous connectez au même compte BigQuery.

![]({% image_buster /assets/img/cloud_ingestion/ingestion_14.png %})

Si vous réutilisez le même utilisateur dans plusieurs intégrations, vous ne pouvez pas le supprimer dans le tableau de bord Braze tant qu'il n'a pas été supprimé de toutes les synchronisations actives.

{% endtab %}
{% tab Databricks %}

Vous pouvez également définir plusieurs intégrations avec Braze, mais chaque intégration devra être configurée pour se synchroniser à un tableau différent. Lorsque vous créez des synchronisations supplémentaires, vous pouvez réutiliser les informations d'identification existantes si vous vous connectez au même compte Databricks.

![]({% image_buster /assets/img/cloud_ingestion/ingestion_17.png %})

Si vous réutilisez le même utilisateur dans plusieurs intégrations, vous ne pouvez pas le supprimer dans le tableau de bord Braze tant qu'il n'a pas été supprimé de toutes les synchronisations actives.

{% endtab %}
{% endtabs %}

## Exécuter la synchronisation

{% tabs %}
{% tab Snowflake %}
Lorsqu'elle est activée, votre synchronisation s'effectuera selon la planification configurée lors de la configuration. Si vous souhaitez exécuter la synchronisation en dehors de la planification normale des tests ou récupérer les données les plus récentes, sélectionnez **Synchroniser maintenant.** Cette exécution n’aura pas d’impact sur les synchronisations futures et habituelles planifiées.

![]({% image_buster /assets/img/cloud_ingestion/ingestion_5.png %})

{% endtab %}
{% tab Redshift %}
Lorsqu'elle est activée, votre synchronisation s'effectuera selon la planification configurée lors de la configuration. Si vous souhaitez exécuter la synchronisation en dehors de la planification normale des tests ou récupérer les données les plus récentes, sélectionnez **Synchroniser maintenant.** Cette exécution n’aura pas d’impact sur les synchronisations futures et habituelles planifiées.

![]({% image_buster /assets/img/cloud_ingestion/ingestion_10.png %})

{% endtab %}
{% tab BigQuery %}

Lorsqu'elle est activée, votre synchronisation s'effectuera selon la planification configurée lors de la configuration. Si vous souhaitez exécuter la synchronisation en dehors de la planification normale des tests ou récupérer les données les plus récentes, sélectionnez **Synchroniser maintenant.** Cette exécution n’aura pas d’impact sur les synchronisations futures et habituelles planifiées.

![]({% image_buster /assets/img/cloud_ingestion/ingestion_15.png %})

{% endtab %}
{% tab Databricks %}

Lorsqu'elle est activée, votre synchronisation s'effectuera selon la planification configurée lors de la configuration. Si vous souhaitez exécuter la synchronisation en dehors de la planification normale des tests ou récupérer les données les plus récentes, sélectionnez **Synchroniser maintenant.** Cette exécution n’aura pas d’impact sur les synchronisations futures et habituelles planifiées.

![]({% image_buster /assets/img/cloud_ingestion/ingestion_18.png %})

{% endtab %}
{% endtabs %}

[1]: {% image_buster /assets/img/cloud_ingestion/ingestion_6.png %}
[2]: {% image_buster /assets/img/cloud_ingestion/ingestion_7.png %}
[3]: {% image_buster /assets/img/cloud_ingestion/ingestion_8.png %}
[4]: {% image_buster /assets/img/cloud_ingestion/ingestion_9.png %}
[5]: {% image_buster /assets/img/cloud_ingestion/ingestion_10.png %}
[6]: {% image_buster /assets/img/cloud_ingestion/ingestion_5.png %}
