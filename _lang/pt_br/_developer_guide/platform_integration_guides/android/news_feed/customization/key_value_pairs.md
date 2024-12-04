---
nav_title: Pares de chave-valor
article_title: Pares de Chave-Valor do feed de notícias para Android e FireOS
page_order: 3
platform: 
  - Android
  - FireOS
description: "Este artigo de referência cobre como usar pares de chave/valor do feed de notícias em seu aplicativo Android ou FireOS."
channel:
  - news feed

---

# Pares chave-valor

> Este artigo de referência cobre como usar pares de chave/valor do feed de notícias em seu aplicativo Android ou FireOS.

{% alert note %}
O feed de notícias será descontinuado. A Braze recomenda que os clientes que usam nossa ferramenta de feed de notícias migrem para o canal de envio de mensagens Content Cards - é mais flexível, personalizável e confiável. Para saber mais, consulte o [guia de migração]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/).
{% endalert %}

Objetos `Card` podem carregar pares chave-valor como `extras`. Esses objetos podem ser usados para enviar dados com um `Card` para processamento adicional pelo aplicativo.

Chame o seguinte em um objeto `Card` para recuperar seus extras:

{% tabs %}
{% tab JAVA %}

```java
Map<String, String> getExtras()
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
extras: Map<String, String>
```

{% endtab %}
{% endtabs %}
