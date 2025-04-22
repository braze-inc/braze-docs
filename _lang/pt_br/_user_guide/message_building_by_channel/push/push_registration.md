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

## 

 







### 



|        |  | Descrição                                                 |
|------------------|------------------|--------------------------------------------------------------------------------------------------------------|
|  |        |            |
|  |         |   |




{% alert note %}
 


### 



Por exemplo, digamos que você tenha dois usuários: Charlie e Kim. Se Charlie tiver ativado as notificações por push para o seu app no telefone dele e Kim usar o telefone de Charlie para sair do perfil de Charlie e registrar o dela, o token por push será reatribuído ao perfil de Kim. O token por push permanecerá atribuído ao perfil de Kim nesse dispositivo até que ela se desconecte e Charlie se conecte novamente.

Um app ou site só pode ter uma inscrição push por dispositivo. Portanto, quando um usuário sai de um dispositivo ou site e um novo usuário faz o registro, o token por push é reatribuído ao novo usuário. Isso é refletido no perfil do usuário na seção **Configurações de contato** da guia **Engajamento**:



Como não há uma maneira de os provedores de push (APNs/FCM) distinguirem entre vários usuários em um dispositivo, passamos o token por push para o último usuário que estava registrado para determinar qual usuário deve ser direcionado no dispositivo para push.

## Registro de token por push

 



 

|        |                                                                                                                                                 |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          |   |
|  |   |




  

|                          |  |                                                                                                                                                      |
|------------------------------------|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|       |                          |   |
|  |                           | Todos os usuários devem aceitar explicitamente o recebimento de notificações por push.                                      |




É necessário solicitar a aceitação explícita dos usuários por meio da caixa de diálogo de permissão nativa do navegador. Receberá um token após a aceitação dos usuários. Ao contrário do iOS e do Android, que permitem que seu app mostre o prompt de permissão a qualquer momento, alguns navegadores modernos só mostrarão o prompt se forem disparados por um "gesto do usuário" (clique do mouse ou pressionamento de tecla). Se o seu site tentar solicitar permissão para notificações por push no carregamento da página, ele provavelmente será ignorado ou silenciado pelo navegador.



### 





- **Perfil do usuário**:  Depois de encontrar o perfil de um usuário (por meio de endereço de e-mail, número de telefone ou ID de usuário externo), é possível selecionar a guia **Engajamento** para visualizar e ajustar manualmente o estado da inscrição de um usuário.
-   A Braze retornará um objeto de tokens por push que contém informações de capacitação por push por dispositivo.

### Verificação do status do registro push

Na guia **Engajamento** no perfil de um usuário, você verá **Push Registered For** seguido pelo nome de um app. Se não houver informações do app para esse dispositivo, você verá dois traços**(--**). Haverá uma entrada para cada dispositivo que pertence ao usuário.

Se o nome do aplicativo da entrada do dispositivo for prefixado por `Foreground:`, o app estará autorizado a receber notificações por push em primeiro plano (visíveis para o usuário) e em segundo plano (não visíveis para o usuário) nesse dispositivo.



Por outro lado, se o nome do aplicativo da entrada do dispositivo for prefixado por `Background:`, o aplicativo só está autorizado a receber notificações [por push em segundo plano]({{site.baseurl}}/user_guide/message_building_by_channel/push/types/#background-push-notifications) e não pode exibir notificações visíveis ao usuário nesse dispositivo. Isso geralmente indica que o usuário desativou as notificações do app nesse dispositivo.

Se um token por push for movido para um usuário diferente no mesmo dispositivo, o primeiro usuário não será mais registrado por push.

## Gerenciamento de tokens por push

Confira no gráfico a seguir as ações que levam à alteração ou remoção de tokens por push dos perfis de usuário. 

| Ação | Descrição |
| ------ | ----------- |
| `changeUser()` método chamado | O método Braze `changeUser()` alterna o ID do usuário ao qual os SDKs estão atribuindo dados de comportamento do usuário. Esse método geralmente é chamado quando um usuário faz o registro em um aplicativo. Quando o `changeUser()` for chamado com uma ID de usuário diferente ou nova em um dispositivo específico, o token por push desse dispositivo será movido para o perfil Braze apropriado com a ID de usuário correspondente. |
| Ocorre um erro de push | Alguns erros comuns de push que levam à remoção do token incluem `MismatchSenderId`, `InvalidRegistration` e outros tipos de bounces de push. <br><br> |
| Desinstalação pelo usuário | Quando um usuário desinstala o aplicativo de um dispositivo, o Braze removerá o token por push do usuário do perfil. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Como isso se parece em uma escala mais ampla?

Quando um usuário abre um novo aplicativo e concede acesso push a partir de um prompt push, é feita uma chamada do SDK da Braze para os provedores push. Quando essa chamada é feita, o provedor de push executa uma verificação para ver se tudo está configurado corretamente. Em caso afirmativo, um token por push é passado para seu dispositivo. Quando esse token chega, o SDK o comunica à Braze. Depois que a Braze receber o token do provedor de push, atualizaremos ou criaremos um novo perfil de usuário. Esses usuários agora são considerados registrados.

Se quisermos lançar uma campanha, criamos uma campanha na Braze que gera uma carga útil de push para enviar ao provedor push. A partir daí, o provedor entrega a carga útil do push para o dispositivo do usuário e o SDK passa o estado do envio de mensagens para o Braze.



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
