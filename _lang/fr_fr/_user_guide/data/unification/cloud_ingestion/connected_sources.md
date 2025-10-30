---
nav_title: Sources connectées
article_title: Sources connectées
description: "Cette page explique comment utiliser Braze Cloud Data Ingestion pour synchroniser des données pertinentes avec votre intégration Snowflake, Redshift, BigQuery et Databricks."
page_order: 2
page_type: reference

---

# Sources connectées

> Les sources connectées constituent une alternative zéro copie à la synchronisation directe des données avec la fonctionnalité Cloud Data Ingestion (CDI) de Braze. Une source connectée interroge directement votre entrepôt de données pour créer de nouveaux segments sans copier les données sous-jacentes dans Braze. 

Après avoir ajouté une source connectée à votre espace de travail Braze, vous pouvez créer un segment CDI dans Segment Extensions. Les CDI Segment Extensions vous permettent d'écrire un langage SQL qui interroge directement votre entrepôt de données (en utilisant les données mises à disposition par votre CDI Connected Source), et de créer et maintenir un groupe d'utilisateurs pouvant être ciblés au sein de Braze. 

Pour plus d'informations sur la création d'un segment avec cette source, reportez-vous à la section [Extensions de segments CDI.]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/cdi_segments/)

{% alert warning %}
Comme les sources connectées s'exécutent directement sur votre entrepôt de données, vous supporterez tous les coûts liés à l'exécution de ces requêtes dans votre entrepôt de données. Les sources connectées n'enregistrent pas les points de données et les CDI Segment Extensions ne consomment pas de crédits de segmentation SQL.
{% endalert %}

## Intégration des sources connectées

### Étape 1 : Connectez vos ressources

Les sources connectées de Cloud Data Ingestion nécessitent une certaine configuration sur Braze et dans votre instance. Suivez les étapes suivantes pour configurer l'intégration - certaines étapes seront effectuées dans votre entrepôt de données et d'autres dans votre tableau de bord de Braze.

{% tabs %}
{% tab Snowflake %}
**Dans votre entrepôt de données**
1. Créez un rôle et accordez des autorisations pour interroger et créer des tables dans un schéma.
2. Configurez votre entrepôt et donnez l'accès à ce rôle.
3. Créez un utilisateur pour ce rôle.
4. En fonction de votre configuration, vous devrez peut-être autoriser les IP de Braze dans votre politique de réseau Snowflake.

**Dans le tableau de bord de Braze**

{: start="5"}
5\. Créez une nouvelle source connectée dans le tableau de bord de Braze.
6\. Configurez les détails de la synchronisation pour la source connectée.
7\. Récupérez la clé publique fournie dans le tableau de bord de Braze.

**Dans votre entrepôt de données**

{: start="8"}
8\. Ajoutez la clé publique du tableau de bord de Braze à l'[utilisateur de Snowflake pour l'authentification](https://docs.snowflake.com/en/user-guide/key-pair-auth.html). Lorsque vous avez terminé, vous pouvez utiliser la source connectée pour créer une ou plusieurs extensions de segments CDI.
{% endtab %}

{% tab Redshift %}
1. Configurez les données sources et les ressources requises dans votre environnement Redshift.
2. Créez une nouvelle source connectée dans le tableau de bord de Braze.
4. Testez l'intégration.
5. Utilisez la source connectée pour créer une ou plusieurs extensions de segments CDI.
{% endtab %}

{% tab BigQuery %}
1. Configurez les données sources et les ressources requises dans votre environnement BigQuery.
2. Créez un compte de service et autorisez l'accès au(x) projet(s) BigQuery et au(x) jeu(x) de données qui contiennent les données que vous souhaitez synchroniser.  
3. Créez une nouvelle source connectée dans le tableau de bord de Braze.
4. Testez l'intégration.
5. Utilisez la source connectée pour créer une ou plusieurs extensions de segments CDI.
{% endtab %}

{% tab Databricks %}
1. Configurez les données sources et les ressources nécessaires dans votre environnement Databricks.
2. Créez un compte de service et autorisez l'accès au(x) projet(s) et jeu(x) de données Databricks contenant les données que vous souhaitez synchroniser.  
3. Créez une nouvelle source connectée dans le tableau de bord de Braze.
4. Testez l'intégration.
5. Utilisez la source connectée pour créer une ou plusieurs extensions de segments CDI.

{% alert important %}
Il peut y avoir un temps de chauffe de deux à cinq minutes lorsque Braze se connecte aux instances SQL Classic et Pro, ce qui entraînera des retards lors de la configuration et des essais de connexion, ainsi que lors de la création et de l'actualisation des extensions segment d'un CDI. L'utilisation d'une instance SQL sans serveur minimisera le temps de chauffe et améliorera le débit des requêtes, mais peut entraîner des coûts d'intégration légèrement plus élevés.
{% endalert %}

{% endtab %}

{% tab Microsoft Fabric %}
1. Créez un principal de service et autorisez l'accès à l'espace de travail Fabric qui sera utilisé pour votre intégration.   
2. Dans votre espace de travail Fabric, configurez les données sources et accordez des autorisations à votre principal de service 
3. Créez une nouvelle source connectée dans le tableau de bord de Braze.
4. Testez l'intégration.
5. Utilisez la source connectée pour créer une ou plusieurs extensions de segments CDI.
{% endtab %}

{% endtabs %}

### Étape 2 : Mettre en place votre entrepôt de données

Configurez les données sources et les ressources nécessaires dans votre environnement d'entrepôt de données. La source connectée peut référencer une ou plusieurs tables, assurez-vous donc que votre utilisateur Braze a le droit d'accéder à toutes les tables souhaitées dans la source connectée.

{% tabs %}
{% tab Snowflake %}
#### Étape 2.1 : Créer un rôle et accorder des autorisations

Créez un rôle pour votre source connectée. Ce rôle sera utilisé pour générer la liste des tables disponibles dans vos extensions de segments CDI, et pour interroger les tables sources afin de créer de nouveaux segments. Après la création de la source connectée, Braze découvre les noms et la description de toutes les tables disponibles pour l'utilisateur dans le schéma de la source.

Vous pouvez choisir d'accorder l'accès à toutes les tables d'un schéma ou d'accorder des privilèges uniquement à des tables spécifiques. Les tables auxquelles le rôle Braze a accès pourront être interrogées dans l'extension de segment CDI.

L'autorisation `create table` est nécessaire pour que Braze puisse créer une table avec les résultats de votre requête CDI Segment Extension avant de mettre à jour le segment dans Braze. Braze créera une table temporaire par segment, et la table ne persistera que pendant que Braze met à jour le segment.

```json
CREATE ROLE BRAZE_INGESTION_ROLE;

GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT CREATE TABLE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;

-- grant access to all current and future tables or views in the schema
GRANT SELECT ON ALL TABLES IN SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT SELECT ON FUTURE TABLES IN SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;

-- grant access to specific tables or views in the schema
GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC TO ROLE BRAZE_INGESTION_ROLE;

```

#### Étape 2.2 : Configurez l'entrepôt et donnez l'accès au rôle de Braze

```json
CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;

GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;
```

{% alert note %}
L'indicateur de **reprise automatique** doit être activé dans l'entrepôt. Si ce n'est pas le cas, vous devrez accorder à Braze des privilèges supplémentaires `OPERATE` sur l'entrepôt pour que Braze l'active au moment de l'exécution de la requête.
{% endalert %}

#### Étape 2.3 : Configurer l'utilisateur
```json
CREATE USER BRAZE_INGESTION_USER;

GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
```

Vous partagerez les informations de connexion avec Braze et recevrez une clé publique à ajouter à l'utilisateur lors d'une étape ultérieure.

{% alert note %}
Lorsque vous connectez différents espaces de travail au même compte Snowflake, vous devez créer un utilisateur unique pour chaque espace de travail Braze dans lequel vous créez une intégration. Au sein d'un espace de travail, vous pouvez réutiliser le même utilisateur entre les intégrations, mais la création d'une intégration échouera si un utilisateur du même compte Snowflake est dupliqué entre les espaces de travail.
{% endalert %}

#### Étape 2.4 : Autoriser les IP de Braze dans votre politique de réseau Snowflake (optionnel)

Selon la configuration de votre compte Snowflake, vous devrez peut-être autoriser les adresses IP suivantes dans votre politique de réseau Snowflake. Pour plus d'informations sur cette opération, reportez-vous à la documentation pertinente de Snowflake sur la [modification d'une politique de réseau](https://docs.snowflake.com/en/user-guide/network-policies.html#modifying-network-policies).

{% multi_lang_include data_centers.md datacenters='ips' %}
{% endtab %}

{% tab Redshift %}
#### Étape 2.1 : Créer un utilisateur et lui accorder des autorisations 

```json
CREATE USER braze_user PASSWORD '{password}';
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT CREATE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT SELECT ON TABLE USERS_ATTRIBUTES_SYNC TO braze_user;
```

Créez un utilisateur pour votre source connectée. Cet utilisateur sera utilisé pour générer la liste des tables disponibles dans vos extensions de segments CDI, et pour interroger les tables sources afin de créer de nouveaux segments. Après la création de la source connectée, Braze découvre les noms et la description de toutes les tables disponibles pour l'utilisateur dans le schéma de la source. Si vous créez plusieurs intégrations CDI, vous souhaiterez peut-être accorder des autorisations à un schéma ou gérer les autorisations à l'aide d'un groupe. 

Vous pouvez choisir d'accorder l'accès à toutes les tables d'un schéma ou d'accorder des privilèges uniquement à des tables spécifiques. Les tables auxquelles le rôle Braze a accès pourront être interrogées dans l'extension de segment CDI. Veillez à accorder à l'utilisateur l'accès à toutes les nouvelles tables lorsqu'elles sont créées, ou définissez des autorisations par défaut pour l'utilisateur. 

L'autorisation `create table` est nécessaire pour que Braze puisse créer une table avec les résultats de votre requête CDI Segment Extension avant de mettre à jour le segment dans Braze. Braze créera une table temporaire par segment, qui ne persistera que pendant la mise à jour du segment par Braze.


#### Étape 2.2 : Autoriser l'accès aux IP de Braze    

Si vous disposez d'un pare-feu ou d'autres stratégies réseau, vous devez donner à Braze un accès réseau à votre instance Redshift. Autorisez l'accès à partir des IP ci-dessous correspondant à la région de votre tableau de bord de Braze. 

Il se peut également que vous deviez modifier vos groupes de sécurité pour permettre à Braze d'accéder à vos données dans Redshift. Veillez à autoriser explicitement le trafic entrant sur les IP ci-dessous et sur le port utilisé pour interroger votre cluster Redshift (5439 par défaut). Vous devez explicitement autoriser la connectivité TCP de Redshift sur ce port, même si les règles d'entrée sont réglées sur "allow all". En outre, il est important que l'endpoint du cluster Redshift soit accessible au public pour que Braze puisse se connecter à votre cluster.

Si vous ne souhaitez pas que votre cluster Redshift soit accessible au public, vous pouvez configurer un VPC et une instance EC2 pour utiliser un tunnel ssh afin d'accéder aux données Redshift. Pour plus d'informations, consultez le site [AWS : Comment puis-je accéder à un cluster Amazon Redshift privé à partir de mon ordinateur local ?](https://repost.aws/knowledge-center/private-redshift-cluster-local-machine)

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}

{% tab BigQuery %}
#### Étape 2.1 : Créer un compte de service et accorder des autorisations 

Créez un compte de service dans GCP que Braze utilisera pour se connecter et lire les données de votre/vos table(s). Le compte de service doit disposer des autorisations suivantes : 

- **Utilisateur de connexion BigQuery :** Permet à Braze d'établir des connexions.
- **Utilisateur BigQuery :** Permet à Braze d'exécuter des requêtes, de lire les métadonnées des ensembles de données et de répertorier les tables.
- **BigQuery Data Viewer :** Permet d'accéder à Braze pour visualiser les ensembles de données et leur contenu.
- **BigQuery Job User :** Permet à Braze d'accéder à l'exécution des travaux.
- **bigquery.tables.create** Permet à Braze de créer des tables temporaires lors de l'actualisation des segments.

Créez un compte de service pour l'utilisation de votre source connectée. Cet utilisateur sera utilisé pour générer la liste des tables disponibles dans vos extensions de segments CDI, et pour interroger les tables sources afin de créer de nouveaux segments. Après la création de la source connectée, Braze découvre les noms et la description de toutes les tables disponibles pour l'utilisateur dans le schéma de la source. 

Vous pouvez choisir d'accorder l'accès à toutes les tables d'un ensemble de données ou d'accorder des privilèges uniquement à des tables spécifiques. Les tables auxquelles le rôle Braze a accès pourront être interrogées dans l'extension de segment CDI. 

L'autorisation `create table` est nécessaire pour que Braze puisse créer une table avec les résultats de votre requête CDI Segment Extension avant de mettre à jour le segment dans Braze. Braze créera une table temporaire par segment, et la table ne persistera que pendant que Braze met à jour le segment. 

Après avoir créé le compte de service et accordé les autorisations, générez une clé JSON. Pour plus d'informations, consultez [Google Cloud : Créer et supprimer des clés de compte de service](https://cloud.google.com/iam/docs/keys-create-delete). Vous le téléchargerez plus tard dans le tableau de bord de Braze.

#### Étape 2.2 : Autoriser l'accès aux IP de Braze    

Si vous avez mis en place des politiques de réseau, vous devez donner à Braze un accès réseau à votre instance de Big Query. Autorisez l'accès à partir des IP ci-dessous correspondant à la région de votre tableau de bord de Braze.  

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}

{% tab Databricks %}
#### Étape 2.1 : Créer un jeton d'accès  

Pour que Braze puisse accéder à Databricks, un jeton d'accès personnel doit être créé.

1. Dans votre espace de travail Databricks, sélectionnez votre nom d'utilisateur Databricks dans la barre supérieure, puis sélectionnez **User Settings** dans le menu déroulant.
2. Assurez-vous que le compte de service dispose des privilèges `CREATE TABLE` sur le schéma utilisé pour la source connectée. 
3. Dans l'onglet **Jetons d'accès**, sélectionnez **Générer un nouveau jeton**.
4. Saisissez un commentaire qui vous aide à identifier ce jeton, par exemple "Braze CDI", et remplacez la durée de vie du jeton par aucune durée de vie en laissant la case Durée de vie (jours) vide (vierge).
5. Sélectionnez **Générer**.
6. Copiez le jeton affiché, puis sélectionnez **Terminé**.

Ce jeton sera utilisé pour générer la liste des tables disponibles dans vos extensions de segments CDI et pour interroger les tables sources afin de créer de nouveaux segments. Après la création de la source connectée, Braze découvre les noms et la description de toutes les tables disponibles pour l'utilisateur dans le schéma de la source. 

Vous pouvez choisir d'accorder l'accès à toutes les tables d'un schéma ou d'accorder des privilèges uniquement à des tables spécifiques. Les tables auxquelles le rôle Braze a accès pourront être interrogées dans l'extension de segment CDI.

L'autorisation `create table` est nécessaire pour que Braze puisse créer une table avec les résultats de votre requête CDI Segment Extension avant de mettre à jour le segment dans Braze. Braze créera une table temporaire par segment, qui ne persistera que pendant la mise à jour du segment par Braze. 

Conservez le jeton en lieu sûr jusqu'à ce que vous ayez besoin de le saisir sur le tableau de bord de Braze lors de l'étape de création de justificatifs d'identité.

#### Étape 2.2 : Autoriser l'accès aux IP de Braze    

Si vous avez mis en place des politiques de réseau, vous devez donner à Braze un accès réseau à votre instance Databricks. Autorisez l'accès à partir des IP ci-dessous correspondant à la région de votre tableau de bord de Braze.  

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}

{% tab Microsoft Fabric %}
#### Étape 2.1 : Accorder l'accès aux ressources du tissu 
Braze se connectera à votre entrepôt Fabric à l'aide d'un principal de service avec authentification Entra ID. Vous créerez un nouveau principal de service que Braze utilisera et accorderez l'accès aux ressources Fabric selon les besoins. Braze aura besoin des informations suivantes pour se connecter :    

* ID de locataire (également appelé répertoire) pour votre compte Azure. 
* ID du principal (également appelé ID de l'application) pour le principal du service. 
* Secret client pour l'authentification de Braze

1. Dans le portail Azure, naviguez jusqu'au centre d'administration de Microsoft Entra, puis **App Registrations**.
2. Sélectionnez **\+ Nouvel enregistrement** sous **Identité > Applications > Enregistrements d'applications** 
3. Saisissez un nom et sélectionnez `Accounts in this organizational directory only` comme type de compte pris en charge. Sélectionnez ensuite **Enregistrer**. 
4. Sélectionnez l'application (service principal) que vous venez de créer, puis naviguez vers **Certificats & secrets > + Nouveau secret client**
5. Saisissez une description pour le secret et définissez une période d'expiration pour le secret. Sélectionnez ensuite **Ajouter**. 
6. Notez le secret client créé pour être utilisé dans la configuration de Braze. 

{% alert note %}
Azure n'autorise pas l'expiration illimitée des secrets des principaux services. N'oubliez pas d'actualiser les informations d'identification avant qu'elles n'expirent afin de maintenir le flux de données vers Braze.
{% endalert %}

#### Étape 2.2 : Accorder l'accès aux ressources du tissu 
Vous fournirez un accès permettant à Braze de se connecter à votre instance Fabric. Dans votre portail d'administration Fabric, naviguez vers **Paramètres** > **Gouvernance et informations** > **Portail d'administration** > **Paramètres des locataires**.    

* Dans les **paramètres du développeur**, activez l'option "Service principals can use Fabric APIs" pour que Braze puisse se connecter à l'aide de Microsoft Entra ID.
* Dans les **paramètres de OneLake**, activez "Les utilisateurs peuvent accéder aux données stockées dans OneLake avec des apps externes à Fabric" afin que le principal du service puisse accéder aux données à partir d'une app externe.

#### Étape 2.3 : Obtenir la chaîne de caractères de l'entrepôt 

Vous aurez besoin de l'endpoint SQL de votre entrepôt pour que Braze puisse se connecter. Pour récupérer l'endpoint SQL, accédez à l'**espace de travail** dans Fabric, et dans la liste des éléments, survolez le nom de l'entrepôt et sélectionnez **Copier la chaîne de caractères SQL**.

La page "Fabric Console" dans Microsoft azure, où les utilisateurs doivent récupérer la chaîne de caractères SQL.]({% image_buster /assets/img/cloud_ingestion/fabric_1.png %})

#### Étape 2.4 : Autoriser les IP de Braze dans le pare-feu (facultatif)

En fonction de la configuration de votre compte Microsoft Fabric, vous devrez peut-être autoriser les adresses IP suivantes dans votre pare-feu pour permettre le trafic en provenance de Braze. Pour plus d'informations sur l'activation de cette fonction, reportez-vous à la documentation relative à l'[accès conditionnel d'Entra.](https://learn.microsoft.com/en-us/fabric/security/protect-inbound-traffic#entra-conditional-access)

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}

{% endtabs %}

### Étape 3 : Créez une source connectée dans le tableau de bord de Braze.

{% tabs %}
{% tab Snowflake %}
#### Étape 3.1 : Ajouter les informations de connexion et le tableau des sources de Snowflake

Créez une source connectée dans le tableau de bord de Braze. Accédez à **Paramètres des données** > **Ingestion de données dans le cloud** > **Sources connectées**, puis sélectionnez **Créer une nouvelle synchronisation de données** > **Importation Snowflake**.

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_tab.png %}){: style="max-width:80%;"}

Saisissez les informations relatives à votre entrepôt de données Snowflake et à votre schéma source, puis passez à l'étape suivante.

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_sf_1.png %})

#### Étape 3.2 : Configurer les détails de la synchronisation

Choisissez un nom pour la source connectée. Ce nom sera utilisé dans la liste des sources disponibles lorsque vous créerez une nouvelle extension de segmentation CDI. 

Configurez une durée d'exécution maximale pour cette source. Lors de la création ou de l'actualisation d'un segment, Braze interrompt automatiquement les requêtes qui dépassent la durée d'exécution maximale. La durée d'exécution maximale autorisée est de 60 minutes ; une durée d'exécution inférieure réduira les coûts encourus sur votre compte Snowflake. 

{% alert note %}
Si les requêtes sont systématiquement interrompues alors que vous avez défini une durée d'exécution maximale de 60 minutes, envisagez d'optimiser le temps d'exécution de vos requêtes ou de dédier un entrepôt plus important à l'utilisateur de Braze.
{% endalert %}

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_sf_2.png %})

#### Étape 3.3 : Notez la clé publique  

Dans l'étape **Test connection**, notez la clé publique RSA. Vous en aurez besoin pour réaliser l'intégration dans Snowflake.

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_sf_3.png %})

{% endtab %}
{% tab Redshift %}
#### Étape 3.1 : Ajouter les informations de connexion Redshift et la table source

Créez une source connectée dans le tableau de bord de Braze. Accédez à **Paramètres des données** > **Ingestion de données dans le cloud** > **Sources connectées**, puis sélectionnez **Créer une connexion de données** > **Importation Amazon Redshift.**

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_tab.png %}){: style="max-width:80%;"}

Saisissez les informations relatives à votre entrepôt de données Redshift et à votre schéma source, puis passez à l'étape suivante.

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_rd_1.png %})

#### Étape 3.2 : Configurer les détails de la synchronisation

Choisissez un nom pour la source connectée. Ce nom sera utilisé dans la liste des sources disponibles lorsque vous créerez une nouvelle extension de segmentation CDI. 

Configurez une durée d'exécution maximale pour cette source. Lors de la création ou de l'actualisation d'un segment, Braze interrompt automatiquement les requêtes qui dépassent la durée d'exécution maximale. La durée d'exécution maximale autorisée est de 60 minutes ; une durée d'exécution inférieure réduira les coûts encourus sur votre compte Redshift. 

{% alert note %}
Si les requêtes sont systématiquement interrompues alors que vous avez défini une durée d'exécution maximale de 60 minutes, envisagez d'optimiser le temps d'exécution de vos requêtes ou de dédier un entrepôt plus important à l'utilisateur de Braze.
{% endalert %}

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_rd_2.png %})

#### Étape 3.3 : Notez la clé publique (facultatif)

Si vous avez sélectionné l'option **Connect with SSH Tunnel**, prenez note de la clé publique RSA dans l'étape **Test connection.**  Vous en aurez besoin pour terminer l'intégration dans Redshift.

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_rd_3.png %})

{% endtab %}
{% tab BigQuery %}
#### Étape 3.1 : Ajouter les informations de connexion BigQuery et la table source

Créez une source connectée dans le tableau de bord de Braze. Accédez à **Paramètres des données** > **Ingestion de données dans le cloud** > **Sources connectées**, puis sélectionnez **Créer une nouvelle synchronisation de données** > **Importation Google BigQuery**.

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_tab.png %}){: style="max-width:80%;"}

Saisissez les informations relatives à votre projet BigQuery et à votre jeu de données, puis passez à l'étape suivante.

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_bg_1.png %})

#### Étape 3.2 : Configurer les détails de la synchronisation

Choisissez un nom pour la source connectée. Ce nom sera utilisé dans la liste des sources disponibles lorsque vous créerez une nouvelle extension de segmentation CDI. 

Configurez une durée d'exécution maximale pour cette source. Lors de la création ou de l'actualisation d'un segment, Braze interrompt automatiquement les requêtes qui dépassent la durée d'exécution maximale. La durée d'exécution maximale autorisée est de 60 minutes ; une durée d'exécution inférieure réduira les coûts encourus sur votre compte BigQuery. 

{% alert note %}
Si les requêtes sont systématiquement interrompues alors que vous avez défini une durée d'exécution maximale de 60 minutes, envisagez d'optimiser le temps d'exécution de vos requêtes ou de dédier un entrepôt plus important à l'utilisateur de Braze.
{% endalert %}

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_bg_2.png %})

#### Étape 3.3 : Testez la connexion

Sélectionnez **Tester la connexion** pour vérifier que la liste des tables visibles par l'utilisateur correspond à ce que vous attendez, puis sélectionnez **Terminé**. Votre source connectée est maintenant créée et prête à être utilisée dans CDI Segment Extensions.

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_test_connection.png %})

{% endtab %}
{% tab Databricks %}
#### Étape 3.1 : Ajouter les informations de connexion Databricks et la table source

Créez une source connectée dans le tableau de bord de Braze. Accédez à **Paramètres des données** > **Ingestion de données dans le cloud** > **Sources connectées**, puis sélectionnez **Créer une nouvelle synchronisation de données** > **Importation de Databricks**.

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_tab.png %}){: style="max-width:80%;"}

Saisissez les informations relatives à vos identifiants Databricks et, en option, au catalogue et au schéma source, puis passez à l'étape suivante.

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_databricks_1.png %})

#### Étape 3.2 : Configurer les détails de la synchronisation

Choisissez un nom pour la source connectée. Ce nom sera utilisé dans la liste des sources disponibles lorsque vous créerez une nouvelle extension de segmentation CDI. 

Configurez une durée d'exécution maximale pour cette source. Lors de la création ou de l'actualisation d'un segment, Braze interrompt automatiquement les requêtes qui dépassent la durée d'exécution maximale. La durée d'exécution maximale autorisée est de 60 minutes ; une durée d'exécution inférieure réduira les coûts encourus sur votre compte Databricks. 

{% alert note %}
Si les requêtes sont systématiquement interrompues alors que vous avez défini une durée d'exécution maximale de 60 minutes, envisagez d'optimiser le temps d'exécution de vos requêtes ou de dédier un entrepôt plus important à l'utilisateur de Braze.
{% endalert %}

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_db_2.png %})

#### Étape 3.3 : Testez la connexion

Sélectionnez **Tester la connexion** pour vérifier que la liste des tables visibles par l'utilisateur correspond à ce que vous attendez, puis sélectionnez **Terminé**. Votre source connectée est maintenant créée et prête à être utilisée dans CDI Segment Extensions.

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_test_connection.png %})

{% endtab %}
{% tab Microsoft Fabric %}
#### Étape 3.1 : Ajouter les informations de connexion et la table source de Microsoft Fabric

Créez une source connectée dans le tableau de bord de Braze. Accédez à **Paramètres des données** > **Ingestion de données dans le cloud** > **Sources connectées**, puis sélectionnez **Créer une nouvelle synchronisation de données** > **Importation Microsoft Fabric.**

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_tab.png %}){: style="max-width:80%;"}

Saisissez les informations relatives à vos identifiants Microsoft Fabric, ainsi que l'entrepôt source et le schéma, puis passez à l'étape suivante.

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_mf_1.png %})

#### Étape 3.2 : Configurer les détails de la synchronisation

Choisissez un nom pour la source connectée. Ce nom sera utilisé dans la liste des sources disponibles lorsque vous créerez une nouvelle extension de segmentation CDI. 

Configurez une durée d'exécution maximale pour cette source. Lors de la création ou de l'actualisation d'un segment, Braze interrompt automatiquement les requêtes qui dépassent la durée d'exécution maximale. La durée d'exécution maximale autorisée est de 60 minutes ; une durée d'exécution inférieure réduira les coûts encourus sur votre compte Microsoft Fabric. 

{% alert note %}
Si les requêtes sont systématiquement interrompues alors que vous avez défini une durée d'exécution maximale de 60 minutes, essayez d'optimiser le temps d'exécution de vos requêtes ou d'augmenter la capacité de la base de données.
{% endalert %}

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_mf_2.png %})

#### Étape 3.3 : Testez la connexion

Sélectionnez **Tester la connexion** pour vérifier que la liste des tables visibles par l'utilisateur correspond à ce que vous attendez, puis sélectionnez **Terminé**. Votre source connectée est maintenant créée et prête à être utilisée dans CDI Segment Extensions.

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_test_connection.png %})

{% endtab %}
{% endtabs %}

### Étape 4 : Finaliser la configuration de l'entrepôt de données

{% tabs %}
{% tab Snowflake %}
Ajoutez la clé publique que vous avez notée lors de la dernière étape à votre utilisateur dans Snowflake. Cela permettra à Braze de se connecter à Snowflake. Pour plus de détails sur la manière de procéder, consultez la [documentation de Snowflake](https://docs.snowflake.com/en/user-guide/key-pair-auth.html). 

Si vous souhaitez effectuer une rotation des clés à un moment donné, vous pouvez créer une nouvelle clé publique en allant dans **Gestion de l'accès aux données** dans **Cloud Data Ingestion** et en sélectionnant **Générer une nouvelle clé** pour le compte concerné.

!Gestion de l'accès aux données pour les justificatifs d'accès aux données de Snowflake, avec un bouton pour générer une nouvelle clé.]({% image_buster /assets/img/cloud_ingestion/connected_source_sf_4.png %})

```json
ALTER USER BRAZE_INGESTION_USER SET rsa_public_key='{INSERT_YOUR_KEY}';
```

Après avoir ajouté la clé à l'utilisateur dans Snowflake, sélectionnez **Tester la connexion** dans Braze, puis **Terminé**. Votre source connectée est maintenant créée et prête à être utilisée dans CDI Segment Extensions.
{% endtab %}

{% tab Redshift %}
Si vous vous connectez avec un tunnel SSH, ajoutez la clé publique que vous avez notée lors de la dernière étape à l'utilisateur du tunnel SSH. 

Après avoir ajouté la clé à l'utilisateur, sélectionnez **Tester la connexion** dans Braze, puis **Terminé**. Votre source connectée est maintenant créée et prête à être utilisée dans CDI Segment Extensions.

{% endtab %}
{% tab BigQuery %}
Cela ne s'applique pas à BigQuery.

{% endtab %}
{% tab Databricks %}
Cela ne s'applique pas aux Databricks.

{% endtab %}
{% tab Microsoft Fabric %}
Cela ne s'applique pas à Microsoft Fabric.

{% endtab %}
{% endtabs %}

{% alert note %}
Vous devez tester avec succès une source avant qu'elle ne passe de l'état "brouillon" à l'état "actif". Si vous devez quitter la page de création, votre intégration sera enregistrée et vous pourrez revenir à la page de détails pour apporter des modifications et effectuer des tests.  
{% endalert %}

## Configuration d'intégrations ou d'utilisateurs supplémentaires (facultatif)

{% tabs %}
{% tab Snowflake %}
Vous pouvez configurer plusieurs intégrations avec Braze, mais chaque intégration doit être configurée pour connecter un schéma différent. Lors de la création de connexions supplémentaires, vous pouvez réutiliser les informations d'identification existantes si vous vous connectez au même compte Snowflake.

Si vous réutilisez le même utilisateur et le même rôle d'une intégration à l'autre, vous n'aurez pas besoin d'ajouter à nouveau la clé publique.
{% endtab %}

{% tab Redshift %}
Vous pouvez configurer plusieurs sources avec Braze, mais chaque source doit être configurée pour connecter un schéma différent. Lorsque vous créez des sources supplémentaires, vous pouvez réutiliser les informations d'identification existantes si vous vous connectez au même compte Redshift.
{% endtab %}

{% tab BigQuery %}
Vous pouvez configurer plusieurs sources avec Braze, mais chaque source doit être configurée pour connecter un ensemble de données différent. Lorsque vous créez des sources supplémentaires, vous pouvez réutiliser les informations d'identification existantes si vous vous connectez au même compte BigQuery.
{% endtab %}

{% tab Databricks %}
Vous pouvez configurer plusieurs sources avec Braze, mais chaque source doit être configurée pour connecter un schéma différent. Lorsque vous créez des sources supplémentaires, vous pouvez réutiliser les informations d'identification existantes si vous vous connectez au même compte Databricks.
{% endtab %}

{% tab Microsoft Fabric %}
Vous pouvez configurer plusieurs sources avec Braze, mais chaque source doit être configurée pour connecter un schéma différent. Lorsque vous créez des sources supplémentaires, vous pouvez réutiliser les informations d'identification existantes si vous vous connectez au même compte Azure.
{% endtab %}
{% endtabs %}

## Utilisation de la source connectée

Une fois la source créée, vous pouvez l'utiliser pour créer une ou plusieurs extensions de segments CDI. Pour plus d'informations sur la création d'un segment avec cette source, reportez-vous à la [documentation CDI Segment Extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/cdi_segments/).

{% alert note %}
Si les requêtes sont systématiquement interrompues alors que vous avez défini une durée d'exécution maximale de 60 minutes, envisagez d'optimiser le temps d'exécution de vos requêtes ou de dédier davantage de ressources de calcul (un entrepôt plus grand, par exemple) à l'utilisateur de Braze.
{% endalert %}
