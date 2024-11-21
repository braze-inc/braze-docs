---
nav_title: Enregistrer les achats
article_title: Enregistrer les achats pour le Web
platform: Web
page_order: 4
page_type: reference
description: "Cet article décrit comment enregistrer des achats et ajouter des propriétés à ces achats pour le Web."

---
 
# Enregistrer les achats

> Enregistrez les achats dans l’application afin que vous puissiez suivre vos revenus au fil du temps et entre leurs différentes sources, tout en segmentant vos utilisateurs selon leur valeur à vie. 

Braze prend en charge les achats dans plusieurs devises. Les achats que vous effectuez dans une devise autre qu’USD seront affichés dans le tableau de bord en USD en fonction du taux de change à la date à laquelle ils ont été enregistrés.

Avant de procéder à la mise en œuvre, n'oubliez pas de consulter les exemples d'options de segmentation offertes par les événements personnalisés, les attributs personnalisés et les événements d'achat dans nos [meilleures pratiques.]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection)

Pour utiliser cette fonctionnalité, ajoutez l'appel [`logPurchase()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logpurchase) après un achat réussi dans votre application. Notez que `quantity` doit être inférieur ou égal à 100.

```javascript
braze.logPurchase(product_id, price, "USD", quantity);
```

## Ajouter des propriétés

Vous pouvez ajouter des [métadonnées](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logpurchase) sur les achats en transmettant un [tableau de propriétés d'événement]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#nested-objects) ou en transmettant un objet de paires clé-valeur contenant vos informations d'achat. 

#### Formatage de l’objet

Les clés sont des objets `string` et les valeurs peuvent être des objets `string`, `numeric`, `boolean` ou `Date`.

```javascript
braze.logPurchase(product_id, price, "USD", quantity, {key: "value"});
```

#### Journaliser les achats au niveau de la commande
Si vous souhaitez enregistrer les achats au niveau de la commande plutôt qu'au niveau du produit, vous pouvez utiliser le nom de la commande ou la catégorie de commande comme `product_id`. Pour en savoir plus, reportez-vous aux [spécifications de l'objet de l'achat]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions). 

## API REST

Vous pouvez également utiliser notre API REST pour enregistrer les achats. Reportez-vous à la documentation de l'[API des utilisateurs]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data) pour plus de détails.

