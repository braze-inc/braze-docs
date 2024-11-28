---
nav_title: Snowflake
article_title: Snowflake
alias: /partners/snowflake/
description: "Cet article de référence décrit le partenariat entre Braze et Snowflake, un entrepôt de données SQL cloud spécialement conçu pour l'ensemble de vos données et de vos utilisateurs."
page_type: partner
search_tag: Partner

---

# [![Cours d'apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/snowflake-secure-data-sharing-via-braze/) {: style="float:right;width:120px;border:0;" class="noimgborder"}Snowflake

> [Snowflake](https://docs.snowflake.net/manuals/user-guide/intro-key-concepts.html) est un entrepôt de données SQL cloud fourni sous forme de logiciel en tant que service (SaaS). Snowflake fournit un entrepôt de données plus rapide, plus facile à utiliser et bien plus flexible que les offres d'entrepôt de données traditionnelles. Grâce à l'architecture unique et brevetée de Snowflake, il est facile de rassembler toutes vos données, d’effectuer des analyses rapides et d'obtenir des informations basées sur les données pour tous vos utilisateurs.

Les campagnes marketing personnalisées et pertinentes nécessitent un accès immédiat aux données. C'est pourquoi Braze s'est associée à Snowflake pour lancer une fonction de partage de données. Cette offre conjointe permet aux marketeurs de tirer pleinement parti de leur engagement client et des données de campagne plus rapidement que jamais.

L'[intégration de Braze et Snowflake](https://www.braze.com/perspectives/article/snowflake-partner-announcement) tire parti de l'échange de données de Snowflake pour créer une présence, trouver de nouveaux clients et étendre sa portée grâce à la clientèle toujours croissante de Snowflake.

{% alert tip %}
**Vous souhaitez accéder aux données de niveau Snowflake sans pour autant avoir de compte Snowflake ?**<br>Consultez les comptes [Snowflake Reader]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/how_braze_uses_currents/#snowflake-reader-accounts). Avec Reader Accounts, Braze créera et partagera vos données sur un compte et vous fournira des informations d'identification pour vous connecter et accéder à vos données. Cela se traduira par le fait que tout le partage des données et la facturation de l'utilisation seront entièrement gérés par Braze.
{% endalert %}

## Qu'est-ce que le partage de données ?

La fonctionnalité de partage [sécurisé des données de](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html) Snowflake permet à Braze de vous donner un accès sécurisé aux données de notre portail Snowflake sans vous soucier de la friction ou du ralentissement du flux de travail, des points de défaillance et des coûts inutiles liés aux relations classiques avec les fournisseurs de données. Le partage des données peut être configuré via l'intégration suivante ou via les comptes [Snowflake Reader]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/how_braze_uses_currents/#snowflake-reader-accounts).

- **Réduisez le temps nécessaire pour obtenir des informations**<br>Dites adieu aux processus ETL dont la mise en place prend des semaines. Les architectures uniques de Braze et Snowflake rendent toutes les données d'engagement client et de campagne immédiatement accessibles et consultables dès leur arrivée dans le lac de données. Aucune donnée n'est copiée ou déplacée, ce qui vous permet de proposer des expériences client basées uniquement sur les informations les plus pertinentes et les plus récentes.
- **Éliminez les silos de données**<br>Créez une vision globale de vos clients sur l'ensemble des canaux et des plateformes. Grâce au partage de données, il est plus facile que jamais d'associer vos données d'engagement client Braze à toutes vos autres données Snowflake, créant ainsi des informations plus riches à partir d'une source fiable et unique de vérité.
- **Découvrez comment se situe votre engagement**<br>Optimisez vos stratégies d'engagement client avec Braze Benchmarks. Cet outil interactif, développé par Braze et Snowflake, vous permet de comparer les données d'engagement de votre marque à des benchmarks sur différents canaux, secteurs d'activité et plateformes d'appareils.

Avec le partage des données, aucune donnée réelle n'est copiée ou transférée entre les comptes. Le partage est effectué via la couche de services et le magasin de métadonnées uniques de Snowflake. Il s'agit d'un concept important car les données partagées n'occupent aucun espace de stockage sur le compte du consommateur et ne contribuent donc pas aux frais mensuels de stockage des données du consommateur. Les **seuls** frais facturés aux consommateurs concernent les ressources informatiques (telles que les entrepôts virtuels) utilisées pour interroger les données partagées.

De plus, grâce aux fonctionnalités intégrées de rôles et d'autorisations de Snowflake, l'accès aux données partagées depuis Braze peut être contrôlé et régi à l'aide des contrôles d'accès déjà en place pour votre compte Snowflake et les données qu'il contient. L'accès peut être restreint et surveillé de la même manière que vos propres données.

Consultez la section [Introduction au partage sécurisé des données](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#how-does-secure-data-sharing-work) pour en savoir plus sur le fonctionnement du partage de données de Snowflake.

## Prérequis

Si cette intégration vous intéresse, contactez votre compte Braze ou votre gestionnaire de la satisfaction client et demandez-leur de consulter les services de stratégie de données de Braze sur le partage sécurisé des données avec Snowflake. Cela nous permettra de configurer vos vues en un rien de temps !

| Exigence | Descriptif |
| ----------- | ----------- |
| Compte Snowflake | Un compte Snowflake avec des autorisations de niveau administrateur est requis pour profiter de ce partenariat. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration

Pour configurer le partage sécurisé des données avec votre compte Braze, procédez comme suit.

1. Accédez à **Partner Integrations** > **Data Sharing** dans le tableau de bord de Braze.
2. Entrez les informations de votre compte Snowflake. Vous pouvez trouver l'ID de votre compte Snowflake en exécutant `SELECT CURRENT_ACCOUNT()` dans le compte de destination.
3. Si vous utilisez un partage CRR, spécifiez le fournisseur de cloud et la région.
4. Sélectionnez **Créer un partage de données.**

Dans quelques instants, votre partage de données devrait être visible dans votre instance Snowflake. Créez une base de données à partir du partage afin de pouvoir consulter et interroger les tables. Notez que vous devez être administrateur de compte pour voir le partage de données.

![Partage de données entrantes ] () {% image_buster /assets/img/inbound-data-share.png %}

Dans le contexte du partage de données, Braze est un [fournisseur](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#providers) de données, c'est-à-dire tout compte Snowflake qui crée des partages et les met à la disposition d'autres comptes Snowflake pour qu'ils puissent les utiliser. Vous êtes un [consommateur de données](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#consumers) : tout compte qui choisit de créer une base de données à partir d'un partage mis à disposition par un fournisseur de données.

## Utilisation et visualisation

Une fois le partage de données configuré, vous devrez créer une base de données à partir du partage de données entrant, afin que toutes les tables partagées apparaissent dans votre instance Snowflake et soient interrogeables comme toutes les autres données que vous stockez dans votre instance. Cependant, gardez à l'esprit que les données partagées sont en lecture seule et peuvent uniquement être interrogées mais ne peuvent en aucun cas être modifiées ou supprimées.

Comme pour Currents, vous pouvez utiliser votre partage de données sécurisé Snowflake pour :
- Créer des rapports complexes
- Réaliser une modélisation d'attribution
- Sécuriser le partage au sein de votre entreprise
- Associer les données brutes des événements ou des utilisateurs à un CRM (tel que Salesforce)
- Et bien plus encore

[Téléchargez les schémas de table bruts ici. ][schémas]

### Schéma d'ID utilisateur

Notez les différences suivantes entre les conventions de dénomination de Braze et Snowflake pour les identifiants utilisateur.

| Schéma de Braze | Schéma Snowflake | Descriptif |
| ----------- | ----------- | ----------- |
| `braze_id` | `"USER_ID"` | L'identifiant unique attribué automatiquement par Braze. |
| `external_id` | `"EXTERNAL_USER_ID"` | Identifiant unique du profil d'un utilisateur défini par le client. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Informations importantes et limites

### Modifications disruptives et non disruptives

#### Changements non disruptifs
Les modifications non disruptives peuvent intervenir à tout moment et apportent généralement des fonctionnalités supplémentaires. Exemples de changements non disruptifs :
- Ajouter une nouvelle table ou vue
- Ajouter une colonne à une table ou à une vue existante

{% alert important %}
Les nouvelles colonnes étant considérées comme non disruptives, Braze recommande vivement de répertorier explicitement les colonnes qui vous intéressent dans chaque requête au lieu d'utiliser des requêtes `SELECT *`. Vous pouvez également créer des vues qui nomment explicitement les colonnes, puis interroger ces vues plutôt que les tables directement.
{% endalert %}

#### Changements disruptifs
Dans la mesure du possible, les changements disruptifs seront précédés d'une annonce et d'une période de migration. Voici quelques exemples de changements radicaux :
- Suppression d'un tableau ou d'une vue
- Suppression d'une colonne d'une table ou d'une vue existante
- Modification du type ou de la nullabilité d'une colonne existante

### Régions Snowflake
Braze héberge actuellement toutes les données au niveau des utilisateurs dans les régions Snowflake AWS US East-1 et EU-Central (Francfort). Pour les utilisateurs situés en dehors de ces régions, Braze peut fournir un partage de données à des clients communs qui hébergent leur infrastructure Snowflake dans n'importe quelle région AWS, Azure ou GCP.

### Conservation des données

#### Politique de rétention
Toutes les données datant de plus de deux ans seront archivées et transférées vers un stockage à long terme. Dans le cadre du processus d'archivage, tous les événements sont anonymisés et tous les champs contenant des informations personnelles identifiables (PII) sont supprimés (notamment des champs d’informations personnelles identifiables, tels que `properties`). Les données archivées contiennent encore le champ `user_id`, qui permet une analyse par utilisateur sur toutes les données d'événements.

Vous pourrez effectuer des recherches sur les données des deux dernières années pour chaque événement dans la vue `USERS_*_SHARED` correspondante. En outre, chaque événement aura une vue `USERS_*_SHARED_ALL` qui pourra être interrogée pour renvoyer des données anonymisées et non anonymisées.

#### Données historiques
Les archives des données d'événements historiques dans Snowflake remontent à avril 2019. Au cours des premiers mois de stockage des données par Braze dans Snowflake, des modifications ont été apportées au produit. Certaines de ces données peuvent avoir légèrement changé ou avoir des valeurs nulles (car nous ne transmettions pas de données dans tous les champs disponibles pour le moment). Il est préférable de supposer que les résultats qui incluent des données antérieures à août 2019 peuvent sembler légèrement différents des attentes.

### Conformité au règlement général sur la protection des données (RGPD)
Presque tous les enregistrements d'événements que Braze stocke incluent quelques champs représentant les informations personnelles identifiables (PII) des utilisateurs. Certains événements peuvent inclure l'adresse e-mail, le numéro de téléphone, l'ID de l'appareil, la langue, le sexe et les informations d'emplacement/localisation. Si la requête d'oubli d'un utilisateur est soumise à Braze, nous annulerons ces champs PII pour tout événement appartenant à ces utilisateurs. De cette façon, nous ne supprimons pas l'historique de l'événement, mais celui-ci ne peut plus jamais être lié à une personne en particulier.

### Rapidité, performance, coût des requêtes
La vitesse, les performances et le coût de toute requête exécutée sur les données sont déterminés par la taille de l'entrepôt que vous utilisez pour interroger les données. Dans certains cas, en fonction de la quantité de données à laquelle vous accédez à des fins d'analyse, il se peut que vous deviez utiliser un entrepôt plus grand pour que la requête aboutisse. Snowflake propose d'excellentes ressources sur la meilleure façon de déterminer la taille à utiliser, notamment [ une vue d'ensemble des entrepôts](https://docs.snowflake.net/manuals/user-guide/warehouses-overview.html) et des[considérations relatives aux entrepôts](https://docs.snowflake.net/manuals/user-guide/warehouses-considerations.html)

## Références Braze

Benchmarks, [un outil de données créé par Braze](https://www.braze.com/perspectives/benchmarks), permet aux prospects et aux clients de Braze de se situer par rapport aux meilleurs acteurs de leur secteur en comparant leurs indicateurs aux benchmarks industriels de Braze.

Les secteurs initiaux sont les suivants :
- Services de livraison
- Commerce électronique
- Éducation
- Divertissement
- Finances
- Jeux
- Santé
- Style de vie
- Restaurants
- Commerce de détail
- Technologie
- Transport
- Tourisme

Nos données d'analyse comparative sont également disponibles directement dans le [Snowflake Data Exchange](https://app.snowflake.com/marketplace/listing/GZT0Z5I4XXR).

> Pour consulter un ensemble d'exemples de requêtes à référencer lors de la configuration de Snowflake, consultez nos [exemples de requêtes][SQ] et nos exemples de [configuration de pipeline d'événements ETL][ETL].

[SQ]: {{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/sample_queries/
[ETL]: {{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/etl_pipline_setup/
[schémas ] : {% image_buster /assets/download_file/data-sharing-raw-table-schemas.txt %}
