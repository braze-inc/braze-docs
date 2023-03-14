---
nav_title: Avril
page_order: 9
noindex: true
page_type: update
description: "Cet article contient les notes de version d’avril 2017."
---

# Avril 2017

## Messages HTML dans le navigateur

Nous prenons désormais les messages in-browser interactifs, y compris les formats HTML et e-mail personnalisés, pour vous permettre d’atteindre vos clients où qu’ils se trouvent. En savoir plus sur les [Messages in-app][48].

## Message in-app personnalisé avec contenu connecté

Nous avons ajouté des blocs {% raw %} {%connected_content%} {% endraw %} dans les messages in-app déclenchés, qui vous permettent d’ajouter une personnalisation riche en insérant directement dans vos messages toute information accessible via l’API. Vous pouvez maintenant utiliser le Contenu connecté à l’intérieur de votre application en plus de vos notifications push, e-mails et webhooks. En savoir plus sur le [Contenu connecté][34].

## Navigation améliorée sur les cartes de fil d’actualité

Nous avons amélioré l’interface utilisateur pour la création de cartes de fil d’actualité afin de faciliter la création et la navigation dans vos campagnes. En savoir plus sur [Cartes de fil d’actualité][33].

## Prévisualisation améliorée pour les notifications riches iOS

Notre prévisualisation pour iOS affiche désormais des notifications riches qui vous donnent une vue claire de ce que vous envoyez à vos clients, jusqu’à la taille de police. En savoir plus sur [Notifications riches sur iOS][32].

## Ajout des « Ouvertures influencées » dans les statistiques push

Nous avons ajouté des « Ouvertures influencées » à notre liste des statistiques de campagne et de Canvas standard proposées dans Braze pour que vous puissiez voir facilement vos ouvertures Directes, Influencées et Totales. En savoir plus sur les [Ouvertures influencées][31].

## Mise à niveau des groupes internes

Vous pouvez maintenant créer plusieurs groupes internes et attribuer des propriétés indiquant si le groupe sera utilisé pour la journalisation SDK, la journalisation API REST ou les tests de contenu des messages. En savoir plus sur les [Journaux d’événements utilisateurs ][30].

> Mise à jour : Les groupes internes peuvent également être utilisés pour [envoyer des e-mails à des seedlists]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/#seed-groups).

## Nouvelles options pour les URL Web

Vous avez maintenant la possibilité d’ouvrir des URL Web dans un navigateur Web externe pour les messages push, les messages in-app et dans le navigateur, et les Cartes de fil d’actualité. L’action « Deep Link into App » (Liens profonds dans l’appli) est également compatible avec les liens profonds HTTP/HTTPS. Si vous utilisez un partenaire comme Branch ou Universal Links d’Apple, vous devez personnaliser le SDK. En savoir plus sur le [Deep linking][29].

## Nouvel événement « Performed Conversion » (Conversion effectuée) dans Canvas

Nous avons ajouté un nouvel événement « Performed Conversion » (Conversion effectuée) et un filtre « In Canvas Control » (Dans le groupe de contrôle Canvas) pour améliorer vos options de reciblage. En savoir plus sur l’utilisation des [filtres de reciblage][28].



[28]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/#retargeting-campaigns
[29]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking
[30]: {{site.baseurl}}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab
[31]: {{site.baseurl}}/user_guide/data_and_analytics/influenced_opens/#influenced-opens
[32]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/#ios-10-rich-notifications
[33]: {{site.baseurl}}/user_guide/engagement_tools/news_feed/creating_a_news_feed_item/#news-feed-cards
[34]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/
[48]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/
[98]:{{site.baseurl}}/user_guide/onboarding/platform_administrative_features/#authentication-rules
