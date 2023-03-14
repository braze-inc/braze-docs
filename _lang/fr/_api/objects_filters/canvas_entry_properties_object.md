---
nav_title: "Objet Propriétés d’entrées de Canvas"
article_title: Objet Propriétés d’entrées de Canvas de l’API
page_order: 2
page_type: reference
tool:
  - Canvas
description: "Cet article explique l’objet Propriétés d’entrées de Canvas de Braze."

---

# Spécification de l’objet Propriétés d’entrées de Canvas

Lorsque vous utilisez l’un des endpoints pour déclencher ou programmer un Canvas via l’API, vous pouvez fournir une carte des clés et des valeurs pour personnaliser les messages envoyés dès les premières étapes de votre Canvas, dans l’espace de nom `canvas_entry_properties`.

{% alert note %}
La limite maximale de taille de l’objet Propriétés d’entrées de Canvas est de 50 Ko. 
{% endalert %}

## Corps de l’objet

Ce corps d’objet contient un exemple de demande.

```json
"canvas_entry_properties": {"product_name" : "shoes", "product_price" : 79.99}
```

{% raw %}
Par exemple, une requête avec `"canvas_entry_properties": {"product_name" : "shoes", "product_price" : 79.99}` pourrait inclure le terme « chaussures » à un message en ajoutant ```{{canvas_entry_properties.${product_name}}}``` à la demande.
{% endraw %}
