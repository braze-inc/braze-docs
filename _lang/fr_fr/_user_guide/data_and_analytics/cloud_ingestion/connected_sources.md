---
nav_title: Sources connectées
article_title: Sources connectées
description: "Cet article de référence explique comment utiliser Cloud Data Ingestion de Braze pour synchroniser des données pertinentes avec votre intégration Snowflake, Redshift, BigQuery et Databricks."
page_order: 2
page_type: reference

---

# Sources connectées

> Les sources connectées constituent une alternative en zéro copie à la synchronisation directe des données avec la fonctionnalité Cloud Data Ingestion (CDI) de Braze. Une source connectée interroge directement votre entrepôt de données pour créer de nouveaux segments sans copier les données sous-jacentes dans Braze. 

Après avoir ajouté une source connectée à votre espace de travail Braze, vous pouvez créer un segment CDI dans Segment Extensions. Les segments CDI vous permettent d'écrire du langage SQL qui interroge directement votre entrepôt de données (en utilisant les données mises à disposition par votre source connectée CDI), et de créer et maintenir un groupe d'utilisateurs qui peut être ciblé dans Braze. 

Pour plus d'informations sur la création d'un segment avec cette source, consultez la rubrique [Segments CDI.]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/cdi_segments/)

{% alert warning %}
Étant donné que les sources connectées s'exécutent directement sur votre entrepôt de données, vous prenez en charge tous les coûts liés à l'exécution de ces requêtes dans votre entrepôt de données. Les sources connectées ne consomment pas de points de données et les segments CDI ne consomment pas de crédits de segments SQL.
{% endalert %}

## Intégration des sources connectées

### Étape 1 : Connectez vos ressources

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
8\. Ajoutez la clé publique fournie dans le tableau de bord de Braze à l'[utilisateur Snowflake pour l'authentification](https://docs.snowflake.com/en/user-guide/key-pair-auth.html). Lorsque vous avez terminé, vous pouvez utiliser la source connectée pour créer un ou plusieurs segments CDI.
{% endtab %}

{% tab Redshift %}
1. Configurez les données sources et les ressources requises dans votre environnement Redshift.
2. Créez une nouvelle source connectée dans le tableau de bord de Braze.
4. Testez l'intégration.
5. Utilisez la source connectée pour créer une ou plusieurs segmentations CDI.
{% endtab %}

{% tab BigQuery %}
1. Configurez les données sources et les ressources requises dans votre environnement BigQuery.
2. Créez un compte de service et autorisez l'accès au(x) projet(s) BigQuery et au(x) jeu(x) de données qui contiennent les données que vous souhaitez synchroniser.  
3. Créez une nouvelle source connectée dans le tableau de bord de Braze.
4. Testez l'intégration.
5. Utilisez la source connectée pour créer une ou plusieurs segmentations CDI.
{% endtab %}

{% tab Databricks %}
1. Configurez les données sources et les ressources nécessaires dans votre environnement Databricks.
2. Créez un compte de service et autorisez l'accès au(x) projet(s) et jeu(x) de données Databricks contenant les données que vous souhaitez synchroniser.  
3. Créez une nouvelle source connectée dans le tableau de bord de Braze.
4. Testez l'intégration.
5. Utilisez la source connectée pour créer une ou plusieurs segmentations CDI.

{% alert important %}
Il peut y avoir un temps de préchauffage de deux à cinq minutes au moment où Braze se connecte aux instances SQL Classic et Pro, ce qui entraînera des retards lors de la configuration et des tests de connexion, ainsi que lors de la création et de l’actualisation des segments CDI. L'utilisation d'une instance SQL sans serveur permet de réduire ce temps de préchauffage et d’améliorer le débit des requêtes, mais peut entraîner des coûts d'intégration légèrement plus élevés.
{% endalert %}

{% endtab %}
{% endtabs %}

### Étape 2 : Configurez votre entrepôt de données

Configurez les données sources et les ressources nécessaires dans votre environnement d'entrepôt de données. La source connectée peut référencer une ou plusieurs tables, assurez-vous donc que votre utilisateur Braze a le droit d'accéder à toutes les tables souhaitées dans la source connectée.

{% tabs %}
{% tab Snowflake %}
#### Étape 2.1 : Créer un rôle et accorder des autorisations

Créez un rôle pour votre source connectée. Ce rôle sera utilisé pour générer la liste des tables disponibles dans vos segments CDI, et pour interroger les tables sources afin de créer de nouveaux segments. Après la création de la source connectée, Braze découvre les noms et la description de toutes les tables disponibles pour l'utilisateur dans le schéma de la source.

Vous pouvez choisir d'accorder l'accès à toutes les tables d'un schéma ou d'accorder des privilèges uniquement à des tables spécifiques. Les tables auxquelles le rôle Braze a accès pourront être interrogées dans le segment CDI.

L'autorisation `create table` est nécessaire pour que Braze puisse créer une table avec les résultats de votre requête de segment CDI avant de mettre à jour le segment dans Braze. Braze créera une table temporaire par segment, et la table ne persistera que pendant que Braze met à jour le segment.

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

#### Étape 2.2 : Définir l’entrepôt et donner accès au rôle Braze

```json
CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;

GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;
```

{% alert note %}
L'indicateur de **reprise automatique** doit être activé dans l'entrepôt. Si ce n'est pas le cas, vous devrez accorder à Braze des privilèges supplémentaires `OPERATE` sur l'entrepôt pour que Braze l'active au moment de l'exécution de la requête.
{% endalert %}

#### Étape 2.3 : Configurer l’utilisateur
```json
CREATE USER BRAZE_INGESTION_USER;

GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
```

Vous partagerez les informations de connexion avec Braze et recevrez une clé publique à ajouter à l'utilisateur lors d'une étape ultérieure.

{% alert note %}
Lorsque vous connectez différents espaces de travail au même compte Snowflake, vous devez créer un utilisateur unique pour chaque espace de travail Braze dans lequel vous créez une intégration. Au sein d'un espace de travail, vous pouvez réutiliser le même utilisateur entre les intégrations, mais la création d'une intégration échouera si un utilisateur du même compte Snowflake est dupliqué entre les espaces de travail.
{% endalert %}

#### Étape 2.4 : Autoriser les IP de Braze dans votre politique de réseau Snowflake (optionnel)

Selon la configuration de votre compte Snowflake, vous pourrez avoir à autoriser les adresses IP suivantes au sein de votre politique réseau Snowflake. Pour plus d'informations sur cette opération, consultez la documentation pertinente de Snowflake sur la [modification d'une politique de réseau](https://docs.snowflake.com/en/user-guide/network-policies.html#modifying-network-policies).

{% subtabs %}
{% subtab United States (US) %}
Pour les instances `US-01`, `US-02`, `US-03`, `US-04`, `US-05`, `US-06`, `US-07`, voici les adresses IP correspondantes :
- `23.21.118.191`
- `34.206.23.173`
- `50.16.249.9`
- `52.4.160.214`
- `54.87.8.34`
- `54.156.35.251`
- `52.54.89.238`
- `18.205.178.15`
{% endsubtab %}

{% subtab European Union (EU) %}
Pour les instances `EU-01` et `EU-02`, voici les adresses IP correspondantes :
- `52.58.142.242`
- `52.29.193.121`
- `35.158.29.228`
- `18.157.135.97`
- `3.123.166.46`
- `3.64.27.36`
- `3.65.88.25`
- `3.68.144.188`
- `3.70.107.88`
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Redshift %}
#### Étape 2.1 : Créer un utilisateur et lui accorder des autorisations 

```json
CREATE USER braze_user PASSWORD '{password}';
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT CREATE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT SELECT ON TABLE USERS_ATTRIBUTES_SYNC TO braze_user;
```

Créez un utilisateur pour votre source connectée. Cet utilisateur sera utilisé pour générer la liste des tables disponibles dans vos segments CDI, et pour interroger les tables sources afin de créer de nouveaux segments. Après la création de la source connectée, Braze découvre les noms et la description de toutes les tables disponibles pour l'utilisateur dans le schéma de la source. Si vous créez plusieurs intégrations CDI, vous souhaiterez peut-être accorder des autorisations à un schéma ou gérer les autorisations à l'aide d'un groupe. 

Vous pouvez choisir d'accorder l'accès à toutes les tables d'un schéma ou d'accorder des privilèges uniquement à des tables spécifiques. Les tables auxquelles le rôle Braze a accès pourront être interrogées dans le segment CDI. Veillez à accorder à l'utilisateur l'accès à toutes les nouvelles tables lorsqu'elles sont créées, ou définissez des autorisations par défaut pour l'utilisateur. 

L'autorisation `create table` est nécessaire pour que Braze puisse créer une table avec les résultats de votre requête de segment CDI avant de mettre à jour le segment dans Braze. Braze créera une table temporaire par segment, qui ne persistera que pendant la mise à jour du segment par Braze.


#### Étape 2.2 : Autoriser l'accès aux IP de Braze    

Si vous avez mis en place un pare-feu ou d’autres politiques réseau, vous devez donner à Braze un accès réseau à votre instance Redshift. Autorisez l'accès à partir des IP ci-dessous correspondant à la région de votre tableau de bord de Braze. 

Il se peut également que vous deviez modifier vos groupes de sécurité pour permettre à Braze d'accéder à vos données dans Redshift. Veillez à autoriser explicitement le trafic entrant sur les IP ci-dessous et sur le port utilisé pour interroger votre cluster Redshift (5439 par défaut). Vous devez explicitement autoriser la connectivité TCP de Redshift sur ce port, même si les règles d'entrée sont définies sur "autoriser tout". En outre, il est important que l'endpoint du cluster Redshift soit accessible au public pour que Braze puisse se connecter à votre cluster.

Si vous ne souhaitez pas que votre cluster Redshift soit accessible au public, vous pouvez configurer un VPC et une instance EC2 pour utiliser un tunnel ssh afin d'accéder aux données Redshift. Pour plus d'informations, consultez [AWS : Comment puis-je accéder à un cluster Amazon Redshift privé à partir de mon ordinateur local ?](https://repost.aws/knowledge-center/private-redshift-cluster-local-machine)

{% subtabs %}
{% subtab United States (US) %}
Pour les instances `US-01`, `US-02`, `US-03`, `US-04`, `US-05`, `US-06`, `US-07`, voici les adresses IP correspondantes :
- `23.21.118.191`
- `34.206.23.173`
- `50.16.249.9`
- `52.4.160.214`
- `54.87.8.34`
- `54.156.35.251`
- `52.54.89.238`
- `18.205.178.15`
{% endsubtab %}

{% subtab European Union (EU) %}
Pour les instances `EU-01` et `EU-02`, voici les adresses IP correspondantes :
- `52.58.142.242`
- `52.29.193.121`
- `35.158.29.228`
- `18.157.135.97`
- `3.123.166.46`
- `3.64.27.36`
- `3.65.88.25`
- `3.68.144.188`
- `3.70.107.88`
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab BigQuery %}
#### Étape 2.1 : Créer un compte de service et accorder des autorisations 

Créez un compte de service dans GCP que Braze utilisera pour se connecter et lire les données de votre/vos table(s). Le compte de service doit disposer des autorisations suivantes : 

- **Utilisateur de connexion BigQuery :** Permet à Braze d'établir des connexions.
- **Utilisateur BigQuery :** Permet à Braze d'exécuter des requêtes, de lire les métadonnées des ensembles de données et de répertorier les tables.
- **Visualisateur des données BigQuery :** Permet d'accéder à Braze pour visualiser les ensembles de données et leur contenu.
- **Utilisateur des tâches BigQuery :** Permet à Braze d'accéder à l'exécution des travaux.
- **bigquery.tables.create** Permet à Braze de créer des tables temporaires lors de l'actualisation des segments.

Créez un compte de service pour l'utilisation de votre source connectée. Cet utilisateur sera utilisé pour générer la liste des tables disponibles dans vos segments CDI, et pour interroger les tables sources afin de créer de nouveaux segments. Après la création de la source connectée, Braze découvre les noms et la description de toutes les tables disponibles pour l'utilisateur dans le schéma de la source. 

Vous pouvez choisir d'accorder l'accès à toutes les tables d'un ensemble de données ou d'accorder des privilèges uniquement à des tables spécifiques. Les tables auxquelles le rôle Braze a accès pourront être interrogées dans le segment CDI. 

L'autorisation `create table` est nécessaire pour que Braze puisse créer une table avec les résultats de votre requête de segment CDI avant de mettre à jour le segment dans Braze. Braze créera une table temporaire par segment, et la table ne persistera que pendant que Braze met à jour le segment. 

Après avoir créé le compte de service et accordé les autorisations, générez une clé JSON. Pour plus d'informations, consultez le site [Google Cloud : Créer et supprimer des clés de compte de service](https://cloud.google.com/iam/docs/keys-create-delete). Vous chargerez ceci ultérieurement dans le tableau de bord de Braze.

#### Étape 2.2 : Autoriser l'accès aux IP de Braze    

Si vous avez mis en place des politiques réseau, vous devez donner à Braze un accès réseau à votre instance Big Query. Autorisez l'accès à partir des IP ci-dessous correspondant à la région de votre tableau de bord de Braze.  

{% subtabs %}
{% subtab United States (US) %}
Pour les instances `US-01`, `US-02`, `US-03`, `US-04`, `US-05`, `US-06`, `US-07`, voici les adresses IP correspondantes :
- `23.21.118.191`
- `34.206.23.173`
- `50.16.249.9`
- `52.4.160.214`
- `54.87.8.34`
- `54.156.35.251`
- `52.54.89.238`
- `18.205.178.15`
{% endsubtab %}

{% subtab European Union (EU) %}
Pour les instances `EU-01` et `EU-02`, voici les adresses IP correspondantes :
- `52.58.142.242`
- `52.29.193.121`
- `35.158.29.228`
- `18.157.135.97`
- `3.123.166.46`
- `3.64.27.36`
- `3.65.88.25`
- `3.68.144.188`
- `3.70.107.88`
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Databricks %}
#### Étape 2.1 : Créer un jeton d'accès  

Pour que Braze puisse accéder à Databricks, un jeton d'accès personnel doit être créé.

1. Dans votre espace de travail Databricks, sélectionnez votre nom d'utilisateur Databricks dans la barre supérieure, puis sélectionnez **User Settings** dans le menu déroulant.
2. Assurez-vous que le compte de service dispose des privilèges `CREATE TABLE` sur le schéma utilisé pour la source connectée. 
3. Dans l'onglet **Jetons d'accès**, sélectionnez **Générer un nouveau jeton**.
4. Saisissez un commentaire qui vous aide à identifier ce jeton, par exemple « Braze CDI », et remplacez la durée de vie du jeton par aucune durée de vie en laissant vide la case Durée de vie (jours).
5. Sélectionnez **Générer**.
6. Copiez le jeton affiché, puis sélectionnez **Terminé**.

Ce jeton sera utilisé pour générer la liste des tables disponibles dans vos segments CDI et pour interroger les tables sources afin de créer de nouveaux segments. Après la création de la source connectée, Braze découvre les noms et la description de toutes les tables disponibles pour l'utilisateur dans le schéma de la source. 

Vous pouvez choisir d'accorder l'accès à toutes les tables d'un schéma ou d'accorder des privilèges uniquement à des tables spécifiques. Les tables auxquelles le rôle Braze a accès pourront être interrogées dans le segment CDI.

L'autorisation `create table` est nécessaire pour que Braze puisse créer une table avec les résultats de votre requête de segment CDI avant de mettre à jour le segment dans Braze. Braze créera une table temporaire par segment, qui ne persistera que pendant la mise à jour du segment par Braze. 

Conservez le jeton en lieu sûr jusqu'à ce que vous ayez besoin de le saisir dans le tableau de bord de Braze lors de l'étape de création d’identifiants.

#### Étape 2.2 : Autoriser l'accès aux IP de Braze    

Si vous avez mis en place des politiques réseau, vous devez donner à Braze un accès réseau à votre instance Databricks. Autorisez l'accès à partir des IP ci-dessous correspondant à la région de votre tableau de bord de Braze.  

{% subtabs %}
{% subtab United States (US) %}
Pour les instances `US-01`, `US-02`, `US-03`, `US-04`, `US-05`, `US-06`, `US-07`, voici les adresses IP correspondantes :
- `23.21.118.191`
- `34.206.23.173`
- `50.16.249.9`
- `52.4.160.214`
- `54.87.8.34`
- `54.156.35.251`
- `52.54.89.238`
- `18.205.178.15`
{% endsubtab %}

{% subtab European Union (EU) %}
Pour les instances `EU-01` et `EU-02`, voici les adresses IP correspondantes :
- `52.58.142.242`
- `52.29.193.121`
- `35.158.29.228`
- `18.157.135.97`
- `3.123.166.46`
- `3.64.27.36`
- `3.65.88.25`
- `3.68.144.188`
- `3.70.107.88`
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Étape 3 : Créez une source connectée dans le tableau de bord de Braze.

{% tabs %}
{% tab Snowflake %}
#### Étape 3.1 : Ajouter les informations de connexion et la table source de Snowflake

Créez une source connectée dans le tableau de bord de Braze. Accédez à **Paramètres des données** > **Ingestion de données dans le cloud** > **Sources connectées**, puis sélectionnez **Créer une nouvelle synchronisation de données** > **Importation Snowflake**.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_tab.png %}){: style="max-width:80%;"}

Saisissez les informations relatives à votre entrepôt de données Snowflake et à votre schéma source, puis passez à l'étape suivante.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_sf_1.png %})

#### Étape 3.2 : Configurer les détails de la synchronisation

Choisissez un nom pour la source connectée. Ce nom sera utilisé dans la liste des sources disponibles lorsque vous créerez un nouveau segment CDI. 

Configurez une durée d'exécution maximale pour cette source. Lors de la création ou de l'actualisation d'un segment, Braze interrompt automatiquement les requêtes qui dépassent la durée d'exécution maximale. La durée d'exécution maximale autorisée est de 60 minutes. Une durée d'exécution inférieure réduira les coûts encourus sur votre compte Snowflake. 

{% alert note %}
Si les requêtes expirent systématiquement alors que vous avez défini une durée d'exécution maximale de 60 minutes, essayez d'optimiser le temps d'exécution de vos requêtes ou de dédier un entrepôt plus important à l'utilisateur Braze.
{% endalert %}

![]({% image_buster /assets/img/cloud_ingestion/connected_source_sf_2.png %})

#### Étape 3.3 : Notez la clé publique  

Dans l'étape **Test connection**, notez la clé publique RSA. Vous en aurez besoin pour réaliser l'intégration dans Snowflake.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_sf_3.png %})

{% endtab %}
{% tab Redshift %}
#### Étape 3.1 : Ajouter les informations de connexion Redshift et la table source

Créez une source connectée dans le tableau de bord de Braze. Accédez à **Paramètres des données** > **Ingestion de données dans le cloud** > **Sources connectées**, puis sélectionnez **Créer une connexion de données** > **Importation Amazon Redshift.**

![]({% image_buster /assets/img/cloud_ingestion/connected_source_tab.png %}){: style="max-width:80%;"}

Saisissez les informations relatives à votre entrepôt de données Redshift et à votre schéma source, puis passez à l'étape suivante.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_rd_1.png %})

#### Étape 3.2 : Configurer les détails de la synchronisation

Choisissez un nom pour la source connectée. Ce nom sera utilisé dans la liste des sources disponibles lorsque vous créerez un nouveau segment CDI. 

Configurez une durée d'exécution maximale pour cette source. Lors de la création ou de l'actualisation d'un segment, Braze interrompt automatiquement les requêtes qui dépassent la durée d'exécution maximale. La durée d'exécution maximale autorisée est de 60 minutes ; une durée d'exécution inférieure réduira les coûts encourus sur votre compte Redshift. 

{% alert note %}
Si les requêtes expirent systématiquement alors que vous avez défini une durée d'exécution maximale de 60 minutes, essayez d'optimiser le temps d'exécution de vos requêtes ou de dédier un entrepôt plus important à l'utilisateur Braze.
{% endalert %}

![]({% image_buster /assets/img/cloud_ingestion/connected_source_rd_2.png %})

#### Étape 3.3 : Notez la clé publique (facultatif)

Si vous avez sélectionné l'option **Connect with SSH Tunnel**, prenez note de la clé publique RSA dans l'étape **Test connection.**  Vous en aurez besoin pour terminer l'intégration dans Redshift.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_rd_3.png %})

{% endtab %}
{% tab BigQuery %}
#### Étape 3.1 : Ajouter les informations de connexion BigQuery et la table source

Créez une source connectée dans le tableau de bord de Braze. Accédez à **Paramètres des données** > **Ingestion de données dans le cloud** > **Sources connectées**, puis sélectionnez **Créer une nouvelle synchronisation de données** > **Importation Google BigQuery**.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_tab.png %}){: style="max-width:80%;"}

Saisissez les informations relatives à votre projet BigQuery et à votre jeu de données, puis passez à l'étape suivante.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_bg_1.png %})

#### Étape 3.2 : Configurer les détails de la synchronisation

Choisissez un nom pour la source connectée. Ce nom sera utilisé dans la liste des sources disponibles lorsque vous créerez un nouveau segment CDI. 

Configurez une durée d'exécution maximale pour cette source. Lors de la création ou de l'actualisation d'un segment, Braze interrompt automatiquement les requêtes qui dépassent la durée d'exécution maximale. La durée d'exécution maximale autorisée est de 60 minutes ; une durée d'exécution inférieure réduira les coûts encourus sur votre compte BigQuery. 

{% alert note %}
Si les requêtes expirent systématiquement alors que vous avez défini une durée d'exécution maximale de 60 minutes, essayez d'optimiser le temps d'exécution de vos requêtes ou de dédier un entrepôt plus important à l'utilisateur Braze.
{% endalert %}

![]({% image_buster /assets/img/cloud_ingestion/connected_source_bg_2.png %})

#### Étape 3.3 : Testez la connexion

Sélectionnez **Tester la connexion** pour vérifier que la liste des tables visibles par l'utilisateur correspond à ce que vous attendez, puis sélectionnez **Terminé**. Votre source connectée est maintenant créée et prête à être utilisée dans les segmentations CDI.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_test_connection.png %})

{% endtab %}
{% tab Databricks %}
#### Étape 3.1 : Ajouter les informations de connexion Databricks et la table source

Créez une source connectée dans le tableau de bord de Braze. Accédez à **Paramètres des données** > **Ingestion de données dans le cloud** > **Sources connectées**, puis sélectionnez **Créer une nouvelle synchronisation de données** > **Importation de Databricks**.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_tab.png %}){: style="max-width:80%;"}

Saisissez les informations relatives à vos identifiants Databricks et, en option, au catalogue et au schéma source, puis passez à l'étape suivante.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_databricks_1.png %})

#### Étape 3.2 : Configurer les détails de la synchronisation

Choisissez un nom pour la source connectée. Ce nom sera utilisé dans la liste des sources disponibles lorsque vous créerez un nouveau segment CDI. 

Configurez une durée d'exécution maximale pour cette source. Lors de la création ou de l'actualisation d'un segment, Braze interrompt automatiquement les requêtes qui dépassent la durée d'exécution maximale. La durée d'exécution maximale autorisée est de 60 minutes ; une durée d'exécution inférieure réduira les coûts encourus sur votre compte Databricks. 

{% alert note %}
Si les requêtes expirent systématiquement alors que vous avez défini une durée d'exécution maximale de 60 minutes, essayez d'optimiser le temps d'exécution de vos requêtes ou de dédier un entrepôt plus important à l'utilisateur Braze.
{% endalert %}

![]({% image_buster /assets/img/cloud_ingestion/connected_source_db_2.png %})

#### Étape 3.3 : Testez la connexion

Sélectionnez **Tester la connexion** pour vérifier que la liste des tables visibles par l'utilisateur correspond à ce que vous attendez, puis sélectionnez **Terminé**. Votre source connectée est maintenant créée et prête à être utilisée dans les segmentations CDI.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_test_connection.png %})

{% endtab %}
{% endtabs %}

### Étape 4 : Finaliser la configuration de l'entrepôt de données

{% tabs %}
{% tab Snowflake %}
Ajoutez la clé publique que vous avez notée lors de la dernière étape à votre utilisateur dans Snowflake. Cela permettra à Braze de se connecter à Snowflake. Pour plus de détails sur la façon de procéder, consultez la [documentation Snowflake](https://docs.snowflake.com/en/user-guide/key-pair-auth.html). 

Si vous souhaitez effectuer une rotation des clés à un moment donné, vous pouvez créer une nouvelle clé publique en allant dans **Gestion de l'accès aux données** dans **Cloud Data Ingestion** et en sélectionnant **Générer une nouvelle clé** pour le compte concerné.

![Gestion de l'accès aux données pour les justificatifs d'accès aux données de Snowflake, avec un bouton pour générer une nouvelle clé.]({% image_buster /assets/img/cloud_ingestion/connected_source_sf_4.png %})

```json
ALTER USER BRAZE_INGESTION_USER SET rsa_public_key='{INSERT_YOUR_KEY}';
```

Après avoir ajouté la clé à l'utilisateur dans Snowflake, sélectionnez **Tester la connexion** dans Braze, puis **Terminé**. Votre source connectée est maintenant créée et prête à être utilisée dans les segmentations CDI.
{% endtab %}

{% tab Redshift %}
Si vous vous connectez avec un tunnel SSH, ajoutez la clé publique que vous avez notée lors de la dernière étape à l'utilisateur du tunnel SSH. 

Après avoir ajouté la clé à l'utilisateur, sélectionnez **Tester la connexion** dans Braze, puis **Terminé**. Votre source connectée est maintenant créée et prête à être utilisée dans les segmentations CDI.

{% endtab %}
{% tab BigQuery %}
Cela ne s'applique pas à BigQuery.

{% endtab %}
{% tab Databricks %}
Cela ne s'applique pas aux Databricks.

{% endtab %}
{% endtabs %}

{% alert note %}
Vous devez tester avec succès une source avant qu'elle ne passe de l'état "brouillon" à l'état "actif". Si vous avez besoin de fermer la page de création, votre intégration sera sauvegardée et vous pourrez revenir à la page Détails pour effectuer des changements et les tester.  
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
{% endtabs %}

## Utilisation de la source connectée

Une fois la source créée, elle peut être utilisée pour créer un ou plusieurs segments CDI. Pour plus d'informations sur la création d'un segment avec cette source, consultez la [documentation sur les segments CDI]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/cdi_segments/).

{% alert note %}
Si les requêtes sont systématiquement interrompues alors que vous avez défini une durée d'exécution maximale de 60 minutes, envisagez d'optimiser le temps d'exécution de vos requêtes ou de dédier davantage de ressources de calcul (un entrepôt plus grand, par exemple) à l'utilisateur de Braze.
{% endalert %}
