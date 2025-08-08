---
nav_title: "Registro Push"
article_title: Registro Push
page_order: 2
page_type: reference
description: "Este artigo de referência discute o que significa estar registrado para push e como enviamos mensagens push e lidamos com tokens por push e registro por push no Braze."
channel:
 - push

---

# Registro push

> Este artigo aborda o processo pelo qual um usuário é atribuído a um token por push e como o Braze envia mensagens por push aos seus usuários.

## Sobre tokens por push {#push-tokens}

Quando um aplicativo solicita permissões push de um dispositivo, o provedor de notificação por push do dispositivo gera um token push para esse aplicativo. Cada aplicativo recebe seu próprio token por push exclusivo e anônimo, que é como ele identifica o dispositivo e a instância atual do app ao enviar uma notificação por push.

Lembre-se de que os tokens por push não são identificadores estáticos que duram para sempre - eles podem ser atualizados e podem [expirar](#push-token-expire).

{% alert tip %}
Para obter detalhes específicos da plataforma, consulte [Registro de token por push](#push-token-registration).
{% endalert %}

### Push em primeiro plano versus push em segundo plano {#foreground-vs-background}

Os tokens por push são usados para enviar notificações por push em primeiro e segundo plano.

| Tipo       | Requer aceitação? | Descrição                                                 |
|------------------|------------------|--------------------------------------------------------------------------------------------------------------|
| Push de primeiro plano | Sim       | Uma notificação é exibida visivelmente para o usuário enquanto o app está em primeiro plano.           |
| Empurrão de fundo | Não        | Uma notificação é entregue silenciosamente em segundo plano, sem ser exibida. Geralmente usado para funcionalidades como rastreamento de desinstalação. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Quando um usuário aceita notificações por push para o seu app, ele será considerado "registrado por push", o que significa que agora pode ser direcionado usando o filtro de segmentação `Push enabled for App` no Braze.

{% alert note %}
Isso é diferente do filtro de segmentação `Push Enabled`, que é usado para identificar os usuários que fizeram a aceitação de pelo menos um de seus aplicativos - não de um aplicativo específico. Para saber mais, consulte [Filtros de segmentação]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#push-enabled).
{% endalert %}

### Vários usuários em um dispositivo

Os tokens por push são exclusivos para o dispositivo e o app, o que significa que os tokens por push não podem ser usados para direcionamento a usuários específicos se vários usuários estiverem usando o mesmo dispositivo.

Por exemplo, digamos que você tenha dois usuários: Charlie e Kim. Se Charlie tiver ativado as notificações por push para o seu app no telefone dele e Kim usar o telefone de Charlie para sair do perfil de Charlie e registrar o dela, o token por push será reatribuído ao perfil de Kim. O token por push permanecerá atribuído ao perfil de Kim nesse dispositivo até que ela se desconecte e Charlie se conecte novamente.

Um app ou site só pode ter uma inscrição push por dispositivo. Portanto, quando um usuário sai de um dispositivo ou site e um novo usuário faz o registro, o token por push é reatribuído ao novo usuário. Isso é refletido no perfil do usuário na seção **Configurações de contato** da guia **Engajamento**:

![Token por push changelog na guia \*\*Engagement** do perfil de um usuário, que lista quando o token por push foi movido para outro usuário e qual era o token.]({% image_buster /assets/img/push_token_changelog.png %})

Como não há uma maneira de os provedores de push (APNs/FCM) distinguirem entre vários usuários em um dispositivo, passamos o token por push para o último usuário que estava registrado para determinar qual usuário deve ser direcionado no dispositivo para push.

## Registro de token por push

Cada plataforma de dispositivo lida com o registro de token por push de forma diferente. Consulte o seguinte para obter detalhes específicos da plataforma:

{% tabs local %}
{% tab Android %}
Quando seu aplicativo é instalado, um token por push é gerado automaticamente para seu app; no entanto, ele só pode ser usado para [notificações por push em segundo plano](#foreground-vs-background) até que o usuário faça a aceitação explícita. Além disso, o registro é tratado de forma diferente em diferentes versões do Android:

| versão       | Informações                                                                                                                                                |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Android 13**         | A permissão push deve ser solicitada e concedida pelo usuário. Seu app pode solicitar a permissão manualmente, ou os usuários serão solicitados automaticamente depois que um [canal de notificação](https://developer.android.com/reference/android/app/NotificationChannel) for criado. |
| **Android 12 e versões anteriores** | Todos os usuários são considerados `Subscribed` após a primeira sessão. O Braze solicita automaticamente um token por push nesse momento, tornando o usuário habilitado para push com um token válido e um estado de inscrição padrão de `Subscribed`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% endtab %}

{% tab ios %}
O iOS não gera automaticamente tokens por push para um app quando ele é instalado. Além disso, o registro é tratado de forma diferente em diferentes versões do iOS: 

| versão                         | Autorização provisória? | Informações                                                                                                                                                     |
|------------------------------------|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **iOS 12**      | Sim                         | Quando um usuário faz a aceitação de notificações por push, você recebe uma autorização padrão que lhe permite enviar [notificações por push em primeiro plano](#foreground-vs-background). No entanto, você também pode solicitar uma [autorização provisória]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/#provisional-push), que permite enviar [notificações por push](#foreground-vs-background) silenciosas [em segundo plano](#foreground-vs-background) diretamente para a central de notificações. |
| **iOS 11 e posterior** | Não                          | Todos os usuários devem aceitar explicitamente o recebimento de notificações por push. Um token por push é gerado somente depois que a permissão é concedida.                                     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
{% endtab %}

{% tab web %}
É necessário solicitar a aceitação explícita dos usuários por meio da caixa de diálogo de permissão nativa do navegador. Receberá um token após a aceitação dos usuários. Ao contrário do iOS e do Android, que permitem que seu app mostre o prompt de permissão a qualquer momento, alguns navegadores modernos só mostrarão o prompt se forem disparados por um "gesto do usuário" (clique do mouse ou pressionamento de tecla). Se o seu site tentar solicitar permissão para notificações por push no carregamento da página, ele provavelmente será ignorado ou silenciado pelo navegador.
{% endtab %}
{% endtabs %}

### Verificação do estado da inscrição push do usuário

![Perfil de usuário para John Doe com seu estado de inscrição push definido como Subscribed (Inscrito).]({% image_buster /assets/img/push_example.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Há duas maneiras de verificar o estado da inscrição push de um usuário com o Braze:

- **Perfil do usuário**: Você pode acessar perfis de usuários individuais por meio do dashboard do Braze na página [User Search (Pesquisa de usuários]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/) ). Depois de encontrar o perfil de um usuário (por meio de endereço de e-mail, número de telefone ou ID de usuário externo), é possível selecionar a guia **Engajamento** para visualizar e ajustar manualmente o estado da inscrição de um usuário.
- **Exportação da API Rest**: É possível exportar perfis de usuários individuais no formato JSON usando os pontos de extremidade Exportar [usuários por segmento]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/) ou [Usuários por identificador]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/). A Braze retornará um objeto de tokens por push que contém informações de capacitação por push por dispositivo.

### Verificação do status do registro push

Na guia **Engajamento** no perfil de um usuário, você verá **Push Registered For** seguido pelo nome de um app. Se não houver informações do app para esse dispositivo, você verá dois traços**(--**). Haverá uma entrada para cada dispositivo que pertence ao usuário.

Se o nome do aplicativo da entrada do dispositivo for prefixado por `Foreground:`, o app estará autorizado a receber notificações por push em primeiro plano (visíveis para o usuário) e em segundo plano (não visíveis para o usuário) nesse dispositivo.

![Push Changelog com um exemplo de token por push.]({% image_buster /assets/img/push_changelog.png %}){: style="float:right;max-width:40%;margin-left:15px;margin-top:10px;"}

Por outro lado, se o nome do aplicativo da entrada do dispositivo for prefixado por `Background:`, o aplicativo só está autorizado a receber notificações [por push em segundo plano]({{site.baseurl}}/user_guide/message_building_by_channel/push/types/#background-push-notifications) e não pode exibir notificações visíveis ao usuário nesse dispositivo. Isso geralmente indica que o usuário desativou as notificações do app nesse dispositivo.

Se um token por push for movido para um usuário diferente no mesmo dispositivo, o primeiro usuário não será mais registrado por push.

## Gerenciamento de tokens por push

Confira no gráfico a seguir as ações que levam à alteração ou remoção de tokens por push dos perfis de usuário. 

| Ação | Descrição |
| ------ | ----------- |
| `changeUser()` método chamado | O método Braze `changeUser()` alterna o ID do usuário ao qual os SDKs estão atribuindo dados de comportamento do usuário. Esse método geralmente é chamado quando um usuário faz o registro em um aplicativo. Quando o `changeUser()` for chamado com uma ID de usuário diferente ou nova em um dispositivo específico, o token por push desse dispositivo será movido para o perfil Braze apropriado com a ID de usuário correspondente. |
| Ocorre um erro de push | Alguns erros comuns de push que levam à remoção do token incluem `MismatchSenderId`, `InvalidRegistration` e outros tipos de bounces de push. <br><br>Confira nossa lista completa de [erros comuns de push]({{site.baseurl}}/help/help_articles/push/push_error_codes/#push-bounced-mismatchsenderid). |
| Desinstalação pelo usuário | Quando um usuário desinstala o aplicativo de um dispositivo, o Braze removerá o token por push do usuário do perfil. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Como isso se parece em uma escala mais ampla?

Quando um usuário abre um novo aplicativo e concede acesso push a partir de um prompt push, é feita uma chamada do SDK da Braze para os provedores push. Quando essa chamada é feita, o provedor de push executa uma verificação para ver se tudo está configurado corretamente. Em caso afirmativo, um token por push é passado para seu dispositivo. Quando esse token chega, o SDK o comunica à Braze. Depois que a Braze receber o token do provedor de push, atualizaremos ou criaremos um novo perfil de usuário. Esses usuários agora são considerados registrados.

Se quisermos lançar uma campanha, criamos uma campanha na Braze que gera uma carga útil de push para enviar ao provedor push. A partir daí, o provedor entrega a carga útil do push para o dispositivo do usuário e o SDK passa o estado do envio de mensagens para o Braze.

![Um fluxograma que mapeia o processo de push mencionado acima entre o Braze, o cliente e o serviço de Notificações por Push da Apple ou o envio de mensagens do Firebase Cloud.]({% image_buster /assets/img/push_process.png %})

| Etapas de registro | Etapas do envio de mensagens |
| ------------------ | --------------- |
| 1\. O cliente (dispositivo) se registra no provedor de push<br>2\. O provedor gera e entrega o token por push<br>3\. Flush tokens no Braze |1\. Braze envia carga útil push para o provedor<br>2\. O provedor entrega a carga útil do push ao dispositivo<br>3\. O SDK passa as estatísticas de envio de mensagens para o Braze |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Perguntas frequentes

### O que acontece quando um usuário com aceitação exclui e depois baixa novamente o meu app?

Suponha que um usuário aceite o push, receba algumas mensagens no app e, posteriormente, exclua o aplicativo. Isso removerá o consentimento push no nível do dispositivo. A partir daqui, o primeiro push com bounce após a desinstalação resultará automaticamente na aceitação desse usuário de futuros envios de mensagens push. Depois disso, se um usuário reinstalar o aplicativo, mas não o iniciar, o Braze não poderá enviar um push para o usuário porque os tokens por push não foram concedidos novamente para o seu app.

Além disso, se um usuário voltasse a ativar o push em primeiro plano, seria necessário iniciar uma sessão para atualizar essas informações em seu perfil de usuário para começar a receber envios de mensagens push.
 
### Quando os tokens por push expiram? {#push-token-expire}

Infelizmente, os APNs e o FCM não definem isso de fato. Os tokens por push podem expirar quando um app é atualizado, quando os usuários transferem seus dados para um novo dispositivo ou quando reinstalam um sistema operacional. Na maioria das vezes, não temos insight sobre por que os provedores de push expiram determinados tokens por push.

Para levar em conta essa ambiguidade, nossas integrações de SDK por push sempre registram e liberam tokens no início da sessão para garantir que tenhamos o token mais atualizado.
