---
nav_title: Snowflake
article_title: Snowflake
alias: /partners/snowflake/
description: "Cet article décrit le partenariat entre Braze et Snowflake, couvrant à la fois le partage de données (de Braze vers Snowflake) et l'ingestion de données cloud (de Snowflake vers Braze)."
page_type: partner
search_tag: Partner

---

# Snowflake

> [Snowflake](https://docs.snowflake.net/manuals/user-guide/intro-key-concepts.html) est un entrepôt de données SQL cloud spécialement conçu, fourni en tant que SaaS (Software-as-a-Service). Snowflake offre un entrepôt de données plus rapide, plus simple d'utilisation et bien plus flexible que les solutions traditionnelles. Grâce à son architecture unique et brevetée, Snowflake vous permet de centraliser facilement toutes vos données, d'effectuer des analyses rapides et d'en tirer des informations exploitables pour l'ensemble de vos utilisateurs.

Braze propose deux intégrations avec Snowflake. Ensemble, elles constituent un pipeline de données bidirectionnel complet entre vos environnements Braze et Snowflake.

## Choisir une intégration

### Partage de données (de Braze vers Snowflake)

Le [partage sécurisé des données]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/data_sharing/) de Snowflake vous donne un accès sécurisé et en temps réel aux données d'engagement et de campagne de Braze, directement dans votre instance Snowflake. Aucune donnée n'est copiée ni transférée entre les comptes : tout le partage s'effectue via la couche de services et le magasin de métadonnées propres à Snowflake.

**Utilisez le partage de données lorsque vous souhaitez :**
- Interroger les données d'événements et de campagnes de Braze en SQL dans Snowflake
- Créer des rapports complexes et réaliser une modélisation d'attribution
- Croiser les données de Braze avec d'autres données de votre entrepôt Snowflake
- Comparer vos données d'engagement entre les canaux, les secteurs d'activité et les plateformes d'appareils

Pour les instructions de configuration, consultez [Partage de données Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/data_sharing/).

### Ingestion de données cloud (de Snowflake vers Braze)

L'[ingestion de données cloud (CDI)]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/) vous permet de synchroniser les données de votre instance Snowflake directement dans Braze. Vous pouvez ainsi maintenir à jour les attributs utilisateur, les événements et les achats dans Braze à partir de votre entrepôt de données de référence.

**Utilisez l'ingestion de données cloud lorsque vous souhaitez :**
- Synchroniser les attributs utilisateur de Snowflake vers les profils utilisateur de Braze
- Envoyer des données d'événements ou d'achats de Snowflake vers Braze
- Maintenir Braze synchronisé avec les transformations de données effectuées dans votre entrepôt
- Éviter de créer et de maintenir des pipelines ETL personnalisés de Snowflake vers Braze

Pour en savoir plus sur le partage de données Snowflake, consultez [Introduction au partage sécurisé des données](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#how-does-secure-data-sharing-work).

## Conditions préalables

Avant de pouvoir utiliser cette fonctionnalité, vous devez remplir les conditions suivantes :

| Condition | Description |
| ----------- | ----------- |
| Accès à Braze | Pour accéder à cette fonctionnalité dans Braze, contactez votre gestionnaire de compte ou votre Customer Success Manager Braze. |
| Compte Snowflake | Un compte Snowflake avec les autorisations `admin`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Mise en place du partage sécurisé des données

Avec Snowflake, le partage des données s'effectue entre un [fournisseur de données](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#providers) et un [consommateur de données](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#consumers). Dans ce contexte, votre compte Braze est le fournisseur de données, car il crée et envoie le partage de données, tandis que votre compte Snowflake est le consommateur de données, car il utilise ce partage pour créer une base de données. Pour plus de détails, consultez [Snowflake : Consommation de données partagées](https://docs.snowflake.com/en/user-guide/data-share-consumers).

### Étape 1 : Envoyer le partage de données depuis Braze

1. Dans Braze, accédez à **Intégrations partenaires** > **Partage des données**.
2. Saisissez les détails de votre compte Snowflake et votre localisateur. Pour obtenir votre localisateur de compte, exécutez `SELECT CURRENT_ACCOUNT()` dans le compte de destination.
3. Si vous utilisez un partage CRR, spécifiez le fournisseur de cloud et la région.
4. Lorsque vous avez terminé, sélectionnez **Créer un partage de données**. Le partage de données sera alors envoyé à votre compte Snowflake.

### Étape 2 : Créer la base de données dans Snowflake

1. Après quelques minutes, vous devriez recevoir le partage de données entrant dans votre compte Snowflake.
2. À partir de ce partage de données entrant, créez une base de données pour visualiser et interroger les tables. Par exemple :
    ```sql
    CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>
    ```
3. Accordez les privilèges nécessaires pour interroger la nouvelle base de données.

{% alert warning %}
Si vous supprimez et recréez un partage dans le tableau de bord de Braze, vous devez supprimer la base de données créée précédemment et la recréer à l'aide de `CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>` pour interroger le partage entrant.
Si vous avez plusieurs espaces de travail partageant des données avec le même compte Snowflake, consultez les [FAQ sur le partage des données Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/faqs/) pour obtenir des conseils sur la gestion des configurations multi-espaces de travail.
{% endalert %}

## Utilisation et visualisation

Une fois le partage de données provisionné, vous devrez créer une base de données à partir du partage entrant. Toutes les tables partagées apparaîtront alors dans votre instance Snowflake et pourront être interrogées comme n'importe quelles autres données stockées dans votre instance. Gardez toutefois à l'esprit que les données partagées sont en lecture seule : elles peuvent être interrogées, mais ne peuvent en aucun cas être modifiées ou supprimées.

Comme avec Currents, vous pouvez utiliser le partage sécurisé de données Snowflake pour :

- Créer des rapports complexes
- Réaliser une modélisation d'attribution
- Partager des données de manière sécurisée au sein de votre entreprise
- Associer les données brutes d'événements ou d'utilisateurs à un CRM (tel que Salesforce)
- Et bien plus encore

Pour obtenir la liste complète des tables et colonnes disponibles, consultez la [référence des tables SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/). Le partage de données Snowflake inclut toutes les tables de cette référence, ainsi que des tables supplémentaires exclusives à Snowflake pour les snapshots, les journaux des modifications de campagnes et de Canvas, les événements de la console d'agent et les événements de renvoi de messages.

Vous pouvez également [télécharger les schémas de tables bruts]({% image_buster /assets/download_file/data-sharing-raw-table-schemas.txt %}) sous forme de fichier texte.

### Schéma d'ID utilisateur

Notez les différences suivantes entre les conventions de nommage de Braze et de Snowflake pour les identifiants utilisateur.

| Schéma Braze | Schéma Snowflake | Description |
| ----------- | ----------- | ----------- |
| `braze_id` | `"USER_ID"` | L'identifiant unique attribué automatiquement par Braze. |
| `external_id` | `"EXTERNAL_USER_ID"` | L'identifiant unique du profil utilisateur, défini par le client. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Informations importantes et limites

### Modifications avec et sans rupture

#### Modifications sans rupture

Les modifications sans rupture peuvent intervenir à tout moment et apportent généralement des fonctionnalités supplémentaires. Exemples :
- Ajout d'une nouvelle table ou vue
- Ajout d'une colonne à une table ou une vue existante

{% alert important %}
Les nouvelles colonnes étant considérées comme des modifications sans rupture, Braze recommande vivement de lister explicitement les colonnes souhaitées dans chaque requête plutôt que d'utiliser `SELECT *`. Vous pouvez également créer des vues qui nomment explicitement les colonnes, puis interroger ces vues plutôt que les tables directement.
{% endalert %}

#### Modifications avec rupture

Dans la mesure du possible, les modifications avec rupture seront précédées d'une annonce et d'une période de migration. Exemples :
- Suppression d'une table ou d'une vue
- Suppression d'une colonne d'une table ou d'une vue existante
- Modification du type ou de la nullabilité d'une colonne existante

### Régions Snowflake

Braze héberge actuellement toutes les données utilisateur dans les régions Snowflake AWS US East-1, EU-Central (Francfort), AP-Southeast-2 (Sydney) et AP-Southeast-3 (Jakarta). Pour les utilisateurs situés en dehors de ces régions, Braze peut fournir un partage de données aux clients communs qui hébergent leur infrastructure Snowflake dans n'importe quelle région AWS, Azure ou GCP.

### Conservation des données

#### Politique de conservation

Toutes les données datant de plus de deux ans sont archivées et transférées vers un stockage à long terme. Dans le cadre de ce processus d'archivage, tous les événements sont anonymisés et les champs contenant des informations personnelles identifiables (PII) sont supprimés (y compris les champs PII facultatifs tels que `properties`). Les données archivées contiennent toujours le champ `user_id`, ce qui permet des analyses par utilisateur sur l'ensemble des données d'événements.

Vous pouvez interroger les données des deux dernières années pour chaque événement dans la vue `USERS_*_SHARED` correspondante. De plus, chaque événement dispose d'une vue `USERS_*_SHARED_ALL` qui permet de récupérer à la fois les données anonymisées et non anonymisées.

#### Données historiques

Les archives des données d'événements historiques dans Snowflake remontent à avril 2019. Au cours des premiers mois de stockage des données par Braze dans Snowflake, des modifications produit ont été apportées, ce qui a pu entraîner de légères différences dans certaines données ou des valeurs nulles (car tous les champs disponibles n'étaient pas encore alimentés à cette époque). Il est préférable de considérer que les résultats incluant des données antérieures à août 2019 peuvent légèrement différer des attentes.

### Conformité au règlement général sur la protection des données (RGPD)

{% multi_lang_include partners/snowflake_pii_gdpr.md %}

### Rapidité, performance et coût des requêtes

La vitesse, les performances et le coût de toute requête exécutée sur les données dépendent de la taille de l'entrepôt utilisé. Dans certains cas, selon le volume de données auquel vous accédez pour vos analyses, il peut être nécessaire d'utiliser un entrepôt plus grand pour que la requête aboutisse. Snowflake propose d'excellentes ressources pour vous aider à déterminer la taille optimale, notamment la [vue d'ensemble des entrepôts](https://docs.snowflake.net/manuals/user-guide/warehouses-overview.html) et les [considérations relatives aux entrepôts](https://docs.snowflake.net/manuals/user-guide/warehouses-considerations.html).

> Pour consulter des exemples de requêtes utiles lors de la configuration de Snowflake, consultez nos [exemples de requêtes]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/sample_queries/) et nos exemples de [configuration de pipeline d'événements ETL]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/etl_pipline_setup/).

Pour les instructions de configuration, consultez [Ingestion de données cloud : intégrations d'entrepôts de données]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/).