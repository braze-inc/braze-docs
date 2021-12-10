---
nav_title: Gestionnaire de tags Google
article_title: Gestionnaire de tags Google pour iOS
platform: iOS
page_order: 7
description: "Cet article couvre la façon d'initialiser, de configurer et d'implémenter le gestionnaire de Google Tag dans votre application iOS."
---

# Gestionnaire de tags Google pour iOS

## Initialisation du SDK {#initializing-ios-google-tag-provider}

Le SDK iOS de Braze peut être initialisé et contrôlé par des balises configurées dans [Google Tag Manager][5].

Mais d'abord - avant d'utiliser Google Tag Manager - assurez-vous d'abord de suivre notre [Configuration initiale du SDK][1].

## Configuration de votre Google Tag Manager {#configuring-ios-google-tag-manager}

Dans notre exemple, nous allons prétendre que nous sommes une application de streaming de musique qui veut enregistrer différents événements lorsque les utilisateurs écoutent des chansons. En utilisant Google Tag Manager pour iOS, nous pouvons contrôler lequel de nos fournisseurs tiers reçoivent cet événement, et créer des tags spécifiques au Brésil.

### Événements personnalisés

Les événements personnalisés sont enregistrés avec `actionType` réglé sur `logEvent`. Le fournisseur de balises personnalisées Braze dans notre exemple attend que le nom de l'événement personnalisé soit défini en utilisant `eventName`.

Pour commencer, créez un trigger qui recherche un "Nom de l'événement" qui équivaut à `la musique jouée`

!\[Déclenchement du nom de l'événement pour les événements\]\[3\]

Ensuite, créez un nouveau tag ("Appel de fonction") et entrez le chemin de classe de votre [fournisseur de tags personnalisés](#adding-ios-google-tag-provider) décrit plus loin dans cet article.

Ce tag sera déclenché lorsque vous enregistrez l'événement `de la chanson jouée` que nous venons de créer.

Dans notre exemple de paramètres personnalisés (paires clé-valeur), nous avons mis `eventName` à `joué la musique` - qui sera le nom de l'événement personnalisé enregistré sur Braze.

{% alert important %}
Lors de l'envoi d'un événement personnalisé, assurez-vous de définir `actionType` à `logEvent`, et définissez une valeur pour `eventName` comme indiqué dans la capture d'écran ci-dessous.

Le fournisseur de tags personnalisés dans notre exemple utilisera ces clés pour déterminer les actions à entreprendre, et quel nom d'événement envoyer à Braze quand il reçoit des données de Google Tag Manager.
{% endalert %}

!\[Tag d'appel de la fonction\]\[4\]

Vous pouvez également inclure des arguments de paire de clés supplémentaires à la balise, qui seront envoyés en tant que propriétés d'événement personnalisées à Braze. `eventName` et `actionType` ne seront pas ignorés pour les propriétés d'événement personnalisées. Dans notre exemple de balise ci-dessous, nous passerons en `genre` qui a été défini en utilisant une balise Variable dans Google Tag Manager - provenant de l'événement personnalisé que nous avons connecté dans notre application.

La propriété événement `genre` est envoyée à Google Tag Manager une variable "Firebase - Event Parameter" depuis que Google Tag Manager pour iOS utilise Firebase comme couche de données.

!\[Tag Variable Event Name\]\[6\]

Enfin, lorsqu'un utilisateur joue une chanson dans notre application, nous allons enregistrer un événement via Firebase/Google Tag Manager en utilisant le nom de l'événement Firebase Analytics qui correspond au nom de trigger de notre tag, `a joué la chanson`.

{% tabs %}
{% tab OBJECTIVE-C %}

```obj-c
NSDictionary *parameters = @{@"genre" : @"pop",
                             @"nombre de fois écoutés" : @42};
[FIRAnalytics logEventWithName:@"play song" parameters:parameters];
```

{% endtab %}
{% endtabs %}

### Logging des attributs personnalisés

Les attributs personnalisés sont définis via un `actionType` défini à `customAttribute`. Le fournisseur de balises personnalisées Braze attend que la clé/valeur d'attribut personnalisé soit définie via `customAttributeKey` et `customAttributeValue`.

{% tabs %}
{% tab OBJECTIVE-C %}

```obj-c
NSDictionary *parameters = @{@"customAttributeKey" : @"chanson préférée",
                             @"customAttributeValue" : @"Private Eyes"};
[FIRAnalytics logEventWithName:@"customAttribute" paramètres:parameters];
```

{% endtab %}
{% endtabs %}

### Calling changeUser

Les appels à `changeUser()` sont faits via une `actionType` définie à `changeUser`. Le fournisseur de balises personnalisées Braze attend que l'ID de l'utilisateur Braze soit défini via une paire clé-valeur `externalUserId` dans votre tag.

{% tabs %}
{% tab OBJECTIVE-C %}

```obj-c
NSDictionary *parameters = @{@"externalUserId" : userId};
[FIRAnalytics logEventWithName:@"changeUser" paramètres:parameters];
```

{% endtab %}
{% endtabs %}

## Fournisseur de tags personnalisés Braze SDK {#adding-ios-google-tag-provider}

Avec les tags et les déclencheurs configurés, vous devrez également implémenter Google Tag Manager dans votre application iOS que vous trouverez dans la [documentation][2] de Google.

Une fois que Google Tag Manager est installé dans votre application, ajouter un fournisseur de tags personnalisés pour appeler les méthodes Braze SDK en fonction des tags que vous avez configurés dans Google Tag Manager.

N'oubliez pas de noter le "chemin de classe" vers le fichier qui - c'est ce que vous allez entrer lors de la configuration d'un Tag dans la console [Google Tag Manager][5].

Cet exemple montre une des nombreuses façons de structurer votre fournisseur de tags personnalisés, où nous déterminons la méthode Braze SDK à appeler en fonction de la paire `actionType` envoyée depuis la balise GTM.

Les `actionType` que nous avons pris en charge dans notre exemple sont `logEvent`, `customAttribute`, et `changeUser`, mais vous pouvez choisir de modifier la façon dont votre fournisseur de tags gère les données de Google Tag Manager.

Ajoutez le code suivant à votre fichier `BrazeGTMTagManager.h`:

{% tabs %}
{% tab OBJECTIVE-C %}

```obj-c
@import Firebase;
@import GoogleTagManager;

@interface BrazeGTagManager : NSObject <TAGCustomFunction>

@end
```

{% endtab %}
{% endtabs %}

Et ajoutez le code suivant à votre fichier `BrazeGTMTagManager.m`:

{% tabs %}
{% tab OBJECTIVE-C %}

```obj-c
#import <Foundation/Foundation.h>
#import "BrazeGTagManager.h"
#import "Appboy-iOS-SDK/AppboyKit. "

NSString statique *const ActionTypeKey = @"actionType";

// Événements personnalisés
static NSString *const LogEventActionType = @"logEvent";
static NSString *const LogEventName = @"eventName";

// Attributs personnalisés
NSString statique *const CustomAttributeActionType = @"customAttribute";
static NSString *const CustomAttributeKey = @"customAttributeKey";
static NSString *const CustomAttributeValueKey = @"customAttributeValue";

// Change User
static NSString *const ChangeUserActionType = @"changeUser";
static NSString *const ChangeUserExternalUserId = @"externalUserId";

@implementation BrazeGTagManager

- (NSObject *)executeWithParameters:(NSDictionary *)parameters {
  NSMutableDictionary *mutableParameters = [parameters mutableCopy];

  NSString *actionType = mutableParameters[ActionTypeKey];
  if (! ctionType) {
    NSLog(@"Il n'y a pas de clé de type d'action Braze dans cet appel. Ne rien faire. , nil);
    return nil;
  }

  [mutableParameters removeObjectForKey:ActionTypeKey];

  if ([actionType isEqualToString:LogEventActionType]) {
    [self logEvent:mutableParameters];
  } sinon if ([actionType isEqualToString:CustomAttributeActionType]) {
    [self logCustomAttribute:mutableParameters];
  } sinon if ([actionType isEqualToString:ChangeUserActionType]) {
    [self changeUser:mutableParameters];
  } sinon {
    NSLog(@"Type d'action invalide. Doing nothing.");
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
[3]: {% image_buster /assets/img/android_google_tag_manager/gtm_android_trigger.png %} [4]: {% image_buster /assets/img/android_google_tag_manager/gtm_android_function_call_tag.png %} [6]: {% image_buster /assets/img/android_google_tag_manager/gtm_android_eventname_variable.png %}

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/
[2]: https://developers.google.com/tag-manager/ios/v5/
[5]: https://tagmanager.google.com/
