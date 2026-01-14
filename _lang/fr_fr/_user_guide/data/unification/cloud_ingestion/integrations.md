---
nav_title: Intégration des entrepôts de données
article_title: "Intégration de l'entrepôt de données"
description: "Cette page explique comment utiliser Braze Cloud Data Ingestion pour synchroniser des données pertinentes avec votre intégration Snowflake, Redshift, BigQuery et Databricks."
page_order: 2
page_type: reference

---

# Intégration de l'entrepôt de données

> Cette page explique comment utiliser Braze Cloud Data Ingestion (CDI) pour synchroniser des données pertinentes avec votre intégration Snowflake, Redshift, BigQuery et Databricks.

## Mise en place d'intégrations d'entrepôts de données

Les intégrations de l'ingestion de données dans le cloud nécessitent une certaine configuration du côté de Braze et dans votre instance d'entrepôt de données. Suivez les étapes suivantes pour configurer l'intégration :

{% tabs %}
{% tab Snowflake %}
1. Dans votre instance Snowflake, configurez les tables ou les vues que vous souhaitez synchroniser avec Braze.
2. Créez une nouvelle intégration dans le tableau de bord de Braze.
3. Récupérez la clé publique fournie dans le tableau de bord de Braze et [ajoutez-la à l'utilisateur de Snowflake pour l'authentification](https://docs.snowflake.com/en/user-guide/key-pair-auth.html).
4. Testez l'intégration et lancez la synchronisation.

{% alert tip %}
Le [guide de démarrage rapide de Snowflake](https://quickstarts.snowflake.com/guide/braze_cdi/index.html) fournit un exemple de code et présente les étapes requises pour créer un pipeline automatisé utilisant Snowflake Streams et CDI pour synchroniser les données à Braze.
{% endalert %}
{% endtab %}
{% tab Redshift %}
1. Assurez-vous que l'accès à Braze est autorisé pour les tables Redshift que vous souhaitez synchroniser. Braze se connectera à Redshift via l'internet.
2. Dans votre instance Redshift, configurez les tables ou les vues que vous souhaitez synchroniser avec Braze.
3. Créez une nouvelle intégration dans le tableau de bord de Braze.
4. Testez l'intégration et lancez la synchronisation.
{% endtab %}
{% tab BigQuery %}
1. Créez un compte de service et autorisez l'accès au(x) projet(s) BigQuery et au(x) jeu(x) de données qui contiennent les données que vous souhaitez synchroniser.  
2. Dans votre compte BigQuery, configurez les tables ou les vues que vous souhaitez synchroniser avec Braze.   
3. Créez une nouvelle intégration dans le tableau de bord de Braze.  
4. Testez l'intégration et lancez la synchronisation.  
{% endtab %}
{% tab Databricks %}
1. Créez un compte de service et autorisez l'accès au(x) projet(s) et jeu(x) de données Databricks contenant les données que vous souhaitez synchroniser.  
2. Dans votre compte Databricks, configurez les tables ou les vues que vous souhaitez synchroniser avec Braze.   
3. Créez une nouvelle intégration dans le tableau de bord de Braze.  
4. Testez l'intégration et lancez la synchronisation.

{% alert important %}
Il peut y avoir un temps de chauffe de deux à cinq minutes lorsque Braze se connecte aux instances SQL Classic et Pro, ce qui entraînera des retards lors de la configuration et des tests de connexion, ainsi qu'au début des synchronisations planifiées. L'utilisation d'une instance SQL sans serveur minimisera le temps de chauffe et améliorera le débit des requêtes, mais peut entraîner des coûts d'intégration légèrement plus élevés.
{% endalert %}

{% endtab %}
{% tab Microsoft Fabric %}
1. Créez un principal de service et autorisez l'accès à l'espace de travail Fabric qui sera utilisé pour votre intégration.   
2. Dans votre espace de travail Fabric, configurez les tables ou les vues que vous souhaitez synchroniser avec Braze.   
3. Créez une nouvelle intégration dans le tableau de bord de Braze.  
4. Testez l'intégration et lancez la synchronisation.
{% endtab %}
{% endtabs %}

### Étape 1 : Configurer des tables ou des vues

{% tabs %}
{% tab Snowflake %}

#### Étape 1.1 : Dresser la table

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

Vous pouvez nommer la base de données, le schéma et la table comme vous le souhaitez, mais les noms des colonnes doivent correspondre à la définition précédente.

- `UPDATED_AT` - Heure à laquelle cette ligne a été mise à jour ou ajoutée au tableau. Nous ne synchroniserons que les lignes qui ont été ajoutées ou mises à jour depuis la dernière synchronisation.
- **Colonnes d'identification de l'utilisateur** \- Votre tableau peut contenir une ou plusieurs colonnes d'identification de l'utilisateur. Chaque ligne ne doit contenir qu'un seul identifiant (soit `external_id`, la combinaison de `alias_name` et `alias_label`, `braze_id`, `email` ou `phone`). Un tableau source peut comporter des colonnes pour un, deux, trois, quatre ou les cinq types d'identifiants.
    - `EXTERNAL_ID` - Il identifie l'utilisateur que vous souhaitez mettre à jour. Cette valeur devrait correspondre à la valeur `external_id` utilisée dans Braze. 
    - `ALIAS_NAME` et `ALIAS_LABEL` \- Ces deux colonnes créent un objet alias d'utilisateur. `alias_name` doit être un identifiant unique et `alias_label` spécifie le type d'alias. Les utilisateurs peuvent avoir plusieurs alias avec des libellés différents, mais un seul `alias_name` par `alias_label`.
    - `BRAZE_ID` - L'identifiant de l'utilisateur de Braze. Celui-ci est généré par le SDK de Braze, et il n'est pas possible de créer de nouveaux utilisateurs à l'aide d'un ID de Braze par le biais de l'ingestion de données dans le cloud. Pour créer de nouveaux utilisateurs, indiquez un ID externe ou un alias d'utilisateur.
    - `EMAIL` - L'adresse e-mail de l'utilisateur. S'il existe plusieurs profils avec la même adresse e-mail, le profil le plus récemment mis à jour sera prioritaire pour les mises à jour. Si vous indiquez à la fois l'e-mail et le téléphone, nous utiliserons l'e-mail comme identifiant principal.
    - `PHONE` - Le numéro de téléphone de l'utilisateur. S'il existe plusieurs profils avec le même numéro de téléphone, le profil le plus récemment mis à jour sera mis à jour en priorité. 
- `PAYLOAD` - Il s'agit d'une chaîne JSON des champs que vous souhaitez synchroniser avec l'utilisateur dans Braze.

#### Étape 1.2 : Configurer le rôle et les autorisations de la base de données

```json
CREATE ROLE BRAZE_INGESTION_ROLE;

GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC TO ROLE BRAZE_INGESTION_ROLE;
```

Modifiez les noms si nécessaire, mais les autorisations doivent correspondre à l'exemple précédent.

#### Étape 1.3 : Configurez l'entrepôt et donnez l'accès au rôle de Braze

```json
CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;

GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;
```

{% alert note %}
L'entrepôt doit avoir l'option de **reprise automatique** activée. Si ce n'est pas le cas, vous devrez accorder à Braze des privilèges supplémentaires `OPERATE` sur l'entrepôt pour que nous puissions l'activer au moment de l'exécution de la requête.
{% endalert %}

#### Étape 1.4 : Configurer l'utilisateur

```json
CREATE USER BRAZE_INGESTION_USER;

GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
```

Après cette étape, vous partagerez les informations de connexion avec Braze et recevrez une clé publique à joindre à l'utilisateur.

{% alert note %}
Lorsque vous connectez différents espaces de travail au même compte Snowflake, vous devez créer un utilisateur unique pour chaque espace de travail Braze dans lequel vous créez une intégration. Au sein d'un espace de travail, vous pouvez réutiliser le même utilisateur entre les intégrations, mais la création d'une intégration échouera si un utilisateur du même compte Snowflake est dupliqué entre les espaces de travail.
{% endalert %}

#### Étape 1.5 : Autoriser les IP de Braze dans la politique réseau de Snowflake (facultatif)

Selon la configuration de votre compte Snowflake, vous devrez peut-être autoriser les adresses IP suivantes dans votre politique de réseau Snowflake. Pour plus d'informations sur l'activation de cette fonction, consultez la documentation pertinente de Snowflake sur la [modification d'une politique de réseau](https://docs.snowflake.com/en/user-guide/network-policies.html#modifying-network-policies).

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}
{% tab Redshift %}

#### Étape 1.1 : Dresser la table 

Si vous le souhaitez, vous pouvez créer une nouvelle base de données et un nouveau schéma pour votre table source.
```json
CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
```
Créez une table (ou une vue) à utiliser pour votre intégration CDI
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

Vous pouvez nommer la base de données, le schéma et la table comme vous le souhaitez, mais les noms des colonnes doivent correspondre à la définition précédente.

- `UPDATED_AT` - Heure à laquelle cette ligne a été mise à jour ou ajoutée au tableau. Nous ne synchroniserons que les lignes qui ont été ajoutées ou mises à jour depuis la dernière synchronisation.
- **Colonnes d'identification de l'utilisateur** \- Votre tableau peut contenir une ou plusieurs colonnes d'identification de l'utilisateur. Chaque ligne ne doit contenir qu'un seul identifiant (soit `external_id`, la combinaison de `alias_name` et `alias_label`, `braze_id`, `email` ou `phone`). Un tableau source peut comporter des colonnes pour un, deux, trois, quatre ou les cinq types d'identifiants.
    - `EXTERNAL_ID` - Il identifie l'utilisateur que vous souhaitez mettre à jour. Cette valeur devrait correspondre à la valeur `external_id` utilisée dans Braze. 
    - `ALIAS_NAME` et `ALIAS_LABEL` \- Ces deux colonnes créent un objet alias d'utilisateur. `alias_name` doit être un identifiant unique et `alias_label` spécifie le type d'alias. Les utilisateurs peuvent avoir plusieurs alias avec des libellés différents, mais un seul `alias_name` par `alias_label`.
    - `BRAZE_ID` - L'identifiant de l'utilisateur de Braze. Celui-ci est généré par le SDK de Braze, et il n'est pas possible de créer de nouveaux utilisateurs à l'aide d'un ID de Braze par le biais de l'ingestion de données dans le cloud. Pour créer de nouveaux utilisateurs, indiquez un ID externe ou un alias d'utilisateur.
    - `EMAIL` - L'adresse e-mail de l'utilisateur. S'il existe plusieurs profils avec la même adresse e-mail, le profil le plus récemment mis à jour sera prioritaire pour les mises à jour. Si vous indiquez à la fois l'e-mail et le téléphone, nous utiliserons l'e-mail comme identifiant principal.
    - `PHONE` - Le numéro de téléphone de l'utilisateur. S'il existe plusieurs profils avec le même numéro de téléphone, le profil le plus récemment mis à jour sera mis à jour en priorité. 
- `PAYLOAD` - Il s'agit d'une chaîne JSON des champs que vous souhaitez synchroniser avec l'utilisateur dans Braze.
 
#### Étape 1.2 : Créer un utilisateur et lui accorder des autorisations 

```json
CREATE USER braze_user PASSWORD '{password}';
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT SELECT ON TABLE USERS_ATTRIBUTES_SYNC TO braze_user;
```

Il s'agit des autorisations minimales requises pour cet utilisateur. Si vous créez plusieurs intégrations CDI, vous souhaiterez peut-être accorder des autorisations à un schéma ou gérer les autorisations à l'aide d'un groupe. 

#### Étape 1.3 : Autoriser l'accès aux IP de Braze

Si vous disposez d'un pare-feu ou d'autres stratégies réseau, vous devez donner à Braze un accès réseau à votre instance Redshift. Un exemple d'endpoint URL Redshift est "exemple-cluster.ap-northeast-2.redshift.amazonaws.com".

Quelques points importants à connaître :
- Vous devrez peut-être également modifier vos groupes de sécurité pour permettre à Braze d'accéder à vos données dans Redshift.
- Veillez à autoriser explicitement le trafic entrant sur les IP du tableau et sur le port utilisé pour interroger votre cluster Redshift (5439 par défaut). Vous devez explicitement autoriser la connectivité TCP de Redshift sur ce port, même si les règles d'entrée sont réglées sur "allow all".
- L'endpoint du cluster Redshift doit être accessible au public pour que Braze puisse se connecter à votre cluster.
     - Si vous ne souhaitez pas que votre cluster Redshift soit accessible au public, vous pouvez configurer un VPC et une instance EC2 pour utiliser un tunnel SSH afin d'accéder aux données Redshift. Consultez cet [article du Centre de connaissances AWS](https://repost.aws/knowledge-center/private-redshift-cluster-local-machine) pour plus d'informations.
 
Autorisez l'accès à partir des IP suivantes correspondant à la région de votre tableau de bord de Braze.

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}
{% tab BigQuery %}

#### Étape 1.1 : Dresser la table 

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
| `UPDATED_AT`| TIMESTAMP | OBLIGATOIRE |
| `PAYLOAD`| JSON | OBLIGATOIRE |
| `EXTERNAL_ID`| CHAÎNE DE CARACTÈRES | NULLABLE |
| `ALIAS_NAME`| CHAÎNE DE CARACTÈRES | NULLABLE |
| `ALIAS_LABEL`| CHAÎNE DE CARACTÈRES | NULLABLE |
| `BRAZE_ID`| CHAÎNE DE CARACTÈRES | NULLABLE |
| `EMAIL`| CHAÎNE DE CARACTÈRES | NULLABLE |
| `PHONE`| CHAÎNE DE CARACTÈRES | NULLABLE |

Vous pouvez nommer le projet, le jeu de données et la table comme vous le souhaitez, mais les noms des colonnes doivent correspondre à la définition précédente.

- `UPDATED_AT` - Heure à laquelle cette ligne a été mise à jour ou ajoutée au tableau. Nous ne synchroniserons que les lignes qui ont été ajoutées ou mises à jour depuis la dernière synchronisation.
- **Colonnes d'identification de l'utilisateur** \- Votre tableau peut contenir une ou plusieurs colonnes d'identification de l'utilisateur. Chaque ligne ne doit contenir qu'un seul identifiant (soit `external_id`, la combinaison de `alias_name` et `alias_label`, `braze_id`, `email` ou `phone`). Un tableau source peut comporter des colonnes pour un, deux, trois, quatre ou les cinq types d'identifiants.
    - `EXTERNAL_ID` - Il identifie l'utilisateur que vous souhaitez mettre à jour. Cette valeur devrait correspondre à la valeur `external_id` utilisée dans Braze. 
    - `ALIAS_NAME` et `ALIAS_LABEL` \- Ces deux colonnes créent un objet alias d'utilisateur. `alias_name` doit être un identifiant unique et `alias_label` spécifie le type d'alias. Les utilisateurs peuvent avoir plusieurs alias avec des libellés différents, mais un seul `alias_name` par `alias_label`.
    - `BRAZE_ID` - L'identifiant de l'utilisateur de Braze. Celui-ci est généré par le SDK de Braze, et il n'est pas possible de créer de nouveaux utilisateurs à l'aide d'un ID de Braze par le biais de l'ingestion de données dans le cloud. Pour créer de nouveaux utilisateurs, indiquez un ID externe ou un alias d'utilisateur.
    - `EMAIL` - L'adresse e-mail de l'utilisateur. S'il existe plusieurs profils avec la même adresse e-mail, le profil le plus récemment mis à jour sera prioritaire pour les mises à jour. Si vous indiquez à la fois l'e-mail et le téléphone, nous utiliserons l'e-mail comme identifiant principal.
    - `PHONE` - Le numéro de téléphone de l'utilisateur. S'il existe plusieurs profils avec le même numéro de téléphone, le profil le plus récemment mis à jour sera mis à jour en priorité.
   e-mail varchar,
   phone_number varchar,
- `PAYLOAD` - Il s'agit d'une chaîne JSON des champs que vous souhaitez synchroniser avec l'utilisateur dans Braze.

#### Étape 1.2 : Créer un compte de service et accorder des autorisations 

Créez un compte de service dans GCP que Braze utilisera pour se connecter et lire les données de votre/vos table(s). Le compte de service doit disposer des autorisations suivantes : 

- **Utilisateur de connexion BigQuery :** Cela permettra à Braze d'établir des connexions
- **Utilisateur BigQuery :** Cela permettra à Braze d'accéder à l'exécution des requêtes, à la lecture des métadonnées des ensembles de données et à la liste des tableaux.
- **BigQuery Data Viewer :** Cela permettra à Braze d'accéder à la visualisation des ensembles de données et de leur contenu.
- **BigQuery Job User :** Cela permettra à Braze d'accéder à l'exécution des travaux.

Après avoir créé le compte de service et accordé les autorisations, générez une clé JSON. Vous trouverez plus d'informations sur la manière de procéder [ici.](https://cloud.google.com/iam/docs/keys-create-delete) Vous le mettrez à jour dans le tableau de bord de Braze ultérieurement. 

#### Étape 1.3 : Autoriser l'accès aux IP de Braze    

Si vous avez mis en place des politiques de réseau, vous devez donner à Braze un accès réseau à votre instance de Big Query. Autorisez l'accès à partir des IP ci-dessous correspondant à la région de votre tableau de bord de Braze.  

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}
{% tab Databricks %}

#### Étape 1.1 : Dresser la table 

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
  payload STRING, STRUCT, or MAP
);
```


| Nom du champ | Type | Mode |
|---|---|---|
| `UPDATED_AT`| TIMESTAMP | OBLIGATOIRE |
| `PAYLOAD`| Chaîne de caractères, STRUCT ou mappage | OBLIGATOIRE |
| `EXTERNAL_ID`| CHAÎNE DE CARACTÈRES | NULLABLE |
| `ALIAS_NAME`| CHAÎNE DE CARACTÈRES | NULLABLE |
| `ALIAS_LABEL`| CHAÎNE DE CARACTÈRES | NULLABLE |
| `BRAZE_ID`| CHAÎNE DE CARACTÈRES | NULLABLE |
| `EMAIL`| CHAÎNE DE CARACTÈRES | NULLABLE |
| `PHONE`| CHAÎNE DE CARACTÈRES | NULLABLE |

Vous pouvez nommer le schéma et la table comme vous le souhaitez, mais les noms des colonnes doivent correspondre à la définition précédente.

- `UPDATED_AT` - Heure à laquelle cette ligne a été mise à jour ou ajoutée au tableau. Nous ne synchroniserons que les lignes qui ont été ajoutées ou mises à jour depuis la dernière synchronisation.
- **Colonnes d'identification de l'utilisateur** \- Votre tableau peut contenir une ou plusieurs colonnes d'identification de l'utilisateur. Chaque ligne ne doit contenir qu'un seul identifiant (soit `external_id`, la combinaison de `alias_name` et `alias_label`, `braze_id`, `email` ou `phone`). Un tableau source peut comporter des colonnes pour un, deux, trois, quatre ou les cinq types d'identifiants.
    - `EXTERNAL_ID` - Il identifie l'utilisateur que vous souhaitez mettre à jour. Cette valeur devrait correspondre à la valeur `external_id` utilisée dans Braze. 
    - `ALIAS_NAME` et `ALIAS_LABEL` \- Ces deux colonnes créent un objet alias d'utilisateur. `alias_name` doit être un identifiant unique et `alias_label` spécifie le type d'alias. Les utilisateurs peuvent avoir plusieurs alias avec des libellés différents, mais un seul `alias_name` par `alias_label`.
    - `BRAZE_ID` - L'identifiant de l'utilisateur de Braze. Celui-ci est généré par le SDK de Braze, et il n'est pas possible de créer de nouveaux utilisateurs à l'aide d'un ID de Braze par le biais de l'ingestion de données dans le cloud. Pour créer de nouveaux utilisateurs, indiquez un ID externe ou un alias d'utilisateur. 
    - `EMAIL` - L'adresse e-mail de l'utilisateur. S'il existe plusieurs profils avec la même adresse e-mail, le profil le plus récemment mis à jour sera prioritaire pour les mises à jour. Si vous indiquez à la fois l'e-mail et le téléphone, nous utiliserons l'e-mail comme identifiant principal.
    - `PHONE` - Le numéro de téléphone de l'utilisateur. S'il existe plusieurs profils avec le même numéro de téléphone, le profil le plus récemment mis à jour sera mis à jour en priorité. 
- `PAYLOAD` - Il s'agit d'une chaîne de caractères ou d'une structure des champs que vous souhaitez synchroniser avec l'utilisateur dans Braze.

#### Étape 1.2 : Créer un jeton d'accès  

Pour que Braze puisse accéder à Databricks, un jeton d'accès personnel doit être créé.

1. Dans votre espace de travail Databricks, sélectionnez votre nom d'utilisateur Databricks dans la barre supérieure, puis sélectionnez **User Settings** dans le menu déroulant.
2. Dans l'onglet Jetons d'accès, sélectionnez **Générer un nouveau jeton**.
3. Saisissez un commentaire qui vous aide à identifier ce jeton, par exemple "Braze CDI", et remplacez la durée de vie du jeton par aucune durée de vie en laissant la case Durée de vie (jours) vide (vierge).
4. Sélectionnez **Générer**.
5. Copiez le jeton affiché, puis sélectionnez **Terminé**.

Conservez le jeton en lieu sûr jusqu'à ce que vous ayez besoin de le saisir sur le tableau de bord de Braze lors de l'étape de création de justificatifs d'identité.

#### Étape 1.3 : Autoriser l'accès aux IP de Braze    

Si vous avez mis en place des politiques de réseau, vous devez donner à Braze un accès réseau à votre instance Databricks. Autorisez l'accès à partir des IP ci-dessous correspondant à la région de votre tableau de bord de Braze.  

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}
{% tab Microsoft Fabric %}

#### Étape 1.1 : Configurer le principal du service et lui accorder l'accès
Braze se connectera à votre entrepôt Fabric à l'aide d'un principal de service avec authentification Entra ID. Vous créerez un nouveau principal de service que Braze utilisera et accorderez l'accès aux ressources Fabric selon les besoins. Braze aura besoin des informations suivantes pour se connecter :    

* ID de locataire (également appelé répertoire) pour votre compte Azure. 
* ID du principal (également appelé ID de l'application) pour le principal du service. 
* Secret client pour l'authentification de Braze

1. Dans le portail Azure, naviguez vers le centre d'administration de Microsoft Entra, puis vers App Registrations 
2. Sélectionnez **\+ Nouvel enregistrement** sous **Identité** > **Applications** > **Enregistrements d'applications.**
3. Saisissez un nom, puis sélectionnez `Accounts in this organizational directory only` comme type de compte pris en charge. Sélectionnez ensuite **Enregistrer**. 
4. Sélectionnez l'application (service principal) que vous venez de créer, puis naviguez vers **Certificats & secrets** > **\+ Nouveau secret client.**
5. Saisissez une description pour le secret et définissez une période d'expiration pour le secret. Sélectionnez ensuite **Ajouter**. 
6. Notez le secret client créé pour être utilisé dans la configuration de Braze. 

{% alert note %}
Azure n'autorise pas l'expiration illimitée des secrets des principaux services. N'oubliez pas d'actualiser les informations d'identification avant qu'elles n'expirent afin de maintenir le flux de données vers Braze.
{% endalert %}

#### Étape 1.2 : Accorder l'accès aux ressources du tissu 
Vous fournirez un accès permettant à Braze de se connecter à votre instance Fabric. Dans votre portail d'administration Fabric, naviguez vers **Paramètres** > **Gouvernance et informations** > **Portail d'administration** > **Paramètres des locataires**.    

* Dans les **paramètres du développeur**, activez l'option "Service principals can use Fabric APIs" pour que Braze puisse se connecter à l'aide de Microsoft Entra ID.
* Dans les **paramètres de OneLake**, activez "Les utilisateurs peuvent accéder aux données stockées dans OneLake avec des apps externes à Fabric" afin que le principal du service puisse accéder aux données à partir d'une app externe.


#### Étape 1.3 : Dresser la table
Braze prend en charge à la fois les tables et les vues dans les Fabric Warehouses. Si vous devez créer un nouvel entrepôt, allez dans **Créer > Entrepôt de données > Entrepôt** dans la console Fabric. 

```json
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
  --If you include both email and phone, we will use the email as the primary identifier
  EMAIL VARCHAR,
  PHONE VARCHAR
)
GO
```

Vous pouvez nommer l'entrepôt, le schéma et la table ou la vue comme vous le souhaitez, mais les noms des colonnes doivent correspondre à la définition précédente.

- `UPDATED_AT` - Heure à laquelle cette ligne a été mise à jour ou ajoutée au tableau. Nous ne synchroniserons que les lignes qui ont été ajoutées ou mises à jour depuis la dernière synchronisation.
- **Colonnes d'identification de l'utilisateur** \- Votre tableau peut contenir une ou plusieurs colonnes d'identification de l'utilisateur. Chaque ligne ne doit contenir qu'un seul identifiant (soit `external_id`, la combinaison de `alias_name` et `alias_label`, `braze_id`, `email` ou `phone`). Un tableau source peut comporter des colonnes pour un, deux, trois, quatre ou les cinq types d'identifiants.
    - `EXTERNAL_ID` - Il identifie l'utilisateur que vous souhaitez mettre à jour. Cette valeur devrait correspondre à la valeur `external_id` utilisée dans Braze. 
    - `ALIAS_NAME` et `ALIAS_LABEL` \- Ces deux colonnes créent un objet alias d'utilisateur. `alias_name` doit être un identifiant unique et `alias_label` spécifie le type d'alias. Les utilisateurs peuvent avoir plusieurs alias avec des libellés différents, mais un seul `alias_name` par `alias_label`.
    - `BRAZE_ID` - L'identifiant de l'utilisateur de Braze. Celui-ci est généré par le SDK de Braze, et il n'est pas possible de créer de nouveaux utilisateurs à l'aide d'un ID de Braze par le biais de l'ingestion de données dans le cloud. Pour créer de nouveaux utilisateurs, indiquez un ID externe ou un alias d'utilisateur.
    - `EMAIL` - L'adresse e-mail de l'utilisateur. S'il existe plusieurs profils avec la même adresse e-mail, le profil le plus récemment mis à jour sera prioritaire pour les mises à jour. Si vous indiquez à la fois l'e-mail et le téléphone, nous utiliserons l'e-mail comme identifiant principal.
    - `PHONE` - Le numéro de téléphone de l'utilisateur. S'il existe plusieurs profils avec le même numéro de téléphone, le profil le plus récemment mis à jour sera mis à jour en priorité. 
- `PAYLOAD` - Il s'agit d'une chaîne JSON des champs que vous souhaitez synchroniser avec l'utilisateur dans Braze.


#### Étape 1.4 : Obtenir la chaîne de caractères de l'entrepôt 
Vous aurez besoin de l'endpoint SQL de votre entrepôt pour que Braze puisse se connecter. Pour la récupérer, allez dans l'**espace de travail** dans Fabric, et dans la liste des éléments, survolez le nom de l'entrepôt et sélectionnez **Copier la chaîne de caractères SQL**.

La page "Fabric Console" dans Microsoft azure, où les utilisateurs doivent récupérer la chaîne de caractères SQL.]({% image_buster /assets/img/cloud_ingestion/fabric_1.png %})


#### Étape 1.5 : Autoriser les IP de Braze dans le pare-feu (facultatif)

En fonction de la configuration de votre compte Microsoft Fabric, vous devrez peut-être autoriser les adresses IP suivantes dans votre pare-feu pour permettre le trafic en provenance de Braze. Pour plus d'informations sur l'activation de cette fonction, reportez-vous à la documentation relative à l'[accès conditionnel d'Entra.](https://learn.microsoft.com/en-us/fabric/security/protect-inbound-traffic#entra-conditional-access)

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}

{% endtabs %}

### Étape 2 : Créez une nouvelle intégration dans le tableau de bord de Braze.

{% tabs %}
{% tab Snowflake %}

Dans le Braze Dashbord, accédez à **Paramètres des données** > **Ingestion de données dans le cloud**, sélectionnez **Créer une nouvelle synchronisation de données**, puis sélectionnez **Importation Snowflake**.

#### Étape 2.1 : Ajouter les informations de connexion et le tableau des sources de Snowflake

Saisissez les informations relatives à votre entrepôt de données Snowflake et à votre table source, puis passez à l'étape suivante.

La page "Create new import sync" pour Snowflake dans le tableau de bord de Braze avec l'exemple des données saisies à l'étape 1 : "Établir la connexion".]({% image_buster /assets/img/cloud_ingestion/ingestion_1.png %})

#### Étape 2.2 : Configurer les détails de la synchronisation

Ensuite, choisissez un nom pour votre synchronisation et saisissez les e-mails de vos contacts. Nous utiliserons ces coordonnées pour vous informer de toute erreur d'intégration, telle que la suppression inattendue de l'accès à la table.

Les e-mails de contact ne recevront que les notifications d'erreurs globales ou au niveau de la synchronisation, telles que les tables manquantes, les autorisations et autres. Ils ne recevront pas de numéros au niveau de la ligne. Les erreurs globales indiquent des problèmes critiques avec la connexion qui empêchent l'exécution des synchronisations. Ces problèmes peuvent être les suivants :

- Problèmes de connectivité
- Manque de ressources
- Problèmes de permissions
- (Pour les synchronisations de catalogues uniquement) Le niveau de catalogue n'a plus d'espace.

\![La page "Create new import sync" pour Snowflake dans le tableau de bord de Braze avec les données d'exemple ajoutées à l'étape 2 : "Configurez les détails de la synchronisation".]({% image_buster /assets/img/cloud_ingestion/ingestion_2.png %})

Vous choisirez également le type de données et la fréquence de synchronisation. La fréquence peut aller de toutes les 15 minutes à une fois par mois. Nous utiliserons le fuseau horaire configuré dans votre tableau de bord Braze pour planifier la synchronisation récurrente. Les types de données pris en charge sont les attributs personnalisés, les événements personnalisés et les événements d'achat. Le type de données d'une synchronisation ne peut pas être modifié après sa création. 

#### Ajouter une clé publique à l'utilisateur Braze

À ce stade, vous devez retourner à Snowflake pour terminer la configuration. Ajoutez la clé publique affichée sur le tableau de bord à l'utilisateur que vous avez créé pour Braze afin de vous connecter à Snowflake.

Pour plus d'informations sur la manière de procéder, consultez la [documentation de Snowflake](https://docs.snowflake.com/en/user-guide/key-pair-auth.html). Si vous souhaitez changer de clé à tout moment, nous pouvons générer une nouvelle paire de clés et vous fournir la nouvelle clé publique.

```json
ALTER USER BRAZE_INGESTION_USER SET rsa_public_key='Braze12345...';
```
{% endtab %}
{% tab Redshift %}

Dans le Braze Dashbord, accédez à **Paramètres des données** > **Ingestion de données dans le cloud**, sélectionnez **Créer une nouvelle synchronisation de données**, puis sélectionnez **Importation Amazon Redshift.**

#### Étape 2.1 : Ajouter les informations de connexion Redshift et la table source

Saisissez les informations relatives à votre entrepôt de données Redshift et à votre table source. Si vous utilisez un tunnel de réseau privé, basculez le curseur et saisissez les informations relatives au tunnel. Passez ensuite à l'étape suivante.

\![La page "Create new import sync" pour Redshift dans le tableau de bord de Braze, réglée sur l'étape 1 : "Établir la connexion".]({% image_buster /assets/img/cloud_ingestion/ingestion_6.png %})

#### Étape 2.2 : Configurer les détails de la synchronisation

Ensuite, choisissez un nom pour votre synchronisation et saisissez les e-mails de vos contacts. Nous utiliserons ces coordonnées pour vous informer de toute erreur d'intégration, telle que la suppression inattendue de l'accès à la table.

Les e-mails de contact ne recevront que les notifications d'erreurs globales ou au niveau de la synchronisation, telles que les tables manquantes, les autorisations et autres. Ils ne recevront pas de numéros au niveau de la ligne. Les erreurs globales indiquent des problèmes critiques avec la connexion qui empêchent l'exécution des synchronisations. Ces problèmes peuvent être les suivants :

- Problèmes de connectivité
- Manque de ressources
- Problèmes de permissions
- (Pour les synchronisations de catalogues uniquement) Le niveau de catalogue n'a plus d'espace.

La page "Create new import sync" pour Redshift dans le tableau de bord de Braze avec quelques données d'exemple ajoutées à l'étape 2 : "Configurez les détails de la synchronisation".]({% image_buster /assets/img/cloud_ingestion/ingestion_7.png %})

Vous choisirez également le type de données et la fréquence de synchronisation. La fréquence peut aller de toutes les 15 minutes à une fois par mois. Nous utiliserons le fuseau horaire configuré dans votre tableau de bord Braze pour planifier la synchronisation récurrente. Les types de données pris en charge sont les attributs personnalisés, les événements personnalisés et les événements d'achat. Le type de données d'une synchronisation ne peut pas être modifié après sa création.
{% endtab %}
{% tab BigQuery %}

Dans le Braze Dashbord, accédez à **Paramètres des données** > **Ingestion de données dans le cloud**, sélectionnez **Créer une nouvelle synchronisation de données**, puis sélectionnez **Importation Google BigQuery**.

#### Étape 2.1 : Ajouter les informations de connexion BigQuery et la table source

Téléchargez la clé JSON et fournissez un nom pour le compte de service, puis saisissez les détails de votre table source.

\![La page "Create new import sync" pour BigQuery dans le tableau de bord de Braze, réglée sur l'étape 1 : "Établir la connexion".]({% image_buster /assets/img/cloud_ingestion/ingestion_11.png %})

#### Étape 2.2 : Configurer les détails de la synchronisation

Ensuite, choisissez un nom pour votre synchronisation et saisissez les e-mails de vos contacts. Nous utiliserons ces coordonnées pour vous informer de toute erreur d'intégration, telle que la suppression inattendue de l'accès à la table.

Les e-mails de contact ne recevront que les notifications d'erreurs globales ou au niveau de la synchronisation, telles que les tables manquantes, les autorisations et autres. Ils ne recevront pas de numéros au niveau de la ligne. Les erreurs globales indiquent des problèmes critiques avec la connexion qui empêchent l'exécution des synchronisations. Ces problèmes peuvent être les suivants :

- Problèmes de connectivité
- Manque de ressources
- Problèmes de permissions
- (Pour les synchronisations de catalogues uniquement) Le niveau de catalogue n'a plus d'espace.

\![La page "Create new import sync" pour BigQuery dans le tableau de bord de Braze, réglée sur l'étape 2 : "Configurez les détails de la synchronisation".]({% image_buster /assets/img/cloud_ingestion/ingestion_12.png %})

Vous choisirez également le type de données et la fréquence de synchronisation. La fréquence peut aller de toutes les 15 minutes à une fois par mois. Nous utiliserons le fuseau horaire configuré dans votre tableau de bord Braze pour planifier la synchronisation récurrente. Les types de données pris en charge sont les attributs personnalisés, les événements personnalisés, les événements d'achat et les suppressions d'utilisateurs. Le type de données d'une synchronisation ne peut pas être modifié après sa création. 

{% endtab %}
{% tab Databricks %}

Dans le Braze Dashbord, accédez à **Paramètres des données** > **Ingestion de données dans le cloud**, sélectionnez **Créer une nouvelle synchronisation de données**, puis sélectionnez **Importation de Databricks**.

#### Étape 2.1 : Ajouter les informations de connexion Databricks et la table source

Saisissez les informations relatives à votre entrepôt de données Databricks et à votre table source, puis passez à l'étape suivante.

\![La page "Create new import sync" pour Databricks dans le tableau de bord de Braze, réglée sur Step 1 : "Établir la connexion".]({% image_buster /assets/img/cloud_ingestion/ingestion_16.png %})

#### Étape 2.2 : Configurer les détails de la synchronisation

Ensuite, choisissez un nom pour votre synchronisation et saisissez les e-mails de vos contacts. Nous utiliserons ces coordonnées pour vous informer de toute erreur d'intégration, telle que la suppression inattendue de l'accès à la table.

Les e-mails de contact ne recevront que les notifications d'erreurs globales ou au niveau de la synchronisation, telles que les tables manquantes, les autorisations et autres. Ils ne recevront pas de numéros au niveau de la ligne. Les erreurs globales indiquent des problèmes critiques avec la connexion qui empêchent l'exécution des synchronisations. Ces problèmes peuvent être les suivants :

- Problèmes de connectivité
- Manque de ressources
- Problèmes de permissions
- (Pour les synchronisations de catalogues uniquement) Le niveau de catalogue n'a plus d'espace.

\![La page "Create new import sync" pour Databricks dans le tableau de bord de Braze, réglée sur l'étape 2 : "Configurez les détails de la synchronisation".]({% image_buster /assets/img/cloud_ingestion/ingestion_12.png %})

Vous choisirez également le type de données et la fréquence de synchronisation. La fréquence peut aller de toutes les 15 minutes à une fois par mois. Nous utiliserons le fuseau horaire configuré dans votre tableau de bord Braze pour planifier la synchronisation récurrente. Les types de données pris en charge sont les attributs personnalisés, les événements personnalisés, les événements d'achat et les suppressions d'utilisateurs. Le type de données d'une synchronisation ne peut pas être modifié après sa création. 

{% endtab %}
{% tab Microsoft Fabric %}

#### Étape 2.1 : Mise en place d'une synchro d'ingestion de données dans le nuage

Vous allez créer une nouvelle synchronisation de données pour Microsoft Fabric. Dans le tableau de bord de Braze, accédez à **Paramètres des données** > **Ingestion de données dans le cloud**, sélectionnez **Créer une nouvelle synchronisation de données**, puis sélectionnez **Importation Microsoft Fabric.**

#### Étape 2.2 : Ajouter les informations de connexion et la table source de Microsoft Fabric

Saisissez les informations relatives aux références de votre entrepôt Microsoft Fabric et à la table source, puis passez à l'étape suivante.

- Credentials Name est une étiquette pour ces informations d'identification dans Braze, vous pouvez définir une valeur utile ici.
- Voir les étapes de la section 1 pour plus de détails sur la façon de récupérer l'ID du locataire, l'ID du principal, le secret du client et la chaîne de caractères de la connexion.

\![La page "Créer une nouvelle synchronisation d'importation" pour Microsoft dans le tableau de bord de Braze, réglée sur l'étape 1 : "Établir la connexion".]({% image_buster /assets/img/cloud_ingestion/fabric_setup_1.png %})

#### Étape 2.3 : Configurer les détails de la synchronisation

Ensuite, configurez les détails suivants pour votre synchronisation : 

- Nom de la synchronisation 
- Type de données - Les types de données pris en charge sont les attributs personnalisés, les événements personnalisés, les événements d'achat, les catalogues et les suppressions d'utilisateurs. Le type de données d'une synchronisation ne peut pas être modifié après sa création. 
- Fréquence de synchronisation - La fréquence peut aller de toutes les 15 minutes à une fois par mois. Nous utiliserons le fuseau horaire configuré dans votre tableau de bord Braze pour planifier la synchronisation récurrente. 
  - Les synchronisations non récurrentes peuvent être déclenchées manuellement ou via l'[API]({{site.baseurl}}/api/endpoints/cdi). 

La page "Créer une nouvelle synchronisation d'importation" pour Microsoft Fabric dans le tableau de bord de Braze, réglée sur l'étape 2 : "Configurez les détails de la synchronisation".]({% image_buster /assets/img/cloud_ingestion/fabric_setup_2.png %})


#### Étape 2.4 : Configurer les préférences de notification

Ensuite, saisissez les e-mails des personnes à contacter. Nous utiliserons ces informations de contact pour vous informer de toute erreur d'intégration, telle que la suppression inattendue de l'accès à la table, ou pour vous alerter lorsque des lignes spécifiques ne sont pas mises à jour.

Par défaut, les e-mails de contact ne recevront que des notifications d'erreurs globales ou au niveau de la synchronisation, telles que des tables manquantes, des autorisations et autres. Les erreurs globales indiquent des problèmes critiques avec la connexion qui empêchent l'exécution des synchronisations. Ces problèmes peuvent être les suivants :

- Problèmes de connectivité
- Manque de ressources
- Problèmes de permissions
- (Pour les synchronisations de catalogues uniquement) Le niveau de catalogue n'a plus d'espace.

Vous pouvez également configurer des alertes pour les problèmes au niveau des lignes ou choisir de recevoir une alerte chaque fois qu'une synchronisation s'exécute avec succès. 

\![La page "Créer une nouvelle synchronisation d'importation" pour Microsoft Fabric dans le tableau de bord de Braze, réglée sur l'étape 3 : "Configurer les préférences de notification".]({% image_buster /assets/img/cloud_ingestion/fabric_setup_3.png %})


{% endtab %}

{% endtabs %}

### Étape 3 : Test de connexion

{% tabs %}
{% tab Snowflake %}

Retournez dans le tableau de bord de Braze et sélectionnez **Tester la connexion**. En cas de succès, vous verrez un aperçu des données. Si, pour une raison quelconque, nous ne pouvons pas nous connecter, nous afficherons un message d'erreur pour vous aider à résoudre le problème.

\![La page "Create new import sync" pour Snowflake dans le tableau de bord de Braze avec l'étape 3 : "Connexion test" affichant une clé publique RSA.]({% image_buster /assets/img/cloud_ingestion/ingestion_3.png %})
{% endtab %}

{% tab Redshift %}
{% subtabs local %}
{% subtab Public Network %}
Retournez dans le tableau de bord de Braze et sélectionnez **Tester la connexion**. En cas de succès, vous verrez un aperçu des données. Si, pour une raison quelconque, nous ne pouvons pas nous connecter, nous afficherons un message d'erreur pour vous aider à résoudre le problème.

\![La page "Create new import sync" pour Redshift dans le tableau de bord de Braze, réglée sur l'étape 3 : "Test de connexion".]({% image_buster /assets/img/cloud_ingestion/ingestion_8.png %})
{% endsubtab %}

{% subtab Private Network %}
Retournez dans le tableau de bord de Braze et sélectionnez **Tester la connexion**. En cas de succès, vous verrez un aperçu des données. Si, pour une raison quelconque, nous ne pouvons pas nous connecter, nous afficherons un message d'erreur pour vous aider à résoudre le problème.

\![La page "Create new import sync" pour Redshift Private Network dans le tableau de bord de Braze, avec l'étape 4 : "Connexion test" affichant une clé publique RSA.]({% image_buster /assets/img/cloud_ingestion/ingestion_19.png %})
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab BigQuery %}

Une fois que tous les détails de la configuration de votre synchronisation ont été saisis, sélectionnez **Tester la connexion**. En cas de succès, vous verrez un aperçu des données. Si, pour une raison quelconque, nous ne pouvons pas nous connecter, nous afficherons un message d'erreur pour vous aider à résoudre le problème.

\![La page "Create new import sync" pour BigQuery dans le tableau de bord de Braze, réglée sur l'étape 3 : "Test de connexion".]({% image_buster /assets/img/cloud_ingestion/ingestion_13.png %})

{% endtab %}

{% tab Databricks %}

Une fois que tous les détails de la configuration de votre synchronisation ont été saisis, sélectionnez **Tester la connexion**. En cas de succès, vous verrez un aperçu des données. Si, pour une raison quelconque, nous ne pouvons pas nous connecter, nous afficherons un message d'erreur pour vous aider à résoudre le problème.

\![La page "Create new import sync" pour Databricks dans le tableau de bord de Braze, réglée sur l'étape 3 : "Test de connexion".]({% image_buster /assets/img/cloud_ingestion/ingestion_13.png %})

{% endtab %}
{% tab Microsoft Fabric %}

Une fois que tous les détails de la configuration de votre synchronisation ont été saisis, sélectionnez **Tester la connexion**. En cas de succès, vous verrez un aperçu des données. Si, pour une raison quelconque, nous ne pouvons pas nous connecter, nous afficherons un message d'erreur pour vous aider à résoudre le problème.

\![La page "Créer une nouvelle synchronisation d'importation" pour Microsoft Fabric dans le tableau de bord de Braze, réglée sur l'étape 4 : "Test de connexion".]({% image_buster /assets/img/cloud_ingestion/fabric_setup_4.png %})

{% endtab %}
{% endtabs %}

{% alert note %}
Vous devez tester avec succès une intégration avant qu'elle ne passe de l'état de projet à l'état actif. Si vous devez quitter la page de création, votre intégration sera enregistrée et vous pourrez revenir à la page de détails pour apporter des modifications et effectuer des tests.  
{% endalert %}

## Configurer des intégrations ou des utilisateurs supplémentaires (facultatif).

{% tabs %}
{% tab Snowflake %}
Vous pouvez configurer plusieurs intégrations avec Braze, mais chaque intégration doit être configurée pour synchroniser une table différente. Lors de la création de synchronisations supplémentaires, vous pouvez réutiliser les identifiants existants si vous vous connectez au compte Snowflake.

La page "Create new import sync" pour Snowflake dans le tableau de bord de Braze, avec le menu déroulant "Select credentials" ouvert à l'étape 1 : "Établir la connexion".]({% image_buster /assets/img/cloud_ingestion/ingestion_4.png %})

Si vous réutilisez le même utilisateur et le même rôle d'une intégration à l'autre, vous **n'aurez pas** besoin de repasser par l'étape de l'ajout de la clé publique.
{% endtab %}
{% tab Redshift %}
Vous pouvez configurer plusieurs intégrations avec Braze, mais chaque intégration doit être configurée pour synchroniser une table différente. Lors de la création de synchronisations supplémentaires, vous pouvez réutiliser les identifiants existants si vous vous connectez au même compte Snowflake ou Redshift.

La page "Create new import sync" pour Redshift dans le tableau de bord de Braze, avec le menu déroulant "Select credentials" ouvert à l'étape 1 : "Établir la connexion".]({% image_buster /assets/img/cloud_ingestion/ingestion_9.png %})

Si vous réutilisez le même utilisateur dans plusieurs intégrations, vous ne pouvez pas le supprimer dans le tableau de bord Braze tant qu'il n'a pas été supprimé de toutes les synchronisations actives.
{% endtab %}
{% tab BigQuery %}

Vous pouvez configurer plusieurs intégrations avec Braze, mais chaque intégration doit être configurée pour synchroniser une table différente. Lors de la création de synchronisations supplémentaires, vous pouvez réutiliser les informations d'identification existantes si vous vous connectez au même compte BigQuery.

La page "Create new import sync" pour BigQuery dans le tableau de bord de Braze, avec le menu déroulant "Select credentials" ouvert à l'étape 1 : "Établir la connexion".]({% image_buster /assets/img/cloud_ingestion/ingestion_14.png %})

Si vous réutilisez le même utilisateur dans plusieurs intégrations, vous ne pouvez pas le supprimer dans le tableau de bord Braze tant qu'il n'a pas été supprimé de toutes les synchronisations actives.

{% endtab %}
{% tab Databricks %}

Vous pouvez configurer plusieurs intégrations avec Braze, mais chaque intégration doit être configurée pour synchroniser une table différente. Lorsque vous créez des synchronisations supplémentaires, vous pouvez réutiliser les informations d'identification existantes si vous vous connectez au même compte Databricks.

La page "Create new import sync" pour Databricks dans le tableau de bord de Braze, avec le menu déroulant "Select credentials" ouvert à l'étape 1 : "Établir la connexion".]({% image_buster /assets/img/cloud_ingestion/ingestion_17.png %})

Si vous réutilisez le même utilisateur dans plusieurs intégrations, vous ne pouvez pas le supprimer dans le tableau de bord Braze tant qu'il n'a pas été supprimé de toutes les synchronisations actives.

{% endtab %}
{% tab Microsoft Fabric %}

Vous pouvez configurer plusieurs intégrations avec Braze, mais chaque intégration doit être configurée pour synchroniser une table différente. Lors de la création de synchronisations supplémentaires, vous pouvez réutiliser les informations d'identification existantes si vous vous connectez au même compte Fabric.

Si vous réutilisez le même utilisateur dans plusieurs intégrations, vous ne pouvez pas le supprimer dans le tableau de bord Braze tant qu'il n'a pas été supprimé de toutes les synchronisations actives.

{% endtab %}
{% endtabs %}

## Exécution de la synchronisation

{% tabs %}
{% tab Snowflake %}
Lorsqu'elle est activée, votre synchronisation s'effectuera selon la planification configurée lors de la configuration. Si vous souhaitez exécuter la synchronisation en dehors de la planification normale des tests ou récupérer les données les plus récentes, sélectionnez **Synchroniser maintenant.** Cette exécution n'aura pas d'impact sur les synchronisations futures régulièrement planifiées.

La page "Importation de données" pour Snowflake dans le tableau de bord de Braze affiche l'option "Synchroniser maintenant" dans le menu à ellipses verticales.]({% image_buster /assets/img/cloud_ingestion/ingestion_5.png %})

{% endtab %}
{% tab Redshift %}
Lorsqu'elle est activée, votre synchronisation s'effectuera selon la planification configurée lors de la configuration. Si vous souhaitez exécuter la synchronisation en dehors de la planification normale des tests ou récupérer les données les plus récentes, sélectionnez **Synchroniser maintenant.** Cette exécution n'aura pas d'impact sur les synchronisations futures régulièrement planifiées.

La page "Importation de données" pour Redshift dans le tableau de bord de Braze affiche l'option "Synchroniser maintenant" dans le menu à ellipses verticales.]({% image_buster /assets/img/cloud_ingestion/ingestion_10.png %})

{% endtab %}
{% tab BigQuery %}

Lorsqu'elle est activée, votre synchronisation s'effectuera selon la planification configurée lors de la configuration. Si vous souhaitez exécuter la synchronisation en dehors de la planification normale des tests ou récupérer les données les plus récentes, sélectionnez **Synchroniser maintenant.** Cette exécution n'aura pas d'impact sur les synchronisations futures régulièrement planifiées.

La page "Importation de données" pour BigQuery dans le tableau de bord de Braze affiche l'option "Synchroniser maintenant" dans le menu à ellipses verticales.]({% image_buster /assets/img/cloud_ingestion/ingestion_15.png %})

{% endtab %}
{% tab Databricks %}

Lorsqu'elle est activée, votre synchronisation s'effectuera selon la planification configurée lors de la configuration. Si vous souhaitez exécuter la synchronisation en dehors de la planification normale des tests ou récupérer les données les plus récentes, sélectionnez **Synchroniser maintenant.** Cette exécution n'aura pas d'impact sur les synchronisations futures régulièrement planifiées.

La page "Importation de données" pour Databricks dans le tableau de bord de Braze affiche l'option "Synchroniser maintenant" dans le menu à ellipses verticales.]({% image_buster /assets/img/cloud_ingestion/ingestion_18.png %})

{% endtab %}
{% tab Microsoft Fabric %}

Lorsqu'elle est activée, votre synchronisation s'effectuera selon la planification configurée lors de la configuration. Si vous souhaitez exécuter la synchronisation en dehors de la planification normale des tests ou récupérer les données les plus récentes, sélectionnez **Synchroniser maintenant.** Cette exécution n'aura pas d'impact sur les synchronisations futures régulièrement planifiées.

{% endtab %}

{% endtabs %}

