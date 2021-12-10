---
nav_title: Livraison déclenchée par l'API
article_title: Livraison déclenchée par l'API
page_order: 2
page_type: Référence
description: "Cet article de référence décrit comment planifier une campagne déclenchée par une API."
tool: Campagnes
platform: API
---

# Campagnes déclenchées par l'API

Les campagnes déclenchées par l'API ou les campagnes de déclenchement par le serveur sont idéales pour des cas d'utilisation transactionnelle plus avancés. Les campagnes déclenchées par l'API de Braze permettent aux marketeurs de gérer la copie de campagne, les tests multivariés, et les règles de rééligibilité dans le tableau de bord Braze tout en déclenchant la livraison de ce contenu à partir de leurs propres serveurs et systèmes. La requête API pour déclencher le message peut également inclure des données supplémentaires à modéliser dans le message en temps réel.

## Mise en place d'une campagne déclenchée par l'API

La mise en place d'une campagne déclenchée par l'API prend quelques étapes rapides. Tout d'abord, créez une nouvelle campagne multicanal ou mono-canal (avec des tests multivariés).

{% alert note %}
Une campagne déclenchée par l'API est différente d'une [campagne API]({{site.baseurl}}/developer_guide/rest_api/api_campaigns/#api-campaigns).
{% endalert %}

Ensuite, configurez votre copie et vos notifications de la même manière que vous si vous étiez une notification normalement planifiée et sélectionnez __la distribution déclenchée par l'API__. Pour plus d'informations sur le déclenchement de ces campagnes à partir de votre serveur, veuillez consulter la section de documentation des terminaux sur la [campagne d'envoi déclenchée par l'API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/).

!\[API-Triggered Delivery Step\]\[37\]

## Utiliser le contenu du modèle inclus avec une requête API

En plus de déclencher le message, vous pouvez également inclure du contenu avec la requête API à modéliser dans le message dans l'objet `trigger_properties`. Ce contenu peut être référencé dans le corps du message en disant quelque chose comme `{% raw %} {{ api_trigger_properties.${ some_value_included_with_request }}} {% endraw %}`. Voir l'exemple suivant de notification sociale pour plus de contextes :

!\[Social Example Delivery Window\]\[38\]{: style="max-width:70%;"}

## Rééligibilité avec des campagnes déclenchées par l'API

Le nombre de fois qu'un utilisateur reçoit une campagne déclenchée par l'API peut être limité en utilisant les paramètres de rééligibilité, ce qui signifie que l'utilisateur ne recevra la campagne qu'une seule fois dans une fenêtre donnée, peu importe le nombre de fois où le déclencheur de l'API est déclenché.

Par exemple, si vous utilisez une campagne déclenchée par une API pour envoyer à l'utilisateur une campagne à propos d'un élément qu'ils ont récemment consulté, vous pouvez limiter la campagne à envoyer un maximum d'un message par jour, peu importe le nombre d'éléments qu'ils ont consultés lors du déclenchement de l'API pour chaque élément. D'un autre côté, si votre campagne déclenchée par l'API est transactionnelle, vous voudrez vous assurer que l'utilisateur reçoit la campagne à chaque fois qu'il fait la transaction en définissant le délai à 0 minutes :

!\[Réglages de rééligibilité\]\[43\]
[37]: {% image_buster /assets/img_archive/api_triggered_campaign_delivery.png %} [38]: {% image_buster /assets/img_archive/api_triggered_photo_social_example_1.png %} [43]: {% image_buster /assets/img_archive/api_triggered_reeligible.png %}