## Sobre el ciclo de vida de la sesión

Una sesión se refiere al periodo de tiempo durante el cual el SDK de Braze realiza un seguimiento de la actividad del usuario en tu aplicación después de su lanzamiento. También puedes forzar una nueva sesión [llamando al método `changeUser()` ]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/#setting-a-user-id).

{% tabs %}
{% tab Android %}
{% alert note %}
Si has configurado la [devolución de llamada del ciclo de vida de la actividad]({{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-4-tracking-user-sessions-in-android) para Android, Braze llamará automáticamente a [`openSession()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/open-session.html) y [`closeSession()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/close-session.html) para cada actividad de tu aplicación.
{% endalert %}

Por defecto, una sesión se inicia cuando se llama por primera vez a `openSession()`. Si tu aplicación pasa a segundo plano y luego vuelve a primer plano, el SDK comprobará si han transcurrido más de 10 segundos desde que se inició la sesión (a menos que [cambies el tiempo de espera predeterminado de la sesión]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=android#change-session-timeout)). Si es así, comenzará una nueva sesión. Ten en cuenta que si el usuario cierra tu aplicación mientras está en segundo plano, es posible que los datos de la sesión no se envíen a Braze hasta que vuelva a abrir la aplicación.

Si llamas a `closeSession()`, la sesión no finalizará inmediatamente. En cambio, finalizará la sesión al cabo de 10 segundos si el usuario no vuelve a llamar a `openSession()` para iniciar otra actividad.
{% endtab %}

{% tab swift %}
Por defecto, una sesión se inicia cuando llamas a `Braze.init(configuration:)`. Esto ocurre cuando se desencadena la notificación `UIApplicationWillEnterForegroundNotification`, lo que significa que la aplicación ha pasado a primer plano.

Si tu aplicación pasa a segundo plano, se desencadenará `UIApplicationDidEnterBackgroundNotification`. Cuando tu aplicación vuelva al primer plano, el SDK comprobará si han pasado más de 10 segundos desde que se inició la sesión (a menos que [cambies el tiempo de espera predeterminado de la sesión]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=swift#change-session-timeout)). Si es así, comenzará una nueva sesión.
{% endtab %}

{% tab web %}
Por defecto, una sesión se inicia cuando llamas por primera vez a `braze.openSession()`. La sesión permanecerá activa hasta `30` minutos de inactividad (a menos que [cambies el tiempo de espera predeterminado de la sesión]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=web#change-session-timeout) o que el usuario cierre la aplicación.
{% endtab %}
{% endtabs %}