## Sobre o ciclo de vida da sessão

Uma sessão refere-se ao período de tempo em que o SDK do Braze rastreia a atividade do usuário em seu app depois que ele é iniciado. Você também pode forçar uma nova sessão [chamando o método `changeUser()` ]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/#setting-a-user-id).

{% tabs %}
{% tab web %}
Por padrão, uma sessão é iniciada quando você chama `braze.openSession()` pela primeira vez. A sessão permanecerá ativa por até `30` minutos de inatividade (a menos que você [altere o tempo limite padrão da sessão]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=web#change-session-timeout) ou o usuário feche o app).
{% endtab %}

{% tab android %}
{% alert note %}
Se você tiver configurado o [retorno de chamada do ciclo de vida da atividade]({{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-4-tracking-user-sessions-in-android) para Android, o Braze chamará automaticamente [`openSession()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/open-session.html) e [`closeSession()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/close-session.html) para cada atividade em seu app.
{% endalert %}

Por padrão, uma sessão é iniciada quando `openSession()` é chamado pela primeira vez. Se o seu app acessar o plano de fundo e depois retornar ao primeiro plano, o SDK verificará se mais de 10 segundos se passaram desde o início da sessão (a menos que você [altere o tempo limite padrão da sessão]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=android#change-session-timeout)). Se for o caso, uma nova sessão será iniciada. Lembre-se de que, se o usuário fechar seu aplicativo enquanto ele estiver em segundo plano, os dados da sessão poderão não ser enviados ao Braze até que ele reabra o app.

A chamada para `closeSession()` não encerrará imediatamente a sessão. Em vez disso, ele encerrará a sessão após 10 segundos se o `openSession()` não for chamado novamente pelo usuário para iniciar outra atividade.
{% endtab %}

{% tab swift %}
Por padrão, uma sessão é iniciada quando você chama `Braze.init(configuration:)`. Isso ocorre quando a notificação `UIApplicationWillEnterForegroundNotification` é disparada, o que significa que o app entrou em primeiro plano.

Se o seu app ficar em segundo plano, o `UIApplicationDidEnterBackgroundNotification` será disparado. Quando seu app retornar ao primeiro plano, o SDK verificará se mais de 10 segundos se passaram desde o início da sessão (a menos que você [altere o tempo limite padrão da sessão]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=swift#change-session-timeout)). Se for o caso, uma nova sessão será iniciada.
{% endtab %}
{% endtabs %}