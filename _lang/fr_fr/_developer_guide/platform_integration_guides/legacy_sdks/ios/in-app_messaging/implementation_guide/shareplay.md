---
nav_title: SharePlay
article_title: Guide d’implémentation des messages in-app SharePlay
platform: iOS
page_order: 1
description: "Ce guide d’implémentation avancée de SharePlay traite le cas d’utilisation vidéo fourni dans le guide d’implémentation avancée des messages in-app. SharePlay est une nouvelle fonctionnalité qui permet aux utilisateurs de l’iOS 15 FaceTime de bénéficier d’une expérience multimédia partagée sur leurs appareils, offrant ainsi une synchronisation audio et vidéo en temps réel."
channel:
  - in-app messages
alias: /shareplay/

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Guide d’implémentation des messages in-app SharePlay

> SharePlay est une nouvelle fonctionnalité qui permet aux utilisateurs de l’iOS 15 FaceTime de bénéficier d’une expérience multimédia partagée sur leurs appareils, offrant ainsi une synchronisation audio et vidéo en temps réel. SharePlay est un excellent moyen pour les utilisateurs de partager du contenu avec leurs amis et leur famille, offrant aux clients Braze une possibilité supplémentaire pour le contenu vidéo et des opportunités de présenter votre application à de nouveaux utilisateurs.

![SharePlay]({% image_buster /assets/img/shareplay/shareplay6.png %}){: style="border:0;margin-top:10px;"}
## Aperçu

La nouvelle infrastructure `GroupActivities` publiée par Apple dans le cadre de la mise à jour iOS 15 vous permet de tirer profit de FaceTime en intégrant SharePlay dans vos applications avec l’aide des messages in-app Braze.
SharePlay![(]){: style="float:right;max-width:30%;margin-left:15px;margin-top:10px;"}

Lorsque les utilisateurs lancent une vidéo SharePlay dans un appel FaceTime, un bouton « Open » (Ouvrir) apparaît en haut de l’écran de tout le monde. Une fois ouvert, l'audio et la vidéo seront synchronisés sur tous les appareils compatibles, ce qui permettra aux utilisateurs de regarder des vidéos ensemble en temps réel. Les personnes qui n’ont pas téléchargé l’application seront redirigées vers l’App Store.

**Lecture de médias synchronisés**<br>
Avec la lecture multimédia synchronisée, si une personne interrompt la vidéo SharePlay, elle sera interrompue sur tous les appareils. <br><br>
![SharePlay]({% image_buster /assets/img/shareplay/shareplay7.png %}){: style="border:0"}

## Intégration

Le message in-app utilisé dans cette intégration est un contrôleur de visualisation modal de messages in-app sous-classé. Un guide de configuration est disponible dans le [guide d’implémentation]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/implementation_guide/) du cas d’utilisation avancé du message in-app iOS. Avant d’intégrer, assurez-vous d’ajouter le droit d’utilisation `GroupActivities` à votre projet Xcode.

{% alert important %}
Nous vous recommandons d'ouvrir la [documentation Apple SharePlay](https://developer.apple.com/documentation/avfoundation/media_playback_and_selection/supporting_coordinated_media_playback) côte à côte avec ce guide pour réaliser l'intégration.
{% endalert %}

### Étape 1 : Remplacer et charger XIB

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

### Étape 2 : Configurer AVPlayer pour les messages in-app

Les messages in-app peuvent lire des vidéos nativement avec un léger travail de développeur. En faisant cela, vous avez accès à toutes les fonctionnalités `AVPlayerVideoController`, comme SharePlay. Le message in-app utilisé pour cet exemple est un `ABKInAppMessageModalViewController` sous-classé qui a un affichage personnalisé pour intégrer un lecteur vidéo natif.

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

#### Configuration du tableau de bord

**Paires clé-valeur**: Le fichier vidéo doit être défini dans les paires clé-valeur sur le message in-app et ne peut pas être attaché à l’élément média lui-même. Vous pouvez également ajouter une vérification de validité d’URL dans `beforeInAppMesageDisplayed` comme sécurité avant d’afficher le contenu.

**Déclenchement**: Le message in-app doit être éligible pour tous les utilisateurs ayant une rééligibilité activée. Cela peut être fait en définissant deux déclencheurs, un déclencheur par défaut pour lancer le message et un autre pour lancer le message lorsqu’il est lancé à partir de SharePlay. Les utilisateurs ne disposant pas d’iOS 15 ne pourront afficher les messages que localement. 

{% alert important %}
Tenez compte de tous les autres messages in-app déclenchés au démarrage de la session qui peuvent entrer en conflit les uns avec les autres.
{% endalert %}

### Étape 3 : Créer une activité d’observation de groupe

Créez un objet conforme au protocole `GroupActivity`. L’objet sera les métadonnées du `GroupSession` partagé tout au long du cycle de vie SharePlay. 

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

#### Préparez-vous à lire

Lorsque vous préparez à lire l’élément média, chaque activité de groupe a trois états `prepareForActivation()` :
- `.activationDisabled` - affichage individuel
- `.activationPreferred` - affichage partagé
- `.cancelled` - ignorer et manipuler avec élégance

Lorsque l’état revient en tant que `activationPreferred`, c’est votre signal pour activer le reste du cycle de vie de l’activité de groupe. 

![SharePlay]({% image_buster /assets/img/shareplay/shareplay.png %}){: style="border:0;"}

### Étape 4 : Lancer le message in-app de l’API SharePlay

L’API `GroupActivities` détermine s’il existe une vidéo. Si c’est le cas, vous devez déclencher l’événement personnalisé pour lancer votre message in-app SharePlay. Le `CoordinationManager` est responsable des changements d’état de SharePlay, par exemple si le ou les utilisateurs quittent ou rejoignent l’appel. 

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

### Étape 5 : Quitter une session de groupe après rejet du message in-app

Lorsque le message in-app est rejeté, il est temps de quitter la session SharePlay et d’ignorer l’objet de session.

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

### Configurer la visibilité des boutons SharePlay

Il est recommandé de masquer ou démasquer dynamiquement tout indicateur SharePlay. Utilisez la variable `isEligibleForGroupSession` pour observer si l’utilisateur est actuellement en appel FaceTime ou non. S’ils sont en appel FaceTime, un bouton doit être visible pour partager la vidéo sur les appareils compatibles dans le chat. La première fois que l’utilisateur lance SharePlay, une invite apparaîtra sur l’appareil d’origine pour sélectionner les options. Une invite ultérieure apparaîtra alors sur les appareils des autres utilisateurs pour accéder au contenu partagé.

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

