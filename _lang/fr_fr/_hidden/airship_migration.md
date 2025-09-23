---
nav_title: Migration du SDK depuis Airship vers Braze
permalink: /sdk_migration_guide_airship/
hidden: true
page_type: reference
---

# Migration des SDK depuis Airship vers Braze (iOS)

> Chez Braze, nous sommes conscients que le passage à une plateforme et un SDK entièrement nouveaux peut être intimidant, mais avec le guide de migration suivant, des exemples de code faciles à comprendre et des fonctionnalités impressionnantes, nous pensons que cela ne vous dérangera pas. Dans cet article, nous avons inclus l’équivalent Braze de nombreuses fonctionnalités clés d’Airship, ainsi que des extraits de code SDK « chercher-remplacer » pour rendre votre migration à la fois simple et rapide.

## Au-delà du code
### Gestion des jetons
Braze utilise le jeton d’appareil Apple, pour iOS.

| **Perspective de Braze :**<br>Nous veillons à ce que les clients puissent communiquer en continu avec leurs utilisateurs (par exemple, avec des notifications push) lorsqu’ils migrent d’Airship vers Braze (qu’il s’agisse d’une migration avec basculement complet vers Braze, ou d’une transition partielle de type 50/50, etc.). |
{: .reset-td-br-1 role="presentation" }

#### Migration des jetons de notification push

Il est nécessaire de [migrer les jetons de notification push via l'API]({{site.baseurl}}/help/help_articles/push/push_token_migration/#migration-via-api). La documentation liée contient des étapes spécifiques, ainsi qu’un exemple de charge utile, mais le processus global est le suivant :

1. Importez les jetons via l'[endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/). Pour les importations de lots, nous disposons de ressources pour accélérer le processus. Contactez votre COM ou SA pour plus de détails !
2. Si le jeton existe déjà dans Braze, il sera ignoré. Sinon, un profil anonyme sera généré.
3. Effectuez l'assurance qualité de l'intégration "push". Assurez-vous que les étapes de la [configuration de push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) ont été effectuées.

Si vos profils d’utilisateur et vos jetons de notification push sont stockés à des endroits distincts, nous vous recommandons d’importer des jetons de notification push de manière anonyme, puis de migration ultérieurement vos profils d’utilisateur existants. Il n’est pas nécessaire de les mapper ensemble car le SDK iOS de Braze va gérer la résolution du jeton lors de l’intégration réussie.

- Nous recommandons de migrer des utilisateurs via API, mais s’il est nécessaire d’importer une liste statique d’utilisateurs, cela peut être fait avec un CSV. Notez que **les jetons de notification push ne peuvent pas être importés via CSV** car l'objet « push_token » ne peut pas être spécifié dans le CSV. Pour visualiser un modèle d'importation et en savoir plus sur l'importation de données dans le tableau de bord, consultez notre [documentation sur les fichiers CSV.]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv)

{% alert note %}
Les jetons push peuvent apparaître sous la forme `subscribed` dans le tableau de bord de Braze, mais deviendront `opted-in` une fois que les utilisateurs auront démarré une session avec le SDK de Braze.
{% endalert %}

#### Plusieurs jetons de notification push

Avec Braze, un utilisateur peut avoir plusieurs jetons de notification push (un pour chaque appareil) et en ciblant tous les jetons de notification push valides, vous pouvez envoyer des notifications à plusieurs appareils d’utilisateur. Il est également possible de configurer des campagnes pour qu’elles ne soient envoyées qu’à l’appareil le plus récent d’un utilisateur.

## Configuration de la campagne
Avec une certaine maîtrise, Braze est un véritable outil unique dans l’espace d’engagement des clients. Grâce à nos options de personnalisation étendues et à notre ensemble de fonctionnalités croissantes, les campagnes migrées dans Braze bénéficient souvent de la replanification pour tirer profit des avantages de ces outils, et notre framework de planification de campagne (contactez votre COM ou SA pour plus de détails) est spécialement conçu pour cela.

### Composition
#### Notifications push
Braze nécessite des canaux distincts pour les notifications push (un pour iOS, un pour Android).

| **Perspective de Braze :**<br>Nous offrons à nos clients la possibilité d’obtenir le meilleur des deux mondes au lieu d’avoir à faire des concessions. Être capable de tirer parti de l’ensemble des capacités d’un seul canal offre plus de flexibilité pour le spécialiste du marketing et une expérience utilisateur améliorée. Cela nous permet d'adopter les dernières fonctionnalités de chaque système d'exploitation ; par exemple, Android a pris en charge les notifications riches avant iOS. |
{: .reset-td-br-1 role="presentation" }

Braze peut envoyer des notifications push aux utilisateurs qui ne mettent pas à jour leur application avec le SDK de Braze installé. Étant donné que Braze dispose d’un jeton de notification push valide, Braze peut envoyer la notification push sans le SDK Braze car les APN s’occupent du reste. Il est crucial de noter que **l’analyse de cette notification push ne sera pas disponible pour les builds sans le SDK Braze**.

##### Partage des jetons

Pour les campagnes spécifiques au cycle de vie qui doivent continuer pendant votre processus de migration vers le SDK Braze, les utilisateurs peuvent être éligibles à la réception de notifications de Braze et Airship, étant donné que Braze a reçu un jeton de notification push valide.

#### Centre de messages
Pour remplacer la fonctionnalité de campagne de centre de messages Airship, nous vous recommandons de créer une campagne multicanal qui consiste en une notification push et une [carte de contenu]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/). Pour en savoir plus sur la façon d’utiliser les cartes de contenu au format de centre de messages, consultez notre [Guide d’implémentation de carte de contenu iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/content_cards/implementation_guide/#content-cards-in-a-message-center).

### Segmentation
Braze propose de multiples filtres de [segmentation]({{site.baseurl}}/user_guide/engagement_tools/segments/) afin d'offrir une expérience utilisateur riche à vos clients.

| **Perspective de Braze** :<br> Dans Braze, les segments sont entièrement dynamiques, de sorte que les utilisateurs entrent et sortent du segment au fur et à mesure que les conditions définies changent. |
{: .reset-td-br-1 role="presentation" }

#### Migration de segment utilisateur

Pour recréer directement un segment statique Airship dans Braze, il existe deux options :
- **Importation via API - Attribuer un attribut personnalisé** (recommandé)<br>
Nous vous recommandons d'importer des utilisateurs via l'[endpoint`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) et, ce faisant, d'attribuer un attribut personnalisé à ces utilisateurs importés. Par exemple, vous pouvez créer un segment d’utilisateurs qui possèdent chacun un attribut personnalisé `Segment_Group_1` défini sur `true`. Pour segmenter ultérieurement ces utilisateurs, vous devez [créer un segment de]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) tous les utilisateurs pour lesquels `Segment_Group_1` est `true`.<br><br>
- **Filtre basé sur l'importation d'utilisateurs CSV**<br>
Il existe une option de Braze pour filtrer uniquement les utilisateurs inclus dans une importation CSV spécifique. Cette option de filtrage est visible lors de l'étape des utilisateurs cibles (outils d'engagement) dans « Filtrer les utilisateurs par `Updated/Imported via CSV` ».
![Filtre d'importation CSV]({% image_buster /assets/img/csv_filter.png %}){: style="max-width:90%;border:0;"}
Notez que pour les importations CSV, un ID externe est requis pour chaque utilisateur importé et **les segments avec des utilisateurs anonymes ou des alias uniquement ne pourront pas être importés**. Pour visualiser un modèle d'importation et en savoir plus sur l'importation de données dans le tableau de bord, consultez notre [documentation sur les fichiers CSV.]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv)

## Rechercher/remplacer les extraits de code SDK
Afin de simplifier la migration, nous avons mis en évidence les extraits de code SDK d’Airship suivants présents dans votre code, avec les extraits de code SDK de Braze correspondants pour les remplacer. Consultez les sujets suivants pour commencer :
- [Installation](#installation)
- [Obtention et paramétrage de l'ID de l'utilisateur](#userid)
- [Gestion des notifications push](#pushnotifications)
- [Analyse](#analytics)
- [Gestion des messages in-app](#iammessages)
- [Centre de messages et cartes de contenu](#messagecenter)

### Installation {#installation}
{% tabs %}
{% tab Swift %}
**Airship**
```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) {

    UAirship.takeOff(UAConfig.default())

    UALocation.shared()?.isLocationUpdatesEnabled = true
    UALocation.shared().isBackgroundLocationUpdatesAllowed = true

    UAirship.push()?.notificationOptions = [.alert, .badge, .sound]
    UAirship.push()?.userPushNotificationsEnabled = true
    UAirship.push()?.pushNotificationDelegate = self

    UAInAppAutomation.shared()?.inAppMessageManager.delegate = self
    UAInAppAutomation.shared()?.inAppMessageManager.displayInterval = 30
}
```
**Braze**
```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) {

    Appboy.start(withApiKey: apiKey, in: application, withLaunchOptions: launchOptions, withAppboyOptions: appboyOptions)

    locationManager.requestAlwaysAuthorization() // locationManager is a CLLocationManager property variable

    // Push Notifications
    let options: UNAuthorizationOptions = [.alert, .sound, .badge]
    UNUserNotificationCenter.current().requestAuthorization(options: options) { (granted, error) in
      Appboy.sharedInstance()?.pushAuthorization(fromUserNotificationCenter: granted)
    }
    UIApplication.shared.registerForRemoteNotifications()

    // In-App Messages
    Appboy.sharedInstance()?.inAppMessageController.inAppMessageUIController?.setInAppMessageUIDelegate?(self)
}
```
{% endtab %}
{% tab Objectif-C %}
**Airship**
```objc
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {

  [UAirship takeOff:[UAConfig defaultConfig]];

  [[UALocation shared] setLocationUpdatesEnabled:YES];
  [[UALocation shared] setBackgroundLocationUpdatesAllowed:YES];

  [UAirship push].notificationOptions = UNAuthorizationOptionAlert | UNAuthorizationOptionSound | UNAuthorizationOptionBadge;
  [[UAirship push] setUserPushNotificationsEnabled:YES];
  [[UAirship push] setPushNotificationDelegate:self];

  [UAInAppAutomation shared].inAppMessageManager.delegate = self;
  [UAInAppAutomation shared].inAppMessageManager.displayInterval = 30;

  return YES;
}
```
**Braze**
```objc
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {

  [Appboy startWithApiKey:self.apiKey inApplication:application withLaunchOptions:launchOptions withAppboyOptions:self.appboyOptions];

  [self.locationManager requestAlwaysAuthorization]; // locationManager is a CLLocationManager property variable

  // Push Notifications
  UNAuthorizationOptions options = UNAuthorizationOptionAlert | UNAuthorizationOptionSound | UNAuthorizationOptionBadge;
  [[UNUserNotificationCenter currentNotificationCenter] requestAuthorizationWithOptions:options
                          completionHandler:^(BOOL granted, NSError * _Nullable error) {
    [[Appboy sharedInstance] pushAuthorizationFromUserNotificationCenter:granted];
  }];
  [[UIApplication sharedApplication] registerForRemoteNotifications];

  // In-App Messages
  [[Appboy sharedInstance].inAppMessageController.inAppMessageUIController setInAppMessageUIDelegate:self];

  return YES;
}
```

{% endtab %}
{% endtabs %}

### Obtenir et définir l’ID utilisateur {#userid}
{% tabs %}
{% tab Swift %}
**Airship**
```swift
extension AirshipManager {
  var userId: String? {
    return UAirship.namedUser()?.identifier
   }

  func setUser(_ userId: String) {
    UAirship.namedUser()?.identifier = userId
  }
}
```
**Braze**
```swift
extension AppboyManager {
  var userId: String? {
     return Appboy.sharedInstance()?.user.userID
  }

  func changeUser(_ userId: String) {
    Appboy.sharedInstance()?.changeUser(userId)
  }
}
```
{% endtab %}
{% tab Objectif-C %}
**Airship**
```objc

- (NSString *)userId {
  return [UAirship namedUser].identifier
}

- (void)setUser:(NSString *)userId {
  [[UAirship namedUser] setIdentifier:userId];
}
```
**Braze**
```objc
- (NSString *)userId {
  return [Appboy sharedInstance].user.userID;
}

- (void)changeUser:(NSString *)userId {
  [[Appboy sharedInstance] changeUser: userId];
}
```
{% endtab %}
{% endtabs %}

### Gérer les notifications push {#pushnotifications}
{% tabs %}
{% tab Swift %}
**Airship**
```swift
extension AirshipManager: UAPushNotificationDelegate {
  func receivedBackgroundNotification(_ notificationContent: UANotificationContent, completionHandler: @escaping (UIBackgroundFetchResult) -> Void) {
    completionHandler(.noData)
  }

  func receivedForegroundNotification(_ notificationContent: UANotificationContent, completionHandler: @escaping () -> Void) {
    completionHandler()
  }

  func receivedNotificationResponse(_ notificationResponse: UANotificationResponse, completionHandler: @escaping () -> Void) {
    completionHandler()
  }
}
```
**Braze**
```swift
extension AppboyManager {
  func application(_ application: UIApplication, didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data) {
    Appboy.sharedInstance()?.registerDeviceToken(deviceToken)
  }

  func application(_ application: UIApplication, didReceiveRemoteNotification userInfo: [AnyHashable : Any], fetchCompletionHandler completionHandler: @escaping (UIBackgroundFetchResult) -> Void) {
    Appboy.sharedInstance()?.register(application, didReceiveRemoteNotification: userInfo, fetchCompletionHandler: completionHandler)
  }

  func userNotificationCenter(_ center: UNUserNotificationCenter, didReceive response: UNNotificationResponse, withCompletionHandler completionHandler: @escaping () -> Void) {
    Appboy.sharedInstance()?.userNotificationCenter(center, didReceive: response, withCompletionHandler: completionHandler)
  }
}
```
{% endtab %}
{% tab Objectif-C %}
**Airship**
```objc
- (void)receivedBackgroundNotification:(UANotificationContent *)notificationContent completionHandler:(void (^)(UIBackgroundFetchResult))completionHandler {
  completionHandler(UIBackgroundFetchResultNoData);
}

- (void)receivedForegroundNotification:(UANotificationContent *)notificationContent completionHandler:(void (^)(void))completionHandler {
  completionHandler();
}

- (void)receivedNotificationResponse:(UANotificationResponse *)notificationResponse completionHandler:(void (^)(void))completionHandler {
  completionHandler();
}
```
**Braze**
```objc
- (void)application:(UIApplication *)application didRegisterForRemoteNotifications
  func application(_ application: UIApplication, didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data) {
    Appboy.sharedInstance()?.registerDeviceToken(deviceToken)
  }

- (void)application:(UIApplication *)application didRegisterForRemoteNotificationsWithDeviceToken:(NSData *)deviceToken {
  [[Appboy sharedInstance] registerDeviceToken:deviceToken];
}

- (void)application:(UIApplication *)application didReceiveRemoteNotification:(NSDictionary *)userInfo fetchCompletionHandler:(void (^)(UIBackgroundFetchResult))completionHandler {
  [[Appboy sharedInstance] registerApplication:application
                didReceiveRemoteNotification:userInfo
                      fetchCompletionHandler:completionHandler];
}

- (void)userNotificationCenter:(UNUserNotificationCenter *)center
didReceiveNotificationResponse:(UNNotificationResponse *)response
         withCompletionHandler:(void (^)(void))completionHandler {
  [[Appboy sharedInstance] userNotificationCenter:center didReceiveNotificationResponse:response withCompletionHandler:completionHandler];
}
```
{% endtab %}
{% endtabs %}

### Analyses {#analytics}
{% tabs %}
{% tab Swift %}
**Airship**
```swift
extension AirshipManager {
  func trackEvent(with name: String, value: NSDecimalNumber? = nil, eventProperties: [String: Any]? = nil) {
    let event = UACustomEvent(name: name, value: value)

    if let eventProperties = eventProperties {
      event.properties = eventProperties
    }

    event.track()
  }

  func applyMutationsWithValue(_ value: String, forAttribute attribute: String) {
    let mutations = UAAttributeMutations()
    mutations.setString(value, forAttribute: attribute)
    UAirship.namedUser().apply(mutations)
  }
}
```
**Braze**
```swift
extension AppboyManager {
  func logCustomEvent(_ eventName: String, withProperties properties: [AnyHashable: Any]? = nil) {
    Appboy.sharedInstance()?.logCustomEvent(eventName, withProperties: properties)
  }

  func setCustomAttributeWithKey(_ key: String, andStringValue value: String) {
    Appboy.sharedInstance()?.user.setCustomAttributeWithKey(key, andStringValue: value)
  }

  func logPurchase(productIdentifier: String, inCurrency currency: String, atPrice price: String, withQuanitity quanity: Int) {
    Appboy.sharedInstance()?.logPurchase(productIdentifier, inCurrency: currency, atPrice: NSDecimalNumber(string: price), withQuantity: UInt(quanity))
  }
}
```
{% endtab %}
{% tab Objectif-C %}
**Airship**
```objc
- (void)trackEventWith:(NSString *)name value:(NSDecimalNumber *)value eventProperties:(NSDictionary *)eventProperties {
  UACustomEvent *event = [[UACustomEvent alloc] init];
  event.eventName = name;
  event.eventValue = value;
  event.properties = eventProperties;

  [event track];
}

- (void)applyMutationWith:(NSString *)value forAttribute:(NSString *)attribute {
  UAAttributeMutations* mutations = [[UAAttributeMutations alloc] init];
  [mutations setString:value forAttribute:attribute];
  [[UAirship namedUser] applyAttributeMutations:mutations];
}
```
**Braze**
```objc
- (void)logCustomEvent:(NSString *)eventName withProperties:(NSDictionary *)properties {
  [[Appboy sharedInstance] logCustomEvent:eventName withProperties: properties];
}

- (void)setCustomAttributeWithKey:(NSString *)key andStringValue:(NSString *)value {
  [[Appboy sharedInstance].user setCustomAttributeWithKey:key andStringValue:value];
}

- (void)logPurchase:(NSString *)productIdentifier inCurrency:(NSString *)currency atPrice:(NSString *)price withQuantity:(NSInteger)quantity {
  [[Appboy sharedInstance] logPurchase:productIdentifier inCurrency:currency atPrice:[[NSDecimalNumber alloc] initWithString:price] withQuantity:quantity];
}
```
{% endtab %}
{% endtabs %}

### Gérer les messages in-app {#iammessages}
{% tabs %}
{% tab Swift %}
**Airship**
```swift

extension AirshipManager: UAInAppMessagingDelegate {
  func extend(_ message: UAInAppMessage) -> UAInAppMessage {
      return message
  }

  func messageWillBeDisplayed(_ message: UAInAppMessage, scheduleID: String) {
  }

  func messageFinishedDisplaying(_ message: UAInAppMessage, scheduleID: String, resolution: UAInAppMessageResolution) {
  }
}
```
**Braze**
```swift
extension AppboyManager: ABKInAppMessageControllerDelegate {
  func before(inAppMessageDisplayed inAppMessage: ABKInAppMessage) -> ABKInAppMessageDisplayChoice {
    // This delegate method defines whether the in-app message will be displayed now, displayed later, or discarded.
    return .displayInAppMessageNow
  }

  func beforeControlMessageImpressionLogged(_ inAppMessage: ABKInAppMessage) -> ABKInAppMessageDisplayChoice {
    // This delegate method defines the timing of when the control in-app message impression event should be logged: now, later, or discarded.
    return .displayInAppMessageNow
  }
}

extension AppboyManager: ABKInAppMessageUIDelegate {
  func on(inAppMessageDismissed inAppMessage: ABKInAppMessage) {
    // Use this method to perform any custom logic that should execute after the in-app message has been dismissed
  }

  func on(inAppMessageClicked inAppMessage: ABKInAppMessage) -> Bool {
    // This delegate method is fired when the user clicks on a slide-up in-app message or a modal/full in-app message without button(s) on it.
    return true
  }

  func on(inAppMessageButtonClicked inAppMessage: ABKInAppMessageImmersive, button: ABKInAppMessageButton) -> Bool {
    // This delegate method is fired whenever the user clicks a button on the in-app message.
    return true
  }

  func on(inAppMessageHTMLButtonClicked inAppMessage: ABKInAppMessageHTMLBase, clickedURL: URL?, buttonID buttonId: String) -> Bool {
    // This delegate method is fired whenever the user clicks a link on the HTML in-app message.
    return true
  }
}
```
{% endtab %}
{% tab Objectif-C %}
**Airship**
```objc
- (UAInAppMessage *)extendMessage:(UAInAppMessage *)message {

  return message;
}

- (void)messageWillBeDisplayed:(UAInAppMessage *)message scheduleID:(NSString *)scheduleID {

}

- (void)messageFinishedDisplaying:(UAInAppMessage *)message scheduleID:(NSString *)scheduleID resolution:(UAInAppMessageResolution *)resolution {

}
```
**Braze**
```objc
- (ABKInAppMessageDisplayChoice) beforeInAppMessageDisplayed:(ABKInAppMessage *)inAppMessage {
  return ABKDisplayInAppMessageNow;
}

- (ABKInAppMessageDisplayChoice) beforeControlMessageImpressionLogged:(ABKInAppMessage *)inAppMessage {
  return ABKDisplayInAppMessageNow;
}

- (void)onInAppMessageDismissed:(ABKInAppMessage *)inAppMessage {
  // Use this method to perform any custom logic that should execute after the in-app message has been dismissed
}

- (BOOL)onInAppMessageClicked: (ABKInAppMessage *)inAppMessage {
  // This delegate method is fired when the user clicks on a slide-up in-app message or a modal/full in-app message without button(s) on it.
  return YES;
}

- (BOOL)onInAppMessageButtonClicked:(ABKInAppMessageImmersive *)inAppMessage
                             button:(ABKInAppMessageButton *)button {
  return YES;
}

- (BOOL)onInAppMessageHTMLButtonClicked:(ABKInAppMessageHTML *)inAppMessage
                             clickedURL:(nullable NSURL *)clickedURL
                               buttonID:(NSString *)buttonID {
  return YES;
}
```
{% endtab %}
{% endtabs %}

### Cartes de contenu et centre de messages {#messagecenter}
{% tabs %}
{% tab Swift %}
**Airship**
```swift
extension AirshipManager {
  func displayMessageCenter() {
    UAMessageCenter.shared()?.defaultUI.title = "My Message Center"

    let style = UAMessageCenterStyle()
    style.navigationBarColor = .black
    style.titleColor = .white
    style.tintColor = .white

    UAMessageCenter.shared()?.defaultUI.messageCenterStyle = style
    UAMessageCenter.shared()?.display()
  }
}
```
**Braze**
```swift
extension AppboyManager {
  func displayContentCards(navigationController: UINavigationController?) {
    let contentCardsVc = ABKContentCardsTableViewController()
    contentCardsVc.title = "My Message Center"
    contentCardsVc.disableUnreadIndicator = true
    navigationController?.pushViewController(contentCardsVc, animated: true)
  }
}
```
{% endtab %}
{% tab Objectif-C %}
**Airship**
```objc
- (void)displayMessageCenter {
  [UAMessageCenter shared].defaultUI.title = @"My Message Center";
  [[UAMessageCenter shared] display];
}
```
**Braze**
```objc
- (void)displayContentCards:(UINavigationController *)navigationController {
  ABKContentCardsTableViewController *contentCards = [[ABKContentCardsTableViewController alloc] init];
  contentCards.title = @"My Message Center";
  [self.navigationController pushViewController:contentCards animated:YES];
}
```
{% endtab %}
{% endtabs %}

