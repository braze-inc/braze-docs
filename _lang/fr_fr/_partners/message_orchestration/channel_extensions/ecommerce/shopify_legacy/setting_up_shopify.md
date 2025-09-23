---
nav_title: Configuration de Shopify
article_title: "Configuration de Shopify"
description: "Cet article de référence explique comment configurer Shopify après l'avoir intégré dans votre SDK Web Braze."
page_type: partner
search_tag: Partner
alias: "/shopify_subscription_states/"
alias: "/setting_up_shopify_legacy/"
page_order: 2
---

# Configuration de Shopify dans Braze

> Cet article explique comment terminer la configuration de l'intégration Shopify avec Braze. Suivez ces instructions après avoir [déployé le SDK Web Braze]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/#implement-web-sdk) sur votre site Web Shopify.

## Configuration de l'intégration Shopify dans Braze

### Étape 1 : Connectez votre boutique Shopify

Dans Braze, allez à **Intégrations de partenaires** > **Partenaires technologiques**, puis recherchez Shopify.

{% alert note %}
Si vous utilisez l'ancienne navigation, vous pouvez trouver **Partenaires technologiques** sous **Intégrations**.
{% endalert %}

Sur la page partenaire Shopify, sélectionnez **Aller à la boutique d'applications Shopify** pour lancer le processus d'intégration.

![]({% image_buster /assets/img/Shopify/shop_setup_1.png %}){: style="max-width:70%"}

Vous serez ensuite dirigé vers l'App Store Shopify pour installer l'application Braze.

{% alert note %}
Si votre compte Shopify est associé à plus d'un magasin, vous pouvez changer de magasin en sélectionnant l'icône du magasin en haut à droite de la page et en sélectionnant **Changer de magasin**.
{% endalert %}

![]({% image_buster /assets/img/Shopify/switch_stores.png %}){: style="max-width:30%"}

Après avoir sélectionné votre magasin de choix, sélectionnez **Installer** sur la page de l'application Braze. 

![]({% image_buster /assets/img/Shopify/braze_install.png %}){: style="max-width:70%"}

Après avoir installé l'application Braze, vous serez redirigé vers Braze pour confirmer l'espace de travail que vous souhaitez connecter à Shopify. 

![]({% image_buster /assets/img/Shopify/confirm_workspace.png %}){: style="max-width:50%"}

Après avoir confirmé que vous êtes dans l'espace de travail correct, vous pouvez terminer la configuration de votre intégration Shopify en sélectionnant **Commencer la configuration**.

![]({% image_buster /assets/img/Shopify/begin_setup.png %}){: style="max-width:70%"}

{% alert note %}
Vous ne pouvez connecter qu'un seul magasin par espace de travail pour le moment. Si vous avez plusieurs boutiques Shopify que vous souhaitez connecter à votre espace de travail, contactez votre gestionnaire de la satisfaction client pour plus de détails sur la version bêta de Shopify pour plusieurs boutiques.
{% endalert %}

### Étape 2 : Sélectionner des événements et un remplissage historique

Après avoir connecté votre boutique Shopify, passez à l'étape 2 et sélectionnez les événements à inclure dans le cadre de votre intégration. Vous devez sélectionner au moins un événement.

![]({% image_buster /assets/img/Shopify/shopify_step_2_events.png %}){: style="max-width:70%"}

La sélection des événements **Produit Consulté**, **Produit Cliqué** ou **Panier Abandonné** nécessitera le SDK Web Braze pour le suivi. Si vous implémentez le SDK Web Braze soit via [Shopify ScriptTag]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/?tab=shopify%20scripttag#supported-features) ou directement sur le site de votre Shopify [`theme.liquid`]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/?tab=theme.liquid#supported-features), Braze générera automatiquement les scripts de suivi et les chargera sur votre site. Si vous déployez le SDK Web sur votre [site Shopify headless]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/#implement-web-sdk), vous devez activer manuellement le suivi de ces événements. 

#### Remplir les données historiques (facultatif)

Vous pouvez éventuellement activer un remplissage rétroactif des achats des 90 derniers jours avant votre installation. En synchronisant automatiquement les données des clients et des achats passés, vous pouvez immédiatement commencer à cibler et à engager vos clients. Pour en savoir plus, consultez le remplissage rétroactif de l’historique de Shopify.

![]({% image_buster /assets/img/Shopify/shop_setup_4.png %}){: style="max-width:70%"}

{% alert warning %}
Pour que le remplissage rétroactif importe les événements de création de commande et d'achat Braze, vous devez avoir inclus **Commande créée** et **Événement d’achat Braze** dans votre intégration.
{% endalert %}

### Étape 3 : Collecter des abonnés (facultatif)

En utilisant l'intégration Shopify, vous pouvez transférer des abonnés aux e-mails et aux SMS de votre boutique Shopify vers Braze. Pour plus d'informations, voir [Synchronisation des abonnés Shopify]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_features/shopify_user_identity/#syncing-shopify-subscribers).

![]({% image_buster /assets/img/Shopify/shopify_step_3_email.png %}){: style="max-width:70%"}

### Étape 4 : Configurer les synchronisations de produits Shopify (facultatif)

Vous pouvez synchroniser vos produits en temps quasi réel depuis votre boutique Shopify dans un catalogue Braze, automatisant le processus pour intégrer des données de produit pour une personnalisation plus poussée de vos messages. Pour en savoir plus, consultez [Synchronisations de produits Shopify]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_features/shopify_catalogs/).

![]({% image_buster /assets/img/Shopify/shopify_step_4_catalog.png %}){: style="max-width:70%"}

### Étape 5: Activer l'envoi de messages dans le navigateur 

Vous pouvez éventuellement utiliser un canal supplémentaire sur votre boutique Shopify pour les messages dans le navigateur en activant cette fonctionnalité. Cela vous permet d'utiliser nos types de message de base comme le diaporama, la fenêtre modale, plein écran, les enquêtes simples et le HTML personnalisé.

![]({% image_buster /assets/img/Shopify/shopify_step_5_channels.png %}){: style="max-width:70%"}

Si vous activez les messages dans le navigateur, le SDK Web Braze doit être déployé pour le suivi. Si vous implémentez le SDK Web Braze soit via [Shopify ScriptTag]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/?tab=shopify%20scripttag#supported-features) ou directement sur le site de votre Shopify [`theme.liquid`]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/?tab=theme.liquid#supported-features), Braze générera automatiquement le script de mise en œuvre de base du message dans le navigateur sur votre site. Si vous implémentez le SDK Web sur votre [site Shopify sans tête]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/#implement-web-sdk) ou prévoyez d'ajouter des personnalisations aux messages dans le navigateur, vous devez ajouter manuellement des messages dans le navigateur sur votre site en utilisant notre [guide du développeur]({{site.baseurl}}/developer_guide/in_app_messages/?sdktab=web). 

### Étape 6 : Terminer la configuration

Après avoir configuré votre intégration, sélectionnez **Terminer la configuration**.

![]({% image_buster /assets/img/Shopify/finish_setup.png %}){: style="max-width:70%"}

C'est tout ! Le statut « Connexion en attente » sera mis à jour en « Connecté » et affichera l'horodatage de l'établissement de la connexion. Vous verrez également si chaque fonctionnalité Shopify a été activée avec succès sur la page. 

![]({% image_buster /assets/img/Shopify/shopify_connected_store.png %}){: style="max-width:70%"}

### Paramètres avancés (facultatif) 

#### Mettre à jour les délais de panier abandonné et de paiement abandonné

Par défaut, Braze définit automatiquement le délai de déclenchement des événements `shopify_abandoned_checkout` et `shopify_abandoned_cart` à une heure d'inactivité. Vous pouvez définir le **Abandoned Cart Delay** et le **Abandoned Checkout Delay** pour chaque événement de 5 minutes à 24 heures en sélectionnant le menu déroulant, puis en sélectionnant **Set Delay** sur la page partenaire Shopify.

![]({% image_buster /assets/img/Shopify/shop_setup_advanced_abandonment.png %}){: style="max-width:30%"}

#### Définissez votre identifiant de produit préféré

Si vous avez inclus des événements d'achat Braze dans la configuration de votre intégration Shopify, par défaut, Braze définira l'ID de produit Shopify comme le `product_id` utilisé dans l'événement d'achat Braze. Cela sera utilisé lorsque vous filtrerez les produits achetés en Y jours ou personnaliserez le contenu de votre message en utilisant liquid.

Vous pouvez également choisir de définir soit l'unité de gestion des stocks soit le nom du produit de Shopify au lieu de l'ID du produit Shopify.

![]({% image_buster /assets/img/Shopify/shop_setup_advanced_productid.png %}){: style="max-width:30%"}

## Résolution des problèmes

{% details Pourquoi l'installation de mon application Shopify est-elle toujours en attente ? %}
Votre installation peut encore être en attente pour l'une des raisons suivantes :
 - Lorsque Braze configure vos webhooks Shopify
 - Lorsque Braze communique avec Shopify


Si l'installation de votre application ne progresse plus pendant 1 heure, Braze annulera l'installation et vous serez invité à recommencer la configuration.<br><br>
![Shopify]({% image_buster /assets/img/Shopify/shopify_integration8.png %}){: style="max-width:70%;"}
{% enddetails %}


{% details Pourquoi l'installation de mon application Shopify a-t-elle échoué ? %}
Votre installation a peut-être échoué pour l'une des raisons suivantes :
 - Braze n'a pas pu atteindre Shopify
 - Braze n'a pas pu traiter la requête
 - Votre jeton d'accès Shopify n'est pas valide
 - L'application Shopify Braze a été supprimée de votre page d'administration Shopify


Si cela se produit, vous pourrez sélectionner **Réessayer la configuration** et recommencer le processus d'installation.<br><br>
![Shopify]({% image_buster /assets/img/Shopify/shopify_integration16.png %}){: style="max-width:70%;"}
{% enddetails %}


{% details Comment désinstaller l'application Braze de ma boutique Shopify ? %}

Il existe deux façons de désinstaller Braze de votre boutique Shopify :

1. Sur la page partenaire Shopify, sélectionnez **Déconnecter**.<br><br> ![La section "Déconnexion de l'intégration" avec un lien pour se déconnecter.]({% image_buster /assets/img/Shopify/disconnect_integration.png %}){: style="max-width:70%;"}

2. Accédez à votre page d'administration Shopify située sous **Apps**. Vous verrez alors une option pour supprimer l'application Braze.<br><br> ![Une fenêtre modale demandant la confirmation que vous souhaitez supprimer l'application Braze.]({% image_buster /assets/img/Shopify/shopify_integration12.png %}){: style="max-width:70%;"}
{% enddetails %}

{% details Je peine à réconcilier mes utilisateurs. Quelle pourrait être la raison? %}

Le type de support dont vous aurez besoin pour le rapprochement des utilisateurs dépend de la façon dont vous avez déployé le SDK Web. Pour plus d'informations, consultez [Premiers pas avec Shopify]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/). 

- Si vous êtes sur un site Shopify headless, consultez la section sur la [mise en œuvre headless]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/?tab=headless%20shopify%20site#supported-features) pour vous assurer que vous avez activé le rapprochement des utilisateurs lors du paiement.
- Si vous rencontrez des profils d'utilisateurs en double avec le même e-mail ou numéro de téléphone, vous pouvez utiliser les outils Braze suivants pour fusionner les doublons en un seul profil : 
    - [`users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) endpoint
    - [Fusion en masse]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users#bulk-merging)
- Si vous utilisez l'intégration ScriptTag, et que votre boutique Shopify propose une option "Acheter maintenant" qui saute le panier, Braze peut avoir du mal à réconcilier les utilisateurs car Shopify ne permet pas aux balises de script de récupérer un `device_id` pour mapper les événements à un utilisateur qui saute le panier.

{% enddetails %}
