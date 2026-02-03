---
nav_title: Swym
article_title: Swym
description: "Cet article de référence présente le partenariat entre Braze et Swym, qui permet aux acheteurs d'enregistrer des produits et de poursuivre leur parcours de façon fluide/sans heurts sur les sites web, les applications mobiles et les magasins de détail."
alias: /partners/swym/
page_type: partner
search_tag: Partner
---

# Swym

> [Swym](https://getswym.com/) aide les marques d'e-commerce à capturer l'intention d'achat avec des listes de souhaits, enregistrer pour plus tard, registre de cadeaux, et des alertes de rupture de stock. Grâce à des données riches et basées sur les autorisations, vous pouvez élaborer des campagnes hyperciblées et proposer des expériences d'achat personnalisées qui stimulent l'engagement, augmentent les conversions et renforcent la fidélisation.

*Cette intégration est maintenue par Swym.*

## À propos de l'intégration

L'intégration de Swym et Braze vous permet de proposer des campagnes marketing personnalisées et événementielles qui convertissent l'intention des acheteurs en ventes. Utilisez l'intégration pour que les acheteurs puissent reprendre là où ils se sont arrêtés, collaborer avec d'autres personnes tout au long de leur parcours d'achat et recevoir des campagnes de reciblage performantes.

## Conditions préalables

Avant de commencer, vous avez besoin des éléments suivants :

| Prérequis          | Description                                                                                                                                |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Swym  | Swym Wishlist Plus, Back in Stock apps, ou les deux doivent être installés sur votre plateforme eCommerce (Shopify ou BigCommerce), et vous devez être sur le plan Enterprise.       |
| Une clé de l'API REST de Braze  | Une clé API REST de Braze avec des autorisations `users.track`. <br><br> Celle-ci peut être créée dans le tableau de bord de Braze à partir de **Paramètres** > **Clés API**. |
| Un endpoint REST Braze | [L'URL de votre endpoint REST.]({{site.baseurl}}/api/basics/#endpoints) Votre endpoint dépendra de l'URL de Braze pour votre instance.                                                 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Cas d’utilisation

En connectant les applications Wishlist Plus et Back in Stock Alerts de Swym avec Braze, vous pouvez envoyer automatiquement les événements liés à l'activité des acheteurs, tels que les ajouts à la liste de souhaits, les abonnements de retour en stock, les alertes de baisse de prix et les rappels, dans Braze en tant qu'événements personnalisés. Ces événements peuvent ensuite être utilisés pour déclencher des messages automatisés dans Braze, facilitant ainsi une communication opportune, pertinente et attrayante qui incite les acheteurs à revenir pour effectuer un achat.

## Intégration de Swym

### Étape 1 : Connectez votre application Swym à Braze

Actuellement, l'intégration Braze Currents avec Swym est une intégration gérée et n'est pas en libre-service. Pour commencer, contactez l'équipe d'assistance de Swym à [support@getswym.com](mailto:support@getswym.com) et fournissez les informations suivantes afin que Swym puisse mettre en place l'intégration en votre nom :

1. Générez une [clé API REST]({{site.baseurl}}/api/basics/#about-rest-api-keys) dans votre tableau de bord de Braze avec l'autorisation `users.track`.

![Générer une clé API dans Braze.]({% image_buster /assets/img/swym/braze-api-key.png %})

{% alert important %}
Pour protéger vos clés API, Swym vous recommande de partager les informations d'identification en toute sécurité à l'aide d'un outil de lien unique et autodestructeur (par exemple, [OneTimeSecret](https://onetimesecret.com/)).
{% endalert %}

{: start="2"}
2\. Braze gère plusieurs instances pour son tableau de bord et ses endpoints REST. Fournissez le [point de terminaison REST]({{site.baseurl}}/api/basics/#endpoints) pour l'instance que vous êtes en train de provisionner.

3. Une fois la clé API et l'URL de l'instance partagées avec l'équipe d'assistance de Swym, celle-ci mettra en place l'intégration pour vous et vous répondra avec une confirmation.

4. Une fois la configuration terminée, les événements personnalisés de Swym seront automatiquement enregistrés dans Braze. Vous pouvez consulter la liste des événements personnalisés enregistrés dans le tableau de bord de Braze en allant dans **Paramètres des données** > Événements personnalisés. 

5. Consultez les propriétés de chaque événement personnalisé Swym en sélectionnant **Gérer les propriétés de** l'événement personnalisé correspondant. Ces propriétés contiennent les valeurs des événements qui peuvent être utilisées pour personnaliser vos messages.

![Propriétés personnalisées dans Braze.]({% image_buster /assets/img/swym/braze-custom-properties.png %})

### Étape 2 : Abonnez-vous aux événements que vous souhaitez envoyer à Braze

Depuis votre appli Wishlist Plus, allez dans l'onglet **Marketing** et trouvez la section **Automatisations**. Ici, vous pouvez sélectionner les événements auxquels vous souhaitez vous abonner. 

![Événements à abonner.]({% image_buster /assets/img/swym/braze-event-subscription.png %})

#### Événements de l'application Swym Wishlist Plus

| Nom de l'événement | Lorsque cet événement est déclenché |  
|------------|------------------------------|  
| Partager la liste de souhaits | Lorsqu'un acheteur partage sa liste de souhaits avec quelqu'un d'autre |  
| Ajouter à la liste de souhaits | Lorsqu'un acheteur ajoute un article à sa liste de souhaits |  
| Rappel de la liste de souhaits | Rappel des articles figurant dans la liste de souhaits d'un acheteur|   
| Rappel d'enregistrement pour plus tard | Rappel concernant les articles enregistrés pour plus tard d'un acheteur |  
| Alerte de baisse de prix | Le produit d'une liste de souhaits est mis en vente |  
| Alerte de stock faible | Le produit d'une liste de souhaits est en rupture de stock |  
| Alerte de réapprovisionnement | Le produit d'une liste de souhaits est réapprovisionné |  
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Swym Back in Stock Alerts app events (en anglais)

| Nom de l’événement | Lorsque cet événement est déclenché |  
|------------|------------------------------|  
| Accusé de réception de réapprovisionnement | L'acheteur s'abonne pour être informé du retour en stock d'un produit. |  
| Alerte de réapprovisionnement | Le produit pour lequel un acheteur a demandé une alerte de rupture de stock est réapprovisionné. |  
| Rappel de réapprovisionnement | Alerte de suivi (généralement environ 24 heures après la première alerte de réapprovisionnement, configurable)|   
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Étape 3 : Créer une campagne ou un canvas de Braze

Pour automatiser la réception/distribution de messages personnalisés pour vos acheteurs, vous devez créer une campagne ou un Canvas distinct dans Braze pour chaque événement auquel vous êtes abonné. Chaque campagne ou Canvas doit être configuré pour se déclencher en fonction de l'événement spécifique et utiliser les propriétés d'événement correspondantes pour alimenter le contenu dynamique de vos messages. Pour obtenir des conseils étape par étape, vous pouvez consulter le site [Getting Started : Campagnes et toiles]({{site.baseurl}}/user_guide/getting_started/campaigns_canvases/).

![Un événement basé sur l'action.]({% image_buster /assets/img/swym/braze-canvas-setup.png %})

Pour plus de détails, reportez-vous au [centre d'aide de Swym](https://help.getswym.com/en/articles/12344153-braze-integration) ou contactez l'équipe d'assistance de Swym à l'adresse [support@getswym.com](mailto:support@getswym.com). 