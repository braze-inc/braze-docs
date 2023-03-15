---
nav_title: Analyses prédictives
article_title: Analyses prédictives
description: "Le présent article de référence couvre les différents composants inclus dans la page d’analyse des achats prédictifs et la manière dont ils peuvent être utilisés pour prendre des décisions pertinentes et motivées."
page_order: 2

---

# Analyses prédictives

Une fois que votre prédiction a été construite et entraînée, vous aurez accès à la page **Prediction Analytics (Analyse prédictive)**. Cette page vous aide à décider des utilisateurs que vous devez cibler en fonction de leur score de risque ou catégorie de probabilité d’achat. Dès que l’entraînement de la prédiction est terminé et que cette page est renseignée, vous pouvez passer directement à l’utilisation de [filtres]({{site.baseurl}}/user_guide/predictive_suite/predictive_churn/messaging_users/#filters) dans les segments ou les campagnes pour commencer à utiliser les résultats du modèle. Si vous voulez de l’aide pour décider qui cibler et pourquoi, cette page peut le faire en fonction de l’exactitude historique du modèle et de vos propres objectifs commerciaux. 

**Composants analytiques**<br>
&#45; [Score de probabilité d’achat](#purchase_score)<br>
&#45; [Ciblage des utilisateurs](#target_users)<br>
&#45; [Qualité de prédiction](#prediction_quality)<br>
&#45; [Résultats estimés](#estimated_results)<br>
&#45; [Tableau de corrélation d’achat](#correlation_table)

## Score de probabilité d’achat {#purchase_score}

Les utilisateurs de l’audience de prédiction recevront un score de probabilité d’achat compris entre 0 et 100. Plus le score est élevé, plus la probabilité d’’achat est grande.

- Les utilisateurs avec des scores de probabilité d’achat compris entre 0 et 50 seront étiquetés dans la catégorie « Faible ». 
- Les utilisateurs ayant des scores compris entre 50 et 75 ainsi que 75 et 100 seront étiquetés respectivement dans les catégories de probabilité moyenne et élevée. 

Les scores et les catégories correspondantes seront mis à jour conformément à la planification que vous avez choisie sur la page de **Prediction Creation (Création de la prédiction)**. Le nombre d’utilisateurs avec des scores de probabilité d’achat dans chacun des 20 compartiments de taille égale ou dans chacune des catégories de probabilité d’achat est affiché dans le graphique en haut de la page.

## Segmentation d’audience {#target_users}

La distribution des scores de probabilité d’achat pour l’audience de prédiction toute entière s’affiche en haut de la page. Les utilisateurs dans les compartiments de droite ont des scores plus élevés et sont plus susceptibles d’acheter. Les utilisateurs dans les compartiments plus à gauche sont moins susceptibles d’acheter. Le curseur sous le graphique vous permet de sélectionner un groupe d’utilisateurs et d’estimer quel résultat aurait le ciblage de ces utilisateurs.

![][4]{: style="max-width:90%"} 

Au fur et à mesure que vous déplacez le curseur d’une position à l’autre, la barre située à gauche du volet vous indiquera combien d’utilisateurs de l’audience de prédiction entière seraient ciblés en utilisant la part de population que vous avez sélectionnée.

### Résultats estimés {#estimated_results}

![][6]

Dans la partie droite du volet en dessous du graphique, nous montrons les estimations de la précision attendue du ciblage de ce groupe de l’audience de prédiction que vous avez sélectionnée de deux manières :

1. Combien d’utilisateurs sélectionnés sont censés acheter<br><br> La prédiction n’est pas parfaitement précise et aucune prédiction ne l’est jamais, ce qui signifie que Braze ne sera pas en mesure d’identifier tous les futurs acheteurs. Les scores de probabilité sont comme un ensemble de prédictions informées et fiables. La barre de progression indique le nombre d’acheteurs « réels » ou « vrais » attendus dans l’audience de prédiction seront ciblés avec l’audience sélectionnée. Notez que nous nous attendons à ce que ce groupe d’utilisateurs achète même si vous ne leur envoyez pas un message. <br><br>

2. Combien d’utilisateurs sélectionnés sont censés ne pas acheter<br><br>Tous les modèles de machine learning font des erreurs. Il peut y avoir des utilisateurs dans votre sélection qui ont un score de probabilité d’achat élevé mais qui, au final, ne réaliseront pas d’achat. Ils n’en feraient pas si vous ne preniez aucune mesure. Ils seront de toute façon ciblés, donc il s’agit d’une erreur ou d’un « faux positif ». La largeur totale de cette deuxième barre de progression représente le nombre attendu d’utilisateurs qui n’achèteront pas et la partie remplie est celle qui sera mal ciblée en raison de la position actuelle du curseur.

À l’aide de ces informations, nous vous encourageons à décider du nombre d’acheteurs que vous souhaitez capturer, du nombre d’utilisateurs qui ne sont pas des acheteurs que vous pouvez accepter de cibler quand même et de ce que les erreurs coûtent à votre entreprise. Si vous envoyez une promotion de valeur, vous pouvez cibler uniquement les non acheteurs en privilégiant le côté gauche du tableau. Vous pouvez également encourager les acheteurs qui achètent souvent à le faire à nouveau en sélectionnant un groupe d’utilisateurs sur le côté droit du tableau.

### Qualité de prédiction {#prediction_quality}

Pour mesurer la précision de votre modèle, l’indicateur de **Qualité de prédiction** vous montrera l’efficacité apparente de ce modèle de machine learning particulier. Il s’agit essentiellement d’une mesure de l’efficacité de cette prédiction pour distinguer les acheteurs des non-acheteurs. Une qualité de prédiction de 100 signifie qu’elle détermine parfaitement qui va ou ne va pas acheter sans erreur (cela ne se produit jamais !) et 0 signifie que c’est une estimation aléatoire. Consultez ce document pour en savoir plus sur ce qui joue sur la [Qualité de prédiction]({{site.baseurl}}/user_guide/predictive_suite/predictive_churn/prediction_analytics/prediction_quality/).

Voici ce que nous recommandons pour diverses plages de qualité de prédiction :

| Plage de qualité de prédiction ( %) | Recommandation |
| ---------------------- | -------------- |
| 60 à 100 | Excellent. Précision supérieure. La modification des définitions d’audience est peu susceptible de fournir un avantage supplémentaire. |
| 40 à 60 | Bon. Ce modèle produira des prédictions précises, mais essayer différents paramètres d’audience peut obtenir de meilleurs résultats. |
| 20 à 40| Juste. Ce modèle peut fournir une précision et une valeur, mais envisagez d’essayer différentes définitions d’audience pour voir si elles augmentent les performances. |
| 0 à 20 | Faible. Nous vous recommandons de modifier les définitions de votre audience et de réessayer. |
{: .reset-td-br-1 .reset-td-br-2}

La prédiction sera entraînée à nouveau toutes les deux semaines et mise à jour en même temps que l’indicateur de qualité de prédiction afin de maintenir vos prédictions actualisées sur les schémas les plus récents de comportement des utilisateurs. La date du dernier entraînement sera affichée sur la page de liste des prédictions ainsi que sur votre page d’analyses prédictives. 

Lorsqu’une prédiction est créée pour la première fois, la qualité de prédiction sera basée sur les données historiques demandées lorsque vous cliquez sur **Build Prediction (Construire la prédiction).** Toutes les deux semaines, la qualité de prédiction est obtenue en comparant les scores de prédiction aux résultats réels.

## Tableau de corrélation d’achat {#correlation_table}

Cette analyse affiche les attributs ou comportements d’utilisateur qui sont corrélés avec les achats dans l’audience de prédiction. Les attributs évalués sont l’âge, le pays, le sexe et la langue. Les comportements analysés comprennent les sessions, les achats, le total dépensé en dollars, les événements personnalisés et les campagnes et Canvas steps reçus au cours des 30 derniers jours. Les tableaux sont divisés avec une partie gauche et droite correspondant respectivement à « plus » et « moins » susceptibles d’acheter. Pour chaque ligne, le rapport indiquant si les utilisateurs ayant cet attribut de comportement dans la colonne de gauche sont plus ou moins susceptibles d’acheter s’affiche dans la colonne de droite. Ce nombre est le rapport entre la probabilité d’achat des utilisateurs ayant ce comportement ou l’attribut divisé par la probabilité d’achat au sein de l’ensemble de l’audience de prédiction.

Ce tableau est mis à jour uniquement lorsque la prédiction est entraînée à nouveau et non lorsque les scores de probabilité d’achat de l’utilisateur sont mis à jour.

{% alert note %}
Les données de corrélation pour les Prévisualisation de prédictions seront partiellement masquées. Un achat est requis pour révéler ces informations. Contactez votre gestionnaire de compte pour plus d’informations.
{% endalert %}

[6]: {% image_buster /assets/img/purchasePrediction/purchaseEstimatedResults.png %}
[4]: {% image_buster /assets/img/purchasePrediction/purchaseTargeting.png %}