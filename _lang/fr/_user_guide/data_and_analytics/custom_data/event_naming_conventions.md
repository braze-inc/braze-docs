---
nav_title: Conventions de nommage des événements
article_title: Conventions de nommage des événements
page_order: 0
page_type: reference
description: "Cet article de référence couvre les conventions et meilleures pratiques de nommage pour les événements."

---

# Conventions de dénomination des événements

Garantir la cohérence de votre taxonomie d’événements et d’attributs lors de votre intégration Braze permettra de garder vos données propres et utilisables par les utilisateurs (nouveaux ou existants) de la plateforme Braze. Cela permet d’éviter des problèmes ultérieurs qui pourraient déclencher une campagne vers un public inadapté ou donner des résultats incohérents car basés sur un événement inadéquat.

## Bonnes pratiques

- Adoptez une convention de nommage claire
- Casse et formatage cohérents pour les noms d’événements
- Évitez de donner des noms similaires à des événements
- Évitez les longues chaînes de caractères pour les attributs, car elles seront tronquées ou coupées sur le tableau de bord de Braze

## Conventions de nommage

### Utilisez des groupes d’événements

Utilisez des groupes pour nommer les événements et différencier les différentes parties de votre produit. En catégorisant votre produit en groupes, tout utilisateur peut clairement comprendre à quoi l’événement fait référence, et à quoi il sert.

### Structure de nommage des événements

La structure de nommage la plus courante est `group_noun_action`. Les événements doivent tous être en minuscules pour éviter les erreurs d’identification des propriétés ou d’instrumentation.

### Propriétés

Taggez un événement, puis identifiez les différences en utilisant les propriétés. C’est utile pour les événements qui sont fondamentalement identiques mais qui présentent des différences mineures (au niveau des canaux de la campagne, par exemple). Cela permet également de voir facilement le cheminement des utilisateurs dans les événements. Consultez les [objets de propriétés de l’événement]({{site.baseurl}}/api/objects_filters/event_object/#event-properties-object) pour trouver un exemple et un contexte supplémentaire.
