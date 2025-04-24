---
nav_title: "Objeto do Windows"
article_title: Objeto de envio de mensagens do Windows
page_order: 14
page_type: reference
channel: push
platform:
  - Windows Universal
description: "Este artigo de referência lista e explica os diferentes objetos do Windows usados na Braze."
hidden: true
---
# Especificação do objeto do Windows

Os objetos `windows_phone8_push` e `windows_universal_push` são usados para definir ou solicitar informações relacionadas ao conteúdo de Push do Windows Phone 8 e Push Universal do Windows via nossos [envio de mensagens]({{site.baseurl}}/api/endpoints/messaging) endpoints.

## objeto push do Windows Phone 8

```json
{
   "push_type": (optional, string) must be "toast",
   "toast_title": (optional, string) the notification title,
   "toast_content": (required, string) the notification message,
   "toast_navigation_uri": (optional, string) page uri to send user to,
   "toast_hash": (optional, object) additional keys and values to send,
   "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under (must be a Windows Phone 8 Push Message)
}
```

## Objeto de push universal do Windows

Consulte o catálogo de [modelos de notificação toast][32] do Windows Universal para obter detalhes sobre as opções para `push_type`.

```json
{
   "push_type": (required, string) one of: "toast_text_01", "toast_text_02", "toast_text_03", "toast_text_04", "toast_image_and_text_01", "toast_image_and_text_02", "toast_image_and_text_03", or "toast_image_and_text_04",
   "toast_text1": (required, string) the first line of text in the template,
   "toast_text2": (optional, string) the second line of text (for templates with > 1 line of text),
   "toast_text3": (optional, string) the third line of text (for the *_04 templates),
   "toast_text_img_name": (optional, string) the path for the image for the templates that include an image,
   "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under (must be a Windows Universal Push Message),
   "extra_launch_string": (optional, string) used to add deep linking functionality by passing extra values to the launch string
}
```

Para saber mais sobre o uso do parâmetro `extra_launch_string` para [deep linking][38], consulte [Deep linking com Windows Universal.][37]

[32]: https://msdn.microsoft.com/en-us/library/windows/apps/hh761494.aspx
[37]: {{site.baseurl}}/developer_guide/platform_integration_guides/windows_universal/push_notifications/integration/#step-4-deep-linking-from-push-into-your-app
[38]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking
