---
nav_title: Tableau d'objets
permalink: "/tableau_de_objets/"
hidden: vrai
---

# Tableau d'objets

Utilisez un tableau d'objets pour regrouper les attributs associés. Vous pouvez avoir un groupe d'objets familiers, d'objets de chanson et d'objets de compte qui appartiennent tous à un seul utilisateur. Ces tableaux d'objets peuvent être utilisés pour personnaliser votre messagerie avec Liquid, ou créer des segments d'audience si un élément d'un objet correspond aux critères.

{% alert important %}
La prise en charge de cette fonctionnalité dépend de [attributs personnalisés imbriqués]({{site.baseurl}}/nested_custom_attribute_support/), qui est actuellement en accès anticipé. Veuillez contacter votre responsable de compte Braze si vous êtes intéressé à participer à l'accès anticipé.
{% endalert %}

## Limitation

- Disponible sur les attributs personnalisés envoyés via l'API uniquement, non pris en charge avec Braze SDKs ou téléchargement CSV.
- Les partenaires ne supportent pas encore les tableaux d'objets. Tant que cette fonctionnalité n'est pas prise en charge, nous vous recommandons de ne pas utiliser cette fonctionnalité avec des groupes d'applications qui ont des intégrations de partenaires activées.
- Les dates ne sont pas prises en charge dans les objets. Si les dattimes sont incluses dans vos objets, elles sont stockées sous la forme de chaînes.
- Les tableaux d'objets n'ont pas de limite sur le nombre d'éléments, mais ont une taille maximale de 50 Ko.

Mettre à jour ou supprimer des éléments d'un tableau nécessite l'identification de l'élément par clé et valeur. Considérez donc d'inclure un identifiant unique pour chaque élément du tableau. L'unicité est limitée au tableau et est utile si vous voulez mettre à jour et supprimer des objets spécifiques de votre tableau. Ce n'est pas le cas du Brésil.

## Exemples d'utilisation

### Corps de la requête API

{% tabs %}
{% tab Create %}

Montré ci-dessous est un exemple de `/users/track` avec un tableau `animaux de compagnie`. Pour capturer les propriétés des animaux de compagnie, envoyez une requête API qui liste les `animaux` en tant que tableau d'objets. Notez que chaque objet a été assigné à un id `unique` qui peut être référencé plus tard lors de la mise à jour.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "animaux de compagnie": [
        {
          "id": 1,
          "type": "chien",
          "race": "beagle",
          "name": "Gus"
        },
        {
          "id": 2,
          "type": "chat",
          "race": "calico",
          "nom": "Gerald"
        }
      ]
    }
  ]
}
```
{% endtab %}
{% tab Add %}

Ajouter un autre élément au tableau en utilisant l'opérateur `$add`. L'exemple suivant montre l'ajout de trois objets familiers supplémentaires au tableau `animaux de compagnie` de l'utilisateur.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "animaux de compagnie": {
        "$add": [
          {
            "id": 3,
            "type": "chien",
            "race": "corgi",
            "name": "Doug"
          },
          {
            "id": 4,
            "type": "poisson",
            "élevage": "saumon",
            "name": "Larry"
          },
           {
            "id": 5,
            "type": "oiseau",
            "race": "parakeet",
            "nom": "Marie"
          }
        ]
        ]
      }
    }
  ]

```
{% endtab %}
{% tab Update %}

Mettre à jour les valeurs des objets spécifiques dans un tableau en utilisant le paramètre `_merge_objects` et l'opérateur `$update`. Similaire aux mises à jour de simples [attributs personnalisés imbriqués]({{site.baseurl}}/nested_custom_attribute_support/#api-request-body) objets, cela effectue une fusion profonde.

L'exemple suivant montre la mise à jour de la propriété `de la race` en `poisson rouge` pour l'objet avec un `id` de `4`. Cet exemple de requête met également à jour l'objet avec l'id `` équivaut à `5` avec un nouveau `nom` de `Annette`. Puisque le paramètre `_merge_objects` est défini à `true`, tous les autres champs pour ces deux objets restent les mêmes.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "_merge_objets": vrai,
      "animaux de compagnie": {
        "$update": [
          {
            "$identifier_key": "id",
            "$identifier_value": 4,
            "$new_object": {
              "élevage": "poisson-rouge"
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
Vous devez définir `_merge_objects` à true, sinon vos objets seront écrasés. `_merge_objects` est faux par défaut.
{% endalert %}

{% endtab %}
{% tab Remove %}

Retire des objets d'une table en utilisant l'opérateur `$remove` en combinaison avec une clé correspondante (`$identifier_key`) et une valeur (`$identifier_value`).

L'exemple suivant montre la suppression de n'importe quel objet dans le tableau `animaux de compagnie` qui a un `id` avec une valeur de `1`, un `id` avec une valeur de `2`, et un `de type` avec une valeur de `chien`. S'il y a plusieurs objets avec la valeur `de type` de `chien`, tous les objets correspondants seront supprimés.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "animaux de compagnie": {
        "$remove": [
          // Supprimé par ID
          {
            "$identifier_key": "id",
            "$identifier_value": 1
          },
          {
            "$identifier_key": "id",
            "$identifier_value": 2
          },
          // Supprime n'importe quel chien
          {
            "$identifier_key": "type",
            "$identifier_value": "chien"
          }
        ]
      }
    }
  ]
}
```
{% endtab %}
{% endtabs %}

### Templating Liquide

Vous pouvez utiliser ce tableau `animaux` pour personnaliser un message. L'exemple de modèle Liquid ci-dessous montre comment référencer les propriétés de l'objet d'attribut personnalisé enregistrées à partir de la requête de l'API ci-dessus et les utiliser dans votre messagerie.

{% raw %}
```liquid
{% assigner les animaux de compagnie = {{custom_attribute.${pets}}} %} 

{% for pet in pets %}
J'ai un {{pet.type}} nommé {{pet.name}}! Il s'agit d'un {{pet.breed}}.
{% endfor %} 
```
{% endraw %}

Dans ce scénario, vous pouvez utiliser Liquid pour parcourir le tableau `animaux de compagnie` et afficher une instruction pour chaque animal. [Assigner une variable]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#assigning-variables) aux `animaux de compagnie` attribut personnalisé et utiliser la notation par point pour accéder aux propriétés sur un objet. Spécifiez le nom de l'objet, suivi d'une période `.`, suivie du nom de la propriété.

### Segmentation

Lors de la segmentation des utilisateurs sur la base de tableaux d'objets, un utilisateur se qualifiera pour le segment si un objet dans le tableau correspond aux critères.

Créez un nouveau segment et sélectionnez **Attribut personnalisé imbriqué** comme filtre. Ensuite, recherchez et sélectionnez le nom de votre tableau d'objets.

!\[Filter by array of objects\]\[1\]

Utilisez la notation point pour spécifier quel champ dans le tableau d'objets que vous voulez utiliser. Démarre le champ de texte avec un ensemble vide de crochets `[]` pour dire à Braze que vous regardez dans un tableau d'objets. Après cela, ajoutez un point `.`, suivi du nom du champ que vous souhaitez utiliser.

Par exemple, si vous voulez filtrer le tableau d'objets `animaux de compagnie` basé sur le champ `type` entrez `[]. ype` et choisissez le type d'animal de compagnie pour lequel filtrer, comme `serpent`.

!\[Filter by pet type equals snake\]\[3\]

Ou vous pouvez filtrer pour les animaux de compagnie qui ont un `type` de `chien`. Ici, un utilisateur a au moins un chien pour que l'utilisateur se qualifie dans le segment de "tout utilisateur qui a au moins un animal de type chien".

!\[Filter by pet type equals dog\]\[2\]

## Points de données

Les points de données sont consommés différemment selon que vous créez, mettez à jour ou supprimiez une propriété.

{% tabs %}
{% tab Create %}

La création d'un nouveau tableau consomme un point de données pour chaque attribut d'un objet. Cet exemple coûte huit points de données : chaque objet familier a quatre attributs et il y a deux objets.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "animaux de compagnie": [
        {
          "id": 1,
          "type": "chien",
          "race": "beagle",
          "name": "Gus"
        },
        {
          "id": 2,
          "type": "chat",
          "race": "calico",
          "nom": "Gerald"
        }
      ]
    }
  ]
}
```
{% endtab %}
{% tab Update %}

La mise à jour d'un tableau existant consomme un point de données pour chaque propriété ajoutée. Cet exemple coûte deux points de données car il ne met à jour qu'une propriété dans chacun des deux objets.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "_merge_objets": vrai,
      "animaux de compagnie": {
        "$update": [
          {
            "$identifier_key": "id",
            "$identifier_value": 4,
            "$new_object": {
              "élevage": "poisson-rouge"
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

La suppression d'un objet d'un tableau consomme un point de données pour chaque critère de suppression que vous envoyez. Cet exemple coûte trois points de données, même si vous pouvez supprimer plusieurs chiens avec cette instruction.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "animaux de compagnie": {
        "$remove": [
          // Supprimé par ID
          {
            "$identifier_key": "id",
            "$identifier_value": 1
          },
          {
            "$identifier_key": "id",
            "$identifier_value": 2
          },
          // Supprime n'importe quel chien
          {
            "$identifier_key": "type",
            "$identifier_value": "chien"
          }
        ]
      }
    }
  ]
}
```

{% endtab %}
{% endtabs %}
[1]: {% image_buster /assets/img_archive/array_of_objects_segmenting_1.gif %} [2]: {% image_buster /assets/img_archive/array_of_objects_segmenting_2.png %} [3]: {% image_buster /assets/img_archive/array_of_objects_segmenting_3.png %}