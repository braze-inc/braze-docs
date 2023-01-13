---
nav_title: SDK Web
article_title: Présentation du SDK Web
page_order: 3

page_type: reference
description: "Le présent article de référence d’onboarding couvre le SDK Web de Braze."

---

# SDK Web

![Liste des applications dans l’onglet Paramètres de la page Manage Settings][7]{: style="float:right;max-width:30%;max-height:30vw;margin-left:15px;"}

Avec le SDK Web de Braze, vous pouvez collecter des données de session, identifier les utilisateurs (avec le même ensemble d’attributs que sur nos autres plates-formes), enregistrer des achats et des événements personnalisés via un navigateur Web/mobile. La mise en œuvre du SDK Web de Braze vous permet d’obtenir une vue plus complète de vos utilisateurs sur les canaux Web et mobiles. Vous pouvez également utiliser le SDK Web pour interagir avec vos utilisateurs en envoyant des messages Web et des notifications push Web.

## Implémentation

Pour plus d’informations sur l’intégration du SDK de Braze Web, voir [Configuration initiale SDK pour le Web][6]. Après la mise en œuvre du SDK Web, votre site Internet apparaîtra comme une application dans votre groupe d'apps et sera regroupé avec vos applications mobiles.

## Communication web In-App

Vous pouvez envoyer des communications Web à des utilisateurs directement dans leur navigateur Web/mobile. Les messages Web sont envoyés sous forme de messages dans l’application et peuvent également être envoyés sous forme de glissières, modales ou en plein écran. Pour plus d’informations sur la composition d’un message dans l’application, consultez notre page sur [créer un message dans l’application][8].

## Notification Push Web

![Notification push affichée sur un navigateur Web par rapport à un appareil mobile][12]{: style="float:right;max-width:60%;margin-left:15px;border:0;"}

La notification push Web est un autre excellent moyen d’interagir avec les utilisateurs de votre application Web. Les clients qui visitent votre site Internet via Chrome, Safari, Firefox et Opera peuvent s’abonner pour recevoir une notification push Web à partir de votre application Web, que la page Web soit chargée ou non. 

Cette fonctionnalité est également prise en charge sur Android Chrome et Firefox Mobile sur Android, ce qui permet des notifications Web mobiles. Le push Web fonctionne de la même façon que les notifications push de l’application fonctionnent sur votre téléphone. Pour plus d’informations sur la composition d’une notification push Web, consultez notre page sur [créer une notification push][11].

Les utilisateurs de votre application Web doivent s’abonner pour recevoir une notification push Web. 

![Notification système demandant des autorisations de notification push][13]

Pour plus d’informations sur les normes de protocole de notification push et le support du navigateur, vous pouvez consulter les ressources d’[Apple][3] [Mozilla][1] et [Microsoft][2]

{% alert important %}
Les fenêtres de navigation privées ne prennent pas en charge la notification push Web.
{% endalert %}

## Règles de livraison

Par défaut, une campagne contenant un message dans l’application envoie un message Web dans l’application ainsi qu’un message mobile dans l’application. Pour envoyer un message in-app exclusivement sur Internet ou mobile, vous devez segmenter votre campagne en conséquence.

## Segmentation des utilisateurs Web

Vous pouvez créer un segment de vos utilisateurs Web en sélectionnant uniquement l’icône de l’application de votre site Internet dans la section **Applications utilisées** d’un segment.

![Page Détails du segment avec application Web sélectionnée][10]

Cela vous permet de cibler les utilisateurs en fonction de leur comportement sur le Web uniquement. Si vous souhaitez cibler des utilisateurs Web pour les encourager à télécharger votre application mobile, vous pouvez créez ce segment comme votre public cible. Si vous souhaitez envoyer une campagne de messagerie qui comprend un messages in-app mobiles mais pas un message Web, il suffit de décocher l’icône de votre site Internet dans votre segment.

[1]: https://developer.mozilla.org/en-us/docs/web/api/push_api#browser_compatibility "Mozilla Push API browser compatibility"
[2]: https://developer.microsoft.com/en-us/microsoft-edge/status/pushapi/ "Microsoft Push API"
[3]: https://developer.apple.com/notifications/safari-push-notifications/ "Safari Push Notifications"
[6]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/
[7]: {% image_buster /assets/img_archive/app_group_list.png %}
[8]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/
[10]: {% image_buster /assets/img_archive/web-users-segment.png %}
[11]: {{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message
[12]: {% image_buster /assets/img_archive/Macbook_Push.png %}
[13]: {% image_buster /assets/img_archive/WebPush_Prompt.png %}
