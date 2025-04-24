---
nav_title: Conector do Currents personalizado
alias: /currents_connector/
hidden: true
---

# Conector do Conector personalizado para parceiros

## Serialização e formato de dados

O formato de dados alvo é JSON sobre HTTPS. Os eventos serão agrupados em lotes de 100 eventos por padrão e enviados para o endpoint como um array JSON contendo todos os eventos. Os lotes serão enviados no seguinte formato:

`{"events": [event1, event2, event3, etc...]}`

Haverá um objeto JSON de nível superior com a chave "events" que mapeia para uma matriz de outros objetos JSON, cada um representando um único evento.

Os seguintes exemplos são para eventos _individuais_ (como se fossem parte de um conjunto maior de objetos JSON, com cada objeto JSON representando um único evento no lote).

### Eventos associados à campanha

Aqui estão alguns exemplos de cargas úteis de eventos para vários eventos, como apareceriam se estivessem associados a uma campanha:

```
// In-App Message Click: users.messages.inappmessage.Click
{
  "event_type": "users.messages.inappmessage.Click",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "device_id": "fedcba87-6543-210f-edc-ba9876543210",
    "timezone": "America/Chicago"
  },
  "properties": {
    "app_id": "01234567-89ab-cdef-0123-456789abcdef",
    "campaign_id": "11234567-89ab-cdef-0123-456789abcdef",
    "campaign_name": "Test Campaign",
    "message_variation_id": "c1234567-89ab-cdef-0123-456789abcdef",
    "message_variation_name": "Test Message Variation",
    "platform": "android",
     "os_version": "Android (N)",
    "device_model": "Nexus 5X",
    "button_id": "0",
    "send_id": "f123456789abcdef01234567"
  }
}
```

```
// Push Notification Send: users.messages.pushnotification.Send
{
  "event_type": "users.messages.pushnotification.Send",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "device_id": "fedcba87-6543-210f-edc-ba9876543210",
    "timezone": "America/Chicago"
  },
  "properties": {
    "app_id": "01234567-89ab-cdef-0123-456789abcdef",
    "platform": "ios",
    "campaign_id": "11234567-89ab-cdef-0123-456789abcdef",
    "campaign_name": "Test Campaign",
    "message_variation_id": "c1234567-89ab-cdef-0123-456789abcdef",
    "message_variation_name": "Test Message Variation",
    "send_id": "f123456789abcdef01234567",
    "dispatch_id": "01234567-89ab-cdef-0123-456789abcdef"
  }
}
```

```
// Email Open: users.messages.email.Open
{
  "event_type": "users.messages.email.Open",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "timezone": "America/Chicago"
  },
  "properties": {
    "campaign_id": "11234567-89ab-cdef-0123-456789abcdef",
    "campaign_name": "Test Campaign",
    "dispatch_id": "12345qwert",
    "message_variation_id": "c1234567-89ab-cdef-0123-456789abcdef",
    "message_variation_name": "Test Message Variation",
    "email_address": "test@test.com",
    "send_id": "f123456789abcdef01234567",
    "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
  }
}
```

```
// SMS Delivery: users.messages.sms.Delivery
{
  "event_type": "users.messages.sms.Delivery",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "timezone": "America/Chicago"
  },
  "properties": {
    "campaign_id": "11234567-89ab-cdef-0123-456789abcdef",
    "campaign_name": "Test Campaign",
    "dispatch_id": "12345qwert",
    "message_variation_id": "c1234567-89ab-cdef-0123-456789abcdef",
    "message_variation_name": "Test Message Variation",
    "to_phone_number": "+16462345678",
    "subscription_group_id": "41234567-89ab-cdef-0123-456789abcdef",
    "from_phone_number": "+12123470922"
  }
}
```

### Eventos associados à canva

Aqui estão alguns exemplos de cargas úteis de eventos para vários eventos, como apareceriam se associados a uma canva:

```
// In-App Message Click: users.messages.inappmessage.Click
{
  "event_type": "users.messages.inappmessage.Click",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "device_id": "fedcba87-6543-210f-edc-ba9876543210",
    "timezone": "America/Chicago"
  },
  "properties": {
    "app_id": "01234567-89ab-cdef-0123-456789abcdef",
    "canvas_id": "11234567-89ab-cdef-0123-456789abcdef",
    "canvas_name": "My Cool Campaign",
    "canvas_variation_id": "31234567-89ab-cdef-0123-456789abcdef",
    "canvas_step_id": "41234567-89ab-cdef-0123-456789abcdef",
    "platform": "android",
    "os_version": "Android (N)",
    "device_model": "Nexus 5X",
    "button_id": "0",
    "send_id": "f123456789abcdef01234567"
  }
}
```

```
// Push Notification Send: users.messages.pushnotification.Send
{
  "event_type": "users.messages.pushnotification.Send",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "device_id": "fedcba87-6543-210f-edc-ba9876543210",
    "timezone": "America/Chicago"
  },
  "properties": {
    "app_id": "01234567-89ab-cdef-0123-456789abcdef",
    "platform": "ios",
    "canvas_id": "11234567-89ab-cdef-0123-456789abcdef",
    "canvas_name": "My Cool Campaign",
    "canvas_variation_id": "31234567-89ab-cdef-0123-456789abcdef",
    "canvas_step_id": "41234567-89ab-cdef-0123-456789abcdef",
    "send_id": "f123456789abcdef01234567",
    "dispatch_id": "01234567-89ab-cdef-0123-456789abcdef"
  }
}
```

```
// Email Open: users.messages.email.Open
{
  "event_type": "users.messages.email.Open",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "timezone": "America/Chicago"
  },
  "properties": {
    "canvas_id": "11234567-89ab-cdef-0123-456789abcdef",
    "canvas_name": "My Cool Canvas",
    "canvas_variation_id": "31234567-89ab-cdef-0123-456789abcdef",
    "canvas_step_id": "41234567-89ab-cdef-0123-456789abcdef",
    "dispatch_id": "12345qwert",
    "email_address": "test@test.com",
    "send_id": "f123456789abcdef01234567",
    "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
  }
}
```

```
// SMS Delivery: users.messages.sms.Delivery
{
  "event_type": "users.messages.sms.Delivery",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "timezone": "America/Chicago"
  },
  "properties": {
    "canvas_id": "11234567-89ab-cdef-0123-456789abcdef",
    "canvas_name": "My Cool Canvas",
    "canvas_variation_id": "31234567-89ab-cdef-0123-456789abcdef",
    "canvas_step_id": "41234567-89ab-cdef-0123-456789abcdef",
    "dispatch_id": "12345qwert",
    "to_phone_number": "+16462345678",
    "subscription_group_id": "41234567-89ab-cdef-0123-456789abcdef",
    "from_phone_number": "+12123470922"
  }
}
```

### Outros eventos

Aqui estão alguns exemplos de cargas úteis de eventos para vários outros eventos que não estão associados nem a campanhas nem a canvas:

```
// Custom Event: users.behaviors.CustomEvent
{
  "event_type": "users.behaviors.CustomEvent",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "device_id": "fedcba87-6543-210f-edc-ba9876543210",
    "timezone": "America/Chicago"
  },
  "properties": {
    "app_id": "01234567-89ab-cdef-0123-456789abcdef",
    "platform": "ios",
    "os_version": "iOS 10.3.1",
    "device_model": "iPhone 7 Plus",
    "name": "custom event name",
    "ad_id": "01234567-89ab-cdef-0123-456789abcdef",
    "ad_id_type": "roku_ad_id",
    "ad_tracking_enabled": true,
    "custom_properties": {
      "string property name": "a",
      "number property name": 1,
      "list property name": ["a", "b"]
    }
  }
}
```

```
// Purchase Event: users.behaviors.Purchase
{
  "event_type": "users.behaviors.Purchase",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id"
    "device_id": "fedcba87-6543-210f-edc-ba9876543210",
    "timezone": "America/Chicago"
  },
  "properties": {
    "app_id": "01234567-89ab-cdef-0123-456789abcdef",
    "platform": "ios",
    "os_version": "iOS 10.3.1",
    "device_model": "iPhone 7 Plus",
    "product_id": "1234",
    "price": 12.34,
    "currency": "AED,
    "ad_id": "01234567-89ab-cdef-0123-456789abcdef",
    "ad_id_type": "roku_ad_id",
    "ad_tracking_enabled": true,
    "purchase_properties": {
      "string property name": "a",
      "number property name": 1,
      "list property name": ["a", "b"]
    }
  }
}
```

```
// Session Start: users.behaviors.app.SessionStart
{
  "event_type": "users.behaviors.app.SessionStart",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "device_id": "fedcba87-6543-210f-edc-ba9876543210"
  },
  "properties": {
    "app_id": "01234567-89ab-cdef-0123-456789abcdef",
    "platform": "ios",
    "os_version": "iOS 10.3.1",
    "device_model": "iPhone 7 Plus",
    "session_id": "b1234567-89ab-cdef-0123-456789abcdef"
  }
}
```

## Autenticação

Se necessário, a autenticação será realizada passando um token no cabeçalho HTTP `Authorization`, via o esquema de autorização `Bearer`, conforme especificado em [RFC 6750](https://tools.ietf.org/html/rfc6750#section-2.1). No futuro, Braze pode optar por usar o `Authorization` cabeçalho para implementar um esquema de autorização de par chave-valor personalizado (único para Braze) em conformidade com [RFC 7235](https://tools.ietf.org/html/rfc7235) (que é como, por exemplo, o esquema de autenticação personalizado da AWS funciona).

De acordo com a RFC 6750, o token deve ser um valor codificado em Base64 com pelo menos um caractere Uma peculiaridade notável da RFC 6750 é que ela permite que o token contenha os seguintes caracteres além dos caracteres normais da Base64: "-", ".", "_", e "~". Os parceiros e clientes são livres para decidir se incluem ou não esses caracteres em seu token. Nota que os clientes são obrigados a fornecer este token em formato Base64; Braze não realizará essa codificação do nosso lado.

De acordo com a RFC 6750, o cabeçalho, se houver, será construído usando o seguinte formato:

`"Authorization: Bearer " + <token>`

Então, por exemplo, se o token da API for `0p3n5354m3==`, o cabeçalho de autorização ficará assim:

`Authorization: Bearer 0p3n5354m3==`

## Versão

Todas as solicitações de nossos Conectores HTTP Integráveis serão enviadas com um cabeçalho personalizado designando a versão da solicitação Currents que está sendo feita:

`Braze-Currents-Version: 1`

A versão será sempre `1`, a menos que façamos alterações severamente incompatíveis com versões anteriores na carga útil ou na semântica da solicitação. Nós não esperamos incrementar esse número com muita frequência, se é que isso vai acontecer.

Os eventos individuais seguirão as mesmas regras de evolução que nossos esquemas Avro S3 existentes para Currents Data Export. Ou seja, os campos de cada evento serão garantidos para serem compatíveis com versões anteriores dos payloads de eventos de acordo com a definição Avro de compatibilidade retroativa, incluindo as seguintes regras:

- Campos de eventos específicos são garantidos para sempre ter o mesmo tipo de dado ao longo do tempo.
- Qualquer novo campo que seja adicionado à carga útil ao longo do tempo deve ser considerado opcional por todas as partes.
- Os campos obrigatórios nunca serão removidos.

## Mecanismo de tratamento de erros e novas tentativas

No caso de um erro, a Braze colocará a solicitação na fila e tentará repeti-la com base no código de retorno HTTP recebido. Qualquer código de erro HTTP não listado abaixo será tratado como um erro HTTP 5XX.

{% alert important %}
Se o nosso mecanismo de repetição falhar em entregar eventos ao seu endpoint por mais de 24 horas, haverá perda de dados.
{% endalert %}

Os seguintes códigos de status HTTP serão reconhecidos pelo nosso cliente conector:
- **2XX** — Sucesso
  - Os dados do evento não serão reenviados.<br><br>
- **5XX** — Erro no servidor
  - Os dados do evento serão reenviados em um padrão de recuo exponencial com jitter. Se os dados não forem enviados com sucesso dentro de 24 horas, eles serão descartados.<br><br>
- **400** — Erro do lado do cliente
  - Nosso conector de alguma forma enviou pelo menos um evento malformado. Se isso ocorrer, os dados do evento serão divididos em lotes de tamanho 1 e reenviados. Qualquer evento nesses lotes de tamanho 1 que receber uma resposta HTTP 400 adicional será descartado permanentemente. Os parceiros e/ou clientes devem nos informar se detectarem isso ocorrendo no lado deles.<br><br>
- **401** (Não autorizado), **403** (Proibido), **404**
  - O conector foi configurado com credenciais inválidas. Os dados do evento serão reenviados após uma postergação de entre 2 e 5 minutos. Se o problema não for resolvido pelo cliente dentro de 48 horas, os dados do evento serão descartados.<br><br>
- **413** — Carga Útil Muito Grande
  - Os dados do evento serão divididos em lotes menores e reenviados.<br><br>
- **429** — Muitas Solicitações
  - Indica limitação de taxa. Os dados do evento serão reenviados em um padrão de recuo exponencial com jitter. Se os dados não forem enviados com sucesso dentro de 24 horas, eles serão descartados.