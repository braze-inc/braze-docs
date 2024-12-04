---
nav_title: Atualizando o feed
article_title: Atualizando o feed de notícias para Android e FireOS
page_order: 7
platform: 
  - Android
  - FireOS
description: "Este artigo de referência mostra como atualizar o feed de notícias em seu aplicativo para Android ou FireOS."
channel:
  - news feed

---

# Atualizar o feed

> Este artigo de referência mostra como atualizar o feed de notícias em seu aplicativo para Android ou FireOS.

{% alert note %}
O feed de notícias será descontinuado. A Braze recomenda que os clientes que usam nossa ferramenta de feed de notícias migrem para o canal de envio de mensagens Content Cards - é mais flexível, personalizável e confiável. Para saber mais, consulte o [guia de migração]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/).
{% endalert %}

Você pode enfileirar uma atualização manual do feed de notícias da Braze a qualquer momento, ligando para:

```java
Braze.requestFeedRefresh()
```

Consulte nosso [KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/request-feed-refresh.html) para obter mais informações.


