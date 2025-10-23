---
nav_title: Connecter plusieurs magasins
article_title: Prise en charge de plusieurs boutiques Shopify
alias: /shopify_connecting_multiple_stores/
page_order: 5
description: "Cet article de référence explique comment connecter et configurer plusieurs boutiques Shopify à un seul espace de travail."
---

# Connecter plusieurs boutiques Shopify

> Connectez plusieurs domaines de boutiques Shopify à un espace de travail unique pour avoir une vue globale de vos clients sur tous les marchés. Créez et lancez des programmes d'automatisation et des parcours dans un espace de travail unique sans dupliquer les efforts dans les magasins régionaux.  

{% alert important %}
Cette fonctionnalité ne prend pas en charge Shopify Markets ou Markets Pro. Si vous souhaitez obtenir de l'aide pour ces produits, soumettez une [demande de produit]({{site.baseurl}}/user_guide/administrative/access_braze/portal/).
{% endalert %}

## Conditions

| Exigence | Description |
| ----------- | ----------- |
| Permettre l'accès à plusieurs magasins | Contactez votre gestionnaire de la satisfaction client pour activer la prise en charge de plusieurs magasins par Shopify. |
| Créer une boutique Shopify | Assurez-vous d'avoir déjà [configuré au moins une boutique Shopify avec Braze]({{site.baseurl}}/shopify_overview/). |
| Domaines uniques de vitrine Shopify pour chaque région. | La prise en charge de plusieurs magasins est destinée à être utilisée avec des domaines de magasin Shopify uniques pour différentes vitrines régionales. <br><br>Si vous souhaitez connecter plusieurs sous-marques à Braze, nous vous recommandons de créer des espaces de travail distincts pour chaque sous-marque. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Connexion d'un magasin supplémentaire
Après avoir installé l'appli Braze sur votre boutique Shopify et installé votre première boutique, sélectionnez **\+ Connecter une nouvelle boutique.**

![Le bouton "+ Connect New Store" sur la page d'intégration de Shopify.]({% image_buster /assets/img/Shopify/begin_setup_button.png %}){: style="max-width:80%;"}

Pour votre boutique régionale Shopify supplémentaire, sélectionnez **Commencer la configuration.**

![La section "Paramètres d'intégration" avec un bouton pour "Commencer la configuration".]({% image_buster /assets/img/Shopify/multiple_stores.png %}){: style="max-width:80%;"}

Comme pour votre première intégration de boutique Shopify, vous pouvez choisir entre une configuration standard ou personnalisée.

![La section "Enable the Braze SDKs" contient des options permettant d'implémenter le Braze Web SDK avec la configuration standard ou personnalisée.]({% image_buster /assets/img/Shopify/standard_or_custom.png %}){: style="max-width:80%;"}

Choisissez l'option qui correspond le mieux à vos besoins :

{% multi_lang_include shopify.md section='Integration Tabs' %}

Pour afficher l'intégration de chaque magasin et configurer les paramètres avancés, sélectionnez un magasin dans le menu déroulant.

!["Paramètres d'intégration" avec un menu déroulant pour sélectionner une boutique Shopify.]({% image_buster /assets/img/Shopify/store_dropdown_menu.png %}).

## Synchronisation des utilisateurs entre les magasins

### Alias Shopify

Lorsque vous connectez plusieurs boutiques, les utilisateurs Shopify synchronisés qui se sont connectés ou ont passé une commande recevront un nouvel alias au format : {% raw %}`shopify_customer_id_{{storename}}`{% endraw %}.

### Braze ID externe

Vous pouvez choisir parmi les options suivantes pour votre ID externe Braze :

|Option|Description|
|------|-----------|
|ID de client Shopify|Si vous utilisez l'ID client de Shopify comme ID externe de Braze, chaque magasin générera un ID client unique pour chaque utilisateur. Cela signifie que si un utilisateur interagit avec plusieurs magasins, il aura des profils distincts dans Braze.|
|E-mail, e-mail haché ou ID externe personnalisé|Si vous utilisez les types d'e-mail, d'e-mail haché ou d'ID externe personnalisé, les utilisateurs qui s'engagent auprès de plusieurs magasins verront leurs profils fusionnés en un seul profil consolidé lorsqu'ils se connecteront ou passeront une commande.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Champs fusionnés

Lorsqu'un profil utilisateur est synchronisé, les champs suivants sont fusionnés. Pour plus de détails sur le comportement en matière de fusion, reportez-vous à la section [Comportement en matière de fusion.]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge-behavior)

- Informations sur l’appareil
- Nombre total de sessions (combiné des deux profils)
- Données personnalisées sur les événements et les achats
- Propriétés d'événement personnalisées pour la segmentation (par exemple, "X fois en Y jours" où X ≤ 50 et Y ≤ 30).
- Nombre d'événements (combiné des deux profils)
- Dates du premier et du dernier événement (Braze sélectionne les dates les plus anciennes et les plus récentes)
- Données d'interaction de la campagne (champs de date les plus récents)
- Résumés des flux de travail (champs de date les plus récents)
- Historique des messages et de l'engagement
- Groupes d’abonnement

### Recueillir les abonnés (facultatif)

Vous pouvez choisir de collecter les abonnés directement via Braze (dans les paramètres de votre connecteur Shopify) ou via des alternatives API et SDK qui synchronisent les données depuis Shopify.

{% tabs local %}
{% tab Connecteur Shopify %}
Dans l'étape **Gérer les utilisateurs** des paramètres de votre connecteur Shopify, vous pouvez utiliser Braze pour collecter les abonnements par e-mail et SMS et les organiser dans un groupe d'abonnements dédié :

1. Créez un groupe d'abonnement unique pour chaque magasin que vous connectez. Cela vous permet de conserver des données précises sur la provenance des abonnés.
2. Activez la collecte d'abonnés par e-mail et par SMS.
{% endtab %}

{% tab API ou SDK de Braze %}
Vous pouvez également synchroniser les informations d'abonnement au marketing par e-mail et par SMS directement depuis Shopify à l'aide de l'API ou des SDK de Braze.

|Option|Ressources|
|------|---------|
|API |\- Les [endpoints des groupes d'abonnement]({{site.baseurl}}/api/endpoints/subscription_groups/) pour remplacer directement ce qui est pris en charge par l'intégration.<br>- [`Users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#set-subscription-groups) pour définir les données du subscription groups ou l'[état de l'abonnement global à l'e-mail.]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-states)<br>\- Le [centre de préférences de Braze]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/overview/) pour des options d'abonnement marketing plus personnalisées|
|SDK |- [`NotificationSubscriptionTypes`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#notificationsubscriptiontypes)<br>- [`addToSubscriptionGroup`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup)<br>- [`removeFromSubscriptionGroup`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#removefromsubscriptiongroup)<br>- [`setEmailNotificationSubscriptionType`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemailnotificationsubscriptiontype)|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% endtab %}
{% endtabs %}

## Données de Shopify 

### Attributs synchronisés

Lorsque vous connectez plus d'un magasin, les attributs suivants seront synchronisés avec l'état le plus récent du profil Shopify :
- Prénom
- Nom
- E-mail
- Genre
- Date de naissance
- Pays
- Ville
- Dernière application utilisée
- Langue
- Fuseau horaire
- Tags Shopify
- Nombre de commandes Shopify
- Total dépensé Shopify

### Événements soutenus

#### Événements recommandés pour le commerce électronique 

Lorsque vous connectez plusieurs magasins, les événements entrants recommandés par eCommerce incluront une propriété d'événement source. Cette propriété identifie l'URL de la vitrine d'où provient l'événement, ce qui vous permet d'utiliser cette information pour la segmentation ou le déclenchement de cas d'utilisation spécifiques.

![Un Canvas basé sur une action avec un déclencheur pour entrer les utilisateurs qui effectuent l'événement personnalisé `ecommerce.order_placed`.]({% image_buster /assets/img/Shopify/ecommerce_order_placed.png %}){: style="max-width:80%;"}

Les événements recommandés eCommerce pris en charge dans le cadre de l'intégration de Shopify sont les suivants :

- `ecommerce.product_viewed`
- `ecommerce.cart_updated`
- `ecommerce.checkout_started`
- `ecommerce.order_placed`
- `ecommerce.order_cancelled`
- `ecommerce.order_refunded`

#### Événements personnalisés de Shopify 

Les événements personnalisés entrants de Shopify comprennent une propriété d'événement appelée `shopify_storefront`. Cette propriété indique l'URL de la vitrine d'où provient l'événement, ce qui vous permet de l'exploiter pour la segmentation ou le déclenchement de cas d'utilisation.

![Un Canvas basé sur une action avec un déclencheur pour entrer les utilisateurs qui effectuent l'événement personnalisé `shopify_paid_order`.]({% image_buster /assets/img/Shopify/shopify_paid_order.png %}){: style="max-width:80%;"}

Les événements personnalisés de Shopify pris en charge sont les suivants :

- `shopify_fulfilled_order`
- `shopify_partially_fulfilled_order`
- `shopify_paid_order`
- `shopify_account_login`

Pour un aperçu complet de toutes les charges utiles des événements, reportez-vous aux [fonctionnalités des données de Shopify]({{site.baseurl}}/shopify_data_features/).

### Synchronisation des produits Shopify 

Lorsque vous connectez et configurez chaque boutique Shopify dans Braze, vous pouvez éventuellement activer la synchronisation des produits Shopify dans le cadre de l'intégration.

Si vous activez la synchronisation des produits pour chaque magasin, Braze inclura le nom de votre magasin Shopify dans le nom du catalogue. Cela vous permet de distinguer les produits des différents magasins.

![Catalogues Shopify avec leur boutique Shopify dans leur nom.]({% image_buster /assets/img/Shopify/catalog_store_name.png %})

