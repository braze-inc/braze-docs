---
nav_title: Analyse/analytique du désabonnement (si utilisé)
article_title: "Analyses prédictives du désabonnement (if used an anjective taux d'attrition)"
description: "Cet article de référence couvre les différents composants inclus dans la page Analyses prédictives du taux d'attrition (et la façon dont ils peuvent être utilisés pour prendre des informations adjectives)."
page_order: 1.5

---

# Analyses prédictives du désabonnement (if used an anjective)

> Une fois que votre prédiction a été créée et entraînée, vous avez accès à la page **Analyses prédictives**. Cette page vous aide à décider quels utilisateurs vous devez cibler en fonction de leur _score de risque de désabonnement_ ou de leur catégorie. 

## A propos des analyses prédictives du désabonnement (si utilisées comme analyses prédictives du taux d'attrition)

Dès que la prédiction est terminée et que cette page est remplie, vous pouvez passer à l'utilisation des [filtres]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/messaging_users/#filters) dans les segments ou les campagnes pour commencer à utiliser les résultats du modèle. Mais, si vous voulez de l’aide pour décider qui cibler et pourquoi, cette page peut le faire en fonction de l’exactitude historique du modèle et de vos propres objectifs commerciaux. 

Telles sont les composantes de l'analyse/analyse prédictive du désabonnement (qui constituent l'analyse prévisionnelle du taux d'attrition) :

- [Score et catégorie de désabonnement](#churn_score)
- [Qualité de prédiction](#prediction_quality)
- [Précision estimée](#estimated_results)
- [Tableau de corrélation du désabonnement](#correlation_table)

La répartition des scores pour l'ensemble de l'audience des prédictions est affichée en haut de la page dans un graphique que vous pouvez consulter, par catégorie ou par score. Les utilisateurs dans les barres de droite ont des scores plus élevés et sont plus susceptibles d’abandonner. Les utilisateurs dans les barres plus à gauche sont moins susceptibles d’abandonner. Le curseur situé sous le graphique vous permet de sélectionner un groupe d'utilisateurs et d'estimer les résultats du ciblage des utilisateurs se situant dans la fourchette sélectionnée du _score de risque de désabonnement_ ou de la catégorie.

Au fur et à mesure que vous déplacez le curseur, la barre située dans la moitié gauche du panneau inférieur vous informe du nombre d'utilisateurs ciblés sur l'ensemble de l'audience de prédictions.

![]({% image_buster /assets/img/churn/churnTargeting.gif %})

## Score et catégorie d’attrition {#churn_score}

Les utilisateurs de l'audience de prédiction se verront attribuer un _score de risque de désabonnement_ compris entre 0 et 100. Plus le score est élevé, plus la probabilité d’attrition est grande. 
- Les utilisateurs dont le score est compris entre 0 et 50 seront classés dans la catégorie " _faible risque"._  
- Les utilisateurs dont le score est compris entre 50 et 75, et entre 75 et 100, seront étiquetés respectivement dans les catégories _Risque moyen_ et _Risque élevé._  

Les scores et les catégories correspondantes seront mis à jour conformément à la planification que vous avez choisie sur la page de création du modèle. Le nombre d’utilisateurs avec des scores d'attrition dans chacun des 20 compartiments de taille égale s’affiche dans le graphique en haut de la page. Cela peut vous aider à déterminer ce à quoi ressemble le risque d’attrition sur la population selon cette prédiction.

## Qualité des prédictions {#prediction_quality}

{% multi_lang_include brazeai/predictive_suite/prediction_quality.md %}

## Précision estimée {#estimated_results}

Dans la moitié droite du panneau situé sous le graphique, nous présentons des estimations de la précision attendue du ciblage de cette partie de l'audience des prédictions. Sur la base des données relatives aux utilisateurs de l'audience prédite dans le passé et de la précision apparente du modèle pour distinguer les utilisateurs qui se désabonnent de ceux qui ne se désabonnent pas sur la base de ces données passées, ces barres de progression permettent d'estimer un futur message potentiel utilisant l'audience mise en évidence par le curseur :

![]({% image_buster /assets/img/churn/churnEstimatedResults.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

- Combien d’utilisateurs sélectionnés sont censés se désabonner
- Combien d'utilisateurs désabonnés sont censés **ne pas** désabonner ?

À l’aide de ces informations, nous vous encourageons à décider du nombre de personnes souhaitant abandonner que vous souhaitez capturer et du coût des faux positifs pour votre entreprise. Si vous envoyez une promotion de valeur, vous voudrez peut-être garder un minimum de ceux qui n’abandonneront pas dans votre ciblage tout en conservant le maximum d’abandons envisagés proposés par le modèle. Ou, si vous êtes moins sensible aux faux positifs et aux utilisateurs recevant des messages supplémentaires, vous pouvez envoyer un message à une audience plus importante afin de capturer plus d’abandons envisagés et ignorer les erreurs probables.

### On s'attend à ce que les utilisateurs désabonnent

Il s'agit d'une estimation du nombre de désabonnés réels qui seront correctement ciblés. Bien entendu, nous ne connaissons pas parfaitement l'avenir, et nous ne savons donc pas précisément quels utilisateurs de l'audience de prédiction se désabonneront à l'avenir. Mais la prédiction est une déduction fiable. Sur la base des performances passées, cette barre de progression indique le nombre total « réel » ou « exact » de désabonnés attendus au sein de l’audience de prédiction (sur la base sur les taux d’attrition précédents) qui seront ciblés avec la sélection de reciblage actuelle. Nous pensons que ce nombre d’utilisateur abandonnera si vous ne le ciblez pas avec un message supplémentaire ou inhabituel.

### On s'attend à ce que les utilisateurs ne se désabonnent pas. 

Il s'agit d'une estimation du nombre d'utilisateurs qui n'auraient pas désabonné et qui seront incorrectement ciblés. Tous les modèles de machine learning font des erreurs. Il se peut que certains utilisateurs de votre sélection aient un _score de risque de désabonnement_ élevé, mais qu'ils ne se désabonnent pas pour autant. Ils n’abandonneront pas même si vous ne prenez aucune mesure. Ils seront de toute façon ciblés, donc il s’agit d’une erreur ou d’un « faux positif ». La largeur totale de cette deuxième barre de progression représente le nombre attendu d'utilisateurs qui ne se désabonneront pas, et la partie remplie représente ceux qui seront incorrectement ciblés en utilisant la position actuelle du curseur.

## Tableau de corrélation de l’attrition {#correlation_table}

Cette analyse affiche tous les attributs ou comportements des utilisateurs qui sont en corrélation avec le désabonnement des utilisateurs dans l'audience de prédiction historique. Les tableaux sont divisés avec une partie gauche et droite correspondant respectivement à « plus » et « moins » susceptibles d’abandonner. Pour chaque ligne, le rapport indiquant si les utilisateurs ayant cet attribut de comportement dans la colonne de gauche sont plus ou moins susceptibles d’abandonner s’affiche dans la colonne de droite. Ce chiffre est le rapport entre la probabilité d’attrition des utilisateurs ayant ce comportement ou cet attribut et la probabilité d’attrition de l'ensemble de l'audience de prédiction.

Ce tableau est uniquement mis à jour lorsque la prédiction est reconvertie et non lorsque les _scores de risque d’attrition_ des utilisateurs sont actualisés.

{% alert note %}
Les données de corrélation pour les aperçus de prédictions seront partiellement cachées. Un achat est requis pour révéler ces informations. Contactez votre gestionnaire de compte pour plus d’informations.
{% endalert %}
