---
nav_title: Achats de journalisation
article_title: Achats de journalisation pour le Web
platform: Web
page_order: 4
page_type: Référence
description: "Cet article décrit comment enregistrer les achats via le Braze SDK."
---

# Journalisation des achats pour le web

Enregistrez vos achats dans l'application afin de pouvoir suivre vos revenus au fil du temps et à travers les sources de revenus. ainsi que segmenter vos utilisateurs par leur valeur à vie.

Braze prend en charge les achats dans plusieurs devises. Les achats que vous rapportez dans une devise autre que le dollar seront affichés dans le tableau de bord en USD en fonction du taux de change à la date à laquelle ils ont été déclarés.

Avant l'implémentation, assurez-vous d'examiner les exemples d'options de segmentation offertes par les événements personnalisés vs. attributs personnalisés par rapport aux événements d'achat dans notre section [Meilleures pratiques][3].

Pour utiliser cette fonctionnalité, ajoutez cette méthode d'appel après un achat réussi dans votre application :

```javascript
appboy.logPurchase(productId, prix, "USD", quantité);
```

Voir les [JSdocs][8] pour plus d'informations. La quantité doit être inférieure ou égale à 100.

## Ajout de propriétés

Vous pouvez ajouter des métadonnées sur les achats en passant un objet de paires clé-valeur avec vos informations d'achat. Les clés sont des objets `chaîne` et les valeurs peuvent être `chaîne`, `numériques`, `booléens`, ou `objets Date`.

```javascript
appboy.logPurchase(productId, prix, "USD", quantité, {key: "value"});
```

Voir les [Jsdocs][8] pour plus d'informations.

## API REST

Vous pouvez également utiliser notre API REST pour enregistrer vos achats. Reportez-vous à la [documentation de l'API utilisateur][1] pour plus de détails.

[1]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[3]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection
[8]: https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html#.logPurchase
[8]: https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html#.logPurchase
