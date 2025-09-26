---
nav_title: Mise à jour utilisateur 
article_title: Mise à jour utilisateur 
alias: "/user_update/"
page_order: 6
page_type: reference
description: "Cet article de référence aborde le composant de mises à jour de l’utilisateur et la façon de l’utiliser dans votre Canvas."
tool: Canvas
---

# Mise à jour utilisateur 

> Le composant User Update (Mise à jour de l’utilisateur) vous permet de mettre à jour les attributs, événements et achats d’un utilisateur dans un éditeur JSON. Il n’est donc pas nécessaire d’inclure des informations sensibles, par exemple des clés API.

## Fonctionnement de ce composant

![Une étape de mise à jour de l'utilisateur nommée "Mise à jour de la loyauté" qui met à jour un attribut "Est membre Premium" à "true".]({% image_buster /assets/img_archive/canvas_user_update_step.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

Lorsque vous utilisez ce composant dans votre Canvas, les mises à jour ne sont pas prises en compte dans votre limite de débit de `/users/track` requêtes par minute. Au lieu de cela, les mises à jour sont regroupées pour que Braze puisse les traiter plus efficacement qu’un webhook Braze-à-Braze. Notez que ce composant ne consomme pas de [points de données]({{site.baseurl}}/user_guide/data/data_points/) lorsqu'il est utilisé pour mettre à jour des points de données non facturables (tels que les groupes d'abonnement).

Les utilisateurs ne passeront à l’étape Canvas suivante qu’une fois les mises à jour pertinentes de l’utilisateur effectuées. Cela signifie que tout envoi de messages ultérieurs reposant sur ces mises à jour de l'utilisateur sera à jour lors de l'exécution de l'étape suivante.

## Création d'une mise à jour de l'utilisateur

Glissez-déposez le composant depuis la barre latérale ou cliquez sur le bouton plus <i class="fas fa-plus-circle"></i> en bas de la variante ou de l'étape et sélectionnez **Mise à jour de l'utilisateur**. 

Il existe trois options qui vous permettent de mettre à jour les informations existantes, d’ajouter de nouvelles ou de supprimer des informations de profil utilisateur. Toutes combinées, les étapes de mise à jour des utilisateurs dans un espace de travail peuvent mettre à jour jusqu'à 200 000 profils utilisateurs par minute.

{% alert tip %}
Vous pouvez également tester les modifications apportées à ce composant en recherchant un utilisateur et en lui appliquant la modification. Cela mettra à jour l’utilisateur.
{% endalert %}

### Mise à jour des attributs personnalisés

Pour ajouter ou mettre à jour un attribut personnalisé, sélectionnez un nom d’attribut dans votre liste d’attributs et entrez la valeur clé.

![Étape de mise à jour de l'utilisateur qui met à jour les deux attributs "Membre fidèle" et "Programme de fidélité" à "true".]({% image_buster /assets/img_archive/canvas_user_update_update.png %}){: style="max-width:90%;"}

### Suppression des attributs personnalisés

Pour supprimer un attribut personnalisé, sélectionnez un nom d’attribut à l’aide de la liste déroulante. Vous pouvez passer au [compositeur JSON avancé](#advanced-json-composer) pour apporter d’autres modifications. 

![Étape de mise à jour de l'utilisateur qui supprime l'attribut "Membre fidèle".]({% image_buster /assets/img_archive/canvas_user_update_remove.png %}){: style="max-width:90%;"}

### Valeurs croissantes et décroissantes

L'étape de mise à jour par l'utilisateur peut augmenter ou diminuer la valeur d'un attribut. Sélectionnez l'attribut, sélectionnez **Incrémenter par** ou **Décrémenter par** et entrez un nombre. 

#### Suivi des progrès hebdomadaires

En incrémentant un attribut personnalisé qui suit un événement, vous pouvez suivre le nombre de cours qu'un utilisateur a suivis en une semaine. À l’aide de ce composant, le nombre de cours peut être réinitialisé au début de la semaine avant de recommencer le suivi. 

![Étape de mise à jour de l'utilisateur qui incrémente l'attribut "class_count" d'une unité.]({% image_buster /assets/img_archive/canvas_user_update_increment.png %}){: style="max-width:90%;"}

### Mise à jour d'un tableau d'objets

Un [tableau d'objets]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/array_of_objects/) est un attribut personnalisé stocké sur le profil d'un utilisateur et riche en données. Cela vous permet de créer un historique des interactions de l'utilisateur avec votre marque. Cela vous permet de créer des segments sur la base d'un attribut personnalisé qui est un champ calculé, comme l'historique des achats ou la valeur vie totale.

L'étape de mise à jour de l'utilisateur peut ajouter ou supprimer des attributs à ce tableau d'objets. Pour mettre à jour un tableau, sélectionnez le nom de l'attribut du tableau dans votre liste d'attributs et saisissez la valeur de la clé.

#### Cas d’utilisation : Mise à jour de la liste de souhaits d'un utilisateur

L'ajout ou la suppression d'un élément dans un tableau met à jour la liste de souhaits de l'utilisateur.

![Utilisateur Mise à jour de l'étape qui ajoute un article "crème solaire" à l'attribut "articles_dans_la_liste_de_souvenirs".]({% image_buster /assets/img_archive/canvas_user_update_wishlist.png %}){: style="max-width:90%;"}

#### Cas d’utilisation : Calculer le total du panier d'achat

Déterminez quand un utilisateur a des articles dans son panier, quand il en ajoute de nouveaux ou en supprime, et quelle est la valeur totale du panier. 

1. Créez un tableau d'objets personnalisé appelé `shopping_cart`. L'exemple suivant montre à quoi peut ressembler cet attribut. Chaque élément possède un `product_id` unique qui contient des données plus complexes dans son propre tableau d'objets imbriqué, y compris `price`.

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
3\. Créez un canvas avec une audience ciblée d'utilisateurs grâce à cet événement personnalisé. Désormais, lorsqu'un utilisateur ajoute un article à son panier, ce canvas est déclenché. Vous pouvez ensuite cibler votre communication directement sur cet utilisateur, en lui proposant des codes de réduction lorsqu'il a atteint un certain montant de dépenses, lorsqu’il a abandonné son panier pendant un certain temps, ou tout autre facteur en adéquation avec votre cas d'utilisation. 

L'attribut `shopping_cart` contient le total de nombreux événements personnalisés : le coût total de tous les articles, le nombre total d'articles dans le panier, si le panier contient un cadeau, etc. Ceci peut ressembler à ce qui suit :

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

Vous pouvez utiliser l’étape de mise à jour de l’utilisateur pour faire persister un `canvas_entry_property`. Imaginons que vous ayez un événement qui se déclenche lorsqu’un article est ajouté à un panier. Vous pouvez stocker l’ID de l’article le plus récemment ajouté au panier et l’utiliser pour une campagne de remarketing. Utilisez la fonctionnalité de personnalisation pour récupérer une propriété d’entrée Canvas et la stocker dans un attribut.

![Étape de mise à jour de l'utilisateur qui met à jour l'attribut "most_recent_cart_item" avec l'ID d'un article.]({% image_buster /assets/img_archive/canvas_user_update_cep.png %}){: style="max-width:90%;"}

### Personnalisation

Pour stocker la propriété de l’événement déclencheur d’un Canvas comme un attribut, utilisez le modal de personnalisation pour extraire et stocker la propriété d’entrée de Canvas. La mise à jour de l’utilisateur prend également en charge les fonctionnalités de personnalisation suivantes : 
* [Contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) 
* [Blocs de contenu]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/)
* [Propriétés d'entrée]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/canvas_persistent_entry_properties/)
* Logique Liquid (y compris l'[annulation de messages]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/))
* Plusieurs mises à jour d’attribut ou d’événement par objet

{% alert warning %}
Nous vous recommandons d'utiliser avec précaution la personnalisation du contenu connecté Liquid dans les étapes de mise à jour de l'utilisateur, car ce type d'étape a une limite de débit de 200 000 demandes par minute. Cette limite de débit prévaut sur la limite de débit de Canvas.
{% endalert %}

## Compositeur JSON avancé

Ajoutez un attribut, un événement ou un objet JSON d'achat d’un maximum de 65 536 caractères à l’éditeur JSON. L'état de l'[abonnement global]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-states) et du [groupe d'abonnement]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-groups) d’un utilisateur peut également être défini.

![]({% image_buster /assets/img_archive/canvas_user_update_composer.png %}){: style="max-width:90%;"}

À l'aide du compositeur avancé, vous pouvez également prévisualiser et tester que le profil utilisateur est mis à jour avec les modifications grâce à l'onglet **Prévisualisation et test.**  Vous pouvez sélectionner un utilisateur aléatoire ou rechercher un utilisateur spécifique. Ensuite, après avoir envoyé un test à un utilisateur, affichez le profil utilisateur en utilisant le lien généré.

![]({% image_buster /assets/img_archive/canvas_user_update_test_preview.png %}){: style="max-width:90%;"}

### Considérations

Vous n’avez pas besoin d’inclure de données sensibles telles que votre clé API lorsque vous utilisez le compositeur JSON, car elles sont automatiquement fournies par la plateforme. Ainsi, les champs suivants ne sont pas nécessaires et ne doivent pas être utilisés dans le compositeur JSON :
* ID utilisateur externe
* Clé API
* URL du cluster Braze
* Champs liés aux importations de jetons de notification push

{% raw %}
### Consigner un événement personnalisé

À l’aide du composeur JSON, vous pouvez également enregistrer des événements personnalisés. Notez que cela nécessite un horodatage au format ISO, il est donc nécessaire d’attribuer une heure et une date avec du Liquid au début. Prenons cet exemple qui enregistre un événement avec une heure.

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

Cet exemple suivant relie un événement à une application spécifique à l’aide d’un événement personnalisé avec des propriétés facultatives et l’`app_id`.

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

Dans le compositeur JSON, vous pouvez également modifier l'état de l'abonnement de votre utilisateur. Par exemple, voici l'état de l'abonnement d'un utilisateur mis à jour sur `opted_in`. 

```
{
  "attributes": [
    {
      "email_subscribe": "opted_in"
    }
  ]
}
```

### Mettre à jour les groupes d’abonnement SMS 

Vous pouvez également mettre à jour les groupes d'abonnement à l'aide de cette étape du canvas. L'exemple suivant montre une mise à jour des groupes d'abonnement. Vous pouvez effectuer une ou plusieurs mises à jour de groupe d'abonnement.

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

