## Integrando o SDK do Cordova

### Pré-requisitos

Antes de começar, verifique se seu ambiente é compatível com a [última versão do SDK do Braze para Cordova](https://github.com/braze-inc/braze-cordova-sdk?tab=readme-ov-file#minimum-version-requirements).

### Etapa 1: Adicione o SDK ao projeto

{% alert warning %}
Adicione o SDK do Braze para Cordova apenas usando os métodos abaixo. Não tente instalar usando outros métodos, pois isso pode levar a uma violação de segurança.
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

A seção a seguir cobre a sintaxe específica da plataforma ao usar Cordova com iOS ou Android.

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
| Método                                            | Descrição                                                                                                                                                                                                                                           |
| ------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ios_api_key`                                     | Define a chave de API para seu aplicativo.                                                                                                                                                                                                                |
| `ios_api_endpoint`                                | Define o [endpoint de SDK]({{site.baseurl}}/api/basics/#endpoints) para seu aplicativo.                                                                                                                                                                 |
| `ios_disable_automatic_push_registration`         | Define se o registro automático de push deve ser desativado.                                                                                                                                                                                          |
| `ios_disable_automatic_push_handling`             | Define se o manuseio automático de push deve ser desativado.                                                                                                                                                                                              |
| `ios_enable_idfa_automatic_collection`            | Define se o SDK do Braze deve coletar automaticamente as informações do IDFA. Para saber mais, consulte [a documentação do método IDFA do Braze](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforadvertiser:)/). |
| `enable_location_collection`                      | Define se a coleta automática de localização está habilitada (se o usuário permitir). O `geofence-branch`                                                                                                                                                |
| `geofences_enabled`                               | Define se os geofences estão habilitados.                                                                                                                                                                                                                   |
| `ios_session_timeout`                             | Define o tempo limite da sessão do Braze para seu aplicativo em segundos. O padrão é 10 segundos.                                                                                                                                                               |
| `sdk_authentication_enabled`                      | Define se deve ativar o recurso de [autenticação do SDK]({{site.baseurl}}/developer_guide/platform_wide/sdk_authentication#sdk-authentication).                                                                                              |
| `display_foreground_push_notifications`           | Define se as notificações por push devem ser exibidas enquanto o aplicativo está em primeiro plano.                                                                                                                                                       |
| `ios_disable_un_authorization_option_provisional` | Define se `UNAuthorizationOptionProvisional` deve ser desativado.                                                                                                                                                                                   |
| `trigger_action_minimum_time_interval_seconds`    | Define o intervalo mínimo de tempo em segundos entre os acionamentos. Padrão de 30 segundos.                                                                                                                                                                   |
| `ios_push_app_group`                              | Define o ID do grupo de app para extensões de push no iOS.                                                                                                                                                                                                        |
| `ios_forward_universal_links`                     | Define se o SDK reconhece automaticamente e encaminha links universais para os métodos do sistema. Necessário para que links profundos de notificações por push funcionem no iOS. Padrão desativado.                                                                |
| `ios_log_level`                                   | Define o nível mínimo de registro para `Braze.Configuration.Logger`.                                                                                                                                                                                      |
| `ios_use_uuid_as_device_id`                       | Define se um UUID gerado aleatoriamente deve ser usado como o ID do dispositivo.                                                                                                                                                                                    |
| `ios_flush_interval_seconds`                      | Define o intervalo em segundos entre as limpezas automáticas de dados. Padrão de 10 segundos.                                                                                                                                                                  |
| `ios_use_automatic_request_policy`                | Define se a política de solicitação para `Braze.Configuration.Api` deve ser automática ou manual.                                                                                                                                                          |
| `should_opt_in_when_push_authorized`              | Define se o estado de inscrição de notificações de um usuário deve ser automaticamente definido como `optedIn` quando as permissões de push forem autorizadas.                                                                                                                       |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert tip %}
Para mais informações, acesse [GitHub: Plugin Braze iOS Cordova](https://github.com/braze-inc/braze-cordova-sdk/blob/master/src/ios/BrazePlugin.m).
{% endalert %}
{% endtab %}

{% tab android %}
| Método                                                            | Descrição                                                                                                                                                                                   |
| ----------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `android_api_key`                                                 | Define a chave de API para seu aplicativo.                                                                                                                                                        |
| `android_api_endpoint`                                            | Define o [endpoint de SDK]({{site.baseurl}}/api/basics/#endpoints) para seu aplicativo.                                                                                                         |
| `android_small_notification_icon`                                 | Define o ícone pequeno da notificação.                                                                                                                                                             |
| `android_large_notification_icon`                                 | Define o ícone grande da notificação.                                                                                                                                                             |
| `android_notification_accent_color`                               | Define a cor de destaque da notificação usando uma representação hexadecimal.                                                                                                                        |
| `android_default_session_timeout`                                 | Define o tempo limite da sessão do Braze para seu aplicativo em segundos. O padrão é 10 segundos.                                                                                                       |
| `android_handle_push_deep_links_automatically`                    | Define se o SDK do Braze lida automaticamente com links profundos de push. Necessário para que os links profundos de notificações por push funcionem no Android. O padrão é desativado.                                   |
| `android_log_level`                                               | Define o nível de log para seu aplicativo. O nível de registro padrão é 4 e registrará minimamente as informações. Para habilitar o registro detalhado para depuração, use o nível de log 2\.                                    |
| `firebase_cloud_messaging_registration_enabled`                   | Define se deve usar o Firebase Cloud Messaging para notificações por push.                                                                                                                          |
| `android_fcm_sender_id`                                           | Define o ID do remetente do Firebase Cloud Messaging.                                                                                                                                                  |
| `enable_location_collection`                                      | Define se a coleta automática de localização está habilitada (se o usuário permitir).                                                                                                              |
| `geofences_enabled`                                               | Define se os geofences estão habilitados.                                                                                                                                                           |
| `android_disable_auto_session_tracking`                           | Desativa o plugin Cordova do Android de rastrear sessões automaticamente. Para saber mais, veja [Desativando o rastreamento automático de sessões](#cordova_disable-automatic-session-tracking) |
| `sdk_authentication_enabled`                                      | Define se deve habilitar o recurso de [autenticação do SDK]({{site.baseurl}}/developer_guide/platform_wide/sdk_authentication#sdk-authentication).                                      |
| `trigger_action_minimum_time_interval_seconds`                    | Define o intervalo mínimo de tempo em segundos entre os acionamentos. O padrão é 30 segundos.                                                                                                           |
| `is_session_start_based_timeout_enabled`                          | Define se o comportamento do tempo limite da sessão deve ser baseado em eventos de início ou fim da sessão.                                                                                          |
| `default_notification_channel_name`                               | Define o nome visível para o usuário conforme visto via `NotificationChannel.getName` para o padrão do Braze `NotificationChannel`.                                                                              |
| `default_notification_channel_description`                        | Define a descrição visível para o usuário conforme visto via `NotificationChannel.getDescription` para o padrão do Braze `NotificationChannel`.                                                                |
| `does_push_story_dismiss_on_click`                                | Define se uma Push Story é automaticamente descartada quando clicada.                                                                                                                            |
| `is_fallback_firebase_messaging_service_enabled`                  | Define se o uso de um fallback do Firebase Cloud Messaging Service está habilitado.                                                                                                               |
| `fallback_firebase_messaging_service_classpath`                   | Define o classpath para o fallback do Firebase Cloud Messaging Service.                                                                                                                         |
| `is_content_cards_unread_visual_indicator_enabled`                | Define se a barra de indicação visual de não lidos dos Content Cards está habilitada.                                                                                                                       |
| `is_firebase_messaging_service_on_new_token_registration_enabled` | Define se o SDK do Braze registrará automaticamente tokens em `com.google.firebase.messaging.FirebaseMessagingService.onNewToken`.                                                         |
| `is_push_deep_link_back_stack_activity_enabled`                   | Define se o Braze adicionará uma atividade à pilha de atividades ao seguir automaticamente links profundos para push.                                                                                   |
| `push_deep_link_back_stack_activity_class_name`                   | Define a atividade que o Braze adicionará à pilha de atividades ao seguir automaticamente links profundos para push.                                                                                     |
| `should_opt_in_when_push_authorized`                              | Define se o Braze deve automaticamente aceitar o usuário quando o push é autorizado.                                                                                                                   |
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

## Desabilitando o rastreamento automático de sessão (apenas Android) {#disable-automatic-session-tracking}

Por padrão, o plug-in do Android Cordova rastreia automaticamente as sessões. Para desativar o rastreamento automático de sessão, adicione a seguinte preferência ao elemento `platform` no arquivo `config.xml` do seu projeto:

```xml
<platform name="android">
    <preference name="com.braze.android_disable_auto_session_tracking" value="true" />
</platform>
```

Para começar a rastrear as sessões novamente, ligue para `BrazePlugin.startSessionTracking()`. Lembre-se de que somente as sessões iniciadas após o próximo `Activity.onStart()` serão rastreadas.
