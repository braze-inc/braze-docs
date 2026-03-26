---
nav_title: Tableau d'objets
article_title: Tableau d'objets
alias: "/array_of_objects/"
page_order: 0
page_type: reference
description: "Cet article de référence couvre l'utilisation d'un tableau d'objets comme type de données pour les attributs personnalisés, y compris les limitations et les exemples d'utilisation." 
---

# Tableau d'objets

> Cette page explique comment utiliser un tableau d'objets pour regrouper des attributs connexes. Vous pouvez, par exemple, avoir un groupe d'objets « animaux de compagnie », un groupe d'objets « chansons » et un groupe d'objets « Compte » pour le même utilisateur. Ces tableaux d'objets peuvent être utilisés pour personnaliser votre envoi de messages avec Liquid, ou segmenter votre audience si un élément d'un objet correspond aux critères.

{% multi_lang_include nested_attribute_objects/supported_data_types.md %}

## Restrictions

- Les tableaux d'objets sont destinés aux attributs personnalisés envoyés par l'API. Les téléchargements de fichiers CSV ne sont pas pris en charge, car les virgules dans le fichier CSV sont interprétées comme des séparateurs de colonnes, et les virgules dans les valeurs provoquent des erreurs d'analyse. 
- Les tableaux d'objets n'ont pas de limite quant au nombre d'éléments, mais leur taille maximale est de 100 Ko.
- Tous les partenaires de Braze ne prennent pas en charge les tableaux d'objets. Consultez la [documentation du partenaire]({{site.baseurl}}/partners/home) pour savoir si l'intégration prend en charge cette fonctionnalité.

La mise à jour ou la suppression d'éléments d'un tableau nécessite l'identification de l'élément par sa clé et sa valeur ; pensez donc à inclure un identifiant unique pour chaque élément du tableau. L'unicité s'applique uniquement au tableau et est utile si vous souhaitez mettre à jour ou supprimer des objets spécifiques dans votre tableau. Braze n'impose pas l'utilisation de tels identifiants uniques.

{% alert important %}
Lorsqu'un attribut personnalisé imbriqué dans votre requête contient des valeurs non valides (telles que des formats d'heure non valides ou des valeurs `null`), Braze ignore toutes les mises à jour des attributs personnalisés imbriqués de la requête lors du traitement. Cela s'applique à toutes les structures imbriquées dans cet attribut spécifique. Vérifiez que toutes les valeurs contenues dans les attributs personnalisés imbriqués sont valides avant l'envoi. Pour plus d'informations, consultez [Créer et mettre à jour des utilisateurs]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#how-does-userstrack-handle-invalid-nested-custom-attributes).
{% endalert %}

{% alert tip %}
Pour plus d'informations sur l'utilisation de tableaux d'objets pour les objets d'attributs utilisateur, reportez-vous à [Objet d'attributs utilisateur]({{site.baseurl}}/api/objects_filters/user_attributes_object).
{% endalert %}

## Exemple d'API

{% tabs local %}
{% tab Create %}

Voici un exemple `/users/track` avec un tableau `pets`. Pour capturer les propriétés des animaux domestiques, envoyez une requête API qui répertorie `pets` en tant que tableau d'objets. Notez que chaque objet a reçu un `id` unique qui peut être utilisé plus tard lors des mises à jour.

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

Ajoutez un autre élément au tableau en utilisant l'opérateur `$add`. L'exemple suivant montre l'ajout de trois objets animaux de compagnie supplémentaires dans le tableau `pets` de l'utilisateur.

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

Mettez à jour les valeurs pour des objets spécifiques dans un tableau en utilisant le paramètre `_merge_objects` et l'opérateur `$update`. Cela effectue une fusion profonde (deep merge), comme pour les mises à jour d'objets d'[attributs personnalisés imbriqués]({{site.baseurl}}/nested_custom_attribute_support/#api-request-body) simples.

Notez que `$update` ne peut pas être utilisé pour supprimer une propriété imbriquée d'un objet à l'intérieur d'un tableau. Pour ce faire, vous devez supprimer l'élément entier du tableau, puis ajouter l'objet sans cette clé spécifique (en utilisant une combinaison de `$remove` et `$add`).

L'exemple suivant montre la mise à jour de la propriété `breed` sur `goldfish` pour l'objet avec un `id` de `4`. Cet exemple de requête met également à jour l'objet avec `id` égal à `5` avec un nouveau `name` de `Annette`. Comme le paramètre `_merge_objects` est défini sur `true`, tous les autres champs de ces deux objets restent les mêmes.

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
Vous devez définir `_merge_objects` sur true, sinon vos objets seront écrasés. Par défaut, `_merge_objects` est défini sur false.
{% endalert %}

{% endtab %}
{% tab Remove %}

Supprimez des objets d'un tableau en utilisant l'opérateur `$remove` en combinaison avec une clé (`$identifier_key`) et une valeur (`$identifier_value`) correspondantes.

L'exemple suivant montre la suppression de tout objet dans le tableau `pets` qui a un `id` avec une valeur de `1`, un `id` avec une valeur de `2`, et un `type` avec une valeur de `dog`. S'il y a plusieurs objets avec une valeur `type` égale à `dog`, tous les objets correspondants seront supprimés.

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

### Ordre de traitement

Lorsqu'une seule requête `/users/track` inclut des opérations `$add`, `$remove` et `$update` pour le même attribut de tableau, Braze les traite dans cet ordre :

1. `$add`
2. `$remove`
3. `$update`

Étant donné que `$add` s'exécute avant `$remove`, il n'est pas possible d'utiliser un `$remove` suivi d'un `$add` comme mécanisme d'upsert dans une seule requête. Le `$add` est traité en premier, puis le `$remove` supprime l'élément. Pour effectuer un upsert, envoyez le `$remove` dans une requête distincte avant le `$add`.

### Horodatages

Lorsque vous incluez des champs tels que des horodatages dans un tableau d'objets, utilisez le format `$time` au lieu de chaînes de caractères simples ou d'entiers unix epoch.

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
Pour plus d'informations, consultez [Attributs personnalisés imbriqués]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support).
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
Les attributs personnalisés imbriqués ne sont pas pris en charge pour AppboyKit.
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

## Modèles Liquid

Vous pouvez utiliser ce tableau `pets` pour personnaliser un message. Les exemples de templating Liquid suivants montrent comment référencer les propriétés d'objet d'attribut personnalisé enregistrées via la requête API précédente et les utiliser dans vos communications.

{% raw %}
```liquid
{% assign pets = {{custom_attribute.${pets}}} %} 
 
{% for pet in pets %}
I have a {{pet.type}} named {{pet.name}}! They are a {{pet.breed}}.
{% endfor %} 
```
{% endraw %}

Dans ce scénario, vous pouvez utiliser Liquid pour parcourir le tableau `pets` et afficher une phrase pour chaque animal de compagnie. [Attribuez une variable]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#assigning-variables) à l'attribut personnalisé `pets` et utilisez la notation par points pour accéder aux propriétés d'un objet. Spécifiez le nom de l'objet, suivi d'un point `.`, suivi du nom de la propriété.

## Segmentation

Lorsque vous segmentez des utilisateurs en fonction d'un tableau d'objets, un utilisateur sera admissible pour le segment si un objet du tableau correspond aux critères. 

Créez un nouveau segment et sélectionnez **Nested Custom Attribute** comme filtre. Recherchez et sélectionnez le nom de votre tableau d'objets.

![Filtre sur un tableau d'objets.]({% image_buster /assets/img_archive/array_of_objects_segmenting_1.gif %})

Utilisez la notation par points pour spécifier le champ du tableau d'objets que vous souhaitez utiliser. Commencez le champ de texte par deux crochets vides `[]` pour indiquer à Braze que vous recherchez dans un tableau d'objets. Ensuite, ajoutez un point `.`, suivi du nom du champ que vous souhaitez utiliser.

Par exemple, si vous souhaitez filtrer un tableau d'objets `top_3_movies` en fonction du champ `type`, entrez `[].type` et choisissez les films à filtrer, comme `Fantasy Movie`.


### Niveaux d'imbrication

Vous pouvez créer un segment avec un tableau imbriqué dans un autre tableau (jusqu'à un niveau d'imbrication). Par exemple, compte tenu des attributs suivants, vous pouvez créer un segment pour lequel `pets[].name` contient `Gus`, mais vous ne pouvez pas créer un segment pour lequel `pets[].nicknames[]` contient `Gugu`.

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

Les points de données sont comptabilisés différemment selon que vous créez, mettez à jour ou supprimez une propriété.

{% tabs local %}
{% tab Create %}

La création d'un nouveau tableau enregistre un point de donnée pour chaque attribut d'un objet. Cet exemple coûte huit points de données : chaque objet animal de compagnie possède quatre attributs et il y a deux objets.

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

La mise à jour d'un tableau existant enregistre un point de donnée pour chaque propriété ajoutée. Cet exemple coûte deux points de données, car il met uniquement à jour une propriété dans chacun des deux objets.

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

La suppression d'un objet d'un tableau enregistre un point de donnée pour chaque critère de suppression que vous envoyez. Cet exemple coûte trois points de données, même si vous pouvez supprimer plusieurs chiens avec cette requête.

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