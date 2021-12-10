---
nav_title: Événements personnalisés de suivi
article_title: Suivi des événements personnalisés pour le Web
platform: Web
page_order: 2
page_type: Référence
description: "Cet article couvre la façon de suivre les événements personnalisés via le Braze SDK."
---

# Suivi des événements personnalisés pour le web

Vous pouvez enregistrer des événements personnalisés dans Braze pour en savoir plus sur les habitudes d'utilisation de votre application et pour segmenter vos utilisateurs par leurs actions sur le tableau de bord.

Avant l'implémentation, assurez-vous d'examiner les exemples d'options de segmentation offertes par les événements personnalisés vs. attributs personnalisés par rapport aux événements d'achat dans notre section [Meilleures pratiques][]. Vous devriez également consulter nos notes sur [les conventions de nommage des événements]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

```javascript
appboy.logCustomEvent(VOTRE_EVENT_NAME);
```

Consultez la documentation [logCustomEvent][1] pour plus d'informations.

## Ajout de propriétés {#properties-events}

Vous pouvez éventuellement ajouter des métadonnées sur les événements personnalisés en passant un objet de propriétés avec votre événement personnalisé.

Les propriétés sont définies comme des paires clé-valeur.  Les clés sont des chaînes de caractères et les valeurs peuvent être `chaîne`, `numérique`, `booléen`, ou [`Date`][2] objets.

```javascript
appboy.logCustomEvent(VOTRE_EVENT_NAME, {key: 'value'});
```

Consultez la documentation [logCustomEvent][1] pour plus d'informations.

[Meilleures pratiques]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection
[1]: https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html#.logCustomEvent
[2]: http://www.w3schools.com/jsref/jsref_obj_date.asp
