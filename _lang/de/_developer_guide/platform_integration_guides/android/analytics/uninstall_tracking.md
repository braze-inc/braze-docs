---
nav_title: Uninstall-Tracking
article_title: Tracking für Android und FireOS deinstallieren
platform: 
  - Android
  - FireOS
page_order: 7
description: "Dieser Artikel beschreibt, wie Sie die Deinstallationsverfolgung für Ihre Android- oder FireOS-Anwendung konfigurieren."

---

# Uninstall-Tracking

> Das Uninstall-Tracking verwendet eine stille Push-Benachrichtigung von Firebase Cloud Messaging, um deinstallierte Geräte zu erkennen. Die Uninstall-Tracking-Benachrichtigung wird auf intelligente Weise übermittelt, ohne angepasste Push-Callbacks in Ihrer App auszulösen. Dieser Artikel beschreibt, wie Sie die Deinstallationsverfolgung für Ihre Android- oder FireOS-Anwendung konfigurieren.

Um festzustellen, ob Sie selbst eine Push-Benachrichtigung zum Uninstall-Tracking erhalten, verwenden Sie [`isUninstallTrackingPush()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.push/-braze-notification-utils/is-uninstall-tracking-push.html).

{% alert important %}
Da die stille Push-Benachrichtigung zum Uninstall-Tracking nicht an Braze Push-Callbacks weitergeleitet wird, kann diese Methode nur verwendet werden, bevor die Push-Benachrichtigung an Braze übergeben wird (z. B. bei Verwendung eines angepassten [Firebase Messaging Dienstes]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-1-register-braze-firebase-messaging-service)).
{% endalert %}

Wenn Sie eine angepasste Unterklasse des Typs [`Application`](https://developer.android.com/reference/android/app/Application) haben, stellen Sie in der Lebenszyklus-Methode [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application#onCreate()) sicher, dass Ihre Server nicht durch eine automatische Logik angepingt werden. Der Grund hierfür ist, dass eine stille Push-Benachrichtigung Ihre App aufweckt und die Komponente `Application` instanziiert, wenn die App nicht bereits ausgeführt wird.

Weitere Informationen finden Sie unter [Tracking deinstallieren]({{site.baseurl}}/user_guide/data_and_analytics/tracking/uninstall_tracking/#uninstall-tracking) in unserem Benutzerhandbuch.

