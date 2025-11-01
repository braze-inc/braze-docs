---
nav_title: Notifications de rupture de stock
article_title: Mise en place de notifications de rupture de stock
page_order: 2
description: "Découvrez comment mettre en place des notifications de rupture de stock à l'aide de votre catalogue et d'événements personnalisés, afin de pouvoir abonner automatiquement les clients à des notifications lorsqu'un article est de nouveau en stock."
---

# Notifications de rupture de stock

> Découvrez comment mettre en place des notifications de rupture de stock à l'aide de votre catalogue et d'événements personnalisés, afin de pouvoir abonner automatiquement les clients à des notifications lorsqu'un article est de nouveau en stock. N'oubliez pas que cela ne s'applique qu'aux utilisateurs qui ont déjà opté pour les notifications.

## Comment cela fonctionne-t-il ?

Vous pouvez définir un événement personnalisé à utiliser comme événement d'abonnement, tel qu'un événement `product_clicked`. Cet événement doit contenir une propriété de l'ID de l'article (ID des articles du catalogue). Nous vous suggérons d'inclure un nom de catalogue, mais ce n'est pas obligatoire. Vous fournirez également le nom d'un champ de quantité d'inventaire, qui doit être un type de données numériques. 

Notez que le stock d'un article de catalogue doit être à zéro pour qu'un utilisateur puisse s'y abonner avec succès. Lorsqu'un article a une quantité en stock supérieure à zéro, Braze recherche tous les utilisateurs abonnés à cet article et envoie un événement personnalisé que vous pouvez utiliser pour déclencher une campagne ou un Canvas.

Les propriétés de l'événement sont envoyées en même temps que l'utilisateur, ce qui vous permet d'intégrer les détails de l'élément dans la campagne ou le canvas qui l'envoie.

## Mise en place de notifications de rupture de stock

Suivez ces étapes pour configurer les notifications de rupture de stock dans un catalogue spécifique.

1. Accédez à votre catalogue et sélectionnez l'onglet **Paramètres**.
2. Basculer sur l'option " **En stock"**.
3. Si les paramètres globaux de retour en stock n'ont pas été configurés, vous serez invité à définir les événements personnalisés et les propriétés qui seront utilisés pour déclencher les notifications de retour en stock :
    <br> \![Tiroir des paramètres du catalogue.]({% image_buster /assets/img/catalog_settings_drawer.png %}){: style="max-width:70%;"}
    - **Catalogue de secours** Il s'agit du catalogue qui sera utilisé pour l'abonnement en rupture de stock, si aucune propriété `catalog_name` n'est présente dans l'événement personnalisé.
    - **Custom event for subscriptions** est l'événement personnalisé de Braze qui sera utilisé pour abonner un utilisateur aux notifications de rupture de stock. Lorsque cet événement se produit, l'utilisateur qui l'a réalisé sera abonné.
    - **Custom event for unsubscribing** est l'événement personnalisé de Braze qui sera utilisé pour désinscrire un utilisateur des notifications de retour en stock. Cet événement est facultatif. Si l'utilisateur n'effectue pas cet événement, il sera désabonné au bout de 90 jours ou lorsque l'événement de rupture de stock se déclenchera, selon ce qui se produira en premier.
    - La **propriété de l'événement ID de l'article** est la propriété de l'événement personnalisé ci-dessus qui sera utilisée pour déterminer l'article pour un abonnement ou un désabonnement en rupture de stock. Cette propriété de l'événement personnalisé doit contenir un ID d'article (`id`) présent dans un catalogue. L'ID de l'article doit être envoyé sous forme de chaîne de caractères afin qu'il corresponde au type de données `id` stocké dans le catalogue cible. L'événement personnalisé doit également contenir une propriété `catalog_name`, afin de spécifier le catalogue dans lequel se trouve cet article.
    
    - Un exemple d'événement personnalisé ressemblerait à ce qui suit
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
Les déclencheurs de rupture de stock et de baisse de prix utilisent le même événement pour abonner l'utilisateur à la notification. Vous pouvez donc utiliser la propriété `type` pour définir les notifications de rupture de stock et de baisse de prix dans le même événement. Notez que la propriété `type` doit être un tableau.
{% endalert %}

{: start="4"}
4\. Sélectionnez **Enregistrer** et continuez vers la page **Paramètres** du catalogue.
5\. Définissez votre règle de notification. Deux options s'offrent à vous :
    - **Notifier tous les utilisateurs abonnés** informe tous les clients en attente lorsque l'article est de nouveau en stock.
    - **Définir des limites de notification** notifie un nombre spécifié de clients par période de notification configurée. Braze informera le nombre de clients spécifié par incréments jusqu'à ce qu'il n'y ait plus de clients à informer ou jusqu'à ce que l'article soit en rupture de stock. Votre taux de notification ne peut pas dépasser 10 000 utilisateurs par minute.
6\. Définissez le **champ Inventaire dans le catalogue**. Ce champ du catalogue sera utilisé pour déterminer si l'article est en rupture de stock. Le champ doit être de type numérique.
7\. Sélectionnez **Enregistrer les paramètres**.

Les paramètres du catalogue qui montrent que la fonctionnalité de rupture de stock est activée. Les règles de notification prévoient d'avertir un millier d'utilisateurs toutes les dix minutes.]({% image_buster /assets/img/back_in_stock_settings.png %})

{% alert important %}
Les règles de notification de ces paramètres ne remplacent pas les paramètres de notification de Canvas, tels que les heures calmes.
{% endalert %}

## Utiliser les notifications de rupture de stock dans un canvas

Après avoir configuré la fonctionnalité de rupture de stock dans un catalogue, suivez les étapes suivantes pour l'utiliser avec Canvas.

1. Mettez en place un Canvas basé sur l'action.
2. Sélectionnez **Retour en stock** comme déclencheur.
3. Sélectionnez le nom du catalogue contenant les notifications de rupture de stock.
4. Continuez à [configurer]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) votre Canvas comme vous le feriez.

Désormais, vos clients peuvent être avertis lorsqu'un article est à nouveau en stock.

### Utilisation du liquide

Pour obtenir des tags détaillés sur l'article du catalogue qui est de nouveau en stock, vous pouvez utiliser l'étiquette Liquid `canvas_entry_properties` pour accéder à la page `item_id`. 

L'utilisation de {%raw%}``{{canvas_entry_properties.${catalog_update}.item_id}}``{%endraw%} renvoie l'ID de l'article qui est revenu en stock. {%raw%}``{{canvas_entry_properties.${catalog_update}.previous_value}}``{%endraw%} renvoie la valeur d'inventaire de l'article avant la mise à jour, et {%raw%}``{{canvas_entry_properties.${catalog_update}.new_value}}``{%endraw%} renvoie la nouvelle valeur d'inventaire après la mise à jour.

Utilisez cette étiquette Liquid {%raw%}``{% catalog_items <name_of_your_catalog> {{canvas_entry_properties.${catalog_update}.item_id}} %}``{%endraw%} en tête de votre message, puis utilisez {%raw%}``{{ items[0].<field_name> }}``{%endraw%} pour accéder aux données relatives à cet élément tout au long du message.

## Considérations

- Les utilisateurs ne sont abonnés que pour 90 jours. Si l'article n'est pas de nouveau en stock dans les 90 jours, l'utilisateur est désabonné.
- Lorsque vous utilisez la règle de notification **Notifier tous les utilisateurs abonnés**, Braze notifie 100 000 utilisateurs en 10 minutes.
- Braze traitera au maximum 10 mises à jour d'éléments en une minute. Si vous mettez à jour 11 articles en une minute, seuls les 10 premiers peuvent déclencher une notification de rupture de stock.

