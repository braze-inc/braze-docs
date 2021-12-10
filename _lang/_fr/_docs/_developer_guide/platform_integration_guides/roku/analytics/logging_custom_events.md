---
nav_title: Événements personnalisés de suivi
article_title: Suivi des événements personnalisés pour Roku
platform: Roku
page_order: 2
page_type: Référence
description: "Cette page couvre les méthodes pour enregistrer des événements personnalisés via le Braze SDK."
---

# Suivi des événements personnalisés

Vous pouvez enregistrer des événements personnalisés dans Braze pour en savoir plus sur les habitudes d'utilisation de votre application et pour segmenter vos utilisateurs par leurs actions sur le tableau de bord. Vous devriez également consulter nos notes sur [les conventions de nommage des événements]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

## Ajouter un événement personnalisé

```javascript
m.Braze.logEvent("VOTRE_EVENT_NAME")
```

### Ajout de propriétés

Vous pouvez ajouter des métadonnées sur les événements personnalisés en passant un dictionnaire de propriétés avec votre événement personnalisé.

Les propriétés sont définies comme des paires clé-valeur.  Les clés sont des objets `String` et les valeurs peuvent être `String`, ou `Integer`.

```javascript
m.Braze.logEvent("VOTRE_EVENT_NAME", {"stringPropKey" : "stringPropValue", "intPropKey" : Integer intPropValue})
```
