{% multi_lang_include developer_guide/prerequisites/swift.md %} Você também precisará [configurar notificações por push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift).

{% alert note %}
Este guia de implementação está centrado em uma implementação Swift, mas são fornecidos trechos em Objective C para os interessados.
{% endalert %}

## Extensões de app de conteúdo de notificação

![Duas mensagens push mostradas lado a lado. A mensagem à esquerda mostra a aparência de um push com a UI padrão. A mensagem à direita mostra um push de cartão perfurado de café feito com a implementação de uma UI de push personalizada.]({% image_buster /assets/img/push_implementation_guide/push1.png %}){: style="max-width:65%;border:0;margin-top:10px"}

As extensões de app de conteúdo de notificação oferecem uma ótima opção para a personalização de notificações por push. As extensões de aplicativo de conteúdo de notificação exibem uma interface personalizada para as notificações do seu app quando uma notificação por push é expandida.

As notificações por push podem ser expandidas de três maneiras diferentes:
- Pressione longamente o banner de push
- Deslizar para baixo no banner push
- Deslize o banner para a esquerda e selecione "Exibir"

Essas visualizações personalizadas oferecem maneiras inteligentes de engajamento com os clientes, exibindo tipos distintos de conteúdo, incluindo notificações interativas, notificações preenchidas com dados de usuários e até mesmo notificações por push que podem capturar informações como números de telefone e e-mail. Um de nossos recursos mais conhecidos no Braze, o [Push Stories]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_stories/), é um excelente exemplo de como pode ser uma extensão de aplicativo de conteúdo de notificação por push!

### Solicitações

![]({% image_buster /assets/img/push_implementation_guide/push15.png %}){: style="float:right;max-width:50%;margin-left:10px; border:0;margin-top:10px"}
- [Notificações por push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) integradas com sucesso em seu app
- Os seguintes arquivos gerados pelo Xcode com base em sua linguagem de codificação:

**Rápido**<br>
- `NotificationViewController.swift`
- `MainInterface.storyboard`

**Objective C**<br>
- `NotificationViewController.h`
- `NotificationViewController.m`
- `MainInterface.storyboard`

## Notificações por push interativas

As notificações por push podem responder às ações do usuário dentro de uma extensão de app de conteúdo. Para usuários que executam o iOS 12 ou posterior, isso significa que você pode transformar suas notificações por push em mensagens totalmente interativas! Isso oferece uma opção interessante para introduzir interatividade em suas promoções e aplicativos. Por exemplo, sua notificação por push pode incluir um jogo para os usuários jogarem, uma roda para ganhar descontos ou um botão "curtir" para salvar uma listagem ou música.

O exemplo a seguir mostra uma notificação por push em que os usuários podem jogar uma partida dentro da notificação expandida.

![Um diagrama de como poderiam ser as fases de uma notificação por push interativa. Uma sequência mostra um usuário pressionando uma notificação por push que exibe um jogo de correspondência interativo.]({% image_buster /assets/img/push_implementation_guide/push12.png %}){: style="border:0"}

### Configuração do dashboard

Para criar uma notificação por push interativa, você deve definir uma exibição personalizada em seu dashboard. 

1. Na página **Campanhas**, clique em **Criar campanha** para iniciar uma nova campanha de notificação por push.
2. Na guia **Criar**, ative **os botões de notificação**. 
3. Digite uma categoria personalizada do iOS no campo **Categoria de notificação do iOS**. 
4. No endereço `.plist` de seu Notification Content Extension Target, defina o atributo `UNNotificationExtensionCategory` para sua categoria personalizada do iOS. O valor fornecido aqui deve corresponder ao que está definido no dashboard do Braze em **iOS Notification Category (Categoria de notificação do iOS**). 
5. Defina a chave `UNNotificationExtensionInteractionEnabled` como `true` para ativar as interações do usuário em uma notificação por push.

![As opções do botão de notificação encontradas nas configurações do criador de mensagens push.]({% image_buster /assets/img/push_implementation_guide/push16.png %}){: style="max-width:75%;border:0;margin-top:10px"}
![]({% image_buster /assets/img/push_implementation_guide/push17.png %}){: style="max-width:75%;border:0;margin-top:10px"}

## Notificações por push personalizadas

![Dois iPhones exibidos lado a lado. O primeiro iPhone mostra a exibição não expandida da mensagem push. O segundo iPhone mostra a versão expandida da mensagem push, exibindo uma foto do "progresso" do curso, o nome da próxima sessão e quando a próxima sessão deverá ser concluída.]({% image_buster /assets/img/push_implementation_guide/push6.png %}){: style="float:right;max-width:40%;margin-left:15px;border:0"}

As notificações por push podem exibir informações específicas do usuário dentro de uma extensão de conteúdo. Isso permite criar conteúdo push focado no usuário, como adicionar a opção de compartilhar seu progresso em diferentes plataformas, mostrar conquistas desbloqueadas ou exibir listas de verificação de integração. Este exemplo mostra uma notificação por push exibida a um usuário após ele ter concluído uma tarefa específica no curso do Braze Learning. Ao expandir a notificação, o usuário pode ver seu progresso na jornada de aprendizagem. As informações fornecidas aqui são específicas do usuário e podem ser disparadas quando uma sessão é concluída ou quando uma ação específica do usuário é realizada, aproveitando um acionador da API. 

### Configuração do dashboard

Para criar uma notificação por push personalizada, você deve definir uma exibição personalizada em seu dashboard. 

1. Na página **Campanhas**, clique em **Criar campanha** para iniciar uma nova campanha de notificação por push.
2. Na guia **Criar**, ative **os botões de notificação**. 
3. Digite uma categoria personalizada do iOS no campo **Categoria de notificação do iOS**. 
4. Na guia **Settings (Configurações** ), crie pares de valores-chave usando o Liquid padrão. Defina as atribuições de usuário apropriadas que deseja que a mensagem mostre. Essas visualizações podem ser personalizadas com base em atribuições específicas de um perfil de usuário específico.
5. No endereço `.plist` de seu Notification Content Extension Target, defina o atributo `UNNotificationExtensionCategory` para sua categoria personalizada do iOS. O valor fornecido aqui deve corresponder ao que está definido no dashboard do Braze em **iOS Notification Category (Categoria de notificação do iOS**). 

![Quatro conjuntos de pares chave-valor, onde "next_session_name" e "next_session_complete_date" são definidos como uma propriedade de disparo da API usando Liquid, e "completed_session contagem" e "total_session_count" são definidos como um atributo de usuário personalizado usando Liquid.]({% image_buster /assets/img/push_implementation_guide/push5.png %}){: style="max-width:60%;"}

### Manuseio de pares de valores-chave

O método `didReceive` é chamado quando a extensão do app de conteúdo de notificação recebe uma notificação. Esse método pode ser encontrado no site `NotificationViewController`. Os pares de valores-chave fornecidos no dashboard são representados no código por meio do uso de um dicionário `userInfo`.

#### Analisando pares de chave-valor de notificações por push

{% tabs %}
{% tab Swift %}
``` swift 
func didReceive(_ notification: UNNotification) {
  let userInfo = notification.request.content.userInfo
     
  guard let value = userInfo["YOUR-KEY-VALUE-PAIR"] as? String,
        let otherValue = userInfo["YOUR-OTHER-KEY-VALUE-PAIR"] as? String,
  else { fatalError("Key-Value Pairs are incorrect.")}
 
  ...
}
```
{% endtab %}
{% tab Objective-C %}
```objc
- (void)didReceiveNotification:(nonnull UNNotification *)notification {
  NSDictionary *userInfo = notification.request.content.userInfo;
   
  if (userInfo[@"YOUR-KEY-VALUE-PAIR"] && userInfo[@"YOUR-OTHER-KEY-VALUE-PAIR"]) {
 
  ...
 
  } else {
    [NSException raise:NSGenericException format:@"Key-Value Pairs are incorrect"];
  }
}
```
{% endtab %}
{% endtabs %}

## Notificação por push de captura de informações

As notificações por push podem capturar informações do usuário dentro de uma extensão de app de conteúdo, empurrando os limites do que é possível com um push. Solicitar a entrada do usuário por meio de notificações por push permite não apenas solicitar informações básicas, como nome ou e-mail, mas também solicitar que os usuários enviem feedback ou completem um perfil de usuário inacabado. 

{% alert tip %}
Para saber mais, veja [Registro de dados de notificação por push]({{site.baseurl}}/developer_guide/analytics/logging_channel_data/push_notifications/).
{% endalert %}

No fluxo a seguir, a exibição personalizada é capaz de responder a alterações de estado. Esses componentes de alteração de estado são representados em cada imagem. 

1. O usuário recebe uma notificação por push.
2. O push é aberto. Depois de expandido, o push solicita informações ao usuário. Neste exemplo, o endereço de e-mail do usuário é solicitado, mas você pode solicitar qualquer tipo de informação.
3. As informações são fornecidas e, se estiverem no formato esperado, o botão de registro é exibido.
3. A visualização de confirmação é exibida e o push é dispensado. 

![]({% image_buster /assets/img/push_implementation_guide/push8.png %}){: style="border:0;"}

### Configuração do dashboard

Para criar uma notificação por push de captura de informações, você deve definir uma exibição personalizada em seu dashboard. 

1. Na página **Campanhas**, clique em **Criar campanha** para iniciar uma nova campanha de notificação por push.
2. Na guia **Criar**, ative **os botões de notificação**. 
3. Digite uma categoria personalizada do iOS no campo **Categoria de notificação do iOS**. 
4. Na guia **Settings (Configurações** ), crie pares de valores-chave usando o Liquid padrão. Defina as atribuições de usuário apropriadas que deseja que a mensagem mostre. 
5. No endereço `.plist` de seu Notification Content Extension Target, defina o atributo `UNNotificationExtensionCategory` para sua categoria personalizada do iOS. O valor fornecido aqui deve corresponder ao que está definido no dashboard do Braze em **iOS Notification Category (Categoria de notificação do iOS**). 

Como visto no exemplo, você também pode incluir uma imagem em sua notificação por push. Para isso, você deve integrar [notificações ricas]({{site.baseurl}}/developer_guide/push_notifications/rich/?sdktab=swift), definir o estilo de notificação em sua campanha como Notificação Rich e incluir uma imagem de notificação por push rica.

![Uma mensagem push com três conjuntos de pares de valores-chave. 1. "Braze_id" definido como uma chamada Liquid para recuperar o ID do Braze. 2. "cert_title" definido como "Certificação de Profissional de Marketing Braze". 3. "Cert_description" definido como "Profissionais de Marketing Braze Certificados impulsionam...".]({% image_buster /assets/img/push_implementation_guide/push9.png %})

### Manipulação de ações de botões

Cada botão de ação é identificado de forma exclusiva. O código verifica se o identificador da resposta é igual a `actionIndentifier` e, em caso afirmativo, sabe que o usuário clicou no botão de ação.

**Manipulação de respostas de botões de ação por push**<br>

{% tabs %}
{% tab Swift %}
``` swift 
func didReceive(_ response: UNNotificationResponse, completionHandler completion: @escaping (UNNotificationContentExtensionResponseOption) -> Void) {
  if response.actionIdentifier == "YOUR-REGISTER-IDENTIFIER" {
    // do something
  } else {
    // do something else
  }
}
```
{% endtab %}
{% tab Objective-C %}
```objc
- (void)didReceiveNotificationResponse:(UNNotificationResponse *)response completionHandler:(void (^)(UNNotificationContentExtensionResponseOption))completion {
  if ([response.actionIdentifier isEqualToString:@"YOUR-REGISTER-IDENTIFIER"]) {
    completion(UNNotificationContentExtensionResponseOptionDismiss);
  } else {
    completion(UNNotificationContentExtensionResponseOptionDoNotDismiss);
  }
}
```
{% endtab %}
{% endtabs %}

### Dispensa de push

As notificações por push podem ser automaticamente descartadas a partir do pressionamento de um botão de ação. Há três opções pré-construídas de push dismissal que recomendamos:

1. `completion(.dismiss)` - Descarta a notificação
2. `completion(.doNotDismiss)` - A notificação permanece aberta
3. `completion(.dismissAndForward)` - O push é descartado e o usuário é encaminhado para o aplicativo
