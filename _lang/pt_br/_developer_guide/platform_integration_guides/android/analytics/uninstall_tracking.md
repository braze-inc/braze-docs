---
nav_title: Uninstall Tracking
article_title: Desinstalar rastreamento para Android e FireOS
platform: 
  - Android
  - FireOS
page_order: 7
description: "Este artigo aborda como configurar o rastreamento de desinstalação para seu aplicativo Android ou FireOS."

---

# Desinstalar rastreamento

> O rastreamento de desinstalação usa um push silencioso do Firebase Cloud Messaging para detectar dispositivos desinstalados. Braze irá descartar inteligentemente a notificação de rastreamento de desinstalação e não ativará nenhum callback de push personalizado no seu app com a intenção de push silenciosa regular. Este artigo aborda como configurar o rastreamento de desinstalação para seu aplicativo Android ou FireOS.

Se você deseja detectar se a notificação por push é rastreamento de desinstalação, use [`isUninstallTrackingPush()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.push/-braze-notification-utils/is-uninstall-tracking-push.html).

{% alert important %}
Como o rastreamento de desinstalação push silencioso não é encaminhado para nenhum callback de push da Braze, este método só pode ser usado antes que a notificação por push seja passada para a Braze, como ao usar um serviço de envio de mensagens [Firebase]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-1-register-braze-firebase-messaging-service) personalizado.
{% endalert %}

Se você tiver uma [`Application`](https://developer.android.com/reference/android/app/Application) subclasse personalizada, certifique-se de não ter lógica automática que pinge seus servidores em seu método de ciclo de vida [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application#onCreate()). Isso ocorre porque um push silencioso acordará seu app e instanciará o componente `Application` se o app não estiver em execução.

Consulte [Rastreamento de Desinstalação]({{site.baseurl}}/user_guide/data_and_analytics/tracking/uninstall_tracking/#uninstall-tracking) em nosso Guia do Usuário para saber mais.

