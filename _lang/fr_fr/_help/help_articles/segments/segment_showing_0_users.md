---
nav_title: Utilisateurs manquants dans le segment
article_title: Utilisateurs manquants dans le segment
page_order: 1

page_type: solution
description: "Cet article d’aide décrit la marche à suivre si vous n’avez pas d’utilisateurs dans un segment alors que vous en attendiez."
tool: Segments
---

# Utilisateurs manquants dans le segment

Il existe deux solutions possibles lorsque vous voyez `0` utilisateurs, alors que vous en attendiez plus :
* [Calculer les statistiques exactes](#calculate-exact-statistics)
* [Vérifier le transfert de données](#verify-data-transfer)

## Calculer les statistiques exactes

Les statistiques du segment fournissent peut-être une estimation. L’estimation est calculée sur la base d’un échantillon aléatoire avec un niveau de confiance à 95 % que le résultat sera exact à `+/- 1%` près. Plus votre base d’utilisateurs est petite, plus il est probable que la taille de votre segment soit une estimation approximative. Cliquez sur **Calculer les statistiques exactes** dans le panneau **Détails du segment**. Cela calculera le nombre exact d’utilisateurs dans votre segment.

![Panneau Détails du segment qui affiche l'option Calculer les statistiques exactes]({% image_buster /assets/img_archive/trouble8.png %})

## Vérifier le transfert de données

Il est possible que les données que vous filtrez ne soient pas envoyées à Braze. Pour vérifier quels événements personnalisés sont envoyés à Braze, consultez votre [Rapport d'événements personnalisés]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-analytics).

Sélectionnez l’événement personnalisé ainsi que les dates et l’application spécifiques pour voir quelles données sont réellement transférées à Braze. Si vous remarquez que les données `0` sont envoyées à Braze, l’étape suivante consiste à évaluer comment vous envoyez les événements à Braze.

![Graphique qui montre que le nombre d'événements personnalisés est égal à zéro]({% image_buster /assets/img_archive/trouble9.png %})

{% alert important %}
Les données que vous voyez dans le tableau de bord de Braze peuvent ne pas avoir la même syntaxe que celles que vous envoyez à Braze. Assurez-vous qu’elles correspondent exactement.
{% endalert %}

Vous avez toujours besoin d’aide ? Ouvrez un [ticket de support]({{site.baseurl}}/braze_support/).

_Dernière mise à jour le 5 janvier 2021_

