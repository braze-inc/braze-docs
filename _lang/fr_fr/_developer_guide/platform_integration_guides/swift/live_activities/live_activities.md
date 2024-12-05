---
nav_title: Activités en direct
article_title: Activités en direct pour iOS
platform: Swift
page_order: 1
description: "Cet article traite de l'utilisation de Braze pour gérer vos jetons d’activités en direct pour le SDK Swift."

---

# Activités en direct

> Les activités en direct sont des notifications interactives persistantes affichées sur votre écran de verrouillage, vous permettant de garder un œil sur les choses en temps réel. Comme elles apparaissent sur l’écran de verrouillage, les activités en direct garantissent que vos notifications ne seront pas manquées. Comme elles sont persistantes, vous pouvez afficher du contenu à jour pour vos utilisateurs sans même leur demander de déverrouiller leur téléphone. 

![Un suivi de livraison d’activité en direct sur l’écran de verrouillage d’un iPhone. Une barre d’état avec une voiture est presque à moitié remplie. Le texte indique « 2 min jusqu’à la récupération »]({% image_buster /assets/img/swift/live_activities/example_2.png %}){: style="max-width:40%;float:right;margin-left:15px;"}

Les activités en direct présentent une combinaison d’informations statiques et dynamiques que vous mettez à jour. Par exemple, vous pouvez créer une activité en direct qui fournit un suivi de statut pour une livraison. Cette activité en direct comporterait le nom de votre entreprise comme information statique, ainsi qu’un « délai de livraison » dynamique qui serait mis à jour à mesure que le livreur approche de sa destination.

En tant que développeur, vous pouvez utiliser Braze pour gérer les cycles de vie de vos activités en direct, faire des appels à l'API REST de Braze pour effectuer des mises à jour des activités en direct, et faire en sorte que tous les appareils abonnés reçoivent la mise à jour dès que possible. De plus, comme vous gérez les activités en direct via Braze, vous pouvez les utiliser en tandem avec vos autres canaux d'envoi de messages (notifications push, messages in-app, cartes de contenu) pour favoriser l'adoption.

## Conditions préalables 

{% sdk_min_versions swift:5.11.0 %}

Les exigences supplémentaires comprennent :

- Les activités en direct sont uniquement disponibles pour l’iPhone et l’iPad sous iOS 16.1 et versions ultérieures. Pour utiliser cette fonctionnalité, assurez-vous que votre projet cible cette version iOS.
- Le droit `Push Notification` doit être ajouté dans la section **Signature et capacités** de votre projet Xcode.
- Les activités en ligne/en production/instantané nécessitent l'utilisation d'une touche `.p8` pour envoyer la notification. Les fichiers plus anciens tels que `.p12` ou `.pem` ne sont pas pris en charge.
- À partir de la version 8.2.0 du SDK Swift Braze, vous pouvez [enregistrer à distance une activité en direct](#step-2-start-the-activity). Pour utiliser cette fonctionnalité, vous devez disposer d'iOS 17.2 ou d'une version ultérieure.

{% alert note %}
Si les activités en direct et les notifications push sont similaires, leurs autorisations système sont distinctes. Par défaut, toutes les fonctionnalités de l'activité en direct sont activées, mais les utilisateurs peuvent désactiver cette fonctionnalité par application.
{% endalert %}

## Mise en œuvre d’une activité en direct

### Étape 1 : Créer une activité

Tout d'abord, assurez-vous d'avoir suivi [Afficher des données en ligne/instantanées avec les activités en direct](https://developer.apple.com/documentation/activitykit/displaying-live-data-with-live-activities) dans la documentation d'Apple pour configurer les activités en direct dans votre application iOS. Dans le cadre de cette tâche, assurez-vous d’inclure `NSSupportsLiveActivities` défini sur `YES` dans votre `Info.plist`.

Comme la nature exacte de votre activité en ligne/instantanée sera spécifique à votre cas d'entreprise, vous devrez configurer et initialiser les objets de [l'activité.](https://developer.apple.com/documentation/activitykit/activityattributes)  Plus important encore, vous définirez :
* `ActivityAttributes` : Ce protocole définit le contenu statique (ne changeant pas) et dynamique (changeant) qui apparaîtra dans votre activité en direct.
* `ActivityAttributes.ContentState` : Ce type définit les données dynamiques qui seront mises à jour au cours de l'activité.

Vous utiliserez également SwiftUI pour créer l’interface utilisateur de la présentation de l’écran de verrouillage et Dynamic Island sur les appareils pris en charge. 

Assurez-vous de bien connaître les [conditions préalables et les limites](https://developer.apple.com/documentation/activitykit/displaying-live-data-with-live-activities#Understand-constraints) d’Apple pour les activités en direct, car ces contraintes sont indépendantes de Braze.

{% alert note %}
Si vous prévoyez d’envoyer des notifications push fréquentes vers la même activité en direct, vous pouvez éviter d’être limité par la limite budgétaire d’Apple en définissant `NSSupportsLiveActivitiesFrequentUpdates` sur `YES` dans votre fichier `Info.plist`. Pour plus de détails, reportez-vous à la section [`Determine the update frequency`](https://developer.apple.com/documentation/activitykit/updating-and-ending-your-live-activity-with-activitykit-push-notifications#Determine-the-update-frequency) dans la documentation ActivityKit.
{% endalert %}

#### Exemple

Imaginons que nous voulions créer une activité en direct pour donner à nos utilisateurs des mises à jour sur le spectacle Superb Owl, où deux équipes concurrentes de sauvetage d’animaux sauvages reçoivent des points pour les hiboux dont ils s’occupent. Dans cet exemple, nous avons créé une structure appelée `SportsActivityAttributes`, mais vous pouvez utiliser votre propre mise en œuvre d’`ActivityAttributes`.

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

### Étape 2 : Démarrer l'activité

Tout d'abord, choisissez le mode d'enregistrement de votre activité :

- **À distance :** Le plus tôt possible dans le cycle de vie de votre application et de vos utilisateurs (et avant que le jeton Push to Start ne soit nécessaire), utilisez la méthode [`registerPushToStart`](<http://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/liveactivities-swift.class/registerpushtostart(fortype:name:)>) méthode. Ensuite, démarrez une activité à l'aide du point de terminaison [`/messages/live_activity/start`]({{site.baseurl}}/api/endpoints/messaging/live_activity/start) endpoint.
- **Localement :** Créez une instance de votre activité en direct, puis utilisez la méthode [`launchActivity`](<https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/liveactivities-swift.class/launchactivity(pushtokentag:activity:fileid:line:)>) pour créer des jetons de notifications push à gérer par Braze.

{% tabs local %}
{% tab à distance %}
{% alert important %}
Pour enregistrer à distance une activité en direct, vous devez disposer d'iOS 17.2 ou d'une version ultérieure.
{% endalert %}

#### Étape 2.1 : Ajoutez BrazeKit à votre extension de widget

Dans votre projet Xcode, sélectionnez le nom de votre application, puis **Général**. Sous **Infrastructures et bibliothèques**, vérifiez que `BrazeKit` est inclus dans la liste.

![Framework BrazeKit sous Infrastructures et bibliothèques dans un exemple de projet Xcode.]({% image_buster /assets/img/swift/live_activities/xcode_frameworks_and_libraries.png %})

#### Étape 2.2 : Ajouter le protocole BrazeLiveActivityAttributes

Dans votre implémentation `ActivityAttributes`, ajoutez la conformité au protocole `BrazeLiveActivityAttributes`, puis ajoutez la chaîne de caractères `brazeActivityId` à votre modèle d'attributs. Il n'est pas nécessaire d'attribuer une valeur à cette chaîne de caractères.

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

#### Étape 2.3 : S'inscrire à la fonctionnalité Push to Start

Ensuite, enregistrez le type d'activité en direct, afin que Braze puisse assurer le suivi de tous les jetons push-to-start et des instances d'activité en direct associés à ce type.

{% alert warning %}
Le système d'exploitation iOS ne génère des jetons push-to-start que lors de la première installation d'appli après le redémarrage d'un appareil. Pour vous assurer que vos jetons sont enregistrés de manière fiable, appelez `registerPushToStart` dans votre méthode `didFinishLaunchingWithOptions`.
{% endalert %}

###### Exemple

Dans l'exemple suivant, la classe `LiveActivityManager` gère des objets de type activité en direct. Ensuite, la méthode `registerPushToStart` enregistre `SportActivityAttributes`:

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

#### Étape 2.4 : Envoyer une notification push-to-start

Envoyez une notification push-to-start à distance à l'aide du endpoint [`/messages/live_activity/start`]({{site.baseurl}}/api/endpoints/messaging/live_activity/start).
{% endtab %}

{% tab local %}
Vous pouvez utiliser [le framework ActivityKit d'Apple](https://developer.apple.com/documentation/activitykit) pour obtenir un jeton de notification push que le SDK Braze peut gérer pour vous. Cela vous permet de mettre à jour les activités en direct via l’API Braze, car Braze enverra le jeton de notification push au service de notification push d’Apple (APN) sur le back-end.

1. Créez une instance de votre implémentation d’activité en direct à l’aide des API ActivityKit d’Apple.
2. Définissez le paramètre `pushType` sur `.token`. 
3. Transmettez les `ActivitiesAttributes` et le `ContentState` des activités en direct que vous avez définis. 
4. Enregistrez votre activité auprès de votre instance Braze en la passant dans la commande [`launchActivity(pushTokenTag:activity:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/liveactivities-swift.class). Le paramètre `pushTokenTag` est une chaîne de caractères personnalisée que vous définissez. Elle doit être unique pour chaque activité en direct que vous créez.

Une fois que vous avez enregistré l’activité en direct, le SDK Braze extrait et observe les changements dans les jetons de notification push.

#### Exemple

Pour notre exemple, nous allons créer une classe appelée `LiveActivityManager` qui servira d'interface pour nos objets d'activité en direct. Ensuite, nous définirons le `pushTokenTag` sur `"sports-game-2024-03-15"`.

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

Votre gadget Activité en direct affichera ce contenu initial à vos utilisateurs. 

![Une activité en direct sur l’écran de verrouillage d’un iPhone avec les scores de deux équipes. Les équipes Wild Bird Fund et Owl Rehab ont toutes deux un score de 0.]({% image_buster /assets/img/swift/live_activities/example_1_1.png %}){: style="max-width:40%;"}
{% endtab %}
{% endtabs %}

### Étape 3 : Reprendre le suivi des activités

Pour que Braze suive votre activité en direct dès le lancement de l'application :

1. Ouvrez votre fichier `AppDelegate`.
2. Importez le module `ActivityKit` s’il est disponible.
3. Appelez [`resumeActivities(ofType:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/liveactivities-swift.class/resumeactivities(oftype:)) à `application(_:didFinishLaunchingWithOptions:)` pour tous les types de `ActivityAttributes` que vous avez enregistrés dans votre application.

Cela permet à Braze de reprendre les tâches pour suivre les mises à jour des jetons de notification push pour toutes les activités en direct actives. Notez que si un utilisateur a explicitement rejeté l’activité en direct sur son appareil, elle est considérée comme supprimée et Braze ne la suivra plus.

###### Exemple

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

### Étape 4 : Mettre à jour l'activité

![Une activité en direct sur l’écran de verrouillage d’un iPhone avec les scores de deux équipes. L’équipe Wild Bird Fund a 2 points et la Owl Rehab a 4 points.]({% image_buster /assets/img/swift/live_activities/example_1_2.png %}){: style="max-width:40%;float:right;margin-left:15px;"}

Le point de terminaison [`/messages/live_activity/update`]({{site.baseurl}}/api/endpoints/messaging/live_activity/update) vous permet de mettre à jour une activité en direct par le biais de notifications push transmises par l'API REST de Braze. Utilisez cet endpoint pour mettre à jour le `ContentState` de votre activité en direct.

Lorsque vous mettez à jour votre `ContentState`, votre gadget Activité en direct affiche les nouvelles informations. Voici à quoi pourrait ressembler le spectacle Superb Owl à la fin de la première partie.

Pour plus de détails, consultez notre article sur le [point de terminaison`/messages/live_activity/update` ]({{site.baseurl}}/api/endpoints/messaging/live_activity/update).

### Étape 5 : Terminer l'activité

Lorsqu’une activité en direct est active, elle s’affiche à la fois sur l’écran de verrouillage d’un utilisateur et sur Dynamic Island. Il existe plusieurs façons de mettre fin à une activité en direct et de la supprimer de l’interface utilisateur d’un utilisateur. 

* **Fermeture par l'utilisateur** : Un utilisateur peut fermer manuellement une activité en direct.
* **Expiration** : Après une durée par défaut de 8 heures, iOS supprimera l’activité en direct de la Dynamic Island de l’utilisateur. Après une durée par défaut de 12 heures, iOS supprimera l’activité en direct de l’écran de verrouillage de l’utilisateur. 
* **Date de suppression** : Vous pouvez fournir une date et une heure pour qu’une activité en direct soit supprimée de l’interface utilisateur d’un utilisateur avant le délai d’expiration. Ceci est défini soit dans l’`ActivityUIDismissalPolicy` de l’activité, soit à l’aide du paramètre `dismissal_date` dans les requêtes adressées à l’endpoint `/messages/live_activity/update`.
* **Fin de l'activité** : Vous pouvez définir `end_activity` sur `true` dans une requête à l’endpoint `/messages/live_activity/update` pour mettre immédiatement fin à une activité en direct.

Pour plus de détails, consultez notre article sur le [point de terminaison`/messages/live_activity/update` ]({{site.baseurl}}/api/endpoints/messaging/live_activity/update).

## Résolution des problèmes

Pour plus de détails sur le dépannage ou les questions fréquemment posées, consultez notre [FAQ]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/live_activities/faq/).

