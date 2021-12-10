---
nav_title: Juillet
page_order: 6
noindex: vrai
page_type: Mettre à jour
description: "Cet article contient des notes de mise à jour pour juillet 2017."
---

# Juillet 2017

## Grandes images en poussant sur le web

Nous avons ajouté la prise en charge de grandes images pour les Push Web sur Chrome pour Windows et Android, vous donnant la possibilité de créer des expériences client riches et intéressantes. En savoir plus sur la campagne web [ici][58].

## Mises à jour des champs email

Vous pouvez maintenant verrouiller les courriels à un ensemble spécifique d’adresses, en veillant à ce que vous ne saisissiez pas accidentellement la mauvaise adresse. Le formulaire de composition de courriel sera pré-rempli avec les adresses utilisées au cours des 6 derniers mois pour simplifier le processus. En savoir plus sur les meilleures pratiques de messagerie [ici][57].

## Mises à jour de l'API des détails de la campagne

Le point de terminaison /campaign/details de l'API donne maintenant des informations à propos de ses messages, vous permettant de tirer le sujet, le corps HTML, l'adresse from-et les champs de réponse à l'aide de l'API. En savoir plus sur nos APIs [ici][56].

## Mises à jour du modèle Liquid

Nous avons ajouté la possibilité de modéliser les attributs des variantes dans les campagnes et les canevas. Dans Canvas, vous pouvez maintenant modéliser à la fois l’identifiant API de la variante et le nom de la variante, et dans les campagnes vous pouvez maintenant modéliser un message message_api_id et message_name. Les deux mises à jour permettent une plus grande flexibilité dans votre messagerie, vous permettant de créer des campagnes personnalisées. En savoir plus sur la messagerie personnalisée [ici][55].

## Nouvel éditeur de courriel HTML

Vous pouvez maintenant facilement écrire et tester les e-mails avec un éditeur HTML plein écran qui permet l'aperçu en direct, la personnalisation via Liquid et un éditeur de texte en plein écran amélioré avec les numéros de ligne et la coloration syntaxique. En savoir plus sur la composition des e-mails [ici][54].

## Mises à jour vers les aperçus

Vous pouvez maintenant suivre la fenêtre d'écran pendant que vous faites défiler les aperçus des messages vers le bas dans les campagnes & Canvas, en veillant à ce que vous puissiez toujours voir les changements reflétés. En savoir plus sur la prévisualisation et le test [ici][53].

## Nouveau filtre d'abonnement au segment

Nous avons ajouté un nouveau filtre, Adhésion au segment, vous permettant de cibler les utilisateurs en fonction de leur adhésion à l'un de vos segments existants. En outre, nous avons ajouté la possibilité d'utiliser la logique « ET » et « Ou » dans les filtres de segments, ainsi que la capacité à imbriquer les segments entre eux. Ces mises à jour vous permettent d'envoyer des messages personnalisés à vos clients avec plus de précision. En savoir plus sur les filtres [ici][52].

## Mettre à jour vers l'aperçu Android

Nous avons mis à jour l'aperçu d'Android pour refléter les versions plus récentes d'Android depuis Android N. En savoir plus sur les messages d'aperçu [ici][51].


[51]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/#step-5-preview-message
[52]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#targeting-filters
[53]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/campaigns_in_multiple_languages/#step-6-preview-message
[54]: {{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_template/#creating-an-email-template
[55]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/personalized_messaging/#personalized-messaging
[56]: {{site.baseurl}}/developer_guide/rest_api/basics/#what-is-a-rest-api
[57]: {{site.baseurl}}/help/troubleshooting_guide/troubleshooting_guide/#email
[58]: {{site.baseurl}}/help/best_practices/web_sdk/#web-push
