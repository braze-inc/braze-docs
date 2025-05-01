---
nav_title: aperçu de Shopify
article_title: "aperçu de Shopify"
description: "Cet article de référence décrit le partenariat entre Braze et Shopify, une entreprise de commerce mondiale qui vous permet de connecter de façon fluide leur boutique Shopify à Braze pour transmettre certains webhooks Shopify dans Braze. Exploitez les stratégies cross-canal de Braze et Canvas pour inciter les clients à finaliser leurs achats ou à recibler les utilisateurs en fonction de leurs achats précédents."
page_type: partner
search_tag: Partner
alias: /shopify_overview_legacy/
page_order: 0
---

# aperçu de Shopify

> [Shopify](https://www.shopify.com/) est une entreprise mondiale de commerce de premier plan offrant des outils fiables pour démarrer, développer, commercialiser et gérer une entreprise de vente au détail de toute taille. Shopify améliore le commerce pour tout le monde avec une plateforme et des services conçus pour la fiabilité tout en offrant une meilleure expérience d'achat aux consommateurs.

L'intégration de Shopify et Braze vous permet de connecter votre boutique Shopify pour transmettre de façon fluide vos données Shopify dans Braze. Vous pouvez tirer parti des stratégies cross-canal et de canvas dans Braze pour engager de nouveaux prospects, envoyer des messages à de nouveaux clients ou recibler vos utilisateurs avec des envois de messages de panier abandonné pour les inciter à finaliser leurs achats.


{% alert important %}
 <br><br> <br><br>  <br><br>    <br><br> 
{% endalert %}

## Fonctionnalités prises en charge

- Suivez le comportement des utilisateurs sur le site et les utilisateurs anonymes via le SDK Web de Braze
- Aidez à synchroniser et à rapprocher les clients Shopify dans Braze via le SDK Web Braze
- Synchroniser les données des clients Shopify
- Collectez les états d'abonnement des utilisateurs abonnés aux e-mails et SMS de Shopify
- Complétez les données d'achat historiques de Shopify 
- Synchronisation du catalogue Shopify 
- Utilisez les messages intégrés à l'application comme canal 

## Cas d'utilisation pris en charge 

- Campagnes de parcours d'achat et parcours utilisateur canvas, y compris : 
  - Abandon de navigation 
  - Panier abandonné 
  - Commande abandonnée 
- Campagnes post-achat et parcours utilisateur canvas, y compris :
  - Confirmations de commande 
  - Mises à jour de l'exécution 
  - Annulations de commande 
  - Remboursements de commande
- Recommandations de produit
- Vente croisée et ventes incitatives
- [De retour en stock]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_catalogs/back_in_stock/)

## Exigences

| Exigence | Descriptif |
| --- | --- |
| Boutique Shopify | Vous avez une boutique [Shopify](https://www.shopify.com/) active.<br><br>Vous pouvez connecter une boutique Shopify par espace de travail. Si vous souhaitez connecter plusieurs magasins à un seul espace de travail, contactez votre gestionnaire de la satisfaction client pour rejoindre la version bêta de Shopify Multiple Stores. |
| Autorisations des utilisateurs Shopify | Vous avez l'une des autorisations suivantes pour votre boutique Shopify :{::nomarkdown}<ul><li>Propriétaire du magasin</li><li>Personnel</li><li>Membre avec tous les paramètres généraux et de la boutique en ligne, ainsi que ces autorisations d'administrateur supplémentaires :<ul><li>Commandes</li><li>Voir (situé sous <b>Produits</b>)</li><li>Clients</li><li>gérer les paramètres</li><li>Voir les applications développées par le personnel et les collaborateurs</li><li>Gérer et installer des applications et des chaînes</li></ul></li></ul>{:/} |
| Implémentation du SDK Web Braze | Pour suivre le comportement sur site et les utilisateurs anonymes, vous devez implémenter le SDK Web Braze soit via notre intégration Shopify par défaut, soit manuellement. <br><br>Pour plus d'informations sur vos options de mise en œuvre, consultez [Mise en œuvre du SDK Web sur votre site Shopify]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/). |
| Segmentation des propriétés d'événement activée | Pour confirmer que vous pouvez segmenter les propriétés des événements Shopify, travaillez avec votre gestionnaire de la satisfaction client ou [Braze Support]({{site.baseurl}}/braze_support/) pour confirmer que la segmentation des propriétés des événements est activée pour votre tableau de bord de Braze. |
{: .reset-td-br-1 .reset-td-br-2 }

## Règlement général sur la protection des données (RGPD)

Concernant les données personnelles soumises aux services de Braze par ou au nom de ses clients, Braze est le processeur de données, et nos clients sont les contrôleurs de données. En conséquence, Braze traite ces données personnelles uniquement sur instruction de nos clients et, le cas échéant, informe nos clients des requêtes des personnes concernées. En tant que responsables du traitement des données, nos clients répondent directement aux requêtes des personnes concernées. Dans le cadre de l'intégration Shopify de la plateforme Braze, Braze reçoit automatiquement les [webhooks RGPD de Shopify](https://shopify.dev/tutorials/add-gdpr-webhooks-to-your-app). Cependant, les clients de Braze sont en fin de compte responsables de répondre aux requêtes des personnes concernées par les données de leurs clients Shopify en utilisant les [SDKs de Braze]({{site.baseurl}}/developer_guide/home/) ou les [APIs REST]({{site.baseurl}}/api/endpoints/user_data/#user-track-endpoint) conformément à nos politiques de conformité [RGPD]({{site.baseurl}}/dp-technical-assistance/).
