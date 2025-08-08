---
nav_title: "POST: Atualizar Atividade ao Vivo"
article_title: "POST: Atualizar Atividade ao Vivo"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "Este artigo traz informações sobre o endpoint \"Atualizar atividade ao vivo\"."

---
{% api %}
# Atualizar Atividade ao Vivo
{% apimethod post %}
/messages/live_activity/update
{% endapimethod %}

> Use este endpoint para atualizar e encerrar [Atividades ao Vivo]({{site.baseurl}}/developer_guide/push_notifications/live_notifications/?sdktab=swift) exibidas pelo seu app iOS. Este endpoint requer configuração adicional.

Depois de registrar uma Atividade ao Vivo, você pode passar uma carga útil JSON para atualizar seu serviço de Notificações por Push da Apple (APNs). Consulte a documentação da Apple sobre [atualizar sua Atividade ao Vivo com payloads de notificação por push](https://developer.apple.com/documentation/activitykit/updating-and-ending-your-live-activity-with-activitykit-push-notifications) para saber mais.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#2300226e-f26a-4154-9bcc-5883f1f294cd {% endapiref %}

## Pré-requisitos

Para usar este endpoint, você precisará concluir o seguinte:

- Gere uma chave de API com a permissão `messages.live_activity.update`.
- Registre uma Atividade ao Vivo [remotamente]({{site.baseurl}}/developer_guide/push_notifications/live_notifications/?tab=remote&sdktab=swift) ou [localmente]({{site.baseurl}}/developer_guide/push_notifications/live_notifications/?tab=local&sdktab=swift) usando o Braze SWIFT SDK.

{% multi_lang_include api/payload_size_alert.md %}

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='default' %}

## Corpo da solicitação

```json
{
   "app_id": "(required, string) App API identifier retrieved from the Developer Console.",
   "activity_id": "(required, string) When you register your Live Activity using launchActivity, you use the pushTokenTag parameter to name the Activity’s push token to a custom string. Set activity_id to this custom string to define which Live Activity you want to update.",
   "content_state": "(required, object) You define the ContentState parameters when you create your Live Activity. Pass the updated values for your ContentState using this object. The format of this request must match the shape you initially defined.",
   "end_activity": "(optional, boolean) If true, this request ends the Live Activity.",
   "dismissal_date": "(optional, datetime in ISO-8601 format) The time to remove the Live Activity from the user’s UI. If this time is in the past, the Live Activity will be removed immediately.",
   "stale_date": "(optional, datetime in ISO-8601 format) The time the Live Activity content is marked as outdated in the user’s UI.",
   "notification": "(optional, object ) Include an `apple_push` object to define a push notification that creates an alert for the user."
 }
 ```

## Parâmetros de solicitação

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
|---|---|---|---|
| `app_id` | Obrigatória | String | [Identificador da API]({{site.baseurl}}/api/identifier_types/#the-app-identifier) do app recuperado da página [Chaves da API]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/).  |
| `activity_id` | Obrigatória | String | Quando você registra sua Atividade ao Vivo usando [`launchActivity`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/liveactivities-swift.class), você usa o parâmetro `pushTokenTag` para nomear o token por push da Atividade para uma string personalizada.<br><br>Defina `activity_id` para esta string personalizada para definir qual Atividade ao Vivo você deseja atualizar. |
| `content_state` | Obrigatória | Objeto | Você define os `ContentState` parâmetros quando cria sua Atividade ao Vivo. Passe os valores atualizados para o seu `ContentState` usando este objeto.<br><br>O formato desta solicitação deve corresponder à forma que você definiu inicialmente. |
| `end_activity` | Opcional | Booleano | Em caso de `true`, esta solicitação encerra a Atividade ao Vivo. |
| `dismissal_date` | Opcional | Datetime <br>(string [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)) | Este parâmetro define o tempo para remover a Atividade ao Vivo da interface do usuário. Se este horário estiver no passado e `end_activity` for `true`, a Atividade ao Vivo será removida imediatamente.<br><br> Se `end_activity` for `false` ou omitido, este parâmetro apenas atualiza a Atividade ao Vivo.|
| `stale_date` | Opcional | Datetime <br>(string [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)) | Este parâmetro informa ao sistema quando o conteúdo da Atividade ao Vivo é marcado como desatualizado na interface do usuário. |
| `notification` | Opcional | Objeto | Inclua um [`apple_push`]({{site.baseurl}}/api/objects_filters/messaging/apple_object/) objeto para definir uma notificação por push. Esse comportamento dessa notificação por push depende se o usuário está ativo ou se o usuário está usando um dispositivo proxy. {::nomarkdown}<ul><li>Se um <code>notification</code> está incluído e o usuário está ativo em seu iPhone quando a atualização é entregue, a interface de atividade ao vivo atualizada deslizará para baixo e será exibida como uma notificação por push.</li><li>Se um <code>notification</code> está incluído e o usuário não está ativo em seu iPhone, sua tela acenderá para exibir a interface de Atividade ao Vivo atualizada em sua tela de bloqueio.</li><li>O <code>notification alert</code> não será exibido como uma notificação por push padrão. Além disso, se um usuário tiver um {dispositivo} proxy, como um Apple Watch, o <code>alert</code> será exibido lá.</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Exemplo de solicitação

```json
curl --location --request POST 'https://rest.iad-01.braze.com/messages/live_activity/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {YOUR-REST-API-KEY}' \
--data-raw '{
    "app_id": "{YOUR-APP-API-IDENTIFIER}",
    "activity_id": "live-activity-1",
    "content_state": {
        "teamOneScore": 2,
        "teamTwoScore": 4
    },
    "end_activity": false,
    "dismissal_date": "2023-02-28T00:00:00+0000",
    "stale_date": "2023-02-27T16:55:49+0000",
    "notification": {
        "alert": {
            "body": "It's halftime! Let's look at the scores",
            "title": "Halftime"
        }
    }
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
