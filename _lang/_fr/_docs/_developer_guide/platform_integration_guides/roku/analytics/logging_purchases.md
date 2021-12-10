---
nav_title: Achats de journalisation
article_title: Achats de journalisation pour Roku
platform: Roku
page_order: 3
page_type: Référence
description: "Cette page fournit des méthodes pour enregistrer les événements d'achat via le Braze SDK."
---

# Achats de journalisation

Enregistrez vos achats dans l'application afin de pouvoir suivre vos revenus au fil du temps et à travers les sources de revenus. ainsi que segmenter vos utilisateurs par leur valeur à vie.

Braze prend en charge les achats dans plusieurs devises. Les achats que vous rapportez dans une devise autre que le dollar seront affichés dans le tableau de bord en USD en fonction du taux de change à la date à laquelle ils ont été déclarés.

Avant l'implémentation, assurez-vous d'examiner les exemples d'options de segmentation offertes par les événements personnalisés vs. attributs personnalisés par rapport aux événements d'achat dans notre section [Meilleures pratiques][3]. Vous devriez également consulter nos notes sur [les conventions de nommage des événements]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

## Suivi des achats et des revenus

Pour utiliser cette fonctionnalité, ajoutez cette méthode d'appel après un achat réussi dans votre application :

```javascript
m.Braze.logPurchase("PURCHASE_NAME", "CURRENCY_CODE", double prix, quantité entière)
```

### Ajout de propriétés

Vous pouvez ajouter des métadonnées sur les achats en passant un dictionnaire de propriétés avec vos informations d'achat.

Les propriétés sont définies comme des paires clé-valeur.  Les clés sont des objets `String` et les valeurs peuvent être `String` ou `Integer`.

```javascript
m.Braze.logPurchase("PURCHASE_NAME", "CURRENCY_CODE", double prix, quantité entière, {"stringPropKey" : "stringPropValue", "intPropKey" : Integer intPropValue})
```

### API REST

Vous pouvez également utiliser notre API REST pour enregistrer vos achats. Reportez-vous à la documentation [de l'API utilisateur][2] pour plus de détails.

[2]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[3]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection
