---
nav_title: Qualité de prédiction
title: Qualité de prédiction
description: "Le présent article de référence examine en détail l’indicateur de la qualité de prédiction situé sur la page Analyses prédictive."
page_order: 1
Tool:
  - Dashboard
---

# Qualité de prédiction

> Pour mesurer la précision de votre modèle, l'indicateur de _qualité des prédictions_ vous montrera à quel point ce modèle de machine learning particulier semble efficace lorsqu'il est testé sur des données historiques. Braze extrait les données selon les groupes que vous avez spécifiés dans la page de création du modèle. Le modèle est entraîné à l’aide d’un ensemble de données (l’ensemble « entraînement ») puis testé sur un nouveau jeu de données distinct (l’ensemble « test »). 

Notre mesure de la _qualité des prédictions_ est la [qualité de l'ascenseur](https://dl.acm.org/doi/10.1145/380995.381018). Vous connaissez probablement la notion de "lift", qui mesure souvent l'augmentation, sous la forme d'un ratio ou d'un pourcentage, d'un résultat positif tel qu'une conversion. Dans ce cas, un résultat fructueux identifie correctement un utilisateur qui aurait abandonné. La qualité de l'augmentation projetée est l'effet de levier moyen de la prédiction sur toutes les tailles d'audience possibles pour l'envoi de messages dans l'ensemble de test. Cette approche mesure l’efficacité du modèle par rapport à une estimation aléatoire. Avec cette mesure, 0 % signifie que le modèle n’est pas meilleur qu’une estimation aléatoire des personnes qui vont abandonner, et 100 % indique une prédiction parfaite de l’attrition.

Voici ce que nous recommandons pour différentes gammes de _qualité de prédictions_:

| Plage de qualité de prédiction ( %) | Recommandation |
| ---------------------- | -------------- |
| 60 - 100 | Excellent. Précision supérieure. La modification des définitions d’audience est peu susceptible de fournir un avantage supplémentaire. |
| 40 - 60 | Bon. Ce modèle produira des prédictions précises, mais essayer différents paramètres d’audience peut obtenir de meilleurs résultats. |
| 20 - 40| Juste. Ce modèle peut fournir une précision et une valeur, mais envisagez d’essayer différentes définitions d’audience pour voir si elles augmentent les performances. |
| 0 - 20 | Faible. Nous vous recommandons de modifier les définitions de votre audience et de réessayer. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

La prédiction sera à nouveau entraînée toutes les deux semaines et mise à jour parallèlement à l'indicateur de _qualité de la prédiction_ afin que vos prédictions soient toujours actualisées en fonction des modèles de comportement des utilisateurs les plus récents. En outre, à chaque fois, les deux dernières semaines de prédictions seront testées par rapport aux résultats réels des utilisateurs. La _qualité de la prédiction_ sera alors calculée sur la base de ces résultats réels (plutôt que sur des estimations). Il s'agit d'un backtest automatique (c'est-à-dire le test d'un modèle prédictif sur des données historiques) qui permet de s'assurer que la prédiction est exacte dans des scénarios réels. La dernière fois que ce recyclage et ce backtesting ont eu lieu sera affichée sur la page des **prédictions** et sur la page d'analyse/analytique d'une prédiction individuelle. Même une prédiction de type "preview" effectuera ce backtest une fois après sa création. Ainsi, vous pouvez être sûr de l'exactitude de vos prédictions personnalisées, même avec la version gratuite de la fonctionnalité.

{% details Détails sur la qualité des prédictions %}

Par exemple, si 20 % de vos utilisateurs abandonnent en moyenne et que vous choisissez un sous-ensemble aléatoire de 20 % de vos utilisateurs et que vous les qualifiez de désabonnés au hasard (qu'ils le soient réellement ou non), vous devriez identifier correctement seulement 20 % des utilisateurs réellement désabonnés. C’est une estimation aléatoire. Si le modèle ne faisait que ça, l’encouragement serait de 1 pour ce cas.

Si le modèle, d’autre part, vous a permis d’envoyer des messages à 20 % des utilisateurs et, de ce fait, de cibler toutes les « vraies » personnes qui abandonnent et personne d’autre, l’encouragement serait 100 % / 20 % = 5. Si vous reportez ce rapport pour chaque proportion des personnes les plus susceptibles d’abandonner à qui vous pourriez envoyer un message, vous obtenez la [courbe d'amélioration projetée](https://towardsdatascience.com/the-lift-curve-unveiled-998851147871). 

Une autre façon d'appréhender la qualité du lift (et aussi la _qualité de la prédiction_) est de voir à quel point la courbe de lift de la prédiction se situe entre la supposition aléatoire (0 %) et la perfection (100 %) dans l'identification des désabonnés sur l'ensemble de test. Pour consulter l'article original sur la qualité de l'amélioration projetée, voir [Mesurer la qualité de l'amélioration projetée dans le marketing de base de données](https://dl.acm.org/doi/10.1145/380995.381018).

{% enddetails %}
