---
nav_title: Google Tag Manager
article_title: Google Tag Manager pour iOS
platform: Swift
page_order: 3
description: "Cet article explique comment initialiser, configurer et déployer Google Tag Manager pour le SDK Swift."

---

# Google Tag Manager

> Le SDK Braze Swift peut être initialisé et contrôlé par des balises configurées dans Google Tag Manager.

L'intégration de votre SDK Swift est une condition préalable à cette mise en œuvre.

## Configuration de votre Google Tag Manager {#configuring-ios-google-tag-manager}

Dans cet exemple, nous allons prétendre que nous sommes une application de streaming de musique qui veut enregistrer différents événements pendant que les utilisateurs écoutent des chansons. Grâce au Google Tag Manager pour iOS, nous pouvons contrôler lequel de nos fournisseurs tiers reçoit cet événement et créer des balises spécifiques à Braze.

### Événements personnalisés

Les événements personnalisés sont enregistrés avec `actionType` réglé sur `logEvent`. Le fournisseur de balises personnalisées de Braze, dans notre exemple, attend que le nom de l’événement personnalisé soit défini à l’aide de `eventName`.

Pour commencer, créez un déclencheur qui recherche un `eventName` équivalent à `played song`.

![Dans Google Tag Manager, un déclencheur personnalisé est défini pour déclencher certains événements lorsque « eventName » est égal à « played song ».]({% image_buster /assets/img/android_google_tag_manager/gtm_android_trigger.png %})

Ensuite, créez une nouvelle balise (« Appel de fonction ») et saisissez le chemin de classe de votre [fournisseur de balises personnalisées](#adding-ios-google-tag-provider) décrit plus loin dans cet article. 

Cette balise sera déclenchée lorsque vous enregistrez l’événement `played song` que nous venons de créer. 

Dans les paramètres personnalisés de notre exemple de balise (paires clé-valeur), nous avons défini `eventName` sur`played song`, qui sera le nom de l’événement personnalisé enregistré dans Braze.

{% alert important %}
Lorsque vous envoyez un événement personnalisé, définissez `actionType` vers `logEvent` et de définir une valeur pour `eventName` comme illustré dans l’exemple suivant.
<br><br>
Le fournisseur de balises personnalisées dans notre exemple utilisera ces clés pour déterminer les mesures à prendre et le nom de l’événement à envoyer à Braze lorsqu’il reçoit des données de Google Tag Manager.
{% endalert %}

![Une balise dans Google Tag Manager avec des champs de chemin de classe et de paires clé-valeur. Cette étiquette est définie pour se déclencher avec le déclencheur "chanson jouée" créé précédemment.]({% image_buster /assets/img/android_google_tag_manager/gtm_android_function_call_tag.png %})

Vous pouvez également inclure des arguments de paires clé-valeur supplémentaires à la balise, qui seront envoyés en tant que propriétés d’événement personnalisé à Braze. `eventName` et `actionType` ne seront pas ignorés pour les propriétés d’événement personnalisé. Dans l’exemple de balise suivant, nous allons transmettre `genre` qui a été défini à l’aide d’une variable de balise dans Google Tag Manager issue de l’événement personnalisé que nous avons enregistré dans notre application.

La propriété de l’événement `genre` est envoyée à l'outil Google Tag Manager en tant que variable « Firebase - paramètre de l’événement » étant donné que Google Tag Manager pour iOS utilise Firebase comme couche de données.

![Une variable du Google Tag Manager où « genre » est ajouté en tant que paramètre de l’événement pour la bibliothèque « Braze - événement de musique jouée ».]({% image_buster /assets/img/android_google_tag_manager/gtm_android_eventname_variable.png %})

Enfin, lorsqu’un utilisateur joue une chanson dans notre application, nous allons enregistrer un événement via Firebase et Google Tag Manager en utilisant le nom d’événement d’analytique Firebase qui correspond au nom de déclencheur de notre balise, `played song` :

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

### Enregistrer des attributs personnalisés

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

### Appeler changeUser

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

## Fournisseur de balises personnalisées du Braze SDK {#adding-ios-google-tag-provider}

Une fois les tags et les déclencheurs configurés, vous devrez également mettre en œuvre Google Tag Manager dans votre application iOS, ce que vous trouverez dans la [documentation de](https://developers.google.com/tag-manager/ios/v5/) Google.

Une fois que l'outil Google Tag Manager est installé dans votre application, ajoutez un fournisseur de balises personnalisées pour appeler les méthodes du SDK Braze en fonction des balises que vous avez configurées dans Google Tag Manager. 

Assurez-vous de noter le « chemin de classe » vers le fichier. C’est ce que vous allez saisir lors de la définition d’une balise dans la console de [Google Tag Manager](https://tagmanager.google.com/).

Cet exemple illustre l'une des nombreuses façons de structurer votre fournisseur d'étiquettes personnalisé. Nous déterminons la méthode SDK de Braze à appeler en fonction de la paire clé-valeur `actionType` envoyée par le gestionnaire de balises Google. Cet exemple suppose que vous avez assigné l'instance de Braze en tant que variable dans l'AppDelegate.

Les `actionType` que nous avons pris en charge dans notre exemple sont `logEvent`, `customAttribute` et `changeUser`, mais vous pouvez modifier la manière dont votre fournisseur de balises gère les données de Google Tag Manager.
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

