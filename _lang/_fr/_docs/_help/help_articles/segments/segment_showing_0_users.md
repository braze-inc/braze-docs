---
nav_title: Utilisateurs manquants dans le segment
article_title: Utilisateurs manquants dans le segment
page_order: 1
page_type: Solution
description: "Cet article d'aide vous guide à travers les étapes de dépannage si aucun utilisateur ne s'affiche dans votre segment, mais vous anticipez plus."
tool: Segments
---

# Utilisateurs manquants dans le segment

Il y a deux solutions possibles lorsque vous voyez `0` utilisateurs, mais vous avez anticipé plus:
* [Calculer les statistiques exactes](#calculate-exact-statistics)
* [Vérifier le transfert de données](#verify-data-transfer)

## Calculer les statistiques exactes

Les statistiques du segment pourraient fournir une estimation. L'estimation est calculée sur la base d'un échantillon aléatoire avec un intervalle de confiance de 95% que le résultat est dans `+/- 1%`. Plus votre base d'utilisateurs est petite, plus il est probable que la taille de votre segment soit approximative. Cliquez sur **Calculer les statistiques exactes** sur le panneau **Détails du segment**. Cela calculera le nombre exact d'utilisateurs dans votre segment.

!\[Calculer des statistiques exactes\]\[28\]


## Vérifier le transfert de données

Il est possible que les données sur lesquelles vous filtrez ne soient pas envoyées au Brésil. Pour vérifier quels événements personnalisés sont envoyés à Braze, cliquez sur **Événements personnalisés** dans le menu de gauche dans la section **Données**. Sélectionnez l'événement personnalisé avec les dates et l'application spécifiques pour voir quelles données sont effectivement transférées vers Braze. Si vous remarquez que `0` données sont envoyées à Braze, la prochaine étape est d'évaluer comment vous envoyez les événements au Brésil.

!\[Vérification du transfert de données\]\[29\]

{% alert important %}
Les données que vous voyez dans le tableau de bord de Braze peuvent ne pas avoir la même syntaxe que ce que vous envoyez à Braze. Assurez-vous que ces deux éléments correspondent exactement.
{% endalert %}

Vous avez encore besoin d'aide ? Ouvrez un ticket de support []({{site.baseurl}}/braze_support/).

_Dernière mise à jour le 5 janvier 2021_
[28]: {% image_buster /assets/img_archive/trouble8.png %} [29]: {% image_buster /assets/img_archive/trouble9.png %}
