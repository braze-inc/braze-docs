---
nav_title: Evento de engajamento com mensagem
layout: message_engagement_events_glossary
alias: /message_events_glossary/
page_order: 5
excerpt_separator: ""
page_type: glossary
description: "Este glossário lista os vários Eventos de Engajamento com Mensagens que o Braze pode rastrear e enviar para Data Warehouses escolhidos usando Currents."
tool: Currents
search_rank: 6
---

Os esquemas de armazenamento se aplicam aos dados de eventos de arquivo simples que enviamos aos parceiros de armazenamento do Data Warehouse (Google Cloud Storage, Amazon S3 e Microsoft Azure Blob Storage). Para esquemas que se aplicam a outros parceiros, consulte nossa lista de [parceiros disponíveis]({{site.baseurl}}/user_guide/data/braze_currents/available_partners/) e verifique suas respectivas páginas.

Entre em contato com o gerente da sua conta ou abra um [ticket de suporte]({{site.baseurl}}/braze_support/) se precisar de acesso a direitos de eventos adicionais. Se não encontrar o que precisa neste artigo, consulte nossa [Biblioteca de eventos de comportamento do cliente]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/) ou nossos [exemplos de dados de amostra Currents](https://github.com/Appboy/currents-examples/tree/master/sample-data).

{% details Explicação da estrutura do evento de engajamento com mensagens e dos valores da plataforma %}

### Estrutura do evento

Esse detalhamento do evento mostra que tipo de informação geralmente é incluído em um evento de engajamento com mensagem. Com uma sólida compreensão de seus componentes, seus desenvolvedores e a equipe de estratégia de business intelligence podem usar os dados de eventos Currents recebidos para criar relatórios e gráficos orientados por dados e tirar proveito de outras métricas de dados valiosas.

![Detalhamento de um evento de engajamento com mensagem mostrando um evento de cancelamento de inscrição de e-mail com as propriedades listadas agrupadas por propriedades específicas do usuário, propriedades de rastreamento da campanha ou do Canvas e propriedades específicas do evento]({% image_buster /assets/img/message_engagement_event.png %})

Os eventos de engajamento com mensagens são compostos por propriedades **específicas do usuário**, propriedades de **rastreamento de campanha/canva** e propriedades **específicas do evento**.

### Esquema de ID de usuário

Note as convenções de nomenclatura para IDs de usuário.

| Esquema do Braze | Esquema de Currents | Descrição |
| ----------- | ----------- | ----------- |
| `braze_id` | `"USER_ID"` | O identificador exclusivo que é atribuído automaticamente pelo Braze. |
| `external_id` | `"EXTERNAL_USER_ID"` | O identificador exclusivo do perfil de um usuário que é definido pelo cliente. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Valores da plataforma

Certos eventos retornam um valor `platform` que especifica a plataforma do dispositivo do usuário.
<br>A tabela a seguir detalha os possíveis valores retornados:

| Dispositivo do usuário | Valor da plataforma |
| --- | --- |
| iOS | `ios` |
| Android | `android` |
| FireTV | `kindle` |
| Kindle | `kindle` |
| Web | `web` |
| tvOS | `tvos` |
| Roku | `roku` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% enddetails %}

{% alert important %}
O Currents descartará eventos com cargas úteis excessivamente grandes, superiores a 900 KB.
{% endalert %}

{% alert note %}
Os objetos relacionados ao Canvas Flow têm IDs que podem ser usados para agrupamento e traduzidos em nomes legíveis por meio do [endpoint Exportar detalhes do Canvas]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/).
{% endalert %}

{% alert note %}
Alguns campos podem levar mais tempo para exibir seu estado mais recente após a atualização de uma campanha ou do Canva. Esses campos são:
<ul>
  <li>"campaign_name" (nome da campanha)</li>
  <li>"canvas_name"</li>
  <li>"canvas_step_name"</li>
  <li>"conversion_behavior" (comportamento de conversão)</li>
  <li>"canvas_variation_name" (nome da variação da tela)</li>
  <li>"experiment_split_name"</li>
  <li>"message_variation_name" (nome da variação da mensagem)</li>
</ul>
Se for necessária uma consistência completa, recomendamos aguardar uma hora a partir da última atualização desses campos antes de enviar as mensagens aos usuários.
{% endalert %}
{% api %}
## Desinstalar eventos

{% apitags %}
Desinstalar
{% endapitags %}

Esse evento ocorre quando um usuário desinstala um app. Use esses dados para rastrear quando os usuários desinstalam um app. Embora esse seja atualmente um evento de engajamento com mensagem, ele será alterado para um evento de comportamento do usuário no futuro.

{% alert important %}
Esse evento não é disparado quando o usuário realmente desinstala o app, pois é impossível rastrear isso com exatidão. O Braze envia um push silencioso diário para determinar se o aplicativo ainda existe no dispositivo do usuário e, se recebermos um erro nesse push silencioso, presume-se que o app foi desinstalado.
{% endalert %}

{% tabs %}
{% tab Amplitude %}
```json
// Uninstall (users.behaviors.Uninstall)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Uninstall (users.behaviors.Uninstall)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Application Uninstalls (users.behaviors.Uninstall)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segmento %}
```json
// Application Uninstalled (users.behaviors.Uninstall)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_id" : "(optional, string) ID of the device on which the event occurred"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Armazenamento em nuvem %}
```json
// users.behaviors.Uninstall

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Eventos de mudança de estado da inscrição global

{% apitags %}
Inscrição
{% endapitags %}

Esse evento ocorre quando o Braze recebe uma solicitação para atualizar o estado de inscrição global do usuário, mesmo que a solicitação não altere o estado de inscrição atual do usuário.

{% tabs %}
{% tab Amplitude %}
```json
// Global Subscription State Change (users.behaviors.subscription.GlobalStateChange)

{
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "channel" : "(optional, string) Channel this event belongs to",
    "channel_identifier" : "(optional, string) [PII] The user's identifier on the channel the event is for.",
    "email_address" : "(optional, string) [PII] Email address of the user",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "state_change_source" : "(optional, string) Source of the state change, e.g: REST API, SDK, Dashboard, etc.",
    "subscription_status" : "(required, string) Subscription status: 'Subscribed', 'Unsubscribed' or 'Opted In'",
    "timezone" : "(optional, string) Time zone of the user"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Global Subscription State Change (users.behaviors.subscription.GlobalStateChange)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "channel" : "(optional, string) Channel this event belongs to",
    "channel_identifier" : "(optional, string) [PII] The user's identifier on the channel the event is for.",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "email_address" : "(optional, string) [PII] Email address of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "state_change_source" : "(optional, string) Source of the state change, e.g: REST API, SDK, Dashboard, etc.",
    "subscription_status" : "(required, string) Subscription status: 'Subscribed', 'Unsubscribed' or 'Opted In'",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Global Subscription State Changes (users.behaviors.subscription.GlobalStateChange)

{
  "device_info" : { },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "channel" : "(optional, string) Channel this event belongs to",
          "channel_identifier" : "(optional, string) [PII] The user's identifier on the channel the event is for.",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "state_change_source" : "(optional, string) Source of the state change, e.g: REST API, SDK, Dashboard, etc.",
          "subscription_status" : "(required, string) Subscription status: 'Subscribed', 'Unsubscribed' or 'Opted In'"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user",
    "email" : "(optional, string) [PII] Email address of the user"
  }
}
```
{% endtab %}

{% tab Segmento %}
```json
// Global Subscription State Changed (users.behaviors.subscription.GlobalStateChange)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : {
      "email" : "(optional, string) [PII] Email address of the user"
    },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "channel" : "(optional, string) Channel this event belongs to",
    "channel_identifier" : "(optional, string) [PII] The user's identifier on the channel the event is for.",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "state_change_source" : "(optional, string) Source of the state change, e.g: REST API, SDK, Dashboard, etc.",
    "subscription_status" : "(required, string) Subscription status: 'Subscribed', 'Unsubscribed' or 'Opted In'"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Armazenamento em nuvem %}
```json
// users.behaviors.subscription.GlobalStateChange

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "channel" : "(optional, string) Channel this event belongs to",
  "channel_identifier" : "(optional, string) [PII] The user's identifier on the channel the event is for.",
  "email_address" : "(optional, string) [PII] Email address of the user",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "state_change_source" : "(optional, string) Source of the state change, e.g: REST API, SDK, Dashboard, etc.",
  "subscription_status" : "(required, string) Subscription status: 'Subscribed', 'Unsubscribed' or 'Opted In'",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### Detalhes da propriedade

- `state_change_source` retornará uma string com o nome completo da fonte. Por exemplo, a importação do CSV de origem retornará a string `CSV Import`. As fontes disponíveis estão listadas abaixo:

| Origem | Descrição |
| --- | --- |
| SDK | Endpoints de SDK |
| Dashboard | Quando o estado da inscrição de um usuário é atualizado na página **Perfil do usuário** no dashboard |
| Página de inscrição | Quando um usuário cancela a inscrição por meio de um link de cancelamento de inscrição por e-mail que não seja a Central de Preferências |
| API REST | Pontos de extremidade da API REST |
| Importação de CSV | Importação de usuário CSV |
| Central de Preferências | Quando um usuário é atualizado a partir da Central de Preferências |
| Mensagem recebida | Quando um usuário é atualizado por mensagens recebidas de usuários finais por meio de canais, como SMS |
| Migração | Quando um usuário é atualizado por migrações internas ou scripts de manutenção |
| Mesclagem de usuários | Quando um usuário é atualizado pelo processo de mesclagem de usuários |
| Etapa de atualização do usuário do canva | Quando um usuário é atualizado pela etapa de atualização do usuário do Canva |
| Registro de token por push | Quando um usuário é atualizado pelo processo de registro de token |
| Cancelar inscrição de lista | Quando um usuário cancela a inscrição por meio do Braze mailto ou do cabeçalho de cancelamento de inscrição da lista de um clique |
| Outro | Inclui quaisquer outras fontes, como trabalhos de sincronização de demonstração ou de provedor, ou retornos de chamada de eventos de SMS e Whatsapp |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endapi %}

{% api %}
## Eventos de mudança de estado do grupo de inscrições

{% apitags %}
Inscrição
{% endapitags %}

Esse evento ocorre quando o estado da inscrição de um usuário em um grupo de inscrições é alterado.

{% alert important %}
No momento, os grupos de inscrições estão disponíveis apenas para os canais de e-mail, SMS e WhatsApp.
{% endalert %}

{% tabs %}
{% tab Amplitude %}
```json
// Subscription Group State Change (users.behaviors.subscriptiongroup.StateChange)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "channel" : "(optional, string) Channel this event belongs to",
    "channel_identifier" : "(optional, string) [PII] The user's identifier on the channel the event is for.",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "email_address" : "(optional, string) [PII] Email address of the user",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "state_change_source" : "(optional, string) Source of the state change, e.g: REST API, SDK, Dashboard, etc.",
    "subscription_group_id" : "(required, string) Subscription group API ID",
    "subscription_status" : "(required, string) Subscription status: 'Subscribed' or 'Unsubscribed'",
    "timezone" : "(optional, string) Time zone of the user"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Subscription Group State Change (users.behaviors.subscriptiongroup.StateChange)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "channel" : "(optional, string) Channel this event belongs to",
    "channel_identifier" : "(optional, string) [PII] The user's identifier on the channel the event is for.",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "email_address" : "(optional, string) [PII] Email address of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "state_change_source" : "(optional, string) Source of the state change, e.g: REST API, SDK, Dashboard, etc.",
    "subscription_group_id" : "(required, string) Subscription group API ID",
    "subscription_status" : "(required, string) Subscription status: 'Subscribed' or 'Unsubscribed'",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Subscription Group State Changes (users.behaviors.subscriptiongroup.StateChange)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "channel" : "(optional, string) Channel this event belongs to",
          "channel_identifier" : "(optional, string) [PII] The user's identifier on the channel the event is for.",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "state_change_source" : "(optional, string) Source of the state change, e.g: REST API, SDK, Dashboard, etc.",
          "subscription_group_id" : "(required, string) Subscription group API ID",
          "subscription_status" : "(required, string) Subscription status: 'Subscribed' or 'Unsubscribed'"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user",
    "email" : "(optional, string) [PII] Email address of the user"
  }
}
```
{% endtab %}

{% tab Segmento %}
```json
// Subscription Group State Changed (users.behaviors.subscriptiongroup.StateChange)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : {
      "email" : "(optional, string) [PII] Email address of the user"
    },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "channel" : "(optional, string) Channel this event belongs to",
    "channel_identifier" : "(optional, string) [PII] The user's identifier on the channel the event is for.",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "state_change_source" : "(optional, string) Source of the state change, e.g: REST API, SDK, Dashboard, etc.",
    "subscription_group_id" : "(required, string) Subscription group API ID",
    "subscription_status" : "(required, string) Subscription status: 'Subscribed' or 'Unsubscribed'"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Armazenamento em nuvem %}
```json
// users.behaviors.subscriptiongroup.StateChange

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "channel" : "(optional, string) Channel this event belongs to",
  "channel_identifier" : "(optional, string) [PII] The user's identifier on the channel the event is for.",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "email_address" : "(optional, string) [PII] Email address of the user",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "phone_number" : "(optional, string) [PII] Phone number of the user in e.164 format (for example +14155552671)",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "state_change_source" : "(optional, string) Source of the state change, e.g: REST API, SDK, Dashboard, etc.",
  "subscription_group_id" : "(required, string) Subscription group API ID",
  "subscription_status" : "(required, string) Subscription status: 'Subscribed' or 'Unsubscribed'",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### Detalhes da propriedade

- `state_change_source` retornará uma string com o nome completo da fonte. Por exemplo, a importação do CSV de origem retornará a string `CSV Import`. As fontes disponíveis estão listadas abaixo:

| Origem | Descrição |
| --- | --- |
| SDK | Endpoints de SDK |
| Dashboard | Quando o estado da inscrição de um usuário é atualizado na página Perfil do usuário no dashboard |
| Página de inscrição | Quando um usuário cancela a inscrição por meio de um link de cancelamento de inscrição por e-mail que não seja a Central de Preferências |
| API REST | Pontos de extremidade da API REST |
| Importação de CSV | Importação de usuário CSV |
| Central de Preferências | Quando um usuário é atualizado a partir da Central de Preferências |
| Mensagem recebida | Quando um usuário é atualizado por mensagens recebidas de usuários finais por meio de canais como SMS |
| Migração | Quando um usuário é atualizado por migrações internas ou scripts de manutenção |
| Mesclagem de usuários | Quando um usuário é atualizado pelo processo de mesclagem de usuários |
| Etapa de atualização do usuário do canva | Quando um usuário é atualizado pela etapa de atualização do usuário do Canva |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endapi %}

{% api %}
## Eventos de conversão de campanha

{% apitags %}
Campanha, Conversão
{% endapitags %}

Esse evento ocorre quando um usuário realiza uma ação que foi definida como um evento de conversão em uma campanha.

{% alert note %}
`dispatch_id` está obsoleto e será removido na próxima versão do Currents.
{% endalert %}

{% alert important %}
Note que o evento de conversão é codificado no campo `conversion_behavior`, que inclui o tipo de evento de conversão, a janela (período) e informações adicionais, dependendo do tipo de evento de conversão. O campo `conversion_behavior_index` representa qual evento de conversão, como 0 = A, 1 = B, 2 = C, 3 = D.
{% endalert %}

{% tabs %}
{% tab Amplitude %}
```json
// Campaign Conversion (users.campaigns.Conversion)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "conversion_behavior" : "(optional, string) JSON-encoded string describing the conversion behavior",
    "conversion_behavior_index" : "(optional, int) Index of the conversion behavior",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Campaign Conversion (users.campaigns.Conversion)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "conversion_behavior" : "(optional, string) JSON-encoded string describing the conversion behavior",
    "conversion_behavior_index" : "(optional, int) Index of the conversion behavior",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Campaign Conversions (users.campaigns.Conversion)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "conversion_behavior" : "(optional, string) JSON-encoded string describing the conversion behavior",
          "conversion_behavior_index" : "(optional, int) Index of the conversion behavior",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segmento %}
```json
// Campaign Converted (users.campaigns.Conversion)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "conversion_behavior" : "(optional, string) JSON-encoded string describing the conversion behavior",
    "conversion_behavior_index" : "(optional, int) Index of the conversion behavior",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Armazenamento em nuvem %}
```json
// users.campaigns.Conversion

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "campaign_id" : "(required, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "conversion_behavior" : "(optional, string) JSON-encoded string describing the conversion behavior",
  "conversion_behavior_index" : "(optional, int) Index of the conversion behavior",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Eventos de inscrição do grupo de controle da campanha

{% apitags %}
Campanha, Entrada
{% endapitags %}

Esse evento ocorre quando um usuário é inscrito em um conjunto de variantes de controle em uma campanha com várias variantes. Esse evento é gerado porque não haverá nenhum evento de envio de canal para esse usuário.

{% alert note %}
`dispatch_id` está obsoleto e será removido na próxima versão do Currents.
{% endalert %}

{% tabs %}
{% tab Amplitude %}
```json
// Campaign Control Group Enrollment (users.campaigns.EnrollInControl)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Campaign Control Group Enrollment (users.campaigns.EnrollInControl)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Campaign Control Group Enrollments (users.campaigns.EnrollInControl)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segmento %}
```json
// Campaign Control Group Entered (users.campaigns.EnrollInControl)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Armazenamento em nuvem %}
```json
// users.campaigns.EnrollInControl

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "campaign_id" : "(required, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Eventos de conversão do Canva

{% apitags %}
Canvas, Conversão
{% endapitags %}

Esse evento ocorre quando um usuário executa uma ação que foi definida como um evento de conversão no Canva.

{% alert important %}
Note que o evento de conversão é codificado no campo `conversion_behavior`, que inclui o tipo de evento de conversão, a janela (período) e informações adicionais, dependendo do tipo de evento de conversão. O campo `conversion_behavior_index` representa qual evento de conversão, como 0 = A, 1 = B, 2 = C, 3 = D.
{% endalert %}

{% tabs %}
{% tab Amplitude %}
```json
// Canvas Conversion (users.canvas.Conversion)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "conversion_behavior" : "(optional, string) JSON-encoded string describing the conversion behavior",
    "conversion_behavior_index" : "(optional, int) Index of the conversion behavior"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Canvas Conversion (users.canvas.Conversion)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "conversion_behavior" : "(optional, string) JSON-encoded string describing the conversion behavior",
    "conversion_behavior_index" : "(optional, int) Index of the conversion behavior",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Canvas Conversions (users.canvas.Conversion)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "conversion_behavior" : "(optional, string) JSON-encoded string describing the conversion behavior",
          "conversion_behavior_index" : "(optional, int) Index of the conversion behavior",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segmento %}
```json
// Canvas Converted (users.canvas.Conversion)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "conversion_behavior" : "(optional, string) JSON-encoded string describing the conversion behavior",
    "conversion_behavior_index" : "(optional, int) Index of the conversion behavior",
    "device_id" : "(optional, string) ID of the device on which the event occurred"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Armazenamento em nuvem %}
```json
// users.canvas.Conversion

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "canvas_id" : "(required, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(required, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "conversion_behavior" : "(optional, string) JSON-encoded string describing the conversion behavior",
  "conversion_behavior_index" : "(optional, int) Index of the conversion behavior",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Eventos de entrada do Canva

{% apitags %}
Canvas, entrada
{% endapitags %}

Esse evento ocorre quando um usuário entra no Canva. Esse evento informa em qual variante o usuário entrou.

{% tabs %}
{% tab Amplitude %}
```json
// Canvas Entry (users.canvas.Entry)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "in_control_group" : "(required, boolean) Whether the user was enrolled in the control group"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Canvas Entry (users.canvas.Entry)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "in_control_group" : "(required, boolean) Whether the user was enrolled in the control group",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Canvas Entries (users.canvas.Entry)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "in_control_group" : "(required, boolean) Whether the user was enrolled in the control group",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segmento %}
```json
// Canvas Entered (users.canvas.Entry)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "in_control_group" : "(required, boolean) Whether the user was enrolled in the control group"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Armazenamento em nuvem %}
```json
// users.canvas.Entry

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "canvas_id" : "(required, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(required, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "in_control_group" : "(required, boolean) Whether the user was enrolled in the control group",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Eventos do público do Exit Match

{% apitags %}
Saída, Canva
{% endapitags %}

Esse evento ocorre quando um usuário sai de um Canva ao corresponder a um público.

{% tabs %}
{% tab Amplitude %}
```json
// Exit Match Audience (users.canvas.exit.MatchedAudience)

{
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Exit Match Audience (users.canvas.exit.MatchedAudience)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Exit Matched Audiences (users.canvas.exit.MatchedAudience)

{
  "device_info" : { },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segmento %}
```json
// Exit Matched Audience (users.canvas.exit.MatchedAudience)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Armazenamento em nuvem %}
```json
// users.canvas.exit.MatchedAudience

{
  "app_group_api_id" : "(optional, string) [DEPRECATED]",
  "app_group_id" : "(required, string) API ID of the app group this user belongs to",
  "canvas_api_id" : "(optional, string) [DEPRECATED]",
  "canvas_id" : "(required, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_api_id" : "(optional, string) [DEPRECATED]",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_api_id" : "(optional, string) [DEPRECATED]",
  "canvas_variation_id" : "(required, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Eventos Exit Perform Event

{% apitags %}
Saída, Canva
{% endapitags %}

Esse evento ocorre quando um usuário sai de um Canva ao executar um evento.

{% tabs %}
{% tab Amplitude %}
```json
// Exit Perform Event (users.canvas.exit.PerformedEvent)

{
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Exit Perform Event (users.canvas.exit.PerformedEvent)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Exit Performed Events (users.canvas.exit.PerformedEvent)

{
  "device_info" : { },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segmento %}
```json
// Exit Performed Event (users.canvas.exit.PerformedEvent)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Armazenamento em nuvem %}
```json
// users.canvas.exit.PerformedEvent

{
  "app_group_api_id" : "(optional, string) [DEPRECATED]",
  "app_group_id" : "(required, string) API ID of the app group this user belongs to",
  "canvas_api_id" : "(optional, string) [DEPRECATED]",
  "canvas_id" : "(required, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_api_id" : "(optional, string) [DEPRECATED]",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_api_id" : "(optional, string) [DEPRECATED]",
  "canvas_variation_id" : "(required, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Experimento Etapa Eventos de conversão

{% apitags %}
Etapa do experimento, Canva
{% endapitags %}

Esse evento ocorre quando um usuário converte para uma etapa do experimento do Canva.

{% tabs %}
{% tab Amplitude %}
```json
// Experiment Step Conversion (users.canvas.experimentstep.Conversion)

{
  "event_properties" : {
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "conversion_behavior" : "(optional, string) JSON-encoded string describing the conversion behavior",
    "conversion_behavior_index" : "(optional, int) Index of the conversion behavior",
    "experiment_split_id" : "(optional, string) API ID of the experiment split the user enrolled in",
    "experiment_split_name" : "(optional, string) Name of the experiment split",
    "experiment_step_id" : "(optional, string) API ID of the experiment step this event belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Experiment Step Conversion (users.canvas.experimentstep.Conversion)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "conversion_behavior" : "(optional, string) JSON-encoded string describing the conversion behavior",
    "conversion_behavior_index" : "(optional, int) Index of the conversion behavior",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "experiment_split_id" : "(optional, string) API ID of the experiment split the user enrolled in",
    "experiment_split_name" : "(optional, string) Name of the experiment split",
    "experiment_step_id" : "(optional, string) API ID of the experiment step this event belongs to",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Experiment Step Conversions (users.canvas.experimentstep.Conversion)

{
  "device_info" : { },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "conversion_behavior" : "(optional, string) JSON-encoded string describing the conversion behavior",
          "conversion_behavior_index" : "(optional, int) Index of the conversion behavior",
          "experiment_split_id" : "(optional, string) API ID of the experiment split the user enrolled in",
          "experiment_split_name" : "(optional, string) Name of the experiment split",
          "experiment_step_id" : "(optional, string) API ID of the experiment step this event belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segmento %}
```json
// Experiment Step Converted (users.canvas.experimentstep.Conversion)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "conversion_behavior" : "(optional, string) JSON-encoded string describing the conversion behavior",
    "conversion_behavior_index" : "(optional, int) Index of the conversion behavior",
    "experiment_split_id" : "(optional, string) API ID of the experiment split the user enrolled in",
    "experiment_split_name" : "(optional, string) Name of the experiment split",
    "experiment_step_id" : "(optional, string) API ID of the experiment step this event belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Armazenamento em nuvem %}
```json
// users.canvas.experimentstep.Conversion

{
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "conversion_behavior" : "(optional, string) JSON-encoded string describing the conversion behavior",
  "conversion_behavior_index" : "(optional, int) Index of the conversion behavior",
  "experiment_split_id" : "(optional, string) API ID of the experiment split the user enrolled in",
  "experiment_split_name" : "(optional, string) Name of the experiment split",
  "experiment_step_id" : "(optional, string) API ID of the experiment step this event belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Eventos de entrada dividida de experimentos

{% apitags %}
Etapa do experimento, Canva
{% endapitags %}

Esse evento ocorre quando um usuário entra em uma etapa do experimento do Canva.

{% tabs %}
{% tab Amplitude %}
```json
// Experiment Split Entry (users.canvas.experimentstep.SplitEntry)

{
  "event_properties" : {
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "experiment_split_id" : "(optional, string) API ID of the experiment split the user enrolled in",
    "experiment_split_name" : "(optional, string) Name of the experiment split",
    "experiment_step_id" : "(optional, string) API ID of the experiment step this event belongs to",
    "in_control_group" : "(required, boolean) Whether the user was enrolled in the control group"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Experiment Split Entry (users.canvas.experimentstep.SplitEntry)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "experiment_split_id" : "(optional, string) API ID of the experiment split the user enrolled in",
    "experiment_split_name" : "(optional, string) Name of the experiment split",
    "experiment_step_id" : "(optional, string) API ID of the experiment step this event belongs to",
    "in_control_group" : "(required, boolean) Whether the user was enrolled in the control group",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Experiment Split Entries (users.canvas.experimentstep.SplitEntry)

{
  "device_info" : { },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "experiment_split_id" : "(optional, string) API ID of the experiment split the user enrolled in",
          "experiment_split_name" : "(optional, string) Name of the experiment split",
          "experiment_step_id" : "(optional, string) API ID of the experiment step this event belongs to",
          "in_control_group" : "(required, boolean) Whether the user was enrolled in the control group",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segmento %}
```json
// Experiment Split Entered (users.canvas.experimentstep.SplitEntry)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "experiment_split_id" : "(optional, string) API ID of the experiment split the user enrolled in",
    "experiment_split_name" : "(optional, string) Name of the experiment split",
    "experiment_step_id" : "(optional, string) API ID of the experiment step this event belongs to",
    "in_control_group" : "(required, boolean) Whether the user was enrolled in the control group"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Armazenamento em nuvem %}
```json
// users.canvas.experimentstep.SplitEntry

{
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "experiment_split_id" : "(optional, string) API ID of the experiment split the user enrolled in",
  "experiment_split_name" : "(optional, string) Name of the experiment split",
  "experiment_step_id" : "(optional, string) API ID of the experiment step this event belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "in_control_group" : "(required, boolean) Whether the user was enrolled in the control group",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Eventos de progressão da etapa do canva

{% apitags %}
CanvasStep, Progressão
{% endapitags %}

Esse evento ocorre quando um usuário avança em uma etapa do Canva com algum resultado. Note que esse evento não ocorre quando as etapas são inseridas ou encerradas. Atualmente, apenas as etapas divididas (jornadas do público, divisão de decisão, jornadas de ação, experimento) e os resultados avançados geram eventos de progressão de etapas.

{% tabs %}
{% tab Amplitude %}
```json
// Canvas Step Progression (users.canvasstep.Progression)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "canvas_entry_id" : "(required, string) Unique identifier for this instance of a user in a canvas",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "exit_reason" : "(optional, string) If this is an exit, the reason a user exited the canvas during the step",
    "is_canvas_entry" : "(optional, boolean) Whether this is entry into a first step in a canvas",
    "next_step_id" : "(optional, string) API ID of the next step in the canvas",
    "progression_type" : "(required, string) What type of step progression event this is"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Canvas Step Progression (users.canvasstep.Progression)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "canvas_entry_id" : "(required, string) Unique identifier for this instance of a user in a canvas",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "exit_reason" : "(optional, string) If this is an exit, the reason a user exited the canvas during the step",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "is_canvas_entry" : "(optional, boolean) Whether this is entry into a first step in a canvas",
    "next_step_id" : "(optional, string) API ID of the next step in the canvas",
    "progression_type" : "(required, string) What type of step progression event this is",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Canvas Step Progressions (users.canvasstep.Progression)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "canvas_entry_id" : "(required, string) Unique identifier for this instance of a user in a canvas",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "exit_reason" : "(optional, string) If this is an exit, the reason a user exited the canvas during the step",
          "is_canvas_entry" : "(optional, boolean) Whether this is entry into a first step in a canvas",
          "next_step_id" : "(optional, string) API ID of the next step in the canvas",
          "progression_type" : "(required, string) What type of step progression event this is",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segmento %}
```json
// Canvas Step Progression (users.canvasstep.Progression)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "canvas_entry_id" : "(required, string) Unique identifier for this instance of a user in a canvas",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "exit_reason" : "(optional, string) If this is an exit, the reason a user exited the canvas during the step",
    "is_canvas_entry" : "(optional, boolean) Whether this is entry into a first step in a canvas",
    "next_step_id" : "(optional, string) API ID of the next step in the canvas",
    "progression_type" : "(required, string) What type of step progression event this is"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Armazenamento em nuvem %}
```json
// users.canvasstep.Progression

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "canvas_entry_id" : "(required, string) Unique identifier for this instance of a user in a canvas",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "exit_reason" : "(optional, string) If this is an exit, the reason a user exited the canvas during the step",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "is_canvas_entry" : "(optional, boolean) Whether this is entry into a first step in a canvas",
  "next_step_id" : "(optional, string) API ID of the next step in the canvas",
  "progression_type" : "(required, string) What type of step progression event this is",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Eventos de abortamento de banner

{% apitags %}
Banner, Abortar
{% endapitags %}

Esse evento ocorre quando uma mensagem de banner originalmente programada foi abortada por algum motivo.

{% tabs %}
{% tab Amplitude %}
```json
// Banner Abort (users.messages.banner.Abort)

{
  "adid" : "(optional, string) [PII] Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "banner_placement_id" : "(optional, string) Customer specified banner placement ID",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "device_model" : "(optional, string) Model of the device",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "timezone" : "(optional, string) Time zone of the user"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) [PII] Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Banner Abort (users.messages.banner.Abort)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "banner_placement_id" : "(optional, string) Customer specified banner placement ID",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Banner Aborts (users.messages.banner.Abort)

{
  "device_info" : {
    "android_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "device_model" : "(optional, string) Model of the device",
    "ios_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred",
    "limit_ad_tracking" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "microsoft_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "platform" : "(optional, string) Platform of the device",
    "roku_advertising_id" : "(optional, string) [PII] Advertising identifier"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
          "abort_type" : "(optional, string) Type of abort",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "banner_placement_id" : "(optional, string) Customer specified banner placement ID",
          "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segmento %}
```json
// Banner Aborted (users.messages.banner.Abort)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : {
      "model" : "(optional, string) Model of the device"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "banner_placement_id" : "(optional, string) Customer specified banner placement ID",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Armazenamento em nuvem %}
```json
// users.messages.banner.Abort

{
  "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
  "abort_type" : "(optional, string) Type of abort",
  "ad_id" : "(optional, string) [PII] Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "banner_placement_id" : "(optional, string) Customer specified banner placement ID",
  "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "carrier" : "(optional, string) Carrier of the device",
  "country" : "(optional, string) [PII] Country of the user",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "gender" : "(optional, string) [PII] Gender of the user, one of ['M', 'F', 'O', 'N', 'P']",
  "id" : "(required, string) Globally unique ID for this event",
  "language" : "(optional, string) [PII] Language of the user",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "resolution" : "(optional, string) Resolution of the device",
  "sdk_version" : "(optional, string) Version of the Braze SDK in use during the event",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Eventos de clique no banner

{% apitags %}
Banner, clique
{% endapitags %}

Esse evento ocorre quando um usuário clica em um banner.

{% tabs %}
{% tab Amplitude %}
```json
// Banner Click (users.messages.banner.Click)

{
  "adid" : "(optional, string) [PII] Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "banner_placement_id" : "(optional, string) Customer specified banner placement ID",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "button_id" : "(optional, string) ID of the button clicked, if this click represents a click on a button",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "device_model" : "(optional, string) Model of the device",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "timezone" : "(optional, string) Time zone of the user"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) [PII] Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Banner Click (users.messages.banner.Click)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "banner_placement_id" : "(optional, string) Customer specified banner placement ID",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "button_id" : "(optional, string) ID of the button clicked, if this click represents a click on a button",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Banner Clicks (users.messages.banner.Click)

{
  "device_info" : {
    "android_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "device_model" : "(optional, string) Model of the device",
    "ios_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred",
    "limit_ad_tracking" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "microsoft_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "platform" : "(optional, string) Platform of the device",
    "roku_advertising_id" : "(optional, string) [PII] Advertising identifier"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "banner_placement_id" : "(optional, string) Customer specified banner placement ID",
          "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
          "button_id" : "(optional, string) ID of the button clicked, if this click represents a click on a button",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segmento %}
```json
// Banner Clicked (users.messages.banner.Click)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : {
      "model" : "(optional, string) Model of the device"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "banner_placement_id" : "(optional, string) Customer specified banner placement ID",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "button_id" : "(optional, string) ID of the button clicked, if this click represents a click on a button",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Armazenamento em nuvem %}
```json
// users.messages.banner.Click

{
  "ad_id" : "(optional, string) [PII] Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "banner_placement_id" : "(optional, string) Customer specified banner placement ID",
  "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
  "button_id" : "(optional, string) ID of the button clicked, if this click represents a click on a button",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "carrier" : "(optional, string) Carrier of the device",
  "country" : "(optional, string) [PII] Country of the user",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "gender" : "(optional, string) [PII] Gender of the user, one of ['M', 'F', 'O', 'N', 'P']",
  "id" : "(required, string) Globally unique ID for this event",
  "language" : "(optional, string) [PII] Language of the user",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "resolution" : "(optional, string) Resolution of the device",
  "sdk_version" : "(optional, string) Version of the Braze SDK in use during the event",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Eventos de impressão de banner

{% apitags %}
Banner, Impressões
{% endapitags %}

Esse evento ocorre quando um usuário visualiza um banner.

{% tabs %}
{% tab Amplitude %}
```json
// Banner Impression (users.messages.banner.Impression)

{
  "adid" : "(optional, string) [PII] Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "banner_placement_id" : "(optional, string) Customer specified banner placement ID",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "device_model" : "(optional, string) Model of the device",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "timezone" : "(optional, string) Time zone of the user"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) [PII] Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Banner Impression (users.messages.banner.Impression)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "banner_placement_id" : "(optional, string) Customer specified banner placement ID",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Banner Impressions (users.messages.banner.Impression)

{
  "device_info" : {
    "android_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "device_model" : "(optional, string) Model of the device",
    "ios_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred",
    "limit_ad_tracking" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "microsoft_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "platform" : "(optional, string) Platform of the device",
    "roku_advertising_id" : "(optional, string) [PII] Advertising identifier"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "banner_placement_id" : "(optional, string) Customer specified banner placement ID",
          "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segmento %}
```json
// Banner Viewed (users.messages.banner.Impression)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : {
      "model" : "(optional, string) Model of the device"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "banner_placement_id" : "(optional, string) Customer specified banner placement ID",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Armazenamento em nuvem %}
```json
// users.messages.banner.Impression

{
  "ad_id" : "(optional, string) [PII] Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "banner_placement_id" : "(optional, string) Customer specified banner placement ID",
  "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "carrier" : "(optional, string) Carrier of the device",
  "country" : "(optional, string) [PII] Country of the user",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "gender" : "(optional, string) [PII] Gender of the user, one of ['M', 'F', 'O', 'N', 'P']",
  "id" : "(required, string) Globally unique ID for this event",
  "language" : "(optional, string) [PII] Language of the user",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "resolution" : "(optional, string) Resolution of the device",
  "sdk_version" : "(optional, string) Version of the Braze SDK in use during the event",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Eventos de interrupção do cartão de conteúdo

{% apitags %}
Abortar, cartões de conteúdo
{% endapitags %}

Esse evento ocorre se uma mensagem do cartão de conteúdo foi abortada com base em abortos do Liquid, etc.

{% tabs %}
{% tab Amplitude %}
```json
// Content Card Abort (users.messages.contentcard.Abort)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Content Card Abort (users.messages.contentcard.Abort)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Content Card Aborts (users.messages.contentcard.Abort)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
          "abort_type" : "(optional, string) Type of abort",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segmento %}
```json
// Content Card Aborted (users.messages.contentcard.Abort)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Armazenamento em nuvem %}
```json
// users.messages.contentcard.Abort

{
  "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
  "abort_type" : "(optional, string) Type of abort",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Eventos de clique do cartão de conteúdo

{% apitags %}
Cartões de conteúdo, cliques
{% endapitags %}

Esse evento ocorre quando um usuário clica em um cartão de conteúdo.

{% alert note %}
`dispatch_id` está obsoleto e será removido na próxima versão do Currents.
{% endalert %}

{% tabs %}
{% tab Amplitude %}
```json
// Content Card Click (users.messages.contentcard.Click)

{
  "adid" : "(optional, string) [PII] Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(required, string) ID of the card that generated this event",
    "device_model" : "(optional, string) Model of the device",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) [PII] Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Content Card Click (users.messages.contentcard.Click)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(required, string) ID of the card that generated this event",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Content Card Clicks (users.messages.contentcard.Click)

{
  "device_info" : {
    "android_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "device_model" : "(optional, string) Model of the device",
    "ios_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred",
    "limit_ad_tracking" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "microsoft_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "platform" : "(optional, string) Platform of the device",
    "roku_advertising_id" : "(optional, string) [PII] Advertising identifier"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "card_id" : "(required, string) ID of the card that generated this event",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segmento %}
```json
// Content Card Clicked (users.messages.contentcard.Click)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : {
      "model" : "(optional, string) Model of the device",
      "type" : "(optional, string) Platform of the device"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(required, string) ID of the card that generated this event",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Armazenamento em nuvem %}
```json
// users.messages.contentcard.Click

{
  "ad_id" : "(optional, string) [PII] Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "content_card_id" : "(required, string) ID of the card that generated this event",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### Detalhes da propriedade

- Para `ad_id`, `ad_id_type` e `ad_tracking_enabled`, você precisa coletar explicitamente o IDFA do iOS e o ID de publicidade do Google do Android por meio dos SDKs nativos. Saiba mais sobre essa configuração para [iOS]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?sdktab=swift) e [Android]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android#android_google-advertising-id).
- Se estiver usando o Kafka para ingerir dados do [Currents]({{site.baseurl}}/user_guide/data/braze_currents/), entre em contato com o gerente de sucesso do cliente para ativar o envio de `ad_id`.
{% endapi %}

{% api %}
## Cartão de conteúdo Descartar eventos

{% apitags %}
Cartões de conteúdo, descarte de cartão
{% endapitags %}

Esse evento ocorre quando um usuário descarta um cartão de conteúdo.

{% alert note %}
`dispatch_id` está obsoleto e será removido na próxima versão do Currents.
{% endalert %}

{% tabs %}
{% tab Amplitude %}
```json
// Content Card Dismiss (users.messages.contentcard.Dismiss)

{
  "adid" : "(optional, string) [PII] Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(required, string) ID of the card that generated this event",
    "device_model" : "(optional, string) Model of the device",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) [PII] Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Content Card Dismiss (users.messages.contentcard.Dismiss)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(required, string) ID of the card that generated this event",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Content Card Dismisses (users.messages.contentcard.Dismiss)

{
  "device_info" : {
    "android_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "device_model" : "(optional, string) Model of the device",
    "ios_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred",
    "limit_ad_tracking" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "microsoft_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "platform" : "(optional, string) Platform of the device",
    "roku_advertising_id" : "(optional, string) [PII] Advertising identifier"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "card_id" : "(required, string) ID of the card that generated this event",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segmento %}
```json
// Content Card Dismissed (users.messages.contentcard.Dismiss)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : {
      "model" : "(optional, string) Model of the device",
      "type" : "(optional, string) Platform of the device"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(required, string) ID of the card that generated this event",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Armazenamento em nuvem %}
```json
// users.messages.contentcard.Dismiss

{
  "ad_id" : "(optional, string) [PII] Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "content_card_id" : "(required, string) ID of the card that generated this event",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### Detalhes da propriedade

- Para `ad_id`, `ad_id_type` e `ad_tracking_enabled`, você precisa coletar explicitamente o IDFA do iOS e o ID de publicidade do Google do Android por meio dos SDKs nativos. Saiba mais sobre essa configuração para [iOS]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?sdktab=swift) e [Android]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android#android_google-advertising-id).
- Se estiver usando o Kafka para ingerir dados do [Currents]({{site.baseurl}}/user_guide/data/braze_currents/), entre em contato com o gerente de sucesso do cliente para ativar o envio de `ad_id`.
{% endapi %}

{% api %}
## Eventos de impressão do cartão de conteúdo

{% apitags %}
Cartões de conteúdo, impressões
{% endapitags %}

Esse evento ocorre quando um usuário visualiza um cartão de conteúdo.

{% alert note %}
`dispatch_id` está obsoleto e será removido na próxima versão do Currents.
{% endalert %}

{% tabs %}
{% tab Amplitude %}
```json
// Content Card Impression (users.messages.contentcard.Impression)

{
  "adid" : "(optional, string) [PII] Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(required, string) ID of the card that generated this event",
    "device_model" : "(optional, string) Model of the device",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) [PII] Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Content Card Impression (users.messages.contentcard.Impression)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(required, string) ID of the card that generated this event",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Content Card Impressions (users.messages.contentcard.Impression)

{
  "device_info" : {
    "android_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "device_model" : "(optional, string) Model of the device",
    "ios_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred",
    "limit_ad_tracking" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "microsoft_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "platform" : "(optional, string) Platform of the device",
    "roku_advertising_id" : "(optional, string) [PII] Advertising identifier"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "card_id" : "(required, string) ID of the card that generated this event",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segmento %}
```json
// Content Card Viewed (users.messages.contentcard.Impression)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : {
      "model" : "(optional, string) Model of the device",
      "type" : "(optional, string) Platform of the device"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(required, string) ID of the card that generated this event",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Armazenamento em nuvem %}
```json
// users.messages.contentcard.Impression

{
  "ad_id" : "(optional, string) [PII] Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "content_card_id" : "(required, string) ID of the card that generated this event",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### Detalhes da propriedade

- Para `ad_id`, `ad_id_type` e `ad_tracking_enabled`, você precisa coletar explicitamente o IDFA do iOS e o ID de publicidade do Google do Android por meio dos SDKs nativos. Saiba mais sobre essa configuração para [iOS]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?sdktab=swift) e [Android]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android#android_google-advertising-id).
- Se estiver usando o Kafka para ingerir dados do [Currents]({{site.baseurl}}/user_guide/data/braze_currents/), entre em contato com o gerente de sucesso do cliente para ativar o envio de `ad_id`.
{% endapi %}

{% api %}
## Cartão de conteúdo Enviar eventos

{% apitags %}
Cartões de conteúdo, envios
{% endapitags %}

Esse evento ocorre quando um cartão de conteúdo é enviado a um usuário.

{% alert note %}
`dispatch_id` está obsoleto e será removido na próxima versão do Currents.
{% endalert %}

{% tabs %}
{% tab Amplitude %}
```json
// Content Card Send (users.messages.contentcard.Send)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(required, string) ID of the card that generated this event",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Content Card Send (users.messages.contentcard.Send)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(required, string) ID of the card that generated this event",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Content Card Sends (users.messages.contentcard.Send)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "card_id" : "(required, string) ID of the card that generated this event",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segmento %}
```json
// Content Card Sent (users.messages.contentcard.Send)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(required, string) ID of the card that generated this event",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Armazenamento em nuvem %}
```json
// users.messages.contentcard.Send

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "content_card_id" : "(required, string) ID of the card that generated this event",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### Detalhes da propriedade

- `message_extras` permite que você anote seus eventos de envio com dados dinâmicos do conteúdo conectado, atributos personalizados (como idioma, país) e propriedades de entrada nos canvas. Consulte [Envio de mensagens extras]({{site.baseurl}}/message_extras_tag/) para saber mais.
{% endapi %}

{% api %}
## Envio de e-mail Abortar eventos

{% apitags %}
Abortar, e-mail
{% endapitags %}

Esse evento ocorre se uma mensagem de e-mail foi abortada com base em abortos de Liquid, etc.

{% tabs %}
{% tab Amplitude %}
```json
// Email Abort (users.messages.email.Abort)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "email_address" : "(required, string) [PII] Email address of the user",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Email Abort (users.messages.email.Abort)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "email_address" : "(required, string) [PII] Email address of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Email Aborts (users.messages.email.Abort)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
          "abort_type" : "(optional, string) Type of abort",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "ip_pool" : "(optional, string) IP pool from which the email send was made",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user",
    "email" : "(required, string) [PII] Email address of the user"
  }
}
```
{% endtab %}

{% tab Segmento %}
```json
// Email Aborted (users.messages.email.Abort)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : {
      "email" : "(required, string) [PII] Email address of the user"
    },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Armazenamento em nuvem %}
```json
// users.messages.email.Abort

{
  "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
  "abort_type" : "(optional, string) Type of abort",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "email_address" : "(required, string) [PII] Email address of the user",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "ip_pool" : "(optional, string) IP pool from which the email send was made",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Eventos de bounce de e-mail

{% apitags %}
Envio de e-mail, bounce
{% endapitags %}

Esse evento ocorre quando um provedor de serviços de Internet retorna um hard bounce. Um hard bounce significa uma falha permanente de entregabilidade.

{% tabs %}
{% tab Amplitude %}
```json
// Email Bounce (users.messages.email.Bounce)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "bounce_reason" : "(optional, string) [PII] The SMTP reason code and user friendly message received for this bounce event",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "email_address" : "(required, string) [PII] Email address of the user",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "is_drop" : "(optional, boolean) Indicates that this event counts as a drop event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Email Bounce (users.messages.email.Bounce)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "bounce_reason" : "(optional, string) [PII] The SMTP reason code and user friendly message received for this bounce event",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "email_address" : "(required, string) [PII] Email address of the user",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "is_drop" : "(optional, boolean) Indicates that this event counts as a drop event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Email Bounces (users.messages.email.Bounce)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "bounce_reason" : "(optional, string) [PII] The SMTP reason code and user friendly message received for this bounce event",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
          "from_domain" : "(optional, string) Sending domain for the email",
          "ip_pool" : "(optional, string) IP pool from which the email send was made",
          "is_drop" : "(optional, boolean) Indicates that this event counts as a drop event",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user",
    "email" : "(required, string) [PII] Email address of the user"
  }
}
```
{% endtab %}

{% tab Segmento %}
```json
// Email Bounced (users.messages.email.Bounce)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : {
      "email" : "(required, string) [PII] Email address of the user"
    },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "bounce_reason" : "(optional, string) [PII] The SMTP reason code and user friendly message received for this bounce event",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "is_drop" : "(optional, boolean) Indicates that this event counts as a drop event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Armazenamento em nuvem %}
```json
// users.messages.email.Bounce

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "bounce_reason" : "(optional, string) [PII] The SMTP reason code and user friendly message received for this bounce event",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "email_address" : "(required, string) [PII] Email address of the user",
  "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "from_domain" : "(optional, string) Sending domain for the email",
  "id" : "(required, string) Globally unique ID for this event",
  "ip_pool" : "(optional, string) IP pool from which the email send was made",
  "is_drop" : "(optional, boolean) Indicates that this event counts as a drop event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "sending_ip" : "(optional, string) IP address from which the email send was made",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### Detalhes da propriedade

- O comportamento do site `dispatch_id` difere entre o canva e as campanhas porque a Braze trata as etapas do canva (exceto as etapas de entrada, que podem ser programadas) como eventos disparados, mesmo quando estão programadas. Saiba mais sobre o [comportamento do ID de despacho]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
{% endapi %}

{% api %}
## Envio de e-mail Eventos de clique

{% apitags %}
Envio de e-mail, cliques
{% endapitags %}

Esse evento ocorre quando um usuário clica em um e-mail. Vários eventos podem ser gerados para a mesma campanha se um usuário clicar várias vezes ou clicar em diferentes links dentro do e-mail.

{% tabs %}
{% tab Amplitude %}
```json
// Email Click (users.messages.email.Click)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_class" : "(optional, string) Device class extracted from user_agent (mobile, desktop, tablet, etc...)",
    "device_model" : "(optional, string) Model of the device",
    "device_os" : "(optional, string) Device operating system extracted from user_agent",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "email_address" : "(required, string) [PII] Email address of the user",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "is_amp" : "(optional, boolean) Indicates that this is an AMP event",
    "is_suspected_bot_click" : "(optional, boolean) Indicates that this is a suspected bot click. Will only populate when Bot Filtering setting is enabled",
    "link_alias" : "(optional, string) Alias associated with this link ID",
    "link_id" : "(optional, string) Unique ID for the link which was clicked, as created by Braze",
    "mailbox_provider" : "(optional, string) Mailbox provider value returned by the esp for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "suspected_bot_click_reason" : "(optional, array of string) Reason(s) why this is a suspected bot click. Will always populate even if Bot Filtering setting is disabled.",
    "url" : "(optional, string) URL that the user clicked on",
    "user_agent" : "(optional, string) User agent on which the spam report occurred"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Email Click (users.messages.email.Click)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "$device" : "(optional, string) Model of the device",
    "device_class" : "(optional, string) Device class extracted from user_agent (mobile, desktop, tablet, etc...)",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "device_os" : "(optional, string) Device operating system extracted from user_agent",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "email_address" : "(required, string) [PII] Email address of the user",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "is_amp" : "(optional, boolean) Indicates that this is an AMP event",
    "is_suspected_bot_click" : "(optional, boolean) Indicates that this is a suspected bot click. Will only populate when Bot Filtering setting is enabled",
    "link_alias" : "(optional, string) Alias associated with this link ID",
    "link_id" : "(optional, string) Unique ID for the link which was clicked, as created by Braze",
    "mailbox_provider" : "(optional, string) Mailbox provider value returned by the esp for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "suspected_bot_click_reason" : "(optional, array of string) Reason(s) why this is a suspected bot click. Will always populate even if Bot Filtering setting is disabled.",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token",
    "url" : "(optional, string) URL that the user clicked on",
    "user_agent" : "(optional, string) User agent on which the spam report occurred"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Email Clicks (users.messages.email.Click)

{
  "device_info" : {
    "device_model" : "(optional, string) Model of the device",
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_class" : "(optional, string) Device class extracted from user_agent (mobile, desktop, tablet, etc...)",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "device_os" : "(optional, string) Device operating system extracted from user_agent",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
          "from_domain" : "(optional, string) Sending domain for the email",
          "ip_pool" : "(optional, string) IP pool from which the email send was made",
          "is_amp" : "(optional, boolean) Indicates that this is an AMP event",
          "is_suspected_bot_click" : "(optional, boolean) Indicates that this is a suspected bot click. Will only populate when Bot Filtering setting is enabled",
          "link_alias" : "(optional, string) Alias associated with this link ID",
          "link_id" : "(optional, string) Unique ID for the link which was clicked, as created by Braze",
          "mailbox_provider" : "(optional, string) Mailbox provider value returned by the esp for this event",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "url" : "(optional, string) URL that the user clicked on",
          "user_agent" : "(optional, string) User agent on which the spam report occurred"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user",
    "email" : "(required, string) [PII] Email address of the user"
  }
}
```
{% endtab %}

{% tab Segmento %}
```json
// Email Link Clicked (users.messages.email.Click)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : {
      "email" : "(required, string) [PII] Email address of the user"
    },
    "device" : {
      "model" : "(optional, string) Model of the device"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_class" : "(optional, string) Device class extracted from user_agent (mobile, desktop, tablet, etc...)",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "device_os" : "(optional, string) Device operating system extracted from user_agent",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "is_amp" : "(optional, boolean) Indicates that this is an AMP event",
    "is_suspected_bot_click" : "(optional, boolean) Indicates that this is a suspected bot click. Will only populate when Bot Filtering setting is enabled",
    "link_alias" : "(optional, string) Alias associated with this link ID",
    "link_id" : "(optional, string) Unique ID for the link which was clicked, as created by Braze",
    "link_url" : "(optional, string) URL that the user clicked on",
    "mailbox_provider" : "(optional, string) Mailbox provider value returned by the esp for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "suspected_bot_click_reason" : "(optional, array of string) Reason(s) why this is a suspected bot click. Will always populate even if Bot Filtering setting is disabled.",
    "user_agent" : "(optional, string) User agent on which the spam report occurred"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Armazenamento em nuvem %}
```json
// users.messages.email.Click

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "device_class" : "(optional, string) Device class extracted from user_agent (mobile, desktop, tablet, etc...)",
  "device_model" : "(optional, string) Model of the device",
  "device_os" : "(optional, string) Device operating system extracted from user_agent",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "email_address" : "(required, string) [PII] Email address of the user",
  "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "from_domain" : "(optional, string) Sending domain for the email",
  "id" : "(required, string) Globally unique ID for this event",
  "ip_pool" : "(optional, string) IP pool from which the email send was made",
  "is_amp" : "(optional, boolean) Indicates that this is an AMP event",
  "is_suspected_bot_click" : "(optional, boolean) Indicates that this is a suspected bot click. Will only populate when Bot Filtering setting is enabled",
  "link_alias" : "(optional, string) Alias associated with this link ID",
  "link_id" : "(optional, string) Unique ID for the link which was clicked, as created by Braze",
  "mailbox_provider" : "(optional, string) Mailbox provider value returned by the esp for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "suspected_bot_click_reason" : "(optional, array of string) Reason(s) why this is a suspected bot click. Will always populate even if Bot Filtering setting is disabled.",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "url" : "(optional, string) URL that the user clicked on",
  "user_agent" : "(optional, string) User agent on which the spam report occurred",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### Detalhes da propriedade

- O comportamento do site `dispatch_id` difere entre o canva e as campanhas porque a Braze trata as etapas do canva (exceto as etapas de entrada, que podem ser programadas) como eventos disparados, mesmo quando estão programadas. Saiba mais sobre o [comportamento do ID de despacho]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
{% endapi %}

{% api %}
## Eventos de envio de e-mail

{% apitags %}
Envio de e-mail, diferimento
{% endapitags %}

Esse evento ocorre quando um provedor de serviços de Internet não entrega imediatamente o e-mail para um endereço de e-mail não hard bounce e o Braze tenta novamente o e-mail por até 72 horas. Os motivos típicos para adiamentos incluem limite de volume de envios de e-mail com base na reputação do provedor de caixa de entrada, problemas temporários de conectividade, caixa de correio do destinatário cheia ou erros de DNS.

{% tabs %}
{% tab Amplitude %}
```json
// Email Deferral (users.messages.email.Deferral)

{
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "attempt_count" : "(optional, int) Number of attempts made to send the message",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "deferral_reason" : "(optional, string) [PII] The SMTP reason code and user friendly message received for this deferral event",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "email_address" : "(required, string) [PII] Email address of the user",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "recipient_domain" : "(optional, string) Receipient's email domain",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "timezone" : "(optional, string) Time zone of the user"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Email Deferral (users.messages.email.Deferral)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "attempt_count" : "(optional, int) Number of attempts made to send the message",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "deferral_reason" : "(optional, string) [PII] The SMTP reason code and user friendly message received for this deferral event",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "email_address" : "(required, string) [PII] Email address of the user",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "recipient_domain" : "(optional, string) Receipient's email domain",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Email Deferrals (users.messages.email.Deferral)

{
  "device_info" : { },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "attempt_count" : "(optional, int) Number of attempts made to send the message",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "deferral_reason" : "(optional, string) [PII] The SMTP reason code and user friendly message received for this deferral event",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
          "from_domain" : "(optional, string) Sending domain for the email",
          "ip_pool" : "(optional, string) IP pool from which the email send was made",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "recipient_domain" : "(optional, string) Receipient's email domain",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user",
    "email" : "(required, string) [PII] Email address of the user"
  }
}
```
{% endtab %}

{% tab Segmento %}
```json
// Email Deferred (users.messages.email.Deferral)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : {
      "email" : "(required, string) [PII] Email address of the user"
    },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "attempt_count" : "(optional, int) Number of attempts made to send the message",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "deferral_reason" : "(optional, string) [PII] The SMTP reason code and user friendly message received for this deferral event",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "recipient_domain" : "(optional, string) Receipient's email domain",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Armazenamento em nuvem %}
```json
// users.messages.email.Deferral

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "attempt_count" : "(optional, int) Number of attempts made to send the message",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "deferral_reason" : "(optional, string) [PII] The SMTP reason code and user friendly message received for this deferral event",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "email_address" : "(required, string) [PII] Email address of the user",
  "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "from_domain" : "(optional, string) Sending domain for the email",
  "id" : "(required, string) Globally unique ID for this event",
  "ip_pool" : "(optional, string) IP pool from which the email send was made",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "recipient_domain" : "(optional, string) Receipient's email domain",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "sending_ip" : "(optional, string) IP address from which the email send was made",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### Detalhes da propriedade

- O comportamento do site `dispatch_id` difere entre o canva e as campanhas porque a Braze trata as etapas do canva (exceto as etapas de entrada, que podem ser programadas) como eventos disparados, mesmo quando estão programadas. Saiba mais sobre o [comportamento do ID de despacho]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
{% endapi %}

{% api %}
## Eventos de envio de e-mail

{% apitags %}
Envio de e-mail, entrega
{% endapitags %}

Esse evento ocorre quando um e-mail enviado chega com êxito à caixa de entrada do usuário final.

{% tabs %}
{% tab Amplitude %}
```json
// Email Delivery (users.messages.email.Delivery)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "email_address" : "(required, string) [PII] Email address of the user",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Email Delivery (users.messages.email.Delivery)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "email_address" : "(required, string) [PII] Email address of the user",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Email Deliveries (users.messages.email.Delivery)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
          "from_domain" : "(optional, string) Sending domain for the email",
          "ip_pool" : "(optional, string) IP pool from which the email send was made",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user",
    "email" : "(required, string) [PII] Email address of the user"
  }
}
```
{% endtab %}

{% tab Segmento %}
```json
// Email Delivered (users.messages.email.Delivery)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : {
      "email" : "(required, string) [PII] Email address of the user"
    },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Armazenamento em nuvem %}
```json
// users.messages.email.Delivery

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "email_address" : "(required, string) [PII] Email address of the user",
  "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "from_domain" : "(optional, string) Sending domain for the email",
  "id" : "(required, string) Globally unique ID for this event",
  "ip_pool" : "(optional, string) IP pool from which the email send was made",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "sending_ip" : "(optional, string) IP address from which the email send was made",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### Detalhes da propriedade

- O comportamento do site `dispatch_id` difere entre o canva e as campanhas porque a Braze trata as etapas do canva (exceto as etapas de entrada, que podem ser programadas) como eventos disparados, mesmo quando estão programadas. Saiba mais sobre o [comportamento do ID de despacho]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
{% endapi %}

{% api %}
## Eventos de envio de e-mail para marcar como spam

{% apitags %}
Envio de e-mail, Spam
{% endapitags %}

Esse evento ocorre quando o usuário final pressiona o botão "spam" no e-mail. Observe que isso não representa o fato de o e-mail ter ido para a pasta de spam, pois o Braze não faz esse rastreamento.

{% tabs %}
{% tab Amplitude %}
```json
// Email Mark As Spam (users.messages.email.MarkAsSpam)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "email_address" : "(required, string) [PII] Email address of the user",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "user_agent" : "(optional, string) User agent on which the spam report occurred"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Email Mark As Spam (users.messages.email.MarkAsSpam)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "email_address" : "(required, string) [PII] Email address of the user",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token",
    "user_agent" : "(optional, string) User agent on which the spam report occurred"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Email Marks As Spam (users.messages.email.MarkAsSpam)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
          "from_domain" : "(optional, string) Sending domain for the email",
          "ip_pool" : "(optional, string) IP pool from which the email send was made",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "user_agent" : "(optional, string) User agent on which the spam report occurred"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user",
    "email" : "(required, string) [PII] Email address of the user"
  }
}
```
{% endtab %}

{% tab Segmento %}
```json
// Email Marked as Spam (users.messages.email.MarkAsSpam)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : {
      "email" : "(required, string) [PII] Email address of the user"
    },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "user_agent" : "(optional, string) User agent on which the spam report occurred"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Armazenamento em nuvem %}
```json
// users.messages.email.MarkAsSpam

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "email_address" : "(required, string) [PII] Email address of the user",
  "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "from_domain" : "(optional, string) Sending domain for the email",
  "id" : "(required, string) Globally unique ID for this event",
  "ip_pool" : "(optional, string) IP pool from which the email send was made",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_agent" : "(optional, string) User agent on which the spam report occurred",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### Detalhes da propriedade

- O comportamento do site `dispatch_id` difere entre o canva e as campanhas porque a Braze trata as etapas do canva (exceto as etapas de entrada, que podem ser programadas) como eventos disparados, mesmo quando estão programadas. Saiba mais sobre o [comportamento do ID de despacho]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
{% endapi %}

{% api %}
## Envio de e-mail Eventos abertos

{% apitags %}
Envio de e-mail, aberturas
{% endapitags %}

Esse evento ocorre quando um usuário abre um e-mail. Vários eventos podem ser gerados para a mesma campanha se um usuário abrir o e-mail várias vezes.

{% alert important %}
É um comportamento conhecido o fato de os campos de evento de abertura de e-mail `device_model` e `mailbox_provider` estarem vazios. Você pode ignorá-los por enquanto.
{% endalert %}

{% tabs %}
{% tab Amplitude %}
```json
// Email Open (users.messages.email.Open)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_class" : "(optional, string) Device class extracted from user_agent (mobile, desktop, tablet, etc...)",
    "device_model" : "(optional, string) Model of the device",
    "device_os" : "(optional, string) Device operating system extracted from user_agent",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "email_address" : "(required, string) [PII] Email address of the user",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "is_amp" : "(optional, boolean) Indicates that this is an AMP event",
    "machine_open" : "(optional, string) Populated to 'true' if the open event is triggered without user engagement, for example by an Apple device with Mail Privacy Protection enabled. Value may change over time to provide more granularity.",
    "mailbox_provider" : "(optional, string) Mailbox provider value returned by the esp for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "user_agent" : "(optional, string) User agent on which the spam report occurred"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Email Open (users.messages.email.Open)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "$device" : "(optional, string) Model of the device",
    "device_class" : "(optional, string) Device class extracted from user_agent (mobile, desktop, tablet, etc...)",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "device_os" : "(optional, string) Device operating system extracted from user_agent",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "email_address" : "(required, string) [PII] Email address of the user",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "is_amp" : "(optional, boolean) Indicates that this is an AMP event",
    "machine_open" : "(optional, string) Populated to 'true' if the open event is triggered without user engagement, for example by an Apple device with Mail Privacy Protection enabled. Value may change over time to provide more granularity.",
    "mailbox_provider" : "(optional, string) Mailbox provider value returned by the esp for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token",
    "user_agent" : "(optional, string) User agent on which the spam report occurred"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Email Opens (users.messages.email.Open)

{
  "device_info" : {
    "device_model" : "(optional, string) Model of the device",
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_class" : "(optional, string) Device class extracted from user_agent (mobile, desktop, tablet, etc...)",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "device_os" : "(optional, string) Device operating system extracted from user_agent",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
          "from_domain" : "(optional, string) Sending domain for the email",
          "ip_pool" : "(optional, string) IP pool from which the email send was made",
          "is_amp" : "(optional, boolean) Indicates that this is an AMP event",
          "machine_open" : "(optional, string) Populated to 'true' if the open event is triggered without user engagement, for example by an Apple device with Mail Privacy Protection enabled. Value may change over time to provide more granularity.",
          "mailbox_provider" : "(optional, string) Mailbox provider value returned by the esp for this event",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "user_agent" : "(optional, string) User agent on which the spam report occurred"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user",
    "email" : "(required, string) [PII] Email address of the user"
  }
}
```
{% endtab %}

{% tab Segmento %}
```json
// Email Opened (users.messages.email.Open)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : {
      "email" : "(required, string) [PII] Email address of the user"
    },
    "device" : {
      "model" : "(optional, string) Model of the device"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_class" : "(optional, string) Device class extracted from user_agent (mobile, desktop, tablet, etc...)",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "device_os" : "(optional, string) Device operating system extracted from user_agent",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "is_amp" : "(optional, boolean) Indicates that this is an AMP event",
    "machine_open" : "(optional, string) Populated to 'true' if the open event is triggered without user engagement, for example by an Apple device with Mail Privacy Protection enabled. Value may change over time to provide more granularity.",
    "mailbox_provider" : "(optional, string) Mailbox provider value returned by the esp for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "user_agent" : "(optional, string) User agent on which the spam report occurred"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Armazenamento em nuvem %}
```json
// users.messages.email.Open

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "device_class" : "(optional, string) Device class extracted from user_agent (mobile, desktop, tablet, etc...)",
  "device_model" : "(optional, string) Model of the device",
  "device_os" : "(optional, string) Device operating system extracted from user_agent",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "email_address" : "(required, string) [PII] Email address of the user",
  "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "from_domain" : "(optional, string) Sending domain for the email",
  "id" : "(required, string) Globally unique ID for this event",
  "ip_pool" : "(optional, string) IP pool from which the email send was made",
  "is_amp" : "(optional, boolean) Indicates that this is an AMP event",
  "machine_open" : "(optional, string) Populated to 'true' if the open event is triggered without user engagement, for example by an Apple device with Mail Privacy Protection enabled. Value may change over time to provide more granularity.",
  "mailbox_provider" : "(optional, string) Mailbox provider value returned by the esp for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_agent" : "(optional, string) User agent on which the spam report occurred",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### Detalhes da propriedade

- O comportamento do site `dispatch_id` difere entre o canva e as campanhas porque a Braze trata as etapas do canva (exceto as etapas de entrada, que podem ser programadas) como eventos disparados, mesmo quando estão programadas. Saiba mais sobre o [comportamento do ID de despacho]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
{% endapi %}

{% api %}
## Envio de e-mail Enviar eventos

{% apitags %}
Envio de e-mail
{% endapitags %}

Esse evento ocorre quando uma solicitação de envio de e-mail foi comunicada com êxito entre o Braze e o SendGrid. No entanto, isso não significa que o e-mail foi recebido na caixa de entrada do usuário final.

{% tabs %}
{% tab Amplitude %}
```json
// Email Send (users.messages.email.Send)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "email_address" : "(required, string) [PII] Email address of the user",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Email Send (users.messages.email.Send)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "email_address" : "(required, string) [PII] Email address of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Email Sends (users.messages.email.Send)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
          "from_domain" : "(optional, string) Sending domain for the email",
          "ip_pool" : "(optional, string) IP pool from which the email send was made",
          "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user",
    "email" : "(required, string) [PII] Email address of the user"
  }
}
```
{% endtab %}

{% tab Segmento %}
```json
// Email Sent (users.messages.email.Send)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : {
      "email" : "(required, string) [PII] Email address of the user"
    },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Armazenamento em nuvem %}
```json
// users.messages.email.Send

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "email_address" : "(required, string) [PII] Email address of the user",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "ip_pool" : "(optional, string) IP pool from which the email send was made",
  "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### Detalhes da propriedade

- O comportamento do site `dispatch_id` difere entre o canva e as campanhas porque a Braze trata as etapas do canva (exceto as etapas de entrada, que podem ser programadas) como eventos disparados, mesmo quando estão programadas. Saiba mais sobre o [comportamento do ID de despacho]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
- `message_extras` permite que você anote seus eventos de envio com dados dinâmicos do conteúdo conectado, atributos personalizados (como idioma, país) e propriedades de entrada nos canvas. Consulte [Envio de mensagens extras]({{site.baseurl}}/message_extras_tag/) para saber mais.
{% endapi %}

{% api %}
## Eventos de envio de e-mail Soft Bounce

{% apitags %}
Envio de e-mail, bounce
{% endapitags %}

Esse evento ocorre quando um prestador de serviço de Internet retorna um soft bounce. Um soft bounce significa que um e-mail não pôde ser entregue devido a uma falha temporária de entregabilidade.

{% tabs %}
{% tab Amplitude %}
```json
// Email Soft Bounce (users.messages.email.SoftBounce)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "bounce_reason" : "(optional, string) [PII] The SMTP reason code and user friendly message received for this bounce event",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "email_address" : "(required, string) [PII] Email address of the user",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Email Soft Bounce (users.messages.email.SoftBounce)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "bounce_reason" : "(optional, string) [PII] The SMTP reason code and user friendly message received for this bounce event",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "email_address" : "(required, string) [PII] Email address of the user",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Email Soft Bounces (users.messages.email.SoftBounce)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "bounce_reason" : "(optional, string) [PII] The SMTP reason code and user friendly message received for this bounce event",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
          "from_domain" : "(optional, string) Sending domain for the email",
          "ip_pool" : "(optional, string) IP pool from which the email send was made",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user",
    "email" : "(required, string) [PII] Email address of the user"
  }
}
```
{% endtab %}

{% tab Segmento %}
```json
// Email Soft Bounced (users.messages.email.SoftBounce)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : {
      "email" : "(required, string) [PII] Email address of the user"
    },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "bounce_reason" : "(optional, string) [PII] The SMTP reason code and user friendly message received for this bounce event",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Armazenamento em nuvem %}
```json
// users.messages.email.SoftBounce

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "bounce_reason" : "(optional, string) [PII] The SMTP reason code and user friendly message received for this bounce event",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "email_address" : "(required, string) [PII] Email address of the user",
  "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "from_domain" : "(optional, string) Sending domain for the email",
  "id" : "(required, string) Globally unique ID for this event",
  "ip_pool" : "(optional, string) IP pool from which the email send was made",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "sending_ip" : "(optional, string) IP address from which the email send was made",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### Detalhes da propriedade

- O comportamento do site `dispatch_id` difere entre o canva e as campanhas porque a Braze trata as etapas do canva (exceto as etapas de entrada, que podem ser programadas) como eventos disparados, mesmo quando estão programadas. Saiba mais sobre o [comportamento do ID de despacho]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
{% endapi %}

{% api %}
## Eventos de cancelamento de inscrição de e-mail

{% apitags %}
Envio de e-mail, inscrição
{% endapitags %}

Esse evento ocorre quando o usuário final clica em "cancelar inscrição" no e-mail.

{% alert important %}
O evento `Unsubscribe` é, na verdade, um evento de clique especializado que é disparado quando o usuário clica no ink de cancelamento de inscrição no e-mail (seja um link normal de cancelamento de inscrição no corpo ou no rodapé do e-mail, seja usando o [cabeçalho list-unsubscribe]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/email_settings#include-a-list-unsubscribe-header)), e não quando o usuário muda o estado para unsubscribed. Se a alteração do estado da inscrição for enviada por meio da API ou por meio de um link de cancelamento de inscrição personalizado (não Braze), ela não disparará um evento no Currents.
{% endalert %}

{% tabs %}
{% tab Amplitude %}
```json
// Email Unsubscribe (users.messages.email.Unsubscribe)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "email_address" : "(required, string) [PII] Email address of the user",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Email Unsubscribe (users.messages.email.Unsubscribe)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "email_address" : "(required, string) [PII] Email address of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Email Unsubscribes (users.messages.email.Unsubscribe)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "ip_pool" : "(optional, string) IP pool from which the email send was made",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user",
    "email" : "(required, string) [PII] Email address of the user"
  }
}
```
{% endtab %}

{% tab Segmento %}
```json
// Unsubscribed (users.messages.email.Unsubscribe)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : {
      "email" : "(required, string) [PII] Email address of the user"
    },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Armazenamento em nuvem %}
```json
// users.messages.email.Unsubscribe

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "email_address" : "(required, string) [PII] Email address of the user",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "ip_pool" : "(optional, string) IP pool from which the email send was made",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### Detalhes da propriedade

- O comportamento do site `dispatch_id` difere entre o canva e as campanhas porque a Braze trata as etapas do canva (exceto as etapas de entrada, que podem ser programadas) como eventos disparados, mesmo quando estão programadas. Saiba mais sobre o [comportamento do ID de despacho]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
{% endapi %}

{% api %}
## Feature Flag Experimento Eventos de impressão

{% apitags %}
FeatureFlags, Impressão
{% endapitags %}

Esse evento ocorre sempre que um usuário tem a oportunidade de interagir com o seu recurso ou quando ele poderia ter interagido se o recurso estivesse desativado (no caso de um grupo de controle em um Testes A/B).

As impressões do Feature Flag são registradas apenas uma vez por sessão.


{% tabs %}
{% tab Amplitude %}
```json
// Feature Flag Experiment Impression (users.messages.featureflag.Impression)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_model" : "(optional, string) Model of the device",
    "feature_flag_id_name" : "(optional, string) The Feature Flag Rollout identifier",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "timezone" : "(optional, string) Time zone of the user"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Feature Flag Experiment Impression (users.messages.featureflag.Impression)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "feature_flag_id_name" : "(optional, string) The Feature Flag Rollout identifier",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Feature Flag Experiment Impressions (users.messages.featureflag.Impression)

{
  "device_info" : {
    "device_model" : "(optional, string) Model of the device",
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred",
    "platform" : "(optional, string) Platform of the device"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "feature_flag_id_name" : "(optional, string) The Feature Flag Rollout identifier",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segmento %}
```json
// Feature Flag Experiment Impressed (users.messages.featureflag.Impression)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : {
      "model" : "(optional, string) Model of the device",
      "type" : "(optional, string) Platform of the device"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "feature_flag_id_name" : "(optional, string) The Feature Flag Rollout identifier",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Armazenamento em nuvem %}
```json
// users.messages.featureflag.Impression

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "carrier" : "(optional, string) Carrier of the device",
  "country" : "(optional, string) [PII] Country of the user",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "feature_flag_id_name" : "(optional, string) The Feature Flag Rollout identifier",
  "gender" : "(optional, string) [PII] Gender of the user, one of ['M', 'F', 'O', 'N', 'P']",
  "id" : "(required, string) Globally unique ID for this event",
  "language" : "(optional, string) [PII] Language of the user",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "resolution" : "(optional, string) Resolution of the device",
  "sdk_version" : "(optional, string) Version of the Braze SDK in use during the event",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Eventos de interrupção de mensagens no app

{% apitags %}
Mensagens no app, Abortar
{% endapitags %}

Esse evento ocorre quando uma mensagem no app originalmente programada foi abortada.

{% tabs %}
{% tab Amplitude %}
```json
// In-App Message Abort (users.messages.inappmessage.Abort)

{
  "adid" : "(optional, string) [PII] Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_model" : "(optional, string) Model of the device",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) [PII] Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// In-App Message Abort (users.messages.inappmessage.Abort)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(optional, string) API ID of the card",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// In-App Message Aborts (users.messages.inappmessage.Abort)

{
  "device_info" : {
    "android_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "device_model" : "(optional, string) Model of the device",
    "ios_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred",
    "limit_ad_tracking" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "microsoft_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "platform" : "(optional, string) Platform of the device",
    "roku_advertising_id" : "(optional, string) [PII] Advertising identifier"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
          "abort_type" : "(optional, string) Type of abort",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segmento %}
```json
// In-App Message Aborted (users.messages.inappmessage.Abort)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : {
      "model" : "(optional, string) Model of the device",
      "type" : "(optional, string) Platform of the device"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(optional, string) API ID of the card",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Armazenamento em nuvem %}
```json
// users.messages.inappmessage.Abort

{
  "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
  "abort_type" : "(optional, string) Type of abort",
  "ad_id" : "(optional, string) [PII] Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "card_id" : "(optional, string) API ID of the card",
  "carrier" : "(optional, string) Carrier of the device",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "resolution" : "(optional, string) Resolution of the device",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event",
  "version" : "(required, string) Which version of in-app message, legacy or triggered"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Eventos de clique de mensagem no app

{% apitags %}
Mensagens no app, cliques
{% endapitags %}

Esse evento ocorre quando um usuário clica em uma mensagem no app.

{% alert note %}
`dispatch_id` está obsoleto e será removido na próxima versão do Currents.
{% endalert %}

{% tabs %}
{% tab Amplitude %}
```json
// In-App Message Click (users.messages.inappmessage.Click)

{
  "adid" : "(optional, string) [PII] Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "button_id" : "(optional, string) ID of the button clicked, if this click represents a click on a button",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(optional, string) API ID of the card",
    "device_model" : "(optional, string) Model of the device",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) [PII] Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// In-App Message Click (users.messages.inappmessage.Click)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "button_id" : "(optional, string) ID of the button clicked, if this click represents a click on a button",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(optional, string) API ID of the card",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// In-App Message Clicks (users.messages.inappmessage.Click)

{
  "device_info" : {
    "android_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "device_model" : "(optional, string) Model of the device",
    "ios_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred",
    "limit_ad_tracking" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "microsoft_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "platform" : "(optional, string) Platform of the device",
    "roku_advertising_id" : "(optional, string) [PII] Advertising identifier"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "button_id" : "(optional, string) ID of the button clicked, if this click represents a click on a button",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "card_id" : "(optional, string) API ID of the card",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segmento %}
```json
// In-App Message Clicked (users.messages.inappmessage.Click)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : {
      "model" : "(optional, string) Model of the device",
      "type" : "(optional, string) Platform of the device"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "button_id" : "(optional, string) ID of the button clicked, if this click represents a click on a button",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(optional, string) API ID of the card",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Armazenamento em nuvem %}
```json
// users.messages.inappmessage.Click

{
  "ad_id" : "(optional, string) [PII] Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "button_id" : "(optional, string) ID of the button clicked, if this click represents a click on a button",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "card_id" : "(optional, string) API ID of the card",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### Detalhes da propriedade

- Para `ad_id`, `ad_id_type` e `ad_tracking_enabled`, você precisa coletar explicitamente o IDFA do iOS e o ID de publicidade do Google do Android por meio dos SDKs nativos. Saiba mais sobre essa configuração para [iOS]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?sdktab=swift) e [Android]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android#android_google-advertising-id).
- Se estiver usando o Kafka para ingerir dados do [Currents]({{site.baseurl}}/user_guide/data/braze_currents/), entre em contato com o gerente de sucesso do cliente para ativar o envio de `ad_id`.
{% endapi %}

{% api %}
## Eventos de impressão de mensagens no app

{% apitags %}
Mensagens no app, impressões
{% endapitags %}

Esse evento ocorre quando um usuário visualiza uma mensagem no app.

{% alert note %}
`dispatch_id` está obsoleto e será removido na próxima versão do Currents.
{% endalert %}

{% tabs %}
{% tab Amplitude %}
```json
// In-App Message Impression (users.messages.inappmessage.Impression)

{
  "adid" : "(optional, string) [PII] Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(optional, string) API ID of the card",
    "device_model" : "(optional, string) Model of the device",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "locale_key" : "(optional, string) [PII] The key corresponding to the translations (for example 'en-us') used to compose this message (null for default).",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) [PII] Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// In-App Message Impression (users.messages.inappmessage.Impression)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(optional, string) API ID of the card",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "locale_key" : "(optional, string) [PII] The key corresponding to the translations (for example 'en-us') used to compose this message (null for default).",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// In-App Message Impressions (users.messages.inappmessage.Impression)

{
  "device_info" : {
    "android_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "device_model" : "(optional, string) Model of the device",
    "ios_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred",
    "limit_ad_tracking" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "microsoft_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "platform" : "(optional, string) Platform of the device",
    "roku_advertising_id" : "(optional, string) [PII] Advertising identifier"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "card_id" : "(optional, string) API ID of the card",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "locale_key" : "(optional, string) [PII] The key corresponding to the translations (for example 'en-us') used to compose this message (null for default).",
          "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segmento %}
```json
// In-App Message Viewed (users.messages.inappmessage.Impression)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : {
      "model" : "(optional, string) Model of the device",
      "type" : "(optional, string) Platform of the device"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(optional, string) API ID of the card",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "locale_key" : "(optional, string) [PII] The key corresponding to the translations (for example 'en-us') used to compose this message (null for default).",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Armazenamento em nuvem %}
```json
// users.messages.inappmessage.Impression

{
  "ad_id" : "(optional, string) [PII] Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "card_id" : "(optional, string) API ID of the card",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "locale_key" : "(optional, string) [PII] The key corresponding to the translations (for example 'en-us') used to compose this message (null for default).",
  "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### Detalhes da propriedade

- Para `ad_id`, `ad_id_type` e `ad_tracking_enabled`, você precisa coletar explicitamente o IDFA do iOS e o ID de publicidade do Google do Android por meio dos SDKs nativos. Saiba mais sobre essa configuração para [iOS]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?sdktab=swift) e [Android]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android#android_google-advertising-id).
- Se estiver usando o Kafka para ingerir dados do [Currents]({{site.baseurl}}/user_guide/data/braze_currents/), entre em contato com o gerente de sucesso do cliente para ativar o envio de `ad_id`.
{% endapi %}

{% api %}
## Eventos de resultados de atividades ao vivo

{% apitags %}
Atividade ao vivo, resultado
{% endapitags %}

Esse evento ocorre quando o Braze recebe uma resposta de um provedor terceirizado (e.g. APNs) após o envio da atividade ao vivo

{% tabs %}
{% tab Amplitude %}
```json
// Live Activity Outcome (users.messages.liveactivity.Outcome)

{
  "event_properties" : {
    "activity_attributes_type" : "(optional, string) Live Activity attribute type",
    "activity_id" : "(optional, string) Live Activity identifier",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "live_activity_event_outcome" : "(optional, string) Outcome of Live Activity event",
    "live_activity_event_type" : "(optional, string) Event type of Live Activity. One of ['start', 'update', 'end']",
    "push_to_start_token" : "(optional, string) Live Activity push to start token",
    "update_token" : "(optional, string) Live Activity update token"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Live Activity Outcome (users.messages.liveactivity.Outcome)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "activity_attributes_type" : "(optional, string) Live Activity attribute type",
    "activity_id" : "(optional, string) Live Activity identifier",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "live_activity_event_outcome" : "(optional, string) Outcome of Live Activity event",
    "live_activity_event_type" : "(optional, string) Event type of Live Activity. One of ['start', 'update', 'end']",
    "push_to_start_token" : "(optional, string) Live Activity push to start token",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token",
    "update_token" : "(optional, string) Live Activity update token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Live Activity Outcomes (users.messages.liveactivity.Outcome)

{
  "device_info" : { },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "activity_attributes_type" : "(optional, string) Live Activity attribute type",
          "activity_id" : "(optional, string) Live Activity identifier",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "live_activity_event_outcome" : "(optional, string) Outcome of Live Activity event",
          "live_activity_event_type" : "(optional, string) Event type of Live Activity. One of ['start', 'update', 'end']",
          "push_to_start_token" : "(optional, string) Live Activity push to start token",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "update_token" : "(optional, string) Live Activity update token"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segmento %}
```json
// Live Activity Outcome (users.messages.liveactivity.Outcome)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "activity_attributes_type" : "(optional, string) Live Activity attribute type",
    "activity_id" : "(optional, string) Live Activity identifier",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "live_activity_event_outcome" : "(optional, string) Outcome of Live Activity event",
    "live_activity_event_type" : "(optional, string) Event type of Live Activity. One of ['start', 'update', 'end']",
    "push_to_start_token" : "(optional, string) Live Activity push to start token",
    "update_token" : "(optional, string) Live Activity update token"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Armazenamento em nuvem %}
```json
// users.messages.liveactivity.Outcome

{
  "activity_attributes_type" : "(optional, string) Live Activity attribute type",
  "activity_id" : "(optional, string) Live Activity identifier",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "live_activity_event_outcome" : "(optional, string) Outcome of Live Activity event",
  "live_activity_event_type" : "(optional, string) Event type of Live Activity. One of ['start', 'update', 'end']",
  "push_to_start_token" : "(optional, string) Live Activity push to start token",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "update_token" : "(optional, string) Live Activity update token",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Atividade ao vivo Enviar eventos

{% apitags %}
Atividade ao vivo, envios
{% endapitags %}

Esse evento ocorre quando o backend do Braze faz uma solicitação ao seu provedor com relação ao Live Activity

{% tabs %}
{% tab Amplitude %}
```json
// Live Activity Send (users.messages.liveactivity.Send)

{
  "event_properties" : {
    "activity_attributes_type" : "(optional, string) Live Activity attribute type",
    "activity_id" : "(optional, string) Live Activity identifier",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "live_activity_event_type" : "(optional, string) Event type of Live Activity. One of ['start', 'update', 'end']",
    "push_to_start_token" : "(optional, string) Live Activity push to start token",
    "update_token" : "(optional, string) Live Activity update token"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Live Activity Send (users.messages.liveactivity.Send)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "activity_attributes_type" : "(optional, string) Live Activity attribute type",
    "activity_id" : "(optional, string) Live Activity identifier",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "live_activity_event_type" : "(optional, string) Event type of Live Activity. One of ['start', 'update', 'end']",
    "push_to_start_token" : "(optional, string) Live Activity push to start token",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token",
    "update_token" : "(optional, string) Live Activity update token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Live Activity Sends (users.messages.liveactivity.Send)

{
  "device_info" : { },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "activity_attributes_type" : "(optional, string) Live Activity attribute type",
          "activity_id" : "(optional, string) Live Activity identifier",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "live_activity_event_type" : "(optional, string) Event type of Live Activity. One of ['start', 'update', 'end']",
          "push_to_start_token" : "(optional, string) Live Activity push to start token",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "update_token" : "(optional, string) Live Activity update token"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segmento %}
```json
// Live Activity Sent (users.messages.liveactivity.Send)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "activity_attributes_type" : "(optional, string) Live Activity attribute type",
    "activity_id" : "(optional, string) Live Activity identifier",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "live_activity_event_type" : "(optional, string) Event type of Live Activity. One of ['start', 'update', 'end']",
    "push_to_start_token" : "(optional, string) Live Activity push to start token",
    "update_token" : "(optional, string) Live Activity update token"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Armazenamento em nuvem %}
```json
// users.messages.liveactivity.Send

{
  "activity_attributes_type" : "(optional, string) Live Activity attribute type",
  "activity_id" : "(optional, string) Live Activity identifier",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "live_activity_event_type" : "(optional, string) Event type of Live Activity. One of ['start', 'update', 'end']",
  "push_to_start_token" : "(optional, string) Live Activity push to start token",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "update_token" : "(optional, string) Live Activity update token",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Eventos de interrupção de notificações por push

{% apitags %}
Abortar, push
{% endapitags %}

Esse evento ocorre se uma mensagem de notificação por push foi abortada com base em Liquid aborts, etc.

{% tabs %}
{% tab Amplitude %}
```json
// Push Notification Abort (users.messages.pushnotification.Abort)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Push Notification Abort (users.messages.pushnotification.Abort)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Push Notification Aborts (users.messages.pushnotification.Abort)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred",
    "platform" : "(optional, string) Platform of the device"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
          "abort_type" : "(optional, string) Type of abort",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segmento %}
```json
// Push Notification Aborted (users.messages.pushnotification.Abort)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "platform" : "(required, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Armazenamento em nuvem %}
```json
// users.messages.pushnotification.Abort

{
  "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
  "abort_type" : "(optional, string) Type of abort",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "platform" : "(required, string) Platform of the device",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Eventos de bounce de notificações por push

{% apitags %}
Push, Envios, Bounce
{% endapitags %}

Esse evento ocorre quando um erro é recebido do serviço de Notificações por Push da Apple ou do Fire Cloud Messaging. Isso significa que a mensagem push sofreu bounce e, portanto, não foi entregue ao dispositivo do usuário.

{% tabs %}
{% tab Amplitude %}
```json
// Push Notification Bounce (users.messages.pushnotification.Bounce)

{
  "adid" : "(optional, string) [PII] Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) [PII] Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Push Notification Bounce (users.messages.pushnotification.Bounce)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Push Notification Bounces (users.messages.pushnotification.Bounce)

{
  "device_info" : {
    "android_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "ios_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred",
    "limit_ad_tracking" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "microsoft_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "platform" : "(optional, string) Platform of the device",
    "roku_advertising_id" : "(optional, string) [PII] Advertising identifier"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segmento %}
```json
// Push Notification Bounced (users.messages.pushnotification.Bounce)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Armazenamento em nuvem %}
```json
// users.messages.pushnotification.Bounce

{
  "ad_id" : "(optional, string) [PII] Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "platform" : "(optional, string) Platform of the device",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### Detalhes da propriedade

- Se estiver usando o Kafka para ingerir dados [do Currents]({{site.baseurl}}/user_guide/data/braze_currents/), entre em contato com seu gerente de sucesso do cliente ou gerente de conta para ativar o flipper de recursos para enviar `ad_id`.
{% endapi %}

{% api %}
## Notificações por push Eventos de abertura em primeiro plano do iOS

{% apitags %}
Push, iOS, Envios
{% endapitags %}

Esse evento não é compatível com nosso [Swift SDK](https://github.com/braze-inc/braze-swift-sdk) e agora está obsoleto em nosso [Obj-C SDK](https://github.com/Appboy/appboy-ios-sdk).

{% tabs %}
{% tab Amplitude %}
```json
// Push Notification iOS Foreground Open (users.messages.pushnotification.IosForeground)

{
  "adid" : "(optional, string) [PII] Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_model" : "(optional, string) Model of the device",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) [PII] Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Push Notification iOS Foreground Open (users.messages.pushnotification.IosForeground)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Segmento %}
```json
// Ios Foreground Push Opened (users.messages.pushnotification.IosForeground)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : {
      "model" : "(optional, string) Model of the device",
      "type" : "(optional, string) Platform of the device"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Armazenamento em nuvem %}
```json
// users.messages.pushnotification.IosForeground

{
  "ad_id" : "(optional, string) [PII] Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "platform" : "(required, string) Platform of the device",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### Detalhes da propriedade

- Para `ad_id`, `ad_id_type` e `ad_tracking_enabled`, você precisa coletar explicitamente o IDFA do iOS e o ID de publicidade do Google do Android por meio dos SDKs nativos. Saiba mais sobre essa configuração para [iOS]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?sdktab=swift) e [Android]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android#android_google-advertising-id).
- Se estiver usando o Kafka para ingerir dados do [Currents]({{site.baseurl}}/user_guide/data/braze_currents/), entre em contato com o gerente de sucesso do cliente para ativar o envio de `ad_id`.
{% endapi %}

{% api %}
## Notificações por push Eventos abertos

{% apitags %}
Push, Aberturas
{% endapitags %}

Esse evento ocorre quando um usuário clica diretamente na notificação por push para abrir o aplicativo. Atualmente, os eventos Push Open referem-se especificamente a "aberturas diretas" em vez de "aberturas totais". Isso não inclui estatísticas mostradas no nível da campanha de "aberturas por influência", pois elas não são atribuídas no nível do usuário.

{% tabs %}
{% tab Amplitude %}
```json
// Push Notification Open (users.messages.pushnotification.Open)

{
  "adid" : "(optional, string) [PII] Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_model" : "(optional, string) Model of the device",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) [PII] Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Push Notification Open (users.messages.pushnotification.Open)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Push Notification Opens (users.messages.pushnotification.Open)

{
  "device_info" : {
    "android_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "device_model" : "(optional, string) Model of the device",
    "ios_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred",
    "limit_ad_tracking" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "microsoft_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "platform" : "(optional, string) Platform of the device",
    "roku_advertising_id" : "(optional, string) [PII] Advertising identifier"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segmento %}
```json
// Push Notification Tapped (users.messages.pushnotification.Open)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : {
      "model" : "(optional, string) Model of the device",
      "type" : "(optional, string) Platform of the device"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Armazenamento em nuvem %}
```json
// users.messages.pushnotification.Open

{
  "ad_id" : "(optional, string) [PII] Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "button_action_type" : "(optional, string) Action type of the push notification button, null if not from a button click. One of ['uri', 'deep_link', 'none', 'close']",
  "button_string" : "(optional, string) Identifier (button_string) of the push notification button clicked. null if not from a button click",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### Detalhes da propriedade

- Para `ad_id`, `ad_id_type` e `ad_tracking_enabled`, você precisa coletar explicitamente o IDFA do iOS e o ID de publicidade do Google do Android por meio dos SDKs nativos. Saiba mais sobre essa configuração para [iOS]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?sdktab=swift) e [Android]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android#android_google-advertising-id).
- Se estiver usando o Kafka para ingerir dados do [Currents]({{site.baseurl}}/user_guide/data/braze_currents/), entre em contato com o gerente de sucesso do cliente para ativar o envio de `ad_id`.
{% endapi %}

{% api %}
## Eventos de envio de notificações por push

{% apitags %}
Push, Envios
{% endapitags %}

Esse evento ocorre quando a Braze processa uma mensagem push para um usuário, comunicando-a ao Serviço de Notificações por Push da Apple ou ao Fire Cloud Messaging. Isso não significa que o push foi entregue ao dispositivo, apenas que uma mensagem foi enviada.

{% tabs %}
{% tab Amplitude %}
```json
// Push Notification Send (users.messages.pushnotification.Send)

{
  "adid" : "(optional, string) [PII] Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "locale_key" : "(optional, string) [PII] The key corresponding to the translations (for example 'en-us') used to compose this message (null for default).",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) [PII] Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Push Notification Send (users.messages.pushnotification.Send)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "locale_key" : "(optional, string) [PII] The key corresponding to the translations (for example 'en-us') used to compose this message (null for default).",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Push Notification Sends (users.messages.pushnotification.Send)

{
  "device_info" : {
    "android_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "ios_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred",
    "limit_ad_tracking" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "microsoft_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "platform" : "(optional, string) Platform of the device",
    "roku_advertising_id" : "(optional, string) [PII] Advertising identifier"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "locale_key" : "(optional, string) [PII] The key corresponding to the translations (for example 'en-us') used to compose this message (null for default).",
          "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segmento %}
```json
// Push Notification Sent (users.messages.pushnotification.Send)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "locale_key" : "(optional, string) [PII] The key corresponding to the translations (for example 'en-us') used to compose this message (null for default).",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "platform" : "(required, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Armazenamento em nuvem %}
```json
// users.messages.pushnotification.Send

{
  "ad_id" : "(optional, string) [PII] Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "locale_key" : "(optional, string) [PII] The key corresponding to the translations (for example 'en-us') used to compose this message (null for default).",
  "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "platform" : "(required, string) Platform of the device",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### Detalhes da propriedade

- Para `ad_id`, `ad_id_type` e `ad_tracking_enabled`, você precisa coletar explicitamente o IDFA do iOS e o ID de publicidade do Google do Android por meio dos SDKs nativos. Saiba mais sobre essa configuração para [iOS]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?sdktab=swift) e [Android]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android#android_google-advertising-id).
- Se estiver usando o Kafka para ingerir dados do [Currents]({{site.baseurl}}/user_guide/data/braze_currents/), entre em contato com o gerente de sucesso do cliente para ativar o envio de `ad_id`.
- `message_extras` permite que você anote seus eventos de envio com dados dinâmicos do conteúdo conectado, atributos personalizados (como idioma, país) e propriedades de entrada nos canvas. Consulte [Envio de mensagens extras]({{site.baseurl}}/message_extras_tag/) para saber mais.
{% endapi %}

{% api %}
## Eventos de abortamento de SMS

{% apitags %}
Abortar, SMS
{% endapitags %}

Esse evento ocorre se uma mensagem SMS foi abortada com base em Liquid aborts, etc.

{% tabs %}
{% tab Amplitude %}
```json
// SMS Abort (users.messages.sms.Abort)

{
  "event_properties" : {
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "subscription_group_id" : "(optional, string) Subscription group API ID"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// SMS Abort (users.messages.sms.Abort)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// SMS Aborts (users.messages.sms.Abort)

{
  "device_info" : { },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
          "abort_type" : "(optional, string) Type of abort",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "subscription_group_id" : "(optional, string) Subscription group API ID"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segmento %}
```json
// SMS Aborted (users.messages.sms.Abort)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "subscription_group_id" : "(optional, string) Subscription group API ID"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Armazenamento em nuvem %}
```json
// users.messages.sms.Abort

{
  "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
  "abort_type" : "(optional, string) Type of abort",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Eventos de envio da operadora de SMS

{% apitags %}
SMS, Envios
{% endapitags %}

Esse evento ocorre quando um SMS é enviado à operadora.

{% alert important %}
`CarrierSend` é suportado apenas para usuários em infraestrutura legada.
{% endalert %}

{% tabs %}
{% tab Amplitude %}
```json
// SMS Carrier Send (users.messages.sms.CarrierSend)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// SMS Carrier Send (users.messages.sms.CarrierSend)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// SMS Carrier Sends (users.messages.sms.CarrierSend)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "subscription_group_id" : "(optional, string) Subscription group API ID"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segmento %}
```json
// SMS Sent to Carrier (users.messages.sms.CarrierSend)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : {
      "phone" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
    },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Armazenamento em nuvem %}
```json
// users.messages.sms.CarrierSend

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Eventos de entrega de SMS

{% apitags %}
SMS, Entrega
{% endapitags %}

Esse evento ocorre quando um SMS é entregue com êxito ao telefone celular do usuário.

{% tabs %}
{% tab Amplitude %}
```json
// SMS Delivery (users.messages.sms.Delivery)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// SMS Delivery (users.messages.sms.Delivery)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// SMS Deliveries (users.messages.sms.Delivery)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "subscription_group_id" : "(optional, string) Subscription group API ID"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segmento %}
```json
// SMS Delivered (users.messages.sms.Delivery)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : {
      "phone" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
    },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Armazenamento em nuvem %}
```json
// users.messages.sms.Delivery

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Eventos de falha na entrega de SMS

{% apitags %}
SMS, Entrega
{% endapitags %}

Esse evento ocorre quando um SMS apresenta falha na entrega. Use esse evento e os códigos de erro fornecidos para ajudar a solucionar problemas com a entrega de SMS.

{% tabs %}
{% tab Amplitude %}
```json
// SMS Delivery Failure (users.messages.sms.DeliveryFailure)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "error" : "(optional, string) Error name",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "provider_error_code" : "(optional, string) Error code from the SMS provider",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// SMS Delivery Failure (users.messages.sms.DeliveryFailure)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "error" : "(optional, string) Error name",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "provider_error_code" : "(optional, string) Error code from the SMS provider",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// SMS Delivery Failures (users.messages.sms.DeliveryFailure)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "error" : "(optional, string) Error name",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "provider_error_code" : "(optional, string) Error code from the SMS provider",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "subscription_group_id" : "(optional, string) Subscription group API ID"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segmento %}
```json
// SMS Delivery Failed (users.messages.sms.DeliveryFailure)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : {
      "phone" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
    },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "error" : "(optional, string) Error name",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "provider_error_code" : "(optional, string) Error code from the SMS provider",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Armazenamento em nuvem %}
```json
// users.messages.sms.DeliveryFailure

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "error" : "(optional, string) Error name",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "provider_error_code" : "(optional, string) Error code from the SMS provider",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Eventos de entrada de SMS recebidos

{% apitags %}
SMS, InboundReceived
{% endapitags %}

Esse evento ocorre quando um dos seus usuários envia um SMS para um número de telefone em um dos seus grupos de inscrições do Braze SMS.

Quando o Braze recebe um SMS de entrada, atribuímos essa mensagem de entrada a qualquer usuário que compartilhe esse número de telefone. Como resultado, você poderá receber vários eventos por mensagem recebida se vários usuários na sua instância do Braze compartilharem o mesmo número de telefone. Se for necessária a atribuição de IDs de usuários específicos com base em mensagens anteriores enviadas a esse usuário, é possível usar o evento SMS Delivered para atribuir eventos Inbound Received ao ID do usuário que recebeu mais recentemente uma mensagem do seu número Braze.

Se detectarmos que essa mensagem de entrada é uma resposta a uma campanha de saída ou a um componente do Canvas enviado pelo Braze, também incluiremos os metadados da campanha ou do Canvas no evento. O Braze define uma resposta como uma mensagem recebida dentro de quatro horas após uma mensagem enviada. No entanto, há um cache de um minuto para as informações da campanha de atribuição do último SMS de saída recebido.


{% tabs %}
{% tab Amplitude %}
```json
// SMS Inbound Received (users.messages.sms.InboundReceive)

{
  "event_properties" : {
    "action" : "(required, string) Action taken in response to this message. (for example Subscribed, Unsubscribed or None).",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "inbound_phone_number" : "(required, string) The inbound number that the message was sent to",
    "media_urls" : "(optional, array of string) Media URLs from the user",
    "message_body" : "(optional, string) Typed response from the user",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "user_phone_number" : "(required, string) [PII] The user's phone number from which the message was received"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// SMS Inbound Received (users.messages.sms.InboundReceive)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "action" : "(required, string) Action taken in response to this message. (for example Subscribed, Unsubscribed or None).",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "inbound_phone_number" : "(required, string) The inbound number that the message was sent to",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "media_urls" : "(optional, array of string) Media URLs from the user",
    "message_body" : "(optional, string) Typed response from the user",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token",
    "user_phone_number" : "(required, string) [PII] The user's phone number from which the message was received"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// SMS Inbound Received (users.messages.sms.InboundReceive)

{
  "device_info" : { },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "action" : "(required, string) Action taken in response to this message. (for example Subscribed, Unsubscribed or None).",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "inbound_phone_number" : "(required, string) The inbound number that the message was sent to",
          "message_body" : "(optional, string) Typed response from the user",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "subscription_group_id" : "(optional, string) Subscription group API ID"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) [PII] The user's phone number from which the message was received"
  },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segmento %}
```json
// SMS Inbound Received (users.messages.sms.InboundReceive)

{
  "anonymousId" : "(optional, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : {
      "phone" : "(required, string) [PII] The user's phone number from which the message was received"
    },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "action" : "(required, string) Action taken in response to this message. (for example Subscribed, Unsubscribed or None).",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "inbound_phone_number" : "(required, string) The inbound number that the message was sent to",
    "media_urls" : "(optional, array of string) Media URLs from the user",
    "message_body" : "(optional, string) Typed response from the user",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "subscription_group_id" : "(optional, string) Subscription group API ID"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Armazenamento em nuvem %}
```json
// users.messages.sms.InboundReceive

{
  "action" : "(required, string) Action taken in response to this message. (for example Subscribed, Unsubscribed or None).",
  "app_group_id" : "(required, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "inbound_phone_number" : "(required, string) The inbound number that the message was sent to",
  "media_urls" : "(optional, array of string) Media URLs from the user",
  "message_body" : "(required, string) Typed response from the user",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) Braze user ID of the user who performed this event",
  "user_phone_number" : "(required, string) [PII] The user's phone number from which the message was received"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Eventos de rejeição de SMS

{% apitags %}
SMS, Rejeição
{% endapitags %}

Esse evento ocorre quando um envio de SMS é rejeitado pela operadora, o que pode ocorrer por vários motivos. Use esse evento e os códigos de erro fornecidos para ajudar a solucionar problemas com a entrega de SMS.

{% tabs %}
{% tab Amplitude %}
```json
// SMS Rejection (users.messages.sms.Rejection)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "error" : "(optional, string) Error name",
    "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "provider_error_code" : "(optional, string) Error code from the SMS provider",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// SMS Rejection (users.messages.sms.Rejection)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "error" : "(optional, string) Error name",
    "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "provider_error_code" : "(optional, string) Error code from the SMS provider",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// SMS Rejections (users.messages.sms.Rejection)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "error" : "(optional, string) Error name",
          "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "provider_error_code" : "(optional, string) Error code from the SMS provider",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "subscription_group_id" : "(optional, string) Subscription group API ID"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segmento %}
```json
// SMS Rejected (users.messages.sms.Rejection)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : {
      "phone" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
    },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "error" : "(optional, string) Error name",
    "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "provider_error_code" : "(optional, string) Error code from the SMS provider",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Armazenamento em nuvem %}
```json
// users.messages.sms.Rejection

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "error" : "(optional, string) Error name",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "provider_error_code" : "(optional, string) Error code from the SMS provider",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Eventos de envio de SMS

{% apitags %}
SMS, Envios
{% endapitags %}

Esse evento ocorre quando um usuário envia um SMS.

{% tabs %}
{% tab Amplitude %}
```json
// SMS Send (users.messages.sms.Send)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "category" : "(optional, string) Keyword category name, only populated for auto-reply messages: 'opt-in', 'opt-out', 'help', or custom value",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// SMS Send (users.messages.sms.Send)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "category" : "(optional, string) Keyword category name, only populated for auto-reply messages: 'opt-in', 'opt-out', 'help', or custom value",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// SMS Sends (users.messages.sms.Send)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "category" : "(optional, string) Keyword category name, only populated for auto-reply messages: 'opt-in', 'opt-out', 'help', or custom value",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "subscription_group_id" : "(optional, string) Subscription group API ID"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segmento %}
```json
// SMS Sent (users.messages.sms.Send)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : {
      "phone" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
    },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "category" : "(optional, string) Keyword category name, only populated for auto-reply messages: 'opt-in', 'opt-out', 'help', or custom value",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Armazenamento em nuvem %}
```json
// users.messages.sms.Send

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "category" : "(optional, string) Keyword category name, only populated for auto-reply messages: 'opt-in', 'opt-out', 'help', or custom value",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### Detalhes da propriedade

- `message_extras` permite que você anote seus eventos de envio com dados dinâmicos do conteúdo conectado, atributos personalizados (como idioma, país) e propriedades de entrada nos canvas. Consulte [Envio de mensagens extras]({{site.baseurl}}/message_extras_tag/) para saber mais.
{% endapi %}

{% api %}
## Eventos de clique em links curtos de SMS

{% apitags %}
SMS, cliques
{% endapitags %}

Esse evento ocorre quando um usuário clica em um link curto de SMS.

{% tabs %}
{% tab Amplitude %}
```json
// SMS Short Link Click (users.messages.sms.ShortLinkClick)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "is_suspected_bot_click" : "(optional, boolean) Whether this event was processed as a bot event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "short_url" : "(required, string) Shortened url that was clicked",
    "suspected_bot_click_reason" : "(optional, array of string) Why this event was classified as a bot",
    "url" : "(optional, string) URL that the user clicked on",
    "user_agent" : "(optional, string) User agent on which the spam report occurred",
    "user_phone_number" : "(optional, string) [PII] The user's phone number from which the message was received"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// SMS Short Link Click (users.messages.sms.ShortLinkClick)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "is_suspected_bot_click" : "(optional, boolean) Whether this event was processed as a bot event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "short_url" : "(required, string) Shortened url that was clicked",
    "suspected_bot_click_reason" : "(optional, array of string) Why this event was classified as a bot",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token",
    "url" : "(optional, string) URL that the user clicked on",
    "user_agent" : "(optional, string) User agent on which the spam report occurred",
    "user_phone_number" : "(optional, string) [PII] The user's phone number from which the message was received"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// SMS Short Link Clicks (users.messages.sms.ShortLinkClick)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "is_suspected_bot_click" : "(optional, boolean) Whether this event was processed as a bot event",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "short_url" : "(required, string) Shortened url that was clicked",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "url" : "(optional, string) URL that the user clicked on",
          "user_agent" : "(optional, string) User agent on which the spam report occurred"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) [PII] The user's phone number from which the message was received"
  },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segmento %}
```json
// SMS Short Link Clicked (users.messages.sms.ShortLinkClick)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : {
      "phone" : "(optional, string) [PII] The user's phone number from which the message was received"
    },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "is_suspected_bot_click" : "(optional, boolean) Whether this event was processed as a bot event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "short_url" : "(required, string) Shortened url that was clicked",
    "suspected_bot_click_reason" : "(optional, array of string) Why this event was classified as a bot",
    "url" : "(optional, string) URL that the user clicked on",
    "user_agent" : "(optional, string) User agent on which the spam report occurred"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Armazenamento em nuvem %}
```json
// users.messages.sms.ShortLinkClick

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "is_suspected_bot_click" : "(optional, boolean) Whether this event was processed as a bot event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "short_url" : "(required, string) Shortened url that was clicked",
  "suspected_bot_click_reason" : "(optional, array of string) Why this event was classified as a bot",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "url" : "(required, string) URL that the user clicked on",
  "user_agent" : "(optional, string) User agent on which the spam report occurred",
  "user_id" : "(required, string) Braze user ID of the user who performed this event",
  "user_phone_number" : "(optional, string) [PII] The user's phone number from which the message was received"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Eventos de abortamento de webhook

{% apitags %}
Abortar, Webhooks
{% endapitags %}

Esse evento ocorre se uma mensagem de webhook foi abortada com base em Liquid aborts, etc.

{% tabs %}
{% tab Amplitude %}
```json
// Webhook Abort (users.messages.webhook.Abort)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Webhook Abort (users.messages.webhook.Abort)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Webhook Aborts (users.messages.webhook.Abort)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
          "abort_type" : "(optional, string) Type of abort",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segmento %}
```json
// Webhook Aborted (users.messages.webhook.Abort)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Armazenamento em nuvem %}
```json
// users.messages.webhook.Abort

{
  "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
  "abort_type" : "(optional, string) Type of abort",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Eventos de falha do webhook

{% apitags %}
Falha, Webhooks
{% endapitags %}

Esse evento ocorre se uma mensagem de webhook foi entregue, mas falhou com uma resposta de erro do endpoint.

{% tabs %}
{% tab Amplitude %}
```json
// Webhook Failure (users.messages.webhook.Failure)

{
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "content_length" : "(optional, int) Content length of the response",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "endpoint_url" : "(optional, string) The endpoint URL of the failed webhook",
    "host" : "(optional, string) The host of the webhook URL that returned a failure response",
    "http_status_code" : "(optional, int) HTTP status code of the response",
    "is_terminal" : "(optional, boolean) Whether this event was the terminal attempt in a send",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "raw_response" : "(optional, string) Truncated raw response from endpoint",
    "retry_count" : "(optional, int) Number of webhook sends attempted before giving up",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "url_path" : "(optional, string) The path of the webhook URL that returned a failure response",
    "webhook_duration" : "(optional, int) Total duration of this request in milliseconds",
    "webhook_failure_source" : "(optional, string) To tell whether an error was created by Braze or by the endpoint itself. The source field could be External Endpoint, Treat no status code to host unreachable"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Webhook Failure (users.messages.webhook.Failure)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "content_length" : "(optional, int) Content length of the response",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "endpoint_url" : "(optional, string) The endpoint URL of the failed webhook",
    "host" : "(optional, string) The host of the webhook URL that returned a failure response",
    "http_status_code" : "(optional, int) HTTP status code of the response",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "is_terminal" : "(optional, boolean) Whether this event was the terminal attempt in a send",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "raw_response" : "(optional, string) Truncated raw response from endpoint",
    "retry_count" : "(optional, int) Number of webhook sends attempted before giving up",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token",
    "url_path" : "(optional, string) The path of the webhook URL that returned a failure response",
    "webhook_duration" : "(optional, int) Total duration of this request in milliseconds",
    "webhook_failure_source" : "(optional, string) To tell whether an error was created by Braze or by the endpoint itself. The source field could be External Endpoint, Treat no status code to host unreachable"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Webhook Failures (users.messages.webhook.Failure)

{
  "device_info" : { },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "content_length" : "(optional, int) Content length of the response",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "endpoint_url" : "(optional, string) The endpoint URL of the failed webhook",
          "host" : "(optional, string) The host of the webhook URL that returned a failure response",
          "http_status_code" : "(optional, int) HTTP status code of the response",
          "is_terminal" : "(optional, boolean) Whether this event was the terminal attempt in a send",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "raw_response" : "(optional, string) Truncated raw response from endpoint",
          "retry_count" : "(optional, int) Number of webhook sends attempted before giving up",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "url_path" : "(optional, string) The path of the webhook URL that returned a failure response",
          "webhook_duration" : "(optional, int) Total duration of this request in milliseconds",
          "webhook_failure_source" : "(optional, string) To tell whether an error was created by Braze or by the endpoint itself. The source field could be External Endpoint, Treat no status code to host unreachable"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segmento %}
```json
// Webhook Failed (users.messages.webhook.Failure)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "content_length" : "(optional, int) Content length of the response",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "endpoint_url" : "(optional, string) The endpoint URL of the failed webhook",
    "host" : "(optional, string) The host of the webhook URL that returned a failure response",
    "http_status_code" : "(optional, int) HTTP status code of the response",
    "is_terminal" : "(optional, boolean) Whether this event was the terminal attempt in a send",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "raw_response" : "(optional, string) Truncated raw response from endpoint",
    "retry_count" : "(optional, int) Number of webhook sends attempted before giving up",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "url_path" : "(optional, string) The path of the webhook URL that returned a failure response",
    "webhook_duration" : "(optional, int) Total duration of this request in milliseconds",
    "webhook_failure_source" : "(optional, string) To tell whether an error was created by Braze or by the endpoint itself. The source field could be External Endpoint, Treat no status code to host unreachable"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Armazenamento em nuvem %}
```json
// users.messages.webhook.Failure

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "content_length" : "(optional, int) Content length of the response",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "endpoint_url" : "(optional, string) The endpoint URL of the failed webhook",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "host" : "(optional, string) The host of the webhook URL that returned a failure response",
  "http_status_code" : "(optional, int) HTTP status code of the response",
  "id" : "(required, string) Globally unique ID for this event",
  "is_terminal" : "(optional, boolean) Whether this event was the terminal attempt in a send",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "raw_response" : "(optional, string) Truncated raw response from endpoint",
  "retry_count" : "(optional, int) Number of webhook sends attempted before giving up",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "url_path" : "(optional, string) The path of the webhook URL that returned a failure response",
  "user_id" : "(required, string) Braze user ID of the user who performed this event",
  "webhook_duration" : "(optional, int) Total duration of this request in milliseconds",
  "webhook_failure_source" : "(optional, string) To tell whether an error was created by Braze or by the endpoint itself. The source field could be External Endpoint, Treat no status code to host unreachable"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Eventos de envio de webhook

{% apitags %}
Webhooks, envios
{% endapitags %}

Esse evento ocorre quando um webhook foi processado e enviado para o terceiro especificado nesse webhook. Observe que isso não significa que a solicitação foi recebida ou não.

{% tabs %}
{% tab Amplitude %}
```json
// Webhook Send (users.messages.webhook.Send)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Webhook Send (users.messages.webhook.Send)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Webhook Sends (users.messages.webhook.Send)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segmento %}
```json
// Webhook Sent (users.messages.webhook.Send)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Armazenamento em nuvem %}
```json
// users.messages.webhook.Send

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### Detalhes da propriedade

- `message_extras` permite que você anote seus eventos de envio com dados dinâmicos do conteúdo conectado, atributos personalizados (como idioma, país) e propriedades de entrada nos canvas. Consulte [Envio de mensagens extras]({{site.baseurl}}/message_extras_tag/) para saber mais.
{% endapi %}

{% api %}
## Eventos de abortamento do WhatsApp

{% apitags %}
WhatsApp, Abortar
{% endapitags %}

Esse evento ocorre se uma mensagem do WhatsApp foi abortada com base em abortos de Liquid, etc.

{% tabs %}
{% tab Amplitude %}
```json
// WhatsApp Abort (users.messages.whatsapp.Abort)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, long) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// WhatsApp Abort (users.messages.whatsapp.Abort)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "time" : "(required, long) UNIX timestamp at which the event happened",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// WhatsApp Aborts (users.messages.whatsapp.Abort)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
          "abort_type" : "(optional, string) Type of abort",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "subscription_group_id" : "(optional, string) Subscription group API ID"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, long) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segmento %}
```json
// WhatsApp Aborted (users.messages.whatsapp.Abort)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : {
      "phone" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
    },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "subscription_group_id" : "(optional, string) Subscription group API ID"
  },
  "timestamp" : "(required, long) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Armazenamento em nuvem %}
```json
// users.messages.whatsapp.Abort

{
  "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
  "abort_type" : "(optional, string) Type of abort",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "time" : "(required, long) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Eventos de clique em links rastreados pelo WhatsApp

{% apitags %}
WhatsApp, clique
{% endapitags %}

Esse evento ocorre quando um usuário clica em um link ou botão em uma mensagem do WhatsApp em que o domínio do link corresponde ao domínio de rastreamento de cliques.

{% tabs %}
{% tab Amplitude %}
```json
// WhatsApp Tracked Link Click (users.messages.whatsapp.Click)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "short_url" : "(required, string) Shortened url that was clicked",
    "timezone" : "(optional, string) Time zone of the user",
    "url" : "(optional, string) URL that the user clicked on",
    "user_agent" : "(optional, string) User agent on which the spam report occurred",
    "user_phone_number" : "(optional, string) [PII] The user's phone number from which the message was received"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// WhatsApp Tracked Link Click (users.messages.whatsapp.Click)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "short_url" : "(required, string) Shortened url that was clicked",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token",
    "url" : "(optional, string) URL that the user clicked on",
    "user_agent" : "(optional, string) User agent on which the spam report occurred",
    "user_phone_number" : "(optional, string) [PII] The user's phone number from which the message was received"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// WhatsApp Tracked Link Clicks (users.messages.whatsapp.Click)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "short_url" : "(required, string) Shortened url that was clicked",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "url" : "(optional, string) URL that the user clicked on",
          "user_agent" : "(optional, string) User agent on which the spam report occurred"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) [PII] The user's phone number from which the message was received"
  },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segmento %}
```json
// WhatsApp Tracked Link Clicked (users.messages.whatsapp.Click)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : {
      "phone" : "(optional, string) [PII] The user's phone number from which the message was received"
    },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "short_url" : "(required, string) Shortened url that was clicked",
    "user_agent" : "(optional, string) User agent on which the spam report occurred"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Armazenamento em nuvem %}
```json
// users.messages.whatsapp.Click

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "short_url" : "(required, string) Shortened url that was clicked",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "url" : "(required, string) URL that the user clicked on",
  "user_agent" : "(optional, string) User agent on which the spam report occurred",
  "user_id" : "(required, string) Braze user ID of the user who performed this event",
  "user_phone_number" : "(optional, string) [PII] The user's phone number from which the message was received"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Eventos do WhatsApp Delivery

{% apitags %}
WhatsApp, Entrega
{% endapitags %}

Esse evento ocorre quando uma mensagem do WhatsApp enviada chega com êxito ao dispositivo do usuário final.

{% tabs %}
{% tab Amplitude %}
```json
// WhatsApp Delivery (users.messages.whatsapp.Delivery)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, long) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// WhatsApp Delivery (users.messages.whatsapp.Delivery)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "time" : "(required, long) UNIX timestamp at which the event happened",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// WhatsApp Deliveries (users.messages.whatsapp.Delivery)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "subscription_group_id" : "(optional, string) Subscription group API ID"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, long) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segmento %}
```json
// WhatsApp Delivered (users.messages.whatsapp.Delivery)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : {
      "phone" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
    },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID"
  },
  "timestamp" : "(required, long) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Armazenamento em nuvem %}
```json
// users.messages.whatsapp.Delivery

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "time" : "(required, long) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Eventos de falha do WhatsApp

{% apitags %}
WhatsApp, Falha
{% endapitags %}

Esse evento ocorre quando o WhatsApp não consegue entregar a mensagem ao usuário. Um hard bounce significa uma falha permanente de entregabilidade.

{% tabs %}
{% tab Amplitude %}
```json
// WhatsApp Failure (users.messages.whatsapp.Failure)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "provider_error_code" : "(required, string) Error code from WhatsApp",
    "provider_error_title" : "(required, string) Description of error from WhatsApp",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, long) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// WhatsApp Failure (users.messages.whatsapp.Failure)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "provider_error_code" : "(required, string) Error code from WhatsApp",
    "provider_error_title" : "(required, string) Description of error from WhatsApp",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "time" : "(required, long) UNIX timestamp at which the event happened",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// WhatsApp Failures (users.messages.whatsapp.Failure)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "provider_error_code" : "(required, string) Error code from WhatsApp",
          "provider_error_title" : "(required, string) Description of error from WhatsApp",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "subscription_group_id" : "(optional, string) Subscription group API ID"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, long) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segmento %}
```json
// WhatsApp Failed (users.messages.whatsapp.Failure)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : {
      "phone" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
    },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "provider_error_code" : "(required, string) Error code from WhatsApp",
    "provider_error_title" : "(required, string) Description of error from WhatsApp",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID"
  },
  "timestamp" : "(required, long) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Armazenamento em nuvem %}
```json
// users.messages.whatsapp.Failure

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "provider_error_code" : "(required, string) Error code from WhatsApp",
  "provider_error_title" : "(required, string) Description of error from WhatsApp",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "time" : "(required, long) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Eventos recebidos de entrada do WhatsApp

{% apitags %}
WhatsApp, InboundReceived
{% endapitags %}

Esse evento ocorre quando um dos seus usuários envia uma mensagem do WhatsApp para um número de telefone em um dos seus grupos de inscrições do Braze WhatsApp.

{% tabs %}
{% tab Amplitude %}
```json
// WhatsApp Inbound Received (users.messages.whatsapp.InboundReceive)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "action" : "(required, string) Action taken in response to this message. (for example Subscribed, Unsubscribed or None).",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "inbound_phone_number" : "(required, string) The inbound number that the message was sent to",
    "media_urls" : "(optional, array of string) Media URLs from the user",
    "message_body" : "(optional, string) Typed response from the user",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "quick_reply_text" : "(optional, string) Text of button pressed by the user",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "user_phone_number" : "(required, string) [PII] The user's phone number from which the message was received"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, long) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// WhatsApp Inbound Received (users.messages.whatsapp.InboundReceive)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "action" : "(required, string) Action taken in response to this message. (for example Subscribed, Unsubscribed or None).",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "inbound_phone_number" : "(required, string) The inbound number that the message was sent to",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "media_urls" : "(optional, array of string) Media URLs from the user",
    "message_body" : "(optional, string) Typed response from the user",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "quick_reply_text" : "(optional, string) Text of button pressed by the user",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "time" : "(required, long) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token",
    "user_phone_number" : "(required, string) [PII] The user's phone number from which the message was received"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// WhatsApp Inbound Received (users.messages.whatsapp.InboundReceive)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "action" : "(required, string) Action taken in response to this message. (for example Subscribed, Unsubscribed or None).",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "inbound_phone_number" : "(required, string) The inbound number that the message was sent to",
          "message_body" : "(optional, string) Typed response from the user",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "quick_reply_text" : "(optional, string) Text of button pressed by the user",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "subscription_group_id" : "(optional, string) Subscription group API ID"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, long) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) [PII] The user's phone number from which the message was received"
  },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segmento %}
```json
// WhatsApp Inbound Received (users.messages.whatsapp.InboundReceive)

{
  "anonymousId" : "(optional, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : {
      "phone" : "(required, string) [PII] The user's phone number from which the message was received"
    },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "action" : "(required, string) Action taken in response to this message. (for example Subscribed, Unsubscribed or None).",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "inbound_phone_number" : "(required, string) The inbound number that the message was sent to",
    "media_urls" : "(optional, array of string) Media URLs from the user",
    "message_body" : "(optional, string) Typed response from the user",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "quick_reply_text" : "(optional, string) Text of button pressed by the user",
    "subscription_group_id" : "(optional, string) Subscription group API ID"
  },
  "timestamp" : "(required, long) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Armazenamento em nuvem %}
```json
// users.messages.whatsapp.InboundReceive

{
  "action" : "(required, string) Action taken in response to this message. (for example Subscribed, Unsubscribed or None).",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "inbound_phone_number" : "(required, string) The inbound number that the message was sent to",
  "media_urls" : "(optional, array of string) Media URLs from the user",
  "message_body" : "(optional, string) Typed response from the user",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "quick_reply_text" : "(optional, string) Text of button pressed by the user",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "time" : "(required, long) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(optional, string) Braze user ID of the user who performed this event",
  "user_phone_number" : "(required, string) [PII] The user's phone number from which the message was received"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## WhatsApp Ler eventos

{% apitags %}
WhatsApp, Ler
{% endapitags %}

Esse evento ocorre quando uma mensagem do WhatsApp é lida pelo usuário final.

{% tabs %}
{% tab Amplitude %}
```json
// WhatsApp Read (users.messages.whatsapp.Read)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, long) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// WhatsApp Read (users.messages.whatsapp.Read)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "time" : "(required, long) UNIX timestamp at which the event happened",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// WhatsApp Reads (users.messages.whatsapp.Read)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "subscription_group_id" : "(optional, string) Subscription group API ID"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, long) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segmento %}
```json
// WhatsApp Read (users.messages.whatsapp.Read)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : {
      "phone" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
    },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID"
  },
  "timestamp" : "(required, long) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Armazenamento em nuvem %}
```json
// users.messages.whatsapp.Read

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "time" : "(required, long) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Eventos de envio do WhatsApp

{% apitags %}
WhatsApp, Envios
{% endapitags %}

Esse evento ocorre quando uma solicitação de envio foi comunicada com êxito entre o Braze e o WhatsApp. No entanto, isso não significa que a mensagem foi recebida pelo usuário final.

{% tabs %}
{% tab Amplitude %}
```json
// WhatsApp Send (users.messages.whatsapp.Send)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, long) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// WhatsApp Send (users.messages.whatsapp.Send)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "time" : "(required, long) UNIX timestamp at which the event happened",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// WhatsApp Sends (users.messages.whatsapp.Send)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
          "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "subscription_group_id" : "(optional, string) Subscription group API ID"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, long) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segmento %}
```json
// WhatsApp Sent (users.messages.whatsapp.Send)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : {
      "phone" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
    },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID"
  },
  "timestamp" : "(required, long) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Armazenamento em nuvem %}
```json
// users.messages.whatsapp.Send

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
  "id" : "(required, string) Globally unique ID for this event",
  "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "time" : "(required, long) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}
