---
nav_title: "Objeto da Apple"
article_title: Objeto de envio de mensagens da Apple
page_order: 1
page_type: reference
channel: push
platform: iOS
description: "Este artigo de referência lista e explica os diferentes objetos Apple usados no Braze."

---

# Objeto push da Apple

> O objeto `apple_push` permite que você defina ou solicite informações relacionadas ao conteúdo do Apple Push e do Apple Push Alert por meio de nossos [endpoints de envio de mensagens]({{site.baseurl}}/api/endpoints/messaging).

## Objeto push da Apple

```json
{
   "badge": (optional, integer) the badge count after this message,
   "alert": (required unless content-available is true, string or Apple Push Alert Object) the notification message,
   // Specifying "default" in the sound field will play the standard notification sound
   "sound": (optional, string) the location of a custom notification sound within the app,
   "extra": (optional, object) additional keys and values to be sent,
   "content-available": (optional, boolean) if set, Braze will add the "content-available" flag to the push payload,
   "interruption_level": (optional, string: "passive", "active", "time-sensitive", or "critical") specifies the interruption level passed (iOS 15+),
   "relevance_score": (optional, float) specifies the relevance score between 0.0 and 1.0 used for grouping notification summaries (iOS 15+),
   "expiry": (optional, ISO 8601 date string) if set, push messages will expire at the specified datetime,
   "custom_uri": (optional, string) a web URL, or Deep Link URI,
   "use_webview": (optional, boolean) whether to open the web URL inside the app if the action is "URI", defaults to true,
   "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under (must be an iOS Push Message),
   "notification_group_thread_id": (optional, string) the notification group thread ID the notification will be sent with,
   "asset_url": (optional, string) content URL for rich notifications for devices using iOS 10 or higher,
   "asset_file_type": (required if asset_url is present, string) file type of the asset - one of "aif", "gif", "jpg", "m4a", "mp3", "mp4", "png", or "wav",
   "collapse_id": (optional, string) To update a notification on the user's device after you've issued it, send another notification with the same collapse ID you used previously
   "mutable_content": (optional, boolean) if true, Braze will add the mutable-content flag to the payload and set it to 1. The mutable-content flag is automatically set to 1 when sending a rich notification, regardless of the value of this parameter.
   "send_to_most_recent_device_only": (optional, boolean) defaults to false, if set to true, Braze will only send this push to a user's most recently used iOS device, rather than all eligible iOS devices,
   "category": (optional, string) the iOS notification category identifier for displaying push action buttons,
   "buttons" : (optional, array of Apple push action button objects) push action buttons to display,
   "apns_priority": (optional, integer) override the default apns_priority value using an integer between 1 and 10; use 10 for immediate delivery, 5 for power-aware delivery, and 1 to minimize power impact and avoid waking the device,
}
```

É necessário incluir um objeto Apple push no site `messages` se quiser que os usuários que você direcionou recebam um push em seus dispositivos iOS. O número total de bytes em sua string `alert`, no objeto `extra` e em outros parâmetros opcionais não deve exceder 1912. A API de envio de mensagens retornará um erro se você exceder o tamanho de mensagem permitido pela Apple. As mensagens que incluírem as chaves `ab` ou `aps` no objeto `extra` serão rejeitadas.

{% alert note %}
Se estiver enviando o objeto de push da Apple como parte de uma carga útil de atividades ao vivo, inclua a string `sound` no objeto `alert`.
{% endalert %}

### Objeto de alerta push da Apple

Na maioria dos casos, `alert` pode ser especificado como uma string em um objeto `apple_push`.

```json
{
   "body": (required unless content-available is true in the Apple Push Object, string) the text of the alert message,
   "title": (optional, string) a short string describing the purpose of the notification, displayed as part of the Apple Watch notification interface,
   "title_loc_key": (optional, string) the key to a title string in the `Localizable.strings` file for the current localization,
   "title_loc_args": (optional, array of strings) variable string values to appear in place of the format specifiers in title_loc_key,
   "action_loc_key": (optional, string) if a string is specified, the system displays an alert that includes the Close and View buttons, the string is used as a key to get a localized string in the current localization to use for the right button's title instead of "View",
   "loc_key": (optional, string) a key to an alert-message string in a Localizable.strings file for the current localization,
   "loc_args": (optional, array of strings) variable string values to appear in place of the format specifiers in loc_key,
   "sound": (optional, string) the location of a custom notification sound within the app (live activities only),
}
```

#### Exemplo

```json
{
  "broadcast": false,
  "external_user_ids": ["PushTest12"],
  "campaign_id": "9c2fefcd-9115-3932-f771-c7f43d18d6b6",
  "override_frequency_capping": "false",
  "recipient_subscription_state": "all",
  "messages": {
    "apple_push": {
      "alert": {
        "title": "Hello!",
        "body": "Message here"
      },
      "message_variation_id": "iosPush-640"
    }
  }
}
```

## Objeto de botão de ação por push da Apple

Você deve incluir o campo `category` no objeto Apple push para usar os botões de ação por push do iOS. A inclusão do campo `category` exibirá todos os botões de ação por push associados; inclua o campo `buttons` somente se quiser definir adicionalmente as ações de clique individuais dos botões. O SDK da Braze fornece um conjunto de botões de ação por push padrão para você usar, mostrado na tabela a seguir. Você também pode usar seus próprios botões se eles tiverem sido registrados no app.

### Objeto de botão de ação por push da Apple para os botões padrão do Braze

| Identificador de categoria   | Texto do botão | Identificador de ação do botão | Ações permitidas         |
|-----------------------|-------------|--------------------------|-------------------------|
| `ab_cat_accept_decline` | Aceitar      | `ab_pb_accept`             | OPEN_APP, URI ou DEEP_LINK |
| `ab_cat_accept_decline` | Recusar     | `ab_pb_decline`            | FECHAR                   |
| `ab_cat_yes_no`         | Sim         | `ab_pb_yes`                | OPEN_APP, URI ou DEEP_LINK |
| `ab_cat_yes_no`         | Não          | `ab_pb_no`                 | FECHAR                   |
| `ab_cat_confirm_cancel` | Confirmar     | `ab_pb_confirm`            | OPEN_APP, URI ou DEEP_LINK |
| `ab_cat_confirm_cancel` | Cancelar      | `ab_pb_cancel`             | FECHAR                   |
| `ab_cat_more`           | Mais        | `ab_pb_more`               | OPEN_APP, URI ou DEEP_LINK |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

```json
{
  "action_id": (required, string) the button's action identifier,
  "action": (optional, string) one of "OPEN_APP", "URI", "DEEP_LINK", or "CLOSE". Defaults to either "OPEN_APP" or "CLOSE" depending on the button,
  "uri": (optional, string) a web URL or Deep Link URI,
  "use_webview": (optional, boolean) whether to open the web URL inside the app if the action is "URI", defaults to true
}
```

### Objeto de botão de ação por push da Apple para categorias definidas por seu app

```json
{
  "action_id": (required, string) the button's action identifier,
  "action": (required, string) one of "URI" or "DEEP_LINK",
  "uri": (required, string) a web URL or Deep Link URI,
  "use_webview": (optional, boolean) whether to open the web URL inside the app if the action is "URI", defaults to true
}
```
