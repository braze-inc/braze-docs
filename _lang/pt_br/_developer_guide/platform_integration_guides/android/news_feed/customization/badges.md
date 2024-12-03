---
nav_title: Ícones
article_title: Emblemas de feed de notícias para Android e FireOS
page_order: 3.2
platform: 
  - Android
  - FireOS
description: "Este artigo de referência aborda como adicionar emblemas do Feed de notícias e solicitar contagens de cartões não lidos do Feed de notícias em seu aplicativo para Android ou FireOS."
channel:
  - news feed
  
---

# Ícones

> Este artigo de referência aborda como adicionar emblemas do Feed de notícias e solicitar contagens de cartões não lidos do Feed de notícias em seu aplicativo para Android ou FireOS.

{% alert note %}
O feed de notícias será descontinuado. A Braze recomenda que os clientes que usam nossa ferramenta de feed de notícias migrem para o canal de envio de mensagens Content Cards - é mais flexível, personalizável e confiável. Para saber mais, consulte o [guia de migração]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/).
{% endalert %}

## Solicitação de contagem de cartões não lidos do Feed de notícias

Você pode solicitar o número de cartões não lidos a qualquer momento, ligando para o telefone:

```java
getUnreadCardCount()
```

Consulte nosso [KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.events/-feed-updated-event/get-unread-card-count.html) para obter mais informações.

