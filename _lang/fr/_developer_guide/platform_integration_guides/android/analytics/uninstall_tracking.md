---
nav_title: Suivi des désinstallations
article_title: Désinstaller le suivi pour Android et FireOS
platform: 
  - Android
  - FireOS
page_order: 7
description: "Cet article montre comment désinstaller le suivi pour votre application Android ou FireOS."

---

# Désinstaller le suivi pour Android et FireOS

La désinstallation du suivi utilise une notification push silencieuse de Firebase Cloud Messaging pour détecter les périphériques non installés. Braze va supprimer intelligemment la notification de désinstallation de suivi et ne réveillera aucune fonction de rappel personnalisée dans votre application avec l’intention habituelle de notification push silencieuse.

Si vous souhaitez détecter vous-mêmes si la notification push est en train de désinstaller le suivi, utilisez [`isUninstallTrackingPush()`][3].

{% alert important %}
Puisque la notification push silencieuse de désinstallation de suivi n’est pas transmise à toute fonction de rappel personnalisée, cette méthode peut être utilisée uniquement avant la transmission de la notification push à Braze, comme lors de l’utilisation d’un [Firebase Messaging Service]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-1-register-braze-firebase-messaging-service) personnalisé.
{% endalert %}

Si vous avez une sous-classe [`Application`][1] personnalisée, assurez-vous que vous n’avez pas de logique automatique qui pingue vos serveurs dans votre méthode de cycle de vie [`Application.onCreate()`][2]. C’est parce qu’une notification push silencieuse réveillera votre application et instanciera le composant `Application` si l’application n’est pas déjà en cours d’exécution.

Consultez [Désinstaller le suivi][4] dans notre guide de l’utilisateur pour plus d’informations.

[1]: https://developer.android.com/reference/android/app/Application
[2]: https://developer.android.com/reference/android/app/Application#onCreate()
[3]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.push/-braze-notification-utils/is-uninstall-tracking-push.html
[4]: {{site.baseurl}}/user_guide/data_and_analytics/tracking/uninstall_tracking/#uninstall-tracking
