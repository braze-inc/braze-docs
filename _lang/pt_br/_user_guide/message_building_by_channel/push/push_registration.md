---
nav_title: "Registro por push"
article_title: Registro por push
page_order: 2
page_type: reference
description: "Este artigo de referência discute o que significa estar registrado para push e como enviamos mensagens push e lidamos com tokens push e registro push no Braze."
channel:
 - push

---

# Registro por push

> Este artigo aborda o processo pelo qual um usuário recebe um token push e como o Braze envia mensagens push para seus usuários.

## Sobre os push tokens {#push-tokens}

Quando um aplicativo solicita permissões push de um dispositivo, o provedor de serviços push do dispositivo gera um token push para esse aplicativo. Cada aplicativo recebe seu próprio token push anônimo e exclusivo, que é a forma de identificar o dispositivo e a instância atual do aplicativo ao enviar uma notificação push.

Lembre-se de que os tokens push não são identificadores estáticos que duram para sempre - eles podem ser atualizados e podem [expirar](#push-token-expire).

{% alert tip %}
Para obter detalhes específicos da plataforma, consulte [Registro de token push](#push-token-registration).
{% endalert %}

### Impulso em primeiro plano versus impulso em segundo plano {#foreground-vs-background}

Os tokens de push são usados para enviar notificações push em primeiro e segundo plano.

| Tipo       | Requer adesão? | Descrição                                                 |
|------------------|------------------|--------------------------------------------------------------------------------------------------------------|
| Impulso de primeiro plano | Sim       | Uma notificação é exibida de forma visível para o usuário enquanto o aplicativo está em primeiro plano.           |
| Impulso de fundo | Não        | Uma notificação é entregue silenciosamente em segundo plano, sem ser exibida. Geralmente usado para funcionalidades como rastreamento de desinstalação. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Quando um usuário optar por receber notificações por push do seu aplicativo, ele será considerado "registrado por push", o que significa que agora pode ser direcionado usando o filtro de segmentação `Foreground Push Enabled for App` no Braze.

{% alert note %}
Isso é diferente do filtro de segmentação `Foreground Push Enabled`, que é usado para identificar usuários que optaram por participar de pelo menos um de seus aplicativos - não de um aplicativo específico. Para obter mais informações, consulte [Filtros de segmentação]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#foreground-push-enabled).
{% endalert %}

### Vários usuários em um dispositivo

Os tokens de push são exclusivos do dispositivo e do aplicativo, o que significa que não podem ser usados para direcionar usuários específicos se vários usuários estiverem usando o mesmo dispositivo.

Por exemplo, digamos que você tenha dois usuários: Charlie e Kim. Se Charlie tiver ativado as notificações push para o seu aplicativo no telefone dele e Kim usar o telefone de Charlie para sair do perfil de Charlie e entrar no dela, o token push será reatribuído ao perfil de Kim. O token de envio permanecerá atribuído ao perfil de Kim nesse dispositivo até que ela faça logout e Charlie faça login novamente.

Um aplicativo ou site só pode ter uma assinatura push por dispositivo. Assim, quando um usuário sai de um dispositivo ou site e um novo usuário faz login, o token push é reatribuído ao novo usuário. Isso é refletido no perfil do usuário na seção **Configurações de contato** da guia **Engajamento**:

Registro de alterações do token de envio na guia \*\*Engagement** do perfil de um usuário, que lista quando o token de envio foi movido para outro usuário e qual era o token.]({% image_buster /assets/img/push_token_changelog.png %})

Como não há uma maneira de os provedores de push (APNs/FCM) distinguirem entre vários usuários em um dispositivo, passamos o token de push para o último usuário que estava conectado para determinar qual usuário deve ser direcionado para o push no dispositivo.

## Registro de token push

Cada plataforma de dispositivo lida com o registro de token push de forma diferente. Consulte o seguinte para obter detalhes específicos da plataforma:

{% tabs local %}
{% tab android %}
Quando o seu aplicativo é instalado, um token push é gerado automaticamente para ele; no entanto, ele só pode ser usado para [notificações push em segundo plano](#foreground-vs-background) até que o usuário opte explicitamente por recebê-las. Além disso, o registro é tratado de forma diferente em diferentes versões do Android:

| Versão       | Detalhes                                                                                                                                                |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Android 13**         | A permissão de envio deve ser solicitada e concedida pelo usuário. Seu aplicativo pode solicitar a permissão manualmente, ou os usuários serão solicitados automaticamente depois que um [canal de notificação](https://developer.android.com/reference/android/app/NotificationChannel) for criado. |
| **Android 12 e versões anteriores** | Todos os usuários são considerados `Subscribed` após a primeira sessão. O Braze solicita automaticamente um token de push nesse momento, tornando o usuário habilitado para push com um token válido e um estado de assinatura padrão de `Subscribed`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% endtab %}

{% tab ios %}
O iOS não gera automaticamente tokens push para um aplicativo quando ele é instalado. Além disso, o registro é tratado de forma diferente em diferentes versões do iOS: 

| Versão                         | Autorização provisória? | Detalhes                                                                                                                                                     |
|------------------------------------|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **iOS 12**      | Sim                         | Quando um usuário opta por receber notificações por push, você recebe uma autorização padrão, o que lhe permite enviar [notificações por push em primeiro plano](#foreground-vs-background). No entanto, você também pode solicitar [uma autorização provisória]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/#provisional-push), que permite enviar [notificações push](#foreground-vs-background) silenciosas [em segundo plano](#foreground-vs-background) diretamente para a central de notificações. |
| **iOS 11 e posterior** | Não                          | Todos os usuários devem optar explicitamente por receber notificações por push. Um token push é gerado somente depois que a permissão é concedida.                                     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
{% endtab %}

{% tab web %}
Você deve solicitar o opt-in explícito dos usuários por meio da caixa de diálogo de permissão do navegador nativo. Receberá um token depois que os usuários optarem por participar. Ao contrário do iOS e do Android, que permitem que seu aplicativo mostre o prompt de permissão a qualquer momento, alguns navegadores modernos só mostrarão o prompt se forem acionados por um "gesto do usuário" (clique do mouse ou pressionamento de tecla). Se o seu site tentar solicitar permissão de notificação por push no carregamento da página, ele provavelmente será ignorado ou silenciado pelo navegador.
{% endtab %}
{% endtabs %}

### Verificação do estado da assinatura push do usuário

\![Perfil de usuário para John Doe com o estado de assinatura de push definido como Subscribed (Inscrito).]({% image_buster /assets/img/push_example.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Há duas maneiras de verificar o estado da assinatura push de um usuário com o Braze:

- **Perfil do usuário**: Você pode acessar perfis de usuários individuais por meio do painel do Braze na página [Pesquisa de usuários]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/). Depois de encontrar o perfil de um usuário (por meio de endereço de e-mail, número de telefone ou ID de usuário externo), você pode selecionar a guia **Engagement (Envolvimento** ) para visualizar e ajustar manualmente o estado da assinatura de um usuário.
- **Exportação de API Rest**: É possível exportar perfis de usuários individuais no formato JSON usando os pontos de extremidade Exportar [usuários por segmento]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/) ou [Usuários por identificador]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/). O Braze retornará um objeto de tokens de push que contém informações de habilitação de push por dispositivo.

### Verificação do status do registro push

Na guia **Envolvimento** do perfil de um usuário, você verá **Push Registered For** seguido do nome de um aplicativo. Se não houver informações sobre o aplicativo para esse dispositivo, você verá dois traços**(--**). Haverá uma entrada para cada dispositivo que pertence ao usuário.

Se o nome do aplicativo da entrada do dispositivo for prefixado por `Foreground:`, o aplicativo estará autorizado a receber notificações push em primeiro plano (visíveis para o usuário) e em segundo plano (não visíveis para o usuário) nesse dispositivo.

Push Changelog com um exemplo de token de envio.]({% image_buster /assets/img/push_changelog.png %}){: style="float:right;max-width:40%;margin-left:15px;margin-top:10px;"}

Por outro lado, se o nome do aplicativo da entrada do dispositivo for prefixado por `Background:`, o aplicativo só está autorizado a receber [push em segundo plano]({{site.baseurl}}/user_guide/message_building_by_channel/push/types/#background-push-notifications) e não pode exibir notificações visíveis ao usuário nesse dispositivo. Isso geralmente indica que o usuário desativou as notificações do aplicativo nesse dispositivo.

Se um token push for movido para um usuário diferente no mesmo dispositivo, o primeiro usuário não será mais registrado por push.

## Gerenciamento de tokens push

Confira no gráfico a seguir as ações que levam a alterações ou remoção de tokens de envio dos perfis de usuário. 

| Ação | Descrição |
| ------ | ----------- |
| `changeUser()` método chamado | O método Braze `changeUser()` alterna o ID do usuário ao qual os SDKs estão atribuindo dados de comportamento do usuário. Esse método geralmente é chamado quando um usuário faz login em um aplicativo. Quando `changeUser()` for chamado com um ID de usuário diferente ou novo em um dispositivo específico, o token push desse dispositivo será movido para o perfil Braze apropriado com o ID de usuário correspondente. |
| Ocorre um erro de envio | Alguns erros comuns de push que levam à remoção do token incluem `MismatchSenderId`, `InvalidRegistration` e outros tipos de push bounces. <br><br>Confira nossa lista completa de [erros]({{site.baseurl}}/help/help_articles/push/push_error_codes/#push-bounced-mismatchsenderid) comuns [de push]({{site.baseurl}}/help/help_articles/push/push_error_codes/#push-bounced-mismatchsenderid). |
| Desinstalação pelo usuário | Quando um usuário desinstala o aplicativo de um dispositivo, o Braze removerá o token push do usuário do perfil. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Como isso se parece em uma escala mais ampla?

Quando um usuário abre um novo aplicativo e concede acesso push a partir de um prompt push, é feita uma chamada do SDK do Braze para os provedores push. Quando essa chamada é feita, o provedor de push executa uma verificação para ver se tudo está configurado corretamente. Em caso afirmativo, um token de envio é passado para seu dispositivo. Quando esse token chega, o SDK o comunica ao Braze. Após o Braze receber o token do provedor de push, atualizamos ou criamos um novo perfil de usuário. Esses usuários agora são considerados registrados.

Se quisermos lançar uma campanha, criamos uma campanha no Braze que gera uma carga de push para enviar ao provedor de push. A partir daí, o provedor entrega a carga útil do push para o dispositivo do usuário e o SDK passa o estado da mensagem para o Braze.

Um fluxograma que mapeia o processo de envio mencionado acima entre o Braze, o cliente e o Apple Push Notification Service ou o Firebase Cloud Messaging.]({% image_buster /assets/img/push_process.png %})

| Etapas do registro | Etapas de mensagens |
| ------------------ | --------------- |
| 1\. O cliente (dispositivo) se registra no provedor de push<br>2\. O provedor gera e entrega o token push<br>3\. Tokens de descarga no Braze |1\. Braze envia carga útil push para o provedor<br>2\. O provedor entrega a carga útil do push ao dispositivo<br>3\. O SDK passa as estatísticas de mensagens para o Braze |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Perguntas frequentes

### O que acontece quando um usuário opt-in exclui e depois baixa novamente o meu aplicativo?

Suponha que um usuário opte pelo push, receba algumas mensagens push e, posteriormente, exclua o aplicativo. Isso removerá o consentimento por push no nível do dispositivo. A partir daí, o primeiro push devolvido após a desinstalação resultará automaticamente na exclusão desse usuário de futuras mensagens push. Depois disso, se um usuário reinstalar o aplicativo, mas não o iniciar, o Braze não poderá enviar um push para o usuário porque os tokens de push não foram concedidos novamente para o seu aplicativo.

Além disso, se um usuário reativasse o push em primeiro plano, seria necessário iniciar uma sessão para atualizar essas informações no perfil do usuário e começar a receber mensagens push.
 
### Quando os push tokens expiram? {#push-token-expire}

Infelizmente, os APNs e o FCM não definem isso de fato. Os tokens push podem expirar quando um aplicativo é atualizado, quando os usuários transferem seus dados para um novo dispositivo ou quando reinstalam um sistema operacional. Na maioria das vezes, não temos informações sobre por que os provedores de push expiram determinados tokens de push.

Para levar em conta essa ambiguidade, nossas integrações push de SDK sempre registram e liberam os tokens no início da sessão para garantir que tenhamos o token mais atualizado.
