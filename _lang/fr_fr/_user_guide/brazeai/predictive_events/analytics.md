---
nav_title: Analyse/analytique (si utilisée comme adjective)
article_title: Analyses prédictives (if used asjective)
description: "Cet article de référence présente les différents composants de la page Analyses prédictives/analytiques d'événements et explique comment ils peuvent être utilisés pour prendre des décisions fondées sur des informations."
page_order: 1.3

---

# Analyses prédictives (if used anjective)

> Une fois que votre prédiction a été créée et entraînée, vous avez accès à la page **Analyses prédictives**. Cette page vous aide à décider quels utilisateurs vous devez cibler en fonction de leur score de probabilité ou de leur catégorie.

## A propos de l'analyse prédictive/analytique (if used anjective)

Dès que la prédiction est terminée et que cette page est remplie, vous pouvez commencer à utiliser les [filtres]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/messaging_users/#filters) dans les segments ou les campagnes pour commencer à utiliser les résultats du modèle. Si vous voulez de l’aide pour décider qui cibler et pourquoi, cette page peut le faire en fonction de l’exactitude historique du modèle et de vos propres objectifs commerciaux.

Tels sont les éléments constitutifs de l'analyse/analytique prévisionnelle des événements :

- [Score de vraisemblance](#purchase_score)
- [Qualité de prédiction](#prediction_quality)
- [Précision estimée](#estimated_results)
- [Tableau de corrélation des événements](#correlation_table)

La distribution des scores de vraisemblance pour l'ensemble de l'audience de prédictions est affichée en haut de la page. Les utilisateurs des compartiments situés plus à droite ont des scores plus élevés et sont plus susceptibles de réaliser l'événement. Les utilisateurs des compartiments situés plus à gauche sont moins susceptibles d'effectuer l'événement. Le curseur situé sous le graphique vous permettra de sélectionner une section d'utilisateurs et d'estimer quels seraient les résultats du ciblage de ces utilisateurs.

Lorsque vous déplacez les curseurs sur différentes positions, la barre située dans la moitié gauche du panneau vous indique combien d'utilisateurs, sur l'ensemble de l'audience prédite, seraient ciblés en utilisant la partie de la population que vous avez sélectionnée.

![]({% image_buster /assets/img/purchasePrediction/purchaseTargeting.png %}){: style="max-width:90%"} 

## Score de vraisemblance {#purchase_score}

Les utilisateurs de l'audience de prédictions se verront attribuer un score de probabilité compris entre 0 et 100. Plus le score est élevé, plus la probabilité de réaliser l'événement est grande. 

Voici comment un utilisateur est classé en fonction de son score de probabilité :

- **Faible :** entre 0 et 50
- **Moyenne :** entre 50 et 75
- **Élevé :** entre 75 et 100

Les scores et les prédictions correspondantes seront mis à jour selon la planification que vous avez choisie dans la page de **création des prédictions**. Le nombre d'utilisateurs ayant des scores de vraisemblance dans chacun des 20 compartiments de taille égale ou dans chacune des catégories de vraisemblance est affiché dans le graphique en haut de la page.

## Précision estimée {#estimated_results}

Dans la moitié droite du panneau situé sous le graphique, nous présentons des estimations de la précision attendue du ciblage de la partie de l'audience de prédictions que vous avez sélectionnée de deux manières : combien d'utilisateurs sélectionnés sont censés réaliser l'événement, et combien sont censés ne pas le faire.

![L'audience sélectionnée et la précision estimée affichées dans le tableau de bord de Braze.]({% image_buster /assets/img/purchasePrediction/purchaseEstimatedResults.png %})

### On attend d'eux qu'ils accomplissent

Vous pouvez utiliser la précision estimée pour vérifier combien d'utilisateurs sélectionnés sont censés effectuer l'événement.

La prédiction n'est pas parfaitement exacte, et aucune prédiction ne l'est jamais, ce qui signifie que Braze ne sera pas en mesure d'identifier chaque futur utilisateur pour réaliser l'événement. Les scores de vraisemblance sont comme un ensemble de prédictions informées et fiables. La barre de progression indique combien de "vrais positifs" attendus dans l'audience de prédiction seront ciblés avec l'audience sélectionnée. Notez que nous nous attendons à ce que ce nombre d'utilisateurs réalise l'événement même si vous ne leur envoyez pas de message.

### On ne s'attend pas à ce qu'ils soient performants

Vous pouvez utiliser la précision estimée pour vérifier combien d'utilisateurs sélectionnés sont susceptibles de ne pas réaliser l'événement.

Tous les modèles de machine learning font des erreurs. Il se peut que certains utilisateurs de votre sélection aient un score de probabilité élevé, mais qu'ils ne réalisent pas l'événement. Si vous n’agissiez pas, ils ne réaliseraient pas l'événement. Ils seront de toute façon ciblés, donc il s’agit d’une erreur ou d’un « faux positif ». La largeur totale de cette deuxième barre de progression représente le nombre attendu d'utilisateurs qui n'effectueront pas l'événement, et la partie remplie représente ceux qui seront incorrectement ciblés en utilisant la position actuelle du curseur.

À l'aide de ces informations, nous vous encourageons à décider du nombre de vrais positifs que vous souhaitez capturer, du nombre de faux positifs dont vous pouvez accepter le ciblage et du coût des erreurs pour votre entreprise. Si vous envoyez une promotion intéressante, vous pouvez cibler uniquement les non acheteurs (faux positifs) en privilégiant le côté gauche du graphique. Vous pouvez également encourager les acheteurs qui achètent souvent (les vrais positifs) à le faire à nouveau en sélectionnant une section d'utilisateurs qui privilégie le côté droit du graphique.

## Qualité des prédictions {#prediction_quality}

{% multi_lang_include brazeai/predictive_suite/prediction_quality.md %}

## Tableau de corrélation des événements {#correlation_table}

Cette analyse affiche les attributs ou les comportements de l'utilisateur qui sont en corrélation avec les événements de l'audience de prédiction. Les attributs évalués sont l’âge, le pays, le sexe et la langue. Les comportements analysés comprennent les sessions, les achats, le montant total des dépenses, les événements personnalisés, ainsi que les campagnes et les étapes canvas reçues au cours des 30 derniers jours.

Les tableaux sont divisés en deux parties, gauche et droite, respectivement pour les personnes les plus et les moins susceptibles de réaliser l'événement. Pour chaque ligne, le ratio par lequel les utilisateurs ayant le comportement ou l'attribut dans la colonne de gauche sont plus ou moins susceptibles de réaliser l'événement est affiché dans la colonne de droite. Ce nombre est le rapport entre les scores de vraisemblance des utilisateurs ayant ce comportement ou cet attribut, divisé par la probabilité de réaliser l'événement sur l'ensemble de l'audience de prédiction.

Ce tableau n'est mis à jour que lorsque la prédiction se réajuste et non lorsque les scores de vraisemblance de l'utilisateur sont mis à jour.

{% alert note %}
Les données de corrélation pour les aperçus de prédictions seront partiellement cachées. Un achat est requis pour révéler ces informations. Contactez votre gestionnaire de compte pour plus d’informations.
{% endalert %}
