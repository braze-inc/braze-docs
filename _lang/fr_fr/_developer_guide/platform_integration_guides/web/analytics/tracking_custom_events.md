---
nav_title: Suivre les événements personnalisés
article_title: Suivre les événements personnalisés pour le Web
platform: Web
page_order: 2
page_type: reference
description: "Cet article explique comment suivre les événements personnalisés et ajouter des propriétés à ces événements pour le Web."

---

# Suivre les événements personnalisés

> Vous pouvez enregistrer des événements personnalisés dans Braze pour en savoir plus sur les modèles d’utilisation de votre application et segmenter vos utilisateurs en fonction de leurs actions sur le tableau de bord.

Avant de procéder à la mise en œuvre, n'oubliez pas de consulter les exemples d'options de segmentation offertes par les événements personnalisés, les attributs personnalisés et les événements d'achat dans nos [meilleures pratiques.]({{site.baseurl}}/developer_guide/platform_wide/getting_started/analytics_overview/#best-practices) Nous vous recommandons également de vous familiariser avec les [conventions de dénomination de nos événements]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

```javascript
braze.logCustomEvent("YOUR-EVENT-NAME");
```

Pour plus d'informations, reportez-vous à la documentation [`logCustomEvent`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent).

## Ajouter des propriétés {#properties-events}

Vous pouvez facultativement ajouter des métadonnées sur les événements personnalisés en transmettant un objet de propriétés avec votre événement personnalisé.

Les propriétés sont définies comme des paires clé-valeur. Les clés sont des chaînes de caractères et les valeurs peuvent être des objets `string`, `numeric`, `boolean` ou [`Date`](http://www.w3schools.com/jsref/jsref_obj_date.asp).

```javascript
braze.logCustomEvent("YOUR-EVENT-NAME", {
  you: "can", 
  pass: false, 
  orNumbers: 42,
  orDates: new Date(),
  or: ["any", "array", "here"],
  andEven: {
     deeply: ["nested", "json"]
  }
});
```

Pour plus d'informations, reportez-vous à la documentation [`logCustomEvent()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent).

