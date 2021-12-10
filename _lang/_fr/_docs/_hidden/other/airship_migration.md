---
nav_title: Migration de SDK de Dirigeable à Braze
permalink: /fr_FR/sdk_migration_guide_airship/
hidden: vrai
page_type: Référence
---

# Migration des SDKs de l'aéronef vers Braze (iOS)

> Chez Braze, nous comprenons que passer à une toute nouvelle plate-forme et SDK peut être intimidant, mais avec le guide de migration suivant, des exemples simples de niveau de code, et des fonctionnalités impressionnantes ont été ajoutées à la table grâce à la plateforme Braze. Nous ne pensons pas que vous en pensiez. Listé ci-dessous, nous avons inclus l'équivalent de Braze à de nombreuses fonctionnalités clés Dirigeables ainsi que des extraits de code SDK "rip-and-replace" pour rendre votre migration rapide, simple, et sans douleur.

## Au-delà du Code
### Gestion des jetons
Braze utilise le jeton de périphérique d'Apple pour iOS.

| __Perspective Braze :__<br>Nous nous assurons que les clients peuvent communiquer en permanence avec leurs utilisateurs (comme les notifications push) lorsqu'ils sont en train de migrer de l'aéronef à Braze (qu'il s'agisse d'un cutover dur à 100 % Braze ou d'une transition granulaire telle que 50 % de l'aéronef brésilien, etc.). |
{: .reset-td-br-1}

#### Migration de jeton Push

Il est nécessaire de [migrer des jetons push via l'API]({{site.baseurl}}/help/help_articles/push/push_token_migration/#migration-via-api). La documentation liée contient des étapes spécifiques, ainsi qu'un exemple de charge utile, mais le processus global est le suivant :

1. Importez les jetons via le point de terminaison [/users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/). Pour les importations massives, nous avons des ressources disponibles pour accélérer le processus. Veuillez contacter votre COM ou SA pour plus de détails!
2. Si le jeton existe déjà dans Braze, il sera ignoré, sinon un profil anonyme sera généré.
3. QA l'intégration poussée. Assurez-vous que les étapes pour [configurer le push]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/) sont terminées.

Si vos profils d'utilisateur et vos jetons push se trouvent stockés dans des emplacements distincts, Nous vous recommandons d'importer des jetons push de manière anonyme et ensuite une migration ultérieure de vos profils d'utilisateurs existants. Il n'est pas nécessaire de les cartographier ensemble car le SDK Braze iOS gérera la résolution des jetons en cas de réussite de l'intégration.

- Nous vous recommandons de migrer des utilisateurs via API, mais s'il y a un besoin d'importer une liste statique d'utilisateurs, cela peut être fait via CSV. Veuillez noter que __les jetons push ne peuvent pas être importés via CSV__ car l'objet "push_token" ne peut pas être spécifié dans le CSV. Pour afficher un modèle d'importation et en savoir plus sur l'importation de données dans le tableau de bord, consultez notre [documentation CSV]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv).

{% alert note %}
Les jetons Push peuvent apparaître comme `inscrits` dans le tableau de bord de Braze, mais passera à `opted-in` une fois que les utilisateurs commenceront une session avec le Braze SDK.
{% endalert %}

#### Jetons Push Multiples

Avec Braze, un utilisateur peut avoir plusieurs jetons push (un pour chaque appareil) et en ciblant tous les jetons de push valides, vous pouvez envoyer des notifications à plusieurs appareils utilisateurs. Il est également possible de configurer des campagnes à envoyer uniquement au périphérique le plus récent d'un utilisateur.

## Configuration de la campagne
À un niveau élevé, Braze est un outil vraiment unique dans l’espace de communication avec le client. En raison de nos nombreuses options de personnalisation et de notre ensemble de fonctionnalités croissantes, Les campagnes migrées à Braze bénéficient souvent de la replanification pour tirer parti des avantages de ces outils - et notre cadre de planification de campagne (aller à votre COM ou SA pour plus de détails) est conçu pour cela.

### Composition
#### Notifications push
Braze nécessite des canaux séparés pour push (un pour iOS, un pour Android).

| __Perspective de Braze :__<br>Nous permettons à nos clients d'obtenir le meilleur des deux mondes au lieu d'avoir à faire des concessions. Être en mesure de tirer parti du canal individuel à sa pleine capacité offre plus de flexibilité pour le marketeur et une expérience utilisateur améliorée. Cela nous permet d'adopter les dernières fonctionnalités de chaque OS; par exemple, Android supporté les notifications riches avant iOS. |
{: .reset-td-br-1}

Braze est en mesure d'envoyer des notifications push aux utilisateurs qui ne mettent pas à jour leur application avec Braze SDK installé. Étant donné que Braze a un jeton push valide, Braze peut envoyer la notification push sans le Braze SDK car les APN géreront le reste. Il est crucial de noter que les analytiques de message push __ne seront pas disponibles pour les versions sans le Braze SDK__.

##### Jetons de partage

Pour le cas de campagnes spécifiques au cycle de vie qui devraient être poursuivies pendant votre processus de migration vers le Braze SDK, les utilisateurs peuvent être autorisés à recevoir des notifications de Braze et Airship, étant donné que Braze a reçu un jeton Push valide.

#### Centre de messages
Pour remplacer la fonctionnalité du centre de messages de Airship, nous recommandons de créer une campagne multicanal qui consiste en une notification push et une [Carte de Contenu]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/). Pour en savoir plus sur l'utilisation des Cartes de Contenu dans un format de centre de messages, consultez notre [guide d'implémentation de Cartes de Contenu iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/implementation_guide/#content-cards-in-a-message-center).

### Segmentation
Braze offre plusieurs filtres [segmentation]({{site.baseurl}}/user_guide/engagement_tools/segments/) pour fournir une expérience utilisateur riche à vos clients.

| __Perspective de Braze__:<br> Segments dans Braze sont entièrement dynamiques, de sorte que les utilisateurs entreront et quitteront le segment lorsque les conditions définies changeront. |
{: .reset-td-br-1}

#### Migration des groupes d'utilisateurs

Pour recréer directement un segment de Dirigeable statique au Brésil, il existe deux options :
- __Importer via API - Assigner un attribut personnalisé__ (Recommandé)<br> Nous recommandons d'importer des utilisateurs via le point de terminaison de l'API [/users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) tout en le faisant ainsi, assignation d'un attribut personnalisé à ces utilisateurs importés. Par exemple, vous pouvez créer un segment d'utilisateurs qui ont chacun un attribut personnalisé `Segment_Group_1` qui est défini à `true`. Pour segmenter plus tard ces utilisateurs, vous [créeriez un segment]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) de tous les utilisateurs où `Segment_Group_1` est `vrai`.<br><br>
- __Filtre basé sur l'importation d'utilisateurs CSV__<br> Il y a une option dans Braze pour filtrer spécifiquement les utilisateurs qui sont inclus dans une importation CSV spécifique. Cette option de filtrage peut être trouvée lors de l'étape cible de nos outils d'engagement sous "filtrer les utilisateurs par `Mis à jour/Importé via CSV`". !\[Filtre d'importation CSV\]\[1\]{: style="max-width:90%;border:0; } Veuillez noter que pour les importations CSV, un `ID externe` est requis pour chaque utilisateur importé et __segments avec un alias anonyme ou anonyme, seuls les utilisateurs ne pourront pas être importés__. Pour afficher un modèle d'importation et en savoir plus sur l'importation de données dans le tableau de bord, consultez notre [documentation CSV]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv).

## Extraire et remplacer les extraits de code SDK
Pour simplifier la migration, nous avons mis en évidence les snippets SDK Airship suivants qui existent dans votre code et nous avons fourni les snippets Braze SDK correspondants nécessaires pour les remplacer. Veuillez visiter les sujets suivants pour commencer :
- [Installation](#installation)
- [Obtention et paramétrage de l'ID de l'utilisateur](#userid)
- [Gestion des notifications Push](#pushnotifications)
- [Analyses](#analytics)
- [Gestion des messages dans l'application](#iammessages)
- [Cartes de contenu / Centre de messages](#messagecenter)

### Installation {#installation}
{% tabs %}
{% tab Swift %}
__Dirigeable__
```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) {

    UAirship.takeOff(UAConfig.default())

    UALocation.shared()?.isLocationUpdatesEnabled = true
    UALocation. hared().isBackgroundLocationUpdatesAllowed = true

    UAirship.push()?.notificationOptions = [.alert, .badge, .sound]
    UAirship. ush()?.userPushNotificationsEnabled = true
    UAirship.push()?.pushNotificationDelegate = self

    UAInAppAutomation. hared()?.inAppMessageManager.delegate = self
    UAInAppAutomation.shared()?.inAppMessageManager.displayInterval = 30
}
```
__Brasero__
```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) {

    Appboy.start(withApiKey: apiKey, in: application, withLaunchOptions: launchOptions, withAppboyOptions: appboyOptions)

    locationManager. equestAlwaysAuthorization() // locationManager est une variable de propriété CLLocationManager

    // Notifications Push
    let options: UNAuthorizationOptions = [. lert, .sound, .badge]
    UNUserNotificationCenter.current(). equestAuthorization(options: options) { (accordé, erreur) dans
      Appboy.sharedInstance()?. ushAuthorization(fromUserNotificationCenter: accordé)
    }
    UIApplication.shared. egisterForRemoteNotifications()

    // Messages In-App
    Appboy.sharedInstance()?.inAppMessageController.inAppMessageUIController?.setInAppMessageUIDelegate?(self)
}
```
{% endtab %}
{% tab Objective-C %}
__Dirigeable__
```objc
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {

  [UAirship takeOff:[UAConfig defaultConfig]];

  [[UALocation shared] setLocationUpdatesEnabled:YES];
  [[UALocation shared] setBackgroundLocationUpdatesAllowed:YES];

  [UAirship push]. otificationOptions = UNAuthorizationOptionAlert | UNAuthorizationOptionSound | UNAuthorizationOptionBadge;
  [[UAirship push] setUserPushNotificationsEnabled:YES];
  [[UAirship push] setPushNotificationDelegate:self];

  [UAInAppAutomation partagée]. nAppMessageManager.delegate = self;
  [UAInAppAutomation partagée].inAppMessageManager.displayInterval = 30;

  return YES;
}
```
__Brasero__
```objc
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {

  [Appboy startWithApiKey:self.apiKey inApplication:application withLaunchOptions:launchOptions withAppboyOptions:self.appboyOptions];

  [self. ocationManager requestAlwaysAuthorization] ; // locationManager est une variable de propriété CLLocationManager

  // Notifications Push
  UNAuthorizationOptions options = UNAuthorizationOptionAlert | UNAuthorizationOptionSound | UNAuthorizationOptionBadge;
  [[UNUserNotificationCenter currentNotificationNotificationCenter] requestAuthorizationWithOptions:options
                          completionHandler:^(BOL accordé, NSError * _Nullable error) {
    [[Appboy sharedInstance] pushAuthorizationFromUserNotificationCenter:granted];
  }];
  [[UIApplication sharedApplication] registerForRemoteNotifications];

  // Messages In-App
  [[Appboy sharedInstance]. nAppMessageController.inAppMessageUIController setInAppMessageUIDelegate:self];

  return YES;
}
```

{% endtab %}
{% endtabs %}

### Obtention et paramétrage de l'ID de l'utilisateur {#userid}
{% tabs %}
{% tab Swift %}
__Dirigeable__
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
__Brasero__
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
{% tab Objective-C %}
__Dirigeable__
```objc

- (NSString *)userId {
  return [UAirship namedUser].identifier
}

- (void)setUser:(NSString *)userId {
  [[UAirship namedUser] setIdentifier:userId];
}
```
__Brasero__
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

### Gestion des notifications Push {#pushnotifications}
{% tabs %}
{% tab Swift %}
__Dirigeable__
```swift
extension AirshipManager : UAPushNotificationDelegate {
  func receivedBackgroundNotification(_ notificationContent: UANotificationContent, completionHandler: @escaping (UIBackgroundFetchResult) -> Void) {
    completionHandler(. oData)
  }

  func receivedForegroundNotification(_ notificationContent: UANotificationContent, completionHandler: @escaping () -> Void) {
    completionHandler()
  }

  func receivedNotificationResponse(_ notificationResponse: UANotificationResponse, completionHandler: @escaping () -> Void) {
    completionHandler()
  }
}
```
__Brasero__
```swift
extension AppboyManager {
  application func(_ application: UIApplication, didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data) {
    Appboy.sharedInstance()?. egisterDeviceToken(deviceToken)
  }

  application func (_ application: UIApplication, didReceiveRemoteNotification userInfo: [AnyHashable : Any], fetchCompletionHandler completionHandler: @escaping (UIBackgroundFetchResult) -> Void) {
    Appboy. haredInstance()?. egister(application, didReceiveRemoteNotification: userInfo, fetchCompletionHandler: completionHandler)
  }

  func userNotificationCenter(_ center: UNUserNotificationCenter, didRecevoir la réponse : UNNotificationResponse, withCompletionHandler completionHandler: @escaping () -> Void) {
    Appboy. haredInstance()?.userNotificationCenter(center, didReceve: response, withCompletionHandler: completionHandler)
  }
}
```
{% endtab %}
{% tab Objective-C %}
__Dirigeable__
```objc
- (void)receivedBackgroundNotification:(UANotificationContent *)notificationContent completionHandler:(void (^)(UIBackgroundFetchResult))completionHandler {
  completionHandler(UIBackgroundFetchResultNoData);
}

- (void)receivedForegroundNotification:(UANotificationContent *)notificationContent completionHandler:(void (^))completionHandler {
  completionHandler();
}

- (void)receivedNotificationResponse:(UANotificationResponse *)notificationResponse completionHandler:(void (^)(void))completionHandler {
  completionHandler();
}
```
__Brasero__
```objc
- (void)application:(UIApplication *)application didRegisterForRemoteForRemoteNotifications
  func application(_ application: UIApplication, didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data) {
    Appboy.sharedInstance()?. egisterDeviceToken(deviceToken)
  }

- (void)application:(UIApplication *)application didRegisterForRemoteNotificationsWithDeviceToken:(NSData *)deviceToken {
  [[Appboy sharedInstance] registerDeviceToken:deviceToken:deviceToken];
}

- (void)application:(UIApplication *)application didReceiveRemoteNotification:(NSDictionary *)userInfo fetchCompletionHandler:(void (^)(UIBackgroundFetchResult))completionHandler {
  [[Appboy sharedInstance] registerApplication:application
                didReceiveRemoteNotification:userInfo
                      fetchCompletionHandler:completionHandler];
}

- (void)userNotificationCenter:(UNUserNotificationCenter *)centre
didReceiveNotificationResponse:(UNNotificationResponse *)réponse
         withCompletionHandler:(void (^)(void)completionHandler {
  [[Appboy sharedInstance] userNotificationCenter:center didReceiveNotificationResponse:response withCompletionHandler:completionHandler:completionHandler];
}
```
{% endtab %}
{% endtabs %}

### Analyses {#analytics}
{% tabs %}
{% tab Swift %}
__Dirigeable__
```swift
extension AirshipManager {
  func trackEvent(avec nom: String, value: NSDecimalNumber? = nil, eventProperties: [String: Any]? = nil) {
    let event = UACustomEvent(nom: nom, valeur: valeur)

    si let eventProperties = eventProperties {
      événement. roperties = eventProperties
    }

    événement. rack()
  }

  func applyMutationsWithValue(_ valeur: String, attribut: String) {
    let mutations = UAAttributeMutations()
    mutations. etString(value, forAttribute: attribute)
    UAirship.namedUser().apply(mutations)
  }
}
```
__Brasero__
```swift
extension AppboyManager {
  func logCustomEvent(_ eventName: String, withProperties properties: [AnyHashable: Any]? = nil) {
    Appboy.sharedInstance()?. ogCustomEvent(eventName, withProperties: properties)
  }

  func setCustomAttributeWithKey(_ key: String, andStringValue value: String) {
    Appboy.sharedInstance()?.user. etCustomAttributeWithKey(key, andStringValue: value)
  }

  func logPurchase(productIdentifier: String, inDevise : String, atPrice price: String, withQuanitity quanity: Int) {
    Appboy. haredInstance()?.logPurchase(productIdentifier, en Devise : devise, atPrice: NSDecimalNumber(string: price), withQuantity: UInt(quanity))
  }
}
```
{% endtab %}
{% tab Objective-C %}
__Dirigeable__
```objc
- (void)trackEventWith:(NSString *)name value:(NSDecimalNumber *)value eventProperties:(NSDictionary *)eventProperties {
  UACustomEvent *event = [[UACustomEvent alloc] init];
  événement. ventName = nom;
  event.eventValue = valeur;
  événement. roperties = eventProperties;

  [Event track];
}

- (void)applyMutationWith:(NSString *)value forAttribute:(NSString *)attribute {
  UAAttributeMutations* mutations = [[UAAttributeMutations alloc] init];
  [mutations setString:value forAttribute:attribute];
  [[UAirship namedUser] applyAttributeMutations:mutations];
}
```
__Brasero__
```objc
- (void)logCustomEvent:(NSString *)eventName withProperties:(NSDictionary *)properties {
  [[Appboy sharedInstance] logCustomEvent:eventName withProperties: properties];
}

- (void)setCustomAttributeWithKey:(NSString *)key andStringValue:(NSString *)value {
  [[Appboy sharedInstance]. ser setCustomAttributeWithKey:key andStringValue:value];
}

- (void)logPurchase:(NSString *)productIdentifier inCurrency:(NSString *)currency atPrice:(NSString *)price withQuantity:(NSInteger)quantity {
  [[Appboy sharedInstance] logPurchase:productIdentifier inCurrency:currency atPrice:[[NSDecimalNumber alloc] initWithString:price] withQuantity:quantity];
}
```
{% endtab %}
{% endtabs %}

### Gestion des messages dans l'application {#iammessages}
{% tabs %}
{% tab Swift %}
__Dirigeable__
```swift

extension AirshipManager : UAInAppMessagingDelegate {
  func extend(_ message: UAInAppMessage) -> UAInAppMessage {
      return message
  }

  func messageWillBeDisplayed(_ message: UAInAppMessage, scheduleID: String) {
  }

  func messageFinishedDisplaying(_ message: UAInAppMessage, scheduleID: String, resolution: UAInAppMessageResolution) {
  }
}
```
__Brasero__
```swift
extension AppboyManager : ABKInAppMessageControllerDelegate {
  func before(inAppMessageDisplayed inAppMessage: ABKInAppMessage) -> ABKInAppMessageDisplayChoice {
    // Cette méthode de délégué définit si le message dans l'application sera affiché maintenant, affiché plus tard, ou rejeté.
    retour . isplayInAppMessageNow
  }

  func beforeControlMessageImpressionLogged(_ inAppMessage: ABKInAppMessage) -> ABKInAppMessageDisplayChoice {
    // Cette méthode déléguée définit le moment où l'événement de l'impression de message de contrôle doit être enregistré dans l'application: maintenant, plus tard, ou rejeté.
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
    // Cette méthode déléguée est activée chaque fois que l'utilisateur clique sur un bouton du message dans l'application.
    return true
  }

  func on(inAppMessageHTMLButtonClicked inAppMessage: ABKInAppMessageHTMLBase, clickedURL: URL? buttonID buttonId: String) -> Bool {
    // Cette méthode déléguée est activée chaque fois que l'utilisateur clique sur un lien sur le message HTML dans l'application.
    retourner le vrai
  }
}
```
{% endtab %}
{% tab Objective-C %}
__Dirigeable__
```objc
- (UAInAppMessage *)extendMessage:(UAInAppMessage *)message {

  return message;
}

- (void)messageWillBeDisplayed:(UAInAppMessage *)message scheduleID:(NSString *)scheduleID {

}

- (void)messageFinishedDisplaying:(UAInAppMessage *)message scheduleID:(NSString *)scheduleID resolution:(UAInAppMessageResolution *)resolution {

}
```
__Brasero__
```objc
- (ABKInAppMessageDisplayChoice) beforeInAppMessageDisplayed:(ABKInAppMessage *)inAppMessage {
  return ABKDisplayInAppMessageNow;
}

- (ABKInAppMessageDisplayChoice) beforeControlMessageImpressionLogged:(ABKInAppMessage *)inAppMessage {
  return ABKDisplayInAppMessageNow;
}

- (void)onInAppMessageDismissed:(ABKInAppMessage *)inAppMessage {
  // Utilisez cette méthode pour exécuter toute logique personnalisée qui devrait s'exécuter après que le message dans l'application a été rejeté
}

- (BOOL)onInAppMessageClicked: (ABKInAppMessage *)inAppMessage {
  // Cette méthode déléguée est déclenchée lorsque l'utilisateur clique sur un message glissant dans l'application ou un message modal/complet dans l'application sans le(s) bouton(s) dessus.
  retourner OUI;
}

- (BOOL)onInAppMessageButtonClicked:(ABKInAppMessageImmersive *)inAppMessage
                             bouton:(ABKInAppMessageButton *)button {
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

### Cartes de contenu / Centre de messages {#messagecenter}
{% tabs %}
{% tab Swift %}
__Dirigeable__
```swift
extension AirshipManager {
  func displayMessageCenter() {
    UAMessageCenter.shared()?.defaultUI. itle = "Mon centre de messages"

    let style = UAMessageCenterStyle()
    style.navigationBarColor = . lack
    style.titleColor = .white
    style.tintColor = .white

    UAMessageCenter. hared()?.defaultUI.messageCenterStyle = style
    UAMessageCenter.shared()?.display()
  }
}
```
__Brasero__
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
{% tab Objective-C %}
__Dirigeable__
```objc
- (void)displayMessageCenter {
  [UAMessageCenter shared].defaultUI.title = @"My Message Center";
  [[UAMessageCenter shared] display];
}
```
__Brasero__
```objc
- (void)displayContentCards:(UINavigationController *)navigationController {
  ABKContentCardsTableViewController *contentCards = [[ABKContentCardsTableViewController alloc] init];
  contentCards.title = @"My Message Center";
  [self.navigationController pushViewController:contentCards animés:YES];

```
{% endtab %}
{% endtabs %}
[1]: {% image_buster /assets/img/csv_filter.png %}
