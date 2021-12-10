---
nav_title: "Push pour le Web"
article_title: Push pour le Web
page_order: 9
page_type: Référence
description: "Cette page de référence couvre brièvement le web push, et renvoie aux étapes nécessaires pour en créer une."
platform: Web
channel:
  - Pousser
---

# Push Web

> Le Web push est un autre excellent moyen de s’engager auprès des utilisateurs de votre application web. Clients visitant votre site Web via Chrome, Safari, Firefox, et Opera peut choisir de recevoir des push web de votre application web, que la page web soit chargée ou non. Cette fonctionnalité est également prise en charge sur Android Chrome et Firefox Mobile sur Android permettant des notifications Web mobiles.

Le Web push fonctionne de la même façon que les notifications push des applications fonctionnent sur votre téléphone. Pour plus d'informations sur la composition d'une push web, consultez notre page sur [la création d'une notification push][11]. Voir à droite pour un exemple de push web envoyé par Braze.

![Exemple[12]

Les utilisateurs de votre application web doivent opter pour recevoir un push web. Voir ci-dessous.

!\[web-push-optin\]\[13\]

Pour plus d'informations sur les normes du protocole push et le support du navigateur, vous pouvez consulter les ressources de [Apple][3] [Mozilla][1] et [Microsoft][2]

{% alert important %}
Les fenêtres de navigation privée ne prennent actuellement pas en charge le push web.
{% endalert %}
[12]: {% image_buster /assets/img_archive/Macbook_Push.png %} [13]: {% image_buster /assets/img_archive/WebPush_Prompt.png %}

[1]: https://developer.mozilla.org/en-us/docs/web/api/push_api#browser_compatibility
[2]: https://developer.microsoft.com/en-us/microsoft-edge/status/pushapi/
[3]: https://developer.apple.com/notifications/safari-push-notifications/
[11]: {{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message
