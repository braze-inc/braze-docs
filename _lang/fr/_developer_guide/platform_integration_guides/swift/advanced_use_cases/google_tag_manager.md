---
hidden: true
nav_title: Google Tag Manager
article_title: Google Tag Manager pour iOS
platform: iOS
page_order: 7
description: "Cet article explique comment initialiser, configurer et implémenter le Google Tag Manager dans votre application iOS."

---

# Google Tag Manager pour iOS

## Initialisation du SDK {#initializing-ios-google-tag-provider}

Le SDK Braze pour iOS peut être initialisé et contrôlé par des balises configurées dans le [Google Tag Manager][5].

Avant d’utiliser le Google Tag Manager, assurez-vous de suivre d’abord notre [configuration initiale du SDK][1].

## Configuration de votre Google Tag Manager {#configuring-ios-google-tag-manager}

Dans cet exemple, nous allons prétendre que nous sommes une application de streaming de musique qui veut enregistrer différents événements pendant que les utilisateurs écoutent des chansons. Grâce au Google Tag Manager pour iOS, nous pouvons contrôler lequel de nos fournisseurs tiers reçoit cet événement et créer des balises spécifiques à Braze.

### Événements personnalisés

Les événements personnalisés sont enregistrés avec `actionType` réglé sur `logEvent`. Le fournisseur de balises personnalisées de Braze, dans notre exemple, attend que le nom de l’événement personnalisé soit défini à l’aide de `eventName`.

Pour commencer, créez un déclencheur qui recherche un « nom de l’événement » qui équivaut à la `chanson jouée`.

![Dans Google Tag Manager, un déclencheur personnalisé est défini pour déclencher certains événements lorsque « nom de l’événement » est égal à « chanson jouée ».][3]

Ensuite, créez une nouvelle balise (« Appel de fonction ») et saisissez le chemin de classe de votre [fournisseur de balises personnalisées](#adding-ios-google-tag-provider) décrit plus loin dans cet article. 

Cette balise sera déclenchée lorsque vous enregistrez l’événement associé à la `chanson jouée` que nous venons de créer. 

Dans notre exemple de paramètres personnalisés de notre balise (paires clé-valeur), nous avons défini `eventName` sur `chanson jouée`, qui sera le nom de l’événement personnalisé enregistré sur Braze.

{% alert important %}
Lorsque vous envoyez un événement personnalisé, définissez `actionType` vers `logEvent` et de définir une valeur pour `eventName` comme illustré dans l’exemple suivant. 

Le fournisseur de balises personnalisées dans notre exemple utilisera ces clés pour déterminer les mesures à prendre et le nom de l’événement à envoyer à Braze lorsqu’il reçoit des données du Google Tag Manager.
{% endalert %}

![Une balise dans le Google Tag Manager avec des champs de chemin de classe et de paires clé-valeur. Cette balise est définie pour répondre au déclencheur créé précédemment « chanson jouée ».][4]

Vous pouvez également inclure des arguments de paires clé-valeur supplémentaires à la balise, qui seront envoyés en tant que propriétés de l’événement personnalisées à Braze. `eventName` et `actionType` ne seront pas ignorés pour les propriétés de l’événement personnalisées. Dans l’exemple de balise suivant, nous allons transmettre `genre` qui a été défini à l’aide d’une variable de balise dans le Google Tag Manager issue de l’événement personnalisé que nous avons enregistré dans notre application.

La propriété de l’événement `genre` est envoyée au Google Tag Manager en tant que variable « Firebase - paramètre de l’événement » étant donné que le Google Tag Manager pour iOS utilise Firebase comme couche de données.

![Une variable dans le Google Tag Manager où « genre » est ajouté en tant que paramètre de l’événement pour la bibliothèque « Braze - événement de musique jouée ».][6]

Enfin, lorsqu’un utilisateur joue une chanson dans notre application, nous allons enregistrer un événement via Firebase et le Google Tag Manager en utilisant le nom d’événement d’analytique Firebase qui correspond au nom de déclencheur de notre balise, `chanson jouée` :

{% tabs %}
{% tab OBJECTIVE-C %}

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
{% tab OBJECTIVE-C %}

```obj-c
NSDictionary *parameters = @{@"customAttributeKey" : @"favorite song",
                             @"customAttributeValue" : @"Private Eyes"};
[FIRAnalytics logEventWithName:@"customAttribute" parameters:parameters];
```

{% endtab %}
{% endtabs %}

### Appeler changeUser

Les appels vers `changeUser()` sont réalisés via un `actionType` réglé sur `changeUser`. Le fournisseur de balises personnalisées Braze attend que l’ID utilisateur Braze soit réglé via une paire clé-valeur `externalUserId` dans votre balise :

{% tabs %}
{% tab OBJECTIVE-C %}

```obj-c
NSDictionary *parameters = @{@"externalUserId" : userId};
[FIRAnalytics logEventWithName:@"changeUser" parameters:parameters];
```

{% endtab %}
{% endtabs %}

## Fournisseur de balises personnalisées du Braze SDK {#adding-ios-google-tag-provider}

Avec les balises et les déclencheurs configurés, vous devrez également implémenter le Google Tag Manager dans votre application iOS, que vous pourrez trouver dans la [documentation][2] Google.

Une fois que le Google Tag Manager est installé dans votre application, ajoutez un fournisseur de balises personnalisées pour appeler les méthodes du SDK Braze en fonction des balises que vous avez configurées au sein de Google Tag Manager. 

Assurez-vous de noter le « chemin de classe » vers le fichier. C’est ce que vous allez saisir lors de la définition d’une balise dans la console du [Google Tag Manager][5].

Cet exemple montre l’une des nombreuses façons de structurer votre fournisseur de balises personnalisées dans laquelle nous déterminons quelle méthode du SDK Braze doit être appelée en fonction de la paire clé-valeur `actionType` envoyée à partir de la balise GTM.

Les `actionType` que nous avons pris en charge dans notre exemple sont `logEvent`, `customAttribute` et `changeUser`, mais vous pouvez modifier la manière dont votre fournisseur de balises gère les données du Google Tag Manager.

Ajoutez le code suivant à votre fichier `BrazeGTMTagManager.h` :

{% tabs %}
{% tab OBJECTIVE-C %}

```obj-c
@import Firebase;
@import GoogleTagManager;

@interface BrazeGTMTagManager : NSObject <TAGCustomFunction>

@end
```

{% endtab %}
{% endtabs %}

Et ajoutez le code suivant à votre fichier `BrazeGTMTagManager.m` :

{% tabs %}
{% tab OBJECTIVE-C %}

```obj-c
#import <Foundation/Foundation.h>
#import "BrazeGTMTagManager.h"
#import "Appboy-iOS-SDK/AppboyKit.h"

static NSString *const ActionTypeKey = @"actionType";

// Custom Events
static NSString *const LogEventActionType = @"logEvent";
static NSString *const LogEventEventName = @"eventName";

// Custom Attributes
static NSString *const CustomAttributeActionType = @"customAttribute";
static NSString *const CustomAttributeKey = @"customAttributeKey";
static NSString *const CustomAttributeValueKey = @"customAttributeValue";

// Change User
static NSString *const ChangeUserActionType = @"changeUser";
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
  
  if ([actionType isEqualToString:LogEventActionType]) {
    [self logEvent:mutableParameters];
  } else if ([actionType isEqualToString:CustomAttributeActionType]) {
    [self logCustomAttribute:mutableParameters];
  } else if ([actionType isEqualToString:ChangeUserActionType]) {
    [self changeUser:mutableParameters];
  } else {
    NSLog(@"Invalid action type. Doing nothing.");
  }
  return nil;
}

- (void)logEvent:(NSMutableDictionary *)parameters {
  NSString *eventName = parameters[LogEventEventName];
  [parameters removeObjectForKey:LogEventEventName];
  [[Appboy sharedInstance] logCustomEvent:eventName withProperties:parameters];
}

- (void)logCustomAttribute:(NSMutableDictionary *)parameters {
  NSString *customAttributeKey = parameters[CustomAttributeKey];
  id customAttributeValue = parameters[CustomAttributeValueKey];
  
  if ([customAttributeValue isKindOfClass:[NSString class]]) {
    [[Appboy sharedInstance].user setCustomAttributeWithKey:customAttributeKey
                                             andStringValue:customAttributeValue];
  } else if ([customAttributeValue isKindOfClass:[NSDate class]]) {
    [[Appboy sharedInstance].user setCustomAttributeWithKey:customAttributeKey
                                               andDateValue:customAttributeValue];
  } else if ([customAttributeValue isKindOfClass:[NSNumber class]]) {
    if (strcmp([customAttributeValue objCType], [@(YES) objCType]) == 0) {
      [[Appboy sharedInstance].user setCustomAttributeWithKey:customAttributeKey
                                                 andBOOLValue:[(NSNumber *)customAttributeValue boolValue]];
    } else if (strcmp([customAttributeValue objCType], @encode(short)) == 0 ||
               strcmp([customAttributeValue objCType], @encode(int)) == 0 ||
               strcmp([customAttributeValue objCType], @encode(long)) == 0) {
      [[Appboy sharedInstance].user setCustomAttributeWithKey:customAttributeKey
                                              andIntegerValue:[(NSNumber *)customAttributeValue integerValue]];
    } else if (strcmp([customAttributeValue objCType], @encode(float)) == 0 ||
               strcmp([customAttributeValue objCType], @encode(double)) == 0) {
      [[Appboy sharedInstance].user setCustomAttributeWithKey:customAttributeKey
                                               andDoubleValue:[(NSNumber *)customAttributeValue doubleValue]];
    } else {
      NSLog(@"Could not map NSNumber value to Appboy custom attribute:%@", customAttributeValue);
    }
  } else if ([customAttributeValue isKindOfClass:[NSArray class]]) {
    [[Appboy sharedInstance].user setCustomAttributeArrayWithKey:customAttributeKey
                                                           array:customAttributeValue];
  }
}

- (void)changeUser:(NSMutableDictionary *)parameters {
  NSString *userId = parameters[ChangeUserExternalUserId];
  [[Appboy sharedInstance] changeUser:userId];
}

@end
```

{% endtab %}
{% endtabs %}

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/
[2]: https://developers.google.com/tag-manager/ios/v5/
[3]: {% image_buster /assets/img/android_google_tag_manager/gtm_android_trigger.png %}
[4]: {% image_buster /assets/img/android_google_tag_manager/gtm_android_function_call_tag.png %}
[5]: https://tagmanager.google.com/
[6]: {% image_buster /assets/img/android_google_tag_manager/gtm_android_eventname_variable.png %}
