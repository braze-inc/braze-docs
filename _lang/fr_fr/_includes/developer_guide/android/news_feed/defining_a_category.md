# Définir une catégorie de fil d’actualité

> Découvrez comment définir une catégorie de fil d'actualité pour le SDK Android de Braze.

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

## Définir une catégorie

Les instances du fil d’actualité Braze peuvent être configurées pour ne recevoir que des cartes d’une certaine « catégorie ». Cela permet l’intégration efficace de plusieurs flux de fils d’actualité au sein d’une seule application. Pour plus d'informations sur cette fonctionnalité, consultez nos [bonnes pratiques]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/reporting/) concernant le fil d'actualité.

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
