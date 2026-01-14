---
nav_title: "Mise à jour de l'utilisateur"
article_title: Mise à jour des utilisateurs 
alias: "/user_update/"
page_order: 6
page_type: reference
description: "Cet article de référence couvre le composant User Update et la manière de l'utiliser dans vos Canvas."
tool: Canvas
---

# Mise à jour des utilisateurs 

> Le composant User Update vous permet de mettre à jour les attributs, les événements et les achats d'un utilisateur dans un compositeur JSON, de sorte qu'il n'est pas nécessaire d'inclure des informations sensibles telles que les clés API.

## Fonctionnement de ce composant

\![Une étape de mise à jour de l'utilisateur nommée "Mise à jour de la loyauté" qui met à jour un attribut "Est membre Premium" à "true".]({% image_buster /assets/img_archive/canvas_user_update_step.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

Lorsque vous utilisez ce composant dans votre Canvas, les mises à jour ne sont pas prises en compte dans votre limite de débit de `/users/track` requêtes par minute. Au lieu de cela, ces mises à jour sont mises en lots afin que Braze puisse les traiter plus efficacement qu'un webhook Braze à Braze. Notez que ce composant n'enregistre pas les [points de données]({{site.baseurl}}/user_guide/data/data_points/) lorsqu'il est utilisé pour mettre à jour des points de données non facturables (tels que les groupes d'abonnement).

Les utilisateurs ne passeront aux étapes du canvas suivantes qu'après avoir effectué les mises à jour nécessaires. Cela signifie que tout envoi de messages ultérieurs reposant sur ces mises à jour de l'utilisateur sera à jour lors de l'exécution de l'étape suivante.

## Création d'une mise à jour de l'utilisateur

Glissez-déposez le composant depuis la barre latérale ou cliquez sur le bouton plus <i class="fas fa-plus-circle"></i> en bas de la variante ou de l'étape et sélectionnez **Mise à jour de l'utilisateur**. 

Trois options vous permettent de mettre à jour les informations du profil utilisateur existant, d'en ajouter de nouvelles ou d'en supprimer. Toutes combinées, les étapes de mise à jour des utilisateurs dans un espace de travail peuvent mettre à jour jusqu'à 200 000 profils utilisateurs par minute.

{% alert tip %}
Vous pouvez également tester les modifications apportées à l'aide de ce composant en recherchant un utilisateur et en lui appliquant la modification. L'utilisateur est alors mis à jour.
{% endalert %}

### Mise à jour des attributs personnalisés

Pour ajouter ou mettre à jour un attribut personnalisé, sélectionnez un nom d'attribut dans votre liste d'attributs et saisissez la valeur de la clé.

\![Étape de mise à jour de l'utilisateur qui met à jour les deux attributs "Membre fidèle" et "Programme de fidélité" à "true".]({% image_buster /assets/img_archive/canvas_user_update_update.png %}){: style="max-width:90%;"}

### Suppression des attributs personnalisés

Pour supprimer un attribut personnalisé, sélectionnez un nom d'attribut à l'aide du menu déroulant. Vous pouvez passer au [compositeur JSON avancé](#advanced-json-composer) pour le modifier davantage. 

\![Étape de mise à jour de l'utilisateur qui supprime un attribut "Membre Fidèle".]({% image_buster /assets/img_archive/canvas_user_update_remove.png %}){: style="max-width:90%;"}

### Valeurs croissantes et décroissantes

L'étape de mise à jour par l'utilisateur peut augmenter ou diminuer la valeur d'un attribut. Sélectionnez l'attribut, sélectionnez **Incrémenter par** ou **Décrémenter par** et entrez un nombre. 

#### Suivre les progrès hebdomadaires

En incrémentant un attribut personnalisé qui suit un événement, vous pouvez suivre le nombre de cours qu'un utilisateur a suivis en une semaine. Grâce à ce composant, le décompte des classes peut être réinitialisé au début de la semaine et recommencer le suivi. 

\![Étape de mise à jour de l'utilisateur qui incrémente l'attribut "class_count" d'une unité.]({% image_buster /assets/img_archive/canvas_user_update_increment.png %}){: style="max-width:90%;"}

### Mise à jour d'un tableau d'objets

Un [tableau d'objets]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/array_of_objects/) est un attribut personnalisé stocké sur le profil d'un utilisateur et riche en données. Cela vous permet de créer un historique des interactions de l'utilisateur avec votre marque. Cela vous permet de créer des segments basés sur un attribut personnalisé qui est un champ calculé, comme l'historique des achats ou la valeur vie totale.

L'étape de mise à jour de l'utilisateur peut ajouter ou supprimer des attributs à ce tableau d'objets. Pour mettre à jour un tableau, sélectionnez le nom de l'attribut du tableau dans votre liste d'attributs et saisissez la valeur de la clé.

#### Cas d'utilisation : Mise à jour de la liste de souhaits d'un utilisateur

L'ajout ou la suppression d'un élément dans un tableau met à jour la liste de souhaits de l'utilisateur.

\![Étape de mise à jour de l'utilisateur qui ajoute un élément "crème solaire" à l'attribut "items_in_wishlist".]({% image_buster /assets/img_archive/canvas_user_update_wishlist.png %}){: style="max-width:90%;"}

#### Cas d'utilisation : Calculer le total du panier d'achat

Déterminez quand un utilisateur a des articles dans son panier, quand il en ajoute de nouveaux ou en supprime, et quelle est la valeur totale du panier. 

1. Créez un tableau d'objets personnalisé appelé `shopping_cart`. L'exemple suivant montre à quoi peut ressembler cet attribut. Chaque élément a un `product_id` unique qui contient des données plus complexes dans son propre tableau d'objets imbriqués, y compris `price`.

{% raw %}
```javascript
{
  "attributes": [
    {
      "shopping_cart": [
       {
         "total_cart_value": number,
         "shipping": number,
         "items_in_cart": number,
         "product_id": array,
         "gift": boolean,
         "discount_code": "enum",
         "timestamp": {"$time" : "{{$isoTimestamp}}"},
       }
      ]
    }
  ]
}
```
{% endraw %}

{:start="2"}
2\. Créez un [événement personnalisé]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) nommé `add_item_to_cart` qui est enregistré lorsqu'un utilisateur ajoute un article au panier.
3\. Créez un canvas avec une audience ciblée d'utilisateurs grâce à cet événement personnalisé. Désormais, lorsqu'un utilisateur ajoute un article à son panier, ce Canvas est déclenché. Vous pouvez ensuite cibler des messages directement sur cet utilisateur, en lui proposant des codes de réduction lorsqu'il a atteint un certain montant de dépenses, abandonné son panier pendant un certain temps, ou toute autre chose qui s'aligne sur votre cas d'utilisation. 

L'attribut `shopping_cart` contient le total de nombreux événements personnalisés : le coût total de tous les articles, le nombre total d'articles dans le panier, si le panier contient un cadeau, etc. Cela peut ressembler à ce qui suit :

{% raw %}
```javascript
{
  "attributes": [
    {
      "shopping_cart": [
       {
         "total_cart_value": 22.99,
         "shipping": 4.99,
         "items_in_cart": 2,
         "product_id": ["1001", "1002"]
         "gift": yes,
         "discount_code": "flashsale1000",
         "timestamp": {"$time" : "{{$isoTimestamp}}"},
       }
      ]
    }
  ]
}
```
{% endraw %}

## Définition de la propriété d'entrée du canvas en tant qu'attribut

Vous pouvez utiliser l'étape de mise à jour de l'utilisateur pour maintenir une `canvas_entry_property`. Imaginons que vous ayez un événement qui se déclenche lorsqu'un article est ajouté à un panier. Vous pouvez enregistrer l'ID du dernier article ajouté au panier et l'utiliser pour une campagne de remarketing. Utilisez la fonctionnalité de personnalisation pour récupérer une propriété d'entrée de Canvas et la stocker dans un attribut.

\![Étape de mise à jour de l'utilisateur qui met à jour l'attribut "most_recent_cart_item" avec un ID d'article.]({% image_buster /assets/img_archive/canvas_user_update_cep.png %}){: style="max-width:90%;"}

### Personnalisation

Pour stocker la propriété de l'événement déclencheur d'un Canvas en tant qu'attribut, utilisez la modale de personnalisation pour extraire et stocker la propriété d'entrée du Canvas. La mise à jour des utilisateurs prend également en charge les fonctionnalités de personnalisation suivantes : 
* [Contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) 
* [Blocs de contenu]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/)
* [Propriétés d'entrée]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/canvas_persistent_entry_properties/)
* Logique des liquides (y compris l'[interruption des messages)]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/)
* Mises à jour multiples d'attributs ou d'événements par objet

{% alert warning %}
Nous vous recommandons d'utiliser avec précaution la personnalisation du contenu connecté Liquid dans les étapes de mise à jour de l'utilisateur, car ce type d'étape a une limite de débit de 200 000 demandes par minute. Cette limite de débit prévaut sur la limite de débit de Canvas.
{% endalert %}

## Compositeur JSON avancé

Ajoutez un attribut, un événement ou un objet JSON d'achat d'une longueur maximale de 65 536 caractères au compositeur JSON. L'état de l' [abonnement global]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-states) et du [groupe d'abonnement d']({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-groups) un utilisateur peut également être défini.

\![]({% image_buster /assets/img_archive/canvas_user_update_composer.png %}){: style="max-width:90%;"}

À l'aide du compositeur avancé, vous pouvez également prévisualiser et tester que le profil utilisateur est mis à jour avec les modifications grâce à l'onglet **Prévisualisation et test.**  Vous pouvez soit sélectionner un utilisateur au hasard, soit rechercher un utilisateur spécifique. Ensuite, après avoir envoyé un test à un utilisateur, affichez le profil utilisateur à l'aide du lien généré.

\![]({% image_buster /assets/img_archive/canvas_user_update_test_preview.png %}){: style="max-width:90%;"}

### Considérations

Vous n'avez pas besoin d'inclure des données sensibles comme votre clé API lors de l'utilisation du compositeur JSON, car elles sont automatiquement fournies par la plateforme. Les champs suivants sont donc inutiles et ne doivent pas être utilisés dans le compositeur JSON :
* ID externe
* clé API
* URL du cluster Braze
* Champs liés à l'importation de jetons de poussée

{% raw %}
### Enregistrer les événements personnalisés

À l'aide du compositeur JSON, vous pouvez également enregistrer des événements personnalisés. Notez que cela nécessite un horodatage au format ISO, il est donc nécessaire d'assigner une heure et une date avec Liquid au début. Prenons l'exemple suivant, qui enregistre un événement avec une heure.

```
{% assign timestamp = 'now' | date: "%Y-%m-%dT%H:%M:%SZ" %}
{
  "events": [
    {
      "name": "logged_user_event",
      "time": "{{timestamp}}"
    }
  ]
}
```

L'exemple suivant lie un événement à une application spécifique en utilisant un événement personnalisé avec des propriétés facultatives et l'adresse `app_id`.

```
{% assign timestamp = 'now' | date: "%Y-%m-%dT%H:%M:%SZ" %}
{
  "events": [
    {
      "app_id": "insert_app_id",
      "name": "rented_movie",
      "time": "{{timestamp}}",
      "properties": {
        "release": {
          "studio": "FilmStudio",
          "year": "2022"
        },
        "cast": [
          {
            "name": "Actor1"
          },
          {
            "name": "Actor2"
          }
        ]
      }
    }
  ]
}
```

### Modifier l'état de l'abonnement

Dans le compositeur JSON, vous pouvez également modifier l'état de l'abonnement de votre utilisateur. Par exemple, voici l'état de l'abonnement d'un utilisateur mis à jour à `opted_in`. 

```
{
  "attributes": [
    {
      "email_subscribe": "opted_in"
    }
  ]
}
```

### Mise à jour des groupes d'abonnement 

Vous pouvez également mettre à jour les groupes d'abonnement à l'aide de cette étape du canvas. L'exemple suivant montre une mise à jour des groupes d'abonnement. Vous pouvez effectuer une ou plusieurs mises à jour de groupes d'abonnement.

```
{
  "attributes": [
    {
      "subscription_groups": [
        {
          "subscription_group_id": "subscription_group_identifier_1",
          "subscription_state": "subscribed"
        },
        {
          "subscription_group_id": "subscription_group_identifier_2",
          "subscription_state": "subscribed"
        },
        {
          "subscription_group_id": "subscription_group_identifier_3",
          "subscription_state": "subscribed"
        }
      ]
    }
  ]
}
```
{% endraw %}

