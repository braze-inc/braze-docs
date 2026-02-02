---
nav_title: "Options de notification"
article_title: Options de notification Android
page_order: 2
page_type: reference
description: "Le présent article de référence couvre plusieurs options de notification Android et comment les utiliser au mieux dans les campagnes Braze."

platform: Android
channel:
  - Push

---

# Options de notification

> Voici quelques-unes des options de notification push spécifiques à Android disponibles via Braze.

## Notifications silencieuses

Lorsque vous [composez votre message de notification push]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/?tab=android#step-4-compose-your-push-message), vous **ne pouvez pas** envoyer un message push Android sans titre - toutefois, vous pouvez saisir un seul espace à la place. Gardez à l'esprit que si votre message ne contient qu'un seul espace, il sera envoyé sous forme de notification push silencieuse. Pour plus d'informations, voir [Notifications push silencieuses]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android).

## Groupes de notification

Si vous souhaitez catégoriser vos messages et les regrouper dans la zone de notification de votre utilisateur, vous pouvez utiliser la fonction de canaux de notification d’Android via Braze.

Tout d'abord, créez votre campagne push Android, puis regardez en haut de l'onglet **Composer** pour le menu déroulant **Canal de notification.** 

![]({% image_buster /assets/img_archive/notification_channel_dropdown.png %}){: style="max-width:60%;"}

Sélectionnez votre canal de notification dans la liste déroulante. Vous devez également sélectionner un canal de secours en cas de dysfonctionnement de votre paramètre de canal de notification.

Si aucun [canal de notification]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/notification_channels/) n'est répertorié ici, vous pouvez en ajouter un en utilisant l'ID du canal de notification. Contactez vos développeurs pour trouver quels sont vos ID de canal de notification ou pour en créer de nouveaux si besoin. 

Pour ajouter un ID de notification à votre canal de notification, cliquez sur **Gestion du canal de notification** dans le menu déroulant du **canal de notification** et remplissez les champs requis. Les canaux de notification doivent être définis sur l’application avant de pouvoir être utilisés sur la plateforme Braze.

![]({% image_buster /assets/img_archive/notification_channels.png %}){: style="max-width:80%;" }


