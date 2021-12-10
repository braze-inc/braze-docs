---
nav_title: Analyses de prédiction
article_title: Analyses de prédiction
description: "Cet article de référence couvre les différents éléments inclus dans la page Analyses de la prédiction des Églises et la façon dont ils peuvent être utilisés pour prendre des décisions éclairées et éclairées."
page_order: 2
---

# Analyses de prédiction

Une fois que votre prédiction aura été construite et formée, vous aurez accès à la page Analyses de prédiction. Cette page vous aide à décider quels utilisateurs vous devez cibler en fonction de leur Score de Risque de Coeur ou de leur Catégorie. Dès que la formation est terminée et que cette page est remplie, vous pouvez simplement utiliser [Filtres]({{site.baseurl}}/user_guide/predictive_suite/predictive_churn/messaging_users/#filters) dans des segments ou des campagnes pour commencer à utiliser les sorties du modèle. Mais si vous voulez aider à décider qui cibler et pourquoi, Cette page peut vous aider en fonction de la précision historique du modèle et de vos propres objectifs commerciaux.

__Composants Analytiques__<br> &#45; [Score de coque et catégorie](#churn_score)<br> &#45; [Qualité de la prévision](#prediction_quality)<br> &#45; [Résultats estimés](#estimated_results)<br> &#45; [Tableau de corrélation des cotés](#correlation_table)

## Aperçu

La distribution des scores pour l'ensemble de l'audience de prédiction est affichée en haut de la page dans un graphique que vous pouvez voir, par catégorie ou par score. Les utilisateurs dans les bacs plus à droite ont des scores plus élevés et sont plus susceptibles de comploter. Les utilisateurs dans les bacs plus à gauche sont moins susceptibles de se tourner. Le curseur au-dessous du graphique vous permettra de sélectionner un échantillon d'utilisateurs et d'estimer quels seraient les résultats de ciblage des utilisateurs dans la gamme sélectionnée de Colin Risk Score ou Catégorie.

!\[Churn Targeting\]\[4\]{: style="max-width:90%"}

Lorsque vous déplacez le curseur, la barre de la moitié gauche du panneau inférieur vous informera du nombre d'utilisateurs qui seraient visés par l'audience prévisionnelle.

## Score de cobaye et catégorie {#churn_score}

Les utilisateurs de l'audience de prédiction se verront attribuer un score entre 0 et 100. Plus le score est élevé, plus la probabilité d'une Église est élevée.
- Les utilisateurs ayant des scores de type Churn entre 0 et 50 seront étiquetés dans la catégorie Risque de faible coque.
- Les utilisateurs ayant des scores entre 50 et 75 et 100 seront étiquetés dans les catégories de risque moyen et de risque élevé respectivement.

Les scores et les catégories correspondantes seront mis à jour selon le calendrier que vous avez choisi sur la page de création du modèle. Le nombre d'utilisateurs ayant des cotes de cote dans chacun des 20 segments de même taille est affiché dans le graphique en haut de la page. Selon cette prédiction, cela peut vous aider à déterminer à quoi ressemble le risque de mordus dans toute la population.

## Cibler les utilisateurs pour réduire leur consommation

### Qualité de la prédiction {#prediction_quality}

Pour mesurer la précision de votre modèle, la métrique __Qualité de Prédiction__ vous montrera à quel point ce modèle d’apprentissage automatique particulier semble être efficace lors des tests sur des données historiques. Consultez ce document pour en savoir plus sur ce qui se trouve dans la [Qualité Prédiction]({{site.baseurl}}/user_guide/predictive_suite/predictive_churn/prediction_analytics/prediction_quality/).

Voici ce que nous recommandons pour différentes gammes de qualité de prédiction :

| Plage de qualité de la prédiction (%) | Recommandation                                                                                                                                                           |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 60 - 100                              | Excellent. Précision du niveau supérieur. Il est peu probable que la modification des définitions du public apporte un avantage supplémentaire.                          |
| 40 - 60                               | Bien. Ce modèle produira des prédictions précises, mais essayer différents paramètres d'audience peut donner de meilleurs résultats.                                     |
| 20 - 40                               | Foire. Ce modèle peut fournir de la précision et de la valeur, mais envisagez d'essayer différentes définitions d'audience pour voir si elles augmentent la performance. |
| 0 - 20                                | « Paul. » Nous vous recommandons de modifier les définitions de votre audience et de réessayer.                                                                          |
{: .reset-td-br-1 .reset-td-br-2}

La prédiction sera de nouveau formée toutes les deux semaines et mise à jour parallèlement à la métrique de qualité de la prédiction pour garder vos prévisions à jour sur les derniers comportements de l'utilisateur. La dernière fois que cette reformation s'est produite sera affichée sur la page de la liste des prédictions ainsi que sur la page d'analyse de votre prédiction.

## Résultats estimés {#estimated_results}

!\[Résultats estimés\]\[6\]{: style="float:right;max-width:30%;margin-left:15px;"}

Dans la moitié droite du panel sous le graphique, nous montrons des estimations de la précision prévue de cibler cette largeur de l'audience de prévision. Basé sur les données sur les utilisateurs dans l'Audience Prédiction dans le passé, et la précision apparente du modèle de discrimination entre les utilisateurs qui ne font pas partie de ces données passées, ces barres de progression estiment pour un message potentiel futur en utilisant le public mis en évidence avec le curseur :

1. Une estimation du nombre de membres réels sera correctement ciblée <br><br> Bien sûr, nous ne connaissons pas le futur parfaitement, donc nous ne savons pas précisément quels utilisateurs de l'Audience Prédiction seront à l'origine dans le futur. Mais la prédiction est une inférence fiable. Basé sur les performances passées, cette barre de progression indique le nombre total de membres « réels » ou « vrais » attendus dans l'audience prévisionnelle (basée sur les taux de départ antérieurs) qui seront ciblés en fonction de la sélection ciblée actuelle. Nous nous attendrions à ce que ce nombre d'utilisateurs s'abstiennent si vous ne les ciblez pas avec un message supplémentaire ou inhabituel. <br><br>

2. Une estimation du nombre d'utilisateurs qui n'auraient pas réellement participé sera mal ciblée<br><br>Tous les modèles d'apprentissage automatique font des erreurs. Il se peut que certains utilisateurs de votre choix aient un score de risque élevé mais ne finissent pas par se retrouver. Ils ne se moqueraient pas même si vous ne preniez aucune mesure. Ils seront de toute façon ciblés, donc c'est une erreur ou un "faux positif". La largeur totale de cette deuxième barre de progression représente le nombre attendu d'utilisateurs qui ne seront pas abonnés, et la portion rouge est celle qui sera mal ciblée en utilisant la position courante.

Utilisation de ces informations Nous vous encourageons à choisir le nombre de personnes que vous voulez capturer et le coût d'une erreur fausse positive pour votre entreprise. Si vous envoyez une promotion précieuse, vous voudrez peut-être garder les personnes qui ne sont pas des personnes qui sont ciblées à un minimum tout en obtenant autant de vraies personnes que le modèle le permettra. Ou, si vous êtes moins sensible aux faux positifs et que les utilisateurs reçoivent un message supplémentaire, vous pouvez envoyer un message à un plus grand nombre de personnes afin de capturer plus de gens attendus et ignorer les erreurs probables.

## Table de corrélation de la coque {#correlation_table}

Cette analyse affiche tous les attributs ou comportements de l'utilisateur qui sont corrélés avec l'utilisateur à l'Audience de Prédiction historique. Les tables sont divisées en gauche et droite pour plus et moins susceptibles de s'abîmer respectivement. Pour chaque ligne, le ratio selon lequel les utilisateurs ayant le comportement ou l'attribut dans la colonne de gauche sont plus ou moins susceptibles de s'afficher dans la colonne de droite. Ce nombre est le rapport entre la probabilité des utilisateurs avec ce comportement ou cet attribut divisé par la probabilité de s'abattre sur l'ensemble de l'Audience de la Prédiction.

Ce tableau n'est mis à jour que lorsque la prédiction se reforme et non lorsque les scores de risque de la part de l'utilisateur sont mis à jour.

{% alert note %}
Les données de corrélation pour les prédictions d'aperçu seront partiellement masquées. Un achat est nécessaire pour divulguer ces informations. Veuillez contacter votre responsable de compte pour plus d'informations.
{% endalert %}
[6]: {% image_buster /assets/img/churn/churmatedResults.png %} [4]: {% image_buster /assets/img/churn/churnTargeting.gif %}