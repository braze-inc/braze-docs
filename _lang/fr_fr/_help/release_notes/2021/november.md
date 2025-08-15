---
nav_title: novembre
page_order: 1
noindex: true
page_type: update
description: "Cet article contient les notes de version de novembre 2021."
---
# Novembre 2021

## Indicateur de rapport « Taux de Click-to-Open »
Braze a ajouté une nouvelle métrique d'email, le taux de clics par ouverture, disponible dans le [Report Builder]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/). Cette mesure représente le pourcentage d’e-mails ouverts qui ont été cliqués.

## Indicateur de rapport « Ouverture machine »

Une nouvelle métrique d'email, [Ouvertures de machine]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/analytics_glossary/#machine-opens), est disponible sur les pages Canvas et Campaign Analytics pour les emails. Cette métrique identifie les ouvertures d'e-mails qui ne sont pas humaines (comme celles ouvertes par les serveurs d'Apple), affichées comme un sous-ensemble du total des ouvertures.

## variable Liquid random_bucket_number
Une variable `random_bucket_number` a été ajoutée à la liste des [variables Liquid prises en charge]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#supported-personalization-tags) pour la personnalisation des messages. 

## Recommandations pour les notifications push riches sur iOS 15
De nouvelles [directives de notification push iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/) ont été ajoutées aux documents riches iOS, y compris des informations sur les états de notification et une répartition des variables de troncature de texte.

## Adresses IP supplémentaires à whitelister pour l’UE pour les webhooks et le Contenu connecté
Des IP supplémentaires à autoriser dans l'UE pour les webhooks et le contenu connecté ont été ajoutées à notre article [webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) et [Contenu Connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/). Ces nouvelles adresses IP incluent `18.157.135.97`, `3.123.166.46`, `3.64.27.36`, `3.65.88.25`, `3.68.144.188` et `3.70.107.88`.

## Endpoint d’exportation des achats
Un nouveau [`/purchases/product_list` point de terminaison]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id/) a été ajouté à Braze. Cet endpoint renvoie des listes paginées d’ID Produit.

## Nouveaux partenariats Braze

### Adobe - Plateforme de données client
L'intégration de Braze et [Adobe]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/adobe/#adobe) permet aux marques de connecter et de mapper leurs données Adobe (attributs personnalisés et segments) à Braze en temps réel. Les marques peuvent ensuite se servir de ces données pour offrir des expériences personnalisées et ciblées à ces utilisateurs. 

### BlueConic - Plateforme de données client
Avec [Blueconic]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/blueconic/#blueconic), les utilisateurs de Braze peuvent unifier les données en profils individuels persistants, puis les synchroniser à travers les points de contact et les systèmes clients pour soutenir une large gamme d'initiatives axées sur la croissance, y compris l'orchestration du cycle de vie des clients, la modélisation et l'analyse, les produits et expériences numériques, la monétisation basée sur l'audience, et plus encore.

### Worthy - Contenu dynamique
L'intégration de Braze et [Worthy]({{site.baseurl}}/partners/message_personalization/dynamic_content/worthy/#worthy) vous permet de créer facilement des expériences personnalisées et riches dans l'application en utilisant l'éditeur de contenu dynamique par glisser-déposer de Worthy et de les diffuser via Braze.

### Judo - Contenu dynamique
L'intégration de [Judo]({{site.baseurl}}/partners/message_personalization/dynamic_content/judo/#judo) et Braze vous permet d'écraser les composants de votre campagne et de les remplacer par des expériences Judo. Les données Braze peuvent également fournir du contenu personnalisé dans une expérience Judo. Les événements et les données des utilisateurs de l’expérience peuvent faire l’objet d’un retour dans Braze pour l’attribution et le ciblage.

### Line - Envoi de messages
L'intégration [Line]({{site.baseurl}}/partners/message_orchestration/additional_channels/messaging/line/#line) et Braze vous permet de tirer parti des webhooks Braze, de la segmentation avancée, de la personnalisation et des fonctionnalités de déclenchement pour envoyer des messages à vos utilisateurs dans Line via l'[API de messagerie Line](https://developers.line.biz/en/docs/messaging-api/overview/).

### RevenueCat - Paiements
L'intégration de [RevenueCat]({{site.baseurl}}/partners/data_and_infrastructure_agility/payments/revenuecat/#revenuecat) et Braze vous permet de synchroniser automatiquement les événements d'achat et de cycle de vie des abonnements de vos clients sur toutes les plateformes. Cela vous permet de créer des campagnes qui réagissent en fonction de l’étape du cycle de vie d’abonnement de vos clients, par exemple pour communiquer avec des clients qui se sont désinscrits pendant leur essai gratuit ou envoyer des rappels aux clients en défaut de paiement.

### Punchh - Fidélisation
[Punchh]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/punchh/#punchh) s'est associé à Braze pour synchroniser les données entre les deux plateformes à des fins de cadeaux et de fidélité. Les données utilisateur publiées dans Braze seront disponibles pour la segmentation et peuvent être synchronisées dans Punchh via des modèles de webhooks configurés dans Braze.   