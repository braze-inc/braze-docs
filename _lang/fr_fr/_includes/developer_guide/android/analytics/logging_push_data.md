## Enregistrement des données avec l'API de Braze (recommandé)

Vous pouvez enregistrer des analyses/analytiques en temps réel en effectuant des appels vers l'[endpoint`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/). Pour l'analyse/analytique, envoyez la valeur `braze_id` depuis le tableau de bord de Braze afin d'identifier le profil utilisateur à mettre à jour.

![Exemple de tableau de bord personnalisé]({% image_buster /assets/img/push_implementation_guide/android_braze_id_configuration.png %}){: style="max-width:79%;"}

## Enregistrement manuel des données

En fonction des détails de votre charge utile, vous pouvez enregistrer les analyses/analytiques manuellement dans votre implémentation `FirebaseMessagingService.onMessageReceived` ou dans votre activité de démarrage. N'oubliez pas que votre sous-classe `FirebaseMessagingService` doit terminer son exécution dans les 9 secondes suivant l'invocation pour éviter d'être [signalée ou interrompue](https://firebase.google.com/docs/cloud-messaging/android/receive) par le système Android.
