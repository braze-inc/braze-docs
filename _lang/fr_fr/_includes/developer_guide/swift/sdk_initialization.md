{% multi_lang_include developer_guide/prerequisites/swift.md %}

## Utilisation de l'initialisation différée

Vous pouvez initialiser votre SDK Braze Swift de manière asynchrone tout en veillant à ce que le traitement des notifications push soit préservé. Cela peut être utile lorsque vous devez configurer d'autres services avant d'initialiser le SDK, par exemple pour récupérer des données de configuration sur un serveur ou attendre le consentement de l'utilisateur.

### Considérations

Lorsque vous utilisez `Braze.prepareForDelayedInitialization(pushAutomation:)`, vous configurez le SDK pour qu'il utilise automatiquement les fonctionnalités d'automatisation des notifications push. Toutes les méthodes déléguées du système qui gèrent les notifications push ne seront pas appelées pour les notifications push provenant de Braze.

Le SDK ne traitera une notification push de Braze et l'action qui en résulte qu'**après** l'initialisation du SDK. Par exemple, si un utilisateur tape sur une notification push qui ouvre un lien profond, ce dernier ne s'ouvrira qu'après l'initialisation de l'instance `Braze`.

Si vous devez effectuer un traitement supplémentaire sur les notifications push de Braze, consultez la section [S'abonner aux mises à jour des notifications push]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#subscribing-to-push-notifications-updates). Gardez à l'esprit que pour recevoir des mises à jour pour les notifications push qui ont été précédemment mises en file d'attente, vous devez mettre en œuvre le gestionnaire d'abonnement directement après l'initialisation du SDK.

### Étape 1 : Préparer le SDK

Par défaut, si un utilisateur final ouvre votre notification push alors que votre application est dans un état terminé, la notification push ne peut pas être traitée avant l'initialisation du SDK.

À partir de la [version 10.1.0 du SDK Braze Swift](https://github.com/braze-inc/braze-swift-sdk/releases/tag/10.1.0), vous pouvez gérer cela à l'aide de la méthode d'aide statique : [Braze.prepareForDelayedInitialization(pushAutomation :).](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/preparefordelayedinitialization(pushautomation:)) Cette méthode prépare le SDK à une initialisation différée en configurant le système d'automatisation de la poussée.

Avant l'initialisation du SDK, toutes les notifications push provenant de Braze seront capturées et mises en file d'attente. Après l'initialisation du SDK, ces notifications push seront traitées par le SDK. Cette méthode doit être appelée le plus tôt possible dans le cycle de vie de votre application, soit dans ou avant la méthode `application(_:didFinishLaunchingWithOptions:)` de votre `AppDelegate`.

{% alert note %}
Le SDK Swift ne capture pas les notifications push autres que celles de Braze : celles-ci continueront d'être gérées par les méthodes de délégation du système.
{% endalert %}

{% tabs %}
{% tab Swift %}
{% subtabs local %}
{% subtab UIKit %}
```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
  // Prepare the SDK for delayed initialization
  Braze.prepareForDelayedInitialization()

  // ... Additional non-Braze setup code

  return true
}
```
{% endsubtab %}

{% subtab SwiftUI %}
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
{% endsubtab %}
{% endsubtabs %}
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

### Étape 2 : Initialiser le SDK

Après avoir préparé le SDK pour une initialisation différée, vous pouvez l'initialiser de manière asynchrone à tout moment dans le futur. Ensuite, le SDK traitera tous les événements de notifications push en file d'attente provenant de Braze.

Pour initialiser le SDK de Braze, suivez le [processus standard d'initialisation du SDK de Swift]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/sdk_integration/#step-2-update-your-app-delegate).

## Utilisation de Google Tag Manager

Le SDK Braze Swift peut être initialisé et contrôlé par des balises configurées dans Google Tag Manager.

Dans l'exemple suivant, une application de flux d'événements musicaux souhaite journaliser différents événements au fur et à mesure que les utilisateurs écoutent des chansons. À l'aide de Google Tag Manager pour iOS, ils peuvent contrôler quels fournisseurs tiers de Braze reçoivent cet événement et créer des tags spécifiques à Braze.

### Étape 1 : Créer un déclencheur pour les événements personnalisés

Les événements personnalisés sont enregistrés avec `actionType` réglé sur `logEvent`. Dans cet exemple, le fournisseur d'étiquettes personnalisées de Braze attend que le nom de l'événement personnalisé soit défini à l'aide de `eventName`.

Tout d'abord, créez un déclencheur qui recherche un `eventName` égal à `played song`.

![Dans Google Tag Manager, un déclencheur personnalisé est défini pour déclencher certains événements lorsque « eventName » est égal à « played song ».]({% image_buster /assets/img/android_google_tag_manager/gtm_android_trigger.png %})

Ensuite, créez une nouvelle étiquette (également appelée "appel de fonction") et entrez le chemin de classe de votre [fournisseur d'étiquettes personnalisé](#adding-ios-google-tag-provider) décrit plus loin dans cet article. Cette étiquette sera déclenchée lorsque vous enregistrerez l'événement `played song`. Comme `eventName` est défini sur `played song`, il sera utilisé comme nom d'événement personnalisé enregistré dans Braze.

{% alert important %}
Lors de l'envoi d'un événement personnalisé, définissez `actionType` sur `logEvent`, et définissez une valeur pour `eventName` afin que Braze reçoive le nom d'événement correct et l'action à entreprendre.
{% endalert %}

![Une balise dans Google Tag Manager avec des champs de chemin de classe et de paires clé-valeur. Cette étiquette est définie pour se déclencher avec le déclencheur "chanson jouée" créé précédemment.]({% image_buster /assets/img/android_google_tag_manager/gtm_android_function_call_tag.png %})

Vous pouvez également inclure des arguments de paires clé-valeur supplémentaires à la balise, qui seront envoyés en tant que propriétés d’événement personnalisé à Braze. `eventName` et `actionType` ne seront pas ignorés pour les propriétés d’événement personnalisé. Dans l'exemple de balise suivant, transmettez `genre`, qui a été défini à l'aide d'une variable de balise dans Google Tag Manager et qui provient de l'événement personnalisé enregistré dans l'application.

La propriété de l’événement `genre` est envoyée à l'outil Google Tag Manager en tant que variable « Firebase - paramètre de l’événement » étant donné que Google Tag Manager pour iOS utilise Firebase comme couche de données.

![Une variable du Google Tag Manager où « genre » est ajouté en tant que paramètre de l’événement pour la bibliothèque « Braze - événement de musique jouée ».]({% image_buster /assets/img/android_google_tag_manager/gtm_android_eventname_variable.png %})

Lorsqu'un utilisateur joue une chanson dans l'application, enregistrez un événement via Firebase et Google Tag Manager en utilisant le nom de l'événement d'analyse/analytique de Firebase qui correspond au nom du déclencheur de l'étiquette, `played song`:

{% tabs %}
{% tab SWIFT %}

```swift
let parameters: [String: Any] = ["genre": "pop",
                                 "number of times listened": 42]
Analytics.logEvent("played song", parameters: parameters)
```

{% endtab %}
{% tab OBJECTIF-C %}

```obj-c
NSDictionary *parameters = @{@"genre" : @"pop",
                             @"number of times listened" : @42};
[FIRAnalytics logEventWithName:@"played song" parameters:parameters];
```

{% endtab %}
{% endtabs %}

### Étape 2 : Enregistrer les attributs personnalisés

Les attributs personnalisés sont définis via un `actionType` réglé sur `customAttribute`. Le fournisseur de balises personnalisées Braze attend de la clé-valeur d’attribut personnalisée qu’elle soit définie via `customAttributeKey` et `customAttributeValue` :

{% tabs %}
{% tab SWIFT %}
```swift
let parameters: [String: Any] = ["customAttributeKey": "favoriteSong",
                                 "customAttributeValue": "Private Eyes"]
FIRAnalytics.logEvent(withName:"customAttribute", parameters: parameters)
```
{% endtab %}
{% tab OBJECTIF-C %}

```obj-c
NSDictionary *parameters = @{@"customAttributeKey" : @"favoriteSong",
                             @"customAttributeValue" : @"Private Eyes"};
[FIRAnalytics logEventWithName:@"customAttribute" parameters:parameters];
```

{% endtab %}

{% endtabs %}

### Étape 3 : Appeler `changeUser()`

Les appels vers `changeUser()` sont réalisés via un `actionType` réglé sur `changeUser`. Le fournisseur de balises personnalisées Braze attend que l’ID utilisateur Braze soit réglé via une paire clé-valeur `externalUserId` dans votre balise :

{% tabs %}
{% tab SWIFT %}
```swift
let parameters: [String: Any] = ["externalUserId": "favorite userId"]
Analytics.logEvent(withName:"changeUser", parameters: parameters)
```
{% endtab %}
{% tab OBJECTIF-C %}

```obj-c
NSDictionary *parameters = @{@"externalUserId" : userId};
[FIRAnalytics logEventWithName:@"changeUser" parameters:parameters];
```

{% endtab %}

{% endtabs %}

### Étape 4 : Ajouter un fournisseur d'étiquettes personnalisé {#adding-ios-google-tag-provider}

Une fois les tags et les déclencheurs configurés, vous devrez également mettre en œuvre Google Tag Manager dans votre application iOS, ce que vous trouverez dans la [documentation de](https://developers.google.com/tag-manager/ios/v5/) Google.

Une fois Google Tag Manager installé dans votre application, ajoutez un fournisseur d'étiquettes personnalisé pour appeler les méthodes du SDK de Braze en fonction des tags que vous avez configurés dans Google Tag Manager.

Assurez-vous de noter le « chemin de classe » vers le fichier. C’est ce que vous allez saisir lors de la définition d’une balise dans la console de [Google Tag Manager](https://tagmanager.google.com/).

Cet exemple illustre l'une des nombreuses façons dont vous pouvez structurer votre fournisseur d'étiquettes personnalisées. Plus précisément, il montre comment déterminer la méthode SDK Braze à appeler en fonction de la paire clé-valeur `actionType` envoyée par l'étiquette GTM. Cet exemple suppose que vous avez assigné l'instance de Braze en tant que variable dans l'AppDelegate.

Les `actionType` pris en charge dans cet exemple sont `logEvent`, `customAttribute`, et `changeUser`, mais il se peut que vous préfériez modifier la façon dont votre fournisseur d'étiquettes traite les données provenant de Google Tag Manager.
{% tabs %}
{% tab SWIFT %}

Ajoutez le code suivant à votre fichier `BrazeGTMTagManager.swift`.
```swift
import FirebaseAnalytics
import GoogleTagManager
import BrazeKit

let ActionTypeKey: String = "actionType"

// Custom Events
let LogEventAction: String = "logEvent"
let LogEventName: String = "eventName"

// Custom Attributes
let CustomAttributeAction: String = "customAttribute"
let CustomAttributeKey: String = "customAttributeKey"
let CustomAttributeValueKey: String = "customAttributeValue"

// Change User
let ChangeUserAction: String = "changeUser"
let ChangeUserExternalUserId: String = "externalUserId"

@objc(BrazeGTMTagManager)
final class BrazeGTMTagManager : NSObject, TAGCustomFunction {
  @objc func execute(withParameters parameters: [AnyHashable : Any]!) -> NSObject! {
    var parameters: [String : Any] = parameters as! [String : Any]
    guard let actionType: String = parameters[ActionTypeKey] as? String else {
      print("There is no Braze action type key in this call. Doing nothing.")
      return nil
    }
    parameters.removeValue(forKey: ActionTypeKey)
    if actionType == LogEventAction {
      logEvent(parameters: parameters)
    } else if actionType == CustomAttributeAction {
      logCustomAttribute(parameters: parameters)
    } else if actionType == ChangeUserAction {
      changeUser(parameters: parameters)
    }
    return nil
  }
  
  func logEvent(parameters: [String : Any]) {
    var parameters: [String : Any] = parameters
    guard let eventName: String = parameters[LogEventName] as? String else { return }
    parameters.removeValue(forKey: LogEventName)
    AppDelegate.braze?.logCustomEvent(name: eventName, properties: parameters)
  }
  
  func logCustomAttribute(parameters: [String: Any]) {
    guard let customAttributeKey = parameters[CustomAttributeKey] as? String else { return }
    let customAttributeValue = parameters[CustomAttributeValueKey]
    
    if let customAttributeValue = customAttributeValue as? String {
      AppDelegate.braze?.user.setCustomAttribute(key: customAttributeKey, value: customAttributeValue)
    } else if let customAttributeValue = customAttributeValue as? Date {
      AppDelegate.braze?.user.setCustomAttribute(key: customAttributeKey, value: customAttributeValue)
    } else if let customAttributeValue = customAttributeValue as? Double {
      AppDelegate.braze?.user.setCustomAttribute(key: customAttributeKey, value: customAttributeValue)
    } else if let customAttributeValue = customAttributeValue as? Bool {
      AppDelegate.braze?.user.setCustomAttribute(key: customAttributeKey, value: customAttributeValue)
    } else if let customAttributeValue = customAttributeValue as? Int {
      AppDelegate.braze?.user.setCustomAttribute(key: customAttributeKey, value: customAttributeValue)
    } else if let customAttibuteValue = customAttributeValue as? [String] {
      AppDelegate.braze?.user.setCustomAttributeArray(key: customAttributeKey, array: customAttibuteValue)
    }
  }
  
  func changeUser(parameters: [String: Any]) {
    guard let userId = parameters[ChangeUserExternalUserId] as? String else { return }
    AppDelegate.braze?.changeUser(userId: userId)
  }
}
```
{% endtab %}
{% tab OBJECTIF-C %}
Ajoutez le code suivant à votre fichier `BrazeGTMTagManager.h` :

```obj-c
@import Firebase;
@import GoogleTagManager;

@interface BrazeGTMTagManager : NSObject <TAGCustomFunction>

@end
```

Et ajoutez le code suivant à votre fichier `BrazeGTMTagManager.m` :

```obj-c
#import <Foundation/Foundation.h>
#import "BrazeGTMTagManager.h"
#import "BrazeKit"
#import "AppDelegate.h"

static NSString *const ActionTypeKey = @"actionType";

// Custom Events
static NSString *const LogEventAction = @"logEvent";
static NSString *const LogEventEventName = @"eventName";

// Custom Attributes
static NSString *const CustomAttributeAction = @"customAttribute";
static NSString *const CustomAttributeKey = @"customAttributeKey";
static NSString *const CustomAttributeValueKey = @"customAttributeValue";

// Change User
static NSString *const ChangeUserAction = @"changeUser";
static NSString *const ChangeUserExternalUserId = @"externalUserId";

@implementation BrazeGTMTagManager

- (NSObject *)executeWithParameters:(NSDictionary *)parameters {
  NSMutableDictionary *mutableParameters = [parameters mutableCopy];
  
  NSString *actionType = mutableParameters[ActionTypeKey];
  if (!actionType) {
    NSLog(@"There is no Braze action type key in this call. Doing nothing.", nil);
    return nil;
  }
  
  [mutableParameters removeObjectForKey:ActionTypeKey];
  
  if ([actionType isEqualToString:LogEventAction]) {
    [self logEvent:mutableParameters];
  } else if ([actionType isEqualToString:CustomAttributeAction]) {
    [self logCustomAttribute:mutableParameters];
  } else if ([actionType isEqualToString:ChangeUserAction]) {
    [self changeUser:mutableParameters];
  } else {
    NSLog(@"Invalid action type. Doing nothing.");
  }
  return nil;
}

- (void)logEvent:(NSMutableDictionary *)parameters {
  NSString *eventName = parameters[LogEventEventName];
  [parameters removeObjectForKey:LogEventEventName];
  [AppDelegate.braze logCustomEvent:eventName
                         properties:parameters];
}

- (void)logCustomAttribute:(NSMutableDictionary *)parameters {
  NSString *customAttributeKey = parameters[CustomAttributeKey];
  id customAttributeValue = parameters[CustomAttributeValueKey];
  
  if ([customAttributeValue isKindOfClass:[NSString class]]) {
    [AppDelegate.braze logCustomEvent:customAttributeKey
                           properties:parameters];
  } else if ([customAttributeValue isKindOfClass:[NSDate class]]) {
    [AppDelegate.braze.user setCustomAttributeWithKey:customAttributeKey
                                            dateValue:customAttributeValue];
  } else if ([customAttributeValue isKindOfClass:[NSNumber class]]) {
    if (strcmp([customAttributeValue objCType], [@(YES) objCType]) == 0) {
      [AppDelegate.braze.user setCustomAttributeWithKey:customAttributeKey
                                              boolValue:[(NSNumber *)customAttributeValue boolValue]];
    } else if (strcmp([customAttributeValue objCType], @encode(short)) == 0 ||
               strcmp([customAttributeValue objCType], @encode(int)) == 0 ||
               strcmp([customAttributeValue objCType], @encode(long)) == 0) {
      [AppDelegate.braze.user setCustomAttributeWithKey:customAttributeKey
                                               intValue:[(NSNumber *)customAttributeValue integerValue]];
    } else if (strcmp([customAttributeValue objCType], @encode(float)) == 0 ||
               strcmp([customAttributeValue objCType], @encode(double)) == 0) {
      [AppDelegate.braze.user setCustomAttributeWithKey:customAttributeKey
                                            doubleValue:[(NSNumber *)customAttributeValue doubleValue]];
    } else {
      NSLog(@"Could not map NSNumber value to Braze custom attribute:%@", customAttributeValue);
    }
  } else if ([customAttributeValue isKindOfClass:[NSArray class]]) {
    [AppDelegate.braze.user setCustomAttributeArrayWithKey:customAttributeKey
                                                     array:customAttributeValue];
  }
}

- (void)changeUser:(NSMutableDictionary *)parameters {
  NSString *userId = parameters[ChangeUserExternalUserId];
  [AppDelegate.braze changeUser:userId];
}

@end
```
{% endtab %}
{% endtabs %}
