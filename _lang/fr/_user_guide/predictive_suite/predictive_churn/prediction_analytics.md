---
nav_title: Analyses prédictives
article_title: Analyses prédictives
description: "Le présent article de référence couvre les différents composants inclus dans la page d’analyse prédictive de la prévision d’attrition et la manière dont ils peuvent être utilisés pour prendre des décisions pertinentes et motivées."
page_order: 2

---

# Analyses prédictives

> Une fois que votre prédiction a été construite et entraînée, vous aurez accès à la page Prediction Analytics (Analyse prédictive). Cette page vous aide à décider des utilisateurs que vous devez cibler en fonction de leur score de risque ou catégorie de Churn. 

Dès que l’entraînement de la prédiction est terminé et que cette page est renseignée, vous pouvez passer directement à l’utilisation de [filtres]({{site.baseurl}}/user_guide/predictive_suite/predictive_churn/messaging_users/#filters) dans les segments ou les campagnes pour commencer à utiliser les résultats du modèle. Mais, si vous voulez de l’aide pour décider qui cibler et pourquoi, cette page peut le faire en fonction de l’exactitude historique du modèle et de vos propres objectifs commerciaux. 

**Composants analytiques**<br>
&#45; [Score et catégorie de Churn](#churn_score)<br>
&#45; [Qualité de prédiction](#prediction_quality)<br>
&#45; [Résultats estimés](#estimated_results)<br>
&#45; [Tableau de corrélation de Churn](#correlation_table)

## Aperçu

La distribution des scores pour l’audience de prédiction toute entière s’affiche en haut de la page dans un graphique que vous pouvez afficher, par catégorie ou par score. Les utilisateurs dans les barres de droite ont des scores plus élevés et sont plus susceptibles d’abandonner. Les utilisateurs dans les barres plus à gauche sont moins susceptibles d’abandonner. Le curseur sous le graphique vous permet de sélectionner un groupe d’utilisateurs et d’estimer quel résultat aurait le ciblage des utilisateurs dans la plage sélectionnée du score de risque ou de la catégorie de Churn.

![][4]{: style="max-width:90%"}

Au fur et à mesure que vous déplacez le curseur, la barre située à gauche du volet inférieur vous indiquera combien d’utilisateurs de l’audience de prédiction entière seraient ciblés.

## Score et catégorie d’attrition {#churn_score}

Les utilisateurs de l’audience de prédiction recevront un score de Churn compris entre 0 et 100. Plus le score est élevé, plus la probabilité d’attrition est grande. 
- Les utilisateurs avec des scores de Churn compris entre 0 et 50 seront étiquetés dans la catégorie « Risque faible de Churn ». 
- Les utilisateurs ayant des scores compris entre 50 et 75 ainsi que 75 et 100 seront étiquetés respectivement dans les catégories de risque moyen et élevé de Churn. 

Les scores et les catégories correspondantes seront mis à jour conformément à la planification que vous avez choisie sur la page de création du modèle. Le nombre d’utilisateurs avec des scores Churn dans chacun des 20 compartiments de taille égale s’affiche dans le graphique en haut de la page. Cela peut vous aider à déterminer ce à quoi ressemble le risque d’attrition sur la population selon cette prédiction.

## Cibler des utilisateurs pour réduire l’attrition

### Qualité de prédiction {#prediction_quality}

Pour mesurer la précision de votre modèle, l’indicateur de **Qualité de prédiction** vous montrera l’efficacité de ce modèle de machine learning particulier lorsqu’il est testé sur des données historiques. Consultez ce document pour en savoir plus sur ce qui joue sur la [Qualité de prédiction]({{site.baseurl}}/user_guide/predictive_suite/predictive_churn/prediction_analytics/prediction_quality/).

Voici ce que nous recommandons pour diverses plages de qualité de prédiction :

| Plage de qualité de prédiction ( %) | Recommandation |
| ---------------------- | -------------- |
| 60 à 100 | Excellent. Précision supérieure. La modification des définitions d’audience est peu susceptible de fournir un avantage supplémentaire. |
| 40 à 60 | Bon. Ce modèle produira des prédictions précises, mais essayer différents paramètres d’audience peut obtenir de meilleurs résultats. |
| 20 à 40| Juste. Ce modèle peut fournir une précision et une valeur, mais envisagez d’essayer différentes définitions d’audience pour voir si elles augmentent les performances. |
| 0 à 20 | Faible. Nous vous recommandons de modifier les définitions de votre audience et de réessayer. |
{: .reset-td-br-1 .reset-td-br-2}

La prédiction sera entraînée à nouveau toutes les deux semaines et mise à jour en même temps que l’indicateur de qualité de prédiction afin de maintenir vos prédictions actualisées sur les schémas les plus récents de comportement des utilisateurs. La date du dernier entraînement sera affichée sur la page de liste des prédictions ainsi que sur votre page d’analyses prédictives.

## Résultats estimés {#estimated_results}

![][6]{: style="float:right;max-width:30%;margin-left:15px;"}

Dans la partie droite du volet en dessous du graphique, nous montrons les estimations de la précision attendue du ciblage de ce groupe de l’audience de prédiction. Sur la base des données passées concernant les utilisateurs dans l’audience de prédiction et la précision apparente du modèle au sujet de la séparation entre les utilisateurs susceptibles ou non d’abandonner, ces barres de progression prévoient l’éventuel message futur en utilisant l’audience mise en évidence avec le curseur :

1. Une estimation du nombre de personnes susceptibles d’abandonner qui seront correctement ciblées <br><br> Bien sûr, nous ne connaissons pas parfaitement l’avenir, donc nous ne savons pas précisément quels utilisateurs de l’audience de prédiction abandonneront à l’avenir. Mais la prédiction est une déduction fiable. Sur la base des performances passées, cette barre de progression indique le nombre total de personnes susceptibles d’abandonner « réelles » ou « exactes » attendu au sein de l’audience de prédiction (sur la base sur les taux d’attrition précédents) et qui sera ciblé avec la sélection actuelle. Nous pensons que ce nombre d’utilisateur abandonnera si vous ne le ciblez pas avec un message supplémentaire ou inhabituel. <br><br>

2. Une estimation du nombre d’utilisateurs ciblés par erreur qui n’auraient pas réellement abandonné<br><br>Tous les modèles de machine learning font des erreurs. Il peut y avoir des utilisateurs dans votre sélection qui ont un score de risque de Churn élevé, mais qui ne finissent pas par abandonner. Ils n’abandonneront pas même si vous ne prenez aucune mesure. Ils seront de toute façon ciblés, donc il s’agit d’une erreur ou d’un « faux positif ». La largeur totale de cette deuxième barre de progression représente le nombre attendu d’utilisateurs qui n’abandonneront pas et la partie remplie est celle qui sera mal ciblée en raison de la position actuelle du curseur.

À l’aide de ces informations, nous vous encourageons à décider du nombre de personnes souhaitant abandonner que vous souhaitez capturer et du coût des faux positifs pour votre entreprise. Si vous envoyez une promotion de valeur, vous voudrez peut-être garder un minimum de ceux qui n’abandonneront pas dans votre ciblage tout en conservant le maximum d’abandons envisagés proposés par le modèle. Ou, si vous êtes moins sensible aux faux positifs et aux utilisateurs recevant des messages supplémentaires, vous pouvez envoyer un message à une audience plus importante afin de capturer plus d’abandons envisagés et ignorer les erreurs probables.

## Tableau de corrélation d’attrition {#correlation_table}

Cette analyse affiche tous les attributs ou comportements d’utilisateur qui sont corrélés avec l’attrition de l’utilisateur dans l’audience de prédiction historique. Les tableaux sont divisés avec une partie gauche et droite correspondant respectivement à « plus » et « moins » susceptibles d’abandonner. Pour chaque ligne, le rapport indiquant si les utilisateurs ayant cet attribut de comportement dans la colonne de gauche sont plus ou moins susceptibles d’abandonner s’affiche dans la colonne de droite. Ce nombre est le rapport entre la probabilité d’attrition des utilisateurs ayant ce comportement ou l’attribut divisé par la probabilité d’attrition au sein de l’ensemble de l’audience de prédiction.

Ce tableau est mis à jour uniquement lorsque la prédiction est entraînée à nouveau et non lorsque les scores de risque de Churn de l’utilisateur sont mis à jour.

{% alert note %}
Les données de corrélation pour les Prévisualisation de prédictions seront partiellement masquées. Un achat est requis pour révéler ces informations. Contactez votre gestionnaire de compte pour plus d’informations.
{% endalert %}

[6]: {% image_buster /assets/img/churn/churnEstimatedResults.png %}
[4]: {% image_buster /assets/img/churn/churnTargeting.gif %}