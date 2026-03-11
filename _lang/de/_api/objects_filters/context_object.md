---
nav_title: "Canvas-Kontext-Objekt"
article_title: API-Canvas-Kontext-Objekt
page_order: 2
page_type: reference
alias: /api/objects_filters/canvas_entry_properties_object/
tool:
  - Canvas
description: "Dieser Artikel erläutert das Braze-Canvas-Kontextobjekt."

---

# Canvas-Kontext-Objekt

> Wenn Sie einen der Endpunkte zum Triggern oder Zeitplanen eines Canvas über die API verwenden, können Sie im Namensraum `context` eine Abbildung von Schlüsseln und Werten bereitstellen, um Nachrichten anzupassen, die von den ersten Schritten Ihres Canvas gesendet werden.

{% alert note %}
Das Kontext-Objekt hat eine maximale Größe von 50 KB.
{% endalert %}

## Objektkörper

Dieser Objektkörper enthält eine Beispielanfrage.

```json
"context": {"product_name" : "shoes", "product_price" : 79.99}
```

{% raw %}
Sie können beispielsweise in Ihre `"context": {"product_name" : "shoes", "product_price" : 79.99}`API-Anfrage einfügen und dann in Ihrer Nachricht das Wort „Schuhe” referenzieren, indem Sie```{{context.${product_name}}}```zum Template der Nachricht hinzufügen.
{% endraw %}
