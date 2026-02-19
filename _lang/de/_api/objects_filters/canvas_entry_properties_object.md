---
nav_title: "Canvas Entry Eigenschaften Objekt"
article_title: API Canvas Eingang-Eigenschaften Objekt
page_order: 2
page_type: reference
tool:
  - Canvas
description: "Dieser Artikel erläutert das Objekt Braze-Canvas Eingang-Eigenschaften."

---

# Canvas Entry Eigenschaften Objekt

> Wenn Sie einen der Endpunkte zum Triggern oder Zeitplanen eines Canvas über die API verwenden, können Sie im Namensraum `canvas_entry_properties` eine Abbildung von Schlüsseln und Werten bereitstellen, um Nachrichten anzupassen, die von den ersten Schritten Ihres Canvas gesendet werden.

{% alert note %}
Das Objekt Canvas Entry-Eigenschaften hat eine maximale Größe von 50 KB.
{% endalert %}

## Objektkörper

Dieser Objektkörper enthält eine Beispielanfrage.

```json
"canvas_entry_properties": {"product_name" : "shoes", "product_price" : 79.99}
```

{% raw %}
Zum Beispiel könnte eine Anfrage mit `"canvas_entry_properties": {"product_name" : "shoes", "product_price" : 79.99}` das Wort "Schuhe" zu einer Nachricht hinzufügen, indem Sie ```{{canvas_entry_properties.${product_name}}}``` zur Anfrage hinzufügen.
{% endraw %}
