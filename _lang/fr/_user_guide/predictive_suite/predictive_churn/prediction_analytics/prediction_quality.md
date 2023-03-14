---
nav_title: Qualité de prédiction
title: Qualité de prédiction
description: "Le présent article de référence examine en détail l’indicateur de la qualité de prédiction situé sur la page Analyses prédictive."
page_order: 1
Outil :
  - Tableau de bord
---

# Qualité de prédiction

Pour mesurer la précision de votre modèle, l’indicateur de **Qualité de prédiction** vous montrera l’efficacité de ce modèle de machine learning particulier lorsqu’il est testé sur des données historiques. Braze extrait les données selon les groupes que vous avez spécifiés dans la page de création du modèle. Le modèle est entraîné à l’aide d’un ensemble de données (l’ensemble « entraînement ») puis testé sur un nouveau jeu de données distinct (l’ensemble « test »). 

Notre mesure de la qualité de prédiction est la [Qualité d’encouragement](https://dl.acm.org/doi/10.1145/380995.381018). Vous connaissez probablement « l’encouragement » qui mesure souvent l’augmentation, tel qu’un ratio ou un pourcentage, de résultats positifs comme une conversion. Dans ce cas, un résultat fructueux identifie correctement un utilisateur qui aurait abandonné. La qualité d’encouragement est la moyenne d’encouragement que la prédiction fournit sur toutes les tailles d’audience possibles pour l’envoi de message de l’ensemble de test. Cette approche mesure l’efficacité du modèle par rapport à une estimation aléatoire. Avec cette mesure, 0 % signifie que le modèle n’est pas meilleur qu’une estimation aléatoire des personnes qui vont abandonner, et 100 % indique une prédiction parfaite de l’attrition.

Voici ce que nous recommandons pour diverses plages de qualité de prédiction :

| Plage de qualité de prédiction ( %) | Recommandation |
| ---------------------- | -------------- |
| 60 à 100 | Excellent. Précision supérieure. La modification des définitions d’audience est peu susceptible de fournir un avantage supplémentaire. |
| 40 à 60 | Bon. Ce modèle produira des prédictions précises, mais essayer différents paramètres d’audience peut obtenir de meilleurs résultats. |
| 20 à 40| Juste. Ce modèle peut fournir une précision et une valeur, mais envisagez d’essayer différentes définitions d’audience pour voir si elles augmentent les performances. |
| 0 à 20 | Faible. Nous vous recommandons de modifier les définitions de votre audience et de réessayer. |
{: .reset-td-br-1 .reset-td-br-2}

La prédiction sera entraînée à nouveau toutes les deux semaines et mise à jour en même temps que la métrique de qualité de prédiction afin de maintenir vos prédictions actualisées sur les schémas les plus récents de comportement des utilisateurs. La date du dernier entraînement sera affichée sur la page de liste des prédictions ainsi que sur une page d’analyses prédictives individuelle.

>**Détails de la qualité de prédiction** <br><br> Exemple : Si 20 % en moyenne de vos utilisateurs abandonnent et que vous choisissez un sous-ensemble aléatoire de 20 % de vos utilisateurs et les étiquetez comme ayant aléatoirement abandonné (que ce soit vrai ou non), vous vous attendriez à identifier correctement uniquement 20 % des personnes qui abandonnent effectivement. C’est une estimation aléatoire. Si le modèle ne faisait que ça, l’encouragement serait de 1 pour ce cas.<br> Si le modèle, d’autre part, vous a permis d’envoyer des messages à 20 % des utilisateurs et, de ce fait, de cibler toutes les « vraies » personnes qui abandonnent et personne d’autre, l’encouragement serait 100 % / 20 % = 5. Si vous reportez ce rapport pour chaque proportion des personnes les plus susceptibles d’abandonner à qui vous pourriez envoyer un message, vous obtenez la [Courbe d’encouragement](https://towardsdatascience.com/the-lift-curve-unveiled-998851147871). <br><br>Une autre façon d’envisager la qualité d’encouragement (et également de la qualité de prédiction) est la distance de la courbe d’encouragement de prédiction entre l’estimation aléatoire (0 %) et la perfection (100 %) en ce qui concerne l’identification des personnes allant abandonner dans l’ensemble de test. Rendez-vous [ici](https://dl.acm.org/doi/10.1145/380995.381018) pour consulter le texte d’origine sur la qualité d’encouragement.

