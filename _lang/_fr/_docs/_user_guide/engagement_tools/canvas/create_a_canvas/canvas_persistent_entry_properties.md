---
nav_title: Propriétés d'entrées persistantes
article_title: Propriétés d'entrées persistantes
alias: "/entrée_persistante/"
page_type: Référence
description: "Cet article de référence décrit comment utiliser les propriétés d'entrée persistantes dans votre Canvas pour envoyer plus de messages organisés et créer une expérience utilisateur finale."
tool: Toile
page_order: 5
---

# Propriétés de l'entrée persistante de la toile

Lorsqu'un Canvas est déclenché par un événement personnalisé, un achat ou un appel API, les clients sont maintenant en mesure d'utiliser des métadonnées à partir de l'appel API, un événement personnalisé ou un événement pour la personnalisation à chaque étape du Canvas. **Avant cette fonctionnalité, les propriétés d'entrée ne pouvaient être utilisées qu'à la première étape de Canvas**. La possibilité d’utiliser les propriétés d’entrée à travers un parcours de Canvas permet aux clients d’envoyer plus de messages organisés et de créer une expérience utilisateur très raffinée.

{% alert important %}
Cette fonctionnalité est actuellement en version bêta. Veuillez contacter votre responsable de compte Braze pour plus d'informations.
{% endalert %}

## Utiliser les propriétés de l'entrée

Les propriétés d'entrée peuvent être utilisées dans les Canvasses basées sur l'action et déclenchées par API. Ces propriétés d'entrée sont définies lorsqu'un Canvas est déclenché par un événement, un achat ou un appel API. Consultez notre documentation pour en savoir plus sur l'objet [Propriétés de l'entrée du canvas]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/), [Event Properties Object]({{site.baseurl}}/api/objects_filters/event_object/), et [Purchase Object]({{site.baseurl}}/api/objects_filters/purchase_object/#purchase-product_id).

Les propriétés passées de ces objets peuvent être référencées en utilisant la balise `canvas_entry_properties` Liquid.

- Par exemple, une requête avec `\"canvas_entry_properties\" : {\"product_name\" : \"shoes\", \"product_price\" : 79. 9}` pourrait ajouter le mot "chaussures" à un message en ajoutant les Liquides {% raw %}`{{canvas_entry_properties.${product_name}}}`{% endraw %}.

Lorsqu'une toile inclut un message avec la balise `canvas_entry_properties` Liquid, les valeurs associées à ces propriétés seront enregistrées pour la durée du voyage d'un utilisateur dans le Canvas et supprimées une fois que l'utilisateur quittera le Canvas.

{% alert important %}
Si votre Canevas comprend une fenêtre de rééligibilité inférieure à la durée totale du Canvas et que vous utilisez `canvas_entry_properties` au-delà de la première étape de votre Canvas, Seules les **étapes de message** sont autorisées. **Les pas complets** ne sont pas autorisés avec ces paramètres en raison du cas d'arête suivant. <br><br> La fenêtre de rééligibilité devrait-elle être inférieure à la durée maximale du Canvas, un utilisateur sera autorisé à re-saisir et à recevoir plus d'un message de chaque étape. Dans le cas où la ré-entrée d'un utilisateur atteint la même étape que son entrée précédente, Braze ne fera que dédupliquer les messages de cette étape si les messages sont programmés pour s’envoyer dans les 5 minutes qui suivent.
{% endalert %}

## Étape de Canvas basée sur l'action

Lorsque `canvas_entry_properties` et `event_properties` sont tous deux référencés dans une étape basée sur l'action d'un Canvas basé sur l'action ou déclenchée par l'API :
- `canvas_entry_properties` va modéliser avec des propriétés associées à l'événement personnalisé, achat ou appel API qui a déclenché le Canvas.
- `event_properties` va modéliser avec des propriétés associées à l'événement personnalisé ou acheter qui a déclenché l'étape.

{% alert note %}
Pour les étapes de message Canvas , `event_properties` ne sont pas pris en charge. Au lieu de cela, utilisez `canvas_entry_properties`.
{% endalert %}

## Mise à jour de Canvas pour utiliser les propriétés d'entrée

Si une toile active qui n'incluait pas auparavant de messages qui utilisent `canvas_entry_properties` est modifiée pour inclure `canvas_entry_properties`, la valeur correspondant à cette propriété ne sera pas disponible pour les utilisateurs qui sont entrés dans le Canvas avant que `canvas_entry_properties` n'ait été ajouté aux Canevas. Les valeurs ne seront enregistrées que pour les utilisateurs qui entrent dans le Canvas après la modification.

Par exemple : Si vous lancez initialement une toile qui n'utilise aucune propriété d'entrée le 3 novembre, puis a ajouté une nouvelle propriété `product_name` sur le Canvas le 11 Novembre, les valeurs pour `product_name` ne seront enregistrées que pour les utilisateurs qui sont entrés dans Canvas le 11 novembre.

Dans le cas où une propriété d'entrée Canvas est nulle ou vide, vous pouvez annuler les messages en utilisant des conditions. Le code snippet suivant est un exemple de la façon dont vous pouvez utiliser Liquid pour annuler un message.
{%raw%}
```
{% si canvas_entry_properties.${product_name} == vide %}
{% abort_message() %}
{% endif %}
```
{%endraw%}

Pour en savoir plus sur les messages d'abandon avec Liquid, consultez notre [documentation Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/#aborting-messages).

## Propriétés globales de l'entrée du canevas

Avec `canvas_entry_properties`, vous pouvez définir des propriétés globales qui s'appliquent à tous les utilisateurs ou aux propriétés spécifiques à l'utilisateur qui s'appliquent uniquement à l'utilisateur spécifié. La propriété spécifique à l'utilisateur remplacera la propriété globale pour cet utilisateur.

Exemple de requête API en utilisant les propriétés d'entrée de Canvas globales :
```
url -X POST \
-H 'Content-Type:application/json' \
-d '{
      "api_key": "une clé api de repos valide",
      "canvas_id": "l'ID de votre toile",
         "canvas_entry_properties": {
            "food_allergies": "none"
          },
      "destinataires": [
        {
          "external_user_id": Customer_123,
          "canvas_entry_properties": {
            "food_allergies": “dairy”
          }
        }
      ]
    }' \
```

Dans la demande ci-dessus, la valeur globale des « allergies alimentaires » est « nulle ». Pour le client_123, la valeur est « dairy ». Messages dans ce Canvas contenant le snippet de Liquide {%raw%}`{{canvas_entry_properties.${food_allergies}}}`{%endraw%} va modéliser avec « dairy» pour le client_123 et « aucun» pour tout le monde.

## Cas d'utilisation

Si vous avez une toile qui est déclenchée lorsqu'un utilisateur navigue un article dans votre site de commerce électronique mais ne l'ajoute pas à son panier, la première étape de la Canvas pourrait être une notification push demandant si elle est intéressée par l'achat de l'objet. Vous pouvez référencer le nom du produit en utilisant {% raw %}`{{canvas_entry_properties.$(product_name)}}`{% endraw %}

!\[Exemple de nom de produit\]\[1\]{: style="border:0;margin-left:15px;"}

La deuxième étape peut envoyer une autre notification push invitant l'utilisateur à passer la commande s'il a ajouté l'article à son panier mais ne l'a pas encore acheté. Vous pouvez continuer à référencer la propriété `product_name` entrée en utilisant {% raw %}`{{canvas_entry_properties.$(product_name)}}`{% endraw %}.

!\[Exemple\]\[2\]{: style="border:0;margin-left:15px;"}
[1]:{% image_buster /assets/img/persistent_entry_properties/PEP1.png %} [2]:{% image_buster /assets/img/persistent_entry_properties/PEP12.png %}
