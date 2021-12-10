---
nav_title: PartagerPlay
article_title: Guide d'implémentation de messages dans l'application SharePlay
platform: iOS
page_order: 1
description: "Ce guide de mise en œuvre avancé de SharePlay se développe sur le cas d'utilisation vidéo fourni dans le guide de mise en œuvre avancée des messages dans l'application. SharePlay est une nouvelle fonctionnalité qui permet aux utilisateurs de Facetime iOS 15 d'avoir une expérience multimédia partagée sur leurs appareils, offrant une synchronisation audio et vidéo en temps réel."
channel:
  - messages intégrés à l'application
alias: /fr/shareplay/
---

# Guide d'implémentation des messages dans l'application SharePlay

> SharePlay est une nouvelle fonctionnalité qui permet aux utilisateurs de Facetime iOS 15 d'avoir une expérience multimédia partagée sur leurs appareils, offrant une synchronisation audio et vidéo en temps réel. SharePlay est un excellent moyen pour les utilisateurs de découvrir du contenu avec leurs amis et leur famille, en offrant aux clients de Braze une avenue supplémentaire pour le contenu vidéo et des possibilités de présenter de nouveaux utilisateurs à votre application.

!\[SharePlay\]\[6\]{: style="border:0;margin-top:10px;"}
## Aperçu

Le nouveau framework `GroupActivities` publié par Apple dans le cadre de la mise à jour iOS 15 vous permet de tirer parti de FaceTime en intégrant SharePlay dans vos applications avec l'aide de messages intégrés à Braze. !\[SharePlay\]\[3\]{: style="float:right;max-width:30%;margin-left:15px;margin-top:10px;"}

Lorsque les utilisateurs lancent une vidéo SharePlay lors d'un appel Facetime, un bouton "Ouvrir" apparaît en haut de l'écran de chacun. Une fois ouvert, l'audio et la vidéo seront synchronisés sur tous les appareils compatibles, permettant aux utilisateurs de regarder des vidéos ensemble en temps réel. Ceux qui n'ont pas l'application téléchargée seront redirigés vers l'App Store.

__Lecture multimédia synchronisée__<br> Avec lecture de médias synchronisés, si une personne met en pause la vidéo SharePlay, elle sera mise en pause sur tous les appareils. <br><br> !\[SharePlay\]\[5\]{: style="border:0"}

## Intégration

Le message dans l'application utilisé dans cette intégration est un contrôleur de vue de messages dans l'application modale sous-classé. Un guide de configuration peut être trouvé dans le message de message avancé iOS dans le cas d'utilisation avancée [guide d'implémentation]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/implementation_guide/). Avant d’intégrer, assurez-vous d’ajouter le droit `GroupActivities` à votre projet Xcode.

{% alert important %}
Nous vous recommandons d'ouvrir la documentation [Apple SharePlay](https://developer.apple.com/documentation/avfoundation/media_playback_and_selection/supporting_coordinated_media_playback) côte à côte par ce guide pour compléter l'intégration.
{% endalert %}

### Étape 1 : Surcharger et charger XIB

{% tabs %}
{% tab Swift %}
```swift
override var nibName: String {
  return "ModalVideoViewController"
}

/// Overriding loadView() from ABKInAppMessageModalViewController to provide our own view for the In-App Message
override func loadView() {
  Bundle. ain.loadNibNamed(nibName, propriétaire: self, options: nil)
}
```
{% endtab %}
{% endtabs %}

### Étape 2 : Configurer AVPlayer pour les messages intégrés à l'application

Les messages intégrés peuvent lire des vidéos en natif avec un travail de développement léger. En faisant cela, vous avez accès à toutes les fonctionnalités de `AVPlayerVideoController` telles que SharePlay. Le message dans l'application utilisé pour cet exemple est un `ABKInAppMessageModalViewController` sous-classé qui a une vue personnalisée pour intégrer un lecteur vidéo natif.

{% tabs %}
{% tab Swift %}
```swift
func configureVideoPlayer() {
  garde laisser urlString = inAppMessage.extras?["video_url"] comme? String,
        let url = URL(string: urlString) sinon { return }

  let videoTitle = inAppMessage.extras?["video_title"] comme? String
  mediaItem = MediaItem(title: videoTitle ?? "Contenu vidéo", url: url)

  let asset = AVAsset(url: url)
  let playerItem = AVPlayerItem(asset: asset)
  player. eplaceCurrentItem(avec: playerItem)
  playerViewController. layer = joueur

  addChild(playerViewController)
  videoPlayerContainer.addSubview(playerViewController.view)
  playerViewController.didMove(toParent: self)
}
```
{% endtab %}
{% endtabs %}

#### Configuration du tableau de bord

__Paires clé-valeur__: le fichier vidéo doit être défini dans les paires clé-valeur sur le message in-app et ne peut pas être attaché au média lui-même. Vous pouvez également ajouter la vérification de la validité des URL dans `beforeInAppMesageDisplayed` en tant que guardrail avant d'afficher le contenu.

__Déclenchement__: le message dans l'application doit être éligible pour tous les utilisateurs avec rééligibilité activée. Cela peut être fait en définissant deux déclencheurs, un déclencheur par défaut pour lancer le message et un autre pour lancer le message lorsqu'il est lancé à partir de SharePlay. Les utilisateurs qui ne sont pas sur iOS 15 ne pourront voir que les messages localement.

{% alert important %}
Soyez attentif à tous les autres messages dans l'application déclenchés au démarrage de la session qui peuvent entrer en conflit les uns avec les autres.
{% endalert %}

### Étape 3 : Créer une activité de surveillance de groupe

Crée un objet qui est conforme au protocole `GroupActivity`. L'objet sera les métadonnées de la `session de groupe` partagées tout au long du cycle de vie de SharePlay.

{% tabs %}
{% tab Swift %}
```swift
struct MediaItem: Hashable, Codable {
  let title: String
  let url: URL
}

@available(iOS 15, *)
struct MediaItemActivity: GroupActivity {
  static let activityIdentifier = "com. ook-demo. roupWatching"

  let mediaItem: MediaItem

  var metadata: GroupActivityMetadata {
    var metadata = GroupActivityMetadata()
    metadata. ype = .watchTogether
    metadata.title = mediaItem.title
    métadonnées. allbackURL = mediaItem.url
    métadonnées de retour
  }
}
```
{% endtab %}
{% endtabs %}

#### Préparez-vous à jouer

Lorsque vous vous apprêtez à lire l'élément média, chaque activité de groupe a trois états de `prepareForActivation()`:
- `.activationdisable` - visualisation individuelle
- `.activationPreferred` - visualisation ensemble
- `.cancelled` - ignorez et gérez gracieusement

Lorsque l'état revient en tant que `activationPreferred`, c'est votre cue pour activer le reste du cycle de vie de l'activité du groupe.

!\[SharePlay\]\[1\]{: style="border:0;"}

### Étape 4 : Lancez le message dans l'application depuis l'API SharePlay

L'API `GroupActivities` détermine s'il y a une vidéo présente. Si c'est le cas, vous devriez déclencher l'événement personnalisé pour lancer votre message SharePlay-able dans l'application. Le `CoordinationManager` est responsable des changements d'état de SharePlay, par exemple si le ou les utilisateurs quittent ou rejoignent l'appel.

{% tabs %}
{% tab Swift %}
```swift
private var subscriptions = Set<AnyCancellable>()  
private var selectedMediaItem: MediaItem? {
  didSet {
    // Assurez-vous que la sélection de l'interface utilisateur représente toujours le média en cours de lecture.
    garde let _ = selectedMediaItem else { return }

    if !BrazeManager.shared.inAppMessageCurrentlyVisible {
      BrazeManager.shared. ogCustomEvent("Événement SharePlay")
    }
  }
}  

func privé launchVideoPlayerIfNecessary() {
  CoordinationManager. partagé.$enqueuedMediaItem
      .receive(on: DispatchQueue. ain)
      .compactMap { $0 }
      . ssign(à: \.selectedMediaItem, sur: self)
      .store(dans: &abonnements)
}
```
{% endtab %}
{% endtabs %}

### Étape 5 : Quitter une session de groupe lors du rejet d'un message dans l'application

Lorsque le message dans l'application est rejeté, il est temps de quitter la session SharePlay et de supprimer l'objet de session.

{% tabs %}
{% tab Swift %}
```swift
override func viewDidDisappear(_ animé: Bool) {
  super.viewDidDisappear(animé)
  groupSession?.leave()
  CoordinationManager.shared.leave()
}

class CoordinationManager() {
...
  // Valeurs publiées que le lecteur, et d'autres éléments de l'interface, observent.
  @Published var enqueuedMediaItem: MediaItem?
  @Published var groupSession: GroupSession<MediaItemActivity>?

  // Efface l'activité lorsque l'utilisateur quitte
  func leave() {
    groupSession = nil
    queuedMediaItem = nil
  }
...
}
```
{% endtab %}
{% endtabs %}

### Configurer la visibilité des boutons SharePlay

Il est préférable de masquer ou d'afficher dynamiquement un indicateur SharePlay. Utilisez la variable `isEligibleForGroupSession` pour observer si l'utilisateur est actuellement sur un appel FaceTime ou non. S'ils se trouvent sur un appel FaceTime, un bouton devrait être visible pour partager la vidéo sur les appareils compatibles dans le chat. La première fois que l'utilisateur lance SharePlay, une invite apparaît sur le périphérique d'origine pour sélectionner les options. Une invite subséquente apparaîtra ensuite sur les périphériques des utilisateurs partagés pour s'engager dans le contenu.

{% tabs %}
{% tab Swift %}
```swift
private var isEligibleForSharePlay: Bool = false {
  didSet {
    sharePlayButton. sHidden = !isEligibleForSharePlay
  }
}

surcharge func viewDidLoad() {
  super. iewDidLoad()

  // bouton SharePlay éligibilité
  groupStateObserver.$isEligibleForGroupSession
    .receive(on: DispatchQueue. ain)
    .assign(à : \.isEligibleForSharePlay, sur: self)
    .store(dans: &abonnements)
}
```
{% endtab %}
{% endtabs %}
[1]: {% image_buster /assets/img/shareplay/shareplay.png %} [2]: {% image_buster /assets/img/shareplay/shareplay2.png %} [3]: {% image_buster /assets/img/shareplay/shareplay3. ng %} [4]: {% image_buster /assets/img/shareplay/shareplay4.png %} [5]: {% image_buster /assets/img/shareplay/shareplay7. ng %} [6]: {% image_buster /assets/img/shareplay/shareplay6.png %}
