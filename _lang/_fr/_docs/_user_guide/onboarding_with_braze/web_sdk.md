---
nav_title: SDK Web
article_title: Aperçu du SDK Web
page_order: 3
page_type: Référence
description: "Cet article de référence sur l'intégration couvre l'implémentation de Braze Web SDK."
---

# SDK Web

Avec Braze Web SDK, vous pouvez collecter des données de session, identifier les utilisateurs (avec le même ensemble d'attributs que ceux que nous prenons en charge sur nos autres plateformes), et enregistrer les achats et les événements personnalisés via un navigateur web/mobile. Implémenter Braze Web SDK vous permet de créer une vue plus complète de vos utilisateurs à travers les canaux Web et mobiles. Vous pouvez également utiliser le SDK Web pour vous engager avec vos utilisateurs en envoyant des messages Web et des notifications push Web dans l'application.

## Implémentation

Pour des informations sur l'intégration du Braze Web SDK, consultez notre [documentation][6]. Après avoir implémenté le SDK Web, votre site Web apparaîtra comme une application dans votre groupe d'applications et sera regroupé avec vos applications mobiles.

!\[Web_App_Group\]\[7\]

## Messagerie web intégrée

Vous pouvez envoyer des messages Web pour vous engager avec les utilisateurs directement dans leur navigateur web/mobile. Les messages Web sont envoyés sous forme de messages intégrés à l'application, et peuvent également être envoyés sous forme de type slideup, modal ou plein écran. Pour plus d'informations sur la composition d'un message dans l'application, consultez notre page sur [la création d'un message dans l'application][8].

## Push Web

!\[Web Push Example\]\[12\]{: style="float:right;max-width:60%;margin-left:15px;border:0;"}

Le Web push est un autre excellent moyen de s’engager auprès des utilisateurs de votre application web. Clients visitant votre site Web via Chrome, Safari, Firefox, et Opera peut choisir de recevoir des push web de votre application web, que la page web soit chargée ou non. Cette fonctionnalité est également prise en charge sur Android Chrome et Firefox Mobile sur Android permettant des notifications Web mobiles. Le Web push fonctionne de la même façon que les notifications push des applications fonctionnent sur votre téléphone. Pour plus d'informations sur la composition d'une push web, consultez notre page sur [la création d'une notification push][11]. Voir ci-dessous pour un exemple de push web envoyé par Braze.

Les utilisateurs de votre application web doivent opter pour recevoir un push web. Voir ci-dessous.

!\[web-push-optin\]\[13\]

Pour plus d'informations sur les normes du protocole push et le support du navigateur, vous pouvez consulter les ressources de [Apple][3] [Mozilla][1] et [Microsoft][2]

{% alert important %}
Les fenêtres de navigation privée ne prennent actuellement pas en charge le push web.
{% endalert %}

## Règles de livraison

Par défaut, une campagne contenant un message dans l'application enverra un message web dans l'application ainsi qu'un message mobile dans l'application. Pour envoyer un message intégré exclusivement au web ou au mobile, vous devrez segmenter votre campagne en conséquence.

## Segmentation pour les utilisateurs web

Vous pouvez créer un segment de vos utilisateurs web en sélectionnant uniquement l'icône de l'application de votre site Web dans la section Apps utilisées.

!\[web-users-segment\]\[10\]

Cela vous permettra de cibler les utilisateurs en fonction de leur comportement sur le web seulement. Si vous voulez cibler les utilisateurs web afin de les encourager à télécharger votre application mobile, vous devriez créer ce segment en tant que public cible. Si vous voulez envoyer une campagne de messagerie qui inclut un message mobile dans l'application mais pas un message web il vous suffit de décocher l’icône de votre site Web dans votre segment.
[7]: {% image_buster /assets/img_archive/web-app-group.png %} [10]: {% image_buster /assets/img_archive/web-users-segment. ng %} [12]: {% image_buster /assets/img_archive/Macbook_Push.png %} [13]: {% image_buster /assets/img_archive/WebPush_Prompt.png %}

[1]: https://developer.mozilla.org/en-us/docs/web/api/push_api#browser_compatibility
[2]: https://developer.microsoft.com/en-us/microsoft-edge/status/pushapi/
[3]: https://developer.apple.com/notifications/safari-push-notifications/
[6]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/
[8]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/
[11]: {{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message
