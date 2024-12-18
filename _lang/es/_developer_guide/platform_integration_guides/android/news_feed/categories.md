---
nav_title: Definir una categoría de canal de noticias
article_title: Definir una categoría de canal de noticias para Android y FireOS
page_order: 3
platform: 
  - Android
  - FireOS
description: "Este artículo de referencia muestra cómo definir una categoría de fuente de noticias en tu aplicación Android o FireOS."
channel:
  - news feed
  
---

# Definir una categoría de canal de noticias

Este artículo de referencia muestra cómo definir una categoría de fuente de noticias en tu aplicación Android o FireOS.

{% alert note %}
Vamos a dejar de usar el canal de noticias. Braze recomienda a los clientes que utilizan nuestra herramienta de fuente de noticias que se pasen a nuestro canal de mensajería de tarjetas de contenido: es más flexible, personalizable y fiable. Para más información, consulta la [guía de migración]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/).
{% endalert %}

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


