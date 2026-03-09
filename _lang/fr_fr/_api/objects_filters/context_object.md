---
nav_title: "Objet de contexte Canvas"
article_title: Objet API Canvas Context
page_order: 2
page_type: reference
alias: /api/objects_filters/canvas_entry_properties_object/
tool:
  - Canvas
description: "Cet article explique l'objet contextuel Braze Canvas."

---

# Objet de contexte Canvas

> Lors de l'utilisation de l'un des points de terminaison pour déclencher ou planifier un Canvas via l'API, vous pouvez fournir une carte de clés et de valeurs pour personnaliser les messages envoyés par les premières étapes de votre Canvas, dans l'espace de noms `context`.

{% alert note %}
L'objet contextuel a une taille maximale de 50 Ko.
{% endalert %}

## Corps de l’objet

Ce corps d’objet contient un exemple de demande.

```json
"context": {"product_name" : "shoes", "product_price" : 79.99}
```

{% raw %}
Par exemple, vous pouvez inclure`"context": {"product_name" : "shoes", "product_price" : 79.99}`  dans votre requête API, puis faire référence au mot « chaussures » dans votre message en ajoutant```{{context.${product_name}}}```  au modèle de message.
{% endraw %}
