---
nav_title: Desinstalar seguimiento
article_title: Uninstall Tracking para Android y FireOS
platform: 
  - Android
  - FireOS
page_order: 7
description: "Este artículo explica cómo configurar Uninstall Tracking para tu aplicación Android o FireOS."

---

# Uninstall Tracking

> Uninstall Tracking utiliza un push silencioso de Firebase Cloud Messaging para detectar los dispositivos desinstalados. Braze eliminará de forma inteligente la notificación de seguimiento Uninstall Tracking y no despertará ninguna devolución de llamada push personalizada en tu aplicación con la intención push silenciosa habitual. Este artículo explica cómo configurar Uninstall Tracking para tu aplicación Android o FireOS.

Si quieres detectar tú mismo si la notificación push es de seguimiento de desinstalación, utiliza [`isUninstallTrackingPush()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.push/-braze-notification-utils/is-uninstall-tracking-push.html).

{% alert important %}
Dado que el push silencioso de Uninstall Tracking no se reenvía a ninguna devolución de llamada push de Braze, este método solo puede utilizarse antes de que la notificación push se pase a Braze, como cuando se utiliza un [servicio de mensajería personalizado de Firebase]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-1-register-braze-firebase-messaging-service).
{% endalert %}

Si tienes una subclase personalizada de [`Application`](https://developer.android.com/reference/android/app/Application) asegúrate de no tener una lógica automática que haga ping a tus servidores en el método [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application#onCreate()) método del ciclo de vida. Esto se debe a que un push silencioso despertará tu aplicación e instanciará el componente`Application` si la aplicación no se está ejecutando todavía.

Para más información, consulta [Uninstall Tracking]({{site.baseurl}}/user_guide/data_and_analytics/tracking/uninstall_tracking/#uninstall-tracking) en nuestra Guía del usuario.

