---
nav_title: Désinstaller le suivi
article_title: Désinstaller le suivi pour Android/FireOS
platform:
  - Android
  - Pare-feu
page_order: 7
description: "Cet article explique comment configurer le suivi de désinstallation pour votre application Android."
---

# Désinstaller le suivi pour Android/FireOS

Désinstaller le suivi utilise un push silencieux de Firebase Cloud Messaging pour détecter les périphériques désinstallés. Cependant, si l'application est toujours installée, alors ce push silencieux est reçu par votre application. Démarrage dans Braze Android SDK v3.1. , nous lâcherons intelligemment la notification de suivi de désinstallation et ne réveillerons aucun récepteur de diffusion personnalisé dans votre application avec l'intention de push en mode silencieux.

Si vous souhaitez détecter si la notification push est le suivi de désinstallation vous-même, veuillez utiliser [`isUninstallTrackingPush()`]().

{% alert important %}
Notez que comme la désinstallation du tracking silencieux n'est pas transmise à votre récepteur de diffusion personnalisé, cette méthode ne peut être utilisée qu'avant que la notification push ne soit passée à Braze, comme lors de l'utilisation d'un [Firebase Messaging Service]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#step-1-register-braze-firebase-messaging-service) personnalisé.
{% endalert %}

Si vous avez une sous-classe personnalisée [`Application`][1] , assurez-vous que vous n'avez pas de logique automatique qui pince vos serveurs dans votre application [`. nCreate()`][2] méthode du cycle de vie. Ceci est dû au fait que le push silencieux réveillera votre application et instanciera le composant [`Application`][1] si l'application n'est pas déjà en cours d'exécution.

Pour plus d'informations, reportez-vous à la page [Désinstaller Tracking][4] de notre Guide d'utilisation.

[1]: https://developer.android.com/reference/android/app/Application
[2]: https://developer.android.com/reference/android/app/Application#onCreate()
[4]: {{site.baseurl}}/user_guide/data_and_analytics/tracking/uninstall_tracking/#uninstall-tracking
