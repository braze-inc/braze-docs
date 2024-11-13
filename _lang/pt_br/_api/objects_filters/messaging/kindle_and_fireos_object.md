---
nav_title: "Objeto push do Kindle e do FireOS"
article_title: Objeto de envio de mensagens push para Kindle e FireOS
page_order: 7
page_type: reference
channel: push
platform:
  - Android
  - FireOS
description: "Este artigo de referência explica os diferentes componentes do objeto push do Braze Kindle e do FireOS."

---

# Objeto push do Kindle e do FireOS

> O objeto `kindle_push` permite que você modifique ou crie notificações por push do Kindle e do FireOS por meio de nossos [endpoints de envio de mensagens]({{site.baseurl}}/api/endpoints/messaging).

```json
{
   "alert": (required, string) the notification message,
   "title": (required, string) the title that appears in the notification drawer,
   "extra": (optional, object) additional keys and values to be sent in the push,
   "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under (must be an Kindle/FireOS Push Message),
   "priority": (optional, integer) the notification priority value,
   "collapse_key": (optional, string) the collapse key for this message,
   // Specifying "default" in the sound field will play the standard notification sound
   "sound": (optional, string) the location of a custom notification sound within the app,
   "custom_uri": (optional, string) a web URL, or Deep Link URI
}
```

O parâmetro `priority` aceitará valores de `-2` a `2`, em que `-2` representa a prioridade mais baixa e `2` representa a prioridade mais alta. `0` é o valor padrão. Quaisquer valores enviados que estejam fora desse intervalo de números inteiros terão como padrão o endereço `0`.
