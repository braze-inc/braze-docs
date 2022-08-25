---
nav_title: Enregistrer les achats
article_title: Enregistrer les achats pour le Web
platform: Web
page_order: 4
page_type: reference
description: "Cet article décrit comment enregistrer les achats pour le Web."

---

# Enregistrer les achats pour le Web

Enregistrez les achats dans l’application afin que vous puissiez suivre vos revenus au fil du temps et entre leurs différentes sources, tout en segmentant vos utilisateurs selon leur valeur à vie. Braze prend en charge les achats dans plusieurs devises. Les achats que vous effectuez dans une devise autre qu’USD seront affichés dans le tableau de bord en USD en fonction du taux de change à la date à laquelle ils ont été enregistrés.

Avant l’implémentation, assurez-vous d’étudier des exemples des options de segmentation offertes par les événements personnalisés, les attributs personnalisés et les événements d’achat dans nos [bonnes pratiques][3].

Pour utiliser cette fonction, appelez [`logPurchase()`][8] après un achat réussi dans votre application. Notez que `quantity` doit être inférieur ou égal à 100.

```javascript
braze.logPurchase(productId, price, "USD", quantity);
```

## Ajouter des propriétés

Vous pouvez ajouter des [métadonnées][8] sur les achats en transmettant un objet de paire clé-valeur avec vos informations d’achat. Les clés sont des objets `string` et les valeurs peuvent être des objets `string`, `numeric`, `boolean` ou `Date`.

```javascript
braze.logPurchase(productId, price, "USD", quantity, {key: "value"});
```

## API REST

Vous pouvez également utiliser notre API REST pour enregistrer les achats. Reportez-vous à la documentation de l’[API utilisateur][1] pour plus de détails.

[1]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[3]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection
[8]: https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logpurchase
