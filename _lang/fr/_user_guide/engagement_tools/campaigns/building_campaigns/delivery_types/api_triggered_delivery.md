---
nav_title: Livraison déclenchée par API
article_title: Livraison déclenchée par API
page_order: 2
page_type: reference
description: "Le présent article de référence décrit comment planifier et configurer une campagne déclenchée par API."
tool: Campagnes
platform: API

---

# Campagnes déclenchées par API

Les campagnes déclenchées par API ou les campagnes déclenchées par serveur sont idéales pour des cas d’utilisation transactionnels plus avancés. Les campagnes déclenchées par API de Braze permettent aux marketeurs de gérer les copies de campagne, les tests multivariés et les règles de rééligibilité dans le tableau de bord de Braze tout en déclenchant la livraison de ce contenu à partir de leurs propres serveurs et systèmes. La demande API pour déclencher le message peut également inclure des données supplémentaires à modéliser dans le message en temps réel.

## Configurer une campagne déclenchée par API

La configuration d’une campagne déclenchée par API nécessite quelques étapes rapides. Commencez par créer une nouvelle campagne à canal unique ou multicanale (avec des tests multivariés).

{% alert note %}
Une campagne déclenchée par API est différente d’une [campagne API]({{site.baseurl}}/developer_guide/rest_api/api_campaigns/#api-campaigns).
{% endalert %}

Configurez ensuite votre texte et vos notifications comme vous le feriez normalement pour les notifications planifiées et sélectionnez **API-Triggered Delivery (Livraison déclenchée par API)**. Pour plus d’informations sur le déclenchement de ces campagnes depuis votre serveur, consultez la documentation de l’endpoint dans [Envoyer une campagne déclenchée par API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/).

![][37]

## Utiliser le contenu modélisé compris dans une demande API

En plus de déclencher le message, vous pouvez également inclure du contenu avec la demande API à modéliser dans le message avec l’objet `trigger_properties`. Ce contenu peut être référencé dans le corps du message. Par exemple, vous pouvez inclure :
``{% raw %} {{ api_trigger_properties.${ some_value_included_with_request }}} {% endraw %}``. Consultez l’exemple suivant de notification sociale pour trouver une mise en contexte supplémentaire :

![Les propriétés de déclenchement mentionnées ci-dessus sont comprises dans le message pour remplir automatiquement le nom de l’utilisateur, suivi du texte : « a aimé votre photo ! Cliquez ici pour voir ses activités. »][38]{: style="max-width:70%;"}

## Rééligibilité aux campagnes déclenchées par les API

Le nombre de fois où un utilisateur reçoit une campagne déclenchée par API peut être limité en utilisant des paramètres de rééligibilité. Cela signifie que l’utilisateur recevra la campagne une seule fois ou une seule fois dans une période donnée, indépendamment du nombre de fois où le déclencheur API est activé.

Supposons par exemple que vous utilisiez une campagne déclenchée par API pour envoyer à l’utilisateur une campagne sur un élément qu’il a récemment consulté. Dans ce cas, vous pouvez limiter la campagne pour envoyer au maximum un message par jour, quel que soit le nombre d’éléments qu’ils ont vus tout en activant le déclencheur API pour chaque élément. D’autre part, si votre campagne déclenchée par API est transactionnelle, vous devez vous assurer que l’utilisateur reçoive la campagne chaque fois qu’il effectue la transaction en définissant le délai sur zéro minute.

![][43]


[37]: {% image_buster /assets/img_archive/api_triggered_campaign_delivery.png %}
[38]: {% image_buster /assets/img_archive/api_triggered_photo_social_example_1.png %}
[39]: {{site.baseurl}}/developer_guide/rest_api/messaging/#sending-messages-via-api-triggered-delivery
[42]: {{site.baseurl}}/developer_guide/rest_api/messaging/#sending-messages-via-api-triggered-delivery
[43]: {% image_buster /assets/img_archive/api_triggered_reeligible.png %}