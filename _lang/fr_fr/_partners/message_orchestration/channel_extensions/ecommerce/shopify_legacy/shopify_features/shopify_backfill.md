---
nav_title: "Remplissage historique de Shopify"
article_title: "Remplissage historique de Shopify"
alias: "/shopify_historical_backfill_legacy/"
description: "Cet article de référence explique comment configurer le remplissage historique de Shopify, y compris les risques et les données prises en charge."
page_type: partner
search_tag: Partner
page_order: 1
---

# Remplissage historique de Shopify 

> La fonctionnalité de remplissage historique de Shopify permet aux marques de synchroniser automatiquement et de manière transparente les données des clients et des achats, afin que vous puissiez immédiatement commencer à interagir avec l'un de vos segments les plus précieux – les acheteurs. 

Dans le cadre de ce remplissage, Braze importera tous les événements de client, de commande et d'achat qui se sont déroulés au cours des 90 derniers jours qui précèdent la connexion de votre intégration Shopify. Notez que cette fonctionnalité est idéale pour les nouveaux clients qui n'ont pas de messages actifs en cours, compte tenu des implications expliquées dans la section suivante. Cette fonctionnalité comptera également pour votre utilisation des points de donnée.

## Risques

Cette fonctionnalité importera des données et des événements historiques qui pourraient entraîner des conséquences imprévues, telles que des utilisateurs recevant des messages non pertinents et intempestifs pour toutes les campagnes ou Canvases concernés. Les campagnes et les canevas utilisant les événements de déclencheur suivants pourraient être impactés s'ils utilisent l'une des données Shopify que cette fonctionnalité synchronise :
- Changer la valeur de l'attribut personnalisé
- Effectuer un événement de conversion
- Effectuer un événement d'exception pour une campagne
- Mettre à jour le statut de l'abonnement
- Mettre à jour le statut du groupe d'abonnement
- Ajouter une adresse e-mail
- Faire un achat*
- Effectuer événement personnalisé*

{% alert important %}
Nous vous recommandons d'auditer vos campagnes actives actuelles et vos Canvases pour les messages qui peuvent déclencher les événements ci-dessus en utilisant les données de notre remplissage historique Shopify. 

- Pour « Effectuer un achat » et « Effectuer un événement personnalisé », vous pouvez mettre à jour la [durée de début]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/#step-4-assign-duration) à toute date et heure après que votre boutique Shopify a été connectée dans Braze. Les événements passés avant cette nouvelle heure de début ne déclencheront aucun message. 
- Pour tous les autres événements ci-dessus, vous pouvez les [arrêter temporairement]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/change_your_campaign_after_launch/#stopping-your-campaign) avant d'activer le remplissage pour garantir qu'aucun message ne soit envoyé.
{% endalert %}

## Configuration de la récupération historique de Shopify

### Conditions préalables

Les événements suivants doivent être activés avant d'activer le remplissage ou leurs données ne seront pas importées :

- `shopify_created_order`
- Événement d'achat Braze 

Les événements ci-dessus peuvent être activés lors de la configuration de Shopify pendant [la sélection des événements]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify/#event-selection).

{% alert important %}
Vous pouvez activer la fonctionnalité de remplissage arrière une seule fois dans votre intégration.
{% endalert %}

### Étape 1 : Démarrez le processus de remplissage rétroactif de Shopify

Sur la page partenaire Shopify, sélectionnez **Démarrer le remplissage des données**. Pour les clients Shopify existants, vous devrez réautoriser l'accès pour que Braze puisse collecter tous les événements de commande passés avant de pouvoir commencer le remplissage des données.

![][3]{: style="max-width:75%;"}

### Étape 2 : Basculer sur le remplissage des données Shopify

Ensuite, le compositeur de configuration apparaîtra, et vous pouvez éventuellement activer le remplissage rétroactif des données historiques de Shopify. Dans le cadre de ce remplissage, Braze synchronisera par défaut uniquement les données Shopify suivantes pour les 90 derniers jours qui se sont écoulés avant votre intégration Shopify :
- Événement de création de commande
- Événement d'achat Braze
- Données client

Pour voir quelles données client spécifiques sont en cours de remplissage, vous pouvez visiter la section [Données clients Shopify prises en charge](#supported-shopify-customer-data).

{% alert note %}
Cette fonctionnalité ne synchronisera que les états d'abonnement par e-mail et SMS pour les nouveaux utilisateurs créés pendant le remplissage rétroactif. Cela ne synchronisera pas les états d'abonnement pour les utilisateurs existants dans Braze afin d'éviter d'écraser les statuts actuels de vos utilisateurs.<br><br>Si vous avez des commentaires sur le comportement actuel, soumettez-les via le portail du produit, répertorié dans le **tableau de bord** sous **Ressources** en tant que **Feuille de route du produit** (Si vous utilisez notre [navigation mise à jour]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/), sélectionnez **Communauté** > **Feuille de route du produit**).
{% endalert %}

Une fois que vous appuyez sur **Suivant**, le remplissage rétroactif s'activera et commencera à synchroniser les données passées. Notez que le remplissage historique ne peut être complété **qu'une seule fois**, vous ne pourrez donc pas exécuter cette importation à nouveau après la synchronisation des données.

![][1]{: style="max-width:75%;"}

### Étape 3 : Remplissage en cours

Vous recevrez une notification sur le tableau de bord, et votre état s'affichera comme "En cours" pour indiquer que le remplissage a commencé. Notez que le temps nécessaire au remplissage dépendra du nombre de clients et de commandes que Braze devra synchroniser depuis Shopify. Pendant ce temps, vous pouvez quitter cette page et attendre une notification de tableau de bord ou un e-mail pour vous informer lorsque le remplissage est terminé.

![][2]{: style="max-width:75%;"}

### Étape 4 : Remplissage terminé
Vous recevrez une notification sur le tableau de bord et un e-mail une fois le remplissage Shopify terminé. La page partenaire Shopify mettra également à jour l’état sous Remplissage historique sur "Terminé".

## Données client Shopify prises en charge

### Attributs personnalisés de Shopify

| Nom de l'attribut | Description |
| --- | --- |
| `shopify_order_count` | Cet attribut personnalisé correspond au total des commandes que ce client a complétées sur Shopify. Ceci est uniquement disponible pour les utilisateurs qui ont été réintégrés dans le cadre de ce processus. |
| `shopify_total_spent` | Cet attribut personnalisé correspond au montant total dépensé par ce client dans Shopify. Ceci est uniquement disponible pour les utilisateurs qui ont été réintégrés dans le cadre de ce processus. |
| `shopify_tags` | Cet attribut correspond aux [tags client](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/using-tags#tag-types) définis par les administrateurs Shopify. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 }

### Attributs standard Shopify
- e-mail
- Prénom
- Nom de famille
- Téléphone
- Ville
- Pays

[1]: {% image_buster /assets/img/Shopify/backfill1.jpg %}
[2]: {% image_buster /assets/img/Shopify/backfill2.png %}
[3]: {% image_buster /assets/img/Shopify/backfill3.png %} 
