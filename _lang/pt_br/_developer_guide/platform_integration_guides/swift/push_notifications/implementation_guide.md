---
nav_title: Implementação avançada (opcional)
article_title: Implementação avançada de notificações por push para iOS (opcional)
platform: Swift
page_order: 30
description: "Este guia de implementação avançada aborda como aproveitar as extensões de aplicativo de conteúdo de notificação por push do iOS para obter o máximo de suas mensagens por push com o Swift SDK."
channel:
  - push
---

<br>
{% alert important %}
Está procurando o guia básico de integração de desenvolvedores de notificações por push? Acesse [aqui]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/).
{% endalert %}

# Guia de implementação avançada

> Este guia de implementação avançado e opcional aborda maneiras de aproveitar as extensões de app de conteúdo de notificação para obter o máximo de suas mensagens por push. 

Este guia fornece três exemplos de implementações de extensões de app de conteúdo de notificação, cada uma com um passo a passo do conceito, casos de uso em potencial e uma visão de como as variáveis de notificação por push podem parecer e ser usadas no dashboard do Braze:
- [Notificações por push interativas](#interactive-push-notification)
- [Notificações por push personalizadas](#personalized-push-notifications)
- [Notificações por push de captura de informações](#information-capture-push-notification)

Este artigo também fornece [orientação sobre análise de dados de registro](#logging-analytics) para essas implementações personalizadas.

Note que este guia de implementação está centrado em uma implementação Swift, mas são fornecidos trechos em Objective C para os interessados.

## Extensões de conteúdo de notificação de app

![Duas mensagens push mostradas lado a lado. A mensagem à esquerda mostra a aparência de um push com a UI padrão. A mensagem à direita mostra um push de cartão perfurado de café feito com a implementação de uma UI de push personalizada.]({% image_buster /assets/img/push_implementation_guide/push1.png %}){: style="max-width:65%;border:0;margin-top:10px"}

As extensões de app de conteúdo de notificação oferecem uma ótima opção para a personalização de notificações por push. As extensões de aplicativo de conteúdo de notificação exibem uma interface personalizada para as notificações do seu app quando uma notificação por push é expandida. 

As notificações por push podem ser expandidas de três maneiras diferentes:
- Pressione longamente o banner de push
- Deslizar para baixo no banner push
- Deslize o banner para a esquerda e selecione "Exibir" 

Essas visualizações personalizadas oferecem maneiras inteligentes de engajamento com os clientes, exibindo tipos distintos de conteúdo, incluindo notificações interativas, notificações preenchidas com dados de usuários e até mesmo notificações por push que podem capturar informações como números de telefone e e-mail. Um de nossos recursos mais conhecidos no Braze, o [Push Stories]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_stories/), é um excelente exemplo de como pode ser uma extensão de aplicativo de conteúdo de notificação por push!

### Solicitações
![]({% image_buster /assets/img/push_implementation_guide/push15.png %}){: style="float:right;max-width:50%;margin-left:10px; border:0;margin-top:10px"}
- [Notificações por push]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/) integradas com sucesso em seu app
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

### Pronto para fazer a análise de dados?
Visite a [seção Análise de registros](#logging-analytics) para entender melhor como deve ser o fluxo de dados.

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

![Quatro conjuntos de pares de valores-chave, em que "next_session_name" e "next_session_complete_date" são definidos como uma propriedade de disparo da API usando o Liquid, e "completed_session count" e "total_session_count" são definidos como um atributo personalizado do usuário usando o Liquid.]({% image_buster /assets/img/push_implementation_guide/push5.png %}){: style="max-width:60%;"}

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
{% tab Objective C %}
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

### Pronto para fazer a análise de dados?
Visite a [seção Análise de registros](#logging-analytics) para entender melhor como deve ser o fluxo de dados.

## Notificação por push de captura de informações

As notificações por push podem capturar informações do usuário dentro de uma extensão de app de conteúdo, empurrando os limites do que é possível com um push. Solicitar a entrada do usuário por meio de notificações por push permite não apenas solicitar informações básicas, como nome ou e-mail, mas também solicitar que os usuários enviem feedback ou completem um perfil de usuário inacabado. 

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

Como visto no exemplo, você também pode incluir uma imagem em sua notificação por push. Para isso, você deve integrar [notificações ricas]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/rich_notifications/), definir o estilo de notificação em sua campanha como Notificação Rich e incluir uma imagem de notificação por push rica.

![Uma mensagem push com três conjuntos de pares de valores-chave. 1\. "Braze_id" definido como uma chamada Liquid para recuperar a ID do Braze. 2\. "cert_title" definido como "Braze Marketer Certification". 3\. "Cert_description" definido como "Certified Braze marketers drive...".]({% image_buster /assets/img/push_implementation_guide/push9.png %})

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
{% tab Objective C %}
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

### Descarte de push

As notificações por push podem ser automaticamente descartadas a partir do pressionamento de um botão de ação. Há três opções pré-construídas de push dismissal que recomendamos:

1. `completion(.dismiss)` - Descarta a notificação
2. `completion(.doNotDismiss)` - A notificação permanece aberta
3. `completion(.dismissAndForward)` - O push é descartado e o usuário é encaminhado para o aplicativo

### Pronto para fazer a análise de dados?
Consulte a [seção a seguir](#logging-analytics) para entender melhor como o fluxo de dados deve ser. 

## Análise de dados de registro

### Registro com a API do Braze (recomendado)

A análise de dados de registro pode ser feita em tempo real com a ajuda do [endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) da API da Braze.]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) Para análise de dados, envie o valor chave-valor `braze_id` (como visto na captura de tela a seguir) para identificar qual perfil de usuário deve ser atualizado.

![Uma mensagem push com três conjuntos de pares de valores-chave. 1\. "Braze_id" definido como uma chamada Liquid para recuperar a ID do Braze. 2\. "cert_title" definido como "Braze Marketer Certification". 3\. "Cert_description" definido como "Certified Braze marketers drive...".]({% image_buster /assets/img/push_implementation_guide/push18.png %}){: style="max-width:80%;"}

### Registro manual

O registro manual exigirá primeiro a configuração dos espaços de trabalho no Xcode e, em seguida, a criação, o salvamento e a recuperação da análise de dados. Isso exigirá algum trabalho de desenvolvedor personalizado de sua parte. Os trechos de código mostrados a seguir ajudarão a resolver esse problema. 

É importante notar que a análise de dados não é enviada à Braze até que o aplicativo móvel seja lançado posteriormente. Isso significa que, dependendo das configurações de dispensa, muitas vezes existe um período indeterminado de tempo entre o momento em que uma notificação por push é dispensada e o aplicativo móvel é iniciado e as análises de dados são recuperadas. Embora esse buffer de tempo possa não afetar todos os casos de uso, você deve considerar esse impacto e ajustar a jornada do usuário conforme necessário para incluir a abertura do aplicativo para resolver essa preocupação. 

![Um gráfico que descreve como as análises de dados são processadas na Braze. 1\. Os dados de análises são criados. 2\. Os dados de análises são salvos. 3\. A notificação por push é dispensada. 4\. Período indeterminado de tempo entre o momento em que a notificação por push é descartada e o app móvel é iniciado. 5\. O app móvel é lançado. 6\. Os dados e análises são recebidos. 7\. Os dados de análises são enviados para o Braze.]({% image_buster /assets/img/push_implementation_guide/push13.png %})

#### Etapa 1: Configurar grupos de app no Xcode
No Xcode, adicione o recurso `App Groups`. Se você não tiver nenhum espaço de trabalho em seu aplicativo, acesse o recurso do direcionamento do aplicativo principal, ative o endereço `App Groups` e clique no botão **+** Adicionar. Em seguida, use o ID do pacote de seu app para criar o espaço de trabalho. Por exemplo, se o ID do pacote do seu app for `com.company.appname`, você poderá nomear seu espaço de trabalho como `group.com.company.appname.xyz`. Certifique-se de que o endereço `App Groups` esteja ativado tanto para o destino principal do app quanto para o destino da extensão de conteúdo.

![]({% image_buster /assets/img/swift/push_story/add_app_groups.png %})

#### Etapa 2: Integrar trechos de código
Os seguintes trechos de código são uma referência útil sobre como salvar e enviar eventos personalizados, atributos personalizados e atributos de usuário. Este guia falará em termos de `UserDefaults`, mas a representação do código será feita na forma do arquivo auxiliar `RemoteStorage`. Há arquivos auxiliares adicionais, `UserAttributes` e `EventName Dictionary`, que são usados ao enviar e salvar atribuições do usuário.

{% tabs localização %}
{% tab Eventos personalizados %}

##### Salvando eventos personalizados

Para salvar eventos personalizados, você deve criar a análise de dados do zero. Isso é feito com a criação de um dicionário, preenchendo-o com metadados e salvando os dados por meio do uso de um arquivo auxiliar.

1. Inicializar um dicionário com metadados de eventos
2. Inicialize `userDefaults` para recuperar e armazenar os dados do evento
3. Se houver um vetor existente, acrescente novos dados a ele e salve-o
4. Se não houver um vetor existente, salve o novo vetor em `userDefaults`

{% subtabs global %}
{% subtab Swift %}
``` swift 
func saveCustomEvent(with properties: [String: Any]? = nil) {
  // 1
  let customEventDictionary = Dictionary(eventName: "YOUR-EVENT-NAME", properties: properties)
  
  // 2
  let remoteStorage = RemoteStorage(storageType: .suite)
  
  // 3   
  if var pendingEvents = remoteStorage.retrieve(forKey: .pendingCustomEvents) as? [[String: Any]] {
    pendingEvents.append(contentsOf: [customEventDictionary])
    remoteStorage.store(pendingEvents, forKey: .pendingCustomEvents)
  } else {
  // 4
    remoteStorage.store([customEventDictionary], forKey: .pendingCustomEvents)
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)saveCustomEvent:(NSDictionary<NSString *, id> *)properties {
  // 1 
  NSDictionary<NSString *, id> *customEventDictionary = [[NSDictionary alloc] initWithEventName:@"YOUR-EVENT-NAME" properties:properties];
  
  // 2
  RemoteStorage *remoteStorage = [[RemoteStorage alloc] initWithStorageType:StorageTypeSuite];
  NSMutableArray *pendingEvents = [[remoteStorage retrieveForKey:RemoteStorageKeyPendingCustomEvents] mutableCopy];
  
  // 3 
  if (pendingEvents) {
    [pendingEvents addObject:customEventDictionary];
    [remoteStorage store:pendingEvents forKey:RemoteStorageKeyPendingCustomAttributes];
  } else {
  // 4
    [remoteStorage store:@[ customEventDictionary ] forKey:RemoteStorageKeyPendingCustomAttributes];
  }
}
```
{% endsubtab %}
{% endsubtabs %}

##### Envio de eventos personalizados para o Braze

O melhor momento para registrar qualquer análise de dados salva de uma extensão de app de conteúdo de notificação é logo após a inicialização do SDK. Isso pode ser feito percorrendo todos os eventos pendentes, verificando a chave "Event Name", definindo os valores apropriados na Braze e, em seguida, limpando o armazenamento para a próxima vez que essa função for necessária.

1. Percorrer a matriz de eventos pendentes
2. Percorra cada par de valores-chave no dicionário `pendingEvents` 
3. Verifique explicitamente a chave de "Event Name" para definir o valor de acordo
4. Todos os outros valores-chave serão adicionados ao dicionário `properties` 
5. Registrar eventos personalizados individuais 
6. Remover todos os eventos pendentes do armazenamento

{% subtabs global %}
{% subtab Swift %}
``` swift 
func logPendingCustomEventsIfNecessary() {
  let remoteStorage = RemoteStorage(storageType: .suite)
  guard let pendingEvents = remoteStorage.retrieve(forKey: .pendingCustomEvents) as? [[String: Any]] else { return }
  
  // 1    
  for event in pendingEvents {
    var eventName: String?
    var properties: [AnyHashable: Any] = [:]
    
  // 2
    for (key, value) in event {
      if key == PushNotificationKey.eventName.rawValue {
  // 3      
        if let eventNameValue = value as? String {
          eventName = eventNameValue
        } else {
          print("Invalid type for event_name key")
        }
      } else {
  // 4 
        properties[key] = value
      }
    }
  // 5    
    if let eventName = eventName {
      AppDelegate.braze?.logCustomEvent(eventName, properties: properties)
    }
  }

  // 6    
  remoteStorage.removeObject(forKey: .pendingCustomEvents)
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)logPendingEventsIfNecessary {
  RemoteStorage *remoteStorage = [[RemoteStorage alloc] initWithStorageType:StorageTypeSuite];
  NSArray *pendingEvents = [remoteStorage retrieveForKey:RemoteStorageKeyPendingCustomEvents];
  
  // 1 
  for (NSDictionary<NSString *, id> *event in pendingEvents) {
    NSString *eventName = nil;
    NSMutableDictionary *properties = [NSMutableDictionary dictionary];
    
  // 2 
    for (NSString* key in event) {
      if ([key isEqualToString:@"event_name"]) {
  // 3       
        if ([[event objectForKey:key] isKindOfClass:[NSString class]]) {
          eventName = [event objectForKey:key];
        } else {
          NSLog(@"Invalid type for event_name key");
        }
      } else {
  // 4 
        properties[key] = event[key];
      }
    }
  // 5  
    if (eventName != nil) {
      [AppDelegate.braze logCustomEvent:eventName properties:properties];
    }
  }

  // 6  
  [remoteStorage removeObjectForKey:RemoteStorageKeyPendingCustomEvents];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Atributos personalizados %}

##### Salvando atributos personalizados

Para salvar atributos personalizados, você deve criar a análise de dados do zero. Isso é feito com a criação de um dicionário, preenchendo-o com metadados e salvando os dados por meio do uso de um arquivo auxiliar.

1. Inicializar um dicionário com metadados de atribuição
2. Inicialize o site `userDefaults` para recuperar e armazenar os dados de atribuição
3. Se houver um vetor existente, acrescente novos dados a ele e salve-o
4. Se não houver um vetor existente, salve o novo vetor em `userDefaults`

{% subtabs global %}
{% subtab Swift %}
``` swift 
func saveCustomAttribute() {
  // 1 
  let customAttributeDictionary: [String: Any] = ["YOUR-CUSTOM-ATTRIBUTE-KEY": "YOUR-CUSTOM-ATTRIBUTE-VALUE"]
  
  // 2 
  let remoteStorage = RemoteStorage(storageType: .suite)
  
  // 3 
  if var pendingAttributes = remoteStorage.retrieve(forKey: .pendingCustomAttributes) as? [[String: Any]] {
    pendingAttributes.append(contentsOf: [customAttributeDictionary])
    remoteStorage.store(pendingAttributes, forKey: .pendingCustomAttributes)
  } else {
  // 4 
    remoteStorage.store([customAttributeDictionary], forKey: .pendingCustomAttributes)
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
``` objc
- (void)saveCustomAttribute {
  // 1 
  NSDictionary<NSString *, id> *customAttributeDictionary = @{ @"YOUR-CUSTOM-ATTRIBUTE-KEY": @"YOUR-CUSTOM-ATTRIBUTE-VALUE" };
  
  // 2  
  RemoteStorage *remoteStorage = [[RemoteStorage alloc] initWithStorageType:StorageTypeSuite];
  NSMutableArray *pendingAttributes = [[remoteStorage retrieveForKey:RemoteStorageKeyPendingCustomAttributes] mutableCopy];
  
  // 3
  if (pendingAttributes) {
    [pendingAttributes addObject:customAttributeDictionary];
    [remoteStorage store:pendingAttributes forKey:RemoteStorageKeyPendingCustomAttributes];
  } else {
  // 4 
    [remoteStorage store:@[ customAttributeDictionary ] forKey:RemoteStorageKeyPendingCustomAttributes];
  }
}
```
{% endsubtab %}
{% endsubtabs %}

##### Envio de atributos personalizados para o Braze

O melhor momento para registrar qualquer análise de dados salva de uma extensão de app de conteúdo de notificação é logo após a inicialização do SDK. Isso pode ser feito percorrendo os atributos pendentes, definindo o atributo personalizado apropriado na Braze e, em seguida, limpando o armazenamento para a próxima vez que essa função for necessária.

1. Percorrer a matriz de atribuições pendentes
2. Percorra cada par de valores-chave no dicionário `pendingAttributes` 
3. Registre atributos personalizados individuais com a chave e o valor correspondentes
4. Remover todas as atribuições pendentes do armazenamento

{% subtabs global %}
{% subtab Swift %}
``` swift 
func logPendingCustomAttributesIfNecessary() {
  let remoteStorage = RemoteStorage(storageType: .suite)
  guard let pendingAttributes = remoteStorage.retrieve(forKey: .pendingCustomAttributes) as? [[String: Any]] else { return }
     
  // 1
  pendingAttributes.forEach { setCustomAttributesWith(keysAndValues: $0) }
  
  // 4 
  remoteStorage.removeObject(forKey: .pendingCustomAttributes)
}
   
func setCustomAttributesWith(keysAndValues: [String: Any]) {
  // 2 
  for (key, value) in keysAndValues {
  // 3
    if let value = value as? [String] {
      setCustomAttributeArrayWithKey(key, andValue: value)
    } else {
      setCustomAttributeWithKey(key, andValue: value)
    }
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)logPendingCustomAttributesIfNecessary {
  RemoteStorage *remoteStorage = [[RemoteStorage alloc] initWithStorageType:StorageTypeSuite];
  NSArray *pendingAttributes = [remoteStorage retrieveForKey:RemoteStorageKeyPendingCustomAttributes];
   
  // 1
  for (NSDictionary<NSString*, id> *attribute in pendingAttributes) {
    [self setCustomAttributeWith:attribute];
  }

  // 4 
  [remoteStorage removeObjectForKey:RemoteStorageKeyPendingCustomAttributes];
}
 
- (void)setCustomAttributeWith:(NSDictionary<NSString *, id> *)keysAndValues {
  // 2
  for (NSString *key in keysAndValues) {
  // 3 
    [self setCustomAttributeWith:key andValue:[keysAndValues objectForKey:key]];
  }
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Atribuições do usuário %}

##### Salvando atribuições do usuário

Ao salvar atribuições do usuário, recomendamos a criação de um objeto personalizado para decifrar que tipo de atributo está sendo atualizado (`email`, `first_name`, `phone_number`, etc.). O objeto deve ser compatível com o armazenamento/recuperação em `UserDefaults`. Consulte o arquivo auxiliar `UserAttribute` para obter um exemplo de como fazer isso.

1. Inicialize um objeto `UserAttribute` codificado com o tipo correspondente
2. Inicialize `userDefaults` para recuperar e armazenar os dados do evento
3. Se houver um vetor existente, acrescente novos dados a ele e salve-o
4. Se não houver um vetor existente, salve o novo vetor em `userDefaults`

{% subtabs global %}
{% subtab Swift %}
``` swift 
func saveUserAttribute() {
  // 1 
  guard let data = try? PropertyListEncoder().encode(UserAttribute.userAttributeType("USER-ATTRIBUTE-VALUE")) else { return }
  
  // 2       
  let remoteStorage = RemoteStorage(storageType: .suite)
  
  // 3    
  if var pendingAttributes = remoteStorage.retrieve(forKey: .pendingUserAttributes) as? [Data] {
    pendingAttributes.append(contentsOf: [data])
    remoteStorage.store(pendingAttributes, forKey: .pendingUserAttributes)
  } else {
  // 4 
    remoteStorage.store([data], forKey: .pendingUserAttributes)
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)saveUserAttribute {
  // 1 
  UserAttribute *userAttribute = [[UserAttribute alloc] initWithUserField:@"USER-ATTRIBUTE-VALUE" attributeType:UserAttributeTypeEmail];
   
  NSError *error;
  NSData *data = [NSKeyedArchiver archivedDataWithRootObject:userAttribute requiringSecureCoding:YES error:&error];

  if (error != nil) {
    // log error
  }
  // 2  
  RemoteStorage *remoteStorage = [[RemoteStorage alloc] initWithStorageType:StorageTypeSuite];
  NSMutableArray *pendingAttributes = [[remoteStorage retrieveForKey:RemoteStorageKeyPendingUserAttributes] mutableCopy];
  
  // 3 
  if (pendingAttributes) {
    [pendingAttributes addObject:data];
    [remoteStorage store:pendingAttributes forKey:RemoteStorageKeyPendingUserAttributes];
  } else {
  // 4 
    [remoteStorage store:@[data] forKey:RemoteStorageKeyPendingUserAttributes];
  }
}
```
{% endsubtab %}
{% endsubtabs %}

##### Envio de atribuições do usuário para o Braze

O melhor momento para registrar qualquer análise de dados salva de uma extensão de app de conteúdo de notificação é logo após a inicialização do SDK. Isso pode ser feito percorrendo os atributos pendentes, definindo o atributo personalizado apropriado na Braze e, em seguida, limpando o armazenamento para a próxima vez que essa função for necessária.

1. Percorra o vetor de dados `pendingAttributes`
2. Inicializar um objeto `UserAttribute` codificado a partir de dados de atribuição
3. Defina um campo de usuário específico com base no tipo de atribuição do usuário (e-mail)
4. Remova todas as atribuições de usuário pendentes do armazenamento

{% subtabs global %}
{% subtab Swift %}
``` swift 
func logPendingUserAttributesIfNecessary() {
  let remoteStorage = RemoteStorage(storageType: .suite)
  guard let pendingAttributes = remoteStorage.retrieve(forKey: .pendingUserAttributes) as? [Data] else { return }
  
  // 1    
  for attributeData in pendingAttributes {
  // 2 
    guard let userAttribute = try? PropertyListDecoder().decode(UserAttribute.self, from: attributeData) else { continue }
    
  // 3    
    switch userAttribute {
    case .email(let email):
      user?.email = email
    }
  }
  // 4   
  remoteStorage.removeObject(forKey: .pendingUserAttributes)
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)logPendingUserAttributesIfNecessary {
  RemoteStorage *remoteStorage = [[RemoteStorage alloc] initWithStorageType:StorageTypeSuite];
  NSArray *pendingAttributes = [remoteStorage retrieveForKey:RemoteStorageKeyPendingUserAttributes];
  
  // 1  
  for (NSData *attributeData in pendingAttributes) {
    NSError *error;
  
  // 2 
    UserAttribute *userAttribute = [NSKeyedUnarchiver unarchivedObjectOfClass:[UserAttribute class] fromData:attributeData error:&error];

    if (error != nil) {
      // log error
    }
    
  // 3  
    if (userAttribute) {
      switch (userAttribute.attributeType) {
        case UserAttributeTypeEmail:
          [self user].email = userAttribute.userField;
          break;
      }
    }
  }
  // 4 
  [remoteStorage removeObjectForKey:RemoteStorageKeyPendingUserAttributes];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Arquivos auxiliares %}

##### Arquivos auxiliares

{% details Arquivo auxiliar RemoteStorage %}
{% subtabs global %}
{% subtab Swift %}
```swift
enum RemoteStorageKey: String, CaseIterable {
   
  // MARK: - Notification Content Extension Analytics
  case pendingCustomEvents = "pending_custom_events"
  case pendingCustomAttributes = "pending_custom_attributes"
  case pendingUserAttributes = "pending_user_attributes"
}
 
enum RemoteStorageType {
  case standard
  case suite
}
 
class RemoteStorage: NSObject {
  private var storageType: RemoteStorageType = .standard
  private lazy var defaults: UserDefaults = {
    switch storageType {
    case .standard:
      return .standard
    case .suite:
      return UserDefaults(suiteName: "YOUR-DOMAIN-IDENTIFIER")!
    }
  }()
   
  init(storageType: RemoteStorageType = .standard) {
    self.storageType = storageType
  }
   
  func store(_ value: Any, forKey key: RemoteStorageKey) {
    defaults.set(value, forKey: key.rawValue)
  }
   
  func retrieve(forKey key: RemoteStorageKey) -> Any? {
    return defaults.object(forKey: key.rawValue)
  }
   
  func removeObject(forKey key: RemoteStorageKey) {
    defaults.removeObject(forKey: key.rawValue)
  }
   
  func resetStorageKeys() {
    for key in RemoteStorageKey.allCases {
      defaults.removeObject(forKey: key.rawValue)
    }
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
@interface RemoteStorage ()
 
@property (nonatomic) StorageType storageType;
@property (nonatomic, strong) NSUserDefaults *defaults;
 
@end
 
@implementation RemoteStorage
 
- (id)initWithStorageType:(StorageType)storageType {
  if (self = [super init]) {
    self.storageType = storageType;
  }
  return self;
}
 
- (void)store:(id)value forKey:(RemoteStorageKey)key {
  [[self defaults] setValue:value forKey:[self rawValueForKey:key]];
}
 
- (id)retrieveForKey:(RemoteStorageKey)key {
  return [[self defaults] objectForKey:[self rawValueForKey:key]];
}
 
- (void)removeObjectForKey:(RemoteStorageKey)key {
  [[self defaults] removeObjectForKey:[self rawValueForKey:key]];
}
 
- (void)resetStorageKeys {
  [[self defaults] removeObjectForKey:[self rawValueForKey:RemoteStorageKeyPendingCustomEvents]];
  [[self defaults] removeObjectForKey:[self rawValueForKey:RemoteStorageKeyPendingCustomAttributes]];
  [[self defaults] removeObjectForKey:[self rawValueForKey:RemoteStorageKeyPendingUserAttributes]];
}
 
- (NSUserDefaults *)defaults {
  if (!self.defaults) {
    switch (self.storageType) {
      case StorageTypeStandard:
        return [NSUserDefaults standardUserDefaults];
        break;
      case StorageTypeSuite:
        return [[NSUserDefaults alloc] initWithSuiteName:@"YOUR-DOMAIN-IDENTIFIER"];
    }
  } else {
    return self.defaults;
  }
}
 
- (NSString*)rawValueForKey:(RemoteStorageKey)remoteStorageKey {
    switch(remoteStorageKey) {
    case RemoteStorageKeyPendingCustomEvents:
      return @"pending_custom_events";
    case RemoteStorageKeyPendingCustomAttributes:
      return @"pending_custom_attributes";
    case RemoteStorageKeyPendingUserAttributes:
      return @"pending_user_attributes";
    default:
      [NSException raise:NSGenericException format:@"Unexpected FormatType."];
  }
}
```
{% endsubtab %}
{% endsubtabs %}
{% enddetails %}
{% details Arquivo auxiliar UserAttribute %}
{% subtabs global %}
{% subtab Swift %}
```swift
enum UserAttribute: Hashable {
  case email(String?)
}
 
// MARK: - Codable
extension UserAttribute: Codable {
  private enum CodingKeys: String, CodingKey {
    case email
  }
   
  func encode(to encoder: Encoder) throws {
    var values = encoder.container(keyedBy: CodingKeys.self)
     
    switch self {
    case .email(let email):
      try values.encode(email, forKey: .email)
    }
  }
   
  init(from decoder: Decoder) throws {
    let values = try decoder.container(keyedBy: CodingKeys.self)
     
    let email = try values.decode(String.self, forKey: .email)
    self = .email(email)
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
@implementation UserAttribute
 
- (id)initWithUserField:(NSString *)userField attributeType:(UserAttributeType)attributeType {
  if (self = [super init]) {
    self.userField = userField;
    self.attributeType = attributeType;
  }
  return self;
}
 
- (void)encodeWithCoder:(NSCoder *)encoder {
  [encoder encodeObject:self.userField forKey:@"userField"];
  [encoder encodeInteger:self.attributeType forKey:@"attributeType"];
}
 
- (id)initWithCoder:(NSCoder *)decoder {
  if (self = [super init]) {
    self.userField = [decoder decodeObjectForKey:@"userField"];
     
    NSInteger attributeRawValue = [decoder decodeIntegerForKey:@"attributeType"];
    self.attributeType = (UserAttributeType) attributeRawValue;
  }
  return self;
}
 
@end
```
{% endsubtab %}
{% endsubtabs %}
{% enddetails %}
{% details Arquivo auxiliar do dicionário EventName %}
{% subtabs global %}
{% subtab Swift %}
```swift
extension Dictionary where Key == String, Value == Any {
  init(eventName: String, properties: [String: Any]? = nil) {
    self.init()
    self[PushNotificationKey.eventName.rawValue] = eventName
     
    if let properties = properties {
      for (key, value) in properties {
        self[key] = value
      }
    }
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
@implementation NSDictionary (Helper)
 
- (id)initWithEventName:(NSString *)eventName properties:(NSDictionary *)properties {
  self = [self init];
  if (self) {
    dict[@"event_name"] = eventName;
     
    for(id key in properties) {
      dict[key] = properties[key];
    }
  }
  return self;
}
 
@end
```
{% endsubtab %}
{% endsubtabs %}
{% enddetails %}
<br>
{% endtab %}
{% endtabs %}

