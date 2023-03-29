---
nav_title: Amazon Personalize
article_title: Amazon Personalize
alias: /partners/amazon_personalize/
description: "Cet article de référence présente une architecture de référence pour l’intégration entre Braze et Amazon Personalize. Cet article de référence vous aidera à comprendre les exemples d’utilisation proposés par Amazon Personalize, les données qu’il contient, comment configurer le service et comment intégrer ce dernier à Braze."
page_type: partner
search_tag: Partenaire
---

# Amazon Personalize
<!--
{% multi_lang_include video.html id="xFZ3HMleYYE" align="right" %}
-->
> Amazon Personalize c’est comme avoir un système personnel de recommandation de machine learning d’Amazon. Avec ses 20 ans et plus d’expérience en recommandation, Amazon Personalize vous permet d’améliorer l’engagement client en mettant en œuvre des recommandations personnalisées en temps réel sur les produits et le contenu et les promotions marketing ciblées.

Grâce au machine learning et à un algorithme que vous contribuez à définir, Amazon Personalize peut vous aider à former un modèle qui émet des recommandations de haute qualité pour vos sites Web et applications. Ces modèles vous permettront de créer des listes de recommandations basées sur les comportements passés des utilisateurs, de trier les articles par pertinence et de recommander d’autres articles en fonction de la similarité. Les listes obtenues à partir de l’API Amazon Personalize peuvent alors être utilisées dans le Contenu connecté de Braze pour exécuter des campagnes de recommandation Braze personnalisées. En intégrant Amazon Personalize, les clients ont la liberté de contrôler les paramètres utilisés pour former les modèles et définir les objectifs commerciaux facultatifs qui optimisent la sortie de l’algorithme. 

Cet article de référence vous aidera à comprendre les exemples d’utilisation proposés par Amazon Personalize, les données qu’il contient, comment configurer le service et comment intégrer ce dernier à Braze.

## Conditions préalables

| Condition| Description|
| ---| ---| 
| Compte Amazon Web Service | Un compte AWS est requis pour profiter de ce partenariat. Une fois que vous avez un compte AWS, vous pouvez accéder à Amazon Personalize via la console Amazon Personalize, l’interface de ligne de commande AWS (AWS CLI) ou les SDK AWS. |
| Cas d’utilisation définis | Avant de créer un modèle, vous devez déterminer votre cas d’utilisation pour cette intégration. Consultez la liste suivante pour les cas d’utilisation courants. |
| Jeux de données | Les modèles de recommandation Amazon Personalize nécessitent trois types différents de jeux de données, d’interactions, d’utilisateurs et d’articles. Reportez-vous aux détails suivants pour voir les exigences de chaque jeu de données. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

{% tabs %}
{% tab Use Cases %}

**Cas d’utilisation**

Avant de créer un modèle, vous devez déterminer votre cas d’utilisation pour cette intégration. Parmi les cas d’utilisation courants figurent les situations suivantes :
- Recommander des articles pour les utilisateurs en fonction de leurs interactions précédentes, créant une expérience réellement personnalisée pour vos utilisateurs.
- Fournir une liste d’articles ou de résultats de recherche adaptés à chaque utilisateur, augmentant l’engagement en affichant des articles par pertinence à l’utilisateur.
- Trouver des recommandations pour des articles similaires, aidant les utilisateurs à découvrir de nouvelles choses.

Dans le guide suivant, nous allons nous concentrer sur la recette des recommandations personnalisées de l’utilisateur.

{% endtab %}
{% tab Datasets %}

**Jeux de données**

Pour commencer avec les modèles de recommandation Amazon Personalize, vous avez besoin de trois types de jeux de données :

- Interactions
  - Stocke l’historique des interactions entre les utilisateurs et les articles
  - Nécessite les valeurs `USER_ID`, `ITEM_ID`, `EVENT_TYPE` et `TIMESTAMP`, et accepte éventuellement les métadonnées sur l’événement
- Utilisateurs
  - Stocke les métadonnées sur les utilisateurs
  - Nécessite valeur `USER_ID` et au moins un champ de métadonnées (chaîne de caractères ou numérique), comme le sexe, l’âge, la fidélité
- Articles
  - Stocke les métadonnées sur les articles
  - Nécessite une valeur `ITEM_ID` et au moins un champ de métadonnées (texturé, catégorique ou numérique) qui décrit l’article

Pour une recette de recommandations d’utilisateur, vous devez fournir un jeu de données d’interactions contenant au moins 1 000 points de données d’interaction d’au moins 25 utilisateurs uniques avec au moins deux interactions chacun. Ces jeux de données peuvent être téléchargés en vrac en utilisant des fichiers CSV stockés dans S3 ou incrémentés par l’API.

{% endtab %}
{% endtabs %}

## Création de modèles

### Étape 1 : Formation

Une fois les jeux de données importés, vous pouvez créer une solution. Une solution utilise l’une des [recettes](https://docs.aws.amazon.com/personalize/latest/dg/working-with-predefined-recipes.html) (algorithmes) Amazon Personalize pour former un modèle. Dans notre cas, nous utiliserons la recette `USER_PERSONALIZATION`. La formation de la solution crée une version de solution (modèle formé) que vous pouvez évaluer en fonction des indicateurs de performance du modèle.

Amazon Personalize vous permet d’ajuster les hyperparamètres que le modèle utilise pour la formation. Par exemple :
- Le paramètre « User history length percentile » (Centile de longueur de l’historique de l’utilisateur) trouvé dans la console Amazon Personalize vous permet d’ajuster le centile de l’historique de l’utilisateur à inclure dans la formation :<br><br>![Paramètre min max du profil utilisateur][3]
  - `min_user_history_length_percentile` : exclut un pourcentage d’utilisateurs ayant des longueurs d’historiques très courtes, ce qui peut être utile pour éliminer les articles populaires et créer des recommandations basées sur des modèles sous-jacents plus profonds.
  - `max_user_history_length_percentile` : règle le pourcentage d’utilisateurs à prendre en compte lors de la formation avec de très longs historiques.

Le nombre de dimensions masquées permet de détecter des modèles plus compliqués pour les jeux de données complexes, tandis que la technique de propagation du temps (BPTT) ajuste les récompenses pour un événement précoce après qu’une chaîne d’événements a eu lieu, ce qui a entraîné une action de valeur élevée.

En outre, Amazon Personalize offre un réglage automatique des hyperparamètres en exécutant plusieurs versions de la solution avec différentes valeurs simultanément. Pour utiliser le réglage, activez **Exécuter HPO** lors de la création d’une solution.

### Étape 2 : Évaluer et comparer

Une fois qu’une solution a terminé la formation, vous êtes prêt à l’évaluer et à comparer différentes versions. Chaque version de solution affiche les indicateurs calculés. Parmi les indicateurs disponibles, citons :

- `Normalize discounted cumulative gain` : compare l’ordre recommandé des articles à la liste des articles réels et donne à chaque article un poids correspondant à sa position dans la liste
- `Precision @k` : la quantité d’articles recommandés correctement divisée par le montant de tous les articles recommandés, où `k` est le nombre d’articles
- `Mean reciprocal rank` : se concentre sur la première recommandation, la plus élevée classée et calcule le nombre d’articles recommandés avant que la première recommandation correspondante apparaisse
- `Coverage` : compare la proportion d’éléments uniques recommandés au nombre total d’éléments uniques dans le jeu de données

## Obtenir des recommandations

Une fois que vous avez créé une version de solution qui vous satisfait, il est temps de mettre les recommandations en pratique. Il existe deux façons d’accéder aux recommandations :

1. Campagne en temps réel<br>Une campagne est une version de solution déployée avec un débit de transaction minimum défini. Une transaction est un appel API unique pour obtenir une sortie de recommandation, et elle est définie comme TPS, ou transactions par seconde, avec une valeur minimale d’un. La campagne va mettre à l’échelle les ressources en cas de charge accrue, mais elle ne chutera pas sous votre valeur minimale. Vous pouvez interroger les recommandations de la console, de la CLI AWS ou des SDK AWS dans votre code.<br><br>
2. Traitement par lot<br>Un traitement par lot exporte les recommandations vers un compartiment S3. Le traitement sélectionne une entrée d’un fichier JSON avec une liste d’ID utilisateur pour lesquels vous souhaitez exporter les recommandations. Ensuite, après avoir spécifié les autorisations correctes et la destination de sortie, vous êtes prêt à exécuter le travail. L’exécution dépend de la taille de vos jeux de données et de la longueur de la liste des recommandations.

### Filtres

Les filtres vous permettent d’ajuster la sortie de la recommandation en excluant les éléments en fonction de l’ID, du type d’événement ou des métadonnées de l’article. Vous pouvez également filtrer les utilisateurs en fonction de leurs métadonnées, telles que l’âge ou l’état de fidélité. Les filtres peuvent être pratiques pour éviter de recommander des articles avec lesquels l’utilisateur a déjà interagi.

## Intégration des résultats à Braze

Avec le modèle et la campagne de recommandations créés, vous êtes prêt à exécuter une campagne Braze pour vos utilisateurs utilisant les Cartes de contenu et le Contenu connecté.
Avant d’exécuter une campagne Braze, vous devez créer un service qui peut transmettre ces recommandations via une API. Vous pouvez suivre [l’étape 3 de l’article de l’atelier][1] pour déployer le service en utilisant les services AWS. Vous pouvez également déployer votre propre service de back-end indépendant qui fournit les recommandations.

### Exemple de Campagne de cartes de contenu

Lançons une Campagne de cartes de contenu avec le premier article recommandé de la liste.<br><br>
Dans les exemples suivants, nous allons interroger
l’endpoint `GET http://<service-endpoint.com>/recommendations?user_id=user123` avec paramètre `user_id` qui renvoie une liste des articles recommandés :

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

Dans le tableau de bord de Braze, créez une nouvelle [Campagne de cartes de contenu]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/). Dans le champ de texte du message, créez un bloc Contenu connecté Liquid pour interroger l’API et enregistrer la réponse dans la variable `recommendations` :

{% raw %}

```liquid
{% connected_content https:/<service-endpoint.com>/recommendations?user_id={{${user_id}}} :save recommendations %}
```

Vous pouvez ensuite référencer le premier élément dans la matrice résultante et afficher le contenu à l’utilisateur :

```liquid
This seems like a great fit for you:
{% recommendations[0].name %}
{% recommendations[0].price %}
```

{% endraw %}

Y compris le titre, l’image et la liaison de l’URL, voilà ce à quoi ressemblerait l’intégralité de la Carte de contenu :

![Image d’une campagne avec Contenu connecté ajoutée au corps du message et au champ « Add Image » (Ajouter une image). Cette image montre également la logique du Contenu connecté ajoutée au champ « Redirect to Web URL » (Redirection vers URL Web), reliant les utilisateurs à une URL de recommandation.][2]

[1]: {{site.baseurl}}/partners/message_personalization/dynamic_content/amazon_personalize/workshop/#step-3-send-personalized-emails-from-braze
[2]: {% image_buster /assets/img/amazon_personalize/content-card-campaign.png %}
[3]: {% image_buster /assets/img/amazon_personalize/min_and_max_user_percentile.png %}