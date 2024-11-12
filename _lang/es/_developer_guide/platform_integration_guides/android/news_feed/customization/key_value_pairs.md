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

{% alert note %}
Vamos a dejar de usar el canal de noticias. Braze recomienda a los clientes que utilizan nuestra herramienta de fuente de noticias que se pasen a nuestro canal de mensajería de tarjetas de contenido: es más flexible, personalizable y fiable. Para más información, consulta la [guía de migración]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/).
{% endalert %}

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
