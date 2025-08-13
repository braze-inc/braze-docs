---
nav_title: Tableau d’objets
article_title: Tableau d’objets
alias: "/array_of_objects/"
page_order: 0
page_type: reference
description: "Cet article de référence couvre l'utilisation d'un tableau d'objets comme type de données pour les attributs personnalisés, y compris les limitations et les exemples d'utilisation." 
---

# Tableau d’objets

> Cette page explique comment utiliser un tableau d'objets pour regrouper des attributs connexes. Vous pouvez, par exemple, avoir un groupe d’objets « animaux de compagnie », un groupe d’objets « chansons » et un groupe d’objets « Compte » pour le même utilisateur. Ces array d’objets peuvent être utilisées pour personnaliser votre envoi de messages avec Liquid, ou segmenter votre audience si un élément d’un objet correspond aux critères.

## Restrictions

- Les tableaux d'objets sont destinés aux attributs personnalisés envoyés par l'API. Les téléchargements de fichiers CSV ne sont pas pris en charge. C'est parce que les virgules dans le fichier CSV seront interprétées comme un séparateur de colonnes, et les virgules dans les valeurs provoqueront des erreurs d'analyse. 
- Les tableaux d'objets n'ont pas de limite quant au nombre d'éléments, mais leur taille maximale est de 100 Ko.
- Tous les partenaires de Braze ne prennent pas en charge les tableaux d'objets. Consultez la [documentation du partenaire]({{site.baseurl}}/partners/home) pour savoir si l'intégration prend en charge cette fonctionnalité.

La mise à jour ou la suppression d'éléments d'un tableau nécessite l'identification de l'élément par sa clé et sa valeur ; pensez donc à inclure un identifiant unique pour chaque élément du tableau. Ces identifiants uniques s’appliqueront uniquement au tableau. Ils sont utiles si vous souhaitez mettre à jour ou supprimer des objets dans votre tableau. Braze n’oblige pas à utiliser de tels identifiants uniques. 

{% alert tip %}
Pour plus d'informations sur l'utilisation de tableaux d'objets pour les objets d'attributs utilisateur, reportez-vous à [Objet d'attributs utilisateur]({{site.baseurl}}/api/objects_filters/user_attributes_object).
{% endalert %}

## Exemple d'API

{% tabs local %}
{% tab Créer %}

Voici un `/users/track` exemple avec un tableau `pets`. Pour capturer les propriétés des animaux domestiques, envoyez une demande API qui répertorie `pets` en tant que tableau d’objets. Notez que chaque objet a reçu un `id` unique qui peut être utilisé plus tard lors des mises à jour.

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
{% tab Ajouter %}

Ajoutez un autre élément au tableau en utilisant l’opérateur `$add`. L’exemple suivant montre l’ajout d’autres objets animaux de compagnie dans le tableau `pets` de l’utilisateur.

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
{% tab Mettre à jour %}

Mettez à jour les valeurs pour des objets spécifiques dans un tableau en utilisant le paramètre `_merge_objects` et l’opérateur `$update`. Cela effectue une fusion profonde (deep merge) comme pour les mises à jour d’objets d’[attributs personnalisés imbriqués]({{site.baseurl}}/nested_custom_attribute_support/#api-request-body) simples.

Notez que `$update` ne peut pas être utilisé pour supprimer une propriété imbriquée d'un objet à l'intérieur d'un tableau. Pour ce faire, vous devez supprimer l'élément entier du tableau, puis ajouter l'objet sans cette clé spécifique (en utilisant une combinaison de `$remove` et `$add`).

L’exemple suivant montre la mise à jour de propriété `breed` sur `goldfish` pour l’objet avec un `id` de `4`. Cet exemple de requête met également à jour l’objet avec `id` égal à `5` et un nouveau `name` de `Annette`. Comme le paramètre `_merge_objects` est défini sur `true`, tous les autres champs de ces deux objets restent les mêmes.

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
Vous devez définir `_merge_objects` sur True (vrai) ou vos objets seront écrasés. Par défaut, `_merge_objects` est défini sur False (faux).
{% endalert %}

{% endtab %}
{% tab Supprimer %}

Supprimer des objets d’un tableau en utilisant l’opérateur `$remove` en combinaison avec une clé (`$identifier_key`) et valeur (`$identifier_value`) correspondantes.

L’exemple suivant montre la suppression d’un objet dans un `pets`tableau qui a un`id` avec une valeur de `1`, un `id` avec une valeur de `2`, et un `type` avec une valeur de `dog`. S’il y a plusieurs objets avec une valeur`type` égale à `dog`, tous les objets correspondants seront supprimés.

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

## Exemple de SDK

{% tabs local %}
{% tab Android SDK %}

**Créer**
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

**Ajouter**
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

**Mettre à jour**
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

**Supprimer**
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

{% endtab %}
{% tab Swift SDK %}

**Créer**
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

**Ajouter**
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

**Mettre à jour**
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

**Supprimer**
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

{% alert important %}
Les attributs personnalisés imbriqués ne sont pas pris en charge pour AppboyKit.
{% endalert %}

{% endtab %}
{% tab Web SDK %}

**Créer**
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

**Ajouter**
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

**Mettre à jour**
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

**Supprimer**
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

{% endtab %}
{% endtabs %}

## Modèles Liquid

Vous pouvez utiliser ce tableau `pets` pour personnaliser un message. Les exemples de templating Liquid suivants montrent comment référencer les propriétés d’objet d’attribut personnalisées de la requête API précédente pour les utiliser dans vos communications Liquid.

{% raw %}
```liquid
{% assign pets = {{custom_attribute.${pets}}} %} 
 
{% for pet in pets %}
I have a {{pet.type}} named {{pet.name}}! They are a {{pet.breed}}.
{% endfor %} 
```
{% endraw %}

Dans ce scénario, vous pouvez utiliser Liquid pour parcourir le tableau `pets` et identifier chaque animal de compagnie. [Attribuez une variable]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#assigning-variables) à l'`pets` attribut personnalisé et utilisez la notation par points pour accéder aux propriétés d'un objet. Spécifiez le nom de l’objet, suivi d’une période `.`, suivi du nom de la propriété.

## Segmentation

Lorsque vous segmentez des utilisateurs en fonction d’un tableau d’objets, un utilisateur sera admissible pour le segment si un objet du tableau correspond aux critères. 

Créez un nouveau segment et sélectionnez **Nested Custom Attribute** comme filtre. Recherchez et sélectionnez le nom de votre tableau d’objets.

![Filtre sur un tableau d'objets.]({% image_buster /assets/img_archive/array_of_objects_segmenting_1.gif %})

Utilisez la notation par points pour spécifier les champ du tableau d’objets que vous souhaitez utiliser. Commencez le champ de texte par deux crochets vides `[]` pour indiquer à Braze que vous regardez dans un tableau (array) d’objets. Ensuite, ajoutez une période `.`, suivi du nom du champ que vous souhaitez utiliser.

Par exemple, si vous souhaitez filtrer un tableau d’objets`pets` basés sur le `type` champ, entrez `[].type` et filtrez sur le type d’animal de compagnie, comme `snake`.

![Filtrer par type d'animal équivaut à un serpent.]({% image_buster /assets/img_archive/array_of_objects_segmenting_3.png %})

Ou vous pouvez filtrer les animaux domestiques qui ont un `type` égal à  `dog`. Ici, l’utilisateur a au moins un chien donc il entre dans le segment «  tout utilisateur ayant au moins un animal de compagnie de type chien ».

![Filtrer par type d'animal de compagnie équivaut à chien.]({% image_buster /assets/img_archive/array_of_objects_segmenting_2.png %})

### Niveaux d’imbrication

Vous pouvez créer un segment avec un tableau (array) imbriqué dans un autre tableau (array).  Par exemple, compte tenu des attributs suivants, vous pouvez faire en sorte qu’un segment pour `pets[].name` contienne `Gus`, mais vous ne pouvez pas faire en sorte qu’un segment pour `pets[].nicknames[]` contienne `Gugu`.

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

Les points de données sont consommés différemment selon que vous créez, mettez à jour ou supprimez une propriété.

{% tabs local %}
{% tab Créer %}

La création d’une tableau consomme un point de données pour chaque attribut de l’objet. Cet exemple coûte huit points de données : chaque objet animal de compagnie possède quatre attributs et il y a deux objets.

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
{% tab Mettre à jour %}

La mise à jour d’un tableau existant consomme un point de données pour chaque propriété ajoutée. Cet exemple coûte deux points de données, car il met uniquement à jour une propriété dans chacun des deux objets.

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
{% tab Supprimer %}

Enlever un objet dans un tableau consomme un point de données pour chaque critère de suppression que vous envoyez. Cet exemple coûte trois points de données, même si vous pouvez supprimer plusieurs chiens avec cette requête.

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

