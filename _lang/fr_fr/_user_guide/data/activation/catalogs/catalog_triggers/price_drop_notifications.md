---
nav_title: Notifications de baisse de prix
article_title: Notifications de baisse de prix
page_order: 3
alias: "/price_drop_notifications/"
description: "Cet article de référence décrit comment créer des notifications de baisse de prix dans les catalogues de Braze."
---

# Notifications de baisse de prix

> Cette page explique comment fonctionnent les notifications de baisse de prix et comment vous pouvez les configurer et les utiliser. En combinant les notifications de baisse de prix via les catalogues de Braze et un Canvas, vous pouvez avertir les clients lorsque le prix d'un article a baissé.

## Comment cela fonctionne-t-il ?

Lorsqu'un utilisateur déclenche un événement personnalisé pour un article, nous l'abonnons automatiquement pour qu'il reçoive des notifications de baisse de prix pour cet article. Lorsque le prix de l'article répond à votre règle d'inventaire (telle qu'une baisse supérieure à 50 %), tous les abonnés pourront recevoir des notifications par le biais d'une campagne ou d'un canvas. Cependant, seuls les utilisateurs ayant opté pour les notifications recevront des notifications. 

## Définition d'un événement personnalisé pour les notifications de baisse de prix

Vous définirez un événement personnalisé à utiliser comme événement d'abonnement, tel que l'événement `product_clicked`. Cet événement doit contenir une propriété de l'ID de l'article (ID des articles du catalogue). Nous vous recommandons d'inclure un nom de catalogue, mais ce n'est pas obligatoire. Vous indiquerez également le nom d'un champ de prix, qui doit être un type de données de type numérique. 

Vous pouvez créer un abonnement à prix réduit pour un utilisateur et un article de catalogue dans les cas suivants :

- Un événement personnalisé sélectionné est réalisé par un utilisateur.
- L'événement personnalisé possède une propriété `type` qui comprend `price_drop` (`type` doit être un tableau).

Pour définir les notifications de baisse de prix et de retour en stock dans le même événement, vous pouvez utiliser la propriété `type`, qui doit être un tableau. Lorsqu'un article subit un changement de prix conforme à votre règle de prix, nous recherchons tous les utilisateurs abonnés à cet article (les utilisateurs qui ont effectué l'événement d'abonnement) et envoyons un événement personnalisé Braze que vous pouvez utiliser pour déclencher une campagne ou un Canvas. 

Les propriétés de l'événement sont envoyées en même temps que l'utilisateur, ce qui vous permet d'intégrer les détails de l'élément dans la campagne ou le canvas qui l'envoie.

## Mise en place de notifications de baisse de prix

Suivez ces étapes pour configurer les notifications de baisse de prix dans un catalogue spécifique.

1. Accédez à votre catalogue et sélectionnez l'onglet **Paramètres**.
2. Basculer vers la **baisse des prix**.
3. Si les paramètres du catalogue global n'ont pas été configurés, vous serez invité à définir les événements personnalisés et les propriétés qui seront utilisés pour déclencher les notifications. <br><br> \![Tiroir des paramètres du catalogue.]({% image_buster /assets/img/catalog_settings_drawer.png %}){: style="max-width:70%;"}

| Champ d'application | Description |
| --- | --- |
| **Catalogue de repli** | Le catalogue utilisé pour l'abonnement s'il n'y a pas de propriété `catalog_name` dans l'événement personnalisé. |
| **Événement personnalisé pour s'abonner** | L'événement personnalisé utilisé pour abonner un utilisateur aux notifications du catalogue. Lorsque cet événement se produit, l'utilisateur qui l'a réalisé sera abonné. |
| **Événement personnalisé pour la désinscription** | L'événement personnalisé utilisé pour désinscrire un utilisateur des notifications. Cet événement est facultatif. Si l'utilisateur n'effectue pas cet événement, il sera désabonné au bout de 90 jours ou lorsque l'événement de baisse de prix se déclenchera, selon ce qui se produira en premier. |
| **Propriété d'événement ID de l'article** | La propriété de l'événement personnalisé ci-dessus utilisée pour déterminer l'élément d'un abonnement ou d'un désabonnement. Cette propriété de l'événement personnalisé doit contenir un ID d'article existant dans un catalogue. L'événement personnalisé doit contenir une propriété `catalog_name` pour spécifier le catalogue dans lequel se trouve cet article. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Voici un exemple d'événement personnalisé :

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
4\. Sélectionnez **Enregistrer** et passez à la section suivante pour configurer les règles de notification.

### Mise en place de règles de notification

1. Accédez à la page **Paramètres** de votre catalogue. 
2. Pour les **règles de notification**, sélectionnez l'une des options suivantes :<br>

    - **Notifier tous les utilisateurs abonnés :** Informez tous les clients en attente lorsque le prix de l'article baisse.
    - **Fixer des limites de notification :** Notifiez un nombre déterminé de clients selon la période de notification que vous avez configurée. Braze informera le nombre de clients spécifié par incréments jusqu'à ce qu'il n'y ait plus de clients à informer ou jusqu'à ce que le prix de l'article augmente à nouveau. Votre taux de notification ne peut pas dépasser 10 000 utilisateurs par minute.<br>

2. Définissez le **champ Prix dans le catalogue**. Il s'agit du champ du catalogue qui sera utilisé pour déterminer le prix de l'article. Il doit s'agir d'un type de nombre.
3. Définissez la **règle de baisse des prix**. Il s'agit de la logique utilisée pour déterminer si une notification doit être envoyée. Une baisse de prix peut être configurée en pourcentage de variation de prix ou en fonction de la variation de la valeur du champ de prix.
4. Sélectionnez **Enregistrer les paramètres**.

Les paramètres du catalogue qui montrent que la fonctionnalité de baisse des prix est activée. La règle de la baisse des prix est une modification de 3 % du prix d'origine.]({% image_buster /assets/img/price_drop_notifications.png %})

{% alert important %}
Les règles de notification de ces paramètres ne remplacent pas les paramètres de notification de Canvas, tels que les heures calmes.
{% endalert %}

## Utiliser les notifications de baisse de prix dans un canvas

Après avoir configuré les notifications de baisse de prix dans un catalogue, suivez les étapes suivantes pour utiliser ces notifications pour un Canvas.

1. Mettez en place un Canvas basé sur l'action.
2. Sélectionnez **Perform Price Drop Event** comme déclencheur.
3. Sélectionnez le nom du catalogue contenant les notifications de baisse de prix.
4. Continuez à [configurer]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) votre Canvas comme vous le feriez.

Désormais, vos clients seront avertis lorsque le prix d'un article baissera.

### Utilisation du liquide

Pour obtenir des tags détaillés sur l'article du catalogue dont le prix a baissé, vous pouvez utiliser l'étiquette Liquid `canvas_entry_properties` pour accéder à la page `item_id`. 

L'utilisation de {%raw%}``{{canvas_entry_properties.${catalog_update}.item_id}}``{%endraw%} renvoie l'ID de l'article dont le prix a baissé. {%raw%}``{{canvas_entry_properties.${catalog_update}.previous_value}}``{%endraw%} renvoie la valeur du prix de l'article avant la mise à jour, et {%raw%}``{{canvas_entry_properties.${catalog_update}.new_value}}``{%endraw%} renvoie la nouvelle valeur du prix après la mise à jour. 

Utilisez cette étiquette Liquid {%raw%}``{% catalog_items <name_of_your_catalog> {{canvas_entry_properties.${catalog_update}.item_id}} %}}``{%endraw%} en tête de votre message, puis utilisez {%raw%}`{{items[0].<field_name>}}`{%endraw%} pour accéder aux données relatives à cet élément tout au long du message.

## Considérations

- Les utilisateurs sont abonnés pour 90 jours. Si le prix d'un article ne baisse pas dans les 90 jours, l'utilisateur est radié de l'abonnement.
- Lorsque vous utilisez la règle de notification **Notifier tous les utilisateurs abonnés**, Braze notifie 100 000 utilisateurs en 10 minutes.
- Braze traitera 10 demandes de mise à jour d'éléments de catalogue par minute. Les endpoints de mise à jour permettent de mettre à jour 50 articles par demande, ce qui permet de mettre à jour jusqu'à 500 articles par minute et de déclencher des notifications de rupture de stock.

