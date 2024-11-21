---
nav_title: Enregistrer les achats
article_title: Enregistrer les achats pour Roku
platform: Roku
page_order: 3
page_type: reference
description: "Cette page fournit des méthodes pour journaliser les événements d’achat pour Roku via le SDK Braze."

---
 
# Enregistrer les achats

> Enregistrez les achats dans l’application afin que vous puissiez suivre vos revenus au fil du temps et entre leurs différentes sources, tout en segmentant vos utilisateurs selon leur valeur à vie.

Braze prend en charge les achats dans plusieurs devises. Les achats que vous effectuez dans une devise autre qu’USD seront affichés dans le tableau de bord en USD en fonction du taux de change à la date à laquelle ils ont été enregistrés.

Avant de procéder à la mise en œuvre, n'oubliez pas de consulter des exemples d'options de segmentation offertes par les événements personnalisés, les attributs personnalisés et les événements d'achat dans notre article sur les [meilleures pratiques.]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection)  Nous vous recommandons également de vous familiariser avec les [conventions de dénomination de nos événements]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

## Suivi des achats et des revenus

Pour utiliser cette fonction, ajoutez cet appel de méthode après un achat réussi dans votre application :

```brightscript
m.Braze.logPurchase("product_id", "currency_code", Double price, Integer quantity)
```

### Ajouter des propriétés

Vous pouvez ajouter des métadonnées sur les achats en transmettant un dictionnaire de propriétés avec vos informations d’achat.

Les propriétés sont définies comme des paires clé-valeur.  Les clés sont des objets `String` et les valeurs peuvent être `String` ou `Integer`.

```brightscript
m.Braze.logPurchase("product_id", "currency_code", Double price, Integer quantity, {"stringPropKey" : "stringPropValue", "intPropKey" : Integer intPropValue})
```

### Journaliser les achats au niveau de la commande
Si vous souhaitez enregistrer les achats au niveau de la commande plutôt qu'au niveau du produit, vous pouvez utiliser le nom de la commande ou la catégorie de commande comme `product_id`. Pour en savoir plus, reportez-vous aux [spécifications de l'objet de l'achat]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions). 

### API REST

Vous pouvez également utiliser notre API REST pour enregistrer les achats. Reportez-vous à la documentation de l'[API des utilisateurs]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data) pour plus de détails.

