## À propos des notifications push pour Android TV

![]({% image_buster /assets/img/Television.png %}){: style="float:right;max-width:25%;margin-left:15px; border: 0"}

Bien qu’il ne s’agisse pas d’une fonctionnalité native, l’intégration d’une notification push pour Android TV est rendue possible en exploitant le SDK Braze pour Android et la messagerie cloud Firebase pour enregistrer un jeton de notification push pour Android TV. Il est cependant nécessaire de construire une interface utilisateur pour afficher la charge utile de la notification après sa réception.

## Conditions préalables

Pour utiliser cette fonctionnalité, vous devez effectuer les opérations suivantes :

- [Intégrer le SDK Android de Braze]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android)
- [Configurer les notifications push pour le SDK Android de Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/?tab=android)

## Mise en place des notifications push

Pour configurer les notifications push pour Android TV :

1. Créez une vue personnalisée dans votre application pour afficher vos notifications.
2. Créez une [usine de notification personnalisée]({{site.baseurl}}/developer_guide/push_notifications/customization#customization-display). Elle remplacera le comportement SDK par défaut et vous permet d’afficher manuellement les notifications. En retournant `null`, elle empêchera le SDK de la traiter et nécessitera un code personnalisé pour afficher la notification. Après avoir terminé ces étapes, vous pouvez commencer à envoyer des notifications push à Android TV !<br><br>
3. (Facultatif) Pour un suivi efficace de l'analyse/analytique des clics, configurez le suivi de l'analyse/analytique des clics. Cela peut être réalisé en créant un [callback de push]({{site.baseurl}}/developer_guide/push_notifications/customization#push-callback) pour écouter les intentions de push ouvertes et reçues de Braze.

{% alert note %}
Ces notifications **ne persistent pas** et ne sont visibles pour l'utilisateur que lorsque l'appareil les affiche. Ceci est dû au centre de notification d’Android TV qui ne prend pas en charge les notifications historiques.
{% endalert %} 

## Tester les notifications push d'Android TV

Pour tester si votre implémentation de notification push est réussie, envoyez une notification depuis le tableau de bord de Braze comme vous le feriez normalement pour un appareil Android.

- **Si l'application est fermée** Le message push affichera une notification de toast à l'écran.
- **Si l'application est ouverte**: Vous avez la possibilité d’afficher le message dans votre propre IU hébergée. Nous vous recommandons de suivre le style IU de nos messages in-app du SDK Android Mobile.

## Bonnes pratiques

Pour les marketeurs utilisant Braze, lancer une campagne vers Android TV sera identique à lancer un push vers les applications mobiles Android. Pour cibler exclusivement ces appareils, nous vous recommandons de sélectionner l’application Android TV dans la segmentation.

La réponse fournie et cliquée retournée par FCM suivra la même convention que l’appareil mobile Android. Par conséquent, toute erreur sera visible dans le journal des activités du message.
