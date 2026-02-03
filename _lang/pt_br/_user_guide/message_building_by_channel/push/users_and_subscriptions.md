---
nav_title: "Capacitação e inscrição por push"
article_title: Capacitação e inscrição push
page_order: 3
page_type: reference
description: "Este artigo de referência aborda os conceitos de estados de capacitação e inscrição de push na Braze, incluindo as diferenças fundamentais de comportamento no iOS, Android e web."
channel:
  - push

---

# Capacitação e inscrição por push

> Este artigo de referência aborda os conceitos de capacitação push e estados de inscrição push na Braze, incluindo as diferenças fundamentais de comportamento entre iOS, Android e Web.

## Estados da inscrição push {#push-sub-states}

Um "estado de inscrição por push" no Braze identifica **a** preferência global **de** um **usuário** quanto ao seu desejo de receber notificações por push. Como o estado da inscrição é baseado no usuário, ele não é específico de nenhum aplicativo individual. Os estados de inscrição tornam-se sinalizadores úteis ao decidir quais usuários devem ser direcionados para notificações por push.

{% alert note %}
O estado da inscrição push de um usuário se aplica a todo o seu perfil de usuário, que inclui todos os dispositivos do usuário.
{% endalert %}

Há três opções de estado da inscrição push: `Subscribed`, `Opted-In`, e `Unsubscribed`.

Por padrão, para que o usuário receba suas mensagens por push, o estado da inscrição no push deve ser `Subscribed` ou `Opted-In`, e ele deve estar [ativado para a capacitação](#foreground-push-enabled). Você pode substituir essa configuração, se necessário, ao criar uma mensagem.

|Estado de aceitação|Descrição|
|---|---|
|`Subscribed`| Estado padrão da inscrição push quando um perfil de usuário é criado no Braze. |
|`Opted-In`| Um usuário expressou explicitamente uma preferência para receber notificações por push. A Braze moverá automaticamente o estado de aceitação de um usuário para `Opted-In` se ele aceitar um pedido de aceitação no nível do sistema operacional.<br><br>Isso não se aplica a usuários do Android 12 ou inferior.|
|`Unsubscribed`| Um usuário cancelou explicitamente a inscrição no push por meio do seu aplicativo ou de outros métodos fornecidos pela sua marca. Por padrão, as campanhas de push da Braze têm como alvo apenas os usuários que são `Subscribed` ou `Opted-in` para push.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
O Braze não altera automaticamente o estado da inscrição push de um usuário para `Unsubscribed`. Lembre-se de que, se o estado da inscrição push de um usuário for `Unsubscribed`, o filtro `Foreground Push Enabled` do usuário na segmentação será `false`.
{% endalert %}

### Atualização dos estados da inscrição push {#update-push-subscription-state}

Há três maneiras de atualizar o estado da inscrição push de um usuário:

#### Aceitação automática (padrão)

Por padrão, o Braze define o estado da inscrição push de um usuário como `Opted-In` quando ele autoriza pela primeira vez as notificações por push para o seu app. A Braze também faz isso quando um usuário reativa as permissões push nas configurações do sistema após tê-las desativado anteriormente.

{% tabs local %}
{% tab android %}
Para desativar esse comportamento padrão, adicione a seguinte propriedade ao arquivo `braze.xml` do seu projeto do Android Studio:

```xml
<bool name="com_braze_optin_when_push_authorized">false</bool>
```
{% endtab %}

{% tab swift %}
A partir da [versão 7.5.0 do Braze Swift SDK](https://github.com/braze-inc/braze-swift-sdk/releases/tag/7.5.0), você pode desativar ou personalizar ainda mais esse comportamento adicionando a configuração `optInWhenPushAuthorized` ao arquivo `AppDelegate.swift` do seu projeto Xcode:

```swift
configuration.optInWhenPushAuthorized = false // disables the default behavior

let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```
{% endtab %}
{% endtabs %}

#### integração de SDK

Você pode atualizar o estado da inscrição de um usuário com o Braze SDK usando o método `setPushNotificationSubscriptionType` na [Web](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setpushnotificationsubscriptiontype), [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/set-push-notification-subscription-type.html) ou [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/set(pushnotificationsubscriptionstate:)). Por exemplo, você pode usar esse método para criar uma página de configurações no seu app em que os usuários possam ativar ou desativar manualmente as notificações por push.

#### API REST

Você pode atualizar o estado de inscrição de um usuário com a API REST do Braze usando o endpoint [`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) para atualizar seu atributo [`push_subscribe`]({{site.baseurl}}/api/objects_filters/user_attributes_object).

### Verificação do estado da inscrição push

![Perfil de usuário para John Doe com seu estado de inscrição push definido como Subscribed (Inscrito).]({% image_buster /assets/img/push_example.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Há duas maneiras de verificar o estado da inscrição push de um usuário na Braze:

1. **Perfil do Usuário** Você pode acessar perfis de usuários individuais através do painel do Braze na página **[Pesquisa de Usuário]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/)**. Depois de encontrar o perfil de um usuário (por meio de endereço de e-mail, número de telefone ou ID de usuário externo), é possível selecionar a guia **Engajamento** para visualizar e ajustar manualmente o estado da inscrição de um usuário.
2. **Exportação da API REST:** Você pode exportar perfis de usuários individuais em formato JSON usando os endpoints de exportação [Usuários por segmento]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/) ou [Usuários por identificador]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/). A Braze retornará um objeto de tokens por push que contém informações de capacitação por push por dispositivo.

## Permissão de push

Todas as plataformas com capacitação push – iOS, Web e Android – exigem aceitação explícita por meio de um pedido de aceitação do sistema em nível de sistema operacional, com algumas pequenas diferenças descritas abaixo.

Como a decisão de um usuário é final e você não pode perguntar novamente após a recusa, usar [mensagens in-app de push primer]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/) é uma estratégia importante para aumentar suas taxas de aceitação.

**Solicitações de permissão push do sistema operacional nativo**

|Plataforma|Captura de tela|Descrição|
|--|--|--|
|iOS| ![Um prompt nativo de push do iOS perguntando "Meu App gostaria de enviar notificações para você" com dois botões, "Não Permitir" e "Permitir" na parte inferior da mensagem.]({% image_buster /assets/img/push_implementation_guide/ios-push-prompt.png %}){: style="max-width:410px;"} | Isso não se aplica ao solicitar permissão provisória de push [](#provisional-push).|
|Android| ![Uma mensagem de push do Android perguntando "Permitir que Kitchenerie envie notificações para você?" com dois botões, "Permitir" e "Não permitir" na parte inferior da mensagem.]({% image_buster /assets/img/push_implementation_guide/android-push-prompt.png %}){: style="max-width:410px;"} | Essa permissão push foi introduzida no Android 13. Antes do Android 13, não era necessária permissão para enviar push.|
|Web| ![Um prompt nativo de push do navegador da web perguntando "Braze.com quer mostrar notificações" com dois botões, "Bloquear" e "Permitir" na parte inferior da mensagem.]({% image_buster /assets/img/push_implementation_guide/web-push-prompt.png %}){: style="max-width:410px;"} | |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Android

Antes do Android 13, não era necessária permissão para enviar notificações por push. No Android 12 e versões anteriores, todos os usuários são considerados `Subscribed` na primeira sessão, quando a Braze solicita automaticamente um token por push. Nesse ponto, o usuário está **ativado por push** com um token por push válido para esse dispositivo e um estado de inscrição padrão de `Subscribed`.

Começando com [Android 13]({{site.baseurl}}/developer_guide/platforms/android/android_13/), a permissão de push deve ser solicitada e concedida pelo usuário. Seu aplicativo pode solicitar manualmente a permissão do usuário em momentos oportunos, mas, caso contrário, os usuários serão solicitados automaticamente quando seu app criar um [canal de notificação](https://developer.android.com/reference/android/app/NotificationChannel).

### iOS

![Uma notificação no Centro de Notificações do sistema com uma mensagem na parte inferior perguntando: "Continuar recebendo notificações do app Yachtr?" com dois botões abaixo para "Manter" ou "Desligar"]({% image_buster /assets/img/push_implementation_guide/ios-provisional-push.png %}){: style="float:right;max-width:430px;width:40%;margin-left:15px;border:0"}

Seu app pode solicitar push provisório ou push autorizado. 

Push autorizado requer permissão explícita de um usuário antes de enviar qualquer notificação, enquanto [push provisório](https://www.braze.com/resources/articles/mastering-provisional-push) permite que você envie notificações __silenciosamente__, diretamente para o centro de notificações sem som ou alerta.

#### Autorização provisória e push silencioso {#provisional-push}

Antes do iOS 12 (lançado em 2018), todos os usuários devem fazer a aceitação explícita para receber notificações por push.

No iOS 12, a Apple introduziu [autorização provisória](https://www.braze.com/resources/articles/mastering-provisional-push), permitindo que marcas enviem notificações push silenciosas para o centro de notificações de seus usuários antes que eles optem explicitamente, dando a você a chance de demonstrar o valor de suas mensagens cedo. Consulte a [autorização provisória]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/#provisional-push-authentication--quiet-notifications) para saber mais.

### Web

Para a Web, é necessário solicitar a aceitação explícita do usuário por meio da caixa de diálogo de permissão do navegador nativo.

Ao contrário do iOS e do Android, que permitem que seu app mostre o prompt de permissão a qualquer momento, alguns navegadores modernos só mostrarão o prompt se forem disparados por um "gesto do usuário" (clique do mouse ou pressionamento de tecla). Se o seu site tentar solicitar permissão para notificações por push no carregamento da página, ele provavelmente será ignorado ou silenciado pelo navegador.

Como resultado, você deve pedir permissão somente quando um usuário clicar em algum lugar do seu site e não aleatoriamente quando uma página for carregada.

## Tokens por push

[Tokens de push]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/) são um identificador anônimo único gerado pelo dispositivo de um usuário e enviado para o Braze para identificar onde enviar a notificação de cada destinatário.

Existem duas maneiras de classificar um [token de push]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/) que são essenciais para entender como uma notificação push pode ser enviada para seus usuários.

1. **O push em primeiro plano** oferece a capacidade de enviar notificações por push visíveis regularmente para o primeiro plano do dispositivo do usuário.
2. **O push em segundo plano** está disponível independentemente do fato de um dispositivo específico ter aceitado receber notificações por push dessa marca. O push em segundo plano permite que as marcas enviem notificações por push silenciosas - notificações que intencionalmente não são exibidas - aos dispositivos para oferecer suporte a funcionalidades importantes, como [rastreamento de desinstalação]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking/).

Quando um perfil de usuário tem um token por push de primeiro plano válido associado a um aplicativo, o Braze considera o usuário "registrado por push" para o aplicativo em questão. OA Braze, então, fornece um filtro de segmentação específico, `Foreground Push Enabled for App,`, para ajudar a identificar esses usuários.

{% alert note %}
O filtro `Foreground Push Enabled for App` considera apenas a presença de um token por push de primeiro e segundo plano válido para o aplicativo em questão. No entanto, o filtro mais genérico [`Foreground Push Enabled`](#foreground-push-enabled) mais genérico, segmenta os usuários que ativaram explicitamente as notificações por push para qualquer app no seu espaço de trabalho. Essa contagem inclui apenas o push em primeiro plano e não inclui os usuários que cancelaram a inscrição. Você pode saber mais sobre esses e outros filtros em [Filtros de segmentação]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters).
{% endalert %}

### Vários usuários em um dispositivo

Os tokens por push são específicos de um dispositivo e de um app, portanto, não é possível usar tokens por push para distinguir entre vários usuários que estão usando o mesmo dispositivo.

Por exemplo, digamos que você tenha dois usuários: Charlie e Kim. Se Charlie tiver ativado as notificações por push para o seu app no telefone dele e Kim usar o telefone de Charlie para sair do perfil de Charlie e registrar o dela, o token por push será reatribuído ao perfil de Kim. O token por push permanecerá atribuído ao perfil de Kim nesse dispositivo até que ela se desconecte e Charlie se conecte novamente.

Um app ou site só pode ter uma inscrição push por dispositivo. Portanto, quando um usuário sai de um dispositivo ou site e um novo usuário faz o registro, o token por push é reatribuído ao novo usuário. Isso é refletido no perfil do usuário, na seção **Configurações de contato** da guia **Engajamento**:

![O changelog do token por push na guia \*\*Engajamento** do perfil de um usuário, que lista quando o token por push foi movido para outro usuário e qual era o token.]({% image_buster /assets/img/push_token_changelog.png %})

Como não há uma maneira de os provedores de push (APNs/FCM) distinguirem entre vários usuários em um dispositivo, passamos o token por push para o último usuário que estava registrado para determinar qual usuário deve ser direcionado no dispositivo para push.

### Vários dispositivos e um usuário

O estado da inscrição push é baseado no usuário e não é específico de nenhum app individual. O estado da inscrição push é o valor que foi definido pela última vez. Portanto, se um usuário tiver aceitado notificações por push, seu estado de inscrição será `Opted-in` em todos os dispositivos elegíveis. Se, posteriormente, um usuário cancelar explicitamente a inscrição nas notificações por push por meio do seu aplicativo ou de outros métodos fornecidos pela sua marca, o estado da inscrição por push dele será atualizado para `Unsubscribed` e nenhum dispositivo registrado poderá receber notificações por push.

## Filtro de Push em Primeiro Plano Habilitado {#foreground-push-enabled}

`Foreground Push Enabled` é um filtro de segmentação no Braze que permite que os profissionais de marketing identifiquem facilmente os usuários que permitem que o Braze envie notificações por push e os usuários que não expressaram preferências para não receber notificações por push. 

O filtro `Foreground Push Enabled` leva em conta o seguinte:
- A capacidade do Braze de enviar uma notificação por push (token por push em primeiro plano)
- A preferência geral do usuário para receber push em qualquer um de seus dispositivos (estado da inscrição push)

![Uma captura de tela do dashboard mostrando que um usuário é "Push Registered for Marketing (iOS)"]({% image_buster /assets/img/push_enablement.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

Um usuário é considerado "ativado por push" ou "registrado por push" se tiver um token por push em primeiro plano ativo para um app no seu espaço de trabalho, o que significa que o status de capacitação por push é específico do app. 

{% alert note %}
Para saber como verificar o estado do registro push, consulte [status do registro push]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/#checking-push-registration-status)
{% endalert %}

## Outros cenários específicos da plataforma

{% tabs %}
{% tab Web %}

Quando um usuário aceitar o prompt de permissão de push nativo, o status da inscrição será alterado para `opted in`.

Para gerenciar inscrições, você pode usar o método de usuário [`setPushNotificationSubscriptionType`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setpushnotificationsubscriptiontype) para criar uma página de configurações de preferências em seu site, após a qual é possível filtrar os usuários por status de aceitação no dashboard.

Se um usuário desativar as notificações em seu navegador, a próxima notificação por push enviada a esse usuário será devolvida e o Braze atualizará o token por push do usuário de acordo. Isso é usado para gerenciar a capacitação para os filtros ativados por push (`Background or Foreground Push Enabled`, `Foreground Push Enabled` e `Foreground Push Enabled for App`). O status da inscrição definido no perfil do usuário é uma configuração no nível do usuário e não muda quando um push é devolvido.

{% alert note %}
As plataformas da Web não permitem push em segundo plano ou silencioso.
{% endalert %}
{% endtab %}
{% tab Android %}

Se um usuário com o push ativado em primeiro plano desativar o push nas configurações do sistema operacional, isso ocorrerá no início da próxima sessão:
- O Braze os marca como desativados por push em primeiro plano e não tenta mais enviar mensagens push a eles.
- O filtro `Foreground Push Enabled for App (Android)` e o filtro de segmentação `Foreground Push Enabled` (supondo que nenhum outro app no perfil do usuário tenha um token por push de primeiro plano válido) retornarão `false`.

Nesse cenário, como ainda existirá um token por push em segundo plano, você poderá continuar a enviar notificações por push em segundo plano (silenciosas) com o filtro de segmentação `Background or Foreground Push Enabled = true`.

Para Android, o Braze considerará um push de usuário desativado se:

- Um usuário desinstala o app de seu dispositivo.
- Uma mensagem push não foi entregue devido a um bounce. Isso geralmente é causado por uma desinstalação, mas também pode ser devido a atualizações do app, nova versão do token por push ou formato. 
- Falha no registro push no envio de mensagens do Firebase Cloud (às vezes causada por conexões de rede ruins ou falha na conexão ou no FCM para retornar um token válido).
- O usuário bloqueia as notificações por push para o app nas configurações do dispositivo e, posteriormente, registra uma sessão.

{% alert note %}
Você só pode interceptar uma notificação push do Android quando o app está em primeiro plano ou em segundo plano (mas ainda em execução). Você não pode interceptar notificações quando o app está encerrado ou completamente fechado.
{% endalert %}

{% endtab %}
{% tab iOS %}

Independentemente de o usuário aceitar o pedido de aceitação do push em primeiro plano, você ainda poderá enviar um push em segundo plano se tiver ativado as notificações remotas no Xcode e seu app chamar [`registerForRemoteNotifications()`](https://developer.apple.com/documentation/uikit/uiapplication/1623078-registerforremotenotifications).

Se o seu app estiver provisoriamente autorizado ou se o usuário tiver aceitado o push, ele receberá um token por push em primeiro plano, o que permitirá enviar todos os tipos de push. No Braze, consideramos que um usuário no iOS que está habilitado para push em primeiro plano está habilitado para push, seja explicitamente (no nível do app) ou provisoriamente (no nível do dispositivo).

Se um usuário se recusar a receber notificações por push no nível do sistema operacional, seu estado de inscrição no push será `Subscribed`, e seu perfil não mostrará que um token por push em primeiro plano foi registrado. 

No cenário em que um usuário, que inicialmente fez a aceitação no nível do sistema operacional, desativa as notificações por push nas configurações do sistema operacional, no próximo início de sessão, ocorrerá o seguinte:
- O Braze os marca como push em primeiro plano desativado e não tenta mais enviar mensagens push.
- O filtro `Foreground Push Enabled for App (iOS)` e o filtro de segmentação `Foreground Push Enabled` (supondo que nenhum outro app no perfil do usuário tenha um token por push de primeiro plano válido) retornarão `false`.

Nesse cenário, como ainda existirá um token por push em segundo plano, você poderá continuar a enviar notificações por push em segundo plano (silenciosas) com o filtro de segmentação `Background or Foreground Push Enabled = true`.

{% alert note %}
O iOS não permite que apps interceptem uma notificação push antes que a notificação push seja exibida. Isso significa que os apps (e o Braze) não têm controle sobre se você pode exibir ou ocultar a notificação. Um usuário pode optar por não receber notificações por push de um app nas configurações do dispositivo, mas isso é controlado pelo sistema operacional.
{% endalert %}

{% endtab %}
{% endtabs %}

## Práticas recomendadas

Consulte nosso artigo dedicado às [práticas recomendadas de push]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices) para obter orientações detalhadas sobre como otimizar o uso do push no Braze.

