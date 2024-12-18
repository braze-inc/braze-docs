---
nav_title: Suivre les événements personnalisés
article_title: Suivre les événements personnalisés pour Roku
platform: Roku
page_order: 2
page_type: reference
description: "Cette page trait des méthodes d’enregistrement des événements personnalisés pour Roku via le SDK Braze."

---

# Suivre les événements personnalisés

> Vous pouvez enregistrer des événements personnalisés dans Braze pour en savoir plus sur les modèles d’utilisation de votre application et segmenter vos utilisateurs en fonction de leurs actions sur le tableau de bord. Nous vous recommandons également de vous familiariser avec les [conventions de dénomination de nos événements]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

## Ajouter un événement personnalisé

```brightscript
m.Braze.logEvent("YOUR_EVENT_NAME")
```

### Ajouter des propriétés

Vous pouvez ajouter des métadonnées aux événements personnalisés en transmettant un dictionnaire de propriétés avec votre événement personnalisé.

Les propriétés sont définies comme des paires clé-valeur.  Les clés sont des objets `String` et les valeurs peuvent être `String` ou `Integer`.

```brightscript
m.Braze.logEvent("YOUR_EVENT_NAME", {"stringPropKey" : "stringPropValue", "intPropKey" : Integer intPropValue})
```
