---
nav_title: Personnaliser Amazon
article_title: Personnaliser Amazon
alias: /fr_FR/FR/FR/FR/FR/FR/FR/FR/FR/FR/FR/FR/FR/FR/FR/FR/FR/FR/FR/FR/FR/FR/FR/FR/FR/FR/FR/
description: "Cet article décrit une architecture de référence et l'intégration entre Braze et Amazon Personalize. Cet article vous aidera à comprendre les cas d'utilisation que Amazon Personnalise offres, les données avec lesquelles il fonctionne, comment configurer le service, et comment intégrer cela avec Braze."
page_type: partenaire
search_tag: Partenaire
---

# Personnaliser Amazon

<!--
{% include video.html id="xFZ3HMleYYE" align="right" %}
-->
> Amazon Personalize est comme avoir votre propre système de recommandation automatique Amazon pour toute la journée. Basé sur plus de 20 ans d'expérience dans les recommandations, La personnalisation d'Amazon vous permet d'améliorer l'engagement de vos clients en faisant fonctionner en temps réel des recommandations de produits et de contenu personnalisés et des promotions marketing ciblées.

En utilisant l'apprentissage automatique et un algorithme que vous aidez à définir, Amazon Personalize peut vous aider à former un modèle qui produit des recommandations de haute qualité pour vos sites Web et applications. Ces modèles vous permettront de créer des listes de recommandations basées sur les comportements passés des utilisateurs, trier les éléments par pertinence, et recommander d'autres éléments en fonction de la similarité. Les listes obtenues de l'API de personnalisation d'Amazon peuvent ensuite être utilisées dans le contenu connecté de Braze pour exécuter des campagnes de recommandation personnalisées de Braze. En intégrant avec Amazon Personalize, les clients ont la liberté de contrôler les paramètres utilisés pour former les modèles et de définir des objectifs commerciaux facultatifs qui optimisent la sortie de l'algorithme.

Cet article vous aidera à comprendre les cas d'utilisation que Amazon Personnalise offres, les données avec lesquelles il fonctionne, comment configurer le service, et comment intégrer cela avec Braze.

## Pré-requis

| Exigences                    | Libellé                                                                                                                                                                                                                                                                     |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Compte du Service Web Amazon | Avant d'utiliser Amazon Personalize, vous devez avoir un compte Amazon Web Services (AWS). Une fois que vous avez un compte AWS, vous pouvez accéder à Amazon Personalize via la console Amazon Personalize l'interface en ligne de commande AWS (AWS CLI), ou les SDK AWS. |
| Cas d'utilisation définis    | Avant de créer un modèle, vous devez déterminer votre cas d'utilisation pour cette intégration. Référez-vous à la liste suivante pour les cas d'utilisation courante.                                                                                                       |
| Datasets                     | Les modèles de recommandation personnalisés Amazon requièrent trois types différents de jeux de données, d'interactions, d'utilisateurs et d'éléments. Référez les détails suivants pour voir les exigences pour chaque jeu de données.                                     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

{% tabs %}
{% tab Use Cases %}

__Cas d'utilisation__

Avant de créer un modèle, vous devez déterminer votre cas d'utilisation pour cette intégration. Certains cas d'utilisation courants incluent :
- Recommandez des éléments pour les utilisateurs en fonction de leurs interactions précédentes, en créant une expérience vraiment personnalisée pour vos utilisateurs.
- Fournir une liste d'éléments ou de résultats de recherche adaptés à chaque utilisateur, augmentant l'engagement en affichant des éléments par pertinence pour l'utilisateur.
- Trouvez des recommandations pour des articles similaires, aidant les utilisateurs à découvrir de nouvelles choses.

Dans le guide ci-dessous, nous nous concentrerons sur la recette de recommandations personnalisées de l'utilisateur.

{% endtab %}
{% tab Datasets %}

__Datasets__

Pour commencer avec Amazon Personalize recommendation models, vous avez besoin de trois types de jeux de données :

- Interactions
  - Stocke les interactions historiques entre les utilisateurs et les éléments
  - Nécessite des valeurs `USER_ID`, `ITEM_ID`, `EVENT_TYPE` et `TIMESTAMP` et éventuellement accepte les métadonnées à propos de l'événement
- Utilisateurs
  - Stocke les métadonnées des utilisateurs
  - Nécessite une valeur `USER_ID` et au moins un champ de métadonnées (chaîne de caractères ou numériques) tel que le sexe, l'âge, l'adhésion à la fidélité
- Éléments
  - Stocke les métadonnées sur les éléments
  - Nécessite un `ITEM_ID` et au moins un champ de métadonnées (textural, catégorique ou numérique) qui décrit l'élément

Pour une recette de recommandations d'utilisateur, vous devez fournir un jeu de données d'interactions contenant au moins 1000 points d'interaction provenant d'au moins 25 utilisateurs uniques avec au moins deux interactions chacune. Ces jeux de données peuvent être téléchargés en vrac en utilisant des fichiers CSV stockés dans S3 ou incrémentalement via l'API.

{% endtab %}
{% endtabs %}

## Création de modèles

### Étape 1 : Entraînement

Une fois les jeux de données importés, vous pouvez créer une solution. Une solution utilise une des recettes [Personnaliser Amazon](https://docs.aws.amazon.com/personalize/latest/dg/working-with-predefined-recipes.html) (algorithmes) pour former un modèle. Dans notre cas, nous utiliserons la recette `USER_PERSONALIZATION`. La formation de la solution crée une version de solution (modèle formé) que vous pouvez évaluer en fonction des paramètres de performance du modèle.

Amazon Personalize vous permet d'ajuster les hyperparamètres que le modèle utilise pour la formation. Par exemple :
- Le paramètre "Percentile de longueur de l'historique de l'utilisateur" trouvé dans la console de personnalisation d'Amazon vous permet d'ajuster le centile de l'historique des utilisateurs à inclure dans la formation :<br><br>! Paramètre de profil maximum minimum][3]
  - `min_user_history_length_percentile`: exclut un pourcentage d'utilisateurs de longueur historique très courte, qui peut être utile pour éliminer les éléments populaires et construire des recommandations basées sur des modèles sous-jacents plus profonds.
  - `max_user_history_length_percentile`: ajuster le pourcentage d'utilisateurs à prendre en compte lors d'une formation avec des longueurs d'histoire très longues.

Le nombre de dimensions cachées permet de détecter des modèles plus compliqués pour des jeux de données complexes, alors que la propagation à travers la technique de temps (BPTT) ajuste les récompenses pour un événement précoce après qu'une chaîne d'événements ait eu lieu qui a donné lieu à une action de grande valeur.

En outre, Amazon Personalize propose un réglage automatique des hyperparamètres en exécutant plusieurs versions de la solution avec différentes valeurs simultanément. Pour utiliser le réglage, activez __Effectuer HPO__ lors de la création d'une solution.

### Étape 2 : Évaluer et comparer

Une fois qu'une solution a terminé la formation, vous êtes prêt à l'évaluer et à comparer différentes versions. Chaque version de la solution affiche les métriques calculées. Certaines des mesures disponibles incluent :

- `Normaliser le gain cumulatif escompté`: compare l'ordre des articles recommandé à la liste réelle des articles et donne à chaque article un poids correspondant à sa position dans la liste
- `Précision @k`: la quantité d'éléments recommandés correctement divisée par la quantité de tous les éléments recommandés, où `k` est le nombre d'éléments
- `Rang moyen`: se concentre sur le premier, la recommandation la plus classée et calcule le nombre d'éléments recommandés avant que la première recommandation apparaisse
- `Couverture`: la proportion d'éléments uniques recommandés par rapport au nombre total d'éléments uniques dans le jeu de données

## Récupération des recommandations

Une fois que vous avez créé une version de la solution qui vous convient, il est temps de mettre les recommandations à utiliser. Il y a deux façons d'accéder aux recommandations :

1. Campagne en temps réel<br>Une campagne est une version de solution déployée avec un débit minimum défini de transaction. Une transaction est un appel API unique pour obtenir la sortie de la recommandation, et il est défini comme TPS, ou transactions par seconde, avec une valeur minimale d'une. La campagne va mettre à l'échelle les ressources en cas d'augmentation de la charge, mais elle ne tombera pas en dessous de votre valeur minimale. Vous pouvez interroger les recommandations dans la console, AWS CLI, ou via AWS SDKs dans votre code.<br><br>
2. Tâche en lot<br>Une tâche en lot exporte les recommandations vers un seau S3. La tâche prend une saisie d'un fichier JSON avec une liste des identifiants utilisateur pour lesquels vous souhaitez exporter les recommandations. Ensuite, après avoir spécifié les autorisations correctes et la destination de sortie, vous êtes prêt à exécuter la tâche. Le temps d'exécution dépend de la taille de vos jeux de données et de la longueur de la liste des recommandations.

### Filtres

Les filtres vous permettent d'ajuster la sortie de recommandation en excluant les éléments en fonction de l'ID de l'élément, du type d'événement ou des métadonnées. Vous pouvez également filtrer les utilisateurs en fonction de leurs métadonnées, telles que l'âge ou le statut d'abonnement de fidélité. Les filtres peuvent être utiles pour éviter de recommander des éléments avec lesquels l'utilisateur a déjà interagi.

## Intégration des résultats avec Braze

Avec le modèle créé et la campagne de recommandations, vous êtes prêt à lancer une campagne Braze pour vos utilisateurs en utilisant les Cartes de Contenu et le Contenu Connecté. Avant de lancer une campagne Braze, vous devez créer un service qui puisse servir ces recommandations à travers une API. Vous pouvez suivre [étape 3 dans l'article de l'atelier][1] pour déployer le service en utilisant les services AWS. Vous pouvez également déployer votre propre service d'arrière-plan indépendant qui fournit les recommandations.

### Exemple de campagne de carte de contenu

Laissons une campagne de carte de contenu avec le premier élément recommandé de la liste.<br><br> Dans les exemples ci-dessous, nous allons interroger `GET http://<service-endpoint.com>/recommendations? ser_id=user123` point de terminaison avec un paramètre `user_id` qui retournera une liste des éléments recommandés :

```json
[
  {
    "id": "abc123",
    "url": "http://productpage. om/product/abc123",
    "name": "First Item",
    "price": 39.99,
    "image": "http://pp.cdn. om/abvh3321pjb1j"
  },
  {
    "id": "xyz987",
    "url": "http://productpage. om/product/xyz987",
    "name": "Great Item",
    "price": 19. 9,
    "image": "http://pp.cdn.com/234bjl1gioj1b2b"
  },
...
]
```

Dans le tableau de bord Braze, créez une nouvelle [campagne de Carte de Contenu]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/). Dans le champ texte du message, créez un bloc Liquid de contenu connecté pour interroger l'API et enregistrer la réponse dans la variable `recommendations`:

{% raw %}

```liquid
{% connected_content https:/<service-endpoint.com>/recommendations?user_id={{${user_id}}} :save recommendations %}
```

Vous pouvez ensuite référencer le premier élément du tableau résultant et afficher le contenu à l'utilisateur :

```liquid
Cela semble être parfait pour vous :
{% recommandations[0].name %}
{% recommandations[0].price %}
```

{% endraw %}

En incluant le titre, l'image et le lien de l'URL, c'est à quoi ressemblerait la fiche de contenu complète :

!\[Campagne personnalisée\]\[2\]
[2]: {% image_buster /assets/img/文_personalize/content-card-campaign.png %} [3]: {% image_buster /assets/img/s3.amazonaws.com/_personalize/min_and_max_user_percentile.png %}

[1]: {{site.baseurl}}/partners/message_personalization/dynamic_content/amazon_personalize/workshop/#step-3-send-personalized-emails-from-braze