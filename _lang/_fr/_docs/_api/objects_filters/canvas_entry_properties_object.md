---
nav_title: "Objet Propriétés de l'entrée de canvas"
article_title: Objet Propriétés de l'entrée de Canvas API
page_order: 2
page_type: Référence
tool:
  - Toile
description: "Cet article explique les Propriétés de l'entrée de Braze Canvas ."
---

# Spécification des propriétés de l'entrée de la toile

Lorsque vous utilisez l'un des points de terminaison pour déclencher ou planifier un Canvas via l'API, vous pouvez fournir une carte des clés et des valeurs pour personnaliser les messages envoyés par les premières étapes de votre Canvas, dans l'espace de noms `canvas_entry_properties`.

## Corps de l'objet

Ce corps d'objet contient une requête d'exemple.

```json
"canvas_entry_properties": {"product_name" : "shoes", "product_price" : 79.99}
```
{% raw %}
Par exemple, une requête avec `"canvas_entry_properties": {"product_name" : "shoes", "product_price" : 79. 9}` pourrait ajouter le mot "chaussures" à un message en ajoutant `{{canvas_entry_properties.${product_name}}}` à la requête.
{% endraw %}
