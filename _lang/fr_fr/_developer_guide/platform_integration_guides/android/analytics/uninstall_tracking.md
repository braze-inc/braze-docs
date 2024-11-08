---
nav_title: Suivi des désinstallations
article_title: Désinstaller le suivi pour Android et FireOS
platform: 
  - Android
  - FireOS
page_order: 7
description: "Cet article montre comment désinstaller le suivi pour votre application Android ou FireOS."

---

# Suivi des désinstallations

> Le suivi des désinstallations utilise une notification push silencieuse de Firebase Cloud Messaging pour détecter les appareils désinstallés. Braze va supprimer intelligemment la notification de désinstallation de suivi et ne réveillera aucune fonction de rappel personnalisée dans votre application avec l’intention habituelle de notification push silencieuse. Cet article montre comment désinstaller le suivi pour votre application Android ou FireOS.

Si vous souhaitez détecter vous-même si la notification push assure le suivi des désinstallations, utilisez [`isUninstallTrackingPush()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.push/-braze-notification-utils/is-uninstall-tracking-push.html).

{% alert important %}
Étant donné que le push silencieux de suivi de désinstallation n'est transmis à aucun rappel de push de Braze, cette méthode ne peut être utilisée qu'avant que la notification push ne soit transmise à Braze, par exemple lors de l'utilisation d'un [service d'envoi de messages Firebase]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-1-register-braze-firebase-messaging-service) personnalisé.
{% endalert %}

Si vous avez une sous-classe [`Application`](https://developer.android.com/reference/android/app/Application) personnalisée, assurez-vous de ne pas avoir de logique automatique qui sonde par PING vos serveurs dans votre méthode de cycle de vie [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application#onCreate()). C’est parce qu’une notification push silencieuse réveillera votre application et instanciera le composant `Application` si l’application n’est pas déjà en cours d’exécution.

Pour plus d'informations, consultez la section [Désinstaller le suivi]({{site.baseurl}}/user_guide/data_and_analytics/tracking/uninstall_tracking/#uninstall-tracking) dans notre guide de l'utilisateur.

