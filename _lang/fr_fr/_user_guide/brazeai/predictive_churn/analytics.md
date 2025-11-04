---
nav_title: Analyse/analytique du désabonnement (si utilisé)
article_title: "Analyses prédictives du désabonnement (if used an anjective taux d'attrition)"
description: "Cet article de référence couvre les différents composants inclus dans la page Analyses prédictives du taux d'attrition (et la façon dont ils peuvent être utilisés pour prendre des informations adjectives)."
page_order: 1.5

---

# Analyses prédictives du désabonnement (if used an anjective)

> Une fois que votre prédiction a été créée et entraînée, vous avez accès à la page **Analyses prédictives**. Cette page vous aide à décider quels utilisateurs vous devez cibler en fonction de leur _score de risque de désabonnement_ ou de leur catégorie. 

## A propos des analyses prédictives du désabonnement (si utilisées comme analyses prédictives du taux d'attrition)

Dès que la prédiction est terminée et que cette page est remplie, vous pouvez passer à l'utilisation des [filtres]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/messaging_users/#filters) dans les segments ou les campagnes pour commencer à utiliser les résultats du modèle. Toutefois, si vous souhaitez obtenir de l'aide pour décider qui cibler et pourquoi, cette page peut vous aider en fonction de l'exactitude historique du modèle et de vos propres objectifs métier. 

Telles sont les composantes de l'analyse/analyse prédictive du désabonnement (qui constituent l'analyse prévisionnelle du taux d'attrition) :

- [Score et catégorie de désabonnement](#churn_score)
- [Qualité des prédictions](#prediction_quality)
- [Précision estimée](#estimated_results)
- [Tableau de corrélation du désabonnement](#correlation_table)

La répartition des scores pour l'ensemble de l'audience des prédictions est affichée en haut de la page dans un graphique que vous pouvez consulter, par catégorie ou par score. Les utilisateurs des bacs situés plus à droite ont des scores plus élevés et sont plus susceptibles de se désabonner. Les utilisateurs désabonnés dans les bacs situés plus à gauche sont moins susceptibles de désabonner. Le curseur situé sous le graphique vous permet de sélectionner un groupe d'utilisateurs et d'estimer les résultats du ciblage des utilisateurs se situant dans la fourchette sélectionnée du _score de risque de désabonnement_ ou de la catégorie.

Au fur et à mesure que vous déplacez le curseur, la barre située dans la moitié gauche du panneau inférieur vous informe du nombre d'utilisateurs ciblés sur l'ensemble de l'audience de prédictions.

\![]({% image_buster /assets/img/churn/churnTargeting.gif %})

## Score et catégorie de désabonnement {#churn_score}

Les utilisateurs de l'audience de prédiction se verront attribuer un _score de risque de désabonnement_ compris entre 0 et 100. Plus le score est élevé, plus la probabilité de désabonner est grande. 
- Les utilisateurs dont le score est compris entre 0 et 50 seront classés dans la catégorie " _faible risque"_. 
- Les utilisateurs dont le score est compris entre 50 et 75, et entre 75 et 100, seront étiquetés respectivement dans les catégories _Risque moyen_ et _Risque élevé._  

Les notes et les catégories correspondantes seront mises à jour selon la planification que vous avez choisie sur la page de création du modèle. Le nombre d'utilisateurs désabonnés dans chacun des 20 compartiments de taille égale est affiché dans le graphique en haut de la page. Cela peut vous aider à déterminer le risque de désabonnement au sein de la population en fonction de cette prédiction.

## Qualité des prédictions {#prediction_quality}

{% multi_lang_include brazeai/predictive_suite/prediction_quality.md %}

## Précision estimée {#estimated_results}

Dans la moitié droite du panneau situé sous le graphique, nous présentons des estimations de la précision attendue du ciblage de cette partie de l'audience des prédictions. Sur la base des données relatives aux utilisateurs de l'audience prédite dans le passé et de la précision apparente du modèle pour distinguer les utilisateurs qui se désabonnent de ceux qui ne se désabonnent pas sur la base de ces données passées, ces barres de progression permettent d'estimer un futur message potentiel utilisant l'audience mise en évidence par le curseur :

\![]({% image_buster /assets/img/churn/churnEstimatedResults.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

- Combien d'utilisateurs désabonnés sont susceptibles de désabonner ?
- Combien d'utilisateurs désabonnés sont censés **ne pas** désabonner ?

À l'aide de ces informations, nous vous encourageons à décider du nombre de désabonnés que vous souhaitez capturer et du coût d'une erreur faussement positive pour votre entreprise. Si vous envoyez une promotion de grande valeur, vous voudrez peut-être limiter au maximum le ciblage des non-désabonnés tout en obtenant autant de vrais désabonnés que le modèle le permet. Ou, si vous êtes moins sensible aux faux positifs et que les utilisateurs reçoivent des messages supplémentaires, vous pouvez envoyer des messages à une plus grande partie de l'audience pour capter davantage de désabonnés attendus et ignorer les erreurs probables.

### On s'attend à ce que les utilisateurs désabonnent

Il s'agit d'une estimation du nombre de désabonnés réels qui seront correctement ciblés. Bien entendu, nous ne connaissons pas parfaitement l'avenir, et nous ne savons donc pas précisément quels utilisateurs de l'audience de prédiction se désabonneront à l'avenir. Mais la prédiction est une déduction fiable. Sur la base des performances passées, cette barre de progression indique le nombre de désabonnés "réels" ou "vrais" attendus dans l'audience de prédiction (sur la base des taux d'attrition antérieurs) qui seront ciblés avec la sélection de ciblage actuelle. On peut s'attendre à ce que ce nombre d'utilisateurs se désabonne si vous ne les ciblez pas avec des messages supplémentaires ou inhabituels.

### On s'attend à ce que les utilisateurs ne se désabonnent pas. 

Il s'agit d'une estimation du nombre d'utilisateurs qui n'auraient pas désabonné et qui seront incorrectement ciblés. Tous les modèles de machine learning font des erreurs. Il peut y avoir des utilisateurs dans votre sélection qui ont un _score de risque de désabonnement_ élevé mais qui ne se désabonnent pas en fin de compte. Ils ne se désabonneraient pas même si vous ne preniez aucune mesure. Ils seront de toute façon ciblés, il s'agit donc d'une erreur ou d'un "faux positif". La largeur totale de cette deuxième barre de progression représente le nombre attendu d'utilisateurs qui ne se désabonneront pas, et la partie remplie représente ceux qui seront incorrectement ciblés en utilisant la position actuelle du curseur.

## Tableau de corrélation du désabonnement {#correlation_table}

Cette analyse affiche tous les attributs ou comportements des utilisateurs qui sont en corrélation avec le désabonnement des utilisateurs dans l'audience de prédiction historique. Les tableaux sont divisés en deux parties, gauche et droite, respectivement pour les personnes les plus et les moins susceptibles de désabonner. Pour chaque ligne, le ratio par lequel les utilisateurs ayant le comportement ou l'attribut dans la colonne de gauche sont plus ou moins susceptibles de désabonner est affiché dans la colonne de droite. Ce chiffre est le rapport entre la probabilité de désabonner les utilisateurs ayant ce comportement ou cet attribut et la probabilité de désabonner l'ensemble de l'audience de prédiction.

Ce tableau n'est mis à jour que lorsque la prédiction se _désabonne_ et non lorsque les _scores de risque de désabonnement des_ utilisateurs sont mis à jour.

{% alert note %}
Les données de corrélation pour les prédictions seront partiellement cachées. Un achat est nécessaire pour révéler ces informations. Contactez votre gestionnaire de compte pour plus d'informations.
{% endalert %}
