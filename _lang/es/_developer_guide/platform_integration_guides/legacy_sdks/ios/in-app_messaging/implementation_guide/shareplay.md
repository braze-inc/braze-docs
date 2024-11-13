---
nav_title: SharePlay
article_title: Guía de implementación de mensajes dentro de la aplicación SharePlay
platform: iOS
page_order: 1
description: "Esta guía de implementación avanzada de SharePlay amplía el caso de uso de video proporcionado en la guía de implementación avanzada de mensajes dentro de la aplicación. SharePlay es una característica recién lanzada que habilita a los usuarios de FaceTime de iOS 15 a tener una experiencia multimedia compartida en todos sus dispositivos, ofreciendo sincronización de audio y video en tiempo real."
channel:
  - in-app messages
alias: /shareplay/

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Guía de implementación de mensajes dentro de la aplicación SharePlay

> SharePlay es una característica recién lanzada que habilita a los usuarios de FaceTime de iOS 15 a tener una experiencia multimedia compartida en todos sus dispositivos, ofreciendo sincronización de audio y video en tiempo real. SharePlay es una forma estupenda de que los usuarios experimenten el contenido con amigos y familiares, ofreciendo a los clientes de Braze una vía adicional para el contenido de video y oportunidades para presentar tu aplicación a nuevos usuarios.

![SharePlay]({% image_buster /assets/img/shareplay/shareplay6.png %}){: style="border:0;margin-top:10px;"}
## Resumen

El nuevo framework `GroupActivities` que lanzó Apple como parte de la actualización de iOS 15 te permite aprovechar FaceTime integrando SharePlay en tus aplicaciones con la ayuda de los mensajes dentro de la aplicación de Braze.
![SharePlay]({% image_buster /assets/img/shareplay/shareplay3.png %}){: style="float:right;max-width:30%;margin-left:15px;margin-top:10px;"}

Cuando los usuarios inicien un video SharePlay en una llamada FaceTime, aparecerá un botón "Abrir" en la parte superior de la pantalla de todos. Cuando se abra, el audio y el video se sincronizarán en todos los dispositivos compatibles, permitiendo a los usuarios ver videos juntos en tiempo real. Los que no tengan la aplicación descargada serán redirigidos a la App Store.

**Reproducción multimedia sincronizada**<br>
Con la reproducción multimedia sincronizada, si una persona pausa el video de SharePlay, se pausará en todos los dispositivos. <br><br>
![SharePlay]({% image_buster /assets/img/shareplay/shareplay7.png %}){: style="border:0"}

## Integración

El mensaje dentro de la aplicación utilizado en esta integración es un controlador de vista de mensaje modal dentro de la aplicación subclaseado. Encontrarás una guía de configuración en [la guía de implementación de]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/implementation_guide/) casos de uso avanzados de mensajes dentro de la aplicación de iOS. Antes de la integración, asegúrate de añadir el derecho `GroupActivities` a tu proyecto de Xcode.

{% alert important %}
Recomendamos abrir la [documentación de Apple SharePlay](https://developer.apple.com/documentation/avfoundation/media_playback_and_selection/supporting_coordinated_media_playback) junto a esta guía para completar la integración.
{% endalert %}

### Paso 1: Sustitución y carga de XIB

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

### Paso 2: Configurar AVPlayer para mensajes dentro de la aplicación

Los mensajes dentro de la aplicación pueden reproducir videos de forma nativa con un ligero trabajo de desarrollo. Al hacerlo, tendrás acceso a todas las funciones de `AVPlayerVideoController`, como SharePlay. El mensaje dentro de la aplicación utilizado para este ejemplo es una subclase de `ABKInAppMessageModalViewController` que tiene una vista personalizada para incrustar un reproductor de video nativo.

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

#### Configuración del panel de control

**Pares clave-valor**: El archivo de vídeo debe establecerse en los pares clave-valor del mensaje dentro de la aplicación y no puede adjuntarse al propio elemento multimedia. También puedes añadir la comprobación de validez de la URL en `beforeInAppMesageDisplayed` como barrera antes de mostrar el contenido.

**Desencadenamiento**: El mensaje dentro de la aplicación debe ser elegible para todos los usuarios que tengan habilitada la reelegibilidad. Esto se puede hacer estableciendo dos desencadenantes: uno predeterminado para lanzar el mensaje y otro para lanzar el mensaje cuando se inicie desde SharePlay. Los usuarios que no usen iOS 15 solo podrán ver los mensajes localmente. 

{% alert important %}
Ten en cuenta cualquier otro mensaje dentro de la aplicación desencadenado al iniciar la sesión que pueda entrar en conflicto entre sí.
{% endalert %}

### Paso 3: Crear actividad de observación en grupo

Crea un objeto conforme al protocolo `GroupActivity`. El objeto serán los metadatos del `GroupSession` compartidos a lo largo del ciclo de vida de SharePlay. 

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

#### Prepárate para jugar

Cuando te preparas para reproducir el elemento multimedia, cada actividad de grupo tiene tres estados de `prepareForActivation()`:
- `.activationDisabled` - ver individualmente
- `.activationPreferred` - visualización conjunta
- `.cancelled` - ignorar y manejar con elegancia

Cuando el estado vuelva a ser `activationPreferred`, esa será tu señal para activar el resto del ciclo de vida de la actividad de grupo. 

![SharePlay]({% image_buster /assets/img/shareplay/shareplay.png %}){: style="border:0;"}

### Paso 4: Lanzar mensaje dentro de la aplicación desde la API de SharePlay

La API `GroupActivities` determina si hay un video presente. Si es así, debes desencadenar el evento personalizado para lanzar tu mensaje dentro de la aplicación apto para SharePlay. El `CoordinationManager` es responsable de los cambios de estado de SharePlay, como si el usuario o usuarios abandonan la llamada o se unen a ella. 

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

### Paso 5: Abandonar una sesión de grupo en la salida de mensajes dentro de la aplicación

Cuando se descarta el mensaje dentro de la aplicación es el momento apropiado para abandonar la sesión de SharePlay y descartar el objeto de sesión.

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

### Configurar la visibilidad del botón SharePlay

Es una buena práctica ocultar o mostrar dinámicamente cualquier indicador de SharePlay. Utiliza la variable `isEligibleForGroupSession` para observar si el usuario está actualmente en una llamada FaceTime o no. Si se encuentran en una llamada FaceTime, debe aparecer un botón para compartir el video entre los dispositivos compatibles en el chat. La primera vez que el usuario inicie SharePlay, aparecerá un aviso en el dispositivo original para seleccionar las opciones. A continuación, en los dispositivos de los usuarios compartidos aparecerá una solicitud de interacción con el contenido.

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

