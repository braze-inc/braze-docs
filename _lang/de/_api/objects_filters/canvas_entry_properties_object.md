---
nav_title: "Objekt Canvas Entry Properties"
article_title: API Canvas Eintrag Eigenschaften Objekt
page_order: 2
page_type: reference
tool:
  - Canvas
description: "Dieser Artikel erklärt das Objekt Braze Canvas entry properties."

---

# Canvas Eintrag Eigenschaften Objekt

> Wenn Sie einen der Endpunkte zum Auslösen oder Planen eines Canvas über die API verwenden, können Sie im Namespace `canvas_entry_properties` eine Zuordnung von Schlüsseln und Werten bereitstellen, um die von den ersten Schritten Ihres Canvas gesendeten Nachrichten anzupassen.

{% alert note %}
Das Objekt Canvas entry properties hat eine maximale Größe von 50 KB.
{% endalert %}

## Objektkörper

Dieser Objektkörper enthält eine Beispielanfrage.

```json
"canvas_entry_properties": {"product_name" : "shoes", "product_price" : 79.99}
```

{% raw %}
Zum Beispiel könnte eine Anfrage mit `"canvas_entry_properties": {"product_name" : "shoes", "product_price" : 79.99}` das Wort "Schuhe" zu einer Nachricht hinzufügen, indem Sie ```{{canvas_entry_properties.${product_name}}}``` zur Anfrage hinzufügen.
{% endraw %}
