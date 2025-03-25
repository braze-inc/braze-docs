---
nav_title: Atividades ao vivo
article_title: Atividades ao vivo para iOS
platform: Swift
page_order: 1
description: "Este artigo aborda o uso da Braze para gerenciar seus tokens de atividades ao vivo para o Swift SDK."

---

# Atividades ao vivo

> As Live Activities são notificações persistentes e interativas exibidas na tela de bloqueio, permitindo que você fique de olho nas coisas em tempo real. Por serem exibidas na tela de bloqueio, as Live Activities garantem que suas notificações não sejam perdidas. Como são persistentes, você pode exibir conteúdo atualizado para seus usuários sem que eles precisem desbloquear o telefone. 

![Atividade ao vivo de um rastreador de entregas em uma tela de bloqueio do iPhone. Uma barra de status com um carro está quase totalmente preenchida. O texto diz "2 min until pickup" (2 minutos até a coleta)]({% image_buster /assets/img/swift/live_activities/example_2.png %}){: style="max-width:40%;float:right;margin-left:15px;"}

As Live Activities apresentam uma combinação de informações estáticas e dinâmicas que você atualiza. Por exemplo, você pode criar uma Live Activity que fornece um rastreador de status para uma entrega. Essa Live Activity teria o nome da sua empresa como informação estática, bem como um "Time to delivery" dinâmico que seria atualizado à medida que o motorista de entrega se aproximasse do destino.

Como desenvolvedor, você pode usar o Braze para gerenciar seus ciclos de vida do Live Activity, fazer chamadas para a API REST do Braze para fazer atualizações do Live Activity e fazer com que todos os dispositivos inscritos recebam a atualização o mais rápido possível. E, como você está gerenciando as Live Activity por meio da Braze, pode usá-las em conjunto com seus outros canais de mensagens – notificações por push, mensagens no app, cartões de conteúdo – para promover a adoção.

## Pré-requisitos 

{% sdk_min_versions swift:5.11.0 %}

Os pré-requisitos adicionais incluem:

- As Live Activities estão disponíveis apenas para iPhones e iPads com iOS 16.1 e posterior. Para usar esse recurso, seu projeto deve estar voltado para essa versão do iOS.
- O direito `Push Notification` deve ser adicionado em **Signing & Capabilities** (Assinatura e recursos) em seu projeto Xcode.
- As Live Activities exigem o uso de uma tecla `.p8` para enviar a notificação. Não há suporte para arquivos mais antigos, como `.p12` ou `.pem`.
- A partir da versão 8.2.0 do Braze Swift SDK, é possível [registrar remotamente uma Live Activity](#step-2-start-the-activity). Para usar esse recurso, é necessário o iOS 17.2 ou posterior.

{% alert note %}
Embora as Live Activities e as notificações por push sejam semelhantes, suas permissões de sistema são separadas. Por padrão, todos os recursos do Live Activity estão ativados, mas os usuários podem desativar esse recurso por aplicativo.
{% endalert %}

## Implementação de uma atividade ao vivo

### Etapa 1: Criar uma atividade

Primeiro, certifique-se de ter seguido o procedimento [Exibindo dados ao vivo com Live Activities](https://developer.apple.com/documentation/activitykit/displaying-live-data-with-live-activities) na documentação da Apple para configurar o Live Activities em seu aplicativo iOS. Como parte dessa tarefa, inclua `NSSupportsLiveActivities` definido como `YES` em `Info.plist`.

Como a natureza exata da sua Live Activity será específica para o seu caso de negócios, você precisará configurar e inicializar os objetos [Activity](https://developer.apple.com/documentation/activitykit/activityattributes). É importante ressaltar que você definirá:
* `ActivityAttributes`: Esse protocolo define o conteúdo estático (imutável) e dinâmico (mutável) que aparecerá em sua Live Activity.
* `ActivityAttributes.ContentState`: Esse tipo define os dados dinâmicos que serão atualizados no decorrer da atividade.

Você também usará o SwiftUI para criar a apresentação da interface do usuário da tela de bloqueio e do Dynamic Island nos dispositivos compatíveis. 

Certifique-se de que você esteja familiarizado com os [pré-requisitos e as limitações](https://developer.apple.com/documentation/activitykit/displaying-live-data-with-live-activities#Understand-constraints) da Apple para o Live Activities, pois essas restrições são independentes do Braze.

{% alert note %}
Se você espera enviar pushs frequentes para a mesma atividade ao vivo, pode evitar ser limitado pelo limite de orçamento da Apple definindo `NSSupportsLiveActivitiesFrequentUpdates` como `YES` no arquivo `Info.plist`. Para saber mais, consulte a seção [`Determine the update frequency`](https://developer.apple.com/documentation/activitykit/updating-and-ending-your-live-activity-with-activitykit-push-notifications#Determine-the-update-frequency) na documentação do ActivityKit.
{% endalert %}

#### Exemplo

Vamos imaginar que queremos criar uma Live Activity para fornecer aos nossos usuários atualizações sobre a série Superb Owl, em que dois resgates de animais selvagens concorrentes recebem pontos pelas corujas que têm em sua residência. Neste exemplo, criamos uma struct chamada `SportsActivityAttributes`, mas você pode usar sua própria implementação de `ActivityAttributes`.

```swift
#if canImport(ActivityKit)
  import ActivityKit
#endif

@available(iOS 16.1, *)
struct SportsActivityAttributes: ActivityAttributes {
  public struct ContentState: Codable, Hashable {
    var teamOneScore: Int
    var teamTwoScore: Int
  }

  var gameName: String
  var gameNumber: String
}
```

### Etapa 2: Iniciar a atividade

Primeiro, escolha como deseja registrar sua atividade:

- **Remotamente:** O mais cedo possível no ciclo de vida do aplicativo e do usuário (e antes que o token por push seja necessário), use o método [`registerPushToStart`](<http://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/liveactivities-swift.class/registerpushtostart(fortype:name:)>). Em seguida, inicie uma atividade usando o endpoint [`/messages/live_activity/start`]({{site.baseurl}}/api/endpoints/messaging/live_activity/start).
- **Localmente:** Crie uma instância de sua Live Activity e, em seguida, use o método [`launchActivity`](<https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/liveactivities-swift.class/launchactivity(pushtokentag:activity:fileid:line:)>) para criar tokens push para serem gerenciados pelo Braze.

{% tabs localização %}
{% tab remoto %}
{% alert important %}
Para registrar remotamente uma Live Activity, é necessário o iOS 17.2 ou posterior.
{% endalert %}

#### Etapa 2.1: Adicione o BrazeKit à sua extensão de widget

Em seu projeto do Xcode, selecione o nome do aplicativo e, em seguida, **General** (Geral). Em **Frameworks and Libraries (Estruturas e bibliotecas**), confirme se o endereço `BrazeKit` está listado.

![O framework BrazeKit em Frameworks e bibliotecas em um projeto de amostra do Xcode.]({% image_buster /assets/img/swift/live_activities/xcode_frameworks_and_libraries.png %})

#### Etapa 2.2: Adicionar o protocolo BrazeLiveActivityAttributes

Em sua implementação do `ActivityAttributes`, adicione a conformidade com o protocolo `BrazeLiveActivityAttributes` e, em seguida, adicione a string `brazeActivityId` ao seu modelo de atributos. Não é necessário atribuir um valor a essa string.

```swift
import BrazeKit

#if canImport(ActivityKit)
  import ActivityKit
#endif

@available(iOS 16.1, *)
struct SportsActivityAttributes: ActivityAttributes, BrazeLiveActivityAttributes {
  public struct ContentState: Codable, Hashable {
    var teamOneScore: Int
    var teamTwoScore: Int
  }

  var gameName: String
  var gameNumber: String
  var brazeActivityId: String?
}
```

#### Etapa 2.3: Registro para push-to-start

Em seguida, registre o tipo de Live Activity, para que a Braze possa rastrear todos os tokens push-to-start e instâncias de Live Activity associadas a esse tipo.

{% alert warning %}
O sistema operacional iOS gera tokens push-to-start somente durante a primeira instalação do aplicativo após a reinicialização do dispositivo. Para garantir que seus tokens sejam registrados de forma confiável, chame `registerPushToStart` no seu método `didFinishLaunchingWithOptions`.
{% endalert %}

###### Exemplo

No exemplo a seguir, a classe `LiveActivityManager` manipula objetos Live Activity. Em seguida, o método `registerPushToStart` registra `SportActivityAttributes`:

```swift
import BrazeKit

#if canImport(ActivityKit)
  import ActivityKit
#endif

class LiveActivityManager {

  @available(iOS 17.2, *)
  func registerActivityType() {
    // This method returns a Swift background task.
    // You may keep a reference to this task if you need to cancel it wherever appropriate, or ignore the return value if you wish.
    let pushToStartObserver: Task = Self.braze?.liveActivities.registerPushToStart(
      forType: Activity<SportsActivityAttributes>.self,
      name: "SportsActivityAttributes"
    )
  }

}
```

#### Etapa 2.4: Enviar uma notificação push-to-start

Enviar uma notificação push-to-start remota usando o endpoint [`/messages/live_activity/start`]({{site.baseurl}}/api/endpoints/messaging/live_activity/start).
{% endtab %}

{% tab localização %}
Você pode usar o [framework do ActivityKit da Apple](https://developer.apple.com/documentation/activitykit) para obter um token de envio, que o SDK da Braze pode gerenciar para você. Isso permite que você atualize as Live Activities por meio da API do Braze, pois o Braze enviará o token de push para o serviço de notificação por push da Apple (APNs) no back-end.

1. Crie uma instância de sua implementação do Live Activity usando as APIs do ActivityKit da Apple.
2. Defina o parâmetro `pushType` como `.token`. 
3. Passe as atividades ao vivo `ActivitiesAttributes` e `ContentState` que você definiu. 
4. Registre sua atividade na instância da Braze, passando-a para [`launchActivity(pushTokenTag:activity:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/liveactivities-swift.class). O parâmetro `pushTokenTag` é uma cadeia de caracteres personalizada que você define. Ele deve ser exclusivo para cada Live Activity que você criar.

Depois de registrar a atividade ao vivo, o SDK da Braze extrairá e observará as alterações nos tokens de envio.

#### Exemplo

Em nosso exemplo, criaremos uma classe chamada `LiveActivityManager` como uma interface para nossos objetos Live Activity. Em seguida, definiremos o endereço `pushTokenTag` como `"sports-game-2024-03-15"`.

```swift
import BrazeKit

#if canImport(ActivityKit)
  import ActivityKit
#endif

class LiveActivityManager {
  
  @available(iOS 16.2, *)
  func createActivity() {
    let activityAttributes = SportsActivityAttributes(gameName: "Superb Owl", gameNumber: "Game 1")
    let contentState = SportsActivityAttributes.ContentState(teamOneScore: "0", teamTwoScore: "0")
    let activityContent = ActivityContent(state: contentState, staleDate: nil)
    if let activity = try? Activity.request(attributes: activityAttributes,
                                            content: activityContent,
      // Setting your pushType as .token allows the Activity to generate push tokens for the server to watch.
                                            pushType: .token) {
      // Register your Live Activity with Braze using the pushTokenTag.
      // This method returns a Swift background task.
      // You may keep a reference to this task if you need to cancel it wherever appropriate, or ignore the return value if you wish.
      let liveActivityObserver: Task = AppDelegate.braze?.liveActivities.launchActivity(pushTokenTag: "sports-game-2024-03-15",
                                                                                        activity: activity)
    }
  }
  
}
```

O widget Live Activity exibiria esse conteúdo inicial para os usuários. 

![Uma atividade ao vivo em uma tela de bloqueio do iPhone com as pontuações de duas equipes. As equipes Wild Bird Fund e do Owl Rehab têm pontuações de 0.]({% image_buster /assets/img/swift/live_activities/example_1_1.png %}){: style="max-width:40%;"}
{% endtab %}
{% endtabs %}

### Etapa 3: Retomada do rastreamento de atividades

Para garantir que a Braze rastreie sua Live Activity na inicialização do aplicativo:

1. Abra seu arquivo `AppDelegate`.
2. Importe o módulo `ActivityKit` se ele estiver disponível.
3. Chame [`resumeActivities(ofType:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/liveactivities-swift.class/resumeactivities(oftype:)) em `application(_:didFinishLaunchingWithOptions:)` para todos os tipos de `ActivityAttributes` que você registrou no seu aplicativo.

Isso permite que o Braze retome as tarefas para rastrear atualizações de tokens push para todas as Live Activities ativas. Observe que, se um usuário tiver explicitamente descartado a Atividade ao vivo em seu dispositivo, ela será considerada removida e o Braze não a rastreará mais.

###### Exemplo

```swift
import UIKit
import BrazeKit

#if canImport(ActivityKit)
  import ActivityKit
#endif

@main
class AppDelegate: UIResponder, UIApplicationDelegate {

  static var braze: Braze? = nil

  func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
  ) -> Bool {
    
    if #available(iOS 16.1, *) {
      Self.braze?.liveActivities.resumeActivities(
        ofType: Activity<SportsActivityAttributes>.self
      )
    }

    return true
  }
}
```

### Etapa 4: Atualizar a atividade

![Uma atividade ao vivo em uma tela de bloqueio do iPhone com as pontuações de duas equipes. A equipe Wild Bird Fund tem 2 pontos, e o Owl Rehab tem 4 pontos.]({% image_buster /assets/img/swift/live_activities/example_1_2.png %}){: style="max-width:40%;float:right;margin-left:15px;"}

O endpoint [`/messages/live_activity/update`]({{site.baseurl}}/api/endpoints/messaging/live_activity/update) permite que você atualize uma Live Activity por meio de notificações push passadas pela REST API da Braze. Use esse endpoint para atualizar sua Live Activity `ContentState`.

Ao atualizar `ContentState`, o widget Live Activity exibirá as novas informações. Veja como será a série do Superb Owl no final do primeiro tempo.

Consulte nosso artigo sobre [endpoints em`/messages/live_activity/update` ]({{site.baseurl}}/api/endpoints/messaging/live_activity/update) para obter detalhes completos.

### Etapa 5: Encerrar a atividade

Quando uma Live Activity está ativa, ela é exibida na tela de bloqueio do usuário e no Dynamic Island. Há algumas maneiras diferentes de uma Live Activity terminar e ser removida da interface do usuário. 

* **Descarte pelo usuário**: Um usuário pode descartar manualmente uma Live Activity.
* **Tempo limite**: Após um tempo padrão de 8 horas, o iOS removerá a Live Activity da Dynamic Island do usuário. Após um tempo padrão de 12 horas, o iOS removerá a Live Activity da tela de bloqueio do usuário. 
* **Data de demissão**: Você pode fornecer uma data e hora para que uma Live Activity seja removida da interface do usuário antes do tempo limite. Isso é definido no `ActivityUIDismissalPolicy` da atividade ou usando o parâmetro `dismissal_date` em solicitações para o endpoint `/messages/live_activity/update`.
* **Encerramento da atividade**: Você pode definir `end_activity` como `true` em uma solicitação para o endpoint `/messages/live_activity/update` para encerrar imediatamente uma Live Activity.

Consulte nosso artigo sobre [endpoints em`/messages/live_activity/update` ]({{site.baseurl}}/api/endpoints/messaging/live_activity/update) para obter detalhes completos.

## Solução de problemas

Para obter mais detalhes sobre solução de problemas ou perguntas frequentes, consulte nossas Perguntas [frequentes]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/live_activities/faq/).

