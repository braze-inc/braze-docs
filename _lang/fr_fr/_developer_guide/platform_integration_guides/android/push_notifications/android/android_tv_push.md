---
nav_title: Notification push pour Android TV
article_title: Notification push pour Android TV
platform: Android
page_order: 8
description: "Cet article montre comment implémenter et tester une notification push pour Android TV."
channel:
  - push

---

# Notification push pour Android TV
![]({% image_buster /assets/img/Television.png %}){: style="float:right;max-width:25%;margin-left:15px; border: 0"}

> Bien qu’il ne s’agisse pas d’une fonctionnalité native, l’intégration d’une notification push pour Android TV est rendue possible en exploitant le SDK Braze pour Android et la messagerie cloud Firebase pour enregistrer un jeton de notification push pour Android TV. Il est cependant nécessaire de construire une interface utilisateur pour afficher la charge utile de la notification après sa réception.

## Mise en œuvre

1. **Intégrer le SDK Android de Braze**<br>
Tout d'abord, vous devez intégrer le [SDK Android de Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/?redirected=true) (si ce n'est pas déjà fait).<br><br>
2. **Intégrer les notifications push**<br>
Ensuite, vous devez intégrer [les notifications push Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/) (si ce n'est pas déjà fait).<br><br>
3. **Créer une vue Toast personnalisée**<br>
Ensuite, vous devrez créer une vue personnalisée pour afficher vos notifications dans l’application.<br><br>
4. **Créer une fabrique de notifications personnalisées**<br>
Enfin, vous devez créer une [fabrique de notifications personnalisées]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#custom-displaying-notifications). Elle remplacera le comportement SDK par défaut et vous permet d’afficher manuellement les notifications. En retournant `null`, elle empêchera le SDK de la traiter et nécessitera un code personnalisé pour afficher la notification. Après avoir terminé ces étapes, vous pouvez commencer à envoyer des notifications push à Android TV !<br><br>
5. **Configurer le suivi des analyses de clics (facultatif)**<br>
Pour effectuer un suivi efficace de l’analyse de clics, il est nécessaire de le gérer manuellement, car Braze ne gère pas automatiquement l’affichage des messages. Cela peut être réalisé en créant un [callback de push]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#android-push-listener-callback) pour écouter les intentions de push ouvertes et reçues de Braze.

{% alert note %}
Notez que ces notifications **ne persisteront pas** et ne seront visibles par l'utilisateur que lorsque l'appareil les affichera. Ceci est dû au centre de notification d’Android TV qui ne prend pas en charge les notifications historiques.
{% endalert %} 

## Comment tester la notification push sur Android TV

Pour tester si votre implémentation de notification push est réussie, envoyez une notification depuis le tableau de bord de Braze comme vous le feriez normalement pour un appareil Android.

- **Si l'application est fermée** Le message push affichera une notification de toast à l'écran.
- **Si l'application est ouverte**: Vous avez la possibilité d’afficher le message dans votre propre IU hébergée. Nous vous recommandons de suivre le style IU de nos messages in-app du SDK Android Mobile.

## Informations supplémentaires
Pour un utilisateur final marketing à Braze, le lancement d’une campagne vers Android TV sera identique au lancement d’une notification push vers des applications mobiles Android. Pour cibler exclusivement ces appareils, nous vous recommandons de sélectionner l’application Android TV dans la segmentation. 

La réponse fournie et cliquée retournée par FCM suivra la même convention que l’appareil mobile Android. Par conséquent, toute erreur sera visible dans le journal des activités du message.

