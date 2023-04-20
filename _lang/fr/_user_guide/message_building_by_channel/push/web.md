---
nav_title: "Notification push Web"
article_title: Notifications push Web
page_order: 8.5
page_type: reference
description: "Cette page de référence couvre brièvement les notifications push pour Web et relie les étapes nécessaires à leur création."
platform: Web
channel:
  - Notification push

---

# Push Web

> Les notifications push pour Web sont un autre excellent moyen d’interagir avec les utilisateurs de votre application Web. Les clients qui visitent votre site Internet via Chrome, Safari, Firefox et Opera peuvent choisir de recevoir des notifications push pour Web à partir de votre application Web, que la page Web soit chargée ou non. Cette fonctionnalité est également prise en charge sur Android Chrome et Firefox Mobile sur Android, ce qui permet des notifications Web mobiles. 

Les notifications push pour Web fonctionnent de la même façon que les notifications push de l’application sur votre téléphone. Pour plus d’informations sur la composition d’une notification push pour Web, consultez [Création d’une notification push][11].

![Exemple de notification push pour Web avec le même message push affiché sur un ordinateur portable et un téléphone.][12]

Les utilisateurs de votre application Web doivent autoriser la réception des notifications push pour Web. 

![Exemple d’abonnement aux notifications push pour Web pour Safari avec deux boutons : Don't Allow (Bloquer) et Allow (Autoriser).][13]

Pour plus d’informations sur les normes de protocole de notifications push et la prise en charge du navigateur, vous pouvez consulter les ressources de votre navigateur :
- [Apple][3]
- [Mozilla][1]
- [Microsoft][2]

{% alert important %}
Les fenêtres de navigation privées ne prennent pas en charge la notification push Web.
{% endalert %}

[1]: https://developer.mozilla.org/en-us/docs/web/api/push_api#browser_compatibility
[2]: https://developer.microsoft.com/en-us/microsoft-edge/status/pushapi/
[3]: https://developer.apple.com/notifications/safari-push-notifications/
[11]: {{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message
[12]: {% image_buster /assets/img_archive/Macbook_Push.png %}
[13]: {% image_buster /assets/img_archive/WebPush_Prompt.png %}
