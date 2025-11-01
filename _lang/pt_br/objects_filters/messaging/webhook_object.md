---
nav_title: "Objeto de webhook"
article_title: Objeto de envio de mensagens de webhook
page_order: 13
page_type: reference
channel: 
  - webhook
description: "Este artigo de referência descreve o objeto webhook do Braze."

---

# Objeto de webhook

> O objeto `webhook` permite que você modifique ou crie mensagens de webhook por meio de nossos [endpoints de envio de mensagens]({{site.baseurl}}/api/endpoints/messaging).

```json
{
  "url": (required, string),
  "request_method": (required, string) one of "POST", "PUT", "DELETE", or "GET",
  "request_headers": (optional, Hash) key-value pairs to use as request headers,
  "body": (optional, string) if you want to include a JSON object, make sure to escape quotes and backslashes,
  "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under
}
```

Como prática recomendada, a Braze recomenda fornecer um valor explícito para `Content-Type` no campo `request_headers` para um comportamento consistente e com previsão, já que os remetentes e servidores podem mudar com o tempo. Se um valor não for especificado para o cabeçalho `Content-Type`, ele será inferido do corpo da solicitação.
