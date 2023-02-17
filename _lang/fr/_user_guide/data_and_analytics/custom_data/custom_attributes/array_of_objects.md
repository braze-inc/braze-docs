---
nav_title: Tableau d’objets
article_title: Tableau d’objets
alias: "/array_of_objects/"
page_order: 0
page_type: reference
description: "Cet article de référence explique comment utiliser un tableau (array) d’objets en tant que type de données pour des attributs personnalisés, avec les limitations et des exemples d’utilisation." 
---

# Tableau d’objets

Utilisez un ensemble d’objets pour regrouper des attributs associés. Vous pouvez, par exemple, avoir un groupe d’objets « animaux de compagnie », un groupe d’objets « chansons » et un groupe d’objets « Compte » pour le même utilisateur. Ces array d’objets peuvent être utilisées pour personnaliser votre message avec Liquid, ou segmenter votre audience si un élément d’un objet correspond aux critères.

## Limitations

- Les baies d’objets sont destinées aux attributs personnalisés envoyés via l’API. Ils ne sont pas pris en charge pour une utilisation avec les SDK Braze ou les téléchargements CSV. Les virgules de votre fichier CSV seront interprétées comme un séparateur de colonnes, de sorte que les virgules dans les valeurs entraîneront des erreurs d’analyse du fichier. 
- Les partenaires ne prennent pas en charge les tableaux d’objets. Nous vous déconseillons d’utiliser cette fonctionnalité avec des groupes d’applications ayant activé des intégrations partenaires.
- Les tableaux d’objets n’ont aucune limite sur le nombre d’articles mais ont une taille maximale de 50 Ko.

La mise à jour ou la suppression des éléments d’un tableau nécessite l’identification de l’élément par clé et valeur. En tant que tel, envisagez d’inclure un identifiant unique pour chaque élément du tableau. Ces identifiants uniques s’appliqueront uniquement au tableau. Ils sont utiles si vous souhaitez mettre à jour ou supprimer des objets dans votre tableau. Braze n’oblige pas à utiliser de tels identifiants uniques. 

## Exemples d’utilisation

### Corps de la requête API

{% tabs %}
{% tab Créez %}

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
{% tab Add %}

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
        ]
      }
    }
  ]
}
```
{% endtab %}
{% tab Update %}

Mettez à jour les valeurs pour des objets spécifiques dans un tableau en utilisant le paramètre `_merge_objects` et l’opérateur `$update`. Cela effectue une fusion profonde (deep merge) comme pour les mises à jour d’objets [d’attributs personnalisés imbriqués]({{site.baseurl}}/nested_custom_attribute_support/#api-request-body) simples.

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
Vous devez définir `_merge_objects` sur True (vrai) ou vos objets seront écrasés. Par défaut,`_merge_objects` est défini sur  False (faux).
{% endalert %}

{% endtab %}
{% tab Remove %}

Supprimer des objets d’un tableau en utilisant l’opérateur `$remove` en combinaison avec une clé (`$identifier_key`) et valeur (`$identifier_value`) correspondantes.

L’exemple suivant montre la suppression d’un objet dans un `pets`tableau qui a un`id` avec une valeur de `1`, un `id` avec une valeur de `2`, et un `type` avec une valeur de `dog`. S’il y a plusieurs objets avec une valeur`type` égale à `dog`, tous les objets correspondants seront supprimés.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "pets": {
        "$remove": [
          // Enlever par ID
          {
            "$identifier_key": "id",
            "$identifier_value": 1
          },
          {
            "$identifier_key": "id",
            "$identifier_value": 2
          },
          // Enlever tous les chiens
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

### Modèles Liquid

Vous pouvez utiliser ce tableau `pets` pour personnaliser un message. L’exemple de templating Liquid suivant montre comment référencer les propriétés d’objet d’attribut personnalisées enregistrées à partir de la demande API précédente pour les utiliser dans vos communications.

{% raw %}
```liquid
{% assign pets = {{custom_attribute.${pets}}} %} 
 
{% for pet in pets %}
J'ai un {{pet.type}} nommé {{pet.name}} ! Ce sont {{pet.breed}}.
{% endfor %} 
```
{% endraw %}

Dans ce scénario, vous pouvez utiliser Liquid pour parcourir le tableau `pets` et identifier chaque animal de compagnie. [Attribuer une variable]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#assigning-variables) au `pets` attribut personnalisé et utilisez la notation par points pour accéder aux propriétés sur un objet. Spécifiez le nom de l’objet, suivi d’une période `.`, suivi du nom de la propriété.

### Segmentation

Lorsque vous segmentez des utilisateurs en fonction d’un tableau d’objets, un utilisateur sera admissible pour le segment si un objet du tableau correspond aux critères. 

Créez un nouveau segment et sélectionnez **Attribut personnalisé imbriqué** en tant que filtre. Recherchez et sélectionnez le nom de votre tableau d’objets.

![Filtrer par tableau d’objets][1]

Utilisez la notation par points pour spécifier les champ du tableau d’objets que vous souhaitez utiliser. Faites commencer le champ de texte par une paire de crochets vides `[]` to tell Braze that you're looking inside an array of objects. After that, add a period `.` suivie par le nom du champ que vous voulez utiliser.

Par exemple, si vous souhaitez filtrer un tableau d’objets `pets` basés sur le champ `type`, entrez `[].type` and choose which type of pet to filter for, such as `snake`.

![Le filtre par type d’animal est égal à « serpent »][3]

Ou vous pouvez filtrer les animaux domestiques qui ont un `type` égal à  `dog`. Ici, l’utilisateur a au moins un chien donc il entre dans le segment «  tout utilisateur ayant au moins un animal de compagnie de type chien ».

![Le filtre par type d’animal est égal à « chien »][2]

#### Niveaux d’imbrication

Vous pouvez créer un segment avec un tableau (array) imbriqué dans un autre tableau (array).  Par exemple, à partir des attributs suivants, vous pouvez créer un segment pour `pets[].name` contains `Gus`, but you can't make a segment for `pets[].nicknames[]` contains `Gugu`.

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

{% tabs %}
{% tab Créez %}

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
{% tab Update %}

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
{% tab Remove %}

Enlever un objet dans un tableau consomme un point de données pour chaque critère de suppression que vous envoyez. Cet exemple coûte trois points de données, même si vous pouvez supprimer plusieurs chiens avec cette requête.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "pets": {
        "$remove": [
          // Enlever par ID
          {
            "$identifier_key": "id",
            "$identifier_value": 1
          },
          {
            "$identifier_key": "id",
            "$identifier_value": 2
          },
          // Enlever tous les chiens
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

[1]: {% image_buster /assets/img_archive/array_of_objects_segmenting_1.gif %}
[2]: {% image_buster /assets/img_archive/array_of_objects_segmenting_2.png %}
[3]: {% image_buster /assets/img_archive/array_of_objects_segmenting_3.png %}
