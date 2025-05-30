## Mise en place d'un suivi des désinstallations

### Étape 1 : Mise en place du FCM

Le SDK Android Braze utilise Firebase Cloud Messaging (FCM) pour envoyer des notifications push silencieuses, qui sont utilisées pour collecter des analyses/analytiques de suivi de désinstallation. Si ce n'est pas déjà fait, [configurez]({{site.baseurl}}/developer_guide/platforms/android/push_notifications/#setting-up-push-notifications) ou [migrez vers l']({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android) API Firebase Cloud Messaging pour les notifications push.

### Étape 2 : Détecter manuellement le suivi des désinstallations (facultatif)

Par défaut, le SDK Android Braze détectera et ignorera automatiquement les notifications push silencieuses liées au suivi de la désinstallation. Cependant, vous choisissez de détecter manuellement le suivi de la désinstallation à l'aide de la méthode [`isUninstallTrackingPush()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.push/-braze-notification-payload/is-uninstall-tracking-push.html) méthode.

{% alert important %}
Étant donné que les notifications silencieuses pour le suivi de la désinstallation ne sont transmises à aucun rappel push de Braze, vous ne pouvez utiliser cette méthode qu'avant de transmettre une notification push à Braze.
{% endalert %}

### Étape 3 : Suppression des pings automatiques vers le serveur

Une notification push silencieuse réveillera votre application et instanciera le composant `Application` si l'application n'est pas déjà en cours d'exécution. Ainsi, si vous avez une sous-classe personnalisée de [`Application`](https://developer.android.com/reference/android/app/Application) personnalisée, supprimez toute logique qui interroge automatiquement vos serveurs au cours de votre méthode de cycle de vie [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application#onCreate()) au cours de votre méthode de cycle de vie.

### Étape 4 : Activer le suivi de désinstallation

Enfin, activez le suivi des désinstallations dans Braze. Pour une description complète, voir [Activer le suivi de la désinstallation]({{site.baseurl}}/user_guide/data_and_analytics/tracking/uninstall_tracking/#uninstall-tracking).

{% alert important %}
Le suivi des désinstallations peut être imprécis. Les indicateurs que vous voyez sur Braze peuvent être retardés ou inexacts.
{% endalert %}
