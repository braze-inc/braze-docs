---
nav_title: Push Android TV
article_title: Push Android TV
platform: Android
page_order: 8
description: "Cet article montre comment implémenter et tester Android TV Push."
channel:
  - Pousser
---

# Push Android TV
!\[TV icon\]\[12\]{: style="float:right;max-width:25%;margin-left:15px; border: 0"}

Bien que pas une fonctionnalité native, L'intégration Push d'Android TV est rendue possible en exploitant le SDK Braze Android et la Messagerie Firebase Cloud pour enregistrer un jeton push pour Android TV. Il est toutefois nécessaire de construire une interface utilisateur pour afficher la charge utile de notification une fois qu'elle est reçue. Les étapes à suivre sont détaillées ci-dessous.

## Implémentation
- __Étape 1 : Intégrez Braze Android SDK__<br> Tout d'abord, vous devez intégrer le [Braze Android SDK][6] (si ce n'est pas déjà terminé).<br><br>
- __Étape 2 : Intégrer les notifications push__<br> Ensuite, vous devez intégrer les [notifications push Android][10] (Si pas déjà terminé).<br><br>
- __Étape 3: Créez une vue Toast personnalisée__<br> Ensuite, vous devrez créer une vue toast personnalisée pour que l'application affiche vos notifications. Veuillez vous référer à [la documentation Google][9] sur la façon de procéder.<br><br>
- __Étape 4: Créez une Facture de Notification Personnalisée__<br> Enfin, vous devez créer une usine de notification personnalisée. Ceci sera utilisé pour remplacer le comportement par défaut du SDK et vous permettra d'afficher manuellement les notifications. En retournant `null`, cela empêchera le SDK de traiter et nécessitera un code personnalisé pour afficher la notification. Veuillez consulter notre documentation [Braze][8] qui décrit comment faire cela.

Une fois ces étapes terminées, vous pouvez commencer à envoyer des messages push sur Android TV !

- __Étape 5 (Optionnel) : Configurer le suivi des clics__<br> Pour suivre efficacement l'analyse des clics, Il est nécessaire de le gérer manuellement, car Braze ne gère pas automatiquement l'affichage des messages. Cela peut être réalisé en créant un `BroadcastReceiver personnalisé` pour écouter les intentions ouvertes et reçues de Braze. Des détails sur la façon de configurer cela peuvent être trouvés dans la [documentation][7].

Notez que ces notifications __ne persisteront pas__ et ne seront visibles que par l'utilisateur au moment où l'appareil les affiche. Ceci est dû au centre de notification d'Android TV ne prenant pas en charge les notifications historiques.

## Comment tester push sur Android TV

Pour tester si votre implémentation de push est réussie, envoyez une notification depuis le tableau de bord Braze comme vous le feriez normalement pour un appareil Android.

- __Si l'application est fermée__: Le message Push affichera une notification toast dans le coin de l'écran. !\[Exemple Push Android TV\]\[11\]
- __Si l'application est ouverte__: vous avez la possibilité d'afficher le message dans votre propre interface utilisateur hébergée, Nous vous recommandons de suivre le style de l'interface utilisateur de nos messages Android Mobile SDK dans l'application.

## Informations complémentaires
Pour un utilisateur de marketing au Brésil, lancer une campagne sur Android TV sera identique au lancement d'une application Push to Android Mobile, pour cibler exclusivement ces appareils, nous vous recommandons de sélectionner l'application __Android TV dans la segmentation__.

La réponse livrée/cliquée retournée par FCM suivra la même convention qu'un appareil mobile Android, par conséquent, toutes les erreurs seront visibles dans le journal d'activité des messages.
[11]: {% image_buster /assets/img/android_tv.png %} [12]: {% image_buster /assets/img/Télévision.png %}

[6]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/?redirected=true
[7]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#custom-handling-for-push-receipts-opens-dismissals-and-key-value-pairs
[8]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#custom-displaying-notifications
[9]: https://developer.android.com/guide/topics/ui/notifiers/toasts#CustomToastView
[10]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/
