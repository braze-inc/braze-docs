---
nav_title: MetaRouter
article_title: MetaRouter
description: "Améliorez la gestion des données de vos clients dans Braze grâce à MetaRouter. Cette solution performante de gestion des étiquettes côté serveur offre une conformité et un contrôle optimaux grâce à des options de déploiement fluides, que ce soit sur un cloud privé hébergé par MetaRouter ou sur votre propre infrastructure."
alias: /partners/MetaRouter/
page_type: partner
search_tag: Partner
---

# MetaRouter

> [MetaRouter améliore votre expérience](https://www.metarouter.io/) Braze en tant que puissante plateforme de gestion des balises côté serveur. Il vous permet d'orchestrer un parcours complet de données clients au sein de Braze, depuis la collecte de données fiable et complète enrichie jusqu'à 30 %, jusqu'à l'activation de flux d'événements en temps réel pour des parcours personnalisés. De plus, MetaRouter simplifie la mise en œuvre en éliminant le besoin de balises Braze ou d'autres balises tierces, ce qui vous permet de contrôler de manière granulaire, paramètre par paramètre, les données circulant dans Braze.

_Cette intégration est maintenue par Metarouter._

## Fonctionnalités prises en charge

- Les nouvelles tentatives peuvent être intégrées.
- Les requêtes sont groupées.
- Les problèmes de limitation de débit sont résolus par une nouvelle tentative.
- L'ID externe et les PII sont pris en charge. MetaRouter transmet leur identifiant anonyme et toutes les informations personnelles (e-mail, numéro de téléphone, nom) souhaitées par les clients.
- Vous pouvez envoyer des données sur les achats effectués à Braze et sur les événements personnalisés.
  - Les propriétés de l'événement sont prises en charge.
  - Les propriétés d'événements imbriquées ne sont pas prises en charge.

## Conditions préalables

Avant de commencer, vous aurez besoin des éléments suivants :

| Exigence           | Description                                                                                                                                          |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| Un compte MetaRouter  | Un compte [MetaRouter Enterprise](https://enterprise.metarouter.io/).                                                                                |
| Clé d'API REST Braze    | Une clé API REST de Braze avec des autorisations `users.track`. Pour en créer un, allez dans **Paramètres** > **Clés d'API**.                                                |
| Un endpoint REST Braze | [L'URL de votre endpoint REST.]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) Votre endpoint dépendra de l'URL de Braze pour votre instance. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Configuration de MetaRouter

Pour configurer MetaRouter pour votre intégration à Braze :

1. Accédez à MetaRouter et créez un nouveau cluster.
2. Choisissez les événements que vous souhaitez suivre.
3. Installez un SDK MetaRouter et intégrez des événements à votre site Web.
4. Connectez votre cluster à l'interface utilisateur de votre site Web.
5. Créez un nouveau pipeline.
6. Vérifiez que votre site Web envoie des événements à MetaRouter.

## Intégrer Braze

### Étape 1 : Ajouter l'intégration Braze

Dans Enterprise MetaRouter, sélectionnez **Intégrations** > **Nouvelle intégration >** **Braze**, puis donnez un nom à votre intégration. Entrez ensuite l'URL et la clé API de votre instance, puis sélectionnez **Appliquer les modifications**.

![Ajout de Braze en tant qu'intégration dans MetaRouter. ]({% image_buster /assets/img/metarouter/img1.png %}){: style="max-width:50%;"}

### Étape 2 : Ajouter un mappage d'événements

Ajoutez un mappage d'événements pour chaque sortie d'identité, puis configurez les événements que vous souhaitez envoyer à Braze. Lorsque vous avez terminé, sélectionnez **Enregistrer en tant que nouvelle révision**.

![Ajoutez un mappage d'événements pour chacune des sorties d'identité. ]({% image_buster /assets/img/metarouter/img2.png %})

