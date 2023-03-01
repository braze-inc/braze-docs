---
nav_title: "Objet Propriétés du déclencheur"
article_title: Objet Propriétés du déclencheur de l’API
page_order: 11
page_type: reference
description: "Cet article explique les différents composants de l’objet Propriétés du déclencheur."
tool: Campaigns

---

# Spécification de l’objet Propriétés du déclencheur

Lorsque vous utilisez l’un des endpoints pour envoyer une campagne avec une livraison déclenchée par API, vous pouvez fournir un mappage de clés et des valeurs pour personnaliser votre message.

Si vous faites une demande API qui contient un objet dans `"trigger_properties"`, les valeurs de cet objet peuvent alors être référencées dans votre modèle de message sous l’espace de nom `api_trigger_properties`.
{% raw %}
For example, a request with the following could add the word `"shoes"` to a message by adding `{{api_trigger_properties.${product_name}}}`.
{% endraw %}

```json
"trigger_properties" : {
  "product_name" : "shoes",
  "product_price" : 79.99,
  "details" : {
    "color" : "red",
    "size" : {
      "numerical" : 10,
      "country" : "US"
    }
  },
  "related_skus": ["123", "456", "789"]
}
```

{% raw %}
The `trigger_properties` object and `api_trigger_properties.${product_name}` syntax is only supported in campaigns. To customize messages with keys and values from an API trigger request, use the [Canvas Entry Properties Object](https://www.braze.com/docs/api/objects_filters/canvas_entry_properties_object/).
{% endraw %}



