---
nav_title: Initialisation retardée
article_title: Initialisation retardée pour le SDK Braze Swift
platform: Swift
page_order: 6
description: "Cet article explique comment mettre en œuvre l'initialisation différée du SDK Swift pour préserver le traitement des notifications push lorsque le SDK est initialisé de manière asynchrone."

---

# Initialisation retardée pour le SDK Braze Swift

> Découvrez comment initialiser votre SDK Braze Swift de manière asynchrone tout en veillant à ce que la gestion des notifications push soit préservée. Cela peut être utile lorsque vous devez configurer d'autres services avant d'initialiser le SDK, par exemple pour récupérer des données de configuration sur un serveur ou attendre le consentement de l'utilisateur.

## Mise en place de l'initialisation différée

### Étape 1 : Préparation du SDK pour une initialisation différée

Par défaut, si un utilisateur final ouvre votre notification push alors que votre application est dans un état terminé, la notification push ne peut pas être traitée avant l'initialisation du SDK.

À partir de la [version 10.1.0 du SDK Braze Swift](https://github.com/braze-inc/braze-swift-sdk/releases/tag/10.1.0), vous pouvez gérer cela à l'aide de la méthode d'aide statique : [Braze.prepareForDelayedInitialization(pushAutomation :).](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/preparefordelayedinitialization(pushautomation:)) Cette méthode prépare le SDK à une initialisation différée en configurant le système d'automatisation de la poussée.

Avant l'initialisation du SDK, toutes les notifications push provenant de Braze seront capturées et mises en file d'attente. Après l'initialisation du SDK, ces notifications push seront traitées par le SDK. Cette méthode doit être appelée le plus tôt possible dans le cycle de vie de votre application, soit dans ou avant la méthode `application(_:didFinishLaunchingWithOptions:)` de votre `AppDelegate`.

{% alert note %}
Le SDK Swift ne capture pas les notifications push autres que celles de Braze : celles-ci continueront d'être gérées par les méthodes de délégation du système.
{% endalert %}

{% tabs %}
{% tab Swift - UIKit %}
```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
  // Prepare the SDK for delayed initialization
  Braze.prepareForDelayedInitialization()

  // ... Additional non-Braze setup code

  return true
}
```
{% endtab %}

{% tab Swift - SwiftUI %}
Les applications SwiftUI doivent mettre en œuvre le wrapper de propriété [@UIApplicationDelegateAdaptor](https://developer.apple.com/documentation/swiftui/uiapplicationdelegateadaptor) pour appeler la méthode `prepareForDelayedInitialization()`.

```swift
@main
struct MyApp: App {
  @UIApplicationDelegateAdaptor var appDelegate: AppDelegate

  var body: some Scene {
    WindowGroup {
      ContentView()
    }
  }
}

class AppDelegate: NSObject, UIApplicationDelegate {
  
  func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil) -> Bool {
    // Prepare the SDK for delayed initialization
    Braze.prepareForDelayedInitialization()

    // ... Additional non-Braze setup code

    return true
  }
  
}
```
{% endtab %}

{% tab Objectif-C %}
```objc
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  // Prepare the SDK for delayed initialization
  [Braze prepareForDelayedInitialization];
  
  // ... Additional non-Braze setup code

  return YES;
}

```
{% endtab %}
{% endtabs %}

{% alert note %}
[Braze.prepareForDelayedInitialization(pushAutomation :)](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/preparefordelayedinitialization(pushautomation:)) prend un paramètre facultatif `pushAutomation` qui représente la configuration de l'automatisation pour les notifications push. Lorsque [Braze.Configuration.Push.Automation](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/push-swift.class/automation-swift.class) est `nil`, toutes les fonctionnalités d'automatisation sont activées, à l'exception de la demande d'autorisation au lancement.
{% endalert %}

### Étape 2 : Initialisation du SDK de Braze

Après avoir préparé le SDK pour une initialisation différée, vous pouvez l'initialiser de manière asynchrone à tout moment dans le futur. Ensuite, le SDK traitera tous les événements de notifications push en file d'attente provenant de Braze.

Pour initialiser le SDK de Braze, suivez le [processus standard d'initialisation du SDK de Swift]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/completing_integration/).

## Considérations

En utilisant `Braze.prepareForDelayedInitialization(pushAutomation:)`, vous configurez le SDK pour qu'il utilise automatiquement les fonctionnalités d'automatisation des notifications push. Toutes les méthodes déléguées du système qui gèrent les notifications push ne seront pas appelées pour les notifications push provenant de Braze.

Le SDK ne traitera une notification push de Braze et l'action qui en résulte qu'**après** l'initialisation du SDK. Par exemple, si un utilisateur tape sur une notification push qui ouvre un lien profond, ce dernier ne s'ouvrira qu'après l'initialisation de l'instance `Braze`.

Si vous devez effectuer un traitement supplémentaire sur les notifications push de Braze, consultez la section [S'abonner aux mises à jour des notifications push]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#subscribing-to-push-notifications-updates). Gardez à l'esprit que pour recevoir des mises à jour pour les notifications push qui ont été précédemment mises en file d'attente, vous devez mettre en œuvre le gestionnaire d'abonnement directement après l'initialisation du SDK.
