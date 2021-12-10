---
nav_title: Notifications Push silencieuses
article_title: Notifications Push silencieuses pour Android
platform: Android
page_order: 3
description: "Cet article couvre comment implémenter les notifications push silencieuses dans votre application Android."
channel:
  - Pousser
---

# Notifications push silencieuses

Les notifications silencieuses vous permettent de notifier votre application en arrière-plan lorsque des événements importants se produisent. Vous pourriez avoir de nouveaux messages instantanés à envoyer, de nouveaux numéros d'un magazine à publier, de nouvelles alertes à envoyer, ou le dernier épisode de la série TV préférée de votre utilisateur prête à être téléchargée pour une consultation hors ligne. Les notifications silencieuses sont idéales pour les contenus sporadiques mais immédiatement importants, où le délai entre les récupérations en arrière-plan pourrait ne pas être acceptable.

Les notifications silencieuses sont disponibles via notre [Messaging RESTful API][2]. Vous n'avez qu'à définir le drapeau `send_to_sync` à `true` dans le [Objet Push Android][3]. Vous devez vous assurer qu'il n'y a pas de champs `titre` ou `alerte` définis dans le [objet push Android][3] car cela causera des erreurs lorsque `send_to_sync` est réglé sur `true`. Vous pouvez cependant inclure des données `extras` dans l'objet [Android Push Object][3].

Des notifications silencieuses sont également disponibles dans le tableau de bord. Pour envoyer une notification silencieuse, vous devez seulement vous assurer que les champs titre et corps de la notification sont vides comme illustré ci-dessous :

!\[Exemple Android silencieux\]\[6\]

Ce message entraînera la réception d'une intention avec une action `BRAZE_PUSH_INTENT_NOTIFICATION_RECEIVED`. La gestion de cette intention de causer toute action telle qu'une actualisation du contenu de l'application doit être définie dans le récepteur de diffusion que vous avez défini lors de l'intégration [Android standard][4]. Veuillez consulter [CustomBroadcastReceiver.java][5] pour un exemple de ce récepteur.
[6]: {% image_buster /assets/img_archive/SilentPushExample.png %} "Exemple de notification silencieuse -- Android"

[2]: {{site.baseurl}}/api/endpoints/messaging/
[3]: {{site.baseurl}}/api/objects_filters/messaging/android_object/
[3]: {{site.baseurl}}/api/objects_filters/messaging/android_object/
[3]: {{site.baseurl}}/api/objects_filters/messaging/android_object/
[4]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#custom-handling-for-push-receipts-opens-dismissals-and-key-value-pairs
[5]: https://github.com/Appboy/appboy-android-sdk/blob/master/samples/custom-broadcast/src/main/java/com/braze/custombroadcast/CustomBroadcastReceiver.java
