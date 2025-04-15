---
nav_title: Notifications de baisse de prix
article_title: Notifications de baisse de prix
page_order: 3
alias: "/price_drop_notifications/"
description: "Cet article de référence décrit comment créer des notifications de baisse de prix dans les catalogues de Braze."
---

# Notifications de baisse de prix

> Utilisez une combinaison de notifications de baisse de prix par le biais des catalogues de Braze et d'un Canvas pour informer les clients de la baisse de prix d'un article. Chaque fois qu'un client effectue un événement personnalisé sélectionné, il peut être automatiquement abonné pour être informé lorsque le prix de l'article est réduit.<br><br>Cette page explique comment fonctionnent les notifications de baisse de prix et comment vous pouvez les configurer et les utiliser.

Lorsqu'un utilisateur déclenche un événement personnalisé pour un produit, nous l'abonnons automatiquement pour qu'il reçoive des notifications de baisse de prix pour ce produit. Lorsque le prix du produit correspond à votre règle d'inventaire (par exemple, une baisse supérieure à 50 %), tous les abonnés pourront recevoir des notifications par le biais d'une campagne ou d'un canvas. Cependant, seuls les utilisateurs ayant opté pour les notifications recevront des notifications. 

## Comment fonctionnent les notifications de baisse de prix ?

Vous définirez un événement personnalisé à utiliser comme événement d'abonnement, tel que l'événement `product_clicked`. Cet événement doit contenir une propriété de l'ID de l'article (ID des articles du catalogue). Nous vous suggérons d'inclure un nom de catalogue, mais ce n'est pas obligatoire. Vous indiquerez également le nom d'un champ de prix, qui doit être de type numérique. 

Lorsqu'un événement personnalisé sélectionné est exécuté par un utilisateur et que sa propriété `type` comprend `price_drop`, il peut être utilisé pour créer un abonnement avec baisse de prix pour un utilisateur et un article de catalogue pour lequel il s'est produit. Vous pouvez également utiliser ce tableau `type` pour définir les notifications de baisse de prix et de retour en stock dans le même événement.

Lorsqu'un article subit un changement de prix conforme à votre règle de prix, nous recherchons tous les utilisateurs abonnés à cet article (les utilisateurs qui ont effectué l'événement d'abonnement) et envoyons un événement personnalisé Braze que vous pouvez utiliser pour déclencher une campagne ou un Canvas.

Les propriétés d'événement sont envoyées en même temps que l'utilisateur, ce qui vous permet d'intégrer les détails du produit dans la campagne ou le canvas qui effectue l’envoi !

## Mise en place de notifications de baisse de prix

Suivez ces étapes pour configurer les notifications de baisse de prix dans un catalogue spécifique.

1. Accédez à votre catalogue et sélectionnez l'onglet **Paramètres.** <br>
2. Basculer vers la **baisse des prix**.<br>
3. Si les paramètres du catalogue global n'ont pas été configurés, vous serez invité à définir les événements personnalisés et les propriétés qui seront utilisés pour déclencher les notifications :
    <br> ![Tiroir des paramètres du catalogue.][2]{: style="max-width:70%;"}
    - **Catalogue de secours :** Le catalogue utilisé pour l'abonnement s'il n'y a pas de propriété `catalog_name` dans l'événement personnalisé.
    - **Événement personnalisé pour s'abonner :** L'événement personnalisé de Braze utilisé pour abonner un utilisateur aux notifications du catalogue. Lorsque cet événement se produit, l'utilisateur qui l'a effectué est abonné.
    - **Événement personnalisé pour la désinscription :** L'événement personnalisé de Braze utilisé pour désinscrire un utilisateur des notifications. Cet événement est facultatif. Si l'utilisateur n'effectue pas cet événement, il sera désabonné au bout de 90 jours ou lorsque l'événement de baisse de prix se déclenchera, selon ce qui se produira en premier.
    - **Propriété d'événement de l’ID du produit :** La propriété de l'événement personnalisé ci-dessus utilisée pour déterminer l'élément d'un abonnement ou d'un désabonnement. Cette propriété de l'événement personnalisé doit contenir un ID d'article existant dans un catalogue. L'événement personnalisé doit contenir une propriété `catalog_name` pour spécifier le catalogue dans lequel se trouve cet article.
   
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
                    "type": ["price_drop", "back_in_stock"]
                }
            }
        ]
    }
    ```

{: start="4"}
4\. Sélectionnez **Enregistrer** et continuez vers la page **Paramètres** du catalogue.
5\. Définissez votre règle de notification. Deux options existent :
    - **Notifier tous les utilisateurs abonnés** notifie tous les clients en attente lorsque le prix de l'article baisse.
    - **Définir des limites de notification** notifie un nombre spécifié de clients par période de notification configurée. Braze informera le nombre de clients spécifié par incréments jusqu'à ce qu'il n'y ait plus de clients à informer ou jusqu'à ce que le prix de l'article augmente à nouveau. Votre taux de notification ne peut pas dépasser 10 000 utilisateurs par minute.
6\. Définissez le **champ Prix dans le catalogue**. Il s'agit du champ du catalogue qui sera utilisé pour déterminer le prix du produit. Il doit s'agir d'un type de nombre.<br>
7\. Définissez la **règle de baisse des prix**. Il s'agit de la logique utilisée pour déterminer si une notification doit être envoyée. Une baisse de prix peut être configurée en pourcentage de variation de prix ou en valeur de variation du champ de prix.<br>
8\. Sélectionnez **Enregistrer les paramètres**.

![Paramètres du catalogue qui montrent que la fonctionnalité de baisse des prix est activée. La règle de la baisse des prix est une modification de 3 % du prix d'origine.][1]{:style="max-width:60%;"}

{% alert important %}
Les règles de notification de ces paramètres ne remplacent pas les paramètres de notification de Canvas, tels que les heures calmes.
{% endalert %}

## Utiliser les notifications de baisse de prix dans Canvas

Après avoir configuré les notifications de baisse de prix dans un catalogue, suivez les étapes suivantes pour utiliser ces notifications dans un canvas.

1. Mettez en place un Canvas basé sur l'action.
2. Sélectionnez **Effectuer un événement de baisse de prix** comme déclencheur.
3. Sélectionnez le nom du catalogue contenant les notifications de baisse de prix.
4. Continuez à [configurer]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) votre Canvas comme vous le feriez.

Désormais, vos clients seront avertis lorsque le prix d'un article baissera.

### Utilisation de Liquid

Pour obtenir des tags détaillés sur le produit du catalogue dont le prix a baissé, vous pouvez utiliser l'étiquette Liquid `canvas_entry_properties` pour accéder à l’`item_id`. 

L'utilisation de {%raw%}``{{canvas_entry_properties.${catalog_update}.item_id}}``{%endraw%} renvoie l'ID du produit dont le prix a baissé. {%raw%}``{{canvas_entry_properties.${catalog_update}.previous_value}}``{%endraw%} renvoie la valeur du prix du produit avant la mise à jour, et {%raw%}``{{canvas_entry_properties.${catalog_update}.new_value}}``{%endraw%} renvoie la nouvelle valeur du prix après la mise à jour. 

Utilisez cette étiquette Liquid {%raw%}``{% catalog_items <name_of_your_catalog> {{canvas_entry_properties.${catalog_update}.item_id}} %}}``{%endraw%} en tête de votre message, puis utilisez {%raw%}`{{items[0].<field_name>}}`{%endraw%} pour accéder aux données relatives à ce produit tout au long du message.

## Considérations

- Les utilisateurs sont abonnés pour 90 jours. Si le prix d'un produit ne baisse pas dans les 90 jours, l'utilisateur est radié de l'abonnement.
- Lorsque vous utilisez la règle de notification **Notifier tous les utilisateurs abonnés**, Braze notifie 100 000 utilisateurs en 10 minutes.
- Braze traitera jusqu'à 10 mises à jour de produits par minute. Cela signifie que si vous mettez à jour 11 produits en une minute, seuls les 10 premiers produits peuvent déclencher une notification de baisse de prix.

[1]: {% image_buster /assets/img/price_drop_notifications.png %}
[2]: {% image_buster /assets/img/catalog_settings_drawer.png %}
