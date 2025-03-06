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

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

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
