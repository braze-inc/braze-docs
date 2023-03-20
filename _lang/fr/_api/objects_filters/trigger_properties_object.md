---
nav_title: "Objet Propriétés du déclencheur"
article_title: Objet Propriétés du déclencheur de l’API
page_order: 11
page_type: reference
description: "Cet article de référence explique les différents composants de l’objet Propriétés du déclencheur."
tool: Campagnes

---

# Spécification de l’objet Propriétés du déclencheur

Lorsque vous utilisez l’un des endpoints pour envoyer une campagne avec une livraison déclenchée par API, vous pouvez fournir un mappage de clés et des valeurs pour personnaliser votre message.

Si vous faites une demande API qui contient un objet dans `"trigger_properties"`, les valeurs de cet objet peuvent alors être référencées dans votre modèle de message sous l’espace de nom `api_trigger_properties`.
{% raw %}
Par exemple, une requête avec les éléments suivants pourrait inclure le terme `"shoes"` à un message en ajoutant `{{api_trigger_properties.${product_name}}}`.
{% endraw %}

## Corps de l’objet

```json
{
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
}
```

{% raw %}
L’objet `trigger_properties` et la syntaxe `api_trigger_properties.${product_name}` sont uniquement pris en charge dans les campagnes. Pour personnaliser les messages avec des clés et des valeurs à partir d’une demande de déclenchement par l’API, utilisez l’[objet de propriétés d’entrées de Canvas](https://www.braze.com/docs/api/objects_filters/canvas_entry_properties_object/).
{% endraw %}


