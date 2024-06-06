---
nav_title: Activités en direct
article_title: Activités en direct pour iOS
platform: Swift
page_order: 1
description: "Cet article couvre l’utilisation de Braze pour gérer vos jetons d’activités en direct."

---

# Activités en direct pour iOS

{% alert important %} 
Les activités en direct sont actuellement en accès anticipé. Contactez votre gestionnaire de compte Braze si vous souhaitez participer. 
{% endalert %}

Les activités en direct sont des notifications interactives persistantes affichées sur votre écran de verrouillage, vous permettant de garder un œil sur les choses en temps réel. Comme elles apparaissent sur l’écran de verrouillage, les activités en direct garantissent que vos notifications ne seront pas manquées. Comme elles sont persistantes, vous pouvez afficher du contenu à jour pour vos utilisateurs sans même leur demander de déverrouiller leur téléphone. 

![Un suivi de livraison d’activité en direct sur l’écran de verrouillage d’un iPhone. Une barre d’état avec une voiture est presque à moitié remplie. Le texte indique « 2 min jusqu’à la récupération »][7]{: style="max-width:40%;float:right;margin-left:15px;"}

Les activités en direct présentent une combinaison d’informations statiques et dynamiques que vous mettez à jour. Par exemple, vous pouvez créer une activité en direct qui fournit un suivi de statut pour une livraison. Cette activité en direct comporterait le nom de votre entreprise comme information statique, ainsi qu’un « délai de livraison » dynamique qui serait mis à jour à mesure que le livreur approche de sa destination.

En tant que développeur, vous pouvez utiliser Braze pour gérer vos cycles de vie d’activité en direct, passer des appels à l’API REST Braze pour effectuer des mises à jour d’activité en direct et faire en sorte que tous les appareils abonnés reçoivent la mise à jour le plus rapidement possible. Et, comme vous gérez les activités en direct via Braze, vous pouvez les utiliser en combinaison avec vos autres canaux de communication&mdash;notifications push, messages in-app, cartes de contenu&mdash;pour stimuler l’adoption. 

## Conditions préalables 

{% sdk_min_versions swift:5.11.0 %}

Les exigences supplémentaires comprennent :
* Les activités en direct ne sont disponibles que pour les iPhones sur iOS 16.1 et les versions ultérieures. Pour utiliser cette fonctionnalité, assurez-vous que votre projet cible cette version iOS.
* Le droit aux `Push Notification` doit être ajouté dans la section **Signing & Capabilities (Signature et capacités)** de l’Xcode de votre projet.

{% alert note %}
Notez que, même si les activités en direct fonctionnent de la même manière que les notifications push, elles sont contrôlées par différents paramètres utilisateur. Un utilisateur à la possibilité de s’abonner aux activités en direct mais pas aux notifications push, et vice versa.
{% endalert %}

## Mise en œuvre d’une activité en direct

Pour gérer le cycle de vie d’une activité en direct, suivez ces quatre étapes.

1. [Créer l’activité en direct.](#developing) Développez l’interface utilisateur de l’activité en direct à l’aide de WidgetKit et SwiftUI. Initialisez un objet Activité en direct avec les modèles de données pertinents pour vos états statiques et dynamiques.<br><br>

2. [Enregistrer l’activité en direct](#registering) Enregistrez une activité en direct avec le SDK Braze en utilisant la méthode [`launchActivity`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/liveactivities-swift.class/launchactivity(pushtokentag:activity:fileid:line:)) avec l’objet Activité en direct et la balise d’activité unique.<br><br>

3. [Mettre à jour l’activité en direct](#updating) Publiez des mises à jour pour l’activité en direct à l’aide de l’endpoint [`/messages/live_activity/update`]({{site.baseurl}}/api/endpoints/messaging/live_activity/update) de l’API de Braze.<br><br>

4. [Terminer l’activité en direct](#ending) Terminez une activité en direct pour tous les destinataires en publiant une mise à jour de [`/messages/live_activity/update`]({{site.baseurl}}/api/endpoints/messaging/live_activity/update) avec le paramètre `"end_activity": true`.

## Étape 1 : Développer votre activité en direct {#developing}

Tout d’abord, assurez-vous d’avoir suivi la section [Afficher des données en direct avec des activités en direct][3] dans la documentation d’Apple pour configurer des activités en direct dans votre application iOS. Dans le cadre de cette tâche, assurez-vous d’inclure `NSSupportsLiveActivities` défini sur `YES` dans votre `Info.plist`. 

Étant donné que la nature exacte de votre activité en direct sera spécifique à votre dossier commercial, vous devrez configurer et initialiser les objets [Activité][4]. Plus important encore, vous définirez :
* `ActivityAttributes` : ce protocole définit le contenu statique (ne changeant pas) et dynamique (changeant) qui apparaîtra dans votre activité en direct.
* `ActivityAttributes.ContentState` : ce type définit les données dynamiques qui seront mises à jour au cours de l’activité.

Vous utiliserez également SwiftUI pour créer l’interface utilisateur de la présentation de l’écran de verrouillage et Dynamic Island sur les appareils pris en charge. 

Assurez-vous de bien connaître les [conditions préalables et les limites][2] d’Apple pour les activités en direct, car ces contraintes sont indépendantes de Braze.

{% alert note %}
Si vous prévoyez d’envoyer des notifications push fréquentes vers la même activité en direct, vous pouvez éviter d’être limité par la limite budgétaire d’Apple en définissant `NSSupportsLiveActivitiesFrequentUpdates` sur `YES` dans votre fichier `Info.plist`. Pour plus de détails, reportez-vous à la section [`Determine the update frequency`](https://developer.apple.com/documentation/activitykit/updating-and-ending-your-live-activity-with-activitykit-push-notifications#Determine-the-update-frequency) dans la documentation ActivityKit.
{% endalert %}

### Exemple

Imaginons que nous voulions créer une activité en direct pour donner à nos utilisateurs des mises à jour sur le spectacle Superb Owl, où deux équipes concurrentes de sauvetage d’animaux sauvages reçoivent des points pour les hiboux dont ils s’occupent. Dans cet exemple, nous avons créé une structure appelée `BrazeActivityAttributes`, mais vous pouvez utiliser votre propre mise en œuvre d’`ActivityAttributes`.

```swift
#if canImport(ActivityKit)
  import ActivityKit
#endif

@available(iOS 16.1, *)
struct BrazeActivityAttributes: ActivityAttributes {
  public struct ContentState: Codable, Hashable {
    var teamOneScore: Int
    var teamTwoScore: Int
  }

  var gameName: String
  var gameNumber: String
}
```

## Étape 2 : Enregistrer une activité en direct {#registering}

Ensuite, vous utiliserez les méthodes Braze pour suivre et gérer vos activités en direct. 

Les mises à jour d’une activité en direct peuvent être envoyées à l’aide d’ActivityKit (cadre d’Apple pour la gestion d’une activité en direct) ou de notifications push à distance. Dans ce cas, vous utiliserez ActivityKit pour obtenir un jeton de notification push que le SDK Braze peut gérer pour vous. Cela vous permet de mettre à jour les activités en direct via l’API Braze, car Braze enverra le jeton de notification push au service de notification push d’Apple (APN) sur le back-end.

1. Créez une instance de votre implémentation d’activité en direct à l’aide des API ActivityKit d’Apple.
2. Définissez le paramètre `pushType` sur `.token`. 
3. Transmettez les `ActivitiesAttributes` et le `ContentState` des activités en direct que vous avez définis. 
4. Enregistrez votre activité avec votre instance Braze en la transmettant dans [`launchActivity(pushTokenTag:activity:)`][5]. Le paramètre `pushTokenTag` est une chaîne de caractères personnalisée que vous définissez. Elle doit être unique pour chaque activité en direct que vous créez.

Une fois que vous avez enregistré l’activité en direct, le SDK Braze extrait et observe les changements dans les jetons de notification push.

### Exemple

Dans notre exemple, nous allons créer une classe appelée LiveActivityManager comme interface pour nos objets Activité en direct. Ensuite, nous définirons le `pushTokenTag` sur `"live-activity-1"`.

```swift
import BrazeKit

#if canImport(ActivityKit)
  import ActivityKit
#endif

class LiveActivityManager {
  
  @available(iOS 16.2, *)
  func createActivity() {
    let activityAttributes = BrazeActivityAttributes(gameName: "Superb Owl", gameNumber: "Game 1")
    let contentState = BrazeActivityAttributes.ContentState(teamOneScore: "0", teamTwoScore: "0")
    let activityContent = ActivityContent(state: contentState, staleDate: nil)
    if let activity = try? Activity.request(attributes: activityAttributes,
                                            content: activityContent,
      // Setting your pushType as .token allows the Activity to generate push tokens for the server to watch.
                                            pushType: .token) {
      // Register your Live Activity with Braze using the pushTokenTag
      AppDelegate.braze?.liveActivities.launchActivity(pushTokenTag: "live-activity-1",
                                                       activity: activity)
    }
  }
  
}
```

Votre gadget Activité en direct affichera ce contenu initial à vos utilisateurs. 

![Une activité en direct sur l’écran de verrouillage d’un iPhone avec les scores de deux équipes. Les équipes Wild Bird Fund et Owl Rehab ont toutes deux un score de 0.][8]{: style="max-width:40%;"}

### Reprise du suivi des activités en direct

Vous devrez vous assurer que Braze suit votre Activité en direct au lancement de l’application.

Pour ce faire :
1. Ouvrez votre fichier `AppDelegate`.
2. Importez le module `ActivityKit` s’il est disponible.
3. Appelez [`resumeActivities(ofType:)`][6] dans `application(_:didFinishLaunchingWithOptions:)` pour tous les types `ActivityAttributes` que vous avez enregistrés dans votre application.

Cela permet à Braze de reprendre les tâches pour suivre les mises à jour des jetons de notification push pour toutes les activités en direct actives. Notez que si un utilisateur a explicitement rejeté l’activité en direct sur son appareil, elle est considérée comme supprimée et Braze ne la suivra plus.

#### Exemple

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
        ofType: Activity<BrazeActivityAttributes>.self
      )
    }

    return true
  }
}
```

## Étape 3 : Mettre à jour une activité en direct {#updating}

![Une activité en direct sur l’écran de verrouillage d’un iPhone avec les scores de deux équipes. Le Wild Bird Fund a 2 points et la Owl Rehab a 4 points.][9]{: style="max-width:40%;float:right;margin-left:15px;"}

L’endpoint [`/messages/live_activity/update`][1] vous permet de mettre à jour une activité en direct via des notifications push transmises via l’API REST de Braze. Utilisez cet endpoint pour mettre à jour le `ContentState` de votre activité en direct.

Lorsque vous mettez à jour votre `ContentState`, votre gadget Activité en direct affiche les nouvelles informations. Voici à quoi pourrait ressembler le spectacle Superb Owl à la fin de la première partie.

Voir la documentation de l’endpoint [`/messages/live_activity/update`][1] pour plus de détails.

## Étape 4 : Arrêter une activité en direct {#ending}

Lorsqu’une activité en direct est active, elle s’affiche à la fois sur l’écran de verrouillage d’un utilisateur et sur Dynamic Island. Il existe plusieurs façons de mettre fin à une activité en direct et de la supprimer de l’interface utilisateur d’un utilisateur. 

* **Fermeture par l’utilisateur** : Un utilisateur peut fermer manuellement une activité en direct.
* **Expiration** : Après une durée par défaut de 8 heures, iOS supprimera l’activité en direct de la Dynamic Island de l’utilisateur. Après une durée par défaut de 12 heures, iOS supprimera l’activité en direct de l’écran de verrouillage de l’utilisateur. 
* **Heure de fermeture** : Vous pouvez fournir une date et une heure pour qu’une activité en direct soit supprimée de l’interface utilisateur d’un utilisateur avant le délai d’expiration. Ceci est défini soit dans l’`ActivityUIDismissalPolicy` de l’activité, soit à l’aide du paramètre `dismissal_date` dans les requêtes adressées à l’endpoint `/messages/live_activity/update`.
* **Fin de l’activité** : Vous pouvez définir `end_activity` sur `true` dans une requête à l’endpoint `/messages/live_activity/update` pour mettre immédiatement fin à une activité en direct.

Voir la documentation de l’endpoint [`/messages/live_activity/update`][1] pour plus de détails.

[1]: {{site.baseurl}}/api/endpoints/messaging/live_activity/update
[2]: https://developer.apple.com/documentation/activitykit/displaying-live-data-with-live-activities#Understand-constraints
[3]: https://developer.apple.com/documentation/activitykit/displaying-live-data-with-live-activities
[4]: https://developer.apple.com/documentation/activitykit/activityattributes
[5]: https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/liveactivities-swift.class
[6]: https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/liveactivities-swift.class/resumeactivities(oftype:)
[7]: {% image_buster /assets/img/swift/live_activities/example_2.png %} 
[8]: {% image_buster /assets/img/swift/live_activities/example_1_1.png %}
[9]: {% image_buster /assets/img/swift/live_activities/example_1_2.png %}