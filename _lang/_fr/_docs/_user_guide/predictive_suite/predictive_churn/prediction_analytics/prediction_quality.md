---
nav_title: Qualité de la prédiction
title: Qualité de la prédiction
description: "Cet article de référence examine en profondeur la métrique de qualité de la prédiction située sur la page Analytiques de la prédiction."
page_order: 1
Tool:
  - Tableau de bord
---

# Qualité de la prédiction

Pour mesurer la précision de votre modèle, la métrique __Qualité de Prédiction__ vous montrera à quel point ce modèle d’apprentissage automatique particulier semble être efficace lors des tests sur des données historiques. Braze tire des données en fonction des groupes que vous avez spécifiés dans la page de création du modèle. Le modèle est formé sur un ensemble de données (le « jeu de formation ») puis testé sur un nouveau jeu de données distinct (le « jeu de test »).

Notre mesure de la qualité de la prédiction est [Qualité de levage](https://dl.acm.org/doi/10.1145/380995.381018). Vous êtes probablement familier avec le "lift", qui mesure souvent l'augmentation, en tant que ratio ou pourcentage, d'un résultat réussi comme une conversion. Dans ce cas, le résultat réussi est d'identifier correctement un utilisateur qui aurait tourné. La qualité de levage est le levier moyen que la prédiction fournit à tous les auditoires possibles pour la messagerie de l'ensemble de test. Cette approche mesure à quel point il est préférable de deviner le modèle. Avec cette mesure, 0% signifie que le modèle ne vaut pas mieux que de deviner aléatoirement qui va rouler, et 100% indique une parfaite connaissance de qui va rouler.

Voici ce que nous recommandons pour différentes gammes de qualité de prédiction :

| Plage de qualité de la prédiction (%) | Recommandation                                                                                                                                                           |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 60 - 100                              | Excellent. Précision du niveau supérieur. Il est peu probable que la modification des définitions du public apporte un avantage supplémentaire.                          |
| 40 - 60                               | Bien. Ce modèle produira des prédictions précises, mais essayer différents paramètres d'audience peut donner de meilleurs résultats.                                     |
| 20 - 40                               | Foire. Ce modèle peut fournir de la précision et de la valeur, mais envisagez d'essayer différentes définitions d'audience pour voir si elles augmentent la performance. |
| 0 - 20                                | « Paul. » Nous vous recommandons de modifier les définitions de votre audience et de réessayer.                                                                          |
{: .reset-td-br-1 .reset-td-br-2}

La prédiction sera de nouveau formée toutes les deux semaines et mise à jour parallèlement à la métrique de qualité de la prédiction pour garder vos prévisions à jour sur les derniers comportements de l'utilisateur. La dernière fois que cette reformation a eu lieu sera affichée sur la page de la liste des prédictions ainsi que sur la page d'analyse d'une prédiction.
> __Détails de la qualité de la prédiction__ <br><br> Exemple : Si 20 % de vos utilisateurs sont habitués en moyenne, et vous choisissez un sous-ensemble aléatoire de 20% de vos utilisateurs et les étiquetez comme étant au hasard (qu'ils soient ou non réels), On s’attendrait à n’identifier correctement que 20 % des habitants de la ville. C'est une supposition aléatoire. Si le modèle devait se contenter de le faire, l'ascenseur serait 1 pour ce cas.<br> Si le modèle, par contre, vous permet de transmettre un message à 20% des utilisateurs et, pour capturer ainsi tous les « vrais » clochers et personne d’autre, l’ascenseur serait 100% / 20% = 5. Si vous classez ce ratio pour chaque proportion des membres les plus probables que vous pourriez écrire, vous obtenez la [Left Curve](https://towardsdatascience.com/the-lift-curve-unveiled-998851147871). <br><br>Une autre façon de penser à la Qualité de Lift (et aussi à la Qualité de Prédiction) est de déterminer jusqu'où se situent entre la devinaison aléatoire (0%) et la perfection (100%) la courbe de levage de la prédiction est d'identifier les aberrants sur l'essai. Pour le papier original sur la qualité de soulagement voir [ici](https://dl.acm.org/doi/10.1145/380995.381018).

