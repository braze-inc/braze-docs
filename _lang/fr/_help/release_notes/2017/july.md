---
nav_title: Juillet
page_order: 6
noindex: true
page_type: update
description: "Cet article contient les notes de version de juillet 2017."
---

# Juillet 2017

## Grandes images dans les push Web

Nous avons ajouté une prise en charge des grandes images pour les notifications push Web sur Chrome pour Windows et Android afin de vous permettre de créer des expériences client riches et engageantes. En savoir plus sur le [push Web][58].

## Mises à jour des champs d’e-mail

Vous pouvez maintenant définir un ensemble spécifique d’adresses d’origine pour vos e-mails afin d’éviter de saisir accidentellement une adresse erronée. Le formulaire de composition d’e-mail sera prérempli avec les adresses utilisées au cours des 6 derniers mois pour rationaliser le processus. Pour plus d’informations, consultez les [meilleures pratiques pour l’e-mail][57].

## Mises à jour de l’endpoint /campaign/details de l’API

Le point de terminaison /campaign/details fournit maintenant des informations sur ses messages, ce qui vous permet d’extraire la ligne d’objet, le corps HTML, l’adresse et le champ « Reply-to (Répondre à) » via l’API. En savoir plus sur les [API Braze][56].

## Mises à jour du templating Liquid

Nous avons ajouté la possibilité de modéliser des attributs de variante dans les Canvas et les campagnes. Dans Canvas, vous pouvez maintenant modéliser l’ID API de la variante ainsi que le nom de la variante, et dans les campagnes, vous pouvez maintenant modéliser le `message_api_id` et `message_name` d’un message. Ces deux mises à jour vous offrent plus de flexibilité dans vos communications, en vous permettant de créer des campagnes personnalisées. En savoir plus sur la [messagerie personnalisée][55].

## Nouvel éditeur de messages HTML

Vous pouvez désormais écrire et tester facilement des e-mails avec un éditeur HTML plein écran avec prévisualisation en direct, une personnalisation via Liquid et un éditeur de texte plein écran amélioré avec des numéros de lignes et une coloration syntaxique. En savoir plus sur la [composition des e-mails][54].

## Mises à jour de la prévisualisation

Vous pouvez maintenant suivre la fenêtre d’écran lorsque vous faites défiler les aperçus des messages dans vos campagnes et Canvas, pour que vous puissiez toujours voir l’impact des modifications. En savoir plus sur la [prévisualisation et les tests][53].

## Filtre d’adhésion à nouveau segment

Nous avons ajouté un filtre [Segment Membership (Appartenance au segment)][52], pour vous permettre de cibler les utilisateurs en fonction de leur appartenance à l’un de vos segments existants. En outre, nous avons ajouté la possibilité d’utiliser les opérateurs « And » (Et) et « Or » (Ou) dans les filtres de segment, ainsi que la capacité d’imbriquer des segments. Ces mises à jour vous permettent d’envoyer des messages personnalisés à vos clients avec plus de précision. 

## Mise à jour de la prévisualisation sur Android

Nous avons mis à jour la [prévisualisation pour Android][51] pour refléter les versions plus récentes d’Android depuis Android N.


[51]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/#step-5-preview-message
[52]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#targeting-filters
[53]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/campaigns_in_multiple_languages/#step-6-preview-message
[54]: {{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_template/#creating-an-email-template
[55]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/personalized_messaging/#personalized-messaging
[56]: {{site.baseurl}}/developer_guide/rest_api/basics/#what-is-a-rest-api
[57]: {{site.baseurl}}/help/troubleshooting_guide/troubleshooting_guide/#email
[58]: {{site.baseurl}}/user_guide/message_building_by_channel/push/web
[98]:{{site.baseurl}}/user_guide/onboarding/platform_administrative_features/#authentication-rules
