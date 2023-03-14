---
nav_title: Définir une catégorie de fil d'actualité
article_title: Définir une catégorie de fil d'actualité pour Android et FireOS
page_order: 3
platform: 
  - Android
  - FireOS
description: "Cet article de référence montre comment définir une catégorie de fil d'actualité dans votre application Android ou FireOS."
channel:
  - fil d’actualité
  
---

# Définir une catégorie de fil d’actualités

{% alert note %}
Le Fil d’actualité est obsolète. Braze recommande aux clients qui utilisent notre outil de fil d’actualités de passer à notre canal de communication de cartes de contenu - il est plus flexible, plus personnalisable et plus fiable. Consultez le [guide de migration]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) pour en savoir plus.
{% endalert %}

Les instances du fil d'actualité Braze peuvent être configurées pour ne recevoir que des cartes d’une certaine « catégorie ». Cela permet l’intégration efficace de plusieurs flux de fils d'actualité au sein d’une seule application. Pour plus d’informations sur cette fonctionnalité, consultez nos [meilleures pratiques][14] concernant le fil d'actualité

Les catégories de fil d'actualité peuvent être définies en appelant les méthodes suivantes lorsque vous chargez le fil d'actualité :

```xml
newsFeed.setCategories(CardCategory.ALL_CATEGORIES);
newsFeed.setCategories(CardCategory.ADVERTISING);
newsFeed.setCategories(CardCategory.ANNOUNCEMENTS);
newsFeed.setCategories(CardCategory.NEWS);
newsFeed.setCategories(CardCategory.SOCIAL);
newsFeed.setCategories(CardCategory.NO_CATEGORY);
```

Vous pouvez également remplir un flux avec une combinaison de catégories comme dans l’exemple suivant :

```xml
newsFeed.setCategories:EnumSet.of(CardCategory.ANNOUNCEMENTS, CardCategory.NEWS);
```


[14]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/reporting/
