---
nav_title: "Objet Propriétés du déclencheur"
article_title: Objet Propriétés du déclencheur de l’API
page_order: 11
page_type: reference
description: "Cet article de référence explique les différents composants de l’objet Propriétés du déclencheur."
tool: Campaigns

---

# Objet Propriétés du déclencheur

> Lorsque vous utilisez l’un des endpoints pour envoyer une campagne avec une livraison déclenchée par API, vous pouvez fournir un mappage de clés et des valeurs pour personnaliser votre message.

Si vous faites une demande API qui contient un objet dans `trigger_properties`, les valeurs de cet objet peuvent alors être référencées dans votre modèle de message sous l’espace de nom `api_trigger_properties`. Par exemple, une demande contenant les éléments suivants pourrait ajouter le mot `"shoes"` à un message en ajoutant {% raw %}`{{api_trigger_properties.${product_name}}}`{% endraw %}. 

Notez que si les propriétés des déclencheurs peuvent être intégrées dans les messages, elles ne sont pas automatiquement stockées dans le profil utilisateur par défaut.

{% alert note %}
L'objet `trigger_properties` et la syntaxe {% raw %}`api_trigger_properties.${product_name}`{% endraw %} ne sont pris en charge que dans les campagnes. Pour personnaliser les messages avec des clés et des valeurs à partir d’une requête de déclenchement par l’API pour Canvas, utilisez l’[objet de propriétés d’entrées de Canvas]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/). La taille maximale de l'objet `trigger_properties` est de 50 ko.
{% endalert %}

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


