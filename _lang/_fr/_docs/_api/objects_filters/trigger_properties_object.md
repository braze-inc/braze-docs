---
nav_title: "Objet Propriétés du déclencheur"
article_title: Objet Propriétés du déclencheur de l'API
page_order: 11
page_type: Référence
description: "Cet article explique les différents composants de l'objet Propriétés de Trigger."
tool: Campagnes
---

# Spécification des propriétés de déclencheur de l'objet

Lors de l'utilisation d'un des terminaux pour envoyer une campagne avec la livraison déclenchée par API, vous pouvez fournir une carte des clés et des valeurs pour personnaliser votre message.

Si vous faites une requête API qui contient un objet dans `"trigger_properties"`, les valeurs de cet objet peuvent alors être référencées dans votre modèle de message sous l'espace de noms api_trigger_properties.
{% raw %}
Par exemple, une requête avec ce qui suit pourrait ajouter le mot `"chaussures"` à un message en ajoutant `{{api_trigger_properties.${product_name}}}`.
{% endraw %}

```json
"trigger_properties" : {
  "product_name" : "shoes",
  "product_price" : 79.99
}
```

{% raw %}
L'objet "trigger_properties" et `api_trigger_properties. La syntaxe${product_name}` n'est prise en charge que dans Campaigns. Pour personnaliser les messages avec des clés et des valeurs à partir d'une requête de déclenchement d'API, utilisez l'objet [Propriétés d'entrée de Canvas](https://www.braze.com/docs/api/objects_filters/canvas_entry_properties_object/).
{% endraw %}


