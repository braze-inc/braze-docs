---
page_order: 1.5
nav_title: Lendo Logs Verbosos
article_title: Lendo logs verbosos
description: "Aprenda a ler e interpretar a saída de logs verbosos do SDK Braze, incluindo entradas-chave para notificações por push, mensagens no app, Cartões de Conteúdo e links profundos."
---

# Lendo logs verbosos

> Esta página explica como interpretar a saída de logs verbosos do SDK Braze. Para cada canal de envio de mensagens, você encontrará as entradas de log-chave a serem observadas, o que elas significam e problemas comuns a serem observados.

Antes de começar, certifique-se de que você [ativou o registro verboso]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging) e sabe como coletar logs na sua plataforma.

## Sessões

As sessões são a base da análise de dados e entrega de mensagens do Braze. Muitos recursos de envio de mensagens—incluindo mensagens no app e Cartões de Conteúdo—dependem de uma sessão válida iniciando antes que possam funcionar. Se as sessões não estiverem registrando corretamente, investigue isso primeiro. Para saber mais sobre como ativar o rastreamento de sessões, veja [Etapa 5: Ativar o rastreamento de sessões do usuário]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android#android_step-5-enable-user-session-tracking).

### Entradas de log-chave

{% tabs %}
{% tab Swift %}

**Início da sessão:**

```
Started user session (id: <SESSION_ID>)
```

**Fim da sessão:**

```
Ended user session (id: <SESSION_ID>, duration: <DURATION>s)
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: sessionEnd(duration: <DURATION>)
```

{% endtab %}
{% tab Android %}

**Início da sessão:**

Procure as seguintes entradas:

```
New session created with ID: <SESSION_ID>
Session start event for new session received
Completed the openSession call
Opened session with activity: <ACTIVITY_NAME>
```

Filtre as solicitações de rede para o seu endpoint Braze configurado (por exemplo, sdk.iad-01.braze.com) para ver o evento de início da sessão (`ss`).

**Fim da sessão:**

```
Closed session with activity: <ACTIVITY_NAME>
Closed session with session ID: <SESSION_ID>
Requesting data flush on internal session close flush timer.
```

{% endtab %}
{% endtabs %}

### O que verificar

- Verifique se um log de início de sessão aparece quando o app é iniciado.
- Se você não ver um início de sessão, verifique se o SDK está devidamente inicializado e se `openSession` (Android) está sendo chamado.
- No Android, confirme se uma solicitação de rede está sendo feita para o endpoint Braze. Se você não vê isso, verifique sua chave de API e a configuração do endpoint.

## Notificações por push

Os registros de notificação por push ajudam a verificar se os tokens dos dispositivos estão registrados, se as notificações são entregues e se os eventos de clique são rastreados.

### Registro de token

Quando uma sessão começa, o SDK registra o token por push do dispositivo com a Braze.

{% tabs %}
{% tab Swift %}

```
Updated push notification authorization:
- authorization: authorized

Received remote notifications device token: <PUSH_TOKEN>
```

Filtre as solicitações para o seu endpoint Braze configurado (por exemplo, sdk.iad-01.braze.com) e procure por `push_token` nos atributos do corpo da solicitação:

```
"attributes": [
  {
    "push_token": "<PUSH_TOKEN>",
    "user_id": "<USER_ID>"
  }
]
```

Também confirme que as informações do dispositivo incluem:

```
"device": {
  "ios_push_auth": "authorized",
  "remote_notification_enabled": 1
}
```

{% endtab %}
{% tab Android %}

Procure o registro de registro do FCM:

```
Registering for Firebase Cloud Messaging token using sender id: <SENDER_ID>
```

Verifique o seguinte:

- `com_braze_firebase_cloud_messaging_registration_enabled` é `true`.
- O ID do remetente do FCM corresponde ao seu projeto Firebase.

Um erro comum é `SENDER_ID_MISMATCH`, que significa que o ID do remetente configurado não corresponde ao seu projeto Firebase.

{% endtab %}
{% endtabs %}

### O que verificar

- Se `push_token` estiver faltando no corpo da solicitação, o token não foi capturado. Verifique a configuração do push no seu app.
- Se `ios_push_auth` mostrar `denied` ou `provisional`, o usuário não concedeu permissão total para push.
- No Android, se você ver `SENDER_ID_MISMATCH`, atualize seu ID do remetente FCM para corresponder ao seu projeto Firebase.

### Entrega e clique do push

Quando uma notificação por push é tocada, o SDK registra o processamento e os eventos de clique.

{% tabs %}
{% tab Swift %}

```
Processing push notification:
- date: <TIMESTAMP>
- silent: false
- userInfo: {
  "ab": { ... },
  "ab_uri": "<DEEP_LINK_OR_URL>",
  "aps": {
    "alert": {
      "body": "<MESSAGE_BODY>",
      "title": "<MESSAGE_TITLE>"
    }
  }
}
```

Seguido pelo evento de clique:

```
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: pushClick(campaignId: ...)
```

Se o push contiver um deep link, você também verá:

```
Opening '<URL>':
- channel: notification
- useWebView: false
- isUniversalLink: false
```

{% endtab %}
{% tab Android %}

```
BrazeFirebaseMessagingService: Got Remote Message from FCM
```

Seguido pela carga útil do push e registros de exibição. Para links profundos, procure as entradas Deep Link Delegate ou `UriAction`.

{% endtab %}
{% endtabs %}

### O que verificar

- Verifique se a carga útil do push contém os `title`, `body` esperados e quaisquer links profundos (`ab_uri`).
- Confirme que um evento `pushClick` é registrado após o toque.
- Se o evento de clique estiver ausente, verifique se seu delegado de app ou manipulador de notificações está encaminhando corretamente os eventos de push para o SDK Braze.

## Mensagem no app

Os registros de mensagens no app mostram todo o ciclo de vida: entrega do servidor, acionamento com base em eventos, exibição, registro de impressão e rastreamento de cliques.

### Entrega da mensagem

Quando um usuário inicia uma sessão e é elegível para uma mensagem no app, o SDK recebe a carga útil da mensagem do servidor.

{% tabs %}
{% tab Swift %}

Filtre as respostas do seu endpoint Braze configurado (por exemplo, sdk.iad-01.braze.com) contendo os dados da mensagem no app.

O corpo da resposta contém a carga útil da mensagem, incluindo:

```
"templated_message": {
  "data": {
    "message": "...",
    "type": "HTML",
    "message_close": "SWIPE",
    "trigger_id": "<TRIGGER_ID>"
  },
  "type": "inapp"
}
```

{% endtab %}
{% tab Android %}

Procure o log do evento de gatilho correspondente:

```
Triggering action: <CAMPAIGN_BSON_ID>
```

Isso confirma que a mensagem no app foi correspondida a um evento de gatilho.

{% endtab %}
{% endtabs %}

### Exibição da mensagem e impressão

{% tabs %}
{% tab Swift %}

```
In-app message ready for display:
- triggerId: (campaignId: <CAMPAIGN_ID>, ...)
- extras: { ... }
```

Seguido pelo log de impressão:

```
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: inAppMessageImpression(triggerIds: [...])
```

{% endtab %}
{% tab Android %}

```
handleExistingInAppMessagesInStackWithDelegate:: Displaying in-app message
```

{% endtab %}
{% endtabs %}

### Eventos de clique e botão

Quando um usuário toca em um botão ou fecha a mensagem:

{% tabs %}
{% tab Swift %}

```
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: inAppMessageButtonClick(triggerIds: [...], buttonId: "<BUTTON_ID>")
```

Se não houver mais mensagens acionadas correspondentes, você também verá:

```
No matching trigger for event.
```

Esse é o comportamento esperado quando não há mensagens no app adicionais configuradas para o evento.

{% endtab %}
{% tab Android %}

Filtre as solicitações para seu endpoint Braze configurado (por exemplo, sdk.iad-01.braze.com) e procure eventos com o nome `sbc` (clique no botão) ou `si` (impressão) no corpo da solicitação.

{% endtab %}
{% endtabs %}

### O que verificar

- Se a mensagem no app não for exibida, verifique se o início da sessão foi registrado primeiro.
- Filtre as respostas do seu endpoint Braze configurado para confirmar que a carga útil da mensagem foi entregue.
- Se as impressões não estão sendo registradas, verifique se você não implementou um delegado `inAppMessageDisplay` personalizado que suprime o registro.
- Se "Nenhum gatilho correspondente para o evento" aparecer, isso é normal e indica que nenhuma mensagem adicional no aplicativo está configurada para esse evento.

## Cartões de conteúdo

Os logs do Cartão de Conteúdo ajudam você a verificar se os cartões estão sincronizados com o dispositivo, exibidos para o usuário e que as interações (impressões, cliques, dispensas) estão sendo rastreadas.

### Sincronização do cartão

Os Cartões de Conteúdo são sincronizados no início da sessão e quando uma atualização manual é solicitada. Se nenhuma sessão for registrada, nenhum Cartão de Conteúdo será exibido.

{% tabs %}
{% tab Swift %}

Filtre as respostas do seu endpoint Braze configurado (por exemplo, sdk.iad-01.braze.com) contendo os dados do cartão.

O corpo da resposta contém os dados do cartão, incluindo:

```
"cards": [
  {
    "id": "<CARD_ID>",
    "tt": "<CARD_TITLE>",
    "ds": "<CARD_DESCRIPTION>",
    "tp": "short_news",
    "v": 0,
    "cl": 0,
    "p": 1
  }
]
```

Campos-chave:
- `v` (visualizado): `0` = não visualizado, `1` = visualizado
- `cl` (clicado): `0` = não clicado, `1` = clicado
- `p` (fixado): `0` = não fixado, `1` = fixado
- `tp` (tipo): `short_news`, `captioned_image`, `classic`, etc.

{% endtab %}
{% tab Android %}

```
Requesting content cards sync.
```

Seguido por uma solicitação POST para o seu endpoint Braze configurado (por exemplo, sdk.iad-01.braze.com) contendo informações do usuário e do dispositivo.

{% endtab %}
{% endtabs %}

### Impressões, cliques e dispensas

{% tabs %}
{% tab Swift %}

**Impressão:**

```
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: contentCardImpression(cardIds: [...])
```

**Clique:**

```
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: contentCardClick(cardIds: [...])
```

Se o cartão tiver uma URL, você também verá:

```
Opening '<URL>':
- channel: contentCard
- useWebView: true
```

**Dispensa:**

```
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: contentCardDismissed(cardIds: [...])
```

{% endtab %}
{% tab Android %}

Filtre as solicitações para o seu endpoint Braze configurado (por exemplo, sdk.iad-01.braze.com) e procure nomes de eventos no corpo da solicitação:
- `cci` — impressão do Cartão de Conteúdo
- `ccc` — Clique no cartão de conteúdo
- `ccd` — Cartão de conteúdo dispensado

{% endtab %}
{% endtabs %}

### O que verificar

- **Nenhum cartão exibido**: Verifique se o início da sessão está registrado. Os cartões de conteúdo requerem uma sessão ativa para sincronizar.
- **Cartões ausentes para novos usuários**: Novos usuários em sua primeira sessão podem não ver os cartões de conteúdo até a próxima sessão. Esse é um comportamento esperado.
- **Cartão excede o limite de tamanho**: Cartões de conteúdo acima de 2 KB não são exibidos e a mensagem é abortada.
- **Cartão persiste após parar a campanha**: Verifique se a sincronização foi concluída após a campanha ser parada. Os cartões de conteúdo são removidos do dispositivo após uma sincronização bem-sucedida. Ao parar uma campanha, certifique-se de que a opção de remover cartões ativos dos feeds dos usuários esteja selecionada.

## Deep links

Os registros de deep link aparecem em notificações por push, mensagens no aplicativo e cartões de conteúdo. A estrutura do registro é consistente, independentemente do canal de origem.

{% tabs %}
{% tab Swift %}

Quando o SDK processa um deep link:

```
Opening '<DEEP_LINK_URL>':
- channel: <SOURCE_CHANNEL>
- useWebView: false
- isUniversalLink: false
- extras: { ... }
```

Onde `<SOURCE_CHANNEL>` é um dos: `notification`, `inAppMessage` ou `contentCard`.

{% endtab %}
{% tab Android %}

Para deep links, procure as entradas **Delegado de Deep Link** ou **AçãoUri** no Logcat. Para testar a resolução de deep link de forma independente, execute o seguinte comando:

```bash
adb shell am start -W -a android.intent.action.VIEW -d "<YOUR_DEEP_LINK>" "<YOUR_PACKAGE_NAME>"
```

Isso confirma se o deep link resolve corretamente fora do SDK do Braze.

{% endtab %}
{% endtabs %}

### O que verificar

- Verifique se a URL do deep link corresponde ao que você configurou na campanha.
- Se o deep link funcionar de um canal (por exemplo, push) mas não de outro (por exemplo, Content Cards), verifique se a sua implementação de manuseio de deep link suporta todos os canais.
- No iOS, links universais requerem manuseio adicional. Se os links universais não estiverem funcionando a partir dos canais do Braze, verifique se seu app implementa o protocolo `BrazeDelegate` para manuseio de URL.
- No Android, verifique se o manuseio automático de deep link está desativado se você usar um manipulador personalizado. Caso contrário, o manipulador padrão pode entrar em conflito com sua implementação.

## Identificação do usuário

Quando um usuário é identificado com um `external_id`, o SDK registra um evento de mudança de usuário.

{% tabs %}
{% tab Android %}

```
changeUser called with: <EXTERNAL_ID>
```

Coisas importantes a saber:
- Chame `changeUser` assim que o usuário fizer login—quanto mais cedo, melhor.
- Se um usuário sair, não há como chamar `changeUser` para revertê-lo a um usuário anônimo.
- Se você não quiser usuários anônimos, chame `changeUser` durante o início da sessão ou a inicialização do app.

{% endtab %}
{% tab Swift %}

Filtre por solicitações para seu endpoint Braze configurado (por exemplo, sdk.iad-01.braze.com) e procure por identificação de usuário no corpo da solicitação:

```
"user_id": "<EXTERNAL_ID>"
```

{% endtab %}
{% endtabs %}

## Solicitações de rede

Logs detalhados incluem todos os detalhes da solicitação e resposta HTTP para comunicação do SDK com os servidores do Braze. Esses são úteis para diagnosticar problemas de conectividade.

### Estrutura da solicitação

Filtre por solicitações para seu endpoint Braze configurado (por exemplo, sdk.iad-01.braze.com). A estrutura da solicitação inclui:

{% tabs %}
{% tab Swift %}

```
[http] request POST: <YOUR_BRAZE_ENDPOINT>
- Headers:
  - Content-Type: application/json
  - X-Braze-Api-Key: <REDACTED>
  - X-Braze-Req-Attempt: 1
  - X-Braze-Req-Tokens-Remaining: <COUNT>
- Body: { ... }
```

{% endtab %}
{% tab Android %}

```
Making request(id = <REQUEST_ID>) to <YOUR_BRAZE_ENDPOINT>
```

{% endtab %}
{% endtabs %}

### O que verificar

- **chave de API**: Verifique se `XBraze-ApiKey` corresponde à chave de API do seu espaço de trabalho.
- **Endpoint**: Confirme se a URL da solicitação corresponde ao endpoint de SDK configurado.
- **Tentativas de nova tentativa**: `XBraze-Req-Attempt` maior que 1 indica que o SDK está tentando novamente uma solicitação falhada, o que pode sinalizar problemas de conectividade.
- **Limitação de taxa**: `XBraze-Req-Tokens-Remaining` mostra os tokens de solicitação restantes. Uma contagem baixa pode indicar que o SDK está se aproximando dos limites de taxa.
- **Solicitações ausentes**: No Android, se você não ver uma solicitação para o endpoint do Braze após o início da sessão, verifique sua chave de API e a configuração do endpoint.

## Abreviações comuns de eventos

Em cargas úteis de log detalhadas, o Braze usa nomes de eventos abreviados. Aqui está uma referência:

| Abreviação | Evento |
|---|---|
| `ss` | Início da sessão |
| `se` | Fim da sessão |
| `si` | impressão de mensagem no app |
| `sbc` | clique no botão da mensagem no app |
| `cci` | impressão do cartão de conteúdo |
| `ccc` | clique no cartão de conteúdo |
| `ccd` | cartão de conteúdo descartado |
| `lr` | local registrado |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }