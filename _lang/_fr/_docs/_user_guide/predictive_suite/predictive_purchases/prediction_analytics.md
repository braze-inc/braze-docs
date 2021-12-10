---
nav_title: Analyses de prédiction
article_title: Analyses de prédiction
description: "Cet article de référence couvre les différents composants inclus dans la page Analyses des achats prédictifs et comment ils peuvent être utilisés pour prendre des décisions éclairées."
page_order: 2
---

# Analyses de prédiction

Une fois que votre prédiction aura été construite et formée, vous aurez accès à la page __Analyses de prédiction__. Cette page vous aide à décider quels utilisateurs vous devez cibler en fonction de leur Score de probabilité d'achat ou de catégorie. Dès que la formation est terminée et que cette page est remplie, vous pouvez simplement utiliser [filtres]({{site.baseurl}}/user_guide/predictive_suite/predictive_churn/messaging_users/#filters) dans des segments ou des campagnes pour commencer à utiliser les sorties du modèle. Si vous voulez aider à décider qui cibler et pourquoi, Cette page peut vous aider en fonction de la précision historique du modèle et de vos propres objectifs commerciaux.

__Analytics Components__<br> &#45; [Purchase Likelihood Score](#purchase_score)<br> &#45; [Targeting Users](#target_users)<br> &#45; [Prediction Quality](#prediction_quality)<br> &#45; [Estimated Results](#estimated_results)<br> &#45; [Purchase Correlation Table](#correlation_table)

## Acheter le score de probabilité {#purchase_score}

Les utilisateurs de l'audience de prédiction se verront attribuer un score de probabilité d'achat entre 0 et 100. Plus le score est élevé, plus la probabilité d’achat est élevée.

- Les utilisateurs ayant des cotes de probabilité d'achat entre 0 et 50 seront étiquetés dans la catégorie Basse
- Les utilisateurs ayant des scores entre 50 et 75 et 100 seront étiquetés respectivement dans les catégories moyenne et haute probabilité.

Les scores et les catégories correspondantes seront mis à jour selon le calendrier que vous avez choisi dans la page __Création de Prédiction__. Le nombre d'utilisateurs ayant acheté des scores de probabilité dans chacun des 20 segments de même taille ou dans chacune des catégories de probabilité d'achat, est affiché dans le graphique en haut de la page.

## Constructeur d'audience {#target_users}

La distribution des cotes de probabilité d'achat pour l'ensemble de l'audience de prédiction est affichée en haut de la page. Les utilisateurs situés dans des seaux plus à droite ont des scores plus élevés et sont plus susceptibles d'acheter. Les utilisateurs situés dans des compartiments plus à gauche sont moins susceptibles d'acheter. Le curseur situé sous le graphique vous permettra de sélectionner un échantillon d'utilisateurs et d'estimer les résultats de ciblage de ces utilisateurs.

!\[Churn Targeting\]\[4\]{: style="max-width:90%"}

Lorsque vous déplacez les poignées du curseur à différentes positions, la barre de la moitié gauche du panneau ci-dessous vous informera du nombre d'utilisateurs de l'ensemble de l'audience prédiction qui serait ciblée en utilisant la partie de la population que vous avez sélectionnée.

### Résultats estimés {#estimated_results}

!\[Résultats estimés\]\[6\]

Dans la moitié droite du panneau sous le graphique, nous montrons les estimations de la précision attendue du ciblage de la portion de l'audience de prédiction que vous avez sélectionnée ci-dessus de deux manières:

1. Combien d'utilisateurs sélectionnés sont censés acheter<br><br> La prédiction n'est pas parfaitement exacte, et aucune prédiction ne l'est jamais, ce qui signifie que Braze ne sera pas en mesure d'identifier chaque acheteur futur. Les cotes de probabilité sont comme un ensemble de prédictions fiables et informées. La barre de progression indique combien d'acheteurs « réels » ou « vrais » attendus dans l'audience de prédiction seront ciblés en fonction du public sélectionné ci-dessus. Notez que nous attendons de ce nombre d'utilisateurs qu'ils achètent même si vous ne leur envoyez pas de message. <br><br>

2. Combien d'utilisateurs sélectionnés doivent ne pas acheter<br><br>Tous les modèles d'apprentissage automatique font des erreurs. Il se peut que certains utilisateurs de votre choix aient un score de probabilité d'achat élevé, mais ne finissent pas par faire un achat. Ils ne feraient pas d’achat si vous ne preniez aucune mesure. Ils seront de toute façon ciblés, donc c'est une erreur ou un "faux positif". La largeur totale de cette deuxième barre de progression représente le nombre attendu d'utilisateurs qui n'achèteront pas, et la portion rouge est celle qui sera mal ciblée en utilisant la position courante.

En utilisant ces informations, nous vous encourageons à décider combien d'acheteurs vous souhaitez capturer, le nombre de non-acheteurs que vous pouvez accepter d'être ciblé et le coût des erreurs pour votre entreprise. Si vous envoyez une promotion précieuse, vous voudrez peut-être cibler uniquement les non-acheteurs en privilégiant le côté gauche du graphique. Ou, vous pouvez encourager les acheteurs qui achètent souvent pour le faire à nouveau en sélectionnant un échantillon d'utilisateurs qui privilégie le côté droit du graphique.

### Qualité de la prédiction {#prediction_quality}

Pour mesurer la précision de votre modèle, la métrique __Qualité de Prédiction__ vous montrera à quel point ce modèle d’apprentissage automatique particulier semble être efficace. Essentiellement, il s'agit de mesurer à quel point cette prédiction est bonne à distinguer les acheteurs des non-acheteurs. Une qualité de Prédiction de 100 signifierait qu'il sait parfaitement qui veut et ne va pas acheter sans erreur (cela ne se produit jamais! , et 0 signifie qu'il est aléatoire de deviner. Consultez ce document pour en savoir plus sur ce qui se trouve dans la [Qualité Prédiction]({{site.baseurl}}/user_guide/predictive_suite/predictive_churn/prediction_analytics/prediction_quality/).

Voici ce que nous recommandons pour différentes gammes de qualité de prédiction :

| Plage de qualité de la prédiction (%) | Recommandation                                                                                                                                                           |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 60 - 100                              | Excellent. Précision du niveau supérieur. Il est peu probable que la modification des définitions du public apporte un avantage supplémentaire.                          |
| 40 - 60                               | Bien. Ce modèle produira des prédictions précises, mais essayer différents paramètres d'audience peut donner de meilleurs résultats.                                     |
| 20 - 40                               | Foire. Ce modèle peut fournir de la précision et de la valeur, mais envisagez d'essayer différentes définitions d'audience pour voir si elles augmentent la performance. |
| 0 - 20                                | « Paul. » Nous vous recommandons de modifier les définitions de votre audience et de réessayer.                                                                          |
{: .reset-td-br-1 .reset-td-br-2}

La prédiction sera de nouveau formée toutes les deux semaines et mise à jour parallèlement à la métrique de qualité de la prédiction pour garder vos prévisions à jour sur les derniers comportements de l'utilisateur. La dernière fois que cette reformation s'est produite sera affichée sur la page de la liste des prédictions ainsi que sur la page d'analyse de votre prédiction.

Quand une prédiction est créée pour la première fois, la Qualité de Prédiction sera basée sur les données historiques qui sont interrogées lorsque vous cliquez sur __Prédiction de Construction__. Toutes les deux semaines par la suite, la qualité de la prédiction est obtenue en comparant les scores de prédiction aux résultats du monde réel.

## Acheter la table de corrélation {#correlation_table}

Cette analyse affiche les attributs ou comportements de l'utilisateur qui sont corrélés avec les achats dans l'audience de prédiction. Les attributs évalués sont l'âge, le pays, le sexe et la langue. Les comportements analysés comprennent les sessions, les achats, le total des dollars dépensés, les événements personnalisés et les campagnes & Les étapes de Canvas reçues au cours des 30 derniers jours. Les tables sont divisées en gauche et droite pour plus et moins susceptibles d'acheter, respectivement. Pour chaque ligne, le ratio selon lequel les utilisateurs ayant le comportement ou l'attribut dans la colonne de gauche sont plus ou moins susceptibles d'acheter est affiché dans la colonne de droite. Ce nombre est le ratio de la probabilité d'achat des utilisateurs avec ce comportement ou cet attribut divisé par la probabilité d'acheter sur l'ensemble de l'audience prévisionnelle.

Ce tableau n'est mis à jour que lorsque la Prédiction se reforme et non lorsque l'utilisateur achète des notes de Likelihood Scores est mis à jour.

{% alert note %}
Les données de corrélation pour les prédictions d'aperçu seront partiellement masquées. Un achat est nécessaire pour divulguer ces informations. Veuillez contacter votre responsable de compte pour plus d'informations.
{% endalert %}
[6]: {% image_buster /assets/img/purchasePrediction/purchaseEstimatedResults.png %} [4]: {% image_buster /assets/img/purchasePrediction/purchaseTargeTargeting.png %}