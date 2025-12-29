---
nav_title: Migration des flux de données vers les codes de promotion
article_title: Migration des flux de données vers les codes de promotion
page_order: 0
description: "Cet article de référence fournit des conseils sur la migration des flux de données vers les codes de promotion."
---

# Migration des flux de données vers les codes de promotion

{% alert note %}
Les flux de données sont obsolètes. Braze recommande à ses clients qui utilisent les flux de données de passer aux listes de codes de promotion.
{% endalert %}

> Cette page vous guide dans la migration des flux de données vers les codes de promotion. Il s'agit d'un processus simple qui implique la création manuelle de listes de codes de promotion avec les informations de vos flux de données et la mise à jour des références de vos messages en conséquence.

## Caractéristiques et fonctionnalités

Il existe quelques différences entre les listes de codes de promotion et les flux de données.

| Fonctionnalité          | Codes de promotion | Flux de données   |
|------------------|-----------------|--------------|
| Descriptions     | Oui             | Non           |
| Dates d'expiration | Oui             | Non           |
| Méthode de création  | Téléchargement d'un fichier CSV | Coller du texte |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Comment migrer

Pour remplacer un flux de données par une liste de codes de promotion, procédez comme suit : 

1. Allez dans **Paramètres des données** et sélectionnez **Créer une liste de codes de promotion**.
2. [Établissez votre liste de codes de promotion]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes).
3. Accédez à vos messages qui faisaient précédemment référence au flux de données et mettez-les à jour pour utiliser la liste des codes de promotion.