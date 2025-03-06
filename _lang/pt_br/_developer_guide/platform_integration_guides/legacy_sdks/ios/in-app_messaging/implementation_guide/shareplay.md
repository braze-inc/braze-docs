---
nav_title: SharePlay
article_title: Guia avançado de implementação de mensagens no app – SharePlay
platform: iOS
page_order: 1
description: "Este guia avançado de implementação do SharePlay expande o caso de uso de vídeos apresentado no guia avançado de implementação de mensagens no app. O SharePlay é um recurso recém-lançado no iOS 15, que proporciona aos usuários do FaceTime uma experiência de compartilhamento de mídias entre seus dispositivos, com sincronização de áudio e vídeo em tempo real."
channel:
  - in-app messages
alias: /shareplay/

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Guia de implementação de mensagem no app do SharePlay

> O SharePlay é um recurso recém-lançado no iOS 15, que proporciona aos usuários do FaceTime uma experiência de compartilhamento de mídias entre seus dispositivos, com sincronização de áudio e vídeo em tempo real. SharePlay é uma ótima maneira para os usuários experimentarem conteúdo com amigos e familiares, oferecendo aos clientes da Braze uma via adicional para conteúdo de vídeo e oportunidades para apresentar novos usuários ao seu aplicativo.

![SharePlay]({% image_buster /assets/img/shareplay/shareplay6.png %}){: style="border:0;margin-top:10px;"}
## Visão geral

O novo framework `GroupActivities` lançado pela Apple como parte da atualização do iOS 15 permite que você aproveite o FaceTime integrando o SharePlay em seus apps com a ajuda de mensagens no app da Braze.
![SharePlay]({% image_buster /assets/img/shareplay/shareplay3.png %}){: style="float:right;max-width:30%;margin-left:15px;margin-top:10px;"}

Quando os usuários iniciam um vídeo do SharePlay em uma chamada FaceTime, um botão "Abrir" aparecerá no topo da tela de todos. Quando aberto, áudio e vídeo serão sincronizados em todos os dispositivos compatíveis, permitindo que os usuários assistam a vídeos juntos em tempo real. Aqueles que não tiverem o app baixado serão redirecionados para a App Store.

**Reprodução de Mídia Sincronizada**<br>
Com a reprodução da mídia sincronizada, se uma pessoa pausar o vídeo do SharePlay, ele será pausado em todos os dispositivos. <br><br>
![SharePlay]({% image_buster /assets/img/shareplay/shareplay7.png %}){: style="border:0"}

## Integração

A mensagem no app usada nesta integração é um controlador modal de subclasse de visualização de mensagens no app. Consulte instruções de configuração no [guia de implementação]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/implementation_guide/), na seção sobre o caso de uso avançado de mensagens no app do iOS. Antes de fazer a integração, dê permissão para `GroupActivities` no seu projeto do Xcode.

{% alert important %}
Recomendamos abrir a [documentação do Apple SharePlay](https://developer.apple.com/documentation/avfoundation/media_playback_and_selection/supporting_coordinated_media_playback) lado a lado com este guia para concluir a integração.
{% endalert %}

### Etapa 1: Substituição e carregamento do XIB

{% tabs %}
{% tab Swift %}
```swift
override var nibName: String {
  return "ModalVideoViewController"
}
   
/// Overriding loadView() from ABKInAppMessageModalViewController to provide our own view for the in-app message
override func loadView() {
  Bundle.main.loadNibNamed(nibName, owner: self, options: nil)
}
```
{% endtab %}
{% endtabs %}

### Etapa 2: Configurar AVPlayer para mensagens no app

As mensagens no app podem reproduzir vídeos de forma nativa utilizando algumas linhas de código. Ao fazer isso, você tem acesso a todos os recursos do `AVPlayerVideoController`, como o SharePlay. A mensagem no app usada para este exemplo é uma subclasse `ABKInAppMessageModalViewController` que tem uma visualização personalizada para incorporar um reprodutor de vídeo nativo.

{% tabs %}
{% tab Swift %}
```swift
func configureVideoPlayer() {
  guard let urlString = inAppMessage.extras?["video_url"] as? String,
        let url = URL(string: urlString) else { return }
     
  let videoTitle = inAppMessage.extras?["video_title"] as? String
  mediaItem = MediaItem(title: videoTitle ?? "Video Content", url: url)
     
  let asset = AVAsset(url: url)
  let playerItem = AVPlayerItem(asset: asset)
  player.replaceCurrentItem(with: playerItem)
  playerViewController.player = player
   
  addChild(playerViewController)
  videoPlayerContainer.addSubview(playerViewController.view)
  playerViewController.didMove(toParent: self)
}
```
{% endtab %}
{% endtabs %}

#### Configuração do dashboard

**Pares de chave/valor:** O arquivo de vídeo deve ser configurado nos pares de chave-valor na mensagem no app e não pode ser anexado ao item de mídia em si. Você também pode adicionar a verificação de validade de URL em `beforeInAppMesageDisplayed` como um verificador de integridade antes de exibir o conteúdo.

**Disparo:** A mensagem no app deve ser elegível para todos os usuários com re-eligibilidade ativada. Isso pode ser feito configurando dois gatilhos: um gatilho padrão para disparar a mensagem, e outro para disparar a mensagem quando iniciada pelo SharePlay. Usuários de versões anteriores ao iOS 15 apenas visualizarão as mensagens. 

{% alert important %}
Esteja atento a quaisquer outras mensagens no app acionadas no início da sessão que possam entrar em conflito umas com as outras.
{% endalert %}

### Etapa 3: Criar atividade de assistir em grupo

Crie um objeto que esteja em conformidade com o protocolo `GroupActivity`. O objeto será os metadados do `GroupSession` compartilhados ao longo do ciclo de vida do SharePlay. 

{% tabs %}
{% tab Swift %}
```swift
struct MediaItem: Hashable, Codable {
  let title: String
  let url: URL
}
 
@available(iOS 15, *)
struct MediaItemActivity: GroupActivity {
  static let activityIdentifier = "com.book-demo.GroupWatching"
 
  let mediaItem: MediaItem
   
  var metadata: GroupActivityMetadata {
    var metadata = GroupActivityMetadata()
    metadata.type = .watchTogether
    metadata.title = mediaItem.title
    metadata.fallbackURL = mediaItem.url
    return metadata
  }
}
```
{% endtab %}
{% endtabs %}

#### Preparação para a reprodução

Na preparação para reproduzir o item de mídia, cada atividade em grupo tem três estados de `prepareForActivation()`:
- `.activationDisabled` - visualizando individualmente
- `.activationPreferred` - assistindo juntos
- `.cancelled` - ignorar e prosseguir com naturalidade

Quando o estado voltar como `activationPreferred`, esse é o seu sinal para ativar o restante do ciclo de vida da atividade em grupo. 

![SharePlay]({% image_buster /assets/img/shareplay/shareplay.png %}){: style="border:0;"}

### Etapa 4: Abrir a mensagem no app a partir da API do SharePlay

A API `GroupActivities` determina se há um vídeo. Se for o caso, você deve disparar o evento personalizado para lançar sua mensagem no app compatível com SharePlay. O componente `CoordinationManager` é responsável pelas mudanças de estado do SharePlay, por exemplo, a entrada e a saída de usuários na chamada. 

{% tabs %}
{% tab Swift %}
```swift
private var subscriptions = Set<AnyCancellable>()  
private var selectedMediaItem: MediaItem? {
  didSet {
    // Ensure the UI selection always represents the currently playing media.
    guard let _ = selectedMediaItem else { return }
 
    if !BrazeManager.shared.inAppMessageCurrentlyVisible {
      BrazeManager.shared.logCustomEvent("SharePlay Event")
    }
  }
}  
 
private func launchVideoPlayerIfNecessary() {
  CoordinationManager.shared.$enqueuedMediaItem
      .receive(on: DispatchQueue.main)
      .compactMap { $0 }
      .assign(to: \.selectedMediaItem, on: self)
      .store(in: &subscriptions)
}
```
{% endtab %}
{% endtabs %}

### Etapa 5: Saída de uma sessão em grupo ao dispensar uma mensagem no app

A dispensa de uma mensagem no app é um bom momento para sair da sessão do SharePlay e descartar o objeto da sessão.

{% tabs %}
{% tab Swift %}
```swift
override func viewDidDisappear(_ animated: Bool) {
  super.viewDidDisappear(animated)
  groupSession?.leave()
  CoordinationManager.shared.leave()
}
 
class CoordinationManager() {
...
  // Published values that the player, and other UI items, observe.
  @Published var enqueuedMediaItem: MediaItem?
  @Published var groupSession: GroupSession<MediaItemActivity>?
 
  // Clear activity when the user leaves
  func leave() {
    groupSession = nil
    enqueuedMediaItem = nil
  }
...
}
```
{% endtab %}
{% endtabs %}

### Configurar a visibilidade do botão SharePlay

É uma prática recomendada ocultar ou exibir dinamicamente qualquer indicador do SharePlay. Use a variável `isEligibleForGroupSession` para observar se o usuário está em uma chamada FaceTime ou não. Se eles estiverem em uma chamada FaceTime, um botão deve estar visível para compartilhar o vídeo entre os dispositivos compatíveis no chat. Na primeira vez que o usuário iniciar o SharePlay, um prompt aparecerá no dispositivo original solicitando a seleção das opções. Um prompt subsequente aparecerá então nos dispositivos dos usuários compartilhados para se engajar no conteúdo.

{% tabs %}
{% tab Swift %}
```swift
private var isEligibleForSharePlay: Bool = false {
  didSet {
    sharePlayButton.isHidden = !isEligibleForSharePlay
  }
}
 
override func viewDidLoad() {
  super.viewDidLoad()
 
  // SharePlay button eligibility
  groupStateObserver.$isEligibleForGroupSession
    .receive(on: DispatchQueue.main)
    .assign(to: \.isEligibleForSharePlay, on: self)
    .store(in: &subscriptions)
}
``` 
{% endtab %}
{% endtabs %}

