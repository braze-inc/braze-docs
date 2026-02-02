---
nav_title: juillet
page_order: 6
noindex: true
page_type: update
description: "Cet article contient les notes de version de juillet 2017."
---

# Juillet 2017

## Grandes images dans les push Web

Nous avons ajouté une prise en charge des grandes images pour les notifications push Web sur Chrome pour Windows et Android afin de vous permettre de créer des expériences client riches et engageantes. En savoir plus sur le [web push.]({{site.baseurl}}/user_guide/message_building_by_channel/push/web)

## Mises à jour des champs d’e-mail

Vous pouvez maintenant définir un ensemble spécifique d’adresses d’origine pour vos e-mails afin d’éviter de saisir accidentellement une adresse erronée. Le formulaire de composition d’e-mail sera prérempli avec les adresses utilisées au cours des 6 derniers mois afin de simplifier le processus. Pour plus d'informations, consultez les [meilleures pratiques en matière d'e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices).

## Mises à jour de l’endpoint /campaign/details de l’API

L'endpoint `/campaign/details` fournit désormais des informations sur ses messages, ce qui vous permet d'extraire les champs sujet, corps HTML, adresse de départ et réponse à l'aide de l'API. En savoir plus sur les [API de Braze]({{site.baseurl}}/developer_guide/rest_api/basics/#what-is-a-rest-api).

## Mises à jour du templating Liquid

Nous avons ajouté la possibilité de modéliser des attributs de variante dans les Canvas et les campagnes. Dans Canvas, vous pouvez maintenant modéliser l’ID API de la variante ainsi que le nom de la variante, et dans les campagnes, vous pouvez maintenant modéliser le `message_api_id` et `message_name` d’un message. Ces deux mises à jour vous offrent plus de flexibilité dans vos communications, en vous permettant de créer des campagnes personnalisées. En savoir plus sur l'[envoi de messages personnalisés]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/).

## Nouvel éditeur de messages HTML

Vous pouvez désormais écrire et tester facilement des e-mails avec un éditeur HTML plein écran avec prévisualisation en direct, une personnalisation via Liquid et un éditeur de texte plein écran amélioré avec des numéros de lignes et une coloration syntaxique. En savoir plus sur la [composition des e-mails]({{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_template/#creating-an-email-template).

## Mises à jour de la prévisualisation

Vous pouvez maintenant suivre la fenêtre d’écran lorsque vous faites défiler les aperçus des messages dans vos campagnes et Canvas, pour que vous puissiez toujours voir l’impact des modifications. En savoir plus sur la [prévisualisation et les tests]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/campaigns_in_multiple_languages/#step-6-preview-message).

## Filtre d’adhésion à nouveau segment

Nous avons ajouté le [filtre d'appartenance à un segment]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#targeting-filters), qui vous permet de cibler les utilisateurs en fonction de leur appartenance à l'un de vos segments existants. En outre, nous avons ajouté la possibilité d’utiliser les opérateurs « And » (Et) et « Or » (Ou) dans les filtres de segment, ainsi que la capacité d’imbriquer des segments. Ces mises à jour vous permettent d’envoyer des messages personnalisés à vos clients avec plus de précision. 

## Mise à jour de la prévisualisation sur Android

Nous avons mis à jour l'[aperçu d'Android]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/#step-5-preview-message) pour refléter les versions plus récentes d'Android depuis Android N.


