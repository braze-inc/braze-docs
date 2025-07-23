# Definir una categoría de canal de noticias

> Aprende a definir una categoría de fuente de noticias para el SDK de Android Braze.

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

## Definir una categoría

Las instancias de la fuente de noticias Braze pueden configurarse para que sólo reciban tarjetas de una determinada "categoría". Esto permite la integración efectiva de múltiples flujos de fuentes de noticias dentro de una única aplicación. Para más información sobre esta característica, consulta nuestras [mejores prácticas]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/reporting/) de la fuente de noticias

Las categorías de la fuente de noticias pueden definirse llamando a los siguientes métodos cuando cargas la fuente de noticias:

```xml
newsFeed.setCategories(CardCategory.ALL_CATEGORIES);
newsFeed.setCategories(CardCategory.ADVERTISING);
newsFeed.setCategories(CardCategory.ANNOUNCEMENTS);
newsFeed.setCategories(CardCategory.NEWS);
newsFeed.setCategories(CardCategory.SOCIAL);
newsFeed.setCategories(CardCategory.NO_CATEGORY);
```

También puedes rellenar una fuente con una combinación de categorías, como en el ejemplo siguiente:

```xml
newsFeed.setCategories:EnumSet.of(CardCategory.ANNOUNCEMENTS, CardCategory.NEWS);
```
