---
nav_title: Propriétés d’entrées persistantes
article_title: Propriétés d’entrées persistantes
alias: "/persistent_entry/"
page_type: reference
description: "Cet article de référence décrit comment utiliser des propriétés d’entrées persistantes dans votre Canvas pour envoyer des messages mieux agencés et créer une expérience d’utilisateur final améliorée."
tool: Canvas
page_order: 5
---

# Propriétés d’entrées persistantes

> Lorsqu'un Canvas est déclenché par un événement personnalisé, un achat ou un appel API, vous pouvez utiliser les métadonnées de l'appel API, de l'événement personnalisé ou de l'événement d'achat pour la personnalisation à chaque étape de votre flux de travail Canvas. 

Avant cette fonctionnalité, les propriétés d’entrée pouvaient être utilisées uniquement dans la première étape du Canvas. La possibilité d’utiliser des propriétés d’entrée dans un parcours de Canvas permet aux clients d’envoyer des messages mieux agencés et de créer une expérience utilisateur final améliorée.

## Utilisation des propriétés d’entrées

Les propriétés d’entrées peuvent être utilisées dans des Canvas par événement et déclenchées par une API. Ces propriétés d’entrées sont définies lorsqu’un Canvas est déclenché par un événement personnalisé, un achat ou un appel API. Reportez-vous aux articles suivants pour en savoir plus :

- [Objet Propriétés d’entrées de Canvas]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/)
- [Objet de propriétés de l’événement]({{site.baseurl}}/api/objects_filters/event_object/)
- [Objet Achat]({{site.baseurl}}/api/objects_filters/purchase_object/#purchase-product_id)

Les propriétés transférées à partir de ces objets peuvent être référencées à l’aide de la `canvas_entry_properties` Balise Liquid. Par exemple, une demande avec `\"canvas_entry_properties\" : {\"product_name\" : \"shoes\", \"product_price\" : 79.99}` pourrait ajouter le terme « chaussures » à un message en ajoutant le Liquid {% raw %}`{{canvas_entry_properties.${product_name}}}`{% endraw %}.

Lorsqu'un Canvas inclut un message avec l'étiquette Liquid `canvas_entry_properties`, les valeurs associées à ces propriétés sont enregistrées pour la durée du parcours de l'utilisateur dans le Canvas et supprimées lorsque l'utilisateur quitte le Canvas. Notez que les propriétés d’entrée de Canvas sont uniquement disponibles pour référence dans Liquid. Pour filtrer sur les propriétés du canvas, utilisez plutôt la [segmentation des propriétés d'événement]({{site.baseurl}}/user_guide/data/custom_data/custom_events/nested_objects/).

{% alert note %}
La limite maximale de taille de l’objet Propriétés d’entrées de Canvas est de 50 Ko.
{% endalert %}

## Mise à jour de Canvas pour utiliser des propriétés d’entrées

Si un Canvas actif qui ne comprenait pas précédemment de message utilisant `canvas_entry_properties` est modifié pour inclure `canvas_entry_properties`, la valeur correspondant à cette propriété ne sera pas disponible pour les utilisateurs ayant saisi le Canvas avant l’ajout de `canvas_entry_properties` au Canvas. Les valeurs seront uniquement sauvegardées pour les utilisateurs qui saisissent le Canvas après la modification.

Par exemple, si vous avez lancé initialement un Canvas qui n’utilisait pas de propriétés d’entrées le 3 novembre, puis avez ajouté une nouvelle propriété `product_name` au Canvas le 11 novembre, les valeurs pour `product_name` seraient uniquement sauvegardées pour des utilisateurs ayant saisi le Canvas après le 11 novembre.

Si une propriété d’entrée de Canvas est nulle ou vide, vous pouvez annuler les messages à l’aide de conditions. L'extrait de code suivant est un exemple de la manière dont vous pourriez utiliser Liquid pour interrompre un message.
{%raw%}
```
{% if canvas_entry_properties.${product_name} == blank %}
{% abort_message() %}
{% endif %}
```
{%endraw%}

Pour en savoir plus sur l'annulation de messages avec Liquid, consultez notre [documentation Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/#aborting-messages).

## Propriétés d’entrées globales de Canvas

`canvas_entry_properties` vous permet de définir des propriétés globales qui s’appliquent à tous les utilisateurs ou des propriétés spécifiques à l’utilisateur qui s’appliquent uniquement à l’utilisateur indiqué. La propriété spécifique à l’utilisateur remplacera la propriété globale pour cet utilisateur.

### Exemple de demande

```
url -X POST \
-H 'Content-Type:application/json' \
-d '{
      "api_key": "a valid rest api key",
      "canvas_id": "the ID of your Canvas",
         "canvas_entry_properties": {
            "food_allergies": "none"
          },
      "recipients": [
        {
          "external_user_id": Customer_123,
          "canvas_entry_properties": {
            "food_allergies": ["dairy", "soy"],
            "nutrition": {
              "calories_per_serving": 200,
              "serving_size_in_ounces": 4
            }
          }
        }
      ]
    }' \
```
 
Dans cette demande, la valeur globale pour « allergies alimentaires » est « aucune ». Pour Customer_123, la valeur est "dairy". Les messages de ce Canvas contenant l'extrait de code liquide {%raw%}`{{canvas_entry_properties.${food_allergies}}}`{%endraw%} auront pour modèle "dairy" pour Customer_123 et "none" pour tous les autres. 

## Cas d’utilisation

Si vous avez un Canvas qui se déclenche lorsqu'un utilisateur parcourt un article sur votre site eCommerce mais ne l'ajoute pas à son panier, la première étape du Canvas pourrait être une notification push lui demandant s'il est intéressé par l'achat de l'article. Vous pourriez faire référence au nom du produit en utilisant {% raw %}`{{canvas_entry_properties.${product_name}}}`{% endraw %}

![]({% image_buster /assets/img/persistent_entry_properties/PEP1.png %}){: style="border:0;margin-left:15px;"}

Dans la seconde étape, une autre notification push pourrait être envoyée, invitant l’utilisateur à vérifier s’il a ajouté l’article dans le panier mais ne l’a pas encore acheté. Vous pouvez continuer à faire référence à la propriété d'entrée `product_name` en utilisant {% raw %}`{{canvas_entry_properties.${product_name}}}`{% endraw %}.

![]({% image_buster /assets/img/persistent_entry_properties/PEP12.png %}){: style="border:0;margin-left:15px;"}

