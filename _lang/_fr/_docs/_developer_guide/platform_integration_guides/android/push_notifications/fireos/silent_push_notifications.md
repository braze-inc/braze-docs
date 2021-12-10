---
nav_title: Notifications Push silencieuses
article_title: Notifications Push silencieuses pour FireOS
platform: Pare-feu
page_order: 3
page_type: Référence
description: "Cet article décrit comment envoyer des notifications push en mode silencieux, et les cas d'utilisation potentiels pour les notifications push silencieuses peuvent être préférables."
channel: Pousser
---

# Notifications push silencieuses

Les notifications silencieuses vous permettent de notifier votre application en arrière-plan lorsque des événements importants se produisent. Vous pourriez avoir de nouveaux messages instantanés à envoyer, de nouveaux numéros d'un magazine à publier, de nouvelles alertes à envoyer, ou le dernier épisode de la série TV préférée de votre utilisateur prête à être téléchargée pour une consultation hors ligne. Les notifications silencieuses sont idéales pour les contenus sporadiques mais immédiatement importants, où le délai entre les récupérations en arrière-plan pourrait ne pas être acceptable.

Les notifications silencieuses sont disponibles via notre [Messaging RESTful API][2]. Vous n'avez qu'à définir le drapeau `send_to_sync` à `true` dans le [Objet Push Android][3]. Vous devez vous assurer qu'il n'y a pas de champs `titre` ou `alerte` définis dans le [objet push Android][3] car cela causera des erreurs lorsque `send_to_sync` est réglé sur `true`. Vous pouvez cependant inclure des données `extras` dans l'objet [Android Push Object][3].

Des notifications silencieuses sont également disponibles dans le tableau de bord. Afin d'envoyer une notification silencieuse, vous devez seulement vous assurer que le titre et le corps de la notification sont vides comme illustré ci-dessous:

!\[Exemple Android silencieux\]\[6\]

Ce message entraînera la réception d'une intention avec une action `.intent.APPBOY_PUSH_RECEIVED`. La gestion de cette intention de causer toute action telle qu'une mise à jour du contenu de l'application doit être définie dans le récepteur de diffusion que vous avez défini dans [Étape 4 de l'activation des notifications push - Android][4]. Veuillez consulter [AppboyBroadcastReceiver.java][5] pour un exemple de ce récepteur.
[6]: {% image_buster /assets/img_archive/SilentPushExample.png %} "Exemple de notification silencieuse -- Android"

[2]: {{site.baseurl}}/api/endpoints/messaging/
[3]: {{site.baseurl}}/api/objects_filters/messaging/android_object/
[3]: {{site.baseurl}}/api/objects_filters/messaging/android_object/
[3]: {{site.baseurl}}/api/objects_filters/messaging/android_object/
[4]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-5-define-notification-channels
[5]: https://github.com/Appboy/appboy-android-sdk/blob/master/samples/custom-broadcast/src/main/java/com/appboy/custombroadcast/AppboyBroadcastReceiver.java "AppboyBroadcastReceiver.java -- Sample Project"
