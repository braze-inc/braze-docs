---
nav_title: Migración del SDK de Airship a Braze
permalink: /sdk_migration_guide_airship/
hidden: true
page_type: reference
---

# Migración de SDK de Airship a Braze (iOS)

> En Braze, entendemos que cambiar a una plataforma y un SDK completamente nuevos puede ser desalentador, pero con la siguiente guía de migración, los sencillos ejemplos a nivel de código y el impresionante conjunto de características que aporta la plataforma Braze, no creemos que te importe. En este artículo hemos incluido el equivalente en Braze de muchas características clave de Airship, así como fragmentos de código del SDK de "arrancar y reemplazar" para que tu migración sea rápida, sencilla e indolora.

## Más allá del código
### Gestión de token
Braze utiliza el token de dispositivo de Apple para iOS.

| **Perspectiva Braze:**<br>Garantizamos que los clientes puedan comunicarse continuamente con sus usuarios (mediante notificaciones push, por ejemplo) durante el proceso de migración de Airship a Braze (tanto si se trata de un cambio radical al 100% de Braze como de una transición granular del 50% de Airship al 50% de Braze, etc.). |
{: .reset-td-br-1 role="presentation" }

#### Migración de token de notificaciones push

Es necesario para [migrar tokens de notificaciones push a través de la API]({{site.baseurl}}/help/help_articles/push/push_token_migration/#migration-via-api). La documentación enlazada contiene pasos específicos, así como un ejemplo de carga útil, pero el proceso general es el siguiente:

1. Importa los tokens a través del punto final [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/). Para las importaciones de grandes lotes, tenemos recursos disponibles para ayudar a agilizar el proceso. Ponte en contacto con tu COM o SA para más detalles.
2. Si el token ya existe en Braze, se ignorará; de lo contrario, se generará un perfil anónimo.
3. Realiza el control de calidad de la integración push. Asegúrate de que se han completado los pasos para [configurar push]({{site.baseurl}}/developer_guide/platforms/swift/push_notifications/).

Si tus perfiles de usuario y tus tokens push están almacenados en ubicaciones distintas, te recomendamos que importes los tokens push de forma anónima y realices una migración posterior de tus perfiles de usuario existentes. No es necesario mapearlos juntos, ya que el SDK de Braze para iOS se encargará de la resolución del token tras una integración correcta.

- Recomendamos migrar usuarios a través de la API, pero si es necesario importar una lista estática de usuarios, puede hacerse a través de CSV. Ten en cuenta que **los tokens de notificaciones push no se pueden importar mediante CSV** porque el objeto "push_token" no se puede especificar en el CSV. Para ver una plantilla de importación y obtener más información sobre la importación de datos al panel, consulta nuestra [documentación sobre CSV]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv).

{% alert note %}
Los tokens de notificaciones push pueden aparecer como `subscribed` en el panel de Braze, pero cambiarán a `opted-in` después de que los usuarios inicien una sesión con el SDK de Braze.
{% endalert %}

#### Múltiples tokens de notificaciones push

Con Braze, un usuario puede tener varios tokens de notificaciones push (uno para cada dispositivo) y, al dirigirte a todos los tokens de notificaciones push válidos, puedes enviar notificaciones a varios dispositivos de usuario. También es posible configurar campañas para que sólo se envíen al dispositivo más reciente de un usuario.

## Configuración de la campaña
A un alto nivel, Braze es una herramienta verdaderamente única en el espacio de interacción con los clientes. Debido a nuestras amplias opciones de personalización y a nuestro creciente conjunto de características, las campañas migradas a Braze a menudo se benefician de una nueva planificación para aprovechar las ventajas de estas herramientas, y nuestro marco de planificación de campañas (ponte en contacto con tu COM o SA para más detalles) está diseñado precisamente para eso.

### Composición
#### Notificaciones emergentes
Braze requiere canales separados para push (uno para iOS, otro para Android).

| **Perspectiva Braze:**<br>Habilitamos a nuestros clientes para que obtengan lo mejor de ambos mundos en lugar de tener que hacer concesiones. Poder aprovechar el canal individual en toda su capacidad ofrece más flexibilidad al especialista en marketing y una experiencia de usuario mejorada. Esto nos permite adoptar las últimas características de cada SO; por ejemplo, Android admitía notificaciones enriquecidas antes que iOS. |
{: .reset-td-br-1 role="presentation" }

Braze puede enviar notificaciones push a los usuarios que no actualicen su aplicación con el SDK de Braze instalado. Dado que Braze tiene un token de notificaciones push válido, Braze puede enviar la notificación push sin el SDK de Braze, ya que las APN se encargarán del resto. Es crucial tener en cuenta que el **análisis de mensajes push no estará disponible para las compilaciones sin el SDK de Braze**.

##### Compartir tokens

En el caso de campañas específicas del ciclo de vida que deban continuar durante tu proceso de migración al SDK de Braze, los usuarios pueden ser elegibles para recibir notificaciones tanto de Braze como de Airship, siempre que Braze haya recibido un token de notificaciones push válido.

#### Centro de mensajes
Para sustituir la funcionalidad de campaña del centro de mensajería de Airship, recomendamos crear una campaña multicanal que consista en una notificación push y una [tarjeta de contenido]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/). Para saber más sobre cómo utilizar las tarjetas de contenido en un formato de centro de mensajes, consulta nuestra [guía de implementación de tarjetas de contenido para iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/content_cards/implementation_guide/#content-cards-in-a-message-center).

### Segmentación
Braze ofrece múltiples filtros [de segmentación]({{site.baseurl}}/user_guide/engagement_tools/segments/) para proporcionar una rica experiencia de usuario a tus clientes.

| **Perspectiva Braze**:<br> Los segmentos en Braze son totalmente dinámicos, por lo que los usuarios entrarán y saldrán del segmento a medida que cambien las condiciones definidas. |
{: .reset-td-br-1 role="presentation" }

#### Migración de segmentos de usuarios

Para recrear directamente un segmento estático de Dirigible en Braze, existen dos opciones:
- **Importar mediante API - Asignar un atributo personalizado** (Recomendado)<br>
Recomendamos importar usuarios a través del [punto final`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) y, al hacerlo, asignar un atributo personalizado a esos usuarios importados. Por ejemplo, puedes crear un segmento de usuarios que tengan cada uno un atributo personalizado `Segment_Group_1` que esté configurado en `true`. Para segmentar posteriormente a estos usuarios, [crearías un segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) de todos los usuarios donde `Segment_Group_1` es `true`.<br><br>
- **Filtro basado en la importación de usuarios en CSV**<br>
Existe una opción en Braze para filtrar específicamente los usuarios incluidos en una importación CSV concreta. Esta opción de filtrar se encuentra en el paso de usuarios objetivo de nuestras herramientas de interacción, en "filtrar usuarios por `Updated/Imported via CSV`".
![Filtro de importación CSV][1]{: style="max-width:90%;border:0;"}
Ten en cuenta que, para las importaciones en CSV, se requiere un ID externo para cada usuario importado, y que **los segmentos con usuarios anónimos o sólo con alias no podrán importarse**. Para ver una plantilla de importación y obtener más información sobre la importación de datos al panel, consulta nuestra [documentación sobre CSV]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv).

## Rasgar y reemplazar fragmentos de código SDK
Para simplificar la migración, hemos resaltado los siguientes fragmentos de SDK de Airship que existen en tu código y hemos proporcionado los correspondientes fragmentos de SDK de Braze necesarios para sustituirlos. Visita los siguientes temas para empezar:
- [Instalación](#installation)
- [Obtención y configuración del ID de usuario](#userid)
- [Gestión de notificaciones push](#pushnotifications)
- [Análisis](#analytics)
- [Gestión de mensajes dentro de la aplicación](#iammessages)
- [Tarjetas de contenido y centro de mensajes](#messagecenter)

### Instalación {#installation}
{% tabs %}
{% tab Swift %}
**Dirigible**
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
{% tab Objective-C %}
**Dirigible**
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

### Obtención y configuración del ID de usuario {#userid}
{% tabs %}
{% tab Swift %}
**Dirigible**
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
{% tab Objective-C %}
**Dirigible**
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

### Gestión de notificaciones push {#pushnotifications}
{% tabs %}
{% tab Swift %}
**Dirigible**
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
{% tab Objective-C %}
**Dirigible**
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

### Análisis {#analytics}
{% tabs %}
{% tab Swift %}
**Dirigible**
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
{% tab Objective-C %}
**Dirigible**
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

### Gestión de mensajes dentro de la aplicación {#iammessages}
{% tabs %}
{% tab Swift %}
**Dirigible**
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
{% tab Objective-C %}
**Dirigible**
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

### Tarjetas de contenido y centro de mensajes {#messagecenter}
{% tabs %}
{% tab Swift %}
**Dirigible**
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
{% tab Objective-C %}
**Dirigible**
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

[1]: {% image_buster /assets/img/csv_filter.png %}
