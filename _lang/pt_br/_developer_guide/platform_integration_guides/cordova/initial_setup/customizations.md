---
nav_title: Personalizações
article_title: Personalização do SDK Cordova Braze
page_order: 1
---

# Personalização do SDK Cordova Braze

> Estas são as personalizações disponíveis para o SDK Cordova Braze.

{% multi_lang_include cordova/prerequisites.md %}

## Opções de personalização

Você pode adicionar qualquer uma das seguintes preferências ao elemento `platform` no arquivo `config.xml` do seu projeto:

{% tabs %}
{% tab ios %}
| Método                                         | Descrição                                                                                                                                            |
| -----------------------------------------------| -------------------------------------------------------------------------------------------------------------------------------------------------------|
| `api_key` | Define a chave de API para seu aplicativo. |
| `ios_api_endpoint`                             | Define o [endpoint de SDK]({{site.baseurl}}/api/basics/#endpoints) para seu aplicativo. |
| `ios_disable_automatic_push_registration`      | Define se o registro automático de push deve ser desativado. |
| `ios_disable_automatic_push_handling`          | Define se a administração automática de push deve ser desativada. |
| `ios_enable_idfa_automatic_collection`         | Define se o SDK da Braze deve coletar automaticamente as informações do IDFA. Para saber mais, consulte a documentação do método IDFA da [Braze](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforadvertiser:)/). |
| `enable_location_collection` | Define se a coleta automática de local está ativada (se o usuário permitir). O `geofence-branch`
`geofences_enabled`                            | Define se as geofences estão ativadas.
| `ios_session_timeout` | Define o tempo limite da sessão do Braze para seu aplicativo em segundos. O padrão é 10 segundos.
| `sdk_authentication_enabled`                   | Define se deve ativar o recurso de [autenticação do SDK](https://www.braze.com/docs/developer_guide/platform_wide/sdk_authentication#sdk-authentication). |
| `display_foreground_push_notifications`        | Define se notificações por push devem ser exibidas enquanto o aplicativo está em primeiro plano. |
| `ios_disable_un_authorization_option_provisional` | Define se `UNAuthorizationOptionProvisional` deve ser desativado. |
| `trigger_action_minimum_time_interval_seconds` | Define o intervalo mínimo de tempo em segundos entre os gatilhos. O padrão é 30 segundos.
| `ios_push_app_group` | Define o ID do grupo de app para extensões de push do iOS. |
| `ios_forward_universal_links` | Define se o SDK deve reconhecer e encaminhar automaticamente links universais para os métodos do sistema.
| `ios_log_level` | Define o nível mínimo de registro para `Braze.Configuration.Logger`. |
| `ios_use_uuid_as_device_id` | Define se um UUID gerado aleatoriamente deve ser usado como o ID do dispositivo. |
| `ios_flush_interval_seconds` | Define o intervalo em segundos entre os despejos automáticos de dados. O padrão é 10 segundos.
| `ios_use_automatic_request_policy` | Define se a política de solicitação para `Braze.Configuration.Api` deve ser automática ou manual. |
| `should_opt_in_when_push_authorized` | Define se o estado de inscrição de notificação de um usuário deve ser automaticamente definido para `optedIn` quando as permissões de push são autorizadas. |

{% alert tip %}
Para mais informações, acesse [GitHub: Plugin Braze iOS Cordova](https://github.com/braze-inc/braze-cordova-sdk/blob/master/src/ios/BrazePlugin.m).
{% endalert %}
{% endtab %}

{% tab Android %}
| Método                                         | Descrição                                                                                                                                            |
| -----------------------------------------------| -------------------------------------------------------------------------------------------------------------------------------------------------------|
| `api_key` | Define a chave de API para seu aplicativo. |
| `android_api_endpoint`                         | Define o [endpoint de SDK]({{site.baseurl}}/api/basics/#endpoints) para seu aplicativo. |
| `android_small_notification_icon`              | Define o ícone pequeno da notificação. |
| `android_large_notification_icon`              | Define o ícone grande da notificação. |
`android_notification_accent_color` Define a cor de destaque da notificação usando uma representação hexadecimal.
| `android_default_session_timeout`              | Define o tempo limite da sessão do Braze para seu aplicativo em segundos. O padrão é 10 segundos.
| `android_handle_push_deep_links_automatically` | Define se o SDK da Braze deve lidar automaticamente com deep links de push. |
| `android_log_level`                            | Define o nível de registro para o seu aplicativo. O nível de registro padrão é 4 e registrará minimamente as informações. Para ativar o registro detalhado para depuração, use o nível de registro 2.
| `firebase_cloud_messaging_registration_enabled`| Define se deve usar o envio de mensagens do Firebase para notificações por push. |
| `android_fcm_sender_id` | Define o ID do remetente do envio de mensagens do Firebase Cloud.
| `enable_location_collection`                   | Define se a coleta automática de localização está ativada (se o usuário permitir). |
`geofences_enabled`                            | Define se as geofences estão ativadas.
| `android_disable_auto_session_tracking`        | Define se deve desativar o rastreio automático de sessões do plugin Adroid Cordova. |
| `sdk_authentication_enabled`                   | Define se deve ativar o recurso de [autenticação do SDK](https://www.braze.com/docs/developer_guide/platform_wide/sdk_authentication#sdk-authentication). |
| `trigger_action_minimum_time_interval_seconds` | Define o intervalo mínimo de tempo em segundos entre os gatilhos. O padrão é 30 segundos.
`is_session_start_based_timeout_enabled` Define se o comportamento de tempo limite da sessão será baseado em eventos de início ou término da sessão.
| `default_notification_channel_name` | Define o nome voltado para o usuário conforme visto via `NotificationChannel.getName` para o `NotificationChannel` padrão da Braze. |
| `default_notification_channel_description`     | Define a descrição voltada para o usuário conforme visto via `NotificationChannel.getDescription` para o padrão Braze `NotificationChannel`. |
| `does_push_story_dismiss_on_click`             | Define se uma story por push é automaticamente descartada quando clicada. |
| `is_fallback_firebase_messaging_service_enabled`| Define se o uso de um serviço de envio de mensagens de fallback do Firebase Cloud Messaging está ativado. |
| `fallback_firebase_messaging_service_classpath`| Define o classpath para o serviço de envio de mensagens de fallback do Firebase Cloud. |
| `is_content_cards_unread_visual_indicator_enabled`| Define se a barra de indicação visual de conteúdo não lido está ativada.
| `is_firebase_messaging_service_on_new_token_registration_enabled`| Define se o SDK da Braze registrará tokens automaticamente em `com.google.firebase.messaging.FirebaseMessagingService.onNewToken`. |
| `is_push_deep_link_back_stack_activity_enabled` | Define se a Braze adicionará uma atividade à pilha de retorno ao seguir automaticamente os deep links para push. |
| `push_deep_link_back_stack_activity_class_name` | Define a atividade que a Braze adicionará à pilha de atividades ao seguir automaticamente os deep links para push. |
| `should_opt_in_when_push_authorized` | Define se a Braze deve aceitar automaticamente o usuário quando o push é autorizado. |

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

{% tab Android %}
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

## Sintaxe específica da plataforma

### Números inteiros

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

{% tab Android %}
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

{% tab Android %}
Preferências booleanas são lidas pelo SDK usando palavras-chave `true` e `false` como uma representação de string, como no exemplo a seguir:

```xml
<platform name="android">
    <preference name="com.braze.should_opt_in_when_push_authorized" value="true" />
    <preference name="com.braze.is_session_start_based_timeout_enabled" value="false" />
</platform>
```
{% endtab %}
{% endtabs %}
