---
nav_title: Pares clave-valor
article_title: Pares clave-valor del canal de noticias para Android y FireOS
page_order: 3
platform: 
  - Android
  - FireOS
description: "Este artículo de referencia explica cómo utilizar los pares clave-valor de la fuente de noticias en tu aplicación Android o FireOS."
channel:
  - news feed

---

# Pares clave-valor

> Este artículo de referencia explica cómo utilizar los pares clave-valor de la fuente de noticias en tu aplicación Android o FireOS.

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

Los objetos `Card` pueden llevar opcionalmente pares clave-valor como `extras`. Se pueden utilizar para enviar datos hacia abajo con un `Card` para su posterior manipulación por parte de la aplicación.

Llama a lo siguiente en un objeto `Card` para recuperar sus extras:

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
