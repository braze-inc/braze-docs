---
nav_title: "Objeto de evento"
article_title: Objeto de evento da API
page_order: 6
page_type: reference
description: "Este artigo de referência aborda o objeto de evento, o que ele é e como é uma parte crucial das estratégias de campanha baseadas em eventos."

---

# Objeto de evento

> Este artigo explica os diferentes componentes de um objeto de evento, como você pode usar esse objeto e os exemplos a serem usados.

## O que é um objeto de evento?

Um objeto de evento é um objeto que é passado pela API quando ocorre um evento específico. Os objetos de eventos são armazenados em um vetor de eventos. Cada objeto de evento no vetor de eventos representa uma única ocorrência de um evento personalizado por um usuário específico no valor de tempo designado. O objeto de evento tem muitos campos diferentes que permitem a personalização por meio da configuração e do uso das propriedades do evento em mensagens, coleta de dados e personalização.

Para obter etapas sobre como configurar eventos personalizados para uma plataforma específica, consulte o Guia de Integração de Plataformas no [Guia do Desenvolvedor]({{site.baseurl}}/developer_guide/home/). Consulte o artigo relevante de acordo com sua plataforma:

- [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/)
- [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/tracking_custom_events/)
- [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_custom_events/)

### Corpo do objeto

```json
{
  // One of "external_id" or "user_alias" or "braze_id" or "email" or "phone" is required
  "external_id" : (optional, string) External user ID,
  "user_alias" : (optional, User Alias Object) User alias object,
  "braze_id" : (optional, string) Braze user identifier,
  "email": (optional, string) User email address,
  "phone": (optional, string) User phone number,
  "app_id" : (optional, string) see App Identifier,
  "name" : (required, string) the name of the event,
  "time" : (required, datetime as string in ISO 8601 or in `yyyy-MM-dd'T'HH:mm:ss:SSSZ` format),
  "properties" : (optional, Properties Object) properties of the event
  // Setting this flag to true will put the API in "Update Only" mode.
  // When using a "user_alias", "Update Only" mode is always true.
  "_update_existing_only" : (optional, boolean)
  // See following notes regarding anonymous push token imports
}
```

- [ID de usuário externo]({{site.baseurl}}/api/basics/#user-ids)
- [Identificador do app]({{site.baseurl}}/api/identifier_types/)
- [Código de tempo ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)

#### Atualizar apenas os perfis existentes

Para atualizar apenas os perfis de usuário existentes no Braze, passe a chave `_update_existing_only` com um valor de `true` no corpo da solicitação. Se esse valor for omitido, a Braze criará um novo perfil de usuário se o `external_id` ainda não existir.

{% alert note %}
Se você estiver criando um perfil de usuário somente de alias por meio do ponto de extremidade `/users/track`, `_update_existing_only` deverá ser definido como `false`. Se esse valor for omitido, o perfil somente de alias não será criado.
{% endalert %}

## Objeto de propriedades do evento

Os eventos personalizados e as compras podem ter propriedades de evento. Os valores das "propriedades" devem ser um objeto em que as chaves são os nomes das propriedades e os valores são os valores das propriedades. Os nomes de propriedades devem ser strings não vazias com até 255 caracteres, sem cifrões ($) à esquerda.

Os valores de propriedade podem ser qualquer um dos seguintes tipos de dados:

| Tipo de dados | Descrição |
| --- | --- |
| Números | Como [números inteiros](https://en.wikipedia.org/wiki/Integer) ou [flutuantes](https://en.wikipedia.org/wiki/Floating-point_arithmetic) |
| Booleanos | `true` ou `false` |
| Datetimes | Deve ser formatado como strings no formato [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) ou em qualquer um dos seguintes formatos: <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY` <br><br>Não é compatível com matrizes. <br><br>Note que "T" é um designador de tempo, não um espaço reservado, e não deve ser alterado ou removido. <br><br>As atribuições de horário sem um fuso horário terão como padrão a meia-noite UTC (e serão formatadas no dashboard como o equivalente à meia-noite UTC no fuso horário da empresa). <br><br> Os eventos com registros de data e hora no futuro terão como padrão a hora atual.  |
| Strings | 255 caracteres ou menos. |
| Matrizes | As matrizes não podem incluir datas e horários. |
| Objetos | Os objetos serão ingeridos como strings. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Os objetos de propriedade de evento que contêm valores de vetor ou objeto podem ter uma carga útil de propriedade de evento de até 100 KB.

### Persistência de propriedades de eventos

As propriedades de eventos são projetadas para filtragem e personalização de Liquid em mensagens disparadas por seus eventos principais. Por padrão, eles não são mantidos no perfil de usuário da Braze. Para usar valores de propriedades de eventos na segmentação, consulte [eventos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/), que detalha as várias abordagens para armazenar valores de propriedades de eventos a longo prazo.

#### Exemplo de solicitação de evento

```json
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "events" : [
    {
      "external_id" : "user1",
      "app_id" : "your-app-id",
      "name" : "watched_trailer",
      "time" : "2013-07-16T19:20:30+01:00"
    },
    {
      "external_id" : "user1",
      "app_id" : "your-app-id",
      "name" : "rented_movie",
      "time" : "2013-07-16T19:20:45+01:00",
      "properties": {
        "movie": "The Sad Egg",
        "director": "Dan Alexander"
      }
    },
    {
      "user_alias" : { "alias_name" : "device123", "alias_label" : "my_device_identifier"},
      "app_id" : "your-app-id",
      "name" : "watched_trailer",
      "time" : "2013-07-16T19:20:50+01:00"
    }
  ]
}
```
- [ISO 8601 Time Code Wiki](http://en.wikipedia.org/wiki/ISO_8601)

## Objetos de eventos

Usando o exemplo fornecido, podemos ver que alguém assistiu a um trailer recentemente e depois alugou um filme. Embora não possamos entrar em uma campanha e segmentar os usuários com base nessas propriedades, podemos usar essas propriedades estrategicamente, usando-as na forma de um recibo, para enviar uma mensagem personalizada por meio de um canal usando o Liquid. Por exemplo, "Hello **Beth**, Thanks for renting **The Sad Egg** by **Dan Alexander**, here are some recommended movies based on your rental..."


