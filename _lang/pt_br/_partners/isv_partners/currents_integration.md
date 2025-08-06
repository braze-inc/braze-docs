---
nav_title: Conector do Currents personalizado
alias: /currents_connector/
hidden: true
---

# Conector Currents personalizado

> Saiba como integrar um conector Currents personalizado, para que você possa obter dados de eventos do Braze em tempo real, ativando análises, relatórios e automação mais personalizados.

## Pré-requisitos

Para integrar um conector Currents personalizado no Braze, você precisará fornecer um URL de endpoint e um [token de autenticação opcional](#authentication).

Além disso, se você tiver mais de um grupo de app no Braze, precisará configurar um conector Currents personalizado para cada grupo. No entanto, você pode apontar todos os grupos de app para o mesmo endpoint ou para um endpoint com um parâmetro `GET` adicional, como `your_app_group_key=”Brand A”`.

## Prevenção da perda de dados

### Monitoramento de erros

Para evitar a perda de dados e a interrupção do serviço, é essencial que você monitore seus endpoints o tempo todo e procure resolver os erros graves ou o tempo de inatividade dentro de 24 horas.

Para a maioria dos tipos de erro (como erros de servidor, erros de conexão de rede, etc.), o Braze continuará a enfileirar e tentar novamente as transmissões de eventos por até 24 horas. Após esse tempo, os eventos não transmitidos serão descartados. Os conectores com taxas de erro ou tempo de atividade consistentemente ruins serão automaticamente suspensos.

### Mudar a resiliência

Ocasionalmente, faremos alterações ininterruptas nos esquemas do Braze Currents. As alterações não significativas são novas colunas anuláveis ou tipos de eventos.

Normalmente, avisamos com duas semanas de antecedência sobre essas alterações, mas às vezes isso não é possível. É essencial que você projete sua integração para lidar com campos ou tipos de eventos não reconhecidos, caso contrário, isso provavelmente levará à perda de dados.

{% alert tip %}
Para obter a lista completa dos esquemas de eventos do Currents, acesse [Eventos de engajamento com mensagem]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events).
{% endalert %}

## Loteamento e serialização

O formato de dados alvo é JSON sobre HTTPS. Por padrão, os eventos são agrupados em grupos de 100 com base no seguinte:

- **Número de eventos em fila**: Por exemplo, se o tamanho do lote estiver configurado para 200 eventos e houver 200 eventos na fila.
- **Duração de um evento:** Normalmente, os eventos não são enfileirados se a duração for superior a 15 minutos. Cada tipo de evento tem uma fila separada, portanto, a latência pode variar entre os tipos de eventos.

Em seguida, os eventos são enviados ao endpoint como uma matriz JSON de todos os eventos no seguinte formato:

```json
{"events": [event1, event2, event3, etc...]}
```

Haverá um objeto JSON de nível superior com a chave `"events"` que mapeia para um vetor de outros objetos JSON, cada um representando um único evento.

## Exemplos de carga útil

Os exemplos a seguir mostram cargas úteis para eventos individuais, o que significa que as cargas úteis pertenceriam a um vetor maior de objetos JSON, em que cada objeto JSON representa um único evento no lote.

Além disso, sua estrutura varia ligeiramente da estrutura plana encontrada nos [eventos de engajamento com mensagens]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events). Em particular, eles contêm dois subobjetos:

|Nome|Descrição|
|----|-----------|
|`"user"`|Contém propriedades do usuário, como `user_id`, `external_user_id`, `device_id` e `timezone`.|
|`"properties"`|Contém atribuições de um evento, como o `app/campaign/canvas/platform` ao qual ele se aplica.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Se um ponto de extremidade downstream receber uma carga útil com zero eventos ou um corpo de solicitação vazio, o resultado deverá ser considerado um no-op, o que significa que nenhum efeito downstream deverá ocorrer a partir dessa chamada. No entanto, você ainda deve verificar o cabeçalho `Authorization` (como faria em uma chamada de API normal) e dar uma resposta HTTP apropriada para [credenciais inválidas](#authentication), como `401` ou `403`. Isso permite que o Braze saiba que as credenciais do conector são válidas.

### Eventos associados à campanha

Aqui estão alguns exemplos de cargas úteis de eventos para vários eventos, como apareceriam se estivessem associados a uma campanha:

#### Clique em mensagem no app

```json
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

#### Envio de notificações por push

```json
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

#### Abertura de e-mail

```json
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

#### Entrega de SMS

```json
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

#### Clique em mensagem no app

```json
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

#### Envio de notificações por push

```json
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

#### Abertura de e-mail

```json
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

#### Entrega de SMS

```json
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

#### Evento personalizado

```json
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

#### Evento de compra

```json
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

#### Início de sessão

```json
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

Os tokens de autenticação em sua carga útil são opcionais. Eles podem ser transmitidos por meio de um cabeçalho HTTP `Authorization` usando o esquema de autorização `Bearer`, conforme especificado na [RFC 6750](https://tools.ietf.org/html/rfc6750#section-2.1). Embora seja opcional, se um token de autenticação for passado, o Braze sempre o validará primeiro - mesmo que não haja eventos na carga útil.

De acordo com a RFC 6750, os tokens devem ser valores codificados em Base64 com pelo menos um caractere. Lembre-se de que a RFC 6750 permite que os tokens contenham os seguintes caracteres, além dos caracteres Base64 normais: `-`, `.`, `_`, e `~`. Você pode escolher se deseja ou não incluir esses caracteres em seu token; no entanto, ele deve estar no formato Base64.

Além disso, se o cabeçalho `Authorization` estiver presente, ele será construído usando o seguinte formato:

```plaintext
"Authorization: Bearer " + <token>
```

Por exemplo, se o token de autenticação for `0p3n5354m3==`, o cabeçalho `Authorization` deverá ser semelhante ao seguinte:

```plaintext
Authorization: Bearer 0p3n5354m3==
```

{% alert note %}
No futuro, poderemos usar os cabeçalhos `Authorization` para implementar um esquema de autorização personalizado, de par de valores-chave, exclusivo do Braze. Isso estaria de acordo com a especificação [RFC 7235](https://tools.ietf.org/html/rfc7235), que é a forma como algumas empresas implementam seus esquemas de autenticação, como a Amazon Web Services (AWS).
{% endalert %}

## Versão

Todas as solicitações de nossa integração do conector HTTP serão enviadas com um cabeçalho personalizado que designa a versão da solicitação do Currents que está sendo feita:

```plaintext
Braze-Currents-Version: 1
```

A versão será sempre `1` a menos que, como não esperamos incrementar esse número com muita frequência, se é que o faremos.

Assim como nossos [esquemas de armazenamento de data warehouse]({{site.baseurl}}/user_guide/data/braze_currents/event_delivery_semantics?redirected=1), cada campo de evento em um evento individual tem a garantia de ser compatível com versões anteriores da carga útil do evento, de acordo com a definição de compatibilidade com versões anteriores do [Apache Avro](https://avro.apache.org/):

1. Campos de eventos específicos são garantidos para sempre ter o mesmo tipo de dado ao longo do tempo.
2. Qualquer novo campo que seja adicionado à carga útil ao longo do tempo deve ser considerado opcional por todas as partes.
3. Os campos obrigatórios nunca serão removidos.

## Mecanismo de tratamento de erros e novas tentativas

Se ocorrer um erro, o Braze colocará a solicitação na fila e tentará novamente com base no código de retorno HTTP recebido. Ele continuará tentando novamente por pelo menos dois dias, desde que os dados estejam armazenados em buffer no sistema. Se os dados ficarem presos por mais de 24 horas, nossos engenheiros de plantão serão alertados automaticamente. Nesse momento, nossa estratégia de backoff é tentar novamente de forma periódica.

Se a integração do Currents começar a retornar erros de `4XX`, o Braze enviará automaticamente um e-mail de notificação e estenderá automaticamente o período de retenção para um mínimo de sete dias.

Qualquer código de erro HTTP não listado abaixo será tratado como um erro HTTP `5XX`.

{% alert warning %}
Se o mecanismo de repetição do Braze não conseguir entregar um evento por mais de 24 horas, ocorrerá perda de dados.
{% endalert %}

Os seguintes códigos de status HTTP serão reconhecidos pelo nosso cliente conector:

<table>
  <thead>
    <tr>
      <th>Código de status</th>
      <th>Resposta</th>
      <th>Descrição</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>2XX</code></td>
      <td>Deu certo</td>
      <td>Os dados do evento não serão reenviados.</td>
    </tr>
    <tr>
      <td><code>5XX</code></td>
      <td>Erro no lado do servidor</td>
      <td>Os dados do evento serão reenviados em um padrão de recuo exponencial com jitter. Se os dados não forem enviados com sucesso dentro de 24 horas, eles serão descartados.</td>
    </tr>
    <tr>
      <td><code>400</code></td>
      <td>Erro no lado do cliente</td>
      <td>O conector enviou pelo menos um evento malformado. Os dados do evento serão divididos em lotes de tamanho 1 e reenviados. Quaisquer eventos nesses lotes de tamanho 1 que recebam outro <code>400</code> a resposta será descartada permanentemente. Você deve relatar ocorrências repetidas.</td>
    </tr>
    <tr>
      <td><code>401</code></td>
      <td>Não autorizado</td>
      <td>O conector foi configurado com credenciais inválidas. Os dados do evento serão reenviados após uma postergação de 2 a 5 minutos. Se não for resolvido em 48 horas, os dados do evento serão descartados.</td>
    </tr>
    <tr>
      <td><code>403</code></td>
      <td>Proibido</td>
      <td>O conector foi configurado com credenciais inválidas. Os dados do evento serão reenviados após uma postergação de 2 a 5 minutos. Se não for resolvido em 48 horas, os dados do evento serão descartados.</td>
    </tr>
    <tr>
      <td><code>404</code></td>
      <td>Não encontrado</td>
      <td>O conector foi configurado com credenciais inválidas. Os dados do evento serão reenviados após uma postergação de 2 a 5 minutos. Se não for resolvido em 48 horas, os dados do evento serão descartados.</td>
    </tr>
    <tr>
      <td><code>413</code></td>
      <td>Carga útil muito grande</td>
      <td>Os dados do evento serão divididos em lotes menores e reenviados.</td>
    </tr>
    <tr>
      <td><code>429</code></td>
      <td>Muitas solicitações</td>
      <td>Indica limitação de taxa. Os dados do evento serão reenviados em um padrão de recuo exponencial com jitter. Se o envio não for bem-sucedido em 24 horas, ele será descartado.</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
