---
nav_title: Notifications de baisse de prix
article_title: Notifications de baisse de prix
page_order: 3
alias: "/price_drop_notifications/"
description: "Cet article de référence décrit comment créer des notifications de baisse de prix dans les catalogues de Braze."
---

# Notifications de baisse de prix

> Cette page explique le fonctionnement des notifications de baisse de prix, ainsi que leur configuration et leur utilisation. En combinant les notifications de baisse de prix via les catalogues de Braze et un Canvas, vous pouvez avertir vos clients lorsque le prix d'un article a baissé.

## Fonctionnement

Lorsqu'un utilisateur déclenche un événement personnalisé pour un article, nous l'abonnons automatiquement aux notifications de baisse de prix pour cet article. Lorsque le prix de l'article correspond à votre règle d'inventaire (par exemple, une baisse supérieure à 50 %), tous les abonnés deviennent éligibles aux notifications via une campagne ou un Canvas. Cependant, seuls les utilisateurs ayant opté pour les notifications les recevront effectivement. 

## Définition d'un événement personnalisé pour les notifications de baisse de prix

Vous devez configurer un événement personnalisé à utiliser comme événement d'abonnement, par exemple un événement `product_clicked`. Cet événement doit contenir une propriété correspondant à l'ID de l'article (ID des articles du catalogue). Nous vous recommandons d'inclure un nom de catalogue, mais ce n'est pas obligatoire. Vous devrez également indiquer le nom d'un champ de prix, qui doit être de type de données numérique. 

Vous pouvez créer un abonnement de baisse de prix pour un utilisateur et un article de catalogue dans les cas suivants :

- Un événement personnalisé sélectionné est réalisé par un utilisateur.
- L'événement personnalisé possède une propriété `type` qui inclut `price_drop` (`type` doit être un tableau).

Pour configurer les notifications de baisse de prix et de retour en stock dans le même événement, vous pouvez utiliser la propriété `type`, qui doit être un tableau. Lorsqu'un article subit un changement de prix conforme à votre règle de prix, nous recherchons tous les utilisateurs abonnés à cet article (ceux qui ont effectué l'événement d'abonnement) et envoyons un événement personnalisé Braze que vous pouvez utiliser pour déclencher une campagne ou un Canvas. 

Les propriétés d'événement sont envoyées avec les données de l'utilisateur, ce qui vous permet d'intégrer les détails de l'article dans la campagne ou le Canvas qui envoie le message.

## Mise en place des notifications de baisse de prix

Suivez ces étapes pour configurer les notifications de baisse de prix dans un catalogue spécifique.

1. Accédez à votre catalogue et sélectionnez l'onglet **Paramètres**.
2. Activez le basculeur **Baisse de prix**.
3. Si les paramètres globaux du catalogue n'ont pas été configurés, vous serez invité à définir les événements personnalisés et les propriétés qui seront utilisés pour déclencher les notifications. <br><br> ![Tiroir des paramètres du catalogue.]({% image_buster /assets/img/catalog_settings_drawer.png %}){: style="max-width:70%;"}

| Champ | Description |
| --- | --- |
| **Catalogue de secours** | Le catalogue utilisé pour l'abonnement s'il n'y a pas de propriété `catalog_name` dans l'événement personnalisé. |
| **Événement personnalisé pour s'abonner** | L'événement personnalisé utilisé pour abonner un utilisateur aux notifications du catalogue. Lorsque cet événement se produit, l'utilisateur qui l'a effectué est abonné. |
| **Événement personnalisé pour se désabonner** | L'événement personnalisé utilisé pour désabonner un utilisateur des notifications. Cet événement est facultatif. Si l'utilisateur n'effectue pas cet événement, il sera désabonné au bout de 90 jours ou lorsque l'événement de baisse de prix se déclenchera, selon ce qui se produit en premier. |
| **Propriété d'événement de l'ID d'article** | La propriété de l'événement personnalisé ci-dessus utilisée pour déterminer l'article concerné par un abonnement ou un désabonnement. Cette propriété de l'événement personnalisé doit contenir un ID d'article existant dans un catalogue. L'événement personnalisé doit contenir une propriété `catalog_name` pour spécifier dans quel catalogue se trouve cet article. |
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
4. Sélectionnez **Enregistrer** et passez à la section suivante pour configurer les règles de notification.

### Mise en place des règles de notification

1. Accédez à la page **Paramètres** de votre catalogue. 
2. Pour les **Règles de notification**, sélectionnez l'une des options suivantes :<br>

    - **Notifier tous les utilisateurs abonnés :** Informez tous les clients en attente lorsque le prix de l'article baisse.
    - **Fixer des limites de notification :** Notifiez un nombre déterminé de clients selon la période de notification que vous avez configurée. Braze informera le nombre de clients spécifié par incréments jusqu'à ce qu'il n'y ait plus de clients à notifier ou jusqu'à ce que le prix de l'article remonte. Votre taux de notification ne peut pas dépasser 10 000 utilisateurs par minute.<br>

2. Définissez le **Champ Prix dans le catalogue**. Il s'agit du champ du catalogue qui sera utilisé pour déterminer le prix de l'article. Il doit être de type numérique.
3. Définissez la **Règle de baisse des prix**. Il s'agit de la logique utilisée pour déterminer si une notification doit être envoyée. Une baisse de prix peut être configurée en pourcentage de variation de prix ou en fonction de la variation de la valeur du champ de prix.
4. Sélectionnez **Enregistrer les paramètres**.

![Paramètres du catalogue montrant que la fonctionnalité de baisse des prix est activée. La règle de baisse des prix consiste en une modification de trois pour cent du prix initial.]({% image_buster /assets/img/price_drop_notifications.png %})

{% alert important %}
Les règles de notification de ces paramètres ne remplacent pas les paramètres de notification du Canvas, tels que les heures calmes.
{% endalert %}

## Utiliser les notifications de baisse de prix dans un Canvas

Après avoir configuré les notifications de baisse de prix dans un catalogue, suivez les étapes ci-dessous pour les utiliser dans un Canvas.

1. Mettez en place un Canvas basé sur une action.
2. Sélectionnez **Effectuer un événement de baisse de prix** comme déclencheur.
3. Sélectionnez le nom du catalogue contenant les notifications de baisse de prix.
4. Continuez à [configurer]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) votre Canvas comme vous le feriez habituellement.

Vos clients seront désormais avertis lorsque le prix d'un article baisse.

### Utilisation de Liquid

Pour intégrer les détails de l'article du catalogue dont le prix a baissé, vous pouvez utiliser l'étiquette Liquid `context` pour accéder à l'`item_id`. 

L'utilisation de {%raw%}``{{context.${catalog_update}.item_id}}``{%endraw%} renvoie l'ID de l'article dont le prix a baissé. {%raw%}``{{context.${catalog_update}.previous_value}}``{%endraw%} renvoie la valeur du prix de l'article avant la mise à jour, et {%raw%}``{{context.${catalog_update}.new_value}}``{%endraw%} renvoie la nouvelle valeur du prix après la mise à jour. 

Utilisez l'étiquette Liquid {%raw%}``{% catalog_items <name_of_your_catalog> {{context.${catalog_update}.item_id}} %}``{%endraw%} en haut de votre message, puis utilisez {%raw%}`{{items[0].<field_name>}}`{%endraw%} pour accéder aux données de cet article dans l'ensemble du message.

{% multi_lang_include alerts/important_alerts.md alert='context variable' %}

{% multi_lang_include alerts/tip_alerts.md alert='catalog data images' %}

## Considérations

- Les utilisateurs sont abonnés pour une durée de 90 jours. Si le prix d'un article ne baisse pas dans les 90 jours, l'utilisateur est retiré de l'abonnement.
- Lorsque vous utilisez la règle de notification **Notifier tous les utilisateurs abonnés**, Braze notifie 100 000 utilisateurs en 10 minutes.
- Braze prend en charge jusqu'à 50 000 articles mis à jour par jour pouvant déclencher des notifications de baisse de prix. Vous pouvez avoir jusqu'à 100 millions d'abonnements actifs à un moment donné, chaque abonnement représentant un profil utilisateur abonné au suivi d'un article du catalogue.