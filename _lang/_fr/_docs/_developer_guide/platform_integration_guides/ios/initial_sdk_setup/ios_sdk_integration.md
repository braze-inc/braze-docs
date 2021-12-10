---
nav_title: Guide d'intégration SDK (facultatif)
article_title: Guide d'intégration de Braze SDK pour iOS (facultatif)
alias: "/ios_sdk/"
description: "Ce guide d'intégration iOS vous emmène étape par étape dans la mise en place des meilleures pratiques lors de l'intégration du SDK iOS et de ses composants principaux dans votre application. Ce guide vous aidera à construire un fichier d'aide BrazeManager.swift."
page_order: 10
platform: iOS
---

# Guide d'intégration de Braze iOS SDK

> Ce guide facultatif d'intégration iOS vous emmène étape par étape dans la mise en place des meilleures pratiques lors de l'intégration du SDK iOS et de ses composants principaux dans votre application. Ce guide vous aidera à construire un `Gestionnaire de Brase. wift` fichier d'aide qui découplera toutes les dépendances du Braze iOS SDK du reste de votre code de production. ce qui a entraîné une `importation AppboyUI` dans toute votre application. Cette approche limite les problèmes liés aux importations excessives de SDK, facilitant le suivi, le débogage et le changement de code.

{% alert important %}
Ce guide suppose que vous avez déjà [ajouté le SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/overview/) dans votre projet Xcode.
{% endalert %}

## Aperçu de l'intégration

Les étapes suivantes vous aident à construire un fichier d'aide `BrazeManager` dans lequel votre code de production appelle. Ce fichier d'aide traitera de toutes les dépendances liées au Brésil en ajoutant diverses extensions pour les sujets d'intégration suivants listés ci-dessous. Chaque sujet inclura les étapes horizontales des onglets et des extraits de code à la fois dans Swift et Objective-C. Veuillez noter que les étapes de la carte de contenu et des messages intégrés à l'application ne sont pas nécessaires à l'intégration si vous ne prévoyez pas d'utiliser ces canaux dans votre application.

- [Créer BrazeManager.swift](#create-brazemanagerswift)
- [Initialiser le SDK](#initialize-the-sdk)
- [Notifications push](#push-notifications)
- [Accéder aux variables utilisateur et aux méthodes](#access-user-variables-and-methods)
- [Analyses du journal](#log-analytics)
- [Messages dans l'application (facultatif)](#in-app-messages)
- [Cartes de contenu (facultatif)](#content-cards)
- [Étapes suivantes](#next-steps)

### Créer BrazeManager.swift

{% tabs local %}
{% tab Create BrazeManager.swift %}

##### Créer BrazeManager.swift
Pour construire votre `BrazeManager. wift` fichier, créez un nouveau fichier Swift nommé _BrazeManager_ à ajouter à votre projet à l'emplacement souhaité. Ensuite, remplacez `import Foundation` par `import AppboyUI` for SPM (`import Appboy_iOS_SDK` pour cocoapods) puis créez une classe `BrazeManager` qui sera utilisée pour héberger toutes les méthodes et variables du Brésil. `Appboy_iOS_SDK`

{% alert note %}
- `BrazeManager` est une classe `NSObject` et non un struct, donc il peut se conformer aux délégués d'ABK tels que le `ABKInAppMessageUIDelegate`.
- Le `BrazeManager` est une classe singletonne par conception pour s'assurer qu'une seule instance de cette classe sera utilisée. Ceci est fait pour fournir un point d'accès unifié à l'objet.
{% endalert %}

1. Ajoute une variable statique nommée _partagé_ qui initialise la classe `BrazeManager`. Cela ne sera garanti qu'une seule fois par la paresse.
2. Ensuite, ajoutez une variable privée constante nommée _apiKey_ et définissez-la comme valeur de la clé API de votre groupe d'applications dans le tableau de bord Braze.
3. Ajoute une variable privée calculée nommée _appboyOptions_, qui stockera les valeurs de configuration pour le SDK. Il sera vide pour l'instant.

{% subtabs global %}
{% subtab Swift %}

```swift
class BrazeManager: NSObject {
  // 1
  static let shared = BrazeManager()

  // 2
  private let apikey = "YOUR-API-KEY"

  // 3
  private var appboyOptions: [String:Any] {
    return [:]
  }
 } }
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
@implementation BrazeManager

// 1
+ (instancetype)partagé {
    static BrazeManager *shared = nil;
    dispatch_once_t statique onceToken;
    dispatch_once(&onceToken, ^{
        partagé = [[BrazeManager alloc] init];
        // Faire n'importe quel autre travail d'initialisation ici
    });
    retour partagé;
}

// 2
- (NSString *)apiKey {
  return @"YOUR-API-KEY";
}

// 3
- (NSDictionary *)appboyOptions {
  return [NSDictionary dictionary];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Initialiser le SDK

{% tabs local %}
{% tab Step 1: Initialize SDK from BrazeManager.swift %}

##### Initialiser le SDK depuis BrazeManager.swift
Ensuite, vous devez initialiser le SDK. Comme mentionné ci-dessus, ce guide suppose que vous avez déjà [ajouté le SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/overview/) dans votre projet Xcode. Vous devez également avoir votre point de terminaison [du groupe d'applications SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/completing_integration/#step-2-specify-your-data-cluster) et [`du niveau de log`]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/other_sdk_customizations/#braze-log-level) défini dans votre `Info. liste` fichier ou dans `appboyOptions`.

Ajoutez la méthode `didFinishLaunchingWithOptions` du fichier `AppDelegate.swift` sans type de retour dans votre fichier `BrazeManager.swift`. En créant une méthode similaire dans le `BrazeManager. wift` fichier, il n'y aura pas d'instruction `import AppboyUI` dans votre fichier `AppDelegate.swift`.

Ensuite, initialisez le SDK en utilisant vos variables nouvellement déclarées `apiKey` et `appboyOptions`.

{% alert important %}
L'initialisation doit être faite dans le fil de discussion principal.
{% endalert %}

{% subtabs global %}
{% subtab Swift %}
```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) {
  Appboy.start(withApiKey: apikey, in: application, withLaunchOptions: launchOptions, withAppboyOptions: appboyOptions)
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  [Appboy startWithApiKey:[self apiKey] inApplication:application withLaunchOptions:launchOptions withAppboyOptions:[self appboyOptions]];
}
```
{% endsubtab %}
{% endsubtabs %}

{% endtab %}
{% tab Step 2: Handle Appboy Initialization %}

##### Gérer l'initialisation Appboy dans l'AppDelegate.swift
Ensuite, revenez vers l'AppDelegate de `. wift` fichier et ajoutez le code snippet suivant dans la méthode de l'AppDelegate `didFinishLaunchingWithOptions` pour gérer l'initialisation Appboy à partir du `BrazeManager. wift` fichier d'aide. Rappelez-vous qu'il n'est pas nécessaire d'ajouter une instruction `import AppboyUI` dans l' `AppDelegate.swift`.

{% subtabs global %}
{% subtab Swift %}

```swift
func application(
  _ application: UIApplication, 
  didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
) -> Bool {
  // Remplacer le point de personnalisation après le lancement de l'application

  BrazeManager.shared.application(application, didFinishLaunchingWithOptions: launchOptions)

  retourner true
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  // Remplacer le point pour la personnalisation après le lancement de l'application

  [[BrazeManager shared] application:application didFinishLaunchingWithOptions:launchOptions];

  return YES;

```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert checkpoint %}
Procédez à la compilation de votre code et exécutez votre application.<br><br>À ce stade, le SDK devrait être opérationnel et en cours d'exécution. Dans votre tableau de bord, notez que les sessions sont en cours de connexion avant d'aller plus loin.
{% endalert %}

### Notifications push

{% tabs local %}
{% tab Step 1: Add Push Certificate %}

##### Ajouter un certificat push

Accédez à votre groupe d'applications existant dans le tableau de bord Braze. Sous __Paramètres de notification Push__ téléversez votre fichier de certificat push dans votre tableau de bord Braze et enregistrez-le.

![Certificat Push]({% image_buster /assets/img/ios_sdk/ios_sdk2.png %}){: style="largeur-max-60%;"}

{% endtab %}
{% tab Step 2: Register for Notifications %}

{% alert important %}
Ne manquez pas le poste de contrôle dédié à la fin de cette étape!
{% endalert %}

##### S'inscrire aux notifications push

Ensuite, inscrivez-vous pour les notifications push. Ce guide suppose que vous avez [correctement configuré vos identifiants push]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/) dans votre portail développeur Apple et votre projet Xcode.

Le code pour l'enregistrement des notifications push sera ajouté dans la méthode `didFinishLaunching...` dans le fichier `BrazeManager.swift`. Votre code d'initialisation devrait finir par ressembler à ce qui suit :

1. Configurer le contenu de la demande d'autorisation pour interagir avec l'utilisateur. Ces options sont listées à titre d'exemple.
2. Demander l'autorisation d'envoyer à vos utilisateurs des notifications push. La réponse de l'utilisateur pour autoriser ou refuser les notifications push est suivie dans la variable `accordée`.
3. Transférer les résultats d'autorisation de push à Braze après que l'utilisateur interagisse avec l'invite de notification.
4. Lancez le processus d'enregistrement avec les APN ; cela devrait être fait dans le fil de discussion principal. Si l'enregistrement réussit, l'application appelle votre méthode `AppDelegate` de l'objet `didRegisterForRemoteNotificationsWithDeviceToken`.

{% subtabs global %}
{% subtab Swift %}
```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions:[UIApplication.LaunchOptionsKey:Any]?) {
  Appboy. tart(withAPIKey: apikey, in: application, withLaunchOptions: launchOptions, withAppboyOptions: appboyOptions)
  // 1 
  let options: UNAuthorizationOptions = [. lert, .sound, .badge]
  // 2 
  UNUserNotificationCenter.current(). equestAuthorization(option: options: options) { (accordé, erreur) in
  // 3 
    Appboy.sharedInstance()?. ushAuthorization(fromUserNotificationCenter: accorted)
  }

  // 4 
  UIApplications.shared.registerForRemoteNotificiations()
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  [Appboy startWithApiKey:[self apiKey] inApplication:application withLaunchOptions:launchOptions withAppboyOptions:[self appboyOptions]];

  // 1
  UNAuthorizationOptions options = (UNAuthorizationOptionSound | UNAuthorizationOptionAlert | UNAuthorizationOptionBadge);

  // 2
  [[UNUserNotificationCenter currentNotificationNotificationNotificationCenter] requestAuthorizationWithOptions:options completionHandler:^(BOL accordé, NSError * _Nullable error) {
  // 3
    [[Appboy sharedInstance] pushAuthorizationFromUserNotificationCenter:granted];
  }];

  // 4
  [[UIApplication sharedApplication] registerForRemoteNotifications];
}
```
{% endsubtab %}
{% endsubtabs %}

{% alert checkpoint %}
Procédez à la compilation de votre code et exécutez votre application.
- Dans votre application, confirmez que vous êtes invité à recevoir des notifications push avant d'aller plus loin.
- Si vous n'êtes pas invité, essayez de supprimer et de réinstaller l'application pour vous assurer que l'invite de notification push n'était pas affichée précédemment.

Observez que vous êtes invité à recevoir des notifications push avant d'aller plus loin.
{% endalert %}

{% endtab %}
{% tab Step 3: Forward Methods %}

##### Transférer les méthodes de notification push

Ensuite, transférez les méthodes de notification du système depuis `AppDelegate.swift` vers `BrazeManager.swift` qui seront gérées par le SDK iOS de Braze.

###### Étape 1 : Créer une extension pour le code de notification push

Créez une extension pour votre code de notification push dans votre `BrazeManager. wift` fichier donc il lit d'une manière plus organisée sur quel but est servi dans le fichier d'aide, comme ceci :

1. Suivant le modèle consistant à ne pas inclure une instruction `import AppboyUI` dans votre `AppDelegate`, nous allons gérer les méthodes de notifications push dans le `BrazeManager. fichier wift`. Les jetons de l'appareil de l'utilisateur devront être passés à Braze à partir de la méthode `didRegisterForRemote...`. Cette méthode est nécessaire pour implémenter les notifications push en mode silencieux. Ensuite, ajoutez la même méthode de la `AppDelegate` dans votre classe `BrazeManager`.
2. Ajoute la ligne suivante à l'intérieur de la méthode pour enregistrer le jeton de l'appareil au Brésil. Ceci est nécessaire pour que Braze associe le jeton avec le périphérique actuel.

{% subtabs global %}
{% subtab Swift %}

```swift
// MARK - Push Notifications
extension BrazeManager {
  // 1 
  application func (
    _ application: UIApplication,
    didRegisterForRemoteNotificationsWithDeviceToken deviceToken : Data
  ) {
    // 2 
    Appboy. haredInstance().?registerDeviceToken(deviceToken)
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
// MARK - Push Notifications
// 1
- (void)application:(UIApplication *)application didRegisRegisterForRemoteNotificationsWithDeviceToken:(NSData *)deviceToken {
  // 2
  [[Appboy sharedInstance] registerDeviceToken:deviceToken:deviceToken];
}
```
{% endsubtab %}
{% endsubtabs %}

###### Étape 2 : Prise en charge des notifications à distance
Dans l’onglet __Signature & Capacités__ , ajoutez la prise en charge des __modes d'arrière-plan__ et sélectionnez __notifications distantes__ pour commencer votre prise en charge des notifications distantes provenant du Brésil.<br><br>![Signature & Capacités]({% image_buster /assets/img/ios_sdk/ios_sdk3.png %})

###### Étape 3 : Gestion distante des notifications
Le Braze SDK peut gérer les notifications à distance provenant de Braze. Transférer les notifications distantes vers Braze ; le SDK ignorera automatiquement les notifications push qui ne proviennent pas de Braze. Ajoutez la méthode suivante à votre fichier `BrazeManager.swift` dans l'extension de notification push.

{% subtabs global %}
{% subtab Swift %}
```swift
func application(
  _ application: UIApplication, 
  didReceiveRemoteNotification userInfo: [AnyHashable : Any], 
  fetchCompletionHandler completionHandler: @escaping (UIBackgroundFetchResult) -> Void
) {
  Appboy. haredInstance()?. egister(
    application, 
    didReceiveRemoteNotification: userInfo, 
    fetchCompletionHandler : completionHandler
  )
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)application:(UIApplication *)application didReceiveRemoteNotification:(NSDictionary *)userInfo fetchCompletionHandler:(void (^)(UIBackgroundFetchResult))completionHandler {
  [[Appboy sharedInstance] registerApplication:application didReceiveRemoteNotification:userInfo fetchCompletionHandler:completionHandler:completionHandler];
}
```
{% endsubtab %}
{% endsubtabs %}

###### Étape 4 : Transférer les réponses aux notifications

Le Braze SDK peut gérer la réponse des notifications push provenant du Brésil. Transférer la réponse des notifications à Braze; le SDK ignorera automatiquement les réponses des notifications push qui ne proviennent pas du Brésil. Ajoutez la méthode suivante à votre fichier `BrazeManager.swift`:

{% subtabs global %}
{% subtab Swift %}

```swift
func userNotificationCenter(
  _ centre : UNUserNotificationCenter, 
  a reçu une réponse : UNNotificationResponse, 
  withCompletionHandler completionHandler: @escaping () -> Void
) {
  Appboy. haredInstance()?. serNotificationCenter(
    centre, 
    didRecevoir : réponse, 
    avec le gestionnaire complet : completionHandler
  )
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)userNotificationCenter:(UNUserNotificationCenter *)centre
didReceiveNotificationResponse:(UNNotificationResponse *)response 
         withCompletionHandler:(void (^))))completionHandler {
  [[Appboy sharedInstance] userNotificationCenter:center 
                   didReceiveNotificationResponse:response 
                            withCompletionHandler:completionHandler];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert checkpoint %}
Procédez à la compilation de votre code et exécutez votre application. <br><br>Essayez de vous envoyer une notification push depuis le tableau de bord de Braze et de constater que les analyses sont enregistrées à partir des notifications push avant d'aller plus loin.
{% endalert %}

### Accéder aux variables utilisateur et aux méthodes

{% tabs local %}
{% tab Create User Variables and Methods %}

##### Créer des variables utilisateur et des méthodes

Ensuite, vous voudrez un accès facile aux variables et méthodes `ABKUser`. Créez une extension pour votre code d'utilisateur dans le `BrazeManager. wift` fichier donc il lit d'une manière plus organisée sur quel but est servi dans le fichier d'aide, comme ceci :

1. Un objet `ABKUser` représente un utilisateur connu ou anonyme dans votre application iOS. Ajouter une variable calculée pour récupérer le `ABKUser`; cette variable sera réutilisée pour récupérer les variables à propos de l'utilisateur.
2. Demander à la variable utilisateur d'accéder facilement à l'identifiant utilisateur `userId`. Parmi les autres variables, l'objet `ABKUser` est responsable (`firstName`, `Nomde`, `téléphone`, `maison`, etc.)
3. Définit l'utilisateur en appelant `changeUser()` avec un `userId` correspondant.

{% subtabs global %}
{% subtab Swift %}

```swift
// MARK: - User
extension BrazeManager {
  // 1
  var user: ABKUser? {
    return Appboy.sharedInstance()?.user
  }

  // 2 
  var userId: String? {
    return user?.userID
  }

  // 3
  func changeUser(_ userId: String) {
    Appboy.sharedInstance()?.changeUser(userId)
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
// MARK: - Utilisateur
  // 1
- (ABKUser *)user {
  return [[Appboy sharedInstance] user];
}

   // 2 
- (NSString *)userId {
  return [self user]. serID;
}

  // 3
- (void)changeUser:(NSString *)userId {
  [[Appboy sharedInstance] changeUser:userId];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert checkpoint %}
Procédez à la compilation de votre code et exécutez votre application.<br><br>Essayez d'identifier les utilisateurs à partir d'une connexion/inscription. Assurez-vous d'avoir une bonne compréhension de ce qui est et de ce qui n'est pas un identifiant utilisateur approprié. <br><br>Dans votre tableau de bord, notez que l'identifiant de l'utilisateur est enregistré avant d'avancer davantage.
{% endalert %}

### Analyses du journal

{% tabs local %}
{% tab Step 1: Custom Events %}

##### Créer une méthode d'événement personnalisé

Basé sur la méthode `logCustomEvent <code> Braze SDK` suivante, créez une méthode correspondante.

__Braze `logCustomEvent` Méthode de référence__<br> C'est par design car seulement le `BrazeManager. wift` file can directly access the Braze iOS SDK. Par conséquent, en créant une méthode de correspondance, le résultat est le même et est fait sans avoir besoin de dépendances directes sur le SDK de Braze iOS dans votre code de production.

```
ouvrir func logCustomEvent(_ eventName: String, withProperties properties: [AnyHashable : Any]?)
```

__Méthode de correspondance__<br> Log des événements personnalisés depuis l'objet `Appboy` vers Braze. `Propriétés` est un paramètre optionnel avec une valeur par défaut de zéro. Les événements personnalisés ne sont pas requis pour avoir des propriétés, mais doivent avoir un nom.

{% subtabs global %}
{% subtab Swift %}
```swift
func logCustomEvent(_ eventName: String, withProperties properties: [AnyHashable: Any]? = nil) {
  Appboy.sharedInstance()?.logCustomEvent(eventName, withProperties: properties)
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)logCustomEvent:(NSString *)eventName withProperties:(nullable NSDictionary *)properties {
  [[Appboy sharedInstance] logCustomEvent:eventName withProperties:properties];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Step 2: Custom Attributes %}

##### Créer une méthode d'attributs personnalisés de log

Le SDK peut enregistrer de nombreux types comme des attributs personnalisés. Il n'est pas nécessaire de créer des méthodes d'aide pour chaque type de valeur qui peut être défini. Au lieu de cela, n'exposer qu'une seule méthode qui peut filtrer jusqu'à la valeur appropriée.

```
- (BOOL)setCustomAttributeWithKey:(NSString *)key andBOOLValue:(BOOL)value; 
- (BOOL)setCustomAttributeWithKey:(NSString *)key andIntegerValue:(NSIntenger)value; 
- (BOOL)setCustomAttributeWithKey:(NSString *)key andDoubleValue:(double)value; 
- (BOOL)setCustomAttributeWithKey:(NSString *)key andStringValue:(NSString *)value; 
- (BOOL)setCustomAttributeWithKey:(NSString *)key andDateValue:(NSDate *)value;
```

Les attributs personnalisés sont enregistrés depuis l'objet `ABKUser`.

Créer __une méthode__ qui peut englober tous les types disponibles qui peuvent être définis pour un attribut. Ajoutez cette méthode dans votre fichier `BrazeManager.swift` dans l'extension Analytics. Cela peut être fait en filtrant à travers les types d'attributs personnalisés valides et en appelant la méthode associée au type correspondant.

- Le paramètre `valeur` est un type générique qui est conforme au protocole `Equatable`. Cela est fait explicitement, donc si le type n'est pas ce que le Braze iOS SDK attend, il y aura une erreur de compilation.
- Les paramètres `clé` et `valeur` sont des paramètres optionnels qui seront décompressés conditionnellement dans la méthode. Ce n'est qu'une façon de s'assurer que les valeurs non-nil sont passées au SDK iOS de Braze.

{% subtabs global %}
{% subtab Swift %}

```swift
func setCustomAttributeWithKey<T: Equatable>(_ clé: String?, andValue value: T?) {
  garde let key = key, let value = value sinon { return }
  valeur de changement. elf {
  case let value as Date:
    user?. etCustomAttributeWithKey(key, andDateValue: value)
  case let value as Bool:
    user?. etCustomAttributeWithKey(key, andBOOLValue: value)
  case let value as String:
    user?. etCustomAttributeWithKey(key, andStringValue: value)
  valeur de la case let comme Double:
    user?. etCustomAttributeWithKey(key, andDoubleValue: value)
  valeur de laisse de cas comme Int:
    utilisateur?. etCustomAttributeWithKey(key, andIntegerValue: value)
  par défaut :
   return
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)setCustomAttributeWith:(NSString *)key andValue:(id)value {
  if ([value isKindOfClass:[NSDate class]]) {
    [[self user] setCustomAttributeWithKey:key andDateValue:value];
  } sinon if ([value isKindOfClass:[NSString class]]) {
    [[self user] setCustomAttributeWithKey:key andStringValue:value];
  } sinon if ([value isKindOfClass:[NSNumber class]]) {
    if (strcmp([value objCType], @encode(double)) == 0) {
      [[self user] setCustomAttributeWithKey:key andDoubleValue:[value doubleValue]];
    } sinon si (strcmp([valeur objCType], @encode(int)) == 0) {
      [[self user] setCustomAttributeWithKey:key andIntegerValue:[value integerValue]];
    } sinon if ([value boolValue]) {
      [[self user] setCustomAttributeWithKey:key andBOOLValue:[value boolValue]];
    }
  }
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Step 3: Purchases %}

##### Créer une méthode d'achat de log

Ensuite, sur la base de la méthode Braze SDK `logPurchase` , créez une méthode correspondante.

__Braze `logPurchase` Méthode de Référence__<br> C'est par design car seulement le `BrazeManager. wift` file can directly access the Braze iOS SDK. Par conséquent, en créant une méthode de correspondance, le résultat est le même et est fait sans avoir besoin de dépendances directes sur le SDK de Braze iOS dans votre code de production.

```
ouvrir la fonction logPurchase(_ productIdentifier: String, dans la devise : String, atPrice price: NSDecimalNumber, withoutQuantity quantity: UInt)
```
__Méthode de correspondance__<br> Log les achats de l'objet `Appboy` à Braze. Le SDK a plusieurs méthodes pour les achats de logging, et ce n'est qu'un exemple. Cette méthode gère également la création des objets `NSDecimal` et `UInt`. La façon dont vous voulez gérer cette partie dépend de vous, à condition que ce ne soit qu'un exemple.

{% subtabs global %}
{% subtab Swift %}

```swift
func logPurchase(_ productIdentifier: String, inCurrency currency: String, atPrice price:
String, withQuantity quantity: Int) {

  Appboy. haredInstance()?.logPurchase(productIdentifier, en Devise : devise, atPrice: NSDecimalNumber(string: price), withQuantity: UInt(quantity))

}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)logPurchase:(NSString *)productIdentifier inCurrency:(nonnull NSString *)currencyCode atPrice:(nonnull NSDecimalNumber *)price withQuantity:(NSUInteger)quantity {
  [[Appboy sharedInstance] logPurchase:productIdentifier inCurrencyCode atPrice:price withQuantity:quantity];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert checkpoint %}
Procédez à la compilation de votre code et exécutez votre application. <br><br>Essayez de journaliser les événements personnalisés.<br><br>Dans votre tableau de bord, remarquez que les événements personnalisés sont enregistrés avant d'aller plus loin.
{% endalert %}

### Messages dans l'application

{% tabs local %}
{% tab Step 1: Conform to Delegate %}

{% alert important %}
La section de message dans l'application suivante n'est pas nécessaire à l'intégration si vous ne prévoyez pas d'utiliser ce canal dans votre application.
{% endalert %}

##### Conforme à ABKInAppMessageUIDelegate

Ensuite, activez votre code de fichier `BrazeManager.swift` pour se conformer au `ABKInAppMessageUIDelegate` pour gérer directement les méthodes associées.

Le code pour se conformer au délégué sera ajouté dans les méthodes `didFinishLaunching...` dans le fichier `BrazeManager.swift`. Votre code d'initialisation devrait finir par ressembler à ceci:

{% subtabs global %}
{% subtab swift %}
```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) {
  Appboy.start(withApiKey: apiKey, in: application, withLaunchOptions: launchOptions, withAppboyOptions: appboyOptions)

  let options: UNAuthorizationOptions = [. lert, .sound, .badge]
  UNUserNotificationCenter.current().requestAuthorization(options: options) { (accordé, erreur) dans
    Appboy. haredInstance()?.pushAuthorization(fromUserNotificationCenter: accordé)
  }
  UIApplication.shared.registerForRemoteNotifications()

  Appboy.sharedInstance()?.inAppMessageController.inAppMessageUIController?.setInAppMessageUIDelegate?(self)
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  [Appboy startWithApiKey:[self apiKey] inApplication:application withLaunchOptions:launchOptions withAppboyOptions:[self appboyOptions]];

  Options UNAuthorizationOptions = (UNAuthorizationOptionSound | UNAuthorizationOptionAlert | UNAuthorizationOptionBadge);
  [[UNUserNotificationCenter currentNotificationNotificationCenter] requestAuthorizationWithOptions:options completionHandler:^(BOL accordé, NSError * _Nullable error) {
    [[Appboy sharedInstance] pushAuthorizationFromUserNotificationCenter:granted];
  }];
  [[UIApplication sharedApplication] registerForRemoteNotifications];

  [[Appboy sharedInstance]. nAppMessageController.inAppMessageUIController setInAppMessageUIDelegate:self];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Step 2: Add Delegate Methods %}

##### Ajouter des méthodes de délégué
Ensuite, créez une extension conforme au `ABKInAppMessageUIDelegate`.

Ajouter ce snippet sous la section analytique. Notez que l'objet `BrazeManager.swift` est défini en tant que délégué ; ce sera là que le `Gestionnaire de freinage. wift` file gère toutes les méthodes `ABKInAppMessageUIDelegate`.

{% alert important %}
Le `ABKInAppMessageUIDelegate` ne vient avec aucune méthode requise, or listée ci-dessous est un exemple d'une.
{% endalert %}

{% subtabs global %}
{% subtab Swift %}
```swift
// MARK: - ABKInAppMessage UI Delegate
extension AppboyManager: ABKInAppMessageUIDelegate{
  func inAppMessageViewControllerWith(_ inAppMessage: ABKInAppMessage) -> ABKInAppMessageViewController {
    switch inAppMessage {
    case is ABKInAppMessageSlideup:
      return ABKInAppMessageSlideupViewController(inAppMessage: inAppMessage)
    case is ABKInAppMessageModal:
      return ABKInAppMessageModalViewController(inAppMessage: inAppMessage)
    case is ABKInAppMessageFull:
      return ABKInAppMessageFullViewController(inAppMessage: inAppMessage)
    case is ABKInAppMessageHTML:
      return ABKInAppMessageHTMLViewController(inAppMessage: inAppMessage)
    default:
      return ABKInAppMessageViewController(inAppMessage: inAppMessage)
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
// MARK: - ABKInAppMessage UI Delegate
- (ABKInAppMessageViewController *)inAppMessageViewControllerWithInAppMessage:(ABKInAppMessage *)inAppMessage {
  if ([inAppMessage isKindOfClass:[ABKInAppMessageSlideup class]]) {
    return [[ABKInAppMessageSlideupViewController alloc] initWithInAppMessage:inAppMessage:inAppMessage];
  } sinon if ([inAppMessage isKindOfClass:[ABKInAppMessageModal class]]) {
    return [[ABKInAppMessageModalViewController alloc] initWithInAppMessage:inAppMessage];
  } sinon if ([inAppMessage isKindOfClass:[ABKInAppMessageFull class]]) {
    return [[ABKInAppMessageFullViewController alloc] initWithInAppMessage:inAppMessage];
  } sinon if ([inAppMessage isKindOfClass:[ABKInAppMessageHTML class]]) {
    return [[ABKInAppMessageHTMLViewController alloc] initWithInAppMessage:inAppMessage];
  }
  nil;
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert checkpoint %}
Procédez à la compilation de votre code et exécutez votre application. <br><br>Essayez de vous envoyer un message dans l'application. <br><br>Dans le fichier `BrazeManager.swift` , définissez un point d'arrêt à l'entrée de la méthode `ABKInAppMessageUIDelegate`. Envoyez-vous un message dans l'application et confirmez que le point d'arrêt est touché avant d'aller plus loin.
{% endalert %}

### Cartes de contenu

{% tabs local %}
{% tab Create Content Card Variables and Methods %}

{% alert important %}
La section de la carte de contenu suivante n'est pas nécessaire à l'intégration si vous ne prévoyez pas d'utiliser ce canal dans votre application.
{% endalert %}

##### Créer des variables et des méthodes de la carte de contenu

Activez votre code de production pour afficher le contrôleur de vue des cartes de contenu sans avoir besoin d'instructions inutiles `import AppboyUI`.

Créez une extension pour le code de vos Cartes de Contenu dans votre `BrazeManager. wift` fichier, donc il lit d'une manière plus organisée sur quel but est servi dans le fichier d'aide, comme ceci :

1. Afficher le `ABKContentCardsTableViewController`. Un `navigationController` optionnel est le seul paramètre nécessaire pour présenter ou pousser le contrôleur de vue de Brase.
2. Initialiser un objet `ABKContentCardsTableViewController` et éventuellement changer le titre. Vous devez également ajouter le contrôleur de vue initialisé à la pile de navigation.

{% subtabs global %}
{% subtab Swift %}
```swift
// MARK: - Content Cards
extension BrazeManager {

  // 1 
  func displayContentCards(navigationController: UINavigationController?) {

    // 2 
    let contentCardsVc = ABKContentCardsTableViewController()
    contentCardsVc.title = "Content Cards"
    navigationController?.pushViewController(contentCardsVc, animé: true)
  }
 } }
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
// MARK: - Content Cards
  // 1
- (void)displayContentCards:(UINavigationController *)navigationController {
  // 2
  ABKContentCardsTableViewController *contentCardsVc = [[ABKContentCardsTableViewController alloc] init];
  contentCardsVc. itle = @"Cartes de contenu";
  [navigationController pushViewController:contentCardsVc animé:YES];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert checkpoint %}
Procédez à la compilation de votre code et exécutez votre application.<br><br>Essayez d'afficher le `ABKContentCardsTableViewController` dans votre application avant d'aller plus loin.
{% endalert %}

## Étapes suivantes

Félicitations ! Vous avez terminé ce guide d'intégration des meilleures pratiques! Un exemple de fichier d'aide `BrazeManager` peut être trouvé [ici](https://github.com/braze-inc/braze-growth-shares-ios-demo-app/blob/master/Braze-Demo/BrazeManager.swift)

Maintenant que vous avez découplé toutes les dépendances du Braze iOS SDK du reste de votre code de production, consultez certains de nos guides de mise en œuvre optionnels avancés :
- [Guide de mise en œuvre avancée des notifications Push]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/implementation_guide/)
- [Guide avancé d'implémentation de messages intégrés]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/implementation_guide/)
- [Guide de mise en œuvre avancée de la carte de contenu]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/implementation_guide/)
[2]: {% image_buster /assets/img/ios_sdk/ios_sdk2.png %} [3]: {% image_buster /assets/img/ios_sdk/ios_sdk3.png %} 
