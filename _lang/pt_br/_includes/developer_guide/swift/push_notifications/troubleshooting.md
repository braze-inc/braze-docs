## Noções básicas sobre o fluxo de trabalho Braze/APNs

O serviço de Notificações por Push da Apple (APNs) é a infraestrutura para o envio de notificações por push para aplicativos executados nas plataformas da Apple. Esta é a estrutura simplificada de como as notificações por push são ativadas para os dispositivos de seus usuários e como o Braze pode enviar notificações por push para eles:

1. Você configura o push certificado e o perfil de provisionamento
2. Os dispositivos se registram no APNs e fornecem à Braze os tokens de push
3. Você lança uma campanha de push da Braze
4. Braze remove tokens inválidos

### Etapa 1: Configuração de certificado de push e perfil de provisionamento

Ao desenvolver seu app, você precisará criar um certificado SSL para ativar notificações por push. Este certificado será incluído no perfil de provisionamento com o qual seu app é construído e também precisará ser enviado para o dashboard do Braze. O certificado permite que a Braze informe ao APNs que estamos autorizados a enviar notificações por push em seu nome.

Há dois tipos de [perfis de provisionamento](https://developer.apple.com/library/content/documentation/IDEs/Conceptual/AppDistributionGuide/MaintainingProfiles/MaintainingProfiles.html) e certificados: desenvolvimento e distribuição. Recomendamos apenas usar perfis de distribuição e certificados para evitar qualquer confusão. Se você optar por usar perfis e certificados diferentes para desenvolvimento e distribuição, certifique-se de que o certificado enviado para o dashboard corresponda ao perfil de provisionamento que você está usando no momento.

{% alert warning %}
Não altere o ambiente do certificado push (desenvolvimento versus produção). Alterar o certificado de push para o ambiente errado pode levar a que os seus usuários tenham o token por push removido acidentalmente, tornando-os inalcançáveis por push.
{% endalert %}

### Etapa 2: Os dispositivos se registram no APNs e fornecem à Braze os tokens de push

Quando os usuários abrirem seu app, eles serão solicitados a aceitar notificações por push. Se aceitarem este prompt, o serviço APNs gerará um token por push para aquele dispositivo específico. O Swift SDK enviará imediatamente e de forma assíncrona o token por push para os apps que usam a [política de descarga automática]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/fine_network_traffic_control/#automatic-request-processing) padrão. Depois que tivermos um token por push associado a um usuário, ele aparecerá como "Push Registrado" no dashboard em seu perfil de usuário na guia **engajamento** e será elegível para receber notificações por push das campanhas da Braze.

{% alert note %}
A partir do macOS 13, em determinados dispositivos, você pode testar as notificações por push em um simulador iOS 16 executado no Xcode 14. Para mais informações, consulte as [Notas de versão do Xcode 14](https://developer.apple.com/documentation/xcode-release-notes/xcode-14-release-notes).
{% endalert %}

#### Considerações sobre a geração de token por push

- Se os usuários instalarem seu app em outro dispositivo, outro token será criado e capturado da mesma forma. 
- Se os usuários reinstalarem seu app, um novo token será gerado e passado para o Braze. No entanto, o token original ainda pode ser registrado como válido pelos APNs e pelo Braze.
- Se os usuários desinstalarem seu app, o Braze não será imediatamente notificado sobre isso e o token ainda aparecerá como válido até que seja retirado pelos APNs. 
- Em algum momento, os APNs retirarão os tokens antigos. O Braze não tem controle nem visibilidade disso. 

### Etapa 3: Lançamento de uma campanha de push da Braze

Quando uma campanha de mensagens push for lançada, a Braze fará solicitações ao APNs para entregar sua mensagem. Especificamente, as solicitações são passadas para APNs para cada token por push válido atualmente, a menos que a opção **Enviar para o dispositivo mais recente de um usuário** seja selecionada. Depois que o Braze receber uma resposta bem-sucedida dos APNs, registraremos uma entrega bem-sucedida no perfil do usuário, embora o usuário possa não ter recebido a mensagem real por motivos que incluem:
- Seu dispositivo está desligado.
- O dispositivo não está conectado à Internet (Wi-Fi ou celular).
- Recentemente, eles desinstalaram o app.

Braze usará o certificado push SSL carregado no dashboard para autenticar e verificar que temos permissão para enviar notificações por push para os tokens push fornecidos. Se um dispositivo estiver online, a notificação deve ser recebida logo após o envio da campanha. Note que a Braze define a [data de expiração](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/sending_notification_requests_to_apns#2947607) padrão do APNs para notificações como 30 dias.

### Etapa 4: Remoção de tokens inválidos

Se os [APNs](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1) nos informarem que qualquer um dos tokens por push para os quais estávamos tentando enviar uma mensagem é inválido, removeremos esses tokens dos perfis de usuário aos quais eles estavam associados.

{% alert note %}
É normal que os APNs retornem inicialmente um status de sucesso mesmo que um token deixe de ser registrado, pois os APNs não relatam imediatamente eventos de invalidação de token. Os APNs intencionalmente postergam o retorno de um status `410` para tokens inválidos em uma programação aleatória, projetada para proteger a privacidade do usuário e evitar o rastreamento de desinstalações de apps. Você pode continuar enviando notificações com segurança para um token não registrado até que o APNs retorne um status `410`.
{% endalert %}

## Usando os registros de erros do push

O [registro de atividade de mensagens]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) oferece a oportunidade de ver todas as mensagens (especialmente mensagens de erro) associadas às suas campanhas e envios, incluindo erros de notificação por push. Esse registro de erros fornece uma variedade de avisos que podem ser muito úteis para identificar por que suas campanhas não estão funcionando como esperado. Ao clicar em uma mensagem de erro, o sistema redirecionará você para a documentação relevante que ajudará a solucionar um incidente específico.

![Registros de erros push exibindo a hora em que o erro ocorreu, o nome do app, o canal, o tipo de erro e a mensagem de erro.]({% image_buster /assets/img_archive/message_activity_log.png %})

Os erros comuns que podem ser vistos aqui incluem notificações específicas do usuário, como ["Received Unregistered Sending to Push Token".](#swift_received-unregistered-sending)

Além disso, a Braze também apresenta um changelog de push no perfil do usuário na guia **Engajamento**. Esse changelog contém insights sobre o comportamento de registro de push, como invalidação de token, erros de registro de push, tokens transferidos para novos usuários, etc.

![]({% image_buster /assets/img_archive/push_changelog.gif %}){: style="max-width:50%;" }

### Erros no registro de atividades de mensagens

#### Recebido envio não registrado para token por push {#received-unregistered-sending}

- Certifique-se de que o token por push enviado para a Braze a partir do método `AppDelegate.braze?.notifications.register(deviceToken:)` seja válido. Consulte o **Registro de atividades de envio de mensagem** para ver o token por push. Deve parecer algo como `6e407a9be8d07f0cdeb9e724733a89445f57a89ec890d63867c482a483506fa6`, uma longa string contendo uma mistura de letras e números. Se seu token por push parecer diferente, verifique seu [código]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-4-register-push-tokens-with-braze) para enviar os tokens por push ao Braze.
- Verifique se o seu perfil de provisionamento push corresponde ao ambiente que está testando. Os certificados universais podem ser configurados no dashboard do Braze para enviar para o ambiente APNs de desenvolvimento ou produção. Usar um certificado de desenvolvimento para um app de produção ou um certificado de produção para um app de desenvolvimento não funcionará.
 - Verifique se o token por push que você enviou para a Braze corresponde ao perfil de provisionamento que você usou para desenvolver o app de onde você enviou o token por push.

#### Token de dispositivo não para tópico

Este erro indica que o certificado de push do seu app e o ID do pacote não correspondem. Verifique se o certificado por push que você enviou para a Braze corresponde ao perfil de provisionamento usado para construir o app do qual o token por push foi enviado.

#### Envio de BadDeviceToken para token por push

O `BadDeviceToken` é um código de erro do APNs e não se origina da Braze. Pode haver várias razões para essa resposta ser retornada, incluindo as seguintes:

- O app recebeu um token por push que era inválido para as credenciais enviadas para o dashboard.
- Push foi desativado para este espaço de trabalho.
- O usuário optou por não receber push.
- O app foi desinstalado.
- A Apple atualizou o token por push, o que invalidou o token antigo.
- O app foi criado para um ambiente de produção, mas as credenciais push feitas upload para o Braze estão definidas para um ambiente de desenvolvimento (ou o contrário).

## Problemas de registro push

### Nenhum prompt de registro push

Se o aplicativo não solicitar que você se registre para notificações por push, provavelmente há um problema com a integração do seu registro de push. Certifique-se de ter seguido nossa [documentação]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) e integrado corretamente nosso registro push. Você também pode definir pontos de interrupção em seu código para garantir que o código de registro de push esteja em execução.

### Nenhum usuário "push registrado" é exibido no dashboard (antes do envio de mensagens)

Certifique-se de que seu app esteja configurado corretamente para permitir notificações por push. Os pontos de falha comuns a serem verificados incluem:

- Verifique se o seu app está solicitando a permissão para notificações por push. Normalmente, este prompt aparecerá na primeira vez que você abrir o app, mas pode ser programado para aparecer em outro momento. Se não aparecer onde deveria, o problema provavelmente está na configuração básica das capacidades de push do seu app.
  - Verifique se as etapas da [integração push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) foram concluídas com êxito.
  - Verifique se o perfil de provisionamento com o qual seu app foi criado inclui permissões para push. Certifique-se de que está baixando todos os perfis de provisionamento disponíveis da sua conta de desenvolvedor Apple. Para confirmar isso, execute as etapas a seguir:
    1. No Xcode, acesse **Preferences > Accounts** (Preferências > Contas) (ou use o atalho de teclado <kbd>Command</kbd>+<kbd>,</kbd>).
    2. Selecione o ID Apple que você usa para sua conta de desenvolvedor e clique em **View Details (Exibir detalhes**).
    3. Na próxima página, clique em **<i class="fas fa-redo-alt"></i> Atualizar** e confirme que você está puxando todos os perfis de provisionamento disponíveis.
- Verifique se você [ativou corretamente a capacitação push]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-2-enable-push-capabilities) em seu app.
- Verifique se o seu perfil de provisionamento push corresponde ao ambiente em que você está testando. Os certificados universais podem ser configurados no dashboard do Braze para enviar para o ambiente APNs de desenvolvimento ou produção. Usar um certificado de desenvolvimento para um app de produção ou um certificado de produção para um app de desenvolvimento não funcionará.
- Verifique se você está chamando nosso método `registerPushToken` com a definição de um ponto de interrupção no código.
- Certifique-se de que esteja testando usando um dispositivo (o push não funcionará em um simulador) e que tenha boa conectividade de rede.

## Notificações por push enviadas, mas não exibidas nos dispositivos dos usuários

### Os usuários "Push registrados" não são mais ativados após o envio de mensagens

Provavelmente indica que o usuário tinha um token por push inválido. Isso pode acontecer por várias razões:

#### A incompatibilidade do certificado do dashboard e do app

Se o certificado de push que você carregou no dashboard não for o mesmo no perfil de provisionamento com o qual seu app foi desenvolvido, o APNs rejeitará o token. Verifique se fez upload do certificado correto e se concluiu outra sessão no app antes de tentar outra notificação de teste.

#### O aplicativo foi desinstalado

Se um usuário tiver desinstalado seu aplicativo, o token por push dele será inválido e removido no próximo envio.

#### Regenerando seu perfil de provisionamento

Como último recurso, começar do zero e criar um perfil de provisionamento totalmente novo pode eliminar erros de configuração decorrentes do trabalho com vários ambientes, perfis e apps ao mesmo tempo. Existem muitos fatores na configuração de notificações por push, então, às vezes, é melhor tentar novamente desde o início. Isso também ajudará a isolar o problema se você precisar continuar com a solução de problemas.

### Envio de mensagens não entregues a usuários "push registrados"

#### O app está em primeiro plano

Nas versões do iOS que não integram push via pelo framework `UserNotifications`, se o app estiver em primeiro plano quando a mensagem push for recebida, ela não será exibida. Você deve colocar o app em segundo plano nos seus dispositivos de teste antes de enviar mensagens de teste.

#### Notificação de teste agendada incorretamente

Verifique a programação que você definiu para sua mensagem de teste. Se estiver definido para fuso local ou [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/), você pode simplesmente não ter recebido a mensagem ainda (ou ter o app em primeiro plano quando foi recebida).

### Usuário não "registrado para push" para o app que está sendo testado

Verifique o perfil do usuário para o qual você está tentando enviar uma mensagem de teste. Na guia **Engajamento**, deve haver uma lista de "apps que podem ser enviados por push". Verifique se o app para o qual você está tentando enviar mensagens de teste está nessa lista. Os usuários aparecerão como "registrados para push" se tiverem um token por push para qualquer app no seu espaço de trabalho, então isso pode ser algo como um falso positivo.

O seguinte indicaria um problema com o registro de push ou que o token do usuário foi retornado ao Braze como inválido pelo APNs após ser pushado:

![Um perfil de usuário exibindo as configurações de contato de um usuário. Em Push, é exibido "No Apps" (Nenhum aplicativo).]({% image_buster /assets/img_archive/registration_problem.png %}){: style="max-width:50%"}

## Cliques de push não registrados {#push-clicks-not-logged}

- Certifique-se de ter seguido as [etapas de integração push]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-5-enable-push-handling).
- A Braze não gerencia notificações por push recebidas silenciosamente em primeiro plano (comportamento padrão de push em primeiro plano antes do framework `UserNotifications`). Isso significa que os links não serão abertos e os cliques no push não serão registrados. Se seu app ainda não estiver integrado com o framework `UserNotifications`, a Braze não gerenciará as notificações por push quando o estado do app for `UIApplicationStateActive`. Certifique-se de que seu app não postergue as chamadas para os [métodos de tratamento de push]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-5-enable-push-handling); caso contrário, o Swift SDK poderá tratar as notificações por push como eventos push silenciosos em primeiro plano e não tratá-las.

## Os deep linkings não estão funcionando

### Os links da Web provenientes de cliques push não abrem

Os links nas notificações por push precisam ser compatíveis com ATS para serem abertos em visualizações na web. Certifique-se de que seus links da web usem HTTPS. Para saber mais, consulte [Conformidade com ATS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/linking/#app-transport-security-ats).

### Links profundos de cliques push não abrem

A maior parte do código que lida com deep links também lida com aberturas de push. Primeiro, confira se as aberturas do push estão sendo registradas. Caso contrário, corrija esse problema (já que a correção geralmente corrige o tratamento de links).

Se as aberturas estiverem sendo registradas, verifique se é um problema com o deep link em geral ou com o manuseio do clique do push de deep linking. Para fazer isso, teste para ver se um deep link de um clique de mensagem no app funciona.

