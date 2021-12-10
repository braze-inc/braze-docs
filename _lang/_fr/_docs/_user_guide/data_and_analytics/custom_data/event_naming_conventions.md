---
nav_title: Conventions de nommage des événements
article_title: Conventions de nommage des événements
page_order: 0
page_type: Référence
description: "Cet article de référence couvre les conventions de nommage des événements et les meilleures pratiques."
---

# Conventions de nommage des événements

Assurer la cohérence de votre événement et de votre attribut taxonomie pendant votre intégration à Braze gardera vos données propres et utilisables par les nouveaux utilisateurs et les utilisateurs existants de la plateforme Braze. Cela aide à éviter les problèmes ultérieurs qui peuvent entraîner le déclenchement d'une campagne à un mauvais public ou des divergences dans les résultats de l'utilisation du mauvais événement.

## Meilleures pratiques

- Gardez votre convention de nommage claire.
- Câblage et formatage cohérents des noms d’événements.
- Évitez de donner des noms similaires à des événements.
- Évitez les chaînes d'attributs d'événements longs qui seront tronquées ou coupées dans le tableau de bord de Braze.

## Conventions de nommage

### Utiliser les groupes d'événements

__Utilisez des groupes pour différencier des parties de votre produit pour nommer des événements.__ En catégorisant votre produit en groupes, tout utilisateur peut comprendre clairement à quoi se réfère l'événement et ce qu'il fait.

### Structure de nommage des événements

La structure de nommage la plus commune est `group_noun_action`. Les événements devraient tous être en minuscule pour éviter de casser les erreurs d'instrumentation et d'identifier les propriétés.

### Propriétés

S'agit-il d'un événement ou d'une propriété? __balise un événement puis identifie les différences en utilisant des propriétés.__

Ceci est utile pour les événements qui sont intrinsèquement les mêmes, mais ont des différences mineures, telles que les canaux pour une campagne. Nous pouvons aussi facilement voir comment les utilisateurs circulent à travers les événements. L'agrégation de ces événements sera plus fastidieuse car nous devrons créer un événement personnalisé pour les regrouper.
