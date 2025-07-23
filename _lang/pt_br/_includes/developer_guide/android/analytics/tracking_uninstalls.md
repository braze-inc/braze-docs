## Configuração do rastreamento de desinstalação

### Etapa 1: Configurar a FCM

O SDK do Android Braze usa o Firebase Cloud Messaging (FCM) para enviar notificações por push silenciosas, que são usadas para coletar análises de dados de rastreamento de desinstalação. Caso ainda não o tenha feito, [configure]({{site.baseurl}}/developer_guide/platforms/android/push_notifications/#setting-up-push-notifications) ou [migre para a]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android) API Firebase Cloud Messaging para notificações por push.

### Etapa 2: Detectar manualmente o rastreamento de desinstalação (opcional)

Por padrão, o SDK do Android Braze detectará e ignorará automaticamente as notificações por push silenciosas relacionadas ao rastreamento de desinstalação. No entanto, se você optar por detectar manualmente o rastreamento de desinstalação usando o método [`isUninstallTrackingPush()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.push/-braze-notification-payload/is-uninstall-tracking-push.html) método.

{% alert important %}
Como as notificações silenciosas para rastreamento de desinstalação não são encaminhadas para nenhum retorno de chamada por push do Braze, você só pode usar esse método antes de passar uma notificação por push para o Braze.
{% endalert %}

### Etapa 3: Remover pings automáticos do servidor

Uma notificação por push silenciosa ativará seu aplicativo e instanciará o componente `Application` se o aplicativo ainda não estiver em execução. Portanto, se você tiver uma subclasse [`Application`](https://developer.android.com/reference/android/app/Application) personalizada, remova qualquer lógica que faça ping automaticamente em seus servidores durante o método [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application#onCreate()) método de ciclo de vida.

### Etapa 4: Ativar o rastreamento de desinstalação

Por fim, ative o rastreamento de desinstalação no Braze. Para obter um passo a passo completo, consulte [Ativar o rastreamento de desinstalação]({{site.baseurl}}/user_guide/data_and_analytics/tracking/uninstall_tracking/#uninstall-tracking).

{% alert important %}
O rastreamento de desinstalações pode ser impreciso. As métricas que você vê no Braze podem sofrer postergação ou ser imprecisas.
{% endalert %}
