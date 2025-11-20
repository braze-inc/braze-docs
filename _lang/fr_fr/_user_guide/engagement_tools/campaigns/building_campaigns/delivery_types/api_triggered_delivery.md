---
nav_title: "Réception/distribution déclenchée par l'API"
article_title: "Réception/distribution déclenchée par l'API"
page_order: 2
page_type: reference
description: "Cet article de référence explique comment planifier et implémenter une campagne déclenchée par l'API."
tool: Campaigns
platform: API

---

# Réception/distribution déclenchée par l'API

> Les campagnes déclenchées par l'API ou par le serveur sont idéales pour les cas d'utilisation transactionnelle plus avancés. Les campagnes déclenchées par l'API de Braze permettent aux marketeurs de gérer le texte de la campagne, les tests multivariés et les règles de rééligibilité dans le bord de Braze tout en déclenchant la réception/distribution de ce contenu à partir de leurs propres serveurs et systèmes. La demande d'API pour déclencher le message peut également inclure des données supplémentaires qui seront intégrées au message en temps réel.

## Implanter une campagne déclenchée par l'API

L'implémentation d'une campagne déclenchée par l'API se fait en quelques étapes. Tout d'abord, créez une nouvelle campagne multicanal ou monocanal (avec des tests multivariés).

{% alert note %}
Une campagne déclenchée par l'API est différente d'une [campagne API]({{site.baseurl}}/developer_guide/rest_api/api_campaigns/#api-campaigns).
{% endalert %}

Ensuite, configurez votre copie et vos notifications de la même manière que vous le feriez normalement pour les notifications planifiées et sélectionnez **API-Triggered Delivery**. Pour plus d'informations sur le déclenchement de ces campagnes à partir de votre serveur, consultez cet article sur l'[envoi de campagnes déclenché par l'API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/).

\![]({% image_buster /assets/img_archive/api_triggered_campaign_delivery.png %})

## Utilisation du contenu modèle inclus dans une demande d'API

Outre le déclencheur du message, vous pouvez également inclure le contenu de la demande d'API dans le message à l'intérieur de l'objet `trigger_properties`. Ce contenu peut être référencé dans le corps du message. Par exemple, vous pouvez inclure :
``{% raw %} {{ api_trigger_properties.${ some_value_included_with_request }}} {% endraw %}``. Pour plus de détails, consultez l'exemple suivant de notification sociale :

\![La propriété du déclencheur susmentionné incluse dans le message pour remplir automatiquement le nom de l'utilisateur suivi du texte : "J'ai aimé votre photo ! Cliquez ici pour voir ce qu'ils ont fait".]({% image_buster /assets/img_archive/api_triggered_photo_social_example_1.png %}){: style="max-width:70%;"}

## Rééligibilité avec des campagnes déclenchées par l'API

Le nombre de fois qu'un utilisateur reçoit une campagne déclenchée par l'API peut être limité à l'aide des paramètres de rééligibilité. Cela signifie que l'utilisateur ne recevra la campagne qu'une seule fois ou une seule fois dans une fenêtre donnée, quel que soit le nombre de fois où le déclencheur de l'API est déclenché.

Par exemple, disons que vous utilisez une campagne déclenchée par l'API pour envoyer à l'utilisateur une campagne sur un article qu'il a récemment consulté. Dans ce cas, vous pouvez limiter la campagne à l'envoi d'un message par jour, quel que soit le nombre d'articles consultés, tout en déclenchant l'API pour chaque article. En revanche, si votre campagne déclenchée par l'API est transactionnelle, vous voudrez vous assurer que l'utilisateur reçoit la campagne à chaque fois qu'il effectue la transaction en définissant le délai à zéro minute.

\![]({% image_buster /assets/img_archive/api_triggered_reeligible.png %})


