## Integração do SDK do Cordova

### Pré-requisitos

Antes de começar, verifique se seu ambiente é compatível com a [versão mais recente do Braze Cordova SDK](https://github.com/braze-inc/braze-cordova-sdk?tab=readme-ov-file#minimum-version-requirements).

### Etapa 1: Adicione o SDK ao projeto

{% alert warning %}
Adicione apenas o SDK do Braze Cordova usando os métodos abaixo. Não tente instalar usando outros métodos, pois isso pode levar a uma violação de segurança.
{% endalert %}

Se você estiver usando o Cordova 6 ou posterior, poderá adicionar o SDK diretamente do GitHub. Como alternativa, você pode baixar um ZIP do [repositório do GitHub](https://github.com/braze-inc/braze-cordova-sdk) e adicionar o SDK manualmente.

{% tabs local %}
{% tab geofence disabled %}
Se não planeja usar a coleta de locais e geofences, use a ramificação `master` do GitHub.

```bash
cordova plugin add https://github.com/braze-inc/braze-cordova-sdk#master
```
{% endtab %}

{% tab geofence enabled %}
Se planeja usar a coleta de locais e geofences, use `geofence-branch` do GitHub.

```bash
cordova plugin add https://github.com/braze-inc/braze-cordova-sdk#geofence-branch
```
{% endtab %}
{% endtabs %}

{% alert tip %}
Você pode alternar entre `master` e `geofence-branch` a qualquer momento, repetindo esta etapa.
{% endalert %}

### Etapa 2: Configure seu projeto

Em seguida, adicione as seguintes preferências ao elemento `platform` no arquivo `config.xml` de seu projeto.

{% tabs %}
{% tab ios %}
```xml
<preference name="com.braze.ios_api_key" value="BRAZE_API_KEY" />
<preference name="com.braze.ios_api_endpoint" value="CUSTOM_API_ENDPOINT" />
```
{% endtab %}

{% tab android %}
```xml
<preference name="com.braze.android_api_key" value="BRAZE_API_KEY" />
<preference name="com.braze.android_api_endpoint" value="CUSTOM_API_ENDPOINT" />
```
{% endtab %}
{% endtabs %}

Substitua o seguinte:

| Valor                 | Descrição                                                                                                                      |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `BRAZE_API_KEY`       | Sua [chave da API REST do Braze]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/#rest-api-keys).              |
| `CUSTOM_API_ENDPOINT` | Um endpoint de API personalizado. Esse endpoint é usado para rotear os dados de sua instância do Braze para o grupo de app correto em seu dashboard do Braze. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

O elemento `platform` em seu arquivo `config.xml` deve ser semelhante ao seguinte:

{% tabs %}
{% tab ios %}
```xml
<platform name="ios">
    <preference name="com.braze.ios_api_key" value="BRAZE_API_KEY" />
    <preference name="com.braze.ios_api_endpoint" value="sdk.fra-01.braze.eu" />
</platform>
```
{% endtab %}

{% tab android %}
```xml
<platform name="android">
    <preference name="com.braze.android_api_key" value="BRAZE_API_KEY" />
    <preference name="com.braze.android_api_endpoint" value="sdk.fra-01.braze.eu" />
</platform>
```
{% endtab %}
{% endtabs %}

## Sintaxe específica da plataforma

A seção a seguir aborda a sintaxe específica da plataforma ao usar o Cordova com iOS ou Android.

### Inteiros

{% tabs %}
{% tab ios %}
As preferências de inteiros são lidas como representações de string, como no exemplo a seguir:

```xml
<platform name="ios">
    <preference name="com.braze.ios_flush_interval_seconds" value="10" />
    <preference name="com.braze.ios_session_timeout" value="5" />
</platform>
```
{% endtab %}

{% tab android %}
Devido à forma como o framework Cordova 8.0.0+ lida com preferências, preferências apenas de número inteiro (como IDs de remetente) devem ser definidas como strings precedidas por `str_`, como no exemplo a seguir:

```xml
<platform name="android">
    <preference name="com.braze.android_fcm_sender_id" value="str_64422926741" />
    <preference name="com.braze.android_default_session_timeout" value="str_10" />
</platform>
```
{% endtab %}
{% endtabs %}

### Booleanos

{% tabs %}
{% tab ios %}
Preferências booleanas são lidas pelo SDK usando palavras-chave `YES` e `NO` como uma representação de string, como no exemplo a seguir:

```xml
<platform name="ios">
    <preference name="com.braze.should_opt_in_when_push_authorized" value="YES" />
    <preference name="com.braze.ios_disable_automatic_push_handling" value="NO" />
</platform>
```
{% endtab %}

{% tab android %}
Preferências booleanas são lidas pelo SDK usando palavras-chave `true` e `false` como uma representação de string, como no exemplo a seguir:

```xml
<platform name="android">
    <preference name="com.braze.should_opt_in_when_push_authorized" value="true" />
    <preference name="com.braze.is_session_start_based_timeout_enabled" value="false" />
</platform>
```
{% endtab %}
{% endtabs %}

## Configurações opcionais {#optional}

Você pode adicionar qualquer uma das seguintes preferências ao elemento `platform` no arquivo `config.xml` do seu projeto:

{% tabs %}
{% tab ios %}
| Método | Descrição | Descrição
| ------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ios_api_key` | Define a chave de API para seu aplicativo.                                                                                                                                                                                                                |
| `ios_api_endpoint` | Define o [endpoint do SDK]({{site.baseurl}}/api/basics/#endpoints) para o seu aplicativo.                                                                                                                                                                 |
| `ios_disable_automatic_push_registration` | Define se o registro push automático deve ser desativado.                                                                                                                                                                                          |
| `ios_disable_automatic_push_handling` | Define se o manuseio automático de push deve ser desativado.                                                                                                                                                                                              |
| `ios_enable_idfa_automatic_collection` | Define se o SDK do Braze deve coletar automaticamente as informações do IDFA. Para saber mais, consulte [a documentação do método Braze IDFA](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforadvertiser:)/). |
| `enable_location_collection` | Define se a coleta automática de locais está ativada (se o usuário permitir). O `geofence-branch` |
| `geofences_enabled` | Define se as geofences estão ativadas.                                                                                                                                                                                                                   |
| `ios_session_timeout` | Define o tempo limite da sessão do Braze para seu aplicativo em segundos. O padrão é 10 segundos.                                                                                                                                                               |
| `sdk_authentication_enabled` | Define se o recurso [de autenticação do SDK]({{site.baseurl}}/developer_guide/platform_wide/sdk_authentication#sdk-authentication) deve ser ativado.                                                                                              |
| `display_foreground_push_notifications` | Define se as notificações por push devem ser exibidas enquanto o aplicativo estiver em primeiro plano.                                                                                                                                                       |
| `ios_disable_un_authorization_option_provisional` Define se o `UNAuthorizationOptionProvisional` deve ser desativado.                                                                                                                                                                                   |
| `trigger_action_minimum_time_interval_seconds` | Define o intervalo de tempo mínimo, em segundos, entre os disparos. O padrão é 30 segundos.                                                                                                                                                                   |
| `ios_push_app_group` | Define o ID do grupo de app para extensões push do iOS.                                                                                                                                                                                                        |
| `ios_forward_universal_links` Define se o SDK deve reconhecer e encaminhar automaticamente os links universais para os métodos do sistema.                                                                                                                                                     |
| `ios_log_level` | Define o nível mínimo de registro para `Braze.Configuration.Logger`.                                                                                                                                                                                      |
| `ios_use_uuid_as_device_id` | Define se um UUID gerado aleatoriamente deve ser usado como ID do dispositivo.                                                                                                                                                                                    |
| `ios_flush_interval_seconds` | Define o intervalo em segundos entre as descargas automáticas de dados. O padrão é 10 segundos.                                                                                                                                                                  |
| `ios_use_automatic_request_policy` | Define se a política de solicitação para `Braze.Configuration.Api` deve ser automática ou manual.                                                                                                                                                          |
`should_opt_in_when_push_authorized` | Define se o estado da inscrição de notificação de um usuário deve ser automaticamente definido como `optedIn` quando as permissões por push forem autorizadas.                                                                                                                       |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert tip %}
Para mais informações, acesse [GitHub: Plugin Braze iOS Cordova](https://github.com/braze-inc/braze-cordova-sdk/blob/master/src/ios/BrazePlugin.m).
{% endalert %}
{% endtab %}

{% tab android %}
| Método | Descrição | Descrição
| ----------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `android_api_key` | Define a chave de API para seu aplicativo.                                                                                                                                                        |
| `android_api_endpoint` | Define o [endpoint do SDK]({{site.baseurl}}/api/basics/#endpoints) para o seu aplicativo.                                                                                                         |
| `android_small_notification_icon` Define o ícone pequeno de notificação.                                                                                                                                                             |
| `android_large_notification_icon` Define o ícone grande de notificação.                                                                                                                                                             |
| `android_notification_accent_color` | Define a cor de destaque da notificação usando uma representação hexadecimal.                                                                                                                        |
| `android_default_session_timeout` | Define o tempo limite da sessão do Braze para seu aplicativo em segundos. O padrão é 10 segundos.                                                                                                       |
| `android_handle_push_deep_links_automatically` | Define se o SDK do Braze deve tratar automaticamente os deep links push.                                                                                                                       |
| `android_log_level` | Define o nível de registro do seu aplicativo. O nível de registro padrão é 4 e registrará minimamente as informações. Para ativar o registro detalhado para depuração, use o nível de registro 2\.                                    |
| `firebase_cloud_messaging_registration_enabled` | Define se o Firebase Cloud Messaging deve ser usado para notificações por push.                                                                                                                          |
| `android_fcm_sender_id` | Define o ID do remetente do Firebase Cloud Messaging.                                                                                                                                                  |
| `enable_location_collection` | Define se a coleta automática de locais está ativada (se o usuário permitir).                                                                                                              |
| `geofences_enabled` | Define se as geofences estão ativadas.                                                                                                                                                           |
| `android_disable_auto_session_tracking` | Desative o plug-in do Android Cordova para que ele não rastreie automaticamente as sessões. Para saber mais, consulte [Desativando o rastreamento automático de sessão](#cordova_disable-automatic-session-tracking) 
| `sdk_authentication_enabled` | Define se o recurso [de autenticação do SDK]({{site.baseurl}}/developer_guide/platform_wide/sdk_authentication#sdk-authentication) deve ser ativado.                                      |
| `trigger_action_minimum_time_interval_seconds` | Define o intervalo de tempo mínimo, em segundos, entre os disparos. O padrão é 30 segundos.                                                                                                           |
| `is_session_start_based_timeout_enabled` | Define se o comportamento de tempo limite da sessão deve se basear em eventos de início ou de ponta a ponta da sessão.                                                                                          |
| `default_notification_channel_name` | Define o nome voltado para o usuário, conforme visto em `NotificationChannel.getName` para o padrão do Braze `NotificationChannel`.                                                                              |
| `default_notification_channel_description` | Define a descrição voltada para o usuário, conforme visto em `NotificationChannel.getDescription` para o padrão do Braze `NotificationChannel`.                                                                |
| `does_push_story_dismiss_on_click` Define se uma story por push é automaticamente descartada quando clicada.                                                                                                                            |
| `is_fallback_firebase_messaging_service_enabled` | Define se o uso de um serviço de envio de mensagens do Firebase Cloud está ativado.                                                                                                               |
| `fallback_firebase_messaging_service_classpath` | Define o classpath para o serviço de envio de mensagens do Firebase Cloud de fallback.                                                                                                                         |
| `is_content_cards_unread_visual_indicator_enabled` | Define se a barra de indicação visual de cartões de conteúdo não lidos está ativada.                                                                                                                       |
| `is_firebase_messaging_service_on_new_token_registration_enabled` | Define se o Braze SDK registrará automaticamente os tokens em `com.google.firebase.messaging.FirebaseMessagingService.onNewToken`.                                                         |
| `is_push_deep_link_back_stack_activity_enabled` | Define se o Braze adicionará uma atividade à pilha traseira ao seguir automaticamente os deep links para push.                                                                                   |
| `push_deep_link_back_stack_activity_class_name` | Define a atividade que o Braze adicionará à pilha traseira ao seguir automaticamente os deep links para push.                                                                                     |
| `should_opt_in_when_push_authorized` | Define se o Braze deve fazer a aceitação automática do usuário quando o push for autorizado.                                                                                                                   |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert tip %}
Para mais informações, acesse [GitHub: Plugin Braze Android Cordova](https://github.com/braze-inc/braze-cordova-sdk/blob/master/src/android/BrazePlugin.kt).
{% endalert %}
{% endtab %}
{% endtabs %}

A seguir veja é um exemplo de arquivo `config.xml` com configurações adicionais:

{% tabs %}
{% tab ios %}
```xml
<platform name="ios">
    <preference name="com.braze.ios_disable_automatic_push_registration" value="NO"/"YES" />
    <preference name="com.braze.ios_disable_automatic_push_handling" value="NO"/"YES" />
    <preference name="com.braze.ios_enable_idfa_automatic_collection" value="YES"/"NO" />
    <preference name="com.braze.enable_location_collection" value="NO"/"YES" />
    <preference name="com.braze.geofences_enabled" value="NO"/"YES" />
    <preference name="com.braze.ios_session_timeout" value="5" />
    <preference name="com.braze.sdk_authentication_enabled" value="YES"/"NO" />
    <preference name="com.braze.display_foreground_push_notifications" value="YES"/"NO" />
    <preference name="com.braze.ios_disable_un_authorization_option_provisional" value="NO"/"YES" />
    <preference name="com.braze.trigger_action_minimum_time_interval_seconds" value="30" />
    <preference name="com.braze.ios_push_app_group" value="PUSH_APP_GROUP_ID" />
    <preference name="com.braze.ios_forward_universal_links" value="YES"/"NO" />
    <preference name="com.braze.ios_log_level" value="2" />
    <preference name="com.braze.ios_use_uuid_as_device_id" value="YES"/"NO" />
    <preference name="com.braze.ios_flush_interval_seconds" value="10" />
    <preference name="com.braze.ios_use_automatic_request_policy" value="YES"/"NO" />
    <preference name="com.braze.should_opt_in_when_push_authorized" value="YES"/"NO" />
</platform>
```
{% endtab %}

{% tab android %}
```xml
<platform name="android">
    <preference name="com.braze.android_small_notification_icon" value="RESOURCE_ENTRY_NAME_FOR_ICON_DRAWABLE" />
    <preference name="com.braze.android_large_notification_icon" value="RESOURCE_ENTRY_NAME_FOR_ICON_DRAWABLE" />
    <preference name="com.braze.android_notification_accent_color" value="str_ACCENT_COLOR_INTEGER" />
    <preference name="com.braze.android_default_session_timeout" value="str_SESSION_TIMEOUT_INTEGER" />
    <preference name="com.braze.android_handle_push_deep_links_automatically" value="true"/"false" />
    <preference name="com.braze.android_log_level" value="str_LOG_LEVEL_INTEGER" />
    <preference name="com.braze.firebase_cloud_messaging_registration_enabled" value="true"/"false" />
    <preference name="com.braze.android_fcm_sender_id" value="str_YOUR_FCM_SENDER_ID" />
    <preference name="com.braze.enable_location_collection" value="true"/"false" />
    <preference name="com.braze.geofences_enabled" value="true"/"false" />
    <preference name="com.braze.android_disable_auto_session_tracking" value="true"/"false" />
    <preference name="com.braze.sdk_authentication_enabled" value="true"/"false" />
    <preference name="com.braze.trigger_action_minimum_time_interval_seconds" value="str_MINIMUM_INTERVAL_INTEGER" />
    <preference name="com.braze.is_session_start_based_timeout_enabled" value="false"/"true" />
    <preference name="com.braze.default_notification_channel_name" value="DEFAULT_NAME" />
    <preference name="com.braze.default_notification_channel_description" value="DEFAULT_DESCRIPTION" />
    <preference name="com.braze.does_push_story_dismiss_on_click" value="true"/"false" />
    <preference name="com.braze.is_fallback_firebase_messaging_service_enabled" value="true"/"false" />
    <preference name="com.braze.fallback_firebase_messaging_service_classpath" value="FALLBACK_FIREBASE_MESSAGING_CLASSPATH" />
    <preference name="com.braze.is_content_cards_unread_visual_indicator_enabled" value="true"/"false" />
    <preference name="com.braze.is_firebase_messaging_service_on_new_token_registration_enabled" value="true"/"false" />
    <preference name="com.braze.is_push_deep_link_back_stack_activity_enabled" value="true"/"false" />
    <preference name="com.braze.push_deep_link_back_stack_activity_class_name" value="DEEPLINK_BACKSTACK_ACTIVITY_CLASS_NAME" />
    <preference name="com.braze.should_opt_in_when_push_authorized" value="true"/"false" />
</platform>
```
{% endtab %}
{% endtabs %}

## Desativar o rastreamento automático de sessão (somente Android) {#disable-automatic-session-tracking}

Por padrão, o plug-in do Android Cordova rastreia automaticamente as sessões. Para desativar o rastreamento automático de sessão, adicione a seguinte preferência ao elemento `platform` no arquivo `config.xml` do seu projeto:

```xml
<platform name="android">
    <preference name="com.braze.android_disable_auto_session_tracking" value="true" />
</platform>
```

Para começar a rastrear as sessões novamente, ligue para `BrazePlugin.startSessionTracking()`. Lembre-se de que somente as sessões iniciadas após o próximo `Activity.onStart()` serão rastreadas.
