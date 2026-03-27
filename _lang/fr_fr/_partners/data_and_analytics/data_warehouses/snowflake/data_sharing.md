---
nav_title: "Partage de données"
article_title: Partage de données Snowflake
page_order: 0
description: "Cet article de référence présente l'intégration Snowflake Secure Data Sharing, qui vous permet d'accéder aux données d'engagement et de campagne de Braze directement dans votre instance Snowflake."
page_type: partner
search_tag: Partner

---

# [![Cours d'apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/snowflake-secure-data-sharing-via-braze/){: style="float:right;width:120px;border:0;" class="noimgborder"}Partage de données Snowflake

> Le [Secure Data Sharing](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html) de Snowflake permet à Braze de vous donner un accès sécurisé aux données de notre portail Snowflake, sans vous soucier des frictions de workflow, des ralentissements, des points de défaillance et des coûts inutiles liés aux relations classiques avec les fournisseurs de données. Le partage de données peut être configuré via l'intégration suivante ou via les [comptes Snowflake Reader]({{site.baseurl}}/user_guide/data/braze_currents/how_braze_uses_currents/#snowflake-reader-accounts).

{% alert tip %}
**Vous souhaitez accéder à des données de niveau Snowflake sans avoir besoin d'un compte Snowflake ?**<br>Consultez les [comptes Snowflake Reader]({{site.baseurl}}/user_guide/data/braze_currents/how_braze_uses_currents/#snowflake-reader-accounts). Avec les comptes Reader, Braze crée un compte dans lequel vos données sont partagées et vous fournit des identifiants pour vous connecter et accéder à vos données. Ainsi, l'ensemble du partage de données et de la facturation d'utilisation est entièrement géré par Braze.
{% endalert %}

## À propos du Secure Data Sharing

Avec le partage de données, aucune donnée n'est réellement copiée ou transférée entre les comptes. Tout le partage s'effectue via la couche de services et le magasin de métadonnées propres à Snowflake. C'est un concept important, car les données partagées n'occupent aucun espace de stockage dans votre compte et ne contribuent donc pas à vos frais mensuels de stockage de données. Les **seuls** frais concernent les ressources de calcul (comme les entrepôts virtuels) utilisées pour interroger les données partagées.

De plus, grâce aux fonctionnalités intégrées de rôles et d'autorisations de Snowflake, l'accès aux données partagées depuis Braze peut être contrôlé et régi à l'aide des contrôles d'accès déjà en place pour votre compte Snowflake et les données qu'il contient. L'accès peut être restreint et surveillé de la même manière que pour vos propres données.

- **Réduisez le délai d'obtention des informations**<br>Dites adieu aux processus ETL qui prennent des semaines à mettre en place. Les architectures uniques de Braze et Snowflake rendent toutes les données d'engagement client et de campagne immédiatement accessibles et interrogeables dès leur arrivée dans le data lake. Aucune donnée n'est copiée ni déplacée, ce qui vous permet de proposer des expériences client basées uniquement sur les informations les plus pertinentes et les plus récentes.
- **Éliminez les silos de données**<br>Créez une vue globale de vos clients à travers les canaux et les plateformes. Le partage de données facilite plus que jamais la jonction de vos données d'engagement client Braze avec toutes vos autres données Snowflake, offrant des informations plus riches à partir d'une source de vérité unique et fiable.
- **Évaluez vos performances d'engagement**<br>Optimisez vos stratégies d'engagement client avec Braze Benchmarks. Cet outil interactif, propulsé par Braze et Snowflake, vous permet de comparer les données d'engagement de votre marque à des références par canal, secteur d'activité et plateforme d'appareil.

Pour en savoir plus sur le partage de données Snowflake, consultez l'[Introduction au Secure Data Sharing](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#how-does-secure-data-sharing-work).

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Accès à Braze | Contactez votre responsable de compte Braze ou votre Customer Success Manager pour configurer le partage de données. |
| Compte Snowflake | Un compte Snowflake avec des autorisations `admin`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Configuration du Secure Data Sharing

Chez Snowflake, le partage de données s'effectue entre un [fournisseur de données](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#providers) et un [consommateur de données](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#consumers). Dans ce contexte, votre compte Braze est le fournisseur de données, car il crée et envoie le datashare, tandis que votre compte Snowflake est le consommateur de données, car il utilise le datashare pour créer une base de données. Pour plus de détails, consultez [Snowflake : Consommer des données partagées](https://docs.snowflake.com/en/user-guide/data-share-consumers).

### Étape 1 : Envoyer le datashare depuis Braze

1. Dans Braze, accédez à **Partner Integrations** > **Data Sharing**.
2. Saisissez les détails et le localisateur de votre compte Snowflake. Pour obtenir votre localisateur de compte, exécutez `SELECT CURRENT_ACCOUNT()` dans le compte de destination.
3. Si vous utilisez un partage CRR, spécifiez le fournisseur cloud et la région.
4. Lorsque vous avez terminé, sélectionnez **Create Datashare**. Le datashare sera alors envoyé à votre compte Snowflake.

### Étape 2 : Créer la base de données dans Snowflake

1. Après quelques minutes, vous devriez recevoir le datashare entrant dans votre compte Snowflake.
2. À l'aide du datashare entrant, créez une base de données pour visualiser et interroger les tables. Par exemple :
    {% raw %}
    ```sql
    CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>
    ```
    {% endraw %}
3. Accordez les privilèges nécessaires pour interroger la nouvelle base de données.

{% alert warning %}
Si vous supprimez et recréez un partage dans le tableau de bord de Braze, vous devez supprimer la base de données précédemment créée et la recréer en utilisant `CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>` pour interroger le partage entrant.
Si vous avez plusieurs espaces de travail partageant des données vers le même compte Snowflake, consultez la [FAQ sur le partage de données Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/faqs/) pour obtenir des conseils sur la gestion des configurations multi-espaces de travail.
{% endalert %}

## Utilisation et visualisation

Une fois le partage de données provisionné, créez une base de données à partir du partage de données entrant. Toutes les tables partagées apparaîtront alors dans votre instance Snowflake et seront interrogeables comme n'importe quelle autre donnée stockée dans votre instance. Gardez toutefois à l'esprit que les données partagées sont en lecture seule : elles peuvent uniquement être interrogées, mais ne peuvent être ni modifiées ni supprimées.

Comme pour Currents, vous pouvez utiliser votre Snowflake Secure Data Sharing pour :

- Créer des rapports complexes
- Réaliser des modélisations d'attribution
- Partager des données de manière sécurisée au sein de votre entreprise
- Associer des données brutes d'événements ou d'utilisateurs à un CRM (comme Salesforce)
- Et bien plus encore

[Téléchargez les schémas de tables brutes ici.]({% image_buster /assets/download_file/data-sharing-raw-table-schemas.txt %})

### Schéma des ID utilisateur

Notez les différences suivantes entre les conventions de nommage de Braze et de Snowflake pour les ID utilisateur.

| Schéma Braze | Schéma Snowflake | Description |
| ----------- | ----------- | ----------- |
| `braze_id` | `"USER_ID"` | L'identifiant unique attribué automatiquement par Braze. |
| `external_id` | `"EXTERNAL_USER_ID"` | L'identifiant unique du profil d'un utilisateur, défini par le client. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Informations importantes et limitations

### Modifications avec et sans rupture

#### Modifications sans rupture

Les modifications sans rupture peuvent survenir à tout moment et apportent généralement des fonctionnalités supplémentaires. Exemples de modifications sans rupture :
- Ajout d'une nouvelle table ou vue
- Ajout d'une colonne à une table ou vue existante

{% alert important %}
Étant donné que les nouvelles colonnes sont considérées comme des modifications sans rupture, Braze recommande fortement de lister explicitement les colonnes souhaitées dans chaque requête plutôt que d'utiliser des requêtes `SELECT *`. Vous pouvez également créer des vues qui nomment explicitement les colonnes, puis interroger ces vues plutôt que les tables directement.
{% endalert %}

#### Modifications avec rupture

Dans la mesure du possible, les modifications avec rupture seront précédées d'une annonce et d'une période de migration. Exemples de modifications avec rupture :
- Suppression d'une table ou vue
- Suppression d'une colonne d'une table ou vue existante
- Modification du type ou de la possibilité de valeur nulle d'une colonne existante

### Régions Snowflake

Braze héberge actuellement toutes les données au niveau utilisateur dans les régions AWS Snowflake suivantes :

 - US East-1
 - EU-Central (Francfort)
 - AP-Southeast-2 (Sydney)
 - AP-Southeast-3 (Jakarta)
 
Pour les utilisateurs situés en dehors de ces régions, Braze peut fournir un partage de données aux clients communs qui hébergent leur infrastructure Snowflake dans n'importe quelle région AWS, Azure ou GCP.

### Conservation des données

#### Politique de conservation

Toute donnée datant de plus de deux ans sera archivée et déplacée vers un stockage à long terme. Dans le cadre du processus d'archivage, tous les événements sont anonymisés et les champs contenant des informations personnelles identifiables (PII) sensibles sont supprimés (cela inclut les champs PII facultatifs comme `properties`). Les données archivées contiennent toujours le champ `user_id`, ce qui permet des analyses par utilisateur sur l'ensemble des données d'événements.

Vous pourrez interroger les deux années les plus récentes de données pour chaque événement dans la vue `USERS_*_SHARED` correspondante. De plus, chaque événement disposera d'une vue `USERS_*_SHARED_ALL` qui peut être interrogée pour obtenir à la fois les données anonymisées et non anonymisées.

#### Données historiques

L'archive des données d'événements historiques dans Snowflake remonte à avril 2019. Au cours des premiers mois de stockage des données par Braze dans Snowflake, des modifications produit ont été apportées, ce qui peut avoir entraîné des différences mineures dans certaines données ou la présence de valeurs nulles (car nous ne transmettions pas les données dans tous les champs disponibles à cette époque). Il est préférable de considérer que tout résultat incluant des données antérieures à août 2019 peut différer légèrement des attentes.

### Conformité au Règlement Général sur la Protection des Données (RGPD)

{% include partners/snowflake_pii_gdpr.md %}

### Vitesse, performance et coût des requêtes

La vitesse, la performance et le coût de toute requête exécutée sur les données dépendent de la taille de l'entrepôt que vous utilisez pour interroger les données. Dans certains cas, selon le volume de données auquel vous accédez pour vos analyses, vous pourriez avoir besoin d'une taille d'entrepôt plus importante pour que la requête aboutisse. Snowflake propose d'excellentes ressources pour vous aider à déterminer la taille optimale, notamment la [Présentation des entrepôts](https://docs.snowflake.net/manuals/user-guide/warehouses-overview.html) et les [Considérations relatives aux entrepôts](https://docs.snowflake.net/manuals/user-guide/warehouses-considerations.html).

{% alert tip %}
Pour consulter un ensemble d'exemples de requêtes utiles lors de la configuration de Snowflake, découvrez nos [exemples de requêtes]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/sample_queries/) et nos exemples de [configuration de pipeline ETL d'événements]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/etl_pipline_setup/).
{% endalert %}