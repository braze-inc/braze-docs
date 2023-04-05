---
nav_title: "Remplissage de l'historique de Shopify"
article_title: "Remplissage de l'historique de Shopify"
alias: "/shopify_historical_backfill/"
description: "Cet article de référence explique comment configurer le remplissage d’historique de Shopify, y compris les risques et les données prises en charge."
page_type: partner
search_tag: Partenaire
page_order: 4
---

# Remplissage de l'historique de Shopify 

La fonctionnalité de remplissage de l'historique de Shopify permet aux marques de synchroniser les données des clients et d’achats de manière automatisée et de manière harmonieuse, pour que vous puissiez commencer immédiatement à contacter votre segment le plus précieux, les acheteurs. Dans le cadre de ce remplissage, Braze importera tous les clients, commandes et événements d’achat des 90 jours avant la connexion de l’intégration Shopify. Notez que cette fonctionnalité est idéale pour les clients plus récents qui n’ont pas de messages actifs en cours d’exécution, compte tenu des implications expliquées dans la section suivante. Prenez en compte que cette fonctionnalité comptera dans votre utilisation de points de données.

## Risques

Cette fonctionnalité importera les données et événements historiques qui pourraient entraîner des conséquences inattendues telles que la réception par l’utilisateur de messages non pertinents et inopportuns de la part des campagnes et Canvas touchés. Les campagnes et les Canvas utilisant les événements déclencheurs suivants pourraient être affectés s’ils utilisaient des données de Shopify synchronisés par cette fonctionnalité :
- Modifier la valeur d’attribut personnalisé
- Effectuer un événement de conversion
- Effectuer un événement d’exception pour la campagne
- Mettre à jour le statut d’abonnement
- Mettre à jour le statut du groupe d’abonnement
- Ajouter une adresse e-mail
- Effectuer un achat*
- Effectuer un événement personnalisé*

{% alert important %}
Nous vous recommandons d’auditer vos campagnes et vos Canvas actifs actuellement pour d’éventuels messages pouvant déclencher les événements ci-dessus utilisant des données de votre remplissage de l'historique de Shopify. 

- Pour « Fait un achat » et « Effectue un événement personnalisé », vous pouvez mettre à jour la [durée de l’heure de départ]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/?redirected=true#step-4-assign-duration) vers n’importe quelle date et heure après la connexion à Braze de votre boutique Shopify. Tous les événements passés situés avant cette nouvelle heure de départ ne déclencheront aucun message. 
- Vous pouvez arrêter [temporairement]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/change_your_campaign_after_launch/#stopping-your-campaign) tous les autres événements ci-dessus avant d’activer le remplissage pour vous assurer qu’aucun message ne sera envoyé. 
{% endalert %}

## Paramétrer le remplissage de l'historique de Shopify

### Étape 1 : Démarrer le processus de remplissage de l'historique de Shopify

Sur la page partenaire de Shopify, sélectionnez **Start Data Backfill (Démarrer le remplissage des données)**. Pour les clients Shopify existants, vous devrez autoriser à nouveau l’accès pour que Braze recueille tous les événements de commande passés avant de démarrer le remplissage de données.

![][3]{: style="max-width:75%;"}

### Étape 2 : Activer le remplissage des données Shopify

Ensuite, l’assistant de configuration s’affichera et vous pourrez, facultativement, activer le remplissage de l'historique des données Shopify. Dans le cadre de ce remplissage, Braze ne synchronisera par défaut que les données Shopify suivantes des 90 derniers jours avant votre intégration Shopify :
- Événement de commande créée
- Événement d’achat Braze
- Données client

Pour voir quelles données client particulières sont remplies, vous pouvez vous rendre sur la section [Données clients prises en charge par Shopify](#supported-shopify-customer-data).

{% alert note %}
Cette fonctionnalité synchronisera uniquement les états d’abonnement aux e-mails et aux SMS pour les nouveaux utilisateurs créés pendant le remplissage. Elle ne synchronisera pas les états d’abonnement des utilisateurs existants dans Braze pour éviter de remplacer les statuts actuels de vos utilisateurs.<br><br>Si vous avez des commentaires sur le comportement actuel, envoyez-les via le portail du produit, répertorié dans le **tableau de bord** sous **Ressources** en tant que **Product Roadmap (Feuille de route du produit)**.
{% endalert %}

Une fois que vous appuyez sur **Next (Suivant)**, le remplissage s’activera et commencera à synchroniser les données passées. Notez que le remplissage d’historique ne peut se faire **qu’une fois**, vous ne pourrez donc plus exécuter une nouvelle fois cette importation une fois la synchronisation des données activées.

![][1]{: style="max-width:75%;"}

### Étape 3 : Remplissage en cours

Vous recevrez une notification du tableau de bord et votre statut passera sur « En cours » pour signaler que votre remplissage a démarré. Prenez en compte le fait que le temps nécessaire pour achever le remplissage dépendra du nombre de clients et de commandes que doit synchroniser Braze depuis Shopify. Pendant ce temps, vous pouvez quitter cette page et attendre une notification ou un e-mail du tableau de bord pour vous signaler que le remplissage est terminé.

![][2]{: style="max-width:75%;"}

### Étape 4 : Remplissage terminé
Vous recevrez une notification et un e-mail du tableau de bord une fois que le remplissage depuis Shopify est terminé. La page partenaire Shopify mettra également à jour le statut dans le Remplissage de l’historique vers « Terminé ».

## Données client Shopify prises en charge

### Attributs personnalisés Shopify

| Nom de l’attribut | Description |
| --- | --- |
| `shopify_order_count` | Cet attribut personnalisé correspond au nombre total de commandes passées par ce client dans Shopify. Il n’est disponible que pour les utilisateurs qui ont été remplis lors de ce processus. |
| `shopify_total_spent` | Cet attribut personnalisé correspond à la somme totale dépensée par ce client dans Shopify. Il n’est disponible que pour les utilisateurs qui ont été remplis lors de ce processus. |
| `shopify_tags` | Cet attribut correspond aux [balises client](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/using-tags#tag-types) définies par les administrateurs Shopify. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 }

### Attributs standard de Shopify
- E-mail
- Prénom
- Nom
- Téléphone
- Ville
- Pays

[1]: {% image_buster /assets/img/Shopify/backfill1.jpg %} 
[2]: {% image_buster /assets/img/Shopify/backfill2.png %} 
[3]: {% image_buster /assets/img/Shopify/backfill3.png %} 
