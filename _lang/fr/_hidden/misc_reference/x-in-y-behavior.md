---
nav_title: Comportement du filtre « X dans Y »
permalink: /x-in-y-behavior/
---

# Comportement actuel du filtre « X dans Y »

Le comportement de ces filtres restera le plus souvent le même et sera défini par les caractéristiques suivantes :

- Exécuter en définissant Jours civils (fin à minuit).
- Les « jours » sont déterminés avec le temps UTC.
- Le jour UTC actuel est défini comme « 0 ».

{% details Pourquoi la définition du temps UTC est-elle passée de « 1 » à « 0 » ? %}
La planification de fuseau horaire local exige que les utilisateurs restent dans les segments pendant 24 heures. Si Y = 1 jour, dans certains cas, nous évaluions moins de 24 heures d'historique de l'utilisateur pour déterminer ce qui devait être traité pour la campagne ou Canvas.

La modification rendra le filtre plus intuitif et plus cohérent avec le comportement de nos autres fonctionnalités de calendrier, comme nos options de planification « en 1 jour ».
{% enddetails %}

<br>

## Exemple

La campagne suivante est/sera envoyée à 21 h 00 le 16 avril. La segmentation de l’audience est « a effectué plus de 2 achats au cours des 3 derniers jours ».

![Planification de campagne][1]

21 h00 ET le 16 avril, correspond à 1 h 00 UTC le 17 avril.

Le 17 avril serait le jour « 0 », le 16 avril le jour « 1 », le 15 avril le jour « 2 » et le 14 avril le jour « 3 ».

L'historique à partir de 0 h 00 UTC le 14 avril jusqu'à l'heure actuelle (1 h 00 UTC le 17 avril).
Cela s’accumule dans une fenêtre qui inclut 73 heures de l’historique de l’utilisateur.

## Jours civils

Les jours civils sont utilisés de façon plus importante que les filtres « X dans Y »

- Planification des messages
- Limite de fréquence
- Filtres « X dans Y »

Les `jours civils` correspondent à la période de temps d’un jour compté, entre 0 h 00 et 23 h 59 le même jour (de 0 h 00 le 8 juin à 23 h 59 le 8 juin constitue un jour civil).

### Limite de fréquence

Les jours civils sont utilisés lorsque vous sélectionnez « jours » ou « semaines » dans `Limite de fréquence`.

- `Chaque jour` limitera le plafonnement au jour civil actuel avec l’heure locale de votre utilisateur (prend fin à minuit heure locale).
- `Tous les 2 jours` limitera le plafonnement aux jours civils actuel et précédent avec l’heure local de votre utilisateur (prend fin à minuit, heure locale, du jour civil actuel).

### Heure locale et de l’entreprise

Le jour civil actuel dans le fuseau horaire de la société correspond au jour `0`.

`Envoyer dans 1 jour civil à 11 h 05 de l’heure de l’entreprise` ou `Envoyer dans 1 jour civil à 11 h 05 à l’heure locale` ajouterait `1` jour au jour civil actuel dans le fuseau horaire de l’entreprise ou dans le fuseau horaire local, respectivement, puis planifierait le message au prochain 11 h 05 (heure de l’entreprise).

Si l’heure locale ou de l’entreprise correspond à l’heure du Pacifique (PT), et que l’utilisateur saisit l’étape Canvas à 20 h 00 PT le 13 avril, Braze programmera celle-ci pour 11 h 05 PT le 14 avril.

## Précédent comportement du filtre « X dans Y »

Braze possède une catégorie spécifique de filtres de segmentation : les filtres « X dans Y ». Ces filtres possèdent chacun une fonctionnalité similaire définie par les caractéristiques suivantes :

- Exécuter en définissant Jours civils (fin à minuit).
- Les « jours » sont déterminés avec le temps UTC.
- Le jour UTC actuel est défini comme « 1 ».



[1]:{% image_buster /assets/img/campaign-schuedule-example.png %}
