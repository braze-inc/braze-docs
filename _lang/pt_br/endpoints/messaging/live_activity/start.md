---
nav_title: "POST: Iniciar atividade ao vivo"
article_title: "POST: Iniciar atividade ao vivo"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint \"Iniciar atividade ao vivo\""

---
{% api %}
# Iniciar atividade ao vivo
{% apimethod post %}
/messages/live_activity/start
{% endapimethod %}

> Use esse endpoint para iniciar remotamente [as Live Activities]({{site.baseurl}}/developer_guide/push_notifications/live_notifications/?sdktab=swift) exibidas em seu app para iOS. Esse endpoint requer configuração adicional.

Depois de criar uma atividade ao vivo, você pode fazer uma solicitação POST para iniciar remotamente sua atividade para qualquer segmento específico. Para saber mais sobre o Live Activities da Apple, consulte [Como iniciar e atualizar o Live Activities com notificações por push do ActivityKit](https://developer.apple.com/documentation/activitykit/starting-and-updating-live-activities-with-activitykit-push-notifications).

Se o endereço `content-available` não estiver definido, a prioridade padrão do serviço Apple Push Notification (APNs) será 10. Se `content-available` estiver definido, essa prioridade será 5. Consulte o [objeto push da Apple]({{site.baseurl}}/api/objects_filters/messaging/apple_object) para obter mais detalhes. 

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#2300226e-f26a-4154-9bcc-5883f1f294cd {% endapiref %}

## Pré-requisitos

Para usar este endpoint, você precisará concluir o seguinte:

- Gerar uma chave de API com a permissão `messages.live_activity.start`.
- [Crie uma atividade ao vivo]({{site.baseurl}}/developer_guide/push_notifications/live_notifications/?tab=local&sdktab=swift#swift_create-an-activity) usando o Braze Swift SDK.

{% multi_lang_include api/payload_size_alert.md %}

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='default' %}

## Corpo da solicitação

```json
{
  "app_id": "(required, string) App API identifier retrieved from the Developer Console.",
  "activity_id": "(required, string) Define a custom string as your `activity_id`. You will use this ID when you wish to send update or end events to your Live Activity.",
  "activity_attributes_type": "(required, string) The activity attributes type you define within `liveActivities.registerPushToStart` in your app",
  "activity_attributes": "(required, object) The static attribute values for the activity type (such as the sports team names, which don't change)",
  "content_state": "(required, object) You define the ContentState parameters when you create your Live Activity. Pass the updated values for your ContentState using this object. The format of this request must match the shape you initially defined.",
  "dismissal_date": "(optional, datetime in ISO-8601 format) The time to remove the Live Activity from the user’s UI. If this time is in the past, the Live Activity will be removed immediately.",
  "stale_date": "(optional, datetime in ISO-8601 format) The time the Live Activity content is marked as outdated in the user’s UI.",
  "notification": "(required, object) Include an `apple_push` object to define a push notification that creates an alert for the user, displayed on paired watchOS devices. Should include `notification.alert.title` and `notification.alert.body`",
  // One of the following:
  "external_user_ids": "(optional, array of strings) see external user identifier, maximum 50",
  "custom_audience": "(optional, connected audience object) see connected audience",
  "segment_id": "(optional, string) see segment identifier"
}
```

## Parâmetros de solicitação

| Parâmetro | Obrigatória | Tipo de dados| Descrição  |
|-----------|----------|----------|--------------|
| `app_id` | Obrigatória | String | [Identificador da API]({{site.baseurl}}/api/identifier_types/#the-app-identifier) do app recuperado da página [Chaves da API]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/).  |
| `activity_id` | Obrigatória | String  | Defina uma string personalizada como seu `activity_id`. Você usará esse ID quando desejar enviar eventos de atualização ou encerramento para sua atividade ao vivo.  |
| `activity_attributes_type`  | Obrigatória | String | O tipo de atribuição de atividade que você define em `liveActivities.registerPushToStart` no seu app.  |
| `activity_attributes` | Obrigatória | Objeto  | Os valores de atribuição estáticos para o tipo de atividade (como os nomes das equipes esportivas, que não mudam). |
| `content_state` | Obrigatória | Objeto  | Você define os `ContentState` parâmetros quando cria sua Atividade ao Vivo. Passe os valores atualizados para o seu `ContentState` usando este objeto.<br><br>O formato desta solicitação deve corresponder à forma que você definiu inicialmente. |
| `dismissal_date` | Opcional | Datetime <br>(string [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)) | Esse parâmetro define o tempo para remover a atividade ao vivo da interface do usuário. |
| `stale_date` | Opcional | Datetime <br>(string [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)) | Este parâmetro informa ao sistema quando o conteúdo da Atividade ao Vivo é marcado como desatualizado na interface do usuário. |
| `notification` | Obrigatória | Objeto | Inclua um [`apple_push`]({{site.baseurl}}/api/objects_filters/messaging/apple_object/) objeto para definir uma notificação por push. O comportamento dessa notificação por push depende se o usuário está ativo ou se está usando um dispositivo proxy. {::nomarkdown}<ul><li>Se uma <code>notificação</code> for incluída e o usuário estiver ativo no iPhone quando a atualização for entregue, a UI do Live Activity atualizada deslizará para baixo e será exibida como uma notificação por push.</li><li>Se uma <code>notificação</code> for incluída e o usuário não estiver ativo no iPhone, a tela se acenderá para exibir a Live Activity UI atualizada na tela de bloqueio.</li><li>O <code>alerta de notificação</code> não será exibido como uma notificação push padrão. Além disso, se um usuário tiver um dispositivo proxy, como um Apple Watch, o <code>alerta</code> será exibido nele.</li></ul>{:/} |
| `external_user_ids` | Opcional se `segment_id` ou `audience` for fornecido | Matriz de strings | Consulte [ID de usuário externo]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields). Máximo de 50 IDs de usuários externos.  |
| `segment_id `  | Opcional se `external_user_ids` ou `audience` for fornecido | String    | Consulte [identificador de segmento]({{site.baseurl}}/api/identifier_types/). |
| `custom_audience` | Opcional se `external_user_ids` ou `segment_id` for fornecido | Objeto do público conectado  | Veja [público conectado]({{site.baseurl}}/api/objects_filters/connected_audience/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Exemplo de solicitação

```json
curl --location --request POST 'https://rest.iad-01.braze.com/messages/live_activity/start' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {YOUR-REST-API-KEY}' \
--data-raw '{
    "app_id": "{YOUR-APP-API-IDENTIFIER}",
    "activity_id": "football-chiefs-bills-2024-01-21",
    "content_state": {
        "teamOneScore": 0,
        "teamTwoScore": 0
    },
    "activity_attributes_type": "FootballActivity",
    "activity_attributes": {
        "team1Name": "Chiefs",
        "team2Name": "Bills"
    },
    "dismissal_date": "2024-01-22T00:00:00+0000",
    "stale_date": "2024-01-22T16:55:49+0000",
    "notification": {
        "alert": {
            "body": "The game is starting! Tune in soon!",
            "title": "Chiefs v. Bills"
        }
    },
    // One of the following required:
    "segment_id": "{YOUR-SEGMENT-API-IDENTIFIER}", // Optional
    "custom_audience": {...}, // Optional
    "external_user_ids": ["user-id1", "user-id2"], // Optional
}'
```

## Resposta

Existem dois códigos de status para este endpoint: `201` e `4XX`.

### Exemplo de resposta bem-sucedida

Um código de status `201` é retornado se a solicitação foi formatada corretamente e recebemos a solicitação. O código de status `201` pode retornar o seguinte corpo de resposta.

```json
{
  "message": "success"
}
```

### Exemplo de resposta de erro

A classe de código de status `4XX` indica um erro do cliente. Consulte o artigo [erros e respostas da API]({{site.baseurl}}/api/errors/) para saber mais sobre os erros que você pode encontrar.

O código de status `400` pode retornar o seguinte corpo de resposta. 

```json
{
    "error": "\nProblem:\n  message body does not match declared format\nResolution:\n  when specifying application/json as content-type, you must pass valid application/json in the request's 'body' "
}
```

{% endapi %}
