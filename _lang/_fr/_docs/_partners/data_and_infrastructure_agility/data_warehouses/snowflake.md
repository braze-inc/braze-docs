---
nav_title: Flocon de neige
article_title: Flocon de neige
alias: /fr/partners/snowflake/
page_order: 1
description: "Cet article décrit le partenariat entre Braze et Snowflake, un entrepôt de données SQL pour toutes vos données et tous vos utilisateurs."
page_type: partenaire
search_tag: Partenaire
---

# Partage de données sécurisées par Snowflake

Les campagnes de marketing personnalisées et pertinentes requièrent un accès immédiat aux données. C’est pourquoi Braze s’est associé à Snowflake pour lancer le partage de données. Cette offre conjointe permet aux marketeurs de libérer plus rapidement que jamais le potentiel de leur engagement client et de leurs données de campagne.

Braze tire parti de l’échange de données de Snowflake pour construire une présence, trouver de nouveaux clients et étendre la portée grâce à la base de clients toujours croissante de Snowflake.

En savoir plus sur ce partenariat [ici](https://www.braze.com/perspectives/article/snowflake-partner-announcement)!

## Qu'est-ce que le flocon de neige ?

[Snowflake](https://docs.snowflake.net/manuals/user-guide/intro-key-concepts.html) est un entrepôt de données analytiques fourni en tant que Logiciel-comme-un-Service (SaaS). Snowflake fournit un entrepôt de données plus rapide, plus facile à utiliser et beaucoup plus souple que les offres d'entrepôt de données traditionnelles.

La plate-forme de données sur le cloud de Snowflake brise les barrières qui empêchent les organisations de toutes tailles de libérer la valeur réelle de leurs données. Snowflake équipe les marques avec une plate-forme unique et intégrée qui offre le seul entrepôt de données construit pour le nuage ; un accès instantané, sécurisé et gouverné à l'ensemble de leur réseau de données.

> Snowflake est un entrepôt de données SQL pour toutes vos données et tous vos utilisateurs. Avec l'architecture unique et brevetée de Snowflake il est facile d'amasser toutes vos données, permettent une analyse rapide et dérivent des informations basées sur des données pour tous vos utilisateurs.

## Qu'est-ce que le partage de données?

La fonctionnalité [de partage de données](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html) de Snowflake permet à Braze de vous donner un accès sécurisé aux données de notre portail Snowflake sans vous soucier du frottement ou du ralentissement du flux de travail, des points de défaillance et des coûts inutiles qui viennent avec les relations habituelles des fournisseurs de données.

#### Réduire le temps pour les aperçus
Dites adieu aux processus de ETL qui prennent des semaines pour se construire. Avec les architectures uniques de Braze et Snowflake, toutes les données d'engagement du client et de campagne sont immédiatement accessibles ET interrogeables à partir du moment où il arrive dans notre lac de données. Aucune donnée n'est copiée ou déplacée, de sorte que vous pouvez livrer des expériences clients en vous basant uniquement sur les informations les plus pertinentes et à jour.

#### Décomposer les silos de données
Créez une vue d'ensemble de vos clients sur les canaux et les plateformes. Le partage de données rend plus facile que jamais de rejoindre les données d'engagement de vos clients Braze avec toutes vos autres données de flocons de neige — créant ainsi des aperçus plus riches à travers un seul, source de vérité fiable.

#### Voyez comment votre engagement se pile
Optimisez vos stratégies d'engagement client avec Braze Benchmarks. Cet outil interactif, propulsé par Braze et Snowflake, vous permet de comparer les données d’engagement de votre marque à des repères à travers les canaux, l’industrie et la plate-forme d’appareils.

En savoir plus sur le fonctionnement du partage de données de Snowflake ici : [Introduction au partage sécurisé de données — Documentation Snowflake](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#how-does-secure-data-sharing-work)

## Intégration

> Si cette intégration vous intéresse, contactez votre gestionnaire de compte Braze ou de succès client et demandez-leur de consulter les Services de stratégie de Braze sur le partage sécurisé de données avec Snowflake. Cela fera entrer les cogs à l'intérieur de Braze et nous aurons vos vues configurées en un rien de temps!

{% alert important %}
Pour utiliser la fonctionnalité de partage de données de Braze, vous devez également être un client de Snowflake. Ceci est dû au fait que les données sont partagées avec la plateforme Snowflake.
{% endalert %}

Avec le partage de données, aucune donnée réelle n'est copiée ou transférée entre les comptes. Tout le partage est réalisé grâce à la couche de services et au magasin de métadonnées uniques de Snowflake. C'est un concept important, car cela signifie que les données partagées ne prennent pas en compte le consommateur et, ne contribue donc pas aux frais mensuels de stockage des données du consommateur. Les **seuls** frais pour les consommateurs sont pour les ressources informatiques (c'est-à-dire les entrepôts virtuels) utilisées pour interroger les données partagées.

En outre, en utilisant les rôles et les capacités d'autorisations intégrées de Snowflake, L'accès aux données partagées à partir de Braze peut être contrôlé et géré en utilisant les contrôles d'accès déjà en place pour votre compte Snowflake et les données qui s'y trouvent. L'accès peut être restreint et surveillé de la même manière que vos propres données.

Lorsqu'un partage de données est demandé par un client, Braze fournira la part des groupes d'applications pour lesquels le partage a été acheté. Une fois le partage fourni, toutes les données sont immédiatement accessibles à partir de votre instance Snowflake sous la forme d'un partage de données entrant.

![partage interne]({% image_buster /assets/img/inbound-data-share.png %})

Une fois que le partage est visible dans votre instance (vous devez être le rôle `ACCOUNTADMIN` pour le voir), vous devrez créer une base de données à partir du partage pour que vous puissiez voir et interroger les tables.

Dans le contexte du partage de données, Braze est un [fournisseur de données](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#providers) - tout compte Snowflake qui crée des partages et les met à la disposition d'autres comptes Snowflake à consommer. Vous, notre client, sont un [consommateur de données](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#consumers) - tout compte qui choisit de créer une base de données à partir d'un partage mis à disposition par un fournisseur de données.

## Utilisation et visualisation

Une fois le partage de données fourni, vous devrez créer une base de données à partir du partage de données entrant, qui fera alors apparaître toutes les tables partagées dans votre instance Snowflake et seront interrogeables comme toutes les autres données que vous stockez dans votre instance. Gardez toutefois à l'esprit que les données partagées sont prêtes et ne peuvent être consultées, mais ne peuvent être modifiées ou supprimées de quelque manière que ce soit.

Comme pour les courants, vous pouvez utiliser votre partage de données Snowflake sécurisé pour...

-   Créer des rapports complexes,
-   Effectuer la modélisation d'attribution,
-   Partage sécurisé au sein de votre propre entreprise,
-   Associer les données d'un événement ou d'un utilisateur à un CRM (comme Salesforce)...

Et bien plus encore!

\[Télécharger les schémas de tables brutes ici.\]\[schemas\]

## Informations et limitations importantes

### Interruption vs modifications sans rupture
#### Changements sans interruption
Les changements sans rupture peuvent se produire à tout moment et fournissent généralement des fonctionnalités supplémentaires.<br> Exemples de modifications non cassées :
- Ajout d'une nouvelle table ou vue
- Ajout d'une colonne à une table ou une vue existante

{% alert important %}
Parce que les nouvelles colonnes sont considérées comme non-cassantes, Braze recommande fortement de lister explicitement les colonnes d'intérêt dans chaque requête au lieu d'utiliser les requêtes `SELECT *`. Alternativement, les clients peuvent vouloir créer des vues qui nomment explicitement les colonnes, puis interroger ces vues au lieu des tables directement.
{% endalert %}

#### Changements en cours
Les changements survenus seront précédés d'une annonce et d'une période de migration si possible. Les exemples de modifications de rupture comprennent :
- Suppression d'une table ou d'une vue
- Supprimer une colonne d'une table ou d'une vue existante
- Modification du type ou de la nullabilité d'une colonne existante

### Régions de flocons de neige
Braze héberge actuellement toutes les données du niveau utilisateur dans les régions de Snowflake AWS US East-1 et EU-Central (Frankfurt). Cependant, nous sommes en mesure de fournir le partage de données à des clients conjoints qui hébergent leur infrastructure Snowflake dans toutes les régions AWS ou Azure.

### Données historiques
Les données historiques des événements de Braze en Snowflake ne remontent qu'à avril 2019. Au cours des premiers mois où nous stockons des données là-bas, nous avons fait quelques changements de produits qui peuvent avoir pour conséquence que certaines de ces données semblent légèrement différentes ou ont des valeurs nulles (comme nous ne passions pas de données dans tous les champs disponibles depuis le début.) Il est préférable de supposer que tout résultat incluant des données avant août 2019 peut sembler légèrement différent des attentes.

### Conformité PII et RGPD
Presque tous les enregistrements d'événements que nous stockons incluent quelques champs qui représentent les IPI des utilisateurs (informations personnellement identifiables). Certains événements peuvent inclure des données telles que l'adresse e-mail, le numéro de téléphone, l'ID de l'appareil, la langue, le sexe et les informations de localisation. En cas de demande d'oubli d'un utilisateur soumis au Brésil, nous annulerons ces champs PII pour tout événement appartenant à ces utilisateurs. De cette façon, nous ne supprimons pas l'historique de l'événement, mais maintenant l'événement ne peut jamais être lié à une personne spécifique.

#### Tableaux PII / NON_PII - obsolète
Dans le passé, Braze séparait les colonnes qui contenaient PII en tables séparées qui se terminaient par _PII. D'autres colonnes étaient stockées dans des tables qui se terminaient par _NON_PII. Ces tables sont devenues obsolètes, en faveur de tables qui contiennent toutes les colonnes associées à un événement. Ce changement évite la nécessité d'effectuer des calculs supplémentaires pour obtenir une vue complète d'un événement. Si vous utilisiez les anciennes tables PII / NON_PII, veuillez mettre à jour votre intégration pour utiliser les nouvelles tables unifiées.

### Vitesse, Performance, Coût des Requêtes
Vitesse, performance, vitesse et le coût de toute requête exécutée en plus des données est entièrement déterminé par la taille de l'entrepôt que vous utilisez pour interroger les données. Dans certains cas, en fonction de la quantité de données auxquelles vous accédez pour les analytiques, il se peut que vous ayez besoin d'utiliser une plus grande taille d'entrepôt pour que la requête soit performante ou même pour qu'elle se termine avant la fin du délai. Snowflake a d'excellentes ressources disponibles pour déterminer la taille à utiliser : [Aperçu des entrepôts — Documentation du flocon de neige](https://docs.snowflake.net/manuals/user-guide/warehouses-overview.html) et [Considérations de l'entrepôt — Documentation du flocon de neige](https://docs.snowflake.net/manuals/user-guide/warehouses-considerations.html)

## Braze benchmarks

Les Benchmarks de Braze permettront aux prospects et aux clients de Braze de voir comment ils se comparent aux meilleurs acteurs de leur industrie en comparant leurs indicateurs à ceux de l'industrie de Braze.

Nous avons créé un [Data Tool for Braze Benchmarks](https://www.braze.com/perspectives/benchmarks) pour que vous puissiez voir une sélection de données, en dehors de l'interface Snowflake.

Les premières industries sont les Services de livraison, Ecommerce, Education, Entertainment, Finance, Gaming, Santé, Mode de vie, Restaurants, Retail, Technologie, Transports et Voyages.

Nos données de benchmarking seront également disponibles directement dans le Snowflake Data Exchange.

> Pour un ensemble d'exemples de requêtes à référence lors de la configuration du flocons de neige, Consultez nos exemples [Échantillons de requêtes][SQ] et [ETL Event Pipeline Setup][ETL].
[schemas]: {% image_buster /assets/download_file/data-sharing-raw-table-schemas.txt %}

[SQ]: {{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/sample_queries/
[ETL]: {{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/etl_pipline_setup/
