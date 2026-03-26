## Acerca del ciclo de vida de la sesión

Una sesión se refiere al período de tiempo durante el cual el SDK de Braze realiza el seguimiento de la actividad de los usuarios en tu aplicación después de su inicio. También puedes forzar una nueva sesión [llamando al`changeUser()`método]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/#setting-a-user-id) .

{% tabs %}
{% tab web %}
De forma predeterminada, una sesión comienza cuando llamas por primera vez a `braze.openSession()`. La sesión permanecerá activa durante un máximo de`30`  minutos de inactividad (a menos que [cambies el tiempo de espera predeterminado de la sesión]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=web#change-session-timeout) o que el usuario cierre la aplicación).
{% endtab %}

{% tab android %}
{% alert note %}
Si has configurado la devolución de llamada del ciclo de]({{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-4-tracking-user-sessions-in-android) vida de la actividad para Android, Braze llamará automáticamente a[`openSession()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/open-session.html)  y[`closeSession()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/close-session.html)  para cada actividad de tu aplicación.
{% endalert %}

De forma predeterminada, una sesión comienza cuando`openSession()`se llama por primera vez a . Si tu aplicación pasa a segundo plano y luego vuelve al primer plano, el SDK comprobará si han pasado más de 10 segundos desde que se inició la sesión (a menos que [cambies el tiempo de espera predeterminado de la sesión]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=android#change-session-timeout)). Si es así, comenzará una nueva sesión. Ten en cuenta que si el usuario cierra tu aplicación mientras está en segundo plano, es posible que los datos de la sesión no se envíen a Braze hasta que vuelva a abrir la aplicación.

Llamar no`closeSession()` terminará inmediatamente la sesión. En su lugar, finalizará la sesión tras 10 segundos si el usuario`openSession()` no vuelve a llamar a  iniciando otra actividad.
{% endtab %}

{% tab swift %}
De forma predeterminada, una sesión comienza cuando llamas a `Braze.init(configuration:)`. Esto ocurre cuando se desencadena la`UIApplicationWillEnterForegroundNotification`notificación, lo que significa que la aplicación ha pasado a primer plano.

Si tu aplicación pasa a segundo plano,`UIApplicationDidEnterBackgroundNotification`  se desencadena. La aplicación no permanece en una sesión activa mientras está en segundo plano. Cuando tu aplicación vuelve al primer plano, el SDK compara el tiempo transcurrido desde el inicio de la sesión con el tiempo de espera de la sesión (a menos que [cambies el tiempo de espera predeterminado]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=swift#change-session-timeout)). Si el tiempo transcurrido desde el inicio de la sesión supera el periodo de tiempo de espera, se inicia una nueva sesión.
{% endtab %}
{% endtabs %}