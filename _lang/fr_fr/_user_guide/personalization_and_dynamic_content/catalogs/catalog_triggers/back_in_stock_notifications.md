---
nav_title: Notifications de rupture de stock
article_title: Notifications de rupture de stock
page_order: 2
description: "Cet article de référence décrit comment créer des notifications de rupture de stock dans les catalogues de Braze."
---

# Notifications de rupture de stock

> Utilisez une combinaison de notifications de retour en stock par le biais des catalogues de Braze et d'un Canvas pour avertir les clients qu'un article est de nouveau en stock. Chaque fois qu'un client effectue un événement personnalisé sélectionné, il peut être automatiquement abonné pour être informé du réapprovisionnement du produit.<br><br>Cette page explique comment fonctionnent les notifications de rupture de stock et comment vous pouvez les configurer et les utiliser.

Lorsqu'un utilisateur déclenche un événement personnalisé pour un produit, nous l'abonnons automatiquement pour qu'il reçoive des notifications de retour en stock pour ce produit. Lorsque la quantité d'inventaire du produit correspond à votre règle d'inventaire (par exemple, un inventaire supérieur à 100), tous les abonnés pourront recevoir des notifications par le biais d'une campagne ou d’un canvas. Cependant, seuls les utilisateurs ayant opté pour les notifications recevront des notifications. 

## Comment fonctionnent les notifications de rupture de stock ?

Vous définirez un événement personnalisé à utiliser comme événement d'abonnement, tel que l'événement `product_clicked`. Cet événement doit contenir une propriété de l'ID de l'article (ID des articles du catalogue). Nous vous suggérons d'inclure un nom de catalogue, mais ce n'est pas obligatoire. Vous indiquerez également le nom d'un champ de quantité d’inventaire, qui doit être de type numérique.

Lorsqu'un produit a une quantité en stock qui correspond à votre règle d'inventaire, nous recherchons tous vos utilisateurs qui sont abonnés à ce produit (les utilisateurs qui ont effectué l'événement d'abonnement) et nous envoyons un événement personnalisé Braze que vous pouvez utiliser pour déclencher une campagne ou un canvas.

Les propriétés d'événement sont envoyées en même temps que l'utilisateur, ce qui vous permet d'intégrer les détails du produit dans la campagne ou le canvas qui effectue l’envoi !

## Mise en place de notifications de retour en stock

Suivez ces étapes pour configurer les notifications de rupture de stock dans un catalogue spécifique.

1. Accédez à votre catalogue et sélectionnez l'onglet **Paramètres.** 
2. Sélectionnez la bascule **De retour en stock**.
3. Si les paramètres globaux de retour en stock n'ont pas été configurés, vous serez invité à définir les événements personnalisés et les propriétés qui seront utilisés pour déclencher les notifications de retour en stock :
    <br> ![Tiroir des paramètres du catalogue.][2]{: style="max-width:70%;"}
    - **Catalogue de secours** Il s'agit du catalogue qui sera utilisé pour l'abonnement aux notifications de retour en stock, si aucune propriété `catalog_name` n'est présente dans l'événement personnalisé.
    - **Custom event for subscriptions** est l'événement personnalisé de Braze qui sera utilisé pour abonner un utilisateur aux notifications de rupture de stock. Lorsque cet événement se produit, l'utilisateur qui l'a effectué est abonné.
    - **Custom event for unsubscribing** est l'événement personnalisé de Braze qui sera utilisé pour désinscrire un utilisateur des notifications de retour en stock. Cet événement est facultatif. Si l'utilisateur n'effectue pas cet événement, il sera désabonné au bout de 90 jours ou lorsque l'événement de rupture de stock se déclenchera, selon ce qui se produira en premier.
    - La **propriété d'événement de l’ID du produit** est la propriété de l'événement personnalisé ci-dessus qui sera utilisée afin de déterminer le produit pour un abonnement ou un désabonnement aux notifications de retour en stock. Cette propriété de l'événement personnalisé doit contenir un ID d'article présent dans un catalogue. L'événement personnalisé doit également contenir une propriété `catalog_name`, afin de spécifier le catalogue dans lequel se trouve cet article.
    
    - Un exemple d'événement personnalisé ressemblerait à ceci
    ```json
    {
        "events": [
            {
                "external_id": "<external_id>",
                "name": "subscription",
                "time": "2024-04-15T19:22:28Z",
                "properties": {
                    "id": "shirt-xl",
                    "catalog_name": "on_sale_products",
                    "type": ["back_in_stock"]
                }
            }
        ]
    }
    ```
{% alert note %}
Les déclencheurs de rupture de stock et de baisse de prix utilisent le même événement pour abonner l'utilisateur à la notification. Vous pouvez donc utiliser le tableau `type` pour définir les notifications de rupture de stock et de baisse de prix dans le même événement.
{% endalert %}

{: start="4"}
4\. Sélectionnez **Enregistrer** et continuez vers la page **Paramètres** du catalogue.
5\. Définissez votre règle de notification. Deux options existent :
    - **Notifier tous les utilisateurs abonnés** informe tous les clients en attente lorsque l'article est de nouveau en stock.
    - **Définir des limites de notification** notifie un nombre spécifié de clients par période de notification configurée. Braze informera le nombre de clients spécifié par incréments jusqu'à ce qu'il n'y ait plus de clients à informer ou jusqu'à ce que l'article soit en rupture de stock. Votre taux de notification ne peut pas dépasser 10 000 utilisateurs par minute.
6\. Définissez le **champ Inventaire dans le catalogue**. Ce champ du catalogue sera utilisé pour déterminer si l'article est en rupture de stock. Le champ doit être de type numérique.
7\. Sélectionnez **Enregistrer les paramètres**.

![Paramètres du catalogue qui montrent la fonctionnalité de retour en stock activée. Les règles de notification prévoient d'avertir un millier d'utilisateurs toutes les dix minutes.][1]

{% alert important %}
Les règles de notification de ces paramètres ne remplacent pas les paramètres de notification de Canvas, tels que les heures calmes.
{% endalert %}

## Utiliser les notifications de rupture de stock dans un canvas

Après avoir configuré la fonctionnalité de rupture de stock dans un catalogue, suivez les étapes suivantes pour l'utiliser avec Canvas.

1. Mettez en place un Canvas basé sur l'action.
2. Sélectionnez **Retour en stock** comme déclencheur.
3. Sélectionnez le nom du catalogue contenant les notifications de rupture de stock.
4. Continuez à [configurer]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) votre Canvas comme vous le feriez.

Désormais, vos clients peuvent être avertis lorsqu'un produit est à nouveau en stock.

### Utilisation de Liquid

Pour insérer des détails sur le produit du catalogue qui est de nouveau en stock, vous pouvez utiliser l'étiquette Liquid `canvas_entry_properties` pour accéder à l’`item_id`. 

L'utilisation de {%raw%}``{{canvas_entry_properties.${catalog_update}.item_id}}``{%endraw%} renvoie l'ID du produit qui est de nouveau disponible en stock. {%raw%}``{{canvas_entry_properties.${catalog_update}.previous_value}}``{%endraw%} renvoie la valeur d'inventaire du produit avant la mise à jour, et {%raw%}``{{canvas_entry_properties.${catalog_update}.new_value}}``{%endraw%} renvoie la nouvelle valeur d'inventaire après la mise à jour.

Utilisez cette étiquette Liquid {%raw%}``{% catalog_items <name_of_your_catalog> {{canvas_entry_properties.${catalog_update}.item_id}} %}``{%endraw%} en tête de votre message, puis utilisez {%raw%}``{{ items[0].<field_name> }}``{%endraw%} pour accéder aux données relatives à ce produit tout au long du message.

## Considérations

- Les utilisateurs ne sont abonnés que pour 90 jours. Si l'article n'est pas de nouveau en stock dans les 90 jours, l'utilisateur est désabonné.
- Lorsque vous utilisez la règle de notification **Notifier tous les utilisateurs abonnés**, Braze notifie 100 000 utilisateurs en 10 minutes.
- Braze traite au maximum 10 mises à jour de produits en une minute. Cela signifie que si vous mettez à jour 11 produits en une minute, seuls les 10 premiers produits peuvent déclencher une notification de retour en stock.

[1]: {% image_buster /assets/img/back_in_stock_settings.png %}
[2]: {% image_buster /assets/img/catalog_settings_drawer.png %}
