---
nav_title: Définir une catégorie de flux d'actualités
article_title: Définition d'une catégorie de flux d'actualités pour Android/FireOS
page_order: 3
platform:
  - Android
  - Pare-feu
description: "Cet article de référence montre comment définir une catégorie de flux d'actualité dans votre application Android."
channel:
  - fil d'actualité
---

# Définition d'une catégorie de flux d'actualité

Les instances de Braze News Feed peuvent être configurées pour recevoir uniquement des cartes d'une certaine « catégorie ». Cela permet une intégration efficace de plusieurs flux RSS dans une seule application. Pour plus d'informations sur cette fonctionnalité, voir plus dans notre [Meilleures pratiques en matière de flux d'actualités][14]

Les catégories de flux d'actualités peuvent être définies en appelant les méthodes suivantes pendant que vous chargez le flux d'actualités :

```xml
newsFeed.setCategories(CardCategory.ALL_CATEGORIES);
newsFeed.setCategories(CardCategory.ADVERTISING);
newsFeed.setCategories(CardCategory.ANNOUNCEMENTS);
newsFeed.setCategories(CardCategory.NEWS);
newsFeed.setCategories(CardCategory.SOCIAL);
newsFeed.setCategories(CardCategory.NO_CATEGORY);
```

Vous pouvez également remplir un flux avec une combinaison de catégories comme dans l'exemple suivant :

```xml
newsFeed.setCategories:EnumSet.of(CardCategory.ANNOUNCEMENTS, CardCategory.NEWS);
```


[14]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/reporting/
