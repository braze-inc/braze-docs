## Sobre o ciclo de vida da sessão

Uma sessão refere-se ao período de tempo em que o SDK Braze rastreia a atividade do usuário em seu app após ser iniciado. Você também pode forçar uma nova sessão [chamando o método `changeUser()`]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/#setting-a-user-id).

{% tabs %}
{% tab Android %}
{% alert note %}
Se você configurou o [callback do ciclo de vida da atividade]({{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-4-tracking-user-sessions-in-android) para Android, o Braze chamará automaticamente [`openSession()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/open-session.html) e [`closeSession()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/close-session.html) para cada atividade em seu app.
{% endalert %}

Por padrão, uma sessão começa quando `openSession()` é chamado pela primeira vez. Se seu app for para o segundo plano e depois retornar ao primeiro plano, o SDK verificará se mais de 10 segundos se passaram desde que a sessão começou (a menos que você [altere o tempo limite padrão da sessão]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=android#change-session-timeout)). Se sim, uma nova sessão começará. Tenha em mente que se o usuário fechar seu app enquanto estiver em segundo plano, os dados da sessão podem não ser enviados ao Braze até que eles reabram o app.

Chamar `closeSession()` não encerrará imediatamente a sessão. Em vez disso, encerrará a sessão após 10 segundos se `openSession()` não for chamado novamente pelo usuário iniciando outra atividade.
{% endtab %}

{% tab swift %}
Por padrão, uma sessão começa quando você chama `Braze.init(configuration:)`. Isso ocorre quando a notificação `UIApplicationWillEnterForegroundNotification` é acionada, significando que o app entrou no primeiro plano.

Se seu app for para o segundo plano, `UIApplicationDidEnterBackgroundNotification` será acionado. Quando seu app retornar ao primeiro plano, o SDK verificará se mais de 10 segundos se passaram desde que a sessão começou (a menos que você [altere o tempo limite padrão da sessão]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=swift#change-session-timeout)). Se sim, uma nova sessão começará.
{% endtab %}

{% tab web %}
Por padrão, uma sessão começa quando você chama `braze.openSession()` pela primeira vez. A sessão permanecerá ativa por até `30` minutos de inatividade (a menos que você [altere o tempo limite padrão da sessão]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=web#change-session-timeout) ou o usuário feche o app.
{% endtab %}
{% endtabs %}