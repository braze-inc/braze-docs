---
nav_title: "Tableau d'objets"
article_title: "Tableau d'objets"
alias: "/array_of_objects/"
page_order: 0
page_type: reference
description: "Cet article de référence traite de l'utilisation d'un tableau d'objets comme type de données pour les attributs personnalisés, y compris les limitations et les exemples d'utilisation." 
---

# Tableau d'objets

> Cette page explique comment utiliser un tableau d'objets pour regrouper des attributs connexes. Par exemple, vous pouvez avoir un groupe d'objets animaux, d'objets chansons et d'objets comptes qui appartiennent tous à un même utilisateur. Ces tableaux d'objets peuvent être utilisés pour personnaliser votre envoi de messages avec Liquid, ou pour créer des segments d'audience si l'un des éléments d'un objet correspond aux critères.

{% multi_lang_include nested_attribute_objects/supported_data_types.md %}

## Limites

- Les tableaux d'objets sont destinés aux attributs personnalisés envoyés par l'API. Les téléchargements CSV ne sont pas pris en charge. En effet, les virgules dans le fichier CSV seront interprétées comme un séparateur de colonnes et les virgules dans les valeurs provoqueront des erreurs d'analyse. 
- Les tableaux d'objets n'ont pas de limite quant au nombre d'éléments, mais leur taille maximale est de 100 Ko.
- Tous les partenaires Braze ne prennent pas en charge les tableaux d'objets. Consultez la [documentation du partenaire]({{site.baseurl}}/partners/home) pour savoir si l'intégration prend en charge cette fonctionnalité.

La mise à jour ou la suppression d'éléments d'un tableau nécessite l'identification de l'élément par sa clé et sa valeur ; pensez donc à inclure un identifiant unique pour chaque élément du tableau. L'unicité est limitée au tableau et est utile si vous souhaitez mettre à jour et supprimer des objets spécifiques de votre tableau. Cette règle n'est pas appliquée par Braze.

{% alert tip %}
Pour plus d'informations sur l'utilisation de tableaux d'objets pour les objets d'attributs utilisateur, reportez-vous à [Objet d'attributs utilisateur]({{site.baseurl}}/api/objects_filters/user_attributes_object).
{% endalert %}

## Exemple d'API

{% tabs local %}
{% tab Create %}

Voici un exemple de `/users/track` avec un tableau de `pets`. Pour capturer les propriétés des animaux, envoyez une requête API qui répertorie `pets` comme un tableau d'objets. Notez que chaque objet s'est vu attribuer un `id` unique qui peut être référencé ultérieurement lors des mises à jour.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "pets": [
        {
          "id": 1,
          "type": "dog",
          "breed": "beagle",
          "name": "Gus"
        },
        {
          "id": 2,
          "type": "cat",
          "breed": "calico",
          "name": "Gerald"
        }
      ]
    }
  ]
}
```
{% endtab %}
{% tab Add %}

Ajoutez un autre élément au tableau à l'aide de l'opérateur `$add`. L'exemple suivant montre l'ajout de trois objets animaux supplémentaires au tableau d'objets de l'utilisateur `pets`.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "pets": {
        "$add": [
          {
            "id": 3,
            "type": "dog",
            "breed": "corgi",
            "name": "Doug"
          },
          {
            "id": 4,
            "type": "fish",
            "breed": "salmon",
            "name": "Larry"
          },
           {
            "id": 5,
            "type": "bird",
            "breed": "parakeet",
            "name": "Mary"
          }
        ]
      }
    }
  ]
}
```
{% endtab %}
{% tab Update %}

Mettez à jour les valeurs d'objets spécifiques dans un tableau en utilisant le paramètre `_merge_objects` et l'opérateur `$update`. Comme pour les mises à jour d'objets d'[attributs personnalisés]({{site.baseurl}}/nested_custom_attribute_support/#api-request-body) simples [imbriqués]({{site.baseurl}}/nested_custom_attribute_support/#api-request-body), il s'agit d'une fusion en profondeur.

Notez que `$update` ne peut pas être utilisé pour supprimer une propriété imbriquée d'un objet à l'intérieur d'un tableau. Pour ce faire, vous devez supprimer l'élément entier du tableau, puis ajouter l'objet sans cette clé spécifique (en utilisant une combinaison de `$remove` et `$add`).

L'exemple suivant montre la mise à jour de la propriété `breed` en `goldfish` pour l'objet dont l'adresse `id` est `4`. Cet exemple de demande met également à jour l'objet dont l'adresse `id` est égale à `5` avec une nouvelle adresse `name` de `Annette`. Étant donné que le paramètre `_merge_objects` est défini sur `true`, tous les autres champs de ces deux objets restent identiques.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "_merge_objects": true,
      "pets": {
        "$update": [
          {
            "$identifier_key": "id",
            "$identifier_value": 4,
            "$new_object": {
              "breed": "goldfish"
            }
          },
          {
            "$identifier_key": "id",
            "$identifier_value": 5,
            "$new_object": {
              "name": "Annette"
            }
          }
        ]
      }
    }
  ]
}
```

{% alert warning %}
Vous devez attribuer la valeur "true" à `_merge_objects`, sinon vos objets seront écrasés. `_merge_objects` est "false" par défaut.
{% endalert %}

{% endtab %}
{% tab Remove %}

Supprimez des objets d'un tableau en utilisant l'opérateur `$remove` en combinaison avec une clé (`$identifier_key`) et une valeur (`$identifier_value`) correspondantes.

L'exemple suivant montre la suppression de tout objet du tableau d'objets `pets` qui possède un `id` avec la valeur `1`, un `id` avec la valeur `2`, et un `type` avec la valeur `dog`. S'il existe plusieurs objets dont la valeur `type` est `dog`, tous les objets correspondants seront supprimés.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "pets": {
        "$remove": [
          // Remove by ID
          {
            "$identifier_key": "id",
            "$identifier_value": 1
          },
          {
            "$identifier_key": "id",
            "$identifier_value": 2
          },
          // Remove any dog
          {
            "$identifier_key": "type",
            "$identifier_value": "dog"
          }
        ]
      }
    }
  ]
}
```
{% endtab %}
{% endtabs %}

### Horodatage

Lorsque vous incluez des champs tels que des horodatages dans un tableau d'objets, utilisez le format `$time` au lieu de chaînes de caractères simples ou d'entiers d'époque Unix.

```json
{
  "attributes": [
    {
      "external_id": "user123",
      "purchases": [
        {
          "item_name": "T-shirt",
          "price": 19.99,
          "purchase_time": {
            "$time": "2020-05-28"
          }
        }
      ]
    }
  ]
}
```

{% alert tip %}
Pour plus d'informations, voir [Attributs personnalisés imbriqués]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support).
{% endalert %}

## Exemple de SDK

{% tabs local %}
{% tab Android SDK %}
{% subtabs %}
{% subtab Create %}
```kotlin
val json = JSONArray()
    .put(JSONObject()
        .put("id", 1)
        .put("type", "dog")
        .put("breed", "beagle")
        .put("name", "Gus"))
    .put(JSONObject()
        .put("id", 2)
        .put("type", "cat")
        .put("breed", "calico")
        .put("name", "Gerald")
    )

braze.getCurrentUser { user ->
    user.setCustomUserAttribute("pets", json)
}
```
{% endsubtab %}

{% subtab Add %}
```kotlin
val json = JSONObject()
    .put("\$add", JSONArray()
        .put(JSONObject()
            .put("id", 3)
            .put("type", "dog")
            .put("breed", "corgi")
            .put("name", "Doug"))
        .put(JSONObject()
            .put("id", 4)
            .put("type", "fish")
            .put("breed", "salmon")
            .put("name", "Larry"))
        .put(JSONObject()
            .put("id", 5)
            .put("type", "bird")
            .put("breed", "parakeet")
            .put("name", "Mary")
        )
    )

braze.getCurrentUser { user ->
    user.setCustomUserAttribute("pets", json, true)
}
```
{% endsubtab %}

{% subtab Update %}
```kotlin
val json = JSONObject()
    .put("\$update", JSONArray()
        .put(JSONObject()
            .put("\$identifier_key", "id")
            .put("\$identifier_value", 4)
            .put("\$new_object", JSONObject()
                .put("breed", "goldfish")
            )
        )
        .put(JSONObject()
            .put("\$identifier_key", "id")
            .put("\$identifier_value", 5)
            .put("\$new_object", JSONObject()
                .put("name", "Annette")
            )
        )
    )

braze.getCurrentUser { user ->
    user.setCustomUserAttribute("pets", json, true)
}
```
{% endsubtab %}

{% subtab Delete %}
```kotlin
val json = JSONObject()
    .put("\$remove", JSONArray()
        .put(JSONObject()
            .put("\$identifier_key", "id")
            .put("\$identifier_value", 1)
        )
        .put(JSONObject()
            .put("\$identifier_key", "id")
            .put("\$identifier_value", 2)
        )
        .put(JSONObject()
            .put("\$identifier_key", "type")
            .put("\$identifier_value", "dog")
        )
    )

braze.getCurrentUser { user ->
    user.setCustomUserAttribute("pets", json, true)
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Swift SDK %}
{% subtabs %}
{% subtab Create %}
```swift
let json: [[String: Any?]] = [
  [
    "id": 1,
    "type": "dog",
    "breed": "beagle",
    "name": "Gus"
  ],
  [
    "id": 2,
    "type": "cat",
    "breed": "calico",
    "name": "Gerald"
  ]
]

braze.user.setCustomAttribute(key: "pets", array: json)
```
{% endsubtab %}

{% subtab Add %}
```swift
let json: [String: Any?] = [
  "$add": [
    [
      "id": 3,
      "type": "dog",
      "breed": "corgi",
      "name": "Doug"
    ],
    [
      "id": 4,
      "type": "fish",
      "breed": "salmon",
      "name": "Larry"
    ],
    [
      "id": 5,
      "type": "bird",
      "breed": "parakeet",
      "name": "Mary"
    ]
  ]
]

braze.user.setCustomAttribute(key: "pets", dictionary: json, merge: true)
```
{% endsubtab %}

{% subtab Update %}
```swift
let json: [String: Any?] = [
  "$update": [
    [
      "$identifier_key": "id",
      "$identifier_value": 4,
      "$new_object": [
        "breed": "goldfish"
      ]
    ],
    [
      "$identifier_key": "id",
      "$identifier_value": 5,
      "$new_object": [
        "name": "Annette"
      ]
    ]
  ]
]

braze.user.setCustomAttribute(key: "pets", dictionary: json, merge: true)
```
{% endsubtab %}

{% subtab Delete %}
```swift
let json: [String: Any?] = [
  "$remove": [
    [
      "$identifier_key": "id",
      "$identifier_value": 1,
    ],
    [
      "$identifier_key": "id",
      "$identifier_value": 2,
    ],
    [
      "$identifier_key": "type",
      "$identifier_value": "dog",
    ]
  ]
]

braze.user.setCustomAttribute(key: "pets", dictionary: json, merge: true)
```
{% endsubtab %}
{% endsubtabs %}

{% alert important %}
Les attributs personnalisés imbriqués ne sont pas pris en charge par AppboyKit.
{% endalert %}
{% endtab %}

{% tab Web SDK %}
{% subtabs local %}
{% subtab Create %}
```javascript
import * as braze from "@braze/web-sdk";
const json = [{
  "id": 1,
  "type": "dog",
  "breed": "beagle",
  "name": "Gus"
}, {
  "id": 2,
  "type": "cat",
  "breed": "calico",
  "name": "Gerald"
}];
braze.getUser().setCustomUserAttribute("pets", json);
```
{% endsubtab %}

{% subtab Add %}
```javascript
import * as braze from "@braze/web-sdk";
const json = {
  "$add": [{
    "id":  3,
    "type":  "dog",
    "breed":  "corgi",
    "name":  "Doug",
  }, {
    "id":  4,
    "type":  "fish",
    "breed":  "salmon",
    "name":  "Larry",
  }, {
    "id":  5,
    "type":  "bird",
    "breed":  "parakeet",
    "name":  "Mary",
  }]
};
braze.getUser().setCustomUserAttribute("pets", json, true);
```
{% endsubtab %}

{% subtab Update %}
```javascript
import * as braze from "@braze/web-sdk";
const json = {
  "$update": [
    {
      "$identifier_key": "id",
      "$identifier_value": 4,
      "$new_object": {
        "breed": "goldfish"
      }
    },
    {
      "$identifier_key": "id",
      "$identifier_value": 5,
      "$new_object": {
        "name": "Annette"
      }
    }
  ]
};
braze.getUser().setCustomUserAttribute("pets", json, true);
```
{% endsubtab %}

{% subtab Delete %}
```javascript
import * as braze from "@braze/web-sdk";
const json = {
  "$remove": [
    {
      "$identifier_key": "id",
      "$identifier_value": 1,
    },
    {
      "$identifier_key": "id",
      "$identifier_value": 2,
    },
    {
      "$identifier_key": "type",
      "$identifier_value": "dog",
    }
  ]
};
braze.getUser().setCustomUserAttribute("pets", json, true);
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Modèle liquide

Vous pouvez utiliser ce tableau `pets` pour personnaliser un message. L'exemple de modèle Liquid suivant montre comment référencer les propriétés de l'objet attribut personnalisé enregistrées à partir de la requête API précédente et les utiliser dans votre envoi de messages.

{% raw %}
```liquid
{% assign pets = {{custom_attribute.${pets}}} %} 
 
{% for pet in pets %}
I have a {{pet.type}} named {{pet.name}}! They are a {{pet.breed}}.
{% endfor %} 
```
{% endraw %}

Dans ce scénario, vous pouvez utiliser Liquid pour parcourir en boucle le tableau `pets` et imprimer une déclaration pour chaque animal. [Attribuez une variable]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#assigning-variables) à l'attribut personnalisé `pets` et utilisez la notation par points pour accéder aux propriétés d'un objet. Indiquez le nom de l'objet, suivi d'un point `.`, suivi du nom de la propriété.

## Segmentation

Lors de la segmentation des utilisateurs sur la base de tableaux d'objets, un utilisateur sera qualifié pour la segmentation si un objet du tableau correspond aux critères. 

Créez un nouveau segment et sélectionnez **Attribut personnalisé imbriqué** comme filtre. Ensuite, recherchez et sélectionnez le nom de votre tableau d'objets.

\![Filtre par tableau d'objets.]({% image_buster /assets/img_archive/array_of_objects_segmenting_1.gif %})

Utilisez la notation par points pour spécifier le champ du tableau d'objets que vous souhaitez utiliser. Commencez le champ de texte par un ensemble vide de crochets `[]` pour indiquer à Braze que vous cherchez dans un tableau d'objets. Ensuite, ajoutez un point `.`, suivi du nom du champ que vous souhaitez utiliser.

Par exemple, si vous souhaitez filtrer le tableau d'objets `pets` sur la base du champ `type`, saisissez `[].type` et choisissez le type d'animal à filtrer, par exemple `snake`.

\![Filtrer par type d'animal équivaut à un serpent.]({% image_buster /assets/img_archive/array_of_objects_segmenting_3.png %})

Vous pouvez aussi filtrer les animaux qui ont un `type` de `dog`. Ici, un utilisateur a au moins un chien, de sorte qu'il entre dans la segmentation "tout utilisateur ayant au moins un animal de compagnie de type chien".

\![Filtrer par type d'animal équivaut à chien.]({% image_buster /assets/img_archive/array_of_objects_segmenting_2.png %})

### Niveaux d'imbrication

Vous pouvez créer un segment avec un maximum d'un niveau d'imbrication de tableaux (tableau à l'intérieur d'un autre tableau). Par exemple, compte tenu des attributs suivants, vous pouvez créer un segment pour `pets[].name` contient `Gus`, mais vous ne pouvez pas créer un segment pour `pets[].nicknames[]` contient `Gugu`.

{% raw %}
```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "pets": [
        {
          "id": 1,
          "type": "dog",
          "breed": "beagle",
          "name": "Gus",
          "nicknames": [
            "Gugu",
            "Gusto"
          ]
        },
        {
          "id": 2,
          "type": "cat",
          "breed": "calico",
          "name": "Gerald",
          "nicknames": [
            "GeGe",
            "Gerry"
          ]
        }
      ]
    }
  ]
}
```
{% endraw %}

## Points de données

Les points de données sont enregistrés différemment selon que vous créez, mettez à jour ou supprimez une propriété.

{% tabs local %}
{% tab Create %}

La création d'un nouveau tableau d'objets enregistre un point de données pour chaque attribut d'un objet. Cet exemple coûte huit points de données - chaque objet animal possède quatre attributs et il y a deux objets.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "pets": [
        {
          "id": 1,
          "type": "dog",
          "breed": "beagle",
          "name": "Gus"
        },
        {
          "id": 2,
          "type": "cat",
          "breed": "calico",
          "name": "Gerald"
        }
      ]
    }
  ]
}
```
{% endtab %}
{% tab Update %}

La mise à jour d'un tableau existant enregistre un point de donnée pour chaque propriété ajoutée. Cet exemple coûte deux points de données car il ne met à jour qu'une propriété dans chacun des deux objets.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "_merge_objects": true,
      "pets": {
        "$update": [
          {
            "$identifier_key": "id",
            "$identifier_value": 4,
            "$new_object": {
              "breed": "goldfish"
            }
          },
          {
            "$identifier_key": "id",
            "$identifier_value": 5,
            "$new_object": {
              "name": "Annette"
            }
          }
        ]
      }
    }
  ]
}
```
{% endtab %}
{% tab Remove %}

La suppression d'un objet d'un tableau enregistre un point de donnée pour chaque critère de suppression que vous envoyez. Cet exemple coûte trois points de données, bien que vous puissiez retirer plusieurs chiens avec cette déclaration.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "pets": {
        "$remove": [
          // Remove by ID
          {
            "$identifier_key": "id",
            "$identifier_value": 1
          },
          {
            "$identifier_key": "id",
            "$identifier_value": 2
          },
          // Remove any dog
          {
            "$identifier_key": "type",
            "$identifier_value": "dog"
          }
        ]
      }
    }
  ]
}
```
{% endtab %}
{% endtabs %}

