---
nav_title: Partage des données avec Snowflake
hidden: true
---

# Intégration du partage des données Snowflake

> Lorsque Snowflake Data Share est utilisé comme méthode d'intégration, Braze provisionne un partage à votre instance Snowflake au nom du client. Ce partage inclura automatiquement tous les événements liés à l'engagement aux messages et au comportement de l'utilisateur.

Les parts sont provisionnées sur une base personnalisée après que le client a acheté un droit de partage de données Snowflake. Lorsqu'un client requête un partage de données, Braze ajoute un partage à l'espace de travail du client, et ce dernier peut utiliser l'interface utilisateur en libre-service pour ajouter les données du compte Snowflake du partenaire concerné.

![]({% image_buster /assets/img/snowflake.png %})

Une fois le partage provisionné, toutes les données sont immédiatement accessibles depuis l'instance Snowflake en tant que partage de données entrant.

![]({% image_buster /assets/img/snowflake2.png %})

Dans votre instance Snowflake, vous verrez une part par région. Chaque tableau comporte une colonne, `app_group_id`, qui est en fait une clé de locataire pour Braze. Lorsque de nouveaux clients sont ajoutés à un partage au sein d'une même région, ils apparaissent sous la forme de différents `app_group_ids` dans les tableaux existants.

{% alert important %}
Braze héberge actuellement toutes les données au niveau de l'utilisateur dans les régions AWS US East-1 et EU-Central (Francfort) de Snowflake. Bien que Braze puisse partager avec d'autres régions, il est plus rentable pour les clients de partager avec `US-EAST-1` et/ou `EU-CENTRAL-1`.
{% endalert %}

{% alert tip %}
Téléchargez les [schémas des tables brutes]({{site.baseurl}}/assets/download_file/data-sharing-raw-table-schemas.txt?ffbc5f5ca7092bc9ae26268aa0e711df) ici ou utilisez cet ensemble d'[exemples de données d'événements](https://app.snowflake.com/marketplace/listing/GZT0Z5I4XY0/braze-braze-user-event-demo-dataset) disponibles sur la place de marché de Snowflake pour vous familiariser avec les événements partagés.
{% endalert %}

## Gestion des événements en double

Les doublons sont possibles, mais tous les événements ont un identifiant unique, la colonne ID. Les doublons peuvent être supprimés à l’aide de `select distinct(id)`.

## Changements disruptifs et non disruptifs

### Changements non disruptifs

Les modifications non disruptives peuvent intervenir à tout moment et apportent généralement des fonctionnalités supplémentaires. Exemples de changements non disruptifs :
- Ajouter une nouvelle table ou vue
- Ajouter une colonne à une table ou à une vue existante

{% alert important %}
Les nouvelles colonnes étant considérées comme non sécables, Braze recommande vivement de répertorier explicitement les colonnes d'intérêt dans chaque requête plutôt que d'utiliser les requêtes `SELECT *`. Vous pouvez également créer des vues qui nomment explicitement des colonnes, puis interroger ces vues au lieu d'interroger directement les tables.
{% endalert %}

### Changements disruptifs

Dans la mesure du possible, les changements disruptifs seront précédés d'une annonce et d'une période de migration. Voici quelques exemples de changements radicaux :
- Suppression d'un tableau ou d'une vue
- Suppression d'une colonne d'une table ou d'une vue existante
- Modifier le type ou la nullité d'une colonne existante

## Conformité au règlement général sur la protection des données (RGPD).

Presque tous les enregistrements d'événements stockés par Braze comprennent quelques champs conseillant les utilisateurs en matière d'informations personnelles identifiables (PII). Certains événements peuvent inclure l'adresse e-mail, le numéro de téléphone, l'ID de l'appareil, la langue, le sexe et les informations d'emplacement/localisation. Si la requête d'oubli d'un utilisateur est soumise à Braze, nous supprimerons ces champs d'informations nominatives pour tout événement appartenant à ces utilisateurs. De cette manière, nous ne supprimons pas l'enregistrement historique de l'événement, mais l'événement ne peut plus être lié à une personne spécifique.
