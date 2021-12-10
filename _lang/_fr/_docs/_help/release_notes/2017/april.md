---
nav_title: Avril
page_order: 9
noindex: vrai
page_type: Mettre à jour
description: "Cet article contient des notes de mise à jour pour avril 2017."
---

# Avril 2017

## Messages HTML dans le navigateur

Nous prenons maintenant en charge les types de messages interactifs dans le navigateur, y compris les formats HTML et de capture de courriels personnalisés, ce qui vous permet de rejoindre vos clients où qu'ils se trouvent. En savoir plus sur les messages dans l'application [ici][48].

## Message personnalisé dans l'application avec le contenu connecté

Nous avons ajouté {% raw %} {%connected_content%} {% endraw %} blocs dans les messages déclenchés dans l'application, ce qui vous permet d'ajouter une personnalisation riche en insérant toutes les informations accessibles via l'API directement dans vos messages. Maintenant, vous pouvez utiliser le Contenu Connecté dans votre application en plus de votre push, e-mail et webhooks. En savoir plus sur le Contenu Connecté [ici][34].

## Amélioration de la navigation pour les cartes de flux d'actualités

Nous avons amélioré l'interface utilisateur pour la création de cartes de flux d'actualités, ce qui vous permet de naviguer plus facilement et de créer vos campagnes. En savoir plus sur les cartes de flux d'actualités [ici][33].

## Aperçu amélioré pour les notifications riches iOS

Nos notifications d'aperçu sur iOS affichent maintenant des notifications enrichies vous donnant une vue claire de ce que vous envoyez à vos clients, jusqu'à la taille de la police. En savoir plus sur les notifications riches iOS [ici][32].

## Ajout des « Opens Influencés» aux statistiques push

Nous avons ajouté « Oens influés » à notre liste de statistiques standard de campagne et de Canvas offertes en Brésil, en facilitant la connaissance de la panne de vos campagnes d'ouvertures influentes, directes et totales. En savoir plus sur les Ouvertures Influencées [ici][31].

## Mettre à niveau vers des groupes internes

Vous pouvez maintenant créer plusieurs groupes internes et assigner des propriétés indiquant si le groupe sera utilisé pour la journalisation du SDK, Enregistrement de l'API REST, ou test de contenu. En savoir plus sur les logs des utilisateurs et les tests [ici][30].

> Mise à jour : Les groupes internes peuvent également être utilisés pour [envoyer des emails de seed]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/#seed-groups).

## Nouvelles options pour les URLs web

Vous avez maintenant la possibilité d'ouvrir des URL web dans un navigateur Web externe pour les messages push, les messages dans l'application et dans le navigateur, et les cartes de News Feed. L'action "Deep Link into App" est également compatible avec les liens profonds HTTP/HTTP. Si vous utilisez un partenaire comme Branch ou Apple Universal Links, vous aurez besoin d'une personnalisation du SDK. En savoir plus sur les liens profonds [ici][29].

## Nouvelle toile d'événement "Conversion effectuée"

Nous avons ajouté un nouvel événement « Conversion exécutée » et un filtre « Contrôle en ligne » pour des options de repositionnement améliorées. En savoir plus sur l'utilisation des filtres de relocalisation [ici][28].



[28]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/#retargeting-campaigns
[29]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking
[30]: {{site.baseurl}}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab
[31]: {{site.baseurl}}/user_guide/data_and_analytics/influenced_opens/#influenced-opens
[32]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/#ios-10-rich-notifications
[33]: {{site.baseurl}}/user_guide/engagement_tools/news_feed/creating_a_news_feed_item/#news-feed-cards
[34]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/
[48]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/
