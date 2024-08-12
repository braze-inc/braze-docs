---
nav_title: Snowflake
article_title: Snowflake
alias: /partners/snowflake/
page_order: 1
description: "Cet article de référence présente le partenariat entre Braze et Snowflake, un entrepôt de données cloud SQL spécialement conçu pour vos données et utilisateurs."
page_type: partner
search_tag: Partenaire

---

# [![Cours d’apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/snowflake-secure-data-sharing-via-braze/){: style="float:right;width:120px;border:0;" class="noimgborder"}Snowflake

> [Snowflake](https://docs.snowflake.net/manuals/user-guide/intro-key-concepts.html) est un entrepôt de données cloud SQL spécialement conçu et proposé sous forme de oftware-as-a-Service S (SaaS). Snowflake fournit un entrepôt de données plus rapide, plus facile à utiliser et bien plus flexible que les entrepôts de données traditionnels. Grâce à l’architecture unique et brevetée de Snowflake, vous pouvez facilement regrouper toutes vos données, effectuer des analyses rapides et tirer parti des données analysées pour tous vos utilisateurs.

Les campagnes marketing personnalisées et pertinentes nécessitent un accès opportun aux données. C’est pourquoi Braze s’est associé à Snowflake pour lancer Data Sharing (Partage de données). Cette offre conjointe permet aux marketeurs de libérer plus rapidement que jamais le plein potentiel de leurs données d’engagement client et de campagne.

L’[intégration de Braze et Snowflake](https://www.braze.com/perspectives/article/snowflake-partner-announcement) tire parti de l’échange de données de Snowflake pour développer votre présence, trouver de nouveaux clients et étendre votre portée grâce à la base de clients en constante croissance de Snowflake.

{% alert tip %}
**Vous désirez avoir accès à des données au niveau de Snowflake sans avoir besoin d’un compte Snowflake ?**<br>Regardez [les comptes en Lecture de Snowflake]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/how_braze_uses_currents/#snowflake-reader-accounts). Avec les comptes Lecture, Braze créera et partagera vos données dans un compte et vous donnera les identifiants pour vous connecter et accéder à vos données. Tous les partages et facturations de données seront alors gérés intégralement par Braze.
{% endalert %}

## Qu’est-ce que Data Sharing ?

La fonctionnalité [Secure Data Sharing](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html) de Snowflake permet à Braze de vous donner un accès sécurisé aux données sur notre portail Snowflake sans que vous ayez à vous soucier des contraintes ou ralentissements du flux de travail, des points d’échec et des coûts inutiles habituellement associés aux fournisseurs de données. Le partage de données peut être défini par l’intégration suivante ou à l’aide des [comptes en Lecture de Snowflake]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/how_braze_uses_currents/#snowflake-reader-accounts).

- **Réduire la durée d’obtention des insights**<br>Dites adieu aux processus ETL qui mettent des semaines à se mettre en place. Les architectures uniques de Braze et Snowflake rendent immédiatement accessibles toutes les données de campagne et d’engagement client, dès l’instant où elles arrivent dans le data lake. Aucune donnée n’est copiée ou déplacée, vous pouvez donc proposer des expériences client basées sur les informations les plus pertinentes et les plus récentes.
- **Répartition des silos de données**<br>Créez une vue globale de vos clients sur tous vos canaux et plateformes. Data Sharing permet de joindre vos données d’engagement client Braze avec toutes vos autres données Snowflake pour obtenir des informations plus approfondies sur une seule source fiable.
- **Découvrez comment votre engagement s’accumule**<br>Optimisez vos stratégies d'engagement client avec Braze Benchmarks. Cet outil interactif, optimisé par Braze et Snowflake, vous permet de comparer les données d’engagement de votre marque à des points de référence de votre secteur et de tous les canaux et plateformes d’appareils.

Consultez [Introduction à Secure Data Sharing](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#how-does-secure-data-sharing-work) pour en savoir plus sur le fonctionnement de Data Sharing (Partage de données) de Snowflake.

## Conditions préalables

Si vous êtes intéressé par cette intégration, contactez votre gestionnaire du succès des clients ou votre gestionnaire de compte Braze et demandez des renseignements sur les services de stratégie de données de Braze pour Secure Data Sharing avec Snowflake. Cela permettra d’accélérer le processus du côté de Braze et nous configurerons vos vues en un rien de temps !

| Condition | Description |
| ----------- | ----------- |
| Compte Snowflake | Un compte Snowflake avec autorisations administrateur est requis pour profiter de ce partenariat. |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

Avec Data Sharing, aucune donnée réelle n’est copiée ou transférée entre les comptes. Le partage est réalisé grâce à la couche de services et à la librairie de métadonnées uniques de Snowflake. Il s’agit d’un concept important, car les données partagées ne prennent pas de place dans un compte client et, par conséquent, ne contribuent pas aux frais mensuels de stockage des données du consommateur. Les **seuls** frais pour les consommateurs concernent les ressources informatiques (c.-à-d. les entrepôts virtuels) utilisées pour interroger les données partagées.

En outre, en utilisant les fonctions intégrées et les capacités d’autorisation de Snowflake, l’accès aux données partagées depuis Braze peut être contrôlé et régi par les contrôles d’accès déjà en place sur votre compte Snowflake et les données qui y sont stockées. L’accès peut être restreint et surveillé de la même manière qu’avec vos propres données.

Lorsqu’un client demande un partage de données, Braze provisionnera le partage depuis le ou les groupes d’apps au sein desquels le partage a été acheté. Une fois le partage provisionné, toutes les données sont immédiatement accessibles depuis votre instance Snowflake sous la forme d’un partage de données entrantes. 

![Partage de données entrantes]({% image_buster /assets/img/inbound-data-share.png %})

Une fois le partage visible dans votre instance (un rôle `ACCOUNTADMIN` est requis pour le voir), vous devez créer une base de données à partir de ce partage de façon à pouvoir voir et interroger les tableaux.

Dans le contexte de Data Sharing, Braze est un [fournisseur de données](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#providers) ; tout compte Snowflake qui crée des partages et les rend disponibles pour d’autres comptes Snowflake. Vous, êtes un [consommateur de données](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#consumers) ; tout compte qui choisit de créer une base de données à partir d’un partage mis à disposition par un fournisseur de données.

## Utilisation et visualisation

Une fois le partage de données provisionné, vous devez créer une base de données à partir du partage de données entrantes, ce qui vous permet de consulter tous les tableaux partagés dans votre instance Snowflake et de les interroger comme pour toutes les autres données que vous stockez dans votre instance. Cependant, gardez à l’esprit que les données partagées sont en lecture seule. Elles peuvent être interrogées, mais vous ne pouvez pas les modifier ou les supprimer de quelque manière que ce soit.

Comme pour Currents, vous pouvez utiliser Secure Data Sharing (Partage de données sécurisé) de Snowflake pour :
- Créer des rapports complexes
- Modéliser des attributions
- Partager des données en toute sécurité au sein de votre entreprise
- Mapper les données brutes ou les données utilisateur vers un système de gestion de la relation client (comme Salesforce)
- Et plus encore

[Téléchargez ici les schémas bruts du tableau.][schemas]

## Informations importantes et restrictions

### Changements cassants et non cassants

#### Changements non cassants
Les changements non cassants peuvent survenir à tout moment et apportent généralement des fonctionnalités supplémentaires. Exemples de changements non cassants :
- Ajout d’un nouveau tableau ou d’une nouvelle vue
- Ajout d’une colonne dans une vue ou un tableau existant

{% alert important %}
Comme les nouvelles colonnes sont considérées comme non cassantes, Braze recommande vivement de répertorier explicitement les colonnes d’intérêt dans chaque requête au lieu d’utiliser des requêtes `SELECT *`. Vous pouvez également créer des vues qui nomment explicitement les colonnes, puis interroger ces vues plutôt que les tableaux.
{% endalert %}

#### Changements cassants
Lorsque cela est possible, les changements cassants seront précédés d’une annonce et d’une période de migration. Voici quelques exemples de changements cassants :
- Suppression d’un tableau ou d’une vue
- Suppression d’une colonne dans une vue ou un tableau existant
- Modification du type ou de la possibilité de valeur nulle d’une colonne existante

### Régions Snowflake
Braze héberge actuellement toutes les données de niveau utilisateur dans les régions de Snowflake AWS US East-1 et Europe centrale (Francfort). Pour les utilisateurs en dehors de ces régions, Braze peut fournir Data Sharing à des clients communs qui hébergent leur infrastructure Snowflake dans n’importe quelle région AWS ou Azure.

### Données historiques
Les historiques de données d’événement de Braze stockées dans Snowflake ne remontent qu’au mois d’avril 2019. Au cours des premiers mois où Braze y stockait des données, des modifications ont été apportées aux produits, et ont pu entraîner certains changements au niveau des données, qui semblaient alors légèrement différentes ou comportaient des valeurs nulles (car nous ne transmettions pas les données dans tous les champs disponibles à ce moment). Il est préférable de supposer que les résultats qui incluent des données avant août 2019 peuvent sembler légèrement différents de ce qui serait attendu.

### Conformité à la réglementation générale sur la protection des données (RGPD)
Presque tous les enregistrements d’événements conservés par Braze comprennent quelques champs représentant des informations personnellement identifiables (IPI) sur les utilisateurs. Certains événements peuvent inclure l’adresse e-mail, le numéro de téléphone, l’ID d’appareil, la langue, le sexe et des informations d’emplacement. Si un utilisateur souhaite faire valoir son droit à l’oubli et en soumet la demande à Braze, nous annulerons ces champs IPI pour tout événement appartenant à cet utilisateur. De cette façon, nous ne supprimons pas l’historique de l’événement, mais l’événement ne pourra plus jamais être associé à une personne donnée.

### Vitesse, performances et coût des requêtes
La vitesse, la performance et le coût de toute requête exécutée sur des données sont déterminés par la taille de l’entrepôt que vous utilisez pour interroger les données. Dans certains cas, selon la quantité de données que vous consultez pour analyse, vous pourrez avoir besoin d’un entrepôt plus grand pour que la requête aboutisse. Snowflake propose d’excellentes ressources pour déterminer la taille de l’entrepôt dont vous avez besoin, notamment [Aperçu des entrepôts](https://docs.snowflake.net/manuals/user-guide/warehouses-overview.html) et [Considérations relatives à l’entrepôt](https://docs.snowflake.net/manuals/user-guide/warehouses-considerations.html)

### Tables d’informations personnellement identifiables et NON_PII - obsolètes
Auparavant, Braze séparait les colonnes qui contenaient des informations personnellement identifiables dans des tableaux séparés qui se terminaient par `_PII`. Les autres colonnes étaient stockées dans des tableaux qui se terminaient par `_NON_PII`. Ces tableaux ont depuis été remplacés par des tableaux qui contiennent toutes les colonnes associées à un événement. Ce changement permet de ne plus effectuer de calculs supplémentaires pour obtenir une vue complète d’un événement. Si vous utilisiez les anciens tableaux d’informations personnellement identifiables ou NON_PII, mettez à jour votre intégration pour utiliser les nouvelles tables unifiées.

## Braze Benchmarks

Benchmarks est [un outil de données développé par Braze](https://www.braze.com/perspectives/benchmarks) pour permettre aux prospects et clients de Braze de se comparer aux meilleurs acteurs de leur secteur en comparant leurs indicateurs aux points de références de Braze.

Les secteurs pris en charge comprennent : 
- Services de livraison
- eCommerce
- Éducation
- Divertissement
- Finance
- Jeux vidéo
- Santé
- Mode de vie
- Restauration
- Vente au détail
- Technologies
- Transports
- Tourisme

Nos données de référence sont également disponibles directement dans [Snowflake Data Exchange](https://app.snowflake.com/marketplace/listing/GZT0Z5I4XXR).

> Consultez nos [exemples de requêtes][SQ] et nos exemples de [configuration du pipeline d’événements ETL][ETL] pour vous aider à configurer Snowflake.

[SQ]: {{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/sample_queries/
[ETL]: {{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/etl_pipline_setup/
[schemas]: {% image_buster /assets/download_file/data-sharing-raw-table-schemas.txt %}
