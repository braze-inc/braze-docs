---
nav_title: "propriétés d'entrées persistantes"
article_title: "propriétés d'entrées persistantes"
alias: "/persistent_entry/"
page_type: reference
description: "Cet article de référence décrit comment utiliser les propriétés d'entrées persistantes dans votre Canvas pour envoyer des messages plus soignés et créer une expérience finale très raffinée pour l'utilisateur."
tool: Canvas
page_order: 5
---

# propriétés d'entrées persistantes

> Lorsqu'un Canvas est déclenché par un événement personnalisé, un achat ou un appel API, vous pouvez utiliser les métadonnées de l'appel API, de l'événement personnalisé ou de l'événement d'achat pour la personnalisation à chaque étape de votre flux de travail Canvas. Vous pouvez utiliser ces propriétés pour envoyer des messages plus élaborés.

{% alert important %}
Les propriétés d'entrées persistantes sont un artefact de l'éditeur Canvas d'origine, il y a donc des références obsolètes à des termes qui restent pour référence historique. Pour la mise à jour actuelle de l'éditeur de canvas, reportez-vous aux [propriétés d'entrée du canvas et aux propriétés d'événement]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties).
{% endalert %}

## Utilisation des propriétés d'entrée

Les propriétés d'entrée peuvent être utilisées dans les toiles basées sur des actions et déclenchées par l'API. Ces propriétés d'événement sont définies lorsqu'un canvas est déclenché par un événement personnalisé, un achat ou un appel API. Reportez-vous aux articles suivants pour plus d'informations :

- [Objet des propriétés de l'entrée dans le canvas]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/)
- [Objet de propriétés d'événement]({{site.baseurl}}/api/objects_filters/event_object/)
- [Objet de l'achat]({{site.baseurl}}/api/objects_filters/purchase_object/#purchase-product_id)

Les propriétés transmises par ces objets peuvent être référencées à l'aide de l'étiquette Liquid `canvas_entry_properties`. Par exemple, une demande avec `\"canvas_entry_properties\" : {\"product_name\" : \"shoes\", \"product_price\" : 79.99}` pourrait ajouter le mot "chaussures" à un message en ajoutant le liquide {% raw %}`{{canvas_entry_properties.${product_name}}}`{% endraw %}.

Lorsqu'un Canvas inclut un message avec l'étiquette Liquid `canvas_entry_properties`, les valeurs associées à ces propriétés sont enregistrées pour la durée du parcours de l'utilisateur dans le Canvas et supprimées lorsque l'utilisateur quitte le Canvas. Notez que les propriétés de l'entrée Canvas ne sont disponibles que pour référence dans Liquid. Pour filtrer sur les propriétés du canvas, utilisez plutôt la [segmentation des propriétés d'événement]({{site.baseurl}}/user_guide/data/custom_data/custom_events/nested_objects/).

{% alert note %}
La taille maximale de l'objet Propriétés de l'entrée Canvas est de 50 Ko.
{% endalert %}

## Mise à jour du canvas pour utiliser les propriétés d'entrée

Si un canvas actif qui n'incluait pas de messages utilisant `canvas_entry_properties` est modifié pour inclure `canvas_entry_properties`, la valeur correspondant à cette propriété ne sera pas disponible pour les utilisateurs qui sont entrés dans le canvas avant que `canvas_entry_properties` ne soit ajouté au canvas. Les valeurs ne seront enregistrées que pour les utilisateurs qui entreront dans le Canvas après la modification.

Par exemple, si vous lancez initialement un canvas qui n'utilise aucune propriété d'entrée le 3 novembre, puis ajoutez une nouvelle propriété `product_name` au canvas le 11 novembre, les valeurs de `product_name` ne seront enregistrées que pour les utilisateurs qui entrent dans le canvas à partir du 11 novembre.

Dans le cas où une propriété d'entrée du canvas est nulle ou vide, vous pouvez interrompre les messages à l'aide de conditionnelles. L'extrait de code suivant est un exemple de la manière dont vous pourriez utiliser Liquid pour interrompre un message.
{%raw%}
```
{% if canvas_entry_properties.${product_name} == blank %}
{% abort_message() %}
{% endif %}
```
{%endraw%}

Pour en savoir plus sur l'interruption des messages avec Liquid, consultez notre [documentation sur Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/#aborting-messages).

## Propriétés globales de l'entrée dans le canvas

Avec `canvas_entry_properties`, vous pouvez définir des propriétés globales qui s'appliquent à tous les utilisateurs ou des propriétés spécifiques qui ne s'appliquent qu'à l'utilisateur spécifié. La propriété spécifique à l'utilisateur remplacera la propriété globale pour cet utilisateur.

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
 
Dans cette demande, la valeur globale pour "allergies alimentaires" est "aucune". Pour Customer_123,, la valeur est "dairy". Les messages de ce Canvas contenant l'extrait de code liquide {%raw%}`{{canvas_entry_properties.${food_allergies}}}`{%endraw%} auront pour modèle "dairy" pour Customer_123 et "none" pour tous les autres. 

## Cas d'utilisation

Si vous avez un Canvas qui se déclenche lorsqu'un utilisateur parcourt un article sur votre site eCommerce mais ne l'ajoute pas à son panier, la première étape du Canvas pourrait être une notification push lui demandant s'il est intéressé par l'achat de l'article. Vous pouvez référencer le nom du produit en utilisant {% raw %}`{{canvas_entry_properties.${product_name}}}`{% endraw %}

\![]({% image_buster /assets/img/persistent_entry_properties/PEP1.png %}){: style="border:0;margin-left:15px;"}

La deuxième étape peut envoyer une autre notification push invitant l'utilisateur à passer à la caisse s'il a ajouté l'article à son panier mais ne l'a pas encore acheté. Vous pouvez continuer à faire référence à la propriété d'entrée `product_name` en utilisant {% raw %}`{{canvas_entry_properties.${product_name}}}`{% endraw %}.

\![]({% image_buster /assets/img/persistent_entry_properties/PEP12.png %}){: style="border:0;margin-left:15px;"}

