---
nav_title: Suivre les événements personnalisés
article_title: Suivre les événements personnalisés pour le Web
platform: Web
page_order: 2
page_type: reference
description: "Cet article explique comment suivre les événements personnalisés pour le Web."

---

# Suivre les événements personnalisés pour le Web

Vous pouvez enregistrer des événements personnalisés dans Braze pour en savoir plus sur les modèles d’utilisation de votre application et segmenter vos utilisateurs en fonction de leurs actions sur le tableau de bord.

Avant l’implémentation, assurez-vous d’étudier des exemples des options de segmentation offertes par les événements personnalisés, les attributs personnalisés et les événements d’achat dans nos [bonnes pratiques][0]. Nous vous recommandons également de vous familiariser avec nos [conventions de dénomination des événements]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

```javascript
braze.logCustomEvent("YOUR-EVENT-NAME");
```

Reportez-vous à la documentation [`logCustomEvent`][1] pour plus d’informations.

## Ajouter des propriétés {#properties-events}

Vous pouvez facultativement ajouter des métadonnées sur les événements personnalisés en transmettant un objet de propriétés avec votre événement personnalisé.

Les propriétés sont définies comme des paires clé-valeur. Les clés sont des chaînes de caractères et les valeurs peuvent être des objets `string`, `numeric`, `boolean` ou [`Date`][2].

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

Reportez-vous à la [`logCustomEvent()`documentation][1] pour plus d’informations.

[0]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection
[1]: https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent
[2]: http://www.w3schools.com/jsref/jsref_obj_date.asp
