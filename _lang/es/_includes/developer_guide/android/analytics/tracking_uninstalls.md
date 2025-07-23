## Configuración de Uninstall Tracking

### Paso 1: Configurar el FCM

El SDK de Android Braze utiliza Firebase Cloud Messaging (FCM) para enviar notificaciones push silenciosas, que se utilizan para recopilar análisis de seguimiento de desinstalaciones. Si aún no lo has hecho, [configura]({{site.baseurl}}/developer_guide/platforms/android/push_notifications/#setting-up-push-notifications) o [migra a]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android) la API de mensajería en la nube de Firebase para las notificaciones push.

### Paso 2: Detectar manualmente el seguimiento de Uninstall Tracking (opcional)

De forma predeterminada, el SDK de Android Braze detectará e ignorará automáticamente las notificaciones push silenciosas relacionadas con el Uninstall Tracking. Sin embargo, elige detectar manualmente el seguimiento de la desinstalación mediante el método [`isUninstallTrackingPush()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.push/-braze-notification-payload/is-uninstall-tracking-push.html) método.

{% alert important %}
Como las notificaciones silenciosas para el seguimiento de desinstalación no se reenvían a ninguna devolución de llamada push de Braze, sólo puedes utilizar este método antes de pasar una notificación push a Braze.
{% endalert %}

### Paso 3: Eliminar los pings automáticos del servidor

Una notificación push silenciosa activará tu aplicación e instanciará el componente `Application` si la aplicación no se está ejecutando todavía. Por lo tanto, si tienes una subclase personalizada de [`Application`](https://developer.android.com/reference/android/app/Application) personalizada, elimina cualquier lógica que haga ping automáticamente a tus servidores durante su [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application#onCreate()) método del ciclo de vida.

### Paso 4: Habilitar el seguimiento de Uninstall Tracking

Por último, habilita el Uninstall Tracking en Braze. Para obtener un tutorial completo, consulta [Habilitar el seguimiento de desinstalación]({{site.baseurl}}/user_guide/data_and_analytics/tracking/uninstall_tracking/#uninstall-tracking).

{% alert important %}
El seguimiento de las desinstalaciones puede ser impreciso. Las métricas que ves en Braze pueden sufrir retrasos o ser inexactas.
{% endalert %}
