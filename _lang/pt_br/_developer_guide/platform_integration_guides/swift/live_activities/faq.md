---
nav_title: Perguntas frequentes
article_title: Perguntas frequentes sobre atividades ao vivo
page_order: 20
description: "Esta página fornece respostas às perguntas mais frequentes sobre atividades ao vivo para o SDK do Swift."
tool: Live Activities
platform:
  - iOS
---

# Perguntas frequentes

> Este artigo fornece respostas a algumas perguntas frequentes sobre as atividades ao vivo.

## Funcionalidade e suporte

### Quais plataformas suportam o Live Activities?

Atualmente, as atividades ao vivo são um recurso específico do iOS. O artigo "Atividades ao vivo" aborda os [pré-requisitos]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/live_activities/live_activities/#prerequisites) para o gerenciamento de atividades ao vivo por meio do SDK da Braze para Swift.

### Os apps React Native são compatíveis com atividades ao vivo?

Sim, o React Native SDK 3.0.0+ oferece suporte a atividades ao vivo por meio do SDK da Braze para Swift. Ou seja, você precisa escrever código React Native iOS diretamente sobre o SDK da Braze para Swift. 

Não há uma API de conveniência JavaScript específica do React Native para atividades ao vivo porque os recursos de atividades ao vivo fornecidos pela Apple usam linguagens intraduzíveis em JavaScript (por exemplo, concorrência Swift, genéricos, SwiftUI).

### O Braze oferece suporte a atividades ativas como uma campanha ou etapa do Canva?

Não, isso não é suportado no momento.

## Notificações por push e atividades ao vivo

### O que acontece se uma notificação por push for enviada enquanto uma Live Activity estiver ativa? 

![Uma tela de telefone com uma atividade ao vivo de um jogo esportivo entre Bulls e Bears no meio da tela e um texto de notificação por push lorem ipsum na parte inferior da tela.]({% image_buster /assets/img/push-vs-live-activities.png %}){: style="max-width:30%;float:right;margin-left:15px;"}

As Live Activities e as notificações por push ocupam espaço diferente na tela e não entram em conflito na tela do usuário.

### Se as Live Activities utilizam a funcionalidade de envio de mensagens push, as notificações por push precisam ser ativadas para receber as Live Activities?

Embora as atividades ao vivo dependam de notificações por push para atualizações, elas são controladas por diferentes configurações de usuário. Um usuário pode aceitar atividades ao vivo, mas não as notificações por push, e vice-versa.

Os tokens de atualização do Live Activity expiram após oito horas.

### As atividades ao vivo requerem push primers?

[Os push primers]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/) são uma prática recomendada para solicitar que os usuários aceitem notificações por push do seu app. No entanto, não há nenhum pedido de aceitação do sistema para atividades ao vivo. Por padrão, os usuários recebem a aceitação do Live Activities para um aplicativo individual quando o usuário instala esse app no iOS 16.1 ou posterior. Essa permissão pode ser ativada ou desativada nas configurações do dispositivo por aplicativo.

## Tópicos técnicos e solução de problemas

### Como posso saber se o Live Activities tem erros?

Todos os erros das atividades ao vivo serão registrados no dashboard da Braze no [Registro de atividades de mensagem]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/), onde é possível filtrar por "Erros de atividade ao vivo".

### Depois de enviar uma notificação por push para iniciar, por que não recebi meu Live Activity?

Primeiro, verifique se sua carga útil inclui todos os campos obrigatórios descritos no [`messages/live_activity/start`]({{site.baseurl}}/api/endpoints/messaging/live_activity/start) endpoint. Os campos `activity_attributes` e `content_state` devem corresponder às propriedades definidas no código de seu projeto. Se tiver certeza de que a carga útil está correta, é possível que você esteja limitado de frequência pelos APNs. Esse limite é imposto pela Apple e não pela Braze.

Para verificar se a notificação por push chegou com sucesso ao dispositivo, mas não foi exibida devido aos limites de frequência, é possível depurar o projeto usando o app Console no Mac. Anexe o processo de gravação do dispositivo desejado e, em seguida, filtre os registros por `process:liveactivitiesd` na barra de pesquisa.

### Estou recebendo uma resposta de acesso negado quando tento usar o endpoint `live_activity/update`. Por quê?

As chaves de API que você usa precisam receber as permissões corretas para acessar os diferentes endpoints da Braze API. Se estiver usando uma chave de API criada anteriormente, é possível que tenha se esquecido de atualizar as permissões. Leia nossa [visão geral da segurança da chave de API]({{site.baseurl}}/api/basics/#rest-api-key-security) para uma atualização.

### O endpoint`messages/send` compartilha os limites de frequência com o endpoint`messages/live_activity/update`? 

Por padrão, o limite de frequência do endpoint`messages/live_activity/update` é de 250.000 solicitações por hora, por espaço de trabalho e em vários endpoints. Consulte os [limites de frequência da API]({{site.baseurl}}/api/api_limits/) para obter mais informações.

### Por que meus tokens por push-to-start não estão sendo gerados?

A Apple limitou suas APIs `pushToStartToken` e `pushToStartTokenUpdates`, que foram introduzidas no iOS 17.2. Na prática, os tokens por push-to-start são gerados somente durante a primeira inicialização do app em `application(_:didFinishLaunchingWithOptions:)` após a primeira instalação. Se essa etapa precisar ser repetida, os tokens só poderão ser gerados novamente com a criação manual de uma nova instância do Live Activity ou após a reinicialização e a reinstalação do app.

### Quantas Live Activities posso iniciar para meu app?

Os limites são definidos pela Apple e podem variar com base em vários fatores. Eles também podem estar sujeitos a alterações no futuro. Na prática, há um limite de cinco instâncias de atividade simultâneas que podem ser iniciadas por app em um determinado momento. Todas as tentativas subsequentes de iniciar uma nova instância além desse limite serão ignoradas pelo sistema.

### Que outros aspectos devo observar durante a solução de problemas?

- Certifique-se de que esteja usando uma chave `.p8` para autenticação em vez de um arquivo `.p12` ou `.pem`.
- Verifique se o seu perfil de provisionamento push corresponde ao ambiente que está testando. Os certificados universais podem ser configurados no dashboard do Braze para serem enviados para o ambiente de desenvolvimento ou de produção do serviço de Notificações por Push da Apple (APNs). O uso de um certificado de desenvolvimento para um aplicativo de produção ou de um certificado de produção para um aplicativo de desenvolvimento não funcionará.


