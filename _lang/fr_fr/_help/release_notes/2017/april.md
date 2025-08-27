---
nav_title: avril
page_order: 9
noindex: true
page_type: update
description: "Cet article contient les notes de version d’avril 2017."
---

# Avril 2017

## Messages HTML intégrés au navigateur

Nous prenons désormais les messages intégrés au navigateur interactifs, y compris les formats HTML et e-mail personnalisés, pour vous permettre d’atteindre vos clients où qu’ils se trouvent. En savoir plus sur les [messages in-app.]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/)

## Message in-app personnalisé avec contenu connecté

Nous avons ajouté les blocs {% raw %} {%connected_content%} {% endraw %} dans les messages in-app déclenchés, ce qui vous permet d'ajouter une personnalisation riche en insérant toute information accessible via l'API directement dans vos messages. Vous pouvez maintenant utiliser le Contenu connecté à l’intérieur de votre application en plus de vos notifications push, e-mails et webhooks. En savoir plus sur le [contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/).

## Navigation améliorée sur les cartes de fil d’actualité

Nous avons amélioré l’interface utilisateur pour la création de cartes de fil d’actualité afin de faciliter la création et la navigation dans vos campagnes. En savoir plus sur les [cartes de fil d'actualité]({{site.baseurl}}/user_guide/engagement_tools/news_feed/creating_a_news_feed_item/#news-feed-cards).

## Prévisualisation améliorée pour les notifications riches iOS

Notre prévisualisation pour iOS affiche désormais des notifications riches qui vous donnent une vue claire de ce que vous envoyez à vos clients, jusqu’à la taille de police. En savoir plus sur les [notifications riches d'iOS.]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#ios-10-rich-notifications)

## Ajout des « Ouvertures influencées » dans les statistiques push

Nous avons ajouté des « Ouvertures influencées » à notre liste des statistiques de campagne et de Canvas standard proposées dans Braze pour que vous puissiez voir facilement vos ouvertures Directes, Influencées et Totales. En savoir plus sur les [Opens Influenced]({{site.baseurl}}/user_guide/analytics/tracking/influenced_opens/).

## Mise à niveau des groupes internes

Vous pouvez maintenant créer plusieurs groupes internes et attribuer des propriétés indiquant si le groupe sera utilisé pour la journalisation SDK, la journalisation API REST ou les tests de contenu des messages. En savoir plus sur les [journaux des événements utilisateurs]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab).

> Mise à jour : Les groupes internes peuvent également être utilisés pour [envoyer des e-mails initiateurs]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/#seed-groups).

## Nouvelles options pour les URL Web

Vous avez maintenant la possibilité d’ouvrir des URL Web dans un navigateur Web externe pour les messages push, les messages in-app et intégrés au navigateur, et les cartes de fil d’actualité. L'action "Lien profond dans l'application" est désormais compatible avec les liens profonds HTTP/HTTPS. Si vous utilisez un partenaire comme Branch ou Universal Links d’Apple, vous devez personnaliser le SDK. En savoir plus sur la [création de liens profonds]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking).

## Nouvel événement « Performed Conversion » (Conversion effectuée) dans Canvas

Nous avons ajouté un nouvel événement « Performed Conversion » (Conversion effectuée) et un filtre « In Canvas Control » (Dans le groupe de contrôle Canvas) pour améliorer vos options de reciblage. En savoir plus sur l'utilisation des [filtres de reciblage]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/#retargeting-campaigns).



