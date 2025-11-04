---
nav_title: "Habilitação de push e assinatura"
article_title: Habilitação de Push e Assinatura
page_order: 3
page_type: reference
description: "Este artigo de referência cobre os conceitos de habilitação de push e estados de assinatura de push no Braze, incluindo as diferenças fundamentais de comportamento entre iOS, Android e web."
channel:
  - push

---

# Habilitação de push e assinatura de push

> Este artigo de referência cobre os conceitos de habilitação de push e estados de assinatura de push no Braze, incluindo as diferenças fundamentais de comportamento entre iOS, Android e Web.

## Estados de assinatura de push {#push-sub-states}

Um "Estado de Assinatura de Push" no Braze identifica a **preferência** global do usuário para receber notificações push. Como o estado de assinatura é baseado no usuário, não é específico para nenhum aplicativo individual. Os estados de assinatura se tornam bandeiras úteis ao decidir quais usuários direcionar para notificações push.

{% alert note %}
O estado de assinatura de push de um usuário se aplica a todo o seu perfil de usuário, que inclui todos os dispositivos do usuário.
{% endalert %}

Existem três opções de estado de assinatura de push: `Subscribed`, `Opted-In` e `Unsubscribed`.

Por padrão, para que seu usuário receba suas mensagens por meio de push, o estado de assinatura de push deve ser `Subscribed` ou `Opted-In`, e eles devem estar [habilitados para push](#foreground-push-enabled). Você pode substituir essa configuração, se necessário, ao compor uma mensagem.

|Estado de Opt-in|Descrição|
|---|---|
|`Subscribed`| Estado de assinatura de push padrão quando um perfil de usuário é criado no Braze. |
|`Opted-In`| Um usuário expressou explicitamente uma preferência para receber notificações push. O Braze moverá automaticamente o estado de opt-in de um usuário para `Opted-In` se um usuário aceitar um prompt de push em nível de SO.<br><br>Isso não se aplica a usuários do Android 12 ou anteriores.|
|`Unsubscribed`| Um usuário se desinscreveu explicitamente das notificações push através do seu aplicativo ou outros métodos que sua marca fornece. Por padrão, as campanhas de push do Braze apenas visam usuários que estão `Subscribed` ou `Opted-in` para push.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
O Braze não altera automaticamente o estado de assinatura de push de um usuário para `Unsubscribed`. Lembre-se de que se o estado de assinatura de push de um usuário for `Unsubscribed`, então o filtro `Foreground Push Enabled` do usuário na segmentação será `false`.
{% endalert %}

### Atualizando estados de assinatura de push {#update-push-subscription-state}

Existem três maneiras de você atualizar o estado de assinatura de push de um usuário:

#### Opt-in automático (padrão)

Por padrão, o Braze define o estado de assinatura de push de um usuário para `Opted-In` quando eles autorizam pela primeira vez as notificações push para seu aplicativo. O Braze também faz isso quando um usuário reativa as permissões de push nas configurações do sistema após desativá-las anteriormente.

{% tabs local %}
{% tab android %}
Para desativar esse comportamento padrão, adicione a seguinte propriedade ao arquivo `braze.xml` do seu projeto no Android Studio:

```xml
<bool name="com_braze_optin_when_push_authorized">false</bool>
```
{% endtab %}

{% tab swift %}
Começando com [Braze Swift SDK versão 7.5.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/7.5.0), você pode desativar ou personalizar ainda mais esse comportamento adicionando a configuração `optInWhenPushAuthorized` ao arquivo `AppDelegate.swift` do seu projeto no Xcode:

```swift
configuration.optInWhenPushAuthorized = false // disables the default behavior

let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```
{% endtab %}
{% endtabs %}

#### Integração do SDK

Você pode atualizar o estado de assinatura de um usuário com o SDK do Braze usando o método `setPushNotificationSubscriptionType` em [Web](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setpushnotificationsubscriptiontype), [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/set-push-notification-subscription-type.html) ou [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/set(pushnotificationsubscriptionstate:)). Por exemplo, você pode usar esse método para criar uma página de configurações em seu aplicativo onde os usuários podem habilitar ou desabilitar manualmente as notificações push.

#### API REST

Você pode atualizar o estado de assinatura de um usuário com a API REST do Braze usando o endpoint [`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) para atualizar seu atributo [`push_subscribe`]({{site.baseurl}}/api/objects_filters/user_attributes_object).

### Verificando o estado de assinatura de push

\![Perfil do usuário para John Doe com seu estado de assinatura de push definido como Inscrito.]({% image_buster /assets/img/push_example.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Existem duas maneiras de verificar o estado da assinatura de push de um usuário com o Braze:

1. **Perfil do Usuário** Você pode acessar perfis de usuários individuais através do painel do Braze na página **[Pesquisa de Usuários]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/)**. Após encontrar o perfil de um usuário (via endereço de e-mail, número de telefone ou ID de usuário externo), você pode selecionar a aba **Engajamento** para visualizar e ajustar manualmente o estado da assinatura de um usuário.
2. **Exportação da API REST:** Você pode exportar perfis de usuários individuais em formato JSON usando os endpoints de exportação [Usuários por segmento]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/) ou [Usuários por identificador]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/). O Braze retornará um objeto de tokens de push que contém informações de habilitação de push por dispositivo.

## Permissão de push

Todas as plataformas habilitadas para push - iOS, Web e Android - exigem opt-in explícito através de um prompt de sistema em nível de SO, com algumas pequenas diferenças descritas abaixo.

Como a decisão de um usuário é final e você não pode perguntar novamente após a recusa, usar mensagens in-app de [introdução ao push]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/) é uma estratégia importante para aumentar suas taxas de opt-in.

**Prompts nativos de permissão de push do SO**

|Plataforma|Captura de tela|Descrição|
|--|--|--|
|iOS| \![Um prompt nativo de push do iOS perguntando "Meu App gostaria de enviar notificações para você" com dois botões, "Não Permitir" e "Permitir" na parte inferior da mensagem.]({% image_buster /assets/img/push_implementation_guide/ios-push-prompt.png %}){: style="max-width:410px;"} | Isso não se aplica ao solicitar permissão de [push provisório](#provisional-push).|
|Android| \![Uma mensagem de push do Android perguntando "Permitir que Kitchenerie envie notificações para você?" com dois botões, "Permitir" e "Não permitir" na parte inferior da mensagem.]({% image_buster /assets/img/push_implementation_guide/android-push-prompt.png %}){: style="max-width:410px;"} | Essa permissão de push foi introduzida no Android 13. Antes do Android 13, a permissão não era necessária para enviar push.|
|Web| \![Um prompt nativo de push do navegador da web perguntando "Braze.com quer mostrar notificação" com dois botões, "Bloquear" e "Permitir" na parte inferior da mensagem.]({% image_buster /assets/img/push_implementation_guide/web-push-prompt.png %}){: style="max-width:410px;"} | |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Android

Antes do Android 13, não era necessário permissão para enviar notificações push. No Android 12 e abaixo, todos os usuários são considerados `Subscribed` na primeira sessão quando o Braze solicita automaticamente um token de push. Neste ponto, o usuário está **push habilitado** com um token de push válido para aquele dispositivo e um estado de assinatura padrão de `Subscribed`.

A partir de [Android 13]({{site.baseurl}}/developer_guide/platforms/android/android_13/), a permissão de push deve ser solicitada e concedida pelo usuário. Seu aplicativo pode solicitar manualmente permissão do usuário em momentos oportunos, mas se não o fizer, os usuários serão solicitados automaticamente quando seu aplicativo criar um [canal de notificação](https://developer.android.com/reference/android/app/NotificationChannel).

### iOS

\![Uma notificação no Centro de Notificações do sistema com uma mensagem na parte inferior perguntando: "Continuar recebendo notificações do aplicativo Yachtr?" com dois botões abaixo para "Manter" ou "Desligar"]({% image_buster /assets/img/push_implementation_guide/ios-provisional-push.png %}){: style="float:right;max-width:430px;width:40%;margin-left:15px;border:0"}

Seu aplicativo pode solicitar push provisório ou push autorizado. 

Push autorizado requer permissão explícita de um usuário antes de enviar qualquer notificação, enquanto [push provisório](https://www.braze.com/resources/articles/mastering-provisional-push) permite que você envie notificações __silenciosamente__, diretamente para o centro de notificações sem som ou alerta.

#### Autorização provisória e push silencioso {#provisional-push}

Antes do iOS 12 (lançado em 2018), todos os usuários devem optar explicitamente por receber notificações push.

No iOS 12, a Apple introduziu [autorização provisória](https://www.braze.com/resources/articles/mastering-provisional-push), permitindo que marcas enviem notificações push silenciosas para o centro de notificações de seus usuários antes que eles optem explicitamente, dando a você a chance de demonstrar o valor de suas mensagens cedo. Consulte [autorização provisória]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/#provisional-push-authentication--quiet-notifications) para saber mais.

### Web

Para a Web, você deve solicitar a opção explícita do usuário através do diálogo de permissão nativo do navegador.

Ao contrário do iOS e Android, que permitem que seu aplicativo mostre o prompt de permissão a qualquer momento, alguns navegadores modernos só mostrarão o prompt se acionado por um "gesto do usuário" (clique do mouse ou pressionamento de tecla). Se seu site tentar solicitar permissão para notificações push ao carregar a página, provavelmente será ignorado ou silenciado pelo navegador.

Como resultado, você deve pedir permissão apenas quando um usuário clicar em algum lugar em seu site e não aleatoriamente quando uma página carregar.

## Tokens de push

[Tokens de push]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/) são um identificador anônimo único gerado pelo dispositivo de um usuário e enviado ao Braze para identificar onde enviar a notificação de cada destinatário.

Existem duas maneiras de um [token de push]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/) ser classificado que são essenciais para entender como uma notificação push pode ser enviada aos seus usuários.

1. **Notificação em primeiro plano** fornece a capacidade de enviar notificações push visíveis regulares para o primeiro plano do dispositivo de um usuário.
2. **Notificação em segundo plano** está disponível independentemente de um dispositivo específico ter optado por receber notificações push daquela marca. A notificação em segundo plano permite que as marcas enviem notificações push silenciosas - notificações que intencionalmente não são exibidas - para dispositivos para suportar funcionalidades chave como [rastreamento de desinstalação]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking/).

Quando um perfil de usuário tem um token de notificação em primeiro plano válido associado a um aplicativo, a Braze considera o usuário "registrado para push" para o aplicativo dado. A Braze, então, fornece um filtro de segmentação específico, `Foreground Push Enabled for App,` para ajudar a identificar esses usuários.

{% alert note %}
O filtro `Foreground Push Enabled for App` considera apenas a presença de um token de notificação em primeiro plano e em segundo plano válido para o aplicativo dado. No entanto, o filtro mais genérico [`Foreground Push Enabled`](#foreground-push-enabled) segmenta usuários que ativaram explicitamente notificações push para qualquer aplicativo em seu espaço de trabalho. Essa contagem inclui apenas notificações em primeiro plano e não inclui usuários que se desinscreveram. Você pode saber mais sobre esses e outros filtros em [Filtros de Segmentação]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters).
{% endalert %}

### Múltiplos usuários em um dispositivo

Os tokens de push são específicos tanto para um dispositivo quanto para um aplicativo, portanto, não é possível usar tokens de push para distinguir entre múltiplos usuários que estão usando o mesmo dispositivo.

Por exemplo, digamos que você tenha dois usuários: Charlie e Kim. Se Charlie ativou notificações push para seu aplicativo em seu telefone e Kim usa o telefone de Charlie para sair do perfil de Charlie e entrar no dela, o token de push será reatribuído ao perfil de Kim. O token de push permanecerá atribuído ao perfil de Kim naquele dispositivo até que ela saia e Charlie entre novamente.

Um aplicativo ou site pode ter apenas uma assinatura de push por dispositivo. Portanto, quando um usuário sai de um dispositivo ou site, e um novo usuário faz login, o token de push é reatribuído ao novo usuário. Isso é refletido no perfil do usuário, na seção **Configurações de Contato** da aba **Engajamento**:

\![Registro de alterações do token de push na aba \*\*Engajamento** do perfil de um usuário, que lista quando o token de push foi movido para outro usuário e qual era o token.]({% image_buster /assets/img/push_token_changelog.png %})

Como não há uma maneira para os provedores de push (APNs/FCM) distinguirem entre múltiplos usuários em um dispositivo, passamos o token de push para o último usuário que estava logado para determinar qual usuário direcionar no dispositivo para push.

### Vários dispositivos e um usuário

O estado da assinatura de push é baseado no usuário e não é específico para nenhum aplicativo individual. O estado da assinatura de push é o valor que foi definido por último. Portanto, se um usuário optou por receber notificações push, o estado da assinatura de push é `Opted-in` em todos os dispositivos elegíveis. Se um usuário posteriormente cancelar explicitamente a assinatura de notificações push através do seu aplicativo ou outros métodos que sua marca fornece, o estado da assinatura de push é atualizado para `Unsubscribed` e nenhum dispositivo registrado para push pode receber notificações push.

## Filtro de Push em Primeiro Plano Habilitado {#foreground-push-enabled}

`Foreground Push Enabled` é um filtro de segmentação no Braze que permite que os profissionais de marketing identifiquem facilmente os usuários que permitem que o Braze envie notificações push e os usuários que não expressaram preferências para não receber notificações push. 

O filtro `Foreground Push Enabled` leva em conta o seguinte:
- A capacidade do Braze de enviar uma notificação push (token de push em primeiro plano)
- A preferência geral do usuário para receber push em qualquer um de seus dispositivos (estado da assinatura de push)

\![Uma captura de tela do painel mostrando que um usuário está "Registrado para Push para Marketing (iOS)"]({% image_buster /assets/img/push_enablement.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

Um usuário é considerado "habilitado para push" ou "registrado para push" se tiver um token de push em primeiro plano ativo para um aplicativo dentro do seu espaço de trabalho, o que significa que o status de habilitação para push é específico do aplicativo. 

{% alert note %}
Para informações sobre como verificar o estado de registro de push, visite [status de registro de push]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/#checking-push-registration-status)
{% endalert %}

## Outros cenários específicos da plataforma

{% tabs %}
{% tab Android %}

Se um usuário habilitado para push em primeiro plano desativar o push nas configurações do seu sistema operacional, então, no início da próxima sessão:
- O Braze os marca como desabilitados para push em primeiro plano e não tenta mais enviar mensagens push para eles.
- O filtro `Foreground Push Enabled for App (Android)` e o filtro de segmentação `Foreground Push Enabled` (assumindo que nenhum outro aplicativo no perfil do usuário tenha um token de push em primeiro plano válido) retornarão `false`.

Neste cenário, uma vez que um token de push em segundo plano ainda existirá, você pode continuar a enviar notificações push em segundo plano (silenciosas) com o filtro de segmentação `Background or Foreground Push Enabled = true`.

Para Android, o Braze considerará um usuário desabilitado para push se:

- Um usuário desinstala o aplicativo de seu dispositivo.
- Uma mensagem push falha ao ser entregue devido a um retorno. Isso geralmente é causado por uma desinstalação, mas também pode ser devido a atualizações de aplicativo, nova versão do token push ou formato. 
- O registro push falha no Firebase Cloud Messaging (às vezes causado por conexões de rede ruins ou uma falha na conexão com o FCM para retornar um token válido).
- O usuário bloqueia notificações push para o aplicativo nas configurações de seu dispositivo e, em seguida, registra uma sessão.

{% alert note %}
Você só pode interceptar uma notificação push do Android quando o aplicativo está em primeiro plano ou em segundo plano (mas ainda em execução). Você não pode interceptar notificações quando o aplicativo está encerrado ou completamente fechado.
{% endalert %}

{% endtab %}
{% tab iOS %}

Independentemente de um usuário aceitar o prompt de opt-in para push em primeiro plano, você ainda poderá enviar um push em segundo plano se tiver notificações remotas habilitadas no Xcode e seu aplicativo chamar [`registerForRemoteNotifications()`](https://developer.apple.com/documentation/uikit/uiapplication/1623078-registerforremotenotifications).

Se seu aplicativo estiver provisoriamente autorizado ou o usuário optou por push, ele receberá um token de push em primeiro plano, permitindo que você envie todos os tipos de push. Dentro do Braze, consideramos um usuário no iOS que está habilitado para push em primeiro plano como habilitado para push, seja explicitamente (nível de aplicativo) ou provisoriamente (nível de dispositivo).

Se um usuário recusar receber notificações push em nível de SO, seu estado de assinatura push será `Subscribed`, e seu perfil não mostrará que um token de push em primeiro plano foi registrado. 

No cenário em que um usuário, que inicialmente optou por receber em nível de SO, desativa as notificações push em suas configurações de SO, na próxima inicialização da sessão, o seguinte ocorrerá:
- O Braze os marca como desabilitados para push em primeiro plano e não tenta mais enviar mensagens push.
- O filtro `Foreground Push Enabled for App (iOS)` e o filtro de segmentação `Foreground Push Enabled` (assumindo que nenhum outro aplicativo no perfil do usuário tenha um token de push em primeiro plano válido) retornarão `false`.

Neste cenário, uma vez que um token de push em segundo plano ainda existirá, você pode continuar a enviar notificações push em segundo plano (silenciosas) com o filtro de segmentação `Background or Foreground Push Enabled = true`.

{% alert note %}
O iOS não permite que aplicativos interceptem uma notificação push antes da exibição da notificação push. Isso significa que aplicativos (e Braze) não têm controle sobre se você pode exibir ou ocultar a notificação. Um usuário pode optar por não receber notificações push para um aplicativo nas configurações do dispositivo, mas isso é controlado pelo sistema operacional.
{% endalert %}

{% endtab %}
{% tab Web %}

Quando um usuário aceita o prompt de permissão nativa para push, seu status de assinatura será alterado para `opted in`.

Para gerenciar assinaturas, você pode usar o método do usuário [`setPushNotificationSubscriptionType`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setpushnotificationsubscriptiontype) para criar uma página de configurações de preferências em seu site, após o que você pode filtrar usuários por status de opt-out no painel.

Se um usuário desativar notificações em seu navegador, a próxima notificação push enviada para esse usuário será devolvida, e o Braze atualizará o token de push do usuário de acordo. Isso é usado para gerenciar a elegibilidade para os filtros habilitados para push (`Background or Foreground Push Enabled`, `Foreground Push Enabled` e `Foreground Push Enabled for App`). O status de assinatura definido no perfil do usuário é uma configuração de nível de usuário e não muda quando uma notificação push falha.

{% alert note %}
Plataformas web não permitem notificações push em segundo plano ou silenciosas.
{% endalert %}
{% endtab %}
{% endtabs %}

## Melhores práticas

Consulte nosso artigo dedicado sobre [Melhores práticas de push]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices) para orientações detalhadas sobre como otimizar o uso de push no Braze.

