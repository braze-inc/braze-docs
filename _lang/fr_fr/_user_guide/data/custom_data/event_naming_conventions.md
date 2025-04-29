---
nav_title: Conventions de nommage des événements
article_title: Conventions de nommage des événements
page_order: 10
page_type: reference
description: "Cet article de référence couvre les conventions et meilleures pratiques de nommage pour les événements."

---

# Conventions de dénomination des événements

> Cette page traite des conventions de dénomination des événements et des meilleures pratiques. En maintenant la cohérence de votre taxonomie d'événements et d'attributs, vous garderez vos données propres et utilisables pour les utilisateurs nouveaux et existants de la plateforme Braze. Cela permet d'éviter des problèmes ultérieurs, comme le déclenchement d'une campagne auprès de la mauvaise audience ou la génération de mauvais résultats après avoir utilisé le mauvais événement.

## Bonnes pratiques

- Adoptez une convention de nommage claire.
- Utilisez des majuscules et un formatage cohérents pour les noms d'événements.
- Évitez de donner des noms similaires à des événements.
- Évitez les longues chaînes de caractères pour les attributs d’événements, car elles seront tronquées ou coupées sur le tableau de bord de Braze.

## Conventions de nommage

### Utilisez des groupes d’événements

Utilisez des groupes pour nommer les événements et différencier les différentes parties de votre produit. En catégorisant votre produit en groupes, tout utilisateur peut clairement comprendre à quoi l’événement fait référence, et à quoi il sert.

### Structure de nommage des événements

La structure de nommage la plus courante est `group_noun_action`. Les événements doivent tous être en minuscules pour éviter les erreurs d’identification des propriétés ou d’instrumentation.

### Propriétés

Sélectionnez un événement, puis identifiez les différences en utilisant les propriétés. C’est utile pour les événements qui sont fondamentalement identiques mais qui présentent des différences mineures (au niveau des canaux de la campagne, par exemple). Cela permet également de voir facilement le cheminement des utilisateurs dans les événements. Reportez-vous à l'[objet propriétés d'événement]({{site.baseurl}}/api/objects_filters/event_object/#event-properties-object) pour un exemple et un contexte supplémentaire.
