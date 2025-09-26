---
nav_title: Incrustar GIFs
article_title: Incrustar GIF en tarjetas de contenido
page_order: 5
description: "Aprende a incrustar GIFs en tarjetas de contenido utilizando el SDK de Braze."
channel:
  - content cards
platform:
  - Android
  - Swift
  - Web
  - FireOS
---

# Incrustar GIF en tarjetas de contenido

> Aprende a incrustar GIFs en tarjetas de contenido utilizando el SDK de Braze.

{% alert note %}
Para los SDK envoltorio que no aparecen en la lista, utiliza en su lugar el método nativo de Android o Swift correspondiente. Ten en cuenta que los SDK Braze de Android y Swift no admiten GIF animados de forma nativa, por lo que deberás implementar GIF de tarjeta de contenido utilizando herramientas de terceros.
{% endalert %}

{% sdktabs %}
{% sdktab android %}
{% multi_lang_include developer_guide/android/_global/gifs.md %}
{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/gifs.md %}
{% endsdktab %}

{% sdktab web %}
En este momento, los GIF de tarjeta de contenido no son compatibles con el SDK de Web Braze.
{% endsdktab %}
{% endsdktabs %}
