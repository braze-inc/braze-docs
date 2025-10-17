---
nav_title: Amazon Personalize
article_title: Amazon Personalize
alias: "/partners/amazon_personalize_overview/"
description: "Cet article de référence décrit une architecture de référence et une intégration entre Braze et Amazon Personalize. Cet article de référence vous aidera à comprendre les cas d'utilisation proposés par Amazon Personalize, les données avec lesquelles il fonctionne, comment configurer le service et comment l'intégrer à Braze."
page_type: partner
search_tag: Partner
---

# Amazon Personalize
<!--
{% multi_lang_include video.html id="xFZ3HMleYYE" align="right" %}
-->
> Amazon Personalize, c'est comme si vous disposiez de votre propre système de recommandation Amazon machine learning ouvert toute la journée. S'appuyant sur plus de 20 ans d'expérience en matière de recommandations, Amazon Personalize vous permet d'améliorer l'engagement client en proposant des recommandations personnalisées de produits et de contenus en temps réel et des promotions marketing ciblées.

_Cette intégration est gérée par Amazon Personalize._

## À propos de l'intégration

À l'aide de l'apprentissage automatique et d'un algorithme que vous aidez à définir, Amazon Personalize peut vous aider à créer un modèle qui génère des recommandations de haute qualité pour vos sites Web et applications. Ces modèles vous permettent de créer des listes de recommandations en fonction des comportements antérieurs des utilisateurs, de trier les éléments par pertinence et de recommander d'autres éléments en fonction de leur similitude. Les listes obtenues à l'aide de l'API Amazon Personalize peuvent ensuite être utilisées dans Braze Connected Content pour lancer des campagnes de recommandation Braze personnalisées. Grâce à l'intégration à Amazon Personalize, les clients ont la liberté de contrôler les paramètres utilisés pour entraîner les modèles et de définir des objectifs commerciaux facultatifs qui optimisent les résultats de l'algorithme. 

Cet article de référence vous aidera à comprendre les cas d'utilisation proposés par Amazon Personalize, les données avec lesquelles il fonctionne, comment configurer le service et comment l'intégrer à Braze.

## Conditions préalables

| Condition| Description|
| ---| ---| 
| Compte Amazon Web Service | Un compte AWS est nécessaire pour bénéficier de ce partenariat. Une fois que vous avez un compte AWS, vous pouvez accéder à Amazon Personalize via la console Amazon Personalize, l'interface de ligne de commande AWS (AWS CLI) ou les kits SDK AWS. |
| Cas d'utilisation définis | Avant de créer un modèle, vous devez déterminer votre cas d'utilisation pour cette intégration. Consultez la liste suivante pour les cas d'utilisation courants. |
| Ensembles de données | Les modèles de recommandation Amazon Personalize nécessitent trois types différents de jeux de données, d'interactions, d'utilisateurs et d'éléments. Consultez les informations suivantes pour connaître les exigences de chaque jeu de données. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% tabs %}
{% tab Cas d'utilisation %}

**Cas d'utilisation**

Avant de créer un modèle, vous devez déterminer votre cas d'utilisation pour cette intégration. Parmi les cas d'utilisation courants, citons :
- Recommandez des articles aux utilisateurs en fonction de leurs interactions précédentes, afin de créer une expérience véritablement personnalisée pour vos utilisateurs.
- Fournissez une liste d'articles ou de résultats de recherche adaptés à chaque utilisateur, en augmentant l'engagement en présentant les éléments en fonction de leur pertinence pour l'utilisateur.
- Trouvez des recommandations pour des articles similaires, afin d'aider les utilisateurs à découvrir de nouvelles choses.

Dans le guide suivant, nous nous concentrerons sur la recette de recommandations personnalisées pour les utilisateurs.

{% endtab %}
{% tab Ensembles de données %}

**Ensembles de données**

Pour commencer à utiliser les modèles de recommandation Amazon Personalize, vous avez besoin de trois types de jeux de données :

- Interactions
  - Stocke l'historique des interactions entre les utilisateurs et les éléments
  - Requiert les valeurs `USER_ID``ITEM_ID`, `EVENT_TYPE` et `TIMESTAMP` et accepte éventuellement les métadonnées relatives à l'événement
- Les utilisateurs
  - Stocke les métadonnées relatives aux utilisateurs
  - Nécessite une valeur `USER_ID` et au moins un champ de métadonnées (chaîne de caractères ou numérique) tel que le sexe, l'âge, l'adhésion au programme de fidélité
- Objets
  - Stocke les métadonnées relatives aux éléments
  - Nécessite un champ `ITEM_ID` et au moins un champ de métadonnées (textuelles, catégoriques ou numériques) qui décrit l'élément

Pour une recette de recommandations aux utilisateurs, vous devez fournir un ensemble de données d'interactions contenant au moins 1 000 points de données d'interaction provenant d'au moins 25 utilisateurs uniques ayant chacun au moins deux interactions. Ces ensembles de données peuvent être chargés en masse à l'aide de fichiers CSV stockés dans S3 ou de manière incrémentielle via l'API.

{% endtab %}
{% endtabs %}

## Création de modèles

### Étape 1 : Entraînement

Une fois les ensembles de données importés, vous pouvez créer une solution. Une solution utilise l'une des [recettes](https://docs.aws.amazon.com/personalize/latest/dg/working-with-predefined-recipes.html) (algorithmes) d'Amazon Personalize pour entraîner un modèle. Dans notre cas, nous utiliserons la recette `USER_PERSONALIZATION`. La formation de la solution crée une version de la solution (modèle entraîné) que vous pouvez évaluer en fonction des indicateurs de performance du modèle.

Amazon Personalize vous permet de régler les hyperparamètres utilisés par le modèle pour l'entraînement. Par exemple :
- Le paramètre « Percentile de longueur de l'historique utilisateur » de la console Amazon Personalize vous permet d'ajuster le percentile de l'historique utilisateur à inclure dans la formation :<br><br>![Min max profil utilisateur]({% image_buster /assets/img/amazon_personalize/min_and_max_user_percentile.png %})
  - `min_user_history_length_percentile`: exclut un pourcentage d'utilisateurs dont l'historique est très court, ce qui peut être utile pour éliminer les articles les plus populaires et créer des recommandations basées sur des modèles sous-jacents plus approfondis.
  - `max_user_history_length_percentile`: ajustez le pourcentage d'utilisateurs à prendre en compte lors des formations dont l'historique est très long.

Le nombre de dimensions cachées permet de détecter des modèles plus complexes pour des ensembles de données complexes, tandis que la technique de rétropropagation dans le temps (BPTT) ajuste les récompenses pour un événement précoce après qu'une chaîne d'événements s'est produite qui a donné lieu à une action de grande valeur.

En outre, Amazon Personalize permet de régler automatiquement les hyperparamètres en exécutant simultanément plusieurs versions de la solution avec différentes valeurs. Pour utiliser le réglage, activez l'option **Perform HPO** lors de la création d'une solution.

### Étape 2 : Evaluer et comparer

Une fois la formation terminée, vous êtes prêt à l'évaluer et à comparer les différentes versions. Chaque version de la solution affiche des indicateurs calculés. Parmi les indicateurs disponibles, citons :

- **Normaliser le gain cumulé actualisé :** compare l'ordre recommandé des articles à la liste réelle des articles et attribue à chaque article un poids correspondant à sa position dans la liste
- **Precision @k :** la quantité d'articles correctement recommandés divisée par la quantité de tous les articles recommandés, où `k` est le nombre d'articles
- **Rang réciproque moyen :** se concentre sur la première recommandation la mieux classée et calcule le nombre d'éléments recommandés consultés avant l'apparition de la première recommandation correspondante
- **Couverture :** proportion d'éléments uniques recommandés par rapport au nombre total d'éléments uniques dans l'ensemble de données

## Obtenir des recommandations

Une fois que vous avez créé une version de solution qui vous convient, il est temps de mettre en œuvre les recommandations. Vous pouvez accéder aux recommandations de deux manières :

1. campagne en temps réel<br>Une campagne est une version de solution déployée avec un débit de transactions minimal défini. Une transaction est un appel d'API unique pour obtenir une sortie de recommandation, et elle est définie comme TPS, ou transactions par seconde, avec une valeur minimale de un. La campagne ajustera les ressources en cas d'augmentation de la charge, mais celles-ci ne tomberont pas en dessous de votre valeur minimale. Vous pouvez consulter les recommandations dans la console, dans l'interface de ligne de commande AWS ou via les kits SDK AWS dans votre code.<br><br>
2. Tâche par lots<br>Une tâche par lots exporte les recommandations vers un compartiment S3. La tâche prend une entrée d'un fichier JSON contenant la liste des ID d’utilisateur pour lesquels vous souhaitez exporter les recommandations. Ensuite, après avoir spécifié les autorisations appropriées et la destination de sortie, vous êtes prêt à exécuter la tâche. Le temps d'exécution dépend de la taille de vos ensembles de données et de la longueur de la liste des recommandations.

### Filtres

Les filtres vous permettent d'ajuster la sortie des recommandations en excluant des éléments en fonction de leur ID, de leur type d'événement ou de leurs métadonnées. Vous pouvez également filtrer les utilisateurs en fonction de leurs métadonnées, telles que leur âge ou leur statut de membre du programme de fidélité. Les filtres peuvent s'avérer utiles pour empêcher de recommander des éléments avec lesquels l'utilisateur a déjà interagi.

## Intégrer les résultats avec Braze

Avec le modèle créé et la campagne de recommandations, vous êtes prêt à lancer une campagne Braze pour vos utilisateurs à l'aide de cartes de contenu et de contenu connecté.
Avant de lancer une campagne Braze, vous devez créer un service capable de diffuser ces recommandations via une API. Vous pouvez suivre l'[étape 3 de l'article de l'atelier]({{site.baseurl}}/partners/amazon_personalize_workshop/#step-3-send-personalized-emails-from-braze) pour déployer le service à l'aide des services AWS. Vous pouvez également déployer votre propre service backend indépendant qui fournit les recommandations.

### Cas d'utilisation de la campagne de carte de contenu

Lancez une campagne de cartes de contenu avec le premier élément recommandé de la liste.<br><br>
Dans les exemples suivants, nous allons interroger
l’`GET http://<service-endpoint.com>/recommendations?user_id=user123` endpoint avec un paramètre `user_id` qui renverra une liste d'articles recommandés :

```json
[
  {
    "id": "abc123",
    "url": "http://productpage.com/product/abc123",
    "name": "First Item",
    "price": 39.99,
    "image": "http://pp.cdn.com/abvh3321pjb1j"
  },
  {
    "id": "xyz987",
    "url": "http://productpage.com/product/xyz987",
    "name": "Great Item",
    "price": 19.99,
    "image": "http://pp.cdn.com/234bjl1gioj1b2b"
  },
  ...
]
```

Dans le tableau de bord de Braze, créez une nouvelle [campagne de cartes de contenu]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/). Dans le champ de texte du message, créez un bloc de contenu connecté Liquid pour interroger l'API et enregistrer la réponse dans la variable `recommendations` :

{% raw %}

```liquid
{% connected_content https:/<service-endpoint.com>/recommendations?user_id={{${user_id}}} :save recommendations %}
```

Vous pouvez ensuite référencer le premier élément du tableau obtenu et afficher le contenu à l'utilisateur :

```liquid
This seems like a great fit for you:
{% recommendations[0].name %}
{% recommendations[0].price %}
```

{% endraw %}

En incluant le titre, l'image et le lien vers l'URL, voici à quoi ressemblerait la fiche de contenu complète :

![Image d'une campagne avec du contenu connecté ajouté au corps du message et au champ « Ajouter une image ». Cette image montre également la logique de contenu connecté ajoutée au champ "Redirect to Web URL", qui renvoie les utilisateurs à une URL de recommandation.]({% image_buster /assets/img/amazon_personalize/content-card-campaign.png %})


