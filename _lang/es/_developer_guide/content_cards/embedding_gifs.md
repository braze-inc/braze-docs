---
nav_title: Incrustar GIF
article_title: Incrustar GIF en tarjetas de contenido
page_order: 5
description: "Aprende a incrustar GIF en tarjetas de contenido utilizando el SDK de Braze."
channel:
  - content cards
platform:
  - Android
  - Swift
  - Web
  - FireOS
---

# Incrustar GIF en tarjetas de contenido

> Aprende a incrustar GIF en tarjetas de contenido utilizando el SDK de Braze.

{% alert note %}
Para los SDK de envoltura que no aparecen en la lista, utiliza el método nativo de Android o SWIFT correspondiente. Ten en cuenta que los SDK de Android y Swift Braze no admiten GIF animados de forma nativa, por lo que deberás implementar los GIF de las tarjetas de contenido utilizando herramientas de terceros.
{% endalert %}

{% sdktabs %}
{% sdktab web %}
La compatibilidad con GIF está incluida por defecto en la integración del SDK Web.
{% endsdktab %}

{% sdktab android %}
{% multi_lang_include developer_guide/android/_global/gifs.md %}
{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/gifs.md %}
{% endsdktab %}
{% endsdktabs %}
