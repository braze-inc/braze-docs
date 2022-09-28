---
nav_title: Notifications push silencieuses
article_title: Notifications Push silencieuses pour FireOS
platform: FireOS
page_order: 3

page_type: reference
description: "Cet article décrit comment envoyer des notifications push silencieuses à FireOS, ainsi que des cas d’usage potentiels lorsque des notifications push silencieuses peuvent être préférables."
channel: notification push

---

# Notifications push silencieuses

Les notifications silencieuses vous permettent d’informer votre application en arrière-plan lorsque des événements importants se produisent. Vous pourriez avoir de nouveaux messages instantanés à livrer, de nouveaux numéros d’un magazine à publier, des alertes de dernières nouvelles à envoyer ou le dernier épisode de l’émission télé préférée de votre utilisateur, prête à être téléchargé pour une visualisation hors-ligne. Les notifications silencieuses sont idéales pour le contenu sporadique mais important dans l’immédiat pour lequel le délai entre les recherches en arrière-plan peut ne pas être acceptable.

Des notifications silencieuses sont disponibles via l’[API de messagerie][2] de Braze. Pour en profiter, vous devez définir le signalement `send_to_sync` sur `true` au sein de l’[objet de notification push Android][3] et vous assurer qu’il n’y a pas de champs `title` ou `alert` définis car cela provoquerait des erreurs s’ils sont utilisés en parallèle de `send_to_sync`. Vous pouvez toutefois inclure les données `extras` dans l’objet.

Les notifications silencieuses sont également disponibles dans le tableau de bord. Pour envoyer une notification silencieuse, assurez-vous que les champs de titre et de corps de la notification sont vides comme illustré :

![][6]

Ce message entraînera la réception d’une intention avec une action `BRAZE_PUSH_INTENT_NOTIFICATION_RECEIVED`. Gérer cette intention en vue de provoquer une action, telle qu’une actualisation du contenu de l’application, doit être défini dans le récepteur de diffusion que vous avez défini pendant l’[intégration standard Android][4]. Consultez [CustomBroadcastReceiver.java][5] pour y trouver un exemple de ce récepteur.

[2]: {{site.baseurl}}/api/endpoints/messaging/
[3]: {{site.baseurl}}/api/objects_filters/messaging/android_object/
[4]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#custom-handling-for-push-receipts-opens-dismissals-and-key-value-pairs
[5]: https://github.com/Appboy/appboy-android-sdk/blob/master/samples/custom-broadcast/src/main/java/com/braze/custombroadcast/CustomBroadcastReceiver.java
[6]: {% image_buster /assets/img_archive/SilentPushExample.png %} "Silent Push Notification Example -- Android"
